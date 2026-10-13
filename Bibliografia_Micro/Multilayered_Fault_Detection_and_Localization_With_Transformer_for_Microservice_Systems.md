| 1502         |             |     |       |     |           |              |     | IEEETRANSACTIONSONRELIABILITY,VOL.73,NO.3,SEPTEMBER2024 |              |     |         |     |     |      |     |
| ------------ | ----------- | --- | ----- | --- | --------- | ------------ | --- | ------------------------------------------------------- | ------------ | --- | ------- | --- | --- | ---- | --- |
| Multilayered |             |     | Fault |     | Detection |              |     | and                                                     | Localization |     |         |     |     | With |     |
|              | Transformer |     |       |     | for       | Microservice |     |                                                         |              |     | Systems |     |     |      |     |
JingyuWang ,SeniorMember,IEEE,YueweiLi ,QiQi ,SeniorMember,IEEE,YanLu ,andBoWu
M
Abstract—Softwarearchitectureisundergoingatransitionfrom Numberofmetricscollectedfromeachcontainer.
monolithic architecture to microservices to achieve resilience, T Durationofmetricscollection(inminutes).
agility, and scalability in the software life cycle. The complex xt m n
|     |     |     |     |     |     |     | (n,m) |     | Value of | metric |     | collected | from | container | at  |
| --- | --- | --- | --- | --- | --- | --- | ----- | --- | -------- | ------ | --- | --------- | ---- | --------- | --- |
dependabilityofthesemicroservicesmayleadtounexpectedfail-
timestampt.
ures,whichbecomesamajorconcernonreliabilityforapplication
|                                                              |     |     |     |     |     |     | xt    |     | Reconstructedvalueofmetricmcollectedfromcon- |     |     |     |     |     |     |
| ------------------------------------------------------------ | --- | --- | --- | --- | --- | --- | ----- | --- | -------------------------------------------- | --- | --- | --- | --- | --- | --- |
| providers.Theexistingfaultdetectionandlocalizationalgorithms |     |     |     |     |     |     | (n,m) |     |                                              |     |     |     |     |     |     |
tainernattimestampt.
| for microservice | systems | only | focus | on the | relationship | within |     |     |     |     |     |     |     |     |     |
| ---------------- | ------- | ---- | ----- | ------ | ------------ | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
microservicesandcannotachievefinergranularityfromalayered T CollectionofmetricsaftercollectingT minutesfor
| system perspective, | including | microservices, |     |     | containers, | physical |     |     |     |     |     |     |     |     |     |
| ------------------- | --------- | -------------- | --- | --- | ----------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
allcontainers.
| machines, | and networks. | To tackle | this | problem, | we  | propose | a   |     |             |      |             |     |           |         |     |
| --------- | ------------- | --------- | ---- | -------- | --- | ------- | --- | --- | ----------- | ---- | ----------- | --- | --------- | ------- | --- |
|           |               |           |      |          |     |         | X   |     | Time-series | data | partitioned |     | into time | windows | for |
multilayeredmethodthatdeconstructscloud-basedmicroservices
input.
andconnectstheinformationfromvariouslayerstoenhancethe
Y
precisionoffaultdetectionandlocalization.TheproposedTrans- Predictionresultsforinputtimewindowdata.
formerencodermodelcandetectanomaliesofcontainersinthere- X Inputdatafortemporalattentionmodule.
sourcelayer,andbydecomposingandanalyzinginvocationlatency, D DimensionoftherowsofmatrixX.
| anomaliesintheservicelayercanbedetected.Afterdetermining |     |     |     |     |     |     | H   |     |     |     |     |     |     |     |     |
| -------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Numberofheadsinmultiheadself-attention.
thefaultyareaoftheresourcelayerbasedontheaboveanomalies,
|               |            |       |         |         |            |         | W   |     | Weightsoffullyconnectednetwork. |     |     |     |     |     |     |
| ------------- | ---------- | ----- | ------- | ------- | ---------- | ------- | --- | --- | ------------------------------- | --- | --- | --- | --- | --- | --- |
| a multifactor | root cause | score | is used | to sort | root cause | metrics |     |     |                                 |     |     |     |     |     |     |
Q
inthefaultyareaforlocalization.Evaluationswereperformedon Querymatrixintransformer.
threedatasets:theSock-Shopdatasetwecollectedfromanactual K Keymatrixintransformer.
microservicesystem,theAIOps2020preliminarydataset,andthe V Valuematrixintransformer.
| SMD.Empiricalinvestigationsconductedonthesedatasetsshow |     |     |     |     |     |     | Z   |     |     |     |     |     |     |     |     |
| ------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Inputforpositionwisefeed-forwardmodule.
| that our | models enhance | the F1 | score | by approximately |     | 0.25 for |     |     |                        |     |     |     |     |     |     |
| -------- | -------------- | ------ | ----- | ---------------- | --- | -------- | --- | --- | ---------------------- | --- | --- | --- | --- | --- | --- |
|          |                |        |       |                  |     |          | O   |     | Outputoftemporalblock. |     |     |     |     |     |     |
anomalydetectionandimprovethemeanaverageprecisionbyupto
R
0.54forrootcauselocalization,whichunderscorestheutilityofour Inputforcontainerblock
modelsineffectivelymanagingmicroservice systemsinpractical A Correlationmatrixofattention.
| scenarios. |               |            |            |     |              |        | s   |     | Anomalyscore. |     |     |     |     |     |     |
| ---------- | ------------- | ---------- | ---------- | --- | ------------ | ------ | --- | --- | ------------- | --- | --- | --- | --- | --- | --- |
| Index      | Terms—Anomaly | detection, | artificial |     | intelligence | for IT |     |     |               |     |     |     |     |     |     |
operations,faultlocalization,microservicesystems,transformer.
|     |     |     |     |     |     |     |      |     |                | I.  | INTRODUCTION |     |              |     |           |
| --- | --- | --- | --- | --- | --- | --- | ---- | --- | -------------- | --- | ------------ | --- | ------------ | --- | --------- |
|     |     |     |     |     |     |     | WITH |     | the continuous |     | expansion    |     | of business, |     | the limi- |
NOMENCLATURE
|     |     |     |     |     |     |     |     | tations | of  | traditional | monolithic |     | architecture |     | have be- |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | ----------- | ---------- | --- | ------------ | --- | -------- |
comeincreasinglyapparentinmeetingthedemandsofmodern
| Notation | Description                                 |     |     |     |     |     |               |          |            |     |               |            |               |             |           |
| -------- | ------------------------------------------- | --- | --- | --- | --- | --- | ------------- | -------- | ---------- | --- | ------------- | ---------- | ------------- | ----------- | --------- |
|          |                                             |     |     |     |     |     | applications. |          | Monolithic |     | applications  | are        | typically     | constructed |           |
| N        | Numberofcontainersinthemicroservicessystem. |     |     |     |     |     |               |          |            |     |               |            |               |             |           |
|          |                                             |     |     |     |     |     | from          | a single | codebase   |     | that packages |            | all functions |             | together. |
|          |                                             |     |     |     |     |     | Consequently, |          | they       | are | unable        | to perform | partial       | expansion,  |           |
increasingthesystem’sthroughputandcapacity.Themicroser-
Manuscriptreceived19April2023;revised21August2023;accepted16
vicearchitecture[1]splitsamonolithicapplicationintomultiple
December2023.Dateofpublication6February2024;dateofcurrentversion
|     |     |     |     |     |     |     | small | autonomous |     | services. | These | services | can | be scaled | and |
| --- | --- | --- | --- | --- | --- | --- | ----- | ---------- | --- | --------- | ----- | -------- | --- | --------- | --- |
4September2024.ThisworkwassupportedinpartbytheNationalNatural
ScienceFoundationofChinaunderGrantU23B2001,Grant62171057,Grant
updatedindependently,leadingtoimprovedflexibility,scalabil-
62101064,Grant62201072,Grant62001054,andGrant62071067,inpartbythe
|     |     |     |     |     |     |     | ity, | and maintainability |     | of  | the | system. | Container | [2], | [3] is a |
| --- | --- | --- | --- | --- | --- | --- | ---- | ------------------- | --- | --- | --- | ------- | --------- | ---- | -------- |
NationalPostdoctoralProgramforInnovativeTalentsunderGrantBX20230052,
virtualizationtechnologythatcanpackageapplicationsandall
inpartbyChinaPostdoctoralScienceFoundationunderGrant2023TQ0039,
in part by the Ministry of Education and China Mobile Joint Fund under their dependencies together to form an independent, portable,
| GrantMCM20200202 | and | Grant MCM20180101, |     | and | in part | by theBeijing |     |            |       |          |     |            |           |     |        |
| ---------------- | --- | ------------------ | --- | --- | ------- | ------------- | --- | ---------- | ----- | -------- | --- | ---------- | --------- | --- | ------ |
|                  |     |                    |     |     |         |               | and | deployable | unit. | Compared |     | to virtual | machines, |     | it has |
UniversityofPostsandTelecommunications-ChinaMobileResearchInstitute
JointInnovationCenter.AssociateEditor:A.Hamou-Lhadj.(Corresponding morerelaxedisolationpropertiestosharetheoperatingsystem
author:QiQi.) among the applications. Therefore, containers are considered
JingyuWang,YueweiLi,QiQi,andYanLuarewiththeStateKeyLaboratory
|     |     |     |     |     |     |     | lightweight. |     | Container | technology |     | accelerates |     | the process | of  |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --- | --------- | ---------- | --- | ----------- | --- | ----------- | --- |
ofNetworking,SwitchingTechnology,BeijingUniversityofPosts,Telecom-
munications, Beijing 100088, China (e-mail: wangjingyu@bupt.edu.cn; microservices development, deployment, and delivery, while
liyuewei2000@bupt.edu.cn;qiqi8266@bupt.edu.cn;luyanfcp@bupt.edu.cn). alsoprovidingaunifiedsolutionfordiversedeploymentenviron-
BoWuiswiththeChinaMobileResearchInstitute,Beijing100053,China
(e-mail:wubo@chinamobile.com). ments.Themicroservicearchitecture,whichdividesthesystem
DigitalObjectIdentifier10.1109/TR.2024.3356717 into multiple independent modules with loose coupling, has
1558-1721©2024IEEE.Personaluseispermitted,butrepublication/redistributionrequiresIEEEpermission.
Seehttps://www.ieee.org/publications/rights/index.htmlformoreinformation.
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on November 08,2025 at 22:35:53 UTC from IEEE Xplore.  Restrictions apply.

