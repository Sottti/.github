<!--
Follow the shared title rules:
https://github.com/Sottti/.github/blob/main/CONTRIBUTING.md#issue-and-pull-request-titles
Match the associated issue's title as closely as scope permits, keeping
its group prefix when present and omitting the issue-only `[U]` marker.
Without an issue, use a concise change title.
Replace the prompts and remove unused optional sections.
Describe the final change for someone unfamiliar with the discussion.
Follow the repository's contribution and verification guidance.
-->

## Summary

<!--
Explain the problem, why it matters, and what this change does.
Include a concrete before/after example when useful.
Link the implementing issue when one exists.
Use "Closes" only when this PR completes it; otherwise use "Part of"
or "Related to". State partial scope or changed acceptance criteria.
-->

## Details

<!--
Optional: explain implementation choices or tradeoffs that help review.
Include relevant preservation requirements, limitations, migration
steps, or rollout considerations. Link durable decisions and longer
design documents. Avoid repeating the summary or listing every file.
Delete this section when the summary is sufficient.
-->

## Verification

<!--
Record actual results against the issue's acceptance criteria, including
relevant failure scenarios and regressions. Without an issue, explain
how the intended outcome was checked.
Identify the tested revision and applicable checks, their outcomes,
and supporting reports or screenshots. Summarize results here and
link detailed logs. Include environment details when they affect proof.
Distinguish passed, failed, pending, blocked, and not-required checks.
Explain omissions and limitations. Evidence from an earlier revision
must identify that revision and explain its applicability.
-->

- Tested revision:
- Check or scenario — result and evidence:
- Outstanding checks or limitations, if any:

## Loop Report

<!--
Loop PRs only: remove this entire section for non-Loop work.
Use coordinator-supplied records, not inferred reviews or timing.
Full semantics and fictional examples:
https://github.com/Sottti/.github/blob/develop/docs/loop-report.md
Identify the as-of head/time and covered records, including unavailable history.
Counts describe completed attributable reviews, not approval. Zero applies only
within known coverage; do not silently reset missing earlier Loop activity.
-->

Snapshot: <!-- head, UTC time, covered records and history limitations -->

| Specialist Reviewer | Review Rounds |
| --- | --- |
| Compose | <!-- count --> |
| State And Concurrency | <!-- count --> |
| Data | <!-- count --> |
| Architecture | <!-- count --> |
| Security | <!-- count --> |
| Local Test | <!-- count --> |
| Connected Test | <!-- count --> |

**Approximate elapsed time**

<!--
One interval per assignment/attempt, outside the reviewer table: role and safe
assignment label, original candidate, start/result times and approximate duration.
Separate resumed/follow-up intervals; mark interrupted work partial, unfinished
work in progress and missing timestamps unavailable. Tools/waits may contribute.
Do not sum overlapping intervals or add role/run totals. Preserve original heads
and any mechanical carry-forward reference. Refresh from supplied records without
recursive self-timing updates. Add ### Exceptions after the intervals only for
noteworthy events; omit the heading when none apply. Keep missing selected reviews
blocking. Outside-scope follow-up links belong in the
coordinator's human summary. Local/Connected Tests remain separate supplied content.
-->

- <!-- assignment interval -->

## Related

<!--
Optional: link dependencies, companion changes and follow-up work,
explaining each relationship. Distinguish prerequisites from related
work and identify anything needed before this PR can merge.
Delete this section when there is nothing to add.
-->

## PR Stack

<!--
Optional: for stacked PRs only.
List raw PR URLs in dependency order, marking this PR exactly once
with **This PR**. Delete this section for an independent PR.
-->
