---
kind: action-todo
status: planned
---

# Purge overlap and build windows

**Task:** [Freeze splits and preprocessing](../CONTEXT.md)

**Inspect:** Split manifest, history length, lead_min, and horizon.

## Exact work

- [ ] Calculate boundary exclusion width from history plus forecast interval; remove decision points that would share information across splits; create windows only after assignment.

**Write:** Purge rules and window IDs in split manifest.

**Complete when:** Near-identical windows or forecast labels do not straddle splits.

Record source paths, PDF pages, or run IDs beside findings. Leave unavailable facts explicitly unknown; this file is a plan until the stated output is reviewed.
