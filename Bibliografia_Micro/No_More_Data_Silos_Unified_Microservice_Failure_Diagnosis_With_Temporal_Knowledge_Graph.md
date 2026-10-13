IEEETRANSACTIONSONSERVICESCOMPUTING,VOL.17,NO.6,NOVEMBER/DECEMBER2024 4013
No More Data Silos: Unified Microservice Failure
Diagnosis With Temporal Knowledge Graph
ShenglinZhang ,Member,IEEE,YongxinZhao ,SiboXia ,ShiruiWei ,YongqianSun ,Member,IEEE,
ChenyuZhao,ShiyuMa ,JunhuaKuang,BolinZhu ,LemengPan ,YichengGuo ,
andDanPei ,SeniorMember,IEEE
Abstract—Microservices improve the scalability and flexibil- I. INTRODUCTION
ity of monolithic architectures to accommodate the evolution of
MICROSERVICES have gained significant attention in
software systems, but the complexity and dynamics of microser-
vices challenge system reliability. Ensuring microservice quality the last few years in both industry and academia [1].
requiresefficientfailurediagnosis,includingdetectionandtriage. However, the complexity and dynamism of microservice sys-
Failuredetectioninvolvesidentifyinganomalousbehaviorwithin tems pose unique challenges for maintenance [2]. When a
the system, while triage entails classifying the failure type and
microservice system fails, the failure will propagate along the
directingittotheengineeringteamforresolution.Unfortunately,
interaction network between microservices, posing significant
currentapproachesreliantonsingle-modalmonitoringdata,such
asmetrics,logs,ortraces,cannotcaptureallfailuresandneglect challengesandpressuresforoperators.Failureswillnegatively
interconnectionsamongmultimodaldata,leadingtoerroneousdi- impact user experience and cause enormous losses for service
agnoses.Recentmultimodaldatafusionstudiesstruggletoachieve providers if they are not quickly diagnosed and mitigated [3],
deepintegration,limitingdiagnosticaccuracyduetoinsufficiently
[4].Toensurehighavailabilityandminimizeservicedowntime,
capturedinterdependencies.Therefore,weproposeUniDiag,which
prompt diagnosis, encompassing both detection and triage, is
leveragestemporalknowledgegraphstofusemultimodaldatafor
effective failure diagnosis. UniDiag applies a simple yet effective crucial [5], [6]. This allows operators to respond efficiently to
stream-basedanomalydetectionmethodtoreducecomputational failures,mitigatingtheirimpactandrestoringservicefunction-
costandanovelmicroservice-orientedgraphembeddingmethod alityasquicklyaspossible.Proactivefailuredetectioncanalert
to represent the state of systems comprehensively. To assess the
operatorstimely,andaccuratefailuretriagecannotonlyprovide
performanceofUniDiag,weconductextensiveevaluationexperi-
operators with suggestions for mitigation measures (Table I)
mentsusingdatasetsfromtwobenchmarkmicroservicesystems,
demonstratingitssuperiorityoverexistingmethodsandaffirming butalsominimizethecostassociatedwithreassignment,which
theefficacyofmultimodaldatafusion.Additionally,wehavepub- referstotheprocessofre-allocatingtheinitiallyassignedmitiga-
liclymadethecodeanddataavailabletofacilitatefurtherresearch. tionmeasurestothepotentiallymoreappropriatemeasures[5].
IndexTerms—Microservice,failurediagnosis,multimodaldata, Therefore,rapidandaccuratefailurediagnosisisindispensable
knowledgegraph. foreffectivelymaintainingmicroservicesystems.
Received18June2024;revised19September2024;accepted16October A microservice system is an architecture composed of mul-
2024. Date of publication 31 October 2024; date of current version 30 De- tiple microservices, with each microservice having multiple
cember 2024. This work was supported in part by the Advanced Research
instances.Tomonitorthestatusofmicroservicesystemsinreal-
ProjectofChinaunderGrant31511010501,andinpartbytheNationalNatural
ScienceFoundationofChinaunderGrant62272249,Grant62302244,andGrant timeandachieverapidfailurediagnosis,operatorsoftencontin-
62072264.(Correspondingauthor:YongqianSun.) uouslycollectthreemodalitiesofmonitoringdata(i.e.,metrics,
ShenglinZhangiswiththeCollegeofSoftware,HaiheLaboratoryofInfor-
logs, traces) for each microservice instance [7]. Fig. 1 shows
mationTechnologyApplicationInnovation(HL-IT),NankaiUniversity,Tianjin
300192,China(e-mail:zhangsl@nankai.edu.cn). the three modalities of data in a microservice system. Metrics
YongxinZhao,SiboXia,ShiyuMa,andJunhuaKuangarewiththeNankai include system-level metrics (e.g., CPU utilization, memory
University, Tianjin 300192, China (e-mail: zyx_nkcs@mail.nankai.edu.cn;
utilization,andnetworkthroughput)anduser-perceivedmetrics
xiath@mail.nankai.edu.cn; mashiyu@mail.nankai.edu.cn; 2013157@mail.
nankai.edu.cn). (e.g., average response time, error rate, and page view count),
ShiruiWeiiswiththeUniversityoftheChineseAcademyofSciences,Beijing presented as time series. Logs are semi-structured text that
101408,China(e-mail:weishirui23@mails.ucas.ac.cn).
records various events and system runtime status. Traces are
YongqianSuniswiththeCollegeofSoftware,TianjinKeyLaboratoryof
SoftwareExperienceandHumanComputerInteraction(TKL-SEHCI),Nankai in the tree structure recording information about user requests
University,Tianjin300192,China(e-mail:sunyongqian@nankai.edu.cn). like instances and service calls, and each call forms a span.
Chenyu Zhao is with the Alibaba Group, Beijing 100020, China (e-mail:
For example, as shown in Fig. 1, after a failure occurs, the
zhaochenyu@mail.nankai.edu.cn).
BolinZhuiswiththeNanjingUniversity,Nanjing210093,China(e-mail: “system.cpu.pct_utilization” metric sharply rises,and simulta-
bolinzhu@smail.nju.edu.cn). neouslymicroserviceinstancesS1 andS2 generateanomalous
Lemeng Pan and Yicheng Guo are with the Huawei Technologies
log messages, with a significant increase in response time in
Co., Ltd., Shenzhen 518129, China (e-mail: panlemeng@huawei.com;
guoyicheng3@huawei.com). relatedtraces.
DanPeiiswiththeDepartmentofComputerScience,TsinghuaUniversity, Over the years, many single-modal data-based failure diag-
Beijing100190,China(e-mail:peidan@tsinghua.edu.cn).
nosisapproachesformicroservicesystemshavebeenproposed
DigitalObjectIdentifier10.1109/TSC.2024.3489444
1939-1374©2024IEEE.Personaluseispermitted,butrepublication/redistributionrequiresIEEEpermission.
Seehttps://www.ieee.org/publications/rights/index.htmlformoreinformation.
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on November 13,2025 at 00:49:19 UTC from IEEE Xplore. Restrictions apply.

4014 IEEETRANSACTIONSONSERVICESCOMPUTING,VOL.17,NO.6,NOVEMBER/DECEMBER2024
TABLEI
ANOMALOUSMANIFESTATIONSOFMULTIMODALDATAAREDERIVEDFROMANEXTENSIVEEMPIRICALANALYSISOFFAILURECASES,ANDMITIGATION
MEASURESFOREACHFAILURETYPEAREBASEDONTHEIRUNDERLYINGROOTCAUSES[21]
Fig.1. Anexampleofthemultimodaldataofamicroservicesystemduringafailure.Fig.1(a)showstwometrics:thebluelineinthefigurerepresentstheoriginal
valueofthemetric,andtheredlinerepresentsananomalousfragment.Fig.1(b)showseightlogs;theredonesareanomalous.Fig.1(c)showsatracewhereanode
representsamicroserviceinstance,anedgefromacallertoacalleedenotesaspan,andtheredspanisanomalousbecauseofitsexcessivelyhighresponsetime.
(e.g.,metrics[8],[9],[10],logs[11],[12],[13],ortraces[14]). learning frameworks in these existing methods introduces a
However, these approaches usually lead to a large number of significantdependencyonlabeleddata,restrictingtheirflexibil-
misdiagnosesduetotheinherentlimitationsofthecharacteris- ityandgeneralizationcapabilities,particularlywhenconfronted
ticsofthedataused: withnovelfailurepatternsorevolvingsystemarchitectures.
LimitationsofMetrics:Metricscanreactrapidlytochanges Muchresearchhasdemonstratedthatknowledgegraph(KG)
in system performance [15], reflecting various failure modes is a potent technique for combining multimodal informa-
viahigherorlowervalues.However,theover-sensitivityofthe tion[22],[23].Itcancaptureentitycharacteristicsforsubsequent
metrics may produce false alarms [15], [16]. For example, in failure detection and triage. Therefore, we try to apply KG to
scenarioswherememoryiseffectivelyreleased,notwithstanding fusemultimodaldataforfailurediagnosis(i.e.,failuredetection
a potentially decreased memory utilization may be lower than andtriage).However,applyingKGtoachievefailurediagnosis
normallevel,itdoesnotindicateasystemfailure. throughmultimodaldatafacesthefollowingchallenges:
LimitationsofLogs:Sincelogsaresemi-structuredtextgen- 1) Theimmensevolumeofmonitoringdatageneratedbymi-
eratedbyloggingstatementsinsoftwaresourcecode[17],they croservicessystems[2],makesitchallengingtointegrate
rely significantly on developers’ domain knowledge. Conse- allthedataintotheKGintheformofentitiesandrelations.
quently,certainnuancedperformanceissues,suchasanomalous Furthermore, as aforementioned, the multimodal data is
memoryutilization,maynotbeadequatelyreflectedinthelogs, heterogeneous.Thefusionoftheseheterogeneousdatain
renderingitimpossibletodiagnose“Resourceunderprovision- aKGposessignificantchallenges.
ing”failures(TableI). 2) The relations between entities in the KG manifest as a
Limitations of Traces: The information reflecting calls be- heterogeneouscomposition,capturingnotonlythestates
tween microservice instances does not provide information ofdistincteventswithinagivenmicroserviceinstancebut
about what is happening inside the instance [18]. This lack of alsotheintricateinteractionsandresource-sharingacross
informationmakesitunfeasibletodiagnose“Systemcomponent different instances. Moreover, the temporal variations in
damage”failuresthroughtracingalone(TableI). instance states and the dynamic fluctuations in the num-
Due to the above limitations, recent studies have explored ber of instances [24], [25] present notable obstacles in
multimodaldatafusionforenhancedfailurediagnosis[19],[20]. effectively acquiring temporal and heterogeneous struc-
However, these approaches often fall short of achieving suffi- turalinformationfromaKG.Furthermore,derivinggraph
cientlydeepintegrationofheterogeneousdatasources.Thislim- representations from dynamic node embeddings adds to
itation in effectively capturing the complex interdependencies thecomplexityofthechallenge.
between different modalities consequently hinders diagnostic In this paper, we propose UniDiag, a novel approach for
accuracy.Furthermore,thepredominantrelianceonsupervised integrating the multimodal data in microservice systems and
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on November 13,2025 at 00:49:19 UTC from IEEE Xplore. Restrictions apply.

