---
kind: experiment-protocol
protocol_version: service-request-failure-v0.1
status: draft-awaiting-review-and-signal-verification
checked: 2026-10-10
---

# Service failure prediction protocol

## 1. Status, intent and evidence

Forecast a sustained request failure of a named Online Boutique service with the user-selected **CNN–LSTM**, then compare it against operational, tabular and temporal baselines. The user selected sustained request failure on 2026-10-10. Numerical settings below are **proposed experiment choices**, not literature-established optimal values or human acceptance of the full protocol. This document specifies future implementation; no collector, labels, model, topology or experiment is implemented by this phase.

The current [baseline audit](BASELINE_AUDIT.md) fails data readiness. There is no verified service request-outcome signal. Consequently the Phase 03 event to-do's requirement for recognition from a verified signal remains open. Human protocol review and signal verification are separate prerequisites. Do not treat this draft as authorization to start a cluster, inject faults or train.

Evidence routes: [literature synthesis](LITERATURE_SYNTHESIS.md), [scope](PROJECT_SCOPE.md), [research gates](RESEARCH_PLAN.md), [extractor](../google_boutique/extract_telemetry.py). Source-specific distinctions inform the design; numerical thresholds and operational choices are project assumptions to assess on training/development evidence before freezing a dated version.

## 2. Service registry and event

### Registry and output order

Keep the extractor's context rows in this exact order:

`[frontend, cartservice, productcatalogservice, currencyservice, paymentservice, shippingservice, emailservice, checkoutservice, recommendationservice, adservice, redis-cart]`.

The first ten are the **proposed forecast targets**, in that order. `redis-cart` is supporting storage context, with no forecast head in this version. The load generator is neither a feature row nor a target. This is a proposed registry derived from the source-code list, not verified deployment inventory. Phase 04 must reconcile pod→logical-service membership and actual protocols/replicas; any registry change requires a new protocol/schema version before labels or test evaluation.

### Candidate decision

| Candidate | Meaning and observability | Decision |
| --- | --- | --- |
| Sustained request failure | A representative valid operation repeatedly fails when sent to a logical service through its normal routing across replicas. HTTP/gRPC outcomes can be normalized by a versioned observer. | Primary, selected by user. Proposed oracle below; local signal unverified. |
| Service unavailable | Reachability alone may detect transport loss while missing a reachable service returning errors. | Secondary diagnostic field; no separate label union. |
| Sustained HTTP 5xx | Requires verified outcome counts/denominator and does not automatically cover gRPC services. The extractor has an unverified error rate but no total-request denominator. | Deferred extension, separately versioned target if adopted. |
| Kubernetes failure state | Pod status/restarts can coexist with a working replicated service. | Context/episode diagnostics, excluded as primary service label. |

### Proposed request oracle

Use a future dedicated observer; its measurements are **label evidence, excluded from model features**. For each target, an oracle manifest must name a representative operation, protocol/endpoint, valid deterministic test payload, expected successful response, service routing/replica mapping, timeout, credentials policy, observer revision and workload interaction. Mutating operations require disposable sandbox fixtures/reset records. Exact deployed operations are unavailable; no default endpoint or unverified health check is silently substituted. Until every included target has a validated operation, its labels are unknown and the proposed ten-target experiment cannot run.

Schedule two attempts per second per service, ten per UTC-aligned five-second bucket `[b,b+5s)`. Each attempt has a two-second deadline and a unique ID; assign it by scheduled start time and keep completion/observation time. Success means transport completes before deadline and satisfies the versioned application response predicate. Validly observed timeouts, connection failures, unsuccessful RPC/HTTP outcomes and incorrect application responses are failed requests. Retries are disabled in the oracle. Observer scheduling loss, missing outcomes, invalid fixture/payload, missing observer heartbeat or failed observer-control validation make the affected bucket **unknown**. Distinguish target-path transport failure from observer failure using a control record; unresolved attribution is unknown.

