---
kind: literature-map
status: initial-screen
checked: 2026-10-06
---

# Initial map of prior work

`Bibliografia_Micro/` contains **81 PDFs and 75 distinct SHA-256 file hashes**. This is a focused screen of opening pages and abstracts from 11 selected works, not a full review of every paper or its methods/results. Similar names may be editions rather than byte-identical copies; five exact-hash duplicate groups account for six extra files. Keep original filenames until citations and editions are reconciled.

## Closest to the proposed task

| Paper in `Bibliografia_Micro/` | What its opening pages establish | Use for this project |
| --- | --- | --- |
| [InstantOps](<../Bibliografia_Micro/InstantOps_ A Joint Approach to System Failure Prediction and Root Cause Identification in Microservices Cloud-Native.pdf>) | Joint failure prediction and root-cause analysis using logs, metrics, traces; GNN for spatial structure and GRU for time. | Closest architecture comparison; distinguish its joint objective and modalities from a metrics-first CNN–LSTM. |
| [Online Failure Prediction for Microservice Architectures](<../Bibliografia_Micro/Online Failure Prediction for Microservice Architectures.pdf>) | Studies how shared-host resource contention affects microservices and online prediction from container metrics. | Motivation for host/pod context and fault mechanisms; inspect full evaluation before citing performance. |
| [PodFailPred](<../Bibliografia_Micro/PodFailPred_ A New Open-Source Dataset to Train AI Models on Predicting Pod Failures in Kubernetes.pdf>) | Chaos-generated Kubernetes pod-failure dataset; abstract reports 15 injected failure types, 21,374 entries, 38 metrics. | Dataset and labeling design; pod failure is not automatically service-level failure. |
| [Explainable GNN fault forecasting](<../Bibliografia_Micro/Explainable_GNN-Based_Approach_to_Fault_Forecasting_in_Cloud_Service_Debugging.pdf>) | Graph-based fault-probability forecasting and explanation across service-mesh structures; abstract describes simulated failure behavior. | Alternative spatial representation and interpretability comparison; check whether its target matches an observed lead-time forecast. |

## Data, observability, and validation

| Paper | Opening-page finding | Research question it informs |
| --- | --- | --- |
| [Quantifying Data Leakage in Failure Prediction Tasks](<../Bibliografia_Micro/Quantifying Data Leakage in Failure Prediction Tasks.pdf>) | Naive train/test splits can inflate failure-prediction results; paper studies leakage measures and split techniques in HDD prediction. | How to prevent near-identical windows or related episodes crossing splits. Domain differs, principle transfers. |
| [ServiceAnomaly](<../Bibliografia_Micro/ServiceAnomaly_ An anomaly detection approach in microservices using distributed traces and profiling metrics.pdf>) | Builds an annotated service graph from traces and profiling metrics for anomaly detection. | How to source a verified call graph; its outcome is detection, not advance failure prediction. |
| [Failure analysis using fault-sensitive microservices](<../Bibliografia_Micro/A failure analysis framework to provide pure anomalous data using multi-source data of fault-sensitive microservices.pdf>) | Selects fault-sensitive services/features and aims to reduce mixed normal/anomalous evidence. | Whether all 55 features are necessary and how to audit feature sensitivity. |
| [MicroFI](<../Bibliografia_Micro/MicroFI_Non-Intrusive_and_Prioritized_Request-Level_Fault_Injection_for_Microservice_Applications.pdf>) | Request-level, non-intrusive fault injection with prioritization. | Design controlled fault episodes and record blast radius; do not infer it generates this project's labels automatically. |

## Adjacent tasks and model baselines

| Paper | Opening-page finding | Boundary |
| --- | --- | --- |
| [A Survey of AIOps Methods for Failure Management](<../Bibliografia_Micro/A Survey of AIOps Methods for Failure Management.pdf>) | Organizes failure-management research by intervention window and target problem. | Taxonomy for separating prediction, detection, localization, and mitigation. |
| [XGBoost anomaly classification](<../Bibliografia_Micro/Classification_of_Anomalies_in_Microservices_Using_an_XGBoost-Based_Approach_With_Data_Balancing_and_Hyperparameter_Tuning.pdf>) | Uses balancing and hyperparameter tuning for anomaly classification on TraceRCA. | A tabular-model reference, but its reported classification scores are not a forecast benchmark. |
| [Multilayered Transformer detection/localization](<../Bibliografia_Micro/Multilayered_Fault_Detection_and_Localization_With_Transformer_for_Microservice_Systems.pdf>) | Uses container, service, host, and network layers to detect/localize faults. | Reminder to define observation layer and target layer separately. |

## Follow-up reading order

1. Read **InstantOps**, **Online Failure Prediction**, and **PodFailPred** in full for target/lead-time definitions, data collection, and evaluation splits.
2. Read **Quantifying Data Leakage** before designing sliding-window splits.
3. Read **ServiceAnomaly** and the GNN forecasting paper before fixing the CNN's service layout.
4. Then screen the remaining corpus by actual research task and modality; create one note per relevant work using [the template](_templates/paper-note.md). Record page numbers for claims and keep reported metrics tied to each paper's dataset and task.
