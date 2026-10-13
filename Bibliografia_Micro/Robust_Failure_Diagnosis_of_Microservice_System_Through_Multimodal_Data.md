IEEETRANSACTIONSONSERVICESCOMPUTING,VOL.16,NO.6,NOVEMBER/DECEMBER2023 3851
| Robust |     |     | Failure |         | Diagnosis |     |            | of  | Microservice |      |     |     | System |     |     |
| ------ | --- | --- | ------- | ------- | --------- | --- | ---------- | --- | ------------ | ---- | --- | --- | ------ | --- | --- |
|        |     |     |         | Through |           |     | Multimodal |     |              | Data |     |     |        |     |     |
ShenglinZhang ,Member,IEEE,PengxiangJin ,ZihanLin ,YongqianSun ,Member,IEEE,
BichengZhang ,SiboXia ,ZhengdanLi ,ZhenyuZhong ,MinghuaMa ,Member,IEEE,WaJin ,
|     |     |     | DaiZhang |     | ,ZhenyuZhu |     | ,andDanPei |     | ,SeniorMember,IEEE |     |     |     |     |     |     |
| --- | --- | --- | -------- | --- | ---------- | --- | ---------- | --- | ------------------ | --- | --- | --- | --- | --- | --- |
Abstract—Automatic failure diagnosis is crucial for large mi- I. INTRODUCTION
croservicesystems.Currently,mostfailurediagnosismethodsrely
MICROSERVICESarchitectureisbecomingincreasingly
| solely on | single-modal |     | data (i.e., | using | either | metrics, | logs, or |     |     |     |     |     |     |     |     |
| --------- | ------------ | --- | ----------- | ----- | ------ | -------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
traces). In this study, we conduct an empirical study using real- popularforitsreliabilityandscalability[1].Typically,it
worldfailurecasestoshowthatcombiningthesesourcesofdata isalarge-scaledistributedsystemwithdozenstothousandsof
| (multimodal | data) | leads | to a more | accurate | diagnosis. |     | However, |     |     |     |     |     |     |     |     |
| ----------- | ----- | ----- | --------- | -------- | ---------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
serviceinstancesrunningonvariousenvironments(e.g.,phys-
effectivelyrepresentingthesedataandaddressingimbalancedfail-
|     |     |     |     |     |     |     |     | ical machines, |     | VMs, or | containers) | [2]. | Due | to the complex |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ------- | ----------- | ---- | --- | -------------- | --- |
uresremainchallenging.Totackletheseissues,weproposeDiag-
anddynamicnatureofmicroservicesystems,thefailureofone
Fusion,arobustfailurediagnosisapproachthatusesmultimodal
data. It leverages embedding techniques and data augmentation serviceinstancecanpropagatetootherserviceinstances,result-
to represent the multimodal data of service instances, combines ing in user dissatisfaction and financial losses for the service
| deployment | data | and | traces to | build a | dependency |     | graph, and |     |     |     |     |     |     |     |     |
| ---------- | ---- | --- | --------- | ------- | ---------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
provider.Forexample,AmazonWebService(AWS)suffereda
| uses a graph | neural | network | to  | localize | the root | cause | instance |     |     |     |     |     |     |     |     |
| ------------ | ------ | ------- | --- | -------- | -------- | ----- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
failureinDecember2021thatimpactedthewholenetworking
anddeterminethefailuretype.Ourevaluationsusingreal-world
systemandtooknearlysevenhourstodiagnoseandmitigate[3].
| datasets | show that | DiagFusion | outperforms |     | existing |     | methods | in  |     |     |     |     |     |     |     |
| -------- | --------- | ---------- | ----------- | --- | -------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
termsofrootcauseinstancelocalization(improvingby20.9%to Therefore,itiscrucialtotimelyandaccuratelydiagnosefailures
368%) and failure type determination (improving by 11.0% to inmicroservicesystems.
169%). To effectively diagnose failures, microservice system oper-
Index Terms—Microservice systems, failure diagnosis, multi- ators typically collect three types of monitoring data: traces,
modaldata,graphneuralnetwork. logs, and metrics. Traces are tree-structured data that record
|            |          |     |                |         |     |           |          | the detailed |           | invocation   | flow of user | requests. |              | Logs are       | semi- |
| ---------- | -------- | --- | -------------- | ------- | --- | --------- | -------- | ------------ | --------- | ------------ | ------------ | --------- | ------------ | -------------- | ----- |
|            |          |     |                |         |     |           |          | structured   | text      | that records | hardware     |           | and software | events         | of    |
|            |          |     |                |         |     |           |          | a service    | instance, | including    | business     |           | events,      | state changes, |       |
| Manuscript | received | 19  | February 2023; | revised | 22  | May 2023; | accepted |              |           |              |              |           |              |                |       |
14June2023.Dateofpublication27June2023;dateofcurrentversion13 hardwareerrors,etc.Metricsaretimeseriesindicatingservice
December2023.ThisworkwassupportedinpartbytheAdvancedResearch status,includingsystemmetrics(e.g.,CPUutilization,memory
| Project of | ChinaunderGrant |     | 31511010501,in |     | partbythe | National | Natural |              |     |                |         |     |        |                  |     |
| ---------- | --------------- | --- | -------------- | --- | --------- | -------- | ------- | ------------ | --- | -------------- | ------- | --- | ------ | ---------------- | --- |
|            |                 |     |                |     |           |          |         | utilization) | and | user-perceived | metrics |     | (e.g., | average response |     |
ScienceFoundationofChinaunderGrants62272249and62072264,andinpart
|     |     |     |     |     |     |     |     | time, | error rate). | From | now on, | we use | the | term modality | to  |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | ------------ | ---- | ------- | ------ | --- | ------------- | --- |
bytheNaturalScienceFoundationofTianjinunderGrant21JCQNJC00180.
RecommendedforacceptancebyT.Batista.(Correspondingauthor:Yongqian describeaparticulardatatype.Fig.1showsanexampleofthe
Sun.)
threemodalitiesofamicroservicesystem.
ShenglinZhangiswiththeCollegeofSoftware,NankaiUniversity,Tianjin
Automaticfailurediagnosisofmicroservicesystemshasbeen
300071,China,alsowiththeKeyLaboratoryofDataandIntelligentSystem
Security,MinistryofEducation,Tianjin300071,China,andalsowiththeHaihe atopicofgreatinterestovertheyears,particularlywhenidentify-
LaboratoryofInformationTechnologyApplicationInnovation(HL-IT),Tianjin
ingtherootcauseinstanceanddeterminingthefailuretype.Most
300350,China(e-mail:zhangsl@nankai.edu.cn).
approachesrelyonsingle-modaldata,suchastraces[1],[4],[5],
PengxiangJin,ZihanLin,YongqianSun,SiboXia,ZhengdanLi,Zhenyu
Zhong, and Wa Jin are with the College of Software, Nankai Univer- [6], logs [7], [8], [9], [10], or metrics [11], [12], [13], [14], to
sity, Tianjin 300071, China (e-mail: jinpengxiang@mail.nankai.edu.cn; linz- capturefailurepatterns.However,relyingsolelyonsingle-modal
ihan@mail.nankai.edu.cn;sunyongqian@nankai.edu.cn;xiasibo@mai.nankai.
edu.cn; lzd@nankai.edu.cn; zyzhong@mail.nankai.edu.cn; 1913173@mail. data for diagnosing failures is not effective enough for two
nankai.edu.cn). reasons.First,afailurecanimpactmultipleaspectsofaservice
BichengZhangiswiththeSchoolofComputerScience,FudanUniversity, instance, causing more than one modality to exhibit abnormal
Shanghai200437,China(e-mail:22210240069@m.fudan.edu.cn).
Minghua Ma is with the Microsoft, Beijing 100080, China (e-mail: patterns.Usingjustonedatasourcecannotfullycapturethese
minghuama@microsoft.com). patterns and accurately distinguish between different types of
Dai Zhang and Zhenyu Zhu are with the ZhejiangE-CommerceBank Co., failures. Second, some types of failures may not be reflected
| Ltd., Hangzhou, |     | Zhejiang | 310013, China | (e-mail: | henry.zd@mybank.cn; |     |     |     |     |     |     |     |     |     |     |
| --------------- | --- | -------- | ------------- | -------- | ------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
incertainmodalities,makingitdifficultformethodsrelyingon
michael.zzy@mybank.cn).
DanPeiiswiththeDepartmentofComputerScience,TsinghuaUniversity, thatmodalitytoidentifythesefailures.
Beijing100190,China,andalsowiththeBeijingNationalResearchCenterfor
Moreover,weconductanempiricalstudyonanopen-source
InformationScienceandTechnology,Beijing100084,China(e-mail:peidan@
|     |     |     |     |     |     |     |     | dataset | to verify | the necessity | of  | combining |     | multimodal | data |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | --------- | ------------- | --- | --------- | --- | ---------- | ---- |
tsinghua.edu.cn).
DigitalObjectIdentifier10.1109/TSC.2023.3290018 for robust failure diagnosis. As listed in Table I, the dataset
1939-1374©2023IEEE.Personaluseispermitted,butrepublication/redistributionrequiresIEEEpermission.
Seehttps://www.ieee.org/publications/rights/index.htmlformoreinformation.
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on November 13,2025 at 00:49:52 UTC from IEEE Xplore.  Restrictions apply.

