TheJournalofSystemsandSoftware209(2024)111917
ContentslistsavailableatScienceDirect
TheJournalofSystems&Software
journalhomepage:www.elsevier.com/locate/jss
ServiceAnomaly:Ananomalydetectionapproachinmicroservicesusing
✩
distributedtracesandprofilingmetrics
MahsaPanahandeha,∗,AbdelwahabHamou-Lhadjb,MohammadHamdaqac,JamesMillera
aDepartmentofElectricalandComputerEngineering,UniversityofAlberta,Canada
bDepartmentofElectricalandComputerEngineering,ConcordiaUniversity,Canada
cDepartmentofComputerandSoftwareEngineering,PolytechniqueMontreal,Canada
| A R T I | C L E | I N F O |     |     | A B S | T R A | C T |     |     |     |     |     |     |
| ------- | ----- | ------- | --- | --- | ----- | ----- | --- | --- | --- | --- | --- | --- | --- |
Keywords: Anomalydetectionisanessentialactivityforidentifyingabnormalbehavioursinmicroservice-basedsystems.
Systemobservability Acommonapproachistomodelthesystembehaviourduringnormaloperationusingeitherdistributedtraces
Distributedtraces
orprofilingmetrics.Themodelisthenusedtodetectanomaliesduringsystemoperation.Inthispaper,we
Anomalydetection
present a new anomaly detection approach, called ServiceAnomaly, for anomaly detection in microservice
Microservicearchitectures systemsthatcombinesdistributedtracesandsixprofilingmetricstobuildanannotateddirectedacyclicgraph
Softwarereliability
thatcharacterizesthenormalbehaviourofthesystem.Unlikeexistingtechniques,ourapproachcapturesthe
AIOps
contextpropagationprovidedbydistributedtracesasagraphthatisannotatedwithfunctionscharacterizing
both linear and non-linear relationships between profiling metrics. The final annotated graph is used to
detect abnormal executions during system operation. The results of applying our approach to two open-
source benchmarks show that our approach detects anomalies with an F1-score up to 86%. We also show
howdeveloperscanusetheannotatedgraphtoreasonaboutthecausesofanomalies
1. Introduction operations or service functions. In this paper, we define spans at the
granularitylevelofservices.Anexampleofadistributedtraceisshown
Microservice architecture has emerged as the design of choice for in Fig. 1. This trace shows the services that are invoked following a
| the development |     | of software | systems | in  | a wide | range of | industry |     |     |     |     |     |     |
| --------------- | --- | ----------- | ------- | --- | ------ | -------- | -------- | --- | --- | --- | --- | --- | --- |
userrequestintheTrainTicketsystem.Thistraceincludesninespans.
| sectors (Pahl,    | 2015; | Balalaieet    | al., | 2015, 2016;Soldani |     | et     | al., 2018). |                |                     |     |                |                  |                |
| ----------------- | ----- | ------------- | ---- | ------------------ | --- | ------ | ----------- | -------------- | ------------------- | --- | -------------- | ---------------- | -------------- |
|                   |       |               |      |                    |     |        |             | Each span      | carries information |     | including      | a name, a unique | span ID,       |
| Unlike monolithic |       | applications, | a    | microservice-based |     | system | is com-     |                |                     |     |                |                  |                |
|                   |       |               |      |                    |     |        |             | and a context, | which consists      |     | of information | including        | the identifier |
posedofasetofservicesthatareeasytodevelop,deployandmaintain. ofthetracethatcontainsthespanandtheparentspan.Adistributed
Despitetheirbenefits,thesesystemsposemajoroperationalchallenges. trace is a directed rooted tree, which can also be represented as a
The highly dynamic aspect of these systems combined with frequent directed acyclic graph (DAG), by capturing common subtrees only
maintenance changes make them prone to failures and crashes in once (OpenTracing Contributors, 2023; Hamou-Lhadj and Lethbridge,
production(KratzkeandQuint,2017;Soldanietal.,2018).
|              |            |               |            |                   |         |          |          | 2002, 2005). | Fig. 1 shows | the       | corresponding  | rotted call | tree of the |
| ------------ | ---------- | ------------- | ---------- | ----------------- | ------- | -------- | -------- | ------------ | ------------ | --------- | -------------- | ----------- | ----------- |
| Distributed  | tracing    | is a          | relatively | new               | tracing | method,  | designed |              |              |           |                |             |             |
|              |            |               |            |                   |         |          |          | distributed  | trace. This  | call tree | is constructed | based on    | the context |
| specifically | to provide | observability |            | into microservice |         | systems. | A dis-   |              |              |           |                |             |             |
information,labelledinbracketsinthefigure.
| tributed | trace represents | an  | end-to-end | request | and | contains | a series |     |     |     |     |     |     |
| -------- | ---------------- | --- | ---------- | ------- | --- | -------- | -------- | --- | --- | --- | --- | --- | --- |
Studieshaveshownthattheanalysisofdistributedtracesisuseful
| of tagged | time intervals | known | as  | spans | as well | as the | spans rela- |             |               |        |     |               |              |
| --------- | -------------- | ----- | --- | ----- | ------- | ------ | ----------- | ----------- | ------------- | ------ | --- | ------------- | ------------ |
|           |                |       |     |       |         |        |             | for program | comprehension | (Niemi | and | Wallin, 2021; | Dashuber and |
tionships,andoptionallymetadatasuchaslogsortagscontextualizing
|     |     |     |     |     |     |     |     | Philippsen, | 2022), fault | diagnosis | (Ayers | et al., 2005; | Chen et al., |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ------------ | --------- | ------ | ------------- | ------------ |
spans(Parkeretal.,2020;OpenTracingContributors,2023).Aspanis
|          |              |         |     |             |          |       |          | 2021), root | cause analysis | (Yu | et al., 2021; | Li et al., | 2022a), and |
| -------- | ------------ | ------- | --- | ----------- | -------- | ----- | -------- | ----------- | -------------- | --- | ------------- | ---------- | ----------- |
| a single | unit of work | carried | out | by a single | service. | Spans | are also |             |                |     |               |            |             |
named a timed operation within a trace (OpenTracing Contributors, anomaly detection (Wang et al., 2020; Nedelkoski et al., 2019a), the
2023). However, the term ‘‘operation’’ does not necessarily denote focusofthispaper.Existinganomalydetectiontechniquesfallintotwo
✩
Editor:LeandroL.Minku.
∗
Correspondingauthor.
E-mailaddresses: panahand@ualberta.ca(M.Panahandeh),wahab.hamou-lhadj@concordia.ca(A.Hamou-Lhadj),mhamdaqa@polymtl.ca(M.Hamdaqa),
jimm@ualberta.ca(J.Miller).
https://doi.org/10.1016/j.jss.2023.111917
Received27March2023;Receivedinrevisedform27November2023;Accepted2December2023
Availableonline15December2023
0164-1212/©2023ElsevierInc.Allrightsreserved.

M.Panahandehetal.
TheJournalofSystems&Software209(2024)111917
|     |     |     |     | Fig.1. AdistributedtraceofTrainTicketsystemanditscorrespondingrootedcalltree. |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | ----------------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
categories.Thefirstgroupofstudiesuselogdata,tracesordistributed into the behaviour of microservices (Li et al., 2022b), which are es-
tracestomodeltheserviceflowofexecution(Baoetal.,2018;Nandi sential for understanding the system and identifying and analysing
etal.,2016)orobservepatternswithinthisdata(Duetal.,2017;Liu anomalies.Thissectionoutlinesthedifferentanomalydetectiontech-
et al., 2020; Bogatinovski et al., 2020) for the purpose of anomaly niques based on the sources they use. Note that, in this section, we
detection.Suchapproachesarelimitedtodetectingonlyanomaliesthat onlyreportonstudiesthatfocusonmicroservices.Thereexiststudies
affect the flow of execution. The second group relies on building a thatuseexecutiontracesforanomalydetectioninmonolithicsystems
performance profile using various metrics (e.g., latency), which can suchastheworkofIslametal.(2018)andKhreichetal.(2017).These
laterbeusedtoindicatesignificantchanges(Nedelkoskietal.,2019a; studiesareoutsidethescopeofthispaper.
Jacobetal.,2022;Wuetal.,2021;Zuoetal.,2020;Samiretal.,2020;
Linetal.,2018;Heetal.,2020;Houetal.,2021;SamirandPahl,2019; 2.1. Detectinganomaliesusinganalysisofexecutiontraces
Kohyarnejadfardetal.,2019).Theseapproachesvarydependingonthe
appliedalgorithmsandtheuseofeithersingleormultiplemetrics.
|        |                  |     |     |                  |        |         |      | Bao et | al. (2018) | built | a control | flow graph | from | the execution |     |
| ------ | ---------------- | --- | --- | ---------------- | ------ | ------- | ---- | ------ | ---------- | ----- | --------- | ---------- | ---- | ------------- | --- |
| Due to | the shortcomings |     | in  | both categories, | recent | studies | have |        |            |       |           |            |      |               |     |
tracesextractedfromtheannotatedsourcecode.Thenthecontrolflow
| attempted   | to combine | log       | data | and distributed | traces | with       | profiling |          |          |                  |             |     |       |              |     |
| ----------- | ---------- | --------- | ---- | --------------- | ------ | ---------- | --------- | -------- | -------- | ---------------- | ----------- | --- | ----- | ------------ | --- |
|             |            |           |      |                 |        |            |           | graph is | labelled | by a conditional | probability |     | value | representing | the |
| metrics for | detecting  | anomalies |      | (Meng et al.,   | 2021;  | Xu et al., | 2022).    |          |          |                  |             |     |       |              |     |
probabilityofdifferentpaths.Thisgraphisusedtodetectanomaliesin
Forexample,Mengetal.(2021)useresponsetimeandaflowgraphto
theexecutionsequences.Similarly,Nandietal.(2016)proposedusinga
detectanomaliesinmicroservicescausedbyperformancedegradation.
controlflowgraphoutoflogdata.Then,offlinetemplateandsequence
The typical metrics used in these studies include execution time (Fu miningtechniquesareappliedtothegraphtogeneratebaselineflows.
et al., 2009), response time (Meng et al., 2021; Nedelkoski et al., Zhang et al. (2022b) have studied the combination of log data and
2019b), and latency (Yu et al., 2021). However, the use of a single distributedtraces.Theygeneratedamodelofthesystemusingcollected
metrichasitsownlimitationssinceperformanceproblemscanmanifest data and applied a deep SVDD (Ruff et al., 2018) model to classify
themselvesacrossmultiplemetricsoracombinationofmetrics.
anomaloustraces.
Inthispaper,weproposeanewanomalydetectiontechnique,called
|     |     |     |     |     |     |     |     | Liu et | al. (2020) | and Du | et al. | (2017) | respectively | proposed | a   |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | ---------- | ------ | ------ | ------ | ------------ | -------- | --- |
ServiceAnomaly,whichbuildsamodelofthenormalbehaviourofthe
deepBayesiannetworkmodelforlearningtracesandLongShort-Term
systemusingaContextPropagationGraph(CPG)andsixprofilingmet-
Memory(LSTM)forunderstandinglogdataandusetheselearntmodels
rics.TheCPGisadirectedacyclicgraphthatmodelsservicesthatare
todetectdeviationsintheexecutionsequences.Giventhepowerofdis-
| invoked | as user | requests | propagate | through | the system. | We  | annotate |     |     |     |     |     |     |     |     |
| ------- | ------- | -------- | --------- | ------- | ----------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
tributedtracesinmicroservices,Gogatinovsketal.(Bogatinovskietal.,
theCPGbymodellingtherelationshipsbetweensixprofilingmetricsto
|     |     |     |     |     |     |     |     | 2020; Bogatinovski |     | and Nedelkoski, |     | 2020) apply | a neural | network | to  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------ | --- | --------------- | --- | ----------- | -------- | ------- | --- |
bettercharacterizetheexpectednormalbehaviourofthesystem.The
distributedtracescombinedwithlogdatatolearnthespans’position
| annotated | CPG is | used as | a baseline | to detect | potential | anomalies | in  |     |     |     |     |     |     |     |     |
| --------- | ------ | ------- | ---------- | --------- | --------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
andtemplateasabaseline.Thesestudiesarelimitedtothedetectionof
tracesofarunningsystem.ServiceAnomalyalsoprovidesthepossibility
anomaliesthatmanifestthemselvesthroughviolationstotheexecution
tocompareadistributedtracethatisgeneratedinthepresenceofan
sequencesofthesystem.
anomalywithamodelofthesystem’snormalexecution,whichshould
helpanalystsconductrootcauseanalysis.Weevaluatetheeffectiveness
|     |     |     |     |     |     |     |     | 2.2. Detectinganomaliesusinganalysisofprofilingmetrics |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- |
ofourapproachusingtwodifferentbenchmarksystems,Teastore(von
Kistowskietal.,2018)andTrainTicket(Zhouetal.,2018).Wefound
Aconsiderablenumberofstudiesanalysemicroservicesbehaviour
thatourapproachcanidentifyanomalytraceswithanF1-scoreof85%
|     |     |     |     |     |     |     |     | and detect | anomalies | by tracking | changes | in  | monitoring | key | perfor- |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --------- | ----------- | ------- | --- | ---------- | --- | ------- |
forTeaStoreand86%forTrainTicket.Moreover,ourapproachprovides
|          |        |           |          |           |      |                |     | mance indicators |        | (KPIs). The | most    | common      | techniques | for | detect-    |
| -------- | ------ | --------- | -------- | --------- | ---- | -------------- | --- | ---------------- | ------ | ----------- | ------- | ----------- | ---------- | --- | ---------- |
| a way to | reason | about the | abnormal | behaviour | that | was identified | in  |                  |        |             |         |             |            |     |            |
|          |        |           |          |           |      |                |     | ing changes      | in the | collected   | metrics | are methods | based      | on  | statistics |
theanomalytraces.
|           |     |           |             |            |     |               |     | and learning | algorithms. | We  | found | that many | anomaly | detection | ap- |
| --------- | --- | --------- | ----------- | ---------- | --- | ------------- | --- | ------------ | ----------- | --- | ----- | --------- | ------- | --------- | --- |
| The paper | is  | organized | as follows: | In Section |     | 2, we provide | an  |              |             |     |       |           |         |           |     |
overview of related work. Section 3 explains our ServiceAnomaly ap- proachesrelyonmonitoringonlytwometrics,mainlytheresponsetime
proach. In Section 4, we list the evaluation questions and discuss or request time. For example, Liu et al. (2021), Samir et al. (2020),
the setup and execution of the experiments we used to answer them. andLinetal.(2018)detectanomaliesinthemicroservicesbyfinding
Section 5 presents the results and answers the evaluation questions. asignificantincreaseinresponsetimeorlatencytimecomparedtothe
Section6discussespotentialthreatstovalidity.Alinktothedataand historicaldata.Nedelkoskietal.(2019a)employanunsuperviseddeep
reproductionpackageisindicatedinSection7.Lastly,weconcludethe Bayesian network model to detect changes in response time collected
paperinSection8anddiscussavenuesforfutureresearch. from distributed traces. Li et al. (2021) and Wu et al. (2021, 2020)
|     |     |     |     |     |     |     |     | use clustering | distributed | traces | to  | find abnormal | response | times | that |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | ----------- | ------ | --- | ------------- | -------- | ----- | ---- |
deviatefromnormaltraces.Zuoetal.(2020)suggestasequentialdeep
2. Relatedwork
learningmodelappliedtologdatatodetectadeviationintheduration
Identifying anomalies in microservices contributes to the stability, of requests. Li et al. (2022a) perform feature generation and model
reliability, and efficiency of microservice systems. Many approaches learningonthelatencyofrequestsextractedfromlogdata.
have been proposed in the literature. Profiling metrics, logs, and dis- However,allofthesestudiescollectonlyasingleperformancemet-
tributedtracesarethethreeprimarysourcesthatoffervaluableinsights ric.Maetal.(2020)believethatasinglemetricsuchasresponsetime
2

M.Panahandehetal.
TheJournalofSystems&Software209(2024)111917
orlatencyisnoteffectiveenoughtodetectanomalies.Theimportance bygeneratingacalltreeannotatedbytheservicesresponsetime.Then,
ofusingmoreperformanceindicatorsisaddressedbyHeetal.(2020). an online incremental clustering (Wang et al., 2015) and a tree edit
Theauthorscollected26metricssuchasCPU,memory,I/O,network, distancealgorithmareusedtoclusterthecalltreesandfinddeviations
load,anddiskusage.Then,theyusedaneuralnetworkmodeltolearn fromtheclusters’centrestodetectanomaliesaffectingdistributedtrace
metrics behaviour and detect anomalies. Hou et al. (2021) also used structures. Also, Wang et al. detect anomalies affecting the response
|          |         |            |     |                |         |        |     | time by tracking | a fluctuation |     | in the | response | time measured |     | by the |
| -------- | ------- | ---------- | --- | -------------- | ------- | ------ | --- | ---------------- | ------------- | --- | ------ | -------- | ------------- | --- | ------ |
| a kernel | density | estimation | and | waiting moving | average | method | on  |                  |               |     |        |          |               |     |        |
KPIs including CPU, I/O, and Network usage to model the system’s coefficientofvariance.
performanceanddetectedanomaliesusingstatisticalhypothesistests. All the aforementioned papers rely on only a single metric along
Samir and Pahl (2019) used Spearman’s rank correlation coefficient withexecutionsequencesinunderstandingthesystembehaviour.Re-
between the collected resource metrics and the number of requests cently,Zhaoetal.(2023)proposedafailuredetectionmethod,which
to reason if the performance degradation in the response time is a operates based on profiling metrics, logs, and distributed traces. The
symptom of an anomaly. Kohyarnejadfard et al. (2019) used a multi- authors used a combination of a Graph Transformer Network (GTN)
classsupportvectormachinefortheclassificationofcallfrequencyand and a Graph Attention Network (GAT) to capture the complex corre-
durationofcallsintodifferentclasseswithknownlabelsofnormal,CPU lation among various modalities of the data, including log templates,
shortage,andmemoryshortage.Theseclassesareusedasbaselinesto profilingmetrics,andresponsetimesextractedfromdistributedtraces.
assistinidentifyingresource-basedanomalies. Then, they used a Gated Recurrent Unit (GRU) to learn the temporal
dependenciesamongthedataandpredictthemultimodaldataforthe
| Although | there | exist | studies | that use multiple |     | metrics, | they are |     |     |     |     |     |     |     |     |
| -------- | ----- | ----- | ------- | ----------------- | --- | -------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
upcomingmoments.Failuresareidentifiedbycomparingtheobserved
| limited to | revealing | a specific |     | type of anomaly | (e.g., | resource-based |     |     |     |     |     |     |     |     |     |
| ---------- | --------- | ---------- | --- | --------------- | ------ | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
anomalies)anddonotprovidereasoningabouttheidentifiedanoma- data with the predicted values. Their work is based on collecting
lies.Infact,findingtherootcauseoftheanomalyneedsmoreinvesti- distributed traces and profiling metrics. However, their method relies
gationintothesystem’sarchitectureandexecutionpaths.Thisgroupof on a formal model and lacks visualization tools that could aid in
studiesdonotusetheinsightprovidedbytheexecutionsequencessuch comprehending the system’s behaviour or facilitating further insights
| aslogdata,traces,anddistributedtraces.Inthefollowing,wereview |     |     |     |     |     |     |     | intoanomalies. |     |     |     |     |     |     |     |
| ------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- |
studiesthatexploitbothmetricsandexecutionsequencesindetecting Similarly, Lee et al. (2023) proposed an anomaly detection pro-
anomaliestoaddressthesechallenges. cess as well as a root cause analysis approach based on KPIs, log
|     |     |     |     |     |     |     |     | data, and | distributed | traces. | They | used neural | network | techniques |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ----------- | ------- | ---- | ----------- | ------- | ---------- | --- |
2.3. Detectinganomaliesusinganalysisofexecutionsequencesandprofiling to acquire insights from various sources: event occurrence from log
metrics data, temporal dependencies and inter-service associations from KPIs,
andlatencydistributionsfromdistributedtraces.Adependencygraph
|               |                |     |         |                  |            |          |          | is also extracted | from    | invocation | calls  | of distributed | traces. | Then,          | a   |
| ------------- | -------------- | --- | ------- | ---------------- | ---------- | -------- | -------- | ----------------- | ------- | ---------- | ------ | -------------- | ------- | -------------- | --- |
| Zhang         | et al. (2022a) |     | encoded | frequent signals | of         | log data | as well  |                   |         |            |        |                |         |                |     |
|               |                |     |         |                  |            |          |          | graph attention   | network | takes      | merged | insights       | learned | from different |     |
| as KPIs using | a transformer. |     | Then,   | a multi-layer    | perception |          | model is |                   |         |            |        |                |         |                |     |
used to learn signals. The learnt signals are used in predicting unex- modalities along with the dependency graph to establish a baseline.
pectedbehaviours.Thisstudydoesnotelaborateontheusedmetrics. Anomalies are detected as deviations from the baseline using a fully
Moreover,theapproachdoesnotassistinunderstandingthesystem’s connected neural network binary classification algorithm. While this
behaviourandanalysinganomalies.Nedelkoskietal.(2019b)proposed study is close to our approach in using both execution sequences
an approach that uses a multimodal LSTM to build a model using and profiling metrics, it solely visualizes dependency extracted from
tracesandtheresponsetimemetricandusedthismodelforanomaly executionsequences.Moreover,itsanomalydetectionprocesslacksthe
detection.Thismodelreliesonasingleperformancemetric. incorporation of visualized information with anomaly detection that
Similar to the first group of studies, a common approach for un- aids users in comprehending the detected anomalies and comparing
themwiththeexpectedbehaviourofthesystem.
derstandingthesystemusingbothmetricsandexecutionsequencesis
Generally,ourworkisdifferentfromtheliteraturein:
modellingthecollecteddataasgraphs.Fuetal.(2009)usedgenerated
| aworkflowstatemachinefromlogdata.Thetransitions(edges)ofthe |     |     |     |     |     |     |     | •      |             |        |         |          |           |         |     |
| ----------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ------ | ----------- | ------ | ------- | -------- | --------- | ------- | --- |
|                                                             |     |     |     |     |     |     |     | We use | distributed | traces | jointly | with six | profiling | metrics | to  |
statemachineareannotatedwithGaussianfunctionscharacterizingthe
provideabettercharacterizationofthenormalbehaviourofthe
| execution | time of | services. | Then, | anomalies | are detected | against | the |     |     |     |     |     |     |     |     |
| --------- | ------- | --------- | ----- | --------- | ------------ | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
system.
| built annotated | graph    | as        | a baseline | if they         | are not | matched           | with the |                |     |           |          |        |             |     |      |
| --------------- | -------- | --------- | ---------- | --------------- | ------- | ----------------- | -------- | -------------- | --- | --------- | -------- | ------ | ----------- | --- | ---- |
|                 |          |           |            |                 |         |                   |          | • In modelling | the | profiling | metrics, | we use | both linear | and | non- |
| graph or        | if their | execution | time       | does not belong | to      | the characterized |          |                |     |           |          |        |             |     |      |
linearrelationshipsbetweenmetrics.
| Gaussian | distribution. | Meng | et  | al. (2021) built | a call | tree from | traces |                 |     |              |     |             |        |              |     |
| -------- | ------------- | ---- | --- | ---------------- | ------ | --------- | ------ | --------------- | --- | ------------ | --- | ----------- | ------ | ------------ | --- |
|          |               |      |     |                  |        |           |        | • Our annotated |     | CPG provides |     | information | beyond | the detected |     |
andresponsetimes.Anomaliesareidentifiedwhenanunexpectedcall
anomalythatassistsinunderstandingandanalysinganomalies.
isfoundbyaneditdistancealgorithmandcomparedtothebuilttree
|         |         |         |        |          |                  |     |        | • Our annotated |     | CPG makes | it  | possible to | compare | an observed |     |
| ------- | ------- | ------- | ------ | -------- | ---------------- | --- | ------ | --------------- | --- | --------- | --- | ----------- | ------- | ----------- | --- |
| or when | a surge | happens | in the | response | time. Similarly, | Xu  | et al. |                 |     |           |     |             |         |             |     |
traceandasnapshotofthesystem’sperformanceincludingpro-
(2022)proposedusingaweighteddirectedgraphextractedfromtraces,
filingmetricswithhistoricaldatawhichcanbeusedincompre-
resourcemetrics,andresponsetimesrepresentingtheeffectofanode
hensionofthesystem.
| in calling | a neighbour | node. | They | use the sliding | window | method | to  |     |     |     |     |     |     |     |     |
| ---------- | ----------- | ----- | ---- | --------------- | ------ | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
predict the next call and response time as a baseline for identifying Table 1 briefly compares our method with most similar studies in
anomalies. thescopeanomalydetectioninmicroservices.Thefirsttwoattributes
These studies are close to our approach in terms of representing comparethemethodsintermsoftheirinputs.Weknowthatdistributed
thesystembehaviourusingagraph.However,theseapproachesmodel tracesprovideabetterinsightintothemicroservicescomparedtothe
themicroservice’sperformancewithoneoraspecificnumberofmet- log data and traditional traces (Parker et al., 2020). Moreover, using
rics that can only enable the detection of anomalies that affect these multiplemetricsismoreeffectiveindetectinganomaliesinthesystem
metrics. performance(Maetal.,2020).However,tothebestofourknowledge,
Yuetal.(2021)clustereddistributedtracesbasedontheirEuclidean the current literature does not include studies using both distributed
distance.Then,eachobserveddistributedtracewasassignedtothecor- tracesandprofilingmetricsindetectingandunderstandinganomalies.
respondingclusterandthen,thelatencyvaluesoftraceswereclustered Thenextstudiedattributeisthevisualizationofexecution-basedinfor-
into two groups. An anomaly is detected if groups’ centroids are far mationofthesystemasamodelthatcanassistinlocatingandbetter
fromeachother.Wangetal.(2020)usedagraph-basedmethodusing understandinganomalies(Beschastnikhetal.,2020).Wealsocompared
distributedtraces.Theyaddressedtheexplanationofdistributedtraces therelatedworkswithourstudiesintermsofgeneratingabaselinefor
3

