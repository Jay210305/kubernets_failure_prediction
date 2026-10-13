---
kind: paper-note
study_id: W054
source_pdf: "Bibliografia_Micro/Online Failure Prediction for Microservice Architectures.pdf"
source_sha256: 7ef1cf2f0fd15b00460d8d514ea03054d5771dbb5862ab70fbccdae441a28464
reviewed_on: 2026-10-10
review_depth: full
reviewed_pages: [3, 50, 53, 55, 64, 80, 81, 83, 84, 85, 86, 88, 90, 91, 97, 98]
research_task: prediction
status: work-complete-awaiting-review
---

# Online Failure Prediction for Microservice Architectures

**Citation:** Tim Zwietasch; 2017; University of Stuttgart master's thesis; Unknown. **Source:** [original PDF](<../../Bibliografia_Micro/Online%20Failure%20Prediction%20for%20Microservice%20Architectures.pdf>) — references below use physical PDF page numbers, including cover pages. **Depth:** full decision review of target, methods, evaluation and limits; references/appendices not exhaustively audited. Inspected pages are recorded above. **Reproduced in this repository:** none.

## Question and target

Forecasts request failures/resource contention in a microservice hierarchy with shared-host context. A failed request is a non-200 outcome: 500 internal error or 0 unreachable (p. 55). This does not freeze a sustained named-service event. Metrics are sampled once per minute (p. 50). Figure 6.38 uses predictions made ten minutes before the shown time (p. 88); Figures 6.42–43 describe five-minute CPU forecasts with a 60-observation rolling window (p. 90). These are distinct experiment settings, not one universal failure horizon. A minimum guaranteed service warning interval is unknown.

## Data and method

Containerized Netflix RSS reader with edge/middle tiers on Kubernetes 1.5.2, four OpenStack VMs, four CPUs and 8 GB each (p. 53). InfluxDB/CSV inputs include container/host CPU, workload, successful/failed requests and response time (p. 50). Workload scenarios induce contention; total independent fault episodes are unknown. Five repeats are reported for particular workload scenarios (pp. 84–86).

ARIMA component-failure forecasts are propagated through a manually modeled service/host dependency hierarchy by HORA. Shared-host overhead makes summed container CPU imperfect; dependency weighting is a modeling choice (pp. 80–84). Monolithic/hierarchical approaches and Holt–Winters are comparisons in different subexperiments (pp. 64, 90–91).

## Evaluation and limits

The inspected evaluation does not establish a single chronological train/validation/test split with held-out service episodes (pp. 64, 84–91). Initialization caused apparent forecast correlation even with no requests; the author diagnoses it and uses a 20-point initialization requirement (pp. 84–86).

Table 6.7 reports CPU-forecast MSE .00486 for Holt–Winters versus .00650 for ARIMA (p. 91). This is resource regression, not service-failure F1. Application/metric breadth and scalability remain limitations (pp. 97–98). No results are reproduced here.

## Relevance here

Supports collecting host placement and workload with container metrics and reporting warm-up behavior. Transfer inference: test whether shared-host context improves service forecasts on independent episodes. Its five/ten-minute settings do not choose this project's lead or horizon; Phase 03 must choose these with an operational event definition.

Route: [project scope](../PROJECT_SCOPE.md), [thematic synthesis](../LITERATURE_SYNTHESIS.md), [corpus identity and queue](../CORPUS_INDEX.md). Human evidence review is pending.
