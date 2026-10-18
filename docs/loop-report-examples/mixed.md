<!-- Fictional rendering fixture. All records and results are invented. -->

## Summary

Preserve a draft when a background refresh finishes. An interrupted specialist
request was resumed, and a separate selected review is still missing.

## Details

This illustrative takeover reconciles known prior Loop records with the new run.

## Verification

- Tested revision: fictional `demo-h2`.
- Local scenario `V1` — the refresh preserves the draft.
- Readiness — blocked on the still-missing selected Security review. Activity counts do not grant approval.

## Loop Report

Snapshot: `demo-h2`, 2026-01-10 09:40 UTC. Coverage: retained run `sample-a`
records `A01–A10` and resumed run `sample-b` records `B01–B14` for the same
fictional issue/PR. Earlier Loop history is unavailable: **partial history**;
counts below apply only to these records, not the entire issue lifetime.
Historical non-Loop reviews are excluded.

| Specialist Reviewer | Review Rounds |
| --- | --- |
| Compose | 2 |
| State And Concurrency | 1 |
| Data | 0 |
| Architecture | 1 |
| Security | 0 |
| Local Test | 1 |
| Connected Test | 0 |

Within this coverage, Compose request `C1` returned no findings for `demo-h1`;
`C2` returned an explicit requested delta/no-impact response for `demo-h2`.
State And Concurrency request `S1` returned complete feedback for `demo-h2`
after interruption/resumption: one round. Re-delivering `C2`'s result changes
nothing. Architecture request `A1` is retained from the earlier run, reviewed
`demo-h1`; it is not relabeled as a new `demo-h2` response. Local Test request
`L1` returned feedback for `demo-h2`. Data and Connected Test were unselected;
Security request `Q1` failed without feedback and remains missing. A retry,
partial response, tool call, advice attempt and an unreviewed intermediate commit
`demo-interim` each add no round.

**Approximate elapsed time**

All endpoints below are UTC on 2026-01-10. The report preserves each assignment's
candidate; parallel intervals overlap and are not totaled.

- General Coordinator `B01`, `demo-h2`: started 08:59; in progress at snapshot.
- Planner `B02`, `demo-h1`: 09:00–09:05; approximately 5 minutes.
- Implementer `B03`, `demo-h1`: 09:05–09:20; approximately 15 minutes, including tool waits.
- Implementer resumed `B04`, `demo-h2`: 09:30–09:37; approximately 7 minutes, separate from `B03`.
- Compose `C1`, `demo-h1`: 09:20–09:24; approximately 4 minutes.
- State And Concurrency `S1`, first attempt on `demo-h2`: start 09:21, interrupted checkpoint 09:23; approximately 2 minutes observed, **partial**, no result endpoint.
- State And Concurrency `S1`, resumed attempt on `demo-h2`: 09:26–09:31; approximately 5 minutes through returned feedback. The request counts once.
- Architecture `A1`, `demo-h1`: returned result retained; start timestamp unavailable, elapsed time **unavailable**.
- Security `Q1`, `demo-h2`: 09:24–09:25 through failure; approximately 1 minute for the failed attempt, no review result.
- Review Coordinator `B10`, `demo-h2`: started 09:20; in progress at snapshot.
- Compose follow-up `C2`, `demo-h2`: 09:32–09:36; approximately 4 minutes.
- Local Test `L1`, `demo-h2`: 09:32–09:35; approximately 3 minutes, overlapping `C2`.
- PR Monitor `B14`, `demo-h2`: started 09:38; in progress at snapshot.

### Exceptions

- Advice was unavailable; none was received. The immediate alert went through General Coordinator; this note is not a substitute for that alert.
- Selected Security review `Q1` is still missing. Review Coordinator reported it through General Coordinator; merge remains blocked. It is not a recovered outage or substitute review.