ZHANGetal.:NOMOREDATASILOS:UNIFIEDMICROSERVICEFAILUREDIAGNOSISWITHTEMPORALKNOWLEDGEGRAPH 4015
conductingfailurediagnosis.Itfirstfusesmultimodaldatausing failuretypes.Yuanetal.[12]usesupervisedmethodstoextract
a temporal knowledge graph (TKG), which is constructed by features from anomalous logs and correlate them with failure
temporally stacking KG snapshots to capture system dynam- behaviors,requiringextensivemanuallabeling.
ics [26]. This method enables the effective fusion of multi- MEPFL [14] predicts errors and failure types for trace in-
modaldata.Subsequently,anovelmicroservice-orientedgraph stancesbasedonsystemtracedata.However,methodslikethose
embedding (MOGE) method is employed to generate graph in [31], [32], [33] using traces for anomaly detection or root
representations of the TKG, encoding its rich structural and causelocalizationdonotspecifyfailuretypes.
temporalinformation.Themaincontributionsofthispaperare Several studies integrate multimodal data for anomaly de-
asfollows: tection or root cause localization [18], [19], [20], [34], [35],
1) UniDiag considers the heterogeneity and correlation of [36], [37]. CloudRCA [20] combines metrics and logs with a
three modalities of data (i.e., metrics, logs, and traces) Knowledge-informed Hierarchical Bayesian Network for root
and combines these data with TKG. To the best of our cause analysis. MicroCBR [34] embeds anomaly event se-
knowledge,weareamongthefirsttoapplytheKG-based quences into a failure knowledge graph for case retrieval and
method to fuse the three modalities of data for failure failuretriage.DiagFusion[19]usesembeddingtechniquesand
diagnosis. aGraphNeuralNetworktodeterminefailuretypes.Eadro[18]
2) TodecreasethenumberofentitiespresentinKGandfuse models intra-service dynamics and inter-service dependencies
theheterogeneousdata,weproposeasimpleyeteffective using traces, logs, and KPIs for anomaly detection and root
stream-based anomaly detection method, addressing the cause localization. TAD [35] employs a Transformer encoder
firstchallenge. modeltoidentifyfailuresandutilizestracingchainstopinpoint
3) To obtain the comprehensive state representation of a faulty services. HeMiRCA [36] utilizes Spearman correlation
microservicesystem,weproposeanovelMOGEmethod, tolocalizehierarchicalrootcauses.MULAN[37]localizesroot
integratingtheRelation-awareGraphConvolutionalNet- causes by co-learning a causal graph from metrics and logs.
work(R-GCN)[27],GateRecurrentUnit(GRU)[28]and However, none of these approaches, including Eadro, TAD,
second-order pooling (SOPOOL) [29], which addresses HeMiRCA,andMULANoffercomprehensivetriageoffailure
the second challenge. R-GCN and GRU effectively cap- typesinmicroservicesystems.
ture the heterogeneous structural and temporal informa-
tion of entities and relations in the TKG, respectively. III. MOTIVATIONANDPROBLEMSTATEMENT
Furthermore,weutilizeSOPOOLtolearnacomprehen-
A. Motivation
sive graph representation of dynamically changing KGs
byleveragingthenodeembeddings. Our goal is to recommend to the operators the occurrence
4) We assess the efficacy and efficiency of UniDiag by andtypeoffailurebasedonthelatestmultimodaldatatohelp
conductingexperimentsontwobenchmarkmicroservice- operatorsquicklytakethecorrectmitigationmeasures.Werefer
generated datasets. Our findings reveal that UniDiag to this as failure diagnosis, which includes failure detection
achievesonlinediagnosiswithin0.6secondsandexhibits and triage, which facilitates a more comprehensive identifica-
robustgeneralizationacrossdiversemicroservicesystems. tion and comprehension of diverse failure types [5], [6], [38].
Furthermore, we observe that UniDiag outperforms the Table I lists typical failures encountered in microservice sys-
baseline methods, as evidenced by an average F1-score tems, showcasing the corresponding manifestations of these
of0.869and0.723forfailurediagnosisontherespective failures on multimodal data and the corresponding mitigation
datasets,representingasignificantimprovementof0.117 measures. The failure types are designated based on their un-
and0.04comparedtothebest-performingbaselinemeth- derlying root causes [21]. Nevertheless, the primary objective
ods,respectively.Beyondachievingsuperiorperformance ofourresearchinthisstudycentersonfailurediagnosisrather
on known failure types, UniDiag demonstrates promis- thanthesubsequentremediationoffailures.
ing capabilities for diagnosing previously unseen failure Ourexaminationof164microservicesystemfailurecasescol-
types,highlightingitspotentialforreal-worlddeployment lectedfrombenchmarkmicroservicesystems(seeSectionVI-A
scenarios.Toensurebetterreproducibility,wehavemade formoredetails)determinedthatthefusionofmultimodaldata
ourcodeanddatapubliclyavailable[30]. holds crucial significance in detecting and triaging failures.
During failures, anomalies can be observed in metrics [8],
[9], [10], logs [11], [12], and traces [31]. Moreover, different
II. RELATEDWORK
typesoffailuresexhibitdistinctanomalouspatternsacrossthese
Variousmethodologiesexistfordiagnosingfailuresthrough multimodaldata[18].
metricanalysis.Forinstance,iSQUAD[8]labelsrootcausesand 1) The Role of Metric in Failure Diagnosis: As shown in
featuresfordifferentfailureclusters,whilePatternMatcher[9] Fig. 1(a), the metric data is defined as x={x1,x2,...,xT },
employscoarse-grainedanomalydetectionandapatternclassi- whereTistheobservationwindowlengthandxt ∈Rrepresents
fiertoidentifyanomalouspatterns.DéjàVu[10]trainsamodel theobservationattimet.Metricsarecrucialforgaugingproper
usinghistoricalfailuresandsystemdependencies. systemfunctioning.Whenamicroserviceinstanceexperiences
Loganalysisisalsopivotalfordiagnosingmicroservicesys- failures, the associated metrics (e.g., memory utilization, disk
temfailures.LogCluster[11]clusterslogsequencestodetermine I/O,CPUutilization,andnetworkthroughput)frequentlyexhibit
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on November 13,2025 at 00:49:19 UTC from IEEE Xplore. Restrictions apply.

4016 IEEETRANSACTIONSONSERVICESCOMPUTING,VOL.17,NO.6,NOVEMBER/DECEMBER2024
abnormalpatterns.Therefore,operatorsmustremainvigilantin orchestration and dynamic interactions. Failure diagnosis is
continuouslymonitoringthemetrics. the core of microservice system maintenance, which enables
2) The Role of Log in Failure Diagnosis: As shown in operatorstoresolvefailureseffectively.
Fig.1(b),alogmessageoftencontainsmultiplefields,including Our goal is to recommend to the operators the occurrence
timestamp,nodeID,anddetailedinformation,etc.Thedetailed and type of failure based on the latest multimodal system
informationfieldisunstructuredandusuallycontainsconstants monitoring data to help operators quickly take the correct re-
and variables. The constants are fixed texts the developers set covery measures. We refer to this as failure diagnosis, which
todescribesystemevententitiesandrelations.Incontrast,the includes failure detection and triage. The detection and triage
variables carry dynamic runtime information (e.g., IP address, of failures facilitate a more comprehensive identification and
file name, status code, etc.) [17]. Various log parsing algo- comprehension of diverse failure types, thereby enabling the
rithms,suchasDrain[39]andFT-tree[40],canautomatically implementation of suitable remedial actions [5], [6], [38]. For
distinguish the constants and the variables, and generate log example, metrics, logs, and traces are the most direct signals
templates(constants)andparameters(variables).Systemstates that characterize underlying failures [43]. Table I lists typical
and significant events at various critical points are the main failures encountered in microservice systems, showcasing the
functionoflogs[41].Diagnosingmicroservicesystemfailures corresponding manifestations of these failures on multimodal
canbeeffectivelyfacilitatedbyanalyzingthediverseanomalous dataandthecorrespondingremedialmeasures.Thefailuretypes
behaviorsmanifestedinlogs. aredesignatedbasedontheirunderlyingrootcauses[21].Never-
3) The Role of Trace in Failure Diagnosis: The microser- theless,theprimaryobjectiveofourresearchinthisstudycenters
vicesystemsencompassasignificantvolumeofasynchronous on failure diagnosis rather than the subsequent remediation of
| interactionsbetweeninstancesofmicroservices,whichinvolve |     |     |     |     |     |     | failures. |     |     |     |     |     |
| -------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- |
intricateinvocationchains[2].AsshowninFig.1(c),themutual
invocationsbetweeninstancescanberepresentedastracetrees,
|           |            |         |             |     |            |      |     |     | IV. PRELIMINARIES |     |     |     |
| --------- | ---------- | ------- | ----------- | --- | ---------- | ---- | --- | --- | ----------------- | --- | --- | --- |
| where one | invocation | request | corresponds | to  | one trace. | Each |     |     |                   |     |     |     |
span corresponds to one service invocation, having a span ID A. TemporalKnowledgeGraph
| and a parent | ID  | to reconstruct | the calling | relations |     | between |     |     |     |     |     |     |
| ------------ | --- | -------------- | ----------- | --------- | --- | ------- | --- | --- | --- | --- | --- | --- |
ATKGincorporatestemporalinformationintoastaticKGby
individualspans[42].Thetracedata,whichcontainsresponse
extendingthetriple(h,r,t)intoaquadruple(h,r,t,τ),whereh
| time, status | codes, | and request | frequency, | etc., | can be | crucial |     |     |     |     |     |     |
| ------------ | ------ | ----------- | ---------- | ----- | ------ | ------- | --- | --- | --- | --- | --- | --- |
representstheheadentity,trepresentsthetailentity,rrepresents
indicatorsforfailures[14]. the relation, τ provides additional temporal information about
| 4) MultimodalDataFusion: |     |     | Forinstance,considera“Net- |     |     |     |          |                |            |          |         |               |
| ------------------------ | --- | --- | -------------------------- | --- | --- | --- | -------- | -------------- | ---------- | -------- | ------- | ------------- |
|                          |     |     |                            |     |     |     | the fact | of the triple, | indicating | that the | fact is | valid at time |
workdevicebreakdown”failuremayresultinincreasednetwork
|               |            |                    |             |         |         |       | τ. KG    | can effectively | combine       | multimodal  | data, | and since   |
| ------------- | ---------- | ------------------ | ----------- | ------- | ------- | ----- | -------- | --------------- | ------------- | ----------- | ----- | ----------- |
| packet errors | for        | affected services. | While       | metrics | alone   | might |          |                 |               |             |       |             |
|               |            |                    |             |         |         |       | metrics, | logs, and       | traces change | dynamically | over  | time, using |
| indicate      | anomalies, | identifying        | the failure | type    | remains | chal- |          |                 |               |             |       |             |
TKGallowsfortheaccuraterepresentationofthemicroservice
| lengingwithoutadditionalcontextualinformation.Byintegrat- |     |     |     |     |     |     | system’sstate. |     |     |     |     |     |
| --------------------------------------------------------- | --- | --- | --- | --- | --- | --- | -------------- | --- | --- | --- | --- | --- |
ingmetricswithtraces,whichexposedisruptedcommunication
pathsbetweenservices,operatorscanmorepreciselydiagnose
|     |     |     |     |     |     |     | B. R-GCN |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- |
theunderlyingnetworkdevicefailure.
Inlightoftheaboveobservations,anovelapproachforthefu-
|     |     |     |     |     |     |     | To capture | the | multiple relations | in the | graph, | R-GCN [27] |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --- | ------------------ | ------ | ------ | ---------- |
sionofmultimodaldatatoenableeffectivefailurediagnosishas
modelsdifferentrelationsforthecentralnodeseparatelywhile
beenconceptualized.Thishasculminatedinthedevelopmentof addingself-loopingfeaturesforfeaturefusionandcontinuously
UniDiag.
updatingtherepresentationofthecentralnode.InKGs,different
It is worth noting that in our study, data collection is con- edge types convey distinct information, and the direction of
ductedwithdistinctgranularitylevelstocapturecomprehensive edges plays a crucial role in determining the underlying facts.
insights.Metricsandlogsarecollectedatthemicroservicein-
Therefore,inourwork,weemployR-GCNtocapturenotonly
stancelevel,gainingadetailedunderstandingoftheperformance the states of individual events within a specific microservice
| and the | events | within individual | microservice |     | instances, | re- |     |     |     |     |     |     |
| ------- | ------ | ----------------- | ------------ | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
instancebutalsotheintricaterelationsamongdiverseinstances.
spectively.Meanwhile,tracesarecollectedatthemicroservices
| system level, | revealing | intricate | interactions | and | dependencies |     |        |     |     |     |     |     |
| ------------- | --------- | --------- | ------------ | --- | ------------ | --- | ------ | --- | --- | --- | --- | --- |
|               |           |           |              |     |              |     | C. GRU |     |     |     |     |     |
amongthemicroservicesandfacilitatingaholisticunderstand-
ing of the whole system. This multi-faceted analysis, encom- Recurrent Neural Network (RNN)[44] isa powerful model
passing various levels of data granularity, enables UniDiag to for processing sequential data [45]. However, it cannot solve
deliveracomprehensiveassessmentofthemicroservicessystem problemssuchaslong-termmemoryandgradientsinbackprop-
andempowersaccuratefailurediagnosis. agation.Long-ShortTermMemory(LSTM)[46]andGRU[28]
|     |     |     |     |     |     |     | have been   | proposed      | to address  | this issue. | GRU        | and LSTM  |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ------------- | ----------- | ----------- | ---------- | --------- |
|     |     |     |     |     |     |     | are similar | in functional | performance | in          | many cases | [47], but |
B. ProblemStatement
|     |     |     |     |     |     |     | compared | to LSTM, | GRU has | fewer parameters |     | and is more |
| --- | --- | --- | --- | --- | --- | --- | -------- | -------- | ------- | ---------------- | --- | ----------- |
Thefine-graineddecompositionofmicroservicesmakesthe computationally efficient. Therefore, we choose GRU in Uni-
| systemsusceptibletoperformanceissuesduetohighlycomplex |     |     |     |     |     |     | Diag. |     |     |     |     |     |
| ------------------------------------------------------ | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- |
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on November 13,2025 at 00:49:19 UTC from IEEE Xplore.  Restrictions apply.

