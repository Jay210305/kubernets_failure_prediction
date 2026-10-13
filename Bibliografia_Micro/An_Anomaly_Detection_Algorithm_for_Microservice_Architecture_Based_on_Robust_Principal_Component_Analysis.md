ReceivedNovember19,2020,acceptedDecember8,2020,dateofpublicationDecember14,2020,
dateofcurrentversionDecember31,2020.
DigitalObjectIdentifier10.1109/ACCESS.2020.3044610
| An Anomaly                      |     |           | Detection    |     | Algorithm |                            |     | for |        |     |     |     |     |     |
| ------------------------------- | --- | --------- | ------------ | --- | --------- | -------------------------- | --- | --- | ------ | --- | --- | --- | --- | --- |
| Microservice                    |     |           | Architecture |     |           | Based                      |     | on  | Robust |     |     |     |     |     |
| Principal                       |     | Component |              |     | Analysis  |                            |     |     |        |     |     |     |     |     |
| MINGXUJIN1,AORANLV1,YUANPENGZHU |     |           |              |     |           | 1,ZIJIANGWEN2,YUBINZHONG2, |     |     |        |     |     |     |     |     |
ZEXINZHAO1,JIANGWU1,HEJIELI1,HANHENGHE1,ANDFENGYICHEN3
1SchoolofMathematics,SouthChinaUniversityofTechnology,Guangzhou510641,China
2JOYYInc.,Guangzhou511442,China
3SchoolofManagementAdministration,GuangdongIndustryPolytechnic,Guangzhou510330,China
Correspondingauthor:YuanpengZhu(ypzhu@scut.edu.cn)
ThisworkwassupportedinpartbytheNationalNaturalScienceFoundationofChinaunderGrant61802129,andinpartbytheNatural
ScienceFoundationofGuangdongProvince,China,underGrant2018A030310381.
ABSTRACT Microservicearchitecture(MSA)isanewsoftwarearchitecture,whichdividesalargesingle
applicationandserviceintodozensofsupportingmicroservices.WiththeincreasinglypopularityofMSA,
the security issues of MSA get a lot of attention. In this paper, we propose an algorithm for mining
causalityandtherootcause.Ouralgorithmconsistsoftwoparts:invocationchainanomalyanalysisbased
on robust principal component analysis (RPCA) and a single indicator anomaly detection algorithm. The
single indicator anomaly detection algorithm is composed of Isolation Forest (IF) algorithm, One-Class
Support Vector Machine (SVM) algorithm, Local Outlier Factor (LOF) algorithm, and 3σ principle. For
generalandnetworktime-consuminganomalyintheprocessoftheMSA,weformulatedifferentanomaly
time-consuming detection strategies. We select a batch of sample data and three batches of test data of
the 2020 International AIOps Challenge to debug our algorithm. According to the scoring criteria of the
competitionorganizers,ouralgorithmhasanaveragescoreof0.8304(Thefullscoreis1)inthefourbatches
ofdata.Ourproposedalgorithmhashigheraccuracythansometraditionalmachinelearningalgorithmsin
anomalydetection.
Microservicearchitecture,rootcauseanalysis,anomalydetection.
INDEXTERMS
I. INTRODUCTION forothers,bythisstrategy,therearestillsomeproblemsinthe
| The concept | of  | microservice |     | emerged | in 2012. As | a way | MSA[3]–[6]: |     |     |     |     |     |     |     |
| ----------- | --- | ------------ | --- | ------- | ----------- | ----- | ----------- | --- | --- | --- | --- | --- | --- | --- |
to speed up the development process of web and mobile ThewholeapplicationofMSAisdividedintomultiple
•
applications,ithasbeenwidelyconcernedsince2014.MSA
services,soitisdifficulttolocatethefailurenodes.
isanarchitectureconcept.Itsmainideaistodecomposeabig • IntheMSA,aservicefailuremayproduceanavalanche
serviceintodiscreteservices,toreducesystemcoupling,and
effect,resultinginthewholesystemfailure.
| provide more | flexible | service |     | support. | MSA divides | a large |     |            |     |                 |     |            |          |     |
| ------------ | -------- | ------- | --- | -------- | ----------- | ------- | --- | ---------- | --- | --------------- | --- | ---------- | -------- | --- |
|              |          |         |     |          |             |         |     | Therefore, | the | fault diagnosis | and | root cause | analysis | of  |
singleapplicationandserviceintoseveralorevendozensof
|     |     |     |     |     |     |     | MSA | is  | particularly | important. | Currently, | most | studies | of  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ---------- | ---------- | ---- | ------- | --- |
supportingmicroservices.Itcanexpandasinglecomponent
|             |     |                    |     |       |             |         | root      | cause | analysis  | (RCA) rely         | mainly | on monitoring |                | data, |
| ----------- | --- | ------------------ | --- | ----- | ----------- | ------- | --------- | ----- | --------- | ------------------ | ------ | ------------- | -------------- | ----- |
| rather than | the | entire application |     | stack | to meet the | service |           |       |           |                    |        |               |                |       |
|             |     |                    |     |       |             |         | including |       | log data, | service dependency |        | data,         | and invocation |       |
levelagreement[1],[2].
chaindata[7]–[11].
TheMSAmakestheresponsibilitiesofeachpartofthesys-
Inrecentyears,therearemoreandmoreRCAalgorithms
temclearer.Eachpartisdedicatedtoprovidingbetterservices
andanomalydetectionalgorithmsdependingongraphs.The
|     |     |     |     |     |     |     | researches |     | of some | MSA and | cloud | applications | are | very |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --- | ------- | ------- | ----- | ------------ | --- | ---- |
representative[9]–[21].
The associate editor coordinating the review of this manuscript and Ma et al. presented iSQUAD, a framework for iSQ root
approvingitforpublicationwasBohuiWang . causediagnoses,todealwiththeproblemofintermittentslow
ThisworkislicensedunderaCreativeCommonsAttribution-NonCommercial-NoDerivatives4.0License.
VOLUME8,2020 Formoreinformation,seehttps://creativecommons.org/licenses/by-nc-nd/4.0/ 226397

