---
kind: action-todo
status: work-complete-awaiting-review
---

# Specify tensor and comparison

**Task:** [Define features and topology](../CONTEXT.md)

**Inspect:** Feature schema, topology choice, and current extractor's 11×5×36 intended shape.

## Exact work

- [x] Write time/row/feature axis order, padding/missingness policy, output service order, and a spatial-order check or order-insensitive comparator; update dimensions if verified service or feature set differs.

**Write:** Tensor contract and layout comparison in docs/EXPERIMENT_PROTOCOL.md.

**Complete when:** A second implementer can reconstruct the input without guessing axis or service order.

Draft outputs and source limitations are recorded below. Checked boxes record documentation work, not human acceptance or verified runtime measurements.

## Draft execution evidence

**Prepared:** 2026-10-10. [Experiment protocol](../../../../EXPERIMENT_PROTOCOL.md), section 5, and [scope](../../../../PROJECT_SCOPE.md). See the protocol action record for exact source assumptions, proposed settings and prerequisites. **Human review:** pending.