For a complete bucket with ten valid attempts, `bad=1` if at least eight fail (≥80%); otherwise `bad=0`. A service event requires **six consecutive bad buckets** (30 seconds). Recorded onset `tau` is the left edge of the first bad bucket of that confirmed run; confirmation occurs after the sixth bucket's outcomes arrive (at most two seconds beyond its end). Record confirmation separately. This retrospective onset has five-second resolution and is not asserted to equal the physical fault time. Events begin only after a validated healthy initialization; an initially failed capture is left-censored.

An event remains active until six consecutive complete buckets each have at least nine successes (≥90%). Recovery is the end of that six-bucket recovery run; confirmation again uses actual arrival times. An unknown bucket breaks confirmation and prevents declaring healthy recovery. Repeated failures before confirmed recovery belong to the same event. Keep injector start/end, observed onset/recovery and downstream affected services as separate fields. No event is inferred from a zero feature, a pod restart or injection start alone.

This strict oracle defines a severe, observer-operation-specific outcome. It does not represent every customer request or root cause. Its two requests/second, thresholds, deadlines, fixtures and overhead require development validation and human acceptance before freeze. Phase 04 must show normal-operation successes, controlled failed outcomes in a separately authorized validation, truthful missingness and replica aggregation; Phase 05 supplies independent episode provenance.

## 3. Timing and labels

All times are UTC with recorded clock synchronization/error. Decision times `t` lie on a five-second grid. Require clock error ≤1 second for accepted oracle/telemetry joins; otherwise mark the interval ineligible. Every raw observation stores `event_time` and `available_at`; online replay may use only values with both relevant source times ≤`t` and `available_at≤t`. A future query of historical Prometheus data cannot reconstruct availability by itself.

| Parameter | Proposed value / exact interpretation |
| --- | --- |
| Decision cadence | 5 seconds |
| Input rows | 36 metric endpoints `e_j=t−180s+5j`, `j=0…35`; last endpoint `t−5s` |
| Nominal observation history | 36 five-second bins = 180 seconds ending five seconds before `t`; endpoints themselves span 175 seconds |
| Raw feature support | Earliest rate endpoint `t−180s` uses preceding 30 seconds: `(t−210s,t−5s]` |
| Minimum lead | `lead_min=30s`, strict lower bound |
| Forecast horizon | `horizon=120s` |
| Positive event interval | `(t+30s,t+120s]` |
| Label-confirmation allowance | 35 seconds: 30-second persistence plus ≤2-second outcome deadline, rounded up to the five-second grid |
| Full split support | Conservative `[t−210s,t+155s]`, including future label confirmation |
| Recovery exclusion | Active event plus 60 seconds after confirmed recovery |

The intended operator action is manual investigation/preparation for mitigation; the ≥30-second warning requirement is a hypothesis about usefulness, not a measured response time. Automatic mitigation is excluded.

Eligibility at decision time requires a complete input history, a validated oracle and no active/recovery-excluded event. For health eligibility, use the six latest complete oracle buckets ending no later than `t−5s`, each with at least nine successful attempts. This causal filter is identical for every model and restricts the primary task to forecasting from an observed healthy state; report how much exposure it excludes.

For an eligible `(service,t)`, use the **first** confirmed future event onset:

- `y=1` if the first onset is in `(t+30s,t+120s]`.
- `y=0` if no onset occurs in `(t,t+120s]`, the oracle is complete throughout that interval plus its confirmation allowance, and no episode uncertainty affects it.
- `y=unknown/too-late` if the first onset is in `(t,t+30s]`; never convert this imminent event to a healthy negative. It is excluded from primary sample classification but retained for operational late-alert reporting.
- `y=unknown` for missing oracle coverage, ambiguous/censored outcomes, active failure, recovery exclusion, incomplete end-of-run follow-up or missing causal input eligibility. Record a reason for every exclusion.

Labels may use future outcomes; features and alert eligibility may not. Example: at `t=12:00:00`, onset `12:00:30` is too-late, onset `12:00:35` or `12:02:00` is positive, onset `12:02:05` is outside the horizon (negative only if the earlier interval is fully observed). An event beginning at the first bucket left edge may be confirmed 32 seconds later; that future confirmation is included in split support. End-of-run samples without this follow-up are censored.

## 4. Feature schema and causal preprocessing