M.Panahandehetal.
TheJournalofSystems&Software209(2024)111917
|     |     |     |     |     |     |     | • Responsesize(𝑚 |     | ):Thismetricrepresentstheamountofdatain |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | --------------------------------------- | --- | --- | --- | --- | --- | --- |
3
bytesthatissentbyacalleetoacallerinresponsetoarequest.
|     |     |     |     |     |     |     | • Servicequeuetime(𝑚 |     |     | ):Itisthetimeinmillisecondsbetweenthe |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | --- | ------------------------------------- | --- | --- | --- | --- | --- |
4
momentarequestisinthepushqueueandthemomentbeforeit
isdequeued.
•
|     |     |     |     |     |     |     | Latency(𝑚 |     | 5 ):Itistheoutgoingrequestlatency,i.e.,thetimein |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------- | --- | ------------------------------------------------ | --- | --- | --- | --- | --- | --- |
millisecondsittakesforarequesttogettoitsdestinationsacross
thenetwork.
|     |     |     |     |     |     |     | • Throughput(𝑚 |     | ):Itisdefinedasthenumberofprocesseshandled |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ------------------------------------------ | --- | --- | --- | --- | --- | --- |
6
byacalleewithinaspecifiedtime.
|     |     |     |     |     |     |     | There are  | two main   | approaches |         | for monitoring |                | a   | microservice   | ap- |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ---------- | ---------- | ------- | -------------- | -------------- | --- | -------------- | --- |
|     |     |     |     |     |     |     | plication  | in order   | to collect | data,   | namely         | agent-based    |     | and agent-less |     |
|     |     |     |     |     |     |     | monitoring | approaches | (Li        | et al., | 2022b).        | In agent-based |     | approaches,    |     |
anagentneedstobedeployedoneachnode/server,itcollectsthedata
|     |     |     |     |     |     |     | and pushes   | data        | to a collector. |              | Agent-less  | approaches,  |            | on the           | other   |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ----------- | --------------- | ------------ | ----------- | ------------ | ---------- | ---------------- | ------- |
|     |     |     |     |     |     |     | hand, do     | not require | any             | specific     | software    | installation |            | as services      | are     |
|     |     |     |     |     |     |     | instrumented | and         | send            | data to      | a collector | directly.    |            | While agent-less |         |
|     |     |     |     |     |     |     | approaches   | tend        | to be           | lightweight, | agent-based |              | approaches |                  | provide |
Fig.2. ServiceAnomaly-constructingtheannotatedcontextpropagationgraph. bettercontroloverthecollectedmetrics,aremoresecure,anddonot
requirecodeinstrumentation(Lietal.,2022b).Forthesereasons,we
useanagent-basedapproachtocollectdatainourtechnique.
Fig.3showsahigh-levelarchitectureofhowthedistributedtraces
| the execution | sequence | (traces, | distributed | traces, | logs) and | metrics. |     |     |     |     |     |     |     |     |     |
| ------------- | -------- | -------- | ----------- | ------- | --------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Then, we studied the attribute of analysing a detected anomaly if it andprofilingmetricsarecollected.Atthetoplevel,wehavemonitoring
has been provided by the different anomaly detection methods. The systems (e.g., Prometheus, Anon., 2022e and Jaeger, Anon., 2022c)
sign ∗ means that the attribute has been addressed partially. Finally, that process and visualize distributed traces and profiling metrics,
theonlineattributeshowsiftheproposedmethodscanautomatically collectedbyanIstioagent(Anon.,2022b).Wedeployourtargetsystem
adapttothechangesinanoperationalenvironment. on Kubernetes (Anon., 2022d). As shown in Fig. 3, the microservice
applicationisruninsidepods.Apodisthesmallestexecutionunitin
3. TheServiceAnomalyapproach Kubernetes,whichcanbereplicated.Wedeployasingleserviceineach
pod.Besidesrunningtheapplication,weinjectanIstioproxyintoeach
Our approach for detecting anomalies in microservice systems, pod. TheIstioproxy isan agentthatdefines ourmicroserviceservice
calledServiceAnomaly,reliesonbuildinganannotatedContextProp- mesh,whichenablestheobservabilityofcommunicationbetweenser-
| agation   | Graph (CPG) to  | model       | the normal | system      | execution. | The        |              |         |         |     |         |             |     |               |     |
| --------- | --------------- | ----------- | ---------- | ----------- | ---------- | ---------- | ------------ | ------- | ------- | --- | ------- | ----------- | --- | ------------- | --- |
|           |                 |             |            |             |            |            | vices. Istio | proxies | mediate | and | control | the network |     | communication |     |
| annotated | CPG is built by | aggregating | context    | propagation |            | trees col- |              |         |         |     |         |             |     |               |     |
betweenservices,collectdataforthetrafficpassingthroughtheservice
lectedfromdistributedtraces.AcontextpropagationtreeisaDAGof
mesh,andpushdatatothecollectors.Inthispaper,Istioagentscollect
servicecalls,derivedfromthespancontextinformation,thatrepresents datafrompodsrunningindividualservices.Therefore,thegranularity
a user request propagating across the system. CPG is an integration ofthecollecteddataisatthelevelofservices.
of these DAGs in which nodes are services and edges denote service WeuseJaeger(Anon.,2022c)andPrometheus(Anon.,2022e),two
invocations.TheCPGisthenusedasareferencemodeltodetectand popularmonitoringsystems,tocollectdistributedtracesandprofiling
analyse abnormal executions caused by faults and other undesirable metrics.Jaeger(Anon.,2022c)isusedfordistributedtracingtotrack
behaviours. ServiceAnomaly requires two types of telemetry data as userrequests,whereasPrometheus(Anon.,2022e)isusedtoaggregate
input: distributed traces and profiling metrics. This data is generated theprofilingmetricsdataofthesystemasawhole.Jaegerisanopen-
byexercisingthesystemscenarios(ortestcases)inalabenvironment.
sourcedistributedtracingsystemthatlistenstotheIstioagentforspans
Theideaistocollectasmuchdataaspossibletocovervariouspaths
|     |     |     |     |     |     |     | sent over | the network. |     | To generate | distributed |     | traces | of the | traffic, |
| --- | --- | --- | --- | --- | --- | --- | --------- | ------------ | --- | ----------- | ----------- | --- | ------ | ------ | -------- |
ofthesystemexecution.WeusedistributedtracestobuildaCPGand
|     |     |     |     |     |     |     | first, the | tracing | feature | of the | Istio service | mesh | must | be activated. |     |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ------- | ------- | ------ | ------------- | ---- | ---- | ------------- | --- |
profilingmetricstoannotatetheCPG,followingthestepsdescribedin
ByIstiotracing,tracingheadersarerecognizedbyIstioandspansare
| Fig.2,which | arediscussedinmoredetail |     |     | inthesubsequentsections. |     |     |               |           |     |          |         |        |       |        |         |
| ----------- | ------------------------ | --- | --- | ------------------------ | --- | --- | ------------- | --------- | --- | -------- | ------- | ------ | ----- | ------ | ------- |
|             |                          |     |     |                          |     |     | automatically | generated |     | for each | service | in the | mesh. | Once a | request |
TheuseoftheannotatedCPGtoidentifyfaultsandtheirrootcausesis
|     |     |     |     |     |     |     | is received, | Istio | assigns | several | headers | to  | it including | an  | ID and |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ----- | ------- | ------- | ------- | --- | ------------ | --- | ------ |
discussedinSection3.4.
|     |     |     |     |     |     |     | the request | is passed | with | its | ID through | the | services. | The | Jaeger |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --------- | ---- | --- | ---------- | --- | --------- | --- | ------ |
platformreceivestherequestswiththeirheadersandspecifiesrequest
3.1. Collectingdata correlationusingIDswhichformtracesandcorrelatedspans.Weusea
Jaegerquerytogatheralltracesorfindaspecifictrace.Prometheusis
Thegoalofthisstepistocollectdistributedtracesincludingcontext
anopen-sourcemonitoringtoolwhichcollectsmetricsreportedwithin
andprofilingmetricsfromthetargetmicroserviceapplicationbyexe-
aservicemesh.ItscrapsendpointsincludingHTPPandIstioendpoints
| cuting the    | system using    | various   | requests.   | The metrics | we focus        | on in |                   |         |               |     |            |           |          |                |         |
| ------------- | --------------- | --------- | ----------- | ----------- | --------------- | ----- | ----------------- | ------- | ------------- | --- | ---------- | --------- | -------- | -------------- | ------- |
|               |                 |           |             |             |                 |       | and collects      | metrics | according     | to  | Prometheus |           | scraping | jobs described |         |
| this paper    | are the service | execution | time,       | request     | size, response  | size, |                   |         |               |     |            |           |          |                |         |
|               |                 |           |             |             |                 |       | in the Prometheus |         | configuration |     | file. The  | collected |          | profiling      | metrics |
| service queue | time, latency,  | and       | throughput, | which       | are extensively |       |                   |         |               |     |            |           |          |                |         |
fromthemicroservicetrafficcanbequeriedbythePrometheusQuery
usedtoassesstheperformanceofamicroservicesystem.Thesemetrics
Language(PromQL).
aredefinedasfollows:
• Requestdurationtime(𝑚 ):Itisthetimeinmillisecondsbetween 3.2. Constructingthecontextpropagationgraph
1
themomentthatacallersendsarequestandthemomentwhen
the caller receives the last byte of the answer. This time is the TheCPGisbuiltfromthedistributedtracesthatarecollectedinthe
timethatarequestisprocessedthroughthemesh. previous step. The CPG is the service call graph. However, we prefer
•
Requestsize(𝑚 2 ):Itisthenumberofbytesofthedatathatissent the term ‘‘context propagation’’ to emphasize the fact that the graph
byacallertoacalleeinordertoinitiatearequest. captures the spans that are invoked as the user request propagates
4

M.Panahandehetal.
Table1
ComparingServiceAnomalywithsimilarstudiesinthesamescope.
Attribute Fu,2009 Nedelkoski,2019 Wang,2020 Meng,2021 Yu,2021 Zhang,2022 Xu,2022. Zhao,2023 Lee,2023 Service-
(Fuetal.,2009) (Nedelkoskietal., (Wangetal., (Mengetal., (Yuetal.,2021) (Zhangetal., (Xuetal.,2022) (Zhaoetal., (Leeetal., Anomaly
|                  |     | 2019b) | 2020) | 2021) |     | 2022a) |     | 2023) | 2023) |     |
| ---------------- | --- | ------ | ----- | ----- | --- | ------ | --- | ----- | ----- | --- |
| Distributedtrace | −   | −      | +     | −     | +   | −      | −   | +     | +     | +   |
5
| Multiplemetrics      | −   | −   | −   | −   | −   | +   | +   | +   | +   | +   |
| -------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Visualization        | +   | −   | +   | +   | −   | −   | +   | −   | +   | +   |
| exe.Sequencebaseline | +   | +   | +   | +   | −   | −   | +   | +   | +   | +   |
| Metricsbaseline      | +   | +   | −   | −   | −   | −   | +   | +   | +   | +   |
| Analysinganomalies   | *   | −   | *   | *   | −   | +   | *   | −   | −   | +   |
| Onlinemethod         | −   | −   | +   | +   | +   | −   | +   | +   | −   | −   |
TheJournalofSystems&Software209(2024)111917

M.Panahandehetal.
TheJournalofSystems&Software209(2024)111917
accordingly.Iftherelationshiptypeis"CHILDOF’’,andthespanisnot
arootspan,itmeansthecurrentspanisthecallee,anditscalleristhe
|     |     |     |     |     |     |     | span parent. | After  | identifying | the      | caller of the | edge, the        | current span |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ------ | ----------- | -------- | ------------- | ---------------- | ------------ |
|     |     |     |     |     |     |     | is assigned  | as the | callee of   | the edge | and the       | edge is appended | to the       |
listofedges.Finally,theConstruct-Rooted-Call-Treefunctionreturns
thelistofedgesasoutput.
|     |     |     |     |     |     |     | To merge       | rooted    | trees                                     | into one  | tree we  | adopt Messaoud | et al.’s      |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --------- | ----------------------------------------- | --------- | -------- | -------------- | ------------- |
|     |     |     |     |     |     |     | algorithm      | (Messaoud | et al.,                                   | 2012)     | that was | developed      | to merge tree |
|     |     |     |     |     |     |     | structures     | of XML    | files. The                                | algorithm | uses     | rules to merge | two trees     |
|     |     |     |     |     |     |     | 𝑡 1⟨𝑁1,𝐸1⟩and𝑡 |           | 2⟨𝑁2,𝐸2⟩,whereN1andN2aresetsofnodes,andE1 |           |          |                |               |
andE2aresetsofedges.TheMerge-by-UnionfunctioninAlgorithm1
explainshowweadoptedMessaoudetal.’salgorithmtomergerooted
|     |     |     |     |     |     |     | call trees. | Lines | 27–32 check | if one | tree is a | subset of | the other tree |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ----- | ----------- | ------ | --------- | --------- | -------------- |
thentheresultingmergedtreewillbethesameasthecontainingtree,
Fig.3. DatacollectionarchitectureusingmonitoringsystemsinServiceAnomaly. asthesmallertreeisalreadyincludedwithinit.Forexample,inFig.4,
t1isasubsetoft2.Therefore,theirmergedtreeresultsint2.Moreover,
|     |     |     |     |     |     |     | whentherearedifferentsubtreesin𝑡 |     |     |     | and𝑡 |                       |     |
| --- | --- | --- | --- | --- | --- | --- | -------------------------------- | --- | --- | --- | ---- | --------------------- | --- |
|     |     |     |     |     |     |     |                                  |     |     |     | 1 2  | withthesameparent,the |     |
throughthesystem.Fig.4describestheprocessofbuildingaCPGusing resultingmergetreeiscomposedofallsubtreesissuedfrom𝑡 1 and𝑡 2 ,
threefictivetraces,t1,t2,andt3.First,westartbymergingtherooted Lines 33–38. For example, t2 and t3 of Fig. 4 have different subtrees
calltreesofthedistributedtracesintoacontextpropagationtree.Then rooted at node ‘‘b’’. The resulting merged tree is shown in step A of
weconvertthecontextpropagationtreeintoanacyclic-directedgraph Fig.4,whichincludesallsubtreesofb.When𝑡 and𝑡 includethesame
|     |     |     |     |     |     |     |     |     |     |     |     | 1 2 |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(DAG).Thisisbecauseeachrootedorderedtreecanbeconvertedintoa subtreesrootedatdifferentparentsorwhentheydonothaveanyedge
DAGbyrepresentingcommonsubtreesonlyonce(Flajoletetal.,1990). in common, the merged tree is obtained through the union of 𝑡 and
1
TheDAGisthefinalCPG. 𝑡 ,Line39.Mergingsubtreest1,t2,andt3ofFig.4resultsinthetree
2
| In this | paper, we merge | the rooted | call | trees while | preserving | the | showninFig.4(A). |      |               |     |           |             |             |
| ------- | --------------- | ---------- | ---- | ----------- | ---------- | --- | ---------------- | ---- | ------------- | --- | --------- | ----------- | ----------- |
|         |                 |            |      |             |            |     | The next         | step | is to convert | the | resulting | rooted tree | to a DAG by |
observedserviceinvocationpathsinthecollectedtraces.Thisinvolves
|                   |         |            |       |          |           |       | capturing  | common   | subtrees | only once. | This      | step is needed   | to reduce |
| ----------------- | ------- | ---------- | ----- | -------- | --------- | ----- | ---------- | -------- | -------- | ---------- | --------- | ---------------- | --------- |
| merging identical | sets of | edges that | share | a common | execution | path. |            |          |          |            |           |                  |           |
|                   |         |            |       |          |           |       | the number | of nodes | and      | edges of   | the final | CPG. Hamou-Lhadj | and       |
Wefollowthesameideawhenconvertingthecontextpropagationtree
intoaDAG.Therefore,withinthefinalCPG,wedifferentiatebetween Lethbridge (2002) showed that the size of routine call traces can be
identical services causing different execution paths. To annotate the significantly reduced if we can represent them as DAGs. The same
CPG with profiling metrics relationships, Section 3.3, we create a principleappliestocalltreesofservices.Forexample,inFig.4(A),we
matrix that contains all the metrics that are collected in the original canseethatthesubtreerootedat‘‘d’’,whichconsistsinourcaseofonly
tracesforeachedgeoftheDAG. onenode,isrepeatedtwice.ToconvertarootedtreeintoaDAG,weuse
Algorithm 1 elaborates on the process of constructing a CPG in a variant of Valiente et al.’s algorithm (Valiente Feruglio, 2000) that
detail.Line1initializesanemptyTree.Next,eachtraceinthecollected is used to solve the common subexpression problem, the presence of
distributed traces (T) is processed as a rooted call tree using the repetitionsinrootedorderedtrees.Valienteetal.’salgorithmiteratively
Construct-Rooted-Call-Trees function. Then, in Line 4, the processed traversestherootedtreebottom-upandassignsacertificate(aunique
identifier)toeachnode.Theassignedcertificatedistinguishesdifferent
| rooted call | tree is merged | with the | previously | processed | rooted | call |     |     |     |     |     |     |     |
| ----------- | -------------- | -------- | ---------- | --------- | ------ | ---- | --- | --- | --- | --- | --- | --- | --- |
nodesandisusedtoidentifyandremoveredundantsubpaths.First,the
treesusingtheMerge-by-Unionfunctionandtheresultisstoredinthe
algorithmcreatesauniquesignatureforeachnode.Thesignature(𝑠𝑖𝑔)
Treedatastructure.Finally,inLine6,themergedresultTreeisfedto
theConvert-to-DAGfunctionandconvertedtoaDAG.ThisDAGisthe is defined by a triple of 𝑠𝑖𝑔(𝑛) = ⟨𝐿𝑎𝑏𝑒𝑙(𝑛),𝑠𝑖𝑔(𝐿𝑒𝑓𝑡(𝑛)),𝑠𝑖𝑔(𝑅𝑖𝑔ℎ𝑡(𝐿))⟩
finalconstructedCPG. where Right (n) and Left (n) represent the right and left children of
The next lines in Algorithm 1 provide more details on each of node n and Label (n) is the label of the node n. The signature deter-
the functions. The Construct-Rooted-Call-Tree function, explained in minesiftwosubtreesareisomorphic.Thealgorithmstoressignatures
Lines 7–24, is designed to create rooted call trees from a given trace inahashtable.Itcheckstoseeiftheassignedsignatureisalreadyinthe
according to the context information propagated through its spans. It table,andifnot,itaddsthesignatureaswellasacomputedcertificate
beginsbyinitializinganemptyset tostoretheedgesofthecalltree. to the table. Then, the certificate is assigned to the traversed node.
Then,foreachspaninthegiventrace,itdefinesanedge.Eachedgeis Thecertificateisapositiveintegerbetween1tothenumberofnodes
atupleofcallerandcalleeextractedfromthespaninformation. computed incrementally and assigned to the nodes. If the hash table
|     |     |     |     |     |     |     | includes | the signature, | the | corresponding | certificate | is  | then returned |
| --- | --- | --- | --- | --- | --- | --- | -------- | -------------- | --- | ------------- | ----------- | --- | ------------- |
AccordingtoOpenTracing(OpenTracingContributors,2023),every
span, except the root span, has a reference to its parent span, which fromthetableandassignedtothetraversednode.Fig.4(B)showsthe
showsthecaller–calleerelationshipamongspans.Therearetwotypes rootedtreewiththecertificates.Fig.4(C)showsthefinalCPGthatis
ofparent–childrelationshipsincludingchild-ofandfollows-from.Edges constructedfromt1,t2,andt3asaDAG.
| are assigned | by checking | parent–child | relationships |     | of span. | Lines 10 |     |     |     |     |     |     |     |
| ------------ | ----------- | ------------ | ------------- | --- | -------- | -------- | --- | --- | --- | --- | --- | --- | --- |
and11intheConstruct-Rooted-Call-Treefunction,checkwhetherthe 3.3. Annotatingthecontextpropagationgraph
| span is a | root one with | any successor. | If  | this condition | is  | met, the |     |     |     |     |     |     |     |
| --------- | ------------- | -------------- | --- | -------------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
algorithmskipstothenextspantogetitschildren’sinformation.Next, The goal of this step is to annotate the CPG with the profiling
Lines 13 and 14 process a root span with no successor that happens metrics(𝑚 ,𝑚 ,...,𝑚 )tohavearepresentativebaselinemodelthat
|     |     |     |     |     |     |     |     | 1 2 | 6   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
when a span is failed to capture its parent–child information. We characterizes the normal execution of the system. Our approach is to
process this span as an edge with a null caller. If the span is not a model the relationship between the metrics for each span invocation
root span, the Construct-Rooted-Call-Tree function checks the type of (i.e.,eachedgeoftheCPG).Wewanttoknowtherelationshipbetween
parent–childrelationshipforthecurrentspan.Iftherelationshiptype anypairofmetrics(𝑚 to𝑚 )foreachedgeoftheCPG.
|     |     |     |     |     |     |     |     |     | 1   | 6   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
𝑚
is "FOLLOWS FROM’’, the algorithm searches for an existing edge in There are two types of relationships among any two metrics, 𝑖

