Guietal./ FrontInform TechnolElectron Eng 202526(9):1551-1576 1551
Frontiers ofInformation Technology& ElectronicEngineering
www.jzus.zju.edu.cn;engineering.cae.cn;www.springerlink.com
ISSN 2095-9184(print); ISSN 2095-9230(online)
E-mail: jzus@zju.edu.cn
Review:
Deep anomaly detection oftemporal heterogeneous
data in AIOps: asurvey∗
JiayiGUI†§,ZhongnanMA†§,HaoZHOU,YanSU,MiaoruZHANG,KeYU†‡,XiaofeiWU
School of ArtificialIntelligence,BeijingUniversityof Posts and Telecommunications, Beijing100876, China
†E-mail:hypatia@bupt.edu.cn; zhongnanma@bupt.edu.cn; yuke@bupt.edu.cn
Received June 1, 2024; Revisionaccepted Nov. 18, 2024; Crosschecked Aug. 1,2025; PublishedonlineSept. 10, 2025
Abstract: The advancement of the fifth generation (5G) mobile communication and Internet of Things (IoT) has
facilitated the development of intelligent applications, but has also rendered these networks increasingly complex
and vulnerable to various targeted attacks. Numerous anomaly detection (AD) models, particularly those using
deep learning technologies, have been proposed to monitor and identify network anomalous events. However, the
implementation of these models poses challenges for network operators due to lacking expert knowledge of these
black-boxsystems. Inthisstudy,wepresentacomprehensivereviewofcurrentADmodelsandmethodsinthefield
of communication networks. Wecategorize these models intofour methodological groups based on theirunderlying
principlesandstructures,withparticularemphasisontheroleofrecentpromisinglargelanguagemodels(LLMs)in
thefield of AD.Additionally, weprovidea detailed discussion of themodels in thefollowing fourapplication areas:
network traffic monitoring, networking system log analysis, cloud and edge service provisioning, and IoT security.
Based on these application requirements, we examine the current challenges and offer insights into future research
directions, includingrobustness, explainability,and theintegration of LLMsfor AD.
Key words: Anomaly detection;AIOps;Large language models; Communication networks
https://doi.org/10.1631/FITEE.2400467 CLC number:TP3
1 Introduction of connected devices required for these intelligent
applications.
Theadventofthefifthgeneration(5G)andthe
Recent incidents, such as the border gateway
convergenceofartificialintelligencehaverevolution-
protocol (BGP) routing error by Abrams (2020),
ized Internet applications, enabling a symbiotic re-
widespread outages by Heinle (2022) and KYODO
lationship between the physical and digital realms,
NEWS (2022), and cellular phone outage across US
and further ushering in an era of digital and intel-
byMontgomery(2024),indicatethesusceptiblevul-
ligent transformation across various sectors (Zhang
nerabilitiesofcurrentnetworkmanagementsystems.
P et al., 2019; IMT-2030 (6G) Promotion Group,
Thus,there is anurgentdemand fortransitionfrom
2021). However,thistransformationbringsunprece-
traditionalhuman-centricmanagementtointelligent
dented challenges to network management due to
and automatic operational management technolo-
the increasingly complex network structures, the
gies, which can ensure secure and efficient network
vast volume of network traffic, and the multitude
performance.
‡ Correspondingauthor In this context, the concept of artificial intel-
§ Thesetwo authorscontributedequallytothiswork
ligence for information technology (IT) operations
* Project supported by the National Natural Science Founda-
tion of China (No. 62371057) and the 111 Project of China (AIOps) (Dang YN et al., 2019) has been proposed
(No. B08004)
to manage the complexity and scale of modern In-
ORCID: KeYU, https://orcid.org/0000-0002-1158-1483
(cid:3)c ZhejiangUniversityPress2025 ternet systems. AIOps aims to develop automated

1552 Guietal./FrontInform TechnolElectron Eng 202526(9):1551-1576
| anomaly | detection | (AD) | models | capable |     | of pro- | specificdetails. |     |     |     |     |     |     |
| ------- | --------- | ---- | ------ | ------- | --- | ------- | ---------------- | --- | --- | --- | --- | --- | --- |
cessing complex, voluminous data streams, identi- The scope of this study is to provide a compre-
fying emergent patterns of anomalies, and remain- hensivereviewofcurrentADmodels,especiallydeep
ing resilient against the ever-changing landscape learningmodels,includingthosebasedonLLMs,and
of network threats. The emergence of large lan- to introduce their specific applications in the field
guage models (LLMs) has introduced novel solu- of wireless communication networks. Specifically,
| tions for | AIOps | development. |     | Recent | studies | show |            |        |     |         |         |             |       |
| --------- | ----- | ------------ | --- | ------ | ------- | ---- | ---------- | ------ | --- | ------- | ------- | ----------- | ----- |
|           |       |              |     |        |         |      | this study | covers |     | network | traffic | monitoring, | which |
that LLMs excel in pattern recognition and rea- involvessophisticatedpatternrecognitiontechniques
soning across complex token sequences. Beyond toidentifydeviationsfromnormativedataflows,net-
| traditional | natural | language | tasks, | LLMs | can | inte- |     |     |     |     |     |     |     |
| ----------- | ------- | -------- | ------ | ---- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
workingsystemloganalysis,whichparsesandinter-
grate text and time-series data to effectively per- pretsvastlogstodetectaberrantbehaviorsandsys-
form time-series forecasting and AD (Su et al., temstates,cloud andedge computing serviceprovi-
2024). Time-LLM (Jin et al., 2024b) demonstrates sioning,tailoredtoenergy-limiteddevicestodevelop
remarkable performance in time-series forecasting AD models, and Internet of Things (IoT) security,
| tasks by | reprogramming |     | time-series |     | data into | tex- |       |          |           |     |        |              |      |
| -------- | ------------- | --- | ----------- | --- | --------- | ---- | ----- | -------- | --------- | --- | ------ | ------------ | ---- |
|          |               |     |             |     |           |      | which | monitors | malicious |     | sensor | and actuator | data |
tualformatssuitableforLLMsandleveragingmetic- inindustrialnetworks.
ulouslycraftedtextprompts. Toaddresstime-series The contributions of our study can be summa-
| AD, TS-BERT |     | (Dang | WX et | al., 2021) | introduces |     |     |     |     |     |     |     |     |
| ----------- | --- | ----- | ----- | ---------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
rizedasfollows:
thepretrainingandfine-tuningparadigm,effectively
|     |     |     |     |     |     |     | 1.  | The | survey | presents | the first | comprehensive |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | -------- | --------- | ------------- | --- |
overcomingthechallengeofmodelinglong-rangede- content on AD in AIOps within the communication
| pendencies.    | As  | demonstrated |          | in Fig. | 1,     | the reg- |                           |     |     |     |           |     |             |
| -------------- | --- | ------------ | -------- | ------- | ------ | -------- | ------------------------- | --- | --- | --- | --------- | --- | ----------- |
|                |     |              |          |         |        |          | domain,providingaholistic |     |     |     | viewofthe |     | fieldandits |
| ular procedure |     | of AD        | in AIOps | for     | secure | com-     |                           |     |     |     |           |     |             |
applications.
| munication | system | monitoring |     | can be | divided | into |     |     |        |        |        |               |       |
| ---------- | ------ | ---------- | --- | ------ | ------- | ---- | --- | --- | ------ | ------ | ------ | ------------- | ----- |
|            |        |            |     |        |         |      | 2.  | The | survey | delves | deeply | into critical | AIOps |
datacollection,datapreparationandrepresentation,
scenarioswithinthecommunicationdomain,suchas
| data analysis        | and | fusion, | and      | pattern | recognition |     |           |         |             |      |            |               |            |
| -------------------- | --- | ------- | -------- | ------- | ----------- | --- | --------- | ------- | ----------- | ---- | ---------- | ------------- | ---------- |
|                      |     |         |          |         |             |     | network   | traffic | monitoring, |      | networking |               | system log |
| and decision-making. |     |         | Although | several | survey      | pa- |           |         |             |      |            |               |            |
|                      |     |         |          |         |             |     | analysis, | cloud   | and         | edge | service    | provisioning, | and        |
pers(Cooketal.,2020;LiGandJung,2023;Zhong
|     |     |     |     |     |     |     | IoT security. |     | We  | provide | thorough | analysis | and de- |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --- | --- | ------- | -------- | -------- | ------- |
et al., 2023; Su et al., 2024) have reviewed the im- tailedexplanationsforeachscenario.
| plementation | of       | AD models, | they          | either | lack    | com-   |             |     |           |             |                 |          |       |
| ------------ | -------- | ---------- | ------------- | ------ | ------- | ------ | ----------- | --- | --------- | ----------- | --------------- | -------- | ----- |
|              |          |            |               |        |         |        | 3.          | The | survey    | establishes | a comprehensive |          | cat-  |
| prehensive   | coverage | of         | technologies, |        | such as | recent |             |     |           |             |                 |          |       |
|              |          |            |               |        |         |        | egorization |     | framework | that        | includes        | specific | meth- |
LLM-basedmethods,ordonotdescribeapplication- ods and detailedintroductions to datasets,enabling
AlOps application
Pattern recognition
and decision-making
|     |     |     | Traffic monitoring |     |     | Fault diagnosis   | Service provisioning |                |     | Network intrusion |           | ... |     |
| --- | --- | --- | ------------------ | --- | --- | ----------------- | -------------------- | -------------- | --- | ----------------- | --------- | --- | --- |
|     |     |     | and forecasting    |     |     | and root analysis |                      | and management |     |                   | detection |     |     |
AlOps model
Data analysis
and fusion
|     |     |     |     |     |     | Machine learning |     | Deep learning |     |     | LLMs |     |     |
| --- | --- | --- | --- | --- | --- | ---------------- | --- | ------------- | --- | --- | ---- | --- | --- |
Statistical analysis
AlOps data
Data preparation
and representation Network traffic  CDRs  System logs  KPIs  Operation trajectories  XData
Network
infrastructure
Data collection
Fig.1 AIOps frameworkwithdataprocessing forcommunicationnetworks. CDRs: calldetailrecords

Guietal./ FrontInform TechnolElectron Eng 202526(9):1551-1576 1553
researchers and practitioners to navigate the field subsequentanalysis,andarecrucialforunderstand-
moreeffectively. ing network performance and detecting anomalies.
4. The surveyintroduces and discusses the cur- Data preprocessing addresses the missing data im-
rent approaches and future directions of leveraging putation,normalization,andslidingwindowstopre-
LLMs for AD in AIOps within the communication parethe dataforanalysis. Atthe featureextracting
domain,highlightingtheirpotentialto revolutionize stage, key features are extracted from the prepro-
the field. By identifying key challenges and oppor- cessed data to capture underlying patterns in the
tunities in explainability, robustness, and the inte- network. Temporal features (e.g., time-based pat-
gration of LLMs, we provide valuable insights and terns in network traffic), spectral features (e.g., fre-
guidanceforfutureresearcheffortsinADforAIOps. quencydomaincharacteristics),andspatialfeatures
|     |     |     |     |     |     |     | (e.g., | topology-related |     | network | behaviors) | are iden- |
| --- | --- | --- | --- | --- | --- | --- | ------ | ---------------- | --- | ------- | ---------- | --------- |
2 Overview tified. The model training stage uses the collected
datasettotrainarangeoftechniquesaimedatiden-
AIOps introduces innovative approaches, and tifyingunusualorabnormalpatternsinthe network
|          |     |            |     |         |           |     | behavior. |     | These models | include | statisticalmethods, |     |
| -------- | --- | ---------- | --- | ------- | --------- | --- | --------- | --- | ------------ | ------- | ------------------- | --- |
| presents | new | challenges |     | for the | evolution | of  | com-      |     |              |         |                     |     |
munication networks, highlighting the need for a machine learning methods, deep learning methods,
thorough understanding of the workflow of intelli- and LLMs, which have recently been applied to an-
|      |               |     |          |     |              |     | alyze | network | logs | and time-series | data | more effec- |
| ---- | ------------- | --- | -------- | --- | ------------ | --- | ----- | ------- | ---- | --------------- | ---- | ----------- |
| gent | communication |     | systems. | As  | demonstrated |     | in    |         |      |                 |      |             |
Fig. 2, the pipeline of AIOps in the communica- tively. Finally, the model deploying stage applies
tion network can be divided into the following five these models to real-world network tasks, such as
stages: data collection, data preprocessing, feature traffic monitoring, log analysis, cloud and edge ser-
extracting, model training, and model deploying. viceprovisioning,andIoT security.
Data collection gatherskey metrics such as network The survey is structured as follows: Section 3
keyperformanceindicators(KPIs),trafficdata,and definesanomalyandAD,andcomparesthescopeof
logs. These datasets serve as the foundation for our study with related works. Section 4 discusses
Missing data imputation
|     |     |     | Data collection |     |     |     |     |     |     |     | Data |     |
| --- | --- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- | ---- | --- |
preprocessing
|     |     | Text |     | Network KPI |     | Network traffic |     |     |     |     |     |     |
| --- | --- | ---- | --- | ----------- | --- | --------------- | --- | --- | --- | --- | --- | --- |
Normalization
Log
Sliding window
|     |     |     |     |     |     |     |     | x   | x x   | x x x | x x x |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | ----- | ----- | --- |
|     |     |     |     |     |     |     |     |     | 1 2 3 | 4 5 6 | 7 8 9 |     |
Window size=5
Feature extracting
|     |     |     |     |     |     |     |     | Temporal |     | Spectral | Spatial |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | -------- | ------- | --- |
features
|     |     |     |     |     |     |     |     |     |     | features | features |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | -------- | --- |
Parametric
|     | Model    |     | Statistical |     |               |     |     |     |     |                 |     |     |
| --- | -------- | --- | ----------- | --- | ------------- | --- | --- | --- | --- | --------------- | --- | --- |
|     | training |     |             |     | Nonparametric |     |     |     |     | Model deploying |     |     |
Machine learning
Network traffic monitoring
Supervised
Methods
|     |     |     | Deep learning |     | Semi-supervised |     |     |     | Networking system log analysis |     |     |     |
| --- | --- | --- | ------------- | --- | --------------- | --- | --- | --- | ------------------------------ | --- | --- | --- |
Unsupervised
Cloud and edge service provisioning
General LLMs
LLMs
IoT security
Time-series LLMs
|     |     |     |     | Fig.2 | Pipelineof |     | AIOps incommunicationnetwork |     |     |     |     |     |
| --- | --- | --- | --- | ----- | ---------- | --- | ---------------------------- | --- | --- | --- | --- | --- |

1554 Guietal./FrontInform TechnolElectron Eng 202526(9):1551-1576
categorization frameworks, current methods, and tect. Collectiveanomaliesconsistofdatapointsthat
datasets. Section 5 explores AD for network traffic graduallyformadivergentpatternovertime,requir-
monitoring with datasets and methods. Section 6 ing long-termcontextanalysisto identify the devia-
focusesonnetworkingsystemloganalysis. Section7 tion from normal behavior. Other researchers have
examinesADforcloudandedgeserviceprovisioning. identified five key data-oriented dimensions to de-
Section 8 discusses AD for IoT security. Section 9 scribe anomaly types and subtypes as follows: data
projectschallengesnowadaysandfuturetrends,em- type, relationship cardinality, anomaly level, data
phasizing interpretability, robustness, and the use distribution, and data structure. These dimensions
of LLMs. Section 10 concludes with a summary of help classify and characterize anomalies in network
| insights. |     |     |     |     |     |     | data. The                            | data | type | distinguishes |     | among        | quantita- |
| --------- | --- | --- | --- | --- | --- | --- | ------------------------------------ | ---- | ---- | ------------- | --- | ------------ | --------- |
|           |     |     |     |     |     |     | tive,qualitative,andmixedattributes. |      |      |               |     | Therelation- |           |
3 Background shipcardinalitydifferentiatesbetweentheunivariate
|     |     |     |     |     |     |     | and multivariate |     | relationships. |     | The | anomaly | level |
| --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | -------------- | --- | --- | ------- | ----- |
3.1 ADdefinition categorizes anomalies as atomic (individual cases)
|     |     |     |     |     |     |     | or aggregate |     | (groups | or collective |     | patterns). | The |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ------- | ------------- | --- | ---------- | --- |
AD is a prevalent and crucial topic across dif- data distribution examines the collection and pat-
ferent domains and applications. Hawkins (1980) terns of attribute values, further refining anomaly
|     |     |     |     |     |     |     | classification. |     | Finally, | the data | structure |     | considers |
| --- | --- | --- | --- | --- | --- | --- | --------------- | --- | -------- | -------- | --------- | --- | --------- |
providedanearlydefinitionofanomaly,oroutlier.
Definition 1 An outlier is an observation that formats such as log data and time series. Conse-
deviates so much from other observations as to quently, the definition of anomalies varies slightly
arouse suspicion that it was generated by a differ- depending onthe specific applicationdomain.
entmechanism.
3.2 Problemformulation
Definition1implicitlypresupposestheexistence
ofa norm-generatingmechanismthatproducesnor-
|                 |               |                 |            |            |            |           | The                   | collected     | data       | can          | be denoted        |        | as X =  |
| --------------- | ------------- | --------------- | ---------- | ---------- | ---------- | --------- | --------------------- | ------------- | ---------- | ------------ | ----------------- | ------ | ------- |
| mal, or         | nonanomalous, |                 | data       | points.    | Anomalies, | in        |                       |               |            |              |                   |        |         |
|                 |               |                 |            |            |            |           | [x ,x                 | ,...,x        | ],         | X ∈          | RD×N,x            | ∈      | RD, N   |
|                 |               |                 |            |            |            |           | 1 2                   | N             | where      |              |                   | i      | is      |
| terms of        | features      | and             | data       | patterns,  | exhibit    | signifi-  |                       |               |            |              |                   |        |         |
|                 |               |                 |            |            |            |           | the numberofsamples,R |               |            | isthe        | setofrealnumbers, |        |         |
| cant deviations |               | from            | this norm. | Therefore, |            | the pro-  | D                     |               |            |              |                   |        |         |
|                 |               |                 |            |            |            |           | and                   | is the        | number     | of features. |                   | In the | context |
| cess of         | AD entails    | identifying     |            | patterns   | in         | data that |                       |               |            |              |                   |        |         |
|                 |               |                 |            |            |            |           | of AD,                | the collected |            | data can     | be in             | either | tempo-  |
| diverge         | from          | the anticipated |            | behaviors  |            | (Chandola |                       |               |            |              |                   |        |         |
|                 |               |                 |            |            |            |           | ral formats           | (e.g.,        | univariate |              | and multivariate  |        | time-   |
etal.,2009).
|     |     |     |     |     |     |     | series data) | or  | non-temporal |     | formats | (e.g., | tabular |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ------------ | --- | ------- | ------ | ------- |
In communication networks, AD primarily fo- and graph data). The task of AD is to find a map
| cuses on | the | analysis | of  | KPIs that | reflect | various |          | :RD |     |           |     |      |              |
| -------- | --- | -------- | --- | --------- | ------- | ------- | -------- | --- | --- | --------- | --- | ---- | ------------ |
|          |     |          |     |           |         |         | function | f   | →R, | such that | y n | =f(x | n ); the bi- |
aspects of network performance. These KPIs, such y = 1 (n = 1,2,...,N)
|                |     |          |        |       |       |           | nary variable                          |     | n   |     |     | indicates | that |
| -------------- | --- | -------- | ------ | ----- | ----- | --------- | -------------------------------------- | --- | --- | --- | --- | --------- | ---- |
| as throughput, |     | latency, | packet | loss, | error | rate, and |                                        |     |     |     |     |           |      |
|                |     |          |        |       |       |           | thesampleispredictedtobeananomaly,andy |     |     |     |     |           | =0   |
n
| quality | of experience |     | (QoE), | serve | as essential | met- |                  |     |        |           |     |     |     |
| ------- | ------------- | --- | ------ | ----- | ------------ | ---- | ---------------- | --- | ------ | --------- | --- | --- | --- |
|         |               |     |        |       |              |      | indicatesthatthe |     | sample | isnormal. |     |     |     |
ricsforevaluatingtheefficiency,reliability,andover-
| all performance |     | of network |     | infrastructure. |     | By mon- |     |     |     |     |     |     |     |
| --------------- | --- | ---------- | --- | --------------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
3.3 Relatedworks
| itoring | these | indicators,networkadministrators |     |     |     | can |     |     |     |     |     |     |     |
| ------- | ----- | -------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
optimizeoperations,andensurehigh-qualityservice. SeveralsurveyshaveaddressedADtasks,meth-
Since KPIs are predominantly time-series data, the ods, and applications according to Table 1. Cook
followingthreemaintypesofanomaliesarerelevant: et al. (2020) examined IoT data’s challenges and
point, contextual, and collective (Choi et al., 2021). methods for detecting anomalies in univariate and
Point anomalies are individual data points or se- multivariate time series. Our survey expands be-
quencesthatdeviatesharplyfromthenormalrange, yond IoT to include network traffic, logs, cloud and
often due to sensor errors or abnormal operations, edge services, and so on, offering a broader applica-
and are detected by comparing values against con- tion scope. Li G and Jung (2023) categorized three
trol limits. Contextual anomalies involve a group anomalytypesinmultivariateseries,focusingonap-
of points that do not contain extreme values, but plications suchas fraud andfault detection. In con-
alter the signal’s shape, making them harder to de- trast,ourstudydelvesdeeperintotheAIOpsdomain