M.Jinetal.:AnomalyDetectionAlgorithmforMSABasedonRPCA
queries (iSQs) in real-world cloud databases [9]. Nie et al. of our algorithm in practical problems is demonstrated in
proposed an automatic diagnosis system based on causality Section III. Section IV summarizes the conclusions and
graph to help system operators find the root causes [10]. describesourfuturework.
| Xu et | al. presented |     | a novel | approach |     | to API | perfor- |     |     |     |     |     |     |     |     |
| ----- | ------------- | --- | ------- | -------- | --- | ------ | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
mance monitoring, which recognizes performance prob- II. PROBLEMDESCRIPTIONANDOURSOLUTION
lems by response time deviation from a baseline response Inthissection,wedescribetheproblemthatourmethodisto
| time/throughput |     | model | that | are created |     | and continuously |     |     |     |     |     |     |     |     |     |
| --------------- | --- | ----- | ---- | ----------- | --- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
solve.Then,weelaborateonourprojectframeworkindetail.
| updated | through | online | learning | [12]. | Wang | et al. | proposed |     |     |     |     |     |     |     |     |
| ------- | ------- | ------ | -------- | ----- | ---- | ------ | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
adynamiccausalrelationshipanalysisapproachtoconstruct
A. DESCRIPTIONOFTHEPROBLEM
impactgraphsamongstapplicationswithoutgiventhetopol- Theanalysisobjectofthischallengeisamicroserviceappli-
| ogy [14]. | Yan | et al. described |     | the design |     | and development |     |     |     |     |     |     |     |     |     |
| --------- | --- | ---------------- | --- | ---------- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
cationsystem(arealmicroserviceapplicationintheprivate
| of a Generic | Root | Cause | Analysis |     | platform | (G-RCA) | for |                   |     |     |         |            |     |      |         |
| ------------ | ---- | ----- | -------- | --- | -------- | ------- | --- | ----------------- | --- | --- | ------- | ---------- | --- | ---- | ------- |
|              |      |       |          |     |          |         |     | cloud environment |     | of  | a large | operator). | The | data | is pro- |
servicequalitymanagement(SQM)inlargeIPnetworks[19]. vided by Zhejiang Mobile, including static topology data
Maetal.presentedaframework,StepWise,whichcandetect
|     |     |     |     |     |     |     |     | between | services, | invocation |     | chain data, | gold | indicator | data |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | --------- | ---------- | --- | ----------- | ---- | --------- | ---- |
concept drift without tuning detection threshold or per-KPI ofobservedservices,andtime-seriesdataofunderlyingser-
| (Key Performance |     | Indicator) |     | model | parameters |     | in a large |     |     |     |     |     |     |     |     |
| ---------------- | --- | ---------- | --- | ----- | ---------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
vices(operatingsystem,oracle,container,andmiddleware).
scaleKPIstreams[21].
|              |           |              |      |              |             |         |          | All the          | datasets | in this | paper | could | be downloaded |     | from: |
| ------------ | --------- | ------------ | ---- | ------------ | ----------- | ------- | -------- | ---------------- | -------- | ------- | ----- | ----- | ------------- | --- | ----- |
| RPCA         | algorithm | has          | been | successfully |             | applied | in image | http://iops.ai/. |          |         |       |       |               |     |       |
| recognition, | face      | recognition, |      | signal       | processing, |         | computer |                  |          |         |       |       |               |     |       |
Inthiscompetition,weaimtocarryoutanomalydetection
visionandmanyotheraspects[22]–[28].
|       |               |     |             |       |            |     |         | on business | indicators, |            | root   | cause analysis |             | at the | time of |
| ----- | ------------- | --- | ----------- | ----- | ---------- | --- | ------- | ----------- | ----------- | ---------- | ------ | -------------- | ----------- | ------ | ------- |
| Li et | al. addressed |     | the singing | voice | separation |     | problem |             |             |            |        |                |             |        |         |
|       |               |     |             |       |            |     |         | anomaly.    | Then        | we further | locate | and            | investigate | the    | failed  |
andproposedanovelunsupervisedapproachbasedonRPCA
|     |     |     |     |     |     |     |     | container | or node, | and | finally | get | the failed | indicators. |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | -------- | --- | ------- | --- | ---------- | ----------- | --- |
exploitingrank-1constraint(CRPCA)[22].Zhangetal.sur- In addition to network type failures, other types of failures
| veyed the   | applications |       | of RPCA    | in    | computer | vision, | image       |                |       |              |        |          |             |        |          |
| ----------- | ------------ | ----- | ---------- | ----- | -------- | ------- | ----------- | -------------- | ----- | ------------ | ------ | -------- | ----------- | ------ | -------- |
|             |              |       |            |       |          |         |             | are needed     | to be | located      | at the | level of | performance |        | indica-  |
| processing, | and          | video | processing | [23]. | Mardani  |         | et al. cor- |                |       |              |        |          |             |        |          |
|             |              |       |            |       |          |         |             | tors (non-gold |       | indicators), | i.e.,  | not only | the         | failed | contain- |
roborated the effectiveness of RPCA in unveiling traffic ers or nodes but also the performance indicators that cause
| anomalies | across | flows | and | time | [24]. Amoozegar |     | et al. |     |     |     |     |     |     |     |     |
| --------- | ------ | ----- | --- | ---- | --------------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
thefailure.
proposedanewrobustonlinesubspaceandanomalytracker
| for anomaly |     | detection | in  | time-evolving |     | networks | [25]. |     |     |     |     |     |     |     |     |
| ----------- | --- | --------- | --- | ------------- | --- | -------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
B. OVERALLFRAMEWORKOFOURPROJECT
| Dingetal. | designed | a   | more | robust | and | useful | real-time |     |     |     |     |     |     |     |     |
| --------- | -------- | --- | ---- | ------ | --- | ------ | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
Thebasicframeworkofouralgorithmisasfollows:
| false data | injection | attack | detection |     | mechanism |     | based on |     |     |     |     |     |     |     |     |
| ---------- | --------- | ------ | --------- | --- | --------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
RPCA applied in the supervisory control and data acquisi- • According to the success rate and average time of esb
indicatorsevery60seconds,wescreenpotentialanoma-
| tion (SCADA) |     | system | in smart | grid | [26]. | Mahapatra | et al. |     |     |     |     |     |     |     |     |
| ------------ | --- | ------ | -------- | ---- | ----- | --------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
loustimeperiod.
presentedamethodfordetectingmaliciousdatainjectionsin
PMUmeasurementsandthecorruptedsignalswererecovered • For the potential anomalous time period, we find out
|     |     |     |     |     |     |     |     | the | invocation | chain | in  | the nearby | time | period, | and |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ----- | --- | ---------- | ---- | ------- | --- |
usingaRPCA-basedalgorithm[27].Songetal.proposedan
|     |     |     |     |     |     |     |     | analyze | the | anomalous |     | nodes in | the invocation |     | chain |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | --------- | --- | -------- | -------------- | --- | ----- |
ensembletensordecompositiontoextractweaktargetsignal
|     |     |     |     |     |     |     |     | (generation |     | of anomalous |     | nodes | candidate | set | based |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ------------ | --- | ----- | --------- | --- | ----- |
ofinfraredthermographyvideosforcracksdetection[28].
ontheRPCA-basedinvocationchainanomalyanalysis
| In this | paper, | we use | invocation |     | chain | anomaly | analysis |     |     |     |     |     |     |     |     |
| ------- | ------ | ------ | ---------- | --- | ----- | ------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
based on RPCA and a single indicator anomaly detection algorithm).
|     |     |     |     |     |     |     |     | • For | the final | anomalous |     | nodes candidate |     | set, | we find |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | --------- | --------- | --- | --------------- | --- | ---- | ------- |
algorithmtohelpsolvetheRCAproblem.Inbrief,ourcon-
|     |     |     |     |     |     |     |     | all | related | cmdb_id | according | to  | the given | architecture |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | ------- | --------- | --- | --------- | ------------ | --- |
tributionscanbesummarizedasfollows:
• OuralgorithmisanRCAapproachcomposingofRPCA table, and perform single indicator anomaly detection
|           |     |             |        |           |     |         |        | (Isolation |     | Forest algorithm, |     | 3σ  | principle, | etc.) | for all |
| --------- | --- | ----------- | ------ | --------- | --- | ------- | ------ | ---------- | --- | ----------------- | --- | --- | ---------- | ----- | ------- |
| algorithm |     | and various | single | indicator |     | anomaly | detec- |            |     |                   |     |     |            |       |         |
tionalgorithms. singleindicatorscorrespondingtothesecmdb_ids.The
Our algorithm gets the anomalous nodes accurately by finaloutputofouralgorithmisthefinalrootcausethat
•
thealgorithmscoresandsortstheindicators.
| invocation |     | chain anomaly |     | analysis | algorithm |     | based on |     |     |     |     |     |     |     |     |
| ---------- | --- | ------------- | --- | -------- | --------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
RPCA,andlocatestheanomalousindicatorsofthecor- Figure 1 and Figure 2 respectively show the invoca-
respondingnodesbycombiningvarioussingleindicator tion chain anomaly detection frame diagram and indicator
| anomalydetectionalgorithms. |     |     |     |     |     |     |     | anomalydetectionflowchart. |     |     |     |     |     |     |     |
| --------------------------- | --- | --- | --- | --- | --- | --- | --- | -------------------------- | --- | --- | --- | --- | --- | --- | --- |
Wehaveprovedthatouralgorithmrankstherootcauses
• Our root cause positioning strategy is as follows: Firstly,
in the top two with 91.3% precision for the given four weimplementtheinvocationchainanomalydetectionalgo-
batches of data. Our algorithm has an average score rithm based on the RPCA algorithm, and analyze a certain
of0.8304inthefourbatchesofdata. number of invocation chains extracted from the fault time
The rest of this paper is structured as follows: The prob- period.Thenwegetthenodeswithhighanomalyscores.Sec-
lemsandsolutionsaredescribedinSectionII.Applications ondly, we invoke the indicator anomaly detection algorithm
| 226398 |     |     |     |     |     |     |     |     |     |     |     |     |     | VOLUME8,2020 |     |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- |

