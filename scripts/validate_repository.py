"""Validate the shared files and the documented protected-branch contract."""

import json
from pathlib import Path
import re
import subprocess


REQUIRED_FILES = [
    'README.md', 'CONTRIBUTING.md', 'AGENTS.md', '.github/pull_request_template.md',
    '.github/ISSUE_TEMPLATE/bug_report.md', '.github/ISSUE_TEMPLATE/task.md',
    '.github/ISSUE_TEMPLATE/config.yml', 'branch-protection/README.md',
    'branch-protection/ruleset.json',
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
    require(set(rules) == {'deletion', 'non_fast_forward', 'pull_request', 'required_status_checks'},
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
    expected_checks = {
        'strict_required_status_checks_policy': True,
        'do_not_enforce_on_create': False,
        'required_status_checks': [{'context': 'verify', 'integration_id': 15368}],
    }
    require(json.dumps(rules['required_status_checks'].get('parameters'), sort_keys=True) == json.dumps(expected_checks, sort_keys=True),
            'Require strict verify checks from GitHub Actions, including branch creation')


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


if __name__ == '__main__':
    validate_tree(Path(__file__).resolve().parents[1])
    print('Shared files, template YAML and branch policy are valid')