set where its callee matches the parent of the current span. If such and𝑚 𝑗 ,linearandnon-linearrelationships.Toidentifyandmodelthe
an edge is found, it means that the current span is the callee, and it typeofrelationshipsofthemetrics,wefollowtwosteps:(a)building
hasacallerspanintherootcalltree.Theedge’scalleristhenassigned the profiling metrics matrix, and (b) characterizing the relationships
6

M.Panahandehetal.
TheJournalofSystems&Software209(2024)111917
Fig.4. ConstructingaContextPropagationGraphusingthreefictivedistributedtraces.Thisprocessincludesconstructingroottreesfromdistributedtraces,mergingthem,and
convertingtheresulttoaDAG.
| Algorithm1:    | ConstructingtheContextPropagationGraphAlgorithm |        |     |     |     |     |     |     |     |
| -------------- | ----------------------------------------------- | ------ | --- | --- | --- | --- | --- | --- | --- |
| 𝑇 ∶𝑑𝑖𝑠𝑡𝑟𝑖𝑏𝑢𝑡𝑒𝑑 |                                                 | 𝑡𝑟𝑎𝑐𝑒𝑠 |     |     |     |     |     |     |     |
Require:
1: InitializeTree=∅
| 2: foreach𝑡𝑟𝑎𝑐𝑒∈𝑇 | do  |     |     |     |     |     |     |     |     |
| ----------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
3: t=Construct-Rooted-Call-Trees(𝑡𝑟𝑎𝑐𝑒)
4: Tree=Merge-by-Union(Tree,t)
5: endfor
6: returnCPG=Convert-to-DAG(Tree)
Function Construct-Rooted-Call-Trees(𝑡𝑟𝑎𝑐𝑒)begin
←∅
7:
foreach𝑠𝑝𝑎𝑛∈𝑡𝑟𝑎𝑐𝑒do
8:
9: Initialize𝑒𝑑𝑔𝑒←𝑛𝑢𝑙𝑙
10: if𝑠𝑝𝑎𝑛isarootand𝑠𝑝𝑎𝑛.next!=nullthen
| 11: continue |     |     |     |     |     |     | ⊳Skiptothenextiteration |     |     |
| ------------ | --- | --- | --- | --- | --- | --- | ----------------------- | --- | --- |
12: endif
13: if𝑠𝑝𝑎𝑛isarootand𝑠𝑝𝑎𝑛.next==nullthen
14: 𝑒𝑑𝑔𝑒.𝑐𝑎𝑙𝑙𝑒𝑟←𝑛𝑢𝑙𝑙
15: endif
16: if(𝑠𝑝𝑎𝑛.𝑟𝑒𝑓𝑇𝑦𝑝𝑒=="FOLLOWS_FROM")then
17: 𝑒𝑑𝑔𝑒.𝑐𝑎𝑙𝑙𝑒𝑟←.𝑔𝑒𝑡(𝑒.𝑐𝑎𝑙𝑙𝑒𝑟|𝑒.𝑐𝑎𝑙𝑙𝑒𝑒=𝑠𝑝𝑎𝑛.𝑝𝑎𝑟𝑒𝑛𝑡)
endif
18:
if(𝑠𝑝𝑎𝑛.𝑟𝑒𝑓𝑇𝑦𝑝𝑒=="CHILD_OF"and𝑠𝑝𝑎𝑛isnotaroot)then
19:
20: 𝑒𝑑𝑔𝑒.𝑐𝑎𝑙𝑙𝑒𝑟←𝑠𝑝𝑎𝑛.𝑝𝑎𝑟𝑒𝑛𝑡
21: endif
22: 𝑒𝑑𝑔𝑒.𝑐𝑎𝑙𝑙𝑒𝑒←𝑠𝑝𝑎𝑛
23: +=𝑒𝑑𝑔𝑒
24: endfor
| 25: return               |     |           |               |     |     |     |     |     |     |
| ------------------------- | --- | --------- | ------------- | --- | --- | --- | --- | --- | --- |
| Function Merge-by-Union(𝑡 |     | <𝑁 ,𝐸 >,𝑡 | <𝑁 ,𝐸 >)begin |     |     |     |     |     |     |
|                           |     | 1 1 1 2   | 2 2           |     |     |     |     |     |     |
26: Initializet-union
| if𝑡 ⊆𝑡  | then |     |     |     |     |     |     |     |     |
| ------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
| 27: 1 2 |      |     |     |     |     |     |     |     |     |
t-union=𝑡
| 28: | 2   |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
29: endif
| 30: if𝑡 2 ⊆𝑡 1 | then |     |     |     |     |     |     |     |     |
| -------------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
| 31: t-union=𝑡  | 1    |     |     |     |     |     |     |     |     |
32: endif
33: if(𝑡 ∩𝑡 ≠∅𝐴𝑁𝐷∃𝑛 ∈𝑁 =𝑛 ∈𝑁 2|(𝑝𝑎𝑟𝑒𝑛𝑡(𝑛 )𝑂𝑅𝑝𝑎𝑟𝑒𝑛𝑡(𝑛 )=𝑛𝑢𝑙𝑙)𝑂𝑅(𝑝𝑎𝑟𝑒𝑛𝑡(𝑛 )=𝑝𝑎𝑟𝑒𝑛𝑡(𝑛 ))𝐴𝑁𝐷𝑐ℎ𝑖𝑙𝑑(𝑛 )≠𝑐ℎ𝑖𝑙𝑑(𝑛 ))then
| 1 2 |     | 𝑖 1 𝑗 | 𝑖   | 𝑗   |     | 𝑖 𝑗 | 𝑖   | 𝑗   |     |
| --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
34: t-union< 𝑁 ,𝐸 >= 𝑡 ∪𝑡 𝑤ℎ𝑒𝑟𝑒 𝑁 = 𝑁 ∪𝑁 ,𝐸 = 𝐸 ∪𝐸 𝑤ℎ𝑒𝑟𝑒 𝑐ℎ𝑖𝑙𝑑(𝑛 ) is connected to ∀𝑛 ∈ 𝑡 2|𝑛 = 𝑛 𝐴𝑁𝐷 𝑐ℎ𝑖𝑙𝑑(𝑛 )
|               | 3 3 | 1 2       | 3 1 2 3 | 1 2 |     | 𝑖   | 𝑘 𝑘 | 𝑗   | 𝑗   |
| ------------- | --- | --------- | ------- | --- | --- | --- | --- | --- | --- |
| isconnectedto | ∀𝑛  | ∈𝑡 1|𝑛 =𝑛 |         |     |     |     |     |     |     |
|               | 𝑘   | 𝑘 𝑖       |         |     |     |     |     |     |     |
35: endif
36: if𝑡 ∩𝑡 ≠∅𝐴𝑁𝐷 ∃𝑛 ∈𝑁 ≠𝑛 ∈𝑁 2|𝑝𝑎𝑟𝑒𝑛𝑡(𝑛 )=𝑝𝑎𝑟𝑒𝑛𝑡(𝑛 )𝐴𝑁𝐷𝑐ℎ𝑖𝑙𝑑(𝑛 )=𝑐ℎ𝑖𝑙𝑑(𝑛 )then
| 1 2 |     | 𝑖 1 𝑗 | 𝑖   | 𝑗   | 𝑖   | 𝑗   |     |     |     |
| --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
t-union<𝑁 ,𝐸 >=𝑡 ∪𝑡 𝑤ℎ𝑒𝑟𝑒𝑝𝑎𝑟𝑒𝑛𝑡(𝑛 )𝑖𝑠𝑐𝑜𝑛𝑛𝑒𝑐𝑡𝑒𝑑𝑡𝑜𝑝𝑎𝑟𝑒𝑛𝑡(𝑛 )𝐴𝑁𝐷𝑁 =𝑁 ∪𝑁 ,𝐸 =𝐸 ∪𝐸
| 37: | 3 3 | 1 2 | 𝑖   | 𝑗   | 3   | 1 2 3 1 2 |     |     |     |
| --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- |
38: else
| 39: t-union<𝑁 | 3 ,𝐸 3 >=𝑡 | 1 ∪𝑡 2 𝑤ℎ𝑒𝑟𝑒𝑡 1 𝑎𝑛𝑑 | 𝑡 2 makeaforest |     |     |     |     |     |     |
| ------------- | ---------- | ------------------- | --------------- | --- | --- | --- | --- | --- | --- |
40: endif
41: returnt-union
Function Convert-to-DAG(𝑡𝑟𝑒𝑒):ThisfunctionisbasedontheworkofValienteFeruglio(2000)
7

M.Panahandehetal.
TheJournalofSystems&Software209(2024)111917
| Algorithm2: |     | AnnotatingtheContextPropagationGraph |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| ----------- | --- | ------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Require: :Collectedprofilingmetrics
Require: 𝐶𝑃𝐺
1: foreach𝑒𝑑𝑔𝑒∈𝐶𝑃𝐺do
| 2:  | extract | matrixfromfor𝑒𝑑𝑔𝑒 |       |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | -------- | ------------------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | foreach𝑚 | ,𝑚                  | ∈ do |     |     |     |     |     |     |     |     |     |     |     |     |     |
| 3:  |          | 𝑖                   | 𝑗     |     |     |     |     |     |     |     |     |     |     |     |     |     |
𝑅2(),𝑁𝑀𝐼()
4:
if𝑟2
| 5:  |     | 𝑚𝑖,𝑚𝑗 >0.6then |     |                                    |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | -------------- | --- | ---------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6:  |     | characterize𝑚  | ,𝑚  | usingalinearregressionfunctionand𝜖 |     |     |     |     |     |     |     |     |     |     |     |     |
|     |     |                | 𝑖 𝑗 |                                    |     |     |     | 𝑟   |     |     |     |     |     |     |     |     |
7: endif
| 8:  | if𝑟2 | <0.6𝑎𝑛𝑑𝑁𝑀𝐼>𝑡then |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | ---- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
𝑚𝑖,𝑚𝑗
|     |     | characterize𝑚 | ,𝑚  | usinganon-linearSVRregressionfunctionand𝜖 |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | ------------- | --- | ----------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 9:  |     |               | 𝑖 𝑗 |                                           |     |     |     |     | 𝑠𝑣𝑟 |     |     |     |     |     |     |     |
10: endif
11: Annotate𝑒𝑑𝑔𝑒withlinearandnon-linearregressionfunctions
12: endfor
13: endfor
14: ⊳Differenterrorevaluationmetricscanbecomputedfrom𝜖 ,𝜖 toevaluatetheerrorinthelinearandnon-linearregressionfunctions
|     |     |     |     |     |     |     |     | 𝑟 𝑠𝑣𝑟 |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
betweenthemetrics.Algorithm2elaboratesonannotatingthecontext 3.3.2. Characterizingtherelationshipsbetweenmetrics
propagation graph using these two steps. This algorithm requires the Inthisstep,wedeterminebothlinearandnon-linearrelationships
constructedCPGfromthepreviousstepandcollectedprofilingmetrics between the profiling metrics. Then, we use regression functions to
| () | from | the Collecting | data | step. We explain | the | algorithm | in the |       |                  |     |         |      |         |             |      |         |
| ---- | ---- | -------------- | ---- | ---------------- | --- | --------- | ------ | ----- | ---------------- | --- | ------- | ---- | ------- | ----------- | ---- | ------- |
|      |      |                |      |                  |     |           |        | model | the relationship |     | between | each | pair of | metrics for | each | edge of |
followingsections.
theCPG.ThefunctionsareusedtoannotatetheCPG.Inthefollowing,
webeginbyidentifyingthelinearrelationshipsusinglinearcorrelation.
Wethenexplaintheprocessofcharacterizingnon-linearrelationships
3.3.1. Buildingtheprofilingmetricmatrix
|     |     |     |     |     |     |     |     | using | mutual | information |     | and non-linear | Support | Vector | Regression |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | ------ | ----------- | --- | -------------- | ------- | ------ | ---------- | --- |
Westartbyrunningthesystemtocollectenoughdatatohelpusde-
(SVR).
terminetherelationshipbetweentheprofilingmetrics.InAlgorithm2,
containsallcollectedprofilingmetrics.Lines1–2inAlgorithm2 (A)Identifyingandcharacterizinglinearrelationships:
| summarizes |     | the construction | of  | the profiling | metrics | matrix | for each |     |     |     |     |     |     |     |     |     |
| ---------- | --- | ---------------- | --- | ------------- | ------- | ------ | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Alinearrelationshipischaracterizedbyadirectconnectionbetween
edgeoftheCPG.WeusethePrometheusQueryLanguage(PromQL)to
|     |     |     |     |     |     |     |     | two | variables, | implying | that | both variables | change | in  | the same | pro- |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | -------- | ---- | -------------- | ------ | --- | -------- | ---- |
collectthemetricsforeachedgeoftheCPG.Forexample,thefollowing portion(DarlingtonandHayes,2017).WeusethePearsonCorrelation
PromQL query returns the request duration time of the invocation Coefficient (Eq. (3)) (Darlington and Hayes, 2017) to estimate the
characterizedbytheedgea→boveroneday,withdatapointscollected
|     |     |     |     |     |     |     |     | degree | of a | linear | relationship | between | two | variables, | in the | case of |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | ---- | ------ | ------------ | ------- | --- | ---------- | ------ | ------- |
at1-minuteintervals:
|     |     |     |     |     |     |     |     | anytwometrics,𝑚 |     |     | 𝑖 and𝑚 𝑗 | .   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- | --- | -------- | --- | --- | --- | --- | --- |
𝑟𝑒𝑞𝑢𝑒𝑠𝑡_𝑑𝑢𝑟𝑎𝑡𝑖𝑜𝑛_𝑚𝑖𝑙𝑙𝑖𝑠𝑒𝑐𝑜𝑛𝑑𝑠{𝑑𝑒𝑠𝑡𝑖𝑛𝑎𝑡𝑖𝑜𝑛_𝑠𝑒𝑟𝑣𝑖𝑐𝑒_𝑛𝑎𝑚𝑒 = ε𝑏ε,𝑟𝑒𝑝𝑜𝑟𝑡𝑒𝑟 = ∑𝑛
|     |     |     |     |     |     |     |     |     |     | (𝑚  | −𝑚̄)(𝑚 | −𝑚̄ | )   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- |
ε𝑠𝑜𝑢𝑟𝑐𝑒ε,𝑠𝑜𝑢𝑟𝑐𝑒_𝑎𝑝𝑝=ε𝑎ε,𝑟𝑒𝑠𝑝𝑜𝑛𝑠𝑒_𝑐𝑜𝑑𝑒=ε200ε}[1𝑑∶1𝑚] 𝑟 = 𝑡=0 𝑖,𝑡 𝑖 𝑗,𝑡 𝑗 =
|     |     |     |     |     |     |     |     | 𝑚𝑖,𝑚𝑗 | √   |     | √   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
Applyingsimilarqueriesforallsixprofilingmetricsdescribedin3.1, ∑𝑛 (𝑚 −𝑚̄)2 ∑𝑛 (𝑚 −𝑚̄ )2
|     |     |     |     |     |     |     |     |     |     | 𝑡=0 𝑖,𝑡 | 𝑖   | 𝑡=0 𝑗,𝑡 | 𝑗   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | ------- | --- | --- | --- | --- |
(3)
weobtainamatrixwherethenumberofcolumnsequalsthenumberof 𝐶𝑜𝑣(𝑚,𝑚 )
|     |     |     |     |     |     |     |     |     |     |     |     |     | 𝑖 𝑗 |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
metrics,i.e.,6,andtherowsrepresentthedifferentobservationpoints
𝜎 𝑚𝑖 𝜎 𝑚𝑗
| intime.Forexample,𝑚 |     |     | referstotheobservedvalueat𝑡 |     |     | forthefirst |     |     |     |     |     |     |     |     |     |     |
| ------------------- | --- | --- | --------------------------- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|                     |     |     | 1,𝑡0                        |     |     | 0           |     |     |     |     |     |     |     |     |     |     |
metric 𝑚 (request duration time) and 𝑚 is the last observed value where 𝑚̄ and 𝑚̄ are the averages of the two metric distributions,
|     | 1   |     |     | 6,𝑡𝑛 |     |     |     |     | 𝑖   | 𝑗   |     |     |     |     |     |     |
| --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
attime𝑡 forthe𝑚 . 𝐶𝑜𝑣(𝑚 ,𝑚 ) is covariance of 𝑚 ,𝑚 , and 𝜎 and 𝜎 are respectively
|     | 𝑛       | 6        |         |     |     |     |     |      | 𝑖 𝑗      |            |       | 𝑖 𝑗                | 𝑚𝑖         | 𝑚𝑗             |             |       |
| --- | ------- | -------- | ------- | --- | --- | --- | --- | ---- | -------- | ---------- | ----- | ------------------ | ---------- | -------------- | ----------- | ----- |
|     |         |          |         |     |     |     |     | the  | standard | deviations | of    | each distribution. |            | 𝑟 𝑚 ,𝑚𝑗 ranges | from        | −1 to |
|     | ⎛𝑚 1,𝑡0 | 𝑚 2,𝑡0 ⋯ | 𝑚 6,𝑡0⎞ |     |     |     |     |      |          |            |       |                    |            | 𝑖              |             |       |
|     |         |          |         |     |     |     |     | 1. A | value    | close to   | −1 or | 1 means            | that there | i s a strong   | correlation |       |
|     | ⎜𝑚      | 𝑚 ⋯      | 𝑎 ⎟     |     |     |     |     |      |          |            |       |                    |            |                |             |       |
=⎜ 1,𝑡1 2,𝑡1 6,𝑡1⎟ (1) betweenthetwovariables.𝑟 convergesto0meansthatthereisno
|     | ⎜ ⋮ | ⋮ ⋱ | ⋮ ⎟ |     |     |     |     |     |     |     |     | 𝑚𝑖,𝑚𝑗 |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- |
linearrelationshipbetweenthetwovariables.Itshouldbenotedthat
|     | ⎜𝑚     | 𝑚 ⋯  | 𝑚 ⎟   |     |     |     |     |      |          |      |            |                 |     |             |         |     |
| --- | ------ | ---- | ----- | --- | --- | --- | --- | ---- | -------- | ---- | ---------- | --------------- | --- | ----------- | ------- | --- |
|     | ⎝ 1,𝑡𝑛 | 2,𝑡𝑛 | 6,𝑡𝑛⎠ |     |     |     |     |      |          |      |            |                 |     |             |         |     |
|     |        |      |       |     |     |     |     | this | does not | mean | that there | is a non-linear |     | correlation | between | the |
Fig. 5 shows an example of profiling metrics for the two traces T1 twovariables(Leeetal.,2012;Freedman,2009)sincetheremaynotbe
and T2 that are collected at times 𝑡 0 and 𝑡 1 , respectively. Each line anyrelationshipsbetweenthetwovariables.Wewilldiscussnon-linear
representsthecollectedprofilingmetricsbasedonthecalledspan.For correlationinthenextsubsection.
| example, | for     | span ‘b’     | called by      | span ‘a’ in these | two         | traces,    | we have |     |         |              |          |             |        |          |              |         |
| -------- | ------- | ------------ | -------------- | ----------------- | ----------- | ---------- | ------- | --- | ------- | ------------ | -------- | ----------- | ------ | -------- | ------------ | ------- |
|          |         |              |                |                   |             |            |         |     | We need | to determine |          | a threshold | beyond | which we | can consider |         |
| two      | sets of | metrics that | were collected | using             | Prometheus. | Extracting |         |     |         |              |          |             |        |          |              |         |
|          |         |              |                |                   |             |            |         | two | metrics | are strongly | linearly | correlated  | using  | the      | Pearson      | coeffi- |
metricsfor‘b’calledby‘a’(𝑎→𝑏forsimplicity)resultsinthefollowing
cient.Forthis,weusethesamethresholdastheoneproposedbyJiang

matrixwhereeachcolumnrepresentsthevaluesofaspecificmetric et al. (2011). The authors used linear correlation and normalized
overtime,andtherowsrepresentthesixmetricsofinterest.Thevalue
|                              |     |     |     |      |                      |     |     | mutual | information |     | (NMI) | together, | as a similarity | measurement |     | to  |
| ---------------------------- | --- | --- | --- | ---- | -------------------- | --- | --- | ------ | ----------- | --- | ----- | --------- | --------------- | ----------- | --- | --- |
| ofeachmetricfor𝑎→𝑏overtimes𝑡 |     |     |     | and𝑡 | usedtobuildthematrix |     |     |        |             |     |       |           |                 |             |     |     |
0 1 cluster similar software applications metrics into groups. According
 arehighlightedinFig.5.
|     |     |       |           |       |     |     |     | toJiangetal.(2011)twometrics𝑚,𝑚 |                       |     |     |        | arestronglylinearlycorrelated |     |     |     |
| --- | --- | ----- | --------- | ----- | --- | --- | --- | ------------------------------- | --------------------- | --- | --- | ------ | ----------------------------- | --- | --- | --- |
|     |     |       |           |       |     |     |     |                                 |                       |     |     | 𝑖      | 𝑗                             |     |     |     |
|     |     |       |           |       |     |     |     | if𝑟2                            | >0.6.Themeasurement𝑟2 |     |     |        | isapositivevaluebetween0and   |     |     |     |
|     | 𝑚   | 1 𝑚 2 | 𝑚 3 𝑚 4 𝑚 | 5 𝑚 6 |     |     |     | 𝑚                               | 𝑖, 𝑚 𝑗                |     |     | 𝑚 𝑖 ,𝑚 | 𝑗                             |     |     |     |
( ) 1 w h i c h s p e ci f i es t h e p ro p o r t io n o f t h e v a ria n ce o f 𝑚 t h a t i s e xp la i ne d
|    | 0 . | 5 1 0 0 | 9 0 2 | 1 0 . 8 8 |     |     |     |     |     |     |     |     |     | 𝑗   |     |     |
| --- | --- | ------- | ----- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 𝑎→𝑏 | =   |         |       |           |     |     | (2) |     |     |     |     |     |     |    |     |     |
1 1 2 1 1 1 0 4 1 0 . 8 8 b y 𝑚 𝑖 ( Da r l in g t o n a n d H a y e s , 2 01 7 ) . G iv e n a m at r ix f o r e a c h ed g e o f
theCPG,wemeasureasymmetricmatrixshowing𝑟2betweenallpairs
8

