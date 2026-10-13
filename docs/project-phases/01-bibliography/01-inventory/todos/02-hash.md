---
kind: action-todo
status: work-complete-awaiting-review
checked: 2026-10-10
---

# Find exact duplicates

**Task:** [Inventory the corpus](../CONTEXT.md)

**Inspect:** The PDF inventory and current files in Bibliografia_Micro/.

## Exact work

- [x] Compute SHA-256 for every PDF; group identical hashes; compare counts with the earlier 81 PDF and 75 distinct hash audit; explain count changes if the corpus has changed.

**Write:** Hash and exact-duplicate columns in docs/CORPUS_INDEX.md.

**Complete when:** Each duplicate group is based on matching bytes, not a similar title.

Record source paths, PDF pages, or run IDs beside findings. Leave unavailable facts explicitly unknown; the checkbox records performed work; human acceptance remains pending.

**Execution evidence (2026-10-10):** [Canonical output](../../../../CORPUS_INDEX.md#exact-duplicate-groups) and [source checks and review handoff](../../../../CORPUS_INDEX.md#execution-checks-and-review-handoff). Human review is pending.
