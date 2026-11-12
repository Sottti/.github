# Branch protection and CI execution

The common policy protects the default branch and `develop`, including a
`develop` branch created later. It requires pull requests and resolved review
threads, blocks force pushes and branch deletion, and has no bypass actors,
including administrators. Preserve unrelated security rules and stricter
non-CI protections. Required approvals remain zero for solo maintenance.

Local verification on the current candidate/base and independent review remain
required before merge. Assess any review findings and top-level comments.
GitHub's conversation rule enforces resolved inline threads only.

## Default weekly-only Actions policy

No Actions or CI starts automatically on PR creation, updates, pushes or merges.
Remove direct and indirect PR/push/tag/release/comment/merge-group/workflow-run
triggers and automatic caller chains, including managed workflows, CodeQL
default setup and legacy publishing paths where applicable. Keep useful
existing checks, thresholds, failure semantics, summaries and reports in the
approved weekly slot or explicit manual execution. Add no meaningless CI.
Talk-To-Google-Health publishes manually only. The owner-approved exceptions
are `Sottti/.github`, `Sottti/Android-App-Template` and `Sottti/RollerCoasters`:
their existing validation runs on every PR and on manual dispatch, without
weekly or post-merge CI. Android App Template retains advanced CodeQL analysis.
Dependabot follows the separate [monthly maintenance policy](#monthly-dependency-updates). Other repositories
do not inherit this execution policy from the shared templates.

Do not require CI status checks on protected branches: weekly results do not
validate each PR. Remove overlapping CI requirements from every effective
ruleset and classic protection. Preserve all other live rules, conditions,
enforcement and bypass settings using fresh reads and minimal changes, rather
than replacing current settings from this example or a historical snapshot.
No dummy successful PR job, temporary bypass or automatic retry loop is used.

Weekly validation can discover a regression after merge. Contributors must run
applicable local checks and complete independent review before merging; report
the exact tested SHA and any remaining limitations.

## Monthly dependency updates

Dependabot version updates are enabled only for the nine repositories below.
They check on the first day of each month in Europe/Madrid, independently of
weekly CI. New or changed configuration may also trigger an initial check.

| Repository | Ecosystems | Local time |
| --- | --- | --- |
| .github | GitHub Actions | 03:17 |
| Agent-Workflows | pip checker requirements, GitHub Actions | 03:17 |
| Android-Interview-Practice | npm/pnpm, GitHub Actions | 03:17 |
| Android-App-Template | Gradle, GitHub Actions | 03:17 |
| Morylia | Gradle / GitHub Actions | 08:30 / 09:00 |
| Morylia-Dashboard | GitHub Actions | 03:17 |
| Morylia-Dashboard-Data | GitHub Actions | 03:17 |
| RollerCoasters | Gradle, GitHub Actions | 03:17 |
| Web | Root application npm, GitHub Actions | 03:17 |

Standard-runner Dependabot maintenance is an explicit allowed exception to the
Actions restriction. GitHub does not charge these update jobs against included
Actions minutes. Validation triggered by update PRs follows the repository's
existing policy: public PR-validation exceptions keep their checks, while
private repositories start no PR CI. Keep the CI triggers and weekly slots.

Monthly scheduling applies to routine version updates. Security alerts and
existing automatic security-update settings remain unchanged; security fixes,
where enabled, respond to advisories independently of this monthly schedule.
Preserve existing groups, labels, assignees, PR limits and rebase settings when
changing an existing schedule. New configurations group minor/patch updates per
ecosystem, keep major updates separate, disable automatic rebasing and limit
each ecosystem to five open update PRs. Update PRs still require verification
and review; no automatic merge is configured.

The profile README repository `Sottti` has no Dependabot configuration. Do not
enable dependency updates for historical repositories, including
`Starling-Android-Interview`, or repositories outside the owner-approved list.

## Weekly timetable

All slots use the IANA timezone **Europe/Madrid**, preserving local time across
DST. The schedule runs the latest default-branch `develop` revision. GitHub
may delay or drop a scheduled event; failure email cannot detect a missing run.
At a DST spring-forward gap, GitHub advances a skipped local time to the next
valid time. Preserve owner-approved local slots; do not restore superseded schedules
or replace them with fixed UTC times.

| Repository | Day | Local time |
| --- | --- | --- |
| .github | Every PR and manual only | — |
| Agent-Workflows | Monday | 00:38 |
| Android-Interview-Practice | Monday | 00:38 |
| Android-App-Template | Every PR and manual only | — |
| Morylia | Monday | 00:38 |
| Morylia-Dashboard-Data | Monday | 00:38 |
| Morylia-Dashboard | Monday | 00:38 |
| Milliscope | No automation | — |
| RollerCoasters | Every PR and manual only | — |
| Web | Monday | 00:38 |
| Talk-To-Google-Health | Manual only | — |
| Material-Design-Nav-Drawer | No automation | — |
| OkHttp-Retrofit-Moshi-Picasso | No automation | — |
| OkHttp-Volley-Gson | No automation | — |
| My-Lists | No automation | — |
| Watch | No automation | — |
| SpaceX-Rocket-Launches | No automation | — |

The seven historical repositories marked **No automation** are exceptions
to the weekly/manual policy: disable GitHub Actions and Dependabot entirely.
They run no scheduled, daily, PR, push or manual CI. Do not reintroduce automated
dependency updates or restore the cancelled Milliscope weekly plan. This covers
the four inactive Medium article companions, the historical personal projects
My-Lists and Watch, and the historical interview project SpaceX-Rocket-Launches.
Their source and local verification commands remain available for reference.
The retired Dependabot demonstration repository has no weekly slot; do not
recreate it or restore its cancelled CI plan.

These are approved target slots, not claims that downstream rollouts or
scheduled runs have completed. Each repository has its own implementation issue
linked from [shared policy #13](https://github.com/Sottti/.github/issues/13).

## This repository: PR validation and manual recovery

`.github/workflows/ci.yml` allows only `pull_request` and `workflow_dispatch`.
Every PR, including draft PRs and updates, runs the `verify` job against the
default checkout of its merge revision. Manual runs execute only from trusted
`refs/heads/develop` in `Sottti/.github`. Both paths retain:

```sh
python3 -m unittest discover -s tests
python3 scripts/validate_repository.py
```

The single standard Ubuntu job needs only read access to repository contents.
It uses no secrets or `pull_request_target`, never runs on pushes or after
merge, and has no scheduled trigger. Concurrency groups use the PR number
(or manual ref), cancelling obsolete work for the same PR without cancelling
other PRs. The validator tests enforce these trigger, source, cancellation,
permission and coverage constraints.

To recover explicitly, select **Repository validation → Run workflow → develop**
in GitHub, or run:

```sh
gh workflow run ci.yml --repo Sottti/.github --ref develop
```

Record the actual source SHA, event, actor, executed jobs and result from the
run. Non-develop manual dispatch skips the trusted job and is not a pass.
Inspect job logs to distinguish an executed test failure from skipped work,
cancellation, or runner/billing rejection before startup. Keep explicit manual
recovery; do not create an automatic retry loop.

Use the owner's existing GitHub Actions **Email** and **failed workflows only**
preferences. Verify the actual account's notification routing and workflow
actor: ownership alone does not establish the recipient. Keep mailbox details
private. A controlled manual-failure email proves that path only; a passing
run does not prove failure-email delivery. Do not deliberately fail production
validation to obtain it. No paid notification service is added.

The original restoration in [#9](https://github.com/Sottti/.github/issues/9)
is historical. Its future instructions and existing follow-up must preserve
this policy and timetable; never replay its restoration helper or reinstate
retired PR checks. Preserve completed results and immutable original evidence.

## New repositories and existing rollouts

GitHub does not inherit rulesets or workflows from this personal `.github`
repository. Repository templates copy files and branch contents; default
branch naming does not install protection or validation.

1. Keep the default branch named `develop`. If meaningful checks exist, retain
   them weekly in an owner-approved weekly slot and allow explicit manual
   execution on trusted `develop`. Never add automatic PR/push execution or a
   required status gate; a repository without meaningful checks needs no CI.
2. Import [ruleset.json](ruleset.json) for a new repository, preserving any
   stricter existing non-CI settings:

   ```sh
   gh api --method POST repos/OWNER/REPOSITORY/rulesets \
     --input branch-protection/ruleset.json
   ```

3. Inventory workflow files on the default branch, open PRs and other live
   branches; registered/retired workflows; managed/default-setup integrations;
   effective rulesets; and classic protection. Coordinate stopped writers before
   updating another active branch. Reconcile stale PR definitions and retired
   registrations so a default-branch-only edit cannot leave old CI running.
4. Remove only required CI gates from fresh live settings everywhere enforced.
   Preserve PR requirements, review threads, force-push/deletion protection and
   unrelated security rules. Read back source settings and effective rules on
   every protected branch. Never recreate deleted `main` refs for old scopes.
5. Validate syntax, schedule/manual eligibility and rejection of automatic
   direct/indirect events. Exercise a normal reviewed PR/update/merge and inspect
   actual Actions runs and mergeability. Do not bypass unrelated merge gates.
6. Run retained checks locally or manually, recording exact source/outcomes.
   Link the first genuine `schedule` run when available; keep scheduled proof
   explicitly pending until then. Manual verification is not scheduler proof.

These setup defaults do not enable PR validation in other repositories.
The three named repositories use their explicit PR/manual exceptions; all
other repositories retain their approved weekly, manual-only or no-automation policy.

For a later `develop` branch, verify its intended tip locally and through review,
then read back protection after creation. There is no required-check creation
gate to satisfy or bypass. This explicit setup does not automatically roll out
to any other repository.

GitHub references: [workflow schedule syntax](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#onschedule),
[rulesets](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets),
and [Actions notifications](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/monitoring-workflows/notifications-for-workflow-runs).
