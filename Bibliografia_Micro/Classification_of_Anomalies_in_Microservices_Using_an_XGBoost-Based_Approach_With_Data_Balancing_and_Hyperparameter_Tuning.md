Received22August2025;revised24September2025;accepted14October2025.Dateofpublication16October2025;
dateofcurrentversion6November2025.ThereviewofthisarticlewasarrangedbyAssociateEditorS.Dustdar.
DigitalObjectIdentifier10.1109/OJCS.2025.3622532
Classification of Anomalies in Microservices
Using an XGBoost-Based Approach With Data
Balancing and Hyperparameter Tuning
LUÍSM.BARATA 1,2 (Member,IEEE),EURICOLOPES 2,PEDROR.M.INÁCIO 1 (SeniorMember,IEEE),
ANDMÁRIOM.FREIRE 1,3 (Member,IEEE)
1InstitutodeTelecomunicações,DepartmentofComputerScience,UniversidadedaBeiraInterior,6201-001Covilhã,Portugal
2DepartmentofComputerScience,EscolaSuperiordeTecnologia,InstitutoPolitécnicodeCasteloBranco,6000-767CasteloBranco,Portugal
3NOVALaboratoryforComputerScienceandInformatics(NOVALINCS),DepartmentofComputerScience,UniversityofBeiraInterior,6201-001Covilhã,
Portugal
CORRESPONDINGAUTHOR:LUÍSM.BARATA(email:luis.miguel.barata@ubi.pt).
ThisworkwassupportedinpartbyFCT/MECIthroughnationalfundsand,whenapplicable,co-fundedbyEUfundsunderUID/50008:Institutode
Telecomunicações,inpartbytheWATERMARKproject(Watermark-BasedAlgorithmsforTrustworthyMediaAuthenticationandRobustCertificationinPublic
Administration),ProjectNo.2024.07356.IACDC,supportedbythe“RE-C05-i08.M04-SupportthelaunchofaprogramofR&Dprojectsaimedatthe
developmentandimplementationofadvancedsystemsincybersecurity,artificialintelligence,anddatascienceinpublicadministration,aswellasascientific
trainingprogram,”undertheRecoveryandResiliencePlan(PRR),aspartofthefundingagreementsignedbetweentheRecoveryPortugalTaskForce(EMRP)and
theFundaçãoparaaCiênciaeaTecnologia(FCT),andinpartbytheUID/04516/NOVALaboratoryforComputerScienceandInformatics(NOVALINCS)with
thefinancialsupportofFCT.IP.
ABSTRACT Microservice architecture has emerged as a leading paradigm for decomposing large mono-
lithic applications into smaller, autonomous services. Although this approach offers many advantages, its
complexity,distributednature,andsubstantialscalecreatesignificantchallengesformonitoringandanomaly
detection.Thevastvolumeofgenerateddatafurtherexacerbatescomputationalloadanddetectionlatency,
complicatingtheidentificationofanomalies.Thisstudyanalysestheimpactofdatabalancingandhyperpa-
rametertuningonanomalyclassificationinmicroservicesandintroducesADMXGB-AnomalyDetectionin
MicroservicesusingXGBoost,aXGBoost-basedframeworktailoredforanomalydetectioninmicroservices
that seamlessly integrates data balancing with hyperparameter tuning. We propose guidelines to determine
appropriate threshold values that balance sensitivity with false positives, and show that the framework is
model-agnostic, enabling integration with different machine learning algorithms beyond XGBoost. Valida-
tionwasperformedusingafour-stageprocessencompassingpreprocessing,training,validation,andtesting.
ADMXGB demonstrated improvements in both Accuracy and F1-Score, reaching 99.96% in both metrics
ontheTraceRCAdataset,outperformingthebaselineXGBoostmethodbyamarginof1.46%inAccuracy
and45.62%inF1-Score.Moreover,ADMXGBachievesreductionsinexecutiontime(-86.3%)andmemory
usage(-21.7%),whilemaintaininganacceptableCPUoverhead.Thesefindingshighlighttherobustnessof
ADMXGBindeliveringhigh-accuracyclassificationinamicroserviceenvironment.
INDEX TERMS Anomaly detection, Data balancing, oversampling, undersampling, hybridsampling, mi-
croservices,hyperparameteroptimization.
I. INTRODUCTION independent development, deployment, and scaling [2],
The rapid adoption of cloud services, particularly Infrastruc- [3], [4]. This design contrasts with monolithic archi-
tureasaService(IaaS)andPlatformasaService(PaaS),has tectures and is widely supported by containerization
been strongly influenced by the emergence of Microservices platforms such as Docker and Kubernetes, which
Architecture (MSA) [1]. MSAs focus on developing simplify orchestration and promote consistency across
modular services with clearly defined interfaces, allowing environments[5].
©2025TheAuthors.ThisworkislicensedunderaCreativeCommonsAttribution4.0License.Formoreinformation,seehttps://creativecommons.org/licenses/by/4.0/
VOLUME6,2025 1673

BARATAETAL.:CLASSIFICATIONOFANOMALIESINMICROSERVICESUSINGANXGBOOST-BASEDAPPROACHWITHDATABALANCING
Microservice-based systems provide clear advantages in Recent research has increasingly adopted automated
scalability and modularity, yet they present unique chal- methods for anomaly detection, including graph neural
lenges for anomaly detection. Their distributed nature, high networks [7], federated learning [8], and sequence-aware ar-
dimensionality,andinterdependenciesmakefaultsdifficultto chitectures [9]. However, two technical challenges remain
localizeanddetect.Conventionalrule-basedmonitoringoften under-addressed: (i) the severe class imbalance in anomaly
failsundersuchdynamicconditions[1]. data,and(ii)thedependenceonoptimalhyperparameterset-
To address these challenges, machine learning (ML) tech- tingsforcomplexmodels.
niques have gained traction. However, anomaly detection in Data balancing is critical to improving model sensitivity
this context faces two persistent problems: the extreme class in rare-event classification tasks. Techniques such as
imbalance in telemetry data, where anomalies are rare, and SMOTE [10], hybridsampling [11], and Denoise Selection
the sensitivity of ML models to hyperparameter configura- Sampling [12] have been proposed to correct skewed
tions. While data balancing strategies (e.g., oversampling, distributions. These techniques aim to prevent overfitting
undersampling,hybridsampling)canmitigatebias[6],andhy- to the majority class and increase recall for minority
perparameter optimization can enhance model performance, (anomalous)instances.
thesetechniquesareoftenappliedinisolation,andtheircom- Hyperparameter optimisation also plays a central role in
putationalcostisfrequentlyoverlooked. improving classification performance and model generalisa-
This study addresses that gap by proposing a framework tion.AutomatedapproacheslikeBayesianoptimisation[13],
thatjointlyexplorestheimpactofdatabalancingandhyperpa- GridSearchCV [14], and end-to-end tuning frameworks [15]
rametertuningonanomalydetectioninmicroservices,while have outperformed manual tuning, particularly in high-
alsoanalyzingtheexecutionfootprintofthesetechniques. dimensionalfeaturespaces.
Thisarticlemakesthefollowingoriginalcontributions: While several studies address either data balancing or
(cid:2)
We propose ADMXGB, an anomaly detection frame- hyperparametertuninginisolation,relativelyfewworkscom-
work for microservices that aims to improve the de- bine both strategies in the context of microservice anomaly
tection accuracy and to reduce computational cost. The detection. Notable exceptions include [9], [11], [16], which
proposed framework introduces a configurable latency report improved F1-scores through joint optimisation. How-
threshold to improve computational efficiency during ever,mostoftheseeffortsareeitherfocusedonIoTnetworks
preprocessing; orlackreproducibledatasets.
(cid:2)
We conduct an extensive evaluation on the TraceRCA The TraceRCA [39] dataset has also become foundational
dataset, where ADMXGB outperforms existing models forbenchmarkingrootcauseanalysis(RCA)inmicroservices.
in multiple evaluation metrics, including classification Recent works have leveraged this dataset to evaluate graph-
accuracyandcomputationalefficiency; based and interpretable learning approaches. For instance,
(cid:2)
We implement a comprehensive training pipeline com- Sleuth [24] employs graph neural networks (GNNs) to gen-
bining data balancing strategies (oversampling, under- eralizeRCAacrosssystems,whileGRACE[26]usesaGCN-
sampling,hybridsampling)withsystematichyperparam- based architecture for interpretable predictions. Benchmark
eteroptimizationthroughGridSearch,RandomSearch, frameworks like RCAEval [25] position TraceRCA among
andBayesianoptimization(HyperOpt),validatedvia10- key datasets for evaluating RCA systems. In addition, ap-
foldcross-validation; proachessuchasTraceStream[40]andTICAD[23]improve
(cid:2)
We identify possible guidelines to determine appro- RCA using feedback-driven clustering and contextual invo-
priate threshold values (e.g., μ+2σ to μ+3σ) that cationpatterns.Zhangetal.[36]combinemulti-dimensional
balancesensitivitywithfalsepositives,andshowthatthe trace inputs with performance localization, and anomaly de-
framework is model-agnostic, enabling integration with tection techniques using PyOD [21] further showcase the
differentmachinelearningalgorithmsbeyondXGBoost. utilityofthedatasetinunsupervisedlearning.
The article is organized as follows: Section II reviews rel- While recent research has advanced anomaly detection in
evant literature; Section III presents the methodology and microservices, most contributions focus on either class bal-
ADMXGB framework; Section IV describes the dataset, ex- ancing or hyperparameter tuning in isolation. Only a limited
periments, and evaluation; and Section V concludes with set of works attempt to integrate both, and even fewer eval-
futureresearchdirections. uate the computational trade-offs of these strategies. These
gaps motivate ADMXGB, which uniquely combines latency
II. RELATEDWORK thresholding, balancing, and systematic tuning in a unified
Microservices architecture has become foundational in mod- frameworkvalidatedonTraceRCA.
erncloud-nativesystemsduetoitsscalabilityandmodularity. Table 1 summarises recent contributions that incorporate
However, its distributed and asynchronous nature introduces either or both of these strategies, highlighting their datasets,
significant challenges for anomaly detection, particularly performancemetrics,andmethodologicalfocus.
when faults propagate across service dependencies. Tradi-
tional approaches based on rule-based heuristics and static III. PROPOSEDMETHODOLOGY
thresholdsarenolongersufficient,promptingtheexploration ADMXGB is an anomaly detection framework based
ofmachinelearning(ML)anddeeplearning(DL)techniques. on the XGBoost algorithm [41], designed to improve
1674 VOLUME6,2025