3852 IEEETRANSACTIONSONSERVICESCOMPUTING,VOL.16,NO.6,NOVEMBER/DECEMBER2023
TABLEI
DETAILEDINFORMATIONOFTHEFAILURESINTHEEMPIRICALSTUDY
|     |     |     |     |     | and | metric | data. | To form | a   | unified | representation |     | of the | three |
| --- | --- | --- | --- | --- | --- | ------ | ----- | ------- | --- | ------- | -------------- | --- | ------ | ----- |
modalitieswithdifferentformatsandnatures,DiagFusioncom-
|     |     |     |     |     | bines | lightweight |                | preprocessing |           | and          | representation |            | learning,  |        |
| --- | --- | --- | --- | --- | ----- | ----------- | -------------- | ------------- | --------- | ------------ | -------------- | ---------- | ---------- | ------ |
|     |     |     |     |     | which | maps        | data           | from          | different | modalities   |                | into the   | same       | vec-   |
|     |     |     |     |     | tor   | space.      | Since          | the labeled   |           | failures     | are usually    |            | inadequate | to     |
|     |     |     |     |     | train | the         | representation |               | model     | effectively, |                | we propose |            | a data |
augmentationmechanism,whichhelpsDiagFusiontolearnthe
correlationbetweenthethreemodalitiesandfailureseffectively.
|     |     |     |     |     | To  | further | enhance | the | accuracy | of  | our diagnosis, |     | DiagFusion |     |
| --- | --- | --- | --- | --- | --- | ------- | ------- | --- | -------- | --- | -------------- | --- | ---------- | --- |
useshistoricalfailurepatternstotrainaGraphNeuralNetwork
|     |     |     |     |     | (GNN),      |     | capturing | both  | spatial | features   |     | and possible |         | failure |
| --- | --- | --- | --- | --- | ----------- | --- | --------- | ----- | ------- | ---------- | --- | ------------ | ------- | ------- |
|     |     |     |     |     | propagation |     | paths,    | which | allows  | DiagFusion |     | to           | conduct | root    |
causeinstancelocalizationandfailuretypedetermination.
Fig.1. Multimodaldataofamicroservicesystem.S1–S7aredifferentmi-
Ourcontributionsaresummarizedasfollows:
| croservices. |     |     |     |     |     | (cid:2) |         |             |           |              |          |            |            |     |
| ------------ | --- | --- | --- | --- | --- | ------- | ------- | ----------- | --------- | ------------ | -------- | ---------- | ---------- | --- |
|              |     |     |     |     |     | We      | propose | DiagFusion, |           | a multimodal |          | data-based |            | ap- |
|              |     |     |     |     |     | proach  | for     | failure     | diagnosis |              | (Section | IV).       | DiagFusion |     |
|              |     |     |     |     |     | builds  | a       | dependency  | graph     | from         | trace    | and        | deployment |     |
containsfailurescausedbyvariousreasons:highmemoryusage, data to capture possible failure propagation paths. Then
incorrectdeallocation,codebug,misconfiguration,networkin- it applies a GNN to achieve a two-fold failure diagnosis,
terruption,etc.Weexaminehundredsofserviceinstancefailures i.e.,rootcauseinstancelocalizationandfailuretypedeter-
and conclude that combining traces, logs, and metrics (mul- mination.Tothebestofourknowledge,weareamongthe
timodal) is crucial for accurate diagnosis. For example, the firsttolearnaunifiedrepresentationofthethreemodalities
forthefailurediagnosisofmicroservicesystems(i.e.,trace,
| microservice | shown in | Fig. 1 | is experiencing | a failure | due to |     |     |     |     |     |     |     |     |     |
| ------------ | -------- | ------ | --------------- | --------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
missingfiles.Itgeneratederrormessagesinlogsandasignificant log,andmetric).
(cid:2)
increase in status code 500 in related traces. Additionally, one We leverage data augmentation to improve the quality of
of its metrics, network out bytes, dropped dramatically during the learned representation, which allows DiagFusion to
thisfailure. workwithlimitedlabeledfailuresandimbalancedfailure
| Theseobservationshighlighttheimportanceofincorporating |     |     |     |     |     | types. |     |     |     |     |     |     |     |     |
| ------------------------------------------------------ | --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
(cid:2)
multimodal data for robust failure diagnosis. However, com- We conduct extensive experiments on two datasets, one
biningmultimodaldatafordiagnosingfailuresinmicroservice from an open-source platform and another from a real-
systemsfacestwomajorchallenges: worldmicroservicesystem(SectionV).Theresultsshow
1) Representationofmultimodaldata:Theformatsofmet- that when DiagFusion is trained on 160 and 80 cases, it
rics,logs,andtracesaresignificantlydifferentfromeach achieves Avg@5 of 0.75 and 0.76 on the two datasets,
other. Service instance metrics are often in the form of respectively,improvingtheaccuracyofrootcauseinstance
timeseries(thebottomofFig.1),whilelogsareusually localization by 20.9% to 368%. Moreover, DiagFusion
semi-structured text (the middle of Fig. 1) and traces achievesF1-scoreof0.84and0.80,improvingtheaccuracy
oftentaketheformoftreestructureswithspansasnodes offailuretypedeterminationby11.0%to169%.
(the top of Fig. 1). It is challenging to find a unified OurimplementationofDiagFusionispubliclyavailable.1
representationofallthismultimodaldatathatfullyutilizes The rest of the paper is organized as follows: Section II
complementaryinformationfromeachdatatype. introduces the necessary background. Section III presents the
2) Imbalancedfailuretypes:Faulttolerancemechanismsin resultsofanempiricalstudyoffailuresinmicroservicesystems.
microservicesystemsoftenresultinahighratioofnormal SectionIVdescribestheoverviewanddetailedimplementation
data to failure-related data. Some types of failures are of DiagFusion in failure diagnosis. In Section V, we evaluate
much rarer than others, leading to an imbalance in the the performance and time efficiency of DiagFusion using two
ratioofdifferenttypesoffailures(TableI).
| To tackle | the above challenges, |     | we present | DiagFusion, | an  |     |     |     |     |     |     |     |     |     |
| --------- | --------------------- | --- | ---------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
automatedfailurediagnosisapproachthatintegratestrace,log, 1https://anonymous.4open.science/r/DiagFusion-378D
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on November 13,2025 at 00:49:52 UTC from IEEE Xplore.  Restrictions apply.

