Received14September2024,accepted7October2024,dateofpublication16October2024,dateofcurrentversion18December2024.
DigitalObjectIdentifier10.1109/ACCESS.2024.3481676
LMGD: Log-Metric Combined Microservice
Anomaly Detection Through Graph-Based
Deep Learning
XULIU1,YUEWENLIU 2,MIAOMIAOWEI2,ANDPENGXU 2
1ChinaAcademyofIndustrialInternet,Beijing100083,China
2StateKeyLaboratoryofNetworkingandSwitchingTechnology,BeijingUniversityofPostsandTelecommunications,Beijing100876,China
Correspondingauthor:YuewenLiu(liuyw@bupt.edu.cn)
ABSTRACT Microservicearchitectureisahigh-cohesionandlow-couplingsoftwarearchitecture.Itscore
ideaistosplittheapplicationintoasetofmicroserviceswithasinglefunctionandindependentdeployment.
Duetotheircomplexityandlargescale,microservicesystemsaretypicallyfragileandfailuresareinevitable.
Therefore,thereisanurgentneedforfastandaccurateanomalydetectioncapabilities.However,theexisting
microserviceanomalydetectionmethodsdonotpayattentiontothemulti-sourcedataofthemicroservice
system and thus have low accuracy. To address this limitation, we propose a Log-Metric Combined
MicroserviceAnomalyDetectionapproachthroughGraph-basedDeepLearning(termedasLMGD).First,
weproposeatime-awareLSTMpredictionneuralnetworktoimprovetheaccuracyofservicedependency
mining.Secondly,basedontheservicedependencygraph,weproposeananomalydetectionmethodbased
on log-metric fusion, which can more accurately describe the running status of microservices, thereby
improvingtheaccuracyofanomalydetection.Theexperimentaloutcomesdemonstratethatcomparedwith
otherstate-of-the-artmethods,ourmethodimprovesrecallandF1-scoreby2.63%and1.05%.
INDEXTERMS Anomalydetection,log,metrics,distributedsystems,GCN,GAT.
I. INTRODUCTION monitoring and anomaly detection. A typical microservices
Withtherapidadvancementofinternettechnology,software system comprises thousands of services distributed across
systems have become increasingly complex, and traditional a large number of servers, interacting frequently with one
monolithic architectures are increasingly revealing their another.Thishighcomplexityandscalerendermicroservices
limitations in meeting modern software demands such as systems highly vulnerable, where a failure in any single
frequent deployment cycles, rapid feature iteration, and service can trigger cascading failures throughout the entire
flexible horizontalscalability. Inthis context,microservices system [3]. Additionally, due to the tight coupling between
architecture has emerged as a novel design paradigm aimed services, issues can rapidly propagate, affecting the overall
at enhancing system flexibility and maintainability by stability of the system.Given these considerations, effective
decomposingapplicationsintoaseriesofsmall,independent monitoring and anomaly detection within microservices
services.Theseservicesarebuiltaroundbusinesscapabilities systemsbecomescritical.
andcanbedeployed,scaled,andupgradedindependently[1]. To date, many studies have been conducted on anomaly
Compared to traditional monolithic applications, microser- detection in microservice systems. The studies [4], [5], [6],
vicesofferfasterdeliveryspeedsandhigherscalability[2]. [7]minetheservicedependencygraphtoestablishabaseline
However, while microservices bring numerous benefits, modelbylearningtheservicelogsofmicroservicesrunning
they also introduce new challenges, particularly in system without faults, and then use the baseline model to detect
whether the new logs deviate from the baseline model;
The associate editor coordinating the review of this manuscript and the studies [8], [9], [10] monitor KPIs (Key Performance
approvingitforpublicationwasBangL.H.Nguyen . Indicators) on its services by installing agents and then
2024TheAuthors.ThisworkislicensedunderaCreativeCommonsAttribution-NonCommercial-NoDerivatives4.0License.
186510 Formoreinformation,seehttps://creativecommons.org/licenses/by-nc-nd/4.0/ VOLUME12,2024

X.Liuetal.:LMGD:Log-MetricCombinedMicroserviceAnomalyDetectionThroughGraph-BasedDeepLearning
processes such KPIs to detect anomalies.However, existing 3) Joint Rule-Based Anomaly Detection: To tackle the
methodshavethefollowinglimitation.Observabledataina third challenge, we propose an anomaly detection
microserviceenvironmentincludeslogsandmetrics.Related method based on joint rules, incorporating multiple
studies only rely on a single observable data, which cannot breakpoints in the online detection phase to assess
fullydiscoverwhetherthesystemisrunningabnormallyand system abnormalities. We categorize anomalies into
leadtolowanomalydetectionaccuracy. threetypes:redundantanomalies,sequenceanomalies,
Therefore,weproposeaLog-MetricCombinedMicroser- and metric anomalies. The detection results are then
vice Anomaly Detection through Graph-based Deep Learn- stored as data labels in memory, a strategy that
ing (LMGD). However, the following three challenges still enhances both the recall and accuracy of anomaly
remain: detection.
1) Incorporating Time Intervals in Service Depen- Insummary,ourcontributionsarelistedasfollows:
dencyMining:Microservicelogsexhibitvaryingtime 1) To the best of our knowledge, this is the first attempt
intervals, yet existing methodologies focus solely on to study the fusion of logs and metrics for anomaly
the sequence of log entries, neglecting the critical detectioninmicroservicescenarios.
aspectoftimeintervalsbetweenlogs.Properconsider- 2) We propose a time-aware service dependency graph
ationofthesetimeintervalscanenhancetheprecision generationmethodtosolvetheproblemofunevenlog
ofidentifyingdependenciesamongmicroservices. data intervals. We propose a method to integrate logs
2) Integrating Metrics and Logs for Anomaly Detec- and metrics data, Which describe the dependencies
tion: Effective anomaly detection necessitates the between services and the running status of services
joint analysis of multi-dimensional data, ensuring withtheaidofgraphneuralnetworks.Weproposean
that no vital information is overlooked. However, the anomalydetectionmethodbasedonjointrules.
integrationofmetricsandlogsiscomplicatedbytheir 3) Wevalidateourmethodusingareal-worlddatasetand
inherent differences, such as distinct data structures compare it with existing anomaly detection methods
andvaryingcollectionfrequencies.Consequently,itis that rely on single data types, demonstrating the
essential to develop a method that seamlessly merges superiority of our approach. The results indicate that
these disparate data types into a unified analytical ourmethodimprovesrecallandF1-scoreby2.63%and
framework. 1.05%,respectively,overstate-of-the-artmethods.
3) ComprehensiveDetectionofMultipleAnomaliesin Therestofthispaperisorganizedasfollows.InSectionII,
Microservice Systems: The inherent complexity of wesummarizerelatedworkaboutanomalydetectionmethods
microservice architectures gives rise to various types formicroservicesandgraphneuralnetworks.InSectionIII,
of anomalies, including call and metric anomalies. weintroduceourproposedalgorithmLMGD.InSectionIV,
Current detection methods often focus on a single weconductextensiveexperimentstoillustratethesuperiority
type of anomaly, presenting a significant challenge in ofLMGD.InSectionV,wemaketheconclusion.
developing a detection method capable of identifying
multipleanomaliesconcurrently. II. RELATEDWORK
In order to meet the above challenges, we have proposed A. CALLCHAIN-BASEDANOMALYDETECTION
thefollowingsolutions: In the context of cloud-native data processing platforms,
1) Time-AwareServiceDependencyGraphMining:To call chain-based anomaly detection can be categorized into
addressthefirstchallenge,weintroduceamethodfor two main types based on the source of call chain data: log-
mining service dependencies that accounts for time basedcallchainconstructionandmonitoringtool-basedcall
intervals, thereby improving accuracy. Initially, tem- chain collection. In log-based call chain construction, the
plateminingisappliedtologdatatoextracttime-series WFG-based method [11] detects call chain anomalies by
log sequences. These sequences are then fed into a learningaWorkflowGraph(WFG)offline.TheCFG-based
time-awareLongShort-TermMemory(LSTM)neural method[5]detectsanomaliesbyleveraginganoffline-learned
networktopredictpotentialsuccessorsforeachnode, Control Flow Graph (CFG). The CPD-based method [12]
ultimatelygeneratingtheservicedependencygraph. performs anomaly detection by comparing the similarities
2) Log-Metric Fusion for Enhanced Microservice between the control flow graphs of multiple call chains.
State Learning: In response to the second challenge, DeepLog[13],ontheotherhand,utilizesanLSTMmodelto
weproposeamethodforthefusionoflogandmetric detectcallpathanomalieswithinthecallchain.Thismethod
data to gain a more comprehensive understanding trains independent LSTM models for each node in the call
of microservice states. Specifically, our approach chain to detect response time anomalies. Compared to log-
integrates the service dependency graph with node based methods, monitoring tool-based call chain collection
metricinformationandutilizesagraphneuralnetwork offersbetterreal-timeperformance,enablingtimelydetection
to jointly learn the operational status of the system of platform performance issues. The AEVB [14] method
underhistoricalnormalconditions,includingbothnode proposes an unsupervised deep Bayesian network model to
dependenciesandstates. detect response time anomalies in call chains. Seer [15]
VOLUME12,2024 186511