Guietal./ FrontInform TechnolElectron Eng 202526(9):1551-1576 1555
in communication systems, incorporating a wider methods, deep learning methods, and LLMs, which
range of methods, including traditional machine willbe discussedlater.
| learning | and statistical |     | approaches, |     | not just | deep |     |     |     |     |     |     |     |
| -------- | --------------- | --- | ----------- | --- | -------- | ---- | --- | --- | --- | --- | --- | --- | --- |
learning. While Zhonget al.(2023)extensivelycov- 4 Methodology
| ered AIOps | AD  | separately | in  | univariate | and | multi- |     |     |     |     |     |     |     |
| ---------- | --- | ---------- | --- | ---------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
variatedata,theymisseddetailedclassificationsand In this section, we introduce practical meth-
| introduction | of  | application | domains |     | within | AIOps. |     |         |               |       |         |      |       |
| ------------ | --- | ----------- | ------- | --- | ------ | ------ | --- | ------- | ------------- | ----- | ------- | ---- | ----- |
|              |     |             |         |     |        |        | ods | for AD. | We categorize | these | methods | into | three |
Su et al. (2024) summarized LLM methodologies, main categories as follows: statistical methods, ma-
their effectivenesscomparedto traditionalmethods, chinelearningmethods,anddeeplearningmethods.
| and their | challenges. |     | Our survey, | distinctively, |     | fo- |       |     |              |               |      |     |         |
| --------- | ----------- | --- | ----------- | -------------- | --- | --- | ----- | --- | ------------ | ------------- | ---- | --- | ------- |
|           |             |     |             |                |     |     | Given | the | recent trend | of leveraging | LLMs |     | for AD, |
cusesoncutting-edgeresearchintoLLMapplications wealsoprovidea separatediscussiononLLM-based
in varied domains, providing a comprehensive and methods, including both general practical applica-
specializedexamination. tions andtime-seriesspecific implementations. This
Our survey encompasses the following four ap- study presents Table 2 to enhance the understand-
plication domains, as illustrated in Fig. 3: network ing of the advantagesand disadvantagesof different
traffic monitoring, networking system log analysis, methods. To respect the originaltext, the letters of
cloud and edge service provisioning, and IoT secu- the formulas appearing are not otherwise modified,
rity. These domains are built on foundational mod- and the relevant meaning is given each time they
| els, including | statistical |     | methods, | machine | learning |                           | appear. |     |     |     |             |     |     |
| -------------- | ----------- | --- | -------- | ------- | -------- | ------------------------- | ------- | --- | --- | --- | ----------- | --- | --- |
|                |             |     | Table1   |         | Thescope | ofrelatedworksandourpaper |         |     |     |     |             |     |     |
|                |             |     | Datatype |         |          | Methodology               |         |     |     |     | Application |     |     |
Reference
|                |           |     | Time    |             |         | Machine  | Deep     |     | Traffic  | Log      | Cloud | and      |         |
| -------------- | --------- | --- | ------- | ----------- | ------- | -------- | -------- | --- | -------- | -------- | ----- | -------- | ------- |
|                |           |     | Log     | Statistical |         |          |          |     | LLMs     |          |       |          | IoT     |
|                |           |     | series  |             |         | learning | learning |     | analysis | analysis | edge  | services |         |
| Cook etal.     | (2020)    |     | (cid:2) |             | (cid:2) | (cid:2)  | (cid:2)  |     |          |          |       |          | (cid:2) |
| Li GandJung    | (2023)    |     | (cid:2) |             |         |          | (cid:2)  |     |          |          |       |          | (cid:2) |
| Zhong et       | al.(2023) |     | (cid:2) |             | (cid:2) | (cid:2)  | (cid:2)  |     |          |          |       |          |         |
| Suet al.(2024) |           |     | (cid:2) |             |         |          | (cid:2)  |     | (cid:2)  |          |       |          |         |
Ours (cid:2) (cid:2) (cid:2) (cid:2) (cid:2) (cid:2) (cid:2) (cid:2) (cid:2) (cid:2)
Applications
|     |     | Network traffic monitoring |     |     |     |     |     | Networking system log analysis |     |     |     |     |     |
| --- | --- | -------------------------- | --- | --- | --- | --- | --- | ------------------------------ | --- | --- | --- | --- | --- |
Traffic feature Intrusion Network KPI Log dimension Log semantic Log anomaly Failure prediction
extraction detection monitoring reduction representation detection and diagnosis
|     |     |     | Cloud and edge service provisioning |             |     |        |     |     |     | loT security |     |     |     |
| --- | --- | --- | ----------------------------------- | ----------- | --- | ------ | --- | --- | --- | ------------ | --- | --- | --- |
|     |     |     |                                     | Cloud-based |     | Cross- |     |     |     |              |     |     |     |
Service system Cloud log computing environment Real-time CPS attack Data privacy Interpretable
|     | maintenance |     | analysis |     |          |              | monitoring |     | detection |     | models |     |     |
| --- | ----------- | --- | -------- | --- | -------- | ------------ | ---------- | --- | --------- | --- | ------ | --- | --- |
|     |             |     |          |     | security | adaptability |            |     |           |     |        |     |     |
Foundation models
Data anomaly detection
|     |     | Statistical |                |               | Machine learning  |                      |                           | Deep learning |                          | LLM methods |                 |     |     |
| --- | --- | ----------- | -------------- | ------------- | ----------------- | -------------------- | ------------------------- | ------------- | ------------------------ | ----------- | --------------- | --- | --- |
|     |     | methods     |                |               | methods           |                      |                           |               | methods                  |             |                 |     |     |
|     |     |             | N o n -        | S u p p o r t | B a y es i a n De | c is ion             | N e a re s t              |               | S e m i -                | G e n er al | Tim e - se ries |     |     |
|     |     | Parametric  | par a m e tric | v e c to r    |                   |                      | n e ig h b o r Supervised | sup           | e r vi s ed Unsupervised |             |                 |     |     |
|     |     |             |                | m a c h i n e | n e tw o r k      | t re e               |                           |               |                          | L L M s     | L L M s         |     |     |
|     |     |             |                |               | Fig.3             | Structureofthesurvey |                           |               |                          |             |                 |     |     |

1556 Guietal./FrontInform TechnolElectron Eng 202526(9):1551-1576
Table2 Summaryofadvantagesanddisadvantagesoftime-seriesanomalydetection(AD)methods
| Method | Reference | Advantage |     |     | Disadvantage |
| ------ | --------- | --------- | --- | --- | ------------ |
Gaussian LuoandZhong,2017 Captures multimodal distribution of Complexparametertuningandsensitiveto
mixture data. Suitable for complex distribu- initialization. High computational com-
| model |     | tionAD |     | plexityforhigh-dimensionaldata |     |
| ----- | --- | ------ | --- | ------------------------------ | --- |
Histogram BansodandNandedkar, Simple and easy to implement. Good Limited in capturing complex patterns.
analysis 2020 fordetectingglobaldistributionshifts Not suitable for detecting local anoma-
liesinhigh-dimensionaldata
Markovian Lüdtkeetal.,2020 Captures hidden structures and state Depends on the number of states and the
model transitions. Suitablefornoisy initial parameter selection. Poor perfor-
|     |     | sequences |     | manceonlong-termdependencies |     |
| --- | --- | --------- | --- | ---------------------------- | --- |
Kernel Aboubacar and El Machk- Nonparametricandflexibleincapturing Sensitivetobandwidthselection. Poorper-
density ouri,2020 complex data distributions. Effective formancewithhigh-dimensionaldata
| estimator |     | forsmallandcontinuousdatasets |     |     |     |
| --------- | --- | ----------------------------- | --- | --- | --- |
Isolation LiuFTetal.,2008 Scales well to high-dimensional data. Limited flexibility in handling complex
forest Noneedfordatastandardization time series. Less effective for strongly
|     |     |     |     | correlated | timeseries |
| --- | --- | --- | --- | ---------- | ---------- |
One-class Ameretal.,2013; Handles nonlinear distributions. Effec- Sensitive to parameter selection and high
SVM SongJetal.,2013; tiveforsmallsamplesizes computationalcomplexity. Longtraining
|     | Chandetal.,2016 |     |     | time |     |
| --- | --------------- | --- | --- | ---- | --- |
Clustering SongJetal.,2013 Identifiessimilargroupsindata. Appli- Depends on distance metrics and high
|     |     | cableforunsupervisedAD |     | complexity. | Difficult to handle high- |
| --- | --- | ---------------------- | --- | ----------- | ------------------------- |
dimensionalanddynamicdata
Nearest Pajouhetal.,2017 Intuitive and easy to implement. Non- Highly sensitive to the choice of the dis-
neighbor parametric and does not require as- tance metric. Suffers from the “curse of
|     |     | sumptionsaboutdatadistribution |     | dimensionality” |     |
| --- | --- | ------------------------------ | --- | --------------- | --- |
Bayesian Smithetal.,2010; Models probabilistic relationships be- Computationally intensive for large
network Mascaroetal.,2014 tween variables. Can handle uncer- datasets. Requires expert knowledge for
|     |     | taintyandmissingdatawell |     | structure | learning |
| --- | --- | ------------------------ | --- | --------- | -------- |
LSTM Hundman et al., 2018; Le Captures long and short-term depen- Longtrainingtimeandhighcomputational
et al.,2019; Gao Setal., dencies. Effective on complex time cost. Complex model tuning and sensi-
|     | 2020;Leeetal.,2020 | series |     | tivetohyperparameters |     |
| --- | ------------------ | ------ | --- | --------------------- | --- |
Active ZhangXetal.,2019a; Reduces labeling cost by selecting the Reliesonagoodinitialmodeltostartwith.
learning RenPZetal.,2021 most informative data points. Im- Maystruggleinimbalanceddatasets
provesmodelefficiency
Transfer ZhangXetal.,2019a; Leverages pretrained models and re- May not perform well when the source
learning ZhangSLetal.,2021 ducestheneedforlargedatasets. Can and target domains are too different.
Zhuangetal.,2021; generalizewellacrosstasks Requires significant fine-tuning in some
cases
Autoencoder ChenZMetal.,2018; Captures nonlinear features. Effective Sensitiveto overfitting. Complexarchitec-
XuHWetal.,2018; inunsupervisedtasks tureandhyperparameter tuning
LiuCetal.,2022
GAN LiDetal.,2019b; Cangeneraterealisticsyntheticdatafor Sensitive to hyperparameters. High com-
Audibertetal.,2020 AD. Effective in modeling complex putational cost, and requires a large
|     |     | distributions |     | amountoftrainingdata |     |
| --- | --- | ------------- | --- | -------------------- | --- |
Transformer Tulietal.,2022 Captures long-range dependencies well. Requires large datasets for effective train-
|     |     | Efficienttrainingusingparallelization |     | ing. Complexity | in model architecture |
| --- | --- | ------------------------------------- | --- | --------------- | --------------------- |
andtuning
CNN RenHSetal.,2019; Parallel processing of long sequences Poor performance on nonstationary data.
|     | Heetal.,2020 | and fast training. | Captures | time de- Sensitivetonoise |     |
| --- | ------------ | ------------------ | -------- | ------------------------- | --- |
pendencieseffectively
General ChenZHetal.,2023; Effective at understanding patterns in High computational resources required for
LLMs Gruveretal.,2024; sequential data. Suitable for struc- training. Challenging to transfer time
Jinetal.,2024b; tured, unstructured, and mixed data seriesintonatural language
|     | XueandSalim,2024 | types |     |     |     |
| --- | ---------------- | ----- | --- | --- | --- |
Time-series Changetal.,2024; Tailored for time-series prediction and Requires clean data for training, unlike
LLMs Ekambaram etal.,2024; AD.Efficientprocessingwithreduced LLMs which are more flexible with raw
GaoSHetal.,2024 computationalcostscomparedtogen- data. Limited generalization beyond
|     |     | eralLLMs |     | time-seriestasks |     |
| --- | --- | -------- | --- | ---------------- | --- |

Guietal./ FrontInform TechnolElectron Eng 202526(9):1551-1576 1557
4.1 Statistical methods complexityofthedata. Onerepresentativeapproach
ishistogramanalysis(BansodandNandedkar,2020),
4.1.1 Parametricmethods
which uses frequency of occurrences to capture nor-
malbehaviorpatterns. Histogramanalysisefficiently
Parametric models (Kourtis et al., 2016) as-
handles low-dimensional univariate data, but faces
sume that the data are sampled from a known dis-
challenges as dimensions increase. Kernel density
tribution. During training, the model parameters
estimators (KDEs) (Aboubacar and El Machkouri,
are estimated using statistical techniques applied to
2020) employ a collection of distributed kernels to
the training data. These models are well-suited for
estimate the probability density function over the
large datasets since their complexity is independent
data space. To estimate an unknown density func-
of data size, enabling fast testing and evaluation.
tion f, the KDE is defined as follows (Aboubacar
However,accuratedistributionassumptionsarecru-
andEl Machkouri,2020):
cial,requiringpriorknowledgeofthedata. Gaussian
(cid:3) (cid:4)
distribution is commonly assumed (Luo and Zhong, 1 (cid:2)n x−x
2017) for both univariate and multivariate continu- fˆ h (x)= nh K h i , (3)
i=1
ousdata,withmeanandcovarianceestimatedusing
the maximum likelihood estimation. For categor- where x i (i = 1,2,...,n) denotes the independent
ical data, multinomial distributions are often used samples drawn from a distribution with density f,
(Reynolds,2009),formulatedby K represents the kernel function, and h > 0 is a
smoothingparameterknownasthe bandwidth.
(cid:2)K
P(x|θ)= α k φ(x|θ k ), (1) 4.2 Machine learningmethods
k=1
Machine learning is capable of effectively iden-
where K represents the number of sub-Gaussian
tifying patterns in data, specifically in the context
models in the mixture model, α k denotes the prob-
of AD, where it distinguishes between the normal
ability that the data belong to the kth submodel,
patterns and the significantly deviating abnormal
and φ(x|θ k ) is the probability density function of
patterns. In recent years, a lot of techniques based
the Gaussian distribution for the kth submodel
on isolation forest, support vector machine (SVM),
(Reynolds,2009),specificallygivenby
Bayesiannetworks,clustering,andthenearestneigh-
(cid:3) (cid:4)
φ(x|θ k )= σ √ 1 2π exp − (x− 2σ μ 2 k )2 . (2) borh I a so v l e at b i e o e n n fo p r r e o s p t o ( s L e i d u f F o T r A et D a . l.,2008)isanADal-
k k
gorithmthatisolatesobservationsbycreatingbinary
Here, x is the one-dimensional data, μ k is the
trees. It identifies outliers based on their shorter
mean value of the kth Gaussian component, and
path lengths in the trees, making it effective for
σ2 is the variance of the kth Gaussian component.
k high-dimensional datasets. SVM has been used for
Sequential data can be modeled using Markovian
AD (Ratschet al.,2002)to learnaboundary region
models (Lüdtke et al., 2020). In real-world appli-
containing the training instances. To effectively ad-
cations, datasets often exhibit random and diverse
dress complex, nonlinear relationships in data, the
distributions, making a single model insufficient to
Gaussian kernel function is widely employed. It
capture the true underlying statistical characteris-
is mathematically defined as follows (Ratsch et al.,
tics. In such cases, a mixture of multiple models is
2002):
commonlyassumed(AhmedMetal.,2016),andthe (cid:3) (cid:4)
|x −x |2
p op a t r i a m m i e z t e e d r . sandmodelweightcoefficients arejointly K(x i ,x j )=exp − i 2σ2 j . (4)
4.1.2 Nonparametricmethods In this expression, x i and x j represent the in-
put data vectors, while σ is a parameter that gov-
The nonparametric method (Kourtis et al., erns the width of the kernel. The Gaussian kernel
2016)differsfromparametricmethodsasitdoesnot function facilitates the transformation of data into
make assumptions about data distributions. These ahigher-dimensionalspace,therebyenabling the ef-
methods adapt their complexity to fit the size and fectiveseparationofdatapointsthatarenotlinearly