M.Jinetal.:AnomalyDetectionAlgorithmforMSABasedonRPCA
FIGURE3. Twosimpleinvocationchainsandservicetimeconsuming.
FIGURE1. Framediagramofinvocationchainanomalydetection. TABLE1. Time-consumingmatrixofthetwoinvocationchains.
invocationchainarchitecturedetection.Otherwise,thesame
| window     | should be used | for       | host network |          | indicator | anomaly  |
| ---------- | -------------- | --------- | ------------ | -------- | --------- | -------- |
| detection. | If there       | is a host | network      | anomaly, |           | we carry |
outnetworktime-consuminganomalydetection.Otherwise,
wecarryoutgeneraltime-consuminganomalydetection.
| According | to the | three | failure | invocation | chain | modes, |
| --------- | ------ | ----- | ------- | ---------- | ----- | ------ |
weproposearootcausenodedetectionalgorithmforfailure
invocationchainasfollows:
| i) We | traverse every   | node | in depth. | If  | there is | a failure |
| ----- | ---------------- | ---- | --------- | --- | -------- | --------- |
| node  | in its subtrees, |      | we change | its | success  | status to |
failure.
| ii) We  | traverse every | node  | in depth | again. | If it  | does not   |
| ------- | -------------- | ----- | -------- | ------ | ------ | ---------- |
| contain | any child      | node, | we       | add it | to the | root cause |
nodecandidateset.Iftherearefailurenodesinitschild
nodes,wedonotaddittotherootcausenodecandidate
set.Wecontinuetotraverseitsfailurenodes’subtrees.
Iftherearenofailurenodesinitschildnodes,weadd
| all | its child nodes | and | all nodes | in  | its subtrees | to the |
| --- | --------------- | --- | --------- | --- | ------------ | ------ |
rootcausenodecandidatesetexceptthenodeitself.
| For general   | time-consuming |     | anomaly    | detection, |          | there are |
| ------------- | -------------- | --- | ---------- | ---------- | -------- | --------- |
| the following | strategies.    | We  | construct  | the        | standard | trees by  |
| the standard  | tree matching  |     | algorithm. | Firstly,   | we       | consider  |
FIGURE2. Flowchartofindicatorsanomalydetection. twodifferentinvocation(A,B,Caredifferentservices,ms=
millisecond):
todetectalltheindicatorsoftheanomalousnodesinthefault It can be seen that the structure of these two invocation
timeperiod.Ifthereisanindicatorwithahigheranomalous
chainsisactuallythesame,sotheirtime-consumingvectors
score and the indicator is also in the candidate set of root shouldbelocatedinthesametime-consumingmatrix.Toper-
causeindicatorsgivenbythecompetitionorganizers,theindi-
| form anomaly | detection | correctly, |     | we expect | elements | in  |
| ------------ | --------- | ---------- | --- | --------- | -------- | --- |
catoristhefinalrootcause.Ifnot,thefaulttypeofthenode eachcolumnofthetime-consumingmatrixtocomefromthe
isnetworkfault. nodes in the same topology location of different invocation
chains,i.e.:
C. ANALYSISOFINVOCATIONCHAINANOMALY Therefore,weneedanalgorithmtorealizenodesmatching
1) ANOMALYDETECTIONSTRATEGYABOUT betweenallinvocationchains.Thenwebrieflyintroducethe
DIFFERENTSITUATIONS standardtreematchingalgorithmtorealizethisrequirement.
The basic framework for anomaly detection of invocation We obtain a standard tree by removing the time-consuming
chainnodesisasfollows: record in the first invocation chain, and assign a number to
When the number of failed invocation chains in the win- eachnodethroughtraversal(depth-firsttraversalorbreadth-
1/3,
dow accounts for more than we carry out anomalous first traversal can be used, breadth-first traversal is used in
VOLUME8,2020 226399

M.Jinetal.:AnomalyDetectionAlgorithmforMSABasedonRPCA
subjectcanstillbecorrectlydetectedingeneralfaultsdueto
therulesi)andii).
2) RPCAALGORITHM
FIGURE4. Thestandardtreegeneratedbystandardtreematching Thebasicprincipleofinvocationchainnodeanomalydetec-
| algorithm.   |                  |     |     |     |          |      |          | tionbasedonRPCAisasfollows. |      |        |           |     |          |                |     |
| ------------ | ---------------- | --- | --- | --- | -------- | ---- | -------- | --------------------------- | ---- | ------ | --------- | --- | -------- | -------------- | --- |
|              |                  |     |     |     |          |      |          | The core                    | idea | of the | algorithm | is  | that for | the invocation |     |
| the specific | implementation). |     |     | The | standard | tree | is shown |                             |      |        |           |     |          |                |     |
chainsinaperiodoftime,weinspectthestandardtreesofthe
inFigure4.
|            |           |          |           |          |     |           |        | invocation         | chains. | We        | calculate    | those | nodes       | of the     | standard |
| ---------- | --------- | -------- | --------- | -------- | --- | --------- | ------ | ------------------ | ------- | --------- | ------------ | ----- | ----------- | ---------- | -------- |
| Invocation | chains    | of       | different | topology |     | structure | corre- |                    |         |           |              |       |             |            |          |
|            |           |          |           |          |     |           |        | tree corresponding |         | to        | the internal | nodes | of each     | invocation |          |
| spond to   | different | standard | trees,    | for      | the | given two | simple |                    |         |           |              |       |             |            |          |
|            |           |          |           |          |     |           |        | chain. Suppose     |         | that each | invocation   |       | chain views |            | the same |
invocation chains in the paper. Due to different subtree nodeasthestartnode,thenthefirstnodeofeachinvocation
| structures,            | the    | two subnodes |         | of node     | A     | are distinguish- |          |           |            |         |               |      |             |      |          |
| ---------------------- | ------ | ------------ | ------- | ----------- | ----- | ---------------- | -------- | --------- | ---------- | ------- | ------------- | ---- | ----------- | ---- | -------- |
|                        |        |              |         |             |       |                  |          | chain can | be thought |         | corresponding |      | to the root | node | of the   |
| able. In               | actual | data, there  | is      | a situation | where | the              | subtrees |           |            |         |               |      |             |      |          |
|                        |        |              |         |             |       |                  |          | standard  | tree.      | By this | means,        | each | node of     | the  | standard |
| are indistinguishable. |        |              | In this | case,       | we    | need to          | perform  |           |            |         |               |      |             |      |          |
treeswouldgetatime-consumingseriesbycalculation.The
| further subtree |     | aggregation, |     | superposition |     | the | same sub- |     |     |     |     |     |     |     |     |
| --------------- | --- | ------------ | --- | ------------- | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
anomalousdegreeoftime-consumingseriesforeachstandard
trees, and record the number of aggregation times for treecanbeinspectedbyRPCAalgorithm.Finally,thealgo-
| the nodes | of  | invocation | chains | to  | ensure | correctness | of  |     |     |     |     |     |     |     |     |
| --------- | --- | ---------- | ------ | --- | ------ | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
rithmwouldreturnthecandidatesetofanomalousnodesand
match.
|                                                  |     |     |     |     |     |     |     | corresponding  |     | anomalous | coefficients |     | in a given | number | of  |
| ------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | --------- | ------------ | --- | ---------- | ------ | --- |
| Whenanewinputinvocationchainisprocessed,itiscom- |     |     |     |     |     |     |     | standardtrees. |     |           |              |     |            |        |     |
paredandmatchedwithallthestandardtreesinthestandard
|     |     |     |     |     |     |     |     | In the | data of | invocation |     | chains, there | is a | condition | that |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | ------- | ---------- | --- | ------------- | ---- | --------- | ---- |
treeset.Ifthereisamatch,weobtainthecorrespondingstan-
|     |     |     |     |     |     |     |     | the same | node | completing |     | the same | call many | times. | For |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ---- | ---------- | --- | -------- | --------- | ------ | --- |
dardtreenodenumberaccordingtothematchingrelationship
|     |     |     |     |     |     |     |     | example, | the service |     | csf_001 | calls local_method_004 |     |     | four |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ----------- | --- | ------- | ---------------------- | --- | --- | ---- |
betweeneachnodeandthestandardtreenode.Weconstruct
|     |     |     |     |     |     |     |     | times and | every | local_method_004 |     | has | carried | on  | the jdbc |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ----- | ---------------- | --- | --- | ------- | --- | -------- |
the vectorized time consuming of invocation chain nodes access to the db_009. For different invocation chains, these
| according          | to the | number  | and | time consuming. |          | After     | getting |                  |      |        |     |                  |       |       |          |
| ------------------ | ------ | ------- | --- | --------------- | -------- | --------- | ------- | ---------------- | ---- | ------ | --- | ---------------- | ----- | ----- | -------- |
|                    |        |         |     |                 |          |           |         | local_method_004 |      | could  | not | be distinguished |       | from  | each     |
| the time-consuming |        | matrix, | we  | use             | the RPCA | algorithm | to      |                  |      |        |     |                  |       |       |          |
|                    |        |         |     |                 |          |           |         | other. Hence,    | it’s | needed | to  | aggregate        | these | nodes | that can |
detecttheanomalyofthetime-consumingmatrix,andobtain
|     |     |     |     |     |     |     |     | not be distinguished |     |     | in the | analysis | of anomaly, |     | then add |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | --- | ------ | -------- | ----------- | --- | -------- |
thesamesizeoftheanomalysubmatrix.Thenweoutputthe
|     |     |     |     |     |     |     |     | up the time | consuming |     | of  | these nodes, | this | operation | is  |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --------- | --- | --- | ------------ | ---- | --------- | --- |
subjectcorrespondingtothetimeanomaly. called as subtree aggregation. In other words, all the same
| For network |     | time-consuming |     | anomaly |     | detection, | there |     |     |     |     |     |     |     |     |
| ----------- | --- | -------------- | --- | ------- | --- | ---------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
subtreesunderthesamenodecouldbeaggregatedasanew
| are the following |           | strategies. | In  | the general |      | time-consuming |         |          |         |     |         |             |     |        |         |
| ----------------- | --------- | ----------- | --- | ----------- | ---- | -------------- | ------- | -------- | ------- | --- | ------- | ----------- | --- | ------ | ------- |
|                   |           |             |     |             |      |                |         | subtree, | whether | the | subtree | is the same | or  | not is | defined |
| anomaly           | detection | strategy,   | the | time        | used | by the         | anomaly |          |         |     |         |             |     |        |         |
undertheaggregationofsubtrees.Inaddition,thedefinitionis
nodesisactuallythesumofthelocaltimeusedbythenode
recursive[13],[34].
and the communication time used between the child nodes. The strategy of the calculation of the candidate sets of
Ifthefaultisaboutthenetworkandoriginatesfromthechild
|            |               |     |               |     |     |      |           | anomalous | nodes | in  | standard | trees | and anomalous |     | coeffi- |
| ---------- | ------------- | --- | ------------- | --- | --- | ---- | --------- | --------- | ----- | --- | -------- | ----- | ------------- | --- | ------- |
| nodes, the | corresponding |     | communication |     |     | time | consuming |           |       |     |          |       |               |     |         |
cientsisasfollows.
| anomaly | will | be reflected | in  | the time | used | by  | its parent |          |          |        |     |           |        |          |      |
| ------- | ---- | ------------ | --- | -------- | ---- | --- | ---------- | -------- | -------- | ------ | --- | --------- | ------ | -------- | ---- |
|         |      |              |     |          |      |     |            | Firstly, | the time | series | of  | each node | in the | standard | tree |
node.Therefore,weassignthetimeusedbythechildnodes
|     |     |     |     |     |     |     |     | is taken | as a column |     | vector | to obtain | the time-consuming |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ----------- | --- | ------ | --------- | ------------------ | --- | --- |
as the sum of the local time used by the parent nodes and matrix.What’smore,thecolumnsoftime-consumingmatrix
| the communication |     | time | used | between | the | child | nodes. It is |                  |     |           |     |              |     |               |     |
| ----------------- | --- | ---- | ---- | ------- | --- | ----- | ------------ | ---------------- | --- | --------- | --- | ------------ | --- | ------------- | --- |
|                   |     |      |      |         |     |       |              | are standardized |     | to ensure | the | adaptability | of  | the algorithm |     |
expectedthatthefaultnodeswillbedetectedcorrectlyincase
|     |     |     |     |     |     |     |     | to data of | different | orders | of  | magnitude. | Then | RPCA | algo- |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --------- | ------ | --- | ---------- | ---- | ---- | ----- |
ofnetworkfailure. rithmwouldbecarriedoutontheprocessedtime-consuming
| For the   | combination |     | of general     | time-consuming |         |     | anomaly    |             |         |           |        |               |       |                  |      |
| --------- | ----------- | --- | -------------- | -------------- | ------- | --- | ---------- | ----------- | ------- | --------- | ------ | ------------- | ----- | ---------------- | ---- |
|           |             |     |                |                |         |     |            | matrix. For | a given | k         | value, | the larger    | first | k characteristic |      |
| detection | and network |     | time-consuming |                | anomaly |     | detection, |             |         |           |        |               |       |                  |      |
|           |             |     |                |                |         |     |            | value would | be      | selected. | For    | each selected |       | principal        | com- |
wecanfindthefollowingrules:
|     |     |     |     |     |     |     |     | ponents, | the absolute |     | value | of the largest | element |     | in linear |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------------ | --- | ----- | -------------- | ------- | --- | --------- |
i) Theshallowertheanomaloustimeis,themoreobvious transformation weight vector corresponding to the nodes as
| itis.   |         |       |       |              |     |              |      | themaincomponentofthecorrespondingnode.Theanoma- |     |     |     |     |     |     |     |
| ------- | ------- | ----- | ----- | ------------ | --- | ------------ | ---- | ------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- |
| ii) The | subject | often | has a | parent-child |     | relationship | with |                                                  |     |     |     |     |     |     |     |
louscoefficientsofthenodesaredefinedascharacteristicsof
| itself. |         |         |          |     |           |     |           | principlecomponentsmultipliedbythenodeweightscorre- |     |     |     |     |     |     |     |
| ------- | ------- | ------- | -------- | --- | --------- | --- | --------- | --------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
| iii) In | case of | network | failure, | the | anomalous |     | time con- |                                                     |     |     |     |     |     |     |     |
spondingtotheweightvectorsinprinciplecomponentlinear
| sumption |     | is reflected | in  | the | last node | of  | the failure | transformation.                                   |     |     |     |     |     |     |     |
| -------- | --- | ------------ | --- | --- | --------- | --- | ----------- | ------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
| subject. |     |              |     |     |           |     |             | ThebriefintroductionsofRPCAalgorithmareasfollows. |     |     |     |     |     |     |     |
Therefore,ifthetimeusedbythechildnodeistakenasthe RPCAalgorithm:RPCA(robustprincipalcomponentanal-
sumofthetimeusedbytheparentnodeandcommunication ysis) is essentially a problem of finding the best projection
timeforbothgeneralfaultsandnetworkfaults,theanomalous of data in low dimensional space like the classical PCA
| 226400 |     |     |     |     |     |     |     |     |     |     |     |     |     | VOLUME8,2020 |     |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- |

M.Jinetal.:AnomalyDetectionAlgorithmforMSABasedonRPCA
algorithm[33]. When the observation data is large enough, thedatainfeatureextraction.
| PCA algorithm |     | can not | give | ideal | results, | while | RPCA |     |     |     |     |     |     |     |     |
| ------------- | --- | ------- | ---- | ----- | -------- | ----- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |

