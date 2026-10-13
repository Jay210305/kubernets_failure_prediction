Root Cause Analysis In Microservice Using Neural Granger Causal Discovery
Cheng-MingLin,ChingChang,Wei-YaoWang,Kuang-DaWang,Wen-ChihPeng
NationalYangMingChiaoTungUniversity,Hsinchu,Taiwan
zmlin1998.cs10@nycu.edu.tw,blacksnail789521@gmail.com,sf1638.cs05@nctu.edu.tw,gdwang.cs10@nycu.edu.tw,
wcpeng@cs.nycu.edu.tw
4202 beF 2  ]GL.sc[  1v04110.2042:viXra
Abstract
Inrecentyears,microserviceshavegainedwidespreadadop-
tioninIToperationsduetotheirscalability,maintenance,and
flexibility.However,itbecomeschallengingforsitereliability
engineers(SREs)topinpointtherootcauseduetothecom-
plexrelationshipsinmicroserviceswhenfacingsystemmal-
| functions. | Previous | research |     | employed | structured | learning |     |     |     |     |     |     |     |     |
| ---------- | -------- | -------- | --- | -------- | ---------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
methods(e.g.,PC-algorithm)toestablishcausalrelationships
andderiverootcausesfromcausalgraphs.Nevertheless,they
| ignored  | the temporal | order       | of  | time series | data   | and failed | to    |     |     |     |     |     |     |     |
| -------- | ------------ | ----------- | --- | ----------- | ------ | ---------- | ----- | --- | --- | --- | --- | --- | --- | --- |
| leverage | the rich     | information |     | inherent    | in the | temporal   | rela- |     |     |     |     |     |     |     |
tionships.Forinstance,incaseswherethereisasuddenspike
in CPU utilization, it can lead to an increase in latency for Figure 1: An example of causal structure discovery-based
othermicroservices.However,inthisscenario,theanomaly techniquesforRCA.
inCPUutilizationoccursbeforethelatencyincrease,rather
| than simultaneously. |     | As  | a result, | the | PC-algorithm | fails | to  |     |     |     |     |     |     |     |
| -------------------- | --- | --- | --------- | --- | ------------ | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
capturesuchcharacteristics.Toaddressthesechallenges,we tionscaneffectivelypinpointtheunderlyingcauseswhena
proposeRUN,anovelapproachforrootcauseanalysisusing
systemmalfunctionoccurs.
| neural Granger |     | causal | discovery | with | contrastive | learning. |     |           |        |        |           |            |     |           |
| -------------- | --- | ------ | --------- | ---- | ----------- | --------- | --- | --------- | ------ | ------ | --------- | ---------- | --- | --------- |
|                |     |        |           |      |             |           |     | In recent | years, | as the | companies | experience |     | continued |
RUNenhancesthebackboneencoderbyintegratingcontex-
|     |     |     |     |     |     |     |     | growth, | the system | operations |     | have scaled | up  | and grown |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ---------- | ---------- | --- | ----------- | --- | --------- |
tualinformationfromtimeseries,andleveragesatimeseries
|     |     |     |     |     |     |     |     | increasingly | complex. |     | Therefore, | these | organizations | have |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | -------- | --- | ---------- | ----- | ------------- | ---- |
forecastingmodeltoconductneuralGrangercausaldiscov-
optedtomigratefromtheso-calledmonolithicarchitecture
ery.Inaddition,RUNincorporatesPagerankwithapersonal-
izationvectortoefficientlyrecommendthetop-krootcauses. tomicroservicearchitecture(Liuetal.2021).Microservice
Extensive experiments conducted on the synthetic and real- architecture offers benefits such as better scalability, easier
worldmicroservice-baseddatasetsdemonstratethatRUNno- maintenance,andgreaterflexibility.Eachservicecanbein-
ticeably outperforms the state-of-the-art root cause analysis dependentlyscaledbasedondemand,enablingefficientre-
methods.Moreover,weprovideananalysisscenarioforthe source utilization. Developers can focus on individual ser-
| sock-shop | case | to showcase | the | practicality |     | and efficacy | of  |     |     |     |     |     |     |     |
| --------- | ---- | ----------- | --- | ------------ | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
vices,makingitsimplertodebug,test,anddeploychanges.
| RUN in | microservice-based |     | applications. |     | Our | code is | pub- |         |              |     |          |                   |     |         |
| ------ | ------------------ | --- | ------------- | --- | --- | ------- | ---- | ------- | ------------ | --- | -------- | ----------------- | --- | ------- |
|        |                    |     |               |     |     |         |      | Despite | the numerous |     | benefits | of microservices, |     | when an |
liclyavailableathttps://github.com/zmlin1998/RUN.
anomalyarisesinoneservice,theinterdependenciesamong
servicescancreateadominoeffect,resultinginsubsequent
1 Introduction issuesandultimatelyleadingtosystemfailure(Zhangetal.
2022).Insuchscenarios,in-depthanalysisbecomesimper-
| Root cause | analysis | plays | a   | crucial | role in | numerous | do- |     |     |     |     |     |     |     |
| ---------- | -------- | ----- | --- | ------- | ------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
ativetoidentifytheculpritoftheanomalyandmitigatethe
| mains such | as cloud | system | operations |     | (Soldani, | Forti, | and |     |     |     |     |     |     |     |
| ---------- | -------- | ------ | ---------- | --- | --------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
problemeffectively.
| Brogi 2022), | manufacturing |     |        | processes             | (Oliveira, |     | Migue´is, |          |     |              |     |            |          |          |
| ------------ | ------------- | --- | ------ | --------------------- | ---------- | --- | --------- | -------- | --- | ------------ | --- | ---------- | -------- | -------- |
|              |               |     |        |                       |            |     |           | However, | in  | microservice |     | monitoring | systems, | only the |
| and de Moura | Borges        |     | 2023), | or telecommunications |            |     | net-      |          |     |              |     |            |          |          |
operationalvaluesofthesystemarerecorded,withoutdocu-
| works (Chen | et  | al. 2022). | For | instance, | during | the | manu- |     |     |     |     |     |     |     |
| ----------- | --- | ---------- | --- | --------- | ------ | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
mentingtherelationshipsbetweenthem.Hence,researchers
| facturing | process | of wafers, |               | if the thickness |       | of a     | wafer is |               |     |            |          |           |                 |              |
| --------- | ------- | ---------- | ------------- | ---------------- | ----- | -------- | -------- | ------------- | --- | ---------- | -------- | --------- | --------------- | ------------ |
|           |         |            |               |                  |       |          |          | have recently |     | employed   | causal   | structure | discovery-based |              |
| found to  | deviate | from       | the standard, | root             | cause | analysis | can      |               |     |            |          |           |                 |              |
|           |         |            |               |                  |       |          |          | techniques    | for | Root Cause | Analysis | (RCA)     | in              | cloud appli- |
beemployedtoidentifythespecificmanufacturingstepthat
cations(Wangetal.2023),aimingtoidentifytheunderlying
causedtheabnormalthickness.Byapplyingrootcauseanal-
causesofanomalies.Figure1illustratesaflowofRCAus-
| ysis to sensor | data | with | complex | relationships, |     | these | situa- |     |     |     |     |     |     |     |
| -------------- | ---- | ---- | ------- | -------------- | --- | ----- | ------ | --- | --- | --- | --- | --- | --- | --- |
ingthecausalstructurediscovery-basedapproach.Whenthe
Copyright©2024,AssociationfortheAdvancementofArtificial anomalydetectionalarmistriggeredbyananomalousKey
Intelligence(www.aaai.org).Allrightsreserved. Performance Indicator (KPI), engineers initially designate

thatparticularKPIasthetriggerpoint.Subsequently,they
aimtoidentifytheunderlyingrootcauseofthistriggerpoint.
Toachievethis,theyconstructacausalgraphthatestablishes
relationshipsbetweendifferentKPIs,allowingthemtopre-
ciselypinpointtheculpritoftheanomalyusingtheinsights
providedbythecausalgraph.
Ontheotherhand,theGrangercausality(Granger1969)
| analysis | is another | widely | recognized |     | approach | used | to as- |     |     |     |     |     |     |     |     |
| -------- | ---------- | ------ | ---------- | --- | -------- | ---- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
sesswhetherasetoftimeseriesxisacausalfactorforan-
| other set | of time | series | y. Granger | causality |     | has gained | at- |     |     |     |     |     |     |     |     |
| --------- | ------- | ------ | ---------- | --------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
tentionandiswidelyacknowledgedforitsadvantagesofin-
|     |     |     |     |     |     |     |     | Figure 2: | Illustrations |     | of contextual | information |     | from | the |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------------- | --- | ------------- | ----------- | --- | ---- | --- |
terpretabilityandcompatibilitywiththeemergenceofdeep same timestamps but with different contexts. The red win-
learning (Tank et al. 2022). Previous works (Nauta, Bucur, dow and green window respectively represent two distinct
andSeifert2019)utilizedtimeseriesforecastingmodelsand types of contextual information. The same timestamp with
interpreted model parameters as the relationships between differentcontextsshouldbeclose.
| variables | to establish |     | causal relationships. |     |     | However, | prior |     |     |     |     |     |     |     |     |
| --------- | ------------ | --- | --------------------- | --- | --- | -------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
approachesinneuralGrangercausaldiscoveryhavenotef-
| fectively | leveraged | the | contextual | information |     | inherent | in  |     |     |     |     |     |     |     |     |
| --------- | --------- | --- | ---------- | ----------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
temporaldata.
| The previous |     | approach | (Yue | et al. | 2022) | generated | posi- |     |     |     |     |     |     |     |     |
| ------------ | --- | -------- | ---- | ------ | ----- | --------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
tiveandnegativesamplesatinstance-wiseandtemporaldi-
mensionsforgeneratingfine-grainedrepresentationsforany
| granularity. | However, |     | we notice | that | real-world | time | series |     |     |     |     |     |     |     |     |
| ------------ | -------- | --- | --------- | ---- | ---------- | ---- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
Figure3:Anillustratedissueofnegativepairselection.
oftenexhibitmultiple-periodicity.Forinstance,thetemper-
| ature tends | to  | reach its | peak at | noon | every | day, there | is an |     |     |     |     |     |     |     |     |
| ----------- | --- | --------- | ------- | ---- | ----- | ---------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
influxofpeopleinthecityduringweekends,andelectricity
|             |               |     |           |        |     |            |     | method | for time   | series | data     | that exclusively |             | treats | iden- |
| ----------- | ------------- | --- | --------- | ------ | --- | ---------- | --- | ------ | ---------- | ------ | -------- | ---------------- | ----------- | ------ | ----- |
| consumption | significantly |     | increases | during |     | the summer | ev- |        |            |        |          |                  |             |        |       |
|             |               |     |           |        |     |            |     | tical  | timestamps | with   | distinct | contextual       | information |        | as    |
eryyear.Therefore,thisapproachmightinadvertentlytreat
timestampswiththesameperiodicityasnegativepairs,even positive pairs. This approach mitigates the problem of
thoughtheyactuallyholdsimilarsignificance. misidentifying timestamps with similar periodicity as
negativepairs,therebypreventingtheseparationofrep-
| To tackle | these | challenges, |     | we propose |     | a novel | frame- |     |     |     |     |     |     |     |     |
| --------- | ----- | ----------- | --- | ---------- | --- | ------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
resentationsfortimestampssharingthesameperiodicity.
workRUN,whichemploysaself-supervisedneuralGranger
causaldiscoveryapproachforconductingrootcauseanaly- • RUN outperforms existing state-of-the-art methods on
sis.Tocapturecontextualinformationintimeseries,weem- synthetic datasets and data generated from a real-world
ploy a self-supervised learning scheme that ensures times- application.Wefurtherconductanablationstudytovali-
tamps with diverse contexts, but the same timestamps are datetheeffectivenessofourcontrastivelearningmethod.
| learned | to exhibit | proximity, | where | we  | only | treat the | iden- |     |     |     |     |     |     |     |     |
| ------- | ---------- | ---------- | ----- | --- | ---- | --------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
tical timestamps as positive pairs for contrastive learning. 2 RelatedWork
| This way  | aims     | to prevent | the      | inclusion | of           | erroneous | in- |                                      |     |     |     |     |     |     |     |
| --------- | -------- | ---------- | -------- | --------- | ------------ | --------- | --- | ------------------------------------ | --- | --- | --- | --- | --- | --- | --- |
|           |          |            |          |           |              |           |     | 2.1 RootCauseAnalysisinMicroservices |     |     |     |     |     |     |     |
| formation | stemming | from       | negative |           | pairs. After | enhancing |     |                                      |     |     |     |     |     |     |     |
the backbone encoder to acquire improved representations, Within large organizations, the adoption of microservices
we utilize neural Granger causal discovery to explore the hasbecometheprevailingarchitectureduetoitsadvantages
causalrelationshipsamongvariables.Subsequently,wepro- in terms of enhanced scalability, simplified maintenance,
ceed to identify the root causes of the trigger point within andincreasedflexibility.Whentheanomalydetectionalarm
the acquired causal graph using Pagerank with a personal- is activated by an anomalous KPI, engineers often have to
izedvector.Comprehensiveexperimentsconductedonboth investasignificantamountoftimetopinpointtheunderly-
synthetic and real-world microservice-based datasets con- ingcausebehindthisanomaly.Consequently,theyengagein
clusivelydemonstratethatourproposedframeworkoutper- the development of automated root cause analysis systems
formsstate-of-the-artrootcauseanalysismethods. to mitigate the time spent on the investigation. ϵ-diagnosis
Ourmaincontributionsaresummarizedasfollows: (Shan et al. 2019) considers the time series of KPIs and
|     |     |     |     |     |     |     |     | computes | the similarity |     | between | them | during | normal | peri- |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | -------------- | --- | ------- | ---- | ------ | ------ | ----- |
• We propose a self-supervised neural Granger causal odsandabnormalperiods,whichservesasananomalyindi-
| discovery-based |     | root | cause | analysis | framework |     | RUN, |     |     |     |     |     |     |     |     |
| --------------- | --- | ---- | ----- | -------- | --------- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
cator.AutoMAP(Maetal.2020)utilizesthePC-algorithm
whichcapturescontextualinformationintemporaldata,
|           |           |        |               |        |              |       |     | to construct | a causality |      | graph based  | on      | the KPIs.       | It           | further |
| --------- | --------- | ------ | ------------- | ------ | ------------ | ----- | --- | ------------ | ----------- | ---- | ------------ | ------- | --------------- | ------------ | ------- |
| and then  | leverages |        | the time      | series | forecasting  | model | to  |              |             |      |              |         |                 |              |         |
|           |           |        |               |        |              |       |     | conducts     | a random    | walk | to determine |         | the candidate’s |              | root    |
| construct | a         | causal | graph between |        | multivariate | time  | se- |              |             |      |              |         |                 |              |         |
|           |           |        |               |        |              |       |     | causes.      | RCD (Ikram  | et   | al. 2022)    | employs | the             | hierarchical |         |
ries.RUNemploysPagerankonthederivedcausalgraph andlocalizedlearningalgorithm.Itdeemsthefailuresasan
toidentifytherootcauseofthetriggerpoint.
intervention,andadoptsadivide-and-conquerschemetodi-
• We introduce an innovative self-supervised learning videthevariablesintomultiplesubsetsforconductingΨ-PC

Figure 4: Overview of our proposed framework, RUN, consisting of three stages: 1) Maximizing the positive pair to capture
thecontextualinformation;2)NeuralGrangercausaldiscoverytoderivethecausalgraphfrommultivariatetimeseries;and3)
Thediagnosisstageinferstherootcausefromtheobtainedcausalgraph.
tofindinterventionaltargetsfromeachsubset. 2022)samplespositivepairswhicharethesametimestamp
Thecandidaterootcausesfromallsubsetsarethencom- withdifferentcontexts,andnegativepairswhicharediffer-
bined, and the same process is iteratively applied until ent timestamps. However, we observe that real-world time
further splitting of candidate root causes is not possible. seriesfrequentlydemonstratemultiple-periodicity.Withthe
Nonetheless, these methods rely on similarity or the PC- advancementofcontrastivelearning,(Grilletal.2020;Chen
algorithm,bothofwhichoverlooktheessentialroleoftem- and He 2021) argue that it can perform well even without
poraldependencyinrootcauseanalysis.Forinstance,when negative pairs because they aim to prevent the inclusion of
a sudden spike in CPU utilization occurs, it can lead to in- incorrect negative pairs. Hence, we propose an innovative
creased latency in other microservices, effectively encom- approachthatexclusivelyleveragesidenticaltimestampsas
passing the temporal dimension of the information. There- positive pairs for self-supervised learning. This scheme is
fore, we aim to develop a neural Granger causal discovery designed to prevent the incorporation of information from
methodthatcanleveragethetemporaldependencytoiden- negativepairs.InFigure3,wecanobservethatthetimese-
tifytherootcausesmoreaccurately. riesdataexhibitsperiodicpatterns.Therefore,ifwewereto
considerthetwocircledredpointsonthegraphasnegative
2.2 NeuralGrangerCausalDiscovery
|                      |        |          |         |                 |     |         | pairs, it would | lead to incorporating | incorrect | information |
| -------------------- | ------ | -------- | ------- | --------------- | --- | ------- | --------------- | --------------------- | --------- | ----------- |
| As deep              | Neural | Networks | (NNs)   | continue        | to  | advance | fromthem.       |                       |           |             |
| rapidly, researchers |        | have     | started | using Recurrent |     | Neural  |                 |                       |           |             |
NetworksorotherTemporalConvolutionalNetworkstoin-
3 ProblemFormulation
| fer nonlinear    | Granger | causality. |             | MSNGC | (Fan et   | al. 2023) |     |     |     |     |
| ---------------- | ------- | ---------- | ----------- | ----- | --------- | --------- | --- | --- | --- | --- |
| extracts diverse |         | causal     | information | from  | the data, | consid-   |     |     |     |     |
ering various delay ranges, and effectively integrates them Themonitoringsystemwillmonitortheoperationalstatusof
using learned attention weights. Tank et al. (2022) applies themicroservicesystemthroughKPIs,andintypicalscenar-
ios,wepinpointtherootcausewhenananomalousKPItrig-
| structured | component-wise |     | multilayer | perceptrons |     | (MLPs) |     |     |     |     |
| ---------- | -------------- | --- | ---------- | ----------- | --- | ------ | --- | --- | --- | --- |
gerstheanomalydetectionsystem.Wetermtheanomalous
| combined | with sparsity-inducing |     |     | penalties | on the | weights. |     |     |     |     |
| -------- | ---------------------- | --- | --- | --------- | ------ | -------- | --- | --- | --- | --- |
KPIasatriggerpointandsubsequentlyidentifytheunder-
| CUTS (Cheng | et  | al. 2023) | utilizes | EM-Style | joint | causal |     |     |     |     |
| ----------- | --- | --------- | -------- | -------- | ----- | ------ | --- | --- | --- | --- |
graph learning and missing data imputation for irregular lying root causes behind the trigger point. These KPIs be-
temporaldata.Nevertheless,previousworkshavenoteffec- longtomultivariatetimeseriesdata.Inthemicroservicear-
chitecture,identifyingtheunderlyingcausesfortheanomaly
| tively leveraged |     | contextual | information | in  | time series | data. |     |     |     |     |
| ---------------- | --- | ---------- | ----------- | --- | ----------- | ----- | --- | --- | --- | --- |
canbeformalizedasfollows.MultivariatetimeseriesXcon-
Asaresult,wepresentaninnovativeapproachfortimese-
|     |     |     |     |     |     |     | sists of N | features, X = [X | ,X ,...,X | ]. We collect the |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ---------------- | --------- | ----------------- |
ries contrastive learning that enables to the capture of con- 1 2 N
|     |     |     |     |     |     |     | corresponding | time series with | a specified | time period T, |
| --- | --- | --- | --- | --- | --- | --- | ------------- | ---------------- | ----------- | -------------- |
textualinformationfromidenticaltimestampsbutwithdif-
[x1,x2,...,xT],
ferentcontexts,asdepictedinFigure2. each time series can be denoted as X i =
i i i
X ∈ RN×T.WeutilizetheneuralGrangercausaldiscovery
| 2.3 ContrastiveLearning |     |     |     |     |     |     | methodtoderivethecausalgraphGˆ |     |     |     |
| ----------------------- | --- | --- | --- | --- | --- | --- | ------------------------------ | --- | --- | --- |
={V,E},wherenodes
Contrastive learning has been widely used in various do- V denoteseachfeatureX andedgesE denotesthatfeature
i
mains, such as natural language processing (NLP) (Gao, X Granger causes feature X . Our goal is to identify the
|                                               |     |     |     |     |     |     | i          |               | j              |              |
| --------------------------------------------- | --- | --- | --- | --- | --- | --- | ---------- | ------------- | -------------- | ------------ |
|                                               |     |     |     |     |     |     | root cause | X which leads | to the trigger | point within |
| Yao,andChen2021),computervision(CV)(ChenandHe |     |     |     |     |     |     |            | culprit       |                |              |
thecausalgraphGˆ.
2021),andtimeseries(Yueetal.2022).TS2Vec(Yueetal.

|                     |          | 4           | Methodology  |              |           |                 |            |     |     |     |     |     |     |     |
| ------------------- | -------- | ----------- | ------------ | ------------ | --------- | --------------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
| Our proposed        |          | framework   | is           | shown        | in Figure |                 | 4, which   |     |     |     |     |     |     |     |
| consists            | of three | stages:     | the          | pre-training |           | stage,          | the neural |     |     |     |     |     |     |     |
| Granger             | causal   | discovery   | stage,       | and          | the       | diagnosis       | stage.     |     |     |     |     |     |     |     |
| In the pre-training |          | stage,      | we           | enhance      | the       | backbone        | en-        |     |     |     |     |     |     |     |
| coder to            | generate | informative |              | time         | series    | representations |            |     |     |     |     |     |     |     |
| that incorporate    |          | contextual  | information. |              | This      | enhancement     |            |     |     |     |     |     |     |     |
| is achieved         | by       | maximizing  | the          | agreement    |           | among           | instances  |     |     |     |     |     |     |     |
withthesametimestampbutwithdifferentcontexts.Inthe
| neural Granger     |          | causal | discovery | stage,  | we             | utilize | the time  |     |     |     |     |     |     |     |
| ------------------ | -------- | ------ | --------- | ------- | -------------- | ------- | --------- | --- | --- | --- | --- | --- | --- | --- |
| series forecasting |          | model  | to        | exploit | the causal     |         | graph and |     |     |     |     |     |     |     |
| prune the          | spurious | edge   | to        | get the | final Directed |         | Acyclic   |     |     |     |     |     |     |     |
Graphs(DAGs).Inthediagnosisstage,weapplyarandom Figure5:Overviewoftimeseriesforecasting.ThereareN
walkalgorithmcalledPagerankwithapersonalizationvec- independentneuralnetworksforeachtimeseriesitopredict
torwhichrecommendsthemostlikelyrootcausesbasedon theircausalrelationships.
thecausalgraph.
4.1 Pre-trainingStage Time Series Forecasting In time series forecasting, we
|            |         |       |     |           |        |          |     | propose | N independent |     | neural network |     | f for time | series |
| ---------- | ------- | ----- | --- | --------- | ------ | -------- | --- | ------- | ------------- | --- | -------------- | --- | ---------- | ------ |
| We utilize | DLinear | (Zeng | et  | al. 2023) | as our | backbone | en- |         |               |     |                |     | θi         |        |
X tofititsdatagenerationfunction(Chengetal.2023).We
| coder for | time | series | forecasting. | In  | order | to enhance | our | i   |     |     |     |     |     |     |
| --------- | ---- | ------ | ------------ | --- | ----- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
definetheinputforourmodelbyapplyingaslidingwindow
| backbone   | encoder, | we     | design | contrastive |      | learning | without |      |             |        |                    |     |             |       |
| ---------- | -------- | ------ | ------ | ----------- | ---- | -------- | ------- | ---- | ----------- | ------ | ------------------ | --- | ----------- | ----- |
|            |          |        |        |             |      |          |         | with | a size of w | across | all the historical |     | time series | X and |
| relying on | negative | pairs. | We     | consider    | that | negative | pairs   |      |             |        |                    |     |             |       |
arenotsuitablefortimeseriesbecausetheyexhibitperiodic multiplyingwithcorrespondingattentionscoreα ni andthe
|          |             |     |        |         |           |     |           | forecastxˆ | attimestamptistheoutputoftheneuralnetwork |     |     |     |     |     |
| -------- | ----------- | --- | ------ | ------- | --------- | --- | --------- | ---------- | ----------------------------------------- | --- | --- | --- | --- | --- |
| patterns | as depicted | in  | Figure | 3. When | selecting |     | different |            | i                                         |     |     |     |     |     |
f
| timestampsasnegativepairs,itispossiblethattheybelong |     |     |     |     |     |     |     | θi  |     |     |     |     |     |     |
| ---------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
tothesameperiodicity.Ifwechoosetheincorrectnegative xˆt =f (X⊙G)=f (xt−w:t−1⊙α ,...,xt−w:t−1⊙α ),
|               |      |               |     |            |     |      |           | i   | θi  | θi  | 1   | 1i  |     | Ni  |
| ------------- | ---- | ------------- | --- | ---------- | --- | ---- | --------- | --- | --- | --- | --- | --- | --- | --- |
| pairs, it may | lead | to separating |     | embeddings |     | that | should be |     |     |     |     |     | N   |     |
i=1,2,...,N.
similar.Therefore,welearnthecontextinformationbycon-
(3)
sideringinstanceswiththesametimestampbutwithdiffer-
|     |     |     |     |     |     |     |     | An overview | of  | time series | forecasting |     | is illustrated | in 5. |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ----------- | ----------- | --- | -------------- | ----- |
entcontextsaspositivepairs.
Eachindependentneuralnetworkhasthesamearchitecture
| First,                                            | we utilize | random | cropping     |     | following | (Yue | et al. |                                             |                  |      |          |              |         |        |
| ------------------------------------------------- | ---------- | ------ | ------------ | --- | --------- | ---- | ------ | ------------------------------------------- | ---------------- | ---- | -------- | ------------ | ------- | ------ |
|                                                   |            |        |              |     |           |      |        | but a                                       | different target | time | series.  | For a neural | network | f ,    |
| 2022)byrandomlysamplingtwooverlappingtimesegments |            |        |              |     |           |      |        |                                             |                  |      |          |              |         | θi     |
|                                                   |            |        |              |     |           |      |        | thegoalistoforecastcorrespondingtimeseriesX |                  |      |          |              |         | bymin- |
| y andy                                            | ,          |        |              |     |           |      |        |                                             |                  |      |          |              |         | i      |
| 1 2                                               |            |        |              |     |           |      |        | imizingthefollowinglossfunction             |                  |      |          |              |         |        |
| y 1 =[a                                           | 1 ,b 1 ],y | 2 =[a  | 2 ,b 2 ],0<a | 1   | ≤a 2 ≤b   | 1 ≤b | 2 ≤T.  |                                             |                  |      |          |              |         |        |
|                                                   |            |        |              |     |           |      |        |                                             |                  |      | 1        | T            |         |        |
|                                                   |            |        |              |     |           |      | (1)    |                                             |                  |      | (cid:88) | (xt−xˆt)2    |         |        |
|                                                   |            |        |              |     |           |      |        |                                             | L                | =−   |          |              |         | (4)    |
The two views y and y are processed by our backbone MSE N −w i i
|     |     | 1   | 2   |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
encoder f and a projector g. To learn the contextual infor- t=w+1
| mation without |     | negative | pairs, | we utilize | the | same | schema |                      |     |     |                              |     |     |     |
| -------------- | --- | -------- | ------ | ---------- | --- | ---- | ------ | -------------------- | --- | --- | ---------------------------- | --- | --- | --- |
|                |     |          |        |            |     |      |        | CausalGraphDiscovery |     |     | Aftertrainingthenetworks,the |     |     |     |
ofSimSiam(ChenandHe2021).Wedenotethetworepre- learnable Causal Attention Matrix G can be used to inter-
| sentationsasz |     | =g(f(y | ))andp |     | =f(y | ),andmaximize |     |     |     |     |     |     |     |     |
| ------------- | --- | ------ | ------ | --- | ---- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
1 1 2 2 pret the causal relationships among time series. When α ij
| the similarity | between |     | both sides. | Here, | we  | define | our loss |     |     |     |     |     |     |     |
| -------------- | ------- | --- | ----------- | ----- | --- | ------ | -------- | --- | --- | --- | --- | --- | --- | --- |
exceedsacertainthresholdH,wecaninferthattimeseries
functionasfollows:
|     |     |     |     |     |     |     |     | X Granger | causes | X   | and add an | edge | from X | to X in |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------ | --- | ---------- | ---- | ------ | ------- |
|     |     |     |     |     |     |     |     | i         |        | j   |            |      |        | i j     |
1
L =− (cos(z ,stopgrad(p ))+cos(stopgrad(p ),z )). thecausalgraphG(cid:101),thatis
| con | 2   | 1   |     | 2   |     |     | 1 2 |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(cid:26)
|     |     |     |     |     |     |     | (2) |     |     |                | 1, ifα | >H  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------------- | ------ | --- | --- | --- |
|     |     |     |     |     |     |     |     |     |     | G(cid:101)ij = |        | ij  |     |     |
(5)
0, else
4.2 NeuralGrangerCausalDiscoveryStage
|     |     |     |     |     |     |     |     | Based | on the definition |     | of a causal | graph, | cycles | are not |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | ----------------- | --- | ----------- | ------ | ------ | ------- |
RUNrepresentsthecausalgraphasaCausalAttentionMa-
|          |      |        |         |                 |     |     |           | allowed | in the graph. | Therefore, |     | we need | to incorporate | a   |
| -------- | ---- | ------ | ------- | --------------- | --- | --- | --------- | ------- | ------------- | ---------- | --- | ------- | -------------- | --- |
| trix G = | {0 ≤ | α ij ≤ | 1, ∀i,j | ∈ [1,2,...,N]}, |     |     | where the |         |               |            |     |         |                |     |
elementα demonstratestheattentionscorefromX toX . pruningstrategytoremovespuriousedges.Wecalculatethe
|     | ij  |     |     |     |     |     | i j |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Eachelementα servesasatrainableparameter,contribut- similarityofeachedge,whichinvolvescomputingthePear-
ij
ing to identifying causal relationships among time series. soncorrelationbetweentwoconnectednodes.Subsequently,
|                                       |     |     |     |                         |      |              |     | we eliminate    | the                                  | edge with | the lowest | similarity |     | iteratively |
| ------------------------------------- | --- | --- | --- | ----------------------- | ---- | ------------ | --- | --------------- | ------------------------------------ | --------- | ---------- | ---------- | --- | ----------- |
| WedefinethefinalcausalgraphG(cid:101) |     |     |     |                         | = {g | ∈ [0,1],∀i,j | ∈   |                 |                                      |           |            |            |     |             |
|                                       |     |     |     |                         | ij   |              |     |                 | transformsintothefinalcausalgraphGˆ. |           |            |            |     |             |
| [0,1]}.Iftheattentionscoreα           |     |     |     | isbeyondacertainthresh- |      |              |     | untilG(cid:101) |                                      |           |            |            |     |             |
ij
| old, g | will be | 1, indicating |     | that time | series | X   | Granger |     |     |     |     |     |     |     |
| ------ | ------- | ------------- | --- | --------- | ------ | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
| ij     |         |               |     |           |        |     | i       |     |     |     |     |     |     |     |
causes X . The proposed neural Granger causal discov- 4.3 DiagnosisStage
j
erycomprisestwocomponents:timeseriesforecastingand In the diagnosis stage, we follow GrootRank (Wang et al.
causalgraphdiscovery. 2021)toapplyPageRankwithnodeweightpersonalization

to calculate the root cause ranking. Wang et al. (2021) ob- Dataset #ofTimeSeries #ofTimestamps
| serves that | dangling | nodes | are | more | likely | to be | the root |     |     |     |     |     |     |     |     |
| ----------- | -------- | ----- | --- | ---- | ------ | ----- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
10
| cause. Hence, |     | we customize |     | the personalization |     |     | vector as |     |     |     |     |     |     |     |     |
| ------------- | --- | ------------ | --- | ------------------- | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
20
| P and             | P , where | P            | is the  | personalization |          | score | for dan- |               |     |     |     |     |     |      |     |
| ----------------- | --------- | ------------ | ------- | --------------- | -------- | ----- | -------- | ------------- | --- | --- | --- | --- | --- | ---- | --- |
| d                 | n         | d            |         |                 |          |       |          | Syntheticdata |     |     | 30  |     |     | 2000 |     |
| gling nodes       | and       | P is         | for the | remaining       | nodes.   | In    | the case |               |     |     |     |     |     |      |     |
|                   |           | n            |         |                 |          |       |          |               |     |     | 40  |     |     |      |     |
| of tied rankings, |           | we calculate |         | the access      | distance |       | from the |               |     |     |     |     |     |      |     |
50
triggerpointtoresolvethetie.Wecalculatetheaccessdis-
| tance(AD)differentlyfromGrootRank |     |     |     |     |     |     |     | Sock-shop |     |     | 38  |     |     | 600 |     |
| --------------------------------- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
(cid:26)
D, distancefromtriggerpointtothevariable
| AD = |     |     |     |     |     |     |     | Table1:Statisticsofthesyntheticandsock-shopdatasets. |     |     |     |     |     |     |     |
| ---- | --- | --- | --- | --- | --- | --- | --- | ---------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
0, ifany“access”isnotreachable
(6)
| In GrootRank, |          | the authors | set      | the    | distance | of unreachable |          |                    |             |         |         |            |            |     |       |
| ------------- | -------- | ----------- | -------- | ------ | -------- | -------------- | -------- | ------------------ | ----------- | ------- | ------- | ---------- | ---------- | --- | ----- |
|               |          |             |          |        |          |                |          | periods            | falls below | a       | certain | confidence | threshold, |     | indi- |
| nodes as      | infinity | and         | consider | that   | shorter  | access         | distance |                    |             |         |         |            |            |     |       |
|               |          |             |          |        |          |                |          | cating significant |             | changes | in      | that       | KPI before | and | after |
| will more     | likely   | be the      | root     | cause. | However, | this may       | con-     |                    |             |         |         |            |            |     |       |
theanomalyoccurrence,itcanbeconsideredacandidate
tradicttheobservedphenomenawhichsuggestthatdangling
rootcause.
| nodes are    | more | likely          | to be | the root | cause. | Hence,       | we set |           |     |     |            |         |     |         |     |
| ------------ | ---- | --------------- | ----- | -------- | ------ | ------------ | ------ | --------- | --- | --- | ---------- | ------- | --- | ------- | --- |
|              |      |                 |       |          |        |              |        | • AutoMAP | (Ma | et  | al. 2020): | AutoMAP |     | creates | a   |
| the distance | of   | the unreachable |       | node     | as 0   | and consider | the    |           |     |     |            |         |     |         |     |
weightedcausalgraphutilizinganadaptedPCalgorithm.
biggeraccessdistancewillmorelikelybetherootcause.Fi-
|            |         |     |       |             |       |     |          | In this | graph, | the weight | of  | an edge | between | two | mi- |
| ---------- | ------- | --- | ----- | ----------- | ----- | --- | -------- | ------- | ------ | ---------- | --- | ------- | ------- | --- | --- |
| nally, RUN | outputs | the | top-k | root causes | based | on  | the root |         |        |            |     |         |         |     |     |
causeranking. croservices reflects the degree of dependence of a per-
|                        |     |             |             |     |            |         |     | formance             | metric.    | The        | process      | concludes   |              | by navigating |        |
| ---------------------- | --- | ----------- | ----------- | --- | ---------- | ------- | --- | -------------------- | ---------- | ---------- | ------------ | ----------- | ------------ | ------------- | ------ |
|                        |     |             |             |     |            |         |     | nodes through        |            | a random   | walk         | algorithm   |              | and identify- |        |
|                        |     | 5           | Experiments |     |            |         |     |                      |            |            |              |             |              |               |        |
|                        |     |             |             |     |            |         |     | ing the              | root cause | via        | the          | correlation | metric       | from          | the    |
| 5.1 ExperimentSettings |     |             |             |     |            |         |     | weightedcausalgraph. |            |            |              |             |              |               |        |
|                        |     |             |             |     |            |         |     | • RCD (Ikram         | et         | al. 2022): | RCD          | treats      | failures     | as            | inter- |
| Dataset                | As  | no publicly | available   |     | real-world | dataset | for |                      |            |            |              |             |              |               |        |
|                        |     |             |             |     |            |         |     | ventions             | on the     | nodes      | representing |             | root causes, | and           | uti-   |
rootcauseanalysisisaccessibleduetodataconfidentiality,
lizesalocalizedhierarchicallearningalgorithmtoiden-
wetestonasyntheticdatasetandatestbedutilizinganac-
tifytheserootcausesoffailure.Italsoemploysadivide-
tualmicroservice-basedapplication.
and-conquerschemetodecreasethetimerequiredforin-
| • Synthetic | data: | To  | generate | synthetic |     | data, we | follow |     |     |     |     |     |     |     |     |
| ----------- | ----- | --- | -------- | --------- | --- | -------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
ferringtherootcausefromtheentiregraph.
RCD Ikram et al. (2022) to randomly generate DAG Ψ-PC:Ψ-PCisaspecificinstanceofRCD.Ψ-PCwillac-
•
andgenerateconditionalprobabilitytables(CPT)forthe
quiretheentirecausalgraph,whichmightnotbeessen-
| normal | period | dataset. | Then, | we  | inject | failures | by ran- |     |     |     |     |     |     |     |     |
| ------ | ------ | -------- | ----- | --- | ------ | -------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
tialforrootcauseidentification.Additionally,localizing
domlychoosingonenodeastherootcauseandregener-
learningwoulddemandextratime.
atingCPTforit.Hence,wecangettheanomalousperiod
|     |     |     |     |     |     |     |     | • CausalRCA | (Xin, | Chen, | and | Zhao | 2023): | CausalRCA |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ----- | ----- | --- | ---- | ------ | --------- | --- |
datasetandcombinethemintoonecase.Finally,wealso
|         |            |     |           |        |     |          |           | uses a      | gradient-based |     | causal | structure | learning |            | method |
| ------- | ---------- | --- | --------- | ------ | --- | -------- | --------- | ----------- | -------------- | --- | ------ | --------- | -------- | ---------- | ------ |
| utilize | an anomaly |     | detection | system | to  | identify | the trig- |             |                |     |        |           |          |            |        |
|         |            |     |           |        |     |          |           | to generate | weighted       |     | causal | graphs    | and a    | root cause | in-    |
gerpoint.Thedataaregeneratedwithnodecountsof10,
ferencemethodtolocalizerootcausemetrics.
20,30,40,and50,spanningover2,000timestamps.
• Sock-shop (Daniel Holbach 2022): The framework of EvaluationMetrics Weevaluateoursolutionbytop-khit
sock-shopencompassesatotalof13microservices,each ratio(HR@k)andmeanreciprocalrank(MRR).
| developed | using        | distinct |               | technologies. |         | These microser- |     |        |            |     |             |     |         |     |         |
| --------- | ------------ | -------- | ------------- | ------------- | ------- | --------------- | --- | ------ | ---------- | --- | ----------- | --- | ------- | --- | ------- |
|           |              |          |               |               |         |                 |     | • HR@k | represents | the | probability | of  | getting | the | correct |
| vices     | are deployed |          | on individual |               | virtual | machines        | or  |        |            |     |             |     |         |     |         |
rootcausefromthetop-koutputs.
containers.Communicationamongthemoccursthrough
• MRRsumsupthereciprocaloftherankoftherootcause.
HTTP-basedAPIrequests.Additionally,thesemicroser-
Iftherootcauseisnotincludedintheoutput,itsrankcan
vicesofferasubstantialvolumeofstatisticaldatainthe
form of various metrics such as CPU and memory uti- bedeemedasinfinity,resultinginascoreofzero.
lization. Within the sock-shop dataset, ten distinct cate- ImplementationDetails Weimplementourmethodona
gories of root causes are present, each comprising five machine with AMD EPYC 7302 16-Core CPU, NVIDIA
instances. RTX A5000 graphics cards. In the time series forecasting
|           |     |         |     |             |     |          |         | stage, the | window | size | w is set | to 32. | We  | use the | Adam |
| --------- | --- | ------- | --- | ----------- | --- | -------- | ------- | ---------- | ------ | ---- | -------- | ------ | --- | ------- | ---- |
| Baselines | We  | compare | our | performance |     | with the | follow- |            |        |      |          |        |     |         |      |
(KingmaandBa2015)optimizerandsetthelearningrateas
ingbaselineapproaches:
0.001andthebatchsizeas128.Inthecausalgraphdiscov-
• ϵ-Diagnosis(Shanetal.2019):ϵ-Diagnosisanalyzesthe erystage,thethresholdH issetto0.5.Thetrainingepochs
timeseriesofKPIsandcalculatesthesimilaritybetween ofthepre-trainingandfine-tuningstagesaresetto50.Inthe
them during both normal and abnormal periods, which diagnosisstage,wesetthevalueofthepersonalizationvec-
serves as an indicator for anomalies. If the similarity of torP d as1andP n as0.5,similarto(Wangetal.2021).The
a particular KPI between normal and anomalous time kinHR@kissetto1,3,and5.

|     |     |     |     |     | CPUhog |     |     |     |     |     | Memoryleak |     |     |     |     |
| --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- |
ϵ-Diag. AMAP Ψ-PC* RCD* CausalRCA RUN ϵ-Diag. AMAP Ψ-PC* RCD* CausalRCA RUN
Carts 0.20 0.05 0.02 0.00 0.00 0.20 0.00 0.14 0.02 0.02 0.00 0.00
Catalogue 0.20 0.22 0.02 0.08 0.00 0.40 0.40 0.00 0.10 0.06 0.00 0.00
Orders 0.20 0.01 0.06 0.12 0.80 0.00 0.00 0.26 0.02 0.04 0.00 0.20
HR@1 Payment 0.60 0.07 0.06 0.04 0.00 0.40 0.20 0.01 0.02 0.02 0.00 0.00
User 0.20 0.29 0.06 0.12 0.20 0.20 0.40 0.08 0.20 0.14 0.00 0.40
Avg. 0.28 0.13 0.04 0.07 0.04 0.40 0.20 0.10 0.07 0.06 0.00 0.12
Carts 0.40 0.23 0.04 0.04 0.00 0.40 0.00 0.20 0.02 0.06 0.00 0.20
Catalogue 0.20 0.22 0.04 0.12 0.00 0.60 0.40 0.00 0.06 0.12 0.00 0.40
|     |     |     |     |     |     |     |     | 0.80 | 0.37 |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | ---- | --- | --- | --- | --- | --- | --- |
HR@3 Orders 0.20 0.36 0.06 0.30 0.00 0.00 0.06 0.14 0.00 0.20
Payment 0.60 0.07 0.06 0.12 0.00 0.40 0.20 0.05 0.02 0.16 0.00 0.40
User 0.20 0.53 0.04 0.12 0.40 0.20 0.40 0.27 0.16 0.28 0.20 0.40
Avg. 0.32 0.28 0.05 0.16 0.08 0.48 0.20 0.14 0.06 0.15 0.04 0.32
Carts 0.40 0.24 0.08 0.22 0.20 0.40 0.00 0.25 0.02 0.04 0.20 0.20
Catalogue 0.20 0.23 0.06 0.08 0.40 0.80 0.40 0.00 0.08 0.12 0.00 0.60
Orders 0.20 0.51 0.06 0.36 0.00 0.80 0.00 0.49 0.08 0.08 0.00 0.20
HR@5
Payment 0.60 0.07 0.06 0.06 0.00 0.40 0.20 0.11 0.04 0.10 0.20 0.40
User 0.20 0.55 0.06 0.34 0.40 0.20 0.40 0.30 0.20 0.28 0.20 0.40
Avg. 0.32 0.32 0.06 0.21 0.20 0.52 0.20 0.18 0.08 0.12 0.12 0.36
Table2:HR@konsock-shopdata.Boldindicatesthebestperformanceandunderlinerepresentsthesecondbestperformance.
WenotethatΨ-PC*andRCD*indicatedifferentresultscomparedwiththeoriginalpaper,wherewedirectlyrerantheexperi-
mentsfromtheofficialcodes.
|     |     |     |        |     |            |     |     | sion. This | underscores | the | importance |     | of considering |     | tem- |
| --- | --- | --- | ------ | --- | ---------- | --- | --- | ---------- | ----------- | --- | ---------- | --- | -------------- | --- | ---- |
|     |     |     | CPUhog |     | Memoryleak |     |     |            |             |     |            |     |                |     |      |
ϵ-Diag. RUN ϵ-Diag. RUN poraldependency,particularlyintimeseriesdatawithinmi-
croservicesystems.
|     | Carts     |     | 0.273 | 0.299 | 0.036 | 0.158 |     |         |         |        |        |     |      |        |      |
| --- | --------- | --- | ----- | ----- | ----- | ----- | --- | ------- | ------- | ------ | ------ | --- | ---- | ------ | ---- |
|     |           |     |       |       |       |       |     | As Ψ-PC | and RCD | cannot | output | the | rank | of the | root |
|     | Catalogue |     | 0.203 | 0.537 | 0.412 | 0.207 |     |         |         |        |        |     |      |        |      |
cause,theyareomittedforcomparingperformanceinterms
|     | Orders |     | 0.212 | 0.825 | 0.017 | 0.267 |     |     |     |     |     |     |     |     |     |
| --- | ------ | --- | ----- | ----- | ----- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ofMRR.Table3illustratestheMRRofrootcauseanalysis
MRR
|     | Payment |     | 0.613 | 0.494 | 0.437 | 0.164 |     |             |                 |        |              |             |                  |               |      |
| --- | ------- | --- | ----- | ----- | ----- | ----- | --- | ----------- | --------------- | ------ | ------------ | ----------- | ---------------- | ------------- | ---- |
|     |         |     |       |       |       |       |     | methods     | between RUN     | and    | ϵ-diagnosis. |             | The              | table clearly |      |
|     | User    |     | 0.221 | 0.264 | 0.231 | 0.443 |     |             |                 |        |              |             |                  |               |      |
|     |         |     |       |       |       |       |     | illustrates | that even       | though | our          | performance | in               | HR@1          | for  |
|     | Avg.    |     | 0.304 | 0.484 | 0.227 | 0.248 |     |             |                 |        |              |             |                  |               |      |
|     |         |     |       |       |       |       |     | Memory      | leaks is the    | second | best,        | it is       | still noticeable |               | that |
|     |         |     |       |       |       |       |     | the root    | cause maintains | a      | relatively   | high        | ranking.         | Further-      |      |
Table3:MRRonsock-shopdata. more,weobservethatRUNoutperformsϵ-diagnosissignifi-
cantly,underscoringtheimpressiveperformanceofRUNin
identifyingCPUhogincidents.
5.2 OverallPerformance
|     |     |     |     |     |     |     |     | Synthetic | Data Figure | 6   | shows | the HR@k | of  | root | cause |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ----------- | --- | ----- | -------- | --- | ---- | ----- |
analysismethodsbetweenRUNandbaselines.However,ϵ-
| Sock-shop | Table | 2   | demonstrates |     | the HR@k | of  | root |     |     |     |     |     |     |     |     |
| --------- | ----- | --- | ------------ | --- | -------- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
causeanalysismethodsbetweenRUNandbaselines,which diagnosis falls short due to the fact that synthetic data lack
|              |             |          |             |                 |             |           |         | the distinctive | behaviors               | during |                | both normal        |         | and anomaly |      |
| ------------ | ----------- | -------- | ----------- | --------------- | ----------- | --------- | ------- | --------------- | ----------------------- | ------ | -------------- | ------------------ | ------- | ----------- | ---- |
| demonstrates |             | that our | proposed    | model           | achieves    | at        | least a |                 |                         |        |                |                    |         |             |      |
|              |             |          |             |                 |             |           |         | periods         | that are characteristic |        | of             | microservice-based |         |             | data |
| 63%          | improvement | in CPU   | hog,        | and 80%         | improvement |           | in      |                 |                         |        |                |                    |         |             |      |
|              |             |          |             |                 |             |           |         | when anomalies  | occur.                  | Since  | the            | synthetic          | dataset | is          | gen- |
| Memory       | leak        | compared | with the    | best-performing |             | baseline. |         |                 |                         |        |                |                    |         |             |      |
|              |             |          |             |                 |             |           |         | erated using    | the function            |        | of generateCPT |                    | in      | PyAgrum,    | it   |
| Considering  | baselines,  |          | ϵ-diagnosis | outperforms     |             | other     | base-   |                 |                         |        |                |                    |         |             |      |
lines because the root cause in the sock-shop data exhibits mightnotfullyexhibitthecharacteristicsoftimeseriesdata.
BothΨ-PCandRCD,ontheotherhand,learncausalgraphs
distinctbehaviorsduringnormalandanomalyperiods.Au-
|          |             |               |               |        |       |           |        | using the | PC-algorithm | from   | these       | synthetic |              | datasets. | As   |
| -------- | ----------- | ------------- | ------------- | ------ | ----- | --------- | ------ | --------- | ------------ | ------ | ----------- | --------- | ------------ | --------- | ---- |
| toMAP’s  | performance |               | is suboptimal | in     | some  | cases     | due to |           |              |        |             |           |              |           |      |
|          |             |               |               |        |       |           |        | a result, | they exhibit | better | performance |           | on synthetic |           | data |
| the fact | that        | it constructs | the           | causal | graph | utilizing | PC-    |           |              |        |             |           |              |           |      |
whencomparedtothesock-shopdata.However,ourmodel
| algorithm, | which, | however, | overlooks |     | the temporal |     | depen- |     |     |     |     |     |     |     |     |
| ---------- | ------ | -------- | --------- | --- | ------------ | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
dency.AlthoughweadheretothesettingsusedinRCD,Ψ- is specifically designed for performing root cause analysis
PCandRCDyieldvaryingrootcausesineachrunandper- withinmicroservicesystemsconsistingofabundanttimese-
|      |          |               |          |     |           |          |     | ries data, | making it | less suitable |     | for application |     | to the | syn- |
| ---- | -------- | ------------- | -------- | --- | --------- | -------- | --- | ---------- | --------- | ------------- | --- | --------------- | --- | ------ | ---- |
| form | worse on | the sock-shop | dataset. |     | CausalRCA | neglects |     |            |           |               |     |                 |     |        |      |
theticdataset.Nonetheless,ourapproachstilldemonstrates
temporalinformationwithintimeseriesdata,leadingtosub-
competitiveperformancewithbothRCDandΨ-PC.
optimalperformanceinsock-shop.ThecomparisonofRUN
| and causal | discovery-based |     | approaches |     | reveals | the signifi- |     |     |     |     |     |     |     |     |     |
| ---------- | --------------- | --- | ---------- | --- | ------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
canceoftemporaldependency.RUNleveragespositivepairs 5.3 AblationStudy
whichcapturethecontextualinformation,andappliesneural Todissectthecontributionsarisingfromdifferentdesignsof
Granger causal discovery to consider the temporal dimen- RUN, we conducted an ablation study by omitting the pre-

|     |     | (a)HR@1 |     |     |     |     | (b)HR@3 |     |     |     |     | (c)HR@5 |     |     |
| --- | --- | ------- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | ------- | --- | --- |
Figure6:HR@konasyntheticdataset
|     |     |     |     |     |     |     |     | Figure 8: | Construct | the | causal | graph from | the | multivariate |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | --------- | --- | ------ | ---------- | --- | ------------ |
timeseries.
|     |     |     |     |     |     |     |     | dangling | node and | impacts | the | trigger | point. Our | approach |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | -------- | ------- | --- | ------- | ---------- | -------- |
Figure7:Ablationstudyremovingthepre-trainingstageand validatestheobservationandsuccessfullyidentifiestheroot
incorporatingthenegativepairsincontrastivelearning. cause from the causal graph. It also illustrates the neural
Grangercausaldiscovery-basedapproachinexplaininghow
toidentifytherootcause.
| training | stage and | incorporating |     | the | consideration |     | of nega- |     |     |     |     |     |     |     |
| -------- | --------- | ------------- | --- | --- | ------------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
tive pairs in contrastive learning on sock-shop data for its 6 Conclusion
| microservice-based |       | architecture. |          | The | results          | are presented |       |                |     |         |     |     |             |          |
| ------------------ | ----- | ------------- | -------- | --- | ---------------- | ------------- | ----- | -------------- | --- | ------- | --- | --- | ----------- | -------- |
|                    |       |               |          |     |                  |               |       | In this paper, | we  | propose | RUN | for | identifying | the root |
| in Figure          | 7. As | expected,     | removing |     | the pre-training |               | stage |                |     |         |     |     |             |          |
significantly results in a notable reduction in the perfor- causesinmicroservices.ExistingworksapplyPC-algorithm
|          |      |      |           |      |                 |     |      | on time series | data | which | leads    | to overlooking |        | the tempo- |
| -------- | ---- | ---- | --------- | ---- | --------------- | --- | ---- | -------------- | ---- | ----- | -------- | -------------- | ------ | ---------- |
| mance of | RUN. | This | indicates | that | when performing |     | root |                |      |       |          |                |        |            |
|          |      |      |           |      |                 |     |      | ral dimension  | of   | data. | Distinct | from these     | works, | our pro-   |
causeanalysisvianeuralGrangercausaldiscovery,incorpo-
|     |     |     |     |     |     |     |     | posed method | is  | able to | capture | the temporal |     | dependency. |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ------- | ------- | ------------ | --- | ----------- |
ratingcontextualinformationcaneffectivelyelevateperfor-
BasedonneuralGrangercausaldiscoveryarchitecture,our
| mance. Nevertheless, |     | excluding |     | the | incorporation |     | of nega- |     |     |     |     |     |     |     |
| -------------------- | --- | --------- | --- | --- | ------------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
tivepairsincontrastivelearningdoesnotleadtoasubstan- model learns the graph structure using a time series fore-
tial decrease in performance. We theorize that this finding castingmodel.However,previousworksonneuralGranger
causaldiscoverydidnotleveragetheinherentcontextualin-
| can be ascribed |             | to the | limited      | temporal | extent   | of the | sock-    |                  |         |        |             |        |             |             |
| --------------- | ----------- | ------ | ------------ | -------- | -------- | ------ | -------- | ---------------- | ------- | ------ | ----------- | ------ | ----------- | ----------- |
|                 |             |        |              |          |          |        |          | formation        | in time | series | data.       | Hence, | contrastive | learning    |
| shop data,      | potentially |        | constraining | the      | capacity | to     | identify |                  |         |        |             |        |             |             |
|                 |             |        |              |          |          |        |          | without negative |         | pairs  | is proposed | to     | leverage    | the context |
themulti-periodicitywithinthetemporaldomain.
oftimeseriestoenhancerepresentationsoftimeseries.The
quantitativeanalysiscarriedoutonbothsyntheticandsock-
5.4 CaseStudy:NeuralGrangerCausal
|     |     |     |     |     |     |     |     | shop datasets | showcases |     | the effectiveness |     | of our | proposed |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --------- | --- | ----------------- | --- | ------ | -------- |
Discovery
approachcomparedtostate-of-the-artbaselines.Forourfu-
InordertoinvestigatetheefficacyofneuralGrangercausal turework,weintendtoenhancethescalabilityofourmodel
discovery,wesampleacausalgraphinwhicheachnodehas to accommodate datasets of varying sizes. This improve-
a pathway to the root cause. In Figure 8, the yellow node ment is crucial as it will allow us to not only build upon
represents the trigger point and the red node represents the theexperimentsconductedonthesock-shopdatasetbutalso
rootcause.Figure8representscausalrelationshipsthatare extend our research to larger-scale and more representative
associatedwithtemporalorderbasedonGrangercausality. datasets.Theselargerdatasetswillprovideamorecompre-
To identify the root cause, each edge is reversed from the hensive understanding of our model’s performance in real-
original causal graph for PageRank analysis. According to worldscenarios,furtherenrichingthedepthandapplicabil-
theobservationfromWangetal.(2021),therootcauseisa ityofourfindings.

References Soldani, J.; Forti, S.; and Brogi, A. 2022. Failure Root
|     |     |     |     |     |     |     |     | CauseAnalysisforMicroservices,Explained. |     |     | InDAIS,vol- |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------------------------------- | --- | --- | ----------- |
Chen,B.;Yu,L.;Luo,W.;Wu,C.;Li,M.;Tan,H.;Huang,
J.; and Wan, Z. 2022. Hybrid tree model for root cause ume 13272 of Lecture Notes in Computer Science, 74–91.
Springer.
| analysisofwirelessnetworkfaultlocalization. |     |     |     |     |     | WebIntell., |     |     |     |     |     |
| ------------------------------------------- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- |
Tank,A.;Covert,I.;Foti,N.J.;Shojaie,A.;andFox,E.B.
20(3):213–223.
|                       |     |     |                            |     |     |     |     | 2022. NeuralGrangerCausality. |     | IEEETrans.PatternAnal. |     |
| --------------------- | --- | --- | -------------------------- | --- | --- | --- | --- | ----------------------------- | --- | ---------------------- | --- |
| Chen,X.;andHe,K.2021. |     |     | ExploringSimpleSiameseRep- |     |     |     |     |                               |     |                        |     |
Mach.Intell.,44(8):4267–4279.
| resentation | Learning. |     | In CVPR, | 15750–15758. |     | Computer |     |     |     |     |     |
| ----------- | --------- | --- | -------- | ------------ | --- | -------- | --- | --- | --- | --- | --- |
VisionFoundation/IEEE. Wang, D.; Chen, Z.; Ni, J.; Tong, L.; Wang, Z.; Fu, Y.;
|             |           |                                      |           |         |      |         |         | and Chen,                                   | H. 2023. Hierarchical | Graph Neural | Networks |
| ----------- | --------- | ------------------------------------ | --------- | ------- | ---- | ------- | ------- | ------------------------------------------- | --------------------- | ------------ | -------- |
| Cheng,      | Y.; Yang, | R.;                                  | Xiao, T.; | Li, Z.; | Suo, | J.; He, | K.; and |                                             |                       |              |          |
|             |           |                                      |           |         |      |         |         | forCausalDiscoveryandRootCauseLocalization. |                       |              | CoRR,    |
| Dai,Q.2023. |           | CUTS:NeuralCausalDiscoveryfromIrreg- |           |         |      |         |         |                                             |                       |              |          |
abs/2302.01987.
InICLR.OpenReview.net.
ularTime-SeriesData.
Wang,H.;Wu,Z.;Jiang,H.;Huang,Y.;Wang,J.;Ko¨pru¨,S.;
| DanielHolbach.2022. |     |     | Sock-shop,amicroservicedemoap- |     |     |     |     |             |                 |                   |          |
| ------------------- | --- | --- | ------------------------------ | --- | --- | --- | --- | ----------- | --------------- | ----------------- | -------- |
|                     |     |     |                                |     |     |     |     | and Xie, T. | 2021. Groot: An | Event-graph-based | Approach |
plication. GitHubrepository. forRootCauseAnalysisinIndustrialSettings.InASE,419–
429.IEEE.
| Fan,C.;Wang,Y.;Zhang,Y.;andOuyang,W.2023. |     |     |     |     |     |     | Inter- |     |     |     |     |
| ----------------------------------------- | --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- |
pretable Multi-Scale Neural Network for Granger Causal- Xin, R.; Chen, P.; and Zhao, Z. 2023. CausalRCA: Causal
ity Discovery. In ICASSP 2023-2023 IEEE International inferencebasedprecisefine-grainedrootcauselocalization
Conference on Acoustics, Speech and Signal Processing formicroserviceapplications. J.Syst.Softw.,203:111724.
(ICASSP),1–5.IEEE.
Yue,Z.;Wang,Y.;Duan,J.;Yang,T.;Huang,C.;Tong,Y.;
Gao,T.;Yao,X.;andChen,D.2021. SimCSE:SimpleCon- and Xu, B. 2022. TS2Vec: Towards Universal Representa-
InEMNLP(1),
trastiveLearningofSentenceEmbeddings. tionofTimeSeries. InAAAI,8980–8987.AAAIPress.
6894–6910.AssociationforComputationalLinguistics. Zeng,A.;Chen,M.;Zhang,L.;andXu,Q.2023.AreTrans-
|          |       |       |               |     |        |           |     | formers Effective | for Time Series | Forecasting? | In AAAI, |
| -------- | ----- | ----- | ------------- | --- | ------ | --------- | --- | ----------------- | --------------- | ------------ | -------- |
| Granger, | C. W. | 1969. | Investigating |     | causal | relations | by  |                   |                 |              |          |
econometricmodelsandcross-spectralmethods. Economet- 11121–11128.AAAIPress.
rica:journaloftheEconometricSociety,424–438. Zhang, C.; Peng, X.; Sha, C.; Zhang, K.; Fu, Z.; Wu,
Grill,J.;Strub,F.;Altche´,F.;Tallec,C.;Richemond,P.H.; X.; Lin, Q.; and Zhang, D. 2022. DeepTraLog: Trace-
Buchatskaya, E.; Doersch, C.; Pires, B. A´.; Guo, Z.; Azar, Log Combined Microservice Anomaly Detection through
M.G.;Piot,B.;Kavukcuoglu,K.;Munos,R.;andValko,M. Graph-basedDeepLearning. InICSE,623–634.ACM.
| 2020. Bootstrap          |              | Your | Own Latent |     | - A New | Approach | to      |     |     |     |     |
| ------------------------ | ------------ | ---- | ---------- | --- | ------- | -------- | ------- | --- | --- | --- | --- |
| Self-SupervisedLearning. |              |      | InNeurIPS. |     |         |          |         |     |     |     |     |
| Ikram, A.;               | Chakraborty, |      | S.; Mitra, | S.; | Saini,  | S. K.;   | Bagchi, |     |     |     |     |
S.;andKocaoglu,M.2022.RootCauseAnalysisofFailures
| inMicroservicesthroughCausalDiscovery. |        |     |                 |     |       | InNeurIPS. |     |     |     |     |     |
| -------------------------------------- | ------ | --- | --------------- | --- | ----- | ---------- | --- | --- | --- | --- | --- |
| Kingma,                                | D. P.; | and | Ba, J. 2015.    |     | Adam: | A Method   | for |     |     |     |     |
| StochasticOptimization.                |        |     | InICLR(Poster). |     |       |            |     |     |     |     |     |
Liu,D.;He,C.;Peng,X.;Lin,F.;Zhang,C.;Gong,S.;Li,
| Z.; Ou,    | J.; and      | Wu, | Z. 2021.       | MicroHECL: |              | High-Efficient |      |     |     |     |     |
| ---------- | ------------ | --- | -------------- | ---------- | ------------ | -------------- | ---- | --- | --- | --- | --- |
| Root Cause | Localization |     | in Large-Scale |            | Microservice |                | Sys- |     |     |     |     |
tems. InICSE(SEIP),338–347.IEEE.
Ma,M.;Xu,J.;Wang,Y.;Chen,P.;Zhang,Z.;andWang,P.
| 2020. AutoMAP: |                | Diagnose | Your | Microservice-based |          |     | Web   |     |     |     |     |
| -------------- | -------------- | -------- | ---- | ------------------ | -------- | --- | ----- | --- | --- | --- | --- |
| Applications   | Automatically. |          |      | In WWW,            | 246–258. |     | ACM / |     |     |     |     |
IW3C2.
| Nauta,M.;Bucur,D.;andSeifert,C.2019. |                 |     |               |     |        | CausalDiscov- |     |     |     |     |     |
| ------------------------------------ | --------------- | --- | ------------- | --- | ------ | ------------- | --- | --- | --- | --- | --- |
| ery with                             | Attention-Based |     | Convolutional |     | Neural | Networks.     |     |     |     |     |     |
Mach.Learn.Knowl.Extr.,1(1):312–340.
| Oliveira, | E. E.; | Migue´is, | V.  | L.; and | de Moura | Borges, | J.  |     |     |     |     |
| --------- | ------ | --------- | --- | ------- | -------- | ------- | --- | --- | --- | --- | --- |
L.C.2023.Automaticrootcauseanalysisinmanufacturing:
| an overview | &   | conceptualization. |     | J.  | Intell. | Manuf., | 34(5): |     |     |     |     |
| ----------- | --- | ------------------ | --- | --- | ------- | ------- | ------ | --- | --- | --- | --- |
2061–2078.
| Shan, H.;             | Chen, | Y.; | Liu, H.;                    | Zhang, | Y.; Xiao, | X.; | He, X.; |     |     |     |     |
| --------------------- | ----- | --- | --------------------------- | ------ | --------- | --- | ------- | --- | --- | --- | --- |
| Li,M.;andDing,W.2019. |       |     | ?-Diagnosis:Unsupervisedand |        |           |     |         |     |     |     |     |
Real-timeDiagnosisofSmall-windowLong-tailLatencyin
| Large-scaleMicroservicePlatforms. |     |     |     |     | InWWW,3215–3222. |     |     |     |     |     |     |
| --------------------------------- | --- | --- | --- | --- | ---------------- | --- | --- | --- | --- | --- | --- |
ACM.