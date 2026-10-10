# .github

Default GitHub community health files for Sottti's repositories.

GitHub applies the default files in this public repository, including issue and pull request templates, to every repository owned by this account that has no file of that type itself, private repositories included. See GitHub's guide to [creating a default community health file](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/creating-a-default-community-health-file).

A repository with any file in its own `.github/ISSUE_TEMPLATE/` folder uses none of the issue templates here.

## Shared issue templates

[Bug Report](.github/ISSUE_TEMPLATE/bug_report.md) captures a confirmed failure
and its reproduction. [Task](.github/ISSUE_TEMPLATE/task.md) covers features,
refactors, tests, documentation, tooling, investigations and decisions.
The configuration disables blank issues for non-maintainers.

The templates originated from Sottti/Morylia commit
`a162ca110419640f2c53e6aa8ac282153ddc2e60`, with repository-specific wording
made neutral. Their title prompts now link to the shared title rules below.

Agents read inherited templates from this repository's
`.github/ISSUE_TEMPLATE/` folder on `main`, using the GitHub contents API:

```sh
gh api 'repos/Sottti/.github/contents/.github/ISSUE_TEMPLATE/bug_report.md?ref=main' -H 'Accept: application/vnd.github.raw+json'
gh api 'repos/Sottti/.github/contents/.github/ISSUE_TEMPLATE/task.md?ref=main' -H 'Accept: application/vnd.github.raw+json'
```

A repository with any file in its own `.github/ISSUE_TEMPLATE/` folder uses none
of these defaults; its agents read that repository's templates instead.

## Shared pull request template

The [pull request template](.github/pull_request_template.md) asks for a
Summary of the delivered change and Verification with actual results and the
tested revision. Details, Related and PR Stack are optional. Linked issues own
scope, acceptance criteria and planned checks; pull requests explain delivered
behavior and evidence. Repository-specific contribution and verification
guidance still applies.

Follow the [shared issue and PR title rules](CONTRIBUTING.md#issue-and-pull-request-titles).
The template provides guidance; it does not enforce titles or workflow behavior.

For stacked PRs, use one sibling PR Stack section with raw PR URLs in dependency
order and exactly one `**This PR**` marker. Remove unused optional sections.

Inherited files are not included in other repositories' clones. Agents read the
current shared PR template from this repository's `main` branch before preparing
a PR body:

```sh
gh api 'repos/Sottti/.github/contents/.github/pull_request_template.md?ref=main' -H 'Accept: application/vnd.github.raw+json'
```

The shared template takes effect after it merges into `main`. A repository's
local PR templates take precedence over this default. Check the root, `docs`
and `.github` directories, including their `PULL_REQUEST_TEMPLATE` subdirectories,
before relying on inheritance. Keep account-wide template changes here instead
of copying the template into other repositories. See GitHub's guide to
[creating a pull request template](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/creating-a-pull-request-template-for-your-repository).

## Shared title rules

[CONTRIBUTING.md](CONTRIBUTING.md#issue-and-pull-request-titles) is the canonical
owner of issue and PR naming rules, including uppercase theme prefixes for
coordinated issue groups, a leading `[U] ` before the theme prefix for umbrella
issues, and scope-appropriate PR titles. All three templates link to it.
Read the current rules before creating an issue or PR:

```sh
gh api 'repos/Sottti/.github/contents/CONTRIBUTING.md?ref=main' -H 'Accept: application/vnd.github.raw+json'
```

A local `CONTRIBUTING` file takes precedence over the shared contribution guide
in GitHub's discovery. Keep repository-specific policies there and link to the
shared title rules. GitHub inheritance does not copy these files into clones or
automatically update local agent guidance and workflows; those consumers must
read the shared sources explicitly.

[AGENTS.md](AGENTS.md) supplies the explicit read path for agents in this
repository. Other repositories need a corresponding routing reference in their
own applicable agent entrypoint. Agents following that guidance read the shared
title rules and selected template before composing a title or body, including
when creating through an API that does not populate templates automatically.
