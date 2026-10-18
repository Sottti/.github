# Loop Report

Loop PRs include **Loop Report** alongside the applicable PR template. Non-Loop
PRs remove the whole section, including its heading. Preserve Summary and
Verification, optional Details/Related and the separate optional PR Stack.
The shared template has no universal Tests section: Loop supplies its Local Tests
and Connected Tests content separately under the test-review contracts.

This guide implements the presentation contract in [issue #5](https://github.com/Sottti/.github/issues/5).
It documents expected records, not a generator, event format or working Loop
runtime. The examples are fictional render fixtures; their records, commit
aliases, URLs and test results are invented and prove no native execution.

## Publishing the section

1. Discover the actual template in the target repository before relying on the
   shared default. Local templates override it; a Loop PR still needs Loop Report
   alongside that template. This task changes no repository-specific template.
2. Obtain supplied records through **Review Coordinator → General Coordinator →
   PR Monitor**. General Coordinator supplies main-role timing; Review Coordinator
   supplies specialist activity/timing and both Tests tables through that path.
   PR Monitor publishes and reads back; it neither chooses specialists nor asks
   them directly, invents missing data or turns counts into approval.
3. State the snapshot's UTC time, current head and covered record range/run
   associations. Reconcile earlier attributable Loop records on takeover or a
   repeated run. Deduplicate stable request/result identities within their run
   and assignment context. Historical non-Loop reviews are excluded.
4. Keep all seven rows and exactly the two columns **Specialist Reviewer** and
   **Review Rounds**. State known coverage before the table. If earlier Loop
   history is unavailable, label the report partial and counts as applying only
   to the covered records; do not present them as lifetime totals or replace
   unknown earlier activity with zero. Zero means no completed attributable round
   within that stated coverage.
5. Put approximate elapsed intervals outside that table. Include Exceptions only
   for noteworthy events. Read back the stored PR body after each publication.

A review round is one requested review of a specific commit followed by that
specialist's complete returned feedback for that commit. No-findings feedback and
an explicitly requested delta/no-impact response count. A second completed request
adds one, even on the same commit. Deduplicate repeated delivery of the same
request/result; do not deduplicate distinct completed requests merely by commit.

Partial/no response, failed/unavailable attempts, retries, interruptions, tool
calls, consultations and unreviewed commits add no rounds. An interrupted request
that is resumed counts once when complete feedback returns. Mechanical approval
carry-forward without a new specialist response adds none. These are activity
counts: even a positive count does not prove current approval or readiness.

## Approximate elapsed time

Use attributable start-to-result event intervals for each assignment, not the
lifetime of a persistent conversation. Label each role/assignment or attempt,
its original candidate and UTC endpoints. Separate a resumed attempt and a
follow-up assignment from the original interval. Preserve an interrupted interval
as partial through its last recorded checkpoint; that checkpoint is not a result.
Duplicate delivery does not create an interval or reset its endpoints.

Label missing endpoints **unavailable** and unfinished assignments **in progress**,
including General Coordinator, PR Monitor and PR Integrator when applicable.
Do not fabricate a result to close the snapshot. Not-yet-created assignments have
no interval, not a zero duration. Update when new records arrive; do not recursively
refresh the report solely to time its own final publication.

Call this **approximate elapsed time**, never active-model, CPU or paid-token time.
Tools and waits inside an interval may contribute. Parallel intervals overlap;
do not sum them as Loop duration or add per-role or per-run totals. Preserve the
original reviewed/executed head on every record. An eligible mechanical sync uses
an explicit carry-forward reference from the original head to the snapshot head;
it never relabels old work as freshly reviewed or executed.

## Exceptions and publication audience

Omit an empty Exceptions heading and ordinary/no-event notes. Noteworthy examples
include unavailable advice and a recovered specialist outage. Advice that was not
obtained is never reported as a consultation result. A still-missing selected
specialist remains a missing-review blocker, never recovered or ready; no fallback
counts as that specialist's response. Notes supplement immediate coordinator alerts.

Outside-scope follow-up links belong in General Coordinator's human summary,
not Loop Report. Ordinary dependency/companion links in Related or PR Stack remain
allowed. Normal reporting of redacted findings inside a private work repository
does not grant permission to transfer private details to a public or wider
audience: flag that change through General Coordinator first. Public shared
examples contain only invented, safe records. Keep private transcripts, native
context identifiers, operational receipts, local paths and sensitive findings out.

## Expected record interface and cross-check

This is a semantic handoff, not a required serialization or new runtime service.
The shared Loop contract and the General Coordinator, Review Coordinator and
PR Monitor role contracts agree on these responsibilities:

| Supplied information | Owner and publication use |
| --- | --- |
| Work issue/repository, PR association, run and covered range; unavailable prior history | General Coordinator reconciles attributable prior records; PR Monitor states coverage. |
| Role/context/parent and assignment/request/result identities, with retry/resume links | Coordinators retain stable scoped identities to deduplicate delivery and distinguish new requests; public reports use safe aliases rather than private native IDs. |
| Requested/reviewed commit, complete feedback or explicit no-findings/delta result; failure/interruption state | Review Coordinator derives specialist rounds and current missing-review blockers. |
| Main-role assignment start/result events and separate resumed/follow-up intervals | General Coordinator supplies main timing, including ongoing/missing state. |
| Specialist start/result events, interrupted checkpoints and separate resumed/follow-up intervals | Review Coordinator supplies specialist timing through General Coordinator. |
| Snapshot head/time, included records, original reviewed/executed heads and any carry-forward reference | Coordinators preserve provenance; PR Monitor publishes the supplied snapshot and reads it back. |
| Noteworthy exception and recovered/still-missing state, with audience-safe detail | Coordinators retain immediate alerts; PR Monitor includes only noteworthy supplied facts. |
| Local Tests and Connected Tests judgments, gaps and actual execution provenance | Review Coordinator consolidates the test reviewers' content; only an unselected test reviewer permits coordinator-supplied content with limits/reasons. A selected unavailable reviewer remains blocking. |

The interface needs no private CPU/model telemetry and can be supplied by either
provider from assignment events. Documentation and fixtures do not prove either
provider has implemented record assembly, handoffs, publication or readback.
Those live demonstrations remain with PR Monitor and later Loop integration;
this task's boundary is wording, rendered examples and this cross-check.

## Render fixtures

Open each source as rendered Markdown. All fixtures are illustrative, including
any apparent verification result. Commit aliases such as `demo-h1` are fictional.

- [Non-Loop PR](loop-report-examples/non-loop.md): useful Summary/Verification;
  no Loop Report or unused optional heading.
- [Loop with no selected specialists](loop-report-examples/no-specialists.md):
  seven scoped zeros, ordinary case without Exceptions, ongoing main assignments.
- [Mixed activity and partial history](loop-report-examples/mixed.md): returned
  reviews, no-findings/delta feedback, takeover, retries, interruption/resumption,
  duplicate delivery, unavailable review/advice, missing timing and overlap.
- [Stacked PR and carry-forward](loop-report-examples/stacked.md): separate Tests
  content and PR Stack, original-head attribution and a recovered outage.
- [Coordinator human summary](loop-report-examples/coordinator-summary.md):
  outside-scope follow-up link outside the PR report.

The examples deliberately contrast unavailable advice, a still-missing selected
reviewer and a recovered reviewer. They introduce no coverage metric, extra
reviewer-table column, approval inference, new review request or suite execution.