ZHANGetal.:ROBUSTFAILUREDIAGNOSISOFMICROSERVICESYSTEMTHROUGHMULTIMODALDATA 3853
datasets. Section VI discusses the technical rationale, robust- Inadditiontotrace,log,andmetric,deploymentdataisalso
ness, and threats to validity. Section VII presents the related importanttofailurediagnosis.Amicroservicesystemcomprises
workinfailurediagnosis.SectionVIIIconcludesthepaper. manyhardwareandsoftwareassetsthatformcomplicatedinter-
relationships. Operators must carefully record these relation-
II. BACKGROUND ships(a.k.a.deploymentdata)tokeephighmaintainabilityofthe
system.Leveragingdeploymentdataenablestheunderstanding
A. MicroserviceSystemsandMultimodalData
offailurepropagationpathsandcharacteristics.
Microservicesystemsallowdeveloperstoindependentlyde-
velopanddeployfunctionalsoftwareunits(microservice).For B. Preliminaries
example,whenausertriestobuyanitemonanonlineshopping
Representation Learning: Representation learning has been
website,theuserwillexperienceitemsearching,itemdisplay-
widely used in natural language processing tasks, usually in
ing, order generation, payment, etc. Each of these functions
theformofwordembedding.Populartechniquesofrepresenta-
is served by a specific microservice. A failure at a specific
tion learning include static representation like word2vec [34],
service instance can propagate to other service instances in
GloVe [35], fastText [36], and dynamic representation like
many ways, bringing cascading failures. However, diagnosing
ELMo [37], BERT [38], GPT [39]. With the similarities be-
onlinefailuresinmicroservicesystemsisdifficultduetothese
tween logs and natural languages, representation learning can
systems’highlycomplexorchestrationanddynamicinteraction.
be applied to extract log features [40]. We employ fastText
Toaccuratelyfindthecauseofafailure,operatorsmustcarefully
to learn a unified representation of events from multimodal
monitorthesystemandrecordtraces,logs,andmetrics.These
data. Compared to word2vec and GloVe, fastText can utilize
threemodalitiesofmonitoringdatastandasthethreepillarsof
more information [36]. We employ fastText to learn a unified
the observability of microservice systems. The collection and
representationofthemultimodaldata.
storage of instances’ monitoring data are not in the scope of
Inessence,fastTextisaneuralnetworkmodelthatprocesses
thispaper.Thethreemodalities:trace,log,andmetric,andtheir
words as input and takes the output from the hidden layer (a
rolesinfailurediagnosisaredescribedbelow.
vector of real numbers) as its representation. It can be trained
Trace: Traces record the execution paths of users’ requests.
inbothsupervisedandunsupervisedmodes,butthesupervised
Fig. 1 shows an example of trace at the top. Google formally
mode generally yields more accurate results due to its incor-
proposedtheconceptoftracesatDapper[15],inwhichitdefined
porationoflabelinformation.Inthesupervisedtrainingmode,
the whole lifecycle of a request as a trace and the invocation
the neural network is optimized by predicting the class of the
andansweringofacomponentasaspan.Byexaminingtraces,
document.Oncethetrainingiscompleted,fastTextcanbeused
operators may identify microservices that have possibly gone
toprovidevectorizedrepresentations(i.e.,embeddings)forany
wrong [4], [6], [16], [17], [18], [19], [20], [21]. Traces can be
giveninput.
viewedastrees,withmicroservicesasnodesandinvocationsas
Graph Neural Network: GNN can effectively model data
edges.Eachsubtreecorrespondstoaspan.Typically,tracescarry
fromnon-euclideanspace,therebybeingpopularamongfields
information about invocations, e.g., start time, caller, callee,
withgraphstructures,e.g.,socialnetworks,biology,andrecom-
responsetime,andstatuscode.
mendationsystems.PopularGNNarchitectureincludesGraph
Log:Logsrecordcomprehensiveeventsofaserviceinstance.
Convolution Network (GCN) [41], GraphSAGE [42], Graph
Some examples of logs are shown in the middle of Fig. 1.
AttentionNetwork(GAT)[43],etc.GNNsapplygraphconvolu-
Logsaregeneratedbydevelopersusingcommandslikeprintf,
tions,allowingnodestoutilizetheirinformationandlearnfrom
logging.debug, logging.error. They provide an internal picture
their neighbors through message passing. There are numerous
ofaserviceinstance.Byexamininglogs,operatorsmaydiscover
componentsinmicroservicesystemsthatinterconnectwitheach
theactualcauseofwhyaninstanceperformsnotwell.Typically,
other. Thus graph structure is suitable to model microservice
logsconsistofthreefields:timestamp,verbositylevel,andraw
systems,andweemployGNNtolearnthepropagationpatterns
message[22].Fourcommonlyusedverbositylevels,i.e.,INFO,
ofhistoricalfailurecases.
WARN, DEBUG, and ERROR, indicate the severity of a log
message.Therawmessageofalogconveysdetailedinformation
C. ProblemStatement
abouttheevent.Toutilizelogsmoreeffectively,researchershave
proposedvariousparsingtechniquestoextracttemplatesandpa- When a failure occurs, operators need to localize the root
rameters,e.g.,FT-Tree[23],Drain[22],POP[24],MoLFI[25], causeinstanceanddeterminewhathashappenedtoittoachieve
Spell[26],andLogram[27]. timelyfailuremitigation.Forlarge-scalemicroservicesystems,
Metric: Various system-level metrics (e.g., CPU utilization, thefirsttaskisarankingproblem:toranktherootcauseinstance
memory utilization) and user-perceived metrics (e.g., average higherthanotherinstances.Weusethetermrootcauseinstance
responsetime)areconfiguredformonitoringsysteminstances. localization to name this task (Task #1). The second task is a
Eachmetriciscollectedatapredefinedinterval,formingatime classification problem: to classify the failure into a predefined
series, as shown at the bottom of Fig. 1. These metrics track setoffailuretypes.Weusethetermfailuretypedetermination
various aspects of performance issues. By examining metrics, tonamethistask(Task#2).
operatorscandeterminewhichphysicalresourceisanomalous After each failure, operators will carefully conduct a post-
oristhebottleneck[28],[29],[30],[31],[32],[33]. failure analysis: labeling its root cause instance and its failure
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on November 13,2025 at 00:49:52 UTC from IEEE Xplore. Restrictions apply.

3854 IEEETRANSACTIONSONSERVICESCOMPUTING,VOL.16,NO.6,NOVEMBER/DECEMBER2023
type.Additionally,chaosengineeringcangeneratealargenum-
beroffailurecases[44].Itcanenlargethenumberoffailurecases
andenrichthetypesoffailures.WetrainDiagFusionbasedon
thesefailurecases.
|     |     | III. | EMPIRICALSTUDY |     |     |     |     |     |     |     |     |     |
| --- | --- | ---- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Mostexistingfailurediagnosismethodsarebasedonsingle-
| modal data.                                                  | However, |     | these methods |     | cannot | fully | capture | the                                                                      |     |     |     |     |
| ------------------------------------------------------------ | -------- | --- | ------------- | --- | ------ | ----- | ------- | ------------------------------------------------------------------------ | --- | --- | --- | --- |
|                                                              |          |     |               |     |        |       |         | Fig.2. Thedistributionoffailuretypesatalarge-scalereal-worldmicroservice |     |     |     |     |
| patternsoffailedinstances,leadingtoineffectivefailurediagno- |          |     |               |     |        |       |         | system.                                                                  |     |     |     |     |
sis.WeconductanempiricalstudyconductedonGenericAIOps
| Atlas (GAIA)2 |     | dataset | to show | the | ineffectiveness |     | of  | these |     |     |     |     |
| ------------- | --- | ------- | ------- | --- | --------------- | --- | --- | ----- | --- | --- | --- | --- |
methods.Thedatasetiscollectedfromasimulationenvironment
consistingof10microservices,twodatabaseservices(MySQL
andRedis),andfivehostmachines.Thesystemservesmobile
| users and | PC users. | Operators |     | injected | five | types | of failures, |     |     |     |     |     |
| --------- | --------- | --------- | --- | -------- | ---- | ----- | ------------ | --- | --- | --- | --- | --- |
includingsystemfailures(SystemstuckandProcesscrash)and
servicefailures(Loginfailure,Filemissing,andAccessdenied).
| The failure | injection  | record  |          | is provided | along        | with | the    | data. |     |     |     |     |
| ----------- | ---------- | ------- | -------- | ----------- | ------------ | ---- | ------ | ----- | --- | --- | --- | --- |
| Table I     | lists some | typical | symptoms |             | of failures. |      | We can | see   |     |     |     |     |
thatnomodalityalonecandistinguishthepatternsofthesefive
| types of | failures. | It also | shows | that | traces, | logs, | and metrics |     |     |     |     |     |
| -------- | --------- | ------- | ----- | ---- | ------- | ----- | ----------- | --- | --- | --- | --- | --- |
maydisplaydifferentanomalouspatternswhenafailureoccurs.
| Mining | the correlation |     | between | multimodal |     | data | can provide |     |     |     |     |     |
| ------ | --------------- | --- | ------- | ---------- | --- | ---- | ----------- | --- | --- | --- | --- | --- |
operatorswithamorecomprehensiveunderstandingoffailures.
| Besides,   | Table | I shows | that         | some | failures  | occur       | much | more |     |     |     |     |
| ---------- | ----- | ------- | ------------ | ---- | --------- | ----------- | ---- | ---- | --- | --- | --- | --- |
| frequently | than  | others. | For example, |      | the total | occurrences |      | of   |     |     |     |     |
Processcrash,Filemissing,andAccessdenied(67)equalsonly
12%oftheoccurrencesofLoginfailure(527).
| To further     | understand   |     | the | distribution    | of  | failure | types    | in                                       |     |     |     |     |
| -------------- | ------------ | --- | --- | --------------- | --- | ------- | -------- | ---------------------------------------- | --- | --- | --- | --- |
|                |              |     |     |                 |     |         |          | Fig.3. ThetrainingframeworkofDiagFusion. |     |     |     |     |
| the production | environment, |     |     | we investigated |     | N       | failures | in a                                     |     |     |     |     |
microservicesystemofMicrosoft.Duetothecompanypolicy,
wehavetohidesomedetailsofthesefailures.Thefailuresofthe
studiedsystemarerecordedintheIncidentManagementSystem andmetricsdataandserializesthembytheirtimestamps.Then,
wetrainaneuralnetworktolearnthedistributedrepresentation
| (IcM) of | Microsoft, | where |     | a failure | is centralized |     | handled, |     |     |     |     |     |
| -------- | ---------- | ----- | --- | --------- | -------------- | --- | -------- | --- | --- | --- | --- | --- |
includingthedetection,discussion,mitigation,andpost-failure of events by encoding events into vectors. The challenge of
dataimbalanceisovercomethroughdataaugmentationduring
| analysis | of failures. | The | IcM | data of | failures | are | persistently |     |     |     |     |     |
| -------- | ------------ | --- | --- | ------- | -------- | --- | ------------ | --- | --- | --- | --- | --- |
stored in a database. We query the failure records from the modeltraining.Weunifythreemodalitieswithdifferentnatures
database within the time range from 2021 August to 2022 by turning unstructured raw data into structured events and
vectors.Thenwecombinetraceswithdeploymentdatatobuild
August.Weonlykeepthefailureswiththestatusof“completed”,
for their post-failure analyses have been reviewed. In the root a dependency graph (DG) of the microservice system. After
|             |                 |     |           |     |           |            |     | that, the representations |     | of events | and DG are | glued together |
| ----------- | --------------- | --- | --------- | --- | --------- | ---------- | --- | ------------------------- | --- | --------- | ---------- | -------------- |
| cause field | of post-failure |     | analysis, |     | operators | categorize |     | the                       |     |           |            |                |
byaGNN.WetrainGNNusinghistoricalfailurestolearnthe
failuresintothefollowingtypes:code,data,network,hardware,
and external. We can see from Fig. 2 that different failure propagationpatternofsystemfailures.
Afterthetrainingstage,wesavetheeventembeddingmodel
| types are | imbalanced |     | regarding | the | number | of failure |     | cases. |     |     |     |     |
| --------- | ---------- | --- | --------- | --- | ------ | ---------- | --- | ------ | --- | --- | --- | --- |
Theimbalanceddataposesasignificantchallengebecausemost and the GNN. Fig. 5 depicts the real-time failure diagnosis
|     |     |     |     |     |     |     |     | framework | of DiagFusion. | The trigger | of DiagFusion | can be |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | -------------- | ----------- | ------------- | ------ |
machinelearningmethodsperformpoorlyonfailuretypeswith
alertsgeneratedthroughpredefinedrules.Whenanewfailureis
feweroccurrences.
alerted,DiagFusionwillperformareal-timediagnosisandgive
theresultsbacktooperators.
IV. APPROACH
A. DesignOverview
B. UnifiedEventRepresentation
Inthisarticle,weproposeDiagFusion,whichcombinesthe
DiagFusionunifiesthethreemodalitiesbyextractingevents
| modality | of trace, | log, | and metric | for | accurate | failure | diagno- |     |     |     |     |     |
| -------- | --------- | ---- | ---------- | --- | -------- | ------- | ------- | --- | --- | --- | --- | --- |
sis. The training framework of DiagFusion is summarized in fromtherawdataandencodingthemintovectors.Specifically,
|     |     |     |     |     |     |     |     | it collects | failure-indicative | events | by leveraging | effective and |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ------------------ | ------ | ------------- | ------------- |
Fig.3.First,DiagFusionextractseventsfromrawtraces,logs,
|     |     |     |     |     |     |     |     | lightweight | methods, | including anomaly | detection | techniques |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | -------- | ----------------- | --------- | ---------- |
2https://github.com/CloudWise-OpenSource/GAIA-DataSet formetricsandtracesandtemplateparsingtechniquesforlogs.
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on November 13,2025 at 00:49:52 UTC from IEEE Xplore.  Restrictions apply.

ZHANGetal.:ROBUSTFAILUREDIAGNOSISOFMICROSERVICESYSTEMTHROUGHMULTIMODALDATA 3855
| Then, it | trains a | fastText | [36] | model | on event | sequences |     | to  |     |     |     |     |     |     |
| -------- | -------- | -------- | ---- | ----- | -------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
generateembeddingvectorsofevents.
| First,       | we introduce | the         | instances | in          | a microservice |           | system.   |     |     |     |     |     |     |     |
| ------------ | ------------ | ----------- | --------- | ----------- | -------------- | --------- | --------- | --- | --- | --- | --- | --- | --- | --- |
| Microservice | systems      | have        | the       | advantage   | of             | dynamic   | deploy-   |     |     |     |     |     |     |     |
| ment by      | utilizing    | the         | container | technique.  |                | In this   | paper, we |     |     |     |     |     |     |     |
| use the term | instance     | to          | describe  | a running   |                | container | and the   |     |     |     |     |     |     |     |
| term service | group        | to describe |           | the logical | component      |           | that an   |     |     |     |     |     |     |     |
| instance     | belongs      | to.For      | example,  | Billingis   |                | aservice  | group     | in  |     |     |     |     |     |     |
amicroservicesystem,andBilling_cff19bdenotesaninstance,
| where cff19b | is  | the container |     | id. Below | we  | will | describe the |     |     |     |     |     |     |     |
| ------------ | --- | ------------- | --- | --------- | --- | ---- | ------------ | --- | --- | --- | --- | --- | --- | --- |
eventextractionfromdifferentmodalities.
| Trace   | Event Extraction: |          | Traces | record | calling | relationships |            |     |     |     |     |     |     |     |
| ------- | ----------------- | -------- | ------ | ------ | ------- | ------------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
| between | services.         | We group | trace  | data   | by its  | caller        | and callee |     |     |     |     |     |     |     |
services.DiagFusionwillexaminemultiplefieldsinsideatrace
group.Underdifferentimplementationsoftracerecording,trace
| data can    | carry different |           | fields, | e.g., response |               | time | and status |     |     |     |     |     |     |     |
| ----------- | --------------- | --------- | ------- | -------------- | ------------- | ---- | ---------- | --- | --- | --- | --- | --- | --- | --- |
| code, which | reflect         | different |         | aspects        | of operators’ |      | interests. |     |     |     |     |     |     |     |
Fig.4. Theeventextractionandserializationprocessusingtraces,logs,and
| We apply | an anomaly |     | detection | algorithm |     | (i.e., 3-sigma) | for |     |     |     |     |     |     |     |
| -------- | ---------- | --- | --------- | --------- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- |
metrics.
| numerical | fields          | like response |        | time        | to detect | anomalous | be-       |     |     |     |     |     |     |     |
| --------- | --------------- | ------------- | ------ | ----------- | --------- | --------- | --------- | --- | --- | --- | --- | --- | --- | --- |
| haviors.  | For categorical |               | fields | like status | code,     | we        | count the |     |     |     |     |     |     |     |
numberofoccurrencesofeachvalue.Ifthecountofsomevalue
increasesdramatically,wedeterminethatthisfieldisanomalous. utilize the label information, we relabel event sequences in an
|              |      |         |     |        |            |     |           | instance-wise | manner. | Specifically, | the | root cause | instance’s |     |
| ------------ | ---- | ------- | --- | ------ | ---------- | --- | --------- | ------------- | ------- | ------------- | --- | ---------- | ---------- | --- |
| We determine | that | a group | of  | caller | and callee | is  | anomalous |               |         |               |     |            |            |     |
eventsequenceislabeledbytheactualfailuretype,whileother
| if one of | its fields | becomes |     | anomalous. | The | extracted | trace |     |     |     |     |     |     |     |
| --------- | ---------- | ------- | --- | ---------- | --- | --------- | ----- | --- | --- | --- | --- | --- | --- | --- |
eventsareintheformoftuple<timestamp,caller-instance-id, instances’ event sequences are labeled as “non-root-cause”. A
|     |     |     |     |     |     |     |     | microservice | system | with p historical | failures | and | q instances |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ------ | ----------------- | -------- | --- | ----------- | --- |
callee-instance-id>.
=p×q
Log Event Extraction: Logs record detailed activities of an results in N event sequences after relabeling. Then,
welearnunifiedrepresentationsfromtheserelabeledhistorical
| instance | (service | or machine). |     | We perform | log | parsing | for log |     |     |     |     |     |     |     |
| -------- | -------- | ------------ | --- | ---------- | --- | ------- | ------- | --- | --- | --- | --- | --- | --- | --- |
eventsequencesusingtheeventembeddingmodel.
| event extraction |     | using | Drain | [22], which | has | been | proven | to  |     |     |     |     |     |     |
| ---------------- | --- | ----- | ----- | ----------- | --- | ---- | ------ | --- | --- | --- | --- | --- | --- | --- |
be effective in practice. Drain uses a fixed depth parse tree Witheventsequenceandinstancelabeling,wecantransform
eventsintovectors.Weusethetermeventembeddingtodescribe
| to distinguish | the | template | part | and | the variable |     | part of log |     |     |     |     |     |     |     |
| -------------- | --- | -------- | ---- | --- | ------------ | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
messages. For example, in the log message “uuid: 8fef9f0 in- themappingofeventstorealnumbervectors.Specifically,we
|           |              |     |        |       |       |              |        | train a fastText | model          | on the event | sequences |           | to obtain   | the |
| --------- | ------------ | --- | ------ | ----- | ----- | ------------ | ------ | ---------------- | -------------- | ------------ | --------- | --------- | ----------- | --- |
| formation | has expired, |     | mobile | phone | login | is invalid”, | “uuid: |                  |                |              |           |           |             |     |
|           |              |     |        |       |       |              |        | vectorized       | representation | for events   | from      | all three | modalities. |     |
******informationhasexpired,mobilephoneloginisinvalid”
isthetemplatepart,and“8fef9f0”isthevariablepart.Afterwe FastTextisaneuralnetworkoriginallyproposedfortextclassi-
fication.Foradocumentwithwordsequences,fastTextextracts
| get the template |     | part of | a log | message, | we  | hash the | string of |     |     |     |     |     |     |     |
| ---------------- | --- | ------- | ----- | -------- | --- | -------- | --------- | --- | --- | --- | --- | --- | --- | --- |
n-gramsfromitandpredictsitslabel.Inourscenario,wereplace
thetemplateparttoobtainaneventtemplateid.Theextracted
log events are in the form of tuple <timestamp, instance-id, word sequences with event sequences and replace document
labelswithfailuretypes.ThetrainingoffastTextminimizesthe
event-template-id>.
Metric Event Extraction: Metrics are also recorded at the negativelog-likelihoodoverclasses:
instancelevel.Weperform3-sigmatodetectanomalousmetrics.
(cid:2)N
| Whenthevalueofametricexceedstheupperboundof3-sigma, |           |     |        |            |     |         |           |     |      | 1            |     |     |     |     |
| --------------------------------------------------- | --------- | --- | ------ | ---------- | --- | ------- | --------- | --- | ---- | ------------ | --- | --- | --- | --- |
|                                                     |           |     |        |            |     |         |           |     | min− | ynlog(f(xn)) |     |     |     | (1) |
| the anomaly                                         | direction |     | is up. | Similarly, | the | anomaly | direction |     |      |              |     |     |     |     |
|                                                     |           |     |        |            |     |         |           |     | f    | N            |     |     |     |     |
n=1
| is down | if the value | is  | below | the lower | bound. | The | extracted |     |     |     |     |     |     |     |
| ------- | ------------ | --- | ----- | --------- | ------ | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
metriceventsareintheformoftuple<timestamp,instance-id,
|     |     |     |     |     |     |     |     | where xn | is the normalized | bag | of features | of  | the n-th | event |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ----------------- | --- | ----------- | --- | -------- | ----- |
metric-name,anomaly-direction>. sequence, yn denotes the relabeled information, and f is the
The above extraction provides events from different modal- neuralnetwork.WetreatfastText’soutputasthevectorizedrep-
| ities. Despite | the | differences |     | in raw | data, all | extracted | events |     |     |     |     |     |     |     |
| -------------- | --- | ----------- | --- | ------ | --------- | --------- | ------ | --- | --- | --- | --- | --- | --- | --- |
resentationofevents.Thetrainingdetailoftheeventembedding
sharetwofields,namelytimestampandinstance-id.Theseare modelisdescribedinSectionIV-D.
| the keys | to unifying | different |     | modalities. | We  | group | events by |     |     |     |     |     |     |     |
| -------- | ----------- | --------- | --- | ----------- | --- | ----- | --------- | --- | --- | --- | --- | --- | --- | --- |
instance-idandserializeeventsinthesamegroupbytimestamp.
C. GraphNeuralNetwork
| Fig. 4 shows | the | event | extraction | and | serialization |     | process for |     |     |     |     |     |     |     |
| ------------ | --- | ----- | ---------- | --- | ------------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
oneinstance.TheeventsequenceofinstanceiisdenotedbyEi. Intheeventrepresentationprocess,DiagFusioncapturesthe
Aftergettingtheeventsequenceofeveryinstance,wefurther local features of instances. However, failures can propagate
assign labels to every event sequence according to operators’ between instances, so we need to have a global picture of the
post-failure analysis. Original failure labels are often in the system, i.e., how a failure will affect the system. To this end,
form of tuple <root cause instance-id, failure type>. To fully we employ a GNN to learn the failure propagation between
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on November 13,2025 at 00:49:52 UTC from IEEE Xplore.  Restrictions apply.

3856 IEEETRANSACTIONSONSERVICESCOMPUTING,VOL.16,NO.6,NOVEMBER/DECEMBER2023
serviceinstancesandintegratealltheinformationofthewhole (determinedbyeuclideandistance)inV 0.Afterallfailuretypes
system. areexpandedtoarelativelylargesize,e.g.,1000,wecanobtain
ToleverageaGNN,itisessentialtoconsiderbothnodesand a more balanced training set. Further details on the choice of
edgeswithinagraph.ThenodesinaGNNcorresponds tothe theexpandingsizecanbefoundatSectionV-E.Thenwetrain
instancesinamicroservicesystem.Aninstanceischaracterized theeventembeddingmodelagain(f1)ontheexpandeddataand
byitsanomalouseventsinDiagFusion.Werepresentaninstance regard the representations generated in this round (V 1) as the
ibyaveragingallofitsevents: finalunifiedeventrepresentations.
|     |     |      |     | (cid:2) |     |     |     | 2) TrainingofGraphNeuralNetwork: |     |     |     |     | WetraintheGNNin |     |
| --- | --- | ---- | --- | ------- | --- | --- | --- | -------------------------------- | --- | --- | --- | --- | --------------- | --- |
|     |     | ( 0) |     | 1       |     |     |     |                                  |     |     |     |     |                 |     |
h = V 1(e) (2) a j o in t lea r n in g fas h i on to fu l l y ut ili z e th e s h a r ed i n fo r m at io n
|     |     | i   | |E  | |   |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
i
∀e∈E i be t w e en ta s k s #1 a n d #2 . T h e n w e c o m b in e t h e tr a in e d G N N
|                                          |     |     |     |     |     |               |     | with a ranking | strategy |     | to better | fit the | nature | of microservice |
| ---------------------------------------- | --- | --- | --- | --- | --- | ------------- | --- | -------------- | -------- | --- | --------- | ------- | ------ | --------------- |
| whereEiistheextractedeventsequences,andV |     |     |     |     |     | 1(e)isthevec- |     |                |          |     |           |         |        |                 |
systems.
torizedrepresentationofeventelearnedbytheeventembedding
|     |     |     |     |     |     |     |     | Ranking | Strategy: | One | of  | the advantages |     | of microservice |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | --------- | --- | --- | -------------- | --- | --------------- |
model.
systemsisthatthearchitectureallowsdynamicdeploymentof
TheedgesinaGNNcorrespondtothedependencygraphin
|                                         |     |     |     |     |     |      |         | service instances. |     | Thus, | service | instances | are | constantly being |
| --------------------------------------- | --- | --- | --- | --- | --- | ---- | ------- | ------------------ | --- | ----- | ------- | --------- | --- | ---------------- |
| amicroservicesystem.Therearetwodominant |     |     |     |     |     | ways | ofprop- |                    |     |       |         |           |     |                  |
createdanddestroyed.However,whenitcomestofailurediag-
| agation failure |     | between | services: | function | calling | or  | resource |     |     |     |     |     |     |     |
| --------------- | --- | ------- | --------- | -------- | ------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
nosis,thiskindofflexibilityraisesachallengeforlearning-based
| contention | [45]. | So we | combine | traces | and | deployment | data |     |     |     |     |     |     |     |
| ---------- | ----- | ----- | ------- | ------ | --- | ---------- | ---- | --- | --- | --- | --- | --- | --- | --- |
methods.Thefailurediagnosismodelwillhavetoberetrained
| to capture | probable | failure | propagation |     | paths. | Specifically, | we  |            |        |        |       |          |         |                 |
| ---------- | -------- | ------- | ----------- | --- | ------ | ------------- | --- | ---------- | ------ | ------ | ----- | -------- | ------- | --------------- |
|            |          |         |             |     |        |               |     | frequently | if the | output | layer | directly | outputs | the probability |
aggregatetracestogetacallgraph.Thenweaddtwodirected
|     |     |     |     |     |     |     |     | of being | the root | cause | instance | for each | instance | since many |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | -------- | ----- | -------- | -------- | -------- | ---------- |
edgesforeachpairofcallerandcallee,withonepointingfrom
|            |        |        |     |           |                |            |     | instances | can be | created | or destroyed |     | after | the model training |
| ---------- | ------ | ------ | --- | --------- | -------------- | ---------- | --- | --------- | ------ | ------- | ------------ | --- | ----- | ------------------ |
| the caller | to the | callee | and | the other | in the reverse | direction. |     |           |        |         |              |     |       |                    |
isfinished.WeaddanextractstepinDiagFusiontoovercome
Fromdeploymentdata,weaddedgesbetweentwoinstancesif
|     |     |     |     |     |     |     |     | this challenge. | Instead |     | of directly | determining |     | the root cause |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | ------- | --- | ----------- | ----------- | --- | -------------- |
theyareco-deployed,i.e.,sharingresources.
|     |     |     |     |     |     |     |     | instance, | DiagFusion | is  | trained | on service | groups, | the logical |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ---------- | --- | ------- | ---------- | ------- | ----------- |
Afterobtainingthedependencygraphandinstancerepresen-
aggregationofserviceinstances,fortask#1.ThenDiagFusion
tations,weemployGNNtolearnthefailurepropagationpattern
rankstheinstancesinsideacandidateservicegroupbythelength
byitsmessage-passingmechanism.AttheK-thlayerofGNN,
oftheireventsequences.Theinstancewithmoreanomalyevents
weapplytopologyadaptivegraphconvolution[46]andupdate
willberankedhigherandlikelybetherootcauseinstance.
theinternaldataofinstancesaccordingto:
JointLearning:Intuitively,thetwotasksoffailurediagnosis,
(cid:2)K (cid:3) (cid:4) i.e.,rootcauseinstancelocalizationandfailuretypedetermina-
k
|     |     | K   |     | −1/2 | −1/2 |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | ---- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
H = D AD XΘk (3) tion,sharesomeknowledgeincommon.Foragivenfailure,the
|     |     | k=0 |     |     |     |     |     | onlydifferencebetweentask#1andtask#2liesintheirlabels.So |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
(cid:5)
DiagFusionintegratesajointlearningmechanismtoutilizethe
| where A  | denotes | the     | adjacency | matrix, | Dii =      | j=0     | Aij is | a                 |     |          |        |              |                  |               |
| -------- | ------- | ------- | --------- | ------- | ---------- | ------- | ------ | ----------------- | --- | -------- | ------ | ------------ | ---------------- | ------------- |
|          |         |         |           |         |            |         |        | shared knowledge  |     | and      | reduce | the training | time.            | (Training two |
| diagonal | degree  | matrix, | Θk        | denotes | the linear | weights | to sum |                   |     |          |        |              |                  |               |
|          |         |         |           |         |            |         |        | models separately |     | requires | twice  | the          | time otherwise.) | Specifi-      |
theresultsofdifferenthopstogether.
cally,thejointlossfunctionis:
Finally, we add a MaxPooling layer as the readout layer to ⎛ ⎞
| integrate | the information |     | of  | the whole | microservice |     | system. |            |          |     |     |     |          |     |
| --------- | --------------- | --- | --- | --------- | ------------ | --- | ------- | ---------- | -------- | --- | --- | --- | -------- | --- |
|           |                 |     |     |           |              |     |         | 1 (cid:2)F | (cid:2)S |     |     |     | (cid:2)T |     |
|           |                 |     |     |           |              |     |         | −          | ⎝        |     |     |     |          | ⎠   |
FollowingtheMaxPoolinglayer,thereisafullyconnectedlayer y(s)i,jlogp(s)i,j + y(t)i,klogp(t)i,k
F
where each neuron corresponds to either a service group with i=1 j=1 k=1
possible root cause instances for task #1 or a failure type for (4)
task#2. where F is the number of historical failures, S is the number
|     |     |     |     |     |     |     |     | ofservicegroups,T |     | isthenumberoffailuretypes,y(s)isthe |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | ----------------------------------- | --- | --- | --- | --- |
D. TrainingofDiagFusion rootcauseservicegrouplabeledbyoperators,y(t)isthefailure
type,p(s)isthepredictedservicegroup,andp(t)isthepredicted
DiagFusionappliesatwo-phasetrainingstrategytolearnthe
failuretype.
failurepatternofamicroservicesystem.First,ittrainedtheevent
| embedding | model | with | data | augmentation. | Then | it trains | the |                              |     |     |     |     |     |     |
| --------- | ----- | ---- | ---- | ------------- | ---- | --------- | --- | ---------------------------- | --- | --- | --- | --- | --- | --- |
|           |       |      |      |               |      |           |     | E. Real-TimeFailureDiagnosis |     |     |     |     |     |     |
GNNwithajointlearningtechnique.
1) Training of Event Embedding Model: DiagFusion em- Afterthetrainingstage,wesavethetrainedeventembedding
ploysadataaugmentationstrategytoenrichthetrainingdataset modelandtheGNN.Whenanewfailureisalerted,DiagFusion
and reduce the model’s bias towards the majority class. First, performsareal-timediagnosisprocessasshowninFig.5.
we train our event embedding model on the original data. 1) RunningExample: Fig.6showshowDiagFusioncanbe
The trained neural network, denoted by f0, maps events to integrated with microservice systems. To better explain how
V
the vector space 0. To increase the number of failure cases, DiagFusiondiagnosesfailure,wedemonstratetheworkflowof
we add new event sequences for each failure type (including DiagFusion using one real-world failure from D1. At 10:46,
“non-root-cause”)byrandomlytakinganeventsequenceofthat service instance B1 encounters a failure of access denied.
type and replacing one of the events with its closest neighbor Fig. 7 shows the original data, event sequence, and the DG.
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on November 13,2025 at 00:49:52 UTC from IEEE Xplore.  Restrictions apply.