ZHANGetal.:NOMOREDATASILOS:UNIFIEDMICROSERVICEFAILUREDIAGNOSISWITHTEMPORALKNOWLEDGEGRAPH 4017
Fig.2. TheframeworkofUniDiag.
V. APPROACH adeptly capturing the dynamic nature of microservices. Their
|     |     |     |     |     | ability to accommodate |     | updates |     | ensures | real-time | accuracy, |
| --- | --- | --- | --- | --- | ---------------------- | --- | ------- | --- | ------- | --------- | --------- |
A. Overview
|     |     |     |     |     | which is essential | for | effective | monitoring |     | in rapidly | evolving |
| --- | --- | --- | --- | --- | ------------------ | --- | --------- | ---------- | --- | ---------- | -------- |
AsshowninFig.2,UniDiaghastwoparts:offlinetrainingand environments.UniDiagappliesTKGstoenhancethefusionof
onlinediagnosis.Intheofflinetrainingstage,UniDiagconsists heterogeneousmultimodaldata.TheTKGscanbeviewedasa
ofthreemainsteps:
|     |     |     |     |     | series of sub-KGs, | i.e., | G=(Gτ−k+1,...,Gτ−1,Gτ), |     |     |     | where |
| --- | --- | --- | --- | --- | ------------------ | ----- | ----------------------- | --- | --- | --- | ----- |
1) Multimodal Temporal Knowledge Graph Construction Gτ istheKGattimeτ.Wetrytoutilizeallinstances,metrics,
(Section V-B): To address the first challenge of KG, we andlogtemplatesinthemicroservicesystemasnodesinGτ.
introduce a stream-based anomaly detection module. It Serializing Multimodal Data: As shown on the left side of
firstserializesthemultimodaldataintostreamsbasedon Fig.3,weneedtoserializemultimodaldataofeachmicroservice
theircharacteristics,andthenconductsanomalydetection
instancetoobtainmultimodalinformationateachtimepoint.
for each stream. To deal with the dynamically changing 1) MetricSerialization:Metricsappearintheformoftimese-
data, UniDiag builds a TKG based on the topological rieswithaserializedstructure.Therefore,UniDiagadopts
relationsofmicroservicesystems. standardpreprocessingstepssuchasnormalization.
2) MOGE (Section V-C): To address the second challenge, 2) Log Serialization: Logs, as semi-structured text, encap-
UniDiagcombinesR-GCN,GRU,andSOPOOL.R-GCN sulate crucial information regarding system events [17].
leverages its ability to handle multi-relational graphs to UniDiagemploystheDrainalgorithm[39]toextractfixed
learnthestructuralinformationwithintheTKG.GRU,on textsegments,referredtoaslogtemplates,whichpreserve
| the other | hand, | captures | long sequence dependencies |     | to       |          |         |     |           |               |        |
| --------- | ----- | -------- | -------------------------- | --- | -------- | -------- | ------- | --- | --------- | ------------- | ------ |
|           |       |          |                            |     | the core | semantic | content |     | essential | for effective | analy- |
learn the temporal information within the TKG. Lastly, sis[48].Utilizingtheslidingwindowtechnique,UniDiag
SOPOOL pools the TKG to capture high-level features segmentsthelogsandquantifiestheoccurrencefrequency
withinthegraph. of each log template per minute. These frequencies are
3) Failure Diagnosis (Section V-D): A hierarchical cluster- subsequently transformed into time series data, aligning
| ing approach |     | is used to | perform failure diagnosis | on the |     |     |     |     |     |     |     |
| ------------ | --- | ---------- | ------------------------- | ------ | --- | --- | --- | --- | --- | --- | --- |
withmetricsforcomprehensiveanalysis.
learnedgraphembeddingstoobtainanumberofclusters. 3) TraceSerialization:UniDiagconcentratesonthreepivotal
Then, UniDiag presents these clusters to operators who metricsfortraces:responsetime(RT),errorcount(EC),
investigate and assign corresponding normal or failure andquerycount(QC)[32].Thesemetricsareessentialfor
typestoeachcluster. identifyinganomalies relatedtoperformance,reliability,
Intheonlinediagnosis(SectionV-E)stage,UniDiagconverts
|     |     |     |     |     | and traffic | [32]. | Specifically, |     | to ensure | a comprehensive |     |
| --- | --- | --- | --- | --- | ----------- | ----- | ------------- | --- | --------- | --------------- | --- |
the data into a graph representation vector and diagnoses the evaluation,wedividethedataintoone-minutetimewin-
failuretypebasedonthetrainedmodel(SectionV-D). dows and obtain the values of the three critical metrics
withineachwindow.Accordingly,wegeneratethreetime
|     |     |     |     |     | series for | each | tuple | <caller, | callee>, | each | reflecting |
| --- | --- | --- | --- | --- | ---------- | ---- | ----- | -------- | -------- | ---- | ---------- |
B. MultimodalTemporalKnowledgeGraphConstruction
theaverageresponsetime,querycount,anderrorcount,
| KG representations, |     | characterized | by their structured | nodes | respectively. |     |     |     |     |     |     |
| ------------------- | --- | ------------- | ------------------- | ----- | ------------- | --- | --- | --- | --- | --- | --- |
and edges, elucidate the relationships among diverse data Capturing Microservice Dependencies: Understanding the
sourceswithinmicroservicesystems.Thisstructuredapproach intricatedependenciesbetweenmicroservicesiscrucialforef-
enhances the comprehension of complex dependencies and fective failure diagnosing [19]. These dependencies primarily
|             |              |            |                    |        | consist of function |     | calling | and | resource | contention | [49]. To |
| ----------- | ------------ | ---------- | ------------------ | ------ | ------------------- | --- | ------- | --- | -------- | ---------- | -------- |
| facilitates | the analysis | of failure | patterns. Temporal | Knowl- |                     |     |         |     |          |            |          |
edgeGraphs(TKGs)offersignificantflexibilityandscalability, accurately model these interdependencies, we integrate traces
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on November 13,2025 at 00:49:19 UTC from IEEE Xplore.  Restrictions apply.

4018 IEEETRANSACTIONSONSERVICESCOMPUTING,VOL.17,NO.6,NOVEMBER/DECEMBER2024
Fig.3. Multimodaldataserialization,stream-basedanomalydetection,andconstructionofTKGs(u_low:unexpectedlow,e_high:excessivelyhigh).
and deployment data. Specifically, we aggregate trace data to the trace-related metrics are anomalous or not. For instance,
representtheinvocationrelationsbetweenmicroservices,adding thequadruplerepresentationforcallsbetweentwomicroservice
adirectededgeintheKGfromeachcallertoitscorresponding instancesS1andS2isexpressedas(S1,anomalouslycalls,S2,
callee. Additionally, when two instances are co-deployed ac- τ).Moreover,therelationbetweenmicroserviceinstanceS1and
cordingtothedeploymentdata,weintroduceadirectededgein hostH1ispresentedas(S1,deploysat,H1,τ).Finally,UniDiag
the KG from the instance to the physical host associated with builds a comprehensive KG (τ) based on the serialized data
thedeploymentdata. and the topological relation between microservice instances.
TransformingTimeSeriesDataintoEvents:Theintuitiveidea UniDiag stacks the KGs of each moment together to form a
is to regard the invocation and deployment relations between graphstream(i.e.,aTKG).
| instances, | the value | of metrics | data, | the number | of  | log tem- |     |     |     |     |     |     |     |
| ---------- | --------- | ---------- | ----- | ---------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
plates, and the value of three vital trace-related metrics data C. Microservice-OrientedGraphEmbedding
asedges.However,thiswillbringexcessivelyhighcalculation
TolearnthenodesandedgesinformationinTKG,UniDiag
andstoragecostsforsubsequenttasks,makingreal-timefailure
usesentityandrelationembedding.WeapplyR-GCNandGRU
| diagnosis | impractical. | Therefore, | UniDiag |     | applies | a stream- |     |     |     |     |     |     |     |
| --------- | ------------ | ---------- | ------- | --- | ------- | --------- | --- | --- | --- | --- | --- | --- | --- |
totakeintoaccountthestructuralandtemporalinformationof
basedanomalydetectionapproachtotransformthesetimeseries
entitiesandrelations,respectively.
| into events | and capture | the   | underlying | characteristics |         | of the     |          |             |             |                     |      |         |            |
| ----------- | ----------- | ----- | ---------- | --------------- | ------- | ---------- | -------- | ----------- | ----------- | ------------------- | ---- | ------- | ---------- |
|             |             |       |            |                 |         |            | Capture  | Structural  | Dependency: |                     | Each | graph   | in the TKG |
| multimodal  | data. As    | shown | in the     | middle          | part of | Fig. 3, we |          |             |             |                     |      |         |            |
|             |             |       |            |                 |         |            | contains | rich facts, | and         | the interconnection |      | between | entities   |
adoptthe3-sigmaruletoclassifythetimeseriesdataasnormal,
demonstratesastructuraldependency.Exploitingthestructural
excessivelyhigh,andunexpectedlyloweveryminute,thenthe
dependencyenablesthecentralentitytoaggregateinformation
typeoftheedgeissetaccordingly.Specifically,theedgesettings
fromitssurroundingneighborsandenhancethelearningofen-
inGτ areasfollows:
tityrepresentations.UniDiagusesL-layerrelation-awareGCN
| The edge | of an instance-type |     | object | represents | whether | itis |     |     |     |     |     |     |     |
| -------- | ------------------- | --- | ------ | ---------- | ------- | ---- | --- | --- | --- | --- | --- | --- | --- |
asanevolutionaryunittomodeltheconcurrentfactsofstructural
anormaloranomalouscall,andthisclassificationdependson
|     |     |     |     |     |     |     | dependency | information. |     | Each entity | et,τ | obtains | information |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ------------ | --- | ----------- | ---- | ------- | ----------- |
whetherthecurrentvaluesofthethreekeytrace-relatedmetrics
|             |             |       |                 |     |      |           | from itself, | its connected |     | neighboring | entities | eh,τ, | and the |
| ----------- | ----------- | ----- | --------------- | --- | ---- | --------- | ------------ | ------------- | --- | ----------- | -------- | ----- | ------- |
| are normal, | excessively | high, | or unexpectedly |     | low. | Moreover, |              |               |     |             |          |       |         |
relationrattimeτ,andpassesdowntothenextlayer
| theedgeofametric-type(log-template-type)objectrepresents |     |     |     |     |     |     |     | ⎛   |     |     |     |     | ⎞   |
| -------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(cid:4)
whetherthecurrentmetric(log)dataisnormal,excessivelyhigh, ⎝1 (cid:5) (cid:6)
|     |     |     |     |     |     |     | k+1 |     |     |     | k k |     | k k ⎠ |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |
or unexpectedly low. UniDiag stores this information on the (cid:3)e t,τ =f γ 1 (cid:3)e h,τ +(cid:3)rτ +γ 2 (cid:3)e t,τ ,
δt
| edgesoftheKG. |     |     |     |     |     |     |     | (h,r),∃(h,r,t)∈ϑ |     |     |     |     |     |
| ------------- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | --- | --- | --- | --- |
τ
(1)
ConstructingtheTKG:Attimeτ,UniDiagutilizestheoutput
∈[0,L−1],(cid:3)ek
obtained from stream-based anomaly detection to derive the whereϑτ isthesetoffactsattimestampτ,k h,τ ,
|            |                         |     |     |          |          |     | (cid:3)rτ,(cid:3)ek | denotethekthlayerembeddingsofentitiesh,relationr, |     |     |       |                   |     |
| ---------- | ----------------------- | --- | --- | -------- | -------- | --- | ------------------- | ------------------------------------------------- | --- | --- | ----- | ----------------- | --- |
| quadruples | requiredforconstructing |     |     | aTKG.For | example, | the | t,τ                 |                                                   |     |     |       |                   |     |
|            |                         |     |     |          |          |     |                     |                                                   |     |     | kandγ | karetheparameters |     |
representationofaquadruplebetweenmicroserviceinstanceS1 andentitiestattimeτ,respectively.γ
|     |     |     |     |     |     |     |     |     |     |     | 1   | 2   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
andmetricm1isindicatedas(S1,hasanormalvalueof,m1,τ), foraggregatingfeaturesandself-loopinthekthlayer.(cid:3)ek +(cid:3)rt
h,τ
whereastherepresentationofaquadruplebetweenmicroservice representstherelationaltranslationbetweentheheadentityand
instanceS1andlogtemplatel1isdenotedas(S1,hasanexces- the tail entity under relation r. δt is a normalization constant,
sivelyhighnumberof,l1,τ).Concerningtracedata,weutilize equaltothein-degreeofentityt.f(·)istheRReLUactivation
| “anomalously | calls” | and “normally |     | calls” to | identify | whether | function. |     |     |     |     |     |     |
| ------------ | ------ | ------------- | --- | --------- | -------- | ------- | --------- | --- | --- | --- | --- | --- | --- |
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on November 13,2025 at 00:49:19 UTC from IEEE Xplore.  Restrictions apply.

