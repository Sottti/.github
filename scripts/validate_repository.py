"""Validate the shared files and the documented protected-branch contract."""

import json
from pathlib import Path
import re
import subprocess


REQUIRED_FILES = [
    'README.md', 'CONTRIBUTING.md', 'AGENTS.md', '.github/pull_request_template.md',
    '.github/ISSUE_TEMPLATE/bug_report.md', '.github/ISSUE_TEMPLATE/task.md',
    '.github/ISSUE_TEMPLATE/config.yml', 'branch-protection/README.md',
    'branch-protection/ruleset.json', '.github/workflows/ci.yml',
]


def require(condition, message):
    if not condition:
        raise ValueError(message)


def parse_yaml(text, name):
    # Ruby/Psych is available in the standard GitHub-hosted Ubuntu image.
    # Safe loading rejects malformed YAML and untrusted object tags.
    result = subprocess.run(
        ['ruby', '-ryaml', '-rjson', '-e', 'puts JSON.generate(YAML.safe_load(STDIN.read))'],
        input=text, text=True, capture_output=True,
    )
    require(result.returncode == 0, f'Invalid YAML in {name}: {result.stderr.strip()}')
    value = json.loads(result.stdout)
    require(isinstance(value, dict), f'Expected a YAML mapping in {name}')
    return value


def validate_policy(policy):
    require(policy.get('name') == 'Common branch protection', 'Unexpected ruleset name')
    require(policy.get('target') == 'branch', 'Ruleset must target branches')
    require(policy.get('enforcement') == 'active', 'Ruleset must be active')
    require(policy.get('bypass_actors') == [], 'Bypass actors must be empty')
    require(policy.get('conditions') == {'ref_name': {
        'include': ['~DEFAULT_BRANCH', 'refs/heads/develop'], 'exclude': []}},
        'Protect the default branch and develop without exclusions')
    rules = {rule['type']: rule for rule in policy['rules']}
    require(len(rules) == len(policy['rules']), 'Duplicate rule types')
    require(set(rules) == {'deletion', 'non_fast_forward', 'pull_request'},
            'Unexpected or missing policy rules')
    expected_pr = {
        'required_approving_review_count': 0,
        'dismiss_stale_reviews_on_push': True,
        'require_code_owner_review': False,
        'require_last_push_approval': False,
        'required_review_thread_resolution': True,
        'allowed_merge_methods': ['merge', 'squash', 'rebase'],
    }
    require(json.dumps(rules['pull_request'].get('parameters'), sort_keys=True) == json.dumps(expected_pr, sort_keys=True),
            'Pull request policy must preserve zero approvals and the documented review settings')


TRUSTED_JOB = """github.repository == 'Sottti/.github' &&
github.ref == 'refs/heads/develop' &&
(github.event_name == 'schedule' || github.event_name == 'workflow_dispatch')"""
RETAINED_COMMANDS = (
    'python3 -m unittest discover -s tests',
    'python3 scripts/validate_repository.py',
)


def validate_workflow(workflow):
    require(workflow.get('on') == {
        'schedule': [{'cron': '17 3 * * 0', 'timezone': 'Europe/Madrid'}],
        'workflow_dispatch': None,
    }, 'Allow only Sunday 03:17 Europe/Madrid schedule and explicit manual dispatch')
    require(workflow.get('permissions') == {'contents': 'read'},
            'Validation needs only read access')
    require(set(workflow.get('jobs', {})) == {'verify'}, 'Retain the verify job inventory')
    job = workflow['jobs']['verify']
    require(' '.join(str(job.get('if', '')).split()) == ' '.join(TRUSTED_JOB.split()),
            'Run schedule/manual validation only on trusted develop; never depend on PR payload')
    require(job.get('runs-on') == 'ubuntu-latest' and job.get('timeout-minutes') == 10,
            'Preserve the validation runner and timeout')
    require('uses' not in job and not job.get('continue-on-error'),
            'Retain local job execution and failure semantics')
    steps = job.get('steps', [])
    require(isinstance(steps, list), 'Expected validation steps')
    for command in RETAINED_COMMANDS:
        checks = [step for step in steps if step.get('run') == command]
        require(len(checks) == 1 and 'if' not in checks[0]
                and not checks[0].get('continue-on-error'),
                'Retain unconditional failing validation: ' + command)
    checkouts = [step for step in steps if str(step.get('uses', '')).startswith('actions/checkout@')]
    require(len(checkouts) == 1 and 'if' not in checkouts[0]
            and checkouts[0].get('with') == {'persist-credentials': False},
            'Check out the event source without credentials or source overrides')
    require(not any(step.get('continue-on-error') for step in steps),
            'Do not hide validation failures')


def validate_tree(root):
    root = Path(root)
    for name in REQUIRED_FILES:
        require((root / name).read_text(encoding='utf-8').strip(), f'Empty shared file: {name}')
    parse_yaml((root / '.github/ISSUE_TEMPLATE/config.yml').read_text(), 'config.yml')
    for path in (root / '.github/ISSUE_TEMPLATE').glob('*.md'):
        match = re.match(r'\A---\r?\n(.*?)\r?\n---(?:\r?\n|\Z)', path.read_text(), re.S)
        require(match is not None, f'Missing YAML front matter in {path}')
        metadata = parse_yaml(match.group(1), str(path))
        require(all(isinstance(metadata.get(key), str) and metadata[key].strip()
                    for key in ['name', 'about']), f'Missing template name or about in {path}')
    validate_policy(json.loads((root / 'branch-protection/ruleset.json').read_text()))
    workflows = sorted(path.relative_to(root).as_posix()
                       for path in (root / '.github/workflows').rglob('*')
                       if path.is_file() and path.suffix in ('.yml', '.yaml'))
    require(workflows == ['.github/workflows/ci.yml'],
            'Unexpected workflow: audit every automatic or reusable caller before adding coverage')
    validate_workflow(parse_yaml((root / '.github/workflows/ci.yml').read_text(), 'ci.yml'))


if __name__ == '__main__':
    validate_tree(Path(__file__).resolve().parents[1])
    print('Shared files, workflow YAML and weekly-only branch policy are valid')