ZHANGetal.:ROBUSTFAILUREDIAGNOSISOFMICROSERVICESYSTEMTHROUGHMULTIMODALDATA 3857
TABLEII
DETAILEDINFORMATIONOFDATASETS
andarchitectures,D1andD2.Topreventdataleakage,wesplit
|     |     |     |     |     | the data | of D1 | and D2 | into training | and | testing | sets according |     |
| --- | --- | --- | --- | --- | -------- | ----- | ------ | ------------- | --- | ------- | -------------- | --- |
totheirstarttime,i.e.,weusedatafromtheearliertimeasthe
trainingsetanddatafromthelatertimeasthetestset.Detailed
Fig.5. Real-timefailurediagnosis.
|     |     |     |     |     | information | is  | listed in | Table II. | The systems |     | that produce | D1  |
| --- | --- | --- | --- | --- | ----------- | --- | --------- | --------- | ----------- | --- | ------------ | --- |
andD2areasfollows:
1) D1.ThedetailsofD1areelaboratedinSectionIII.
|     |     |     |     |     | 2) D2. | The    | second | dataset  | is collected | from  | the manage- |         |
| --- | --- | --- | --- | --- | ------ | ------ | ------ | -------- | ------------ | ----- | ----------- | ------- |
|     |     |     |     |     | ment   | system | of a   | top-tier | commercial   | bank. | The         | studied |
systemconsistsof14instances,includingmicroservices,
webservers,applicationservers,databases,anddockers.
|     |     |     |     |     | Due | to the | non-disclosure |     | agreement, |     | we cannot | make |
| --- | --- | --- | --- | --- | --- | ------ | -------------- | --- | ---------- | --- | --------- | ---- |
thisdatasetpubliclyavailable.Twoexperiencedoperators
|     |     |     |     |     | examined |     | the failure | records | from | January | 2021 | to June |
| --- | --- | --- | --- | --- | -------- | --- | ----------- | ------- | ---- | ------- | ---- | ------- |
2021.Theyclassifiedthefailuresintofivetypesoffailures,
i.e.,CPU-relatedfailures,memory-relatedfailures,JVM-
CPU-relatedfailures,JVM-memory-relatedfailures,and
IO-relatedfailures.Theclassificationwasdoneseparately,
andtheycheckedthelabelingwitheachothertoreacha
consensus.
Fig.6. IntegrationofDiagFusionwithamicroservicesystem.
|           |                  |                         |        |      | 2) BaselineMethods: |     |          | Weselectsixadvancedsingle-modal- |                  |      |            |        |
| --------- | ---------------- | ----------------------- | ------ | ---- | ------------------- | --- | -------- | -------------------------------- | ---------------- | ---- | ---------- | ------ |
|           |                  |                         |        |      | based methods       |     | (two for | trace                            | (i.e., MicroHECL |      | [5],       | Micro- |
|           |                  |                         |        |      | Rank [6]),          | two | for log  | (i.e.,                           | Cloud19          | [8], | LogCluster | [7]),  |
| From Fig. | 7(a), we can see | that failure-indicative | events | from |                     |     |          |                                  |                  |      |            |        |
differentmodalitiesaretemporallyintertwined.ThentheGNN and two for metric (i.e., AutoMAP [13], MS-Rank [12])),
predicts service group “B” and failure type “access denied”. and two multimodal-based methods (i.e., PDiagnose [47],
CloudRCA[48])asthebaselinemethods.Moredetailscanbe
Furtherrankingwithintheservicegroup“B”gives“B1”asthe
Top1instance.Theoverallprocesstakeslessthan10seconds. found in Section VII. Among the baseline methods, Cloud19,
|     |     |     |     |     | LogCluster, | and | CloudRCA |     | cannot address |     | Task #1 | (root |
| --- | --- | --- | --- | --- | ----------- | --- | -------- | --- | -------------- | --- | ------- | ----- |
Thus,DiagFusioneffectivelyaddressestasks#1and#2.
|     |     |     |     |     | cause instance |     | localization), | while | MicroHECL, |     | MicroRank, |     |
| --- | --- | --- | --- | --- | -------------- | --- | -------------- | ----- | ---------- | --- | ---------- | --- |
V. EVALUATION AutoMAP, MS-Rank, and PDiagnose cannot address Task #2
(failuretypedetermination).Therefore,wedividethebaseline
| In this section, | we evaluate | the performance | of DiagFusion |     |     |     |     |     |     |     |     |     |
| ---------------- | ----------- | --------------- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
methodsintotwogroupstoevaluatetheperformanceofTask#1
usingtworeal-worlddatasets.Weaimtoanswerthefollowing
andTask#2,respectively:MicroHECL,MicroRank,AutoMAP,
researchquestions(RQs):
MS-Rank,andPDiagnoseforTask#1,Cloud19,LogCluster,and
RQ1: HoweffectiveisDiagFusioninfailurediagnosis?
CloudRCAforTask#2.
RQ2: DoeseachcomponentofDiagFusionhavesignificant
Weconfiguretheparametersofallthesemethodsaccording
contributionstoDiagFusion’sperformance?
totheirpapers.Specifically,weusethesameconfigurationfor
| RQ3: Is | the computational | efficiency | of DiagFusion | suffi- |           |          |            |           |     |        |        |         |
| ------- | ----------------- | ---------- | ------------- | ------ | --------- | -------- | ---------- | --------- | --- | ------ | ------ | ------- |
|         |                   |            |               |        | parameter | settings | explicitly | mentioned |     | in the | papers | and not |
cientforfailurediagnosisintherealworld?
|     |     |     |     |     | limited | to a particular | dataset |     | (e.g., significance |     | level, | feature |
| --- | --- | --- | --- | --- | ------- | --------------- | ------- | --- | ------------------- | --- | ------ | ------- |
RQ4: Whatistheimpactofdifferenthyperparameters?
|     |     |     |     |     | dimension). | For | parameter | settings | that | apply | to a particular |     |
| --- | --- | --- | --- | --- | ----------- | --- | --------- | -------- | ---- | ----- | --------------- | --- |
dataset(e.g.,windowlength,period),weadaptthemaccording
A. ExperimentalSetup
totherangethepapersprovideortoourdata.
1) Dataset: ToevaluatetheperformanceofDiagFusion,we 3) Evaluation Metrics: As stated in Section II-C, DiagFu-
conduct extensive experiments on two datasets collected from sionaimstolocalizetherootcauseinstanceanddeterminethe
twomicroservicesystemsunderdifferentbusinessbackgrounds failuretype.Wecarefullyselectdifferentevaluationmetricsfor
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on November 13,2025 at 00:49:52 UTC from IEEE Xplore.  Restrictions apply.

