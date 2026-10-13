---
kind: literature-map
status: evidence-review-awaiting-review
checked: 2026-10-10
---

# Prior work navigation

The [corpus index](CORPUS_INDEX.md) owns the 81-PDF inventory, 75 distinct hashes, 74 provisional study identities, first-pass screening, edition reconciliation and ranked queue. Original sources are preserved. The local corpus is a starting collection, not a completed systematic search.

Phase 01 and Phase 02 execution outputs are prepared, with human review pending. The [thematic synthesis](LITERATURE_SYNTHESIS.md) owns cross-paper comparison, seven protocol themes, the bounded gap, unresolved Phase 03 choices and [execution/review handoff](LITERATURE_SYNTHESIS.md#execution-checks-and-review-handoff). Detailed claims, physical PDF pages, source hashes and unknowns belong to the notes below.

## Reviewed studies

All twenty queued works have a note: five full decision reviews and fifteen focused methods/evaluation reviews. “Full” covers target, method, evaluation and limits; focused notes record fields not extracted. No paper's experiment was reproduced here. Unlike targets and datasets are not a performance ranking.

| Queue rank | Study / evidence note | Review depth | Decision route |
| ---: | --- | --- | --- |
| 1 | [InstantOps: A Joint Approach to System Failure Prediction and Root Cause Identification in Microservices Cloud-Native Applications](papers/W033-instantops.md) | Full decision review | System forecast versus service event; multimodal graph/GRU comparison |
| 2 | [Online Failure Prediction for Microservice Architectures](papers/W054-online-failure-prediction.md) | Full decision review | Shared-host context, forecast settings and warm-up |
| 3 | [PodFailPred: A New Open-Source Dataset to Train AI Models on Predicting Pod Failures in Kubernetes](papers/W057-podfailpred.md) | Full decision review | Pod provenance; unresolved future label and result counts |
| 4 | [Latent error prediction and fault localization for microservice applications by learning from system trace logs](papers/W040-latent-error-prediction.md) | Full decision review | Completed-trace error versus advance event |
| 5 | [Quantifying Data Leakage in Failure Prediction Tasks](papers/W058-data-leakage.md) | Full decision review | Chronology/groups and leakage transfer limits |
| 6 | [Explainable GNN-Based Approach to Fault Forecasting in Cloud Service Debugging](papers/W029-explainable-gnn.md) | Focused methods/evaluation | Simulated topology/probability versus observed telemetry |
| 7 | [ServiceAnomaly: An anomaly detection approach in microservices using distributed traces and profiling metrics](papers/W064-serviceanomaly.md) | Focused methods/evaluation | Trace-derived graph and path coverage |
| 8 | [MicroFI: Non-Intrusive and Prioritized Request-Level Fault Injection for Microservice Applications](papers/W045-microfi.md) | Focused methods/evaluation | Request recipes and injection blast radius |
| 9 | [A failure analysis framework to provide pure anomalous data using multi-source data of fault-sensitive microservices](papers/W001-fault-sensitive-framework.md) | Focused methods/evaluation | Feature/service selection and graph transformations |
| 10 | [Can We Trust Auto-Mitigation? Improving Cloud Failure Prediction with Uncertain Positive Learning](papers/W019-uncertain-positive-learning.md) | Focused methods/evaluation | Mitigation-censored labels |
| 11 | [Performance prediction and resource adaptive adjustment for cloud-native microservices](papers/W056-cnn-performance.md) | Focused methods/evaluation | CNN image layout and resource-performance boundary |
| 12 | [TraceWeaver: Distributed Request Tracing for Microservices Without Application Modification](papers/W070-traceweaver.md) | Focused methods/evaluation | Trace reconstruction prerequisites |
| 13 | [Classification of Anomalies in Microservices Using an XGBoost-Based Approach With Data Balancing and Hyperparameter Tuning](papers/W022-xgboost-anomalies.md) | Focused methods/evaluation | Tabular baseline; preprocessing/split ambiguity |
| 14 | [Multilayered Fault Detection and Localization With Transformer for Microservice Systems](papers/W049-multilayer-transformer.md) | Focused methods/evaluation | Observation/target layers and training scaling |
| 15 | [Resilient Microservice Applications, by Design, and without the Chaos](papers/W059-resilient-microservices.md) | Focused methods/evaluation | Controlled RPC tests and fault provenance |
| 16 | [To Split or to Merge? Exploring Multi-modal Data Flexibly for Failure Classification in Microservices](papers/W068-agilemfc.md) | Focused methods/evaluation | Failure taxonomy and modality-dependent classification |
| 17 | [Investigating Performance Overhead of Distributed Tracing in Microservices and Serverless Systems](papers/W036-tracing-overhead.md) | Focused methods/evaluation | Trace overhead and capture conditions |
| 18 | [A systematic mapping study on observability of microservices-based applications: fundamentals, classifications, and challenges](papers/W005-observability-mapping.md) | Focused methods/evaluation | Modality/tool taxonomy and heterogeneous datasets |
| 19 | [Observability in Microservices: An In-Depth Exploration of Frameworks, Challenges, and Deployment Paradigms](papers/W053-observability-frameworks.md) | Focused methods/evaluation | Deployment/coverage limitations |
| 20 | [A Survey of AIOps Methods for Failure Management](papers/W004-aiops-taxonomy.md) | Focused methods/evaluation | Prediction/detection/diagnosis/mitigation timing |

## Follow-up reading order

The [original ranked queue](CORPUS_INDEX.md#ranked-reading-queue) is now covered by the notes above at its stated depth. It remains the provenance of selection, rather than a list of unfinished reviews. Use the [question-to-paper map](CORPUS_INDEX.md#papers-mapped-to-protocol-questions), [synthesis](LITERATURE_SYNTHESIS.md) and [paper-folder contract](papers/CONTEXT.md) to reopen evidence for a particular decision.

Next is the [Phase 03 protocol](project-phases/03-protocol/CONTEXT.md), after the required human evidence review. Additional external search may address the documented service-forecast/operational-metric coverage gap; no claim of comprehensive novelty follows from these twenty local reviews. [PROJECT_SCOPE.md](PROJECT_SCOPE.md) keeps CNN–LSTM primary and owns the proposed event/timing/evaluation boundary.
