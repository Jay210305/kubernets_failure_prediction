---
kind: literature-synthesis
status: work-complete-awaiting-review
checked: 2026-10-10
---

# Evidence review and project decisions

## Scope and reading depth

This Phase 02 output covers all **20 unique studies** in the [Phase 01 ranked queue](CORPUS_INDEX.md#ranked-reading-queue): five full decision reviews and fifteen focused reviews. “Full” covers target, data/method, evaluation and limits; it does not claim an exhaustive audit of references/appendices. Focused notes declare inspected physical PDF pages and fields left unknown/not extracted. The published GNN edition is the canonical source; its manuscript is not counted again. Source identity and hashes live in each [paper note](papers/CONTEXT.md).

This is a decision-focused review of the local corpus, not a completed systematic literature search. All numerical outcomes below are reported by the source papers, with **no experiments reproduced in this repository**. Project implications explicitly marked “transfer inference” require protocol choices or local validation. Human evidence acceptance remains pending.

## Cross-paper evidence matrix

The two tables share study IDs and together record target, lead, modality, label source, split, baseline and metric. Values remain tied to source task and dataset; row order follows the reading queue and is not a performance ranking. “Unknown” means the inspected PDF does not establish the fact; “not extracted” marks focused-review scope; “not applicable” marks a nonforecast task. Detailed sample/episode counts and threats belong to the linked notes. PDF links and page locators refer to the exact edition reviewed.

### Target and provenance

| Study / note | Target and layer | History / lead / horizon | Modality | Label or outcome provenance | Source pages |
| --- | --- | --- | --- | --- | --- |
| [W033](papers/W033-instantops.md) | System forecast + localization | Next one-minute bin; minimum lead/history unknown | Metrics/logs/traces/events | Crash/error SLA; definitions disagree | [PDF pp. 4–9](<../Bibliografia_Micro/InstantOps_%20A%20Joint%20Approach%20to%20System%20Failure%20Prediction%20and%20Root%20Cause%20Identification%20in%20Microservices%20Cloud-Native.pdf#page=4>) |
| [W054](papers/W054-online-failure-prediction.md) | Request/resource forecast | 5-minute CPU; 10-minute scenario; 60-point CPU history | Container/host CPU, workload, HTTP/latency | Non-200 requests; controlled contention | [PDF pp. 50–55,80–91](<../Bibliografia_Micro/Online%20Failure%20Prediction%20for%20Microservice%20Architectures.pdf#page=50>) |
| [W057](papers/W057-podfailpred.md) | Pod failure claim | History/sampling/positive horizon unknown | Metrics + current pod/events | Chaos Studio; exact label mapping unknown | [PDF pp. 2–5,8–9](<../Bibliografia_Micro/PodFailPred_%20A%20New%20Open-Source%20Dataset%20to%20Train%20AI%20Models%20on%20Predicting%20Pod%20Failures%20in%20Kubernetes.pdf#page=2>) |
| [W040](papers/W040-latent-error-prediction.md) | Captured-trace latent error + localization | Completed trace; no advance lead established | Trace execution/config/resource/response | Injected code/tests; four labeling conditions | [PDF pp. 3–10](<../Bibliografia_Micro/Latent%20error%20prediction%20and%20fault%20localization%20for%20microservice%20applications%20by%20learning%20from%20system%20trace%20logs.pdf#page=3>) |
| [W058](papers/W058-data-leakage.md) | HDD failure/RUL | Daily; critical≤7d, warning≤28d | SMART + drive serial/time | Backblaze failures | [PDF pp. 4–10](<../Bibliografia_Micro/Quantifying%20Data%20Leakage%20in%20Failure%20Prediction%20Tasks.pdf#page=4>) |
| [W029](papers/W029-explainable-gnn.md) | Simulated disruption-probability regression | Simulation T steps; no wall-clock forecast lead | Directed graph; leaf probabilities/retries | PRISM model-checking probabilities | [PDF pp. 6–13](<../Bibliografia_Micro/Explainable_GNN-Based_Approach_to_Fault_Forecasting_in_Cloud_Service_Debugging%20%281%29.pdf#page=6>) |
| [W064](papers/W064-serviceanomaly.md) | Current service/path anomaly detection | Normal reference + observed trace; no future lead | Trace graph + six profiling metrics | Host/service fault scenarios | [PDF pp. 4–14](<../Bibliografia_Micro/ServiceAnomaly_%20An%20anomaly%20detection%20approach%20in%20microservices%20using%20distributed%20traces%20and%20profiling%20metrics.pdf#page=4>) |
| [W045](papers/W045-microfi.md) | Request-level resilience testing | Not applicable to forecasting | Trace API graph + request marker | Istio Delay/Abort recipes and business outcomes | [PDF pp. 5–6,10–17](<../Bibliografia_Micro/MicroFI_Non-Intrusive_and_Prioritized_Request-Level_Fault_Injection_for_Microservice_Applications.pdf#page=5>) |
| [W001](papers/W001-fault-sensitive-framework.md) | Current anomaly detection | Minute-aligned observations; future lead unknown | Trace-derived tree + metrics | Chaos Mesh/HypnoFailpoint; 3-minute faults | [PDF pp. 5–11](<../Bibliografia_Micro/A%20failure%20analysis%20framework%20to%20provide%20pure%20anomalous%20data%20using%20multi-source%20data%20of%20fault-sensitive%20microservices.pdf#page=5>) |
| [W019](papers/W019-uncertain-positive-learning.md) | Mitigation-censored disk/node forecast | Numeric lead/history not extracted | SMART/node counters/events | Certain/uncertain outcomes after intervention | [PDF pp. 3,6,8,10](<../Bibliografia_Micro/Can%20We%20Trust%20Auto-Mitigation_%20Improving%20Cloud%20Failure%20Prediction%20with%20Uncertain%20Positive%20Learning.pdf#page=3>) |
| [W056](papers/W056-cnn-performance.md) | Response-time prediction/resource control | Allocation-conditioned performance; lead unknown | Resource/allocation table→CNN image; traces | Measured performance under resource interference | [PDF pp. 5–8,13–17](<../Bibliografia_Micro/Performance%20prediction%20and%20resource%20adaptive%20adjustment%20for%20cloud-native%20microservices.pdf#page=5>) |
| [W070](papers/W070-traceweaver.md) | Trace reconstruction | Not applicable to forecasting | eBPF timestamps + graph/order prerequisites | Jaeger ground truth; controlled requests | [PDF pp. 6,9–11](<../Bibliografia_Micro/TraceWeaver_%20Distributed%20Request%20Tracing%20for%20Microservices%20Without%20Application%20Modification.pdf#page=6>) |
| [W022](papers/W022-xgboost-anomalies.md) | Current trace-latency classification | No positive forecast interval | Trace latency/tabular features | Latency mean+3σ threshold | [PDF pp. 4–9](<../Bibliografia_Micro/Classification_of_Anomalies_in_Microservices_Using_an_XGBoost-Based_Approach_With_Data_Balancing_and_Hyperparameter_Tuning.pdf#page=4>) |
| [W049](papers/W049-multilayer-transformer.md) | Container anomaly + multilayer localization | Five-observation reconstruction window; no future lead | Container metrics + traces/host mapping | SMD/AIOps2020/SockShop injected faults | [PDF pp. 4–5,9–10,13](<../Bibliografia_Micro/Multilayered_Fault_Detection_and_Localization_With_Transformer_for_Microservice_Systems.pdf#page=4>) |
| [W059](papers/W059-resilient-microservices.md) | Development-time resilience testing | Not applicable to forecasting | RPC execution indexes + functional tests | Configured RPC faults; test assertions | [PDF pp. 78–80,173](<../Bibliografia_Micro/Resilient%20Microservice%20Applications%2C%20by%20Design%2C%20and%20without%20the%20Chaos.pdf#page=78>) |
| [W068](papers/W068-agilemfc.md) | Existing failure-type classification | Window around failure; positive lead not established | Logs/metrics/traces; modality/expert gates | GAIA/TT/SN injected fault classes | [PDF pp. 5,8–10](<../Bibliografia_Micro/To%20Split%20or%20to%20Merge%20Exploring%20Multi-modal%20Data%20Flexibly%20for%20Failure%20Classification%20in%20Microservices.pdf#page=5>) |
| [W036](papers/W036-tracing-overhead.md) | Instrumentation overhead measurement | Not applicable to forecasting | Load/instrumentation throughput/latency/resources | Instrumented/uninstrumented controls | [PDF pp. 3–6](<../Bibliografia_Micro/Investigating%20Performance%20Overhead%20of%20Distributed%20Tracing%20in%20Microservices%20and%20Serverless%20Systems.pdf#page=3>) |
| [W005](papers/W005-observability-mapping.md) | Observability mapping | Not applicable to forecasting | Secondary log/trace/metric taxonomy | Primary-study literature selection | [PDF pp. 7,11,19,21](<../Bibliografia_Micro/A%20systematic%20mapping%20study%20on%20observability%20of%20microservices-based%20applications_%20fundamentals%2C%20classifications%2C%20and%20challenges.pdf#page=7>) |
| [W053](papers/W053-observability-frameworks.md) | Observability review | Not applicable to forecasting | Secondary frameworks/health/deployment taxonomy | Reviewed frameworks; not experimental labels | [PDF pp. 4,7,20,24,26](<../Bibliografia_Micro/Observability_in_Microservices_An_In-Depth_Exploration_of_Frameworks_Challenges_and_Deployment_Paradigms.pdf#page=4>) |
| [W004](papers/W004-aiops-taxonomy.md) | Failure-management survey | Lead=event−prediction; no chosen numeric horizon | Secondary literature across modalities | Literature categories; no shared labels | [PDF pp. 8–9,17,28,34](<../Bibliografia_Micro/A%20Survey%20of%20AIOps%20Methods%20for%20Failure%20Management.pdf#page=8>) |

### Evaluation and comparators

| Study / note | Split / independence | Named baselines or comparison | Reported metric / outcome (not reproduced) |
| --- | --- | --- | --- |
| [W033](papers/W033-instantops.md) | ~20/80 train/test; chronology/episodes unknown | GNN/LSTM/GTN variants; JLT/AnoFusion detection | F1 .98/.98/.96 (MicroSS/TT/QoTD); localization separate |
| [W054](papers/W054-online-failure-prediction.md) | Rolling experiments; held-out episode split unknown | ARIMA/Holt–Winters; HORA hierarchy | CPU MSE .00650/.00486; not failure F1 |
| [W057](papers/W057-podfailpred.md) | Ratio/chronology/episode grouping unknown | RF/GB/SVM/KNN | RF/GB table F1 99.73%; confusion counts inconsistent |
| [W040](papers/W040-latent-error-prediction.md) | Random five-fold trace CV | RF/KNN/MLP; trace matching diagnosis | MLP error F1 .990/.943; Top-1 separate |
| [W058](papers/W058-data-leakage.md) | Random/time/drive-group; 2016 future test | HGBC/RF/MLP/LSTM | ROC-AUC/F1/G-mean/MCC; LSTM random .99→.70 future |
| [W029](papers/W029-explainable-gnn.md) | Random graph 80/10/10; topology grouping unknown | Linear/MLP with/without spectral features | Tree MAE .009±.001; DAG .009±.002 |
| [W064](papers/W064-serviceanomaly.md) | Normal-reference/fault test; exact partition unknown | Full baseline setup not extracted | Detection F1 up to .85/.86; small anomaly sets |
| [W045](papers/W045-microfi.md) | Testing groups; predictive split not applicable | ChaosBlade/Istio/Gremlin/3MileBeach; prioritization | Failed functions/injection efficiency/overhead |
| [W001](papers/W001-fault-sensitive-framework.md) | 7/1/2; chronology/episode independence unknown | TraceAnomaly; complete list not extracted | Precision/recall/FPR; Boutique 97.16/97.85/3.10% |
| [W019](papers/W019-uncertain-positive-learning.md) | Sequential update stages; ratios/purge not extracted | Offline oracle/certain-label update; RNN/LSTM/Transformer/TCNN | Precision/recall/F1; numeric gains not extracted |
| [W056](papers/W056-cnn-performance.md) | Chronological/episode split not extracted | FIRM/VIME/Scarf/trees/XGBoost/RF/NB | Classification metrics/resource/response outcomes; no forecast score imported |
| [W070](papers/W070-traceweaver.md) | Load/caching/async tests; no predictive split | WAP5/vPath/DeepFlow/FCFS | Recovery evaluation; numeric metrics not extracted |
| [W022](papers/W022-xgboost-anomalies.md) | 70/20/10 + ten-fold CV; preprocessing order ambiguous | XGBoost/LightGBM/AE/Isolation Forest/trees/NB | Max classification F1 99.97%; not forecast benchmark |
| [W049](papers/W049-multilayer-transformer.md) | Training-only min/max; chronology/episodes not extracted | Temporal/classic detectors; MicroRCA/MonitorRank localization | Detection F1/AUC/AP; localization PR@k/MAP/F1 |
| [W059](papers/W059-resilient-microservices.md) | Configured fault-space exploration; no predictive split | Numeric comparative evaluation not extracted | Coverage/findings; no forecast score |
| [W068](papers/W068-agilemfc.md) | Earlier train/later test; ratios/episode purge unknown | Cloud19/LogCluster/CloudRCA/DiagFusion | Weighted F1 .939/.728/.701, five repeats |
| [W036](papers/W036-tracing-overhead.md) | Controlled benchmarks; predictive split not applicable | OpenTelemetry/Elastic APM/no tracing | Throughput/latency/resources; not universal overhead bound |
| [W005](papers/W005-observability-mapping.md) | Review methodology; predictive split not applicable | No common predictive baseline | Tool/dataset classifications; no unified forecast gain |
| [W053](papers/W053-observability-frameworks.md) | Review; predictive split not applicable | No common predictive baseline | Capabilities/limitations/tool frequency |
| [W004](papers/W004-aiops-taxonomy.md) | Survey; predictive split not applicable | No common predictive baseline | Taxonomy/timing/metric definitions |

## Decision-focused themes

### 1. Target, time and operational action

InstantOps forecasts an application failure in a subsequent minute, yet its error threshold/status definitions disagree between methods and evaluation ([W033](papers/W033-instantops.md), PDF pp. 4, 8–9). The older online-prediction thesis demonstrates different CPU/request forecasting settings, including five- and ten-minute examples rather than one universal service event ([W054](papers/W054-online-failure-prediction.md), pp. 55, 88–91). PodFailPred does not establish a shifted future target or numeric lead in its inspected protocol ([W057](papers/W057-podfailpred.md), pp. 4–5, 8–9). Latent trace errors, simulated disruption probabilities and existing failure types are different targets ([W040](papers/W040-latent-error-prediction.md), pp. 3–4; [W029](papers/W029-explainable-gnn.md), pp. 6–8; [W068](papers/W068-agilemfc.md), p. 5).

**Project implication / transfer inference:** Phase 03 must choose one named-service event, its onset and sustained threshold, history, minimum lead and horizon. Define useful lead with the intended operator action using the survey's timing distinction ([W004](papers/W004-aiops-taxonomy.md), p. 17). Do not borrow a paper's event or score without matching the prediction contract. CNN–LSTM remains the selected primary architecture.

### 2. Telemetry available before decision time

InstantOps combines request/log/resource/Kubernetes evidence; some status/events can already indicate failure ([W033](papers/W033-instantops.md), p. 6). PodFailPred includes current state, readiness and event reasons without a clear target/feature separation ([W057](papers/W057-podfailpred.md), pp. 4–5). Host placement and contention matter in the thesis; the multilayer Transformer separates container observations, service causes and resource metrics ([W054](papers/W054-online-failure-prediction.md), pp. 80–84; [W049](papers/W049-multilayer-transformer.md), pp. 4, 9–10). Observability reviews organize capabilities but do not verify local measurements ([W005](papers/W005-observability-mapping.md), pp. 11, 19; [W053](papers/W053-observability-frameworks.md), pp. 7, 20, 24).

**Project implication / transfer inference:** retain metrics-first input until additional modalities are measured and justified. Audit event time, collection/availability time, pod/service/host identity and missingness before inclusion. The existing all-zero capture remains invalid under [BASELINE_AUDIT.md](BASELINE_AUDIT.md); a paper's zero-row filter is not evidence that deleting it would create healthy data. Whether traces add enough benefit to justify overhead is open ([W036](papers/W036-tracing-overhead.md), pp. 3–6).

### 3. Fault episodes and label provenance

MicroFI constrains request blast radius using explicit Delay/Abort recipes, while SFIT explores a configured RPC failure space with functional tests ([W045](papers/W045-microfi.md), pp. 5–6, 10–11; [W059](papers/W059-resilient-microservices.md), pp. 78–80). PodFailPred supplies pod/resource/network faults; latent-error labeling depends on injected versions and test conditions ([W057](papers/W057-podfailpred.md), pp. 2–5; [W040](papers/W040-latent-error-prediction.md), pp. 7–9). Intervention can censor whether a predicted failure would occur ([W019](papers/W019-uncertain-positive-learning.md), pp. 3, 6, 8).

**Project implication / transfer inference:** episode manifests must distinguish root fault, injector start/end, request/workload, observed failure onset/recovery, affected services/replicas, and uncertainty. An injection, failed pod or trace label does not automatically establish service failure. Preserve normal controls and censored outcomes. Independent episode count, rather than telemetry row count, must govern uncertainty. Local injector compatibility and safe schedules remain unverified.

### 4. Leakage and sample independence

In an HDD dataset, random-split LSTM AUC around .99 becomes .70±.01 on future data, while temporal .75±.01 becomes .73±.01 ([W058](papers/W058-data-leakage.md), p. 10). Its leakage measure assumes independent groups and does not inspect feature proxies (pp. 4–5, 12). Random trace CV in MEPFL and unspecified episode/time rules in InstantOps/PodFailPred do not establish this project's intended deployment evaluation ([W040](papers/W040-latent-error-prediction.md), p. 9; [W033](papers/W033-instantops.md), p. 8; [W057](papers/W057-podfailpred.md), pp. 8–9). XGBoost's preprocessing/split order is ambiguous, whereas the Transformer explicitly uses training min/max ([W022](papers/W022-xgboost-anomalies.md), p. 5; [W049](papers/W049-multilayer-transformer.md), p. 10).

**Project implication / transfer inference:** assign complete failure episodes chronologically before generating overlapping windows. A sample's full support is `[t−history, t+horizon]`; purge samples whose observation or target support crosses partitions. Keep the same injection's affected services together, since microservices are interdependent. Set recovery buffer/embargo explicitly in Phase 03; fit imputation, scaling, feature selection, resampling and tuning inside training folds. The HDD result supports caution, not a measured service-specific leakage reduction.

### 5. Fair baseline families

InstantOps compares graph/temporal variants on its own datasets, while some additional comparisons use detection approaches ([W033](papers/W033-instantops.md), pp. 8–9). XGBoost addresses current latency classification; CNNRPM maps resource/allocation samples into images and predicts performance for resource control ([W022](papers/W022-xgboost-anomalies.md), pp. 4–9; [W056](papers/W056-cnn-performance.md), pp. 5–8, 13–17). ARIMA/Holt–Winters CPU regression compares a different outcome ([W054](papers/W054-online-failure-prediction.md), pp. 90–91).

**Project implication / transfer inference:** implement the [scope's](PROJECT_SCOPE.md) operational threshold, tabular-window and temporal-only baseline families on identical future service labels, held-out episodes and available inputs. An optional graph model tests spatial representation. Match tuning budgets and thresholds; report extra modality/feature access. No reviewed score establishes that CNN–LSTM wins or should be replaced.

### 6. Service topology and CNN layout

ServiceAnomaly derives a context propagation DAG from traces; path context can duplicate logical service nodes ([W064](papers/W064-serviceanomaly.md), pp. 4, 6). The fault-sensitive framework converts its graph to a tree and removes a direct edge, a consequential preprocessing choice ([W001](papers/W001-fault-sensitive-framework.md), pp. 5–6). GNN forecasting uses simulated service meshes, while TraceWeaver reconstruction itself requires graph/order prerequisites and protocol/kernel assumptions ([W029](papers/W029-explainable-gnn.md), pp. 6–8; [W070](papers/W070-traceweaver.md), pp. 6, 9). CNNRPM's grayscale placement represents features, not a validated service-call neighborhood ([W056](papers/W056-cnn-performance.md), pp. 7–8).

**Project implication / transfer inference:** version a directed caller→callee graph from verified traces and reconcile it with configuration, recording absent/low-coverage paths. Keep full graph, derived ordering/tree and pod→service mapping separately. Justify grid adjacency and test permutation/layout sensitivity against temporal-only or order-insensitive input. None of these sources verifies the current Boutique graph.

### 7. Metrics, ambiguity and operational usefulness

Reported F1 values cover system forecasts, pod classification, trace errors and failure types; MAE covers simulated probability, and CPU MSE covers resource regression. They cannot be ranked as a common forecast task (matrix above). PodFailPred's RF/GB confusion counts contradict its performance table ([W057](papers/W057-podfailpred.md), pp. 8–9). InstantOps also has abstract/table and labeling discrepancies ([W033](papers/W033-instantops.md), pp. 1, 4, 8–9). The survey distinguishes lead from warning time and discusses precision/FPR denominators ([W004](papers/W004-aiops-taxonomy.md), pp. 8, 17).

**Project implication / transfer inference:** follow [PROJECT_SCOPE.md](PROJECT_SCOPE.md): per-service precision/recall, PR-AUC when defined, false alerts/hour, first-alert lead and episode-based uncertainty, with validation-only alert calibration. Specify alert deduplication/cooldown, eligible healthy exposure and missed episodes. Keep root-cause/top-k metrics separate. Exact aggregation, confidence intervals and acceptable alert rates are Phase 03 decisions; this review does not invent source operational metrics.

## Narrow gap and unresolved decisions

**Bounded research gap:** the reviewed local evidence does not establish a reproducible, matched evaluation of the selected CNN–LSTM for a future event of a named Online Boutique service, with verified predecision telemetry/topology, chronology plus episode isolation, and operational first-alert/false-alert metrics. The project can address that concrete evidence gap in its local experiment. This is not a claim that no previous service forecasting work exists, nor an architectural novelty claim.

Before labels/training, Phase 03 must resolve:

1. Event and unit: availability or sustained error/latency event; threshold/duration, replica aggregation and onset/recovery rules.
2. Timing: numeric sampling, history, minimum lead, future horizon, action time and warm-up.
3. Inputs: feature availability audit, missingness policy, workload/host context, optional trace/log costs.
4. Episodes: injector/provenance schema, observed-vs-injected onset, downstream labels, controls and censored cases.
5. Evaluation: chronological boundaries, complete-episode grouping, support purge/recovery embargo, preprocessing/tuning discipline.
6. Spatial layout and comparators: verified graph/order, sensitivity checks, common inputs and tuning budget for threshold/tabular/temporal/optional graph baselines.
7. Alerts and uncertainty: validation threshold, deduplication, healthy exposure, missed events, lead summaries and episode-based intervals.

Route: [Phase 03 contract](project-phases/03-protocol/CONTEXT.md), [scope](PROJECT_SCOPE.md), [canonical research gates](RESEARCH_PLAN.md). Protocol choices remain draft; Gate 1 also requires human evidence/contract acceptance.

## Execution checks and review handoff

**Execution finished:** 2026-10-10. Twenty notes cover the queue, including all four explicitly named direct-paper task sources and the leakage/topology/injection/taxonomy sources. Five full decision reviews and fifteen focused reviews declare their depth. Original InstantOps pp. 8–9 and PodFailPred pp. 8–9 were rendered and visually checked for table/text discrepancies. Source hashes, page ranges and navigation checks are recorded below after checking the saved artifacts. No raw PDF, baseline capture or model code was changed by this phase.

| Phase 02 action | Durable evidence / output | Execution record |
| --- | --- | --- |
| 01-direct-papers / 01-targets | W033/W054/W057/W029 notes, Question and target | Units, histories and timing extracted; unknowns and task distinctions explicit. |
| 01-direct-papers / 02-data-method | Same four notes, Data and method | Environments, modalities, counts, labels, architecture and comparison families with pages. |
| 01-direct-papers / 03-results | Same four notes, Evaluation and limits / Relevance here | Split limitations and task-specific outcomes; inconsistencies retained; no reproduction claimed. |
| 02-design-evidence / 01-leakage | W058 note and theme 4 | Domain/independence limits; episode/support purge marked transfer inference. |
| 02-design-evidence / 02-topology | W064/W029/W001/W070/W056 notes and theme 6 | Graph source, node/edge meaning and Boutique feasibility assumptions. |
| 02-design-evidence / 03-injection-taxonomy | W045/W004/W059/W057/W068 notes and themes 1/3 | Injection provenance and separate forecasting/detection/diagnosis/testing tasks. |
| 03-synthesis / 01-evidence-matrix | Two keyed matrix tables above | Twenty rows each; all seven comparison fields, note links and PDF pages. |
| 03-synthesis / 02-themes | Seven decision-focused themes above | Evidence, disagreement/limits and project implication/open choice per theme. |
| 03-synthesis / 03-gap | Narrow gap, unresolved decisions, literature navigation | Local gap without unsupported novelty; notes/synthesis accessible from map. |

**Human review pending:** accept or revise target/time classifications, exact page evidence, depth limits, the GNN edition choice, InstantOps SLA/result conflicts, PodFailPred temporal-label/count ambiguities and project transfer inferences. Record reviewer, date and decision here before changing Phase 02 to `complete`. Agent checks record work performed and do not represent human acceptance.

**Artifact checks (2026-10-10):** SHA-256 recomputation matches all 81 inventory PDFs; the 20 notes also match their exact source hashes. All inspected/cited page ranges fall inside their source PDFs. The four template sections and no-reproduction declaration exist in every note. All 568 local file links and 21 Markdown anchors checked across the notes, phase files and affected navigation resolve. Each of the two matrix tables has exactly one row for each of the 20 study IDs. All 16 Phase 02 files use `work-complete-awaiting-review`; all nine action boxes are checked, with zero unchecked actions. These are artifact/source checks, not experimental validation or human scientific review.