1558 Guietal./FrontInform TechnolElectron Eng 202526(9):1551-1576
separable in the original feature space. Extensions algorithms mentioned above. For example, Chand
of the basic technique have been developed to en- et al. (2016) designed a model based on SVM and
hanceone-classSVMs(Ameretal.,2013). Bayesian random forest for intrusion detection. Song J et al.
networks are used for AD in the multi-class setting. (2013) developed a practical unsupervised AD sys-
Several variations of the basic technique have been tembasedonSVMandclustering. Similarly,Pajouh
proposed that capture the conditional dependencies etal.(2017)designedahierarchicalADsystembased
betweenthedifferentattributesusingmorecomplex onNaiveBayesandthe K-nearestneighbors.
Bayesiannetworks(Smithetal.,2010;Mascaroetal.,
|     |     |     |     |     |     |     | 4.3 Deeplearningmethods |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----------------------- | --- | --- | --- | --- | --- | --- |
2014). Clusteringandthenearestneighbormethods
| are commonly |     | used | approaches | in  | AD. Clustering |     |     |     |     |     |     |     |     |
| ------------ | --- | ---- | ---------- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
methods partition the data into K clusters by min- 4.3.1 Supervisedmethods
C
| imizing | the intra-cluster |     | variance. |     | For cluster | k,  |     |     |     |     |     |     |     |
| ------- | ----------------- | --- | --------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
its centroid µ is calculated as follows (Rokach and Supervisedmethodsrequirelabeleddatapoints
k
|     |     |     |     |     |     |     | in the training |     | dataset | to learn | the | distinctions | be- |
| --- | --- | --- | --- | --- | --- | --- | --------------- | --- | ------- | -------- | --- | ------------ | --- |
Maimon,2005):
|     |     |     |     | (cid:2) |     |     | tween the | normal | and | anomalous |     | instances | using |
| --- | --- | --- | --- | ------- | --- | --- | --------- | ------ | --- | --------- | --- | --------- | ----- |
1
|     |     | µ = |     | x   | ,   |     |                |     |               |     |            |         |     |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ------------- | --- | ---------- | ------- | --- |
|     |     | k   |     | i   |     | (5) | discriminative |     | or generative |     | algorithms | (Esling | and |
|C |
|     |     |     | k   | xi∈C |     |     | Agon, 2012). |     | In terms | of the | overall | accuracy, | su- |
| --- | --- | --- | --- | ---- | --- | --- | ------------ | --- | -------- | ------ | ------- | --------- | --- |
k
where|C |isthenumberofdatapointsinthecluster, pervisedADistheoreticallysuperiorduetoitsclear
k
|      |              |     |                             |     |     |     | understandingofnormalityandabnormality. |     |     |     |     |     | Neural |
| ---- | ------------ | --- | --------------------------- | --- | --- | --- | --------------------------------------- | --- | --- | --- | --- | --- | ------ |
| andx | isthedatainC |     | k. Theobjectiveofclustering |     |     |     |                                         |     |     |     |     |     |        |
i
|     |     |     |     |     |     |     | network | models, | particularly |     | multi-layer | perceptron |     |
| --- | --- | --- | --- | --- | --- | --- | ------- | ------- | ------------ | --- | ----------- | ---------- | --- |
istominimizethesumofsquareddistancesbetween
|           |       |     |              |           |     |         | (MLP)         | and recurrent |                        | neural | networks | (RNNs), | are |
| --------- | ----- | --- | ------------ | --------- | --- | ------- | ------------- | ------------- | ---------------------- | ------ | -------- | ------- | --- |
| each data | point | and | its assigned | centroid. |     | The ob- |               |               |                        |        |          |         |     |
|           |       |     |              |           |     |         | knownfortheir |               | robustnessandaccuracy. |        |          |         |     |
jectivefunctionisformulatedasfollows(Rokachand
| Maimon,2005): |     |          |         |     |     |     | MLP,         | a feedforward |     | neural          | network | with    | mul-    |
| ------------- | --- | -------- | ------- | --- | --- | --- | ------------ | ------------- | --- | --------------- | ------- | ------- | ------- |
|               |     |          |         |     |     |     | tiple hidden | layers,       |     | can effectively |         | capture | complex |
|               |     | (cid:2)K | (cid:2) |     |     |     |              |               |     |                 |         |         |         |
J = (cid:5)x −µ (cid:5)2, time dependencies and correlationswithin the data.
|     |     |         |     | i   | k   | (6) |        |           |      |      |        |           |     |
| --- | --- | ------- | --- | --- | --- | --- | ------ | --------- | ---- | ---- | ------ | --------- | --- |
|     |     | k=1xi∈C |     |     |     |     | On the | contrary, | RNNs | have | gained | attention | in  |
k
|                |          |                |                   |             |                  |          | time-series     | forecasting |             | due           | to their | ability      | to re-  |
| -------------- | -------- | -------------- | ----------------- | ----------- | ---------------- | -------- | --------------- | ----------- | ----------- | ------------- | -------- | ------------ | ------- |
| K              |          |                |                   |             | µ                |          |                 |             |             |               |          |              |         |
| where          | is the   | number         | of                | clusters,   | k is             | the cen- |                 |             |             |               |          |              |         |
|                |          |                |                   |             |                  |          | tain memory     | states      |             | from previous |          | time steps.  | The     |
| troidofcluster |          | C k,and(cid:5) | x                 | −µ (cid:5)2 | is the Euclidean |          |                 |             |             |               |          |              |         |
|                |          |                |                   | i k         |                  |          |                 |             |             |               |          |              |         |
|                |          |                |                   | x           |                  | µ        | long short-term |             | memory      | (LSTM)        |          | model, a     | variant |
| distance       | between  | the            | point             | i and       | the centroid     | k.       |                 |             |             |               |          |              |         |
|                |          |                |                   |             |                  |          | of RNN,         | has         | introduced  | innovative    |          | solutions    | and     |
| The nearest    |          | neighbor       | method            | relies      | on a             | distance |                 |             |             |               |          |              |         |
|                |          |                |                   |             |                  |          | demonstrated    |             | exceptional | performance   |          | in forecast- |         |
| metric to      | identify | the            | nearestneighbors. |             | A common         |          |                 |             |             |               |          |              |         |
ingtime-seriesdatawithlong-termtemporaldepen-
|            |     |           |          | d(x,x | )         |     |         |        |            |     |      |             |        |
| ---------- | --- | --------- | -------- | ----- | --------- | --- | ------- | ------ | ---------- | --- | ---- | ----------- | ------ |
| choice is  | the | Euclidean | distance |       | i between |     | a       |        |            |     |      |             |        |
|            |     |           |          |       |           |     | dencies | (Le et | al., 2019; | Gao | S et | al., 2020). | Previ- |
| test point | x   | and a     | training | point | x (Rokach | and |         |        |            |     |      |             |        |
i
|     |     |     |     |     |     |     | ous studies | (Hundman |     | et al., | 2018;Lee | et al., | 2020) |
| --- | --- | --- | --- | --- | --- | --- | ----------- | -------- | --- | ------- | -------- | ------- | ----- |
Maimon,2005):
haveshownthatLSTMoutperformsmanyotherap-
(cid:5)
(cid:6)
(cid:6)(cid:2)m proachesandneuralnetworksin terms ofprediction
)=(cid:7)
|     | d(x,x |     |     | (x −x | )2, | (7) |           |     |     |     |     |     |     |
| --- | ----- | --- | --- | ----- | --- | --- | --------- | --- | --- | --- | --- | --- | --- |
|     |       | i   |     | j     | ij  |     | accuracy. |     |     |     |     |     |     |
j=1
|     |     |     |     |     |     |     | Another |     | significant | category |     | of supervised |     |
| --- | --- | --- | --- | --- | --- | --- | ------- | --- | ----------- | -------- | --- | ------------- | --- |
m
where is the number of features. Other dis- methodsistheconvolutionalneuralnetwork(CNN).
tancemetrics,suchasManhattandistanceorcosine CNNs are particularly effective in capturing tem-
similarity, can also be employed depending on the poral features. Additionally, they possess unique
application. characteristics such as parameter sharing and per-
Clustering can be particularly useful when the mutation invariance,which helps reduce complexity
underlying structure of normal data points is well- and enhances robust representation learning. The
defined, and distinct clusters can be formed. On MTAD-TF (He et al., 2020) uses a CNN to capture
the contrary, the nearest neighbor methods can be temporal patterns and a graph attention network
moreeffectivewhenanomaliesareisolatedandhave (GAT) to model spatial correlations, subsequently
a few neighbors. Many models enhance the perfor- integratingspatiotemporalfeaturesthrougha gated
| manceofADbycombiningvariousmachinelearning |     |     |     |     |     |     | RNN. |     |     |     |     |     |     |
| ------------------------------------------ | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- |

Guietal./ FrontInform TechnolElectron Eng 202526(9):1551-1576 1559
4.3.2 Semi-supervisedmethods PUAD (ZhangSL etal.,2021) addresses label up-
datechallengesusingpositive-unlabeled(PU) learn-
Semi-supervised methods offer a promising ap-
ing (Zhang JQ et al., 2019). It pretrains a lin-
proach in academic research, as they allow re-
ear model on the positive set, and employs active
searchers to harness the precision and effectiveness
learning-based self-training with a random forest
of supervised learning (SL) while alleviating the la-
classifier. The classifier identifies negative and po-
borioustaskofmanuallabeling. Thesefunctionsare
tentialpositivesamplesintheunlabeledset,verified
achievedbyintegratingauxiliarytechniques,suchas
by operators. This iterative process continues until
active learning andtransfer learning,into the learn-
sufficientlabeledsamplesareobtained.
ing process.
Activelearning(RenPZetal.,2021)reducesla- 4.3.3 Unsupervisedmethods
belingworkloadbyselectinginformativesamplesfor
Unsupervisedtechniquesaretypicallyemployed
annotation. The model is iteratively trained on la-
in situations where no prior knowledge of the data
beleddataandevaluatedonunlabeleddatatoiden-
labels is available. A typical example of this ap-
tify the most valuable samples. For instance, ac-
proach is AD based on autoencoders (AEs) (Chen
tive transfer AD (ATAD) (Zhang X et al., 2019a)
ZMetal.,2018). AnAEgenerallyconsistsofthefol-
combines active learning and transfer learning tech-
lowing two primary components: an encoder, which
niques. It extracts general features from labeled
compressesthe inputdata,andadecoder,whichre-
and unlabeled time series, employing instance- and
constructstheinputbyminimizingthedifferencebe-
feature-based transfer learning methods to train a
tween the original and reconstructed vectors. Vari-
base detection model. Active learning recommends
ational autoencoders (VAEs) extend AEs by intro-
informative samples for manual labeling, improving
ducingaprobabilisticmodel,allowingthemtogener-
performancebyconsideringuncertaintyandcontext
atenewsamplesresemblingtheinputdatabylearn-
diversity. ATADtargetshigh-precisionADwithlim-
ing the data’s distribution (Xu HW et al., 2018).
ited labeleddata,suchascross-datasettasks.
Conditionalvariationalautoencoders(C-VAEs) fur-
Transferlearning(Zhuangetal.,2021)leverages
ther enhance VAEs by incorporating external vari-
knowledge from pretrained models to enhance per-
ables,suchastimestamps,tobettercaptureanoma-
formance on related target tasks. In this context,
lies related to time-dependent information (Liu C
maximummeandiscrepancy(MMD) is employedto
et al., 2022). Another example is the various gener-
align the distributions of the source and target do-
ativemodels,suchasgenerativeadversarialnetwork
mains. Minimizing MMD helps mitigate domain
(GAN) (Li D et al., 2019b; Audibert et al., 2020)
shift, thereby improving model performance in the
and Transformer (Tuli et al., 2022). These gener-
target domain. Mathematically, MMD is defined as
ative models develop the normal data distribution,
follows(Zhuangetal.,2021):
and instances that do not conform to this distribu-
MMD(P
s
,P
t
) tionaredetectedas anomalies.
(8)
=(cid:5)E [φ(X )]−E [φ(X )](cid:5)2, Other methods, such as spectral residual CNN
Xs∼Ps s Xt∼Pt t
(SR-CNN) (Ren HS et al., 2019), use a CNN di-
where P s and P t are the source and target dis- rectly on the output of the SR model. The SR
tributions, respectively, and φ is a feature map- algorithm involves applying the Fourier transform
ping function. In this study, E Xs∼Ps [φ(X s )] denotes to obtain the log amplitude spectrum, calculating
the expectation of the feature mappings of samples the spectral residual, and then applying the inverse
X s drawn from the source distribution P s, while Fourier transform to return to the time domain.
E
Xt∼Pt
[φ(X
t
)]denotestheexpectationofthefeature The Fourier transform can be formulated as follows
mappings of samples X t drawn from the target dis- (BochnerandChandrasekharan,1949):
tribution P t. By fine-tuning the pretrained models N(cid:2)−1
on a small labeled dataset, transfer learning adapts X(f)=F{x(t)}= x(t)e−j2πft/N, (9)
to specific tasks and capitalizes on prior knowledge, t=0
effectively reducing the need for extensive labeled where x(t) represents the time-series data, X(f) is
data and minimizing training time. For instance, theFouriertransformofthetimeseries,andN isthe

1560 Guietal./FrontInform TechnolElectron Eng 202526(9):1551-1576
number ofsamples in the time series. By employing 4.4.2 Time-seriesLLMs
aCNNasits discriminativemodelarchitecture,SR-
In the realm of time series, a specialized sub-
CNN simplifies the learning process compared with
set of LLMs is gaining prominence, tailored specif-
thatusing the originaltime series.
ically for temporal data processing. These models
4.4 LLM methods are adept at handling sequences, and are increas-
ingly used for tasks such as forecasting, detecting
4.4.1 GeneralLLMs anomalies, classifying, and performing imputation.
By leveraging architectures that excel at capturing
General LLMs encompass a diverse array of
long-term dependencies, such as RNNs, LSTMs as
models, including open-source options such as
mentioned above, and more recently Transformer-
LLaMA (Touvron et al., 2023a, 2023b), GLM (Du
based models that possess parameters over 0.5 bil-
ZX et al., 2022; Zeng et al., 2023), QWEN (Bai
lion adapted for sequential data, these LLMs can
et al., 2023), and Mistral (Jiang AQ et al., 2023).
discern complex temporal dynamics. UniTS uses
On the contrary,application programminginterface
sequence and variable attention along with a dy-
(API)-basedLLMssuchasthegenerativepretrained
namic linear operator to build a unified model that
Transformer(GPT)family,includingmodelssuchas
can do classification, forecasting, imputation, and
GPT-3 (Brown et al., 2020)and its successor (Ope-
AD tasks at the same time (Gao SH et al., 2024).
nAI, 2024), and Claude offer robust pretrained
LLM4TS designs a two-stage fine-tuning strategy:
capabilities accessible via cloud services. General
time-series stage to align LLMs with the nuances of
LLMs are characterized by their extensive training
time-seriesdataandforecastingfine-tuningstagefor
on vast corpora of multimodal data, encompassing
downstream time-series forecasting tasks. The sec-
text, images, and videos in both structured and un-
ond stage can possibly be manipulated to adapt to
structured formats. Nevertheless, the challenge re-
AD tasks (Chang et al., 2024). Tiny time mixers
mainsinseamlesslyintegratingtime-seriesdatawith
(TTMs) make their effort to develop fast and tiny
natural language to maximize the potential of these
general pretrained models possessing less than one
tools. OneapproachistouseLLMsthroughprompt-
million parameters, with effective transfer learning
basedmethods. Forinstance,PromptCast(Xueand
capabilities for forecasting based on the lightweight
Salim,2024)reformulatesnumericalinputsandout-
TSMixerarchitecture(Ekambarametal.,2024).
puts into prompts, framing the forecasting process
Generalized LLMs have notably demonstrated
as a sentence-to-sentence conversion, allowing lan-
thecapabilitytoprocessawidearrayofdiverseinput
guage models to handle forecasting tasks. Another
formats, including structured data formats such as
example involves prompting ChatGPT with finan-
JSON and XML, beyond the scope of time-series
cial news, social media insights, and corporate re-
LLMs. Although no existing studies of generalized
ports to enhance predictions of stock market move-
LLMs have specifically focused on addressing spe-
ments(ChenZHetal.,2023). Inadditiontoprompt-
cializedanomalies,these modelsexhibit potentialin
based methods, a notable approach is reprogram-
detectingabroaderrangeofanomalies,suchasrout-
ming (Jin et al., 2024b), which introduces the con-
ing errors, by leveraging their ability to understand
cept of modifying input data to leverage a model’s
and analyze complex patterns within the data af-
latent knowledge without altering its parameters.
ter specialized training. As our study delves deeply
Time-LLM(Jinetal.,2024b)transformsinputtime-
into AD in temporal data, the subsequent discus-
seriesintotextualprototyperepresentations,making
sionofLLMtechniques willprimarilyfocus ontheir
them more interpretable for the LLM, and enhanc-
applicationinthe temporaldomain.
ing context with declarative prompts to guide the
LLM’s reasoning. Similarly, LLMTIME finds way
4.5 Current datasets
toaligntime-seriesdatawithAPI-basedLLMssuch
asGPT-3includingeffectivelytokenizingtime-series In the realm of AIOps, particularly within the
data and converting discrete distributions over to- contextofADincommunicationnetworks,theavail-
kens into highly flexible densities over continuous abilityandutilizationofdiversedatasetsplayapiv-
values (Gruveretal.,2024). otal role. This study provides a detailed overview

Guietal./ FrontInform TechnolElectron Eng 202526(9):1551-1576 1561
of the most prominent datasets used in the field as ingthesedatasetsinastructuredmanner,thisstudy
shown in Table 3, each contributing uniquely to the aimsto equipresearchersandpractitionerswiththe
development and evaluation of AD methods. The necessaryresourcestoadvancetheirworkinAD,fa-
datasets span various application scenarios, includ- cilitating a deeper understanding of the challenges
ingIoTservicessuchasIoTsecurity,networktraffic andopportunities withinthis domain.
monitoring,cloudandedgeserviceprovisioning,and
| networking | system |      | log analysis. | They         | encompass |       | a   |         |         |     |     |     |
| ---------- | ------ | ---- | ------------- | ------------ | --------- | ----- | --- | ------- | ------- | --- | --- | --- |
|            |        |      |               |              |           |       | 4.6 | Current | methods |     |     |     |
| wide range | of     | data | types, from   | multivariate |           | time- |     |         |         |     |     |     |
series to log files, and vary significantly in terms of Inthis study,we conclude variousmethods em-
| size, time | length, | and | dimensionality. |     | For | instance, |        |     |           |        |              |          |
| ---------- | ------- | --- | --------------- | --- | --- | --------- | ------ | --- | --------- | ------ | ------------ | -------- |
|            |         |     |                 |     |     |           | ployed | for | AD within | AIOps, | particularly | focusing |
datasets such as PUMP and secure water treat- on their applications in communication networks as
ment(SWaT)focusonIoTapplicationswithdetailed shown in Table 4. The methods are categorized
time-seriesdata,whileotherssuchasCanadianInsti- basedontheirunderlyingtechniques,suchasRNN-,
tute for Cyber Security Intrusion Detection System CNN-, graph-, and AE-based approaches. Each
| 2017 (CIC-IDS2017) |     |     | and University |     | of New | South |        |     |             |         |          |              |
| ------------------ | --- | --- | -------------- | --- | ------ | ----- | ------ | --- | ----------- | ------- | -------- | ------------ |
|                    |     |     |                |     |        |       | method | is  | designed to | address | specific | applications |
Wales-NetworkBenchmark2015(UNSW-NB15)are in AD, leveraging advanced algorithms to enhance
gearedtowardsinvasiondetectionwithextensivenet- detection accuracy and efficiency. Table 4 offers a
| work traffic | records. |     | Additionally, | datasets |     | such as |          |          |          |          |           |       |
| ------------ | -------- | --- | ------------- | -------- | --- | ------- | -------- | -------- | -------- | -------- | --------- | ----- |
|              |          |     |               |          |     |         | detailed | overview | of these | methods, | including | their |
hadoop distributed file system (HDFS) and Blue- supervision types (STs) and the datasets used for
Gene/L(BGL)providerichlogdatacrucialforiden- evaluation. The detailed introduction can be found
tifyinganomaliesinlarge-scalesystems. Bypresent- inSections5–8foreachapplicationdomain.
|     |     | Table3  | Overviewofcurrentdatasetsindifferent |     |     |        |            |            | applicationdomains |      |     |               |
| --- | --- | ------- | ------------------------------------ | --- | --- | ------ | ---------- | ---------- | ------------------ | ---- | --- | ------------- |
|     |     |         |                                      |     |     |        |            | Statistics |                    | Data |     | Overall       |
|     |     | Dataset |                                      |     |     | Domain |            |            | Timelength         |      | Dim |               |
|     |     |         |                                      |     |     |        | (training; | test)      |                    | type |     | anomaly ratio |
PUMP(DataSetsAI, 2020) IoT 76 901; 143 401 5months MulTS 44 10.05
SWaT (Mathur and Tippenhauer, 2016) IoT 99360; 89984 11days MulTS 25 11.99
WADI (AhmedCM etal.,2017) IoT 241 921; 15 701 16days MulTS 67 7.09
| N-BaIoT | (Meidan | etal.,2018) |     |     |     | IoT |     | 7062 606 |     | MulTS | 115 | 92.13 |
| ------- | ------- | ----------- | --- | --- | --- | --- | --- | -------- | --- | ----- | --- | ----- |
BoT-IoT (Koroniotis et al.,2019) IoT 73million MulTS 29 0.013
5% BoT-IoT subset (Koroniotis et al.,2019) IoT 3668 522 MulTS 43 0.013
NSL-KDD(Tavallaee etal.,2009) IoT/Network traffic 125 973; 22 544 MulTS 41 36.98
UNSW-NB15(Moustafa andSlay, 2015) Network traffic 175 341; 82 332 2days MulTS 49 63.9
CIC-IDS2017 (Sharafaldin et al.,2018) Network traffic 125 973; 22 533 MulTS 83 47.1
CIC-IDS2018 (Sharafaldin et al.,2018) Network traffic 16 232943 MulTS 80 16.9
CIC-DDoS2019 (Sharafaldin et al.,2019) Network traffic 11 687590 MulTS 87 99.84
Edge-IIoTset (Ferrag et al.,2022) IIoT/Network traffic 324 928; 38 813 MulTS 61 29.3
USTC-TFC2016(Wang Wet al.,2017) Network traffic 245 437; 27 271 MulTS 95.59
KDDCup 1999 (Cup, 2007) Cloudservice 5000 000; 2000000 9weeks MulTS 41
ISOT CID phase1 (Aldribi et al.,2018) Cloudservice 24 519987 5days MulTS 5 37.58
ISOT CID phase2 (Aldribi et al.,2018) Cloudservice 12 418998 6days MulTS 5 21.32
TON_IoT (Alsaedi et al.,2020) Cloudservice 276 625; 184428 MulTS 46 3.6
X-IIoTID (Al-Hawawrehet al.,2022) Cloudservice 820 834 114 days MulTS 67 48.66
| CICIoT2023 | (Neto         | et al.,2023) |     |     | Cloudservice |     |     | –         |     | MulTS | 47  |      |
| ---------- | ------------- | ------------ | --- | --- | ------------ | --- | --- | --------- | --- | ----- | --- | ---- |
| HDFS(XuW   | etal.,2009)   |              |     |     |              | Log |     | 11 175629 |     | Log   |     | 2.93 |
| BGL(Liang  | Y etal.,2005) |              |     |     |              | Log |     | 4747 963  |     | Log   |     | 7.34 |
Thunderbird (Olinerand Stearley, 2007) Log 10 000000 Log 0.49
| Spirit(Oliner | andStearley, |     | 2007) |     |     | Log |     | 5000 000 |     | Log |     | 15.29 |
| ------------- | ------------ | --- | ----- | --- | --- | --- | --- | -------- | --- | --- | --- | ----- |
Mul TS means multivariate time series; “–” means that the statistics is inaccessible; the blank means that the data do not exist.
| Dim: dimension;IIoT: |     | IndustrialInternetofThings |     |     |     |     |     |     |     |     |     |     |
| -------------------- | --- | -------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

1562 Guietal./FrontInform TechnolElectron Eng 202526(9):1551-1576
|        | Table4 |        | Overviewof currentmethodsindifferentapplicationdomains |           |     |     |     |         |     |     |     |
| ------ | ------ | ------ | ------------------------------------------------------ | --------- | --- | --- | --- | ------- | --- | --- | --- |
| Domain |        | Method |                                                        | Technique |     | ST  |     | Dataset |     |     |     |
SGmVRNN (Dai etal.,2022) RNN-based SL CDNmultivariate KPIdataset and SMD
|     | D-PACK(Hwang |     | etal.,2020) | CNN-based |     | UL  | USTC-TFC2016 |     |     |     |     |
| --- | ------------ | --- | ----------- | --------- | --- | --- | ------------ | --- | --- | --- | --- |
MSRC(Duan et al.,2023) AE-based UL KDDCUP99, NSL-KDD, UNSW-NB15,
|     |            |     |                |           |     |     | and     | CIC-IDS2018 |     |     |     |
| --- | ---------- | --- | -------------- | --------- | --- | --- | ------- | ----------- | --- | --- | --- |
|     | LSTM-GAN-G |     | (Huang et al., | RNN-based |     | UL  | CellPAD |             |     |     |     |
2022)
RENOIR(Andresinietal.,2021) AE-based SL KDDCUP99,AAGM17,andCIC-IDS2017
|     | CMAE(Lu | etal.,2022) |     | AE-based |     | UL  | KDDCUP99 |     |     |     |     |
| --- | ------- | ----------- | --- | -------- | --- | --- | -------- | --- | --- | --- | --- |
ARCADE(Lunardi et al.,2023) AE-based UL ISCX-IDS,USTC-TFC,andMIRAI-RGU
Network APAE(BasatiandFaghih,2023) AE-based UL UNSW-NB15, CIC-IDS2017, and
| traffic |     |     |     |     |     |     | KDDCUP99 |     |     |     |     |
| ------- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- |
monitoring
|     | HCRNNIDS(Khan, |     | 2021) | RNN-based |     | SL  | CSE-CIC-IDS2018 |     |     |     |     |
| --- | -------------- | --- | ----- | --------- | --- | --- | --------------- | --- | --- | --- | --- |
CNN-LSTM (Halbouni et al., RNN-based SL CIC-IDS2017, UNSW-NB15, and WSN-
|     | 2022) |     |     |     |     |     | DS  |     |     |     |     |
| --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
DCNNBiLSTM (Hnamte and RNN-based UL CIC-IDS2018 and Edge_IIoT
Hussain,2023)
CANET(Ren KY etal.,2023) CNN-based SL UNSW-NB1, NSL-KDD, CIC-IDS2017,
|     |         |          |         |           |     |     | and     | CICDDoS2019 |     |     |     |
| --- | ------- | -------- | ------- | --------- | --- | --- | ------- | ----------- | --- | --- | --- |
|     | CBR-CNN | (Chouhan | et al., | CNN-based |     | UL  | NSL-KDD |             |     |     |     |
2019)
LogPrompt(LiuYLetal.,2024) LLM-based UL HDFS, Hadoop, Zookeeper, BGL, HPC,
|     |     |     |     |     |     |     | Linux, | Proxifier, | Android, | and Spirit |     |
| --- | --- | --- | --- | --- | --- | --- | ------ | ---------- | -------- | ---------- | --- |
Networking DeepLog (DuM et al.,2017) RNN-based SL HDFSand OpenStack
system
|     | LogAnomaly(Meng |     | et al.,2019) | RNN-based |     | UL  | BGLandHDFS |     |     |     |     |
| --- | --------------- | --- | ------------ | --------- | --- | --- | ---------- | --- | --- | --- | --- |
log
|     | PLELog(Yang |     | Let al.,2021) | RNN-based |     | SSL | BGL |     |     |     |     |
| --- | ----------- | --- | ------------- | --------- | --- | --- | --- | --- | --- | --- | --- |
analysis
LogRobust (Zhang X et al., RNN-based SL HDFSand Microsoft’s data
2019b)
|     | NSIBF(Feng | and | Tian,2021)   | CNN-based+BF |     | SL  | PUMP,WADI, | andSWaT |     |     |     |
| --- | ---------- | --- | ------------ | ------------ | --- | --- | ---------- | ------- | --- | --- | --- |
|     | GAN-AD(Li  | D   | etal.,2019a) | RNN-based+   |     | UL  | SWaT       |         |     |     |     |
GAN-based
|     | MAE and | MDAE | (Vu et al., | AE-based |     | SL  | N-BaIoT |     |     |     |     |
| --- | ------- | ---- | ----------- | -------- | --- | --- | ------- | --- | --- | --- | --- |
2022)
IoT
|     | N-BaIoT | (Meidanet | al.,2018) | AE-based |     | SL  | N-BaIoT |     |     |     |     |
| --- | ------- | --------- | --------- | -------- | --- | --- | ------- | --- | --- | --- | --- |
security
|     | FDL(Popoola | etal.,2022) |              | DNN-based+FL |     | SL  | BoT-IoT | andN-BaIoT |     |     |     |
| --- | ----------- | ----------- | ------------ | ------------ | --- | --- | ------- | ---------- | --- | --- | --- |
|     | FeCo(Wang   | N           | etal.,2022)  | FL+CL        |     | SL  | NSL-KDD |            |     |     |     |
|     | FedPG       | (Nguyen     | et al.,2023) | FL           |     | SL  | NSL-KDD |            |     |     |     |
|     | LogNL(Zhu   | et          | al.,2020)    | RNN-based    |     | SL  | HDFSand | OpenStack  |     |     |     |
Cloud
andedge GLLD (Khalaf et al.,2022) Graph-based SL BoT IoT and code red worm
| service | CGNN-MHSA-AR |     | (Song YJ | GRU+self- |     | SL  | Server | machine |     |     |     |
| ------- | ------------ | --- | -------- | --------- | --- | --- | ------ | ------- | --- | --- | --- |
provisioning
|                                                 | et al.,2023) |     |     | attention            |     |     |     |     |     |     |     |
| ----------------------------------------------- | ------------ | --- | --- | -------------------- | --- | --- | --- | --- | --- | --- | --- |
| BF: Bayesfilter;SSL:semi-supervisedlearning;UL: |              |     |     | unsupervisedlearning |     |     |     |     |     |     |     |
5 AD for networktraffic monitoring informationordisrupting communicationlinks. AD
modelsorintrusiondetectionsystemsarewidelyem-
|                    |                  |      |                     |         | ployed   | to identify |            | such threats, | such    | as spikes | in    |
| ------------------ | ---------------- | ---- | ------------------- | ------- | -------- | ----------- | ---------- | ------------- | ------- | --------- | ----- |
| In the             | 5G communication |      | environment,        | the in- |          |             |            |               |         |           |       |
|                    |                  |      |                     |         | traffic, | unusual     | access     | patterns,     | and     | potential | dis-  |
| creasing volume    | of traffic       | data | is vulnerable       | to ma-  |          |             |            |               |         |           |       |
|                    |                  |      |                     |         | tributed | denial      | of service | (DDoS)        | attacks | or        | other |
| licious activities | which            | aim  | at stealing private | user    |          |             |            |               |         |           |       |

Guietal./ FrontInform TechnolElectron Eng 202526(9):1551-1576 1563
intrusionattacks. This sectionintroduces the appli- the network traffic. CBR-CNN (Chouhan et al.,
cations of AD models for malicious network traffic 2019)exemplifies this approachby combining chan-
monitoring. nel boosting and residual learning to enhance fea-
|     |     |     |     |     | ture representation. |     |     | It employs |     | stacked | AEs to |
| --- | --- | --- | --- | --- | -------------------- | --- | --- | ---------- | --- | ------- | ------ |
5.1 Applicationdescription model normal traffic and uses a multipath residual
|     |     |     |     |     | learning-based |     | CNN | to detect | intrusions |     | at various |
| --- | --- | --- | --- | --- | -------------- | --- | --- | --------- | ---------- | --- | ---------- |
The backbone network comprises hundreds of levelsof granularity. CANET (Ren KY et al.,2023)
interconnectednodes,andvariousillegitimateactivi-
|     |     |     |     |     | integrates | CNN | with | attention | mechanisms |     | in hi- |
| --- | --- | --- | --- | --- | ---------- | --- | ---- | --------- | ---------- | --- | ------ |
tiessuchasDDoSattacks,portscans,andwormscan
|                        |     |                         |     |     | erarchical            | certificate |     | authority | (CA)        | blocks, | focus- |
| ---------------------- | --- | ----------------------- | --- | --- | --------------------- | ----------- | --- | --------- | ----------- | ------- | ------ |
| causetrafficanomalies. |     | Theseanomaliesoftenman- |     |     |                       |             |     |           |             |         |        |
|                        |     |                         |     |     | ing on spatiotemporal |             |     | feature   | extraction. |         | By ad- |
ifestasfluctuationsintheoriginal-destination(OD)
|                |                                |     |              |            | dressing           | class imbalance  |             | using    | equalization |                 | loss v2   |
| -------------- | ------------------------------ | --- | ------------ | ---------- | ------------------ | ---------------- | ----------- | -------- | ------------ | --------------- | --------- |
| traffic volume | between nodes.                 |     | However,     | monitoring |                    |                  |             |          |              |                 |           |
|                |                                |     |              |            | (a gradient-guided |                  | reweighting |          | loss),       | the             | extracted |
| traffic at     | OD level is resource-intensive |     | and          | difficult  |                    |                  |             |          |              |                 |           |
|                |                                |     |              |            | features           | are particularly |             | suitable |              | for large-scale | in-       |
| to analyze     | due to the scale               | of  | the network. | On the     |                    |                  |             |          |              |                 |           |
trusiondetectiondownstreamtasks.
contrary,suddenincreasesordecreasesinODtraffic
can directly impact link traffic volume. Since link- 5.3 Intrusiondetectiontechniques
leveltrafficmonitoringismorescalableandmanage-
|                  |                |          |                  |            | A            | variety | of          | intrusion | detection |               | systems,    |
| ---------------- | -------------- | -------- | ---------------- | ---------- | ------------ | ------- | ----------- | --------- | --------- | ------------- | ----------- |
| able, it becomes | more           | feasible | as the indicator | for        |              |         |             |           |           |               |             |
|                  |                |          |                  |            | leveraging   | diverse |             | deep      | learning  | technologies, |             |
| AD. The          | task of AD for | network  | traffic          | focuses on |              |         |             |           |           |               |             |
|                  |                |          |                  |            | are deployed |         | for network |           | security  |               | monitoring. |
identifyingmalicioustrafficpatternsatthelinklevel
to enhancenetworksecurityandperformance. RENOIR(Andresinietal.,2021)combinesAEswith
tripletnetworkstocreateembeddingsthateffectively
5.2 Traffic feature extraction distinguishbetweenthenormalandattacktrafficby
|     |     |     |     |     | training | AEs on | historical | data, | and | using | a triplet |
| --- | --- | --- | --- | --- | -------- | ------ | ---------- | ----- | --- | ----- | --------- |
Traffic volume is crucial for analyzing network network to ensure accurate classification of network
operationalstatus. Variousfeatureextractionmeth- flows based on their reconstructions. Similarly,
ods are used to obtain informative representations cognitivememory-guidedautoencoder(CMAE) (Lu
of traffic volume, and can be applied to down- etal.,2022)enhancestraditionalAEswithamemory
streamtasks,suchasAD.Inthiscontext,deepneu- module to store normal feature patterns, making it
ral networks, such as RNNs and CNNs, are used. robusttoimbalancedsamples,andleveragingrecon-
HCRNNIDS(Khan,2021)exemplifiesthisapproach struction error, feature reconstruction loss, and fea-
bymergingCNNandRNN,wheretheCNNcompo- ture sparsity loss to improve detection capabilities,
nent extracts spatial features and the RNN compo- particularlyforunknownattacks. Adversariallyreg-
nent captures temporal dependencies. This synergy ularizedconvolutionalautoencoderforunsupervised
enhances the ability of intrusion detection system network anomaly detection (ARCADE) (Lunardi
to classify and predict cyber attacks by leveraging et al., 2023) uses a convolutional AE to profile nor-
the temporal AD capabilities of RNNs, making it mal network traffic, and employs adversarial train-
highly effectiveindetecting time-seriesanomaliesin ing to reduce the AE’s ability to reconstructout-of-
network traffic. Similarly, DCNNBiLSTM (Hnamte distributionflows,therebyenhancingitsADcapabil-
andHussain,2023)combinesCNNforspatialfeature ities. Multi-scale residual classifier (MSRC) (Duan
extraction, bidirectional LSTM (Bi-LSTM) for se- et al., 2023) uses wavelet transforms for multi-scale
quenceprediction,anddeepneuralnetworks(DNN) analysis and a stacked AE for learning data dis-
for error optimization, leveraging the strengths of tributions, effectively capturing anomalies at vari-
each component. CNN-LSTM (Halbouni et al., ousscalesandcomplexities. Meanwhile,asymmetric
2022) uses CNN to extract spatial features and parallel AE (APAE) (Basati and Faghih, 2023) fea-
LSTM to capture temporal dependencies, creating turesadual-encoderdesignthatcapturesbothlocal
a robust hybrid model for intrusion detection. The and long-range features using convolutional layers
inclusion of batch normalization and dropout lay- and attention mechanisms. Its lightweight architec-
ers further enhances its performance and robust- ture and robust decoder make it suitable for real-
ness,effectivelydetectingtemporalanomalieswithin timeintrusiondetectionandgeneralizationevenwith

1564 Guietal./FrontInform TechnolElectron Eng 202526(9):1551-1576
limitedtrainingdata. D-PACK(Hwangetal.,2020) crucial to use efficient methodologies grounded in
addressesthe vulnerabilitiesexploitedbylarge-scale machinelearninganddeeplearning. ADmethodsin
cyber attacks. This system integrates CNN with system logs can be effectively categorized based on
an unsupervised deep learning model, to efficiently the specific-appliedscenarios.
| profile | traffic | patterns | and | filter out | abnormalities. |     |     |     |     |     |     |     |     |
| ------- | ------- | -------- | --- | ---------- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
6.1 Applicationdescription
| What sets  | D-PACK    |           | apart     | is its method |              | of inspect- |                 |      |             |          |                     |     |             |
| ---------- | --------- | --------- | --------- | ------------- | ------------ | ----------- | --------------- | ---- | ----------- | -------- | ------------------- | --- | ----------- |
| ing just   | the first | few       | bytes     | of the        | initial      | packets in  |                 |      |             |          |                     |     |             |
|            |           |           |           |               |              |             | System          | logs | record      | critical | states              |     | and changes |
| each flow, | enabling  | early     | detection |               | of malicious | ac-         |                 |      |             |          |                     |     |             |
|            |           |           |           |               |              |             | within asystem, |      | enablingthe |          | analysisofanomalous |     |             |
| tivities.  | This      | strategic | focus     | allows        | for          | prompt in-  |                 |      |             |          |                     |     |             |
events. InlogAD,theprocessbeginswiththecollec-
| tervention,      | potentially |               | stopping      | attacks     |               | before they |                                     |            |                  |            |         |                |            |
| ---------------- | ----------- | ------------- | ------------- | ----------- | ------------- | ----------- | ----------------------------------- | ---------- | ---------------- | ---------- | ------- | -------------- | ---------- |
|                  |             |               |               |             |               |             | tion of system                      |            | logs, each       | comprising |         | a standardized |            |
| escalate.        | Training    | LLM           | models        |             | for intrusion | de-         |                                     |            |                  |            |         |                |            |
|                  |             |               |               |             |               |             | templateandsystem-specificvariable. |            |                  |            |         | Subsequently,  |            |
| tection          | leverages   | sophisticated |               | approaches  |               | to opti-    |                                     |            |                  |            |         |                |            |
|                  |             |               |               |             |               |             | logs are                            | parsed     | to differentiate |            | between |                | the static |
| mize performance |             | and           | resource      | efficiency. |               | Specif-     |                                     |            |                  |            |         |                |            |
|                  |             |               |               |             |               |             | components                          | (e.g.,     | predefinedtext   |            |         | ortemplates)   | and        |
| ically, models   |             | such as       | bidirectional |             | encoder       | repre-      |                                     |            |                  |            |         |                |            |
|                  |             |               |               |             |               |             | the dynamic                         | components |                  | (e.g.,     | thread  | names          | or job     |
| sentations       | from        | Transformers  |               | (BERT)      | are           | adapted     |                                     |            |                  |            |         |                |            |
ID).Thelogsarethenpartitionedintoseveralgroups
| for identifying |        | malicious | network     |     | flows. | The train- |                                     |            |     |         |     |         |            |
| --------------- | ------ | --------- | ----------- | --- | ------ | ---------- | ----------------------------------- | ---------- | --- | ------- | --- | ------- | ---------- |
|                 |        |           |             |     |        |            | basedontimestampsandlogidentifiers. |            |     |         |     |         | Featureex- |
| ing process     | begins | with      | fine-tuning |     | the    | pretrained |                                     |            |     |         |     |         |            |
|                 |        |           |             |     |        |            | traction                            | techniques | are | applied | to  | capture | relevant   |
BERTmodelonspecializeddatasetsofnetworktraf-
|                   |     |             |     |          |                  |         | characteristics |            | of the | data.     | Finally, | these    | features  |
| ----------------- | --- | ----------- | --- | -------- | ---------------- | ------- | --------------- | ---------- | ------ | --------- | -------- | -------- | --------- |
| fic. Enhancements |     | such        | as  | temporal | feature          | extrac- |                 |            |        |           |          |          |           |
|                   |     |             |     |          |                  |         | are used        | by anomaly |        | detectors | to       | identify | instances |
| tion and          | the | integration | of  | flow-    | and packet-level |         |                 |            |        |           |          |          |           |
ofanomalouslogs.
| data within | heterogeneous |     |     | graph structures |     | further |     |     |     |     |     |     |     |
| ----------- | ------------- | --- | --- | ---------------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
refinethemodel’sabilitytoprovidedetailed,contex- 6.2 Log dimensionreduction
tually richinsights(Farrukhetal.,2024).
Inscenariosdealingwithhigh-dimensionaldata
| 5.4 Network  |            | KPIanalysis |             |             |             |             |                 |                |              |           |            |             |              |
| ------------ | ---------- | ----------- | ----------- | ----------- | ----------- | ----------- | --------------- | -------------- | ------------ | --------- | ---------- | ----------- | ------------ |
|              |            |             |             |             |             |             | where capturing |                | essential    |           | variance   | is          | important,   |
|              |            |             |             |             |             |             | methods         | such           | as principal |           | component  |             | analysis     |
| Monitoring   |            | KPIs,       | such        | as hit      | ratio       | and delay   |                 |                |              |           |            |             |              |
|              |            |             |             |             |             |             | (PCA) (Xu       | W              | et al.,      | 2009)     | come       | into        | play. PCA    |
| in content   | delivery   |             | networks    | (CDNs)      | (Dai        | et al.,     |                 |                |              |           |            |             |              |
|              |            |             |             |             |             |             | reduces         | dimensionality |              | to        | identify   | anomalous   | pat-         |
| 2022),       | is crucial | as          | performance |             | degradation | can         |                 |                |              |           |            |             |              |
|              |            |             |             |             |             |             | terns in        | log vectors,   |              | which     | are useful |             | in recogniz- |
| be reflected |            | in these    | KPIs.       | The         | LSTM-GAN-G  |             |                 |                |              |           |            |             |              |
|              |            |             |             |             |             |             | ing anomalies   |                | within       | complex   | log        | structures. | For          |
| model        | (Huang     | et al.,     | 2022)       | integrates  |             | GAN with    |                 |                |              |           |            |             |              |
|              |            |             |             |             |             |             | real-time       | monitoring     |              | and quick | AD         | for         | large scale  |
| LSTM         | cells,     | enabling    | it to       | effectively | capture     | the         |                 |                |              |           |            |             |              |
|              |            |             |             |             |             |             | log data,       | clustering     | approaches   |           | are        | highly      | effective.   |
| temporal     | dynamics   | of          | cellular    | KPI         | time        | series. For |                 |                |              |           |            |             |              |
Thesemethodsevaluatetheproximityofnewlogsto
| AD, the | model | uses | the trained |     | generator | to re- |     |     |     |     |     |     |     |
| ------- | ----- | ---- | ----------- | --- | --------- | ------ | --- | --- | --- | --- | --- | --- | --- |
clustercenters(LinQWetal.,2016),enablingrapid
| construct    | testing                  | samples, |      | and identifies |          | anomalies |                            |         |            |         |                         |     |            |
| ------------ | ------------------------ | -------- | ---- | -------------- | -------- | --------- | -------------------------- | ------- | ---------- | ------- | ----------------------- | --- | ---------- |
|              |                          |          |      |                |          |           | identificationofanomalies. |         |            |         | This isparticularlyben- |     |            |
| by comparing |                          | these    | with | the actual     | data.    | The       |                            |         |            |         |                         |     |            |
|              |                          |          |      |                |          |           | eficial for                | systems | that       | require | constant                |     | monitoring |
| SGmVRNN      | model                    | (Dai     | et   | al., 2022)     | uses     | a varia-  |                            |         |            |         |                         |     |            |
|              |                          |          |      |                |          |           | andimmediate               |         | responseto |         | unusualactivities.      |     |            |
| tionalRNN    | architecturethatcombines |          |      |                | amixture | of        |                            |         |            |         |                         |     |            |
Gaussiandistributionsforlatentvariables,capturing
|               |             |     |      |         |     |            | 6.3 Log | semanticrepresentation |     |     |     |     |     |
| ------------- | ----------- | --- | ---- | ------- | --- | ---------- | ------- | ---------------------- | --- | --- | --- | --- | --- |
| the intricate | time-series |     | data | of KPIs | in  | CDN effec- |         |                        |     |     |     |     |     |
tively. It also introduces a switching mechanism to In applications requiring sequence prediction
better representthe variable structures and dynam- and detailed log pattern analysis, DeepLog (Du M
ics withinthe KPIs. etal.,2017)transformsrawlogdataintostructured
|     |     |     |     |     |     |     | sequences | for | training | an  | LSTM | neural | network. |
| --- | --- | --- | --- | --- | --- | --- | --------- | --- | -------- | --- | ---- | ------ | -------- |
6 AD for networking system log analy- This enables the model to learn normal patterns of
|     |     |     |     |     |     |     | log sequences, |     | and predict |     | subsequent |     | logs, detect- |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ----------- | --- | ---------- | --- | ------------- |
sis
inganomaliesbyassessingdeviationsfromexpected
The log data encompass a substantial volume, templates. LogAnomaly (Meng et al., 2019) incor-
extending across diverse system layers and formats. porates semantic analysis with Template2Vec, con-
Therefore, to adeptly identify log anomalies, it is vertinglogtemplatesintosemanticvectorsprocessed

Guietal./ FrontInform TechnolElectron Eng 202526(9):1551-1576 1565
|               |                 |              |              |                       |            |        | 7 AD    | for cloud     | and | edge    | service |         | provi- |
| ------------- | --------------- | ------------ | ------------ | --------------------- | ---------- | ------ | ------- | ------------- | --- | ------- | ------- | ------- | ------ |
| by a Bi-LSTM  |                 | with         | an attention |                       | mechanism. | This   |         |               |     |         |         |         |        |
| method        | is particularly |              | effective    | in                    | scenarios  | where  | sioning |               |     |         |         |         |        |
| understanding |                 | the          | context      | and                   | semantics  | of log |         |               |     |         |         |         |        |
|               |                 |              |              |                       |            |        | In      | this section, | we  | examine | current | studies | re-    |
| data is       | critical        | for accurate |              | AD. Transformer-based |            |        |         |               |     |         |         |         |        |
models (Balasubramanian et al., 2023) use pre- gardingthedetectionofanomaliesincloudandedge
|     |     |     |     |     |     |     | service | provisioning, | using | a   | variety | of approaches, |     |
| --- | --- | --- | --- | --- | --- | --- | ------- | ------------- | ----- | --- | ------- | -------------- | --- |
trainedembeddingtorepresentlogentriesinahigh-
dimensional space, capturing semantic information includingstatisticalanalysis,machinelearning,deep
learning,andhybridmethods.
| beyondsimple |     | token-levelrepresentations. |     |     |     |     |     |     |     |     |     |     |     |
| ------------ | --- | --------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
7.1 Applicationdescription
| 6.4 Log | AD  |     |     |     |     |     |     |     |     |     |     |     |     |
| ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Thecloudsystemincludesvariousconnectedre-
| For | robust | AD  | in  | noisy environments, |     | ap- |     |     |     |     |     |     |     |
| --- | ------ | --- | --- | ------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
sourcesthroughthedistributednetwork,andcandy-
| proaches  | such   | as PLELog |           | (Yang L   | et al., | 2021) and     |           |          |           |     |       |         |         |
| --------- | ------ | --------- | --------- | --------- | ------- | ------------- | --------- | -------- | --------- | --- | ----- | ------- | ------- |
|           |        |           |           |           |         |               | namically | allocate | resources |     | based | on user | demand. |
| LogRobust | (Zhang |           | X et al., | 2019b)are |         | highly effec- |           |          |           |     |       |         |         |
tive. PLELog uses a gated recurrent unit (GRU) However,cloudenvironmentissusceptibletovarious
|          |           |     |           |        |          |          | attacks,     | including | those     | targeting   | virtual | machines,        |     |
| -------- | --------- | --- | --------- | ------ | -------- | -------- | ------------ | --------- | --------- | ----------- | ------- | ---------------- | --- |
| with an  | attention |     | mechanism | to     | classify | log se-  |              |           |           |             |         |                  |     |
|          |           |     |           |        |          |          | unauthorized |           | access to | interfaces, |         | and vulnerabili- |     |
| quences, | focusing  | on  | parts     | of the | log data | that in- |              |           |           |             |         |                  |     |
dicate anomalies. LogRobust, designed to handle tiesinAPIs orInternetprotocols. Todetectattacks
withincloudinfrastructure,datapacketsandsystem
| noisy or | unstable | log | data, | starts | by converting | log |     |     |     |     |     |     |     |
| -------- | -------- | --- | ----- | ------ | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
logsarecollectedandanalyzedfordetectinganoma-
dataintosemanticvectors,andusesanLSTMmodel
|     |     |     |     |     |     |     | lies. On | the contrary, |     | KPIs | can be | gathered | from |
| --- | --- | --- | --- | --- | --- | --- | -------- | ------------- | --- | ---- | ------ | -------- | ---- |
forAD.Thismethodensuresreliabledetectioneven
|            |       |             |     |        |     |              | localdevices | for | edge-levelAD, |     | which | enhances | effi- |
| ---------- | ----- | ----------- | --- | ------ | --- | ------------ | ------------ | --- | ------------- | --- | ----- | -------- | ----- |
| under less | ideal | conditions, |     | making | it  | suitable for |              |     |               |     |       |          |       |
applicationswithsignificantlogdatavariabilityand ciencyandenablestheswiftidentificationofanoma-
louseventswithminimaldelay.
| noise.          | LLMs              | have   | demonstrated |                | a profound | ca-          |             |                   |     |     |     |     |     |
| --------------- | ----------------- | ------ | ------------ | -------------- | ---------- | ------------ | ----------- | ----------------- | --- | --- | --- | --- | --- |
| pability        | for understanding |        |              | and processing |            | complex      |             |                   |     |     |     |     |     |
|                 |                   |        |              |                |            |              | 7.2 Service | systemmaintenance |     |     |     |     |     |
| data sequences. |                   | By     | leveraging   | self-attention |            | mech-        |             |                   |     |     |     |     |     |
| anisms,         | these             | models | can          | understand     |            | log content, |             |                   |     |     |     |     |     |
Statisticalanalysisempowerscloudprovidersto
conduct anomaly classification among parallel file detect anomalies within their cloud environments,
| system | logs (Egersdoerfer |     |     | et al., 2023), |     | and localize |              |        |               |     |     |                |     |
| ------ | ------------------ | --- | --- | -------------- | --- | ------------ | ------------ | ------ | ------------- | --- | --- | -------------- | --- |
|        |                    |     |     |                |     |              | facilitating | prompt | interventions |     |     | and minimizing |     |
configurationerrors(Shanetal.,2024). disruptions. For instance, SCHEDA, introduced
By aligning each method with its optimal by Guigou et al. (2019), integrates three algorithms
application scenario, both machine learning and to compute Euclidean anomaly scores for detect-
deep learning techniques enhance the effectiveness ing anomalies in cloud data. This system excels in
and accuracy of detecting anomalies in system real-timeanomalyscoringwithouttheneedfordata
| logs, addressing |     | diverse |     | challenges | with | tailored |            |               |     |           |     |              |     |
| ---------------- | --- | ------- | --- | ---------- | ---- | -------- | ---------- | ------------- | --- | --------- | --- | ------------ | --- |
|                  |     |         |     |            |      |          | buffering, | significantly |     | enhancing |     | the security | and |
approaches. efficiency of cloud services. Similarly, the approach
|             |     |                        |     |     |     |     | proposedby | Khatibzadehetal.(2019)leveragesthe |     |     |     |     |     |
| ----------- | --- | ---------------------- | --- | --- | --- | --- | ---------- | ---------------------------------- | --- | --- | --- | --- | --- |
| 6.5 Failure |     | predictionanddiagnosis |     |     |     |     |            |                                    |     |     |     |     |     |
catastrophetheoryandentropytoidentifyanomalies
|         |              |            |               |                |       |           | incloudtraffic. |     | Thesestatisticalmethodsarepartic- |            |     |     |          |
| ------- | ------------ | ---------- | ------------- | -------------- | ----- | --------- | --------------- | --- | --------------------------------- | ---------- | --- | --- | -------- |
| For     | failure      | prediction |               | and diagnosis, |       | methods   |                 |     |                                   |            |     |     |          |
|         |              |            |               |                |       |           | ularly useful   | for | real-time                         | monitoring |     | and | ensuring |
| such as | the decision |            | tree approach |                | (Chen | M et al., |                 |     |                                   |            |     |     |          |
systemstability.
| 2004),     | which | categorizes |            | logs based | on  | predefined   |     |     |     |     |     |     |     |
| ---------- | ----- | ----------- | ---------- | ---------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- |
| attributes | and   | branching   | decisions, |            | are | particularly |     |     |     |     |     |     |     |
7.3 Cloudloganalysis
useful. Thisapproachcanhighlightwhetherlogsare
normal or abnormal, aiding in predicting and diag- Deep learning algorithms significantly enhance
nosing system failures. Similarly, the SVM (Liang the detection of anomalies in cloud computing by
YLetal.,2007)approachconstructsahyperplaneto capturing intricate patterns in log data. Zhu et al.
separate normal and abnormal activities, making it (2020) introduced the LogNL technique, which uses
idealforscenarioswhereprecisefailure predictionis LSTMandnaturallanguageprocessing(NLP)tech-
| critical. |     |     |     |     |     |     | niques | for log | AD. This | approach |     | is particularly |     |
| --------- | --- | --- | --- | --- | --- | --- | ------ | ------- | -------- | -------- | --- | --------------- | --- |

1566 Guietal./FrontInform TechnolElectron Eng 202526(9):1551-1576
effective for analyzing cloud platform logs, and has series textual records, achieving high detection ac-
demonstrated high accuracy and F1 score in evalu- curacy in the OpenStack environment. Song YJ
ations. Similarly, Khalaf et al. (2022) developed a etal.(2023)employedparallelgraphneuralnetworks
graph-based layer-driven learning (GLLD) method (GNNs) and multi-head self-attention mechanisms
for AD in cloud networks. This method excels in to enhance detection accuracy in multivariate time-
detecting anomalies in cloud traffic, though it faces series, making it particularly suitable for real-time
challengesinidentifying varioustypes ofanomalies. AD.
7.4 Cloud-basedcomputingsecurity 7.7 Distributed hierarchical edge computing
(HEC)
Machine learningalgorithmsoffersophisticated
solutions for enhancing the security of cloud-based
In distributed HEC systems, AD is crucial for
computing. Parameswarappa et al. (2023) applied
reducing latency and ensuring high accuracy across
machine learning methods to propose a novel fire-
differentcomputationallayers,includingedgeservers
wall strategy aimed at enhancing cloud security.
and cloud platforms. Schneible and Lu (2017) pre-
Their approach combines historical and current de-
sentedanADmethodusingAEsondistributededge
cisions to form the “most frequent decision” tech-
devices, reducing the need for data transmission to
nique, achieving high accuracy and F1 score on the
acentralserverandenablingmorelocalizedprocess-
UNSW-NB15 dataset, despite high computational
ing. Peng et al.(2019)presenteda multi-source AD
costs. Similarly, Jiang J et al. (2023) proposed
systembasedonHEC,focusingonindustrialapplica-
the adaptive ensemble random fuzzy (AERF) algo-
tionssuchasmining. Itimprovesdetectionaccuracy
rithm for cloud network AD. AERF effectively ad-
andreduceslatency. Ngoetal.(2020)demonstrated
dressesdisruptionsfromatypicaldatadistributions,
thatusingtheirproposedmethodindistributedHEC
showcasing its utility in maintaining robust cloud
systems significantly reduces detection delay by ap-
security.
proximately 71% while maintaining accuracy, mak-
ing it highly suitable for real-time applications in
7.5 Cross-environmentadaptability
edge computing environments. Ngo et al. (2021)in-
troducedanadaptivemodelselectionschemeforAD
Zhang X et al. (2019a) developed the ATAD
method, which integrates active and transfer learn- inIoTenvironmentswithHEC.Itoptimizesbothac-
curacy and delay through a reinforcement learning-
ing techniques to identify abnormalities in an un-
labeled dataset. This method demonstrates high basedpolicynetwork.
F1 score in cross-dataset evaluations. Yu et al.
7.8 Intelligentvideosurveillance
(2020) introduced an AD framework based on the
behavioral characteristics of time-series networks,
Intelligent video surveillance systems use edge
using the DBN-BiGRU algorithm model. Lalotra
and cloud computing to enable real-time AD. In
et al. (2022) presented the intelligent real-time AD
thesesystems,visualsensorscollectrawdata,which
system (iReTADS), which employs a data summa-
are then preprocessed and subjected to feature ex-
rization strategy to reduce network traffic and en-
traction(Georgiouetal.,2020). Theprocesseddata
hance security in real time. These hybrid methods
are analyzed by machine learning models to detect
are particularly beneficial for applications requiring
abnormalbehavior. Whilecloudcomputingistradi-
adaptability and robust AD across diverse datasets
tionallyusedfordataprocessingandstorage,itoften
andenvironments.
suffers from longer response time due to bandwidth
limitations and network latency. For delay-sensitive
7.6 Real-timemonitoring
applications such as video surveillance, edge com-
For real-time monitoring and quick AD, meth- puting provides a better solution (Srivastava and
odssuchasthoseproposedbyGirishandRao(2023) Singh, 2016). By performing preprocessing and
andSongYJetal.(2023)arehighlyeffective. Girish initial analysis locally on edge devices, edge com-
andRao(2023)usedstackedandbidirectionalLSTM puting reduces data transmission to the cloud and
models to detect cloud abnormalities from time- minimizes latency. This hybrid approach improves

Guietal./ FrontInform TechnolElectron Eng 202526(9):1551-1576 1567
real-time AD and response, making it suitable for tems. The collected data are then transmitted via
public safety, industrial security, and critical infras- communication networks to SCADA for monitoring
tructure monitoring(Shi WB etal.,2016). andsystemcontrol. However,sensorsandactuators
Recent advances, such as language-based video may fail due to attacks or insufficient maintenance,
anomaly detection (LAVAD) (Zanella et al., 2024) andattackerscanmanipulate controllers,communi-
and AnomalyRuler (Yang YC et al., 2024), propose cation networks, and SCADA systems. Therefore,
innovative training-free paradigms leveraging pre- the deployment of AD mechanisms is essential for
trained LLMs and vision language models (VLMs) safeguardingCPS againstpotentialthreats.
| forintelligentvideosurveillance. |     |                 |     | LAVADusesVLM- |     |          |               |     |           |     |     |     |     |
| -------------------------------- | --- | --------------- | --- | ------------- | --- | -------- | ------------- | --- | --------- | --- | --- | --- | --- |
|                                  |     |                 |     |               |     |          | 8.2 CPSattack |     | detection |     |     |     |     |
| based caption                    |     | for frame-level |     | descriptions, |     | applying |               |     |           |     |     |     |     |
promptsfortemporalaggregationandanomalyscor-
|     |     |     |     |     |     |     | Various | AD  | models | leverage | the | rich | represen- |
| --- | --- | --- | --- | --- | --- | --- | ------- | --- | ------ | -------- | --- | ---- | --------- |
ing, thus eliminating extensive training. Anoma- tational capacity of deep learning architectures to
| lyRuler                  | employs        | few-shot  | learning     |           | to induce    | rules |           |               |           |             |            |                 |      |
| ------------------------ | -------------- | --------- | ------------ | --------- | ------------ | ----- | --------- | ------------- | --------- | ----------- | ---------- | --------------- | ---- |
|                          |                |           |              |           |              |       | capture   | informative   |           | features    | from       | time-series     | data |
| fromnormalpatterns,using |                |           |              | deductive | reasoningfor |       |           |               |           |             |            |                 |      |
|                          |                |           |              |           |              |       | in CPSs.  | For instance, |           | Li D        | et al.     | (2019a)proposed |      |
| AD. These                | methodologies  |           | harness      |           | the inherent | rea-  |           |               |           |             |            |                 |      |
|                          |                |           |              |           |              |       | a novel   | approach      | employing |             | a GAN      | coupled         | with |
| soning                   | and contextual |           | capabilities |           | of LLMs,     | pro-  |           |               |           |             |            |                 |      |
|                          |                |           |              |           |              |       | LSTM-RNNs |               | within    | a composite | framework. |                 | This |
| viding                   | robust,        | scalable, | and          | rapidly   | adaptive     | solu- |           |               |           |             |            |                 |      |
frameworkisdesignedtomodelthenormaldistribu-
| tions essential |     | for real-time |     | surveillance | in  | dynamic |             |               |     |     |          |               |     |
| --------------- | --- | ------------- | --- | ------------ | --- | ------- | ----------- | ------------- | --- | --- | -------- | ------------- | --- |
|                 |     |               |     |              |     |         | tion of CPS | measurements, |     |     | with the | discriminator |     |
environments.
|     |     |     |     |     |     |     | tasked to | efficiently | identify |     | anomalies. | In  | addition |
| --- | --- | --- | --- | --- | --- | --- | --------- | ----------- | -------- | --- | ---------- | --- | -------- |
Thesecategorizedapproacheshighlightthever- to LSTM, a feedforward network (Feng and Tian,
| satility | and robustness |            | of  | various  | methods | in ad-    |               |          |                |              |        |              |       |
| -------- | -------------- | ---------- | --- | -------- | ------- | --------- | ------------- | -------- | -------------- | ------------ | ------ | ------------ | ----- |
|          |                |            |     |          |         |           | 2021) is      | employed | to             | characterize |        | practical    | CPSs. |
| dressing | different      | challenges |     | in cloud | and     | edge ser- |               |          |                |              |        |              |       |
|          |                |            |     |          |         |           | Subsequently, |          | the identified |              | system | is simulated | to    |
vice AD. By aligning each method with its optimal predictsensorreadings,withdeviationsbetweenob-
| application   | scenario, |            | these | techniques | enhance   | the |                          |          |        |     |               |            |           |
| ------------- | --------- | ---------- | ----- | ---------- | --------- | --- | ------------------------ | -------- | ------ | --- | ------------- | ---------- | --------- |
|               |           |            |       |            |           |     | servedandpredictedvalues |          |        |     | flaggedas     | anomalies. |           |
| effectiveness | and       | accuracyof |       | detecting  | anomalies | in  |                          |          |        |     |               |            |           |
|               |           |            |       |            |           |     | An                       | AE-based | method |     | for detecting |            | IoT-based |
diversecloudenvironments.
|      |                 |     |     |     |     |     | attacks was | introduced,  |     | involving |         | the construction |             |
| ---- | --------------- | --- | --- | --- | --- | --- | ----------- | ------------ | --- | --------- | ------- | ---------------- | ----------- |
|      |                 |     |     |     |     |     | of Mirai    | and BASHLITE |     | botnets   | to      | target           | IoT net-    |
| 8 AD | for IoTsecurity |     |     |     |     |     |             |              |     |           |         |                  |             |
|      |                 |     |     |     |     |     | works in    | a laboratory |     | setting   | (Meidan | et               | al., 2018). |
|      |                 |     |     |     |     |     | The method  | included     |     | launching | several | types            | of at-      |
IntherealmofIoTsecurity,cyber-physicalsys-
|     |     |     |     |     |     |     | tacks such | as Scan, | ACK, |     | SYN, and | UDP | flooding. |
| --- | --- | --- | --- | --- | --- | --- | ---------- | -------- | ---- | --- | -------- | --- | --------- |
tems (CPSs), such as water treatment systems and An AE trained on benign network traffic was used,
intelligentpowercontrolsystems,exposecriticalde-
withanalertbeingtriggeredwhenthereconstruction
| vices to | network | vulnerabilities. |     | These | systems | can |                                    |     |     |     |     |              |     |
| -------- | ------- | ---------------- | --- | ----- | ------- | --- | ---------------------------------- | --- | --- | --- | --- | ------------ | --- |
|          |         |                  |     |       |         |     | errorexceededapredefinedthreshold. |     |     |     |     | Furthermore, |     |
be compromised, and even the slightest deviation a regularized AE was presented to segregate known
| from expected |     | sensor | readingsor | controlcommands |     |     |     |     |     |     |     |     |     |
| ------------- | --- | ------ | ---------- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
attacksandnormaldataintoseparateregionswithin
| can indicate     |        | critical  | malfunctions, |       | potentially | lead-      |                               |       |                          |     |                  |          |          |
| ---------------- | ------ | --------- | ------------- | ----- | ----------- | ---------- | ----------------------------- | ----- | ------------------------ | --- | ---------------- | -------- | -------- |
|                  |        |           |               |       |             |            | thelatentspace(Vuetal.,2022). |       |                          |     | Itwaspositedthat |          |          |
| ing to cascading |        | failures. | Therefore,AD  |       |             | models are |                               |       |                          |     |                  |          |          |
|                  |        |           |               |       |             |            | the latentspace               |       | representationsofunknown |     |                  |          | attacks  |
| crucial          | in IoT | security, | enabling      | swift | corrective  | ac-        |                               |       |                          |     |                  |          |          |
|                  |        |           |               |       |             |            | would be                      | close | to those                 | of  | known            | attacks, | and this |
tionswhenalarmsareraisedtoprotectthesevulner-
|     |     |     |     |     |     |     | characteristicwasusedto |     |     | developaclassifierforde- |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----------------------- | --- | --- | ------------------------ | --- | --- | --- |
able systems.
tectionofIoT-basedattacks.
RecentmethodsenhanceCPSsecuritybylever-
8.1 Applicationdescription
|     |     |     |     |     |     |     | aging LLMs | with | embedding |     | models | (Diaf | et al., |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ---- | --------- | --- | ------ | ----- | ------- |
CPSs comprise physical systems, control sys- 2024)andretrieval-augmentedgeneration(RAG)to
tems, and supervisory control and data acquisition map attack patterns (Webb et al., 2024). Train-
(SCADA) systems. Various sensors are deployed to ing involves encapsulating attack data into vector
monitorthestatesofphysicalinfrastructures,suchas formats and using RAG for structured mappings
power plants and water treatment facilities. Based thatareevaluatedagainststandardmodelsforaccu-
on sensor feedback, controllers issue commands to racy. Another approachintegrates fine-tuned GPTs
manage critical devices within these physical sys- and BERT with LSTM networks. GPT predicts

1568 Guietal./FrontInform TechnolElectron Eng 202526(9):1551-1576
network traffic, BERT evaluates predictions, and developed an interior clustering tree to decompose
LSTM identifies malicious packets using datasets data into sub-distribution based on model predic-
such as CICIoT2023. A feedback loop refines LLM tions and generate the decomposition distribution
accuracy, ensuring proactive and effective detection rules. Subsequently, they formulated a composi-
indynamic IoTenvironments. tional boundary exploration algorithm to infer the
|     |     |     |     |     |     |     | decision | boundaries | and | derive | boundary |     | inference |
| --- | --- | --- | --- | --- | --- | --- | -------- | ---------- | --- | ------ | -------- | --- | --------- |
8.3 Data privacy rules. The decomposition distribution rules and
|               |             |               |              |          |             |         | boundary       | inference          | rules         | were            | further     | used      | to fa-   |
| ------------- | ----------- | ------------- | ------------ | -------- | ----------- | ------- | -------------- | ------------------ | ------------- | --------------- | ----------- | --------- | -------- |
| Data          | privacy     | is            | increasingly | becoming |             | a focal |                |                    |               |                 |             |           |          |
|               |             |               |              |          |             |         | cilitate       | the interpretation |               | of              | predictions |           | from un- |
| point in      | the field   | of CPS        | security,    | as       | the sensor  | and     |                |                    |               |                 |             |           |          |
|               |             |               |              |          |             |         | supervised     | AD                 | models.       | Han             | et al.      | (2021)    | devised  |
| actuator      | data        | transmitted   |              | through  | industrial  | net-    |                |                    |               |                 |             |           |          |
|               |             |               |              |          |             |         | an interpreter |                    | and distiller | to              | explain     | anomalies | for      |
| works contain |             | the operating |              | status   | and control | in-     |                |                    |               |                 |             |           |          |
|               |             |               |              |          |             |         | analysts.      | They               | framed        | an optimization |             | problem   | to       |
| structions    | of critical |               | facilities.  | If these | data        | are in- |                |                    |               |                 |             |           |          |
generate“reference”forinterpretinganomaliesacross
| tercepted | and | used during |     | global model | training, | it  |         |               |     |         |      |        |         |
| --------- | --- | ----------- | --- | ------------ | --------- | --- | ------- | ------------- | --- | ------- | ---- | ------ | ------- |
|           |     |             |     |              |           |     | various | data formats: |     | tabular | data | in the | Kitsune |
could result in significant security breaches. Feder- system (Mirsky et al., 2018),time-series data in the
atedlearning(FL)hasbeenemployedtosynchronize
DeepLogsystem(DuMetal.,2017),andgraphdata
| local models | across | gateways |     | in the | CPS or | IoT en- |                     |     |     |                |     |        |      |
| ------------ | ------ | -------- | --- | ------ | ------ | ------- | ------------------- | --- | --- | -------------- | --- | ------ | ---- |
|              |        |          |     |        |        |         | inthe graphlearning |     |     | withglobalview |     | (GLGV) | sys- |
vironment,withafocusonmaintainingthedatapri- tem (Bowman et al., 2020). Additionally, they em-
| vacyofindividualgateways. |      |            |      | Theapproachproposed |     |          |               |                  |        |                 |     |          |          |
| ------------------------- | ---- | ---------- | ---- | ------------------- | --- | -------- | ------------- | ---------------- | ------ | --------------- | --- | -------- | -------- |
|                           |      |            |      |                     |     |          | ployed        | two finite-state |        | machines        | to  | create   | the dis- |
| by Wang                   | N et | al. (2022) | uses | contrastive         |     | learning |               |                  |        |                 |     |          |          |
|                           |      |            |      |                     |     |          | tiller, which | can              | enable | security-domain |     | analysts | to       |
(CL)techniquestoimprovethetrafficdatarepresen-
|            |     |                |     |       |             |     | interact | with | detected      | anomalies | effectively. |          | Train-   |
| ---------- | --- | -------------- | --- | ----- | ----------- | --- | -------- | ---- | ------------- | --------- | ------------ | -------- | -------- |
| tation and | has | been evaluated |     | using | the NSK-KDD |     |          |      |               |           |              |          |          |
|            |     |                |     |       |             |     | ing LLMs | for  | interpretable |           | IoT          | security | involves |
dataset. Additionally,aprivacy-preservingfederated leveragingpretrainedmodelssuchasGPT-4fortheir
| PCA frameworkhas |     |          | been devised, | combining |         | feder-   |                    |       |                              |      |                 |     |      |
| ---------------- | --- | -------- | ------------- | --------- | ------- | -------- | ------------------ | ----- | ---------------------------- | ---- | --------------- | --- | ---- |
|                  |     |          |               |           |         |          | vastknowledgebase. |       | Housseletal.(2024)fine-tuned |      |                 |     |      |
| ated learning    |     | with PCA | to            | extract   | traffic | features |                    |       |                              |      |                 |     |      |
|                  |     |          |               |           |         |          | pretrained         | model | GPT-4                        | with | domain-specific |     | net- |
fromvariousIoTdeviceswithoutcompromisingdata work data. By using RAG, the model aligns real-
| exchange | (Nguyen  | et       | al., | 2023).    | Furthermore, |        | a              |           |               |              |      |                |         |
| -------- | -------- | -------- | ---- | --------- | ------------ | ------ | -------------- | --------- | ------------- | ------------ | ---- | -------------- | ------- |
|          |          |          |      |           |              |        | world threat   | patterns, |               | facilitating |      | the generation | of      |
| method   | has been | proposed |      | that uses | deep         | neural |                |           |               |              |      |                |         |
|          |          |          |      |           |              |        | human-readable |           | explanations. |              | This | process        | ensures |
networksforeachedgeIoTdevicewithinafederated
thatLLMscancontextualizethreatsandprovidede-
| framework | to aggregate |     | local | model | parameters. | A   |     |     |     |     |     |     |     |
| --------- | ------------ | --- | ----- | ----- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
tailedinterpretiveinsights.
| global DNN | is       | also designed |     | within         | this framework |          |              |     |     |                  |     |     |     |
| ---------- | -------- | ------------- | --- | -------------- | -------------- | -------- | ------------ | --- | --- | ---------------- | --- | --- | --- |
| to detect  | zero-day | attacks       |     | in IoT devices |                | (Popoola |              |     |     |                  |     |     |     |
|            |          |               |     |                |                |          | 9 Challenges |     | and | futuredirections |     |     |     |
etal.,2022).
|                   |     |             |     |                     |     |     | 9.1 Challenges  |     |     |                  |     |     |              |
| ----------------- | --- | ----------- | --- | ------------------- | --- | --- | --------------- | --- | --- | ---------------- | --- | --- | ------------ |
| 8.4 Interpretable |     | models      |     |                     |     |     |                 |     |     |                  |     |     |              |
|                   |     |             |     |                     |     |     | Althoughvarious |     |     | practicalmethods |     |     | in the field |
| Although          |     | deep models |     | provide informative |     | and |                 |     |     |                  |     |     |              |
accurate results, they are often considered “black- ofpatternregressionareadaptedforADtasks,there
|              |     |       |       |            |        |     | are specific | challenges |     | in AD | that | must | be consid- |
| ------------ | --- | ----- | ----- | ---------- | ------ | --- | ------------ | ---------- | --- | ----- | ---- | ---- | ---------- |
| box” models, |     | which | means | that these | models | are |              |            |     |       |      |      |            |
eredwhendesigningframeworksusingmethodsfrom
| unreliable | for | network | operators. | Despite |     | advance- |     |     |     |     |     |     |     |
| ---------- | --- | ------- | ---------- | ------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
ments in model accuracy, building trust with net- other machine learning domains such as computer
|               |          |                      |          |                |     |          | vision (CV) | and | NLP. | These | challenges | include | the |
| ------------- | -------- | -------------------- | -------- | -------------- | --- | -------- | ----------- | --- | ---- | ----- | ---------- | ------- | --- |
| work analysts |          | remains              | crucial. | Interpretative |     | mod-     |             |     |      |       |            |         |     |
| els usually   | generate | human-understandable |          |                |     | rules to | following:  |     |      |       |            |         |     |
explain anomalies, or apply existing interpretation 1. High dimensionality. Communication sys-
strategies in deep-learning domain to enhance the tems generate high-dimensional data from multiple
understandability for the AD models. To this end, sources, such as network logs, performance metrics,
several studies have been conducted to provide in- and user activity records. Analyzing these complex
sights into the interpretability of AD methods. For datatodetectanomaliesrequirestechniquesthatcan
instances, Li RY et al. (2024) proposed a rule ex- effectivelyhandletheincreaseddimensionalitywhile
tractionstrategyforunsupervisedADmodels. They maintainingcomputationalefficiency.

Guietal./ FrontInform TechnolElectron Eng 202526(9):1551-1576 1569
2. Nonstationary. Communication systems of- ing methods, such as bagging or boosting, can help
ten exhibit nonstationary, such as seasonalpatterns balance the distribution of anomalous and normal
andlong-termtrends,inuserbehavior,networktraf- samples and improve the overall performance and
fic,andresourceutilization. Distinguishingbetween stability of the AD system. Additionally, unsuper-
thegenuineanomaliesandtheexpectedpatternsbe- vised AD approaches, such as isolation forests or
comes challenging due to the presence of these sea- AEs, can reduce the dependency onlabeled data by
sonalandtrendcomponentsinthe data. learningtheinherentpatternsandstructureswithin
3. Class imbalance. Anomalies in communica- the communicationdata.
tion systems, such as network failures or network 2.DevelopingADsystemsresistanttoadversar-
| attacks, | are relatively rare | compared | to normal | sys- ialattacks |     |     |     |     |     |
| -------- | ------------------- | -------- | --------- | --------------- | --- | --- | --- | --- | --- |
tem behavior. This class imbalance can bias AD Future research on enhancing the resilience of
algorithmstowardthe majorityclass,reducingtheir AD systems against adversarial attacks may focus
sensitivity indetecting actualanomalies. on integrating robust adversarial training regimes
4.Labelsparsity.ObtaininglabeleddataforAD andensemblelearningmethods(Nawazetal.,2024).
| in communication | systems | is often | difficult | or im-    |         |           |         |            |     |
| ---------------- | ------- | -------- | --------- | --------- | ------- | --------- | ------- | ---------- | --- |
|                  |         |          |           | GANs (Xia | et al., | 2022; Lim | et al., | 2024; Lüer | and |
practical. Labeling anomalies requires domain ex- Bohm,2024)canbeusedtocreaterobustADmodels
pertise and can be time-consuming,especially given bytrainingthemonsimulatedadversarialscenarios,
thevastamountofdatageneratedbythesesystems. reducingfalsenegativesandfalse positives.
This scarcity of labeled data poses challenges for 3.RobustADindynamicandevolvingcommu-
| trainingsupervisedADmodels. |     |     |     | nicationnetworks |     |     |     |     |     |
| --------------------------- | --- | --- | --- | ---------------- | --- | --- | --- | --- | --- |
5.Conceptdrift.Internet-basedservicesincom- To ensure robust AD in dynamic communica-
munication systems often operate in dynamic envi- tion networks, future research may concentrate on
| ronmentswhere | the underlying | patternsandbehav- |     |          |               |         |       |        |          |
| ------------- | -------------- | ----------------- | --- | -------- | ------------- | ------- | ----- | ------ | -------- |
|               |                |                   |     | creating | self-adaptive | systems | using | online | learning |
iorschangeovertime. Thisconceptdriftnecessitates algorithms (Segerholm, 2023) and continual learn-
theadaptationofADmodelstoaccountforevolving ing approaches such as elastic weight consolida-
data patternsandensuredetectionaccuracy.
|                  |            |     |     | tion (EWC)  | (Ao              | and Fayek,        | 2023).       | Meta-learning     |     |
| ---------------- | ---------- | --- | --- | ----------- | ---------------- | ----------------- | ------------ | ----------------- | --- |
|                  |            |     |     | algorithms, | such             | as model-agnostic |              | meta-learning     |     |
| 9.2 Future       | directions |     |     |             |                  |                   |              |                   |     |
|                  |            |     |     | (MAML)      | (Griffiths       | et al.,           | 2019),       | can significantly |     |
|                  |            |     |     | enhance     | the adaptability |                   | of AD models | in dynamic        |     |
| 9.2.1 Robustness | inAD       |     |     |             |                  |                   |              |                   |     |
networks.
1.Enhancingrobustnesstoaddressconceptdrift
|     |     |     |     | 9.2.2 ExplainabilityinAD |     |     |     |     |     |
| --- | --- | --- | --- | ------------------------ | --- | --- | --- | --- | --- |
andclassimbalanceincommunicationsystems
Future researchshouldfocus ondeveloping AD 1. Enhancing explainability to address nonsta-
models with enhanced cross-domain robustness and tionaryandconceptdrift
adoptingrobustlearningstrategiestotackleconcept Incorporatingcausalreasoning,temporalcausal
driftandclassimbalanceincommunicationsystems. modeling, and domain knowledge into AD mod-
Transferlearningtechniques,suchasadversarialdo- els can help address the challenges of nonstation-
main adaptation (Shi YJ et al., 2022;Ozyurt et al., ary and concept drift in communication networks.
2023) and MMD minimization (Tzeng et al., 2014; By analyzing the relationships between the com-
Venkateswara et al., 2017; Wang YX et al., 2022), munication variables and their temporal dependen-
can align feature distributions across different com- cies,causalreasoningapproachescandistinguishbe-
munication environments, enabling models to learn tweenthe seasonalor trend-relatedchangesand the
transferable and domain-invariant representations. trueanomalies,providingamorecomprehensiveun-
GNNs (Dhadhania et al., 2024; Jin et al., 2024a) derstanding of the system’s behavior. Integrating
cancapturecomplexrelationshipsanddependencies domain knowledge through expert systems, graph-
incommunicationnetworks,facilitatingthegeneral- based representations, or modular neural networks
izationofADmodelsacrossvariousnetworktopolo- cangenerateexplanationsthatalignwiththeunique
gies and configurations. Oversampling techniques, challenges and terminology of communication net-
such as SMOTE or ADASYN, and ensemble learn- works. Thesetechniquesimprovetheinterpretability

1570 Guietal./FrontInform TechnolElectron Eng 202526(9):1551-1576
of AD models, and ensure that their predictions re- to their specialized pretraining, enabling them to
main robust in the face of evolving network condi- differentiate between true anomalies and innocuous
tions andshifting anomalypatterns. deviations caused by seasonal or trend-related fac-
2.Standardizationofexplainabilitymetrics tors. Furthermore, the powerful encoding capabili-
Future research could focus on developing a tiesofLLMscanbeusedforrepresentationlearning,
comprehensiveframeworkforevaluatingtheexplain- extracting low-dimensional semantic features from
ability of AD models in communication systems. high-dimensional communication time-series data,
This includes defining quantitative measures that makingthemmoretractableforAD tasks.
assess the clarity, conciseness, and relevance of ex- 2.TrainingtailoredLLMsfortime series
| planations, | considering |     | the | specific | challenges | and |     |         |     |             |     |                |     |
| ----------- | ----------- | --- | --- | -------- | ---------- | --- | --- | ------- | --- | ----------- | --- | -------------- | --- |
|             |             |     |     |          |            |     | To  | advance | LLM | performance |     | in time-series |     |
requirements of communication networks. Estab- AD, future research should focus on how to train
lishing standardized benchmarks and datasets will time-series specific LLMs. There are three main
| enable consistent |     | evaluation |     | and | comparison | of ex- |            |     |          |      |          |       |       |
| ----------------- | --- | ---------- | --- | --- | ---------- | ------ | ---------- | --- | -------- | ---- | -------- | ----- | ----- |
|                   |     |            |     |     |            |        | approaches | for | creating | such | tailored | LLMs: | zero- |
plainability acrossdifferentmodels andtechniques. shot, fine-tuning, and training from scratch. Zero-
3. Tailoring explanations to different shot strategies use pretrained LLMs without task-
stakeholders
|     |     |     |     |     |     |     | specific | data, | leveraging | the | models’ | broad | general- |
| --- | --- | --- | --- | --- | --- | --- | -------- | ----- | ---------- | --- | ------- | ----- | -------- |
Future research should prioritize the develop- ization abilities achieved through diverse pretrain-
| ment of | user-centric |     | explainability |     | frameworks | that |                   |     |       |      |     |                 |     |
| ------- | ------------ | --- | -------------- | --- | ---------- | ---- | ----------------- | --- | ----- | ---- | --- | --------------- | --- |
|         |              |     |                |     |            |      | ing. Prompt-based |     | LLMs, | such | as  | those employing |     |
adapttodiverseneedsandexpertiseofvariousstake- task-specificpromptsfortime-seriestasks,exemplify
holders. This involves designing explanation gener- thisapproach(XueandSalim,2024). Fine-tuning,a
| ation systems |     | that consider |     | user | profiles, | roles, and |          |      |            |          |     |           |        |
| ------------- | --- | ------------- | --- | ---- | --------- | ---------- | -------- | ---- | ---------- | -------- | --- | --------- | ------ |
|               |     |               |     |      |           |            | commonly | used | technique, | involves |     | adjusting | a pre- |
preferences to deliver personalized explanations for trained LLM on domain-specific data for enhanced
detectedanomalies. Thegoalistoenhanceusertrust task performance (Darban et al., 2024; Fang et al.,
| and decision-makingby |     |     | providingthe |     | most | relevant |        |             |     |          |          |     |         |
| --------------------- | --- | --- | ------------ | --- | ---- | -------- | ------ | ----------- | --- | -------- | -------- | --- | ------- |
|                       |     |     |              |     |      |          | 2024). | Fine-tuning |     | modifies | a subset | of  | parame- |
andactionableinsightsforeachstakeholder. ters, retaining core knowledge while improving do-
|     |     |     |     |     |     |     | main accuracy. |     | An  | advanced | fine-tuning |     | method |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | --- | -------- | ----------- | --- | ------ |
9.2.3 LLMapplicationsinAD
|               |     |      |     |         |     |            | incorporates |             | a multi-head | attention |      | mechanism    | to   |
| ------------- | --- | ---- | --- | ------- | --- | ---------- | ------------ | ----------- | ------------ | --------- | ---- | ------------ | ---- |
|               |     |      |     |         |     |            | convert      | time-series | data         | into      | text | format while | pre- |
| 1. Leveraging |     | LLMs | to  | address | AD  | challenges |              |             |              |           |      |              |      |
incommunicationsystems serving the original model parameters (Jin et al.,
|       |              |     |             |     |       |       | 2024b). | Training | from | scratchinvolvesdeveloping |     |     | a   |
| ----- | ------------ | --- | ----------- | --- | ----- | ----- | ------- | -------- | ---- | ------------------------- | --- | --- | --- |
| LLMs, | particularly |     | time-series |     | LLMs, | offer |         |          |      |                           |     |     |     |
dedicatedlargemodeloptimizedfortime-seriesanal-
| promising | solutions |     | to address | the | challenges | faced |     |     |     |     |     |     |     |
| --------- | --------- | --- | ---------- | --- | ---------- | ----- | --- | --- | --- | --- | --- | --- | --- |
by AD in communication systems. By harnessing ysisfromthe groundup(Gao SHet al.,2024). This
|                 |     |        |          |     |          |        | method | emphasizes | learning |     | temporal | dependencies |     |
| --------------- | --- | ------ | -------- | --- | -------- | ------ | ------ | ---------- | -------- | --- | -------- | ------------ | --- |
| the instruction |     | tuning | paradigm |     | and open | domain |        |            |          |     |          |              |     |
knowledge of LLMs, researchers can generate new and sequence patterns, improving performance for
data and enable active learning of evolving com- time-series tasks, but requiring extensive computa-
|            |           |     |          |     |       |            | tionalpoweranda |     | substantialdataset. |     |     |     |     |
| ---------- | --------- | --- | -------- | --- | ----- | ---------- | --------------- | --- | ------------------- | --- | --- | --- | --- |
| munication | patterns, |     | tackling | the | issue | of concept |                 |     |                     |     |     |     |     |
drift. Continual learning techniques (Gupta et al., 3. Addressing resource intensity in time-series
| 2021; Wu | et  | al., 2024) | and | change | point | detection | LLMsforAD |     |     |     |     |     |     |
| -------- | --- | ---------- | --- | ------ | ----- | --------- | --------- | --- | --- | --- | --- | --- | --- |
methods (Aminikhanghahi and Cook, 2017) can be Theresourceintensityoftraininganddeploying
employed to update LLMs incrementally and iden- time-series LLMs for AD is a significant challenge.
tify significantshifts in data patterns,ensuring that When models such as UniTS (Gao SH et al., 2024)
the models remain aligned with the latest trends. show superior performance, their computational
LLMs’ few-shot learning capabilities and unsuper- costs may outweigh the benefits. Future directions
vised representation learning can mitigate the im- should focus on developing efficient model architec-
pact of class imbalance and limited labeled data by tures and applying compression techniques such as
effectively learning from a small number of anoma- quantization (Lin Z et al., 2024), pruning (Lin Z
loussamplesandcapturingtemporalpatternswithin et al., 2024), and knowledge distillation (Wang L
thedata. Time-seriesLLMs,suchasUniTS(GaoSH and Yoon, 2022). Balancing performance with cost
et al., 2024),excelin contextualcomprehensiondue efficiency, scalability, and maintainability is crucial

Guietal./ FrontInform TechnolElectron Eng 202526(9):1551-1576 1571
3rd
forthepracticalvalueandlong-termoperationalsus- secure cyber physical systems. Proc Int Workshop
tainability ofLLMs inreal-worldAD applications. onCyber-Physical Systems forSmart Water Networks,
p.25-28. https://doi.org/10.1145/3055366.3055375
|     |     |     |     |     |     |     | AhmedM,MahmoodAN,HuJK,2016. |     |     |     | Asurveyofnetwork |     |
| --- | --- | --- | --- | --- | --- | --- | --------------------------- | --- | --- | --- | ---------------- | --- |
10 Conclusions
|     |     |     |     |     |     |     | anomaly | detection | techniques. | J   | Netw Comput | Appl, |
| --- | --- | --- | --- | --- | --- | --- | ------- | --------- | ----------- | --- | ----------- | ----- |
60:19-31. https://doi.org/10.1016/j.jnca.2015.11.016
This survey has comprehensively explored the AldribiA,TraoreI,MoaB,2018. Datasourcesanddatasets
landscape of AD in AIOps, covering applications in for cloud intrusion detection modeling and evaluation.
|         |         |             |            |     |        |     | In: Mishra | BSP,              | Das H, Dehuri | S,           | et al. | (Eds.), Cloud |
| ------- | ------- | ----------- | ---------- | --- | ------ | --- | ---------- | ----------------- | ------------- | ------------ | ------ | ------------- |
| network | traffic | monitoring, | networking |     | system | log |            |                   |               |              |        |               |
|         |         |             |            |     |        |     | Computing  | for Optimization: |               | Foundations, |        | Applica-      |
analysis, cloud and edge service provisioning, and tions,and Challenges. Springer, Cham, p.333-366.
IoT security. By examining diverse datasets and https://doi.org/10.1007/978-3-319-73676-1_13
methods across these domains, we have highlighted Al-HawawrehM,SitnikovaE,AboutorabN,2022. X-IIoTID:
the challenges and opportunities in each area. As a connectivity-agnostic and device-agnostic intrusion
|           |           |     |         |          |              |     | data set | for Industrial | Internet | of  | Things. | IEEE Int |
| --------- | --------- | --- | ------- | -------- | ------------ | --- | -------- | -------------- | -------- | --- | ------- | -------- |
| the field | continues | to  | evolve, | the need | for explain- |     |          |                |          |     |         |          |
ThingsJ, 9(5):3962-3977.
able, robust, and LLM-driven AD becomes increas- https://doi.org/10.1109/JIOT.2021.3102056
| ingly apparent. |     | Toadvance | state-of-the-arttechnol- |     |     |     |                     |     |         |            |       |         |
| --------------- | --- | --------- | ------------------------ | --- | --- | --- | ------------------- | --- | ------- | ---------- | ----- | ------- |
|                 |     |           |                          |     |     |     | Alsaedi A, Moustafa |     | N, Tari | Z, et al., | 2020. | TON_IoT |
ogy, researchers should focus on developing inter- telemetrydataset: anewgenerationdatasetofIoTand
|     |     |     |     |     |     |     | IIoTfordata-drivenintrusiondetectionsystems. |     |     |     |     | IEEE |
| --- | --- | --- | --- | --- | --- | --- | -------------------------------------------- | --- | --- | --- | --- | ---- |
pretablemodelsthatcaneffectivelyhandlecomplex,
Access, 8:165130-165150.
| high-dimensional |     | data | while | maintaining | resilience |     |     |     |     |     |     |     |
| ---------------- | --- | ---- | ----- | ----------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
https://doi.org/10.1109/ACCESS.2020.3022862
against adversarial attacks. Furthermore, the inte- AmerM,GoldsteinM,AbdennadherS,2013. Enhancingone-
gration of LLMs in AD pipelines holds promise for classsupportvectormachinesforunsupervisedanomaly
|           |            |          |                |               |          |        | detection. | Proc             | ACM SIGKDD | Workshop |     | on Outlier |
| --------- | ---------- | -------- | -------------- | ------------- | -------- | ------ | ---------- | ---------------- | ---------- | -------- | --- | ---------- |
| enhancing | the        | accuracy | and efficiency |               | of these | sys-   |            |                  |            |          |     |            |
|           |            |          |                |               |          |        | Detection  | and Description, |            | p.8-15.  |     |            |
| tems. By  | addressing |          | these key      | challengesand |          | lever- |            |                  |            |          |     |            |
https://doi.org/10.1145/2500853.2500857
agingtheinsightsgainedfromthissurvey,theAIOps
|     |     |     |     |     |     |     | AminikhanghahiS,CookDJ,2017. |     |     | Asurveyofmethods |     | for |
| --- | --- | --- | --- | --- | --- | --- | ---------------------------- | --- | --- | ---------------- | --- | --- |
community can pave the way for more reliable, se- timeserieschangepointdetection. KnowlInformSyst,
51(2):339-367.
cure,andintelligentADsolutions.
https://doi.org/10.1007/s10115-016-0987-z
|     |     |     |     |     |     |     | AndresiniG,AppiceA,MalerbaD,2021. |     |     |     | Autoencoder-based |     |
| --- | --- | --- | --- | --- | --- | --- | --------------------------------- | --- | --- | --- | ----------------- | --- |
Contributors
|     |     |     |     |     |     |     | deep metric | learning | for | network | intrusion | detection. |
| --- | --- | --- | --- | --- | --- | --- | ----------- | -------- | --- | ------- | --------- | ---------- |
Alltheauthorscontributedtotheoutlineofthereview. Inform Sci,569:706-727.
Jiayi GUI,ZhongnanMA,HaoZHOU,YanSU,andMiaoru https://doi.org/10.1016/j.ins.2021.05.016
|       |         |            |       |               |     |     | AoSI,FayekH,2023. |          | Continualdeeplearningfortimeseries |     |     |     |
| ----- | ------- | ---------- | ----- | ------------- | --- | --- | ----------------- | -------- | ---------------------------------- | --- | --- | --- |
| ZHANG | drafted | the paper. | Jiayi | GUI, Zhongnan | MA, | and |                   |          |                                    |     |     |     |
|       |         |            |       |               |     |     | modeling.         | Sensors, | 23(16):7167.                       |     |     |     |
KeYU organized the paper. Jiayi GUI, Zhongnan MA,Hao https://doi.org/10.3390/s23167167
ZHOU,YanSU,andMiaoruZHANGrevisedthepaper,while
|     |     |     |     |     |     |     | Audibert J, Michiardi |     | P, Guyard | F, et | al., 2020. | USAD: |
| --- | --- | --- | --- | --- | --- | --- | --------------------- | --- | --------- | ----- | ---------- | ----- |
Jiayi GUI, Zhongnan MA, Hao ZHOU, Ke YU, and Xiaofei unsupervised anomaly detection on multivariate time
series. Proc26thACMSIGKDDIntConfonKnowledge
| WU reviewed | and | finalizedthe | paper. |     |     |     |           |                           |     |     |     |     |
| ----------- | --- | ------------ | ------ | --- | --- | --- | --------- | ------------------------- | --- | --- | --- | --- |
|             |     |              |        |     |     |     | Discovery | & DataMining,p.3395-3404. |     |     |     |     |
https://doi.org/10.1145/3394486.3403392
Conflictofinterest
|     |             |         |      |           |             |     | BaiJZ,BaiS,ChuYF,etal.,2023. |     |     | QWENtechnicalreport. |     |     |
| --- | ----------- | ------- | ---- | --------- | ----------- | --- | ---------------------------- | --- | --- | -------------------- | --- | --- |
| All | the authors | declare | that | they have | no conflict | of  |                              |     |     |                      |     |     |
https://doi.org/10.48550/arXiv.2309.16609
interest. BalasubramanianP,SebyJ,Kostakos P,2023. Transformer-
|     |     |     |     |     |     |     | basedLLMsincybersecurity: |           |                    | anin-depthstudyonlog |              |        |
| --- | --- | --- | --- | --- | --- | --- | ------------------------- | --------- | ------------------ | -------------------- | ------------ | ------ |
|     |     |     |     |     |     |     | anomaly                   | detection | and conversational |                      | defense      | mecha- |
|     |     |     |     |     |     |     | nisms. IEEE               | Int       | Conf on            | BigData,             | p.3590-3599. |        |
References
https://doi.org/10.1109/BigData59044.2023.10386976
| Aboubacar | A, El             | Machkouri | M, 2020.     | Recursive | kernel | den-   |                               |            |                |                       |     |     |
| --------- | ----------------- | --------- | ------------ | --------- | ------ | ------ | ----------------------------- | ---------- | -------------- | --------------------- | --- | --- |
|           |                   |           |              |           |        |        | BansodSD,Nandedkar            |            | AV,2020.       | Crowdanomalydetection |     |     |
| sity      | estimation        | for       | time series. | IEEE      | Trans  | Inform |                               |            |                |                       |     |     |
|           |                   |           |              |           |        |        | andlocalizationusinghistogram |            |                | ofmagnitudeandmo-     |     |     |
| Theory,   | 66(10):6378-6388. |           |              |           |        |        |                               |            |                |                       |     |     |
|           |                   |           |              |           |        |        | mentum.                       | VisComput, | 36(3):609-620. |                       |     |     |
https://doi.org/10.1109/TIT.2020.3014797
https://doi.org/10.1007/s00371-019-01647-0
| Abrams L,      | 2020. | CenturyLink | routing | issue | led to outages |     |                  |     |       |          |     |               |
| -------------- | ----- | ----------- | ------- | ----- | -------------- | --- | ---------------- | --- | ----- | -------- | --- | ------------- |
|                |       |             |         |       |                |     | Basati A, Faghih | MM, | 2023. | APAE: an | IoT | intrusion de- |
| on Hulu,Steam, |       | Discord,    | more.   |       |                |     |                  |     |       |          |     |               |
https://www.bleepingcomputer.com/news/technology/ tection system usingasymmetric parallel auto-encoder.
centurylink-routing-issue-led-to-outages-on-hulu-steam NeurComput Appl, 35(7):4813-4833.
-discord-more [Accessed onApr. 1, 2024]. https://doi.org/10.1007/s00521-021-06011-9
Ahmed CM, Palleti VR, Mathur AP, 2017. WADI: a wa- Bochner S, Chandrasekharan K, 1949. Fourier Transforms.
ter distribution testbed for research in the design of Princeton University Press, Princeton, USA.

1572 Guietal./FrontInform TechnolElectron Eng 202526(9):1551-1576
Bowman B, Laprade C, Ji YD, et al., 2020. Detecting lat- Darban ZZ, Yang YY, Webb GI, et al., 2024. DACAD:
eral movement in enterprise computer networks with domainadaptationcontrastivelearningforanomalyde-
unsupervised graph AI. 23rd Int Symp on Research in tection inmultivariate timeseries.
Attacks, Intrusions andDefenses, p.257-268. https://doi.org/10.48550/arXiv.2404.11269
|                                  |          |           |      |                |     |        | DataSetsAI,                              | 2020. | Water | Pumps. |     |             |     |
| -------------------------------- | -------- | --------- | ---- | -------------- | --- | ------ | ---------------------------------------- | ----- | ----- | ------ | --- | ----------- | --- |
| BrownTB,MannB,RyderN,etal.,2020. |          |           |      | Languagemodels |     |        |                                          |       |       |        |     |             |     |
|                                  |          |           |      | 34th           |     |        | https://datasets.ai/datasets/water-pumps |       |       |        |     | [Accessedon |     |
| are                              | few-shot | learners. | Proc | Int Conf       | on  | Neural |                                          |       |       |        |     |             |     |
Aug. 17, 2025].
| Information |     | Processing | Systems, | p.1877-1901. |     |     |     |     |     |     |     |     |     |
| ----------- | --- | ---------- | -------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ChandN,MishraP,KrishnaCR,etal.,2016. Acomparative DhadhaniaA,BhatiaJ,MehtaR,etal.,2024. Unleashingthe
analysis of SVM and its stacking with other classifica- powerofSDNandGNNfornetworkanomalydetection:
tion algorithm for intrusion detection. Int Conf on state-of-the-art,challenges,andfuturedirections. Secur
Advances in Computing, Communication, & Automa- Priv,7(1):e337. https://doi.org/10.1002/spy2.337
tion, p.1-6. Diaf A, Korba AA, Karabadji NE, et al., 2024. Beyond
|     |     |     |     |     |     |     | detection: |     | leveraging | large | language | models | for cyber |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --- | ---------- | ----- | -------- | ------ | --------- |
https://doi.org/10.1109/ICACCA.2016.7578859
|          |             |     |        |                  |     |        | attack      | prediction |            | in IoT | networks. | 20th Int    | Conf on |
| -------- | ----------- | --- | ------ | ---------------- | --- | ------ | ----------- | ---------- | ---------- | ------ | --------- | ----------- | ------- |
| Chandola | V, Banerjee | A,  | Kumar  | V, 2009. Anomaly |     | detec- |             |            |            |        |           |             |         |
|          |             |     |        |                  |     |        | Distributed |            | Computing  | in     | Smart     | Systems and | the In- |
| tion:    | asurvey.    | ACM | Comput | Surv, 41(3):15.  |     |        |             |            |            |        |           |             |         |
|          |             |     |        |                  |     |        | ternet      | ofThings,  | p.117-123. |        |           |             |         |
https://doi.org/10.1145/1541880.1541882
https://doi.org/10.1109/DCOSS-IoT61029.2024.00026
Chang C, Peng WC, Chen TF, 2024. LLM4TS: two-stage Du M, Li FF, Zheng GN, et al., 2017. DeepLog: anomaly
fine-tuning for time-series forecasting with pre-trained detection and diagnosis from system logs through deep
| LLMs.   | https://doi.org/10.48550/arXiv.2308.08469 |           |          |                    |           |     |                |      |           |        |              |             |     |
| ------- | ----------------------------------------- | --------- | -------- | ------------------ | --------- | --- | -------------- | ---- | --------- | ------ | ------------ | ----------- | --- |
|         |                                           |           |          |                    |           |     | learning.      | Proc | ACM       | SIGSAC | Conf         | on Computer | and |
| Chen M, | Zheng                                     | AX, Lloyd | J, et    | al., 2004. Failure | diagnosis |     |                |      |           |        |              |             |     |
|         |                                           |           |          |                    |           |     | Communications |      | Security, |        | p.1285-1298. |             |     |
| using   | decision                                  | trees.    | Int Conf | on Autonomic       | Comput-   |     |                |      |           |        |              |             |     |
https://doi.org/10.1145/3133956.3134015
ing, p.36-43.
|     |     |     |     |     |     |     | DuZX,QianYJ,LiuX,etal.,2022. |     |     |     | GLM:generallanguage |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---------------------------- | --- | --- | --- | ------------------- | --- | --- |
https://doi.org/10.1109/ICAC.2004.1301345
|     |     |     |     |     |     |     | model | pretraining |     | withautoregressive |     | blankinfilling. |     |
| --- | --- | --- | --- | --- | --- | --- | ----- | ----------- | --- | ------------------ | --- | --------------- | --- |
ChenZH,ZhengLN,LuC,etal.,2023. ChatGPT informed https://doi.org/10.48550/arXiv.2103.10360
graph neural network forstock movement prediction. DuanXY,FuY,WangK,2023. Networktrafficanomalyde-
https://arxiv.org/abs/2306.03763 tection method based on multi-scale residual classifier.
ChenZM,YeoCK,LeeBS, etal.,2018. Autoencoder-based Comput Commun, 198:206-216.
network anomaly detection. Wireless Telecommunica- https://doi.org/10.1016/j.comcom.2022.10.024
tions Symp,p.1-5. Egersdoerfer C, Zhang D, Dai D, 2023. Early exploration
https://doi.org/10.1109/WTS.2018.8363930 of using ChatGPT for log-based anomaly detection on
32nd
Choi K, Yi JH, Park C, et al., 2021. Deep learning for parallel file systems logs. Proc Int Symp on
anomalydetectionintime-seriesdata: review,analysis, High-PerformanceParallelandDistributedComputing,
and guidelines. IEEE Access, 9:120043-120065. p.315-316. https://doi.org/10.1145/3588195.3595943
https://doi.org/10.1109/ACCESS.2021.3107975 Ekambaram V, Jati A, Dayama P, et al., 2024. Tiny time
|           |         |               |         |               |          |     | mixers        | (TTMs): | fast        | pre-trained |              | models for  | enhanced |
| --------- | ------- | ------------- | ------- | ------------- | -------- | --- | ------------- | ------- | ----------- | ----------- | ------------ | ----------- | -------- |
| Chouhan   | N, Khan | A, Khan       | HUR,    | 2019. Network | anomaly  |     |               |         |             |             |              |             |          |
|           |         |               |         |               |          |     | zero/few-shot |         | forecasting | of          | multivariate | timeseries. |          |
| detection |         | using channel | boosted | and residual  | learning |     |               |         |             |             |              |             |          |
https://doi.org/10.48550/arXiv.2401.03955
| based   | deep       | convolutional | neural | network. | Appl | Soft |           |      |          |             |     |              |     |
| ------- | ---------- | ------------- | ------ | -------- | ---- | ---- | --------- | ---- | -------- | ----------- | --- | ------------ | --- |
|         |            |               |        |          |      |      | Esling P, | Agon | C, 2012. | Time-series |     | data mining. | ACM |
| Comput, | 83:105612. |               |        |          |      |      |           |      |          |             |     |              |     |
Comput Surv,45(1):12.
https://doi.org/10.1016/j.asoc.2019.105612
https://doi.org/10.1145/2379776.2379788
| Cook AA, | Mook            | AA G, | Fan Z,    | 2020. Anomaly | detection  |     |          |     |         |        |            |             |     |
| -------- | --------------- | ----- | --------- | ------------- | ---------- | --- | -------- | --- | ------- | ------ | ---------- | ----------- | --- |
|          |                 |       |           |               |            |     | Fang YQ, | Yap | PT, Lin | WL, et | al., 2024. | Source-free | un- |
| for      | IoT time-series | data: | a survey. | IEEE          | Int Things | J,  |          |     |         |        |            |             |     |
7(7):6481-6494. supervised domain adaptation: a survey. Neur Netw,
174:106230.
https://doi.org/10.1109/jiot.2019.2958185
https://doi.org/10.1016/j.neunet.2024.106230
| Cup K,2007. | KDD | Cup1999 | Data. |     |     |     |         |          |         |       |            |         |       |
| ----------- | --- | ------- | ----- | --- | --- | --- | ------- | -------- | ------- | ----- | ---------- | ------- | ----- |
|             |     |         |       |     |     |     | Farrukh | YA, Wali | S, Khan | I, et | al., 2024. | XG-NID: | dual- |
https://kdd.ics.uci.edu/databases/kddcup99/kddcup99
|             |           |        |              |           |          |     | modality | network |        | intrusion | detection | using a  | heteroge- |
| ----------- | --------- | ------ | ------------ | --------- | -------- | --- | -------- | ------- | ------ | --------- | --------- | -------- | --------- |
| .html       | [Accessed | onApr. | 1, 2024].    |           |          |     |          |         |        |           |           |          |           |
|             |           |        |              |           |          |     | neous    | graph   | neural | network   | andlarge  | language | model.    |
| Dai L, Chen | WC,       | LiuYW, | et al.,2022. | Switching | Gaussian |     |          |         |        |           |           |          |           |
https://doi.org/10.48550/arXiv.2408.16021
mixture variational RNN for anomaly detection of Feng C, Tian PW, 2021. Time series anomaly detection for
diverse CDN websites. IEEE Conf on Computer cyber-physical systems via neural system identification
Communications, p.300-309. and Bayesian filtering. Proc 27th ACM SIGKDD Conf
https://doi.org/10.1109/INFOCOM48880.2022.9796836 onKnowledge Discovery & Data Mining,p.2858-2867.
Dang WX, Zhou BY, Wei LW, et al., 2021. TS-Bert: time https://doi.org/10.1145/3447548.3467137
| series | anomaly  | detection       | via | pre-training | model      | Bert. |                                      |               |     |           |       |               |            |
| ------ | -------- | --------------- | --- | ------------ | ---------- | ----- | ------------------------------------ | ------------- | --- | --------- | ----- | ------------- | ---------- |
|        |          |                 |     |              |            |       | FerragMA,FrihaO,HamoudaD,etal.,2022. |               |     |           |       | Edge-IIoTset: |            |
| 21st   | Int Conf | onComputational |     | Science,     | p.209-223. |       |                                      |               |     |           |       |               |            |
|        |          |                 |     |              |            |       | anew                                 | comprehensive |     | realistic | cyber | security      | dataset of |
https://doi.org/10.1007/978-3-030-77964-1_17
IoTandIIoTapplicationsforcentralizedandfederated
Dang YN,LinQW,Huang P,2019. AIOps: real-worldchal- learning. IEEE Access, 10:40281-40306.
41st
lenges and research innovations. IEEE/ACM Int https://doi.org/10.1109/ACCESS.2022.3165809
Conf on Software Engineering: Companion Proceed- Gao S, Huang YF, Zhang S, et al., 2020. Short-term
ings, p.4-5. runoff prediction withGRU and LSTM networks with-
https://doi.org/10.1109/ICSE-Companion.2019.00023 out requiring time step optimization during sample