WANGetal.:MULTILAYEREDFAULTDETECTIONANDLOCALIZATIONWITHTRANSFORMER 1503
manybenefits.However,italsobringsaboutservicedependence
characteristics that may lead to unexpected errors and raises
concernsaboutthereliabilityofmicroservices.Asmicroservice
systems become more complex, the probability of problems
arisingalsoincreases.Failuretopromptlydetectandlocatethese
issuescancompromisethereliabilityandstabilityofthesystem,
ultimatelyaffectingtheuserexperienceandbusinessefficiency.
Unlike other scenarios, such as anomaly detection in time-
series data and fault localization at the level of program state-
ments[4],maintainingreliabilitywithmicroservicespresentsus
withthefollowingfourchallenges.1)Distributedandheteroge-
neoussystems:Typically,microservicesystemsrunonmultiple
machines, and different services may perform differently in
Fig.1. (a)Existingschemeoffaultdetectionandlocalization.(b)Proposed
termsofmetricsduetofactorssuchasdevelopmentlanguages. schemeoffaultdetectionandlocalization.
2)Bigdata:Intheindustry,therecanbehundredsoforthousands
ofmicroservices,anditiseasytoachievemillionsofdatatodeal
with. 3) Dynamic dependencies: The interconnections among theservicelayer,androotcauselocalization oftenusesoverly
containerized services are dictated by the constantly evolving simplistic anomaly detection methods, which to some extent,
business logic. The constituent containers within services dy- canaffecttheaccuracyofrootcauselocalization.Incontrast,as
namicallyscaleandmigrateinresponsetoloadvariationsand illustratedinFig.1(b),weintegrateanomalydetectionandroot
thestateoftheunderlyingmachines.4)Faultpropagation[5]: causelocalizationwithfinergranularity.Ourapproachinitially
Duetothecomplexdependabilityofservices,faultscanquickly identifiesfaultyareaswithintheresourcelayerthroughanomaly
spread between services, making it difficult for operators to detectionandthenpreciselytracesbacktotherootcausemetrics,
locate the root cause. To cope with these challenges, so far which can better handle the complex scenario of cloud-based
therehavebeenmanystudiesonsystemanomalydetectionand systems.
rootcauselocalization.Concerninganomalydetection,several Specifically, concerning the detection of anomalies in time-
classic outlier detection methods, such as local outlier factor seriesmetrics,wepreviouslynotedtheinefficiencyofrecurrent
(LOF)[6]andsupportvectormachines(SVMs)[7],continueto models due to their sequential nature, where computations at
beappliedtotheanomalydetectionofmicroservicesystemmet- each time step depend on the output of the previous one. The
rics.However,thesemethodsareprimarilyutilizedforswiftly emergenceoftransformer[14]enablesustoleverageattention
identifying obvious abrupt anomalies and are challenged by mechanisms that simultaneously consider all inputs, facilitat-
accuratelyhandlingintricateintramicroservicedatapatternsand ingamorecomprehensiveunderstandingoftemporalfeatures.
dependencies.Deeplearningtechniques[8],[9]havealsobeen Through GPU parallelism, transformer can detect anomalies
widelyadoptedfordetectinganomaliesinthemultidimensional faster than recurrent models. Consequently, we build a model
metricsofmicroservices.Forinstance,approacheslikeLSTM- based onthetransformerarchitecture astheanomaly detector.
AD [10] and TopoMAD [11] utilize long-short-term-memory We use it to not only learn temporal patterns but also capture
(LSTM)-basedmodelstocapturetemporalfeaturesforanomaly dependenciesbetweencontainers,enablingpreciseandefficient
detection.However,recurrentmodelslikeLSTMareknownfor localizationofanomalouscontainers.Buildinguponthisfoun-
their slowness and substantial computational overhead. Thus, dation, we additionally employ breadth-first search (BFS) and
there is a demand for an efficient model capable of acquiring kerneldensityestimation(KDE)fordetectinginvocationlatency
thecomplexfeaturesofmicroserviceswhileavoidingtheselim- anomaliesintraces.Coupledwithmetricanalysisandranking,
itations.Intheresearchonlocatingrootcauses,previouswork thisapproachenablesustoconclusivelyidentifytherootcause
mainly constructed a dependence graph [12] or a cause-effect metrics responsible for the failure. The contributions of this
graph[13]andperformedrootcauseinferenceonthegraphto articlecanbesummarizedasfollows.
locaterootcauseservice.Theseexistingmethodsdonotpinpoint 1) Weproposeamultilayeredfaultdetectionandlocalization
rootcausesatafinergranularity,offeringlimitedassistanceto method,whichcandetectfaultsintheresourcelayerand
operational personnel in identifying the fundamental reasons accurately locate them in the metric layer, significantly
behindfailures. enhancingthesystemreliabilityandstability.
In order to conduct a more thorough analysis and address 2) A transformer encoder model called TAD, designed for
thelimitationspresentincurrentmethodologies,wedeconstruct detectinganomaliesatthecontainerlevelinmultivariate
microservices into multiple layers and propose a more refined time-series data, is proposed. To accommodate the dy-
approach for anomaly detection and root cause localization. namictopologychanges,weintroducethecontainerblock,
We decompose microservices into three layers: service layer, whichemploysself-definedattentionmechanisms.
resourcelayer,andmetriclayer.Theservicelayerreferstothe 3) We perform extensive experiments on three datasets to
runningservices,theresourcelayerencompassesthecontainers compare and analyze our models against baselines, and
andphysicalmachinessupportingservices,andthemetriclayer theresultsshowthatourmodelsachieveimprovementof
integratesessentialmetricdatacollectedfromresourcelayers. uptoabout0.25inF1scorefordetectionand0.54inmean
AsdepictedinFig.1(a),existingmethodsoftenfocussolelyon averageprecisionforlocalization.
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on November 08,2025 at 22:35:53 UTC from IEEE Xplore. Restrictions apply.

| 1504 |     |     |     |     |     |     |     | IEEETRANSACTIONSONRELIABILITY,VOL.73,NO.3,SEPTEMBER2024 |     |     |     |     |     |     |     |
| ---- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
4) We publish the Sock-Shop dataset we collected on LSTM, and variational autoencoder to perform unsupervised
GitHub1 for better reproducibility of the results of this anomaly detection for microservice systems. With the help of
article. topological information,itcan learnthespatialdependence of
| The rest | of this | article | is organized |     | as follows. | Section |     | II metrics. |     |     |     |     |     |     |     |
| -------- | ------- | ------- | ------------ | --- | ----------- | ------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
introduces some related work. Section III overviews the fault AllofthesemodelsexceptTopoMADfocusonlyontemporal
detection and localization method we proposed. Section IV relationships, and none of them achieve high efficiency and
outlines the TAD model for anomaly detection. Sections V accuracy at the same time. In contrast to these models, our
andVIpresentafaultyareadiscoveryalgorithmandrootcause approachnotonlyaccountsfortemporalrelationshipsbutalso
metriclocalizationmethod.Theevaluationandanalysisofthe incorporates spatial relationships among containers. Leverag-
proposedmethodareshowninSectionVII.Finally,SectionVIII ing the efficiency of the transformer architecture, our model
| concludesthisarticle. |     |     |             |     |     |     |     | efficientlydetectsanomalies. |     |     |     |     |     |     |     |
| --------------------- | --- | --- | ----------- | --- | --- | --- | --- | ---------------------------- | --- | --- | --- | --- | --- | --- | --- |
|                       |     | II. | RELATEDWORK |     |     |     |     | B. RootCauseLocalization     |     |     |     |     |     |     |     |
A. MicroserviceAnomalyDetection MonitorRank [21] takes into account both internal and ex-
|     |     |     |     |     |     |     |     | ternal factors, | constructs |     | a call | graph, | and performs |     | a random |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | ---------- | --- | ------ | ------ | ------------ | --- | -------- |
Existingeffortsinmicroservicesanomalydetectionprimarily
|     |     |     |     |     |     |     |     | walk over | this | graph | based | on the similarity |     | with | frontend |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ---- | ----- | ----- | ----------------- | --- | ---- | -------- |
revolvearoundmonitoringmetrics,logs[15],[16],ortraces[17],
metrics.Microscope[22]employsthePCalgorithmtoconstruct
| [18]. Due | to the | easier | analyzability | and | real-time |     | nature of |          |       |              |       |     |          |              |     |
| --------- | ------ | ------ | ------------- | --- | --------- | --- | --------- | -------- | ----- | ------------ | ----- | --- | -------- | ------------ | --- |
|           |        |        |               |     |           |     |           | a causal | graph | of services, | where | the | subnodes | of anomalous |     |
metrics,thissubsectionprimarilyfocusesonpresentingmodels
|     |     |     |     |     |     |     |     | nodes are | included | in  | a candidate | set. | Nodes | within | this can- |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | -------- | --- | ----------- | ---- | ----- | ------ | --------- |
foranomalydetectioninmicroservicetime-seriesdata.
|            |         |         |         |     |               |     |         | didate set | are       | evaluated | for their | correlation  |     | with | the initial |
| ---------- | ------- | ------- | ------- | --- | ------------- | --- | ------- | ---------- | --------- | --------- | --------- | ------------ | --- | ---- | ----------- |
| 1) Classic | Models: | Classic | methods |     | often measure |     | the de- |            |           |           |           |              |     |      |             |
|            |         |         |         |     |               |     |         | front-end  | anomalies | using     | relevance | calculations |     | to   | determine   |
greeofsimilaritybetweenpointsandpointsbydistances.Similar
|     |     |     |     |     |     |     |     | the root | cause. | Using | causal | relationships | to  | construct | graph |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------ | ----- | ------ | ------------- | --- | --------- | ----- |
pointsareverycloseandpointsfarawayfrommostpointsare
enhancestheinterpretabilityofthisapproach.MicroRCA[12]
generallyregardedasanomalies.LOF[6]calculatesthedensity
constructsaservicedependencegraph,leveragingrandomwalks
| ratio between | each            | data | point and | its neighboring |       | data   | points |                      |     |         |     |                 |     |               |     |
| ------------- | --------------- | ---- | --------- | --------------- | ----- | ------ | ------ | -------------------- | --- | ------- | --- | --------------- | --- | ------------- | --- |
|               |                 |      |           |                 |       |        |        | and similarity-based |     | anomaly |     | representation. |     | Additionally, | it  |
| to measure    | the outlierness |      | of data   | points,         | where | points | with   |                      |     |         |     |                 |     |               |     |
takesintoaccounttheresourceutilizationofrelatedcomponents
significantlydifferentdensitiesareidentifiedasanomalies.On
torepresentserviceanomalies,whichimprovestheaccuracyof
| the other | hand, one-class |     | SVM | [7] treats | all | normal | data as |     |     |     |     |     |     |     |     |
| --------- | --------------- | --- | --- | ---------- | --- | ------ | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
rootcauselocalization.
| a single | class and | employs | support | vector | machines |     | to create |     |     |     |     |     |     |     |     |
| -------- | --------- | ------- | ------- | ------ | -------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
Whilethesemethodsalltakesimilarityintoaccount,metric
| a boundary                            | that separates |     | normal | data | points from | anomalies.    |     |            |              |            |             |          |           |          |           |
| ------------------------------------- | -------------- | --- | ------ | ---- | ----------- | ------------- | --- | ---------- | ------------ | ---------- | ----------- | -------- | --------- | -------- | --------- |
|                                       |                |     |        |      |             |               |     | similarity | does         | not always | effectively |          | represent | anomaly. | In        |
| Thesetwoalgorithmsarecommonlyemployed |                |     |        |      |             | inindustryfor |     |            |              |            |             |          |           |          |           |
|                                       |                |     |        |      |             |               |     | contrast,  | our proposed |            | methodology | involves |           | a BFS    | traversal |
quicklydetectingevidentanomalies.Therefore,wechosethem
ofthetracetree,employingstatisticaltechniquesfordetecting
asthebaselinealgorithms.
anomaliesininvocationlatency.Moreover,ourapproachextends
| 2) Forecasting-Based |     |          | Models: | The   | primary     | focus | of the   |             |         |       |              |     |            |         |      |
| -------------------- | --- | -------- | ------- | ----- | ----------- | ----- | -------- | ----------- | ------- | ----- | ------------ | --- | ---------- | ------- | ---- |
|                      |     |          |         |       |             |       |          | beyond mere | service | layer | localization |     | and delves | further | into |
| forecasting-based    |     | approach | is to   | learn | from normal |       | data and |             |         |       |              |     |            |         |      |
thegranularmetriclayer.
| predict  | future data  | points    | following | the    | established |     | normal  |     |     |     |     |     |     |     |     |
| -------- | ------------ | --------- | --------- | ------ | ----------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
| pattern. | As a result, | anomalies |           | can be | detected    | by  | analyz- |     |     |     |     |     |     |     |     |
III. METHODOVERVIEW
| ing the prediction |     | errors. | LSTM-AD | [10] | constructs |     | a stacked |     |     |     |     |     |     |     |     |
| ------------------ | --- | ------- | ------- | ---- | ---------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
LSTMnetworktodetectanomaliesthroughpredictiveanalysis. As shown in Fig. 2, we divide the microservice system
DAGMM[19]combinesdeepautoencodersandGaussianmix- into three layers: the service layer, the resource layer, and
turemodel(GMM)toforecastthenextdatapoint,enablingthe
|     |     |     |     |     |     |     |     | the metric | layer. | The service |     | layer represents |     | several | running |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------ | ----------- | --- | ---------------- | --- | ------- | ------- |
detectionofanomalies.Itoptimizestheparametersoftwomod- microservices, from which we can obtain information such
elssimultaneouslyinanend-to-endfashion,whichenhancesits as service dependence graph and traces. The resource layer
robustnessandoverallperformance. referstotheunderlyingresourcesthatsupporttheoperationof
3) Reconstruction-Based Models: The main idea of these microservices,includingcontainersandphysicalmachines.We
models is to reduce the original data dimension, map it to cangatherinformationaboutthenumberandstatusofcontainers
the latent space, and then reconstruct the original input. By runningonthemachines.Themetricslayerconsistsofvarious
learning only the normal data, the model can only reconstruct containerandmachinemetricscollectedfromtheresourcelayer.
normal data and then evaluate the degree of anomaly through We can collect data from machines and containers through
reconstructionerrors.OmniAnomaly[20]constructsastochas- monitoring agents such as Node exportor2 and cAdvisor,3 and
ticrecurrentneuralnetwork,whichreconstructsinputdatafrom thenPrometheus4periodicallypullsmetricsuniformlyfromthe
therepresentationsandusesthereconstructionprobabilitiesto HTTPaddressesexposedbytheseagents.Thesemetricsarenot
determineanomalies.Itdemonstratesexceptionalperformance onlyusefulforanomaly detectionandrootcause analysis,but
| when applied | to the  | dataset | they     | collected | within | cloud     | envi- |     |     |     |     |     |     |     |     |
| ------------ | ------- | ------- | -------- | --------- | ------ | --------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
| ronments.    | TopoMAD | [11]    | combines | graph     | neural | networks, |       |     |     |     |     |     |     |     |     |
2[Online].Available:https://github.com/prometheus/node_exporter
3[Online].Available:https://github.com/google/cadvisor
1[Online].Available:https://github.com/OpenNetAI/Sock-Shop-Dataset 4[Online].Available:https://prometheus.io
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on November 08,2025 at 22:35:53 UTC from IEEE Xplore.  Restrictions apply.