X.Liuetal.:LMGD:Log-MetricCombinedMicroserviceAnomalyDetectionThroughGraph-BasedDeepLearning
uses a CNN to perform dimensionality reduction on data correspondingtolog,andthestructuredlogcanbedefined
i
and then employs LSTM to learn temporal and spatial by a triple (k, pod, t ), where k is the log template, pod is
s
patternsincallchaindata.Thismethodeffectivelyanalyzes thelabelofthemicroservicenodetowhichthelogbelongs,
and predicts QoS, providing crucial insights and support and t is the timestamp when the log is printed.The output
s
for system performance improvement. The Multimodal ofsubsequentpredictionstagesisvectorV 0 .Thesubsequent
LSTM [14] model simultaneously learns and detects call prediction result of real-time detection is V. The input of
i
path anomalies and response time anomalies in call chains. thegraphattentionnetworkisasetofnodefeaturesh={h ⃗ ,
1
|     |     |     |     |     |     | ⃗   | ⃗ ⃗ |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
TraceAnomaly [16] and CRISP [17] represent call chains h 2 ,...,h N ,h i ∈R}.Nisthenumberofnodes,Fisthenumber
as Service Tracking Vectors (STV) and use Variational of features of a node. We categorize the log data into two
Autoencoders(VAE)[18]todetectbothcallpathanomalies types:normalandabnormal.Amongtheabnormalsamples,
andresponsetimeanomalies. wefurtherclassifythemintothreelevelsofseveritybasedon
thedegreeofabnormality:mild,moderate,andsevere.
B. LOG-BASEDANOMALYDETECTION
| In log-based | anomaly | detection |     | research, | unsupervised |     |     |     |     |     |     |     |
| ------------ | ------- | --------- | --- | --------- | ------------ | --- | --- | --- | --- | --- | --- | --- |
learning methods are commonly employed. These methods IV. LMGDOVERVIEW
model the logs recorded during the stable operation of the Figure 1 provides a comprehensive overview of our pro-
platform using unsupervised learning algorithms and then posed method, LMGD. The input to LMGD consists of
use this model to detect whether newly recorded log events microservice transaction logs and the associated metrics
matchthemodeltodetermineiftheplatformisexperiencing of each service node, while the output is a determination
|            |           |     |        |          |             | of whether | the analyzed | data | batch | is  | abnormal. | The |
| ---------- | --------- | --- | ------ | -------- | ----------- | ---------- | ------------ | ---- | ----- | --- | --------- | --- |
| anomalies. | The OASIS | [5] | method | analyzes | logs during |            |              |      |       |     |           |     |
stableoperationtoconstructacontrolflowgraphthatmodels approach is divided into two primary stages: the offline
theplatform’sbehaviorundernormalconditions,identifying stage, which focuses on constructing service dependency
whicheventsshouldberecordedbywhichserviceandinwhat graphs fromlogs and training abaseline model thatreflects
order.Jiaetal.[19],[20]analyzelogsduringstableoperation the system’s normal operational state, and the online stage,
|     |     |     |     |     |     | which monitors | deviations | between |     | real-time | data | and the |
| --- | --- | --- | --- | --- | --- | -------------- | ---------- | ------- | --- | --------- | ---- | ------- |
tomineatime-weightedcontrolflowgraphforeachservice
| tomodelitsinternalprocesses. |     |     |     |     |     | establishedbaselinemodel. |                |     |               |     |                 |     |
| ---------------------------- | --- | --- | --- | --- | --- | ------------------------- | -------------- | --- | ------------- | --- | --------------- | --- |
|                              |     |     |     |     |     | In the                    | offline phase, | two | key processes |     | are undertaken. |     |
C. KPI-BASEDANOMALYDETECTION First, microservice transaction logs are analyzed to extract
In KPI-based anomaly detection research, abnormal situa- information necessary for constructing an inter-service
|     |     |     |     |     |     | dependency | graph, which | elucidates |     | the interactions |     | among |
| --- | --- | --- | --- | --- | --- | ---------- | ------------ | ---------- | --- | ---------------- | --- | ----- |
tionsareidentifiedbymonitoringkeyperformanceindicators
(KPIs) of nodes in the platform, such as CPU usage, components within the microservice architecture. Second,
memoryusage,andresponsetime.Commonmethodsinclude using the extracted log data, a baseline model is trained to
bothunsupervisedandsupervisedlearning.Inunsupervised represent the normal behavior of the system. This model
learning,theunsupervisedlearningalgorithmprocessesKPIs serves as the foundation for anomaly detection during the
detected during the platform’s normal operation to form a subsequentonlinephase.
model,whichisthenusedtodetectifnewKPIsareabnormal. Theonlinephaseisconcernedwithreal-timesurveillance
Gulenkoetal.[10]establisheddifferentmodelsfordifferent ofmicroservicebehavior.Bycomparingthecurrentdataflow
services within the platform, modeling KPIs as vectors and againstthebaselinemodelestablishedintheofflinephase,the
clusteringthesevectorsusingclusteringalgorithms.Mariani systemidentifiespotentialanomalies.Significantdeviations
et al. [21] paired each KPI with the corresponding service from the baseline are flagged as potential anomalies,
and trained a model for the entire platform. By establishing facilitating timely detection and resolution of issues within
KPI models and causal graphs, KPIs that fall outside the the microservice architecture. This real-time monitoring
capabilityenhancesthestabilityandreliabilityofthesystem.
| acceptable | range of | the model | are | identified | as anomalies. |     |     |     |     |     |     |     |
| ---------- | -------- | --------- | --- | ---------- | ------------- | --- | --- | --- | --- | --- | --- | --- |
Insupervisedlearning,ADS[22]andPreMiSE[23]injected LMGD comprises three core components: the generation
specific faults into specific services during the training of the service dependency graph, data fusion based on
phase and labeled the KPIs to distinguish between KPIs graphneuralnetworks,andanomalydetection.SectionIV-A
collectedundernormalconditionsandthosecollectedduring details the generation of the service dependency graph,
|     |     |     |     |     |     | where log | files are processed |     | into template |     | sequences | and |
| --- | --- | --- | --- | --- | --- | --------- | ------------------- | --- | ------------- | --- | --------- | --- |
faults.
|     |     |     |     |     |     | a time-aware | deep learning |     | model | is employed | to  | extract |
| --- | --- | --- | --- | --- | --- | ------------ | ------------- | --- | ----- | ----------- | --- | ------- |
III. PROBLEMDEFINITION servicedependencies.SectionIV-Bdiscussesthedatafusion
In this section, we will introduce necessary notations and process, in which the microservice system is modeled as a
formallyformulateourproblem.Wedefinetherawdatasetas graph, and a two-layer graph neural network is utilized to
Rdata.Amongthem,theoriginallogsetisL={log ,log ,..., train a baseline model representing normal system states.
|     |     |     |     |     | 1 2 |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
log n },afterparsingbythelogtemplateparser,astructuredlog Finally, Section IV-C addresses anomaly detection, where
setcanbeobtained,expressedasD={d ,d ,...,d }andthe joint conditions are designed to systematically identify
|     |     |     |     | 1   | 2 n |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
logtemplatesetisK={k
|        |     | 1 ,k | 2 ,...,k m | }.d i isthestructuredlog |     | anomalieswithinthesystem. |     |     |     |     |               |     |
| ------ | --- | ---- | ---------- | ------------------------ | --- | ------------------------- | --- | --- | --- | --- | ------------- | --- |
| 186512 |     |      |            |                          |     |                           |     |     |     |     | VOLUME12,2024 |     |