Guietal./ FrontInform TechnolElectron Eng 202526(9):1551-1576 1573
generation. JHydrol, 589:125188. Huang JJ, Kurniawan E, Sun SM, 2022. Cellular KPI
https://doi.org/10.1016/j.jhydrol.2020.125188 anomalydetectionwithGANandtimeseriesdecompo-
Gao SH, Koker T, Queen O, et al., 2024. UniTS: a unified sition. IEEEIntConfonCommunications,p.4074-4079.
multi-tasktimeseries model. https://doi.org/10.1109/ICC45855.2022.9838810
https://doi.org/10.48550/arXiv.2403.00131 Hundman K, Constantinou V, Laporte C, et al., 2018. De-
Georgiou T, Liu Y, Chen W, et al., 2020. A survey of tecting spacecraft anomalies using LSTMS and non-
traditional and deep learning-based feature descriptors parametric dynamic thresholding. Proc 24th ACM
for high dimensional data in computer vision. Int J SIGKDD Int Conf on Knowledge Discovery & Data
Multimed Inform Retr,9(3):135-170. Mining,p.387-395.
https://doi.org/10.1007/s13735-019-00183-w https://doi.org/10.1145/3219819.3219845
Girish L, Rao SKN, 2023. Anomaly detection in cloud en- Hwang RH, Peng MC, Huang CW, et al., 2020. An unsu-
vironmentusingartificialintelligencetechniques. Com- pervised deep learning model for early network traffic
puting, 105(3):675-688. anomalydetection. IEEE Access, 8:30387-30399.
https://doi.org/10.1007/s00607-021-00941-x https://doi.org/10.1109/ACCESS.2020.2973023
Griffiths TL, Callaway F, Chang MB, et al., 2019. Doing IMT-2030(6G)PromotionGroup,2021. WhitePaperon6G
more with less: meta-reasoning and meta-learning in VisionandCandidate Technologies. Technical Report.
humans andmachines. CurrOpinBehav Sci,29:24-30. Jiang AQ, Sablayrolles A, Mensch A, et al., 2023. Mistral
https://doi.org/10.1016/j.cobeha.2019.01.005 7B.https://doi.org/10.48550/arXiv.2310.06825
Gruver N, Finzi M, Qiu SK, et al., 2024. Large language Jiang J, Liu FG, Ng WWY, et al., 2023. AERF: adaptive
models are zero-shot time series forecasters. Proc 37th ensemblerandomfuzzyalgorithmforanomalydetection
Int Conf on Neural Information Processing Systems, incloud computing. Comput Commun, 200:86-94.
p.19622-19635. https://doi.org/10.1016/j.comcom.2023.01.004
https://dl.acm.org/doi/10.5555/3666122.3666983 Jin M, Koh HY, Wen QS, et al., 2024a. A survey on graph
Guigou F, Collet P, Parrend P, 2019. SCHEDA: lightweight neural networks for time series: forecasting, classifica-
Euclidean-like heuristics for anomaly detection in peri- tion, imputation, and anomalydetection.
odic timeseries. Appl Soft Comput, 82:105594. https://doi.org/10.48550/arXiv.2307.03759
https://doi.org/10.1016/j.asoc.2019.105594 JinM,WangSY,MaLT,etal.,2024b. Time-LLM:timese-
Gupta V, Narwariya J, Malhotra P, et al., 2021. Continual riesforecasting byreprogramming large language mod-
learningformultivariatetimeseries tasks withvariable els. https://doi.org/10.48550/arXiv.2310.01728
input dimensions. IEEE Int Conf on Data Mining, Khalaf OI, Ogudo KA, Sangeetha SKB, 2022. Design of
p.161-170. graph-based layered learning-driven model for anomaly
https://doi.org/10.1109/ICDM51629.2021.00026 detectionindistributedcloudIoTnetwork. MobInform
Halbouni A,Gunawan TS, Habaebi MH, et al.,2022. CNN- Syst,2022:6750757.
LSTM: hybrid deep neural network for network intru- https://doi.org/10.1155/2022/6750757
siondetection system. IEEE Access, 10:99837-99849. Khan MA, 2021. HCRNNIDS: hybrid convolutional recur-
https://doi.org/10.1109/ACCESS.2022.3206425 rent neural network-based network intrusion detection
Han DQ, Wang ZL, Chen WQ, et al., 2021. DeepAID: in- system. Processes, 9(5):834.
terpreting and improving deep learning-based anomaly https://doi.org/10.3390/pr9050834
detection in security applications. Proc ACM SIGSAC KhatibzadehL,BornaeeZ,BafghiAG,2019. Applyingcatas-
Conf on Computer and Communications Security, trophe theory for network anomaly detection in cloud
p.3197-3217. https://doi.org/10.1145/3460120.3484589 computingtraffic. SecurCommunNetw,2019:5306395.
Hawkins DM, 1980. Identification of Outliers. Springer, https://doi.org/10.1155/2019/5306395
Dordrecht, Netherlands. KoroniotisN,MoustafaN,SitnikovaE,etal.,2019. Towards
https://doi.org/10.1007/978-94-015-3994-4 thedevelopmentofrealisticbotnetdatasetintheInter-
HeQ, Zheng YJ,Zhang CL, etal.,2020. MTAD-TF:multi- net of Things for network forensic analytics: BoT-IoT
variate time series anomaly detection using the combi- dataset. Future GenerComput Syst,100:779-796.
nation of temporal pattern and feature pattern. Com- https://doi.org/10.1016/j.future.2019.05.041
plexity,2020:8846608. KourtisMA,XilourisG,GardikisG,etal.,2016. Statistical-
https://doi.org/10.1155/2020/8846608 based anomaly detection forNFV services. IEEE Conf
Heinle A, 2022. The Canada wide Rogers outage on July on Network Function Virtualization and Software De-
8, 2022: what exactly happened & how can it be finedNetworks, p.161-166.
prevented? https://doi.org/10.1109/NFV-SDN.2016.7919492
https://www.coguard.io/post/canada-rogers-outage- KYODONEWS, 2022. KDDInetwork outage affects record
root-cause-analysis [Accessedon Apr. 15, 2024]. 30.91millionusers.
Hnamte V, Hussain J, 2023. DCNNBiLSTM: an efficient https://english.kyodonews.net/news/2022/07/57bbb532
hybrid deep learning-based intrusion detection system. c4d7-kddi-network-outage-affects-record-3091-million-
Telemat Inform Rep, 10:100053. users.html [Accessed onApr. 15, 2024].
https://doi.org/10.1016/j.teler.2023.100053 Lalotra GS, Kumar V, Bhatt A, et al., 2022. iReTADS:
Houssel PR, Singh P, Layeghy S, et al., 2024. Towards an intelligent real-time anomaly detection system for
explainablenetworkintrusiondetectionusinglargelan- cloud communications using temporal data summa-
guage models. rization and neural network. Secur Commun Netw,
https://doi.org/10.48550/arXiv.2408.04342 2022:9149164. https://doi.org/10.1155/2022/9149164