M.Panahandehetal. TheJournalofSystems&Software209(2024)111917
Fig.5. ProfilingmetricsfortracesT1,T2.Eachlineshowsthecollectedsixprofilingmetricsbasedonthecalledspan.
ofmetricsinmatrix (Lines3–4inAlgorithm2). • Meansquarederror(MSE):Thisrepresentstheexpectedvalueof
the quadratic loss. The lower the MSE value, the more accurate
𝑟2 𝑟2 ⋯ 𝑟2
⎛ 𝑚1,𝑚1 𝑚1,𝑚2 𝑚1,𝑚𝑘 ⎞ the function to the actual observed value (Mohan et al., 2021;
⎜𝑟2 𝑟2 ⋯ 𝑟2 ⎟
2=⎜ 𝑚−2,𝑚1 𝑚2,𝑚2 𝑚2,𝑚𝑘⎟ (4) BoehmkeandGreenwell,2019).TheMSEiscalculatedas:
⎜ ⋮ ⋮ ⋱ ⋮ ⎟
⎜ ⎝ 𝑟2 𝑚−𝑘,𝑚1 𝑟2 𝑚𝑘,𝑚2 ⋯ 𝑟2 𝑚𝑘,𝑚𝑘 ⎟ ⎠ 𝑀𝑆𝐸(𝑚
𝑖
,𝑚̂
𝑖
)= 1
𝑛
∑
𝑡𝑛
(𝜖
𝑟𝑡
)2
Weuselinearregressiontocharacterizethelinearlycorrelatedmetrics. 𝑡=𝑡0
Linear regression attempts to find the best function that describes • Root mean square error (RMSE): This is the standard deviation
the linear relationship of the data (Freedman, 2009). The linear re-
oftheresidualsthatshowshowtheregressionisadjustedtothe
lationship for metrics 𝑚 and ,𝑚 is characterized using the following
𝑖 𝑗 dataandthequalityofthemodel.AlowerRMSEmeansahigher
regressionfunction(DarlingtonandHayes,2017):
regressionquality(Mohanetal.,2021;BoehmkeandGreenwell,
𝑚 =𝛽 +𝛽 𝑚 +𝜀 (5) 2019).RMSEiscalculatedas:
𝑖 0 1 𝑗 𝑟
√
𝑚
to
𝑖
𝑡
an
.
d
𝛽
𝑚
=
𝑗
(
ar
𝛽
e
0 )
tim
co
e
n
s
t
e
a
r
i
i
n
e
s
s
c
r
o
e
e
p
f
r
f
e
ic
se
ie
n
n
t
t
in
s
g
of
th
t
e
he
va
re
lu
g
e
re
o
ss
f
i
t
o
h
n
es
m
e
o
m
de
e
l
tr
a
ic
n
s
d
a
𝜀
t𝑡
i
0
s 𝑅𝑀𝑆𝐸(𝑚 𝑖 ,𝑚̂ 𝑖 )=
∑𝑡 𝑡 𝑛 =𝑡0
𝑛
(𝜖 𝑟𝑡 )2
𝑛 𝛽
thedisturban 1 cevectororerrorcalculatedasfollows: • Median absolute error (MedAE): is a robust measurement to
∑𝑛 (𝑚 −𝑚̄)(𝑚 −𝑚̄ ) outliers which captures the median of all absolute differences
𝛽 1 = 𝑡=0 ∑𝑛 𝑖𝑡 (𝑚 𝑖 −𝑚̄ 𝑗𝑡 )2 𝑗 ,𝛽 0 =𝑚̄ 𝑖 −𝛽 1 𝑚̄ 𝑗 , betweenthetargetandtheprediction(Mohanetal.,2021).The
𝑡=0 𝑖𝑡 𝑖 MedAEiscalculatedas:
⎛
⎜
1
1
𝑚
𝑚
𝑡0𝑗⎞
⎟ 𝑀𝑒𝑑𝐴𝐸(𝑚 𝑖 ,𝑚̂ 𝑖 )=𝑚𝑒𝑑𝑖𝑎𝑛(|𝜖 𝑟𝑡|),𝑡=𝑡 0 ,𝑡 1 ,…,𝑡 𝑛
𝜀
𝑟
=𝑚
𝑖
−⎜
⎜1 ⋮
𝑡1𝑗⎟
⎟
𝛽
• Maximumerror(max-error):Wealsousemaximumerrorwhich
⎜1 𝑚 ⎟
⎝ 𝑡𝑛𝑗⎠ is suggested in the literature (Keogh et al., 2001). It is a metric
Lines 3–6 in Algorithm 2 summarize identifying and characterizing measuringtheworst-caseerrorbetweenthepredictedvalueand
linearrelationshipsforeachpairofmetrics. thetruevalue.Alowmax-errmeansthepresenceoflowererror
The𝜖 vectorincludestheactualerrorvaluesof𝑚 orresidualfor valuesandhenceabetter-fitregression.Themax-erriscomputed
𝑟 𝑖
each entry, i.e., 𝑚 −𝑚̂ when 𝑚̂ represents the computed value for asfollows:
𝑖 𝑖 𝑖
𝑚 using the regression function (5). There are various error evalua-
tio
𝑖
n metrics used to evaluate errors in regression functions, each of
𝑚𝑎𝑥−𝑒𝑟𝑟(𝑚
𝑖
,𝑚̂
𝑖
)=max(|𝜖 𝑟𝑡|),𝑡=𝑡
0
,𝑡
1
,…,𝑡
𝑛
which computes an individual error evaluation value based on actual We will discuss different error evaluation metrics and their effect on
error values. In this study, we use the following six error evaluation ourexperimentsintheevaluationsection(Section4).
metrics (Mohan et al., 2021; Boehmke and Greenwell, 2019) that are
calculatedfromthevector𝜖. (B)Identifyingandcharacterizingnon-linearrelationships:
𝑟
The correlationcoefficient𝑟 can beused to determineif two vari-
• Meanabsoluteerror(MAE):Itisametricmeasuringthemeanof ablesarelinearlycorrelated.However,itcannotbeusedtodeducethat
absolute residuals. A lower MAE value corresponds to a better- two variables are not linearly correlated (Lee et al., 2012; Freedman,
fitfunction(Mohanetal.,2021;BoehmkeandGreenwell,2019). 2009).Fig.6showscaseswherethecorrelationcoefficient𝑟alonecan-
Given a 𝜖 vector including the actual error values of metric 𝑚 not describe non-linear relationships between variables. For example,
𝑟 𝑖
for the time points 𝑡 to 𝑡 , we measure MAE as follows, where theremaynotbeanyrelationshipbetweenthetwovariables(asshown
0 𝑛
𝜖 representstheactualerrorvalueattime𝑡: inFig.6bottomleftquadrant).Toidentifythenon-linearrelationships
𝑟𝑡
between our metrics, we use the mutual information (MI) concept
𝑀𝐴𝐸(𝑚 𝑖 ,𝑚̂ 𝑖 )= 1 𝑛 𝑡 ∑ =
𝑡𝑛
𝑡0 |𝜖 𝑟𝑡| w M i u th tua th l e in c f o o r r r m e a la t t io io n n d c e o f e in ff e i d cie u n s t in a g s c s o u n g d g i e t s io te n d al b e y n J tr i o a p n y g a et nd al d . e ( s 2 c 0 r 1 ib 1 e ) s .
the amount of information that each variable provides knowing the
• Meanabsolutepercentageerror(MAPE):Itisameasuredefined
otherone.Inthispaper,weuseNormalizedMutualInformation(NMI)
based on the relative percentage of errors. It represents the av-
measurementsinceourcollectedmetricshavedifferentranges,which
erage absolute percentage errors while a lower value shows a
iscalculatedusingEq.(6).
strongerregressionfitmodel(DeMyttenaereetal.,2016;Mohan
et al., 2021). Given a 𝜖 𝑟 vector, MAPE is computed using the 𝑁𝑀𝐼(𝑋|𝑌)=
𝐻
√
(𝑋)−𝐻(𝑋|𝑌)
(6)
followingequation: 𝐻(𝑋)𝐻(𝑌)
𝑀𝐴𝑃𝐸(𝑚 𝑖 ,𝑚̂ 𝑖 )= 1 𝑛 𝑡 ∑ = 𝑡𝑛 𝑡0 | | | | | 𝑚 𝜖 𝑟 𝑖 𝑡 𝑡 | | | | | T de h f e in n e o d rm as al f i o ze ll d ow m s u w tu h a e l r i e nf 𝐻 or ( m 𝑋 a ) ti i o s n th fo e r e t n w tr o op v y ari o a f b 𝑋 les a o n f d 𝑋 𝐻 a ( n 𝑋 d |𝑌 𝑌 ) i i s s
9

M.Panahandehetal.
TheJournalofSystems&Software209(2024)111917
|     |     |     |     |     |     |     |     | Where 𝑛       | is the length of | the data      | sets (number | of collected |            | metrics). |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | ---------------- | ------------- | ------------ | ------------ | ---------- | --------- |
|     |     |     |     |     |     |     |     | The constant  | 𝑏 is the model   | parameter     | and          | 𝛼 = (𝛼       | ,𝛼 ,…,𝛼    | )𝑇,𝛼∗ =   |
|     |     |     |     |     |     |     |     |               |                  |               |              | 1            | 2          | 𝑛         |
|     |     |     |     |     |     |     |     | (𝛼∗,𝛼∗,…,𝛼∗)𝑇 | are model        | coefficients, | measured     | by           | maximizing | the       |
|     |     |     |     |     |     |     |     | 1 2           | 𝑛                |               |              |              |            |           |
objectivefunction:
𝑛
1 ∑ (𝛼∗−𝛼)(𝛼∗−𝛼
|     |     |     |     |     |     |     |     | −   | 𝑖 𝑗 )𝑘(𝑥,𝑥 | 𝑖 𝑗 )− |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------ | --- | --- | --- | --- |
|     |     |     |     |     |     |     |     | 2   | 𝑖 𝑗        |        |     |     |     |     |
𝑖,𝑗=1
(9)
|     |     |     |     |     |     |     |     | ∑ 𝑛 | ∑ 𝑛             |       |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --------------- | ----- | --- | --- | --- | --- |
|     |     |     |     |     |     |     |     | 𝜖   | (𝛼∗−𝛼)+ (𝛼∗−𝛼)𝑦 |       |     |     |     |     |
|     |     |     |     |     |     |     |     |     | 𝑖 𝑖             | 𝑖 𝑖 𝑖 |     |     |     |     |
|     |     |     |     |     |     |     |     | 𝑖=1 | 𝑖=1             |       |     |     |     |     |
subjecttotheconstraintsof:
𝑛
∑
(𝛼∗−𝛼)=0,0≤𝛼,𝛼∗≤𝐶
|     |     |     |     |     |     |     |     | 𝑖   | 𝑖 𝑖 𝑖 |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- |
𝑖=1
|     |     |     |     |     |     |     |     | While𝑦                                                     | istheindicatorofeachdatapoint(labelof𝑚 |     |     |     | and𝑚 | )and𝜖 |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------------------------------------------------- | -------------------------------------- | --- | --- | --- | ---- | ----- |
|     |     |     |     |     |     |     |     | 𝑖                                                          |                                        |     |     |     | 𝑖    | 𝑗     |
|     |     |     |     |     |     |     |     | and𝐶 areknownasthehyper-parametersusedtominimizethefitting |                                        |     |     |     |      |       |
errorfortheregression.
|     |     |     |     |     |     |     |     | Similarlytothe𝜀,foreachnon-linearregression,thereisanerror | 𝑟       |          |          |        |       |            |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------------------------------------------------- | ------- | -------- | -------- | ------ | ----- | ---------- |
|     |     |     |     |     |     |     |     | vector called                                              | 𝜀 . The | vector 𝜀 | includes | actual | error | values for |
Fig. 6. Different types of the relationship between variables X and Y. The top right 𝑆𝑉𝑅 𝑆𝑉𝑅
|     |     |     |     |     |     |     |     | eachentryof𝑚 | computedfromthedifferencebetweenanobserved𝑚 |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ------------------------------------------- | --- | --- | --- | --- | --- |
shows a linear relationship with high values of both the correlation and MI. In the 𝑖 𝑖
bottom right, there is a non-linear relationship that is well captured by the MI, but attime𝑡 andthecorrespondingcomputed𝑚 usingEq.(8).Weusethe
|     |     |     |     |     |     |     |     | 𝑛   |     |     |     | 𝑖   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
thecorrelationdoesnotreflectit.Thebottom-leftshowsnorelationshipandbothMI sameerrorevaluationmetricsofMAE,MAPE,MSE,RMSE,MedAE,and
and correlation are low. The top left is impossible since high correlation cause high max-errormeasuredfrom𝜀 foridentifiednon-linearrelationships.
𝑆𝑉𝑅
MIvalue.
Source:AdaptedfromLeeetal.(2012). Algorithm2,line4measuresNMIforeachpairofmetricsforevery
|     |     |     |     |     |     |     |     | edge. Then, | lines 8–10 | identify | and characterize | non-linear |     | relation- |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ---------- | -------- | ---------------- | ---------- | --- | --------- |
ships.
|                                                       |     |     |     |     |     |     |         | When                                  | applied to the | fictive | example, | 𝑟2 and NMI           | matrices | are |
| ----------------------------------------------------- | --- | --- | --- | --- | --- | --- | ------- | ------------------------------------- | -------------- | ------- | -------- | -------------------- | -------- | --- |
| conditionalentropydescribingtheuncertaintyof𝑋whenthe𝑌 |     |     |     |     |     |     | valueis |                                       |                |         |          |                      |          |     |
|                                                       |     |     |     |     |     |     |         | calculatedforeachedgeoftheCPGoverthe |                |         |          | matrices.Forexample, |          |     |
known.Themutualinformationisasymmetricvaluethatdescribesthe
|                       |     |     |       |                         |     |     |      | inFig.7,inStepI,𝑟2 | andNMImatricesarecalculatedbasedonthe |     |     |     |     |     |
| --------------------- | --- | --- | ----- | ----------------------- | --- | --- | ---- | ------------------ | -------------------------------------- | --- | --- | --- | --- | --- |
| reduceduncertaintyin𝑋 |     |     | when𝑌 | isknown.Iftwovariables𝑋 |     |     | and𝑌 |                    |                                        |     |     |     |     |     |
metricmatrixforedge𝑎→𝑏.Forrealcases,weneedalargesamplesize
| aredeterminedtogether,i.e.,if𝑌 |     |     |     | doesnotadduncertaintyto𝑋value, |     |     |     |     |     |     |     |     |     |     |
| ------------------------------ | --- | --- | --- | ------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
toconfidentlyidentifythetypeofrelationshipbetweenthemetrics.In
| then,𝑋 | and𝑌 | aredependentandtheconditionalentropyequalszero. |     |     |     |     |     |     |     |     |     |     |     |     |
| ------ | ---- | ----------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Fig.7,highlinearcorrelationcoefficientsareingreencolourandhigh
| In this | case, | 𝑁𝑀𝐼(𝑋,𝑌) | equals | one | that it means | NMI is | in its max |     |     |     |     |     |     |     |
| ------- | ----- | -------- | ------ | --- | ------------- | ------ | ---------- | --- | --- | --- | --- | --- | --- | --- |
value.ThehighertheNMIvalue,themoredependentthevariablesare. NMIvaluesareinblue.InStepII,twolinearrelationshipsandonenon-
𝑟2  linearrelationshipareidentifiedaccordingto𝑟2andNMI.Asshownin
| Similarly | to  | the for | a given | matrix, | we measure | an NMI | matrix |     |     |     |     |     |     |     |
| --------- | --- | ------- | ------- | ------- | ---------- | ------ | ------ | --- | --- | --- | --- | --- | --- | --- |
showingtheNMIvalueforeachpairofmetrics𝑚 1 to𝑚 6 . StepII,eachrelationshipischaracterizedbyaregressionfunction.
Finally,weannotatetheCPGbythefunctionsthatcharacterizethe
|     | ⎛ 𝑁 | 𝑀 𝐼 𝑚1,𝑚1 | 𝑁 𝑀 𝐼 | 𝑚1,𝑚2 | ⋯ 𝑁 𝑀 𝐼 𝑚1,𝑚𝑘 | ⎞   |     |     |     |     |     |     |     |     |
| --- | --- | --------- | ----- | ----- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
relationshipsbetweenthemetrics(Line11)inAlgorithm2.Fig.7,Step
|     | ⎜ 𝑁 | 𝑀 𝐼 | 𝑁 𝑀 𝐼 |     | ⋯ 𝑁 𝑀 𝐼 | ⎟   |     |     |     |     |     |     |     |     |
| --- | --- | --- | ----- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
𝑀𝐼=⎜ 𝑚2,𝑚1 𝑚2,𝑚2 𝑚2,𝑚𝑘⎟ (7) III,showstheannotatededge𝑎→𝑏sowingthelinearandnon-linear
|     | ⎜   | ⋮   | ⋮   |     | ⋱ ⋮ | ⎟   |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
relationships.OtheredgesoftheCPGareannotatedsimilarly.
|     | ⎜𝑁𝑀𝐼        |       | 𝑁𝑀𝐼       |            | ⋯ 𝑁𝑀𝐼    | ⎟       |           |                                             |     |     |     |     |     |     |
| --- | ----------- | ----- | --------- | ---------- | -------- | ------- | --------- | ------------------------------------------- | --- | --- | --- | --- | --- | --- |
|     | ⎝           | 𝑚𝑘,𝑚1 |           | 𝑚𝑘,𝑚2      | 𝑚𝑘,𝑚𝑘⎠   |         |           |                                             |     |     |     |     |     |     |
| An  | NMI greater | than  | a certain | threshold, | 𝑡 (which | will be | discussed |                                             |     |     |     |     |     |     |
|     |             |       |           |            |          |         |           | 3.4. DetectinganomaliesusingtheannotatedCPG |     |     |     |     |     |     |
later),indicatesthatthereiseitheralinearoranon-linearrelationship
betweentwovariables(Leeetal.,2012;Songetal.,2012;Jiangetal.,
|     |     |     |     |     |     |     |     | To detect | an anomaly | during | the system | execution, | we  | collect a |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ---------- | ------ | ---------- | ---------- | --- | --------- |
2011).Jiangetal.(2011)suggestusing𝑟2jointlywiththeNMIvalueto
|     |     |     |     |     |     |     |     | distributed | trace (we refer | to this | trace as | a test | trace) along | with |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --------------- | ------- | -------- | ------ | ------------ | ---- |
interprettheNMImagnitudeandidentifynon-linearrelationships.For
|                 |     |      |       |       |                         |     |     | profiling | metrics as the | system is | running. | Next, we | follow | the same |
| --------------- | --- | ---- | ----- | ----- | ----------------------- | --- | --- | --------- | -------------- | --------- | -------- | -------- | ------ | -------- |
| apairofmetrics𝑚 |     | and𝑚 | ,if𝑟2 |       | >0.6thenweconcludethat𝑚 |     | and |           |                |           |          |          |        |          |
|                 |     | 𝑖    | 𝑗     | 𝑚𝑖,𝑚𝑗 |                         |     | 𝑖   |           |                |           |          |          |        |          |
𝑚 arestronglylinearlycorrelated.Ontheotherhandif𝑟2 <0.6and steps of our method to build a CPG from the test trace and annotate
| 𝑗   |          |     |        |                                        |     | 𝑚𝑖,𝑚𝑗 |     |                 |           |          |           |          |        |          |
| --- | -------- | --- | ------ | -------------------------------------- | --- | ----- | --- | --------------- | --------- | -------- | --------- | -------- | ------ | -------- |
|     |          |     |        |                                        |     |       |     | it by labelling | the edges | with the | profiling | metrics. | We use | the term |
| 𝑁𝑀𝐼 | >=𝑡then𝑚 | 𝑖   | and𝑚 𝑗 | arenon-linearlycorrelated.Thethreshold |     |       |     |                 |           |          |           |          |        |          |
testCPGtorefertotheCPGextractedfromatesttrace.Notethatwe
𝑡needstobedeterminedbyanalysingthedataassuggestedbyJiang
|     |     |     |     |     |     |     |     | do not need | to model the | linear | and non-linear | correlations |     | between |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ------------ | ------ | -------------- | ------------ | --- | ------- |
etal.byJiangetal.(2011).Inthispaper,wefollowthesameapproach,
themetrics.Forthetesttrace,weonlyneedthevalueofthemetrics.
| explained | in  | the next | section, | to identify | the threshold | 𝑡 according | to  |                                        |     |     |     |                       |     |     |
| --------- | --- | -------- | -------- | ----------- | ------------- | ----------- | --- | -------------------------------------- | --- | --- | --- | --------------------- | --- | --- |
|           |     |          |          |             |               |             |     | Inotherwords,theprofilingmetricmatrix𝑃 |     |     |     | (1)correspondingtothe |     |     |
ourexperiments.
testtraceconsistsofonerowonly.Fig.8showsthestepsfordetecting
Tocharacterizeanon-linearrelationship,weusenon-linearSupport
anomaliesusingtheCPG.Inthisfigure,afictiveCPGisusedfortesting
VectorRegression(SVR)(Vapnik,1998;Vapniketal.,1996).SVRuses
inthedashed-bluerectanglewhileanedgeof𝑎→𝑏hasbeenannotated
| decision | boundaries |     | along with | a maximal | margin | to find | the best-fit |     |     |     |     |     |     |     |
| -------- | ---------- | --- | ---------- | --------- | ------ | ------- | ------------ | --- | --- | --- | --- | --- | --- | --- |
hyperplanebetweentwovariablesincludingthemaximumnumberof withitscorrespondingprofilingmetricasanexample.Inrealcases,all
data points on it. These points are called support vectors (SV). Non- edgesareannotatedwiththeirprofilingmetricmatrix.
lineardecisionboundariesofSVRtransformtheoriginalfeaturespace We compare the test CPG against the baseline CPG, which charac-
intoahigh-dimensionalspaceinwhichnon-linearrelationshipscanbe terizes the normal behaviour of the system (see Fig. 8). To achieve
estimated by a linear regression model. Feature space transformation this,weturntographmatching.Thegoalistodeterminewhetherthe
canbewrittenasamappingof𝜑∶𝑚,𝑚 𝑖 𝑗 →𝑍 andthetransformation testCPGisanedge-inducingsub-graphofthegeneralCPGornot.An
|     |     |     |     | 𝐾(𝑥,𝑥 | 𝜑(𝑥)𝑇𝜑(𝑥 |     | 𝑥   |     |     |     |     |     |     |     |
| --- | --- | --- | --- | ----- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
function (kernels) is defined as: 𝑖 𝑗 ) = 𝑖 𝑗 ), while ∈ edge-induced sub-graph includes a subset of edges and their incident
| 𝑚,𝑚 | .Thisfunctionshowshow𝑥 |     |     | iscomparedto𝑥 |     |     |     |     |     |     |     |     |     |     |
| --- | ---------------------- | --- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
𝑖 𝑗 𝑖 𝑗 . vertices. We use an extended version of the VF2 algorithm (Cordella
Thenon-linearSVRregressionfunctioniscalculatedas:
etal.,1998)tocheckifthebaselineCPGcontainsasub-graphthatis
𝑛
∑ (𝛼∗−𝛼)𝑘(𝑥,𝑥)+𝑏 isomorphictothetestCPG.ThetestCPGisisomorphictothegeneral
| 𝑤=  |     | 𝑖 𝑖 | 𝑖   |     |     |     | (8) |            |               |                   |     |         |           |        |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------------- | ----------------- | --- | ------- | --------- | ------ |
|     |     |     |     |     |     |     |     | CPG if and | only if there | is an isomorphism |     | mapping | for edges | issued |
𝑖=1,𝑥∈𝑆𝑉
10