X.Liuetal.:LMGD:Log-MetricCombinedMicroserviceAnomalyDetectionThroughGraph-BasedDeepLearning
|     | FIGURE1. Approachoverview. |     |     |     |     |     |       |         |        |         |          |           |          |
| --- | -------------------------- | --- | --- | --- | --- | --- | ----- | ------- | ------ | ------- | -------- | --------- | -------- |
|     |                            |     |     |     |     |     | Next, | we will | obtain | the log | template | sequence, | which is |
readyforsubsequentservicedependencygraphmining.Logs
|     |     |     |     |     |     |     | with time  | tags,        | node tags, | and      | template  | tags | are obtained |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ------------ | ---------- | -------- | --------- | ---- | ------------ |
|     |     |     |     |     |     |     | through    | log parsing, | and        | the logs | collected | by   | each node    |
|     |     |     |     |     |     |     | are sorted | by time      | to obtain  | a log    | sequence. | This | sequence     |
containsthepossiblecallsofeachnode.Forexample,nodec
|     |     |     |     |     |     |     | always      | follows | After   | node b,   | it can | be judged | that the      |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ------- | ------- | --------- | ------ | --------- | ------------- |
|     |     |     |     |     |     |     | possibility | of b    | calling | c is very | high,  | that is,  | the successor |
nodeofbnodeisverylikelytobecnode.
Sinceeachnodeofthesystemexecutestaskswithmultiple
threads,thegeneratedlogsequenceischaoticandinterlaced,
|     |     |     |     |     |     |     | so a neural  | network    | with   | a certain | depth      | can           | better detect |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ---------- | ------ | --------- | ---------- | ------------- | ------------- |
|     |     |     |     |     |     |     | the frequent | patterns   | among  | them.     | Input      | this sequence | into          |
|     |     |     |     |     |     |     | the LSTM     | artificial | neural | network   | prediction |               | model with    |
FIGURE2. Logparsingalgorithmprocess.
|     |     |     |     |     |     |     | time perception |                | ability,          | learn the | frequent    | pattern     | of node |
| --- | --- | --- | --- | --- | --- | --- | --------------- | -------------- | ----------------- | --------- | ----------- | ----------- | ------- |
|     |     |     |     |     |     |     | calls, and      | mine           | the statistically |           | significant | successor   | nodes   |
|     |     |     |     |     |     |     | of each         | node template. |                   | Here, the | LSTM        | multi-input | single- |
A. GENERATIONOFSERVICEDEPENDENCYGRAPH
First,wepreprocesstherawlogdataandparsethelogtext outputpredictionmodelisusedtopredictpossiblesuccessor
nodesforeachnode.
| into structured | data. The     | template | extraction |     | is performed  |     |            |     |          |      |       |      |            |
| --------------- | ------------- | -------- | ---------- | --- | ------------- | --- | ---------- | --- | -------- | ---- | ----- | ---- | ---------- |
|                 |               |          |            |     |               |     | Meanwhile, | the | standard | LSTM | model | only | implicitly |
| on the logs,    | and different | types    | of logs    | are | distinguished |     |            |     |          |      |       |      |            |
dealswithuniformtimeintervalsintheinputsequence,sothe
| by clustering. | The log       | parsing | steps are | shown | in  | Figure 2. |           |             |     |        |            |           |     |
| -------------- | ------------- | ------- | --------- | ----- | --- | --------- | --------- | ----------- | --- | ------ | ---------- | --------- | --- |
|                |               |         |           |       |     |           | LSTM unit | is equipped |     | with a | time-aware | mechanism | to  |
| Drain is       | an online log | parsing | method    | based | on  | a fixed   |           |             |     |        |            |           |     |
depthtree.Whenanewrawlogmessageissent,Drainwill payattentiontotheimpactofdifferenttimeintervalsonthe
|     |     |     |     |     |     |     | prediction | results. | It is | well understood |     | that sequences | with |
| --- | --- | --- | --- | --- | --- | --- | ---------- | -------- | ----- | --------------- | --- | -------------- | ---- |
preprocessthelogdatausingsimplifiedregularexpressions
shortlogintervalsaremorelikelytocontainactualcallsthan
basedonknowledgeofthedomaintowhichthelogbelongs,
sequenceswithlongerintervals,thelattercell’scontribution
| so as to | better match | the specific | design | rules | encoded | in  |     |     |     |     |     |     |     |
| -------- | ------------ | ------------ | ------ | ----- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
willdecreaseastheintervalincreases.
| the internal | nodes of | the tree. | If the | log can | be  | matched |     |     |     |     |     |     |     |
| ------------ | -------- | --------- | ------ | ------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
Add(cid:49)tinformationtotheinputgateandforgetgatetopay
| to an appropriate | log | group, | the log | will be | grouped | with |     |     |     |     |     |     |     |
| ----------------- | --- | ------ | ------- | ------- | ------- | ---- | --- | --- | --- | --- | --- | --- | --- |
attentiontotheimpactofdifferenttimeintervals:
| the previously | collected     | log  | group. If  | there | is no | matching |     |     |     |                |     |     |        |
| -------------- | ------------- | ---- | ---------- | ----- | ----- | -------- | --- | --- | --- | -------------- | --- | --- | ------ |
| result, a      | new log group | will | be created | based | on    | the log  |     |     |     |                |     |     |        |
|                |               |      |            |       |       |          |     |     | ′   | =e −(cid:49)tf | .   |     |        |
| information.   |               |      |            |       |       |          |     |     | f t |                | t   |     | (1)    |
| VOLUME12,2024  |               |      |            |       |       |          |     |     |     |                |     |     | 186513 |

