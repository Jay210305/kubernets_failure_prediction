---
kind: research-plan
status: proposed
---

# Research gates

| Gate | Output for human review | Exit condition |
| --- | --- | --- |
| 1. Question and evidence | Final event definitions, lead interval, paper notes | Target is measurable from available signals; related work is cited by task and method. |
| 2. Telemetry | Capture manifest and data quality report | Real values, expected coverage, timestamp alignment, and workload are demonstrated. |
| 3. Fault episodes | Injection/incident log and label specification | Multiple distinct episodes per target, onset times, and no ambiguous train/test overlap. |
| 4. Baselines | Threshold, tabular, and temporal results | Chronological/episode split and alert metrics are reproducible. |
| 5. CNN–LSTM | Architecture/configuration, topology ordering, evaluation report | Improvement and costs are measured against the same episodes and lead times. |

At each gate, save the exact input data/version, code revision, decision, and output in a dated run directory when experiments begin. If a gate fails, fix the measurement or question before moving to the next one. The current state is **Gate 2 failed: old all-zero telemetry and new source-freshness failures**, with Gate 1 awaiting human acceptance of the [proposed protocol](EXPERIMENT_PROTOCOL.md) and verified service request-outcome evidence. Numerical target/timing and evaluation rules are drafted, not frozen. Phase 03's event action remains open until its signal is verified; gates and experiment prerequisites are unchanged.

Phase 04 implementation and real workload measurement are recorded in [the dated telemetry audit](telemetry/2026-10-10-phase04.md). CSV/Parquet/mask/hash parity passes, but source cadence/freshness and retrospective availability still prevent causal model use. Human gate acceptance, service request oracle and independent fault episodes remain pending; labels/training are not enabled.
