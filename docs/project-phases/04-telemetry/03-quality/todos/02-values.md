---
kind: action-todo
status: work-complete-awaiting-review
---

# Check values and file parity

**Task:** [Judge data readiness](../CONTEXT.md)

**Inspect:** Captured CSV/Parquet, raw query responses, and expected metric units.

## Exact work

- [x] Count nonzero and varying samples, detect all-zero or constant series, compare CSV and Parquet timestamps/values after precision normalization, and explain discrepancies.

**Write:** Value and parity section in quality report.

**Complete when:** No absent series is accepted as a measured healthy zero.

Execution evidence is recorded below. Checked boxes mean work performed; human acceptance and measurement readiness are separate gates.

## Execution evidence

**Performed:** 2026-10-10. [Dated query/capture/quality audit](../../../../telemetry/2026-10-10-phase04.md) records the exact pair-level measurements and canonical manifest, with raw responses, masks, provenance and source hashes. All nine action outputs are prepared. **Readiness:** failed source freshness under the proposed protocol. **Human check:** pending; no labels/training are enabled by checked boxes.
