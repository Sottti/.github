---
name: Bug Report
about: Report something broken and describe how to reproduce it.
title: ""
labels: Bug
assignees: ""
---

<!--
Use a concise title that describes the failure, following the shared title rules:
https://github.com/Sottti/.github/blob/main/CONTRIBUTING.md#issue-and-pull-request-titles
Use the group's uppercase theme prefix for coordinated issues.
Assign the issue's actual
author using GitHub metadata; add relevant durable classification labels
alongside Bug when useful. Replace the prompts before submitting.
If the failure itself is unconfirmed, use Task for an investigation.
-->

## Summary

<!-- Describe what is broken, why it matters, and the affected behavior. -->

## Scope

<!--
Identify the affected behavior and the correction this issue owns. Include
behavior to preserve and explicit exclusions; keep unrelated cleanup separate.
-->

- Affected behavior and intended correction.
- Behavior to preserve and work outside this issue.

## Acceptance Criteria

<!--
List observable outcomes that demonstrate the corrected behavior, including
relevant failure handling and behavior that must remain unchanged.
If correction scope still needs agreement, state "Criteria pending scope
agreement" rather than inventing settled criteria.
-->

- [ ] Describe an observable completion criterion.

## Verification

<!--
Map the criteria to checks that repeat the failing scenario and cover relevant
regressions. Identify expected results and evidence. Follow
the repository's own verification guidance for applicable readiness. Keep the
plan here; record detailed results, tested revisions, and reports in the
implementing PR and link them here when available. If the plan is unresolved,
state "Verification pending scope agreement" rather than inventing settled
checks.
-->

- Check or scenario, expected result, and evidence.

## Notes

### How To Reproduce

<!--
Include relevant preconditions and the smallest steps or command that show the
failure. Identify the affected version or inspected commit. Add device, OS,
or tooling details only when they matter to reproduction.
If reproduction steps are not yet known, say so and rely on Evidence.
-->

1. Reproduction step.

### Expected Behavior

<!-- Describe the intended behavior and link its contract when available. -->

### Actual Behavior

<!--
Describe the observed failure and its frequency, when known. Distinguish an
observed failure from a suspected defect or source-audit finding.
-->

### Evidence

<!--
Add concise logs, screenshots, failing tests, or source links. Put unconfirmed
causes and questions under an Open Questions subsection when useful. Link long
reports and delivery history instead of accumulating full logs here.
-->

## Depends On

<!--
List actual prerequisites with issue links and explain what each must provide.
Describe external or not-yet-filed prerequisites without inventing a number.
Replace "None" when a prerequisite exists. Put coordination with related work
in Notes when it is not a prerequisite.
-->

- None.

## Blocks

<!--
List downstream issues with links and explain what this issue must provide.
If a downstream issue has not been created, describe it without inventing a
number. Replace "None" when there is a downstream dependency.
-->

- None.

## Stacked Issues

<!--
Optional: delete this section when the issue is not part of a stack. List the
issues in execution order with links and short titles. Include this issue once
it has a number and mark it with **This Issue**. Depends On and Blocks above
describe the actual prerequisite and downstream relationships.
-->

1. Issue link — Short title.
