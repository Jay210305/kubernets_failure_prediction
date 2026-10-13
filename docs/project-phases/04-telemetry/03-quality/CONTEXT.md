---
kind: task-contract
status: work-complete-awaiting-review
---

# Judge data readiness

**Purpose:** Judge data readiness within [Telemetry readiness](../CONTEXT.md).

**Inputs:** docs/BASELINE_AUDIT.md, .agents/skills/audit-telemetry/SKILL.md, google_boutique/extract_telemetry.py.

**Expected output:** dated data-quality report and updated docs/BASELINE_AUDIT.md verdict.

**Work:** Follow the [to-do index](TODO.md), then its three linked action files. Each action file names evidence, output, and a completion check.

**Human check:** A human accepts the quality report before episodes or model work begins.

## Execution evidence

**Performed:** 2026-10-10. [Dated query/capture/quality audit](../../../telemetry/2026-10-10-phase04.md) records the exact pair-level measurements and canonical manifest, with raw responses, masks, provenance and source hashes. All nine action outputs are prepared. **Readiness:** failed source freshness under the proposed protocol. **Human check:** pending; no labels/training are enabled by checked boxes.
