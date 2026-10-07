---
kind: research-scope
status: draft-for-review
---

# Research scope and boundaries

## Aim

Build and evaluate a model that uses recent microservice telemetry and service relationships to forecast a defined failure of a particular service early enough for an operator to respond. Google Online Boutique on a local kind cluster is the initial experimental environment. The proposed primary model is a CNN–LSTM: the CNN processes a deliberately defined service/feature layout; the LSTM processes successive observations in a fixed history window.

## Prediction contract to finalize before training

- **Unit:** one named service at one decision time, with context from other services.
- **Input:** observations available no later than decision time `t`; declare sampling interval, history length, feature set, service ordering, and topology version.
- **Target:** a specified operational failure event in a future interval `(t + lead_min, t + horizon]`. Candidate events include service unavailable, sustained elevated 5xx rate, or a Kubernetes failure state. Each is a separate label definition; do not combine them silently.
- **Output:** a calibrated risk score per service and an alert threshold chosen on validation data. Record when an alert first fires and when the event begins.
- **Action:** a DevOps decision such as capacity increase or mitigation. The first research deliverable is a forecast evaluation, not an automated remediation system.

`lead_min`, `horizon`, event thresholds, and acceptable false alert rate are open research decisions. They must be fixed in an experiment protocol before looking at the test results.

## Architecture boundary

The current extractor's intended array is `(time, 11 services, 5 metrics)`; a 36-step window at five-second sampling covers three minutes. A CNN on this grid has a **spatial assumption**: adjacent rows are treated as related. Alphabetical or arbitrary service order does not represent call topology. Before training, record a stable layout based on a documented service dependency graph or justify a grid design and compare against an order-insensitive or graph-aware baseline. The LSTM sees only past windows at inference time.

## Evaluation boundary

Use a simple operational baseline (for example, current metric threshold), a tabular time-window baseline, and a temporal-only model before attributing gain to the CNN–LSTM. Split by chronology and fault episode, with overlap/purge around boundaries so near-identical windows cannot cross splits. Fit scaling and imputation on training data only. Report per-service precision, recall, PR-AUC when defined, false alerts per hour, lead time, and uncertainty across fault episodes; raw accuracy alone is insufficient for rare failures. Keep root-cause localization and anomaly detection as related literature, not equivalent success criteria.

## Current exclusions

No production deployment, automatic capacity changes, or causal claim that a forecast identifies the root cause. The current bibliography is a starting corpus rather than a completed systematic review. The current baseline files are not usable training data; see [BASELINE_AUDIT.md](BASELINE_AUDIT.md).