3858 IEEETRANSACTIONSONSERVICESCOMPUTING,VOL.16,NO.6,NOVEMBER/DECEMBER2023
Fig.7. ArunningexampleofDiagFusion.(a)theserializedmultimodaleventsequenceoftherootcauseinstance(B1);(b)theoriginaldatacorrespondingto
theeventsequence;(c)partofthedependencygraphinthisfailure.
both tasks to better reflect the real-world performance of all TABLEIII
selectedmethods. EFFECTIVENESSOFFAILURETYPEDETERMINATION(TASK#2)
ForTask#1,weuseTop-kaccuracy(A@k)andTop-5average
| accuracy | (Avg@5) as | the evaluation |     | metrics. | A@k | is a well- |     |     |     |     |     |
| -------- | ---------- | -------------- | --- | -------- | --- | ---------- | --- | --- | --- | --- | --- |
adoptedmetricthatquantifiestheprobabilitythattop-kinstances
| output by      | each method | indeed | contain  | the root     | cause | instance |     |     |     |     |     |
| -------------- | ----------- | ------ | -------- | ------------ | ----- | -------- | --- | --- | --- | --- | --- |
| [5]. Formally, | given |A|   | as the | test set | of failures, | RCi   | as the   |     |     |     |     |     |
groundtruthrootcauseinstance,RCs[k]asthetop-krootcause
instancessetgeneratedbyamethod,A@kisdefinedas:
(cid:10)
(cid:2) ∈RCsa[k] The comparison result of Task #1 is shown in Fig. 8. Diag-
|     | 1   | 1,  | ifRCia |     |     |     |     |     |     |     |     |
| --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
| A@k | =   |     |        |     |     | (5) |     |     |     |     |     |
|A| 0, otherwise Fusionachievesthebestperformance.Specifically,theA@1to
a∈A
|     |     |     |     |     |     |     | A@5 of DiagFusion | are almost | the best on | D1 and D2. | More |
| --- | --- | --- | --- | --- | --- | --- | ----------------- | ---------- | ----------- | ---------- | ---- |
Avg@5 is another popular metric that evaluates a method’s specifically,theAvg@5ofDiagFusionexceeds0.75onbothD1
overall capability of localizing the root cause instance[49]. In andD2,respectively.Itisatleast0.13higheronbothdatasets
practice, operators often examine the top 5 results. Avg@5 is thanbaselinesusingsingle-modaldataduetotheadvantageof
calculatedby:
usingmultimodaldata.ComparedwithPDiagnose,whichalso
(cid:2) uses multimodal data, the Avg@5 of DiagFusion is higher by
1
Avg@5= A@k (6) atleast0.18.Thisindicatesthatlearningfromhistoricalfailures
5
1≤k≤5
improvestheaccuracyofdiagnosissignificantly.
ForTask#2,whichisamulti-classclassificationproblem,we The result of Task #2 is shown in Table III. For this task,
usetheweightedaverageprecision,recall,andF1-scoretotest DiagFusion is better than almost all baselines. On D1, the
the performances. These metrics have been selected based on precision, recall, and F1-score of DiagFusion are over 0.80.
OnD2,DiagFusionmanagestomaintainanF1-scoreof0.80,
| a previous | study [50] as | a reliable | way | to assess | the | model’s |     |     |     |     |     |
| ---------- | ------------- | ---------- | --- | --------- | --- | ------- | --- | --- | --- | --- | --- |
effectivenessinthisspecificcontext.WithTruePositives(TP), which is at least 0.195 higher than the baselines. Considering
FalsePositives(FP),andFalseNegatives(FN),thecalculationis both systems and tasks, DiagFusion consistently demonstrates
| F1-score=2× |     | precision×recall |     |     |     |     |     |     |     |     |     |
| ----------- | --- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
given by , where precision= superiorperformance,therebysubstantiatingitseffectiveness.
precision+recall
| TP               | TP    |     |     |     |     |     |     |     |     |     |     |
| ---------------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TP+FP andrecall= | TP+FN | .   |     |     |     |     |     |     |     |     |     |
4) Implementation: We implement DiagFusion and base- C. AblationStudy(RQ2)
| lines with | Python 3.7.13, | PyTorch | 1.10.0, | scikit-learn |     | 1.0.2, |     |     |     |     |     |
| ---------- | -------------- | ------- | ------- | ------------ | --- | ------ | --- | --- | --- | --- | --- |
Toevaluatetheeffectsofthethreekeytechniquecontributions
| fastText 0.9.2, | and DGL | 0.9.0. | We run | the experiments |     | on  | a              |                       |             |            |     |
| --------------- | ------- | ------ | ------ | --------------- | --- | --- | -------------- | --------------------- | ----------- | ---------- | --- |
|                 |         |        |        |                 |     |     | of DiagFusion: | 1) data augmentation; | 2) fastText | embedding; |     |
serverwith12×Intel(R)Xeon(R)CPUE5-2650v4@2.20GHz
|     |     |     |     |     |     |     | 3) DG and | GNN, we create | five variants | of DiagFusion. | C1: |
| --- | --- | --- | --- | --- | --- | --- | --------- | -------------- | ------------- | -------------- | --- |
and128GRAM(withoutGPUs).Werepeateveryexperiment
Removethedataaugmentation.C2:Useword2vecembedding
| five times | and take the | average | result | to reduce | the | effect of |     |     |     |     |     |
| ---------- | ------------ | ------- | ------ | --------- | --- | --------- | --- | --- | --- | --- | --- |
insteadoffastText.C3:UseGloVeembeddinginsteadoffast-
randomness.
|     |     |     |     |     |     |     | Text. C4: Replace | the GNN | output layer with | a decision | tree. |
| --- | --- | --- | --- | --- | --- | --- | ----------------- | ------- | ----------------- | ---------- | ----- |
C5:ReplacetheGNNoutputlayerwithakNNmodel.
B. OverallPerformance(RQ1)
|     |     |     |     |     |     |     | Table IV | lists that DiagFusion | outperforms | all the | variants |
| --- | --- | --- | --- | --- | --- | --- | -------- | --------------------- | ----------- | ------- | -------- |
TodemonstratetheeffectivenessofDiagFusion,wecompare on D1 and D2, demonstrating each component’s significance.
itwiththebaselinemethodsonTask#1andTask#2. When removing the data augmentation (C1), the performance
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on November 13,2025 at 00:49:52 UTC from IEEE Xplore.  Restrictions apply.