**Primary features in order:** `[cpu_usage, memory_usage, network_rx, network_tx]`. All four are mandatory sources pending validation; none is presently verified by the all-zero capture. The existing fifth feature `http_errors` is cataloged as an optional extension rather than silently treated as available. Removing it changes the primary layout from the extractor's intended 11×5 to **11×4**. A future implementation must select columns explicitly, not reshape the unchanged 55-column capture as 44 columns.

These are exact current query templates from the extractor, with `s` replaced by a registry service name and `namespace="demo-app"`. They describe current intent; label semantics and correct aggregation require live validation in Phase 04.

| Feature | Unit / source | Current PromQL template | Inference rule |
| --- | --- | --- | --- |
| cpu_usage | CPU-seconds/second (cores), cAdvisor counter | `sum(rate(container_cpu_usage_seconds_total{namespace="demo-app", pod=~"{s}-.*", container!=""}[30s]))` | Trailing rate ending at an eligible past endpoint; audit replica and sidecar inclusion. |
| memory_usage | Bytes, working-set gauge | `sum(container_memory_working_set_bytes{namespace="demo-app", pod=~"{s}-.*", container!=""})` | Gauge with actual sample timestamp and arrival record; audit sidecar/container scope. |
| network_rx | Bytes/second, receive counter | `sum(rate(container_network_receive_bytes_total{namespace="demo-app", pod=~"{s}-.*"}[30s]))` | Trailing rate; audit shared network namespace/interface double counting. |
| network_tx | Bytes/second, transmit counter | `sum(rate(container_network_transmit_bytes_total{namespace="demo-app", pod=~"{s}-.*"}[30s]))` | Same trailing-rate and aggregation checks. |
| http_errors (optional) | Requests/second, HTTP counter | `sum(rate(http_requests_total{namespace="demo-app", pod=~"{s}-.*", status=~"5.."}[30s])) or vector(0)` | Unverified and excluded from primary input. No denominator; remove zero fallback in a future validated collector so absence remains missing. |

Every accepted capture must record Prometheus URL, namespace, query/version, scrape cadence, actual labels, replica mapping and source timestamps. Five-second query cadence is not evidence of a five-second scrape. Require verified source updates no older than ten seconds at endpoint; no future interpolation. Query errors, empty results and absent series are missing, never measured zero. Known zero values retain their observed flag.

Preserve raw values and masks. A proposed input sample is admitted only if each primary feature exists for every context service during validated normal intervals, every service/feature window has ≥90% observed cells, and no missing run exceeds two bins. For sporadic gaps: causal forward fill for at most ten seconds, using only earlier available values; otherwise use the feature/service median fit on training observations. The quality eligibility rule still applies. Do not backward-fill. Carry observed/missing flags even after imputation; reject captures whose missingness was already destroyed by zero filling.

Fit each service/feature median and standardization mean/std on unique raw training grid rows only, not duplicated overlapping windows. Zero training standard deviation uses denominator 1 and a recorded constant-feature flag. Reuse these parameters unchanged on validation/test; do not clip based on their distributions. Any feature selection/resampling occurs inside training folds. Probe results, future status/recovery, injected-fault metadata and labels are excluded as model inputs. Host/workload/log/trace features are later matched-input extensions with their own versions.

## 5. Topology, tensors and layout comparison

No local graph is verified. **Layout v0 is the exact registry order in section 2**, with arbitrary neighboring rows explicitly treated as a CNN assumption. The code graph in `graphify-out/` covers extractor relationships and is not a service-call graph. Proposed topology validation: obtain traces with caller/parent→callee/child edges, canonicalize pod instances to logical services, record counts/coverage, reconcile configuration and retain cycles/multiple paths. Store evidence path/hash, capture interval, service mapping and graph version; derive a separately versioned ordering only after review. Literature routes: [ServiceAnomaly](papers/W064-serviceanomaly.md), PDF pp. 4, 6; [fault-sensitive framework](papers/W001-fault-sensitive-framework.md), pp. 5–6; [TraceWeaver](papers/W070-traceweaver.md), pp. 6, 9. These support transfer hypotheses, not local validation.