ZHANGetal.:NOMOREDATASILOS:UNIFIEDMICROSERVICEFAILUREDIAGNOSISWITHTEMPORALKNOWLEDGEGRAPH 4019
CaptureTemporalInformation:ATKGcontainsinformation We train the MOGE model with the KG inference task of
about the dynamic evolution of KGs over time. UniDiag uti- theTKG.Specifically,theinferenceisperformedontheKGof
lizes two temporal gating components to model the sequential thenextmomentbasedontheKGofthecurrentmoment,and
informationofentitiesandrelations,respectively. across-entropylossiscomputedaccordingtotheresultofthe
Theembeddingofallentitiesattimeτ isdeterminedbythe inferredandtheactualKGofthenextmoment.
| finallayeroutputoftherelation-awareGCNattimeτ |     |     |              |     | andthe |                     |     |     |     |     |     |     |
| --------------------------------------------- | --- | --- | ------------ | --- | ------ | ------------------- | --- | --- | --- | --- | --- | --- |
| entityembeddingrepresentationattimeτ          |     |     | −1.Formally, |     |        |                     |     |     |     |     |     |     |
|                                               |     |     |              |     |        | D. FailureDiagnosis |     |     |     |     |     |     |
◦E L +(1−Uτ)◦Eτ−1,
|         | Eτ =Uτ          |            |           |         | (2) |                                                        |            |            |     |          |          |          |
| ------- | --------------- | ---------- | --------- | ------- | --- | ------------------------------------------------------ | ---------- | ---------- | --- | -------- | -------- | -------- |
|         |                 | τ          |           |         |     | UniDiagtrainsfailurediagnosismodelsusingvariousfailure |            |            |     |          |          |          |
| where E | ∈R|E|∗d denotes | the entity | embedding | matrix, | E   | is                                                     |            |            |     |          |          |          |
|         |                 |            |           |         |     | features.                                              | Initially, | the number | of  | clusters | n is set | based on |
thesetofentities,anddisthedimensionoftheembeddings.◦
operators’priorknowledge.UniDiagthenclusterstheembedded
denotestheHadamardproduct.ThetemporalgateUτ ∈R|E|×d representationsofmultimodalTKGsaccordington.Thefarthest
conductsnonlineartransformation. distancebetweenclustercentersdefinesthedistancethreshold
| Theembeddingofarelationattimeτ |     |     | isinfluencedbyEτ−1 |     |     | d.  |     |     |     |     |     |     |
| ------------------------------ | --- | --- | ------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ander,τ,whichcanbeformulatedas Weemployhierarchicalagglomerativeclustering(HAC)for
(cid:6) the following reasons: (1) it uses a “bottom-up” approach to
|     | (cid:3)r =[pooling(Eτ−1,er,τ);(cid:3)r], |     |     |     | (3) |     |     |     |     |     |     |     |
| --- | ---------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
τ identifyhierarchicalrelations;(2)itiseasytodefineandflexible
where(cid:3)ristheembeddingofrelationr,er,τ isthesetofr-related with distance similarities and rules; (3) it handles clusters of
entities, pooling denotes the mean pooling operation, and [;] differentsizes;and(4)itiswidelyusedinfailurediagnosis[13],
|     |     |     |     |     |     | [50], [51]. | Operators | label | each cluster | with | a specific | failure |
| --- | --- | --- | --- | --- | --- | ----------- | --------- | ----- | ------------ | ---- | ---------- | ------- |
denotesthevectorconcatenationoperation.
UniDiagusestheGRUcomponenttoobtaintheembedding type using a typical case, thus reducing annotation effort by
ofallrelations labelingonlythetypicalcaseclosesttoeachclustercenter.
(cid:6)
|     | Rτ =GRU(Rτ−1,R |     | ),  |     | (4) |     |     |     |     |     |     |     |
| --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
τ
|                |         |              |           |         |     | E. OnlineDiagnosisandUpdate |     |     |     |     |     |     |
| -------------- | ------- | ------------ | --------- | ------- | --- | --------------------------- | --- | --- | --- | --- | --- | --- |
| where R∈R|R|∗d | denotes | the relation | embedding | matrix, | and |                             |     |     |     |     |     |     |
Risthesetofrelations.
Foranewwindow’smultimodaldata,UniDiagcalculatesthe
Our goal is to diagnose failures in the entire microservice distancebetweenthefailure’sembeddingandtheexistingcluster
system,soweneedtolearnthegraphembeddingsoftheKGat centers,mappingthefailuretothenearestcluster.Ifthedistance
eachmomenttoperformdownstreamdiagnostictasks.Because is less than d, the failure is classified according to the nearest
microservice instances are dynamically created and deleted in clustercenter.Otherwise,anewclusteriscreatedandlabeledby
themicroservicesystem,thedeploymentandinvocationrelation operators,whothenupdateUniDiagaccordingly.Discrepancies
also change dynamically [24], [25]. That is, the KGs in the betweenUniDiag’sdiagnosisandoperators’verificationresult
constructedTKGcanbedifferent,whichbringschallengesfor inclustersetupdates,enhancingperformance.
subsequent failure detection and triage. Moreover, there is no UniDiagisinitiallydeployedinalimitednumberofscenarios
inherentorderingrelationamongthenodesinthegraph,andwe and gradually expanded as it stabilizes. Failures identified in
getthesameoutput byusinganyorder ofnoderepresentation onescenariocaninformdiagnosesinotherscenarios,allowing
asinput. operators to build a comprehensive knowledge base of failure
|     |     |     |     |     |     | types. This | enables | quick | labeling | of new | failures, | thereby |
| --- | --- | --- | --- | --- | --- | ----------- | ------- | ----- | -------- | ------ | --------- | ------- |
SOPOOL[29]collectssecond-orderstatisticsfromtheinfor-
mationofallnodes.Itcapturesthecorrelationsamongfeatures improvingdiagnosisefficiencyandmitigation.
andtopologyinformationingraphrepresentationlearning[29].
| In this way, | it can help UniDiag |     | address the | above challenge. |     |     |     |     |     |     |     |     |
| ------------ | ------------------- | --- | ----------- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- |
F. ComputationalComplexityAnalysis
Therefore,UniDiagusesSOPOOLtoobtainagraphrepresen-
UniDiag To evaluate the computational efficiency of UniDiag, we
| tation based | on node representation. |     |     | transforms | the |     |     |     |     |     |     |     |
| ------------ | ----------------------- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
entityembeddingmatrixEusingalinearmappingtoobtainthe conduct a complexity analysis of two critical components:
embeddingofthegraph Multimodal Temporal Knowledge Graph Construction and
|     |             |     | T   |     |     | Microservice-Oriented |     | Graph | Embedding. |     | In the | Multimodal |
| --- | ----------- | --- | --- | --- | --- | --------------------- | --- | ----- | ---------- | --- | ------ | ---------- |
|     | SOPOOL(E)=E |     | Eμ, |     | (5) |                       |     |       |            |     |        |            |
TemporalKnowledgeGraphConstructionphase,thetimecom-
whereμ∈Rdisatrainablevector. plexity for serializing multimodal data is determined by the
These graph embeddings, encapsulating the rich informa- number of data entries at each timestamp. Constructing the
tional content of three distinct monitoring data (metrics, logs, knowledge graph entails the insertion of nodes and edges.
|E |
andtraces)gatheredduringmicroservicesystemoperation,ef- Assuming the number of nodes is all and the number of
fectively capture the nuanced patterns embedded within each edges is |R all |, the complexity is O(|E all |+|R all |). In the
modality.Thiscomprehensiverepresentation,derivedfromthe Microservice-OrientedGraphEmbeddingphase,thetimecom-
plexityforcapturingstructuraldependenciesisO(|F|L),where
fusionofheterogeneousdatasources,enablesamorediscrim-
inating differentiation between various failure types, thereby |F| denotes the maximum number of concurrent facts within
facilitatingincreasedaccuracyindownstreamfailurediagnosis the knowledge graph. Additionally, the time complexity for
|        |     |     |     |     |     | capturingtemporalinformationisO(|E |     |     |     |     | ||R|),where|E | |is |
| ------ | --- | --- | --- | --- | --- | ---------------------------------- | --- | --- | --- | --- | ------------- | --- |
| tasks. |     |     |     |     |     |                                    |     |     |     | sub |               | sub |
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on November 13,2025 at 00:49:19 UTC from IEEE Xplore.  Restrictions apply.