TABLE1. SummaryofRelatedWorkinMicroserviceAnomalyDetectionUsingDataBalancingorHyperparameterOptimisation
classification performance and resource efficiency in mi- thefilteringstep,consideradatasetwithlatencyvalues[2,3,
croserviceenvironments.Itcombinesthreemaincomponents: 8, 15, 100]. Applying a threshold τ =10 removes all traces
(i) latency-based data filtering, (ii) class balancing, and (iii) with latency below 10 ms, resulting in the subset composed
hyperparameter optimization, all integrated in a structured of[15,100].Thesefilteredtracesarethenprocessedforbal-
four-phasepipelineshowninFig.1. ancing and later partitioned intotraining, validation, and test
τ
|     |     |     | subsets. | This simple example | demonstrates | how acts | as a |
| --- | --- | --- | -------- | ------------------- | ------------ | -------- | ---- |
noisefilterbydiscardinglow-latencyvaluesthatareunlikely
A. FRAMEWORKOVERVIEW
TheADMXGBpipeline(Algorithm1)comprisesfourphases: torepresentanomalousbehavior.
preprocessing,trainingandtuning,validationandtest. An anomaly is defined as a significant latency deviation
relativetothesystembaselinebehaviour.Duringpreprocess-
| In the preprocessing | phase, the dataset | is filtered | using a |     |     |     |     |
| -------------------- | ------------------ | ----------- | ------- | --- | --- | --- | --- |
latency threshold τ, removing low-latency traces to reduce ing,anomaliesareidentifiedbasedonlatencyspikesthatalign
|                     |                      |                | with known | fault injection | events in | the TraceRCA dataset. |     |
| ------------------- | -------------------- | -------------- | ---------- | --------------- | --------- | --------------------- | --- |
| noise and overhead. | Standard exploratory | data analysis, | fea-       |                 |           |                       |     |
ture scaling, and categorical encoding are applied. To clarify Latencyservesastheprimarymetricforlabelling,providing
| VOLUME6,2025 |     |     |     |     |     |     | 1675 |
| ------------ | --- | --- | --- | --- | --- | --- | ---- |

BARATAETAL.:CLASSIFICATIONOFANOMALIESINMICROSERVICESUSINGANXGBOOST-BASEDAPPROACHWITHDATABALANCING
FIGURE1. OverviewoftheADMXGBfour-phasepipeline.Eachphasehighlightsthemainstepsinvolvedinanomalydetection,fromdatapreprocessing
andtrainingwithhyperparametertuningtomodelvalidationandfinalevaluationontestdata.
| the ground | truth | used | for supervised |     | training | and evaluation. |     |           |           |           |           |        |
| ---------- | ----- | ---- | -------------- | --- | -------- | --------------- | --- | --------- | --------- | --------- | --------- | ------ |
|            |       |      |                |     |          |                 |     | Algorithm | 1: ADMXGB | – Anomaly | Detection | in Mi- |
This approach ensures consistency in anomaly identification croservicesUsingXGBoost.
| and reflects | real-world |     | scenarios | in  | which | increased | latency |     |     |     |     |     |
| ------------ | ---------- | --- | --------- | --- | ----- | --------- | ------- | --- | --- | --- | --- | --- |
Require:DatasetD,latencythresholdτ,hyperparameterspace
| typically | indicates | service | degradation |     | or  | failure. | To miti- | H   |     |     |     |     |
| --------- | --------- | ------- | ----------- | --- | --- | -------- | -------- | --- | --- | --- | --- | --- |
gateclassimbalance,threeresamplingstrategiesareexplored: Ensure:OptimizedmodelM∗
| oversampling | (e.g., | SMOTE |     | [42]), | undersampling, |     | and hy- |     |     |     |     |     |
| ------------ | ------ | ----- | --- | ------ | -------------- | --- | ------- | --- | --- | --- | --- | --- |
Phase1:DataPreprocessing
|                    |     |          |     |       |               |     |        | FiltertracesinDwithlatency<τ |     |     | (cid:2)Removealltraces |     |
| ------------------ | --- | -------- | --- | ----- | ------------- | --- | ------ | ---------------------------- | --- | --- | ---------------------- | --- |
| bridsampling,which |     | combines |     | both. | Databalancing |     | mustbe | 1:                           |     |     |                        |     |
applied carefully, particularly in the context of highly im- whoseobservedlatencyisstrictlylowerthanτ
2: Performdatacleaningandexploratoryanalysis
| balanced | data. | Oversampling |     | may introduce |     | noise | or lead | to  |     |     |     |     |
| -------- | ----- | ------------ | --- | ------------- | --- | ----- | ------- | --- | --- | --- | --- | --- |
3: Applyfeaturescalingandencodecategoricalvariables
overfitting,whileundersamplingcandiscardimportantinfor-
mation[43],[44].Therefore,thechoiceofbalancingstrategy 4: Applydatabalancing(SMOTE,undersampling,or
hybridsampling)
mustbealignedwiththedatasetcharacteristicsandthetoler-
Phase2:ModelTraining
ancetonoiseofthemodel.
|     |     |     |     |     |     |     |     | 5: foreachhyperparametersettingh∈H |     |     | do  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------------------------- | --- | --- | --- | --- |
Duringtraining,modelsareoptimizedusing10-foldcross-
|            |       |              |       |                     |      |        |        | 6:           | SplitDintotrainingsetD | andvalidationsetD |     |     |
| ---------- | ----- | ------------ | ----- | ------------------- | ---- | ------ | ------ | ------------ | ---------------------- | ----------------- | --- | --- |
|            |       |              |       |                     |      |        |        |              |                        | train             |     | val |
| validation | on    | the training |       | set. Hyperparameter |      |        | tuning | is           |                        |                   |     |     |
|            |       |              |       |                     |      |        |        | 7:           | TrainmodelM            | h onD train       |     |     |
| performed  | using | one of       | three | strategies:         | Grid | Search | (which |              |                        |                   |     |     |
|            |       |              |       |                     |      |        |        | 8: EvaluateM | h onD                  | usingF1-Score     |     |     |
val
| exhaustively | evaluates |     | all possible |     | combinations |     | within | a 9: endfor |     |     |     |     |
| ------------ | --------- | --- | ------------ | --- | ------------ | --- | ------ | ----------- | --- | --- | --- | --- |
predefined grid), Random Search (which randomly samples 10: Selectoptimalhyperparametersh∗withhighestF1-Score
hyperparameter values), or Bayesian Optimization (Hyper- Phase3:ModelValidation
|     |     |     |     |     |     |     |     | RetrainmodelM∗usingD |     | ∪D  | andh∗ |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | --- | ----- | --- |
Opt [45], which uses a probabilistic model to guide the 11: train val
search). The best hyperparameter configuration is selected Phase4:ModelTesting
EvaluateM∗onD
|                                   |     |     |     |     |     |     |     | 12: |     | usingAccuracy,Precision,Recall, |     |     |
| --------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------- | --- | --- |
| basedonthehighestaverageF1-Score. |     |     |     |     |     |     |     |     |     | test                            |     |     |
F1-Score,andAUC
| In the | validation | phase, | the | best | configuration |     | is used | to  |     |     |     |     |
| ------ | ---------- | ------ | --- | ---- | ------------- | --- | ------- | --- | --- | --- | --- | --- |
13: returnM∗
retrainthemodelonthefulltrainingandvalidationset.
Thefinalphaseevaluatestheperformanceofeachmodelon
| a hold-out | test | set using | the classification |     | and | computational |     |     |     |     |     |     |
| ---------- | ---- | --------- | ------------------ | --- | --- | ------------- | --- | --- | --- | --- | --- | --- |
metricsdescribedintheSectionIII-B. computational efficiency makes it a more complete solution
XGBoostwasselectedasthecorealgorithmofADMXGB comparedtoalternativessuchasRandomForest,LightGBM,
| because | it is an | ensemble-based |     | method | that | combines | mul- |     |     |     |     |     |
| ------- | -------- | -------------- | --- | ------ | ---- | -------- | ---- | --- | --- | --- | --- | --- |
ordeepAutoencodermodels.
| tiple weak | learners | into   | a       | robust | predictive | model. | This  |     |     |     |     |     |
| ---------- | -------- | ------ | ------- | ------ | ---------- | ------ | ----- | --- | --- | --- | --- | --- |
| ensemble   | strategy | allows | XGBoost |        | to achieve | high   | accu- |     |     |     |     |     |
racywhilemaintainingefficiencythroughoptimizedmemory B. EVALUATIONPROTOCOL
management and parallel execution. Unlike traditional tree- Toensurefaircomparisonacrossmodels,weapplyauniform
| based models, |     | XGBoost | integrates |     | regularization |     | to reduce |     |     |     |     |     |
| ------------- | --- | ------- | ---------- | --- | -------------- | --- | --------- | --- | --- | --- | --- | --- |
evaluationprotocolbasedon10-foldcross-validationandtest
overfitting and supports handling of sparse input, making set isolation. Unlike standard K-fold workflows, our method
| it suitable   | for | large-scale | telemetry |              | data from         | microservice |     |           |                    |                   |     |             |
| ------------- | --- | ----------- | --------- | ------------ | ----------------- | ------------ | --- | --------- | ------------------ | ----------------- | --- | ----------- |
|               |     |             |           |              |                   |              |     | separates | the test partition | from all training | and | tuning pro- |
| environments. |     | Its balance | of        | scalability, | interpretability, |              | and |           |                    |                   |     |             |
cesses.Algorithm2outlinesafour-stageprocedureformodel
| 1676 |     |     |     |     |     |     |     |     |     |     |     | VOLUME6,2025 |
| ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------ |