Serialize values and masks as two separate arrays `(N,36,11,4)` with explicit time/service/feature metadata. Time increases oldest→newest. Logical CNN input stacks them as `(batch,time,service,feature,channel)=(B,36,11,4,2)`, channels `[standardized_value,observed_flag]`. Observed flag is 1 only for a genuine source measurement, 0 for either fill. A framework permutation must be named explicitly. No padded history, fabricated service rows or windows spanning capture gaps are allowed. Labels/eligibility masks are `(N,10)` and scores `(N,10)`, matching the ten target services; masked targets do not contribute to supervised loss.

Primary CNN–LSTM v0: at each time step two 2-D convolutions, 16 then 32 channels, 3×3 kernels, stride 1, zero padding of one cell, ReLU; flatten the fixed 11×4 spatial map, project to 64 features, then one 64-unit causal LSTM. Final hidden state feeds a ten-output sigmoid head. No pooling across service identity. Convolution boundary padding is architectural padding, not fake observed telemetry. Weighted binary cross-entropy uses training-only positive counts, with per-service weights capped at 20 and recorded. Architecture is proposed, not implemented or proven beneficial.

Spatial sensitivity: use the reversed registry and two independent Fisher–Yates permutations generated with explicitly recorded PCG64 seeds 101 and 202. Save the realized row arrays and hashes, permute values/masks together, keep output IDs canonical, and retrain each variant on identical splits/seeds. Do not choose the best ordering using test results. Report all prespecified variants. Temporal-only and tabular comparators provide inputs without CNN adjacency; an optional graph model requires a verified graph and is secondary. The hypothesis is that the CNN layout contributes measurable benefit, not that arbitrary adjacency encodes actual calls.

## 6. Episodes, chronology and leakage controls

Before window generation, create a frozen manifest of runs, workload, root injection/incident IDs, recipes, injector times, observed per-service onsets/recoveries, uncertainty, controls and topology/query revisions. One root incident and all affected services form one group. Define its protected interval from 365 seconds before injector/incident start through 210 seconds after the latest confirmed recovery. For events without injection records, use earliest observed onset as incident start with a provenance caveat. Merge incidents with overlapping protected intervals; multi-fault groups are identified separately. Censored/unrecoverable/ambiguous groups do not enter primary supervised analysis.

Proposed split: 70% training, 15% validation, 15% test by **observed UTC duration** of the chronological run schedule, before inspecting model results. Freeze actual boundary timestamps in a dated split manifest. The nominal 70/85% cut times are shifted forward to the end of any intersected protected group, including merged groups; record realized durations/counts. If this empties validation/test or lacks required events, collect additional independently authorized episodes or revise the protocol before fitting. Never distribute a root incident or its services between partitions. Boundaries cannot be moved to improve a model score.

Allow no sample unless its full conservative support `[t−210s,t+155s]` is contained in one partition and one uninterrupted capture. At boundary `B`, earlier decisions need `t+155s<B` and later decisions need `t−210s>B`; equality is excluded conservatively. This creates a **365-second decision-time gap** around each boundary, in addition to whole-group exclusion. Exact support checks govern inclusion, not a guessed “36-step purge.” Label persistence, PromQL lookback and data-availability lag are included. Windowing follows group assignment and support filtering; preprocessing is fit only after assignment to training.

For tuning, divide training duration into four chronological quarters Q1–Q4 and use three expanding-time folds: Q1→Q2, Q1+Q2→Q3, Q1+Q2+Q3→Q4, where the left side fits and the right side selects checkpoints/hyperparameters. Shift nominal quarter boundaries forward out of protected groups as for the outer split; apply the same support checks. Save actual fold boundaries before scoring. If a fold lacks two classes for an evaluated service, exclude that service/fold and record it; if no valid folds remain, model selection is underpowered and fitting stops for the confirmatory study. Do not fall back to random windows. The final validation partition serves calibration/alert selection only; test remains untouched until configuration is frozen.

Minimum planning requirement: ten independent confirmed groups involving each target in training, five in validation and five in test, plus at least ten eligible healthy service-hours per target in validation and test. These are pragmatic minimums, not a statistical power proof. An unmet target is reported as insufficient evidence; narrowing the confirmatory target set requires a new pretest protocol version, not silent exclusion after results. Shared incidents count once, not once per row/service. Rare fault types and merged multi-fault groups must be tabulated separately. Use naturally observed class prevalence in validation/test; no synthetic test negatives or resampling.