WANGetal.:MULTILAYEREDFAULTDETECTIONANDLOCALIZATIONWITHTRANSFORMER 1505
Fig.2. Overviewofproposedfaultdetectionandlocalizationmethod.
alsoforenhancingperformanceandresourceplanning,among temporalblockandcontainerblock,addressingmetrictemporal
otheraspects. relationshipsandcontainerrelationships,respectively.Then,we
WeusethecaseofFig.2toexplainhowtheproposedapproach provideanoverviewofthestructureofthemodel,lossfunction,
| works.Fourservices,S |     |                                 | 1–S           |     |                  |               |                            |     |     |     |     |     |     |
| -------------------- | --- | ------------------------------- | ------------- | --- | ---------------- | ------------- | -------------------------- | --- | --- | --- | --- | --- | --- |
|                      |     |                                 | 4,aredeployed |     | onthreemachines, |               | andanomalydetectionmethod. |     |     |     |     |     |     |
| i.e., Machines       |     | 1–3. Each                       | service       | has | multiple         | container in- |                            |     |     |     |     |     |     |
| stances,totalingN    |     | containerinstances.WefoundthatS |               |     |                  |               |                            |     |     |     |     |     |     |
1hasa
slowresponsetimeandwouldliketodeterminetherootcause.
A. ProblemDefinition
| We start | by extracting |     | metrics | related | to containers | from the |     |     |     |     |     |     |     |
| -------- | ------------- | --- | ------- | ------- | ------------- | -------- | --- | --- | --- | --- | --- | --- | --- |
Notationsusedforanomalydetectionarelistedwithdescrip-
metriclayer,suchascontainerCPUusageandmemoryusage.
|     |     |     |     |     |     |     | tions in | Nomenclature. | We  | define | that there are | N containers |     |
| --- | --- | --- | --- | --- | --- | --- | -------- | ------------- | --- | ------ | -------------- | ------------ | --- |
Thesemetricsarethenfedintoourproposedtransformer-based
inamicroservicesystem,andwecollectM
anomaly detector (TAD), which employs multiple transformer metricsfromeach
|         |         |                |     |           |          |            | container | for a total | of T minutes |     | to get T ={x1,...,xT}∈ |     |     |
| ------- | ------- | -------------- | --- | --------- | -------- | ---------- | --------- | ----------- | ------------ | --- | ---------------------- | --- | --- |
| encoder | modules | to reconstruct |     | the input | metrics, | generating |           |             |              |     |                        |     |     |
RN×M×T,wherethedataatminutetare:
| anomaly | scores | s for | container | n.  | Containers | with top-k |     |     |     |     |     |     |     |
| ------- | ------ | ----- | --------- | --- | ---------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
n
anomalyscoresareidentifiedastheinitialfaultyareainthere-
|     |     |     |     |     |     |     |     |     | ⎡   |     | ⎤   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
sourcelayer.Wealsoanalyzethetracesintheservicelayerusing
|     |     |     |     |     |     |     |     |     | xt  | ... | xt  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
BFSandKDE,disassemblingremoteprocedurecall(RPC)la- (1,1) (1,M)⎥
xt ⎢
|     |     |     |     |     |     |     |     |     | =⎣ ... | ... | ... ⎦. |     | (1) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | ------ | --- | --- |
tencyanddiscardingdownstreamredundantcalllatencyinorder
|                                                        |     |     |     |     |     |     |     |     | xt    |     | xt    |     |     |
| ------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | ----- | --- | --- |
| tofocusonanalyzingthelatencyofeachservice,analyzingthe |     |     |     |     |     |     |     |     |       | ... |       |     |     |
|                                                        |     |     |     |     |     |     |     |     | (N,1) |     | (N,M) |     |     |
rootcauseserviceasS
2.Wecombinetheresourcesassociated
withthisservicewiththeanomalouscontainersdetectedbythe
|     |     |     |     |     |     |     |     |     |     |     | L,  |     | ith |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
TADtodeterminethefinalfaultyarea.Wethencollectmetrics Let the length of the time window be the data for the
|          |         |       |          |         |          |               | window                       | are defined | as Xi | ={x(i−1)∗L+1,...,xi∗L}, |                   |     | and we |
| -------- | ------- | ----- | -------- | ------- | -------- | ------------- | ---------------------------- | ----------- | ----- | ----------------------- | ----------------- | --- | ------ |
| from the | metrics | layer | for this | failure | area and | evaluate them |                              |             |       |                         |                   |     |        |
|          |         |       |          |         |          |               | getatotalofT/LwindowsofdataX |             |       |                         | ={X1,...,XT/L}.We |     |        |
basedonmultiplefactorstoobtainarankingoftherootcause
nowdefinethetwoproblemsofmicroserivceanomalydetection
metrics.Therankingsshowthatthemostlikelyrootcauseishigh
andanomalouscontainerlocalization.
| CPU usage | on machine |     | 1. If only | the | root cause | service S 1 | is  |     |     |     |     |     |     |
| --------- | ---------- | --- | ---------- | --- | ---------- | ----------- | --- | --- | --- | --- | --- | --- | --- |
detectedlikeothermethods,operationspersonnelwillstillneed 1) MicroserviceAnomalyDetection:Givenatrainingsetof
|          |              |     |           |         |     |                 | time-series | data | X collected |     | from a microservice |     | sys- |
| -------- | ------------ | --- | --------- | ------- | --- | --------------- | ----------- | ---- | ----------- | --- | ------------------- | --- | ---- |
| to start | from scratch | to  | determine | whether | the | issue lies with |             |      |             |     |                     |     |      |
L
theserviceitselforwiththeunderlyingresources.However,our tem, for a test set of window length and time length
|     |     |     |     |     |     |     | Tˆ(Tˆ | ≥L)collectedfromthesamesystem,predictY |     |     |     |     | =   |
| --- | --- | --- | --- | --- | --- | --- | ----- | -------------------------------------- | --- | --- | --- | --- | --- |
approachcanprovidethemwithamoreprecisetarget,leading
|            |            |      |             |     |       |              | {y1,...,yTˆ/L},whereyi |     |     | ∈{0,1}representswhethermi- |     |     |     |
| ---------- | ---------- | ---- | ----------- | --- | ----- | ------------ | ---------------------- | --- | --- | -------------------------- | --- | --- | --- |
| to clearer | solutions, | such | as reducing | CPU | usage | or migrating |                        |     |     |                            |     |     |     |
theservice. croservice has an anomaly in the ith time window (1
denotesananomalouswindow).
|     |     |     |     |     |     |     | 2) Anomalous |     | Container | Localization: | Given | the | above |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --- | --------- | ------------- | ----- | --- | ----- |
IV. ANOMALYDETECTION trainingandtestsets,predictY ={y1,...,yTˆ/L},where
|     |     |     |     |     |     |     | yi  | indicateswhetherthenthcontainerhasananomaly |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------- | --- | --- | --- | --- | --- |
Inthissection,webeginbypresentingtheproblemdefinition.
(n,·)
We subsequently introduce the key components of TAD: the intheithtimewindow.
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on November 08,2025 at 22:35:53 UTC from IEEE Xplore.  Restrictions apply.

1506 IEEETRANSACTIONSONRELIABILITY,VOL.73,NO.3,SEPTEMBER2024
B. TemporalBlock C. ContainerBlock
Temporal block primarily comprises two components: The container block comprises a sole container attention
temporal attention module and positionwise feed-forward module. In this article, we introduce an attention mechanism
module. tocapturethereciprocalinfluenceandinteractionsamongcon-
1) Temporal Attention: Vanilla self-attention is used here tainers,termedascontainerself-attention.Thespecificstructure
to capture temporal relationships, but there has been a lot of is shown in Fig. 4. First, we transform the output O ∈RD×L
work [23], [24], [25], [26] on improving the efficiency and of temporal block into R∈RN×M×L. Subsequently, the data
performanceofattention,andattentionhereshouldbeanopen fromeachcontainerR nisforwardedthroughastraightforward
and replaceable module that can be chosen according to the fullyconnectedlayer,generatingembeddingsforeachcontainer.
usagescenario.First,weexpandthedataofeachtimewindow These embeddings are concatenated to form the query matrix
Xi from X into a 2-D matrix X ∈RD×L with timestamps (Q)andkeymatrix(K),structuredasfollows:
as columns, where D =N ×M. The expanded format is as (cid:10) (cid:11)
q =f Wn∗R +bn ,k =f(Wn∗R +bn)
follows: n q n q n k n k
⎡ ⎤
x(i−1)∗L+1 ... xi∗L Q=Concat(q 1 ,...q N ),K =Concat(k 1 ,...k N ) (7)
⎢ (1,1) (1,1) ⎥
⎢ ... ... ... ⎥
⎢ ⎥ where q n ,k n represent the embedding vector of container n.
⎢ ⎢ ⎢ x( (1 i− ,M 1) ) ∗L+1 ... xi ( ∗ 1 L ,M) ⎥ ⎥ ⎥ Subsequently, Q and K matrix are employed to compute the
X =⎢ ... ... ... ⎥. (2) correlationmatrixofattention
⎢ ⎥
⎢ ⎢ ⎢ x( ( i N − , 1 1 ) ) ∗L+1 ... xi ( ∗ N L ,1) ⎥ ⎥ ⎥ A=Softmax (cid:8) Q √ KT (cid:9) . (8)
⎣ ... ... ... ⎦ d
x(i−1)∗L+1 ... xi∗L
(N,M) (N,M) For the output X˜ ∈RN×M×T, the data of container n are
Temporal attention (TA) employs multihead attention. Each expressedas
attention head can focus on different segments of the data
(cid:12)N
andgeneratedistinctattentionweightdistributions.Theoutputs
x˜ n = a n,j ∗R n (9)
fromthesemultipleattentionheadsarecombined,therebyrep-
j=1
resentingvariousaspectsofthedatainhigherdimensions.This
enhancesthemodel’scapacityforexpressionandgeneralization. where a n,j is the element in the nth row and jth column of
TAcanbeexpressedas matrixA.
TA(X)=Concat(head1 ,head2 ,...,headH )·W
0
D. OverallStructureofTAD
headh =Attention(Q h ,K h ,V h ) (3)
The overall structure is shown in Fig. 3. Before inputting
where Q h =W q hX, K h =W k hX, V h =W v hX, and H is the the data, we add positional embedding which is used to add
localizationinformationtothetime-seriesdimension.Thedata
numberofheads.Vanillaself-attentionherecanbeexpressedas
(cid:8) (cid:9) arefedintoanencoderconsistingofthreeTADblocks,where
QKT thetemporalblocklearnsthecorrelationbetweenthetimeseries
Attention(Q,K,V)=Softmax √ V. (4)
D throughamultiheadattentionmechanism.Meanwhile,thecon-
tainer block models the relationships between container-based
2) PositionwiseFeed-ForwardModule: Thismoduleprimar- time-series data, capturing the relationships between contain-
ily involves two linear transformations and an intermediate ers. The information between the two modules is then fused
ReLUactivationtofacilitatefeaturefusionandtransformation and propagated through a sandwich structure inspired by the
ST-ConvmoduleinSTGCN[27].Followingthedecodingofthe
FFN(Z)=ReLU(Z∗W 1 +b 1 )W 2 +b 2 (5) reconstructedtime-seriesdata,boththereconstructedandactual
dataarefedintothescorertocalculatetheanomalyscore.
where Z is the input to the module and W 1 and W 2 are the
weightsofthelineartransformation.
Toenhanceefficiency,theskipconnectionandlayernormal- E. LossFunction
ization are introduced after the operation of the two modules.
ForTAD,takingintoaccountpotentialsignificantfluctuations
Consequently,thetemporalblockcanberepresentedas in the data, we use smooth in the objective function. The
techniquewasinitiallyintroducedinfast-RCNN[28]toreduce
Z =Norm(TA(X)+X)
theinterferenceofoutliersongradients,therebyenhancingthe
O =Norm(Z+FFN(Z)) (6) robustnessoftraining.Itsformis
(cid:13)
whereOistheoutputoftemporalblock,normislayernormal- 0.5x2 if|x|<1
smooth(x)= (10)
ization. |x|−0.5 otherwise.
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on November 08,2025 at 22:35:53 UTC from IEEE Xplore. Restrictions apply.

