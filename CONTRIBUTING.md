# Contribution guidance

These shared rules apply to issues and pull requests across Sottti-owned
repositories. Follow the target repository's contribution and verification
guidance as well.

## Issue and pull request titles

An issue title concisely summarizes what that individual issue is about.
A standalone issue has no stack or theme prefix.

When issues form a stack or a coordinated multi-issue goal or implementation,
all issues in that group share the same prefix summarizing the overall theme.
The prefix may contain one or multiple words and is uppercase. Use a colon
followed by a space between the prefix and the individual issue summary:

```text
THEME PREFIX: Individual issue summary
```

For example:

```text
TEST RULES REVIEW: Align local and instrumentation test conventions
```

The uppercase rule applies to the theme prefix, not the individual summary.

A PR title matches its associated issue title as closely as its scope permits,
preserving the shared uppercase theme prefix when present. Use the same title
when the issue and PR scopes match. For a partial or narrower implementation,
keep the relevant group prefix and adjust the descriptive portion to state
what the PR delivers.

Without an associated issue, use a concise title summarizing the PR's change.
There is no need to create an issue solely for naming.

## Shared templates and discovery

Use the shared [Bug Report](.github/ISSUE_TEMPLATE/bug_report.md),
[Task](.github/ISSUE_TEMPLATE/task.md) and
[pull request template](.github/pull_request_template.md).
The [README](README.md) explains inheritance and how agents read the current
shared sources through GitHub. Local contribution guidance should link to
these title rules while retaining repository-specific policies.

Templates and this guide provide creation guidance; they do not automatically
enforce title wording or install agent instructions or workflows in other
repositories.
