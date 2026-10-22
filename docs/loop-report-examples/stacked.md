<!-- Fictional rendering fixture. All records, URLs, tests and results are invented. -->

## Summary

Add draft restoration after the prerequisite storage change. This PR depends on
the first PR in the stack and keeps its implementation diff separate.

## Verification

- Original exercised revision: fictional `demo-h1`; fixture evidence `L1/C1` below.
- Later report-refresh snapshot: fictional `demo-h2`, a conflict-free mechanical synchronization.
- Carry-forward `M1`: `demo-h1 → demo-h2`; the supplied coordinator assessment preserves prior review/execution provenance and states no relevant impact. No specialist was requested merely to refresh this report.
- Current-head CI `CI2` — passed in this fictional scenario. Source synchronization alone would not establish applicability or fresh execution.

## Tests

These illustrative tables are separate from Loop activity; real tables follow
the target repository's obligations. Assessment, execution and gaps are distinct.

### Local Tests

| Area | Assessment | Execution / evidence | Gaps |
| --- | --- | --- | --- |
| Screenshot Tests | Adequate for defined fixture states | 8 examples passed on `demo-h1`; `L1`, carried by `M1` | None in fixture scope |
| Integration Tests | Restoration behavior assessed | 6 examples passed on `demo-h1`; `L1`, carried by `M1` | None in fixture scope |
| Unit Tests | Owned draft logic assessed | 10 examples passed on `demo-h1`; `L1`, carried by `M1` | None in fixture scope |

### Connected Tests

| Area | Assessment | Execution / evidence | Gaps |
| --- | --- | --- | --- |
| Unit Tests | Required device behavior assessed | 4 examples passed on `demo-h1`; `C1`, carried by `M1` | None in fixture scope |
| Integration Tests | Device storage behavior assessed | 3 examples passed on `demo-h1`; `C1`, carried by `M1` | None in fixture scope |
| End-To-End Tests | Restoration journey assessed | 1 example passed on `demo-h1`; `C1`, carried by `M1` | None in fixture scope |

## Loop Report

Snapshot: `demo-h2`, 2026-01-10 10:00 UTC. Coverage: run `sample-c`, records
`C01–C14`; prior history reconciled. All completed specialist responses below
reviewed `demo-h1`. Carry-forward `M1` preserves them for `demo-h2`; it is not
new feedback and adds no rounds. Counts are activity, not approval.

The PR was already jointly approved at `demo-h1`; PR Monitor completed its
publication/approval assignment before PR Integrator started. The base advance
was detected during PR Integrator’s final refresh; the mechanical sync and
coordinator assessment returned it to final CI/merge watch. This is a later
report refresh, not the initial PR adoption.

| Specialist Reviewer | Review Rounds |
| --- | --- |
| Compose | 1 |
| State And Concurrency | 1 |
| Data | 0 |
| Architecture | 0 |
| Security | 1 |
| Local Test | 1 |
| Connected Test | 1 |

**Approximate elapsed time**

All endpoints below are UTC on 2026-01-10. Data and Architecture were unselected.
Intervals remain attributed to their original candidate and are not summed.

- Planner `C01`, `demo-h1`: 09:00–09:05; approximately 5 minutes.
- Implementer `C02`, `demo-h1`: 09:05–09:20; approximately 15 minutes.
- Compose `C03`, `demo-h1`: 09:20–09:24; approximately 4 minutes.
- State And Concurrency `C04`, `demo-h1`: 09:20–09:25; approximately 5 minutes.
- Security `C05`, failed attempt on `demo-h1`: 09:21–09:22; approximately 1 minute through failure, no feedback.
- Security `C05`, recovered attempt on `demo-h1`: 09:24–09:28; approximately 4 minutes through complete feedback. One completed round across both attempts.
- Local Test `C06`, `demo-h1`: 09:20–09:26; approximately 6 minutes.
- Connected Test `C07`, `demo-h1`: 09:20–09:27; approximately 7 minutes.
- Review Coordinator `C08`, `demo-h1`: 09:20–09:30; approximately 10 minutes.
- PR Monitor `C13`, `demo-h1`: 09:31–09:35; approximately 4 minutes through publication and joint approval.
- PR Integrator `C14`, original candidate `demo-h1`: started 09:36; in progress at snapshot, watching final CI/merge at `demo-h2` under carry-forward `M1`.
- Implementer follow-up `C09`, `demo-h2`: 09:45–09:48; approximately 3 minutes for mechanical synchronization, not a new specialist review.
- Review Coordinator follow-up `C10`, `demo-h2`: 09:49–09:51; approximately 2 minutes for the supplied applicability assessment, not specialist feedback.
- General Coordinator `C11`, current candidate `demo-h2`: started 08:59; in progress at snapshot. Earlier candidate events remain attributed to `demo-h1` in the covered records.
- PR Monitor report-refresh follow-up `C12`, `demo-h2`: started 09:52; in progress at snapshot.

### Exceptions

- Security's initial attempt was unavailable. Review Coordinator alerted General Coordinator immediately and recovered the same current request. Complete feedback later returned; no selected review is still missing. The failed attempt added no round.

## Related

The first PR supplies storage support. Eventual integration target: `main`.

## PR Stack

1. https://github.com/example/fictional-project/pull/10
2. https://github.com/example/fictional-project/pull/11 — **This PR**