WANGetal.:MULTILAYEREDFAULTDETECTIONANDLOCALIZATIONWITHTRANSFORMER 1507
Fig.3. ArchitectureofproposedanomalydetectionmodelTAD.
Fig.5. DetailedbreakdownofRPClatency,wherethegreensectionrepresents
theclientqueuingdelay,thebluesectionrepresentsthenetworklatency,the
|     |     |     |     |     |     |     | yellow section | represents | the | server | queuing delay, | and | the orange | section |
| --- | --- | --- | --- | --- | --- | --- | -------------- | ---------- | --- | ------ | -------------- | --- | ---------- | ------- |
representstheruntimeofserver.
Fig.4. Structureofcontainerself-attention.ThegreenpartshowstheQand
Kparts,theprocessofembeddingeachnodefromtheFClayertothecontainer arearrangedindescendingorder,andthetop-kcontainerswith
node.
thehighestscoresareidentifiedastheanomalouscontainers.
Ourobjectivefunctionis
V. FAULTYAREADISCOVERY
|     | (cid:12)N | (cid:12)M (cid:12)i∗L |        | (cid:14) |      | (cid:15)   |         |           |        |            |         |           |            |     |
| --- | --------- | --------------------- | ------ | -------- | ---- | ---------- | ------- | --------- | ------ | ---------- | ------- | --------- | ---------- | --- |
|     |           |                       |        |          |      |            | After   | obtaining | the    | collection | of      | anomalous | containers |     |
| L=  |           |                       | smooth | xt       | −xˆt |            |         |           |        |            |         |           |            |     |
|     |           |                       |        | (n,m)    |      | (n,m) (11) |         |           |        |            |         |           |            |     |
|     |           |                       |        |          |      |            | through | the TAD   | model, | this       | section | further   | determines | the |
n=1m=1t=(i−1)∗L+1
faultyareabydiscomposingandanalyzingtheRPCsoftraces
wherexisinputdataandxˆisreconstructeddata.
|     |     |     |     |     |     |     | in the service  | layer.     | This | section  | first | introduces | the      | concept |
| --- | --- | --- | --- | --- | --- | --- | --------------- | ---------- | ---- | -------- | ----- | ---------- | -------- | ------- |
|     |     |     |     |     |     |     | of differential | invocation |      | latency, | which | can help   | us focus | on      |
F. AnomalyScore detecting each service without being affected by downstream
|     |       |            |           |       |          |             | redundant | calls. | Then | we propose | to  | use a | service anomaly |     |
| --- | ----- | ---------- | --------- | ----- | -------- | ----------- | --------- | ------ | ---- | ---------- | --- | ----- | --------------- | --- |
| The | model | is trained | on normal | data, | with the | primary ob- |           |        |      |            |     |       |                 |     |
detectorusingKDE,andfinally,usingthisexistinginformation,
jectivebeingthereconstructionofthesenormaldatapoints.In
the real-life scenarios with anomalies, the model relies on its weproposeaBFS-basedfaultyareadetectionalgorithm.
learnedpatternstoreconstructdata,therebyenablinganomaly
A. DifferentialInvocationLatency
| detection. | During | the training |     | phase, the | maximum | value of |     |     |     |     |     |     |     |     |
| ---------- | ------ | ------------ | --- | ---------- | ------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
the mean squared error between input data and reconstructed Due to the dependencies between services, faulty services
dataisemployedastheanomalythresholdfordetection.Inthe can be located and potential faulty areas can be identified by
detectionphase,ananomalyisflaggedifthereconstructionerror
analyzingtraces.Specifically,asshowninFig.5,webreakdown
surpassesthethreshold.Thereconstructionerror,alsoreferred andanalyzetheRPClatencyintraces.
toasthetotalanomalyscore,isformulatedasfollows: Theentireinvocationprocessisdividedinto7parts.AsRPC
(cid:12)N (cid:12)M (cid:12)i∗L (cid:14) (cid:15) in microservices generally communicates based on TCP, pro-
2
s= xt −xˆt cessesneedtopushdataintothesendingqueuefirst,andthenthe
|     |     |     |     | (n,m) | (n,m) | (12) |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | ----- | ----- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
n=1m=1t=(i−1)∗L+1 networkinterfacecard(NIC)sendsittothenetwork.Similarly,
|     |     |                       |          |       |          |      | when receiving,                                       |     | the NIC | also | first receives | the | data | into the |
| --- | --- | --------------------- | -------- | ----- | -------- | ---- | ----------------------------------------------------- | --- | ------- | ---- | -------------- | --- | ---- | -------- |
|     |     | (cid:12)M (cid:12)i∗L | (cid:14) |       | (cid:15) |      |                                                       |     |         |      |                |     |      |          |
|     |     |                       |          |       | 2        |      | receivingqueue.Whenthequeuemeetscertainconditions(for |     |         |      |                |     |      |          |
|     | =   |                       | xt       | −xˆt  | .        |      |                                                       |     |         |      |                |     |      |          |
|     | sn  |                       |          | (n,m) | (n,m)    | (13) |                                                       |     |         |      |                |     |      |          |
examplebeingfull),theinformationinthereceivingqueuewill
m=1t=(i−1)∗L+1
bedeliveredtotheupstreamprocess.Therefore,inRPCrequest
(cid:6)(cid:6)(cid:6)(cid:6)
Whenanomalousdataarepresentintheinput,thereconstruction andresponse,therearedelaysinthequeue,andthe 1 ; 3 ; 5 ; 7
errorsofeachcontainers
n,alsocalledcontaineranomalyscores partinthefigurerepresentsthesedelays.Duringthetransmission
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on November 08,2025 at 22:35:53 UTC from IEEE Xplore.  Restrictions apply.