M.Panahandehetal.
TheJournalofSystems&Software209(2024)111917
Fig.7. ModellingmetricrelationshipsandAnnotatingCPG.(I),𝑟2 andNMIarecalculatedforeachpairofmetrics.Next,instep(II)identifiedrelationshipsarecharacterized,
and(III)theCPGisannotatedwiththecharacterizedrelationships.(Forinterpretationofthereferencestocolourinthisfigurelegend,thereaderisreferredtothewebversion
ofthisarticle.)
|     |     |     |     |     |     |     | CPG. In | this case, the | test CPG | is not | a sub-graph |     | of the baseline |     |
| --- | --- | --- | --- | --- | --- | --- | ------- | -------------- | -------- | ------ | ----------- | --- | --------------- | --- |
CPGbecauseofnode‘‘f’’.Secondly,metriccheckingfortheannotated
instanceedgeof𝑎→𝑏resultsinviolatingtwofunctionsoutofthree:
⎧Responsesize,queuetime:|350−(10∗7+70)|≰20
⎪ Latency,Throughput:|2−(0.6+0.2)|≰1.0
⎨
|     |     |     |     |     |     |     | ⎪ Requestduration,RequestSize:|1.3−(0.5∗1650.5−4.5)| |     |     |     |     |     | ≤0.7 |     |
| --- | --- | --- | --- | --- | --- | --- | ---------------------------------------------------- | --- | --- | --- | --- | --- | ---- | --- |
⎩
|     |     |     |     |     |     |     | We perform     | metric checking   | for        | all common |          | edges    | between       | the test |
| --- | --- | --- | --- | --- | --- | --- | -------------- | ----------------- | ---------- | ---------- | -------- | -------- | ------------- | -------- |
|     |     |     |     |     |     |     | CPG and        | the baseline.     | Finally,   | according  | to       | Fig. 8,  | any violation | in       |
|     |     |     |     |     |     |     | graph checking | and metric        | checking   | is         | reported | to       | the analyst   | as an    |
|     |     |     |     |     |     |     | anomaly.       | We also highlight | violations |            | in the   | baseline | CPG for       | further  |
anomalyanalysis.Otherwise,ifthetestCPGmatchesthebaselineCPG,
thetesttraceisrecognizedasanormaltrace.
3.5. AnalysingServiceAnomalyusageprocessandcomplexity
|                 |           |         |       |                 |        |                    | Fig. 9   | shows how          | our approach |              | can be | used   | in practice. | First, |
| --------------- | --------- | ------- | ----- | --------------- | ------ | ------------------ | -------- | ------------------ | ------------ | ------------ | ------ | ------ | ------------ | ------ |
|                 |           |         |       |                 |        |                    | the user | needs to configure | the          | microservice |        | system | to provide   | the    |
| Fig. 8. Anomaly | detecting | process | using | ServiceAnomaly. | A test | trace and observed |          |                    |              |              |        |        |              |        |
metricsaremodelledinatestCPG.Then,thetestCPGiscomparedwiththegeneral necessary telemetry data for ServiceAnomaly. Our proposed architec-
CPGusingtwostepsofgraphmatchingandmetricmatching.(Forinterpretationofthe ture for data collection is detailed in Section 3.1. In this paper, we
referencestocolourinthisfigurelegend,thereaderisreferredtothewebversionof deployed microservices on Kubernetes, where Prometheus and Jaeger
thisarticle.)
|     |     |     |     |     |     |     | were added | as monitoring | systems | into | the Kubernetes |     | cluster. | How- |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ------------- | ------- | ---- | -------------- | --- | -------- | ---- |
ever,ServiceAnomalycanbeintegratedwithalternativearchitectures
thatoffertheessentialtelemetrydata.
fromthesamevertices.SinceourCPGgraphsaredirectedgraphs,we To enable data collection, the user needs to (a) inject Istio agents
usedirectedsub-graphmatching. intotherunningKubernetespodstoenablethedatacollectionprocess,
In addition, we compare the test CPG against the baseline CPG (b) deploy Prometheus and Jaeger into the Kubernetes clusters and
to make sure that the metrics match. In this step, we check whether configure them to collect data from Istio agents, and (c) optionally,
| common | edges’ annotations |     | are matched | together. |     | Edges’ annotation |     |     |     |     |     |     |     |     |
| ------ | ------------------ | --- | ----------- | --------- | --- | ----------------- | --- | --- | --- | --- | --- | --- | --- | --- |
ifneeded,performinstrumentationonthemicroservices.Afterthein-
inthetestCPGisaprofilingmetricmatrix.Thesematricesaretested
stallationofPrometheusandJaeger,additionalinstrumentationmight
againstlinearandnon-linearfunctionsannotatedonthebaselineCPG’s
|             |            |            |           |         |              |                  | be necessary | for users looking |           | to collect | customized |      | profiling       | metrics |
| ----------- | ---------- | ---------- | --------- | ------- | ------------ | ---------------- | ------------ | ----------------- | --------- | ---------- | ---------- | ---- | --------------- | ------- |
| edges. We   | check to   | see if the | profiling | metric  | values       | at the test time |              |                   |           |            |            |      |                 |         |
|             |            |            |           |         |              |                  | (e.g., the   | CPU usage of      | services) | or         | customize  | span | specifications. |         |
| satisfy the | linear and | non-linear |           | metrics | relationship | functions. To    |              |                   |           |            |            |      |                 |         |
Forexample,Next,thecollecteddataisacquiredbyServiceAnomaly,
identify the degree by which a metric in the test CPG matches the showninthedashedboxinFig.9,whichisusedtobuildtheCPGand
functionsonthebaselineCPF,weneedtodefinethemarginofaccepted profilingmetricsmodels.
error. As mentioned in Section 3.3.2, in this paper, we analyse six During the test time, which we refer to as online setup, the user
differenterrorevaluationmetricscomputedforeach𝜖 𝑟 ,𝜖 𝑆𝑉𝑅 vectorsof collectsatesttracealongwithitscorrespondingprofilingmetricsusing
linearandnon-linearrelationships.Thesemetricsspecifytheaccepted theJaegerandPrometheusdashboardsorbyqueryingtheirAPIs.The
deviationmarginfortheprofilingmetricvaluesatthetesttime.Wewill data collected during this test phase is then fed to ServiceAnomaly.
discusstheimpactofthemarginvaluesonanomalydetectionaccuracy Withintheonlinesetup,constructingtheCPG,annotatingtheCPG,and
inSection4. graphmatchingarecarriedouttogeneratetheoutputincludingthetest
Fig. 8 shows the baseline CPG built from the fictive traces t1–t3 annotated CPG and then the anomaly detection result. If an anomaly
in a green rectangle. The edge of 𝑎 → 𝑏 has been annotated with is detected, the nodes and edges that deviate from the baseline CPG,
| the metric | relationship | functions |     | and error | evaluation | metric as an |     |     |     |     |     |     |     |     |
| ---------- | ------------ | --------- | --- | --------- | ---------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
i.e.,unseennodesandedges,arehighlighted.Additionally,anyviolated
example. Checking the test CPG against the baseline CPG includes I) linear and nonlinear relationships are also flagged in the test CPG,
checking if the test CPG is an edge-induce sub-graph of the baseline along with the degree of violation for each relationship. The process
CPG; and II) if for each common edge, the relationships between the of analysing a test trace against the baseline annotated CPG can be
metricsonthetestCPGmatchtheannotatedfunctiononthebaseline repeatedforupcomingtesttraces.
11

M.Panahandehetal. TheJournalofSystems&Software209(2024)111917
The computational complexity of the online phase of
ServiceAnomaly, which is detecting anomalies using the annotated
CPG,comprisesseveraltasks:ConstructingtheCPGforthetesttrace,
AnnotatingtheCPG,GraphMatchingandMetricMatching.Giventhat
a test trace with a constant number of spans, the complexities of all
tasks are overshadowed by the task of graph matching. (Annotation
E1) The graph matching algorithm for a graph with s’ nodes has
complexities ranging from 𝑂(𝑠′2) to 𝑂(𝑠′!𝑠′) (Cordella et al., 2004).
However, as shown by Luks (Luks, 1982), graph-matching algorithms
demonstratepolynomialcomplexityinscenariosinvolvinggraphswith
tree-likestructuresandboundednodevalence.Thisfindingisespecially
relevant to our study, in which a test CPG derived from a request
inherently possesses a tree-like configuration with limited inter-nodal
connections. In the specified context of our study, the test CPGs are
characterizedaslabelled,directedtreessharingidenticalpartswiththe
generalCPG.Infact,bothnormalandabnormaltestCPGsareexpected
to differ from the general CPG only in certain segments. Moreover,
theseCPGsarestructuredasDirectedAcyclicGraphs(DAGs),wherein
Fig.9. UserinteractionwithServiceAnomaly.
common subtrees are encapsulated singularly, thereby eliminating
redundantembeddingsoftheentiretestCPGwithinthegeneralCPG.
These characteristics contribute to the feasibility of graph matching,
To analyse the computational complexity of ServiceAnomaly, we
enablingefficientpruningofthesearchspaceandswiftidentification
breakitdownintodistinctcomputationalfunctions.AsshowninFig.9,
ofmatchingnodesbetweenthetestCPGandthegeneralCPG.
ServiceAnomalyoperatesinbothofflineandonlinephases.Theoffline
phaseofServiceAnomalyincludes(a)constructingtheContextPropa-
4. Experimentalsetup
gationGraph,(b)modellingmetricrelationships,and(c)constructing
theAnnotatedContextPropagationGraph.
Inthissection,weexplainthedesignoftheexperimentthatweused
ConstructingContextPropagationGraphexplainedbyAlgorithm1 toevaluateourServiceAnomalyapproachandtoanswerthefollowing
involves performing several functions for each trace of the collected researchquestions:
set of 𝑇 traces. These functions include Construct-Rooted-Call-Trees,
Merge-by-Union,andConvert-to-DAG.TheConstruct-Rooted-Call-Trees • RQ1—HowaccurateisServiceAnomalyatdetectinganomalies?
function exhibits linear complexity, reliant on the span count within • RQ2—HowcantheServiceAnomalyapproachbeusedtoreason
each trace. Moreover, the computation complexity of the Merge-by- aboutanomalies?
Union function is derived by traversing the input rooted trees. We • RQ3—WhatarethelimitationsofServiceAnomalyindetecting
use a hash table structure to search through rooted trees capping the anomalies?
complexity of merging rooted trees at the complexity of converting
them to hash maps—this conversion’s complexity is linked to rooted 4.1. Targetsystems
tree size. In the worst case scenario, if 𝑆 denotes the service count
within the longest trace and there is a call between each pair of We use two open-source microservice applications, TeaStore1 and
services,therootedtreeresultsin ( 𝑆 ) edges,calledthetreesize. TrainTicket.2 TeaStore was developed as a benchmark to conduct ex-
2=𝑆(𝑆
2
−1)
perimentswithperformancemodellingtechniques.Thetoolemulatesa
Therefore,thecomplexityoftheMerge-by-Unionisprimarilydictated
teawebstoreforautomatically-generatedteaproducts(vonKistowski
by𝑂(𝑆2).FortheConvert-to-DAGfunction,weadoptasimilarstrategy
etal.,2018).TeaStorehassixmicroservicesincludingWebUI,Image-
proposed by Hamou-Lhadj and Lethbridge (2002), using a hash table
Provider, Auth, Persistence, Recommender, and a Registry service.
tomaintaincertificatesandsignatures.AccordingtoHamou-Lhadjand
TrainTicket is one of the academic largest open-source microservice
Lethbridge (2002), if a tree’s degree (the count of children for any
systems to our knowledge with over 30 microservices and many ser-
node) remains bounded by a constant, the Convert-to-DAG function
vice dependencies. Examples of microservices of TrainTicket include
performsinlineartime.Asaresult,thecomputationcomplexityofthe
servicesprovidingticketenquiry,reservation,foodandseatselection,
Constructing Context Propagation Graph step drives from 𝑂(𝑇𝑆2) in
payment,searchontravelandroutes,consign,etc.Zhouetal.(2018).
which𝑇 representsthetracecountand𝑆 isthenumberofservices.
TrainTicketisdeployedon56Kubernetespodscomposedof32logical
Algorithm2explainsthestepsrelatedtomodellingmetricrelation-
microservicesimplementedinJava,node.js,Python,andGo,aswellas
ships and constructing the Annotated Context Propagation Graph of
24MongoDBandMySqldatabase-relatedservices.
ServiceAnomalyintheofflinesetup.Thisalgorithmrequirescomputa-
tionsof𝑟2 (Eq.(3)),𝑁𝑀𝐼 (Eq.(6)),regressionfunction(Eq.(5)),and
4.2. Datacollection
non-linear SVR regression function (Eq. (8)) for each edge within the
baselineCPG.Thecomputationcomplexityof𝑟2isdirectlyproportional
Tocollectdistributedtracesandprofilingmetricsthatcharacterize
to the number of data points within the amassed profiling metrics,
thenormalbehaviourofTeaStoreandTrainTicketsystems,weexecuted
resulting in a linear function. The computation of 𝑁𝑀𝐼—as defined
theloadtestsuitesthataccompanythesesystems.Theobjectiveisto
by Danon et al. (2005)—exhibits a complexity of 𝑂(𝑛+𝐾2), where 𝑛
exercise as many execution paths as possible. For TeaStore, we used
representsthedatapointcountoftheprofilingmetrics,and𝑘signifies
JMeter (Anon., 2022a) to run the load tests. We simulated 10,000
the number of distinct categories or clusters. According to documen- user requests with different numbers of concurrent active users to
tation (scikit learn, 2023), finding the regression function has linear test the system under different stress load scenarios. Finally, we used
complexitywhilethenon-linearSVRregressionfunctioncomplexityis
morethanquadraticwiththenumberofsamples,approximatedbyHui
etal.(2016)at𝑂(𝑛3).ThereforeifthebaselineCPGconsistsof𝐸edges, 1 https://github.com/DescartesResearch/TeaStore
thedominantcomputationcomplexityofAlgorithm2is𝑂(𝐸𝑛3). 2 https://github.com/FudanSELab/train-ticket/wiki
12

M.Panahandehetal.
TheJournalofSystems&Software209(2024)111917
|          |         |      |                 | Fig.10. | Serviceperformancechangeatthetimeofinjectedfaults,at7:00PM. |        |          |        |     |     |     |     |     |     |     |
| -------- | ------- | ---- | --------------- | ------- | ----------------------------------------------------------- | ------ | -------- | ------ | --- | --- | --- | --- | --- | --- | --- |
| a sample | of more | than | 3000 successful |         | distributed                                                 | traces | and 9160 | Table2 |     |     |     |     |     |     |     |
Collecteddataforeachcasestudy.
| rows of    | six metrics | collected |           | in a one-minute |           | window. | TrainTicket |         |                      |     |     |                      |     |     |     |
| ---------- | ----------- | --------- | --------- | --------------- | --------- | ------- | ----------- | ------- | -------------------- | --- | --- | -------------------- | --- | --- | --- |
|            |             |           |           |                 |           |         |             |         | Trainingdatato       |     |     | Normalandanomaly     |     |     |     |
| comes with | 15          | load test | scenarios | written         | in Python | and     | JavaScript, |         |                      |     |     |                      |     |     |     |
|            |             |           |           |                 |           |         |             | Systems | constructbaselineCPG |     |     | tracesusedfortesting |     |     |     |
whichweexecutedusingadifferentnumberofconcurrentactiveusers.
We collected more than 5000 traces and 5410 rows of metrics for Traces Metrics Normaltraces Anomalytraces
TrainTicket.Weusedfourscenariosforinjectingfaultsintothesystems TeaStore 3000 9160 15 15
|     |     |     |     |     |     |     |     | TrainTicket | 5000 | 5410 |     | 32  |     | 32  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ---- | ---- | --- | --- | --- | --- | --- |
basedontheliteratureLinetal.(2018),Nedelkoskietal.(2019a)and
Brandónetal.(2020).
| Stressing | the hosts: | We  | generated | resource | stress | by targeting | 80%– |     |     |     |     |     |     |     |     |
| --------- | ---------- | --- | --------- | -------- | ------ | ------------ | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
Intotal,weinjected15faultsintoTeaStoreand32inTrainTicket.
| 100% of | the CPU | and | disk capacity | of  | the node | running | the target |     |     |     |     |     |     |     |     |
| ------- | ------- | --- | ------------- | --- | -------- | ------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
Inadditiontothedatacollectedafterfaultinjectionintothetargetsys-
| service. To | do this, | we  | used Stress-ng,3 |     | or Linux | CPU exhausting | test |     |     |     |     |     |     |     |     |
| ----------- | -------- | --- | ---------------- | --- | -------- | -------------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
tems,wealsogatheredanequalamountofnormaltracesandprofiling
| to impose | an amount | of  | CPU on | the host | (Lin | et al., 2018; | Brandón |              |           |      |             |     |        |          |          |
| --------- | --------- | --- | ------ | -------- | ---- | ------------- | ------- | ------------ | --------- | ---- | ----------- | --- | ------ | -------- | -------- |
|           |           |     |        |          |      |               |         | metrics. The | collected | data | from normal | and | faulty | requests | are used |
etal.,2020). togetherasourtestdatainevaluatingourmethod.Table2showsthe
|         |          |             |     |             |         |     |             | number of | collected | traces | and profiling | metric | rows | that are | used to |
| ------- | -------- | ----------- | --- | ----------- | ------- | --- | ----------- | --------- | --------- | ------ | ------------- | ------ | ---- | -------- | ------- |
| Service | latency: | We injected |     | a 15-second | latency | for | %80 of HTTP |           |           |        |               |        |      |          |         |
constructthebaselineannotatedCPG,aswellasthenumberofnormal
| traffic passing | through | the | target | service. | We use | Kiali4 | to add a rule |     |     |     |     |     |     |     |     |
| --------------- | ------- | --- | ------ | -------- | ------ | ------ | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
andfaultytracesusedtoevaluatetheeffectivenessofServiceAnomaly
| to the Istio | service | mesh | and | control traffic | transmitting |     | across the |     |     |     |     |     |     |     |     |
| ------------ | ------- | ---- | --- | --------------- | ------------ | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
todetectanomalies.
targetservice.UsingKiali,weadda15-secondlatencytotheIstioagent
runninginsidethetargetservicepod.TheIstioagentappliesthelatency
4.3. BuildingthebaselineannotatedCPGs
| tothetestingservicetraffic |     |     | (Linetal.,2018;Nedelkoskietal.,2019a; |     |     |     |     |     |     |     |     |     |     |     |     |
| -------------------------- | --- | --- | ------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Brandónetal.,2020). We built the baseline annotated CPG for each system using the
|     |     |     |     |     |     |     |     | collected distributed |     | traces | and profiling | metrics. | Table | 3 shows | the |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------------- | --- | ------ | ------------- | -------- | ----- | ------- | --- |
Servicetimeout:Networkconnectionfailuresmightcauseanerroror
|                |            |       |          |           |          |          |              | number of            | nodes,        | edges, and | an average | number      | of      | linear        | and non- |
| -------------- | ---------- | ----- | -------- | --------- | -------- | -------- | ------------ | -------------------- | ------------- | ---------- | ---------- | ----------- | ------- | ------------- | -------- |
| failed request | instead    | of    | a delay. | To induce | request  | failure, | we used      |                      |               |            |            |             |         |               |          |
|                |            |       |          |           |          |          |              | linear relationships |               | per edge   | in the     | CPG. The    | maximum | number        | of       |
| Kiali and      | instrument | Istio | traffic  | routing   | rules to | inject   | a timeout in |                      |               |            |            |             |         |               |          |
|                |            |       |          |           |          |          |              | all possible         | relationships | for        | each       | edge of the | CPG     | is the number | of       |
trafficpassingthroughthetargetservice.Weadded5secondstimeout
𝑚
forthetargetservice,whichmeansthetargetservicestopsanswering combinations of metrics considering two metrics at a time that is
𝑚!
|                                                           |            |     |          |             |     |           |            | . In             | our case, | at every      | edge,       | at most     | 15 metric | relationships |      |
| --------------------------------------------------------- | ---------- | --- | -------- | ----------- | --- | --------- | ---------- | ---------------- | --------- | ------------- | ----------- | ----------- | --------- | ------------- | ---- |
| therequestsiftheytakelongerthan5secondsandatimeouterroris |            |     |          |             |     |           |            | 2!(𝑚−2)!         |           |               |             |             |           |               |      |
|                                                           |            |     |          |             |     |           |            | are possible     | to be     | characterized | for         | each linear | and       | non-linear    | type |
| returned.                                                 | To trigger | the | timeout, | we injected | a   | 10-second | latency in |                  |           |               |             |             |           |               |      |
|                                                           |            |     |          |             |     |           |            | of relationship. | However,  |               | it is clear | that we     | have      | fewer numbers | of   |
oneofthetestingservice’sdependencies.Allinjectedrulesareapplied
|     |     |     |     |     |     |     |     | relationships | since | there might | not | be a relationship |     | between | each |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | ----- | ----------- | --- | ----------------- | --- | ------- | ---- |
tothepassingtrafficbyIstio(Brandónetal.,2020).
|                                                         |     |     |     |     |     |     |     | pair of metrics | or  | the relationship |     | might | not be | significant | to be |
| ------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- | ---------------- | --- | ----- | ------ | ----------- | ----- |
| Servicehangup:Tosimulateadeadprocessoraservicehangup,we |     |     |     |     |     |     |     | characterized.  |     |                  |     |       |        |             |       |
pause the pod running the target service. Killing a pod is simulated AsmentionedinSection3.3.2,weadoptthesameprocessproposed
|     |     |     |     |     |     |     |     | by Jiang et | al. (2011) | to interpret |     | 𝑟2 and NMI | values | for each | target |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ---------- | ------------ | --- | ---------- | ------ | -------- | ------ |
byscalingdowntheKubernetesdeploymentwithzeroreplicasofthe
|     |     |     |     |     |     |     |     | systemandfindlinearandnon-linearrelationships.Weconsider𝑟2 |     |     |     |     |     |     | >   |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
testingservice’spod(Linetal.,2018;Nedelkoskietal.,2019a).
0.6asanindicatorofastronglinearrelationshipassuggestedbyJiang
| At the | test time, | we  | execute | 2 to 3 | requests | per second | for each |     |     |     |     |     |     |     |     |
| ------ | ---------- | --- | ------- | ------ | -------- | ---------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
etal.(2011).Tofindthebest𝑡thresholdforNMIvalues,foreachtarget
| target system.  | To  | collect | normal | test traces, | we    | continuously | monitor  |                                          |         |        |         |           |            |                |         |
| --------------- | --- | ------- | ------ | ------------ | ----- | ------------ | -------- | ---------------------------------------- | ------- | ------ | ------- | --------- | ---------- | -------------- | ------- |
|                 |     |         |        |              |       |              |          | system, we                               | compute | 𝑟2 and | NMI for | all pairs | of metrics | and            | compare |
| the performance |     | of the  | target | system using | Kiali | to ensure    | that the |                                          |         |        |         |           |            |                |         |
|                 |     |         |        |              |       |              |          | NMIto𝑟2.Fig.11showsthatforTeaStorewhen𝑟2 |         |        |         |           |            | ≥0.6andthereis |         |
systemisoperatingasnormal.Forcollectinganomalytraces,weinject
astronglinearrelationshipbetweenmetrics,NMIvalueisatleast0.6.
faultsintoindividualservices,oneatatime.Thesystemperformance Weknowthatforalinearrelationshipboth𝑟2andNMIareattheirhigh
ismonitoredbeforeandafterinjectingafault.Tomakesurethatthe values.WeconsiderNMI>0.6asthethresholdfordeterminingahigh
collected trace contains a fault, we use Kiali to check the changes in NMIvalueforTeaStore.Moreover,weknowthatcorrelateddatawitha
theexecutionofthesystemthatarecausedbythefault.Fig.10shows non-linearrelationshipshowsalow𝑟2
andhighNMIvalue.Therefore,
examplesofchangesinthesystemexecutionafterinjectingafault. 𝑟2 ≥
|     |     |     |     |     |     |     |     | when < | 0.6 and | NMI | 0.6 we | identify | non-linear | relationships. |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | ------- | --- | ------ | -------- | ---------- | -------------- | --- |
AccordingtoFig.11,thethresholdfortheTrainTicketsystemisNMI
=0.47andforTeaStoreisNMI=0.6.
3 https://wiki.ubuntu.com/Kernel/Reference/stress-ng Fig. 12 shows a partial view of the baseline CPG for TeaStore.
4 https://kiali.io/ TheCPGisontherightsideandthemetricrelationshipfunctionsfor
13