4020 IEEETRANSACTIONSONSERVICESCOMPUTING,VOL.17,NO.6,NOVEMBER/DECEMBER2024
TABLEII Baselines: We compare UniDiag with the following base-
DATASETINFORMATION line methods: iSQUAD [8], DéjàVu [10], LogCluster [11],
Cloud19[12],MEPFL[14],CloudRCA[20],MicroCBR[34],
andDiagFusion[19],whicharebasedoneithersingle-modalor
multimodaldata.Weimplementthesemethodsreferringtothe
|     |     |     |     |     |     | codes provided |     | by the | original | papers. | For | the | papers | without |
| --- | --- | --- | --- | --- | --- | -------------- | --- | ------ | -------- | ------- | --- | --- | ------ | ------- |
open-sourcecodes,wesetthehyperparametersaccordingtothe
descriptionsprovidedintherespectivepapers.
EvaluationMetrics:Inthetaskoffailurediagnosis,distinct
|     |     |     |     |     |     | labels are | assigned |     | to each | type | of failure. | Hence, | to  | assess |
| --- | --- | --- | --- | --- | --- | ---------- | -------- | --- | ------- | ---- | ----------- | ------ | --- | ------ |
multi-labeltasks,weutilizetheextensivelyemployedevaluation
metricsknownasWeightedAveragePrecision,WeightedAver-
themaximumnumberofentitiesinvolvedintherelationships, ageRecall,andWeightedAverageF1-score[55].Foreachlabel,
and|R|isthesizeoftherelationset. weperformcalculationstodeterminetherespectiveprecision=
|     |     |     |     |     |     | TP/(TP | +FP),recall |     | =TP/(TP |     | +FN),and |     | F1-score= |     |
| --- | --- | --- | --- | --- | --- | ------ | ----------- | --- | ------- | --- | -------- | --- | --------- | --- |
2×precision×recall/(precision+recall),withTruePos-
|     |     | VI. EVALUATION |     |     |     |                   |     |           |     |          |       |           |     |       |
| --- | --- | -------------- | --- | --- | --- | ----------------- | --- | --------- | --- | -------- | ----- | --------- | --- | ----- |
|     |     |                |     |     |     | itives (TP),False |     | Positives |     | (FP),and | False | Negatives |     | (FN). |
Weaimtoanswerthefollowingresearchquestions(RQs):
Subsequently,thesemetricsareaveragedbyapplyingweighting
RQ1:HoweffectivedoesUniDiagperforminfailurediagno-
|     |     |     |     |     |     | based on | the | support, | representing |     | the | number | of true | cases |
| --- | --- | --- | --- | --- | --- | -------- | --- | -------- | ------------ | --- | --- | ------ | ------- | ----- |
sis?
associatedwitheachlabel.
RQ2:DoeseachcomponentcontributetoUniDiag?
|     |     |     |     |     |     | Furthermore, |     | in the | ablation | experiments, |     | we  | employ | two |
| --- | --- | --- | --- | --- | --- | ------------ | --- | ------ | -------- | ------------ | --- | --- | ------ | --- |
RQ3:DoeseachdatamodalitycontributetoUniDiag?
|     |     |     |     |     |     | widely | acknowledged |     | metrics, | namely | Normalized |     | Mutual | In- |
| --- | --- | --- | --- | --- | --- | ------ | ------------ | --- | -------- | ------ | ---------- | --- | ------ | --- |
RQ4:IsUniDiagcomputationallyefficient?
|     |     |     |     |     |     | formation | (NMI) | [56] | and | Clustering | Accuracy |     | (ACC) | [57], |
| --- | --- | --- | --- | --- | --- | --------- | ----- | ---- | --- | ---------- | -------- | --- | ----- | ----- |
RQ5:Whatistheimpactofdifferenthyperparametersettings?
|     |     |     |     |     |     | to evaluate | the | performance |     | of UniDiag. |     | NMI | is a commonly |     |
| --- | --- | --- | --- | --- | --- | ----------- | --- | ----------- | --- | ----------- | --- | --- | ------------- | --- |
usedevaluationmetricforclusteringresults,whichmeasuresthe
A. ExperimentalSetup
|          |             |          |     |                   |        | consistency      | between |     | clustering | results | and | ground-truth |     | class            |
| -------- | ----------- | -------- | --- | ----------------- | ------ | ---------------- | ------- | --- | ---------- | ------- | --- | ------------ | --- | ---------------- |
| Dataset: | To evaluate | UniDiag, | we  | conduct extensive | exper- | labels.Formally, |         |     |            |         |     |              |     |                  |
|          |             |          |     |                   |        |                  |         |     | (cid:10)   |         |     | (cid:10)     |     | (cid:11)(cid:11) |
iments using two datasets, D1 and D2, sourced from distinct (cid:9) (cid:9)
|     |     |     |     |     |     |     |     | 2×  |     | |T ∩Q | |×log | C   | ×| T i ∩ Q j | |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | ----- | --- | -------------- | --- |
microservice systems with varying business contexts and ar- i j i j |T | × | Q |
|     |     |     |     |     |     | NMI=−(cid:9) |     | (cid:10) | (cid:10) | (cid:11)(cid:11) | (cid:10) |     | i (cid:10)j | (cid:11)(cid:11), |
| --- | --- | --- | --- | --- | --- | ------------ | --- | -------- | -------- | ---------------- | -------- | --- | ----------- | ----------------- |
c h i te c t u r e s . T a b l e I I d e t a il s the da ta s e t s. B o th d a ta se ts a re s p li t (cid:9)
|     |     |     |     |     |     |     |     | |T |×log |     | |T | |     | |Q |× | |Q  | j | |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | ---- | --- | ----- | --- | --- |
|     |     |     |     |     |     |     |     | i i      |     | i +  | j   | j     | log |     |
in t o t r a i n i n g ( t h e i n it i a l 7 0 % of fa il u r e c as e s) a n d te st in g ( th e C C
| remaining30%)setsbasedontheirstarttime. |         |              |             |         |       |          |                           |     |           |         |         |           |                | (6)    |
| --------------------------------------- | ------- | ------------ | ----------- | ------- | ----- | -------- | ------------------------- | --- | --------- | ------- | ------- | --------- | -------------- | ------ |
|                                         |         |              |             |         |       |          | isthetotalnumberofcases,T |     |           |         |         | andQ      |                |        |
|                                         |         |              |             |         |       | whereC   |                           |     |           |         | i       |           | j denotetheith |        |
| Dataset                                 | 1 (D1), | derived from | CloudWise’s | Generic | AIOps |          |                           |     |           |         |         |           |                |        |
|                                         |         |              |             |         |       | class of | the ground                |     | truth and | the jth | cluster | generated |                | by the |
Atlas(GAIA)1,servesasabenchmarkformicroservicefailure
diagnosis [19], [52], [53], [54]. GAIA data, primarily from clusteringalgorithm,respectively.
|             |         |            |         |             |      | ACC       | elucidates   | the | correspondence |        | between        |     | clustering | re-    |
| ----------- | ------- | ---------- | ------- | ----------- | ---- | --------- | ------------ | --- | -------------- | ------ | -------------- | --- | ---------- | ------ |
| CloudWise’s | MicroSS | simulation | system, | encompasses | com- |           |              |     |                |        |                |     |            |        |
|             |         |            |         |             |      | sults and | ground-truth |     | class          | labels | by quantifying |     | the        | degree |
prehensivemonitoringdataandsimulatedfailures.Wetestfour
towhicheachclusterencompassesdatapointsbelongingtothe
typesoffailures:“Memoryresourceunderprovisioning”,“Sys-
respectiveground-truthclass.ACCcanbecalculatedasfollows:
temcomponentdamage”,“Filesystemmisconfigurations”,and
“Accesscontrolerrors”.
(cid:4)C
1
Dataset2(D2)originatesfromasimulatede-commerceap- ACC(x,xˆ)= δ(xc =xˆc), (7)
C
plicationutilizingmicroservices.Itincludesavarietyofrealfail- c=1
| ure injections | to  | replicate e-commerce |     | operational | challenges. |     |     |     |     |     |     |     |     |     |
| -------------- | --- | -------------------- | --- | ----------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
wherexandxˆdenotetheactualclasslabelsoftheresultsandthe
Thisdatasetencompassesdynamicservicetopologies,real-time
|     |     |     |     |     |     | labelsthatmatchthegroundtruthbest,respectively.δ |     |     |     |     |     |     |     | denotes |
| --- | --- | --- | --- | --- | --- | ------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | ------- |
traces,metrics,andlogs.Wetestfivetypesoffailures:“CPUre-
theKroneckerdelta.
sourceunderprovisioning”,“Memoryresourceunderprovision-
| ing”, “Disk | resource | underprovisioning”, |     | “System | component |                            |     |     |     |     |     |     |     |     |
| ----------- | -------- | ------------------- | --- | ------- | --------- | -------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
|             |          |                     |     |         |           | B. OverallPerformance(RQ1) |     |     |     |     |     |     |     |     |
damage”,and“Containerresourcequotaviolations”.
Implementation:UniDiagisimplementedinPyTorch,andall Table III presents the number of labeled samples (failures
of the experiments are conducted on a Linux Server with 64 needing labeling) and the overall performance comparison on
16C32T Intel(R) Xeon(R) Gold 5218 CPU @ 2.30GHz, two thetwodatasets.Thequantityoflabeleddataforeachbaseline
NVIDIA(R) Tesla(R) V100S, and 187.5 GB RAM. As for the istailoredtoitsspecificrequirements.Weempiricallydetermine
hyperparameters, the number of layers and the hidden size in the optimal number of labeled samples for methods without
R-GCN are 2 and 50, respectively. The dimension of graph explicitlabelingneedsbyconductingmultipleexperimentswith
embeddingis100. varying labeled sample numbers, selecting the best configura-
tion.Notably,thelabeledsamplesareonlyasubsetofthetraining
1https://github.com/CloudWise-OpenSource/GAIA-DataSet data, while larger datasets are used for training and testing to
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on November 13,2025 at 00:49:19 UTC from IEEE Xplore.  Restrictions apply.

ZHANGetal.:NOMOREDATASILOS:UNIFIEDMICROSERVICEFAILUREDIAGNOSISWITHTEMPORALKNOWLEDGEGRAPH 4021
TABLEIII
EFFECTIVENESSANDEFFICIENCYOFFAILUREDIAGNOSIS
ensure comprehensive learning and robust evaluation. A key asthemicroservicearchitectureevolvesanddevelops,newtypes
distinctionisthatMEPFL[14]labelsanomaloustraces,unlike offailures,thatis,undiscoveredtypesoffailuresthathavenever
othermethodsthatlabelfailurecases.TableIIIdetailsthenum- occurredoroccurredlessfrequentlyinthepast,oftenmanifest
beroftracesneedinglabelingforMEPFL.UniDiagoutperforms withinthemicroservicesystems.
allbaselinesonbothdatasets,achievinganimpressiveWeighted To evaluate UniDiag’s robustness in diagnosing new failure
AverageF1-scoreof0.869and0.723,respectively. types, we select distinct failure types from diverse datasets
iSQUAD [8] diagnoses failures using ground truths from and excluded associated samples from the training set. Given
similar failures but lacks historical failure integration, risking thatsupervisedmethodscannotdiagnosenewfailuretypesand
errorsfromnoiseandfluctuations.DéjàVu[10]trainsamodel MicroCBR can only match new cases with existing types, we
withhistoricalfailuresandFailureDependencyGraphs(FDGs), usediSQUADandLogClusterasbaselines.AslistedinTableIV,
requiringmanylabeledcases.Bothmethodsrelyonmetricdata, byaveragingtheresultsofeachnewfailuretypediagnosisonthe
lackingcomprehensivefeatures,resultinginpoorperformance. same dataset, we calculate the precision, recall, and F1-score.
LogCluster [11] struggles to parse log entries into meaningful UniDiagsignificantlyoutperformstheothermethods.iSQUAD
events, missing semantic information. Cloud19 [12] fails to andLogCluster,limitedtosingle-modaldata,failtodetectsome
address polysemy and uses a limited context window, missing failures,resultinginnumerousfalsepositivesandnegatives.In
broadercontextualinformationandleadingtosuboptimalper- contrast,UniDiag’sfusionofthreemodalitiesofmonitoringdata
formance. captures unique features from each modality, leading to com-
MEPFL[14]usesasupervisedlearningmodelthroughtraces, prehensive representation learning for each failure type. This
relyingonlabelingallanomaloustracepatterns. demonstrates that multimodal data fusion enhances UniDiag’s
| CloudRCA | [20] | combines | logs | and metrics | but | ignores | the | performance. |     |     |     |     |     |
| -------- | ---- | -------- | ---- | ----------- | --- | ------- | --- | ------------ | --- | --- | --- | --- | --- |
microservicesystem’stopology,missingcrucialfeatures.Italso
| requires many | labeled | historical |     | failure cases, | and | insufficient |     |     |     |     |     |     |     |
| ------------- | ------- | ---------- | --- | -------------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- |
C. ContributionofKeyComponents(RQ2)
| training samples |     | harm its | performance. | In  | contrast, | UniDiag |     |     |     |     |     |     |     |
| ---------------- | --- | -------- | ------------ | --- | --------- | ------- | --- | --- | --- | --- | --- | --- | --- |
excels in failure diagnosis, achieving a significantly higher ToshowtheeffectivenessofUniDiag’skeytechniques(i.e.,,
|     |     |     |     |     |     |     |     | entity embedding, | graph embedding, | and | clustering), |     | we creat |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | ---------------- | --- | ------------ | --- | -------- |
WeightedAverageF1-scorethanexistingmethods.
fivevariants(C1-C5)bysubstitutingthesetechniqueswithcom-
UniDiagdemonstratessuperiorperformanceinfailurediag-
nosis compared to MicroCBR [34] and DiagFusion [19] by mon or state-of-the-art alternatives: (1) C1 uses RE-NET [58]
|             |      |        |             |       |         |           |     | instead of MOGE | for learning | entity | embedding. | (2) | C2 uses |
| ----------- | ---- | ------ | ----------- | ----- | ------- | --------- | --- | --------------- | ------------ | ------ | ---------- | --- | ------- |
| integrating | both | normal | and failure | data, | thereby | capturing | a   |                 |              |        |            |     |         |
holisticviewofthesystemstateandmitigatinginformationloss. TANGO[59]insteadofMOGEforlearningentityembedding.
(3)C3usesmeanpoolinginsteadofMOGEforlearninggraph
UnlikeMicroCBR,whichisconstrainedbyitsrelianceonfailure
embedding.(4)C4usesDBSCANinsteadofHAC.(5)C5uses
dataalone,andDiagFusion,whichdependsheavilyonlabeled
historicalcases,UniDiagemploysTKGandMOGEtoprovide K-meansinsteadofHAC.
TableVdemonstratesthatUniDiagoutperformsallvariants
| a comprehensive |     | temporal | representation |     | of the | microservice |     |     |     |     |     |     |     |
| --------------- | --- | -------- | -------------- | --- | ------ | ------------ | --- | --- | --- | --- | --- | --- | --- |
system’sstate,effectivelymodelingcomplexdependenciesand ontwodatasets,underscoringthesignificanceofeachcompo-
| interactions. |            |       |         |           |          |     |       | nent.SubstitutingMOGEwithRE-NET(C1)orTANGO(C2) |              |          |     |                 |     |
| ------------- | ---------- | ----- | ------- | --------- | -------- | --- | ----- | ---------------------------------------------- | ------------ | -------- | --- | --------------- | --- |
|               |            |       |         |           |          |     |       | results in decreased                           | performance. | RE-NET’s |     | use of subgraph |     |
| RT and        | invocation | paths | reflect | anomalous | patterns | in  | trace |                                                |              |          |     |                 |     |
data,whileECandQCarekeyfordetectingreliabilityandtraffic aggregatorsandGRUsneglectsthestructuraldependenciesand
|                    |     |      |         |             |            |     |     | static attributes | in TKGs, leading | to the | potential | loss | or mix- |
| ------------------ | --- | ---- | ------- | ----------- | ---------- | --- | --- | ----------------- | ---------------- | ------ | --------- | ---- | ------- |
| failures. MicroCBR |     | uses | only RT | for anomaly | detection, |     | and |                   |                  |        |           |      |         |
DiagFusion uses RT and EC, potentially leading to inaccurate ing of historical facts. TANGO’s Neural Ordinary Differential
diagnoses.Incontrast,UniDiagusesinvocationpaths,RT,EC, Equations (NODE) [60] are better suited for continuous time
domainsandfailtocapturepatternsinthediscretesnapshotsof
| and QC to | construct | a   | knowledge | graph, | incorporating |     | rich |     |     |     |     |     |     |
| --------- | --------- | --- | --------- | ------ | ------------- | --- | ---- | --- | --- | --- | --- | --- | --- |
informationformoreaccuratefailurediagnosis. TKGsamidstfrequentmicroservicechanges.
|     |     |     |     |     |     |     |     | Replacing | MOGE with | mean pooling | (C3) | degrades | per- |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | --------- | ------------ | ---- | -------- | ---- |
Frequentfailurescenariosinhistoricaldatacanbeswiftlyand
accuratelyidentifiedthroughobservationandpractice.However, formance as traditional pooling methods (e.g., mean pooling)
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on November 13,2025 at 00:49:19 UTC from IEEE Xplore.  Restrictions apply.