| 1508 |     |     |     |     |     |     |     | IEEETRANSACTIONSONRELIABILITY,VOL.73,NO.3,SEPTEMBER2024 |                    |               |          |              |          |               |        |
| ---- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------------- | ------------------ | ------------- | -------- | ------------ | -------- | ------------- | ------ |
|      |     |     |     |     |     |     |     | As the                                                  | invocation         | latency       | does     | not change   | over     | time,         | there  |
|      |     |     |     |     |     |     |     | is almost                                               | no autocorrelation |               | in       | the temporal | order,   | so            | we use |
|      |     |     |     |     |     |     |     | a probabilistic                                         | method             | to            | detect   | anomalies.   | In       | contrast      | to as- |
|      |     |     |     |     |     |     |     | suming                                                  | a specific         | distribution, |          | such as      | a normal | distribution, |        |
|      |     |     |     |     |     |     |     | we believe                                              | that               | refraining    | from     | making       | explicit | assumptions   |        |
|      |     |     |     |     |     |     |     | about the                                               | distribution       | of            | the data | and directly |          | constructing  | an     |
estimationfunctionfromthesampledatathroughnonparametric
estimationismorerobustandaccurate.Inthisstudy,weuseKDE
|     |     |     |     |     |     |     |     | to estimate  | the        | distribution | of            | differential | invocation |      | latency |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ---------- | ------------ | ------------- | ------------ | ---------- | ---- | ------- |
|     |     |     |     |     |     |     |     | under normal | conditions |              | for different | nodes.       | KDE        | is a | typical |
Fig.6. Exampleofdifferentialinvocationlatency.
|     |     |     |     |     |     |     |     | nonparametric | estimation |     | method, | which | estimates | the | proba- |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | ---------- | --- | ------- | ----- | --------- | --- | ------ |
bilitydensityfunction(PDF)fˆ(x)withoutanyassumptionsby
ofthemessageinthenetwork,thereisalsoalatencyrepresented
superimposingseveralkernelfunctions
| bythe | (cid:6)(cid:6) | ; partinthefigure.Toobtainprecisenetworklatency, |     |     |     |     |     |     |     |     |     |         |         |     |     |
| ----- | -------------- | ------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | ------- | --- | --- |
|       | 2              | 6                                                |     |     |     |     |     |     |     |     |     | (cid:8) | (cid:9) |     |     |
(cid:12)n
weneedtoolslikeSystemTap[29]toprobeLinuxkernelwith fˆ(x)= 1 x−x
|                                                       |     |     |     |     |     |     |     |     |     |     |     | K   | i . |     | (15) |
| ----------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |
| anotableperformanceoverhead.InspiredbytheSage[30],the |     |     |     |     |     |     |     |     |     |     | nh  | h   |     |     |      |
i=1
latencyofheartbeatsignalsismeasuredtoapproximatenetwork
latency. The other parts are the processes of the RPC receiver Here,Krepresentsthekernelfunction,hrepresentsthesmooth-
calculating the result and preparing to return it, including the n
|     |     |     |     |     |     |     |     | ing parameter, | and | represents |     | the number |     | of observation |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ---------- | --- | ---------- | --- | -------------- | --- |
serializationanddeserializationoftheRPC.Bysplittingthese points. Commonly used kernel functions include Gaussian,
| parts,                 | this | article can | locate | the faulty | area | more accurately |     | in              |     |        |         |        |        |              |     |
| ---------------------- | ---- | ----------- | ------ | ---------- | ---- | --------------- | --- | --------------- | --- | ------ | ------- | ------ | ------ | ------------ | --- |
|                        |      |             |        |            |      |                 |     | tophat, linear, | and | so on. | In this | study, | we use | the Gaussian |     |
| theinspectionoftraces. |      |             |        |            |      |                 |     | kernelfunction  |     |        |         |        |        |              |     |
Afteranalysis,itcanbeconcludedthattherearethreepossible (cid:8) (cid:9)
|     |     |     |     |     |     |     |     |     |     |     | 1   | 1   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
reasonsforproblemsexhibitedbyRPCcall,forexample,service K(x)= √ exp − x2 .
(16)
|     |     |     |     |     |     |     |     |     |     |     | 2π  | 2   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
AcallsserverB:1)issueswiththesendingorreceivingqueuesof
thecontainerorphysicalmachinewhereserviceAislocated;2)
AfterapplyingKDEtothestabledata,weobtaintheprobability
networkcommunicationissuesbetweencontainersorphysical
|     |     |     |     |     |     |     |     | distribution | function | of  | the differential |     | invocation | latency | for |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | -------- | --- | ---------------- | --- | ---------- | ------- | --- |
machines; 3) issues with service B. Since the latency of each thatnode,anddetermineitsupperquartilex(cid:16)
αandlowerquartile
invocationisverycomplex,especiallythelatencyofthecurrent
x|
α
call may include the overhead of all downstream calls, this (cid:17)
| studyproposestheconceptofdifferentialinvocationlatencyto |     |     |     |     |     |     |     |     |     |     | +∞  |         |     |     |      |
| -------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | ---- |
|                                                          |     |     |     |     |     |     |     |     |     | α=  |     | fˆ(x)dx |     |     |      |
| simplifythelatencyoftraces.                              |     |     |     |     |     |     |     |     |     |     |     |         |     |     | (17) |
x(cid:2) α
|     | AssumingthereisatraceasshowninFig.6,iftheinvocation |     |     |     |     |     |     |     |     |     | (cid:17) |     |     |     |     |
| --- | --------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- |
x|
latenciesforusertoA,AtoB,andAtoCaret user−>A,t A−>B, α fˆ(x)dx.
|     |     |     |     |     |     |     |     |     |     | α=  |     |     |     |     | (18) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |
t
and A−>C, respectively, the average network latency for user −∞
| t o | A i s τ | − > A , t h e n | fo r s e | r v i c e A | , t h e d | i f fe r e n t ia | l i n v o c a t io | n   |     |     |     |     |     |     |     |
| --- | ------- | --------------- | -------- | ----------- | --------- | ----------------- | ------------------ | --- | --- | --- | --- | --- | --- | --- | --- |
u s e r S im i la r t o t h e t h r e e - s i g m a ru le f o r n o r m a ld ist r i b u ti o n , w h e n αi s
| l a | te n c y | i s τ = t |     | − 2 ∗ τ |     | − t | − t | .   |     |     |     |     |     |     |     |
| --- | -------- | --------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
d e lta u s er − > A u s e r− > A A − > B A − > C (− ∞ , x | ) ( x(cid:16) , + ∞ )
|     |            |                        |          |               |               |                |                     | s m al l e n | o u g h , i f i | t f a l l s in | to th e r | a n g e o f | α   | o r α | ,   |
| --- | ---------- | ---------------------- | -------- | ------------- | ------------- | -------------- | ------------------- | ------------ | --------------- | -------------- | --------- | ----------- | --- | ----- | --- |
| T h | e re f o r | e , f o r se r v i c e | A , i ts | d i f f e r e | n t i a l i n | v o c a ti o n | l a t e n c y r e p | -            |                 |                |           |             |     |       |     |
itshouldbeconsideredasanoutlierevent.
resentsthequeuingdelayofthemachinewheretheserviceuser
islocatedandtheservicetimeofAitselfonthecurrentmachine.
Thismethodseparatesacallfromitsdownstreamcalls,which C. RootCauseAreaDiscovery
facilitatesmoreaccurateanomalydetectionforeachservice.
WiththeanomalydetectorusingtheKDEabove,itispossible
Thedifferentialinvocationlatencyisformallydefinedas to locate the suspicious faulty area. Based on the observation
(cid:12)n of various traces in the preliminary dataset of the AIOps2020
τ =t −2∗τ − t (14) InternationalChallenge,wesummarizethecharacteristicsofthe
|                                   | delta     | prev−>cur                                |     | prev−>cur |                            | curr−>i |     |                         |      |            |       |            |             |        |         |
| --------------------------------- | --------- | ---------------------------------------- | --- | --------- | -------------------------- | ------- | --- | ----------------------- | ---- | ---------- | ----- | ---------- | ----------- | ------ | ------- |
|                                   |           |                                          |     |           |                            | i=0     |     | rootcauseareaasfollows: |      |            |       |            |             |        |         |
|                                   |           |                                          |     |           |                            |         |     | Observation             | 1:   | Faults     | often | propagate  | from        | bottom | to top. |
| wheret                            | prev−>cur | representstheinvocationlatencywhentheup- |     |           |                            |         |     |                         |      |            |       |            |             |        |         |
|                                   |           |                                          |     |           |                            |         |     | For example,            | when | a database |       | times out, | the running | status | of      |
| streamserviceinvokesthisservice,t |           |                                          |     |           | cur−>irepresentsthelatency |         |     |                         |      |            |       |            |             |        |         |
forcallingotherservicesbythecurrentservice,τ allupstreaminvocationsisaffectedtovaryingdegrees.Although
|     |     |     |     |     |     | prev−>cur | isthe |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
thedifferentialinvocationlatencyeliminatessomeoftheeffects
networklatencywhentheupstreamservicecallscurrentservice,
andnisthenumberofservicescalledbythecurrentservice. ofupstreamanddownstreamcalls,anomaliesstillcausevarying
degreesoffluctuationintheservice’sruntime.
|     |     |     |     |     |     |     |     | Observation | 2:  | Different | services | on  | the same | machine | or  |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --------- | -------- | --- | -------- | ------- | --- |
B. AnomalyDetectorUsingKDE
|     |     |     |     |     |     |     |     | container | may also | experience |     | certain faults | when | one | service |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | -------- | ---------- | --- | -------------- | ---- | --- | ------- |
With the differential invocation latency, we can perform fails,butthenumberoffaultsandthestarttimeofthefaultsare
anomalydetectionforeachservicenode,whichlaysthefoun- delayedrelativetothecontainerormachineassociatedwiththe
| dationforrootcauseanalysis. |     |     |     |     |     |     |     | rootcause. |     |     |     |     |     |     |     |
| --------------------------- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on November 08,2025 at 22:35:53 UTC from IEEE Xplore.  Restrictions apply.

WANGetal.:MULTILAYEREDFAULTDETECTIONANDLOCALIZATIONWITHTRANSFORMER 1509
Algorithm1:BFS-BasedAlgorithmforDiscoveringPoten- VI. ROOTCAUSEMETRICLOCALIZATION
tialRootCauseArea. After identifying the faulty area, the next step is to collect
Require:Q,thequeuestoresalltracetreesofthe
metricsfromthesecontainersormachinestodeterminetheroot
anomalousinterval;Detector,thedetectorfordifferential
cause of the failure. After analyzing the data of AIOps2020
invocationlatencyoftracesusingKDE;CS TAD , competition,thisstudyfoundthefollowingphenomenaforthe
anomalouscontainersoutputbyTAD;d m,maximum rootcausemetric.Observation1:Therootcausefluctuationsare
depthofalltracetrees alwaysrelatedtodifferentialinvocationlatencies.Observation
1:M_C ←initialthemappingfromnodetoitsaccess
2: The root cause metric is often the most volatile metric.
count Observation 3: The root cause metric undergoes a mutation
2:M_A←initialthemappingfromnodetoitsanomalous
earlierthananyotherchangingmetrics.
count Based on the three observations above, assuming that each
3:repeat metric is a time series o, we calculate the scores of them by
4: T ←popatracetreefromQ combiningthethreecharacteristics.
5: NodeQ←initialthenodequeue Basedonobservation1,thedataarefirstsubtractedfromits
6: pushrootnodev r ofT totheendofNodeQ averagevalueduringthestableperiod,whichcanalleviatethe
7: repeat influenceoncalculatingthecausality
8: v ←popnodefromNodeQ
9: M_C[v]+=1 o˜=o−o m . (19)
10: ifDetector(Q)then
11: M_A[v]+=1
Thevariableo mrepresentsthemeanvalueofthesequenceunder
stableandnormalconditions.Then,aGrangercausalitytestis
12: endif
performedbetweeneachmetricandthedifferentialinvocation
13: foreachchildnodev cofvinT do
latenciesinthetrace.Thistestisusedtodeterminewhetherthere
14: pushv ctotheendofNodeQ
isacausalrelationshipbetweentwotimeseries,withasmaller
15: endfor
p-valueindicatingastrongercausalrelationship.Therefore,this
16: untillen(NodeQ)=0
study defines the causal coefficient of all metrics as s =
17:untillen(Q)=0 casual
1−p,wherep∈[0,1].
18:s
m
←0
Weevaluatethefluctuationinobservation2bycalculatingthe
19:forv,cinM_Ado
distancebetweenthedistributionsofthemetricintheabsence
20: c m ←M_C[v]
of faults and in the presence of faults. As different metrics
21: s←c/c m +λ∗depth(v)/d m
havedifferentdimensionalities,wefirstnormalizethedatausing
22: ifs>s mthen
the maximum and minimum values, and denote the processed
2
2
3
4
:
:
s
v
m
(cid:9) ←
←
v
s sequenceaso˙.Thedifferenceindatadistributionisdefinedas
25: endif s =WassersteinDistance(o˙ ,o˙ ) (20)
fluct norm fault
26:endfor
27:v
p
(cid:9) ←parentservicenodeofrootcauseservicenodev(cid:9) whereo˙
norm
isthenormaltimeseries,o˙
fault
istheanomaloustime
28:CS
v(cid:9)
←containersofv(cid:9)andv
p
(cid:9) series,ands
fluct
∈[0,1]
29:CS r ←intersectionofCS v(cid:9) andCS TAD,finalpotential Accordingtoobservation3,metricsthatfluctuateearlierare
rootcausecontainers morelikelytobetherootcauses.Weidentifythestarttimeof
30:PA←potentialrootcauseareaconsistingofCS r,v(cid:9), the fluctuation by calculating the absolute derivative value of
andv(cid:9) eachmetricdatapoint,whichisdesignedby[31].Letthetime
p
31:returnPA oftheinflectionpointbet(cid:9)
t(cid:9) =argmax(|o −o |) (21)
prev next
whereo ando aretwoadjacentpoints,andt(cid:9) isthetime
prev next
pointcorrespondingtothemaximumchangeofthemetric.Time
Based on these two observations, the localization method scores tthencanbewrittenas
is summarized in Algorithm 1. We use BFS to traverse each
|t−t(cid:9)|
trace tree, count the number of occurrences of each service s t = Δt . (22)
nodeaswellasthenumberoftimesitisjudgedasanomalous max
(from Line 9 to Line 12), and score them based on the node’s Here,tisthetimepointofthedetection,Δt isthemaximum
abnormality count and depth (Line 21, λ is a hyperparameter valueofthetimedifferencebetweentande m a a c x ht(cid:9),s t ∈[0,1].
for balance). Then, the service node with the highest score is
Therefore,thisstudycombinesthescoresrepresentingcausal-
consideredastherootcausenode.Finally,weaddthenodeand ity s causal , fluctuation s fluct , and time distance of change s t to
its parent service node to the potential root cause area, along proposeamultifactorrootcausescores
with the intersection CS r of all containers in these two nodes root
andanomalouscontainersdetectedbyTAD. s root =α×s causal +β×s fluct +γ×s t (23)
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on November 08,2025 at 22:35:53 UTC from IEEE Xplore. Restrictions apply.