1574 Guietal./FrontInform TechnolElectron Eng 202526(9):1551-1576
Le XH, Ho HV, Lee G, et al., 2019. Application of long Lüdtke O, Robitzsch A, West SG, 2020. Regression models
short-term memory (LSTM) neural network for flood involving nonlinear effects with missing data: a se-
forecasting. Water,11(7):1387. quential modeling approach using Bayesian estimation.
https://doi.org/10.3390/w11071387 PsycholMethods, 25(2):157-181.
LeeMC,LinJC,GranEG,2020. RePAD:real-timeproactive https://doi.org/10.1037/met0000233
| anomaly | detection | for | time series. | Proc | 34th | Int Conf |              |     |               |     |           |       |            |
| ------- | --------- | --- | ------------ | ---- | ---- | -------- | ------------ | --- | ------------- | --- | --------- | ----- | ---------- |
|         |           |     |              |      |      |          | Lüer F, Bohm | C,  | 2024. Anomaly |     | detection | using | generative |
onAdvancedInformationNetworkingandApplications,
|              |     |     |     |     |     |     | adversarial    |     | networks                       | reviewingmethodological |     |     | progress |
| ------------ | --- | --- | --- | --- | --- | --- | -------------- | --- | ------------------------------ | ----------------------- | --- | --- | -------- |
| p.1291-1302. |     |     |     |     |     |     | andchallenges. |     | ACMSIGKDDExplorNewsl,25(2):29- |                         |     |     |          |
https://doi.org/10.1007/978-3-030-44041-1_110 41. https://doi.org/10.1145/3655103.3655109
Li D, Chen DC, Goh J, et al., 2019a. Anomaly detection Lunardi WT, Lopez MA, Giacalone JP, 2023. ARCADE:
with generative adversarial networks for multivariate adversarially regularized convolutional autoencoder for
timeseries. https://doi.org/10.48550/arXiv.1809.04758 network anomaly detection. IEEE Trans Netw Serv
Li D, Chen DC, Jin BH, et al., 2019b. MAD-GAN: Manage,20(2):1305-1318.
multivariateanomalydetectionfortimeseriesdatawith https://doi.org/10.1109/TNSM.2022.3229706
| generative    | adversarial |     | networks.  | 28th | IntConfonArti- |     |         |           |           |      |          |        |          |
| ------------- | ----------- | --- | ---------- | ---- | -------------- | --- | ------- | --------- | --------- | ---- | -------- | ------ | -------- |
|               |             |     |            |      |                |     | Luo H,  | Zhong     | SS, 2017. | Gas  | turbine  | engine | gas path |
| ficial Neural | Networks,   |     | p.703-716. |      |                |     |         |           |           |      |          |        |          |
|               |             |     |            |      |                |     | anomaly | detection | using     | deep | learning | with   | Gaussian |
https://doi.org/10.1007/978-3-030-30490-4_56
|                  |      |                                 |             |     |               |     | distribution. |     | Prognostics | and | System | Health | Manage- |
| ---------------- | ---- | ------------------------------- | ----------- | --- | ------------- | --- | ------------- | --- | ----------- | --- | ------ | ------ | ------- |
| LiG,JungJJ,2023. |      | Deeplearningforanomalydetection |             |     |               | in  |               |     |             |     |        |        |         |
|                  |      |                                 |             |     |               |     | mentConf,     |     | p.1-6.      |     |        |        |         |
| multivariate     | time | series:                         | approaches, |     | applications, | and |               |     |             |     |        |        |         |
https://doi.org/10.1109/PHM.2017.8079166
challenges. Inform Fus, 91:93-102. MascaroS,NicholsoAE,KorbKB,2014. Anomalydetection
https://doi.org/10.1016/j.inffus.2022.10.008 invessel tracks using Bayesian networks. Int J Approx
Li RY, Li Q, Zhang Y, et al., 2024. Interpreting unsuper- Reason, 55(1):84-98.
visedanomalydetection insecurity viaruleextraction. https://doi.org/10.1016/j.ijar.2013.03.012
37th
| Proc                                       | Int            | Conf on      | Neural        | Information | Processing |           |             |             |                   |                           |       |         |           |
| ------------------------------------------ | -------------- | ------------ | ------------- | ----------- | ---------- | --------- | ----------- | ----------- | ----------------- | ------------------------- | ----- | ------- | --------- |
|                                            |                |              |               |             |            |           | Mathur AP,  | Tippenhauer |                   | NO, 2016.                 | SWaT: | a water | treat-    |
| Systems,                                   | p.62224-62243. |              |               |             |            |           |             |             |                   |                           |       |         |           |
|                                            |                |              |               |             |            |           | menttestbed |             | forresearch       | andtrainingonICSsecurity. |       |         |           |
| LiangY,ZhangY,SivasubramaniamA,etal.,2005. |                |              |               |             |            | Filtering |             |             |                   |                           |       |         |           |
|                                            |                |              |               |             |            |           | Int         | Workshop    | on Cyber-Physical |                           |       | Systems | for Smart |
| failure                                    | logs for       | a BlueGene/L |               | prototype.  | Int        | Conf on   |             |             |                   |                           |       |         |           |
|                                            |                |              |               |             |            |           | Water       | Networks,   | p.31-36.          |                           |       |         |           |
| Dependable                                 | Systems        |              | and Networks, | p.476-485.  |            |           |             |             |                   |                           |       |         |           |
https://doi.org/10.1109/CySWater.2016.7469060
https://doi.org/10.1109/DSN.2005.50
|                 |     |       |            |       |         |         | MeidanY,BohadanaM,MathovY,etal.,2018. |     |           |     |            | N-BaIoT— |       |
| --------------- | --- | ----- | ---------- | ----- | ------- | ------- | ------------------------------------- | --- | --------- | --- | ---------- | -------- | ----- |
| Liang YL, Zhang | YY, | Xiong | H, et al., | 2007. | Failure | predic- |                                       |     |           |     |            |          |       |
|                 |     |       |            |       |         |         | network-based                         |     | detection | of  | IoT botnet | attacks  | using |
7th
tioninIBMBlueGene/Leventlogs. IEEEIntConf deep autoencoders. IEEE Pervasive Comput, 17(3):12-
on DataMining,p.583-588.
22. https://doi.org/10.1109/MPRV.2018.03367731
https://doi.org/10.1109/ICDM.2007.46
|                                |           |          |           |                    |           |     | Meng WB,     | Liu        | Y, Zhu          | YC, et        | al., 2019.   | LogAnomaly:      |           |
| ------------------------------ | --------- | -------- | --------- | ------------------ | --------- | --- | ------------ | ---------- | --------------- | ------------- | ------------ | ---------------- | --------- |
| LimW,YongKSC,LauBT,etal.,2024. |           |          |           | Futureofgenerative |           |     |              |            |                 |               |              |                  |           |
|                                |           |          |           |                    |           |     | unsupervised |            | detection       | of sequential |              | and quantitative |           |
| adversarial                    | networks  |          | (GAN) for | anomaly            | detection | in  |              |            |                 |               |              |                  |           |
|                                |           |          |           |                    |           |     | anomalies    |            | in unstructured | logs.         | Proc         | 28th             | Int Joint |
| network                        | security: | areview. | Comput    | Secur,139:103733.  |           |     |              |            |                 |               |              |                  |           |
|                                |           |          |           |                    |           |     | Confon       | Artificial | Intelligence,   |               | p.4739-4745. |                  |           |
https://doi.org/10.1016/j.cose.2024.103733
|               |     |                |             |               |     |            | MirskyY,DoitshmanT,EloviciY,etal.,2018. |     |                                           |     |        | Kitsune: | an        |
| ------------- | --- | -------------- | ----------- | ------------- | --- | ---------- | --------------------------------------- | --- | ----------------------------------------- | --- | ------ | -------- | --------- |
| Lin QW, Zhang | HY, | Lou            | JG, et al., | 2016.         | Log | clustering |                                         |     |                                           |     |        |          |           |
|               |     |                |             |               |     |            | ensemble                                | of  | autoencoders                              | for | online | network  | intrusion |
| based problem |     | identification | for         | onlineservice |     | systems.   |                                         |     |                                           |     |        |          |           |
|               |     |                |             |               |     |            | detection.                              |     | https://doi.org/10.48550/arXiv.1802.09089 |     |        |          |           |
Proc38thIntConfonSoftwareEngineeringCompanion,
p.102-111. Montgomery B, 2024. Large-scale cellularphone outage hits
Lin Z, Qu GQ, Chen QY, et al., 2024. Pushing large lan- AT&Tcustomers across US.
https://www.theguardian.com/technology/2024/feb/22
| guage | models | to the | 6G edge: | vision, | challenges, | and |                  |     |           |     |        |            |     |
| ----- | ------ | ------ | -------- | ------- | ----------- | --- | ---------------- | --- | --------- | --- | ------ | ---------- | --- |
|       |        |        |          |         |             |     | /phone-outage-us |     | [Accessed |     | onApr. | 15, 2025]. |     |
opportunities.
|     |     |     |     |     |     |     | Moustafa | N, Slay | J, 2015. | UNSW-NB15: |     | a comprehen- |     |
| --- | --- | --- | --- | --- | --- | --- | -------- | ------- | -------- | ---------- | --- | ------------ | --- |
https://doi.org/10.48550/arXiv.2309.16739
|                 |          |      |                 |         |           |          | sive       | data set | for network | intrusion |       | detection | systems  |
| --------------- | -------- | ---- | --------------- | ------- | --------- | -------- | ---------- | -------- | ----------- | --------- | ----- | --------- | -------- |
| LiuC, Antypenko | R,Sushko |      | I, et al.,2022. |         | Intrusion | detec-   |            |          |             |           |       |           |          |
|                 |          |      |                 |         |           |          | (UNSW-NB15 |          | network     | data      | set). | Military  | Communi- |
| tion system     | after    | data | augmentation    | schemes |           | based on |            |          |             |           |       |           |          |
the VAE and CVAE. IEEE Trans Reliab, 71(2):1000- cations and Information Systems Conf,p.1-6.
1010. https://doi.org/10.1109/TR.2022.3164877 https://doi.org/10.1109/MilCIS.2015.7348942
LiuFT,TingKM,ZhouZH,2008. Isolationforest. 8thIEEE Nawaz A, Khan SS, Ahmad A, 2024. Ensemble of autoen-
Int Conf on DataMining,p.413-422. coders for anomaly detection in biomedical data: a
https://doi.org/10.1109/ICDM.2008.17 narrative review. IEEE Access, 12:17273-17289.
Liu YL, Tao SM, Meng WB, et al., 2024. LogPrompt: https://doi.org/10.1109/ACCESS.2024.3360691
|     |     |     |     |     |     |     | NetoECP,DadkhahS,FerreiraR,etal.,2023. |     |     |     |     | CICIoT2023: |     |
| --- | --- | --- | --- | --- | --- | --- | -------------------------------------- | --- | --- | --- | --- | ----------- | --- |
promptengineeringtowardszero-shotandinterpretable
|               |     | 46th     |     |          |     |          | a real-time |     | dataset | and benchmark |     | for large-scale | at- |
| ------------- | --- | -------- | --- | -------- | --- | -------- | ----------- | --- | ------- | ------------- | --- | --------------- | --- |
| log analysis. |     | IEEE/ACM |     | Int Conf | on  | Software |             |     |         |               |     |                 |     |
Engineering, p.364-365. tacks inIoT environment. Sensors, 23(13):5941.
https://doi.org/10.1145/3639478.3643108 https://doi.org/10.3390/s23135941
Lu HM, Wang T, Xu X, et al., 2022. Cognitive memory- Ngo MV, Luo T, Chaouchi H, et al., 2020. Contextual-
guided autoencoder for effective intrusion detection bandit anomaly detection for IoT data in distributed
in Internet of Things. IEEE Trans Industr Inform, hierarchical edge computing. IEEE 40th Int Conf on
| 18(5):3358-3366. |     |     |     |     |     |     | Distributed |     | ComputingSystems, |     | p.1227-1230. |     |     |
| ---------------- | --- | --- | --- | --- | --- | --- | ----------- | --- | ----------------- | --- | ------------ | --- | --- |
https://doi.org/10.1109/TII.2021.3102637 https://doi.org/10.1109/ICDCS47774.2020.00191

