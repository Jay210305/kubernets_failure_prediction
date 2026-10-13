---
kind: task-contract
status: planned
---

# Freeze splits and preprocessing

**Purpose:** Freeze splits and preprocessing within [Baseline evaluation](../CONTEXT.md).

**Inputs:** docs/EXPERIMENT_PROTOCOL.md, labeled dataset, docs/RESEARCH_PLAN.md.

**Expected output:** versioned split manifest and preprocessing configuration.

**Work:** Follow the [to-do index](TODO.md), then its three linked action files. Each action file names evidence, output, and a completion check.

**Human check:** No episode or near-identical window crosses a split; held-out test remains untouched.
