import copy
import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from validate_repository import REQUIRED_FILES, validate_tree


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
            ('required_status_checks', 'strict_required_status_checks_policy', False),
            ('required_status_checks', 'strict_required_status_checks_policy', 1),
            ('required_status_checks', 'do_not_enforce_on_create', True),
            ('required_status_checks', 'required_status_checks', []),
        ]
        for kind, key, value in changes:
            with self.subTest(rule=kind, parameter=key):
                policy = copy.deepcopy(original)
                next(rule for rule in policy['rules'] if rule['type'] == kind)['parameters'][key] = value
                path.write_text(json.dumps(policy))
                with self.assertRaises(ValueError):
                    validate_tree(self.root)


if __name__ == '__main__':
    unittest.main()
