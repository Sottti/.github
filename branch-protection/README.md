# Branch protection and weekly validation

The common policy protects the default branch and `develop`, including a
`develop` branch created later. It requires pull requests and resolved review
threads, blocks force pushes and branch deletion, and has no bypass actors,
including administrators. Preserve unrelated security rules and stricter
non-CI protections. Required approvals remain zero for solo maintenance.

Local verification on the current candidate/base and independent review remain
required before merge. Assess automated review findings and top-level comments;
GitHub's conversation rule enforces resolved inline threads only.

## Weekly-only Actions policy

No Actions or CI starts automatically on PR creation, updates, pushes or merges.
Remove direct and indirect PR/push/tag/release/comment/merge-group/workflow-run
triggers and automatic caller chains, including managed workflows, CodeQL
default setup and legacy publishing paths where applicable. Keep useful
existing checks, thresholds, failure semantics, summaries and reports in the
approved weekly slot or explicit manual execution. Add no meaningless CI.
Talk-To-Google-Health publishes manually only.

Do not require CI status checks on protected branches: weekly results do not
validate each PR. Remove overlapping CI requirements from every effective
ruleset and classic protection. Preserve all other live rules, conditions,
enforcement and bypass settings using fresh reads and minimal changes, rather
than replacing current settings from this example or a historical snapshot.
No dummy successful PR job, temporary bypass or automatic retry loop is used.

Weekly validation can discover a regression after merge. Contributors must run
applicable local checks and complete independent review before merging; report
the exact tested SHA and any remaining limitations.

## Weekly timetable

All slots use the IANA timezone **Europe/Madrid**, preserving local time across
DST. The schedule runs the latest default-branch `develop` revision. GitHub
may delay or drop a scheduled event; failure email cannot detect a missing run.
At a DST spring-forward gap, GitHub advances a skipped local time to the next
valid time. Do not replace these slots with fixed UTC or old Monday schedules.

| Repository | Day | Local time |
| --- | --- | --- |
| .github | Sunday | 03:17 |
| Agent-Workflows | Monday | 03:17 |
| Android-Interview-Practice | Tuesday | 02:17 |
| Android-App-Template | Tuesday | 03:17 |
| dependabot | Wednesday | 02:17 |
| Morylia | Wednesday | 03:17 |
| Morylia-Dashboard-Data | Thursday | 02:17 |
| Morylia-Dashboard | Thursday | 03:17 |
| Milliscope | Friday | 02:17 |
| RollerCoasters | Friday | 03:17 |
| Web | Saturday | 03:17 |
| Talk-To-Google-Health | Manual only | — |

These are approved target slots, not claims that downstream rollouts or
scheduled runs have completed. Each repository has its own implementation issue
linked from [shared policy #13](https://github.com/Sottti/.github/issues/13).

## This repository: validation and recovery

`.github/workflows/ci.yml` allows only `schedule` (`17 3 * * 0` with
`timezone: Europe/Madrid`) and `workflow_dispatch`. The `verify` job runs on
trusted `refs/heads/develop` in `Sottti/.github`, retaining:

```sh
python3 -m unittest discover -s tests
python3 scripts/validate_repository.py
```

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
preferences. Verify the actual account's notification routing and schedule
actor: ownership alone does not establish the recipient. Keep mailbox details
private. A controlled manual-failure email proves that path only; a passing
schedule does not prove scheduled-failure delivery. Do not deliberately fail a
production weekly suite to obtain it. No paid notification service is added.

The original restoration in [#9](https://github.com/Sottti/.github/issues/9)
is historical. Its future instructions and existing follow-up must preserve
this policy and timetable; never replay its restoration helper or reinstate
retired PR checks. Preserve completed results and immutable original evidence.

## New repositories and existing rollouts

GitHub does not inherit rulesets or workflows from this personal `.github`
repository. Repository templates copy files and branch contents; default
branch naming does not install protection or validation.

1. Keep the default branch named `develop`. If meaningful checks exist, retain
   them weekly in an owner-approved staggered slot and allow explicit manual
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

For a later `develop` branch, verify its intended tip locally and through review,
then read back protection after creation. There is no required-check creation
gate to satisfy or bypass. This explicit setup does not automatically roll out
to any other repository.

GitHub references: [workflow schedule syntax](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#onschedule),
[rulesets](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets),
and [Actions notifications](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/monitoring-workflows/notifications-for-workflow-runs).