4022 IEEETRANSACTIONSONSERVICESCOMPUTING,VOL.17,NO.6,NOVEMBER/DECEMBER2024
TABLEIV
EFFECTIVENESSOFTHEMODELSDEALINGWITHNEWTYPESOFFAILURES
TABLEV differently.TracescontributetheleastinD1andD2,asindicated
EXPERIMENTALRESULTSOFABLATIONSTUDY bytheminorperformancedropinUniDiagw/oT,duetolimited
tracerecordsandfluctuatingRTandQC.Conversely,UniDiag
|     |     |     |     |     |     | w/o M | shows significant |     | performance |     | degradation, | aligning |     |
| --- | --- | --- | --- | --- | --- | ----- | ----------------- | --- | ----------- | --- | ------------ | -------- | --- |
withobservationsinTableI.
|     |     |     |     |     |     | In conclusion,  |     | integrating | all            | three | data modalities |     | signifi- |
| --- | --- | --- | --- | --- | --- | --------------- | --- | ----------- | -------------- | ----- | --------------- | --- | -------- |
|     |     |     |     |     |     | cantly enhances |     | UniDiag’s   | effectiveness, |       | highlighting    | the | cru-     |
cialroleofdiversedatainimprovingfailurediagnosis.
E. ComputationalEfficiency(RQ4)
TableIIIcomparestherunningtimesofUniDiagwithother
baselinemethods,coveringbothofflinetrainingandonlinedi-
agnosisdurations.Notably,UniDiagachievesanaverageonline
|     |     |     |     |     |     | diagnosis  | time of         | 0.6s, meeting |           | real-time | diagnostic | demands, |          |
| --- | --- | --- | --- | --- | --- | ---------- | --------------- | ------------- | --------- | --------- | ---------- | -------- | -------- |
|     |     |     |     |     |     | given that | data collection |               | intervals | for       | D1 and     | D2 are   | at least |
TABLEVI
CONTRIBUTIONSOFDIVERSEDATASOURCES 30s.However,UniDiaghaslongerofflinetrainingtimesdueto
|     |     |     |     |     |     | the entity | embedding | process, |     | which is | influenced | by the | size |
| --- | --- | --- | --- | --- | --- | ---------- | --------- | -------- | --- | -------- | ---------- | ------ | ---- |
andcomplexityoftheKGandtheGCN.Despitethis,UniDiag
minimizestheneedforfrequentretraining.
TotestUniDiag’sefficiencyonlargerdatasets,weconstructed
|     |     |     |     |     |     | a KG with        | 2,553         | entities | and         | 3,807,420  | edges          | by replicating |     |
| --- | --- | --- | --- | --- | --- | ---------------- | ------------- | -------- | ----------- | ---------- | -------------- | -------------- | --- |
|     |     |     |     |     |     | nodes and        | attributes    | from     | D1.         | UniDiag    | achieved       | an average     |     |
|     |     |     |     |     |     | offline training | time          | of       | 5.12h and   | an average | online         | diagnosis      |     |
|     |     |     |     |     |     | time of 4.73s,   | demonstrating |          | suitability |            | for real-world | deploy-        |     |
|     |     |     |     |     |     | ment. These      | results       | confirm  | UniDiag’s   |            | robust         | performance    | on  |
large-scaledatasets.
cannoteffectivelycharacterizefeatures.SOPOOL,bymodeling
general graph information correlations, captures long-distance F. EffectofHyperparameters(RQ5)
featureinformationmoreeffectively.
|     |     |     |     |     |     | We discuss | the | impact | of UniDiag’s |     | three hyperparameters |     |     |
| --- | --- | --- | --- | --- | --- | ---------- | --- | ------ | ------------ | --- | --------------------- | --- | --- |
SubstitutingHACwithDBSCANorK-means(C4&C5)also
|         |              |        |                  |         |        | and different | training | set | sizes. | Fig. 4 | shows how | NMI, | ACC, |
| ------- | ------------ | ------ | ---------------- | ------- | ------ | ------------- | -------- | --- | ------ | ------ | --------- | ---- | ---- |
| reduces | performance. | HAC is | robust to random | initial | values |               |          |     |        |        |           |      |      |
andWeightedAverageF1-scorevarywiththeseparameters.
| and can | identify | outliers in KGs. | DBSCAN, | a density-based |     |     |     |     |     |     |     |     |     |
| ------- | -------- | ---------------- | ------- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
TheNumberofLayersinEntityEmbedding:UniDiag’sper-
method,isinsensitivetonoiseandoutliers,makingitunsuitable
formancedeclinesasthenumberofGCNlayersincreasesfrom1
forfailuredetection.K-meansstruggleswithnon-sphericaland
to5,withoptimalresultsachievedat2or3layers.Anexcessive
| varied-sized | clusters, | and the | choice of initial | cluster | centers |        |           |        |      |                 |     |             |     |
| ------------ | --------- | ------- | ----------------- | ------- | ------- | ------ | --------- | ------ | ---- | --------------- | --- | ----------- | --- |
|              |           |         |                   |         |         | number | of layers | causes | node | representations |     | to converge | and |
significantlyaffectstheresults.
losedistinction.
|     |     |     |     |     |     | Graph | Embedding | Dimension: |     | Optimal | performance |     | is ob- |
| --- | --- | --- | --- | --- | --- | ----- | --------- | ---------- | --- | ------- | ----------- | --- | ------ |
D. ContributionofEachModality(RQ3)
servedatagraphembeddingdimensionof100.Largerdimen-
Weconductablationexperimentstoexaminethecontributions sions risk sparsity, over-fitting, and increased computational
of different data sources by creating the following variants: complexity,buttheymaybesuitableforcomplexmicroservice
| (1)UniDiagw/oMdropsmetricswhileinputslogsandtraces. |     |     |     |     |     | systems. |     |     |     |     |     |     |     |
| --------------------------------------------------- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
L
(2) UniDiagw/o drops logs while inputs metrics and traces. The Number of Clusters: Increasing the number of clusters
(3)UniDiagw/oT dropstraceswhileinputsmetricsandlogs. enhances the utilization of training data; however, too many
Table VI indicates that UniDiag’s effectiveness depends on clusters raise the labeling effort. We select 15 and 20 clusters
the integration of all data modalities, with each contributing forD1andD2,respectively.
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on November 13,2025 at 00:49:19 UTC from IEEE Xplore.  Restrictions apply.

ZHANGetal.:NOMOREDATASILOS:UNIFIEDMICROSERVICEFAILUREDIAGNOSISWITHTEMPORALKNOWLEDGEGRAPH 4023
Fig.4. HyperparameterssensitivityonUniDiag.
The Size of the Training Set: We evaluated UniDiag with experimentaltestsanditerativelyoptimizedtheapproach.The
trainingsetsizesof30%,40%,50%,60%,and70%,usingthe resultspresentedareaveragesofmultipletrials.
remaining 30% for testing. Fig. 4 demonstrates that UniDiag Externally, there are two primary threats. First, the lim-
achievesahighWeightedAverageF1-scoreevenwithalimited itedscaleofourdatasetscomparedtoreal-worldmicroservice
numberoffailurecases,provingitseffectivenessinreal-world systems in production environments restricts generalizability.
scenarioswithconstrainedhistoricaldata. These datasets might not fully represent all microservice sys-
|     |     |     |     |     |     |     | tems. Nevertheless, | we  | believe | our | approach | is sufficiently |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------- | --- | ------- | --- | -------- | --------------- | --- |
general.Weplantocollaboratewithatop-tierInternetservice
VII. DISCUSSION
|     |     |     |     |     |     |     | provider to | deploy UniDiag |     | and validate | its | effectiveness | in  |
| --- | --- | --- | --- | --- | --- | --- | ----------- | -------------- | --- | ------------ | --- | ------------- | --- |
A. LessonsLearned real-world scenarios. Second, our datasets may not capture
|         |            |              |     |            |      |           | all failure types | compared | to  | industry-collected |     | data. | Future |
| ------- | ---------- | ------------ | --- | ---------- | ---- | --------- | ----------------- | -------- | --- | ------------------ | --- | ----- | ------ |
| 1) Data | Collection | Granularity: |     | Currently, | most | IT enter- |                   |          |     |                    |     |       |        |
prises collect data at minute-level granularity, typically every work will involve evaluating our approach on a broader range
|                |     |             |      |             |           |          | of microservice | systems, | incorporating |     | larger-scale | real-world |     |
| -------------- | --- | ----------- | ---- | ----------- | --------- | -------- | --------------- | -------- | ------------- | --- | ------------ | ---------- | --- |
| 1 or 5 minutes |     | [61], [62]. | This | granularity | generally | does not |                 |          |               |     |              |            |     |
significantlyimpactthemodel’seffectiveness.Inourapproach, caseswithdiversefailuretypestoaddressthislimitation.
oncethemetricgranularityisset,logsandtracesmustbealigned
| withthemetrics.   |     |         |              |     |          |            | C. Limitations |               |              |     |     |                |     |
| ----------------- | --- | ------- | ------------ | --- | -------- | ---------- | -------------- | ------------- | ------------ | --- | --- | -------------- | --- |
| 2) Effectiveness: |     | UniDiag | demonstrates |     | superior | effective- |                |               |              |     |     |                |     |
|                   |     |         |              |     |          |            | Based on       | the conducted | experiments, |     | we  | draw attention | to  |
ness in failure diagnosis by integrating comprehensive multi- twoprimarylimitationsofUniDiag,asfollows:
| modal data | and | leveraging | TKGs | to capture | the | full system |     |     |     |     |     |     |     |
| ---------- | --- | ---------- | ---- | ---------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
1) WhileUniDiagisdesignedtoleveragemetrics,logs,and
stateovertime.Unlikeothermethodsthatrelyonlimiteddata tracesforcomprehensivefailurediagnosis,itremainsro-
sources,insufficientlabeleddata,orsimplisticmodels,UniDiag
bustevenwhendatafromsomemodalitiesareunavailable.
incorporatesabroaderrangeoffeatures,whichensuresaccurate
|     |     |     |     |     |     |     | This is | crucial since | acquiring |     | synchronized | multimodal |     |
| --- | --- | --- | --- | --- | --- | --- | ------- | ------------- | --------- | --- | ------------ | ---------- | --- |
diagnosisinmicroservicesystems. data can be challenging in certain microservice deploy-
| 3) Flexibility: |     | UniDiag’sflexibilityisdrivenbyitsdynamic |     |     |     |     |     |     |     |     |     |     |     |
| --------------- | --- | ---------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ments.AlthoughUniDiagcanfunctionwithmissingdata
| TKG updates | and | incremental |     | learning. | The system | continu- |         |            |                 |     |         |           |     |
| ----------- | --- | ----------- | --- | --------- | ---------- | -------- | ------- | ---------- | --------------- | --- | ------- | --------- | --- |
|             |     |             |     |           |            |          | sources | due to its | loosely-coupled |     | nature, | providing | all |
ously adapts to new data, integrating evolving failure patterns datatypesmaximizesitseffectiveness.Open-sourcetoolk-
andarchitecturalchangeswithoutrequiringfullretraining,en-
|     |     |     |     |     |     |     | its such | as cAdvisor | [63] | for | metrics, | Elasticsearch | [64] |
| --- | --- | --- | --- | --- | --- | --- | -------- | ----------- | ---- | --- | -------- | ------------- | ---- |
suring it remains effective in diagnosing emerging failures as forlogs,andJaeger[65]fortracingfacilitatemonitoring
theenvironmentevolves.
datacollectioninmicroservicesystems.Thesetoolssim-
| 4) Scalability: |     | UniDiagexhibitsahighdegreeofadaptabil- |     |     |     |     |       |           |               |     |                    |     |      |
| --------------- | --- | -------------------------------------- | --- | --- | --- | --- | ----- | --------- | ------------- | --- | ------------------ | --- | ---- |
|                 |     |                                        |     |     |     |     | plify | equipping | microservices |     | with comprehensive |     | data |
itytothedynamicnatureofmicroservicearchitectures.Asmi- collectioncapabilities[18].
croserviceinstancesarecreatedordestroyed,UniDiagrequires
2) UniDiagreliesonadata-drivenapproach.Ifspecificfail-
only the addition or removal of the corresponding entities and uresdonotmanifestanomaliesinthecollecteddata,accu-
relationswithintheTKG.TheworkflowofUniDiagisinherently
ratediagnosisbecomeschallenging.Thisissueiscommon
generalanddoesnotrelyonanyspecificdatamodality,thereby
andalsorecognizedinMEPFL[14]andSCWarn[16].
| maintaining | its       | effectiveness | even | in production |                  | environments |     |       |            |     |     |     |     |
| ----------- | --------- | ------------- | ---- | ------------- | ---------------- | ------------ | --- | ----- | ---------- | --- | --- | --- | --- |
| where not   | all three | modalities    | of   | data          | are concurrently | moni-        |     |       |            |     |     |     |     |
|             |           |               |      |               |                  |              |     | VIII. | CONCLUSION |     |     |     |     |
tored.
Recognizingthelimitationsofrelyingsolelyonsingle-modal
data,whichmayfailtocaptureasubstantialamountofcrucial
B. ThreatstoValidity
information,wepresentUniDiagasanovelapproachforfailure
Regardinginternalvaliditythreats,theprimaryconcernisthe diagnosis. UniDiag fuses multimodal data, including metrics,
implementationprocess.Toaddressthis,weconductedrepeated logs, and traces, using TKG. It includes a three-step process:
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on November 13,2025 at 00:49:19 UTC from IEEE Xplore.  Restrictions apply.