| 1510 |     |     |        |     |     |     | IEEETRANSACTIONSONRELIABILITY,VOL.73,NO.3,SEPTEMBER2024 |     |     |         |     |     |     |
| ---- | --- | --- | ------ | --- | --- | --- | ------------------------------------------------------- | --- | --- | ------- | --- | --- | --- |
|      |     |     | TABLEI |     |     |     |                                                         |     |     | TABLEII |     |     |     |
TYPESANDQUANTITIESOFFAULTSINTHEAIOPS2020 TYPESANDQUANTITIESOFFAULTSINJECETEDINSOCK-SHOP
PRELIMINARYDATASET
|     |     |     |     |     |     |     | the ratio | of true | positives | among | predicted | positives, | while |
| --- | --- | --- | --- | --- | --- | --- | --------- | ------- | --------- | ----- | --------- | ---------- | ----- |
where α+β+γ =1, s ∈[0,1]. If we calculate the scores recall represents the proportion of true positives within actual
root
of all metrics in the collection S, then the ranking of the root positives.Theycanbecalculatedasfollows:
causeisdeterminedbytherankingofthescoresinS
|     |     |     |     |     |     |     |     |     | TP  |     | TP  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     |     |     |     |     | P = | ,R= |     |     |     |
(25)
|         |      | RM                         | =top-k(S    | )     |     | (24) |                                                      |     | TP         | +FP                              | TP +FN   |          |           |
| ------- | ---- | -------------------------- | ----------- | ----- | --- | ---- | ---------------------------------------------------- | --- | ---------- | -------------------------------- | -------- | -------- | --------- |
|         |      | LIST                       |             | score |     |      |                                                      |     |            |                                  |          |          |           |
|         |      |                            |             |       |     |      | where TP                                             | is  | the number | of true                          | positive | samples, | FP is the |
| whereRM |      | isthetopkrootcausemetrics. |             |       |     |      |                                                      |     |            |                                  |          |          |           |
|         | LIST |                            |             |       |     |      | numberoffalsepositivesamples,andFNisthenumberoffalse |     |            |                                  |          |          |           |
|         |      |                            |             |       |     |      | negativesamples.AndP                                 |     |            | denotestheprecisionrate,Rdenotes |          |          |           |
|         |      | VII.                       | EXPERIMENTS |       |     |      |                                                      |     |            |                                  |          |          |           |
therecallrate.
Within this section, our primary focus revolves around the F1denotestheharmonicaverageoftheprecisionandrecall
introductionofdatasets,thehyperparametersofthemodels,the valuesofthemodel’spredictionoutcomes.Itsformulais
| performance  | of       | the models,                                | and | a comprehensive | comparison |     |     |     |         |     |     |     |      |
| ------------ | -------- | ------------------------------------------ | --- | --------------- | ---------- | --- | --- | --- | ------- | --- | --- | --- | ---- |
|              |          |                                            |     |                 |            |     |     |     |         | 2   | P   | ·R  |      |
| wit h ba s e | li n em  | o d el s .                                 |     |                 |            |     |     |     |         |     |     |     |      |
|              |          |                                            |     |                 |            |     |     |     | F 1 =   |     | =2· | .   | (26) |
|              |          |                                            |     |                 |            |     |     |     | R−1+P−1 |     | P   | +R  |      |
| W e u s      | e S M D, | 5 A I O ps2020PreliminaryDataset,6andSock- |     |                 |            |     |     |     |         |     |     |     |      |
ShopDatasetdescribedasfollows. AUC stands for area under the ROC (receiver operating char-
SMD:Adatasetspansadurationoffiveweeksandoriginates acteristic)curveandiscommonlyutilizedtoassesstheperfor-
from a prominent Internet corporation, which was published mance of binary classifiers. A high AUC value indicates that
withtheOmniAnomaly[20]model.
|     |     |     |     |     |     |     | the classifier | has | good | performance | and | is able to | effectively |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ---- | ----------- | --- | ---------- | ----------- |
AIOps2020 Preliminary Dataset: It is collected from a mi- differentiatebetweenpositiveandnegativesamples.TheROC
croservicessysteminatestingenvironmentofalargeoperator. curverepresentstheclassifier’struepositiverate(recall)versus
Its microservices are also containerized to support their basic falsepositiverateatdifferentthresholds.
servicesandcommunicatedwitheachotherthroughRPC.There AP finds the area under the precision-recall curve, which is
were81anomalouscasesinthisdataset,includingtheinjected
oftenusedtoevaluatetheeffectofclassificationmodels.
anomaliesshowninTableI,andeachfaultinjectiontimelasted We use precision at k (PR@k), mean average precision
for5min.Thewholedataweresimulatedfor22days. (MAP) and F1 to evaluate the performance of root cause
Sock-ShopDataset:Sock-Shop7isamicroservicesdemoand localization.PR@kreferstotheprecisionwhenthetopkranked
wedeployitwithinaKubernetesclusterwiththreenodes.Each rootcausesareconsideredastheactualrootcause
(cid:18)
service, excluding the database, has two pod replicas, and the (cid:12)
|     |     |     |     |     |     |     |     |      |     | 1   | (R[i]∈v | )   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | ------- | --- | --- |
|     |     |     |     |     |     |     |     | PR@k | =   |     | i<k     | rc  |     |
resource provisioning is set to default configurations. We use (27)
|     |     |     |     |     |     |     |     |     | |A| |     | (min(k,|v | |)) |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | --- |
Locust8 to develop a workload generator and randomly inject a∈A rc
faultsusingchaosblade.9WeuseNodeexporterandcAvisorfor
|     |     |     |     |     |     |     | wherev | rcistherootcauseset,|v |     |     | |isthesizeoftherootcause |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------ | ---------------------- | --- | --- | ------------------------ | --- | --- |
rc
monitoringandwecollectdatathroughPrometheusfor7days. R[i] ith A |A|
|     |     |     |     |     |     |     | set, | is the | root | cause, | is the fault | set, and | is the |
| --- | --- | --- | --- | --- | --- | --- | ---- | ------ | ---- | ------ | ------------ | -------- | ------ |
Thereare102simulatedfaultsinjectedwithaminimuminterval
numberoffaults.
of30minbetweeninjections.Theinjectedfaultslastedfor5min
MAPmainlymeasurestheeffectivenessoftheentiremodel
| each and | there | were four | types of | faults injected, | as shown |     | in  |     |     |     |     |     |     |
| -------- | ----- | --------- | -------- | ---------------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
(cid:12) (cid:12)
| TableII. |     |     |     |     |     |     |     |     |       | 1   |      |     |      |
| -------- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | ---- | --- | ---- |
|          |     |     |     |     |     |     |     |     | MAP = |     | PR@k |     | (28) |
|A|
a∈A1≤k≤N
A. EvaluationMetrics
|         |            |            |         |          |              |         | whereN             | isthenumberofselectedmetrics. |     |     |     |     |     |
| ------- | ---------- | ---------- | ------- | -------- | ------------ | ------- | ------------------ | ----------------------------- | --- | --- | --- | --- | --- |
| There   | are five   | evaluation | metrics | used in  | this article | for     |                    |                               |     |     |     |     |     |
| anomaly | detection: | precision, | recall, | F1, area | under        | the ROC |                    |                               |     |     |     |     |     |
|         |            |            |         |          |              |         | B. ExperimentSetup |                               |     |     |     |     |     |
curve(AUC),andaverageprecision(AP).Precisionquantifies
|     |     |     |     |     |     |     | 1) AnomalyDetection:                       |     |     | Forbaselinesthatonlyconsidertem- |     |     |         |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------------------ | --- | --- | -------------------------------- | --- | --- | ------- |
|     |     |     |     |     |     |     | poralrelationships,wedothesameastheTopoMAD |     |     |                                  |     |     | [11]ap- |
5[Online].Available:https://github.com/NetManAIOps/OmniAnomaly
proach,combiningallthemetricsfromthedifferentcomponents
| 6[Online]. | Available: | https://github.com/NetManAIOps/AIOps-Challenge- |     |     |     |     |     |     |     |     |     |     |     |
| ---------- | ---------- | ----------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
2020-Data intoonehugevectorandusingthatvectorasinput.Forclassic
7[Online].Available:https://github.com/microservices-demo/microservices-
models,weusescikit-learnlibrary[32]withdefaultparameters,
demo
8[Online].Available:https://locust.io andfortheothermodels,weusethehyperparametersgivenin
9[Online].Available:https://github.com/chaosblade-io/chaosblade thisarticleandimplementthemusingPyTorch[33]onNVIDIA
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on November 08,2025 at 22:35:53 UTC from IEEE Xplore.  Restrictions apply.

WANGetal.:MULTILAYEREDFAULTDETECTIONANDLOCALIZATIONWITHTRANSFORMER 1511
Fig.7. PerformanceofourdetectionmodelTADandbaselines.Giventhemetrics,thescorecorrespondingtothebestperformingmodel.
RTX3090GPU.OurmodelisoptimizedusingtheAdamopti- whichindicatesthattheeffectofTADisbetterthanthatofthe
mizer with an initial learning rate of 0.001. The input data is baselinemodelwithoutconsideringthespecificthresholdsetting
processed in batches of size 100, with a time window length andonlyconsideringtheoverallperformanceofthemodel.
of 5, and the number of stacks of the model is 3. We choose Inourexperiments,classicmethodslikeLOFandone-class
hyperparametersotherthantimewindowsizeusinggridsearch, SVM exhibit comparatively poorer performance due to the
and the effect of window size on the performance of anomaly insufficientcomplexity.
detectionisdiscussedinSectionVII-H. DAGMM faces two primary issues. First, it overlooks the
2) RootCauseLocalization: Forbaselines,weusethesame historical dependence within a time series, instead focusing
setup as for MicroRCA [12], where the pseudoanomaly clus- solely on multidistribution modeling of the data. Second, it
tering algorithm is not implemented for MonitorRank [21] to modelsthevalueofasingletimepointasanormaldistribution,
identify the external factors since we only consider internal whichfailstofitnumerousspecialcases.
factorsasinMicroRCA.Sinceallthesemethodslocalizeonlyto ThedrawbackofOmniAnomalyisthatitcannotclearlyad-
theservicelayer,forcomparisonpurposes,ourmethodisusedto dressfeaturecorrelationwithinthemodel.AlthoughTopoMAD
localizetotherootcausemetricsafterlocalizingtotheservice incorporatesstatictopologygraphinformation,itsenhancement
layer. The KDE algorithm we proposed is also implemented inmodelperformanceisrestrictedduetothedynamicinterac-
usingscikit-learnlibrary[32].λinthepotentialrootcausearea tionscommonlyobservedamongcontainers.
| discovery | algorithm is | 1.5. α, β, and γ | in the multifactor | root        |                       |     |         |              |     |
| --------- | ------------ | ---------------- | ------------------ | ----------- | --------------------- | --- | ------- | ------------ | --- |
|           |              |                  |                    | In contrast | to the aforementioned |     | models, | our proposed | ap- |
causescoreis0.23,0.55,and0.22.Thehyperparametersofour proachemploystheattentionmechanismtomodelthedynamic
proposedrootcauselocalizationmethodarealsodeterminedby influencebetweencontainers.Additionally,thetemporalblock
gridsearch. capturestemporaldependencieswithintimeseries.Weintegrate
|     |     |     |     | the spatial | and temporal | information | between | containers | to  |
| --- | --- | --- | --- | ----------- | ------------ | ----------- | ------- | ---------- | --- |
achievestate-of-the-artperformance.
C. DataPreprocessing
| To mitigate | dimensionality | effects, | data normalization | are |     |     |     |     |     |
| ----------- | -------------- | -------- | ------------------ | --- | --- | --- | --- | --- | --- |
E. PerformanceofAnomalyDetectionLatency
| conducted | prior to training. | For the time | series of the | ith di- |     |     |     |     |     |
| --------- | ------------------ | ------------ | ------------- | ------- | --- | --- | --- | --- | --- |
xi,
mension denoted as normalization is executed using the Inreal-worldmicroservicesscenarios,theabilitytopromptly
maximumandminimumvaluesfromthetrainingdata detect anomalies holds significant importance. Referring to
|     |     | (cid:10)  | (cid:11) |              |              |             |         | l          |     |
| --- | --- | --------- | -------- | ------------ | ------------ | ----------- | ------- | ---------- | --- |
|     |     |           |          | SR-CNN [34], | we calculate | the average | latency | of anomaly |     |
|     |     | xi−min Xi |          |              |              |             |         |            |     |
x (cid:19) i = (cid:10) (cid:11) trai(cid:10)n (cid:11). detectionbymodelsasfollows:
(29)
|     | max | Xi −min | Xi    |     |     |            |     |     |     |
| --- | --- | ------- | ----- | --- | --- | ---------- | --- | --- | --- |
|     |     | train   | train |     |     | (cid:12) l |     |     |     |
i
|     |     |     |     |     |     | l=  |     |     | (30) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |
|A|
D. OverallPerformanceofAnomalyDetection
i∈A
|     |     |     |     | A   |     |     |     | l   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
In this section, we will compare the performance of our where represents the set of anomaly blocks, i signifies the
modelwithotherbaselinemodelsforanomalydetectionusing minimumdistanceintermsoftimestepsbetweentheanomaly
detectionpointintheithanomalyblockandthepointatwhich
theSock-ShopdatasetandSMD.Fig.7presentstheprecision,
recall,andF1scoreofmodels.Evidently,ourmodeloutperforms theanomalyoccursasshowninFig.9.Fig.10illustratesacom-
or matches the baseline anomaly detectors. We also draw the parison of the latency metric between our model and baseline
ROC curve and P-R curve (see Fig. 8). It can be seen that in models on Sock-Shop dataset and SMD. Evidently, TAD ex-
thetwodatasets,TADistheclosesttothetopleftcornerinthe hibitsthelowestlatencyindetectinganomaliesintheSock-Shop
ROCfigureandtothetoprightcornerintheP-Rfigure,andthe datasetcharacterizedbyrelativelybriefanomalydurationandin
area surrounded by the curve in the two figures is the largest, SMD,whichfeaturesprolongedanomalyduration.Asaresult,
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on November 08,2025 at 22:35:53 UTC from IEEE Xplore.  Restrictions apply.