classdistribution.Defaulthyperparameterconfigurationsand
| Algorithm | 2:  | Model | Selection | and | Evaluation | using 10- |     |     |     |     |     |     |
| --------- | --- | ----- | --------- | --- | ---------- | --------- | --- | --- | --- | --- | --- | --- |
FoldCross-Validation. therangesusedintuningaredetailedinTables2and3.
Require:DatasetD,hyperparameterspaceH,numberof The performance of the different models was evaluated
foldsK =10 using a range of metrics, including Accuracy, Precision, Re-
Ensure:FinalmodelM ∗ andtestperformanceP call, F1-Score, and AUC [54], as well as execution time,
test
|     |     |     |     |     |     |     | RAM usage, | and CPU | utilization. | The results | obtained | un- |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ------- | ------------ | ----------- | -------- | --- |
Step1:DataSplitting
1: SplitDinto: der various data balancing and hyperparameter optimization
|     |         |         |     |         |            |     | conditions  | are comprehensively |     | summarized      | in Tables  | 4–  |
| --- | ------- | ------- | --- | ------- | ---------- | --- | ----------- | ------------------- | --- | --------------- | ---------- | --- |
|     | D train | (70%),D | val | (20%),D | test (10%) |     |             |                     |     |                 |            |     |
|     |         |         |     |         |            |     | 6, enabling | a direct comparison |     | across methods, | evaluation |     |
Step2:HyperparameterTuningonD
train
2: foreachh∈Hdo metrics,andcomputationalresourceconsumption.Thiscom-
←[] prehensive evaluation tests the generalization capability of
3: InitializeperformancelistL
4: PartitionD intoK =10folds: each model, reducing the risk of overfitting while enhanc-
train
F ,F ,...,F ing predictive accuracy and reliability. This layered design,
|     | 1   | 2   | 10 . |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
fori=1to10do which combines data filtering, balancing, nested validation,
5:
6: T ←D \F,V ←F and final isolation of test sets, supports reproducibility and
|     |             |     | train i |          | i     |     |            |           |           |               |     |          |
| --- | ----------- | --- | ------- | -------- | ----- | --- | ---------- | --------- | --------- | ------------- | --- | -------- |
|     |             |     |         |          |       |     | highlights | the novel | structure | of the ADMXGB |     | training |
| 7:  | TrainmodelM |     | h,i     | onT      |       |     |            |           |           |               |     |          |
| 8:  | EvaluateM   |     | h,i onV | toobtain | p h,i |     | pipeline.  |           |           |               |     |          |
| 9:  | Append      |     | p toL   |          |       |     |            |           |           |               |     |          |
h,i
10: endfor
11: Computemeanperformance p¯ ←mean(L) IV. RESULTSANDDISCUSSION
h
A. DATASET
12: endfor
∗
13: Selecth =argmax p¯ ThedatasetmadeavailablebytheauthorsofTraceRCA[39],
h h
Step3:FinalModelTraining apracticalroot-causelocalisationmethodintroducedin2021,
|     |          | ∗   |       | ∪D  | ∗      |     | wasused.SinceTraceRCAdoesnotprovideexplicitanomaly |     |     |     |     |     |
| --- | -------- | --- | ----- | --- | ------ | --- | -------------------------------------------------- | --- | --- | --- | --- | --- |
| 14: | RetrainM | onD |       |     | usingh |     |                                                    |     |     |     |     |     |
|     |          |     | train | val |        |     |                                                    |     |     |     |     |     |
Step4:FinalEvaluation labels,weannotatedanomaliesbyaligningfaultinjectionlogs
|     |           | ∗   |          |           |      |     | withtracetimestamps.Latencyspikeswereidentifiedusinga |     |     |     |     |     |
| --- | --------- | --- | -------- | --------- | ---- | --- | ----------------------------------------------------- | --- | --- | --- | --- | --- |
| 15: | EvaluateM |     | onD test | toobtainP | test |     |                                                       |     |     |     |     |     |
∗
16: returnM andP statistical criterion: traces with latency exceeding the mean
test
|     |     |     |     |     |     |     | μ plus three                              | standard   | deviations | (μ+3σ)         | of the      | baseline |
| --- | --- | --- | --- | --- | --- | --- | ----------------------------------------- | ---------- | ---------- | -------------- | ----------- | -------- |
|     |     |     |     |     |     |     | distributionwerelabeledasanomalous.This3σ |            |            |                | rulehasbeen |          |
|     |     |     |     |     |     |     | widely used                               | in anomaly | detection  | to distinguish | abnormal    |          |
selection and evaluation, combining 10-fold cross-validation valuesfromnaturalfluctuations[56],[57].
withanexplicittrain/validation/testsplit. Most existing studies based on the TraceRCA dataset pri-
First, the dataset D is partitioned into training (D ), marily utilize metrics tailored for RCA, so to provide a
train
validation (D ), and test (D ) sets. The test set is held fair and transparent comparison, we benchmark ADMXGB
|     |     | val |     | test |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
out entirely for final evaluation. Note that D test is initialized againstninewidelyadoptedanomaly-detectionbaselinesthat
during the first data split and is never subject to threshold aredataset-agnosticandhavepublicimplementations.
filtering or balancing, ensuring unbiased evaluation of the While we acknowledge the importance of multi-dataset
finalmodel.Algorithm2doesnotoperatedirectlyontheraw validation, the TraceRCA dataset was selected due to its
datasetD.Instead,itreceivesasinputthepreprocesseddataset real-world characteristics, comprehensive labelling, and het-
(cid:6)
D,whichresultsfromAlgorithm1(ADMXGB)afterapply- erogeneous trace patterns. Additionally, its substantial size
ing latency thresholding, data cleaning, feature scaling, and (5.5GB)andvolume(over85millionentries)offerarealistic
balancing.Next,hyperparametertuningisperformedonD and challenging benchmark for anomaly detection methods.
train
h∈H
using 10-fold cross-validation. Each configuration is Its widespread adoption in recent anomaly detection studies
evaluated across folds, and the average performance p¯ is furtherreinforcesitssuitabilityasabenchmarkforevaluating
h
∗
computed. The best configuration h is selected. Then, the microservices-basedmethods.
|     |     | ∗   |     |     |     | ∗   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
final model M is trained using D ∪D and h . Finally, Tobetterunderstandthecharacteristicsofthedataset,sev-
|     |     |     |     | train | val |     |     |     |     |     |     |     |
| --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
M ∗ is evaluated on D , yielding the test performance P . eral preliminary checks were conducted. No missing values
|     |     |     | test |     |     | test |     |     |     |     |     |     |
| --- | --- | --- | ---- | --- | --- | ---- | --- | --- | --- | --- | --- | --- |
Thisapproachensuresreliablemodelselectionwhileprevent- were identified, thus eliminating the need for imputation.
ingdataleakage. However, an anomaly was detected: 37 records contained
ThispipelineisappliedtoADMXGBandallbaselinemod- negative latency values, which required careful handling to
els. These include classical algorithms (e.g., Decision Trees, preserve dataintegrity.Feature selectionwasapplied, retain-
Naive Bayes, KNN), as well as advanced ensemble learners ingthefollowingattributes:latency,source,target,andsucc.
(e.g., Random Forest, LightGBM, XGBoost) and deep mod- To ensure compatibility with algorithms that require numer-
els(Autoencoders).Theobjectivefunctioninhyperparameter ical inputs (e.g., XGBoost, LightGBM, and ADMXGB), the
tuningmaximizestheaverageF1-scoretohandletheskewed categoricalattributessource,target,andsuccweremappedas
| VOLUME6,2025 |     |     |     |     |     |     |     |     |     |     |     | 1677 |
| ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |

BARATAETAL.:CLASSIFICATIONOFANOMALIESINMICROSERVICESUSINGANXGBOOST-BASEDAPPROACHWITHDATABALANCING
TABLE2. DefaultHyperparametersforAnomalyDetectionMethods
TABLE3. ValuesUsedforRandomandGridSearchMethods
TABLE4. PerformanceComparison(MeanTrainAccuracy,TestAccuracy,andF1-Score)ofImbalancedvs.BalancedSamplingMethods
integer values. Additionally, the class distribution was anal- 161.587 ms, the median is 1 ms, and the 95th percentile
ysedtoassesspotentialimbalance(seeTable7). is 34 ms. Consequently, more than 95% of traces fall
The latency distribution in TraceRCA exhibits a pro- below34ms,whichweconsiderthenormaloperatingrange.
nounced right skew typical of microservice workloads. The Adopting a statistical criterion, we set the anomaly thresh-
mean latency is 9.758 ms with a standard deviation of old at μ+3σ ≈494.520 ms. Although this criterion does
1678 VOLUME6,2025

