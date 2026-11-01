# Agent guidance

## Creating GitHub issues and pull requests

Before composing an issue or PR title or body, read the current
[shared contribution guide](https://github.com/Sottti/.github/blob/develop/CONTRIBUTING.md)
and the appropriate template from `Sottti/.github` on `develop`:

```sh
gh api 'repos/Sottti/.github/contents/CONTRIBUTING.md?ref=develop' -H 'Accept: application/vnd.github.raw+json'
# For a bug report:
gh api 'repos/Sottti/.github/contents/.github/ISSUE_TEMPLATE/bug_report.md?ref=develop' -H 'Accept: application/vnd.github.raw+json'
# For other issues:
gh api 'repos/Sottti/.github/contents/.github/ISSUE_TEMPLATE/task.md?ref=develop' -H 'Accept: application/vnd.github.raw+json'
# For a pull request:
gh api 'repos/Sottti/.github/contents/.github/pull_request_template.md?ref=develop' -H 'Accept: application/vnd.github.raw+json'
```

Apply the shared title rules and fill the selected template before submitting.
Raw API creation does not populate templates automatically. Preserve applicable
repository-specific metadata, contribution and verification policies, and read
back the stored title and body after creation. If a shared source cannot be
read, report that limitation instead of silently assuming a local copy is current.

## Validation and delivery

Read the shared CI policy in `CONTRIBUTING.md` and
`branch-protection/README.md`. This repository is the owner-approved exception:
run its existing validation on every PR and on explicit manual dispatch from
`develop`, cancel superseded PR runs, and use no weekly or post-merge run.
Run applicable local checks, assess the actual PR check and obtain independent
review before merge. Do not add required CI status gates or revive retired
restoration instructions. Other repositories retain their own approved PR, weekly,
manual-only or no-automation policy; shared templates do not enable their CI.