M.Panahandehetal.
TheJournalofSystems&Software209(2024)111917
| Table3 |     |     |     |     |     |     | • FalseNegative(FN):Ananomalytracedetectedashealthy |     |     |     |     |     |     |
| ------ | --- | --- | --- | --- | --- | --- | --------------------------------------------------- | --- | --- | --- | --- | --- | --- |
CPGcharacteristicsforeachsystem. • TrueNegative(TN):Ahealthytracedetectedashealthy
| SUT | #Nodes | #Edges | Avg#Linear |     | Avg#Nonlinear |     |     |     |     |     |     |     |     |
| --- | ------ | ------ | ---------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
relations/edge relations/edge Theprecisionreflectsthenumberofcorrectpositivepredictionsoutof
TeaStore 6 12 3.6 1.5 allpositivepredictionsmade,whichincludethosefalselyclassifiedas
| TrainTicket | 32  | 83  | 4.0 |     | 2.95 |     |     |     |     |     |     |     |     |
| ----------- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
anomalies,anditismeasuredas:
𝑇𝑃
𝑃𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛=
𝑇𝑃+𝐹𝑃
Therecallquantifiesthenumberofpositiveclasspredictionsmadeout
ofallpositivecasesinthedataset,calculatedas:
|     |     |     |     |     |     |     | 𝑅𝑒𝑐𝑎𝑙𝑙= | 𝑇𝑃  |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- |
𝑇𝑃+𝐹𝑁
|     |     |     |     |     |     |     | F1-score | is a single score | that balances |     | precision | and recall | and is |
| --- | --- | --- | --- | --- | --- | --- | -------- | ----------------- | ------------- | --- | --------- | ---------- | ------ |
definedastheharmonicmeanofPrecisionandRecall:
𝑃𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛∗𝑅𝑒𝑐𝑎𝑙𝑙
𝐹1−𝑠𝑐𝑜𝑟𝑒=2∗
𝑃𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛+𝑅𝑒𝑐𝑎𝑙𝑙
5. Results
|     |     |     |     |     |     |     | 5.1. RQ1.HowaccurateisServiceAnomalyatdetectinganomalies? |                     |            |         |             |                |         |
| --- | --- | --- | --- | --- | --- | --- | --------------------------------------------------------- | ------------------- | ---------- | ------- | ----------- | -------------- | ------- |
|     |     |     |     |     |     |     | The accuracy                                              | of ServiceAnomaly   |            | can     | be affected | by the         | choice  |
|     |     |     |     |     |     |     | between                                                   | different error     | evaluation | metrics | since       | they determine | the     |
|     |     |     |     |     |     |     | expected                                                  | amount of deviation | in         | anomaly | detection.  | Table          | 4 shows |
precision,recall,andF1-scoreforbothTeaStoreandTrainTicketwith
thesixdifferenterrorevaluationmetricsdiscussedinSection3.3.2.As
showninTable4,ourapproachachievesanF1-scoreofupto85%for
TeaStoreand86%forTrainTicket.
Thechoicebetweenerrorevaluationmetricsdependsonthespecific
characteristicsofthedataset.Inourcase,wehaveobservedthatusing
theRMSEerrorevaluationmetrictoassesstheaccuracyofthemodel
|     |     |     |     |     |     |     | yields the    | best results compared |           | to other | error evaluation | metrics           | for |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --------------------- | --------- | -------- | ---------------- | ----------------- | --- |
|     |     |     |     |     |     |     | both systems. | This may              | be due to | the fact | that             | RMSE is sensitive | to  |
outliersandthereforepenalizeslargeerrors,resultinginamodelthat
| Fig.11. | 𝑟2 andNMImeasuredforpairofmetricsinTeaStoreandTrainTicket. |     |     |     |     |     |          |                        |      |               |     |            |        |
| ------- | ---------------------------------------------------------- | --- | --- | --- | --- | --- | -------- | ---------------------- | ---- | ------------- | --- | ---------- | ------ |
|         |                                                            |     |     |     |     |     | provides | better classification. | This | is contrasted |     | with MAPE, | MedAE, |
andMAE,whicharenotassensitivetooutliersasRMSE(Gzyletal.,
each edge are listed on the left side of the figure. Fig. 12 shows five 2023).Table4showsthatmodelsobtainedusingtheseerrorevaluation
linearrelationships.Thefigurealsoshowsonenon-linearrelationship metricshaveaveryhighrecall(100%forTeaStoreandupto94%for
for the edge connecting the services ‘‘teastore-auth’’ and ‘‘teastore- TrainTicket),andalowprecision(50%to60%forTeaStore)and(48%
persistence’’. To clearly characterize the relationships, a partial heat to 58% for TrainTicket), meaning that they introduce a considerable
|               |         |           |            |              |          |     | number of | false positives | (i.e., healthy | traces | detected | as anomalies). |     |
| ------------- | ------- | --------- | ---------- | ------------ | -------- | --- | --------- | --------------- | -------------- | ------ | -------- | -------------- | --- |
| map for three | metrics | collected | over these | two services | is shown | in  |           |                 |                |        |          |                |     |
Fig. 13. As shown, there is a high correlation between the latency Wealsofoundthatoutofthe15anomalytracesofTeaStore,7werede-
and request size, highlighted by a circle, which results in a linear tectedusingtheCPGmatchingalone,and7weredetectedwithmetric
relationship between these metrics. Similarly, a high NMI value and matching with RMSE. The remaining anomaly trace was not detected
low correlation between the latency and queue time, highlighted by asananomaly,whichexplainsarecallof93%.Outofthe7anomaly
squares in the figure, results in a non-linear relationship between tracesdetectedbyCPGmatching,2wereaffectedbyaninjectedservice
latencyandqueuetime.ThelowcorrelationcoefficientandNMIvalues latency, 3 were affected by an injected service timeout, and 2 were
forrequestsizeandqueuesizeindicatethatthesemetricsdonothave affected by an injected service hangup scenario. Furthermore, the 7
arelationship.
detectedanomalytracesthroughmetricmatchingincluded3collected
|     |     |     |     |     |     |     | after injecting | a stress scenario, | 2   | after injecting |     | a latency, 1 | after an |
| --- | --- | --- | --- | --- | --- | --- | --------------- | ------------------ | --- | --------------- | --- | ------------ | -------- |
4.4. Evaluationmetrics
|     |     |     |     |     |     |     | injected service | timeout, | and 1 after | an  | injected | service hangup. | We  |
| --- | --- | --- | --- | --- | --- | --- | ---------------- | -------- | ----------- | --- | -------- | --------------- | --- |
didasimilaranalysisonTrainTicketandfoundthatoutof32anomaly
| To assess | the accuracy | of  | our method, we | measure | the precision, |     |     |     |     |     |     |     |     |
| --------- | ------------ | --- | -------------- | ------- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
traces,5weredetectedusingCPGmatchingand25weredetectedusing
recall,andF1score.Thesemeasuresareusedtodescribeatestaccuracy
|     |     |     |     |     |     |     | metric matching | with RMSE. | Among | the | 5 detected | anomaly | traces |
| --- | --- | --- | --- | --- | --- | --- | --------------- | ---------- | ----- | --- | ---------- | ------- | ------ |
which detects the presence or absence of a condition (Yerushalmy, usingCPGmatching,3wereattributedtoaninjectedservicetimeout
1947).Inourcase,thepositivecondition,P,isdefinedasthenumber
|     |     |     |     |     |     |     | scenario, | one to an injected | service | latency, | and | one to an | injected |
| --- | --- | --- | --- | --- | --- | --- | --------- | ------------------ | ------- | -------- | --- | --------- | -------- |
ofrealanomalies,i.e.testtracescollectedwhenweinjectedfault/stress
|            |                  |     |               |               |     |        | service hangup. | Similarly, | with | metric matching, |     | 25 anomaly | traces |
| ---------- | ---------------- | --- | ------------- | ------------- | --- | ------ | --------------- | ---------- | ---- | ---------------- | --- | ---------- | ------ |
| scenarios, | and the negative |     | condition, N, | is the number | of  | normal |                 |            |      |                  |     |            |        |
weredetected,where8werecollectedafterinjectingaservicelatency
traces.
scenario,7afterinjectingaservicetimeout,6afterstressingthehost,
Accordingtotheerroroftheanomalydetection,differentoutcomes
and4afterinjectingaservicehangup.
includingtrue(T)andfalse(F)resultscanbeconcluded.
Basedonouranalysis,wecanconcludethatbothCPGmatchingand
•
TruePositive(TP):Ananomalytracedetectedasanomaly metricmatchingareneededtodetectavarietyoffaultsinmicroservice
•
| FalsePositive(FP):Ahealthytracedetectedasanomaly |     |     |     |     |     |     | applications. |     |     |     |     |     |     |
| ------------------------------------------------ | --- | --- | --- | --- | --- | --- | ------------- | --- | --- | --- | --- | --- | --- |
14

M.Panahandehetal.
TheJournalofSystems&Software209(2024)111917
Fig.12. ApartialbaselineannotatedCPGforTeaStore.
|     |     |     |     | 5.2. RQ2. | How can | the | ServiceAnomaly |     | approach | be used to | analyse |
| --- | --- | --- | --- | --------- | ------- | --- | -------------- | --- | -------- | ---------- | ------- |
anomalies?
Inthisquestion,weshowhowourapproachcanhelpdevelopersto
betterunderstandtheanomaliesbyexploringtheannotatedCPG.
|     |     |     |     | In the       | following, | we          | select two | examples     | of  | anomaly traces | from     |
| --- | --- | --- | --- | ------------ | ---------- | ----------- | ---------- | ------------ | --- | -------------- | -------- |
|     |     |     |     | the TeaStore | and        | TrainTicket | systems    | respectively |     | that were      | detected |
intheprevioussectionandexaminethecausesoftheanomaliesusing
theCPGandthemetricsmodel.
5.2.1. Scenario1:TrainTicketanomalytrace
|     |     |     |     | Fig. 14-(a)   | shows    | a      | portion        | of a TrainTicket |          | anomaly        | trace us- |
| --- | --- | --- | --- | ------------- | -------- | ------ | -------------- | ---------------- | -------- | -------------- | --------- |
|     |     |     |     | ing Jaeger.   | We could | not    | show           | the entire       | trace,   | which contains | 28        |
|     |     |     |     | spans showing | a        | record | of the various | services         | involved | in             | reserving |
aticketusingtheTrainTicketsystem.Toreserveaticket,inanormal
trace,first,the‘‘ts-ui-dashboard’’callsthe‘‘ts-preserve-service’’.Then,
|     |     |     |     | the ‘‘ts-preserve-service’’ |     |     | span invokes | a   | series of | services, | including |
| --- | --- | --- | --- | --------------------------- | --- | --- | ------------ | --- | --------- | --------- | --------- |
‘‘ts-security-service’’,‘‘ts-contact-service’’,‘‘ts-travel-service’’,andeight
otherservices,inasequentialmannertocompletetherequest.
|     |     |     |     | Fig. 14-(b) | shows | part | of the | TrainTicket’s | baseline | CPG | including |
| --- | --- | --- | --- | ----------- | ----- | ---- | ------ | ------------- | -------- | --- | --------- |
thecontextpropagationpathsinvokedasaresultofaticketreservation
|     |     |     |     | request. However, |     | in this | scenario, | we simulated |     | a timeout | fault sce- |
| --- | --- | --- | --- | ----------------- | --- | ------- | --------- | ------------ | --- | --------- | ---------- |
nariointo‘‘ts-preserve-service’’usingKialiasexplainedinSection3.1.
Fig.13. Apartialheat-mapforanedgeofTeaStore. Weusedthefaultinjectionwizardon‘‘ts-preserve-service’’andcreated
arulethattriggersatimeouterrorafter5secondsiftheservicedoes
Table4 not receive a response within that time frame. To activate this rule,
AccuracyofServiceAnomalywhenappliedtoTeaStoreandTrainTicketsystemswith we introduced a latency to the ‘‘ts-contact-service’’ using the same
differenterrorevaluationmetrics. wizard in Kiali. This latency causes delays in the traffic forwarding
| Targetsystems | Error | Precision | Recall F1-score |                              |         |       |                            |           |              |            |           |
| ------------- | ----- | --------- | --------------- | ---------------------------- | ------- | ----- | -------------------------- | --------- | ------------ | ---------- | --------- |
|               |       |           |                 | from ‘‘ts-preserve-service’’ |         |       | to ‘‘ts-contact-service’’, |           |              | which then | triggers  |
|               | MAPE  | 0.50      | 1.00 0.67       |                              |         |       |                            |           |              |            |           |
|               |       |           |                 | the injected                 | timeout | rule. | As a                       | result of | the injected | fault,     | the ‘‘ts- |
|               | MedAE | 0.54      | 1.00 0.70       |                              |         |       |                            |           |              |            |           |
preserve-service’’spanthrowsanerrorpropagatedtoitscaller,shown
|     | MAE | 0.60 | 1.00 0.75 |     |     |     |     |     |     |     |     |
| --- | --- | ---- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
TeaStore RMSE 0.78 0.93 0.85 in Fig. 14-(a), lines 1–2, 5–6, and 9. Moreover, in comparison to the
MSE 0.67 0.67 0.67 observed normal paths in the baseline CPG, ‘‘ts-preserve-service’’ has
max_error 0.89 0.53 0.66 beenrepetitivelycalledinlines5and9withoutanynestedchild.
MAPE 0.48 0.94 0.64 To detect the anomalous trace using our approach, the test trace,
MedAE 0.54 0.94 0.69 Fig.14-(a),collectedatthetimeofinjectingthetimeoutintothe‘‘ts-
TrainTicket MAE 0.59 0.91 0.72 preserve-service’’serviceistakenandcheckedagainstthebaselineCPG.
|     | RMSE | 0.79 | 0.94 0.86 |              |               |     |         |           |     |              |       |
| --- | ---- | ---- | --------- | ------------ | ------------- | --- | ------- | --------- | --- | ------------ | ----- |
|     |      |      |           | As a result, | the developer |     | will be | presented | by  | the test CPG | shown |
|     | MSE  | 0.53 | 0.88 0.68 |              |               |     |         |           |     |              |       |
inFig.15.Aswecanseethematchingalgorithmhashighlightedthe
|     | Max_error | 0.77 | 0.72 0.74 |                                  |       |           |         |         |          |                       |      |
| --- | --------- | ---- | --------- | -------------------------------- | ----- | --------- | ------- | ------- | -------- | --------------------- | ---- |
|     |           |      |           | unmatched                        | nodes | and edges | in red  | colour. | In the   | test CPG, there       | is a |
|     |           |      |           | ‘‘ts-preserve-service’’          |       | node      | with no | child   | that is  | because of repetitive |      |
|     |           |      |           | calls of ‘‘ts-preserve-service’’ |       |           | in      | lines 5 | and 9 of | the test trace        | (14- |
(a)).Parsingthecontextualinformationpropagatedthroughthespans
RQ1.HowaccurateServiceAnomalyisatdetectinganomalies? of the test trace shows that one of the recalled ‘‘ts-preserve-service’’
Finding: The results show that ServiceAnomaly can detect has missed contextual information. Our algorithm assigns an empty
anomalieswithanF1-scoreupto85%forTeaStoreand86% reference to this service, shown by a node with no name in Fig. 15.
for TrainTicket. The RMSE error evaluation metric yields a Thegraphmatchingstepfindsthisnodeanditsconnectionunmatched
more accurate model for both systems compared to other withthegeneralCPG.Inaddition,themetricmatchingstepidentifies
errorevaluationmetrics.Wealsoshowedthatthecombination linearandnon-linearmetricrelationshipsthatdeviatefromthenormal
of CPG and profiling metrics is an effective way to detect metric relationships. In this case, there are eight linear and three
differenttypesoffaults. non-linear metric relationships on seven edges that deviate from the
|     |     |     |     | metric relationships |     | on  | the edges | of the | baseline | CPG. These | metric |
| --- | --- | --- | --- | -------------------- | --- | --- | --------- | ------ | -------- | ---------- | ------ |
relationshipsarehighlightedandreportedtothedeveloperalongwith
|     |     |     |     | the metric | types,     | the expected | value    | range | for    | each metric,        | and the |
| --- | --- | --- | --- | ---------- | ---------- | ------------ | -------- | ----- | ------ | ------------------- | ------- |
|     |     |     |     | amount of  | deviation. | Fig.         | 15 shows | part  | of the | reported identified |         |
unmatchedmetricrelationships.
15

M.Panahandehetal. TheJournalofSystems&Software209(2024)111917
Fig.14. (a)Scenario1-AnanomalousTrainTickettracedetectedbyServiceAnomaly,(b)ApartialTrainticketgeneralCPG.
Fig.15. Scenario1-TestCPGresultforthetesttraceshowninFig.14-(a).(Forinterpretationofthereferencestocolourinthisfigurelegend,thereaderisreferredtotheweb
versionofthisarticle.)
5.2.2. Scenario2:TeaStoreanomalytrace be learnt from the collected test trace. Therefore, given the result of
Fig. 16-(a) shows one of the TeaStore traces that was flagged our approach, the developer is able to learn about the reason for the
as an anomaly by our approach. This trace includes three events detectedanomaly,‘‘teastore-recommender’’inthiscase.
each of which has two spans. First, ‘‘teastore-webui’’ calls ‘‘teastore-
persistence’’,thenitinvokesaserviceof‘‘teastore-image’’,andfinally,
‘‘teastore-webui’’calls‘‘teastore-auth’’tofulfiltheuserrequest.Fig.16-
(b)presentsapartialviewofthebaselineCPGforTeaStore.Thisgraph RQ2. How can the ServiceAnomaly approach be used to
includes the context propagation path from ‘‘teastore-webui’’ to each analyseanomalies?
oftheotherthreecalledspansthatwasobservedinthetraceshownin Finding:Ourapproachcanpinpointplacesofinterestwhere
Fig.16-(a).TheannotationsoneachedgeofFig.16-(b)brieflydescribe theanomaliesoccurusingthetestCPGandthebaselineCPG.
the linear (L) and non-linear (NL) relationships between the profiling We illustrate this feature through two examples of anomaly
metricsforeachedge,aswellasthespecificprofilingmetricsinvolved traces from TeaStore and TrainTicket. Additional studies in-
ineachrelationship. volving developers should be conducted to further assess the
To test our approach, we injected a latency into the ‘‘teastore- usefulnessofourapproachinrootcausesofanomalies.
recommender’’ service using Kiali as explained in Section 4.2. To
injectalatencyintothe‘‘teastore-recommender’’,weconfigureafault
injection rule where 80% of requests forwarding to the ‘‘teastore-
recommender’’ will be delayed 15 seconds. The test trace shown 5.3. RQ3.WhatarethelimitationsofServiceAnomalyindetectinganoma-
in Fig. 16-(a) was collected after injecting this fault into ‘‘teastore- lies?
recommender’’.
AswecanseeinFig.16-(c),theanomalywascausedbyaviolation To identify the limitations of our approach, ServiceAnomaly, in
tothemetricrelationships.Inthisscenario,thetestCPGisasubgraph this question, we discuss anomalies that were not detected by Ser-
of the baseline CPG. Therefore, graph matching did not identify the viceAnomaly and attempt to determine the causes. According to our
traceasananomaly.However,theinjectedfaultintothetracehasbeen observations,anomaliesthatchangetheCPGstructurecomparedtothe
detected by metric matching. In total, one linear and two non-linear baseline CPG were successfully detected at the graph matching step.
relationshipshavedeviatedfromthistrace.Usingthisinformationthe However,ifthetestCPGisanedge-inducingsub-graphofthebaseline
developercandomoreinvestigationsaboutthereasonforthedetected CPG,theanomalymightremainundetectedbythemetricmatching.
anomaly. In this scenario, the relationship between some metrics in Thefirstreasonforundetectedanomaliescanbefoundinthemag-
the test CPG did not match the expected relationships on all three nitudeofdeviationinthemetricsaffectedbytheanomaly.Inthiscase,
edgesconnectedtothe‘‘teastore-webui’’.Thedevelopercananalysethe usingdifferenterrorevaluationmetricscanaltertheoutcomeandcause
‘‘teastore-webui’’serviceanditsdependenciestouncoverthecausesof the detection of the anomaly. For example, Table 5 shows profiling
the anomaly. For example, comparing the test CPG (Fig. 16-(c)) with metric relationships for a test trace of TeaStore with an injected CPU
the baseline CPG (Fig. 16-(b)) shows that in addition to three called stressthatisnotdetectedbytheerrorevaluationmetricofmax-error
spansby‘‘teastore-webui’’inthetestCPG,the‘‘teastore-recommender’’ butisdetectedbyasmallererrorevaluationmetricsuchasRMSE.
and‘‘teastore-registry’’arealsoconnectedtothe‘‘teastore-webui’’and Table5describesthecharacterizedmetricrelationshipsforanedge
can be the cause of the detected anomaly. This information cannot between ‘‘teastore-webui’’ and ‘‘teastore-persistence’’. The first two
16

