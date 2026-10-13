---
kind: paper-note
study_id: W057
source_pdf: "Bibliografia_Micro/PodFailPred_ A New Open-Source Dataset to Train AI Models on Predicting Pod Failures in Kubernetes.pdf"
source_sha256: 88e7ce41c4f1455f0ca7a09a48161bc9e290efd3e0fe449ff7d2f9377aa3108f
reviewed_on: 2026-10-10
review_depth: full
reviewed_pages: [1, 2, 3, 4, 5, 8, 9, 11]
research_task: prediction
status: work-complete-awaiting-review
---

# PodFailPred: A New Open-Source Dataset to Train AI Models on Predicting Pod Failures in Kubernetes

**Citation:** Ilyass Tarhri et al.; 2025; International Journal of Intelligent Engineering and Systems; 10.22266/ijies2025.0430.34. **Source:** [original PDF](<../../Bibliografia_Micro/PodFailPred_%20A%20New%20Open-Source%20Dataset%20to%20Train%20AI%20Models%20on%20Predicting%20Pod%20Failures%20in%20Kubernetes.pdf>) — references below use physical PDF page numbers, including cover pages. **Depth:** full decision review of target, methods, evaluation and limits; references/appendices not exhaustively audited. Inspected pages are recorded above. **Reproduced in this repository:** none.

## Question and target

The claimed target is Kubernetes pod failure, a pod-level outcome rather than availability of a replicated service (pp. 1–2). A future label shift, fixed history window, numeric sampling interval and positive lead/horizon are unknown in the inspected methods/results. Monitoring reads current pod states/events and uses a Sleep_Interval parameter without a numeric value (pp. 4–5). Advance service forecasting is therefore not established by the PDF.

## Data and method

OpenTelemetry Demo with 13 microservices on Azure AKS, one master/two workers and Locust workloads. Azure Chaos Studio supplies CPU/memory stress, pod termination, network delay/partition/loss, node/disk and application faults; OTLP, Prometheus, Jaeger and Grafana provide monitoring (pp. 2–3). The paper claims 15 fault types and 21,374 entries with 38 columns/metrics; these are not 21,374 independent episodes (pp. 1–2).

Table 1 includes CPU/memory/network/filesystem metrics, current status/reason, restart/readiness counts, event reason/message/source and node identity (p. 5). Exact feature-to-label separation and onset mapping are unknown. Preprocessing removes zero CPU/memory/network entries and median-imputes missing values (p. 4). RF, Gradient Boosting, SVM and KNN are evaluated (p. 8).

## Evaluation and limits

Split ratio, chronology, episode grouping and preprocessing fit scope are unknown. Table 2 reports RF/GB accuracy 99.94%, precision 100%, recall 99.47% and F1 99.73% (p. 8). The prose reports TN=5663, TP=724, FP=0, FN=25 for RF/GB (p. 9), which gives accuracy 99.61% and recall 96.66% by arithmetic. Both pages were visually inspected; the discrepancy remains unresolved, not corrected silently.

The received/revised dates are internally inconsistent with each other (p. 1); retain the printed 2025 journal identity with this caveat. Comparisons to other publications do not supply a matched service forecast experiment (pp. 9–11). No project reproduction exists.

## Relevance here

Useful for pod/event provenance and fault taxonomy, with substantial unresolved temporal/label details. Transfer inference: exclude outcome-proxy features unless demonstrably available before t; retain all-zero captures for diagnosis rather than adopting the zero-row filter. A terminated pod must not automatically label its replicated service as failed.

Route: [project scope](../PROJECT_SCOPE.md), [thematic synthesis](../LITERATURE_SYNTHESIS.md), [corpus identity and queue](../CORPUS_INDEX.md). Human evidence review is pending.