TABLE5. PerformanceComparison(Precision,RecallandAUC)ofImbalancedvs.BalancedSamplingMethods
TABLE6. PerformanceComparison(ExecutionTime,MemoryUsageandCPUUsage)ofImbalancedvs.BalancedSamplingMethods
TABLE7. ClassImbalanceCalculation (SMOTE, RandomUnderSampler, SMOTEENN). Hyperpa-
|     |     |     |     |     | rameter             | optimisation | was | performed | using    | GridSearchCV, |        |
| --- | --- | --- | --- | --- | ------------------- | ------------ | --- | --------- | -------- | ------------- | ------ |
|     |     |     |     |     | RandomizedSearchCV, |              | and | Hyperopt  | (v0.2.7) | with          | TPE as |
thesearchalgorithm.
|     |     |     |     |     | The experiments     |     | were | executed | on a local | testbed   | with an |
| --- | --- | --- | --- | --- | ------------------- | --- | ---- | -------- | ---------- | --------- | ------- |
|     |     |     |     |     | Intel CoreTMi7-8700 |     | CPU  | @ 3.20   | GHz (12    | threads), | 64 GB   |
RAM,andUbuntu22.04.4LTS64-bit.Allcodewasrunusing
| not assume | normality, | it effectively | captures | rare latency |     |     |     |     |     |     |     |
| ---------- | ---------- | -------------- | -------- | ------------ | --- | --- | --- | --- | --- | --- | --- |
acontrolledvirtualenvironment(venv)toensureconsistency
| spikes. In | the full dataset | (N =85,561,389), |     | this rule flags |     |     |     |     |     |     |     |
| ---------- | ---------------- | ---------------- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- |
acrossruns.
| approximately | 0.05% | of traces as anomalous, |     | underscoring |     |     |     |     |     |     |     |
| ------------- | ----- | ----------------------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- |
Thecompletesourcecode,configurationfiles,trainedmod-
therarityofextremedelays.
|     |     |     |     |     | els, and | preprocessing | scripts | are | publicly | available | in our |
| --- | --- | --- | --- | --- | -------- | ------------- | ------- | --- | -------- | --------- | ------ |
Thisevaluationhelpeddeterminewhethertechniquessuch GitHub repository [58]. The dataset used (TraceRCA) was
asresamplingorclassweightingwouldbenecessarytomiti-
preprocessedusingtimestampsprovidedinthefaultinjection
gateskewedclassdistributions.
|     |     |     |     |     | logs to label | anomalous |           | traces. Our | processed | version  | of the   |
| --- | --- | --- | --- | --- | ------------- | --------- | --------- | ----------- | --------- | -------- | -------- |
|     |     |     |     |     | dataset is    | also      | available | via Zenodo  | [59],     | ensuring | that all |
B. TESTBEDANDREPRODUCIBILITY resultscanbereproducedandverified.
AllexperimentswereimplementedinPython(v3.12.3),using
| the following | key libraries: | Scikit-learn | (v1.5.2) | for general |     |     |     |     |     |     |     |
| ------------- | -------------- | ------------ | -------- | ----------- | --- | --- | --- | --- | --- | --- | --- |
machine learning tasks, Pandas (v2.2.3) for data manipu- C. IMPACTOFLATENCYTHRESHOLD
lation, NumPy (v2.0.2) for numerical operations, XGBoost AspreviouslydescribedinSectionIII,thelatencythresholdτ
(v2.1.1) and LightGBM (v4.1.0) for gradient boosting mod- wasvariedtoassessitseffectonperformanceandefficiency.
els, and Imbalanced-learn (v0.12.4) for sampling techniques TheADMXGBmodelwasevaluatedacrossarangeofvalues
| VOLUME6,2025 |     |     |     |     |     |     |     |     |     |     | 1679 |
| ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |

BARATAETAL.:CLASSIFICATIONOFANOMALIESINMICROSERVICESUSINGANXGBOOST-BASEDAPPROACHWITHDATABALANCING
TABLE8. ImpactofLatencyThreshold(τ)onADMXGBPerformance
for τ : 0 (no filtering), 5, 10, 20, 50, 100, 200, 500, and reactdifferentlytobalancingstrategies.Oversamplingboosts
1000 ms. Table 8 presents the results in terms of F1-Score, minority class representation, with LightGBM, KNN, and
accuracy,executiontime,andbesthyperparameters(forGrid ADMXGB showing notable gains in Recall and F1-score.
Searchwithdatabalancedviaundersampling). However, it increases computational cost, particularly for
Aparticularlyinterestingobservationisrelatedtoexecution resource-heavymodelslikeAutoencoders.
time. Contrary to expectations, lower thresholds, which cor- In contrast, undersampling reduces the dataset size by re-
respond to significantly larger datasets, do not always result movingmajorityclasssamples,easingresourceusebutoften
in longer training times. For example, with τ =1000, the lowering F1-score and AUC for models like Decision Trees
training set contains only 68,039 samples, yet the execution andRandomForests.ADMXGBstaysrelativelystable,while
timereaches3,197seconds.Incontrast,atτ =10,themodel KNNandLightGBMperformvariably.
processes more than 8.9 million records but completes train- Hybridsampling,combiningbothmethods,provesmostef-
inginjust1,154seconds. fective. It enhances performance while mitigating individual
This counterintuitive result can be attributed to the drawbacks. ADMXGB and LightGBM reach near-optimal
increased complexity of the models trained on smaller AUCandF1-scores,withXGBoostandRandomForestsalso
datasets. At higher thresholds (e.g., τ =1000 and τ = benefiting,thoughathigherresourcecost.Overall,itimproves
500),theselectedhyperparametersincludedeepertrees(e.g., modelrobustnessandgeneralisation.
max_depth=7) and higher learning rates. These configu- Although dataset balancing is a common strategy to mit-
rations, when applied to limited and less diverse data, can igate the bias caused by the extreme class imbalance [60],
leadtooverfittingandlongerconvergencetimes,asthemodel [61], the results indicate that for certain algorithms, such as
strugglestolearngeneralizedpatterns. Decision Tree, KNN, Gaussian Naive Bayes, and Isolation
Incontrast,withlowerthresholdsandmorecomprehensive Forest,theF1-scorevalueswerehigherwhenusingtheorigi-
datasets,themodelconvergesfasterusingshallowertreesand nal,imbalanceddataset.Whilethismightseemcontradictory,
smallerlearningrates.Thelargerdatasetsizeprovidesricher, itcanbeexplainedbythefactthatsomemethodstendtoover-
morerepresentativepatterns,allowingthelearningprocessto fit to synthetic patterns introduced by balancing techniques,
bebothmorestableandefficient. particularlyoversampling[62],[63],[64].
Thesefindingsdemonstratethatapplyingalatencythresh-
oldisnotmerelyafilteringmechanismbutalsoadeterminant
oflearningefficiency.Modelstrainedonheavilyfiltereddata E. IMPACTOFHYPERPARAMETERSOPTIMIZATION
(high τ) may experience inflated training times, even with Hyperparameter tuning using Grid Search, Random Search,
smaller datasets, due to hyperparameter-driven complexity and HyperOPT raises Precision, Recall, F1Score, and AUC
andreduceddatavariance. towardtheoreticallimits,complementingdatabalancing.Grid
Search exhaustively tests every parameter set and yields top
D. IMPACTOFBALANCINGTHEDATASET performance, but its exponential runtime is prohibitive on
Dataset balancing improves model performance, especially large data. Random Search and HyperOPT explore only part
with class-imbalanced data. Results show that models of the space, sacrificing a little Accuracy for much lower
1680 VOLUME6,2025