1512 IEEETRANSACTIONSONRELIABILITY,VOL.73,NO.3,SEPTEMBER2024
(a)
(b)
Fig.8. ROCandR-Pcurvesofdifferentmodelson(a)theSock-ShopDatasetand(b)SMD.ThesolidbluelineisTAD,whichisbetterthanotherbaseline
methodsinboththeareaunderthelineandthedegreeclosetotheupperleftcorner.(a)Sock-ShopDataset.(b)SMD.
Fig.9. Latencyofdetectinganomalies.
ourTADmodelisproficientinswiftlyidentifyinganomaliesin
real-world scenarios, thus reducing the time required for root
causelocalization. Fig.10. ThelatencycomparisonbetweenTADandthebaselinemodelsonthe
Sock-ShopDatasetandSMD.Thelowerx-axiscorrespondstotheSock-Shop
Dataset,whiletheupperx-axiscorrespondstoSMD.
F. OverallPerformanceofRootCauseLocalization
In order to verify the reliability of the proposed model, this here,whichisslightlydifferentfromanomalydetectionmodels,
sectionwillcomparetheperformanceofitwiththreeotherbase- tobetterdemonstratethewideapplicabilityofourmodel.
line algorithms: MonitorRank, Microscope, and MicroRCA. Table III shows the results of baseline algorithms and the
WeuseSock-ShopdatasetandAIOps2022preliminarydataset multilayered root cause localization method we proposed on
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on November 08,2025 at 22:35:53 UTC from IEEE Xplore. Restrictions apply.

WANGetal.:MULTILAYEREDFAULTDETECTIONANDLOCALIZATIONWITHTRANSFORMER 1513
TABLEIII
PERFORMANCECOMPARISONOFOURLOCALIZATIONMETHODWITHBASELINES
the two datasets. It can be seen that the performance of the TABLEIV
ABLATIONSTUDYOFTAD
multilayeredrootcauselocalizationalgorithmfarexceedsthat
ofothermodels.Comparedwithothermodels,themultilayered
rootcauselocalizationmethodhassignificantimprovementsin
allevaluationmetrics.
| MonitorRank |           | proposes | a           | random | walk algorithm | by       | simu- |     |     |     |     |     |     |     |
| ----------- | --------- | -------- | ----------- | ------ | -------------- | -------- | ----- | --- | --- | --- | --- | --- | --- | --- |
| lating the  | operation | and      | maintenance |        | personnel.     | However, | the   |     |     |     |     |     |     |     |
customweightofedgesdoesnotconsiderthedelaypropagation
| of faults, | resulting | in  | a large | number | of misjudgments |     | and |     |     |     |     |     |     |     |
| ---------- | --------- | --- | ------- | ------ | --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
reportingalargenumberofnormalmetricsandnodes.
MicroscopeusesthePCalgorithmtoconstructthecasualrela-
tionshipofservices,butthePCalgorithmcanonlycalculatethe
instantaneouscausalgraph,whiletheinfluencebetweenmetrics
| is a process | that               | requires  | a certain    |                       | time delay.  | Second,         | it uses  |     |     |     |     |     |     |     |
| ------------ | ------------------ | --------- | ------------ | --------------------- | ------------ | --------------- | -------- | --- | --- | --- | --- | --- | --- | --- |
| the Pearson  | correlation        |           | coefficient  |                       | to calculate | the correlation |          |     |     |     |     |     |     |     |
| between      | anomalous          | front-end |              | service               | metrics      | and root        | cause    |     |     |     |     |     |     |     |
| candidate    | metrics.foramutant |           |              | metric,itscorrelation |              |                 | withthe  |     |     |     |     |     |     |     |
| front end    | is very            | low,      | and the      | Pearson               | correlation  | coefficient     |          |     |     |     |     |     |     |     |
| mainly       | considers          | linear    | correlation, |                       | while the    | relationship    | be-      |     |     |     |     |     |     |     |
| tween root   | causes             | and       | front-end    | metrics               | is often     | not             | linearly |     |     |     |     |     |     |     |
related.Therefore,manyothermetricsthatgrowwithincreased
servicewillbeconsideredrootcauses,moretypicallymemory Fig.11. ChangesofthethreeindicatorsofAP,AUC,andlatencyontheSock-
| usage.   |     |         |           |       |              |     |         | ShopdatasetoftheTADmodelasthewindowsizechanges. |     |     |     |     |     |     |
| -------- | --- | ------- | --------- | ----- | ------------ | --- | ------- | ----------------------------------------------- | --- | --- | --- | --- | --- | --- |
| MicroRCA |     | uses an | attribute | graph | to construct | the | overall |                                                 |     |     |     |     |     |     |
relationshipgraphanddeterminestherootcausethroughrandom
|            |          |     |          |     |                        |     |        | then replaced | all | temporal | blocks | with container | blocks | and |
| ---------- | -------- | --- | -------- | --- | ---------------------- | --- | ------ | ------------- | --- | -------- | ------ | -------------- | ------ | --- |
| walk. When | randomly |     | walking, | it  | still uses correlation |     | as the |               |     |          |        |                |        |     |
thenperformedtheexperimentagain.Theexperimentalresults
weight,soitalsofacesthesameproblemasamicroscope.How-
obtainedareshowninTableIV.
ever,itsattributegraphaddstherelationshipbetweencontainers
|     |     |     |     |     |     |     |     | It can be | seen | that after | removing | the container | block, | the |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ---- | ---------- | -------- | ------------- | ------ | --- |
andphysicalmachines,soitseffectisslightlybetterthanthatof
modeleffectdecreasesslightly,andafterremovingthetemporal
amicroscope.
blockalone,themodeleffectdecreasessignificantly.Themain
| Unlike | other | methods, | the | multilayered | root | cause | localiza- |     |     |     |     |     |     |     |
| ------ | ----- | -------- | --- | ------------ | ---- | ----- | --------- | --- | --- | --- | --- | --- | --- | --- |
reasonisthatthedynamicrelationshipbetweenthecontainers
| tion method | determines |     | the | potential | root cause | area | through |     |     |     |     |     |     |     |
| ----------- | ---------- | --- | --- | --------- | ---------- | ---- | ------- | --- | --- | --- | --- | --- | --- | --- |
inthemicroservicesystemhaslittleeffectontheperformance
| differential     | latency | and   | the            | BFS-based | faulty         | area discovery |        |                     |             |            |            |                     |                    |        |
| ---------------- | ------- | ----- | -------------- | --------- | -------------- | -------------- | ------ | ------------------- | ----------- | ---------- | ---------- | ------------------- | ------------------ | ------ |
|                  |         |       |                |           |                |                |        | parameters          | of each     | node,      | especially | under               | normal conditions, |        |
| algorithm.       | The     | prior | operation      | and       | maintenance    | experience     |        |                     |             |            |            |                     |                    |        |
|                  |         |       |                |           |                |                |        | and the performance |             | indicators |            | are all time-series | data.              | If you |
| are incorporated |         | into  | the algorithm, |           | which improves | the            | inter- |                     |             |            |            |                     |                    |        |
|                  |         |       |                |           |                |                |        | remove the          | time-series |            | modeling,  | the effect          | of the model       | will   |
pretabilityandeffectivenessofthealgorithm.
|     |     |     |     |     |     |     |     | be greatly | reduced. | When | the | two modules | are combined, | the |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | -------- | ---- | --- | ----------- | ------------- | --- |
dynamicrelationshipandtimingcharacteristicsofthecontainer
arelearned,sotheeffectisthebest.
G. AblationStudyofAnomalyDetectionModel
Themaingoalofthispartistoverifythereliabilityofeachpart
|     |     |     |     |     |     |     |     | H. ImpactofTimeWindow |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------------- | --- | --- | --- | --- | --- | --- |
ofTAD,andthemainverificationistheeffectofmodelingthe
time series and the relationship between the containers. Since Thissectionmainlydiscussestheimpactofthetimewindow
the Sock-shop dataset is more in line with the characteristics sizeontheoveralleffectoftheTADmodel.Intheexperiment,
of microservices, this part mainly uses this data as the exper- weincreasethetimewindowsizefrom1to20,andthenrecord
imental dataset. To study each component of our approach’s theeffectofTADonthesock-shopdataset.AsshowninFig.11,
effectiveness,wefirstremovedthecontainerblockofthemodel asthetimewindowincreases,themodeleffectisfirstdecreased,
andperformedexperimentstogettheexperimentalresults,and then increased, and then decreased, and does not change after
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on November 08,2025 at 22:35:53 UTC from IEEE Xplore.  Restrictions apply.

