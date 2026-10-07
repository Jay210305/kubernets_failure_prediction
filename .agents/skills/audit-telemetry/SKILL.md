---
name: audit-telemetry
description: Use when checking Prometheus extraction, baseline capture quality, feature schema, timestamps, or training-data readiness in this project.
---

# Audit telemetry before modeling

Read `docs/BASELINE_AUDIT.md`, then inspect the named capture and `google_boutique/extract_telemetry.py`. Report row count, time span and spacing, service/feature columns, missingness before any fill when available, nonzero/variance counts, impossible values, and CSV/Parquet consistency if both exist.

For a live capture, verify Prometheus reachability, actual label names, at least one sample per expected query, timestamp alignment, and workload/fault context. Distinguish measured zero from missing query results; never convert the latter into a healthy observation. Record query failures per service and metric. Do not start a cluster or inject faults solely to audit a local file.

Produce a concise report with evidence paths, counts, pass/fail readiness, suspected causes labeled as hypotheses, and exact next checks. Update `docs/BASELINE_AUDIT.md` only after remeasuring; keep earlier findings dated.