resource-constrainedscenarios.Balancingmethods,including
|     |     |     |     |     |     |     | oversampling, |           | undersampling, |        | and hybrid  | strategies, |                | further    |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --------- | -------------- | ------ | ----------- | ----------- | -------------- | ---------- |
|     |     |     |     |     |     |     | refine model  | outcomes. |                | Hybrid | approaches, |             | in particular, | ef-        |
|     |     |     |     |     |     |     | fectively     | merge     | the strengths  |        | of both     | techniques, |                | benefiting |
ADMXGBandLightGBM.Hyperparametertuningenhances
|     |     |     |     |     |     |     | model performance |             | but            | varies          | in computational |        | cost:    | Grid      |
| --- | --- | --- | --- | --- | --- | --- | ----------------- | ----------- | -------------- | --------------- | ---------------- | ------ | -------- | --------- |
|     |     |     |     |     |     |     | Search            | is thorough | yet            | resource-heavy, |                  | Random |          | Search is |
|     |     |     |     |     |     |     | faster but        | less        | comprehensive, |                 | and HyperOpt     |        | balances | accu-     |
racyandefficiencymoreeffectively.
|     |     |     |     |     |     |     | Hyperparameter |     | optimisation |     | and | sampling | strategies | act |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ------------ | --- | --- | -------- | ---------- | --- |
synergisticallyonADMXGBperformance:
|     |     |     |     |     |     |     | 1) Precision |     | boost: On | the | raw, highly | imbalanced |     | Trac- |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --- | --------- | --- | ----------- | ---------- | --- | ----- |
eRCAdatathemodelachievesonly18.36%Precision;
FIGURE2. Comparativeperformancemetrics(Accuracy,Precision,Recall, RandomSearch+hybridsamplingliftsthisto99.95%,
F1-Score)ofallevaluatedmethodstrainedonhybrid-balanceddatawith
animprovementof+81.6%;
hyperparametertuningviaGridSearch.Inthisscenario,ADMXGB
|     |     |     |     |     |     |     | 2) Recallrecovery:Whileaggressivetuningontheunbal- |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
demonstratesthemostsignificantperformancegainsoverthebaseline
| methods. |     |     |     |     |     |     | anced | set | may drive | Recall | down | to  | 6.82%, | applying |
| -------- | --- | --- | --- | --- | --- | --- | ----- | --- | --------- | ------ | ---- | --- | ------ | -------- |
SMOTEbeforetrainingrestoresitto99.99%(+93.2%);
|              |            |     |          |       |              |      | 3) Globalbalance(F1-Score,AUC):GridSearch+hybrid |     |             |         |        |            |     |         |
| ------------ | ---------- | --- | -------- | ----- | ------------ | ---- | ------------------------------------------------ | --- | ----------- | ------- | ------ | ---------- | --- | ------- |
| computation; | HyperOPT’s |     | Bayesian | focus | often rivals | Grid |                                                  |     |             |         |        |            |     |         |
|              |            |     |          |       |              |      | sampling                                         |     | aligns both | classes | almost | perfectly, |     | pushing |
oncomplextasks.
|             |      |        |              |     |                 |     | F1-Score |     | and AUC | to  | 99.97% | and | 99.96%, | respec- |
| ----------- | ---- | ------ | ------------ | --- | --------------- | --- | -------- | --- | ------- | --- | ------ | --- | ------- | ------- |
| Experiments | show | tuning | particularly |     | aids imbalanced |     |          |     |         |     |        |     |         |         |
tively.HyperOPTachievesthesameAUCwithonlyone
data:ADMXGBexcelswithGridandHyperOPT;LightGBM
|     |     |     |     |     |     |     | third | of  | the search | budget, | confirming |     | the efficiency | of  |
| --- | --- | --- | --- | --- | --- | --- | ----- | --- | ---------- | ------- | ---------- | --- | -------------- | --- |
andXGBoostimproveunderallthree.AutoencodersandIso-
Bayesianhyperparameteroptimisation;
| lation Forests | gain | most | from Grid | yet incur | heavy | costs, |                                                    |     |     |     |     |     |     |     |
| -------------- | ---- | ---- | --------- | --------- | ----- | ------ | -------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
|                |      |      |           |           |       |        | 4) Resourcefootprint:Balancingaddsnegligiblememory |     |     |     |     |     |     |     |
whileDecisionTreesandGaussianNaiveBayeschangelittle,
|     |     |     |     |     |     |     | overhead |     | (<1 GB) | and | hyperparameter |     | optimisation |     |
| --- | --- | --- | --- | --- | --- | --- | -------- | --- | ------- | --- | -------------- | --- | ------------ | --- |
reflectingweaktuningdependence.
|                  |          |                |           |            |              |     | adds       | modest | CPU      | overhead   | (20%) | when   | Bayesian | op-     |
| ---------------- | -------- | -------------- | --------- | ---------- | ------------ | --- | ---------- | ------ | -------- | ---------- | ----- | ------ | -------- | ------- |
| Selecting        | a tuning | method         | therefore | means      | balancing    | ac- |            |        |          |            |       |        |          |         |
|                  |          |                |           |            |              |     | timisation |        | is used; | exhaustive | Grid  | Search | can      | be over |
| curacy, runtime, |          | and resources, | which     | is crucial | for realtime |     |            |        |          |            |       |        |          |         |
oneorderofmagnitudeslowerandshouldthereforebe
anomalydetectionandotherlargescaleapplications.
reservedforofflinere-training.
|     |     |     |     |     |     |     | Among        | the    | tested methods, |         | ADMXGB |           | demonstrates | a   |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ------ | --------------- | ------- | ------ | --------- | ------------ | --- |
|     |     |     |     |     |     |     | particularly | strong | balance         | between |        | Accuracy, | Recall,      | and |
F. VALIDATION
The experimental results show that the proposed ADMXGB execution time, making it a suitable candidate for near real-
framework outperforms the Accuracy figures commonly re- time anomaly detection in microservices. This performance
ported in the literature (see Table 1). Whereas most recent is primarily attributed to two synergistic mechanisms. First,
studiesonmicroserviceanomalydetectionremainintherange the introduction of a configurable latency threshold (τ) en-
ablesthemodeltodisregardlow-latencytracesthattypically
of85%–99%AccuracyandRecall,ADMXGBreaches:upto
99.96% test Accuracy, 99.95% Precision, 99.99% Recall, a introduce noise and false positives. Second, the systematic
99.97% F1-Score and an AUC of 99.96%. These values are integration of data balancing strategies with hyperparame-
obtainedunderthefollowingconfigurations: ter optimisation, validated through 10-fold cross-validation,
(cid:2)
GridSearch+hybridsampling:Accuracy=99.96%,F1- enhances model generalization and stability. Furthermore,
Score=99.97%,AUC=99.96%; ADMXGB leverages hybrid sampling to address class im-
(cid:2)
Precision=99.95%
Random Search + hybridsampling: balance and employs efficient optimisation algorithms such
(+81.6%overtheimbalancedbaseline); as HyperOpt to maintain resource efficiency. These mecha-
(cid:2)
Random Search + oversampling (SMOTE): Recall nismsareparticularlyeffectiveinthecontextoftheTraceRCA
=99.99%(+93.2%overtheimbalancedbaseline); dataset, where subtle anomaly patterns challenge traditional
(cid:2)
No tuning + imbalanced dataset: Train-Accuracy = models. ADMXGB’s gradient boosting structure proves es-
99.96%(upperboundonfittingcapacity). pecially robust under undersampling and hybrid sampling
ADMXGBconsistentlyachieveshighAccuracy,Precision, conditions, achieving consistently high precision and F1-
andRecall(seeFig.2),maintainingnear-real-timeexecution Scorewhilemaintainingpracticalexecutiontimes(seeFig.3).
| even under | higher | CPU and | memory | usage, | making | it well- |     |     |     |     |     |     |     |     |
| ---------- | ------ | ------- | ------ | ------ | ------ | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
suitedfor rapidanomaly detection. Incomparison, XGBoost G. COMPUTATIONALPERFORMANCECOMPARISON
and LightGBM offer competitive Accuracy but require ex- FollowingrecommendationsfromtheAI-CentricComputing
tensive tuning, increasing computational costs in large-scale ContinuumSystemsframework[65],weextendedtheevalu-
settings. Autoencoders and Isolation Forests, while effective ationbeyondaccuracy-relatedmetricstoincludesystem-level
in specific cases, are memory-intensive and less suitable for indicators such as CPU utilization, memory footprint, and
| VOLUME6,2025 |     |     |     |     |     |     |     |     |     |     |     |     |     | 1681 |
| ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |

BARATAETAL.:CLASSIFICATIONOFANOMALIESINMICROSERVICESUSINGANXGBOOST-BASEDAPPROACHWITHDATABALANCING
Ourmethodisespeciallysuitedforscenarioswhereteleme-
|     |     |     |     | try is abundant |     | but | computational |     | efficiency | is  | a priority, |
| --- | --- | --- | --- | --------------- | --- | --- | ------------- | --- | ---------- | --- | ----------- |
suchascontinuousdeliverypipelinesorautoscalingdecision-
|     |     |     |     | making   | processes. | While | the      | evaluation         | was | conducted | on        |
| --- | --- | --- | --- | -------- | ---------- | ----- | -------- | ------------------ | --- | --------- | --------- |
|     |     |     |     | a single | real-world |       | dataset, | the methodological |     |           | design is |
dataset-agnosticandcanbereplicatedonothertelemetry-rich
environments.
|     |     |     |     | Inpractice,thelatencythresholdτ |     |     |     |     | shouldbecalibratedto |     |     |
| --- | --- | --- | --- | ------------------------------- | --- | --- | --- | --- | -------------------- | --- | --- |
theapplicationbaselineperformance.Arecommendedguide-
lineistocomputethemeanlatencyμduringstableoperation
|     |     |     |     | and set      | τ between | μ+2σ         |     | and μ+3σ,   | depending |       | on the     |
| --- | --- | --- | --- | ------------ | --------- | ------------ | --- | ----------- | --------- | ----- | ---------- |
|     |     |     |     | acceptable   | trade-off | between      |     | sensitivity | and       | false | positives. |
|     |     |     |     | This ensures | that      | thresholding |     | remains     | aligned   | with  | system-    |
specificperformance.
FutureextensionswillvalidateADMXGBondifferentmi-
|     |     |     |     | croservices | platforms |     | and explore | its | integration | with | AIOps |
| --- | --- | --- | --- | ----------- | --------- | --- | ----------- | --- | ----------- | ---- | ----- |
pipelinesforautomatedroot-causeidentificationandanomaly
|     |     |     |     | response. | In this | context, | ADMXGB |     | can be | embedded | into |
| --- | --- | --- | --- | --------- | ------- | -------- | ------ | --- | ------ | -------- | ---- |
modernmonitoringarchitecturesbasedonobservabilitytools
FIGURE3. Resourceusageofmethodsusingdatabalancedwith like Prometheus, Jaeger, or OpenTelemetry. The model may
hybridsamplingandhyperparametertuningviaHyperopt. actasadedicatedanomalydetectionmicroservice,processing
|     |     |     |     | telemetry | in real-time |     | or batch | mode | and | emitting | alerts to |
| --- | --- | --- | --- | --------- | ------------ | --- | -------- | ---- | --- | -------- | --------- |
execution time. These additional parameters are reported in externalsystemssuchasGrafanaorSlack.
Table 6 and Fig. 3, providing a comprehensive view of the The performance of ADMXGB can be explained by the
operationalcostofADMXGBcomparedtobaselinemodels. combinedeffectofthreefactors:(i)latencythresholdfiltering,
The results confirm that ADMXGB maintains competitive whichremoveslow-latencynoiseandreducesfalsepositives,
| efficiency | while significantly | improving anomaly | detection |            |            |       |          |     |             |     |            |
| ---------- | ------------------- | ----------------- | --------- | ---------- | ---------- | ----- | -------- | --- | ----------- | --- | ---------- |
|            |                     |                   |           | (ii) class | balancing, | which | prevents |     | bias toward |     | the major- |
performance. ity class and enhances recall for anomalous cases, and (iii)
Execution time, memory usage, and CPU utilization show systematic hyperparameter tuning, which improves general-
clear trade-offs between algorithms, sampling strategies, and ization by exploring a broader parameter space. Together,
tuning methods. ADMXGB is fastest with undersampling these elements create a synergy that allows ADMXGB to
(BDU)andminimaltuning,reaching64s(RandomSearch), outperform baselines not only in accuracy-related measures
but oversampling (BDO) or hybridsampling (BDH) with ex- but also in terms of stability and efficiency, as shown in
| haustivetuningcanexceed41,000s.Tree-basedmodelsgen- |     |     |     | Tables4–6. |     |     |     |     |     |     |     |
| --------------------------------------------------- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
erallytake2,000–8,000s,whileAutoencodersarehighlyvari- Furthermore, ADMXGB can be coupled with Gambi-
able, sometimes extreme. In memory, Gaussian Naive Bayes tRCA [66], a complementary framework for root-cause
and Robust Covariance use under 2 GB, tree-based mod- analysis based on cooperative game theory. In this com-
els remain moderate (2–7 GB), and Autoencoder/ADMXGB bined pipeline, ADMXGB first detects anomalous traces,
can peak very high (e.g., 63.49 GB for Autoencoder with which are then processed by GambitRCA to identify the
BDO and Random Search) due to dataset size and search most probable components responsible for the incident.
space. For CPU, ADMXGB often reaches the highest loads This layered approach enhances the reliability and inter-
(up to 95.40%) in balanced datasets with exhaustive tuning, pretabilityofanomalymanagementincomplexmicroservice
| whereasDecisionTreesandGaussianNaiveBayesstaybelow |                 |                          |       | systems. |     |     |     |     |     |     |     |
| -------------------------------------------------- | --------------- | ------------------------ | ----- | -------- | --- | --- | --- | --- | --- | --- | --- |
| 10%, making                                        | them preferable | for resource-constrained | envi- |          |     |     |     |     |     |     |     |
ronments.
I. THREATSTOVALIDITY
H. IMPLICATIONSANDPRACTICALIMPACT Severalfactorsmayaffectthevalidityofourfindings.Inter-
The ADMXGB framework addresses key operational chal- nal validity may be limited by the use of a single dataset
lenges in microservices environments by offering a practical (TraceRCA); however, its real-world origin, fault diversity,
and lightweight anomaly detection mechanism. The use of and volume mitigate this concern. External validity could
latencythresholdingreducesCPUandmemoryusage,making be impacted by architectural differences in other microser-
it viable for near real-time deployment in edge or container- vice systems. Future work will address this by including
izedinfrastructures.Moreover, theuseofdatabalancing and other datasets. Construct validity depends on the chosen
hyperparameter tuning allows the model to adapt to highly evaluation metrics, which, although standard, may not cap-
imbalanced and dynamic workloads, which are frequent in ture interpretability or robustness. Conclusion validity is
productionmicroservicesystems. supported by reproducibility, 10-fold cross-validation, and
| 1682 |     |     |     |     |     |     |     |     |     |     | VOLUME6,2025 |
| ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------ |