These episode/support rules are **transfer inferences** from the [leakage note](papers/W058-data-leakage.md), PDF pp. 4–5, 8–10, 12, and the [synthesis](LITERATURE_SYNTHESIS.md#4-leakage-and-sample-independence). The HDD study does not demonstrate this project's independence or prove these buffers optimal.

## 7. Comparators and model selection

All models share service registry, primary available values/masks, eligible decision times, labels, support filters, splits, alert policy and test data. Use seeds `[11,22,33,44,55]`; report each seed and five-seed summary without selecting a favorable seed.

| Family | Proposed implementation / input | Training selection budget |
| --- | --- | --- |
| Operational threshold | Per-target maximum of four adverse latest-bin empirical training percentiles, with memory/CPU/rx/tx all defined higher-is-adverse as a declared crude baseline; missing cells use the same preprocessing. | No supervised hyperparameter search; alert threshold uses common validation rule. |
| Tabular window | Per-target logistic regression and RF using each context service/feature's mean, std, min, max, last, slope plus observed fraction over the same 36 bins. | Up to 12 prespecified configurations each, same time folds/seeds. RF is a separate baseline, not selected over logistic using test. |
| Temporal-only | Flatten canonical service/feature/value/mask axes per step → one LSTM → ten sigmoid outputs; no spatial convolution. | Up to 12 prespecified configurations, same time folds/seeds. |
| CNN–LSTM (primary) | Section 5's per-step CNN → LSTM → ten scores. | Up to 12 prespecified configurations, same time folds/seeds; v0 included. |

Logistic grid: `C∈{0.01,0.1,1,10}`, unweighted or training inverse-frequency class weights (8 configurations). RF grid: 200/500 trees × max depth 8/16/unlimited × unweighted/training-balanced (12). LSTM grid: hidden 32/64/128 × dropout 0/0.2 × learning rate 0.001/0.0003 (12). CNN–LSTM grid: convolution widths (8,16)/(16,32) × LSTM hidden 32/64/128 × learning rate 0.001/0.0003 (12), projection 64 and dropout 0.2 fixed. Dropout applies between projection/recurrent head layers, not implicit single-layer recurrent dropout. Batch size 64, Adam, maximum 100 epochs, early stopping patience ten on each fold's macro AP; restore the selected checkpoint. Save the exact grid and fold inclusion list before fitting.

Hyperparameters maximize mean macro average precision across eligible training fold/service pairs. Ties within 1e−6 choose fewer parameters, then lexicographic configuration ID. Record fits, early-stopping epochs, wall time, memory and hardware; equal trial counts do not imply equal compute. Fit final training model at the median selected-fold best epoch count (minimum one, maximum 100), without inspecting validation/test losses. No model/ordering family is selected based on test performance.

Fit a per-service sigmoid score calibrator on final validation predictions only, identically for all families; require both classes. Use the same validation data for alert threshold selection and disclose that these are selection results, not an unbiased performance estimate. Test is the sole held-out performance report. Without two validation classes, calibration/threshold fitting is unavailable and the target fails the confirmatory adequacy rule. The operational percentile score is a ranking score until calibrated. Report reliability/Brier score as secondary calibration diagnostics; do not assert calibrated probabilities based solely on a sigmoid output.

## 8. Alerts, metrics and denominators

At an eligible decision, raise an alert when score is at least a per-service validation-selected threshold. Issue at `a`, the actual wall-clock availability time of the forecast. Require scoring/issue within five seconds of decision `t`; otherwise record a missed inference deadline and exclude the delayed decision from sample metrics, but retain its issued alert for operational scoring using `a`. Record coverage and missed deadlines for every family. A late computed risk is not credited with lead measured from its earlier decision timestamp.

Deduplicate per service: after an alert at `a`, suppress further alerts until `a+120s` (strictly earlier times suppressed). Keep all risk decisions for sample metrics. A causally observed active failure or unconfirmed healthy return suppresses future alerts; retrospective labels must not suppress alerts during replay. No cross-service alert deduplication. Apply identical replay logic to every model.

Match each issued alert to the first subsequently confirmed onset of that service. It is a true advance alert if `30s<tau−a≤120s`. Match at most one alert per service event (earliest eligible alert); additional issued alerts for that event are duplicate/unmatched alerts, even if they would otherwise fall in the window. An alert before an onset with `0<tau−a≤30s` is late and receives no advance credit. Alerts with unresolved oracle follow-up are censored, not credited as true/false. Only evaluate alerts whose future observation/confirmation support is available. Record alerts after onset separately when current causal health state lag allowed them.

| Metric | Definition / handling |
| --- | --- |
| Sample precision/recall/F1 per service | TP/FP/FN over eligible known `(service,t)` labels at frozen threshold, with TP/(TP+FP), TP/(TP+FN), harmonic mean. Precision undefined with no predicted positives; recall undefined with no positives; zero recall if positives exist and none detected. |
| PR-AUC summary | Use noninterpolated **average precision (AP)** from score-ranked eligible labels and name this estimator; store the PR curve. AP undefined if either class is absent. Report positive prevalence alongside AP; no substitution by accuracy. |
| Alert precision | Advance-matched alerts / all evaluable issued alerts, including late and duplicate/unmatched alerts in denominator. Undefined if no alerts. |
| Event recall | Events with a matched advance alert / confirmed events with at least one causally eligible decision in their warning interval and complete support. Also report end-to-end recall over all observed confirmed events, counting events with no eligible opportunity as missed; left/right-censored events separate. |
| False alerts per healthy service-hour | Unmatched evaluable issued alerts occurring during observable healthy eligible decision exposure / eligible healthy service-hours. “Healthy” is outside active/recovery intervals and outside any next-onset 120-second interval; exclude unknown and too-late exposure. Each eligible five-second slot contributes 5/3600 hours. State this exclusion policy; late/duplicate alerts are additionally reported per all monitored service-hours. |
| First-alert lead | `tau−a` in seconds for earliest matched advance alert; median, IQR, minimum and complete per-event records. Missed events carry a missed flag and are never encoded as zero lead. |
| Coverage | Eligible decisions / scheduled decisions; causal-feature, oracle, active/recovery, censoring and deadline exclusions by service/reason. Report total monitored hours, healthy eligible hours and event opportunities. |

All monitored service-hours count five-second slots with complete validated oracle observation, regardless of feature/forecast eligibility; report unknown observer time separately. Eligible healthy service-hours use the narrower denominator in the table. Include all eligible continuous healthy slots in rate evaluation, including slots with no issued alert, so cooldown cannot shrink the denominator.

Per-service threshold candidates are each distinct finite calibrated validation score plus a no-alert threshold above the maximum. Replay every candidate on validation using the same cooldown/matching rules. Choose maximum event recall subject to ≤0.1 false alerts per eligible healthy service-hour. Break ties by higher alert precision (undefined precision treated lower than defined), then lower alert count, then higher threshold. If only no-alert is feasible, retain it and report zero operational sensitivity; do not relax the budget using test results. Minimum ten healthy validation hours is still weak evidence for a rate cap; report counts/exposure and uncertainty rather than asserting the true rate meets the cap.

Report per-service and macro scores over services where the metric is defined, naming excluded service IDs; also show micro counts and denominator-weighted alert rates. Services with no positives retain exposure/FP/coverage but have undefined recall/AP as specified above. Do not impute undefined metrics with zero or one. Present classification and episode-alert results separately. Root-cause top-k and fault-class accuracy are outside primary success criteria.

Uncertainty: 1,000 paired bootstrap resamples of complete root-incident groups for event recall and model differences, keeping affected services together. For exposure/rate/AP comparisons, use paired resamples of preassigned complete capture sessions; capture-session IDs must be fixed before model scoring, with episodes nested within sessions and merged cross-session incidents treated as a single block. Recompute denominators/matching within original continuous blocks, never across artificial bootstrap joins. Report percentile 95% intervals, seed results and block counts. If fewer than five independent blocks or a resample lacks a defined denominator/class, mark intervals underpowered/unavailable and record valid resample counts; windows are never bootstrap units. A performance claim requires actual adequate data and runtime costs on identical held-out episodes.

## 9. Freeze, provenance and implementation handoff

Before any confirmatory training, save this accepted protocol version/hash, reviewer/date/decisions, collector/query versions, oracle manifests for every target, actual registry, row orders/graph evidence, feature and label schemas, source hashes, workload/incident/session manifests, chronological boundaries and fold/seed grids. Save eligibility masks, exclusion reasons, training preprocessing parameters, checkpoints/calibrators/thresholds, decision/alert logs and scoring version in a dated run directory. Test outcomes stay sealed until models, calibration and thresholds are frozen. Post-freeze changes require a new version and a new untouched test interval; report the previous attempt.

### Decision log and remaining prerequisites

| Decision | Basis / status |
| --- | --- |
| Primary sustained request failure | User selection; service-level representative-operation interpretation needs oracle review. Pod-level targets remain separate ([PodFailPred](papers/W057-podfailpred.md), pp. 4–5). |
| Five-second cadence / 36 steps | Current extractor intent; actual scrape/availability unverified. Numerical lead, horizon and event persistence are proposed project choices. |
| Four metrics / ten outputs / eleven context rows | Source schema and audit support conservative exclusion of unverified HTTP errors and storage-only context; deployment/series/operation validation pending. |
| CNN–LSTM primary and layout v0 assumption | User-selected architecture; source registry is reproducible, not verified topology. Permutation and no-CNN comparisons required. |
| Episode/time split plus support purge | Transfer inference from leakage literature and source 30-second rate lookbacks; no local leakage result asserted. |
| Alert budget/calibration/bootstrap choices | Explicit project design choices, subject to review and development adequacy checks before freeze. |

Required handoff: human evidence/protocol acceptance; Phase 04 valid metrics, timestamps, oracle operations, overhead and topology checks; Phase 05 incident/label provenance and adequate independent groups. Training gates remain closed until these prerequisites pass. A future signal failure must revise the target/collector and protocol version rather than silently redefine labels.

## 10. Phase 03 execution record

The nine actions have concrete draft outputs in sections 2–8. Eight actions have their documentation work recorded; **01-target/01-event remains open for its verified-signal completion condition**. No currently checked-in signal proves this event. All numerical choices are reviewable here; human gate is pending.

| Action | Output | Status |
| --- | --- | --- |
| 01-target / 01-event | Section 2 registry, candidate decision and oracle | Definition prepared; verified local signal missing. |
| 01-target / 02-time | Section 3 timing, labels, eligibility and boundary examples | Draft work complete; human review pending. |
| 01-target / 03-boundaries | Sections 1–3, 9 and scope | Draft work complete; alternatives/exclusions explicit. |
| 02-input-layout / 01-features | Section 4 queries, units, quality and causal fitting | Draft work complete; live measurement prerequisites stated. |
| 02-input-layout / 02-topology | Section 5 proposed registry layout and graph route | Draft work complete; arbitrary adjacency explicit. |
| 02-input-layout / 03-shape | Section 5 values/masks/axes/output mapping and variants | Draft work complete; updated primary dimensions explicit. |
| 03-evaluation / 01-splits | Section 6 whole-group chronology and 365-second support gap | Draft work complete; actual manifests await data. |
| 03-evaluation / 02-comparators | Section 7 models/grids/folds/seeds/calibration | Draft work complete; no fitting performed. |
| 03-evaluation / 03-metrics | Section 8 alert matching, denominators, thresholds and uncertainty | Draft work complete; no results claimed. |

**Artifact checks, 2026-10-10:** all 113 relative file links and 11 Markdown anchors in the protocol, scope, Phase 03 and affected navigation resolve. All 16 Phase 03 files have execution status and evidence routes; eight action boxes are checked and only `01-target/todos/01-event.md` remains unchecked. All 81 original PDF hashes still match the corpus inventory. A document consistency pass resolved explicit quarter-based tuning folds and distinguishes 180 seconds of binned history, 210 seconds of raw feature support and 155 seconds of future label support. These checks verify saved documentation and source preservation; no telemetry experiment or model test was performed.