ZHANGetal.:ROBUSTFAILUREDIAGNOSISOFMICROSERVICESYSTEMTHROUGHMULTIMODALDATA 3859
Fig.8. Effectivenessofrootcauseinstancelocalization(Task#1).
TABLEIV
CONTRIBUTIONSOFCOMPONENTS
reduces across the board as models trained from imbalanced TABLEV
data are more likely to bias predictions toward classes with
THECOMPARISONOFTRAININGTIME(OFFLINE)ANDDIAGNOSISTIME
(ONLINE)PERCASE(“-”MEANSNONEEDTRAINING)
more samples. Data augmentation can alleviate this problem.
Theperformancebecomes worsewhenreplacingfastTextem-
beddingstrategy(C2&C3).ThereasonisthatfastTextcanlearn
fromoperators’failurelabelingaswellasco-occurrelationships,
while word2vec and GloVe can only learn from the co-occur
relationshipsbetweenevents.ReplacingtheGNNoutputlayer
withclassifierssuchasdecisiontreesandkNN(C4&C5)de-
gradesperformancebecausetheGNNcancapturetheinteraction
patternsandfaultpropagationamonginstancesinmicroservice
systems,buttraditionalclassifierscannotunderstandthegraph
structureinformation.
D. Efficiency(RQ3) E. HyperparameterSensitivity(RQ4)
Werecordtherunningtimeofallmethodsandcomparethem WediscusstheeffectoffourhyperparametersofDiagFusion.
inTableV.TheofflinetrainingtimeofDiagFusionisacceptable, Fig.9showshowAvg@5(Task#1),F1-score(Task#2)change
particularlywhenconsideringitsinfrequentneedforretraining. withdifferenthyperparameters.
It shows that DiagFusion can diagnose one failure within 12 EmbeddingDimension:TheperformanceofDiagFusionre-
seconds on average online, which means it can achieve quasi- acts differently on different datasets in terms of sensitivity to
real-timediagnosisbecausetheintervalofdatacollectioninD1 dimensionality (D1 remains stable while D2 fluctuates more),
and D2 is at least 30 seconds. Although DiagFusion may not and the optimal dimensionality is inconsistent across datasets
possess apparent advantages among the methods in Table V, and tasks. We choose the 100 dimensions in our experiments
DiagFusioncanmeettheneedsofonlinediagnosis. becauseithasthebestoverallperformance.
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on November 13,2025 at 00:49:52 UTC from IEEE Xplore. Restrictions apply.

3860 IEEETRANSACTIONSONSERVICESCOMPUTING,VOL.16,NO.6,NOVEMBER/DECEMBER2023
Fig.9. TheeffectivenessofDiagFusionunderdifferenthyperparameters.
The Number of Augmented Samples: The experiments in relationships, making them well-suited to handle complicated
SectionV-Bshowthatdataaugmentationhassomeimprovement data.
inthemodel’sperformance.However,whenthenumberofsam- Why FastText? FastText was chosen because trace, log, and
plesincreasestoacertainamount,theinformationinthetraining metricdatahaveverydifferentformats.However,theyallshare
sethasalreadybeenfullyutilized.Instead,theperformancemay timestamps,meaningtheycanbesequencedaccordingtotheir
bedegradedduetotheexcessiveintroductionofnoise.Generally temporal order. FastText provides superior performance over
speaking, DiagFusion does not need an excessive number of other static embeddings like word2vec and GloVe, which was
augmentedsamplesaslongasthesamplesarebalanced. demonstratedinSectionV-C.Althoughdeepdynamicembed-
TheNumberofLayersinGNN:AsthelayernumberofGNN dingslikeELMo,BERT,andGPTarepopularinNaturalLan-
variesfrom1to5,theperformanceofDiagFusioninthreetasks guageProcessing,theyarenotsuitableformicroservicesettings
shows a decreasing trend. The model performs best when the asthenumberoffailurecasesisinsufficienttotraintheselarge
layer number is lower than 3. We do not recommend setting models.
the layer number too large since training deep GNN requires Why GNN? GNN was chosen because the structure of mi-
extra training samples, which is hard to meet in real-world croservicesystemsinvolvesmanyinstancesandtheirrelation-
microservicesystems. ships,whichformthestructureofagraph.Variousapproaches
TimeWindow:Thelengthofthetimewindowhaslittleimpact incorporatingRandomWalk[12],[13]existtoaccomplishfail-
on performance because the moments when failures occur are urediagnosisonsuchgraphstructures.However,theirabilityto
sparse, and the anomaly events reported in a time window generalizeislimitedsincedomainknowledgecanvarygreatly
areonlyrelevanttothecurrentfailure.Withaccurateanomaly between different systems. The domain knowledge contained
detection,theperformanceofDiagFusionisstable. ingraphdatacanbeeffectivelylearnedbyGNNs[51],giving
themastrongergeneralizationabilitythanapproachesbasedon
VI. DISCUSSION RandomWalk.
Concerns About Learning-Based Methods: While learning-
A. WhyLearning-BasedMethods?
basedmethodsofferseveraladvantages,theydorequirelabeled
The DiagFusion approach incorporates several learning- samples for training. This can be addressed by 1) utilizingthe
based techniques, such as fastText in the Unified Event Rep- well-established failure management system in microservice
resentation(SectionIV-B)andGNN(SectionIV-C).Bydoing systems as a natural source of failure labeling, 2) DiagFusion
so,DiagFusionsignificantlyoutperformsbaselineapproaches. not requiring too many training samples to achieve good per-
We chose to build DiagFusion using learning-based methods formance (the sizes of the training set of D1 and D2 are 160
for the following reasons: 1) Accuracy: learning-based meth- and 80, respectively), and 3) the increasing adoption of chaos
ods provide high accuracy (Section V) and are therefore ideal engineering,whichenablesoperatorstoquicklyobtainsufficient
fordiagnosingfailures.2)Generalizationability:failurecases failurecases.Severalsuccessfulpracticeswiththehelpofchaos
used to train DiagFusion contain different patterns of failure engineeringhavebeenreported[2],[6],[16],[18].
propagationfordifferentsystems.Astronggeneralizationabil-
ity allows DiagFusion to perform robust diagnosis for each
B. Robustness
system.3)Abilitytohandlecomplicateddata:asmicroservice
systemsbecomeincreasinglycomplexandmonitoringdatamore Inpractice,somemodalitiescanbeabsent,hinderingasuc-
high-dimensional,manuallysettinguprulesforfailurediagno- cessful failure diagnosis system to some extent. The cause
sis becomes time-consuming and error-prone. Learning-based of missing modalities can be generally classified into three
methods,ontheotherhand,takethisdataasinputandlearntheir categories.Thefirstcategoryreferstomissingmodalitiescaused
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on November 13,2025 at 00:49:52 UTC from IEEE Xplore. Restrictions apply.

ZHANGetal.:ROBUSTFAILUREDIAGNOSISOFMICROSERVICESYSTEMTHROUGHMULTIMODALDATA 3861
|     |     |     | TABLEVI |     |     |     | modality.Besides,theGNNmoduledealswithfeaturevectors |     |     |     |     |     |     |     |
| --- | --- | --- | ------- | --- | --- | --- | ---------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
ROBUSTNESSCOMPAREDTOPDIAGNOSE(TASK#1) rather than original monitor data. DiagFusion can work given
thatanytwoofthethreemodalitiesareavailable.
|     |     |     |     |     |     |     | There | are two | main | threats | to the | validity | of the study. | The |
| --- | --- | --- | --- | --- | --- | --- | ----- | ------- | ---- | ------- | ------ | -------- | ------------- | --- |
firstoneliesinthelimitedsizesofthetwodatasetsusedinthe
study.D1andD2arerelativelysmallerthancomplexindustrial
|     |     |     |     |     |     |     | microservice   | systems. |                 | The second |            | one lies | in the    | limitation |
| --- | --- | --- | --- | --- | --- | --- | -------------- | -------- | --------------- | ---------- | ---------- | -------- | --------- | ---------- |
|     |     |     |     |     |     |     | of the failure | cases    | used            | in         | the study. | Some     | failure   | cases of   |
|     |     |     |     |     |     |     | D1 are         | simpler  | than industrial |            | failures   | and      | represent | only a     |
bydatacollectionproblems.Modernmicroservicesystemsare
limitedpartofdifferenttypesoffailures.However,accordingto
| developing | rapidly; | the | same | truth applies | to their | monitoring |     |     |     |     |     |     |     |     |
| ---------- | -------- | --- | ---- | ------------- | -------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
ourexperiments,DiagFusioniseffectiveandrobust.Itisvery
agents.Therefore,itishardtoguaranteethatallmonitoringdata
|     |     |     |     |     |     |     | promising | that | DiagFusion | can | also | be effectively | applied | to  |
| --- | --- | --- | --- | --- | --- | --- | --------- | ---- | ---------- | --- | ---- | -------------- | ------- | --- |
areideallycollectedandtransmitted.Asaresult,missingdata
muchlargerindustrialmicroservicesystemsandmorecomplex
| is inevitable, | which | can | give | rise to missing | modalities | when |     |     |     |     |     |     |     |     |
| -------------- | ----- | --- | ---- | --------------- | ---------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
failurecases.
specificmodalitiesofthemonitoringdataarehavingcollection
| problems. | The | second | category | refers | to missing | modalities |     |     |     |     |     |     |     |     |
| --------- | --- | ------ | -------- | ------ | ---------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
causedbydataavailabilityproblems.Insomelargecorporations, VII. RELATEDWORK
| monitoring | data       | is individually |          | collected  | by  | many different |              |     |         |           |          |     |            |      |
| ---------- | ---------- | --------------- | -------- | ---------- | --- | -------------- | ------------ | --- | ------- | --------- | -------- | --- | ---------- | ---- |
|            |            |                 |          |            |     |                | Metric-Based |     | Failure | Diagnosis | Methods: |     | Monitoring | met- |
| divisions. | Sometimes, |                 | specific | modalities | can | be exclusively |              |     |         |           |          |     |            |      |
ricsareoneofthemostimportantobservabledatainmicroser-
governedbyadivisionthatdoesnotwanttodiscloseitsservice
vicesystems.Manyworkstrytobuildadependencygraphtode-
| maintenance | data.Thus,thesemodalitiesarecollectedbutnot |     |     |     |     |     |     |     |     |     |     |     |     |     |
| ----------- | ------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
picttheinteractionbetweensystemcomponentsduringfailure,
| available | to general | operators. |     | The third | category | stands for |         |            |       |         |     |           |         |       |
| --------- | ---------- | ---------- | --- | --------- | -------- | ---------- | ------- | ---------- | ----- | ------- | --- | --------- | ------- | ----- |
|           |            |            |     |           |          |            | such as | Microscope | [11], | MS-Rank |     | [12], and | AutoMAP | [13]. |
missingmodalitiescausedbydataretrievalproblems.Inprac-
|     |     |     |     |     |     |     | However, | the correctness |     | of the | above | works | heavily | depends |
| --- | --- | --- | --- | --- | --- | --- | -------- | --------------- | --- | ------ | ----- | ----- | ------- | ------- |
tice,weoftenencountersituationswhereitisveryinconvenient
|             |            |     |      |          |            |            | on the parameter |      | settings, | which   | degrades |      | their applicability. |           |
| ----------- | ---------- | --- | ---- | -------- | ---------- | ---------- | ---------------- | ---- | --------- | ------- | -------- | ---- | -------------------- | --------- |
| to retrieve | monitoring |     | data | from the | data pool. | Multimodal |                  |      |           |         |          |      |                      |           |
|             |            |     |      |          |            |            | Besides,         | many | methods   | extract | features | from | system               | failures, |
failurediagnosisrequiresmuchmoredatatobecollectedthan
suchasGraph-RCA[52]andiSQUAD[50].Nonetheless,failure
| single-modal-based |     | methods |     | and may | face missing | modality |     |     |     |     |     |     |     |     |
| ------------------ | --- | ------- | --- | ------- | ------------ | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
casesarefewinmicroservicesystemsbecauseoperatorstryto
| problems. | However, | an  | excellent | multimodal-based |     | approach |         |        |             |     |           |          |           |     |
| --------- | -------- | --- | --------- | ---------------- | --- | -------- | ------- | ------ | ----------- | --- | --------- | -------- | --------- | --- |
|           |          |     |           |                  |     |          | run the | system | as robustly | as  | possible, | severely | affecting | the |
shouldperformwellevenwhensomemodalitiesaremissing.We
performanceofthesefeature-basedmethods.
discoverthat62failurecasesofD1lackmetricdata.DiagFusion
Trace-BasedFailureDiagnosisMethods:Tracecanbeused
| is compared | with | PDiagnose |     | in these | cases. | As PDiagnose |             |     |         |          |     |          |          |      |
| ----------- | ---- | --------- | --- | -------- | ------ | ------------ | ----------- | --- | ------- | -------- | --- | -------- | -------- | ---- |
|             |      |           |     |          |        |              | to localize | the | culprit | service, | for | example, | TraceRCA | [4], |
cannotaddressTask#2,weonlypresenttheresultsofTask#1.
|     |     |     |     |     |     |     | MEPFL | [18], MicroHECL |     | [5], | and | MicroRank | [6]. | However, |
| --- | --- | --- | --- | --- | --- | --- | ----- | --------------- | --- | ---- | --- | --------- | ---- | -------- |
AsshowninTableVI,theperformanceofPDiagnosedrops
thesetrace-basedmethodsoftenfocusontheglobalfeatureof
| dramatically | in  | these cases, | while | DiagFusion |     | presents salient |     |     |     |     |     |     |     |     |
| ------------ | --- | ------------ | ----- | ---------- | --- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- |
thesystemsanddonotdealwiththelocalfeaturesofaservice
robustness.AlthoughDiagFusionalsowitnessesaperformance
instance.
| degradation,    | it         | is still    | better | than PDiagnose            |     | and other Task  |                    |         |            |     |          |           |            |          |
| --------------- | ---------- | ----------- | ------ | ------------------------- | --- | --------------- | ------------------ | ------- | ---------- | --- | -------- | --------- | ---------- | -------- |
|                 |            |             |        |                           |     |                 | Log-Based          | Failure | Diagnosis  |     | Methods: |           | LogCluster | [7] per- |
| #1 baselines.   | DiagFusion |             | has    | seen complete             |     | data modalities |                    |         |            |     |          |           |            |          |
|                 |            |             |        |                           |     |                 | forms hierarchical |         | clustering |     | on log   | sequences | and        | matches  |
| during training |            | and learned |        | a unified representation, |     | allowing        |                    |         |            |     |          |           |            |          |
onlinelogsequencestothemostsimilarcluster.Cloud19[8]ap-
| it to capture | anomalous |     | patterns’ | correlation | to  | failures better |     |     |     |     |     |     |     |     |
| ------------- | --------- | --- | --------- | ----------- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- |
pliesword2vectoconstructthevectorizedrepresentationofalog
thansingle-modal-basedmethods.Ontheotherhand,PDiagnose
itemandtrainsclassifierstoidentifythefailuretype.Onion[9]
treatseachmodalityindependently,makingitineffectivewhen
performscontrastanalysisonagglomeratedlogcliquestofind
facingmissingmodalities.Tosumup,DiagFusiondemonstrates
incident-indicatinglogs.DeepLog[10]andLogFlash[53]inte-
robustnesssinceitachievessatisfactoryperformanceevenwhen
|     |     |     |     |     |     |     | grate anomaly |     | detection | and | failure | diagnosis. | They | calculate |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --- | --------- | --- | ------- | ---------- | ---- | --------- |
workingwithdatawithincompletemodalities.
|     |     |     |     |     |     |     | the deviation | from      | normal | status  | and   | suggest | the root        | cause |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --------- | ------ | ------- | ----- | ------- | --------------- | ----- |
|     |     |     |     |     |     |     | accordingly.  | Log-based |        | methods | often | ignore  | the topological |       |
C. ConcernsAboutDeploymentandValidity
featureofmicroservicesystems.
There are some concerns about deploying DiagFusion to Multimodal Data-Based Failure Diagnosis Methods: Re-
real-worldmicroservicesystems:1)DiagFusionneedstoadapt cently,combiningmultimodaldatatoconductfailurediagnosis
tothehighlydynamicnatureofmicroservicearchitecture.The hasdrawnincreasingattention.CloudRCA[48]usesbothmetric
storedmodelofDiagFusioncanstillbeeffectivewhenservice andlog.ItusesthePCalgorithmtolearnthecausalrelationship
instances are created or destroyed, for DiagFusion utilizes the betweenanomalypatternsofmetrics,anomalypatternsoflogs,
conceptofservicegroupasamiddlelayer.Theonlysituationin andtypesoffailure.ThenitconstructsahierarchicalBayesian
which DiagFusion needs to be retrained is when new service Network to infer the failure type. PDiagnose [47] combines
groups are created. However, the creation of service groups metric, log, and trace. It uses lightweight anomaly detection
is very rare in practice. 2) Some production systems do not of the three modalities to detect anomaly patterns. Then its
monitor all three modalities at the same time. The workflow vote-based strategy selects the most severe component as the
of DiagFusion is general because the event embedding model root cause. However, these two methods ignore the topology
istrainedoneventsequencesanddoesnotrelyonanyspecific featureofmicroservicesystems.Groot[54]integratesmetrics,
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on November 13,2025 at 00:49:52 UTC from IEEE Xplore.  Restrictions apply.

