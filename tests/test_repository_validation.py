import copy
import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from validate_repository import REQUIRED_FILES, validate_tree, validate_workflow, parse_yaml


class RepositoryValidationTest(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        for name in REQUIRED_FILES:
            destination = self.root / name
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / name, destination)

    def test_current_repository_is_valid(self):
        validate_tree(self.root)

    def test_invalid_community_configuration_yaml_is_rejected(self):
        (self.root / '.github/ISSUE_TEMPLATE/config.yml').write_text('blank_issues_enabled: [\n')
        with self.assertRaisesRegex(ValueError, 'Invalid YAML'):
            validate_tree(self.root)

    def test_invalid_issue_template_front_matter_is_rejected(self):
        path = self.root / '.github/ISSUE_TEMPLATE/task.md'
        path.write_text('---\nname: [\n---\n# Task\n')
        with self.assertRaisesRegex(ValueError, 'Invalid YAML'):
            validate_tree(self.root)

    def test_solo_maintenance_blockers_and_check_bypasses_are_rejected(self):
        path = self.root / 'branch-protection/ruleset.json'
        original = json.loads(path.read_text())
        changes = [
            ('pull_request', 'required_approving_review_count', 1),
            ('pull_request', 'required_approving_review_count', False),
            ('pull_request', 'require_code_owner_review', True),
            ('pull_request', 'require_last_push_approval', True),
            ('pull_request', 'required_review_thread_resolution', False),
        ]
        for kind, key, value in changes:
            with self.subTest(rule=kind, parameter=key):
                policy = copy.deepcopy(original)
                next(rule for rule in policy['rules'] if rule['type'] == kind)['parameters'][key] = value
                path.write_text(json.dumps(policy))
                with self.assertRaises(ValueError):
                    validate_tree(self.root)



    def test_required_ci_defaults_are_rejected(self):
        path = self.root / 'branch-protection/ruleset.json'
        original = json.loads(path.read_text())
        for kind in ('required_status_checks', 'workflows'):
            with self.subTest(kind=kind):
                policy = copy.deepcopy(original)
                policy['rules'].append({'type': kind, 'parameters': {}})
                path.write_text(json.dumps(policy))
                with self.assertRaisesRegex(ValueError, 'Unexpected or missing policy rules'):
                    validate_tree(self.root)

    def workflow(self):
        return parse_yaml((self.root / '.github/workflows/ci.yml').read_text(), 'ci.yml')

    def test_automatic_events_and_indirect_callers_are_rejected(self):
        for event in ('pull_request', 'pull_request_target', 'push', 'issue_comment',
                      'pull_request_review', 'pull_request_review_comment', 'merge_group',
                      'workflow_run', 'workflow_call', 'repository_dispatch', 'release',
                      'create', 'page_build', 'check_suite'):
            with self.subTest(event=event):
                workflow = self.workflow()
                workflow['on'][event] = None
                with self.assertRaisesRegex(ValueError, 'Allow only'):
                    validate_workflow(workflow)
        for value in ('push', ['schedule', 'pull_request']):
            workflow = self.workflow()
            workflow['on'] = value
            with self.assertRaisesRegex(ValueError, 'Allow only'):
                validate_workflow(workflow)

    def test_schedule_drift_and_manual_removal_are_rejected(self):
        for change in ('utc', 'monday', 'twice-weekly', 'no-manual'):
            workflow = self.workflow()
            if change == 'utc':
                workflow['on']['schedule'][0]['timezone'] = 'UTC'
            elif change == 'monday':
                workflow['on']['schedule'][0]['cron'] = '17 3 * * 1'
            elif change == 'twice-weekly':
                workflow['on']['schedule'].append({'cron': '17 3 * * 2'})
            else:
                del workflow['on']['workflow_dispatch']
            with self.subTest(change=change), self.assertRaisesRegex(ValueError, 'Allow only'):
                validate_workflow(workflow)

    def test_pr_payload_gates_and_untrusted_sources_are_rejected(self):
        for condition in ("github.event.pull_request.draft == false", 'true',
                          "github.event_name == 'workflow_dispatch'", ''):
            workflow = self.workflow()
            workflow['jobs']['verify']['if'] = condition
            with self.subTest(condition=condition), self.assertRaisesRegex(ValueError, 'trusted develop'):
                validate_workflow(workflow)

    def test_retained_coverage_cannot_skip_or_hide_failure(self):
        for change in ('skip-job', 'skip-check', 'hide-failure', 'remove-check', 'swallow-failure'):
            workflow = self.workflow()
            job = workflow['jobs']['verify']
            step = next(s for s in job['steps'] if s.get('run', '').startswith('python3 -m unittest'))
            if change == 'skip-job':
                job['if'] = 'false'
            elif change == 'skip-check':
                step['if'] = 'false'
            elif change == 'hide-failure':
                step['continue-on-error'] = True
            elif change == 'remove-check':
                job['steps'].remove(step)
            else:
                step['run'] += ' || true'
            with self.subTest(change=change), self.assertRaises(ValueError):
                validate_workflow(workflow)

    def test_extra_workflow_cannot_reintroduce_automatic_ci(self):
        (self.root / '.github/workflows/legacy.yaml').write_text('on: push\njobs: {}\n')
        with self.assertRaisesRegex(ValueError, 'Unexpected workflow'):
            validate_tree(self.root)

    def test_non_ci_safeguards_remain_required(self):
        path = self.root / 'branch-protection/ruleset.json'
        original = json.loads(path.read_text())
        for kind in ('deletion', 'non_fast_forward', 'pull_request'):
            policy = copy.deepcopy(original)
            policy['rules'] = [r for r in policy['rules'] if r['type'] != kind]
            path.write_text(json.dumps(policy))
            with self.subTest(kind=kind), self.assertRaises(ValueError):
                validate_tree(self.root)


if __name__ == '__main__':
    unittest.main()
