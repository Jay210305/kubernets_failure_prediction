---
kind: implementation-plan
status: work-complete-awaiting-review
checked: 2026-10-10
---

# Phase 04 implementation plan

**Goal:** collect auditable telemetry from the existing local cluster, with real zeros distinguished from unavailable measurements.

**Spec:** the nine action files under this phase, [baseline audit](../../BASELINE_AUDIT.md), and the proposed [protocol](../../EXPERIMENT_PROTOCOL.md). Scope is measurement readiness; fault injection, label-oracle implementation and model training belong to separate work.

**Files:** repair `google_boutique/extract_telemetry.py` for UTC grids, explicit schema, raw response/provenance preservation and safe CLI capture; add `google_boutique/telemetry_quality.py` for coverage/value/parity reports; add a manifest template and dated query/quality reports. Update folder contracts, phase status, README and ICM/code-graph routes.

## Steps

- [x] Inspect the existing endpoint, workload, actual metric labels and scrape configuration; record failures/configuration separately from observations.
- [x] Implement configurable endpoint/namespace, missing-preserving extraction, explicit-column tensors, raw query responses, source timestamps and arrival metadata, unique capture directories and hashes.
- [x] Implement capture quality reporting with per-series coverage/nonzero/variance, source freshness, query failures, CSV/Parquet parity and a conservative readiness verdict.
- [x] Capture an uninterrupted interval of the existing workload; preserve deployment/pod/workload evidence and old baseline hashes.
- [x] Write evidence-backed reports, update action status honestly, and refresh the code graph or explicitly flag it stale if its installed runtime is unavailable.

No test suite is added/run without a user request, per the session developer instruction. Necessary live measurement/audit is the requested Phase 04 work. Syntax/import checks and saved-artifact integrity checks are distinguished from regression tests. No commits, dependency installs or cluster deployment changes are part of this plan.