multipleoptimisationstrategies,reducingbiasandoverfitting
|     |     |     |     |     |     |     | [6] S.Wolfe,“Amazon’sonehourofdowntimeonPrimeDaymayhave |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
costitupto$100millioninlostsales,”2018.Accessed:Apr.21,2024.
risks.
|     |     |     |     |     |     |     | [Online]. | Available: | https://www.businessinsider.com/amazon-prime- |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------- | ---------- | --------------------------------------------- | --- | --- | --- | --- | --- |
day-website-issues-cost-it-millions-in-lost-sales-2018-7
V. CONCLUSION [7] P.Wang,X.Zhang,andZ.Cao,“Anomalydetectionformicroservice
Effective anomaly detection in microservices requires bal- system via augmented multimodal data and hybridgraph representa-
tions,”Inf.Fusion,vol.118,2025,Art.no.103017.
ancing data handling, hyperparameter tuning, and resource [8] M. Raeiszadeh, A. Ebrahimzadeh, R. H. Glitho, J. Eker, and R. A.
efficiency. Our results show that hybridsampling achieves F.Mini,“Asynchronousreal-timefederatedlearningforanomalyde-
the highest Recall, F1-Score, and AUC across models like tectioninmicroservicecloudapplications,”IEEETrans.Mach.Learn.
Commun.Netw.,vol.3,pp.176–194,2025.
ADMXGB, LightGBM, and XGBoost, while keeping high [9] H. Ge et al., “SRdetector: Sequence reconstruction method for mi-
values of Accuracy. Oversampling improves minority-class croservice anomaly detection,” Electronics, vol. 14, no. 1, 2025,
Art.no.65.
representation,itincreasesmemoryusage,especiallyforAu-
|     |     |     |     |     |     |     | [10] M.S.Haq,“Data-centricanalysisofsecurityandprivacyofcontainer- |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- |
toencoders.Undersampling,thoughfaster,riskslosingcritical
|     |     |     |     |     |     |     | ized | applications,” | Ph.D. | dissertation, | Univ. | Texas | San Antonio, | San |
| --- | --- | --- | --- | --- | --- | --- | ---- | -------------- | ----- | ------------- | ----- | ----- | ------------ | --- |
data.However,combiningitwithADMXGBoffersapractical Antonio,TX,USA,2024.
|     |     |     |     |     |     |     | [11] X.Li,P.Wen,P.Chen,J.Chen,X.Wen,andY.Xia,“Aneffectiveparal- |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
trade-offforreal-timeapplications.
lelconvolutionalanomalymulti-classificationmodelforfaultdiagnosis
| For hyperparameter |     | tuning, | Grid | Search | is thorough | but |     |     |     |     |     |     |     |     |
| ------------------ | --- | ------- | ---- | ------ | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
inmicroservicesystem,”Softw.Qual.J.,vol.32,pp.921–938,2024.
computationally expensive. Random Search provides a cost- [12] W.Xiong,W.Chen,J.Liu,andK.Zhao,“Ananomalydetectionframe-
workforsystemlogsbasedonensemblelearning,”inProc.PacificRim
| effective | alternative, | while | HyperOpt | optimally | balances | ac- |     |     |     |     |     |     |     |     |
| --------- | ------------ | ----- | -------- | --------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Int.Conf.TrendsArtif.Intell.,2023,vol.14325,pp.52–65.
curacyandefficiency,especiallyforlarge-scalesystems.Our
|     |     |     |     |     |     |     | [13] M. Steidl, | M.  | Leitner, | P. Urbanke, | M.  | Gattringer, | M. Felderer, | and |
| --- | --- | --- | --- | --- | --- | --- | --------------- | --- | -------- | ----------- | --- | ----------- | ------------ | --- |
method adapts well to different strategies, maintaining high S. Ristov, “Understanding microservice runtime monitoring data for
Proc. Int.
detection rates even in the presence of class imbalance. Ul- anomaly detection with structural equation modeling,” in
|     |     |     |     |     |     |     | Conf. | Product-Focused |     | Softw. | Process. | Improvement | Conf., | in Lec- |
| --- | --- | --- | --- | --- | --- | --- | ----- | --------------- | --- | ------ | -------- | ----------- | ------ | ------- |
timately, practitioners must balance recall, precision, and ture Notes in Computer Science, D. Pfahl, J. Gonzalez Huerta, J.
resource constraints. Undersampling with ADMXGB suits Klünder, and H. Anwar, Eds., Cham, Switzerland, 2025, vol. 15452,
fast detection, while hybridsampling with advanced optimi- pp.404–413.
|     |     |     |     |     |     |     | [14] J. Nobre, | E.  | J. S. Pires, | and | A. Reis, | “Anomaly | detection | in  |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ------------ | --- | -------- | -------- | --------- | --- |
sation(e.g.,HyperOpt)maximisesperformance. microservice-based systems,” Appl. Sci., vol. 13, no. 13, 2023,
| WhilethisworkfocusedonXGBoost,thethresholdingand |     |     |     |     |     |     | Art.no.7891.                                                       |     |     |     |     |     |     |     |
| ------------------------------------------------ | --- | --- | --- | --- | --- | --- | ------------------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- |
|                                                  |     |     |     |     |     |     | [15] D.R.Mathews,“Applicationserviceresilienceincloud:Anend-to-end |     |     |     |     |     |     |     |
balancingcomponentsofADMXGBaremodel-agnosticand
perspective,”M.S.Thesis,Dept.Comput.Sci.Automat.,IndianInst.of
canbeappliedtootherlearnerssuchasLightGBM,Random Sci.(IISC),Bangalore,India,2025.
Forests, or deep neural networks, further broadening the ap- [16] L. Vigoya, A. Pardal, D. Fernandez, and V. Carneiro, “Application
|     |     |     |     |     |     |     | of machine | learning | algorithms |     | for the | validation | of a new | CoAP- |
| --- | --- | --- | --- | --- | --- | --- | ---------- | -------- | ---------- | --- | ------- | ---------- | -------- | ----- |
plicabilityoftheframework.
|          |     |         |                |      |                |     | IoT anomaly |     | detection | dataset,” | Appl. | Sci., vol. | 13, no. | 7, 2023, |
| -------- | --- | ------- | -------------- | ---- | -------------- | --- | ----------- | --- | --------- | --------- | ----- | ---------- | ------- | -------- |
| Although | the | results | are promising, | this | study presents |     |             |     |           |           |       |            |         |          |
Art.no.4482.
somelimitations.Theanalysiswasconductedusinganexten- [17] L.Vigoya,D.Fernandez,V.Carneiro,andF.J.Nóvoa,“IoTdataset
validationusingmachinelearningtechniquesfortrafficanomalydetec-
| sive and | realistic, | yet single | real-world | dataset | (TraceRCA), |     |     |     |     |     |     |     |     |     |
| -------- | ---------- | ---------- | ---------- | ------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
tion,”Electronics,vol.10,no.22,2021,Art.no.2857.
| which may | limit | generalizability |     | across different | microser- |     |                 |          |     |         |         |                 |           |     |
| --------- | ----- | ---------------- | --- | ---------------- | --------- | --- | --------------- | -------- | --- | ------- | ------- | --------------- | --------- | --- |
|           |       |                  |     |                  |           |     | [18] S. Garcia, | “IoT-23: | A   | labeled | dataset | for IoT network | intrusion | de- |
vice platforms and workloads. Moreover, while supervised tection,” 2020. Accessed: Apr. 29, 2025. [Online]. Available: https:
//www.stratosphereips.org/datasets-iot23
| learning    | yields high | accuracy, | it           | depends heavily | on        | labelled |                  |          |             |              |               |                |                      |       |
| ----------- | ----------- | --------- | ------------ | --------------- | --------- | -------- | ---------------- | -------- | ----------- | ------------ | ------------- | -------------- | -------------------- | ----- |
|             |             |           |              |                 |           |          | [19] H. Benaddi, |          | M. Jouhari, | K. Ibrahimi, |               | J. Ben Othman, | and                  | E. M. |
| data, which | is often    | scarce    | or expensive | to              | obtain in | oper-    |                  |          |             |              |               |                |                      |       |
|             |             |           |              |                 |           |          | Amhoud,          | “Anomaly | detection   |              | in industrial | IoT            | using distributional |       |
ational environments. Future work will aim to extend this reinforcementlearningandgenerativeadversarialnetworks,”Sensors,
approach tomultipledatasets,exploreunsupervisedorsemi- vol.22,no.21,2022,Art.no.8085.
|     |     |     |     |     |     |     | [20] N.MoustafaandJ.Slay,“Unsw-Nb15dataset,”2015.Accessed:Apr. |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
supervised labelling techniques, and integrate more detailed 29, 2025. [Online]. Available: https://www.unsw.adfa.edu.au/unsw-
telemetrydata(e.g.,logs,metrics,traces)tosupportnotonly canberra-cyber/cybersecurity/ADFA-NB15-Datasets/
detectionbutalsoaccuraterootcauselocalisationincomplex [21] L. Landim, L. Barata, and E. Lopes, “A simple approach to detect
anomaliesinmicroservices-basedsystemsusingPYOD,”inProc.22a
environments. Conferência da Associação Portuguesa de Sistemas de Informação,
Nov.2022,pp.177–186.
|     |     |     |     |     |     |     | [22] N.Bugshan,I.Khalil,andA.Kalapaaking,“Intrusiondetection-based |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- |
REFERENCES
ensemblelearningandmicroservicesforzerotouchnetworks,”IEEE
Commun.Mag.,vol.61,no.6,pp.86–92,Jun.2023.
[1] M.Brandón,A.Solé,D.Huélamo,M.S.SolansServicePérez,andV.
Muntés-Mulero,“Graph-basedrootcauseanalysisforservice-oriented [23] Q.Du,L.Zhao,F.Tian,andY.Han,“Trace-basedanomalydetection
and microservice architectures,” J. Syst. Softw., vol. 159, Jan. 2020, withcontextualsequentialinvocations,”inProc.Int.Conf.Database
| Art.no.110432. |     |     |     |     |     |     | ExpertSyst.Appl.,2023,pp.113–118. |     |     |     |     |     |     |     |
| -------------- | --- | --- | --- | --- | --- | --- | --------------------------------- | --- | --- | --- | --- | --- | --- | --- |
[2] C. Fetzer, “Building critical applications using microservices,” IEEE [24] Y.Gan,G.Liu,X.Zhang,Q.Zhou,andJ.Wu,“Sleuth:Atrace-based
Secur.Privacy,vol.14,pp.86–89,Nov./Dec.2016. root cause analysis system for large-scale microservices with graph
[3] S. Newman, Building Microservices. 1st ed. Sebastopol, CA, USA: neural networks,” in Proc. 28th ACM Symp. Operating Syst. Princ.,
| O’ReillyMedia,Inc.,2015. |     |     |     |     |     |     | 2023,pp.324–337. |     |     |     |     |     |     |     |
| ------------------------ | --- | --- | --- | --- | --- | --- | ---------------- | --- | --- | --- | --- | --- | --- | --- |
[4] M.Fowler,“Microservicesdefinition,”2024.Accessed:Apr.20,2024. [25] L. Pham, H. Zhang, H. Ha, F. Salim, and X. Zhang, “RCAEval: A
[Online]. Available: https://martinfowler.com/articles/microservices. benchmarkforrootcauseanalysisofmicroservicesystemswithteleme-
| html |     |     |     |     |     |     | trydata,”inProc.CompanionACMWebConf.,2025,pp.777–780. |     |     |     |     |     |     |     |
| ---- | --- | --- | --- | --- | --- | --- | ----------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
[5] D.Inc.,“Docker:Accelerated,containerizedapplicationdevelopment,” [26] R.Ren,Y.Wang,F.Liu,Z.Li,andG.Tyson,“Grace:Interpretableroot
2011. Accessed: Apr. 20, 2024. [Online]. Available: https://www. causeanalysisbygraphconvolutionalnetworkformicroservices,”in
docker.com/ Proc.IEEE/ACM31stInt.Symp.Qual.Serv.,2023,pp.1–4.
| VOLUME6,2025 |     |     |     |     |     |     |     |     |     |     |     |     |     | 1683 |
| ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |

