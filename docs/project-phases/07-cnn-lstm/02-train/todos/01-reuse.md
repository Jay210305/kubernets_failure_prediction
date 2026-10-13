---
kind: action-todo
status: planned
---

# Load frozen data and transforms

**Task:** [Train and select the model](../CONTEXT.md)

**Inspect:** Baseline split manifest, labeled dataset, and training-fitted preprocessing.

## Exact work

- [ ] Verify sample IDs, feature order, label version, topology version, and train/validation/test partitions match baseline runs; halt on mismatch.

**Write:** Input consistency record in CNN–LSTM run config.

**Complete when:** Primary and baseline runs use the same eligible examples.

Record source paths, PDF pages, or run IDs beside findings. Leave unavailable facts explicitly unknown; this file is a plan until the stated output is reviewed.
