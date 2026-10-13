---
kind: paper-note
study_id: W040
source_pdf: "Bibliografia_Micro/Latent error prediction and fault localization for microservice applications by learning from system trace logs.pdf"
source_sha256: fbc447e7853538803934ec3feb250dc75d0074fb1e36af56de94877f1ed7f12c
reviewed_on: 2026-10-10
review_depth: full
reviewed_pages: [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
research_task: detection
status: work-complete-awaiting-review
---

# Latent error prediction and fault localization for microservice applications by learning from system trace logs

**Citation:** Xiang Zhou et al.; 2019; ESEC/FSE '19; 10.1145/3338906.3338961. **Source:** [original PDF](<../../Bibliografia_Micro/Latent%20error%20prediction%20and%20fault%20localization%20for%20microservice%20applications%20by%20learning%20from%20system%20trace%20logs.pdf>) — references below use physical PDF page numbers, including cover pages. **Depth:** full decision review of target, methods, evaluation and limits; references/appendices not exhaustively audited. Inspected pages are recorded above. **Reproduced in this repository:** none.

## Question and target

MEPFL infers latent errors, faulty microservices and fault types from an already captured request trace (pp. 3–4, 8–9). Its use of “prediction” does not establish a future service event or positive lead interval. Unit: trace instance, with associated service/type labels. History is the captured trace, not a declared pre-event time window.

## Data and method

Runtime trace features include execution time, response code, resource/configuration and instance information, and asynchronous ordering. Code transformations inject multi-instance/configuration/asynchronous-interaction faults; tests exercise faulty versions under controlled environments (pp. 4–7). Labels depend on unexpected test outcomes, a faulty service occurring in the trace, environment validity, and passing monolithic controls. The latent-error label is 0; other cases, including unknown errors, are 1 (pp. 7–8).

SockShop: eight services, 32 faults, 243,606 traces, 32,643 latent-error traces. TrainTicket: 40 services, 142 faults, 1,214,637 traces, 211,347 latent-error traces; private cloud of 20 VMs (p. 9). RF, KNN and MLP classifiers with grid search are evaluated; trace matching is a diagnosis comparison (pp. 8–10).

## Evaluation and limits

Random five-fold trace-instance cross-validation, rather than chronological held-out episodes (p. 9). Table 4 gives MLP latent-error F1 .990 SockShop and .943 TrainTicket; Top-1 localization .933/.937 is a separate metric (p. 10). Cross-application latent-error F1 drops to .501 TrainTicket→SockShop and .471 SockShop→TrainTicket (pp. 10–11). Injection/label assumptions, benchmark coverage and runtime noise limit transfer (p. 11). Original work is ESEC/FSE 2019; the PDF download date is not publication date (pp. 1–2). No reproduction.

## Relevance here

Supports recording fault configuration and separating trace-error, fault-type and service labels. Transfer inference: hold out complete episodes and avoid completed-trace response features when claiming an early forecast. Cross-application weakness motivates reporting local scope, not assuming portability.

Route: [project scope](../PROJECT_SCOPE.md), [thematic synthesis](../LITERATURE_SYNTHESIS.md), [corpus identity and queue](../CORPUS_INDEX.md). Human evidence review is pending.
