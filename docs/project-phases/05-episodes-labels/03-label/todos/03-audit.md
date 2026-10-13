---
kind: action-todo
status: planned
---

# Audit labels and class distribution

**Task:** [Generate forecast labels](../CONTEXT.md)

**Inspect:** Labeled dataset, episode log, and protocol.

## Exact work

- [ ] Manually recompute samples before, inside, and after the forecast interval; count positives, negatives, excluded times, and episodes per service; detect overlap or contradictory labels.

**Write:** Label audit in dataset manifest.

**Complete when:** Counts and spot checks support the labels before split/model work.

Record source paths, PDF pages, or run IDs beside findings. Leave unavailable facts explicitly unknown; this file is a plan until the stated output is reviewed.