M.Panahandehetal.
TheJournalofSystems&Software209(2024)111917
|     |     |     |     | Fig.16. | Scenario2-AnanomalousTeaStoretracedetectedbyServiceAnomaly. |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | ------- | ----------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
Table5 experiments.However,insomecases,theremightbeserviceswithlow
Detailsof‘‘teastore-webui→teastore-persistence’’profilingmetricrelationships.
interactionswiththerestofthesystem.Therefore,fewprofilingmetric
| Metrics |     |     | Rel. Residual |     | Max-error | RMSE |     |     |     |     |     |     |     |
| ------- | --- | --- | ------------- | --- | --------- | ---- | --- | --- | --- | --- | --- | --- | --- |
valuescanbedetectedforthoseservicesthatitmakesitchallengingto
y=responsesize(Kb), L 10.9 25.6 4.7 identifyrelationshipsbetweenthosemetrics.Forexample,inTeaStore,
x=requestsize(kb) there are services of an Image provider and a Recommender calling
| y=latency(s), |     |     | NL 16.6∗10−3 |     | 30.3 | 5.62 |                 |         |      |      |        |        |                    |
| ------------- | --- | --- | ------------ | --- | ---- | ---- | --------------- | ------- | ---- | ---- | ------ | ------ | ------------------ |
|               |     |     |              |     |      |      | the Persistence | service | only | once | at the | system | execution startup. |
x=queuetime(s)
|                    |     |     |            |     |          |         | Therefore, | no relationship |     | can be | identified | for them | out of a few |
| ------------------ | --- | --- | ---------- | --- | -------- | ------- | ---------- | --------------- | --- | ------ | ---------- | -------- | ------------ |
| y=requestsize(kb), |     |     | NL 67.1∗10 |     | 46.9∗102 | 64.2∗10 |            |                 |     |        |            |          |              |
x=durationtime(s) telemetry data extracted from them. Moreover, there is a possibility
y=responsesize(kb), NL 20.4∗10 13.9∗102 18.9∗10 that there are enough collected profiling metrics for an edge but the
x=durationtime(s) collectedmetricsdonotshowanylinearornon-lineardependencyfor
anedgeoftheCPG.Therefore,collectedtesttracesincludingthatedge
|     |     |     |     |     |     |     | with no relationships |     | cannot | be  | cooperative | in detecting | anomalies |
| --- | --- | --- | --- | --- | --- | --- | --------------------- | --- | ------ | --- | ----------- | ------------ | --------- |
usingmatchingmetricrelationships.
columnsspecifytheinvolvedmetricsineachcharacterizedrelationship
| and the type | of relationship, |     | with L | denoting | linear and | NL denoting |     |     |     |     |     |     |     |
| ------------ | ---------------- | --- | ------ | -------- | ---------- | ----------- | --- | --- | --- | --- | --- | --- | --- |
non-linearrelationships.Thethirdcolumnindicatestheresidualvalue
| or absolute | difference | between | the | observed | value | of metric 𝑦 and |     |     |     |     |     |     |     |
| ----------- | ---------- | ------- | --- | -------- | ----- | --------------- | --- | --- | --- | --- | --- | --- | --- |
the computed value using the characterized relationships. The last RQ3.WhatarethelimitationsofServiceAnomalyindetecting
| two columns | show | the values | of different |     | error evaluation | metrics, | anomalies? |     |     |     |     |     |     |
| ----------- | ---- | ---------- | ------------ | --- | ---------------- | -------- | ---------- | --- | --- | --- | --- | --- | --- |
i.e.,error-maxandRMSE,foreachmetricrelationship.TheCPUstress Finding: ServiceAnomaly cannot detect anomalies when (I)
can be detected when the absolute difference (third column) exceeds The anomaly has not changed the metric values significantly
theexpectederrorvalues(lasttwocolumns).Acomparisonofthethird to be captured by the used error evaluation metric. (II) The
columnwiththeexpectedresidualsrevealsthattheinjectedCPUstress collectedtesttracedoesnotincludetheaffectedservicesand
can be detected using the smaller error evaluation metric (RMSE) by (III) There are edges in the general CPG with no profiling
onelinearandtwonon-linearviolatedrelationships. metricrelationshipandthetesttraceincludesspansassociated
Thesecondreasonforundetectedanomaliesisperforminganomaly withthoseedges.
| detection | on test | traces that | are unaffected |     | by the anomaly. | In this |     |     |     |     |     |     |     |
| --------- | ------- | ----------- | -------------- | --- | --------------- | ------- | --- | --- | --- | --- | --- | --- | --- |
case,althoughtheinjectedfaultscenariohaschangedthesystemper-
formance,theinjectedfaulthasnotbeenpropagatedintothecollected
6. Threatstovalidity
| spans of     | the test trace. | These      | traces   | remain | undetected | with different |     |     |     |     |     |     |     |
| ------------ | --------------- | ---------- | -------- | ------ | ---------- | -------------- | --- | --- | --- | --- | --- | --- | --- |
| experimented | error           | evaluation | metrics. | For    | instance,  | Fig. 17 shows  |     |     |     |     |     |     |     |
InternalThreats:
| some of | the performance |     | views of Kiali | for | ‘‘ts-food-service.default’’ |     |     |     |     |     |     |     |     |
| ------- | --------------- | --- | -------------- | --- | --------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
Thethreatstointernalvalidityconcernthefactorsthatmightinflu-
serviceinTrainTicketbeforeandafterinjectingaservicelatencyinto
|               |     |         |                  |     |      |                  | ence our | results. | To collect | distributed | traces | and profiling | metrics to |
| ------------- | --- | ------- | ---------------- | --- | ---- | ---------------- | -------- | -------- | ---------- | ----------- | ------ | ------------- | ---------- |
| this service. | The | service | latency scenario | has | been | injected at 6:26 |          |          |            |             |        |               |            |
characterizethenormalbehaviourofthesystem,werunbothsystems
| PM, shown | by a | border | in Fig. 17. | As the | monitoring | dashboards |     |     |     |     |     |     |     |
| --------- | ---- | ------ | ----------- | ------ | ---------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
show,theserviceperformancehaschangedafterinjectingthelatency. using the accompanying load tests. A different strategy may lead to
However, the collected test trace at the time of experiments does anothersetoftraces.However,wepurposelyresortedtoloadtests to
not reveal these changes. Fig. 17, shows the test trace that we col- observe as many execution paths as possible. An alternative solution
lected after injecting this fault scenario in the blue colour. This test wouldbetorunthesystemsusingexecutionscenarios,butthiswould
traceincludesaspan‘‘ts-travel-service.default’’thatcalls‘‘ts-ticketinfo- requireagoodsetofsystemfeatures,whichwedonothave.Another
service.default’’.Fig.17showshowthe‘‘ts-food-service.default’’service threattointernalvalidityconsistsofthecollectionofanomalytracesby
with the injected latency is connected to the collected spans. While injectingfaultsintothesystems.Tomakesurethatthecollectedreflect
the ‘‘ts-food-service.default’’ service has been affected by the injected the abnormal behaviour caused by the fault, we carefully observed
latency,thisanomalydidnotmanifestitselfinthetesttrace.Therefore, the system to see the impact of the fault on the execution as shown
thecollectedtesttracesweremissedbyourapproach. in Fig. 10. In addition, the profiling metrics values collected through
Wetrieddifferenttesttracesinthisgroupofundetectedanomalies the service mesh can be affected by the network delay. For instance,
and realized that anomalies are more likely to be detected when the a request duration time is defined as the time between establishing
|           |            |            |           |     |          |                 | a request | to its completion. |     | However, | network | delays | may increase |
| --------- | ---------- | ---------- | --------- | --- | -------- | --------------- | --------- | ------------------ | --- | -------- | ------- | ------ | ------------ |
| collected | test trace | is a trace | generated | by  | requests | to the affected |           |                    |     |          |         |        |              |
processingtime.Weignoredanalysingthepresentdelayinthenetwork
| service (i.e., | the service | with | the injected | fault) | or its | dependencies. |     |     |     |     |     |     |     |
| -------------- | ----------- | ---- | ------------ | ------ | ------ | ------------- | --- | --- | --- | --- | --- | --- | --- |
Moreover,generally,collectedtesttracescomprisingmorespanswith since it is applied to all the metrics. However, to make sure that
alongerrequestpropagationpatharemorelikelytoshowthechange the profiling metrics are not affected by a long delay, we monitored
causedbytheinjectedfault. ourtargetsystem’shealthduringtheexperimenttoidentifyandfilter
Thethirdgroupofundetectedanomalieshappenwhenthecollected any significant delays. Finally, there is a possible threats in the way
testtraceincludesspanswithnorelationships.Itisararecaseinour weimplementedServiceAnomaly.Animplementationerrormayhave
17

M.Panahandehetal.
TheJournalofSystems&Software209(2024)111917
Fig.17. Anexampleofaserviceperformanceaffectedbyinjectingnetworklatencyat6:26P.M.,ApartialCPGrepresentingthepropagationpathofinjectedfaulttotheservices.
(Forinterpretationofthereferencestocolourinthisfigurelegend,thereaderisreferredtothewebversionofthisarticle.)
| an impact | on the | results. | To mitigate |     | this threat, | we  | checked the | 8. Conclusion |     |     |     |     |     |     |     |
| --------- | ------ | -------- | ----------- | --- | ------------ | --- | ----------- | ------------- | --- | --- | --- | --- | --- | --- | --- |
implementationverycarefullyandtesteditonsmallexamples.Wealso
makethescriptsandthedatasetsavailableonlineforverifiability.5 Anomaly detection of microservices is a challenging task due to
ExternalThreats: the complexity of these systems, the volume of logs and traces, and
The threats to the external validity of this study lie in the gener- metrics collected during monitoring microservices. In this paper, we
alizability of the results. We evaluated our approach on two differ- proposed ServiceAnomaly, a method based on modelling the context
|                   |     |         |       |        |            |        |            | propagation | as a graph, | which | is annotated |     | with | the linear | and non- |
| ----------------- | --- | ------- | ----- | ------ | ---------- | ------ | ---------- | ----------- | ----------- | ----- | ------------ | --- | ---- | ---------- | -------- |
| ent microservices |     | using a | large | number | of traces. | To our | knowledge, |             |             |       |              |     |      |            |          |
linearrelationshipsofsixprofilingmetrics.Weevaluatedourapproach
theTrainTicketsystemisthelargestopen-sourcemicroservicesystem
againsttwocasestudiesofTeaStoreandTrainTicket.Theresultsshow
| available. | To generalize | our    | results,   | we    | should experiment |             | with more |          |                |            |                |         |          |         |             |
| ---------- | ------------- | ------ | ---------- | ----- | ----------------- | ----------- | --------- | -------- | -------------- | ---------- | -------------- | ------- | -------- | ------- | ----------- |
|            |               |        |            |       |                   |             |           | that our | approach       | identifies | traces         | with an | accuracy | of      | F1-score up |
| systems    | once they     | become | available. | There | is also           | an external | threat    |          |                |            |                |         |          |         |             |
|            |               |        |            |       |                   |             |           | to 86%.  | we also showed | how        | ServiceAnomaly |         | can      | be used | to reason   |
tovalidityrelatedtothetypesoffaultsthatwereinjectedtogenerate
|     |     |     |     |     |     |     |     | about anomalies, |     | a starting | point | for root | cause | analysis. | For future |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | ---------- | ----- | -------- | ----- | --------- | ---------- |
anomalytraces.Althoughwecovereddifferenttypesoffaults(service
|          |              |        |           |            |     |           |          | work, we | intend | to experiment | with | more | microservice |     | systems as |
| -------- | ------------ | ------ | --------- | ---------- | --- | --------- | -------- | -------- | ------ | ------------- | ---- | ---- | ------------ | --- | ---------- |
| latency, | stress host, | etc.), | we should | experiment |     | with more | types of |          |        |               |      |      |              |     |            |
faultscenariostoclaimgeneralizabilityoftheapproach. they become available. We also need to integrate ServiceAnomaly in
|     |     |     |     |     |     |     |     | an observability | tool | and | work with | developers |     | to examine | the use- |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | ---- | --- | --------- | ---------- | --- | ---------- | -------- |
ConstructionThreats:
fulnessofthismethodinpractice.Anotherimportantfuturedirection
| The threats  |            | to the construction |               | validity    | of our    | method      | mainly lie   |             |            |              |          |             |      |               |        |
| ------------ | ---------- | ------------------- | ------------- | ----------- | --------- | ----------- | ------------ | ----------- | ---------- | ------------ | -------- | ----------- | ---- | ------------- | ------ |
|              |            |                     |               |             |           |             |              | is to study | how the    | annotated    | CPG      | can be      | used | to understand | large  |
| in modelling | metric     | relationships.      |               | Calculating | mutual    | information | is           |             |            |              |          |             |      |               |        |
|              |            |                     |               |             |           |             |              | distributed | traces.    | A particular | line     | of research |      | is to examine | how    |
| dependent    | on entropy | and                 | probabilities |             | which     | makes it    | difficult to |             |            |              |          |             |      |               |        |
|              |            |                     |               |             |           |             |              | abstraction | techniques | such         | as those | developed   | for  | traditional   | traces |
| be measured  | for        | empirical           | data          | (Smith,     | 2015). We | used the    | proposed     |             |            |              |          |             |      |               |        |
(e.g.Pirzadehetal.,2013)canimprovetheanalysisoftheannotated
| binning | approach | for calculating |     | entropy | (Beirlant | et al., | 1997) in |     |     |     |     |     |     |     |     |
| ------- | -------- | --------------- | --- | ------- | --------- | ------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
CPGtosupportprogramcomprehension,animportantenablerforroot
whichtheobserveddataisdividedintokbinswith𝑛
𝑖 samplesineach causeanalysisoffaults.Moreover,weshouldinvestigatetechniquesto
binand𝑛 𝑖 representsthenumberofoccurrencesofeachmetricvalue. improvethecausalityandexplainabilityofourapproach.Theideaisto
| Then,entropyismeasuredusingthefollowingformulaformetric𝑚: |     |     |     |     |     |     | 𝑖   |         |                  |     |           |         |            |     |              |
| --------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ------- | ---------------- | --- | --------- | ------- | ---------- | --- | ------------ |
|                                                           |     |     |     |     |     |     |     | improve | ServiceAnomaly’s |     | decisions | through | a feedback |     | loop process |
|                                                           |     | 𝑛   | 𝑛   |     |     |     |     |         |                  |     |           |         |            |     |              |
𝑒𝑛𝑡𝑟𝑜𝑝𝑦(𝑚)=−𝛴𝑘 𝑖 log 𝑖 (10) that considers the analyst feedback. Finally, we need to study the
|     | 𝑖   | 𝑖=1𝑛 | 𝑛   |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
scalabilityofourapproachwhenworkingwithlargesystems.Forthe
(Annotation E1) the adapted VF2 algorithm employed for graph current work, we collected traces for 3 to 7 days depending on the
matchingisexpectednottosurpasspolynomialtimecomplexity,con- systemtohaveagoodcoverageoftheexecutionpathsforeachsystem.
sidering the specific characteristics of CPGs and the assumption that For larger systems, we may need to collect more traces, which can
test CPGs are expected to have identical parts with the general CPG. impactscalability.
| However,    | this  | assumption | may         | encounter | challenges | under       | certain  |     |     |     |     |     |     |     |     |
| ----------- | ----- | ---------- | ----------- | --------- | ---------- | ----------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
| conditions: | I) if | the test   | CPG closely | resembles |            | the general | CPG, but |     |     |     |     |     |     |     |     |
CRediTauthorshipcontributionstatement
| is not identical. |           | i.e., when | the test    | CPG | is very       | similar to | the general |             |                |      |                    |         |              |            |            |
| ----------------- | --------- | ---------- | ----------- | --- | ------------- | ---------- | ----------- | ----------- | -------------- | ---- | ------------------ | ------- | ------------ | ---------- | ---------- |
| CPG in both       | structure | and        | attributes, | but | not identical | in         | many parts  |             |                |      |                    |         |              |            |            |
|                   |           |            |             |     |               |            |             | Mahsa       | Panahandeh:    |      | Conceptualization, |         | Methodology, |            | Software,  |
| or II) the        | test CPG  | can be     | embedded    | in  | the general   | CPG        | in multiple |             |                |      |                    |         |              |            |            |
|                   |           |            |             |     |               |            |             | Validation, | Investigation, | Data | curation,          | Writing |              | – original | draft, Vi- |
ways.Whilethealgorithmdemonstratesfeasibilityforourtestedtarget
|     |     |     |     |     |     |     |     | sualization. | Abdelwahab |     | Hamou-Lhadj: |     | Conceptualization, |     | Method- |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ---------- | --- | ------------ | --- | ------------------ | --- | ------- |
system,thesescenariosnecessitatefurtheranalysistorefinethegraph-
|          |             |             |          |           |          |          |              | ology, Writing | – original      | draft, | Writing  | –   | review   | & editing,     | Supervi- |
| -------- | ----------- | ----------- | -------- | --------- | -------- | -------- | ------------ | -------------- | --------------- | ------ | -------- | --- | -------- | -------------- | -------- |
| matching | task.       | A potential | solution | to        | mitigate | these    | complexities |                |                 |        |          |     |          |                |          |
|          |             |             |          |           |          |          |              | sion, Project  | administration. |        | Mohammad |     | Hamdaqa: | Conceptualiza- |          |
| involves | structuring | anomalies,  |          | i.e. null | nodes    | or novel | patterns, as |                |                 |        |          |     |          |                |          |
tion,Methodology,Writing–review&editing.JamesMiller:Writing
distinctpatterns.Bydoingso,thegraph-matchingalgorithmcanspecif-
–review&editing,Supervision,Projectadministration.
icallysearchforthesepatterns,facilitatingtargetedpruningbasedon
predefinedanomalycharacteristics.
Declarationofcompetinginterest
7. Reproductionpackage
|         |      |              |       |         |        |             |          | The authors    | declare     | that | they          | have no | known | competing | finan-      |
| ------- | ---- | ------------ | ----- | ------- | ------ | ----------- | -------- | -------------- | ----------- | ---- | ------------- | ------- | ----- | --------- | ----------- |
|         |      |              |       |         |        |             |          | cial interests | or personal |      | relationships | that    | could | have      | appeared to |
| All the | data | used in this | paper | as well | as the | scripts can | be found |                |             |      |               |         |       |           |             |
influencetheworkreportedinthispaper.
| on Github | repository | using | the following |     | link: https://github.com/M- |     |     |     |     |     |     |     |     |     |     |
| --------- | ---------- | ----- | ------------- | --- | --------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
panahandeh/ServiceAnomaly.
Dataavailability
5 https://github.com/M-panahandeh/ServiceAnomaly DataandscriptsareavailableonGithubmentionedinthepaper.
18

