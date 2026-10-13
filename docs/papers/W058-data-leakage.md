---
kind: paper-note
study_id: W058
source_pdf: "Bibliografia_Micro/Quantifying Data Leakage in Failure Prediction Tasks.pdf"
source_sha256: 11a0429310169a643c519b6097abf666d8eae9e492c902603b48f893396f41c1
reviewed_on: 2026-10-10
review_depth: full
reviewed_pages: [4, 5, 6, 7, 8, 9, 10, 12]
research_task: prediction
status: work-complete-awaiting-review
---

# Quantifying Data Leakage in Failure Prediction Tasks

**Citation:** Daniel Grillmeyer et al.; 2025; ICPE '25; 10.1145/3676151.3719368. **Source:** [original PDF](<../../Bibliografia_Micro/Quantifying%20Data%20Leakage%20in%20Failure%20Prediction%20Tasks.pdf>) — references below use physical PDF page numbers, including cover pages. **Depth:** full decision review of target, methods, evaluation and limits; references/appendices not exhaustively audited. Inspected pages are recorded above. **Reproduced in this repository:** none.

## Question and target

HDD failure/RUL classification, not microservice availability. Daily drive observations; critical class is within seven days and warning class within 28 days (pp. 6–7). These thresholds are HDD-specific and do not choose service lead/horizon.

## Data and method

Backblaze 2014–2015 ST4000DM000: 823 failures and 10,154,343 drive-days; SMART features and drive serials, with 2016 as an independent future test. Only 2.5% of healthy drives are retained in a downsampling experiment (pp. 6–7).

Leakage measurement uses temporal proximity and groups; alpha changes how past observations of a known unit are treated. It assumes correct timestamps and independent groups, and does not inspect feature values/proxies (pp. 4–5). No-split, random, temporal and drive-group splits are studied; outer train/test is 70/30, with train/validation/test 60/10/30. HGBC, RF, MLP and LSTM use validation tuning; scalers fit after splitting (pp. 5, 8).

## Evaluation and limits

Ten seeds; F1, G-mean, MCC and ROC-AUC (p. 8). Table 2's normalized leakage for alpha=0/1 is random .34/.59, temporal 0/.002 and group 0/0 (p. 9). LSTM random-split AUC about .99 falls to .70±.01 on future 2016 data; temporal-split AUC .75±.01 is .73±.01 on the future set (p. 10). This is one HDD model, with undersampling and group-independence limitations (p. 12); it does not quantify this repo's leakage. No reproduction.

## Relevance here

Transfer inference: split by chronology and whole failure episode before making windows; purge any sample whose observation support or future label interval crosses a split boundary. Define a sample's complete support as [t−history, t+horizon], then exclude intersecting supports across partitions. Keep one injection and its affected services together; services/pods alone are not independent HDD-like groups. Exact history, embargo and recovery buffer remain Phase 03 choices. Fit imputation, scaling, feature selection and resampling only within training folds.

Route: [project scope](../PROJECT_SCOPE.md), [thematic synthesis](../LITERATURE_SYNTHESIS.md), [corpus identity and queue](../CORPUS_INDEX.md). Human evidence review is pending.