4024 IEEETRANSACTIONSONSERVICESCOMPUTING,VOL.17,NO.6,NOVEMBER/DECEMBER2024
(1)effectivefusionofmetrics,logs,andtracesthroughTKGs, [17] S. He, P. He, Z. Chen, T. Yang, Y. Su, and M. R. Lyu, “A survey on
(2) utilization of MOGE for entity embedding and graph em- automatedloganalysisforreliabilityengineering,”ACMComput.Surv.,
vol.54,no.6,pp.1–37,2021.
bedding,and(3)trainingofthefailurediagnosismodeltodetect
[18] C.Lee,T.Yang,Z.Chen,Y.Su,andM.R.Lyu,“Eadro:Anend-to-end
failuresandidentifyfailuretypesaccurately.Wehaveconducted troubleshooting framework for microservices on multi-source data,” in
extensiveevaluationexperimentsontwodatasetstovalidatethe Proc.IEEE/ACM45thInt.Conf.Softw.Eng.,LosAlamitos,CA,2023,
pp.1750–1762.
efficacy,efficiency,andgeneralizationofUniDiag.Theempiri-
[19] S.Zhangetal.,“Robustfailurediagnosisofmicroservicesystemthrough
calfindingsaffirmtherobustnessandeffectivenessofUniDiag multimodaldata,”IEEETrans.Serv.Comput.,vol.16,no.6,pp.3851–
inachievingaccurateandefficientfailurediagnosis.Moreover, 3864,Nov./Dec.2023.
[20] Y.Zhangetal.,“CloudRCA:Arootcauseanalysisframeworkforcloud
to overcome the limitations of the data-driven approach, a
computingplatforms,”inProc.30thACMInt.Conf.Inf.Knowl.Manage.,
contextual analysis module could effectively analyze external NewYork,NY,2021,pp.4373–4382.
factors,suchasdeploymentchangesandsystemupdates,which [21] P.Dogga,K.Narasimhan,A.Sivaraman,S.Saini,G.Varghese,andR.Ne-
travali,“Revelio:ML-generateddebuggingqueriesforfindingrootcauses
mightprovideadditionalcluesaboutpotentialfailuresformore
indistributedsystems,”Proc.Mach.Learn.Syst.,vol.4,pp.601–622,
accuratefailurediagnosis. 2022.
[22] C.Dengetal.,“GAKG:Amultimodalgeoscienceacademicknowledge
graph,”inProc.30thACMInt.Conf.Inf.Knowl.Manage.,NewYork,NY,
REFERENCES 2021,pp.4445–4454.
[23] A.V.Kannanetal.,“Multimodalknowledgegraphfordeeplearningpapers
[1] T.Colanzietal.,“Arewespeakingtheindustrylanguage?Thepracticeand andcode,”inProc.29thACMInt.Conf.Inf.Knowl.Manage.,NewYork,
literatureofmodernizinglegacysystemswithmicroservices,”inProc.15th NY,2020,pp.3417–3420.
Braz.Symp.Softw.Compon.ArchitecturesReuse,NewYork,NY,2021, [24] X.Li,Y.Chen,andZ.Lin,“Towardsautomatedinter-serviceauthorization
pp.61–70. for microservice applications,” in Proc. ACM SIGCOMM 2019 Conf.
[2] X.Zhouetal.,“Faultanalysisanddebuggingofmicroservicesystems: PostersDemos,NewYork,NY,2019,pp.3–5.
Industrialsurvey,benchmarksystem,andempiricalstudy,”IEEETrans. [25] S. Chakraborty, S. Garg, S. Agarwal, A. Chauhan, and S. K. Saini,
Softw.Eng.,vol.47,no.2,pp.243–260,Feb.2021. “CausIL:Causalgraphforinstancelevelmicroservicedata,”inProc.ACM
[3] A.Mahimkar,C.E.deAndrade,R.Sinha,andG.Rana,“Acomposition WebConf.,NewYork,NY,2023,pp.2905–2915.
framework for change management,” in Proc. 2021 ACM SIGCOMM [26] R.Trivedi,H.Dai,Y.Wang,andL.Song,“Know-evolve:Deeptemporal
Conf.,NewYork,NY,2021,pp.788–806. reasoningfordynamicknowledgegraphs,”inProc.34thInt.Conf.Mach.
[4] J.Y.Chung,C.Joe-Wong,S.Ha,J.W.-K.Hong,andM.Chiang,“CYRUS: Learn.,NewYork,NY:PMLR,2017,pp.3462–3471.
Towardsclient-definedcloudstorage,”inProc.10thEur.Conf.Comput. [27] M. Schlichtkrull, T. N. Kipf, P. Bloem, R. v. d. Berg, I. Titov, and
Syst.,NewYork,NY,2015,pp.1–16. M. Welling, “Modeling relational data with graph convolutional net-
[5] J.Chenetal.,“Anempiricalinvestigationofincidenttriageforonline works,”inProc.Eur.SemanticWebConf.,Berlin:Springer-Verlag,2018,
servicesystems,”inProc.IEEE/ACM41stInt.Conf.Softw.Eng.:Softw. pp.593–607.
Eng.Pract.,LosAlamitos,CA,2019,pp.111–120. [28] K. Cho et al., “Learning phrase representations using RNN encoder-
[6] J.Chenetal.,“Continuousincidenttriageforlarge-scaleonlineservice decoderforstatisticalmachinetranslation,”inProc.Conf.Empir.Methods
systems,” in Proc. 34th IEEE/ACM Int. Conf. Autom. Softw. Eng., Los NaturalLang.Process.,Stroudsburg,PA:AssociationforComputational
Alamitos,CA,2019,pp.364–375. Linguistics,2014,pp.1724–1734.
[7] Y.Mengetal.,“Localizingfailurerootcausesinamicroservicethrough [29] Z.Wang andS. Ji, “Second-orderpoolingforgraphneuralnetworks,”
causalityinference,”inProc.IEEE/ACM28thInt.Symp.Qual.Serv.,Los IEEETrans.PatternAnal.Mach.Intell.,vol.45,no.6,pp.6870–6880,
Alamitos,CA,2020,pp.1–10. Jun.2023.
[8] M. Ma et al., “Diagnosing root causes of intermittent slow queries in [30] UniDiag,“Opensourcerepositoryofunidiag,”2024.[Online].Available:
clouddatabases,”Proc.VLDBEndowment,vol.13,no.8,pp.1176–1189, https://github.com/AIOps-Lab-NKU/UniDiag.git
2020. [31] P. Liu et al., “Unsupervised detection of microservice trace anoma-
[9] C. Wu et al., “Identifying root-cause metrics for incident diagnosis in lies through service-level deep Bayesian networks,” in Proc. IEEE
onlineservicesystems,”inProc.IEEE32ndInt.Symp.Softw.Rel.Eng., 31st Int. Symp. Softw. Rel. Eng., Los Alamitos, CA, 2020,
LosAlamitos,CA,2021,pp.91–102. pp.48–58.
[10] Z. Li et al., “Actionable and interpretable fault localization for recur- [32] D.Liuetal.,“MicroHECL:High-efficientrootcauselocalizationinlarge-
ring failures in online service systems,” in Proc. 30th ACM Joint Eur. scalemicroservicesystems,”inProc.IEEE/ACM43rdInt.Conf.Softw.
Softw. Eng. Conf. Symp. Found. Softw. Eng., New York, NY, 2022, Eng.:Softw.Eng.Pract.,LosAlamitos,CA,2021,pp.338–347.
pp.996–1008. [33] Z.Lietal.,“Practicalrootcauselocalizationformicroservicesystems
[11] Q. Lin, H. Zhang, J.-G. Lou, Y. Zhang, and X. Chen, “Log cluster- viatraceanalysis,”inProc.IEEE/ACM29thInt.Symp.Qual.Serv.,Los
ing based problem identification for online service systems,” in Proc. Alamitos,CA,2021,pp.1–10.
IEEE/ACM38thInt.Conf.Softw.Eng.Companion,LosAlamitos,CA, [34] F.Liuetal.,“MicroCBR:Case-basedreasoningonspatio-temporalfault
2016,pp.102–111. knowledgegraphformicroservicestroubleshooting,”inProc.Int.Conf.
[12] Y.Yuan,W.Shi,B.Liang,andB.Qin,“Anapproachtocloudexecution Case-BasedReasoning,Berlin:Springer-Verlag,2022,pp.224–239.
failurediagnosisbasedonexceptionlogsinOpenStack,”inProc.IEEE [35] J.Wang,Y.Li,Q.Qi,Y.Lu,andB.Wu,“Multilayeredfaultdetection
12thInt.Conf.CloudComput.,LosAlamitos,CA,2019,pp.124–131. andlocalizationwithtransformerformicroservicesystems,”IEEETrans.
[13] X. Zhang et al., “Onion: Identifying incident-indicating logs for cloud Rel.,vol.73,no.3,pp.1502–1515,Sep.2024.
systems,”inProc.29thACMJointMeetingEur.Softw.Eng.Conf.Symp. [36] Z.Zhu,C.Lee,X.Tang,andP.He,“HeMiRCA:Fine-grainedrootcause
Found.Softw.Eng.,NewYork,NY,2021,pp.1253–1263. analysisformicroserviceswithheterogeneousdatasources,”ACMTrans.
[14] X.Zhouetal.,“Latenterrorpredictionandfaultlocalizationformicroser- Softw.Eng.Methodol.,Jul.2024,doi:10.1145/3674726.
viceapplicationsbylearningfromsystemtracelogs,”inProc.27thACM [37] L.Zheng,Z.Chen,J.He,andH.Chen,“MULAN:Multi-modalcausal
JointMeetingEur.Softw.Eng.Conf.Symp.Found.Softw.Eng.,NewYork, structurelearningandrootcauseanalysisformicroservicesystems,”in
NY,2019,pp.683–694. Proc.ACMWebConf.,NewYork,NY,USA,2024,pp.4107–4116.
[15] C.Lee,T.Yang,Z.Chen,Y.Su,Y.Yang,andM.R.Lyu,“Heterogeneous [38] A.Workshop,“2022CCFAiOpschallenge,”2022.[Online].Available:
anomalydetectionforsoftwaresystemsviasemi-supervisedcross-modal https://workshop.aiops.org
attention,”inProc.IEEE/ACM45thInt.Conf.Softw.Eng.,LosAlamitos, [39] P.He,J.Zhu,Z.Zheng,andM.R.Lyu,“Drain:Anonlinelogparsing
CA,2023,pp.1724–1736. approachwithfixeddepthtree,”inProc.2017IEEEInt.Conf.WebServ.,
[16] N.Zhaoetal.,“Identifyingbadsoftwarechangesviamultimodalanomaly LosAlamitos,CA,2017,pp.33–40.
detectionforonlineservicesystems,”inProc.29thACMJointMeeting [40] S. Zhang et al., “Syslog processing for switch failure diagnosis and
Eur.Softw.Eng.Conf.Symp.Found.Softw.Eng.,NewYork,NY,2021, predictionindatacenternetworks,”inProc.IEEE/ACM25thInt.Symp.
pp.527–539. Qual.Serv.,LosAlamitos,CA,2017,pp.1–10.
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on November 13,2025 at 00:49:19 UTC from IEEE Xplore. Restrictions apply.