Guietal./ FrontInform TechnolElectron Eng 202526(9):1551-1576 1575
Ngo MV, Luo T, Quek TQS, 2021. Adaptive anomaly de- Schneible J, Lu A, 2017. Anomaly detection on the edge.
tection forInternet of Thingsinhierarchical edge com- IEEE MilitaryCommunications Conf, p.678-682.
puting: a contextual-bandit approach. ACM Trans Int https://doi.org/10.1109/MILCOM.2017.8170817
Things, 3(1):4. SegerholmL,2023. UnsupervisedOnlineAnomalyDetection
https://doi.org/10.1145/3480172 inMultivariate Time-Series.
Nguyen TA, He JY, Le LT, et al., 2023. Federated PCA https://stsprogrammet.se/wp-content/uploads/2023/
on Grassmann manifold for anomaly detection in IoT 02/2312_Ludvig_Segerholm.pdf [Accessed on Apr. 1,
networks. IEEE Conf on Computer Communications, 2024].
p.1-10. ShanSW,HuoYT,SuYX,etal.,2024. Faceityourselves: an
https://doi.org/10.1109/infocom53939.2023.10229026 LLM-basedtwo-stage strategy to localize configuration
Oliner A, Stearley J, 2007. What supercomputers say: a errorsvialogs. Proc33rd ACMSIGSOFTIntSympon
study of five system logs. 37th Annual IEEE/IFIP Int Software Testing andAnalysis,p.13-25.
ConfonDependable SystemsandNetworks, p.575-584. https://doi.org/10.1145/3650212.3652106
https://doi.org/10.1109/DSN.2007.103 Sharafaldin I, Lashkari AH, Ghorbani AA, 2018. Toward
OpenAI, 2024. GPT-4technical report. generating a new intrusion detection dataset and in-
https://doi.org/10.48550/arXiv.2303.08774 trusion traffic characterization. Proc 4th Int Conf on
OzyurtY,FeuerriegelS,ZhangC,2023. Contrastivelearning Information Systems Security and Privacy, p.108-116.
for unsupervised domainadaptation of timeseries. https://doi.org/10.5220/0006639801080116
https://doi.org/10.48550/arXiv.2206.06243 Sharafaldin I, Lashkari AH, Hakak S, et al., 2019. Develop-
Pajouh HH, Dastghaibyfard G, Hashemi S, 2017. Two-tier ingrealisticdistributeddenialofservice(DDoS)attack
network anomaly detection model: a machine learning dataset and taxonomy. Int Carnahan Conf on Security
approach. JIntellInform Syst,48(1):61-74. Technology, p.1-8.
https://doi.org/10.1007/s10844-015-0388-x https://doi.org/10.1109/CCST.2019.8888419
Parameswarappa P, Shah T, Lanke GR, 2023. A machine Shi WB, Cao J, Zhang Q, et al., 2016. Edge computing:
learning-based approach for anomaly detection for se- visionandchallenges. IEEEIntThingsJ,3(5):637-646.
cure cloudcomputing environments. Int Conf onIntel- https://doi.org/10.1109/JIOT.2016.2579198
ligent Data Communication Technologies and Internet Shi YJ, Ying XH, Yang JF, 2022. Deep unsupervised do-
of Things, p.931-940. mainadaptationwithtimeseriessensordata: asurvey.
https://doi.org/10.1109/IDCIoT56793.2023.10053518 Sensors, 22(15):5507.
Peng YH, Tan AP, Wu JJ, et al., 2019. Hierarchical edge https://doi.org/10.3390/s22155507
computing: anovelmulti-sourcemulti-dimensionaldata SmithD,GuanQ,FuS,2010. Ananomalydetectionframe-
anomaly detection scheme for Industrial Internet of workforautonomicmanagement ofcomputecloudsys-
Things. IEEE Access, 7:111257-111270. tems. IEEE 34th Annual Computer Software and Ap-
https://doi.org/10.1109/ACCESS.2019.2930627 plications Conf Workshops, p.376-381.
Popoola SI,AndeR,AdebisiB,etal.,2022. Federated deep https://doi.org/10.1109/COMPSACW.2010.72
learning for zero-day botnet attack detection in IoT- Song J, Takakura H, Okabe Y, et al., 2013. Toward a more
edge devices. IEEE Int ThingsJ, 9(5):3930-3944. practical unsupervised anomaly detection system. In-
https://doi.org/10.1109/JIOT.2021.3100755 formSci,231:4-14.
Ratsch G, Mika S, Scholkopf B, et al., 2002. Constructing https://doi.org/10.1016/j.ins.2011.08.011
boostingalgorithmsfromSVMs: anapplicationtoone- Song YJ, Xin RY, Chen P, et al., 2023. Identifying per-
classclassification. IEEE TransPattAnalMachIntell, formance anomalies in fluctuating cloud environments:
24(9):1184-1199. a robust correlative-GNN-based explainable approach.
https://doi.org/10.1109/TPAMI.2002.1033211 Future GenerComput Syst,145:77-86.
Ren HS, Xu BX, Wang YJ, et al., 2019. Time-series https://doi.org/10.1016/j.future.2023.03.020
anomalydetectionserviceatMicrosoft. Proc25thACM Srivastava S,Singh SP, 2016. A survey on latency reduction
SIGKDD Int Conf on Knowledge Discovery & Data approaches forperformance optimizationincloudcom-
Mining,p.3009-3017. puting. 2nd Int Conf on Computational Intelligence &
https://doi.org/10.1145/3292500.3330680 CommunicationTechnology, p.111-115.
Ren KY, Yuan S, Zhang C, et al., 2023. CANET: a hi- Su J, Jiang CF, Jin X, et al., 2024. Large language models
erarchical CNN-attention model for network intrusion for forecasting and anomaly detection: a systematic
detection. Comput Commun, 205:170-181. literature review.
https://doi.org/10.1016/j.comcom.2023.04.018 https://doi.org/10.48550/arXiv.2402.10350
Ren PZ, Xiao Y, Chang XJ, et al., 2021. A survey of deep Tavallaee M, Bagheri E, Lu W, et al., 2009. A detailed
active learning. ACM Comput Surv,54(9):180. analysis of the KDD CUP 99 data set. IEEE Symp
https://doi.org/10.1145/3472291 onComputationalIntelligenceforSecurityandDefense
Reynolds D. 2009. Gaussian mixture models. In: Li SZ, Applications,p.1-6.
Jain A (Eds.), Encyclopedia of Biometrics. Springer, https://doi.org/10.1109/CISDA.2009.5356528
Boston, MA. TouvronH,LavrilT,IzacardG,etal.,2023a. LLaMA:open
https://doi.org/10.1007/978-0-387-73003-5_196 andefficient foundation language models.
Rokach L, Maimon O. 2005. Clustering methods. In: Mai- https://doi.org/10.48550/arXiv.2302.13971
mon O, Rokach L (Eds.), Data Miningand Knowledge Touvron H, Martin L, Stone K, et al., 2023b. LLaMA 2:
Discovery Handbook. Springer, Boston, MA. openfoundation andfine-tuned chat models.
https://doi.org/10.1007/0-387-25465-X_15 https://doi.org/10.48550/arXiv.2307.09288