|     |     |     |     |     |     |     |     |     |     | y ( 1 ) = | x , |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- |
a l g o r i t h m c a n r e c o v e r t h e d a t a w i t h e s s e n t i a l l y l o w r a n k  i
i
f r o m t h e l a r g e a n d s p a r s e n o i s e p o l l u t e d o b s e r v a t i o n d a t a . y ( 2 ) = x − x ,
|     |     |     |     |     |     |     |     |     |     | i   | i i − | 1   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- |
R P C A a lg o r i t h m c o n s i d e r s s u c h a p r o b l e m : T h e g e n e r a l d a t a y ( 3 ) = x − 2 x + x ,
|               |         |               |             |              |               |           |             |     |     | i         | i       | i − 1 | i − 2 |     |     |
| ------------- | ------- | ------------- | ----------- | ------------ | ------------- | --------- | ----------- | --- | --- | --------- | ------- | ----- | ----- | --- | --- |
| m a t r i x D | c o n t | a i n s b o t | h s t r u c | t u ra l i n | f o r m a t i | o n a n d | n o i s e . |     |     |           |         |       |       |     |     |
|               |         |               |             |              |               |           |             |     |     | y ( 4 ) = | x − 3 x | + 3   | x +x  | ,   |     |
T h e n t h e m a t r i x c a n b e d e c o m p o s e d i n t o t w o m a t r i c e s a n d i i i − 1 i− 2 i−3
|     |     |     |     |     |     |     |     |     |     |     | 1 i |     |     |     | (4) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
a d d e d : D = A + E , A i s l o w r a n k ( d u e t o t h e i n t e r n a l ( 5 ) (cid:88) ,
|     |     |     |     |     |     |     |     |     |  | y = |     | x j |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | --- | --- | --- | --- | --- |
s t r u c t u r e i n fo r m a t i o n , t h e r e i s a l i n e a r c o r r e l a t i o n b e t w e e n i m
= i−
j m
r o w s o r c o lu m n s ) , E i s s p a r s e (i f t h e r e i s n o i s e , i t i s s p a r s e ) , (cid:118)
|     |     |     |     |     |     |     |     |     |     |     | (cid:117) | i   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- |
t h e n R P C A a l g o r i t h m c a n b e w ri t t e n a s t h e f o l l o w i n g o p t i - ( 6 ) (cid:117) 1 (cid:88) ( 5)
|     |     |     |     |     |     |     |     |     |     | y = | (cid:116) | (x −y | )2, |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | ----- | --- | --- | --- |
m i z a t i o n p r o b l e m [ 3 4 ] – [ 3 7 ] , i . e . : i m j i
j=i−m

|     |     |     |     |     |     |     |     |     | ,   |     | m,i |     | 1,...,i |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | --- |
min rank(A)+λ||E|| , where x j j = i − − m + represent the KPI
|     |       | A,E |     |     | 0   |     |     |      |              |        |     |               |     |            |       |
| --- | ----- | --- | --- | --- | --- | --- | --- | ---- | ------------ | ------ | --- | ------------- | --- | ---------- | ----- |
|     |       |     |     |     |     |     | (1) | data | five minutes | before | the | corresponding |     | time point | of x, |
|     | s.t. |     | =D. |     |     |     |     |      |              |        |     |               |     |            | i     |
A+E
andmrepresentstheamountofdatafiveminutesbeforethe
|     |     |     |     |     |     |     |     | correspondingtimepointt |     |     |     | ofx. |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------------- | --- | --- | --- | ---- | --- | --- | --- |
i i
| Since rank | and | L norm | have | non | convex | and | non |     |     |     |     |     |     |     |     |
| ---------- | --- | ------ | ---- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
0
smooth properties, this NP problem is generally trans- 2) SLIALGORITHM
| formed | into | solving | a relaxed |     | convex | optimization |     |          |     |         |           |     |                 |           |     |
| ------ | ---- | ------- | --------- | --- | ------ | ------------ | --- | -------- | --- | ------- | --------- | --- | --------------- | --------- | --- |
|        |      |         |           |     |        |              |     | Firstly, | we  | briefly | introduce | the | four algorithms | Isolation |     |
problem:
|     |     |     |     |     |     |     |     | Forest,One-ClassSVM,LOFalgorithmand3σ |     |     |     |     |     | principleas |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------- | --- | --- | --- | --- | --- | ----------- | --- |
follows.

|     |     | min | ||A|| ∗ +λ||E|| |     | ,   |     |     |     |     |     |     |     |     |     |     |
| --- | --- | ---- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     | A,E  |                 | 1   |     |     |     |     |     |     |     |     |     |     |     |
(2)
|     |     | s.t. |     | =D. |     |     |     | a: ISOLATIONFOREST |     |     |     |     |     |     |     |
| --- | --- | ----- | --- | --- | --- | --- | --- | ------------------ | --- | --- | --- | --- | --- | --- | --- |
A+E
|     |     |     |     |     |     |     |     | In an | isolated   | forest, | an anomaly |                | is defined | as more | likely |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | ---------- | ------- | ---------- | -------------- | ---------- | ------- | ------ |
|     |     |     |     |     |     |     |     | to be | separated, | which   | is         | understandable | as         | a point | thinly |
D. INDICATORSANOMALYDETECTION
|     |     |     |     |     |     |     |     | distributed |     | and far | from a | dense | population. | In an isolated |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ------- | ------ | ----- | ----------- | -------------- | --- |
In this section, we would like to introduce our single indi- forest,thedatasetisrecursivelyrandomlydivideduntilallthe
| cator anomaly |     | detection | algorithm | in  | detail. | The algorithm |     |     |     |     |     |     |     |     |     |
| ------------- | --- | --------- | --------- | --- | ------- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
samplepointsareisolated.Underthisrandomsegmentation
| is composed | of  | two parts: | The | first | part is | Features | Min- |     |     |     |     |     |     |     |     |
| ----------- | --- | ---------- | --- | ----- | ------- | -------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
strategy,theanomalouspointwhaveashortpathusuallyand
ing Method and the second part is SLI Algorithm, which wedefineL(w)=1[39].Otherwise,wedefineL(w)=0.
| ingrates | One-Class | Support | Vector | Machine, |     | Local | Outlier |     |     |     |     |     |     |     |     |
| -------- | --------- | ------- | ------ | -------- | --- | ----- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
3σ
| Factor algorithm, |           | Isolation | Forest  | algorithm, |                    | and | prin- |                 |     |     |     |     |     |     |     |
| ----------------- | --------- | --------- | ------- | ---------- | ------------------ | --- | ----- | --------------- | --- | --- | --- | --- | --- | --- | --- |
|                   |           |           |         |            |                    |     |       | b: ONE-CLASSSVM |     |     |     |     |     |     |     |
| ciple. SLI        | algorithm | can       | combine | with       | the aforementioned |     |       |                 |     |     |     |     |     |     |     |
Itisassumedthattheparametersofthegeneratedhypersphere
featuresminingmethodandmakefulluseoftheadvantages
|     |     |     |     |     |     |     |     | arecentercandthecorrespondinghypersphereradiusr |     |     |     |     |     |     | >0, |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
3σ
| of IF algorithm, |     | One-Class | SVM, | LOF | algorithm |     | and |     |     |     |     |     |     |     |     |
| ---------------- | --- | --------- | ---- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
thevolumeofthehypersphereF(r)isminimizedandcenterc
principle.
isalinearcombinationofthelinesthataresupported.Similar
tothetraditionalSVMmethod,thedistancebetweenalltrain-
1) FEATURESMININGMETHOD ingdatapointsy andthecentercanberequiredtobestrictly
i
In order to eliminate the influence of dimension and ensure lessthanr.Butforbetterperformance,penaltycoefficientD
that the scale of data change is not lost, we first use the ϑ
|     |     |     |     |     |     |     |     | of the | relaxation | variable |     | is constructed | [40], | [41]. | Thus, |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | ---------- | -------- | --- | -------------- | ----- | ----- | ----- |
Max method to normalize KPI data of the anomalous node theoptimizationproblemcanbewrittenasfollows,i.e.,
asfollow,i.e.,
|     |     |     |     |     |     |     |     |     |    |     | n   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(cid:88)
|     |     |     |     |     |     |     |     |     |  m i | nF(r)+ | ϑ     | ,     |               |           |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------ | ----- | ----- | ------------- | --------- | --- |
|     |     |     | X   | i   |     |     |     |     |           |        | i     |       |               |           |     |
|     |     |     | x = | ,   |     |     | (3) |     | r, o      |        |       |       |               |           |     |
|     |     |     | i X |     |     |     |     |     |           |        | j=1   |       |               |           |     |
|     |     |     |     | max |     |     |     |     |           |        |       |       |               |           | (5) |
|     |     |     |     |     |     |     |     |     | | |y      | − c || | ≤r +ϑ | , i = | 1 , 2 , 3 , . | . . , n , |     |
|     |     |     |     |     |     |     |     |     |      | i 2    |       | i     |               |           |     |
whereX =(X ,X ,...,X )representsaKPIvector,X = ϑ ≥ 0 , i = 1 , 2 , 3 , . . . , n .
|          | 1      | 2    | n      |           |     |         | max  |     | i   |     |     |     |     |     |     |
| -------- | ------ | ---- | ------ | --------- | --- | ------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
| max{X ,X | ,...,X | }, n | is the | dimension | of  | the KPI | vec- |     |     |     |     |     |     |     |     |
| 1        | 2      | n    |        |           |     |         |      |     |     |     |     |     |     |     |     |
tor X. In order to make full use of the information in the Next,weuseLagrangedualtosolvetheaboveoptimization
indicator data, six features [38] of the normalized KPI data problem(5).Forthenewdatapointp,ifthedistancefromp
| =   | ,x ,...,x |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
x (x 1 2 n ) are mined as input data for the subse- to the center is less than or equal to the radius r, it’s not an
quentanomalydetectionalgorithm(SLIAlgorithm).Differ- anomalous point and we define L(p) = 0, otherwise it’s an
entfrom[38],weconsiderbothlocalandglobalfeaturesof anomalouspointandwedefineL(p)=1.
| VOLUME8,2020 |     |     |     |     |     |     |     |     |     |     |     |     |     |     | 226401 |
| ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |

M.Jinetal.:AnomalyDetectionAlgorithmforMSABasedonRPCA
c: LOFALGORITHM X represents the data before the anomalous time period
train
ofthecorrespondingindicator.
TherelevantexpressionsoftheLOFalgorithmaredefinedas
|               |     |                |     |     |     |     |              |           |          |                               |     |          |        | ,U ,    |
| ------------- | --- | -------------- | --- | --- | --- | --- | ------------ | --------- | -------- | ----------------------------- | --- | -------- | ------ | ------- |
| follows,i.e., |     |                |     |     |     |     | When         | we verify | the      | algorithm,                    | we  | input    | U =    | [U      |
|               |     |                |     |     |     |     |              |           |          |                               |     |          |        | 1 2     |
|               |     |                |     |     |     |     | U ,U ,U      | ,U        | ],whereU | representsthedataobtainedfrom |     |          |        |         |
|               |     | d(w,a)=||w−a|| |     |     | ,   |     | 3 4          | 5 6       |          |                               |     |          |        |         |
|               |     |                |     |     | 2   | (6) |              |           |          |                               |     |          |        |         |
|               |     |                |     |     |     |     | the original | data      | X test   | through                       | the | features | mining | method. |
where d(w,a) represents the distance from w to a. What’s X isanindicatordataoftheanomalousnodeintheanoma-
test
lousperiod.
more,d k (w)isdefinedasthek-distanceofw.Thatistosay
| d (w)representsthedistancefromthekthmostdistantpoint |     |     |     |     |     |     | OUTPUT: |     |     |     |     |     |     |     |
| ---------------------------------------------------- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
k
|            |     |               |     |                            |     |     | The anomalous |     | score | S   | = q | /q of | the indicator | in  |
| ---------- | --- | ------------- | --- | -------------------------- | --- | --- | ------------- | --- | ----- | --- | --- | ----- | ------------- | --- |
| ofwtowandk |     | isaconstant.O |     | k (w)isdefinedask-distance |     |     |               |     |       |     | ab  | all   |               |     |
neighborhoodofw,whichrepresentsthesetofallthepoints the anomalous period, where q all represents the amount of
whicharelessthand (w)awayfromw.dr isdefinedasthe indicatordataoftheanomalousnodeintheanomalousperiod,
k
q representsthenumberofanomalousdatapointsdetected
| kthreach-distancefrompointwtopointa,whichsatisfiesthe |       |             |     |                |     |     | ab                 |     |          |         |           |     |               |     |
| ----------------------------------------------------- | ----- | ----------- | --- | -------------- | --- | --- | ------------------ | --- | -------- | ------- | --------- | --- | ------------- | --- |
| followingexpression[42].                              |       |             |     |                |     |     | bytheSLIalgorithm. |     |          |         |           |     |               |     |
|                                                       |       |             |     |                |     |     | The whole          |     | steps of | the SLI | algorithm |     | are described | as  |
|                                                       |       | (w,a)=max(k |     | −d(w),d(w,a)). |     |     |                    |     |          |         |           |     |               |     |
|                                                       | dr −d | k           |     |                |     | (7) |                    |     |          |         |           |     |               |     |
follows.
Furthermore, the local reachability density is defined as Step1:NormalizeKPIdataoftheanomalousnodebythe
Maxmethod.
follows,i.e.,
Step2:Usefeaturesminingmethodtoextractthefeatures
|O k (w)|
|     | dl  | (w)= |          |     | .     | (8) | ofnormalizedKPIdata. |     |     |     |     |     |     |     |
| --- | --- | ---- | -------- | --- | ----- | --- | -------------------- | --- | --- | --- | --- | --- | --- | --- |
|     |     | k    | (cid:80) | −d  | (w,a) |     |                      |     |     |     |     |     |     |     |
a∈Ok(w) dr k Step3:UsetrainingdatatotraintheIsolationForest,One-
ClassSVM,LOFalgorithmand3σ
| Thelocaloutlierfactorisdefinedasfollows,i.e., |     |     |     |     |     |     |     |     |     |     |     | principle. |     |     |
| --------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- |
Step4:Usefourmodelstrainedinstep3todetectthedata
|     |     | (cid:80) | dlk(a) | (cid:80) | dlk(a)  |     |     |     |     |     |     |     |     |     |
| --- | --- | -------- | ------ | -------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     | a∈Ok(w)  |        |          | a∈Ok(w) |     |     |     |     |     |     |     |     |     |
lof (w)= dlk(w) = dlk(w). (9) ofanomaloussubjectsinanomaloustimeperiod.
k
|O (w)| |O (w)|dl (w) Step5:CalculateN(x ) = L (x )+L (x )+L (x )+
|     |     |     | k   |     | k k |     |       |          |     | i       | if i  | svm  | i     | lof i  |
| --- | --- | --- | --- | --- | --- | --- | ----- | -------- | --- | ------- | ----- | ---- | ----- | ------ |
|     |     |     |     |     |     |     | 2L (x | ), where | L   | (x ), L | (x ), | L (x | ) and | L (x ) |
For LOF algorithm, if the lof (w) is less than 1, it means sigma i if i svm i lof i sigma i
k
that the density of w is higher than the density of its neigh- represent the label value of x i obtained by Isolation Forest
|         |         |     |          |        |           |           | algorithm,One-ClassSVM,LOFalgorithmand3σ |     |               |     |     |         |     | principle |
| ------- | ------- | --- | -------- | ------ | --------- | --------- | ---------------------------------------- | --- | ------------- | --- | --- | ------- | --- | --------- |
| borhood | points, | and | w is the | normal | point and | we define |                                          |     |               |     |     |         |     |           |
|         |         |     |          |        |           |           |                                          |     | )>3,wetakeL(x |     |     | )=1andx |     |           |
L(w) = 0. If the lof (w) is greater than 1, it means that respectively.IfN(x i i i isjudged
k
thedensityofwislessthanthedensityofitsneighborhood asananomalouspoint.
Step6:CalculatetheanomalousscoreSoftheindicatorin
points,andthemorelikelythatwistheanomalouspointand
| andwedefineL(w)=1. |           |     |     |     |     |     | theanomalousperiod.              |        |      |     |        |                   |     |        |
| ------------------ | --------- | --- | --- | --- | --- | --- | -------------------------------- | ------ | ---- | --- | ------ | ----------------- | --- | ------ |
| d: 3σ              | PRINCIPLE |     |     |     |     |     | III. EXPERIMENTANDRESULTANALYSIS |        |      |     |        |                   |     |        |
|                    |           |     |     |     |     |     | This section                     | mainly | aims | to  | verify | the effectiveness |     | of our |
Wedefine
|     |     |     |      |        |     |      | algorithm | framework. |     | In this | section, | firstly, | we  | select the |
| --- | --- | --- | ---- | ------ | --- | ---- | --------- | ---------- | --- | ------- | -------- | -------- | --- | ---------- |
|     |     |     | x    | −x     |     |      |           |            |     |         |          |          |     |            |
|     |     | v   | =| i | mean|, |     | (10) |           |            |     |         |          |          |     |            |
i sample data and the first three batches of test data of the
x std
|     |     |     |     |     |     |     | 2020 International |     | AIOps | Challenge |     | to evaluate |     | our algo- |
| --- | --- | --- | --- | --- | --- | --- | ------------------ | --- | ----- | --------- | --- | ----------- | --- | --------- |
,x ,...,x
where x i represents the ith data point, x = [x 1 2 n ], rithm.Secondly,wecomparetherootcauseanalysisresults
|     | (cid:80)nx/n |     |     | (cid:2)(cid:80)n |     | )2/n (cid:3)1/2. |     |     |     |     |     |     |     |     |
| --- | ------------ | --- | --- | ---------------- | --- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- |
x = i and x = (x −x of IF, LOF and One-Class SVM algorithm with our algo-
| mean |     | i   | std | i=1 | i   | mean |     |     |     |     |     |     |     |     |
| ---- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
If v > 3, x can be viewed as an anomalous point and we rithm. Finally, we analyze the results of our algorithm in
| i   |     | i   |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
defineL(w)=1.Otherwise,wedefineL(w)=0.
detail.
Secondly,AdetaileddescriptionoftheSLIalgorithmisas
| follows,i.e., |     |     |     |     |     |     | A. PERFORMANCEOFOURALGORITHM |     |     |     |     |     |     |     |
| ------------- | --- | --- | --- | --- | --- | --- | ---------------------------- | --- | --- | --- | --- | --- | --- | --- |
INPUT: Firstly, we should read the file containing all invocation
Whentrainingthemodel,weinputT =[T ,T ,T ,T ,T , chaininformationgivenbythecompetitionorganizers.Then,
|     |     |     |     |     | 1   | 2 3 4 5 |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
T 6 ]and we define the invoking relationship and establish complete
|     |     |      |                       |     |     |     | invocationchainsaccordingtothreereservedfields‘id’,‘tra- |     |     |     |     |     |     |     |
| --- | --- | ----- | --------------------- | --- | --- | --- | -------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
|     |     | T =[y | (1),y (1),...,y(1)]T, |     |     |     |                                                          |     |     |     |     |     |     |     |
 1 1 2 n c e id ’ , an d ‘ p id ’ of th e fi l e . B e c a u s e t h e c o m p l e t e i n v o k i n g
|     |     |     | ( 2 ) ( | 2 )           |           |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | ------- | ------------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     | T = | [ y , y | , . . . , y ( | 2 ) ] T , |     |     |     |     |     |     |     |     |     |
2 1 2 n t o p o l o g y d i a g r a m i s to o l a r g e , p a r t o f t h e c o m p l e t e i n v o k i ng
|     |     |     | ( 3 ) ( | 3 ) |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
T = [ y , y , . . . , y ( 3 ) ] T , t o p o l o g y d i a g r a m i s s h o w n in F i g u r e 5 .
|     |     | 3   | 1 2       | n               |         | (11) |     |     |     |     |     |     |     |     |
| --- | --- | --- | --------- | --------------- | ------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     | ( 4 ) , ( | 4 ) , . . . , ( | 4 ) T , |      |     |     |     |     |     |     |     |     |
 T = [ y y y ] A n o m a l i e s a r e u s u a l l y o b s e r v e d i n s e v e r a l m o n i to r i n g i n d i -
|     |     | 4   | 1 2 | n   |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
( 5 ) , ( 5 ) , . . . , ( 5 ) T , c at o r s . F o r m i c ro s e r v i c e s , r e s p o n s e a n d l a t e n cy t i m e s a r e
|     |     | T 5 = | [ y y | y   | ]   |     |     |     |     |     |     |     |     |     |
| --- | --- | ----- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
1 2 n im p o r ta n t k e y p e r f o r m a n c e i n d i c a to r s ( K P I s ). W e e x t r a c t
|     |     | =   | ( 6 ) , ( | 6 ) , . . . , ( | 6 ) T , |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --------- | --------------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     | T 6 | [ y y     | y               | ]       |     |     |     |     |     |     |     |     |     |
1 2 n more static attributes or KPIs from other subjects, such as
where T represents the data obtained from the original CPU memory usage, container memory usage and cache-
| training | data | X train | through | the features | mining | method. | relatedKPIs. |     |     |     |     |     |              |     |
| -------- | ---- | ------- | ------- | ------------ | ------ | ------- | ------------ | --- | --- | --- | --- | --- | ------------ | --- |
| 226402   |      |         |         |              |        |         |              |     |     |     |     |     | VOLUME8,2020 |     |

M.Jinetal.:AnomalyDetectionAlgorithmforMSABasedonRPCA
FIGURE6. Averageresponsetimeforbusinessindicatordata.Thetime
nodeswherethefaultperiodbeginsismarkedinred.
TABLE3. 11faultsofthesampledata.
FIGURE5. Invokingrelationshiptopologydiagram.
TABLE2. MainmonitoringKPIs.
Inthepreliminarystageofthiscompetition,thecompeti-
tionorganizersinjectthefaultintothetargetenvironmentby
manualinjection,andthedurationoftheinjectionis6hours
TABLE4. Partialapplicationdeploymentarchitecturelist.
(from 0:00 a.m. to 6:00 a.m. every day). Since different
technology stacks have different indicators and the number
ofeffectiveindicatorsreachesmorethan100,alargenumber
of resources and costs will be wasted if all of them are
detected. By testing, some specific KPIs are collected as
showninTable2.
Throughthetestandanalysisofthesampledatagivenby
the competition organizers, we filter hundreds of KPI data,
and finally get some important KPI data shown in Table 2.
These KPI data has an obvious data fluctuation in the time We debug our algorithm with the sample data. Firstly,
period of failure, which facilitates our anomaly detection anomalous nodes of 10 out of 11 faults are located by
algorithm to identify the specific fault container. We sim- our invocation chain anomaly analysis algorithm based on
plify the set of root cause indicators to effectively reduce RPCAalgorithm.Then,specificfaultnodesofcorresponding
the computational complexity of anomaly detection algo- anomalouscontainerscouldalsobeverifiedaccuratelybyour
rithm and improve the overall efficiency of the algorithm, singleindicatoranomalydetectionalgorithm.Bycomparing
tomoreaccuratelylocatethespecificanomalousindicators. the output candidate set of root cause and the file of fault
We eliminate some KPI data which change little with time, contentgivenbythecompetitionorganizers,thetoptworoot
and use certain prior knowledge to simplify the detection causeslocatedbyouralgorithmcouldhittherealrootcause.
complexity. Accordingtotable3,itcanbeseenthatforthedetectedfaults
The fault time information of the sample data has been of two anomalous nodes, take the first fault as an example.
providedbythecompetitionorganizers,whichisconvenient Because docker_003 is deployed on os_019, the invocation
for the teams to debug their own algorithm. From Figure 6, chain detection algorithm would get two anomalous nodes,
weseethatduringthefaultperiod(5minutes),thevalueof i.e., the anomalous node itself and its deployed principle.
KPIcurveofbusinessindicatorswillfluctuatesignificantly, Throughtheexperimentofthesampledata,itcanbeseenthat
and accordingly, some indicators related to the underlying ouralgorithmhasahigheraccuracytosomeextent.Table4
serviceswillbeanomalousduringthisperiodoftime. showsapartialapplicationdeploymentarchitecturelist.
VOLUME8,2020 226403

M.Jinetal.:AnomalyDetectionAlgorithmforMSABasedonRPCA
TABLE5. 11faultsofthefirstbatchoftestdata. TABLE7. 11faultsofthethirdbatchoftestdata.
TABLE6. 13faultsofthesecondbatchoftestdata.
FIGURE7. KPIcurvescorrespondingtoanomalousnodesdetectedinthe
faulttimeperiodexceptnetworkfaultofsampledata.Greenlinesshow
normaltimeperiods.Yellowlinesshowanomaloustimeperiods.The
anomalouspointsdetectedbyourindicatoranomalydetectionalgorithm
aremarkedinred.
actually is fly remote according to application deployment
architecture list given by competition organizers. The spe-
cific reason is that the complete set of faults given by the
competitionorganizersdoesnotincludefaultsofflyremote.
Bymanuallyviewingthefailedinvocationchaininformation
Thesampledataofthiscompetitionhasgiventhespecific and the KPI curves of the anomalous indicators, we could
anomalousnodesandcorrespondingindicatorswhenthefault lockthelocationofanomalousnodeasflyremote_001.
occurs.Then,weselectthefirstthreebatchesoftestdatato Figures7-10showKPIcurvescorrespondingtoanomalous
test our algorithm. The test data only gives the time point nodesdetectedinthefaulttimeperiodexceptnetworkfault
wherethefaultoccurs,andcontestantsdonotneedtocarry of the first three batches of test data. From our root cause
out anomaly detection on the esb indicator. The given time location strategy mentioned in Section II, we can see that
pointstothetimestamparetakenastheinputofouralgorithm there is no corresponding anomalous indicator of network
togetthefinalanomalousnodesandcorrespondinganoma- fault. If the anomalous node is docker, it is generally the
lousindicators,asshowninTables5–7. CPUfaultandthevalueoftheindicator‘container_cpu_used’
According to Table 5, we consider the 4th fault in the is usually around 90, for example, Figure 7(a) and 8(a).
firstbatchoftestdata.Theactualfaultislocatedonos_009, Iftheanomalyisdb,therearegenerallytwotypesoffaults:
226404 VOLUME8,2020

M.Jinetal.:AnomalyDetectionAlgorithmforMSABasedonRPCA
FIGURE8. KPIcurvescorrespondingtoanomalousnodesdetectedinthe
faulttimeperiodexceptnetworkfaultofthefirstbatchoftestdata.
Greenlinesshownormaltimeperiods.Yellowlinesshowanomalous FIGURE10. KPIcurvescorrespondingtoanomalousnodesdetectedin
timeperiods.Theanomalouspointsdetectedbyourindicatoranomaly thefaulttimeperiodexceptnetworkfaultofthethirdbatchoftestdata.
detectionalgorithmaremarkedinred. Greenlinesshownormaltimeperiods.Yellowlinesshowanomalous
timeperiods.Theanomalouspointsdetectedbyourindicatoranomaly
detectionalgorithmaremarkedinred.
TABLE8. Comparativeresultsofdifferentalgorithms.
B. PERFORMANCEOFDIFFERENTALGORITHMS
Table8showsthecomparisonresultsonthesampledataand
thefirstthreebatchesofdataofthe2020InternationalAIOps
Challengeusingdifferentalgorithms.Wetransformthefault
timegivenbyeachbatchofdataintothecorrespondingtimes-
tamp as the input. We obtain the final root cause indicator
score by indicator anomaly detection with four algorithms,
IFalgorithm,LOFalgorithm,One-ClassSVMalgorithmand
our algorithm. And our indicator anomaly detection algo-
rithmisthecombinationofvotingscoresofthreealgorithms
IF, LOF, and One-Class SVM. Besides, the final scoring
rulesoftherootcauseindicatorareconsistentwiththerules
of this International AIOps Challenge, i.e., if the first root
FIGURE9. KPIcurvescorrespondingtoanomalousnodesdetectedinthe cause indicator is correct, we get 1 point, if the second
faulttimeperiodexceptnetworkfaultofthesecondbatchoftestdata. root cause indicator is correct, we get 0.2 point, if there is
Greenlinesshownormaltimeperiods.Yellowlinesshowanomalous
timeperiods.Theanomalouspointsdetectedbyourindicatoranomaly no root cause indicator is correct, we get 0 point. The total
detectionalgorithmaremarkedinred. scoreofrootcauseindicatorsdividedbytheamountoffaults
isthefinalrootcauseindicatorscore.
database connection limit and database off monitoring. For ComparedwithIFalgorithm(Theaveragescoreofthefour
theformer,theindicator‘Sess_Connection’woulddroptoa batchesofdatais0.6784),LOFalgorithm(Theaveragescore
very low value, for example, Figure 7(c) and 8(b). For the of the four batches of data is 0.5657), and One-Class SVM
latter,theindicator‘On_Off_State’wouldchangefrom1to algorithm (The average score of the four batches of data is
0, for example, Figure 7(f) and 9(c). If the anomaly is os, 0.5913),ouralgorithm(Theaveragescoreofthefourbatches
thevaluesofindicators‘Sent_queue’and‘Received_queue’ of data is 0.8304) has a higher score, which indicates our
would increase sharply, and the indicator ‘Received_queue’ single indicator algorithm including three algorithms has a
wouldshowacertainlag,forexample,Figure8(c)and9(b). betterrootcauselocationeffect.
VOLUME8,2020 226405

M.Jinetal.:AnomalyDetectionAlgorithmforMSABasedonRPCA
IV. CONCLUSION [10] X.Nie,Y.Zhao,K.Sui,D.Pei,Y.Chen,andX.Qu,‘‘Miningcausality
Inthispaper,weproposearootcauselocationmethodbased graphforautomaticWeb-basedservicediagnosis,’’inProc.IEEE35thInt.
Perform.Comput.Commun.Conf.(IPCCC),Dec.2016,pp.1–8.
| on execution | trace      | for | MSA.       | Firstly, | we describe |        | the exe- |                                                                   |     |     |     |     |     |
| ------------ | ---------- | --- | ---------- | -------- | ----------- | ------ | -------- | ----------------------------------------------------------------- | --- | --- | --- | --- | --- |
|              |            |     |            |          |             |        |          | [11] L.Meng,Y.Sun,andS.Zhang,‘‘Midiag:Asequentialtrace-basedfault |     |     |     |     |     |
| cution trace | of request |     | processing | by       | invocation  | trees, | and      |                                                                   |     |     |     |     |     |
diagnosisframeworkformicroservices,’’inProc.17thInt.Conf.Services
Comput.(SCC),Honolulu,HI,USA,Sep.2020,pp.137–144.
| construct | a standard | tree  | library | by      | using          | the standard | tree   |                                                                |     |     |     |     |     |
| --------- | ---------- | ----- | ------- | ------- | -------------- | ------------ | ------ | -------------------------------------------------------------- | --- | --- | --- | --- | --- |
|           |            |       |         |         |                |              |        | [12] J.Xu,Y.Wang,P.Chen,andP.Wang,‘‘Lightweightandadaptiveser- |     |     |     |     |     |
| matching  | algorithm. | Then, | we      | extract | the invocation |              | chains |                                                                |     |     |     |     |     |
viceAPIperformancemonitoringinhighlydynamiccloudenvironment,’’
intheperiodofpartialexecutiontracefailuretomatchwith
inProc.IEEEInt.Conf.ServicesComput.(SCC),Honolulu,HI,USA,
the standard tree library, and vectorize the time-consuming Jun.2017,pp.35–43.
matrixofthestandardtreenodestobuildananomaloustime- [13] P.-S. Huang, S. D. Chen, P. Smaragdis, and M. Hasegawa-Johnson,
‘‘Singing-voiceseparationfrommonauralrecordingsusingrobustprinci-
consuming matrix. We use RPCA algorithm to analyze the palcomponentanalysis,’’inProc.IEEEInt.Conf.Acoust.,SpeechSignal
anomalous time-consuming matrix, and the single indicator Process.(ICASSP),Mar.2012,pp.57–60.
anomalydetectionalgorithmtolocatetherootcauses.Finally [14] P. Wang, J. Xu, M. Ma, W. Lin, D. Pan, Y. Wang, and P. Chen,
|           |       |           |           |     |         |              |     | ‘‘CloudRanger: | Root cause | identification | for cloud | native | systems,’’ in |
| --------- | ----- | --------- | --------- | --- | ------- | ------------ | --- | -------------- | ---------- | -------------- | --------- | ------ | ------------- |
| we output | nodes | with high | anomalous |     | scores. | Experimental |     |                |            |                |           |        |               |
Proc.18thIEEE/ACMInt.Symp.Cluster,CloudGridComput.(CCGRID),
resultsshowthattheproposedalgorithmrankstherootcauses May2018,pp.492–502.
|     |     |     |     |     |     |     |     | [15] J.Lin,P.Chen,andZ.Zhang,‘‘Microscope:Pinpointperformanceissues |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------------------------- | --- | --- | --- | --- | --- |
inthetoptwowithover90%precisionforgivensampledata
|     |     |     |     |     |     |     |     | with causal | graphs in micro-service |     | environments,’’ | in  | Proc. 16th Int. |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ----------------------- | --- | --------------- | --- | --------------- |
andtestdata,whichverifytheeffectivenessoftheproposed
Conf.Service-OrientedComput.(ICSOC),Hangzhou,China,Nov.2018,
algorithm.
pp.3–20.
At present, this method still has the following problems [16] P.Chen,Y.Qi,andD.Hou,‘‘CauseInfer:Automatedend-to-endperfor-
mancediagnosiswithhierarchicalcausalitygraphincloudenvironment,’’
| to be improved: |     | Firstly, | the root | cause | location | of  | offline |     |     |     |     |     |     |
| --------------- | --- | -------- | -------- | ----- | -------- | --- | ------- | --- | --- | --- | --- | --- | --- |
IEEETrans.ServicesComput.,vol.12,no.2,pp.214–230,Mar.2019.
dataisbasedontheconditionthatthecompetitionorganizers
|     |     |     |     |     |     |     |     | [17] P.Chen,Y.Qi,P.Zheng,andD.Hou,‘‘CauseInfer:Automaticanddis- |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------------------------------------------------------- | --- | --- | --- | --- | --- |
have given the specific time nodes of fault occurrence. Our tributedperformancediagnosiswithhierarchicalcausalitygraphinlarge
next work is to explore some effective anomaly detection distributed systems,’’ in Proc. IEEE Conf. Comput. Commun. (INFO-
COM),Toronto,ON,Canada,Apr.2014,pp.1887–1895.
algorithms for esb indicators; Secondly, our algorithm only [18] M.Ma,J.Xu,Y.Wang,P.Chen,Z.Zhang,andP.Wang,‘‘AutoMAP:
performswellforofflinedata.Tosuccessfullyapplyouralgo- Diagnose your microservice-based Web applications automatically,’’ in
rithmtoonlinedata,wetrytouseKafkatoacceptstreaming Proc.WebConf.,Apr.2020,pp.246–258.
|           |           |           |     |          |         |     |          | [19] H. Yan, | L. Breslau, Z.       | Ge, D. Massey, | D.           | Pei, and | J. Yates, ‘‘G- |
| --------- | --------- | --------- | --- | -------- | ------- | --- | -------- | ------------ | -------------------- | -------------- | ------------ | -------- | -------------- |
| data from | the cloud | services. |     | After we | convert | the | received |              |                      |                |              |          |                |
|           |           |           |     |          |         |     |          | RCA:         | A generic root cause | analysis       | platform for | service  | quality man-   |
streaming data into the data in a specific format, the online agementinlargeIPnetworks,’’IEEE/ACMTrans.Netw.,vol.20,no.6,
pp.1734–1747,Dec.2012.
datacanbeperfectlyconnectedwithouralgorithm.
|     |     |     |     |     |     |     |     | [20] D.Liu,Y.Zhao,H.Xu,Y.Sun,D.Pei,J.Luo,X.Jing,andM.Feng, |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------------------------------------------------- | --- | --- | --- | --- | --- |
‘‘Opprentice:Towardspracticalandautomaticanomalydetectionthrough
REFERENCES machinelearning,’’inProc.InternetMeas.Conf.,Oct.2015,pp.211–224.
[1] Á. Brandón, M. Solé, A. Huélamo, D. Solans, M. S. Pérez, and [21] M. Ma, S. Zhang, D. Pei, X. Huang, and H. Dai, ‘‘Robust and rapid
adaptionforconceptdriftinsoftwaresystemanomalydetection,’’inProc.
| V. Muntés-Mulero, |                  | ‘‘Graph-based |                  | root | cause    | analysis for | service-  |           |                   |           |          |          |          |
| ----------------- | ---------------- | ------------- | ---------------- | ---- | -------- | ------------ | --------- | --------- | ----------------- | --------- | -------- | -------- | -------- |
|                   |                  |               |                  |      |          |              |           | IEEE 29th | Int. Symp. Softw. | Rel. Eng. | (ISSRE), | Memphis, | TN, USA, |
| oriented          | and microservice |               | architectures,’’ |      | J. Syst. | Softw.,      | vol. 159, |           |                   |           |          |          |          |
Oct.2018,pp.13–24.
pp.110432.1–110432.17,Jan.2020.
|             |        |                      |     |             |     |                 |       | [22] F. Li and | M. Akagi, ‘‘Unsupervised |     | singing voice | separation | based on |
| ----------- | ------ | -------------------- | --- | ----------- | --- | --------------- | ----- | -------------- | ------------------------ | --- | ------------- | ---------- | -------- |
| [2] J. Zhao | and L. | Huang, ‘‘Exploration |     | of research |     | on microservice | fault |                |                          |     |               |            |          |
diagnosis technology,’’ J. Netw. New Media, vol. 9, no. 1, pp.57–64, robustprincipalcomponentanalysisexploitingrank-1constraint,’’inProc.
Jan.2020. 26thEur.SignalProcess.Conf.(EUSIPCO),Sep.2018,pp.1920–1924.
|             |        |         |        |                   |     |          |         | [23] T.Bouwmans,S.Javed,H.Zhang,Z.Lin,andR.Otazo,‘‘Ontheapplica- |     |     |     |     |     |
| ----------- | ------ | ------- | ------ | ----------------- | --- | -------- | ------- | ---------------------------------------------------------------- | --- | --- | --- | --- | --- |
| [3] W. Lin, | M. Ma, | D. Pan, | and P. | Wang, ‘‘FacGraph: |     | Frequent | anomaly |                                                                  |     |     |     |     |     |
tionsofrobustPCAinimageandvideoprocessing,’’Proc.IEEE,vol.106,
correlationgraphminingforrootcausediagnoseinmicro-servicearchitec-
no.8,pp.1427–1457,Aug.2018.
ture,’’inProc.IEEE37thInt.Perform.Comput.Commun.Conf.(IPCCC),
Nov.2018,pp.1–8. [24] M.Mardani,G.Mateos,andG.B.Giannakis,‘‘Recoveryoflow-rankplus
[4] J.M.Q.Alvarez,J.A.O.Sanabria,andJ.I.M.Garcia,‘‘Microservices- compressedsparsematriceswithapplicationtounveilingtrafficanoma-
basedarchitectureforfaultdiagnosisintele-rehabilitationequipmentoper- lies,’’IEEETrans.Inf.Theory,vol.59,no.8,pp.5186–5205,Aug.2013.
|     |     |     |     |     |     |     |     | [25] M.Amoozegar,B.Minaei-Bidgoli,M.Rezghi,andH.Fanaee-T,‘‘Extra- |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------------------------------------------------------- | --- | --- | --- | --- | --- |
atedviaInternet,’’inProc.IEEELatinAmer.TestSymp.(LATS),Mar.2019,
adaptiverobustonlinesubspacetrackerforanomalydetectionfromstream-
pp.1–6.
[5] X. Zhou, X. Peng, T. Xie, J. Sun, C. Ji, W. Li, and D. Ding, ‘‘Fault ingnetworks,’’Eng.Appl.Artif.Intell.,vol.94,Sep.2020,Art.no.103741.
analysisanddebuggingofmicroservicesystems:Industrialsurvey,bench- [26] Y. Ding and J. Liu, ‘‘Real-time false data injection attack detection in
marksystem,andempiricalstudy,’’IEEETrans.Softw.Eng.,earlyaccess, energyInternetusingonlinerobustprincipalcomponentanalysis,’’inProc.
Dec.18,2018,doi:10.1109/TSE.2018.2887384. IEEE Conf. Energy Internet Energy Syst. Integr. (EI), Beijing, China,
Nov.2017,pp.1–6.
[6] L.Huang,W.Zhuang,M.Sun,andH.Zhang,‘‘Researchandapplicationof
microserviceinpowergriddispatchingcontrolsystem,’’inProc.IEEE4th [27] K.MahapatraandN.R.Chaudhuri,‘‘Maliciouscorruption-resilientwide-
Inf.Technol.,Netw.,Electron.Automat.ControlConf.(ITNEC),Jun.2020, areaoscillationmonitoringusingonlinerobustPCA,’’inProc.IEEEPower
pp.1895–1899. Energy Soc. Gen. Meeting (PESGM), Portland, OR, USA, Aug. 2018,
| [7] J.Qiu,Q.Du,K.Yin,S.-L.Zhang,andC.Qian,‘‘Acausalitymining |     |     |     |     |     |     |     | pp.1–5. |     |     |     |     |     |
| ------------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- |
andknowledgegraphbasedmethodofrootcausediagnosisforperfor- [28] J.Song,B.Gao,W.L.Woo,andG.Y.Tian,‘‘Ensembletensordecom-
manceanomalyincloudapplications,’’Appl.Sci.,vol.10,no.6,p.2166, positionforinfraredthermographycracksdetectionsystem,’’Infr.Phys.
| Mar.2020. |     |     |     |     |     |     |     | Technol.,vol.105,Mar.2020,Art.no.103203. |     |     |     |     |     |
| --------- | --- | --- | --- | --- | --- | --- | --- | ---------------------------------------- | --- | --- | --- | --- | --- |
[8] Z.Wang,T.Wang,W.Zhang,N.Chen,andC.Zuo,‘‘Faultdiagnosisfor [29] M.Kim,R.Sumbaly,andS.Shah,‘‘Rootcausedetectioninaservice-
microserviceswithexecutiontracemonitoring,’’J.Softw.,vol.28,no.6, orientedarchitecture,’’ACMSIGMETRICSPerform.Eval.Rev.,vol.41,
| pp.1435–1454,Jun.2017. |     |     |     |     |     |     |     | no.1,pp.93–104,Jun.2013. |     |     |     |     |     |
| ---------------------- | --- | --- | --- | --- | --- | --- | --- | ------------------------ | --- | --- | --- | --- | --- |
[9] M.Ma,Z.Yin,S.Zhang,S.Wang,C.Zheng,X.Jiang,H.Hu,C.Luo,Y.Li, [30] N. Laptev, S. Amizadeh, and I. Flint, ‘‘Generic and scalable frame-
N.Qiu,F.Li,C.Chen,andD.Pei,‘‘Diagnosingrootcausesofintermittent workforautomatedtime-seriesanomalydetection,’’inProc.21thACM
slowqueriesinclouddatabases,’’Proc.VLDBEndowment,vol.13,no.10, SIGKDDInt.Conf.Knowl.DiscoveryDataMining(KDD),Aug.2015.,
| pp.1176–1189,Jun.2020. |     |     |     |     |     |     |     | pp.1939–1947. |     |     |     |     |              |
| ---------------------- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | --- | --- | --- | ------------ |
| 226406                 |     |     |     |     |     |     |     |               |     |     |     |     | VOLUME8,2020 |

M.Jinetal.:AnomalyDetectionAlgorithmforMSABasedonRPCA
[31] W.Xu,L.Huang,A.Fox,D.A.Patterson,andI.M.Jordan,‘‘Detecting ZIJIANG WEN was born in China, in 1991.
large-scalesystemproblemsbyminingconsolelogs,’’inProc.27thInt. He received the B.S. degree in statistics from
Conf.Mach.Learn.(ICML),Haifa,Israel,Jun.2010,pp.112–132. Guangdong Medical University, Guangzhou,
[32] Q.Fu,J.-G.Lou,Y.Wang,andJ.Li,‘‘Executionanomalydetectionin China,in2015.Heiscurrentlyengagedinmachine
distributedsystemsthroughunstructuredloganalysis,’’inProc.9thIEEE learning with JOYY Inc. His research interests
Int.Conf.DataMining,Miami,FL,USA,Dec.2009,pp.149–158.
includeartificialintelligenceanddeeplearning.
| [33] M. Partridge | and | M. Jabri, | ‘‘Robust | principal component |     | analysis,’’ in |     |     |     |     |     |
| ----------------- | --- | --------- | -------- | ------------------- | --- | -------------- | --- | --- | --- | --- | --- |
Proc.IEEESignalProcess.Soc.WorkshopNeuralNetw.SignalProcess.,
Sydney,NSW,Australia,vol.1,Dec.2000,pp.1–10.
[34] E.J.Candes,X.Li,Y.Ma,andJ.Weight,‘‘Robustprincipalcomponent
analysis?’’J.ACM,vol.58,no.3,pp.1–37,Dec.2009.
[35] J.Wright,A.Ganesh,S.Rao,andY.Ma,‘‘Robustprincipalcomponent
| analysis: | Exact | recovery | of corrupted | low-rank matrices,’’ |     | Apr. 2009, |     |     |     |     |     |
| --------- | ----- | -------- | ------------ | -------------------- | --- | ---------- | --- | --- | --- | --- | --- |
arXiv:0905.0233.[Online].Available:https://arxiv.org/abs/0905.0233
| [36] N. Vaswani, | T.        | Bouwmans, | S. Javed, | and P. Narayanamurthy, |           | ‘‘Robust   |     |     |     |     |     |
| ---------------- | --------- | --------- | --------- | ---------------------- | --------- | ---------- | --- | --- | --- | --- | --- |
| subspace         | learning: | Robust    | PCA,      | robust subspace        | tracking, | and robust |     |     |     |     |     |
subspacerecovery,’’IEEESignalProcess.Mag.,vol.35,no.4,pp.32–55, YUBINZHONGwasborninChina,in1993.He
| Jul.2018. |     |     |     |     |     |     | received the | master’s | degree | in control | science |
| --------- | --- | --- | --- | --- | --- | --- | ------------ | -------- | ------ | ---------- | ------- |
[37] N. Vaswani, Y. Chi, and T. Bouwmans, ‘‘Rethinking PCA for modern andengineeringfromtheGuangdongUniversity
datasets:Theory,algorithms,andapplications[scanningtheissue],’’Proc.
ofTechnology,Guangzhou,China,in2019.Heis
IEEE,vol.106,no.8,pp.1274–1276,Aug.2018.
currentlyengagedindataminingwithJOYYInc.
[38] Zhang,Zhu,Li,Wang,andGuo,‘‘Anomalydetectionbasedonmining
|     |     |     |     |     |     |     | His research | interests | include | machine | learning, |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --------- | ------- | ------- | --------- |
sixlocaldatafeaturesandBPneuralnetwork,’’Symmetry,vol.11,no.4, anomalydetection,andrecommendationsystems.
p.571,Apr.2019.
[39] F.Liu,K.Ting,andZ.Zhou,‘‘Isolationforest,’’inProc.IEEE8thInt.
Conf.DataMining,Pisa,Italy,Dec.2008,pp.413–422.
[40] R.Perdisci,G.Gu,andW.Lee,‘‘Usinganensembleofone-classSVM
classifierstohardenpayload-basedanomalydetectionsystems,’’inProc.
6thInt.Conf.DataMining(ICDM),HongKong,Dec.2006,pp.488–498.
| [41] Y.-S. | Choi, ‘‘Least | squares | one-class | support vector | machine,’’ | Pattern |     |     |     |     |     |
| ---------- | ------------- | ------- | --------- | -------------- | ---------- | ------- | --- | --- | --- | --- | --- |
Recognit.Lett.,vol.30,no.13,pp.1236–1240,Oct.2009.
[42] M.M.Breunig,H.-P.Kriegel,R.T.Ng,andJ.Sander,‘‘LOF:Identifying
density-basedlocaloutliers,’’inProc.ACMSIGMODInt.Conf.Manage. ZEXIN ZHAO was born in China, in 1999.
Data(SIGMOD),May2000,pp.93–104. He is currently pursuing the B.Eng. degree in
informationmanagementandinformationsystem
|     |     |     |     |     |     |     | with the South | China | University | of Technology, |     |
| --- | --- | --- | --- | --- | --- | --- | -------------- | ----- | ---------- | -------------- | --- |
Guangzhou,China.Hisresearchinterestsinclude
|     |     | MINGXU | JIN | was born in | China, | in 1998. He |     |     |     |     |     |
| --- | --- | ------ | --- | ----------- | ------ | ----------- | --- | --- | --- | --- | --- |
softwareengineeringandmachinelearning.
|     |     | received | the | B.S. degree | in mathematics | and |     |     |     |     |     |
| --- | --- | -------- | --- | ----------- | -------------- | --- | --- | --- | --- | --- | --- |
appliedmathematicsfromtheSouthChinaUni-
versityofTechnology,Guangzhou,China,in2020,
whereheiscurrentlypursuingthemaster’sdegree
incomputationalmathematics.Hisresearchinter-
estsincludecomputer-aidedgeometricdesignand
machinelearning.
|     |     |           |          |                    |        |             | JIANG WU        | was        | born in | China,      | in 1999.  |
| --- | --- | --------- | -------- | ------------------ | ------ | ----------- | --------------- | ---------- | ------- | ----------- | --------- |
|     |     | AORAN     | LV       | was born in China, | in     | 1999. He is |                 |            |         |             |           |
|     |     |           |          |                    |        |             | He is currently | pursuing   | the     | B.Eng.      | degree in |
|     |     | currently | pursuing | the B.S.           | degree | in informa- |                 |            |         |             |           |
|     |     |           |          |                    |        |             | information     | management | and     | information | sys-      |
tionandcomputingsciencewiththeSouthChina
|     |     |     |     |     |     |     | tem with | the South | China University |     | of Tech- |
| --- | --- | --- | --- | --- | --- | --- | -------- | --------- | ---------------- | --- | -------- |
UniversityofTechnology,Guangzhou,China.His
nology,Guangzhou,China.Hisresearchinterests
researchinterestsincludecomputergraphicsand
includeneuralnetworks,optimizationalgorithm,
machinelearning.
datamining,bigdataprocessing,androbotics.
|     |     | YUANPENG |     | ZHU was born | in China, | in 1984. |     |     |     |     |     |
| --- | --- | -------- | --- | ------------ | --------- | -------- | --- | --- | --- | --- | --- |
Hereceivedthemaster’sdegreeincomputational
mathematicsandthePh.D.degreeinappliedmath-
ematicsfromCentralSouthUniversity,Changsha, HEJIE LI was born in China, in 2000. He is
China, in 2011 and 2014, respectively. From currently pursuing the B.S. degree in informa-
2014to2016,hewasaPostdoctoralFellowwith
tionandcomputingsciencewiththeSouthChina
theSchoolofMathematicalSciences,University
UniversityofTechnology,Guangzhou,China.His
ofScienceandTechnologyofChina,Hefei,China.
|     |     |                                          |     |     |     |     | research interests | include | machine | learning | and |
| --- | --- | ---------------------------------------- | --- | --- | --- | --- | ------------------ | ------- | ------- | -------- | --- |
|     |     | Since2016,hehasbeenwiththeSouthChinaUni- |     |     |     |     | dataalgorithm.     |         |         |          |     |
versityofTechnology,Guangzhou,China,where
heiscurrentlyaLecturerwiththetheSchoolofMathematics.Hisresearch
interestsincludecomputer-aidedgeometricdesign,geometricmodeling,and
spline.
| VOLUME8,2020 |     |     |     |     |     |     |     |     |     |     | 226407 |
| ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |

M.Jinetal.:AnomalyDetectionAlgorithmforMSABasedonRPCA
HANHENG HE wasborninChina,in1998.He FENGYICHENwasborninChina,in1985.She
iscurrentlypursuingtheB.S.degreeininforma- received the master’s degree in accounting sci-
tionandcomputingsciencewiththeSouthChina encefromtheUniversityofMacau,in2012.She
UniversityofTechnology,Guangzhou,China.His is currently pursuing the Ph.D. degree with The
research interests include machine learning and HongKongPolytechnicUniversity.Herresearch
computervision. interests include grey forecasting and market
forecasting.
226408 VOLUME8,2020