3862 IEEETRANSACTIONSONSERVICESCOMPUTING,VOL.16,NO.6,NOVEMBER/DECEMBER2023
TABLEVII
COMPARISONOFDIAGFUSIONANDEXISTINGREPRESENTATIVEAPPROACHES
statuslogs,anddeveloperactivity.Itneedsnumerouspredefined [8] Y.Yuan,W.Shi,B.Liang,andB.Qin,“Anapproachtocloudexecution
rules to conduct accurate failure diagnosis, which degrades its failurediagnosisbasedonexceptionlogsinOpenStack,”inProc.IEEE
12thInt.Conf.CloudComput.,2019,pp.124–131.
applicabilitytomostscenarios.
[9] X. Zhang et al., “Onion: Identifying incident-indicating logs for cloud
We compare DiagFusion and existing representative ap- systems,”inProc.29thACMJointMeetingEur.Softw.Eng.Conf.Symp.
proachesinTableVII.Inconclusion,comparedtosingle-modal- Found.Softw.Eng.,2021,pp.1253–1263.
[10] M.Duetal.,“DeepLog:Anomalydetectionanddiagnosisfromsystem
basedmethods,DiagFusiontakesthethreeimportantmodalities
logsthroughdeeplearning,”inProc.ACMSIGSACConf.Comput.Com-
intoaccount.Comparedtoexistingmultimodal-basedmethods, mun.Secur.,2017,pp.1285–1298.
DiagFusionisamongthefirsttorepresentdifferentmodalitiesin [11] J.Lin,P.Chen,andZ.Zheng,“Microscope:Pinpointperformanceissues
withcausalgraphsinmicro-serviceenvironments,”inProc.16thInt.Conf.
aunifiedmanner,thusperformingmorerobustlyandaccurately.
Serv.-OrientedComput.,Springer,Hangzhou,China,Nov.12–15,2018,
pp.3–20.
[12] M.Ma,W.Lin,D.Pan,andP.Wang,“Self-adaptiverootcausediagnosis
VIII. CONCLUSION
forlarge-scalemicroservicearchitecture,”IEEETrans.ServicesComput.,
vol.15,no.3,pp.1399–1410,May/Jun.2022.
Failure diagnosis is of great importance for microservice
[13] M.Maetal.,“AutoMAP:Diagnoseyourmicroservice-basedwebappli-
systems. In this paper, we first conduct an empirical study to cationsautomatically,”inProc.WebConf.,Y.HuangEds.etal.,Taipei,
illustrate the importance of using multimodal data (i.e., trace, Taiwan,Apr.20–24,2020,pp.246–258.
[14] Y.Panetal.,“Faster,deeper,easier:Crowdsourcingdiagnosisofmicroser-
metric,log)forfailurediagnosisofmicroservicesystems.Then
vicekernelfailurefromuserspace,”inProc.30thACMSIGSOFTInt.
weproposeDiagFusion,anautomaticfailurediagnosismethod, Symp.Softw.TestingAnal.,2021,pp.646–657.
which first extracts events from three modalities of data and [15] B.H.Sigelmanetal.,“Dapper,alarge-scaledistributedsystemstracing
infrastructure,” 2010. [Online]. Available: http://research.google.com/
applies fastText embedding to unify the event from different
archive/papers/dapper-2010-1.pdf
modalities. During training, DiagFusion leverages data aug- [16] T. Yang et al., “AID: Efficient prediction of aggregated intensity of
mentation to tackle the challenge of data imbalance. Then it dependencyinlarge-scalecloudsystems,”inProc.IEEE/ACM36thInt.
Conf.AutomatedSoftw.Eng.,2021,pp.653–665.
constructsadependencygraphbycombiningtraceanddeploy-
[17] J.Kaldoretal.,“Canopy:Anend-to-endperformancetracingandanalysis
ment data. Moreover, DiagFusion integrates event embedding system,”inProc.26thSymp.OperatingSyst.Princ.,Shanghai,China,Oct.
and the dependency graph through GNN. Finally, the GNN 28–31,2017,pp.34–50.
[18] X.Zhouetal.,“Latenterrorpredictionandfaultlocalizationformicroser-
reports the root cause instance and the failure type of online
viceapplicationsbylearningfromsystemtracelogs,”inProc.27thACM
failure.WeevaluateDiagFusionusingtworeal-worlddatasets. Joint Meeting Eur. Softw. Eng. Conf. Symp. Found. Softw. Eng., 2019,
Theevaluationresultsconfirmtheeffectivenessandefficiency pp.683–694.
[19] C.Zhangetal.,“DeepTraLog:Trace-logcombinedmicroserviceanomaly
ofDiagFusion.
detection through graph-based deep learning,” in Proc. 44th Int. Conf.
Softw.Eng.,2022,pp.623–634.
REFERENCES [20] B.Lietal.,“Enjoyyourobservability:Anindustrialsurveyofmicroser-
vicetracingandanalysis,”EmpiricalSoftw.Eng.,vol.27,no.1,2022,
[1] X.Guoetal.,“Graph-basedtraceanalysisformicroservicearchitecture Art.no.25.
understandingandproblemdiagnosis,”inProc.28thACMJointMeeting [21] P. Liu et al., “Unsupervised detection of microservice trace anomalies
Eur.Softw.Eng.Conf.Symp.Found.Softw.Eng.,2020,pp.1387–1397. throughservice-leveldeepBayesiannetworks,”inProc.IEEE31stInt.
[2] X.Zhouetal.,“Faultanalysisanddebuggingofmicroservicesystems: Symp.Softw.Rel.Eng.,2020,pp.48–58.
Industrialsurvey,benchmarksystem,andempiricalstudy,”IEEETrans. [22] P.He,J.Zhu,Z.Zheng,andM.R.Lyu,“Drain:Anonlinelogparsing
Softw.Eng.,vol.47,no.2,pp.243–260,Feb.2021. approach with fixed depth tree,” in Proc. IEEE Int. Conf. Web Serv.,
[3] AWS,“SummaryoftheAWSserviceeventintheNorthernVirginia(US- I. Altintas and S. Chen, Eds., Honolulu, HI, USA, Jun. 25–30, 2017,
EAST-1)region,”2021.[Online].Available:https://aws.amazon.com/cn/ pp.33–40.
message/12721/ [23] S. Zhang et al., “Syslog processing for switch failure diagnosis and
[4] Z.Lietal.,“Practicalrootcauselocalizationformicroservicesystems predictionindatacenternetworks,”inProc.25thIEEE/ACMInt.Symp.
viatraceanalysis,”inProc.IEEE/ACM29thInt.Symp.Qual.Serv.,2021, Qual.Serv.,VilanovailaGeltrú,Spain,Jun.14–16,2017,pp.1–10.
pp.1–10. [24] P. He, J. Zhu, S. He, J. Li, and M. R. Lyu, “Towards automated log
[5] M.Jinetal.,“Ananomalydetectionalgorithmformicroservicearchitec- parsingforlarge-scalelogdataanalysis,”IEEETrans.DependableSecure
turebasedonrobustprincipalcomponentanalysis,”IEEEAccess,vol.8, Comput.,vol.15,no.6,pp.931–944,Nov./Dec.2018.
pp.226397–226408,2020. [25] S.Messaoudietal.,“Asearch-basedapproachforaccurateidentification
[6] G. Yu et al., “MicroRank: End-to-end latency issue localization with oflogmessageformats,”inProc.26thConf.Prog.Comprehension,F.
extendedspectrumanalysisinmicroserviceenvironments,”inProc.Web Khomh,C.K.Roy,andJ.Siegmund,Eds.,Gothenburg,Sweden,May
Conf.,2021,pp.3087–3098. 27/28,2018,pp.167–177.
[7] Q. Lin et al., “Log clustering based problem identification for online [26] M. Du and F. Li, “Spell: Online streaming parsing of large unstruc-
servicesystems,”inProc.38thInt.Conf.Softw.Eng.Companion,2016, tured system logs,” IEEE Trans. Knowl. Data Eng., vol. 31, no. 11,
pp.102–111. pp.2213–2227,Nov.2019.
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on November 13,2025 at 00:49:52 UTC from IEEE Xplore. Restrictions apply.

