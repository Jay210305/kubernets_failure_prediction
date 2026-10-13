---
kind: research-scope
status: draft-for-review
checked: 2026-10-10
---

# Research scope and boundaries

## Aim

Build and evaluate the user-selected **CNN–LSTM** to forecast sustained request failure of a named Online Boutique service early enough for manual investigation/preparation for mitigation. The initial environment is a local kind cluster; deployment and data readiness remain unverified.

## Proposed prediction contract

The user selected **sustained request failure** on 2026-10-10. [EXPERIMENT_PROTOCOL.md](EXPERIMENT_PROTOCOL.md) owns the exact event oracle, numerical timing, labels, eligibility, schemas and evaluation rules. Its settings are proposed for human review, with a verified service-level signal still missing.

- **Unit:** a named logical application service at decision time `t`, with context from the extractor's eleven named services/storage rows. Ten proposed application targets; storage is context only. Registry/operations require deployment verification.
- **Event:** repeated failure of a representative valid request routed to the logical service across replicas, confirmed by persistence. Failure onset, confirmation, recovery and root injection are distinct timestamps; unknown observer coverage is not a healthy outcome.
- **Input:** causal resource telemetry and observed/missing flags, available by `t`. The primary draft uses four features (CPU, memory, receive/transmit rates); HTTP errors are an unverified optional extension. Labels/observer outcomes, future status and injection metadata are excluded as input.
- **Timing:** proposed five-second decisions, 36 observation bins, 30-second minimum lead and 120-second horizon. The protocol defines exact endpoint alignment, strict interval `(t+lead_min,t+horizon]`, rate lookback and future label confirmation support.
- **Output:** one risk score per target service and a validation-selected alert threshold. Probability calibration must be assessed; a sigmoid alone does not establish calibrated risk. Actual issued-alert time determines lead.
- **Action:** manual investigation/preparation for mitigation. Usefulness of the proposed minimum warning interval is an assumption to review, not a measured operator response time.

## Architecture and comparison boundary

The proposed value/mask tensors are `(window,36 time bins,11 context rows,4 features)` each. CNN input combines two channels; output has ten target scores. This is a **new proposed schema**, not the current extractor's implemented 11×5 reshape. A future implementation must explicitly select/map columns and cannot directly train on the unchanged 55-column all-zero capture.

Registry-order adjacency is an explicit, unverified CNN assumption. The protocol versions the order, specifies permutation sensitivity and temporal/tabular comparisons, and routes to trace/configuration evidence for future graph verification. CNN–LSTM remains primary; a baseline or graph model cannot replace it without a documented decision.

## Evaluation boundary

Chronological train/validation/test partitions assign complete incident groups before window construction. The protocol includes raw rate lookbacks, future event confirmation and episode protection in its support/purge rules. Training alone fits imputation, scaling and hyperparameters; validation fits calibration/alert thresholds; test is held out until freeze.

Operational threshold, tabular-window and temporal-only baselines share eligibility, inputs, future labels, incident groups, seeds and alert rules with CNN–LSTM. Report per-service sample precision/recall/AP, episode alert precision/recall, healthy exposure and false alerts/hour, first-alert lead, coverage, missed events and block-based uncertainty. Undefined metrics and insufficient independent events remain explicit. No forecast performance has been measured.

## Current exclusions and gates

No production deployment, automatic mitigation, model training or cluster experiment is authorized as a side effect of these documents. Current detection, localization, hardware/pod failures and resource-regression literature remain separate tasks. Observer-operation failure does not claim a root cause or complete customer-request coverage. This local bibliography is a starting corpus, not a completed systematic search.

The [baseline audit](BASELINE_AUDIT.md) still fails. Human evidence/protocol acceptance, verified oracle/telemetry/topology, and independent labeled episodes remain prerequisites in [RESEARCH_PLAN.md](RESEARCH_PLAN.md). This phase prepares a concrete protocol; it does not pass those gates.