1576 Guietal./FrontInform TechnolElectron Eng 202526(9):1551-1576
Tuli S, Casale G, Jennings NR, 2022. TranAD: deep trans- TransKnowlData Eng,36(11):6851-6864.
former networks for anomaly detection in multivariate https://doi.org/10.1109/TKDE.2023.3342137
timeseries data. Yang L, Chen JJ, Wang Z, et al., 2021. Semi-supervised
https://doi.org/10.48550/arXiv.2201.07284 log-based anomaly detection via probabilistic label es-
Tzeng E, Hoffman J, Zhang N, et al., 2014. Deep domain timation. IEEE/ACM 43rd Int Conf onSoftware Engi-
| confusion: | maximizingfordomaininvariance. |     |     |     |     |     | neering, | p.1448-1460. |     |     |     |     |
| ---------- | ------------------------------ | --- | --- | --- | --- | --- | -------- | ------------ | --- | --- | --- | --- |
https://doi.org/10.48550/arXiv.1412.3474 https://doi.org/10.1109/ICSE43902.2021.00130
Venkateswara H, Eusebio J, Chakraborty S, et al., 2017. Yang YC, Lee K, Dariush B, et al., 2024. Follow the rules:
|     |     |     |     |     |     |     | reasoning | for | video | anomaly | detection with | large lan- |
| --- | --- | --- | --- | --- | --- | --- | --------- | --- | ----- | ------- | -------------- | ---------- |
Deephashingnetworkforunsuperviseddomainadapta-
|                                              |     |     |     |     |     |     | guage | models. |     |     |     |     |
| -------------------------------------------- | --- | --- | --- | --- | --- | --- | ----- | ------- | --- | --- | --- | --- |
| tion. ProcIEEEConfonComputerVisionandPattern |     |     |     |     |     |     |       |         |     |     |     |     |
https://doi.org/10.48550/arXiv.2407.10299
| Recognition, | p.5385-5394. |     |     |     |     |     |           |       |           |             |         |         |
| ------------ | ------------ | --- | --- | --- | --- | --- | --------- | ----- | --------- | ----------- | ------- | ------- |
|              |              |     |     |     |     |     | Yu XY, Li | T, Hu | AQ, 2020. | Time-series | network | anomaly |
https://doi.org/10.1109/CVPR.2017.572
IEEE6th
Vu L, Cao VL, Nguyen QU, et al., 2022. Learning latent detection basedonbehaviourcharacteristics.
representation for IoT anomaly detection. IEEE Trans IntConfonComputerandCommunications,p.568-572.
Cybern,52(5):3769-3782. https://doi.org/10.1109/ICCC51575.2020.9345249
https://doi.org/10.1109/TCYB.2020.3013416 ZanellaL,MenapaceW,ManciniM,etal.,2024. Harnessing
WangL,YoonKJ,2022. Knowledgedistillationandstudent- large language models for training-free video anomaly
teacher learning for visual intelligence: a review and detection. Proc IEEE/CVF Conf on Computer Vision
new outlooks. IEEE Trans Patt Anal Mach Intell, andPattern Recognition, p.18527-18536.
44(6):3048-3068. https://doi.org/10.1109/CVPR52733.2024.01753
|     |     |     |     |     |     |     | Zeng AH, | Liu X, Du | ZX, | et al., 2023. | GLM-130B: | an open |
| --- | --- | --- | --- | --- | --- | --- | -------- | --------- | --- | ------------- | --------- | ------- |
https://doi.org/10.1109/TPAMI.2021.3055564
|              |     |       |         |             |          |     | bilingualpre-trained |     |     | model. |     |     |
| ------------ | --- | ----- | ------- | ----------- | -------- | --- | -------------------- | --- | --- | ------ | --- | --- |
| Wang N, Chen | YM, | Hu Y, | et al., | 2022. FeCo: | boosting |     |                      |     |     |        |     |     |
https://doi.org/10.48550/arXiv.2210.02414
| intrusion    | detection    | capability |           | in IoT      | networks | via  |           |                   |      |        |                  |                |
| ------------ | ------------ | ---------- | --------- | ----------- | -------- | ---- | --------- | ----------------- | ---- | ------ | ---------------- | -------------- |
|              |              |            |           |             |          |      | Zhang JQ, | Wang ZZ,          | Meng | JJ, et | al., 2019.       | Boosting posi- |
| contrastive  | learning.    |            | IEEE Conf | on Computer |          | Com- |           |                   |      |        |                  |                |
|              |              |            |           |             |          |      | tiveand   | unlabeledlearning |      | for    | anomalydetection | with           |
| munications, | p.1409-1418. |            |           |             |          |      |           |                   |      |        |                  |                |
https://doi.org/10.1109/INFOCOM48880.2022.9796926 multi-features. IEEE Trans Multimedia, 21(5):1332-
Wang W, Zhu M, Zeng XW, et al., 2017. Malware traf- 1344. https://doi.org/10.1109/TMM.2018.2871421
fic classification using convolutional neural network for ZhangP,NiuK,TianH,etal.,2019. Technologyprospectof
representation learning. Int Conf on Information Net- 6G mobile communications. J Commun, 40(1):141-148
| working, | p.712-717. |     |     |     |     |     | (inChinese). |     |     |     |     |     |
| -------- | ---------- | --- | --- | --- | --- | --- | ------------ | --- | --- | --- | --- | --- |
https://doi.org/10.1109/ICOIN.2017.7899588 Zhang SL, Zhao CY, Sui YC, et al., 2021. Robust KPI
Wang YX, Yan J, Ye XY, et al., 2022. Few-shot trans- anomalydetection forlarge-scalesoftwareserviceswith
fer learning with attention mechanism for high-voltage partial labels. IEEE 32nd Int Symp on Software Relia-
|         |         |                  |     |            |     |       | bilityEngineering, |     | p.103-114. |     |     |     |
| ------- | ------- | ---------------- | --- | ---------- | --- | ----- | ------------------ | --- | ---------- | --- | --- | --- |
| circuit | breaker | fault diagnosis. |     | IEEE Trans | Ind | Appl, |                    |     |            |     |     |     |
https://doi.org/10.1109/ISSRE52982.2021.00023
58(3):3353-3360.
|     |     |     |     |     |     |     | ZhangX,LinQW,XuY,etal.,2019a. |     |     |     | Cross-datasettimese- |     |
| --- | --- | --- | --- | --- | --- | --- | ----------------------------- | --- | --- | --- | -------------------- | --- |
https://doi.org/10.1109/TIA.2022.3159617
|          |         |          |          |       |           |     | riesanomalydetectionforcloudsystems. |     |     |     |     | ProcUSENIX |
| -------- | ------- | -------- | -------- | ----- | --------- | --- | ------------------------------------ | --- | --- | --- | --- | ---------- |
| Webb BK, | Purohit | S, Meyur | R, 2024. | Cyber | knowledge |     |                                      |     |     |     |     |            |
completion usinglarge language models. Annual Technical Conf,p.1063-1076.
https://doi.org/10.48550/arXiv.2409.16176 Zhang X, Xu Y, Lin QW, et al., 2019b. Robust log-based
27th
Wu TT, LuoLH, LiYF, et al.,2024. Continual learning for anomaly detection on unstable log data. Proc
large language models: asurvey. ACMJointMeetingonEuropeanSoftwareEngineering
https://doi.org/10.48550/arXiv.2402.01364 Conf and Symp on the Foundations of Software Engi-
Xia X, Pan XZ, Li N, et al., 2022. GAN-based anomaly neering, p.807-817.
detection: areview. Neurocomputing, 493:497-535. https://doi.org/10.1145/3338906.3338931
https://doi.org/10.1016/j.neucom.2021.12.093 ZhongZY,FanQL,ZhangJC,etal.,2023. Asurveyoftime
Xu HW, Chen WX, Zhao NW, et al., 2018. Unsupervised seriesanomalydetectionmethodsintheAIOpsdomain.
https://doi.org/10.48550/arXiv.2308.00393
| anomalydetection            |            | viavariational |     | auto-encoder     |     | forsea- |                           |             |           |                        |            |          |
| --------------------------- | ---------- | -------------- | --- | ---------------- | --- | ------- | ------------------------- | ----------- | --------- | ---------------------- | ---------- | -------- |
|                             |            |                |     |                  |     |         | ZhuB,LiJ,GuRB,etal.,2020. |             |           | Anapproachtocloudplat- |            |          |
| sonalKPIsinwebapplications. |            |                |     | ProcWorldWideWeb |     |         |                           |             |           |                        |            |          |
|                             |            |                |     |                  |     |         | form                      | log anomaly | detection | based                  | on natural | language |
| Conf,                       | p.187-196. |                |     |                  |     |         |                           |             |           |                        |            |          |
processingandLSTM.Proc3rdIntConfonAlgorithms,
https://doi.org/10.1145/3178876.3185996
Xu W, Huang L, Fox A, et al., 2009. Detecting large-scale Computingand Artificial Intelligence, Article88.
system problems by mining console logs. Proc ACM https://doi.org/10.1145/3446132.3446415
SIGOPS 22nd Symp on Operating Systems Principles, ZhuangFZ,QiZY,DuanKY,etal.,2021. Acomprehensive
p.117-132. https://doi.org/10.1145/1629575.1629587 survey ontransfer learning. Proc IEEE, 109(1):43-76.
Xue H, Salim FD, 2024. PromptCast: a new prompt-based https://doi.org/10.1109/JPROC.2020.3004555
| learning | paradigm | for | time series | forecasting. |     | IEEE |     |     |     |     |     |     |
| -------- | -------- | --- | ----------- | ------------ | --- | ---- | --- | --- | --- | --- | --- | --- |