X.Liuetal.:LMGD:Log-MetricCombinedMicroserviceAnomalyDetectionThroughGraph-BasedDeepLearning
i ′ =(1−e −(cid:49)t)i . (2) a two-dimensional matrix, and the rank of the matrix is the
t t
number of nodes n. Among them, ‘‘0.35’’ means that the
where(cid:49)tisthetimeinterval,representingthetimedifference
probabilitythatnodeAcallsnodeBis35%.
between two log events. It measures the impact of the time
interval on the prediction results; f t is the forget gate in the  0.01 0.35 ... 0.02 
LSTMunit.Theforgetgatecontrolstheextenttowhichpast 0.12 0.00 ... 0.01
information is forgotten. In the original formula, it is the  ... ... ... ...  (3)
 
output of the forget gate. In the new formula, it is adjusted 0.00 0.00 ... 0.05
by (cid:49)t to generate f′; i is the input gate in the LSTM unit.
t t
Theinputgatecontrolstheextenttowhichnewinformation Amongthem,thecallfromnodetonodewhoseprobability
is added to the LSTM unit state. In the original formula, is lower than a threshold is regarded as an error, so as to
i t is the output of the input gate. In the new formula, it is prunethedataandreducethecostofsubsequentgraphneural
adjusted by (cid:49)t to generate i′ t ; f t ′ is the adjusted forget gate network information transmission and anomaly detection.
output. f t ′ = e−(cid:49)tf t indicates that the forget gate output Inthegeneratedgraph,eachpointrepresentsaservicenode,
is influenced by the time interval (cid:49)t. As (cid:49)t increases, f t ′ an edge represents the existence of calls between the two
decreases,meaningthedegreeofforgettingpastinformation services,andtheweightoftheedgerepresentsthedegreeof
ishigher;i′
t
istheadjustedinputgateoutput.i′
t
=(1−e−(cid:49)t)i
t dependencebetweenservices.
indicatesthattheinputgateoutputisinfluencedbythetime
interval(cid:49)t.As(cid:49)tincreases,i′ increases,meaningthedegree
t B. DATAFUSIONBASEDONGRAPHNEURALNETWORK
ofincorporatingnewinformationishigher.
Based on the service dependency graph obtained in the
The prediction model consists of three layers: the input
previousstage,weintegrateitwithmetricstojointlylearnthe
layer, the neural network hidden layer, and the output
running status of microservices. The microservice running
layer. The input layer encodes all logs into one-hot vectors.
statusinformationcontainedintheloginformationhasbeen
The input layer receives the log template sliding window
fullyminedintheservicedependencygraphgenerationstage.
w=<x t−h , ..., x t−2 , x t−1 > of the training data set in the In addition, the metrics data also contains rich information.
training phase, and receives the log template sliding of the
Therefore, we propose a two-layer graph neural network to
detectiondatasetinthedetectionphasewindoww.wherex
fusetheservicedependencygraphandmetricstocharacterize
representsthelogtemplateintheslidingwindow.hrepresents
microservicesystems.
the length of the sliding window, the number of past log
First, we propose a graph structure to describe the
templates considered in each prediction.The output layer is
microservice. It is known that the observable metrics
responsible for converting the hidden state set H t−h , ..., dimensionsofallservicenodesarethesame,andassuming
H t−2 , H t−1 output by the neural network layer into the that the contribution of the same metrics on different nodes
subsequent prediction probability vector V of the final
w is the same, at this time, the microservice scenario can be
outputlogtemplate.whereHrepresentsthehiddenstateinthe
composed of a large graph of service nodes and each node
neuralnetwork.ThehiddenstateH capturestheinformation
t and the metrics is composed of tree subgraphs. In the large
from the input sequence up to time t. It is an internal state
graph, nodes represent microservices, and edges between
usedbytheLSTMtostoreinformationaboutpreviousinputs
points represent dependencies between microservices, that
inthesequence.
is, invocation situations. In the subgraph, there are only
In the detection phase, when the model predicts a large
central nodes and edge nodes. The central node represents
difference between the log template and the actual log
microservices, and the edge nodes are service-level observ-
template, exceeding the set threshold, it is determined that
ablemetrics.Therearenoedgesbetweenmetrics.Thereare
theloghasanabnormalcall.
onlydependenciesbetweencentralnodesandedgenodesin
thesubgraph,andtheweightofedgenodes,thecontribution
degree,isdifferent,andthestructureisshowninFigure4.
Then,weapplygraphneuralnetworkstographstructures
to capture the features of a node by aggregating and
transforming the features of its neighbors, thus taking
into account the influence of related nodes on nodes. For
subgraphs,theconnectivitybetweenknownnodesiscertain,
but the metrics contribution weight is unknown, the graph
attentionnetwork(GraphAttentionNetwork,GAT)canlearn
the attention weight, and the operation of the self-attention
FIGURE3. Time-awareLSTMalgorithm. layer can be in all edges are performed in parallel, and the
calculationofoutputfeaturesofallnodesisalsoperformedin
Finally, we obtain the possible successors and sepa- parallel.Theattentionmechanismcanbesharedandapplied
rate possibilities of each node V . Its data structure is to all edges in the graph. Therefore, the graph attention
0
186514 VOLUME12,2024

X.Liuetal.:LMGD:Log-MetricCombinedMicroserviceAnomalyDetectionThroughGraph-BasedDeepLearning
neural network, and finally, the results are probabilized
through the Softmax activation function to obtain the
probabilitydistributionofthepredictedresults:
Z =softmax(A ˆ ReLU(A ˆ XW(0)W(1))). (7)
where Z is the final output result, which is the probability
distribution of the prediction results after applying the
ˆ
softmax activation function.A is the normalized adjacency
matrix of the graph, containing the information about the
edges between nodes. X is the initial node feature matrix,
where each row corresponds to the feature vector of a
node.W(0)andW(1)istheweightmatricesusedinthetraining
processforlineartransformationofnodefeatures.
Aftertheentirenetwork,thefeatureofeachnodeofGCN
has changed from X to Z. During the whole process, the
FIGURE4. Servicedependencygraphandsubgraph.
adjacency matrix A is shared and unchanged.The layer-to-
layerpropagationmethodisasfollows,andHisthefeature
˜
networkisselectedtolearntheweightinformationofmetrics of node,D is the degree matrix of the normalized adjacency
˜
nodesandservicenodes. matrixA:
However,theinformationofeachedgeofthelargegraph
Hl+1 =σ(D ˜−1/2A ˜ D ˜−1/2H(l)W(l)). (8)
between services is certain, and the edges are weighted and
directed,sothereisnoneedtopayattentiontothelearning
It is worth noting that this graph neural network infor-
of the edges. After the GAT training of the sub-graph is
mation transfermethod isnot only applicableto theservice
completed, the characteristic data of the service nodes can
dependency graph generated based on the log in this paper,
be obtained. At this time, it is necessary to focus on how
but also applicable to the call chain generated by the trace
mucheachnodeisaffectedbyneighbornodes,thatis,nodes
collectedbylinktracingandothermethods.
withcallingrelationships.Here,agraphconvolutionalneural
network (Graph Convolutional Network, GCN) is used to
C. ANOMALYDETECTION
processneighborhoodinformation.Eachconvolutionallayer
The core concept behind anomaly detection is to compare
canprocessaTheinformationtransferofmulti-orderneigh-
real-time logs and metrics against log templates, service
borhoods can be realized by stacking several convolutional
dependencygraphs,andgraphneuralnetworksderivedfrom
layers.Microservicenodesarenotonlyaffectedbyneighbor
normalsystembehaviorduringthetrainingphase.Bydoing
nodes, but the nodes involved in the entire call chain may
so, the system can diagnose potential anomalies. During
affect the operation of the service. Therefore, the design of
training, various techniques are employed to model the
thenumberofconvolutionallayerswillbediscussedlater.
system’snormalbaselinestate,allowingfortheestablishment
The input of the graph attention network is a set of node
features h={h ⃗ , h ⃗ , ..., h ⃗ , h ⃗ ∈RF}, N is the number of of multiple checkpoints to detect anomalies, a process
1 2 N i
referredtoasthejointrule-basedanomalydetectionmethod.
nodes, F is the number of features of a node, here is 1.
This method is typically divided into three components:
Apply the weight matrix W∈R, which is a shared linear
(1)determiningwhetheralogcanbeparsedandmapped;ifit
transformation, to each node, perform self-attention on the
cannot,itisclassifiedasaredundancyanomaly;(2)assessing
node,andcalculatetheattentioncoefficient:
whether there is an anomaly within the log sequence;
e ij =α(Wh ⃗ i ,Wh ⃗ j ). (4) if one is detected, it is considered a sequence anomaly;
and (3) evaluating the deviation between the graph neural
Here,e representstheimportanceofnodejtonodei.Then
ij
network,theservicedependencygraph,andthemetricsfrom
calculatetheattentioncoefficientbetweennodes,theformula
the training phase; significant deviations indicate a metrics
αisasfollows:
anomaly.
exp(LeakyRelu(a⃗T[Wh ⃗ ][Wh ⃗ ]))
α = i j . (5) First, we verify whether the real-time log data can be
ij P exp(LeakyRelu(a⃗T[Wh ⃗ ][Wh ⃗ ])) mapped to a predefined log template. If the log cannot be
k∈Ni i k
classified into any existing log group, it is considered an
Afterobtainingthenormalizedattentioncoefficient,calculate
theupdatedoutputfeatures,andσ istheactivationfunction anomalouslog.Thisisintuitive,asthesystemmaygenerate
h ⃗′ =σ( X α Wh ⃗ ). (6) abnormal logs under fault conditions. The logs used during
i ij j the parsing stage are all collected under normal system
jϵNi
operation. Consequently, any logs that cannot be clustered
Forsubsequentlarge-scaletraining,theoutputfeaturesofthe withexistingloggroups—obtainedthroughclusteringduring
previous layer are used as input to the graph convolutional normaloperation—areflaggedasabnormal.
VOLUME12,2024 186515