M.Panahandehetal. TheJournalofSystems&Software209(2024)111917
References Hamou-Lhadj,Abdelwahab,Lethbridge,TimothyC.,2005.Measuringvariousproperties
ofexecutiontracestohelpbuildbettertraceanalysistools.In:Proceedings10th
Anon., 2022a. Apache JMeter. Available at https://jmeter.apache.org/. (Accessed 4 InternationalConferenceonEngineeringofComplexComputerSystems.IEEE,pp.
August2022). 559–568.
He, Zilong, Chen, Pengfei, Li, Xiaoyun, Wang, Yongfeng, Yu, Guangba, Chen, Cailin,
Anon.,2022b.istio-simplifyobservability,trafficmanagement,security,andpolicywith
Li, Xinrui, Zheng, Zibin, 2020. A spatiotemporal deep learning approach for
theleadingservicemesh.Availableathttps://istio.io/.(Accessed4February2022).
unsupervisedanomalydetectionincloudsystems.IEEETrans.NeuralNetw.Learn.
Anon.,2022c.Jaeger:Opensource,end-to-enddistributedtracing.Availableathttps:
Syst..
//www.jaegertracing.io/.(Accessed4February2022).
Hou,Chuanjia,Jia,Tong,Wu,Yifan,Li,Ying,Han,Jing,2021.Diagnosingperformance
Anon., 2022d. Kubernetes. Available at https://kubernetes.io/. (Accessed 9 August
issuesinmicroserviceswithheterogeneousdatasource.In:2021IEEEIntlConfon
2022).
Parallel & Distributed Processing with Applications, Big Data & Cloud Comput-
Anon., 2022e. Prometheus: From metrics to insight power your metrics and alerting
ing, Sustainable Computing & Communications, Social Computing & Networking
withtheleadingopen-sourcemonitoringsolution.Availableathttps://prometheus.
(ISPA/BDCloud/SocialCom/SustainCom).IEEE,pp.493–500.
io/.(Accessed4February2022).
Hui,Yu,Wenzhu,Sun,Xiuzhi,Zhou,Guotao,Zhu,Wenting,Hu,2016.Heuristicsample
Ayers, Andrew, Schooler, Richard, Metcalf, Chris, Agarwal, Anant, Rhee, Junghwan,
reduction based support vector regression method. In: 2016 IEEE International
Witchel, Emmett, 2005. Traceback: First fault diagnosis by reconstruction of
ConferenceonMechatronicsandAutomation.IEEE,pp.2065–2069.
distributed control flow. In: Proceedings of the 2005 ACM SIGPLAN Conference
Islam, Md. S., Khreich, Wael, Hamou-Lhadj, Abdelwahab, 2018. Anomaly detection
onProgrammingLanguageDesignandImplementation.pp.201–212.
techniquesbasedonkappa-prunedensembles.IEEETrans.Reliab.67(1),212–229.
Balalaie, Armin, Heydarnoori, Abbas, Jamshidi, Pooyan, 2015. Migrating to cloud- Jacob, Stephen, Qiao, Yuansong, Ye, Yuhang, Lee, Brian, 2022. Anomalous dis-
native architectures using microservices: An experience report. In: European tributedtraffic:Detectingcybersecurityattacksamongstmicroservicesusinggraph
ConferenceonService-OrientedandCloudComputing.Springer,pp.201–215. convolutionalnetworks.Comput.Secur.118,102728.
Balalaie,Armin,Heydarnoori,Abbas,Jamshidi,Pooyan,2016.Microservicesarchitec- Jiang, Miao, Munawar, Mohammad A, Reidemeister, Thomas, Ward, Paul AS,
tureenablesdevops:Migrationtoacloud-nativearchitecture.IEEESoftw.33(3), 2011. Efficient fault detection and diagnosis in complex software systems with
42–52. information-theoretic monitoring. IEEE Trans. Dependable Secure Comput. 8 (4),
Bao,Liang,Li,Qian,Lu,Peiyao,Lu,Jie,Ruan,Tongxiao,Zhang,Ke,2018.Execution 510–522.
anomaly detection in large-scale systems through console log analysis. J. Syst. Keogh,Eamonn,Chu,Selina,Hart,David,Pazzani,Michael,2001.Anonlinealgorithm
Softw.143,172–186. forsegmentingtimeseries.In:Proceedings2001IEEEInternationalConferenceon
Beirlant,Jan,Dudewicz,EdwardJ.,Györfi,László,VanderMeulen,EdwardC.,etal., DataMining.IEEE,pp.289–296.
1997. Nonparametric entropy estimation: An overview. Int. J. Math. Stat. Sci. 6 Khreich, Wael, Khosravifar, Babak, Hamou-Lhadj, Abdelwahab, Talhi, Chamseddine,
(1),17–39. 2017. An anomaly detection system based on variable N-gram features and
Beschastnikh,Ivan,Liu,Perry,Xing,Albert,Wang,Patty,Brun,Yuriy,Ernst,MichaelD., one-classSVM.Inf.Softw.Technol.91,186–197.
2020.Visualizingdistributedsystemexecutions.ACMTrans.Softw.Eng.Methodol. vonKistowski,Jóakim,Eismann,Simon,Schmitt,Norbert,Bauer,André,Grohmann,Jo-
29(2),1–38. hannes,Kounev,Samuel,2018.TeaStore:Amicro-servicereferenceapplicationfor
Boehmke, Brad, Greenwell, Brandon, 2019. Hands-on Machine Learning with R. benchmarking,modelingandresourcemanagementresearch.In:Proceedingsofthe
ChapmanandHall/CRC. 26thIEEEInternationalSymposiumontheModelling,Analysis,andSimulationof
Bogatinovski, Jasmin, Nedelkoski, Sasho, 2020. Multi-source anomaly detection in ComputerandTelecommunicationSystems.MASCOTS’18.
distributeditsystems.In:InternationalConferenceonService-OrientedComputing. Kohyarnejadfard, Iman, Shakeri, Mahsa, Aloise, Daniel, 2019. System performance
Springer,pp.201–213. anomaly detection using tracing data analysis. In: Proceedings of the 2019 5th
Bogatinovski, Jasmin, Nedelkoski, Sasho, Cardoso, Jorge, Kao, Odej, 2020. Self- InternationalConferenceonComputerandTechnologyApplications.pp.169–173.
supervised anomaly detection from distributed traces. In: 2020 IEEE/ACM 13th Kratzke, Nane, Quint, Peter-Christian, 2017. Understanding cloud-native applications
InternationalConferenceonUtilityandCloudComputing,UCC.IEEE,pp.342–347. after10yearsofcloudcomputing-asystematicmappingstudy.J.Syst.Softw.126,
Brandón,Álvaro,Solé,Marc,Huélamo,Alberto,Solans,David,Pérez,MaríaS,Muntés- 1–16.
Mulero, Victor, 2020. Graph-based root cause analysis for service-oriented and scikit learn, 2023. Scikit-learn: Machine learning in Python. https://scikit-learn.org/
microservicearchitectures.J.Syst.Softw.159,110432. stable/index.html.(AccessedAugust2023).
Chen, Hao, Wei, Kegang, Li, An, Wang, Tao, Zhang, Wenbo, 2021. Trace-based Lee, Sungyoung, Park, Young-Tack, d’Auriol, Brian J., et al., 2012. A novel feature
intelligentfaultdiagnosisformicroserviceswithdeeplearning.In:2021IEEE45th selection method based on normalized mutual information. Appl. Intell. 37 (1),
Annual Computers, Software, and Applications Conference, COMPSAC. IEEE, pp. 100–120.
884–893. Lee,Cheryl,Yang,Tianyi,Chen,Zhuangbin,Su,Yuxin,Lyu,MichaelR.,2023.Eadro:
Cordella, Luigi P., Foggia, Pasquale, Sansone, Carlo, Vento, Mario, 1998. Subgraph Anend-to-endtroubleshootingframeworkformicroservicesonmulti-sourcedata.
transformationsfortheinexactmatchingofattributedrelationalgraphs.In:Graph In:Proceedingsofthe45thInternationalConferenceonSoftwareEngineering.ICSE
BasedRepresentationsinPatternRecognition.Springer,pp.43–52. ’23,IEEEPress,pp.1750–1762.
Li, Richard, Du, Min, Wang, Zheng, Chang, Hyunseok, Mukherjee, Sarit, Eide, Eric,
Cordella,LuigiP.,Foggia,Pasquale,Sansone,Carlo,Vento,Mario,2004.A(sub)graph
2022a.LongTale:Towardautomaticperformanceanomalyexplanationinmicroser-
isomorphismalgorithmformatchinglargegraphs.IEEETrans.PatternAnal.Mach.
vices. In: Proceedings of the 2022 ACM/SPEC on International Conference on
Intell.26(10),1367–1372.
PerformanceEngineering.pp.5–16.
Danon, Leon, Diaz-Guilera, Albert, Duch, Jordi, Arenas, Alex, 2005. Comparing
Li,Bowen,Peng,Xin,Xiang,Qilin,Wang,Hanzhang,Xie,Tao,Sun,Jun,Liu,Xuanzhe,
communitystructureidentification.J.Stat.Mech.TheoryExp.2005(09),P09008.
2022b.Enjoyyourobservability:Anindustrialsurveyofmicroservicetracingand
Darlington,RichardB.,Hayes,AndrewF.,2017.RegressionAnalysisandLinearModels:
analysis.Empir.Softw.Eng.27(1),1–28.
Concepts,Applications,andImplementation.Guilford,NewYork,NY.
Li,Min,Tang,Dingyong,Wen,Zepeng,Cheng,Yunchang,2021.Microserviceanomaly
Dashuber,Veronika,Philippsen,Michael,2022.Tracevisualizationwithinthesoftware
detection based on tracing data using semi-supervised learning. In: 2021 4th
city metaphor: Controlled experiments on program comprehension. Inf. Softw.
InternationalConferenceonArtificialIntelligenceandBigData,ICAIBD.IEEE,pp.
Technol.150,106989.
38–44.
DeMyttenaere,Arnaud,Golden,Boris,LeGrand,Bénédicte,Rossi,Fabrice,2016.Mean Lin,Jinjin,Chen,Pengfei,Zheng,Zibin,2018.Microscope:Pinpointperformanceissues
absolutepercentageerrorforregressionmodels.Neurocomputing192,38–48. withcausalgraphsinmicro-serviceenvironments.In:Pahl,Claus,Vukovic,Maja,
Du,Min,Li,Feifei,Zheng,Guineng,Srikumar,Vivek,2017.Deeplog:Anomalydetection Yin, Jianwei, Yu, Qi (Eds.), Service-Oriented Computing. Springer International
and diagnosis from system logs through deep learning. In: Proceedings of the Publishing,Cham,pp.3–20.
2017 ACM SIGSAC Conference on Computer and Communications Security. pp. Liu,Dewei,He,Chuan,Peng,Xin,Lin,Fan,Zhang,Chenxi,Gong,Shengfang,Li,Ziang,
1285–1298. Ou,Jiayu,Wu,Zheshun,2021.Microhecl:High-efficientrootcauselocalizationin
Flajolet, Philippe, Sipala, Paolo, Steyaert, Jean-Marc, 1990. Analytic variations on large-scalemicroservicesystems.In:2021IEEE/ACM43rdInternationalConference
the common subexpression problem. In: International Colloquium on Automata, onSoftwareEngineering:SoftwareEngineeringinPractice(ICSE-SEIP).IEEE,pp.
Languages,andProgramming.Springer,pp.220–234. 338–347.
Freedman, David A., 2009. Statistical Models: Theory and Practice. Cambridge Liu,Ping,Xu,Haowen,Ouyang,Qianyu,Jiao,Rui,Chen,Zhekang,Zhang,Shenglin,
UniversityPress. Yang, Jiahai, Mo, Linlin, Zeng, Jice, Xue, Wenman, et al., 2020. Unsupervised
Fu, Qiang, Lou, Jian-Guang, Wang, Yi, Li, Jiang, 2009. Execution anomaly detection detection of microservice trace anomalies through service-level deep bayesian
in distributed systems through unstructured log analysis. In: 2009 Ninth IEEE networks. In: 2020 IEEE 31st International Symposium on Software Reliability
InternationalConferenceonDataMining.IEEE,pp.149–158. Engineering,ISSRE.IEEE,pp.48–58.
Gzyl,H.,Mayoral,S.,Gomes-Gonçalves,E.,2023.LossDataAnalysis:TheMaximum Luks, Eugene M., 1982. Isomorphism of graphs of bounded valence can be tested in
EntropyApproach.DeGruyterSTEM,DeGruyter. polynomialtime.J.Comput.Syst.Sci.25(1),42–65.
Hamou-Lhadj,Abdelwahab,Lethbridge,TimothyC.,2002.Compressiontechniquesto Ma, Meng, Xu, Jingmin, Wang, Yuan, Chen, Pengfei, Zhang, Zonghua, Wang, Ping,
simplifytheanalysisoflargeexecutiontraces.In:Proceedings10thInternational 2020.Automap:Diagnoseyourmicroservice-basedwebapplicationsautomatically.
WorkshoponProgramComprehension.IEEE,pp.159–168. In:ProceedingsoftheWebConference2020.pp.246–258.
19

M.Panahandehetal.
TheJournalofSystems&Software209(2024)111917
Meng,Lun,Ji,Feng,Sun,Yao,Wang,Tao,2021.Detectinganomaliesinmicroservices Yu, Guangba, Huang, Zicheng, Chen, Pengfei, 2021. TraceRank: Abnormal service
withexecutiontracecomparison.FutureGener.Comput.Syst.116,291–301. localizationwithdis-aggregatedend-to-endtracingdataincloudnativesystems.J.
Messaoud, Ines Ben, Feki, Jamel, Zurfluh, Gilles, 2012. A first step for building a Softw.Evol.Processe2413.
documentwarehouse:UnificationofXMLdocuments.In:2012SixthInternational Zhang, Qixun, Jia, Tong, Wu, Zhonghai, Wu, Qingxin, Jia, Lichun, Li, Donglei,
ConferenceonResearchChallengesinInformationScience,RCIS.IEEE,pp.1–6. Tao,Yuqing,Xiao,Yutong,2022a.Faultlocalizationformicroserviceapplications
Mohan, Neeraj, Singla, Ruchi, Kaushal, Priyanka, Kadry, Seifedine, 2021. Artificial withsystemlogsandmonitoringmetrics.In:20227thInternationalConferenceon
Intelligence,MachineLearning,andDataScienceTechnologies:futureImpactand CloudComputingandBigDataAnalytics,ICCCBDA.IEEE,pp.149–154.
Well-BeingforSociety5.0.CRCPress. Zhang, Chenxi, Peng, Xin, Sha, Chaofeng, Zhang, Ke, Fu, Zhenqing, Wu, Xiya,
Nandi, Animesh, Mandal, Atri, Atreja, Shubham, Dasgupta, Gargi B., Bhat- Lin,Qingwei,Zhang,Dongmei,2022b.DeepTraLog:Trace-logcombinedmicroser-
tacharya, Subhrajit, 2016. Anomaly detection using program control flow graph vice anomaly detection through graph-based deep learning. In: Conference on
miningfromexecutionlogs.In:Proceedingsofthe22ndACMSIGKDDInternational SoftwareEngineering,ICSE.
ConferenceonKnowledgeDiscoveryandDataMining.pp.215–224. Zhao, Chenyu, Ma, Minghua, Zhong, Zhenyu, Zhang, Shenglin, Tan, Zhiyuan,
Nedelkoski, Sasho, Cardoso, Jorge, Kao, Odej, 2019a. Anomaly detection and clas- Xiong, Xiao, Yu, LuLu, Feng, Jiayi, Sun, Yongqian, Zhang, Yuzhi, Pei, Dan,
sification using distributed tracing and deep learning. In: 2019 19th IEEE/ACM Lin, Qingwei, Zhang, Dongmei, 2023. Robust multimodal failure detection for
International Symposium on Cluster, Cloud and Grid Computing, CCGRID. IEEE, microservice systems. In: Proceedings of the 29th ACM SIGKDD Conference on
pp.241–250. Knowledge Discovery and Data Mining. KDD ’23, Association for Computing
Nedelkoski,Sasho,Cardoso,Jorge,Kao,Odej,2019b.Anomalydetectionfromsystem Machinery,pp.5639–5649.
tracing data using multimodal deep learning. In: 2019 IEEE 12th International Zhou, Xiang, Peng, Xin, Xie, Tao, Sun, Jun, Ji, Chao, Li, Wenhai, Ding, Dan, 2018.
ConferenceonCloudComputing,CLOUD.IEEE,pp.179–186. Faultanalysisanddebuggingofmicroservicesystems:Industrialsurvey,benchmark
Niemi, Edvin, Wallin, Richard, 2021. Visualization of microservices: Mapping system,andempiricalstudy.IEEETrans.Softw.Eng.47(2),243–260.
dependenciesinadistributedarchitecture. Zuo,Yuan,Wu,Yulei,Min,Geyong,Huang,Chengqiang,Pei,Ke,2020.Anintelligent
OpenTracing Contributors, 2023. OpenTracing specification. https://opentracing.io/ anomaly detection scheme for micro-services architectures with temporal and
specification/.(Accessed23February2023). spatialdataanalysis.IEEETrans.Cogn.Commun.Netw.6(2),548–561.
| Pahl, Claus, | 2015. Containerization |     | and | the paas | cloud. IEEE | Cloud Comput. | 2 (3), |     |     |     |     |     |
| ------------ | ---------------------- | --- | --- | -------- | ----------- | ------------- | ------ | --- | --- | --- | --- | --- |
24–31.
Parker,A.,Spoonhower,D.,Mace,J.,Sigelman,B.,Isaacs,R.,2020.DistributedTrac-
|                  |                |     |            |     |           |                |          | Mahsa Panahandeh | received | her B.Sc. | and M.Sc. | in  |
| ---------------- | -------------- | --- | ---------- | --- | --------- | -------------- | -------- | ---------------- | -------- | --------- | --------- | --- |
| ing in Practice: | Instrumenting, |     | Analyzing, | and | Debugging | Microservices. | O’Reilly |                  |          |           |           |     |
SoftwareEngineeringfromUniversityofIsfahan,Iran.Cur-
Media,Incorporated.
Pirzadeh, Heidar, Shanian, Sara, Hamou-Lhadj, Abdelwahab, Alawneh, Luay, Shar- rently,sheisaPh.D.candidateinsoftwareengineeringat
ifee,Arya,2013.Stratifiedsamplingofexecutiontraces:Executionphasesserving theUniversityofAlberta,Edmonton,Canada.Herresearch
interestincludesanalysisandevaluatingofsoftwaresystems
asstrata.Sci.Comput.Program.78(8),1099–1118.
Ruff, Lukas, Vandermeulen, Robert, Goernitz, Nico, Deecke, Lucas, such as microservices and serverless application, software
Siddiqui, Shoaib Ahmed, Binder, Alexander, Müller, Emmanuel, Kloft, Marius, tracingandlogging,DevOps,AIOps,andstudyingsoftware
architecturesandpatterns.
| 2018. Deep | one-class | classification. |     | In: International | Conference |     | on Machine |     |     |     |     |     |
| ---------- | --------- | --------------- | --- | ----------------- | ---------- | --- | ---------- | --- | --- | --- | --- | --- |
Learning.PMLR,pp.4393–4402.
| Samir, Areeg, | El Ioini, | Nabil,  | Fronza,   | Ilenia, Barzegar, | Hamid        | R., Le,     | Van Thanh, |     |     |     |     |     |
| ------------- | --------- | ------- | --------- | ----------------- | ------------ | ----------- | ---------- | --- | --- | --- | --- | --- |
| Pahl, Claus,  | 2020.     | Anomaly | detection | and               | analysis for | reliability | management |     |     |     |     |     |
clusteredcontainerarchitectures.Int.J.Adv.Syst.Meas.12(3&4),247–264. Abdelwahab Hamou-Lhadj is a Professor in the Depart-
Samir,Areeg,Pahl,Claus,2019.DLA:Detectingandlocalizinganomaliesincontainer- ment of ECE at the Gina Cody School of Engineering and
ized microservice architectures using markov models. In: 2019 7th International ComputerScience,ConcordiaUniversity,Montreal,Canada.
ConferenceonFutureInternetofThingsandCloud,FiCloud.IEEE,pp.205–213. His research interests are in AI for Software Systems and
Smith,Reginald,2015.Amutualinformationapproachtocalculatingnonlinearity.Stat ITOperations,SoftwareEngineering,SystemObservability,
4(1),291–303. andModel-drivenEngineering.HereceivedhisPh.D.from
Soldani,Jacopo,Tamburri,DamianAndrew,VanDenHeuvel,Willem-Jan,2018.The the University of Ottawa, Canada. He is a senior member
painsandgainsofmicroservices:Asystematicgreyliteraturereview.J.Syst.Softw. ofIEEE,along-lastingmemberofACM,andaprofessional
146,215–232. engineerwithOIQ.Heisalsoafrequentcontributortothe
Song, Lin, Langfelder, Peter, Horvath, Steve, 2012. Comparison of co-expression Object Management Group (OMG) certification programs,
measures: Mutual information, correlation, and model based indices. BMC OCUP2andOCEB2.
Bioinformatics13(1),1–21.
ValienteFeruglio,GabrielAlejandro,2000.SimpleandEfficientTreePatternMatching
(Ph.D.thesis).UniversitatPolitècnicadeCatalunya. Mohammad Hamdaqa is an Assistant Professor at the
|                   |       |     |         |               |             |             |     | Department | of Computer Engineering | and | Software | Engi- |
| ----------------- | ----- | --- | ------- | ------------- | ----------- | ----------- | --- | ---------- | ----------------------- | --- | -------- | ----- |
| Vapnik, Vladimir, | 1998. | The | support | vector method | of function | estimation. | In: |            |                         |     |          |       |
NonlinearModeling.Springer,pp.55–85. neeringatPolytechniqueMontréal(Canada),whereheleads
Vapnik, Vladimir, Golowich, Steven, Smola, Alex, 1996. Support vector method for theSoftwareandEmergingTechnologiesLab.Heisalsoan
|     |     |     |     |     |     |     |     | Adjunct Professor | at the Department | of  | Computer | Science |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | ----------------- | --- | -------- | ------- |
functionapproximation,regressionestimationandsignalprocessing.Adv.Neural
|     |     |     |     |     |     |     |     | at Reykjavik | University (Iceland). | Hamdaqa | is interested |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --------------------- | ------- | ------------- | --- |
Inf.Process.Syst.9.
Wang, Tao, Zhang, Wenbo, Xu, Jiwei, Gu, Zeyu, 2020. Workflow-aware automatic insoftwareengineeringapproaches,methods,andpractices
faultdiagnosisformicroservice-basedapplicationswithstatistics.IEEETrans.Netw. thatcanbetailoredtotamethecomplexitiesofarchitect-
|     |     |     |     |     |     |     |     | ing, building, | and deploying decentralized |     | and distributed |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --------------------------- | --- | --------------- | --- |
Serv.Manag.17(4),2350–2363.
Wang, Tao, Zhang, Wenbo, Ye, Chunyang, Wei, Jun, Zhong, Hua, Huang, Tao, applications.
| 2015. FD4C: | Automatic | fault | diagnosis | framework | for web | applications | in cloud |     |     |     |     |     |
| ----------- | --------- | ----- | --------- | --------- | ------- | ------------ | -------- | --- | --- | --- | --- | --- |
computing.IEEETrans.Syst.ManCybern.A46(1),61–75.
|                   |        |               |     |         |                |      |             | Dr. James | Miller, P.Eng(Alberta) | – jimm@ualberta.ca |     | –   |
| ----------------- | ------ | ------------- | --- | ------- | -------------- | ---- | ----------- | --------- | ---------------------- | ------------------ | --- | --- |
| Wu, Li, Tordsson, | Johan, | Bogatinovski, |     | Jasmin, | Elmroth, Erik, | Kao, | Odej, 2021. |           |                        |                    |     |     |
MicroDiag:Fine-grainedperformancediagnosisformicroservicesystems.In:2021 has been a full professor with the Dept. Electrical and
|     |     |     |     |     |     |     |     | Computer Engineering | at The | University | of Alberta | since |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------- | ------ | ---------- | ---------- | ----- |
IEEE/ACMInternationalWorkshoponCloudIntelligence,CloudIntelligence.IEEE,
|     |     |     |     |     |     |     |     | 2000. Previously, | he was a professor |     | at the University |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | ------------------ | --- | ----------------- | --- |
pp.31–36.
Wu, Li, Tordsson, Johan, Elmroth, Erik, Kao, Odej, 2020. Microrca: Root cause of Strathclyde (U.K.) and a principal research scientist at
|     |     |     |     |     |     |     |     | the National | Electronics Research | Initiative | (U.K.). | He has |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | -------------------- | ---------- | ------- | ------ |
localizationofperformanceissuesinmicroservices.In:NOMS2020-2020IEEE/IFIP
beenanactiveresearcherformorethanthirtyyearsacross
NetworkOperationsandManagementSymposium.IEEE,pp.1–9.
|                |      |                  |     |             |                      |     |         | a wide range | of topics, ranging | from | Computer | Vision, |
| -------------- | ---- | ---------------- | --- | ----------- | -------------------- | --- | ------- | ------------ | ------------------ | ---- | -------- | ------- |
| Xu, Peng, Gao, | Xue, | Zhang, Zhongbao, |     | 2022. Graph | neural network-based |     | anomaly |              |                    |      |          |         |
detectionfortraceofmicroservices.AvailableatSSRN4111928. Pattern Recognition, Embedded System Design, Software
Engineering,WebEngineeringandProactiveAnalytics.He
| Yerushalmy, | Jacob, 1947. | Statistical | problems | in  | assessing methods | of  | medical diag- |               |               |          |                  |     |
| ----------- | ------------ | ----------- | -------- | --- | ----------------- | --- | ------------- | ------------- | ------------- | -------- | ---------------- | --- |
|             |              |             |          |     |                   |     |               | has published | more than 100 | articles | in peer-reviewed |     |
nosis,withspecialreferencetoX-raytechniques.PublicHealthRep.(1896–1970)
| 1432–1449. |     |     |     |     |     |     |     | journalsincludingmanyIEEEandACMvenues. |     |     |     |     |
| ---------- | --- | --- | --- | --- | --- | --- | --- | -------------------------------------- | --- | --- | --- | --- |
20