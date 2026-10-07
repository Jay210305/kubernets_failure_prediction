# Graph Report - Microservices_fault_preditcion  (2026-10-06)

## Corpus Check
- cluster-only mode — file stats not available

## Summary
- 15 nodes · 17 edges · 3 communities (0 shown, 3 thin omitted)
- Extraction: 100% EXTRACTED · 0% INFERRED · 0% AMBIGUOUS
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `32db139f`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- Community 1
- Community 2

## God Nodes (most connected - your core abstractions)
1. `extract_dataset()` - 5 edges
2. `build_spatiotemporal_tensor()` - 4 edges
3. `query_prometheus_range()` - 3 edges
4. `Ejecuta una consulta al endpoint query_range de Prometheus.` - 1 edges
5. `Extrae las series temporales de todos los servicios y métricas, alineando…` - 1 edges
6. `Convierte el DataFrame (T, 55) en un tensor 3D de ventanas deslizantes con…` - 1 edges

## Surprising Connections (you probably didn't know these)
- `extract_dataset()` --references--> `DataFrame`  [EXTRACTED]
  extract_telemetry.py →   _Bridges community 1 → community 2_

## Import Cycles
- None detected.

## Communities (3 total, 3 thin omitted)

## Knowledge Gaps
- **3 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `build_spatiotemporal_tensor()` connect `Community 2` to `Community 0`?**
  _High betweenness centrality (0.308) - this node is a cross-community bridge._
- **Why does `extract_dataset()` connect `Community 1` to `Community 0`, `Community 2`?**
  _High betweenness centrality (0.220) - this node is a cross-community bridge._
- **Why does `query_prometheus_range()` connect `Community 1` to `Community 0`?**
  _High betweenness centrality (0.143) - this node is a cross-community bridge._