ZHANGetal.:ROBUSTFAILUREDIAGNOSISOFMICROSERVICESYSTEMTHROUGHMULTIMODALDATA 3863
[27] H.Dai,H.Li,C.Chen,W.Shang,andT.-H.Chen,“Logram:Efficient [49] Y.Mengetal.,“Localizingfailurerootcausesinamicroservicethrough
logparsingusingn-gramdictionaries,”IEEETrans.Softw.Eng.,vol.48, causality inference,” in Proc. IEEE/ACM 28th Int. Symp. Qual. Serv.,
no.3,pp.879–892,Mar.2022. Hangzhou,China,Jun.15–17,2020,pp.1–10.[Online].Available:https:
[28] M.Sunetal.,“CTF:Anomalydetectioninhigh-dimensionaltimeseries //doi.org/10.1109/IWQoS49365.2020.9213058
withcoarse-to-finemodeltransfer,”inProc.IEEE40thConf.Comput. [50] M. Ma et al., “Diagnosing root causes of intermittent slow queries in
Commun.,Vancouver,BC,Canada,May10–13,2021,pp.1–10. large-scaleclouddatabases,”inProc.VLDBEndowment,vol.13,no.8,
[29] Y.Suetal.,“DetectingoutliermachineinstancesthroughGaussianmix- pp.1176–1189,2020.
turevariationalautoencoderwithonedimensionalCNN,”IEEETrans. [51] Z.Zhang,P.Cui,andW.Zhu,“Deeplearningongraphs:Asurvey,”IEEE
Comput.,vol.71,no.4,pp.892–905,Apr.2022. Trans.Knowl.DataEng.,vol.34,no.1,pp.249–270,Jan.2022.
[30] L.Shenetal.,“Timeseriesanomalydetectionwithmultiresolutionensem- [52] Á. Brandón et al., “Graph-based root cause analysis for service-
bledecoding,”inProc.35thAAAIConf.Artif.Intell.33rdConf.Innov. orientedandmicroservicearchitectures,”J.Syst.Softw.,vol.159,2020,
Appl.Artif.Intell.11thSymp.Educ.Adv.Artif.Intell.,2021,pp.9567– Art.no.110432.
9575. [53] T.Jia,Y.Wu,C.Hou,andY.Li,“LogFlash:Real-timestreaminganomaly
[31] M.Maetal.,“Jump-startingmultivariatetimeseriesanomalydetection detection and diagnosis from system logs for large-scale software sys-
foronlineservicesystems,”inProc.USENIXAnnu.Tech.Conf.,I.Calciu tems,”inProc.IEEE32ndInt.Symp.Softw.Rel.Eng.,Z.JinEds.etal.,
andG.Kuenning,Eds.,USENIXAssoc.,2021,pp.413–426. Wuhan,China,Oct.25–28,2021,pp.80–90.
[32] Z.Lietal.,“Multivariatetimeseriesanomalydetectionandinterpretation [54] H.Wangetal.,“Groot:Anevent-graph-basedapproachforrootcauseanal-
usinghierarchicalinter-metricandtemporalembedding,”inProc.27th ysisinindustrialsettings,”inProc.IEEE/ACM36thInt.Conf.Automated
ACMSIGKDDConf.Knowl.Discov.DataMining,F.Zhu,B.C.Ooi,and Softw.Eng.,Melbourne,Australia,Nov.15–1,2021,pp.419–429.
C.Miao,Eds.,2021,pp.3220–3230.
[33] L.Daietal.,“SDFVAE:StaticanddynamicfactorizedVAEforanomaly
detectionofmultivariateCDNKPIs,”inProc.WebConf.,J.LeskovecEds. Shenglin Zhang (Member, IEEE) received the BS
etal.,2021,pp.3076–3086. degree in network engineering from the School of
[34] T.Mikolov,K.Chen,G.Corrado,andJ.Dean,“Efficientestimationof ComputerScienceandTechnology,XidianUniver-
wordrepresentationsinvectorspace,”2013,arXiv:1301.3781. sity,Xi’an,China,in2012,andthePhDdegreein
[35] J.Pennington,R.Socher,andC.D.Manning,“GloVe:Globalvectors computersciencefromTsinghuaUniversity,Beijing,
forwordrepresentation,”inProc.Conf.EmpiricalMethodsNaturalLang. China,in2017.Heiscurrentlyanassociateprofessor
Process.,A.Moschitti,B.Pang,andW.Daelemans,Eds.,2014,pp.1532– with the College of Software, Nankai University,
1543. Tianjin,China.Hiscurrentresearchinterestsinclude
[36] P.Bojanowskietal.,“Enrichingwordvectorswithsubwordinformation,” failuredetection,diagnosis,andpredictionforservice
Trans.Assoc.Comput.Linguistics,vol.5,pp.135–146,2017. management.
[37] M.E.Petersetal.,“Deepcontextualizedwordrepresentations,”inProc.
Conf. North Amer. Chapter Assoc. Comput. Linguistics: Hum. Lang.
Technol.,M.A.Walker,H.Ji,andA.Stent,Eds.,NewOrleans,LA,USA,
Jun.1–6,2018,pp.2227–2237. PengxiangJinreceivedthebachelor’sdegreeinsoft-
[38] J.Devlinetal.,“BERT:Pre-trainingofdeepbidirectionaltransformersfor ware engineering from Nankai University, Tianjin,
languageunderstanding,”2018,arXiv:1810.04805. China,in2020.Heiscurrentlyworkingtowardthe
[39] T. B. Brown et al., “Language models are few-shot learners,” in Proc. masterdegreewiththeCollegeofSoftware,Nankai
Int. Conf. Neural Inf. Process. Syst., H. Larochelle Eds. et al., 2020, University. His research interests include anomaly
Art.no.159. detectionandanomalylocalization.
[40] W.Mengetal.,“LogAnomaly:Unsuperviseddetectionofsequentialand
quantitativeanomaliesinunstructuredlogs,”inProc.28thInt.JointConf.
Artif.Intell.,S.Kraus,Ed.,Macao,China,Aug.10–16,2019,pp.4739–
4745.
[41] T.N.KipfandM.Welling,“Semi-supervisedclassificationwithgraph
convolutionalnetworks,”2016,arXiv:1609.02907.
[42] W. L. Hamilton, Z. Ying, and J. Leskovec, “Inductive representation
learningonlargegraphs,”inProc.Int.Conf.NeuralInf.Process.Syst.,I. ZihanLinreceivedthebachelor’sdegreeinsoftware
GuyonEds.etal.,LongBeach,CA,USA,2017,pp.1024–1034. engineeringfromNankaiUniversity,Tianjin,China,
[43] L.Zhou,Q.Zeng,andB.Li,“Hybridanomalydetectionviamultihead in2021.Heiscurrentlyworkingtowardthemaster
dynamic graph attention networks for multivariate time series,” IEEE degreewiththeCollegeofSoftware,NankaiUniver-
Access,vol.10,pp.40967–40978,2022. sity.Hisresearchinterestsincludefailurelocalization
[44] L.Zhang,B.Morin,P.Haller,B.Baudry,andM.Monperrus,“AChaos andanomalydetection.
engineeringsystemforliveanalysisandfalsificationofexception-handling
intheJVM,”IEEETrans.Softw.Eng.,vol.47,no.11,pp.2534–2548,
Nov.2021.
[45] Y.Wangetal.,“Fastoutageanalysisoflarge-scaleproductioncloudswith
servicecorrelationmining,”inProc.IEEE/ACM43rdInt.Conf.Softw.
Eng.,Madrid,Spain,May22–30,2021,pp.885–896.
[46] Y. Zhou et al., “Graph neural networks: Taxonomy, advances, and
trends,”ACMTrans.Intell.Syst.Technol.,vol.13,no.1,pp.15:1–15:54, YongqianSun(Member,IEEE)receivedtheBSde-
2022. greeinstatisticalspecialtyfromNorthwesternPoly-
[47] C.Hou,T.Jia,Y.Wu,Y.Li,andJ.Han,“Diagnosingperformanceissues technicalUniversity,Xi’an,China,in2012,andthe
in microservices with heterogeneous data source,” in Proc. IEEE Int. PhDdegreeincomputersciencefromTsinghuaUni-
Conf.ParallelDistrib.Process.Appl.BigDataCloudComput.Sustain. versity,Beijing,China,in2018.Heiscurrentlyanas-
Comput. Commun. Social Comput. Netw., New York, NY, USA, 2021, sistantprofessorwiththeCollegeofSoftware,Nankai
pp.493–500. University,Tianjin,China.Hisresearchfocuseson
[48] Y.Zhangetal.,“CloudRCA:Arootcauseanalysisframeworkforcloud anomaly detection, root cause analysis, and failure
computingplatforms,”inProc.30thACMInt.Conf.Inf.Knowl.Manage., diagnosisinservicemanagement.
G.DemartiniEds.etal.,2021,pp.4373–4382.
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on November 13,2025 at 00:49:52 UTC from IEEE Xplore. Restrictions apply.

3864 IEEETRANSACTIONSONSERVICESCOMPUTING,VOL.16,NO.6,NOVEMBER/DECEMBER2023
BichengZhangreceivedthebachelor’sdegreefrom Wa Jin is currently working toward the bachelor
NankaiUniversity.Heiscurrentlyworkingtoward degree.Hermainresearchinterestsincludeanomaly
themasterdegreewithFudanUniversity.Hisresearch detectionandfailurediagnosis.
interestsincludecloudnativeandAIOps.
SiboXiaiscurrentlyworkingtowardthemasterde-
gree.Hismainresearchinterestsincludeknowledge
graph,failuredetection,anddiagnosis. Dai Zhang is employed with ZhejiangE-
CommerceBankCo.,Ltd.,LaunchedbyAntGroup.
Asatechnicalexpert,hemainlyfocusesonfinancial
basictechnicalarchitectureandcloud-nativesystem
stability.
ZhengdanLiisanexperimentalistwithNankaiUni-
versity,Tianjin,China.Herresearchinterestsinclude
artificialintelligenceandsoftwareengineering.
Zhenyu Zhu is employed with ZhejiangE-
CommerceBankCo.,Ltd.,LaunchedbyAntGroup.
Asatechnicalexpert,hemainlyfocusesonfinancial
basictechnicalarchitectureandcloud-nativesystem
stability.
ZhenyuZhongreceivedtheBSdegreeinsoftware
engineeringfromNankaiUniversity,Tianjin,China,
in2020.HeiscurrentlyworkingtowardthePhDde-
greewiththeCollegeofSoftware,NankaiUniversity,
Tianjin,China.Hiscurrentresearchinterestsinclude
anomalydetection,deeplearning,andNLP.
DanPei(SeniorMember,IEEE)receivedtheBEand
MSdegreesincomputersciencefromtheDepartment
ofComputerScienceandTechnology,TsinghuaUni-
versity,in1997and2000,respectively,andthePhD
degreeincomputersciencefromtheComputerSci-
Minghua Ma (Member, IEEE) received the PhD enceDepartment,UniversityofCalifornia,LosAn-
degreefromTsinghua University, in 2021.He is a geles(UCLA),in2005.Heiscurrentlyanassociate
researcherwithMicrosoft.Hiscurrentresearchinter- professorwiththeDepartmentofComputerScience
estsincludecloudintelligence/AIOps. andTechnology,TsinghuaUniversity.Hisresearch
interestsincludenetworkandservicemanagementin
general.HeisaseniormemberoftheACM.
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on November 13,2025 at 00:49:52 UTC from IEEE Xplore. Restrictions apply.