1514 IEEETRANSACTIONSONRELIABILITY,VOL.73,NO.3,SEPTEMBER2024
TABLEV the differential invocation latency obtained could more accu-
ABLATIONSTUDYOFMULTILAYEREDROOTCAUSELOCALIZATION
ratelyconfirmthefaultyservice.Amultifactorrootcausescore
ALGORITHM
wasproposedtorankmetricsofpotentialfaultyarea,andfinally
possible root cause metrics were obtained. This method also
performedbestonSock-ShopdatasetandAIOps2020prelimi-
nary dataset. In summary, our models improved the reliability
ofmicroservicesystemsthroughefficientandaccurateanomaly
the time window reaches 10. When the time window is 1, the detectionandrootcauselocalization.Inourfuturework,wewill
characteristicsofthecycletimesequencearenotused.Atthis considerwhichmetricsbetterexposemicroservicefailuresand
time, the spatial relationship mainly captured by the model is trytocombinedatafromothermodalitiesforanomalydetection
less effective. As the time window increases, although TAD androotcauselocalization.
begins to capture some time-related information, because the
time window does not reach a certain length, it cannot fully
capture the periodic information, and the model effect at this
REFERENCES
time will even gradually deteriorate. When the time window
reaches the right time, that is, window_size=5, the model [1] N.Dragonietal.,“Microservices:Yesterday,today,andtomorrow,”in
PresentandUlteriorSoftwareEngineering.Cham,Switzerland:Springer,
effectwillberemarkablycompiled.Later,asthetimewindowof
2017,pp.195–216.
themodelcontinuestoincrease,thedifficultyofreconstruction [2] M.Lv,J.Fan,W.Fan,andX.Jia,“Faultdiagnosisbasedonsubsystem
isalsoincreasing,sotheeffectwillbeworse. structuresofdatacenternetworkBCube,”IEEETrans.Rel.,vol.71,no.2,
pp.963–972,Jun.2022.
[3] S.Meng,L.Luo,X.Qiu,andY.Dai,“Service-orientedreliabilitymodeling
I. AblationStudyofRootCauseLocalizationAlgorithm andautonomousoptimizationofreliabilityforpubliccloudcomputing
systems,”IEEETrans.Rel.,vol.71,no.2,pp.527–538,Jun.2022.
Inthissection,wetrytoverifythereliabilityofeachpartof [4] W.E.Wong,R.Gao,Y.Li,R.Abreu,andF.Wotawa,“Asurveyonsoftware
multilayeredrootcauselocalizationalgorithm.Wemakesome faultlocalization,”IEEETrans.Softw.Eng.,vol.42,no.8,pp.707–740,
Aug.2016.
adjustmentstotheentiremethod,usingthescoreofonespecific
[5] M.-C. Chiang, C.-Y. Huang, C.-Y. Wu, and C.-Y. Tsai, “Analysis of a
factor as the root cause score in root cause analysis. Table V fault-tolerantframeworkforreliabilitypredictionofservice-orientedar-
showsitseffectiveness. chitecturesystems,”IEEETrans.Rel.,vol.70,no.1,pp.13–48,Mar.2021.
[6] M.M.Breunig,H.-P.Kriegel,R.T.Ng,andJ.Sander,“LOF:Identifying
The results of the ablation experiment show that using only
density-basedlocaloutliers,”inProc.ACMInt.Conf.Manage.Data,2000,
thefluctuationscoremodelhasthebestperformance,followed pp.93–104.
by the time score model, while using only the causality score [7] Y.Chen,X.S.Zhou,andT.S.Huang,“One-classSVMforlearningin
imageretrieval,”inProc.IEEEInt.Conf.ImageProcess.,2001,pp.34–37.
modelhastheworstperformance.Thisindicatesthatthedom-
[8] A.HeandX.Jin,“Deepvariationalautoencoderclassifierforintelligent
inant feature in locating the root cause is the severity of the fault diagnosis adaptive to unseen fault categories,” IEEE Trans. Rel.,
fluctuations, but in some cases, there may be multiple options vol.70,no.4,pp.1581–1595,Dec.2021.
[9] P.Qi,D.Li,andS.-K.Ng,“MAD-SGCN:Multivariateanomalydetection
withseverefluctuations,makingitdifficulttodeterminethetrue
withself-learninggraphconvolutionalnetworks,”inProc.IEEEInt.Conf.
root cause using the fluctuation score only. Similarly, if only DataEng.,2022,pp.1232–1244.
thetimescoreisused,smallfluctuationsinsomemetricsmay [10] P. Malhotra et al., “Long short term memory networks for anomaly
detectionintimeseries,”Esann,vol.2015,2015,Art.no.89.
bedirectlyconsideredastherootcause,leadingtomanyfalse
[11] Z.Heetal.,“Aspatiotemporaldeeplearningapproachforunsupervised
positives.However,whenlocatingcontainerfailures,themetrics anomalydetectionincloudsystems,”IEEETrans.NeuralNetw.Learn.
changesarerelativelystable,anddirectlyrankingthemasroot Syst.,vol.34,no.4,pp.1705–1719,Apr.2023.
[12] L.Wu,J.Tordsson,E.Elmroth,andO.Kao,“MicroRCA:Rootcause
causescorescanstillobtainsomecorrectresults.Thecausality
localizationofperformanceissuesinmicroservices,”inProc.IEEE/IFIP
score is the worst because the Granger causality test used can Netw.OperationsManage.Symp.,2020,pp.1–9.
onlydetectlinearcausalitywithouthiddenvariables,henceits [13] M.Lietal.,“Causalinference-basedrootcauseanalysisforonlineservice
systems with intervention recognition,” in Proc. 28th ACM Int. Conf.
poorperformance.However,fornetworkissues,itsmetricsare
Knowl.Discov.DataMining,2022,pp.3230–3240.
generally directly proportional to latency. In this case, using [14] A.Vaswanietal.,“Attentionisallyouneed,”inProc.Adv.NeuralInf.
causalrelationshipscanhelplocatesomeoftherootcauses. Process.Syst.,2017,pp.6000–6010.
[15] M.Cinque,R.D.Corte,andA.Pecchia,“Micro2vec:Anomalydetection
inmicroservicessystemsbyminingnumericrepresentationsofcomputer
VIII. CONCLUSION logs,”J.Netw.Comput.Appl.,vol.208,2022,Art.no.103515.
[16] L.Wang,N.Zhao,J.Chen,P.Li,W.Zhang,andK.Sui,“Root-cause
This article analyzed the entire microservices architecture metriclocationformicroservicesystemsvialoganomalydetection,”in
and focused on solving the problems of anomaly detection Proc.IEEEInt.Conf.WebServ.,2020,pp.142–150.
[17] P. Liu et al., “Unsupervised detection of microservice trace anomalies
androotcauselocalizationformicroservicesystems.Through
throughservice-leveldeepBayesiannetworks,”inProc.IEEEInt.Symp.
capturingthedependenciesbetweencontainersandthetemporal Softw.Rel.Eng.,2020,pp.48–58.
relationshipwithinatimewindow,ourapproachoutperformed [18] K.Zhang,C.Zhang,X.Peng,andC.Sha,“PUTraceAD:Traceanomaly
detectionwithpartiallabelsbasedonGNNandPUlearning,”inProc.
otherstate-of-the-artmodelsforcontaineranomalydetectionon
IEEEInt.Symp.Softw.Rel.Eng.,2022,pp.239–250.
boththeSock-ShopdatasetandSMD.Notably,ourmodelalso [19] B.Zongetal.,“DeepautoencodingGaussianmixturemodelforunsu-
exhibitedsuperiorspeedinanomalydetectionwhencomparedto pervisedanomalydetection,”inProc.Int.Conf.Learn.Representations,
2018.
alternativeapproaches.Afaultyareadiscoveryalgorithmbased
[20] Y.Su,Y.Zhao,C.Niu,R.Liu,W.Sun,andD.Pei,“Robustanomaly
onBFSwasalsoproposed.Bydecomposingthetracingchain, detectionformultivariatetimeseriesthroughstochasticrecurrentneural
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on November 08,2025 at 22:35:53 UTC from IEEE Xplore. Restrictions apply.

WANGetal.:MULTILAYEREDFAULTDETECTIONANDLOCALIZATIONWITHTRANSFORMER 1515
network,”inProc.25thACMInt.Conf.Knowl.Discov.DataMining,2019, YueweiLireceivedtheB.S.degreeincomputersci-
pp.2828–2837. enceandtechnologyfromXidianUniversity,Xi’an,
[21] M.Kim,R.Sumbaly,andS.Shah,“Rootcausedetectioninaservice- China,in2018.Heiscurrentlyworkingtowardthe
oriented architecture,” in Proc. ACM SIGMETRICS/Int. Conf. Meas. M.S.degreeincomputertechnologywiththeState
Model.Comput.Syst.,2013,pp.93–104. KeyLaboratoryofNetworkingandSwitchingTech-
[22] J.Lin,P.Chen,andZ.Zheng,“Microscope:Pinpointperformanceissues nology,BeijingUniversityofPostsandTelecommu-
with causal graphs in micro-service environments,” in Proc. Int. Conf. nications,Beijing,China.
Serv.-OrientedComput.,2018,pp.3–20. His research interests include AIOps and cloud
[23] N.Kitaev,L.Kaiser,andA.Levskaya,“Reformer:Theefficienttrans- computing.
former,”inProc.Int.Conf.Learn.Representations,2019.
[24] H. Zhou et al., “Informer: Beyond efficient transformer for long se-
quencetime-seriesforecasting,”inProc.AAAIConf.Artif.Intell.,2021,
pp.11106–11115.
[25] S.Liuetal.,“Pyraformer:Low-complexitypyramidalattentionforlong-
rangetimeseriesmodelingandforecasting,”inProc.Int.Conf.Learn.
Representations,2021. Qi Qi (Senior Member, IEEE) received the Ph.D.
[26] Y. Liu, H. Wu, J. Wang, and M. Long, “Non-stationary transformers: degreeincomputerscienceandtechnologyfromthe
Exploringthestationarityintimeseriesforecasting,”inProc.Adv.Neural BeijingUniversityofPostsandTelecommunications,
Inf.Process.Syst.,2022,pp.9881–9893. Beijing,China,in2010.
[27] B.Yu,H.Yin,andZ.Zhu,“Spatio-temporalgraphconvolutionalnetworks: She is currently a Professor with the State Key
Adeeplearningframeworkfortrafficforecasting,”inProc.27thInt.Joint Laboratory of Networking and Switching Technol-
Conf.Artif.Intell.,2018,pp.3634–3640. ogy,BeijingUniversityofPostsandTelecommuni-
[28] R.Girshick,“FastR-CNN,”inProc.IEEEInt.Conf.Comput.Vis.,2015, cations.Shehasauthoredorcoauthoredmorethan
pp.1440–1448. 100papersininternationaljournalsandconferences.
[29] P.Olivier,J.Boukhobza,M.Soula,M.L.Grand,I.C.Draa,andE.Senn, Herresearchinterestsincludetimeserialsanalysis,
“AtracingtoolsetforembeddedLinuxflashfilesystem,”inProc.8thInt. edgeintelligentnetwork,distributedmachinelearn-
Conf.Perform.Eval.Methodol.Tools,2014,pp.153–158. ing,cloudcomputing,InternetofThings,anddeepreinforcementlearning.
[30] Y.Gan,M.Liang,S.Dev,D.Lo,andC.Delimitrou,“Sage:Practicaland Dr.QiwastherecipientofthreeawardsfromtheNationalNaturalScience
scalableML-drivenperformancedebugginginmicroservices,”inProc. FoundationsofChina.
ACMInt.Conf.ArchitecturalSupportProgram.Lang.OperatingSyst.,
2021,pp.135–151.
[31] P.Liuetal.,“FluxRank:Awidely-deployableframeworktoautomatically
localizingrootcausemachinesforsoftwareservicefailuremitigation,”in YanLureceivedtheM.S.degreeincomputerscience
Proc.IEEEInt.Symp.Softw.Rel.Eng.,2019,pp.35–46. and technology from the State Key Laboratory of
[32] F.Pedregosaetal.,“Scikit-learn:MachinelearninginPython,”J.Mach. NetworkingandSwitchingTechnology,BeijingUni-
Learn.Res.,vol.12,pp.2825–2830,2011. versity of Posts and Telecommunications, Beijing,
[33] A.Paszkeetal.,“PyTorch:Animperativestyle,high-performancedeep China,in2023.
learninglibrary,”inProc.Adv.NeuralInf.Process.Syst.,2019,pp.8026– Hisresearchinterestsincludetimeseriesanomaly
8037. detection,rootcausediagnose,andcloudcomputing.
[34] H.Renetal.,“Time-seriesanomalydetectionserviceatmicrosoft,”in
Proc.ACMInt.Conf.Knowl.Discov.DataMining,2019,pp.3009–3017.
JingyuWang(SeniorMember,IEEE)receivedthe
Ph.D. degree in computer science and technology
fromtheBeijingUniversityofPostsandTelecom-
BoWureceivedthemaster’sdegreeininformation
munications,Beijing,China,in2008. andcommunicatonsystemfromtheHuazhongUni-
HeiscurrentlyaProfessorwiththeStateKeyLab- versityofScienceandTechnology,Wuhan,China,in
oratory of Networking and Switching Technology, 2007.
BeijingUniversityofPostsandTelecommunications. HeistheGroupManagerandDeputyDirectorof
Hehasauthoredorcoauthoredmorethan200papers theDepartmentofServiceTechnology,ChinaMobile
in the JSAC, ToN, TPDS, NSDI, and so on. His ResearchInstitute,Beijing,China.Hisresearchinter-
researchinterestsincludebroadaspectsofintelligent estsincludehomebandwidthnetworkservice,future
networks,Edge/Cloudcomputing,machinelearning, servicefor6G,andAIOpsformobilenetworksand
AIOps and self-driving network, IoV/IoT, knowledge-defined network and services.
intent-drivennetworking.
Dr.WangisSeniorMemberofCICandselectedforBeijingYoungTalents
Program.
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on November 08,2025 at 22:35:53 UTC from IEEE Xplore. Restrictions apply.