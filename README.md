# .github

Default GitHub community health files for Sottti's repositories.

GitHub applies the default files in this public repository, such as issue templates, to every repository owned by this account that has no file of that type itself, private repositories included. See GitHub's guide to [creating a default community health file](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/creating-a-default-community-health-file).

A repository with any file in its own `.github/ISSUE_TEMPLATE/` folder uses none of the issue templates here.

## Shared issue templates

[Bug Report](.github/ISSUE_TEMPLATE/bug_report.md) captures a confirmed failure
and its reproduction. [Task](.github/ISSUE_TEMPLATE/task.md) covers features,
refactors, tests, documentation, tooling, investigations and decisions.
The configuration disables blank issues for non-maintainers.

The templates come from Sottti/Morylia commit
`a162ca110419640f2c53e6aa8ac282153ddc2e60`, preserving its sections, order,
guidance and front matter with repository-specific wording made neutral.

Agents read inherited templates from this repository's
`.github/ISSUE_TEMPLATE/` folder on `main`, using the GitHub contents API:

```sh
gh api 'repos/Sottti/.github/contents/.github/ISSUE_TEMPLATE/bug_report.md?ref=main' -H 'Accept: application/vnd.github.raw+json'
gh api 'repos/Sottti/.github/contents/.github/ISSUE_TEMPLATE/task.md?ref=main' -H 'Accept: application/vnd.github.raw+json'
```

A repository with any file in its own `.github/ISSUE_TEMPLATE/` folder uses none
of these defaults; its agents read that repository's templates instead.
