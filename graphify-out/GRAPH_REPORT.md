# Graph Report - google_boutique  (2026-10-10)

## Corpus Check
- 3 files · ~1,914 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 35 nodes · 72 edges · 7 communities (2 shown, 5 thin omitted)
- Extraction: 100% EXTRACTED · 0% INFERRED · 0% AMBIGUOUS
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- Community 0
- Community 1
- Community 3
- Community 4
- Community 5
- Community 6

## God Nodes (most connected - your core abstractions)
1. `capture()` - 13 edges
2. `main()` - 6 edges
3. `api_record()` - 5 edges
4. `range_values()` - 5 edges
5. `build_spatiotemporal_tensor()` - 5 edges
6. `quality_report()` - 5 edges
7. `utc()` - 4 edges
8. `source_selectors()` - 4 edges
9. `query_prometheus_range()` - 4 edges
10. `extract_dataset()` - 4 edges

## Surprising Connections (you probably didn't know these)
- `capture()` --calls--> `utc()`  [EXTRACTED]
  telemetry_capture.py → telemetry_capture.py  _Bridges community 4 → community 3_
- `utc()` --calls--> `pandas`  [EXTRACTED]
  telemetry_capture.py →   _Bridges community 4 → community 1_
- `source_selectors()` --calls--> `json`  [EXTRACTED]
  telemetry_capture.py →   _Bridges community 3 → community 6_
- `capture()` --calls--> `api_record()`  [EXTRACTED]
  telemetry_capture.py → telemetry_capture.py  _Bridges community 0 → community 3_
- `capture()` --calls--> `range_values()`  [EXTRACTED]
  telemetry_capture.py → telemetry_capture.py  _Bridges community 5 → community 3_

## Import Cycles
- None detected.

## Communities (7 total, 5 thin omitted)

### Community 0 - "Community 0"
Cohesion: 0.22
Nodes (3): api_record(), extract_dataset(), query_prometheus_range()

### Community 3 - "Community 3"
Cohesion: 0.50
Nodes (3): capture(), metric_queries(), source_selectors()

## Knowledge Gaps
- **5 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `capture()` connect `Community 3` to `Community 0`, `Community 1`, `Community 2`, `Community 4`, `Community 5`, `Community 6`?**
  _High betweenness centrality (0.094) - this node is a cross-community bridge._
- **Why does `build_spatiotemporal_tensor()` connect `Community 1` to `Community 0`, `Community 2`?**
  _High betweenness centrality (0.065) - this node is a cross-community bridge._
- **Why does `api_record()` connect `Community 0` to `Community 2`, `Community 3`?**
  _High betweenness centrality (0.063) - this node is a cross-community bridge._

Scope: three telemetry Python modules only. Papers, raw captures, event labels and deployed topology are excluded. Source files have local uncommitted changes; compare telemetry-source-hashes.json, not commit identity alone, for freshness.