ZHANGetal.:NOMOREDATASILOS:UNIFIEDMICROSERVICEFAILUREDIAGNOSISWITHTEMPORALKNOWLEDGEGRAPH 4025
[41] J.Kulkarni,S.Joshi,S.Bapat,andK.Jambhali,“Analysisofsystemlogs Shenglin Zhang (Member, IEEE) received the BS
forpatterndetectionandanomalyprediction,”inProc.Int.Conf.Comput. degree in network engineering from the School of
Sci.Appl.,Berlin:Springer-Verlag,2020,pp.427–436. ComputerScienceandTechnology,XidianUniver-
[42] B.H.Sigelmanetal.,“Dapper,Alarge-scaledistributedsystemstracing sity,Xi’an,China,in2012,andthePhDdegreein
infrastructure,”Google,Inc.,Tech.Rep.,2010. computersciencefromtheDepartmentofComputer
[43] Z.Chenetal.,“Adaptiveperformanceanomalydetectionforonlineservice ScienceandTechnology,TsinghuaUniversity,Bei-
systemsviapatternsketching,”inProc.44thInt.Conf.Softw.Eng.,New jing, China, in 2017. He is currently an associate
York,NY,2022,pp.61–72. professorwiththeCollegeofSoftware,NankaiUni-
[44] S. Kim, S. An, P. Chikontwe, and S. H. Park, “Bidirectional versity,Tianjin,China.Hiscurrentresearchinterests
RNN-based few shot learning for 3D medical image segmenta- include failure detection, diagnosis, and prediction
tion,” in Proc. AAAI Conf. Artif. Intell., Palo Alto, CA:AAAI, 2021, forservicemanagement.
pp.1808–1816.
[45] M.S.Murshed,C.Murphy,D.Hou,N.Khan,G.Ananthanarayanan,andF.
Hussain,“Machinelearningatthenetworkedge:Asurvey,”ACMComput.
Surv.,vol.54,no.8,pp.1–37,2021. YongxinZhaoreceivedtheBSandMSdegreesin
[46] S. Hochreiter and J. Schmidhuber, “Longshort-term memory,” Neural softwareengineeringfromtheCollegeofSoftware,
Comput.,vol.9,no.8,pp.1735–1780,1997. NankaiUniversity,Tianjin,China,in2021and2024,
[47] J.Chung,C.Gulcehre,K.Cho,andY.Bengio,“Empiricalevaluationof respectively.SheiscurrentlyworkingtowardthePhD
gatedrecurrentneuralnetworksonsequencemodeling,”inProc.Neural degreewiththeCollegeofSoftware,NankaiUniver-
Inf.Process.Syst.WorkshopDeepLearn.,2014. sity.Herresearchinterestsincludefailuredetection
[48] N. Zhao et al., “An empirical investigation of practical log anomaly andfailurediagnosis.
detectionforonlineservicesystems,”inProc.29thACMJointMeeting
Eur.Softw.Eng.Conf.Symp.Found.Softw.Eng.,NewYork,NY,2021,
pp.1404–1415.
[49] Y.Wangetal.,“Fastoutageanalysisoflarge-scaleproductioncloudswith
servicecorrelationmining,”inProc.IEEE/ACM43rdInt.Conf.Softw.
Eng.,LosAlamitos,CA,2021,pp.885–896.
SiboXiareceivedtheBSdegreeinsoftwareengineer-
[50] Y.Sunetal.,“EfficientandrobustKPIoutlierdetectionforlarge-scale
ingfromtheCollegeofSoftware,NankaiUniversity,
datacenters,” IEEE Trans. Comput., vol. 72, no. 10, pp. 2858–2871,
Tianjin, China, in 2022. He is currently working
Oct.2023.
toward the PhD degree with the College of Soft-
[51] Y.Fu,M.Yan,Z.Xu,X.Xia,X.Zhang,andD.Yang,“Anempiricalstudy
ware, Nankai University. His research interests in-
oftheimpactoflogparsersontheperformanceoflog-basedanomaly
cludeanomalydetectionandfailurediagnosis.
detection,”Empir.Softw.Eng.,vol.28,no.1,2023,Art.no.6.
[52] Y. Sui et al., “LogKG: Log failure diagnosis through knowledge
graph,” IEEE Trans. Serv. Comput., vol. 16, no. 5, pp. 3493–3507,
Sep./Oct.2023.
[53] S.Zhangetal.,“Efficientandrobusttraceanomalydetectionforlarge-scale
microservicesystems,”inProc.IEEE34thInt.Symp.Softw.Rel.Eng.,Los
Alamitos,CA,2023,pp.69–79. ShiruiWeireceivedtheBSdegreeinsoftwareengi-
[54] C. Zhao et al., “Robust multimodal failure detection for microservice neeringfromtheCollegeofSoftware,NankaiUniver-
systems,”inProc.29thACMSIGKDDConf.Knowl.Discov.DataMining, sity,Tianjin,China,in2023.Sheiscurrentlyworking
NewYork,NY,2023,pp.5639–5649. toward the master’s degree with the National As-
[55] B.M.Sundheim,“Overviewofthefourthmessageunderstandingevalu- tronomicalObservatories,ChineseAcademyofSci-
ationandconference,”NavalCommandControlandOceanSurveillance ences,Beijing,China.Herresearchinterestsinclude
CenterRDTandEDIV,SanDiegoCA,USA,Tech.Rep.,1992. astroinformaticsandvirtualobservatories.
[56] L.Danon,A.Diaz-Guilera,J.Duch,andA.Arenas,“Comparingcommu-
nitystructureidentification,”J.Stat.Mechanics:TheoryExp.,vol.2005,
no.09,2005,Art.no.P09008.
[57] N.Zhao,L.Zhang,B.Du,Q.Zhang,J.You,andD.Tao,“Robustdual
clustering with adaptive manifold regularization,” IEEE Trans. Knowl.
DataEng.,vol.29,no.11,pp.2498–2509,Nov.2017. YongqianSun(Member,IEEE)receivedtheBSde-
[58] W.Jin,M.Qu,X.Jin,andX.Ren,“Recurrenteventnetwork:Autore-
greeinstatisticalspecialtyfromNorthwesternPoly-
gressive structure inferenceover temporal knowledge graphs,” in Proc. technicalUniversity,Xi’an,China,in2012,andthe
2020 Conf. Empir. Methods Natural Lang. Process., Stroudsburg, PA: PhD degree in computer science from the Depart-
AssociationforComputationalLinguistics,2020,pp.6669–6683. mentofComputerScienceandTechnology,Tsinghua
[59] Z.Han,Z.Ding,Y.Ma,Y.Gu,andV.Tresp,“Learningneuralordinary University,Beijing,China,in2018.Heiscurrently
equationsforforecastingfuturelinksontemporalknowledgegraphs,”in anassociateprofessorwiththeCollegeofSoftware,
Proc.2021Conf.Empir.MethodsNaturalLang.Process.,Stroudsburg,
NankaiUniversity,Tianjin,China.Hisresearchinter-
PA:AssociationforComputationalLinguistics,2021,pp.8352–8364. estsincludeanomalydetectionandrootcauselocal-
[60] R.Dasetal.,“Goforawalkandarriveattheanswer:Reasoningover izationinservicemanagement.
pathsinknowledgebasesusingreinforcementlearning,”inProc.Int.Conf.
Learn.Representations,2018,pp.1–18.
[61] Z.Li,Y.Zhao,R.Liu,andD.Pei,“RobustandrapidclusteringofKPIs
forlarge-scaleanomalydetection,”inProc.IEEE/ACM26thInt.Symp.
ChenyuZhaoreceivedtheBSandMSdegreesin
Qual.Serv.,LosAlamitos,CA,2018,pp.1–10.
softwareengineeringfromtheCollegeofSoftware,
[62] Z. Li, W. Chen, and D. Pei, “Robust and unsupervised KPI anomaly
NankaiUniversity,Tianjin,China,in2020and2023,
detectionbasedonconditionalvariationalautoencoder,”inProc.IEEE
respectively. Her research interests are focused on
37th Int. Perform. Comput. Commun. Conf., Los Alamitos, CA, 2018,
anomalydetectionandrootcauseanalysis.
pp.1–9.
[63] Google, “Container advisor,” 2024. [Online]. Available: https://github.
com/google/cadvisor
[64] Elastic,“Elasticsearch,”2024.[Online].Available:https://www.elastic.co/
[65] C.N.C.Foundation,“Jaeger,”2024.[Online].Available:https://www.
jaegertracing.io/
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on November 13,2025 at 00:49:19 UTC from IEEE Xplore. Restrictions apply.

4026 IEEETRANSACTIONSONSERVICESCOMPUTING,VOL.17,NO.6,NOVEMBER/DECEMBER2024
ShiyuMareceivedtheBSdegreeinsoftwareengi- Lemeng Pan received the PhD degree in statistics
neeringfromtheCollegeofSoftware,NankaiUniver- fromtheUniversityofMarylandCollegePark,Mary-
sity,Tianjin,China,in2022.Sheiscurrentlywork- land.HeiscurrentlyaresearchscientistwithHuawei
ingtowardthemaster’sdegreewiththeCollegeof TechnologiesCompany,Ltd.
Software,NankaiUniversity.Herresearchinterests
includefailurediagnosisandroot-causelocalization.
YichengGuoreceivedtheBSdegreeinparticleand
nuclearphysicsfromtheUniversityofScienceand
JunhuaKuangreceivedtheBSdegreeinsoftware TechnologyofChina,in2014,andthePhDdegreein
engineering from the College of Software, Nankai particleandnuclearphysicsfromtheDepartmentof
University,Tianjin,China,in2024.Heiscurrently ModernPhysics,UniversityofScienceandTechnol-
workingtowardthemaster’sdegreewiththeCollege ogyofChina,Hefei,China,in2019.Heiscurrentlya
ofSoftware,NankaiUniversity.Hisresearchinterests seniorengineerwithHuaweiTechnologiesCompany,
includeanomalydetectionandanomalylocalization. Ltd.
Dan Pei (Senior Member, IEEE) received the BE
andMSdegreesincomputersciencefromtheDe-
BolinZhureceivedtheBSdegreeinsoftwareengi- partmentofComputerScienceandTechnology,Ts-
neeringfromtheCollegeofSoftware,NankaiUniver- inghuaUniversity,Beijing,China,in1997and2000,
sity,Tianjin,China,in2023.Heiscurrentlyworking respectively, and the PhD degree in computer sci-
towardthemaster’sdegreewiththeComputerSci- encefromtheComputerScienceDepartment,Uni-
enceandTechnologyDepartment,NanjingUniver- versityofCalifornia,LosAngeles(UCLA),in2005.
sity.Hisresearchinterestsincludethereasoningof HeiscurrentlyanassociateprofessorwiththeDe-
largelanguagemodels. partmentofComputerScienceandTechnology,Ts-
inghuaUniversity.Hisresearchinterestsincludenet-
workandservicemanagementingeneral.Heisan
ACMseniormember.
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on November 13,2025 at 00:49:19 UTC from IEEE Xplore. Restrictions apply.