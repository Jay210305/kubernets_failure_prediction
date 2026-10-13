---
kind: action-todo
status: planned
---

# Fit training-only preprocessing

**Task:** [Freeze splits and preprocessing](../CONTEXT.md)

**Inspect:** Train/validation/test windows and feature schema.

## Exact work

- [ ] Fit missingness handling, imputation, scaling, and any feature selection on training only; save parameters and transform validation/test without refitting; count examples and positives per split/service.

**Write:** Preprocessing config and split summary.

**Complete when:** Held-out distributions cannot influence fitted transformations.

Record source paths, PDF pages, or run IDs beside findings. Leave unavailable facts explicitly unknown; this file is a plan until the stated output is reviewed.