BARATAETAL.:CLASSIFICATIONOFANOMALIESINMICROSERVICESUSINGANXGBOOST-BASEDAPPROACHWITHDATABALANCING
[27] A. Oliner and J. Stearley, “BGL log dataset,” 2007. Accessed: Apr. [53] P.J.RousseeuwandK.VanDriessen,“Fastandrobustfixed-pointal-
29,2025.[Online].Available:https://github.com/logpai/loghub gorithmsforindependentcomponentanalysis,”Technometrics,vol.41,
[28] W. Xu et al., “HDFS log dataset,” 2009. Accessed: Apr. 29, 2025. no.3,pp.212–223,1999.
[Online].Available:https://github.com/logpai/loghub [54] G. Developers, “Classification: Precision and recall|machine learning
[29] S.Zhou,X.Zhan,L.Li,andY.Liu,“Effectiveanomalydetectionfor crash course |google developers,” 2020. Accessed: Apr. 12, 2025.
microservicesystemswithreal-timefeatureselection,”inProc.Asia- [Online]. Available: https://developers.google.com/machine-learning/
PacificSoftw.Eng.Conf.,2023,pp.101–110. crash-course/classification/precision-and-recall
[30] M. Tavallaee et al., “NSL-KDD dataset,” 2009. Accessed: Apr. [55] L. M. Barata, “Admxgb - Anomaly detection data tables,” 2025.
29,2025.[Online].Available:https://www.unb.ca/cic/datasets/nsl.html Accessed: Jul. 29, 2025. [Online]. Available: https://github.com/
[31] N.Moustafa,“Ton_IoTdatasets,”2019.Accessed:Apr.29,2025.[On- luisbarata-ubi/anomally-detection/tree/main/data
line].Available:https://research.unsw.edu.au/projects/toniot-datasets [56] V.BarnettandT.Lewis,OutliersinStatisticalData,3rded.Hoboken,
[32] J. Mante and K. Kolhe, “Ensemble of tree classifiers for improved NJ,USA:Wiley,1994.
DDoSattackdetectionintheInternetofThings,”Math.Model.Eng. [57] V.Chandola,A.Banerjee,andV.Kumar,“Anomalydetection:Asur-
Problems,vol.11,no.9,pp.2355–2367,2024. vey,”ACMComput.Surv.,vol.41,pp.15:1–15:58,Jul.2009.
[33] N. Moustafa and J. Slay, “IoT-botnet dataset,” 2019. Accessed: Apr. [58] L. M. Barata, “Anomaly detection github repository - Luís Barata,”
29, 2025. [Online]. Available: https://research.unsw.edu.au/projects/ 2025.Accessed:May14,2025.[Online].Available:https://github.com/
toniot-datasets luisbarata-ubi/anomally-detection
[34] M.Steidl,B.Dornauer,andM.Felderer,“Howindustrytacklesanoma- [59] L.M.Barata,“Classifiedversionofthetracercadataset,”May2025.
lies during runtime: Approaches and key monitoring parameters,” in [Online].Available:https://doi.org/10.5281/zenodo.15399920
Proc.50thEuromicroConf.Softw.Eng.Adv.Appl.,2024,pp.364–372. [60] Y.Zhang,Y.Chen,J.Wang,andZ.Pan,“Unsuperviseddeepanomaly
[35] S.Gaoetal.,“Deathstarbench:Abenchmarksuiteforcloudmicroser- detection for multi-sensor time-series signals,” IEEE Trans. Knowl.
vices,” 2020. Accessed: Apr. 29, 2025. [Online]. Available: https:// DataEng.,vol.35,no.2,pp.2118–2132,Feb.2023.
github.com/delimitrou/DeathStarBench [61] D. F. N. Oliveira et al., “A new interpretable unsupervised anomaly
[36] C. Zhang, Z. Dong, X. Peng, and B. Zhang, “Trace-based multi- detectionmethodbasedonresidualexplanation,”IEEEAccess,vol.10,
dimensionalrootcauselocalizationofperformanceissuesinmicroser- pp.1401–1409,2022.
vicesystems,”inProc.IEEEInt.Conf.Softw.Eng.,2024,pp.1347– [62] J. Wang et al., “An anomaly prediction framework for financial IT
1358. systems using hybrid machine learning methods,” J. Ambient Intell.
[37] P. Fusco, A. Montefusco, G. P. Rimoli, F. Palmieri, and M. Ficco, HumanizedComput.,vol.14,no.11,pp.15277–15286,2023.
“Tinyml-basedintrusiondetectionsystemforhandlingclassimbalance [63] B.Krawczyk,“Learningfromimbalanceddata:Openchallengesand
iniot-edgedomainusingsiameseneuralnetworkonMCU,”inProc. futuredirections,”Prog.Artif.Intell.,vol.5,no.4,pp.221–232,2016.
Comput.Intell.PatternRecognit.,2025,pp.389–402. [64] V.J.HodgeandJ.Austin,“Asurveyofoutlierdetectionmethodolo-
[38] I. Sharafaldin, A. H. Lashkari, and A. A. Ghorbani, “Cicids 2017 gies,”Artif.Intell.Rev.,vol.22,pp.85–126,Oct.2004.
dataset,” 2017. Accessed: Apr. 29, 2025. [Online]. Available: https: [65] P.K.Donta,Q.Zhang,andS.Dustdar,“Performancemeasurementsin
//www.unb.ca/cic/datasets/ids-2017.html theai-centriccomputingcontinuumsystems,”2025,arXiv:2506.22884.
[39] Z.Lietal.,“Practicalrootcauselocalizationformicroservicesystems [66] L. M. Barata, E. Lopes, P. R. M. Inácio, and M. M. Freire,
viatraceanalysis,”inProc.IEEE/ACM29thInt.Symp.Qual.Service, “GambitRCA: An approach for anomaly root- cause identification
Jun.2021,pp.1–10. in microservices using game theory,” Under revision, 2025. [On-
[40] T.Zhou,C.Zhang,X.Peng,Z.Yan,andP.Li,“Tracestream:Anoma- line]. Available: https://github.com/luisbarata-ubi/gambitRCA/blob/
lousservicelocalizationbasedontracestreamclusteringwithonline main/GambitRCA.pdf
feedback,” in Proc. IEEE 34th Int. Symp. Softw. Rel. Eng., 2023,
pp.601–611.
[41] T.ChenandC.Guestrin,“Xgboost:Ascalabletreeboostingsystem,”
Proc. 22nd ACM SIGKDD Int. Conf. Knowl. Discov. Data Mining,
2016,pp.785–794.
[42] N. V. Chawla, K. W. Bowyer, L. O. Hall, and W. P. Kegelmeyer,
“SMOTE:Syntheticminorityover-samplingtechnique,”J.Artif.Intell.
Res.,vol.16,pp.321–357,2002.
[43] G.Haixiang,Y.Li,S.Shang,H.Ming,Y.Wang,andB.Wu,“Learn-
ingfromclass-imbalanceddata:Reviewofmethodsandapplications,”
ExpertSyst.Appl.,vol.73,pp.220–239,2017.
[44] H.HeandE.A.Garcia,“Learningfromimbalanceddata,”IEEETrans.
Knowl.DataEng.,vol.21,no.9,pp.1263–1284,Sep.2009.
[45] J.Bergstraetal.,“Hyperopt:Apythonlibraryforoptimizingthehy-
LUÍS M. BARATA (Member, IEEE) was born in
perparametersofmachinelearningalgorithms,”Comput.Sci.Discover.,
Castelo Branco, Portugal, in 1977. He received
vol.8,no.1,2013,Art.no.014008.[Online].Available:http://hyperopt.
the Graduation degree in computer engineering,
github.io/hyperopt/
and the M.Sc. degree in software development
[46] M. Sakurada and T. Yairi, “Anomaly detection using autoencoders
andinteractivesystemsfromtheSuperiorSchool
withnonlineardimensionalityreduction,”inProc.2ndWorkshopMach.
of Technology, Polytechnic Institute of Castelo
Learn.SensoryDataAnal.,2014,vol.2,pp.4–11.
Branco,CasteloBranco,Portugal.HisM.S.thesis
[47] J. R. Quinlan, Induction of Decision Trees, vol. 1. Berlin, Germany:
was titled as “Informatics at the Service of the
Springer,1986.
Elderly-Anemergingtheory,”combiningtheuse
[48] G. H. John and P. Langley, “Estimating continuous distributions in
ofITbytheelderlyusingaGroundedTheoryap-
Bayesian classifiers,” in Proc. 11th Conf. Uncertainty Artif. Intell.,
proach.HeiscurrentlyworkingtowardthePh.D.
1995,pp.338–345.
degreeincomputerengineeringwiththeDepartmentofComputerScience,
[49] F.T.Liu,K.M.Ting,andZ.-H.Zhou,“Isolationforest,”inProc.80th
UniversityofBeiraInterior’s,Covilhã,Portugal.HeisalsoaLevel2Engineer
IEEEInt.Conf.DataMining,2008,pp.413–422.
bythePortugueseOrderofEngineerswiththeCollegeofComputerScience.
[50] F.AngiulliandC.Pizzuti,“Fastoutlierdetectioninhighdimensional
Hisresearchinterestsincludemicroservicearchitectures,capturinganomalies
spaces,”inProc.Eur.Conf.Princ.DataMiningKnowl.Discov.,2002,
and determining their cause, predictive algorithms, machine learning, and
pp.15–27.
federatedlearninghaverecentlyattractedconsiderableattention.Heholdsthe
[51] G.Keetal.,“LightGBM:Ahighlyefficientgradientboostingdecision
titleofSpecialistwiththeDevelopmentofInformationSystems(Computer
tree,”inProc.Adv.NeuralInf.Process.Syst.,2017,pp.3146–3154.
Science), awardedbyPolytechnicInstitute ofCasteloBranco,Polytechnic
[52] A.LiawandM.Wiener,“Classificationandregressionbyrandomfor-
InstituteofSantarém,PolytechnicInstituteofGuarda,PortugueseOrderof
est,”RNews,vol.2,no.3,pp.18–22,2002.
Engineers(OE)andPortugueseInformationSystemsAssociation(APSI).
1684 VOLUME6,2025