X.Liuetal.:LMGD:Log-MetricCombinedMicroserviceAnomalyDetectionThroughGraph-BasedDeepLearning
Next, we examine whether the log sequence exhibits any topredictthenextloggingeventinthesequenceandidentify
anomalies. Successfully mapping a log to its corresponding possibleanomalies.
template does not guarantee that the system is functioning 4) LogAnomaly [26] is a log anomaly detection method
normally,asanomaliescanmanifestinvariousforms.Even that treats the log as a sequence of events and considers
if a service failure does not produce an error log, it may the count of distinct log events as an additional feature.
still disrupt multiple services, impacting their invocation ItemploysLSTMmodelstolearnsequentialandquantitative
sequences.Atthisstage,attentionisfocusedonthereal-time patterns. Similar to DeepLog, it detects anomalies by
log template sequence, which is then compared with the predictingthenextlogevent.
time-awaresuccessorpredictiondatatodeterminewhetheran SinceTraceAnomalyonlyconsiderstracedata,whenusing
exceptionhasoccurred.Thetime-awaresuccessorprediction them, only provide trace to them. DeepLog only considers
stageprovidesthepotentialsuccessornodesforeachservice, log data and treats it as a sequence of events. Therefore,
andanydeviationfromthisexpectedsequenceisflaggedas combine all events of different services in a trace into a
anomalous. sequence of events sorted by timestamp, and provide the
Finally,weevaluatethemetricsdataforanyirregularities. sequence of events for all traces as input to these two
Anomalies may also be reflected in changes to system methods. TraceAnomaly and DeepLog provide open source
metrics, such as a sudden spike in resource usage. The code implementations, use them directly. DeepTraLog uses
real-time metrics data is fed into the graph neural network, tracedataandlogdata.
| which is    | followed    | by  | a fully    | connected   | layer               | to determine |       |                                               |     |     |     |     |     |
| ----------- | ----------- | --- | ---------- | ----------- | ------------------- | ------------ | ----- | --------------------------------------------- | --- | --- | --- | --- | --- |
| whether     | the metrics |     | indicate   | an anomaly. |                     | By applying  |       |                                               |     |     |     |     |     |
|             |             |     |            |             |                     |              |       | TABLE1. Methodeffectivenessevaluationresults. |     |     |     |     |     |
| this joint  | rule-based  |     | anomaly    | detection   | method,             |              | which |                                               |     |     |     |     |     |
| encompasses | redundancy  |     | anomalies, |             | sequence            | anomalies,   |       |                                               |     |     |     |     |     |
| and metrics | anomalies,  |     | the        | system      | can comprehensively |              |       |                                               |     |     |     |     |     |
determinewhetheritisfunctioningabnormally.
V. EXPERIMENTS
A. DATASET
Thispaperadoptsthemulti-sourcedistributedsystemdataset
proposedbyliterature[24]forartificialintelligenceanalysis.
| Thisdatasetcaptureshigh-qualitymulti-sourcedataconsist- |     |         |             |     |           |         |     | C. METRICS     |            |          |            |                |     |
| ------------------------------------------------------- | --- | ------- | ----------- | --- | --------- | ------- | --- | -------------- | ---------- | -------- | ---------- | -------------- | --- |
|                                                         |     |         |             |     |           |         |     | Use precision, | recall and | F1 score | to measure | the effective- |     |
| ing of distributed                                      |     | traces, | application |     | logs, and | metrics | for |                |            |          |            |                |     |
distributed systems. Remove the call information from the nessofanomalydetection.
trace data and use it. The actual call information is used to Accuracy rate: the percentage of real anomalies in all
detectedanomalies,whichcanbeunderstoodastheprecision
| verify the | accuracy | of  | the results | in  | the anomaly | detection |     |     |     |     |     |     |     |
| ---------- | -------- | --- | ----------- | --- | ----------- | --------- | --- | --- | --- | --- | --- | --- | --- |
rate,expressedas:
phase.
| Thedatasetcomesfrom5differentnodesofthedistributed |     |     |     |     |     |     |     |     |            | TP  |     |     |     |
| -------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- |
|                                                    |     |     |     |     |     |     |     |     | Precision= |     | .   |     | (9) |
system,including829,562logdata,eachnodehasanaverage
TP+FP
of239,127metrics,andatotalof1,195,637metrics.Among
|     |     |     |     |     |     |     |     | Recall | rate: the percentage | of detected |     | abnormalities | in  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | -------------------- | ----------- | --- | ------------- | --- |
them,theinjectedfaultdataaccountsforabout6.8%,andthis
|     |     |     |     |     |     |     |     | all abnormal | data, which | can be understood |     | as recall | rate, |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ----------- | ----------------- | --- | --------- | ----- |
datasetrunsthroughtheentireexperimentalstudy.
expressedas:
TP
| B. BASELINE |     |     |     |     |     |     |     |     |        | =   | .   |     |      |
| ----------- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | ---- |
|             |     |     |     |     |     |     |     |     | Recall |     |     |     | (10) |
The following four state-of-the-art log-based or trace-based TP+FN
anomalydetectionmethodsareusedasbaselines. F1-Score: the harmonic mean of precision and recall,
| 1)DeepTraLog[25]usesaunifiedgraphrepresentationto |     |     |     |     |     |     |     | representedas |     |     |     |     |     |
| ------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | --- | --- | --- | --- |
describethecomplexstructureofthetraceandthelogevents
2Precision·Recall
embeddedinthestructure.Basedonthegraphrepresentation, F1= . (11)
Precision+Recall
| DeepTraLog | trains | a deep | SVDD | model | based | on GGNNs |     |     |     |     |     |     |     |
| ---------- | ------ | ------ | ---- | ----- | ----- | -------- | --- | --- | --- | --- | --- | --- | --- |
by combining traces and logs, and detects new traces and Accuracy is an important metric to measure the accuracy
anomaliesinthecorrespondinglogs. of outlier recognition, and wrong anomaly recognition will
2)TraceAnomaly[16]isatraceanomalydetectionmethod affect the accuracy of the algorithm. The recall rate reflects
that only considers service-level traces (operations are not the completeness of outlier identification, and the lack of
considered). It employs a posterior flow-based variational anomaly identification will affect the recall rate of the
autoencoder(VAE)todetectanomaloustrajectories. algorithm. The F1 score is the weighted harmonic average
3) DeepLog [13] is a log anomaly detection method that ofPrecisionandRecall,whichcanbetterevaluatetheresults
treatslogsasasequenceofevents.ItemploysLSTMmodels ofanomalydetection.
| 186516 |     |     |     |     |     |     |     |     |     |     |     | VOLUME12,2024 |     |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |

X.Liuetal.:LMGD:Log-MetricCombinedMicroserviceAnomalyDetectionThroughGraph-BasedDeepLearning
FIGURE5. AccuracymetricsindifferenthiddenlayersinGCN/GAT.
DeepTraLoghashighprecisionandhighrecall,itconsiders
allspaneventsandlogeventsofacallchain,andhasbetter
|     |     |     |     |     | performance | than | log anomaly |     | detection | methods | based on |
| --- | --- | --- | --- | --- | ----------- | ---- | ----------- | --- | --------- | ------- | -------- |
slidingwindowloganalysis.DeepTraLogistheonlybaseline
|     |     |     |     |     | method           | that considers | multi-source |        | trace        | and log | data for   |
| --- | --- | --- | --- | --- | ---------------- | -------------- | ------------ | ------ | ------------ | ------- | ---------- |
|     |     |     |     |     | fusion analysis, |                | so it shows  | better | performance. |         | In term of |
precision,DeepTraLogisslightlyhigherthanLMGD,andit
iseasytounderstandthattracedatacanprovidemoreaccurate
systemglobalinformationthanlogdata,whichisobtainedat
theexpenseofsystemintrusionandperformance.
|     |     |     |     |     | LMGD          | has      | the highest | F1                 | score | compared | to the    |
| --- | --- | --- | --- | --- | ------------- | -------- | ----------- | ------------------ | ----- | -------- | --------- |
|     |     |     |     |     | four baseline | methods, |             | thus demonstrating |       | its      | excellent |
FIGURE6. Performancemetricsindifferentmaximumleafnodes. performance. The precision rate is slightly lower than
|     |     |     |     |     | DeepTraLog, | and | the recall | rate | is the | highest. | Based on |
| --- | --- | --- | --- | --- | ----------- | --- | ---------- | ---- | ------ | -------- | -------- |
thedetailedanalysisofthepreviousalgorithm,itcanbeseen
D. EXPERIMENTALRESULTS
thattheanomalydetectionalgorithmofLMGDpaysattention
| Table 1 shows | the effectiveness | evaluation | results | of  |     |     |     |     |     |     |     |
| ------------- | ----------------- | ---------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
totheoccurrenceofthreekindsofanomalies,soitcancheck
differentmethods.TheresultsshowthatLMGDoutper-
|     |     |     |     |     | all the anomalies; |     | under | the requirements |     | of the | scene, this |
| --- | --- | --- | --- | --- | ------------------ | --- | ----- | ---------------- | --- | ------ | ----------- |
formsthebaselinemethodsandachieves0.827precision,
|     |     |     |     |     | method | mines the | information |     | in the log | and | metric data |
| --- | --- | --- | --- | --- | ------ | --------- | ----------- | --- | ---------- | --- | ----------- |
0.902recalland0.862F1-score.
|               |            |                    |        |     | as much | as possible | to obtain | relatively | high | precision | and |
| ------------- | ---------- | ------------------ | ------ | --- | ------- | ----------- | --------- | ---------- | ---- | --------- | --- |
| The precision | and recall | of the trace-based | method |     |         |             |           |            |      |           |     |
highestoverallF1score.
TraceAnomalyarelow.Thisapproachdoesnottakelogsinto
|     |     |     |     |     | In summary, |     | LMGD | is  | effective | in microservice |     |
| --- | --- | --- | --- | --- | ----------- | --- | ---- | --- | --------- | --------------- | --- |
account,soanomaliesinlogeventscannotbedetected.The
|     |     |     |     |     | anomaly | detection, | achieving |     | an average | improvement |     |
| --- | --- | --- | --- | --- | ------- | ---------- | --------- | --- | ---------- | ----------- | --- |
inputtoTraceAnomalyissequence-basedtracedata,witha
|     |     |     |     |     | of 2.63% | and 1.05% | in  | recall and | F1-score | than | existing |
| --- | --- | --- | --- | --- | -------- | --------- | --- | ---------- | -------- | ---- | -------- |
specialfocusonresponsetime,soitcanonlydetectanomalies
|                    |             |                  |             |     | trace-based | and | log-based | anomaly | detection |     | methods, |
| ------------------ | ----------- | ---------------- | ----------- | --- | ----------- | --- | --------- | ------- | --------- | --- | -------- |
| where the sequence | of spans or | the distribution | of response |     |             |     |           |         |           |     |          |
respectively.
timeshaveasignificantimpact.
| The log-based | methods DeepLog | and LogAnomaly |     | have |     |     |     |     |     |     |     |
| ------------- | --------------- | -------------- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
high recall and low precision. These two methods take into E. ABLATIONEXPERIMENT
account the events within the span and thus can detect The numbers of hidden layers of GCN and GAT are two
anomalies in the sequence of spans and the sequence of important parameters of this algorithm. The number of
log events. However, this method relies on predicting the hiddenlayersofGCNdeterminesthenumberofiterationsof
next event in a sliding window of the event sequence, messagepassingbetweennodes,whichhasagreaterimpact
and thus has no structured global view. As a result, on the underlying representation of the graph. The number
subsequencesofeventsthatarenotvisiblemaybeincorrectly ofhiddenlayersofGCNisusuallysetto2to4.Theresults
reported as exceptions. These two log anomaly detection showthatbothrecallandF1scoredecreaseasthenumber
methods are usually performed on a single sequence of log of hidden layers increases. This is usually because more
events such as HDFS datasets. Therefore, it does not work hidden layers can easily lead to over-smoothing, making
well for microservice anomaly detection involving parallel features indistinguishable and thus affecting classification
and asynchronous service calls involving multiple service accuracy. In addition, the system contains five nodes with
instancesanddistributedlogevents. low complexity. Excessive data exchange will lose the
| VOLUME12,2024 |     |     |     |     |     |     |     |     |     |     | 186517 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |

X.Liuetal.:LMGD:Log-MetricCombinedMicroserviceAnomalyDetectionThroughGraph-BasedDeepLearning
characteristicsofthedata,anditwillbedifficulttominethe (3)Weproposeananomalydetectionmethodthatisbased
dependenciesbetweenservices. on conjoint rule analysis. We conduct lots of experiments
The number of hidden layers of GAT determines the on the dataset proposed by Sasho Nedelkoski and compare
number of iterations of node and metrics message trans- our method with some current baselines in the field of
mission, which has a greater impact on the judgment of anomaly detection. The experimental results indicate that
metricsweight.Theinfluenceofthenumberofhiddenlayers the proposed method significantly outperforms state-of-the-
of GAT on the accuracy of anomaly detection is shown art approaches, with recall and F1-score metrics reaching
in the figure 5. The experimental results show that the 0.902and0.862,respectively.
2-layergraphnetworkcanachievebettertrainingresults. In our future work, we will study the influence of more
Accordingtothecharacteristicsofthedataset,itisalsoeasy parametersonthealgorithmeffect,andmakemoreeffortsin
to understand, and the metrics dimensions used are fewer, reducingthealgorithmcomplexity.
| only three, | and the   | complexity          |     | is very low. | Excessive |     | data  |            |     |     |     |     |     |
| ----------- | --------- | ------------------- | --- | ------------ | --------- | --- | ----- | ---------- | --- | --- | --- | --- | --- |
| exchange    | will lose | the characteristics |     | of           | the data, | and | it is | REFERENCES |     |     |     |     |     |
difficulttominethemetricstrend.
|     |     |     |     |     |     |     |     | [1] F. Auer, | V. Lenarduzzi, |     | M. Felderer, | and D. Taibi, | ‘‘From monolithic |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | -------------- | --- | ------------ | ------------- | ----------------- |
At the same time, the system also analyzes the impact systemstomicroservices:Anassessmentframework,’’Inf.Softw.Technol.,
of the maximum number of leaf nodes in the tree structure vol.137,Sep.2021,Art.no.106600.
in the template extraction stage on the performance of the [2] Z.Li,J.Chen,R.Jiao,N.Zhao,Z.Wang,S.Zhang,Y.Wu,L.Jiang,L.Yan,
Z.Wang,Z.Chen,W.Zhang,X.Nie,K.Sui,andD.Pei,‘‘Practicalroot
algorithm.Thedifferenceofthelargestleafnodewillhavean causelocalizationformicroservicesystemsviatraceanalysis,’’inProc.
importantimpactonthetimecomplexityofthealgorithmand IEEE/ACM29thInt.Symp.QualityService(IWQOS),Jun.2021,pp.1–10.
the effect of anomaly detection. Figure 6 shows that with [3] L.Wang,N.Zhao,J.Chen,P.Li,W.Zhang,andK.Sui,‘‘Root-cause
metriclocationformicroservicesystemsvialoganomalydetection,’’in
theincreaseofthelargestleafnode,thetimeconsumption
Proc.IEEEInt.Conf.WebServices(ICWS),Oct.2020,pp.142–150.
ofthealgorithmincreasesexponentially,andthegrowth
|     |     |     |     |     |     |     |     | [4] W.Setiawan,Y.Thounaojam,andA.Narayan,‘‘GWAD:Greedyworkflow |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------------------------------------------------- | --- | --- | --- | --- | --- |
graphanomalydetectionframeworkforsystemtraces,’’inProc.IEEEInt.
rateoftheF1scoregraduallyslowsdown.Thisisbecause,
Conf.Syst.,Man,Cybern.(SMC),Oct.2020,pp.2790–2796.
| if there      | is no limit | to the   | maximum | leaf         | node, | the number    |     |                                                               |           |       |         |                    |             |
| ------------- | ----------- | -------- | ------- | ------------ | ----- | ------------- | --- | ------------------------------------------------------------- | --------- | ----- | ------- | ------------------ | ----------- |
|               |             |          |         |              |       |               |     | [5] A.Nandi,A.Mandal,S.Atreja,G.B.Dasgupta,andS.Bhattacharya, |           |       |         |                    |             |
| of log groups | will        | increase | after   | the template |       | is extracted, |     |                                                               |           |       |         |                    |             |
|               |             |          |         |              |       |               |     | ‘‘Anomaly                                                     | detection | using | program | control flow graph | mining from |
thematchingtimeoflogdatawillincrease,andthenumber executionlogs,’’inProc.22ndACMSIGKDDInt.Conf.Knowl.Discovery
of nodes in the prediction stage of subsequent nodes will DataMining,Aug.2016,pp.215–224.
|     |     |     |     |     |     |     |     | [6] T.Jia,L.Yang,P.Chen,Y.Li,F.Meng,andJ.Xu,‘‘LogSed:Anomaly |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------------------ | --- | --- | --- | --- | --- |
alsoincrease,andthetrainingtimewillnaturallyincreaseto diagnosis through mining time-weighted control flow graph in logs,’’
a large extent. From the perspective of abnormal detection in Proc. IEEE 10th Int. Conf. Cloud Comput. (CLOUD), Jun. 2017,
effect, the increase of the largest leaf node, the accuracy pp.447–455.
|             |            |     |              |     |      |              |     | [7] P.Aggarwal,A.Gupta,P.Mohapatra,S.Nagar,A.Mandal,Q.Wang,and |     |     |     |     |     |
| ----------- | ---------- | --- | ------------ | --- | ---- | ------------ | --- | -------------------------------------------------------------- | --- | --- | --- | --- | --- |
| of template | extraction | and | log matching |     | will | be improved, |     |                                                                |     |     |     |     |     |
A.Paradkar,‘‘Localizationofoperationalfaultsincloudapplicationsby
and the learning of the system state will be more accurate, miningcausaldependenciesinlogsusinggoldensignals,’’inProc.Int.
Conf.Service-OrientedComput.Springer,2020,pp.137–149.
| so the F1 | score will | increase, | but | after reaching |     | the | critical |            |                  |     |                |              |             |
| --------- | ---------- | --------- | --- | -------------- | --- | --- | -------- | ---------- | ---------------- | --- | -------------- | ------------ | ----------- |
|           |            |           |     |                |     |     |          | [8] L. Wu, | J. Bogatinovski, |     | S. Nedelkoski, | J. Tordsson, | and O. Kao, |
point,theF1scorewilltendtobestable.Becausesubsequent
‘‘Performancediagnosisincloudmicroservicesusingdeeplearning,’’in
fetchesandmatcheswillnolongerchange.Inthiscase,this
Proc.Int.Conf.Service-OrientedComput.Springer,2020,pp.85–96.
paper selects a critical point to reduce the training time of [9] L.Wu,J.Tordsson,E.Elmroth,andO.Kao,‘‘MicroRCA:Rootcause
thealgorithmonthepremiseofensuringtheeffectivenessof localization of performance issues in microservices,’’ in Proc. NOMS
IEEE/IFIPNetw.OperationsManage.Symp.,Apr.2020,pp.1–9.
anomalydetection. [10] A. Gulenko, F. Schmidt, A. Acker, M. Wallschläger, O. Kao, and F.
Liu,‘‘Detectinganomalousbehaviorofblack-boxservicesmodeledwith
distance-basedonlineclustering,’’inProc.IEEE11thInt.Conf.Cloud
Comput.(CLOUD),Jul.2018,pp.912–915.
VI. CONCLUSION
|     |     |     |     |     |     |     |     | [11] Q.Fu,J.-G.Lou,Y.Wang,andJ.Li,‘‘Executionanomalydetectionin |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------------------------------------------------------- | --- | --- | --- | --- | --- |
Inthispaper,weproposeananomalydetectionmethodina
distributedsystemsthroughunstructuredloganalysis,’’inProc.9thIEEE
microservice environment. This method solves the problem Int.Conf.DataMining,Dec.2009,pp.149–158.
|              |            |         |           |               |      |          |         | [12] L.Bao,Q.Li,P.Lu,J.Lu,T.Ruan,andK.Zhang,‘‘Executionanomaly |                |         |         |             |                      |
| ------------ | ---------- | ------- | --------- | ------------- | ---- | -------- | ------- | -------------------------------------------------------------- | -------------- | ------- | ------- | ----------- | -------------------- |
| of not being | able       | to pay  | attention | to the        | time | interval | of      |                                                                |                |         |         |             |                      |
|              |            |         |           |               |      |          |         | detection                                                      | in large-scale | systems | through | console log | analysis,’’ J. Syst. |
| log data,    | solves the | problem |           | of log metric |      | data     | fusion, |                                                                |                |         |         |             |                      |
Softw.,vol.143,pp.172–186,Sep.2018.
and also solves the problem of simultaneous detection of [13] M.Du,F.Li,G.Zheng,andV.Srikumar,‘‘DeepLog:Anomalydetection
multipleanomalytypes.WeproposeaLog-MetricCombined anddiagnosisfromsystemlogsthroughdeeplearning,’’inProc.ACM
MicroserviceAnomalyDetectionthroughGraph-basedDeep SIGSACConf.Comput.Commun.Secur.,Oct.2017,pp.1285–1298.
|     |     |     |     |     |     |     |     | [14] S.Nedelkoski,J.Cardoso,andO.Kao,‘‘Anomalydetectionfromsystem |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------------------------------------------------------- | --- | --- | --- | --- | --- |
Learning(LMGD).Themethodisdividedintothreeparts: tracingdatausingmultimodaldeeplearning,’’inProc.IEEE12thInt.Conf.
(1) To address the issue of irregular log data intervals, CloudComput.(CLOUD),Jul.2019,pp.179–186.
|            |              |     |         |            |     |       |        | [15] Y.Gan,Y.Zhang,K.Hu,D.Cheng,Y.He,M.Pancholi,andC.Delimitrou, |            |          |             |                |                |
| ---------- | ------------ | --- | ------- | ---------- | --- | ----- | ------ | ---------------------------------------------------------------- | ---------- | -------- | ----------- | -------------- | -------------- |
| we propose | a time-aware |     | service | dependency |     | graph | gener- |                                                                  |            |          |             |                |                |
|            |              |     |         |            |     |       |        | ‘‘Seer:                                                          | Leveraging | big data | to navigate | the complexity | of performance |
ationmethod.
debuggingincloudmicroservices,’’inProc.24thInt.Conf.Architectural
| (2) we | propose | a novel | approach | for | integrating | log | and |     |     |     |     |     |     |
| ------ | ------- | ------- | -------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
SupportforProgram.Lang.OperatingSyst.,Apr.2019,pp.19–33.
metrics data to capture the inter-service dependencies and [16] P.Liu,H.Xu,Q.Ouyang,R.Jiao,Z.Chen,S.Zhang,J.Yang,L.Mo,
|             |        |              |            |     |                  |     |     | J.Zeng, | W. Xue, | and D. | Pei, ‘‘Unsupervised | detection | of microservice |
| ----------- | ------ | ------------ | ---------- | --- | ---------------- | --- | --- | ------- | ------- | ------ | ------------------- | --------- | --------------- |
| operational | status | of services, | leveraging |     | the capabilities |     | of  |         |         |        |                     |           |                 |
traceanomaliesthroughservice-leveldeepBayesiannetworks,’’inProc.
graphneuralnetworks. IEEE31stInt.Symp.Softw.Rel.Eng.(ISSRE),Oct.2020,pp.48–58.
| 186518 |     |     |     |     |     |     |     |     |     |     |     |     | VOLUME12,2024 |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- |

