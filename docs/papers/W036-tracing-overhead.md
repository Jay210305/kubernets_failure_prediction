---
kind: paper-note
study_id: W036
source_pdf: "Bibliografia_Micro/Investigating Performance Overhead of Distributed Tracing in Microservices and Serverless Systems.pdf"
source_sha256: 47b61f93e7672374c89ef6e19a405e1688b4d226210065100b3e38852a502ebf
reviewed_on: 2026-10-10
review_depth: methods
reviewed_pages: [3, 4, 5, 6]
research_task: other
status: work-complete-awaiting-review
---

# Investigating Performance Overhead of Distributed Tracing in Microservices and Serverless Systems

**Citation:** Anders Nõu et al.; 2025; ICPE '25; 10.1145/3680256.3721316. **Source:** [original PDF](<../../Bibliografia_Micro/Investigating%20Performance%20Overhead%20of%20Distributed%20Tracing%20in%20Microservices%20and%20Serverless%20Systems.pdf>) — references below use physical PDF page numbers, including cover pages. **Depth:** focused methods/evaluation review for the queued design decision; unrelated sections are not claimed as reviewed. Inspected pages are recorded above. **Reproduced in this repository:** none.

## Question and target

Controlled measurement of tracing overhead, with throughput, latency and resources as outcomes. No service-failure forecast labels/history/lead/split are applicable (p. 3).

## Data and method

Noninstrumented, OpenTelemetry and Elastic APM configurations compare microservice frameworks with PostgreSQL and k6 constant-arrival-rate loads. Scenarios specify warm-up/cooling, request rate and instrumentation configuration (pp. 3–4). SeBS serverless workloads compare instrumented/uninstrumented Python Flask and Node.js applications (p. 5).

## Evaluation and limits

Within the microservice benchmarks, throughput reductions range from 19.55% to 80.18%; this is not a universal overhead bound for Boutique (p. 4). Export is the largest microservice overhead contributor in the analyzed breakdown, with workload-dependent serverless effects (p. 6). Complete run counts/uncertainty are not extracted; no reproduction.

## Relevance here

Transfer inference: document sampling/export configuration and measure instrumentation overhead alongside eventual captures. Do not assume traces are free or transfer these throughput percentages to this cluster.

Route: [project scope](../PROJECT_SCOPE.md), [thematic synthesis](../LITERATURE_SYNTHESIS.md), [corpus identity and queue](../CORPUS_INDEX.md). Human evidence review is pending.