EURICOLOPESreceivedthecomputerengineer- MÁRIOM.FREIRE(Member,IEEE)receivedthe
ingdegreefromInstitutoSuperiorTécnico,Lisbon, B.Sc. degree in electrical engineering, the M.Sc.
Portugal, the M.Sc. degree in computer acience degreeinsystemsandautomationfromtheUniver-
from Essex University, Colchester, U.K., and the sityofCoimbra,Coimbra,Portugal,in1992and
Ph.D. degree in information management from 1994, respectively, the Ph.D. degree in electrical
LeedsMetropolitanUniversity,Leeds,U.K.Whilst engineering, and the Habilitation degree in com-
teachingandresearching,EuricohasbeenaCon- putersciencefromtheUniversityofBeiraInterior
sultantwithlocalenterprises.Since1990,Eurico (UBI), Covilhã, in 2000 and 2007, respectively.
has been a Researcher of computer engineering In 1991, he started his research activities with
andinformationsystems.Euricoassistedbanking theUniversityofCoimbra,havingworkedwithin
sectorandtheindustryasanEngineer,Program- theEuropeanProjectEECRACE2011TRAVEL,
mer,SystemsAnalyst,Trainer,andthenaProjectLeader.Whilstteaching withinwhichhecarriedoutaone-monthinternshipin1993withNokiaNet-
and researching, Eurico has established various collaborations, including works(formerlyALCATELSELAG)ResearchCenter,Stuttgart,Germany.
severalmajorprojectswithlocalenterprises,involvingtechnologytransfer He is currently a Full Professor of computer science with UBI, which he
acrosstheorganizationforthedevelopmentandimplementationinformation joined in 1994. He is the coauthor of six international patents, co-editor
systems.EuricohasbeenamemberofOrdemdosEngenheirosandInstalla- of eight books published in Springer LNCS book series, and coauthor of
tionCommitteeTechnologicalandManagementSchoolinCasteloBranco more than 130 papers in international journals and conferences. His main
and Idanha-a-Nova. Eurico has also been with CCISP (Conselho Coorde- researchinterestsincludecomputersystemsandnetworks,includingnetwork
nadorInstitutosSuperiorPolitécnicos)asaConsultantofICTandnetwork andsystemvirtualization,cloudandedgecomputing,computersecurityand
projects,includingworkonPRODEPI&II.EuricoLopeswasconvenedas privacy,andapplicationsofAIincomputersystemsandnetworks.Hewas
anObserverwithuserspanelonFCCN(FundaçãoComputaçãoCientifica ontheeditorialboardofACMSIGAPPAppliedComputingReview,Asso-
Nacional).Since2013,EuricohasbeenappointedasanExpertwithAgencia ciateEditorforWileySecurityandPrivacyJournalandWileyInternational
deAvaliaçãoeAcreditaçãodoEnsinoSuperior(AgencyforAssessmentand JournalofCommunicationSystems,andEditorofIEEECOMMUNICATIONS
AccreditationofHigherEducation-A3ES).EuricoiscurrentlyaProfessor SURVEYSANDTUTORIALSfrom2007to2011.Hewasatechnicalprogram
withInstitutoPolitécnicodeCasteloBranco,CasteloBranco,Portugal.His committeememberforseveralIEEEinternationalconferencesandCo-Chair
researchinterestsincludeprojectmanagement,businessanalytics,decision ofthetrackonComputerNetworkingofACMSAC2025.Dr.MárioFreire
support systems, research methodology, and systems thinking. Eurico is a isaCharteredEngineerbythePortugueseEngineeringAssociationandis
SeniorMemberofACM. alsoamemberofIEEEComputerSocietyandAssociationforComputing
Machinery.
PEDRO R. M. INÁCIO (Senior Member, IEEE)
receivedtheB.Sc.degreeinmathematicsorcom-
puter science, and the Ph.D. degree in computer
science and engineering from Universidade da
Beira Interior (UBI), Covilhã, Portugal, in 2005
and 2009 respectively. The Ph.D. work was per-
formed in the enterprise environment of Nokia
Siemens Networks Portugal S.A., through the
Ph.D. grant from the Portuguese Foundation for
ScienceandTechnology.In2010,hejoinedUBI,
whereheiscurrentlyanAssociateProfessorwith
theDepartmentofComputerScience.Helecturessubjectsrelatedwithinfor-
mationassuranceand(cyber)security,tograduateandundergraduatecourses,
namelytotheB.Sc.,M.Sc.andPh.D.programmesincomputerscienceand
engineering.HeisalsoaResearcherwithInstitutodeTelecomunicações(IT).
Hisresearchinterestsincludeinformationassuranceandsecurity,computer
basedsimulation,andnetworktrafficmonitoring,analysisandclassification.
HefrequentlyreviewspapersofIEEE,Springer,WileyandElsevierjournals.
HeisamemberoftheTechnicalProgramCommitteesofflagshipnationaland
internationalworkshopsandconferences,suchasACMSAC,IEEENCA,
IFIPSECorARES.HeistheSeniorEditorofIEEEACCESS.HeisanACM
ProfessionalMember.
VOLUME6,2025 1685