X.Liuetal.:LMGD:Log-MetricCombinedMicroserviceAnomalyDetectionThroughGraph-BasedDeepLearning
[17] Z. Zhang, M. K. Ramanathan, and P. Raj, ‘‘CRISP: Critical path YUEWENLIUiscurrentlypursuingthemaster’s
analysisoflarge-scalemicroservicearchitectures,’’inProc.USENIXAnnu. degreeincomputerscienceandtechnologywith
Tech.Conf.(USENIXATC),2022,pp.655–672. Beijing University of Posts and Telecommuni-
[18] M.Kim,R.Sumbaly,andS.Shah,‘‘Rootcausedetectioninaservice- cations. His research interests include machine
orientedarchitecture,’’ACMSIGMETRICSPerform.Eval.Rev.,vol.41, learningandAInative.
no.1,pp.93–104,Jun.2013.
[19] T.Jia,P.Chen,L.Yang,Y.Li,F.Meng,andJ.Xu,‘‘Anapproachfor
anomalydiagnosisbasedonhybridgraphmodelwithlogsfordistributed
services,’’ in Proc. IEEE Int. Conf. Web Services (ICWS), Jun. 2017,
pp.25–32.
[20] T.Jia,L.Yang,andP.Chen,‘‘Anomalydiagnosisthroughminingtime-
weightedcontrolflowgraphinlogs,’’inProc.IEEE10thInt.Conf.Cloud
Comput.(CLOUD),Sep.2017,pp.25–30.
[21] L.Mariani,C.Monni,M.Pezzé,O.Riganelli,andR.Xin,‘‘Localizing
faults in cloud systems,’’ in Proc. IEEE 11th Int. Conf. Softw. Test.,
VerificationValidation(ICST),Apr.2018,pp.262–273.
[22] Q.Du,T.Xie,andY.He,‘‘Anomalydetectionanddiagnosisforcontainer-
based microservices with performance monitoring,’’ in Proc. 18th Int.
Conf.AlgorithmsArchit.ParallelProcess.(ICA3PP),Guangzhou,China.
Springer,Nov.2018,pp.560–572.
MIAOMIAOWEIiscurrentlypursuingthemas-
[23] L. Mariani, M. Pezzè, O. Riganelli, and R. Xin, ‘‘Predicting failures
ter’sdegreeincomputerscienceandtechnology
in multi-tier distributed systems,’’ J. Syst. Softw., vol. 161, Mar. 2020,
withBeijingUniversityofPostsandTelecommu-
Art.no.110464.
[24] S.Nedelkoski,J.Bogatinovski,A.K.Mandapati,S.Becker,J.Cardoso, nications.Herresearchinterestsincludemachine
and O. Kao, ‘‘Multi-source distributed system data for AI-powered learningandanomlydetection.
analytics,’’inProc.8thIFIPWG2.14Eur.Conf.(ESOCC),Crete,Greece.
Springer,2020,pp.161–176.
[25] C. Zhang, X. Peng, C. Sha, K. Zhang, Z. Fu, X. Wu, Q. Lin, and
D. Zhang, ‘‘DeepTraLog: trace-log combined microservice anomaly
detectionthroughgraph-baseddeeplearning,’’inProc.IEEE/ACM44th
Int.Conf.Softw.Eng.(ICSE),May2022,pp.623–634.
[26] W.Meng,Y.Liu,Y.Zhu,S.Zhang,D.Pei,Y.Liu,Y.Chen,R.Zhang,
S.Tao,andP.Sun,‘‘Loganomaly:Unsuperviseddetectionofsequential
andquantitativeanomaliesinunstructuredlogs,’’inProc.IJCAI,vol.19,
2019,pp.4739–4745.
XU LIU received the Ph.D. degree in computer PENG XU receivedthePh.D.degreeincommu-
science from Beijing University of Posts and nication and information systems from Beijing
Telecommunications, China, in 2018. He is cur- University of Posts and Telecommunications,
rently working as a Senior Engineer with China China, in 2004. He is currently working as
Academy of Industrial Internet. His research an Associate Professor with Beijing University
interestsincludeindustrialinternetandbigdata. of Posts and Telecommunications. His research
interestsincludeAIOpsandindustrialbigdata.
VOLUME12,2024 186519