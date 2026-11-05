<!--
Follow the shared title rules:
https://github.com/Sottti/.github/blob/develop/CONTRIBUTING.md#issue-and-pull-request-titles
Match the associated issue's title as closely as scope permits, keeping
its group prefix when present and omitting the issue-only `[U]` or `[SU]`
marker.
Without an issue, use a concise change title.
Replace the prompts and remove unused optional sections.
Describe the final change for someone unfamiliar with the discussion.
Follow the repository's contribution and verification guidance.
Keep PRs focused. If a PR exceeds 1,000 changed lines (additions plus
deletions), or requires more than five completed peer-review rounds, assess
whether it can be split into coherent, independently testable PRs. Split when
practical; otherwise briefly document why keeping it together is preferable
and continue. These are reassessment thresholds, not hard limits. An issue
may be implemented through multiple PRs. Full guidance:
https://github.com/Sottti/.github/blob/develop/CONTRIBUTING.md#pr-scope-and-review-rounds
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
Record applicable local verification and independent review. Most repositories
use weekly/manual validation; do not wait for or invent nonexistent PR checks.
For repositories with an approved PR-validation exception, report their actual
check results. Weekly/manual results apply to their tested source; manual success does
not prove the weekly scheduler fired.
Explain omissions and limitations. Evidence from an earlier revision
must identify that revision and explain its applicability.
-->

- Tested revision:
- Check or scenario — result and evidence:
- Outstanding checks or limitations, if any:

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
