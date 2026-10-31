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

An umbrella issue coordinates a group of related issues. Its title must begin
with the literal marker `[U]` followed by one space, before any theme prefix.
Keep the group's existing uppercase theme prefix and colon after the marker:

```text
[U] THEME PREFIX: Umbrella issue summary
```

For example:

```text
[U] TEST RULES REVIEW: Align test conventions across repositories
```

An umbrella whose children split into distinct concerns may group them under
sub-umbrella issues, one per concern. A sub-umbrella is a sub-issue of its
umbrella and coordinates part of the umbrella's group. Its title must begin
with the literal marker `[SU]` followed by one space, before the same theme
prefix:

```text
[SU] THEME PREFIX: Sub-umbrella issue summary
```

For example:

```text
[SU] TEST RULES REVIEW: Align instrumented test conventions
```

Sub-umbrellas are optional. Keep children directly under the umbrella when the
group is small or has a single concern. GitHub allows one parent per issue, so
a sub-umbrella lists any child that already has another parent instead of
holding it as a sub-issue.

Only umbrella issues use `[U]` and only sub-umbrella issues use `[SU]`; other
issues keep the normal title format.

A PR title matches its associated issue title as closely as its scope permits,
preserving the shared uppercase theme prefix when present and omitting the
issue-only `[U]` or `[SU]` marker. Otherwise, use the same title when the issue
and PR scopes match. For a partial or narrower implementation, keep the relevant
group prefix and adjust the descriptive portion to state what the PR delivers.

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

## Protected branches and merge requirements

Follow the [common branch protection policy](branch-protection/README.md).
Use pull requests for the default branch and `develop`, pass the repository's
required CI checks against the current base, and address review feedback before
merging. Resolve completed inline review threads; handle top-level comments
explicitly as well. Do not bypass unmet gates.

Apply the policy when setting up a new repository: GitHub does not inherit
branch rules from this defaults repository or from an app template.
