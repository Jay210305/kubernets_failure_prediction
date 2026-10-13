---
kind: action-todo
status: planned
---

# Train with recorded settings

**Task:** [Train and select the model](../CONTEXT.md)

**Inspect:** Architecture config and allowed training/validation data.

## Exact work

- [ ] Record seeds, optimizer, learning rate, batch size, class handling, search space/budget, checkpoint rule, stopping rule, and runtime; save checkpoint and predictions.

**Write:** Dated training log, config, checkpoint, and hashes.

**Complete when:** A rerun can recover the selected model without test-set choices.

Record source paths, PDF pages, or run IDs beside findings. Leave unavailable facts explicitly unknown; this file is a plan until the stated output is reviewed.
