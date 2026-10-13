IEEETRANSACTIONSONSOFTWAREENGINEERING,VOL.50,NO.10,OCTOBER2024 2583
iTCRL: Causal-Intervention-Based Trace
Contrastive Representation Learning for
Microservice Systems
Xiangbo Tian , Shi Ying , Tiangang Li , Mengting Yuan , Ruijin Wang , Yishi Zhao , and
Jianga Shang , Member, IEEE
Abstract—Nowadays, microservice architecture has become I. INTRODUCTION
mainstream way of cloud applications delivery. Distributed
tracing is crucial to preserve the observability of microservice WITH the rapid development of cloud computing, mi-
systems. However, existing trace representation approaches only croservicearchitectureisappliedbytheincreasedcloud
concentrate on operations, relationships and metrics related applicationsduetotheadvantagesofmodularityandelasticity
to service invocations. They ignore service events that denotes
[1],[2],[3],[4].Whileitbringsgreaterreliabilityandflexibility
meaningful,singularpointintimeduringtheservice’sduration.
to software development, it brings new challenges to software
In this paper, we propose iTCRL, a novel trace contrastive
representation learning approach based on causal intervention. operationandmaintenance,suchashigherdynamicsandmore
This approach first constructs a unified graph representation complex dependencies. To address these challenges, the dis-
for each trace to describe the runtime status of service events tributedtracing[5],[6]iswidelyusedinmicroservicesystems.
in traces and the complex relationships between them. Then,
Microservicesystemsproducealargenumberoftracesevery
Causal-intervention-based Trace Contrastive Learning is pro-
day. These traces consist of much useful information, such
posed,whichlearnstracerepresentationsfromcausalperspective
based on the unified graph representations of traces. It uses as span events, span attributes, timestamps and span links.
causal intervention to generate contrastive views, heterogeneous The information can help to improve the expressive ability
graph neural network-based trace encoder to learn trace rep- oftracerepresentations.However,existingtracerepresentation
resentations, and direct causal effect to guide the training of
approaches only concentrate on operations, relationships and
trace encoder. Experimental results on three datasets show that
metricsrelatedtoserviceinvocations,butignoreserviceevents
iTCRL outperforms all baselines in terms of trace classification,
trace anomaly detection, trace sampling and noise robustness, denoting meaningful, singular time points during the service’s
and also validate the contribution of Causal-intervention-based duration.
Trace Contrastive Learning. In this paper, we propose iTCRL, a novel trace contrastive
Index Terms—Microservice systems, distributed tracing, trace representationlearningapproachbasedoncausalintervention.
representation, causal intervention, graph contrastive learning. This approach first constructs a Service-Event-based Trace
Graphs(SETGs)foreachtrace,usingserviceeventsasnodes,
the relationships between service events as edges and service
metrics as node attributes or edge attributes. SETGs can
effectivelydescribetheruntimestatusofserviceeventsandthe
complex relationships between them. Then, Causal-
intervention-based Trace Contrastive Learning is proposed,
Manuscript received 31 December 2023; revised 30 July 2024; accepted
which learns trace representations from causal perspective
12August2024.Dateofpublication20August2024;dateofcurrentversion
17 October 2024. This work was supported in part by the National Key based on SETGs. It uses causal intervention to generate
R & D Program of China under Grant 2022YFB3304300, in part by the contrastive views, heterogeneous graph neural network-based
NationalNaturalScienceFoundationProjectofChinaunderGrant62072342
trace encoder to learn trace representations, and direct causal
and Grant 61672392, and in part by the Fundamental Research Funds for
the Central Universities under Grant 2042023kf1018. Recommended for effect to guide the training of trace encoder. Experimental
acceptancebyÁ.Beszédes.(Correspondingauthor:ShiYing.) results on three datasets show that iTCRL outperforms all
Xiangbo Tian, Shi Ying, Tiangang Li, and Mengting Yuan are with
baselines in terms of trace classification, trace anomaly
the School of Computer Science, Wuhan University, Wuhan 430072,
China (e-mail: tianxiangbo@whu.edu.cn; yingshi@whu.edu.cn; tiangangli@ detection, trace sampling and noise robustness, and also
whu.edu.cn;ymt@whu.edu.cn). validate the contribution of Causal-intervention-based Trace
RuijinWangiswiththeSchoolofInformationandSoftwareEngineering,
ContrastiveLearning.Insummary,ourcontributionsaregiven
UniversityofElectronicScienceandTechnologyofChina,Chengdu610054,
China(e-mail:ruijinwang@uestc.edu.cn). asfollows.
Yishi Zhao and Jianga Shang are with the School of Computer Science, (cid:129) To our best knowledge, we are the first to introduce ser-
ChinaUniversityofGeosciences,Wuhan430074,China(e-mail:zhaoyishi@
viceeventsthatdenotemeaningful,singularpointintime
cug.edu.cn;jgshang@cug.edu.cn).
DigitalObjectIdentifier10.1109/TSE.2024.3446532 duringtheservice’sduration tohelpmodel traces.
0098-5589©2024IEEE.Personaluseispermitted,butrepublication/redistributionrequiresIEEEpermission.
Seehttps://www.ieee.org/publications/rights/index.htmlformoreinformation.
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on March 20,2026 at 23:38:31 UTC from IEEE Xplore. Restrictions apply.

2584 IEEETRANSACTIONSONSOFTWAREENGINEERING,VOL.50,NO.10,OCTOBER2024
(cid:129) We design a Causal-intervention-based Trace Contrastive (cid:129) Service Invocation Event (SIE). It is a type of SE that
Learning approach, which can learn trace representation denotes thestartandend ofaspan.
fromcausalperspective,andeffectivelyavoidthecreation (cid:129) Service Runtime Event (SRE). It is a type of SE that
oftraces thatdonotexistinrealworld. denotes a meaningful, singular point in time during the
(cid:129) Weconductcomprehensiveexperimentsonthreedatasets span’s duration.
to show that iTCRL outperforms all baselines in terms (cid:129) Service Event Metric (SEM). It is the metric set that
oftraceclassification,traceanomalydetection,tracesam- describes thestatusofSEswithinatimeinterval.
plingand noiserobustness. (cid:129) Invocation Event Constant Template (IECT). It is the
The rest of the paper is organized as follows. Section II constant templateofSIE.
introducesthebackgroundofthisresearch.SectionIIIdescribes (cid:129) Invocation Event Variable Template (IEVT). It is the
thespecificdetailsofiTCRL.SectionIVgivestheexperimental variable templateof SIE.
results and analysis. Section V introduces the related works. (cid:129) Runtime Event Constant Template (RECT). It is the
Section VIgives conclusion, limitationsand futurework. constant templateofSRE.
|     |     |     |            |     |     |     |     | (cid:129) Runtime | Event      |     | Variable | Template |     | (REVT). | It is the |
| --- | --- | --- | ---------- | --- | --- | --- | --- | ----------------- | ---------- | --- | -------- | -------- | --- | ------- | --------- |
|     |     | II. | BACKGROUND |     |     |     |     | variable          | templateof |     | SRE.     |          |     |         |           |
(cid:129) ServiceEventRuntimeMetric(SERM).Itisthemetric
Microservicesystemsareusuallydistributedsystems,which
|                                 |                |                |            |                     |              |              |          | set               | that describes |            | the runtime | status     | of                 | SEs within | a time |
| ------------------------------- | -------------- | -------------- | ---------- | ------------------- | ------------ | ------------ | -------- | ----------------- | -------------- | ---------- | ----------- | ---------- | ------------------ | ---------- | ------ |
| replace the                     | highly-coupled |                | monolithic |                     | services     | with         | a set of |                   |                |            |             |            |                    |            |        |
| loosely-coupled                 |                | microservices. |            | Although            | microservice |              | archi-   | interval.         |                |            |             |            |                    |            |        |
|                                 |                |                |            |                     |              |              |          | (cid:129) Service | Event          | Invocation |             | Metric     | (SEIM).Itisthemet- |            |        |
| tecture brings                  | larger         | reliability    |            | and flexibility     |              | for software | de-      |                   |                |            |             |            |                    |            |        |
|                                 |                |                |            |                     |              |              |          | ric               | set that       | describes  | the         | invocation | status             | between    | SIEs   |
| velopment,itbringsnewchallenges |                |                |            | tosoftwareoperation |              |              | and      |                   |                |            |             |            |                    |            |        |
withinatimeinterval.
| maintenance, | such | as more          | complex |      | dependencies |         | and larger |             |     |       |     |     |     |     |     |
| ------------ | ---- | ---------------- | ------- | ---- | ------------ | ------- | ---------- | ----------- | --- | ----- | --- | --- | --- | --- | --- |
| dynamicity   | [7]. | These challenges |         | make | distributed  | tracing | be-        |             |     |       |     |     |     |     |     |
| comemoreand  |      | moreimportant.   |         |      |              |         |            | B. Overview | of  | iTCRL |     |     |     |     |     |
InOpenTelemetryspecifications[8],spansarebasicbuilding In this paper, we propose iTCRL, a novel trace contrastive
| blocks of | traces | and represent |     | units | of work | or operation. | In  |     |     |     |     |     |     |     |     |
| --------- | ------ | ------------- | --- | ----- | ------- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
representationlearningapproachbasedoncausalintervention.
| OpenTelemetry  |       | specifications,        |     | a span | includes | the          | following |               |               |       |            |                |              |                 |             |
| -------------- | ----- | ---------------------- | --- | ------ | -------- | ------------ | --------- | ------------- | ------------- | ----- | ---------- | -------------- | ------------ | --------------- | ----------- |
|                |       |                        |     |        |          |              |           | This approach | can           | learn | trace      | representation |              | from            | causal per- |
| information.   |       |                        |     |        |          |              |           | spective      | basedonSETGs. |       | Fig.1shows |                | itsoverview. |                 |             |
| (cid:129) Span | Name: | Itisastringthatrecords |     |        |          | thespanname. |           |               |               |       |            |                |              |                 |             |
|                |       |                        |     |        |          |              |           | As shown      | in            | Fig.  | 1, iTCRL   | includes       |              | two components. |             |
(cid:129) Parent Span ID:Itisastringthatrecordstheparentspan Service-Event-based Trace Graph Construction constructs
ofaspan.
|                 |     |                 |     |      |     |            |      | a Service-Event-based     |     |     | Trace | Graph | (SETG)      | for | each trace. |
| --------------- | --- | --------------- | --- | ---- | --- | ---------- | ---- | ------------------------- | --- | --- | ----- | ----- | ----------- | --- | ----------- |
| (cid:129) Start | and | End Timestamps: |     | They | are | timestamps | that |                           |     |     |       |       |             |     |             |
|                 |     |                 |     |      |     |            |      | Causal-intervention-based |     |     |       | Trace | Contrastive |     | Learning    |
record thestartandend ofaspan. trainsatracerepresentation learningmodel.
| (cid:129) Span | Context: | It  | is an immutable |     | object | that | contains |     |     |     |     |     |     |     |     |
| -------------- | -------- | --- | --------------- | --- | ------ | ---- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
Trace ID,Span ID,Trace Flags and TraceState. C. Service-Event-Based Trace Graph Construction
| (cid:129) Span | Attributes: |     | They are | key-value |     | pairs that | records |     |     |     |     |     |     |     |     |
| -------------- | ----------- | --- | -------- | --------- | --- | ---------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
operation information. Service-Event-based Trace Graph Construction consists
|                |        |        |     |         |       |              |     | offoursteps.Trace |       | Data  | PreprocessinggetSEMs,SIEsand |      |         |          |        |
| -------------- | ------ | ------ | --- | ------- | ----- | ------------ | --- | ----------------- | ----- | ----- | ---------------------------- | ---- | ------- | -------- | ------ |
| (cid:129) Span | Event: | It can | be  | thought | of as | a structured | log |                   |       |       |                              |      |         |          |        |
|                |        |        |     |         |       |              |     | SREs from         | trace | data. | Span                         | Data | Parsing | extracts | SERMs, |
message(orannotation)onaspan,typicallyusedtodenote
|               |     |          |       |     |      |        |            | SEIMs,      | IECTs, | IEVTs, | RECTs    | and    | REVTs          | by SEM | Parsing, |
| ------------- | --- | -------- | ----- | --- | ---- | ------ | ---------- | ----------- | ------ | ------ | -------- | ------ | -------------- | ------ | -------- |
| a meaningful, |     | singular | point | in  | time | during | the span’s |             |        |        |          |        |                |        |          |
|               |     |          |       |     |      |        |            | SIE Parsing | and    | SRE    | Parsing. | Vector | Representation |        | trans-   |
duration.
(cid:129) Span Status:Eachspanhasastatus,containing‘Unset’, forms SERMs, SEIMs, IECTs, IEVTs, RECTs and REVTs
|               |     |                                          |         |        |     |             |        | into vector  | representations. |                  | Graph |        | Construction  | constructs | a       |
| ------------- | --- | ---------------------------------------- | ------- | ------ | --- | ----------- | ------ | ------------ | ---------------- | ---------------- | ----- | ------ | ------------- | ---------- | ------- |
| ‘Error’and    |     | ‘OK’.                                    |         |        |     |             |        |              |                  |                  |       |        |               |            |         |
|               |     |                                          |         |        |     |             |        | SETG for     | each             | trace            | based | on the | relationships | between    | SEs     |
| BasedonSpan   |     | Attributes,serviceinvocationoperationcan |         |        |     |             |        |              |                  |                  |       |        |               |            |         |
|               |     |                                          |         |        |     |             |        | and theabove | vector           | representations. |       |        |               |            |         |
| be got. Based | on  | Span                                     | Events, | we can | get | the service | events |              |                  |                  |       |        |               |            |         |
|               |     |                                          |         |        |     |             |        | 1) Trace     | Data             | Preprocessing:   |       | Based  | on            | the above  | defini- |
thatdenotemeaningful,singulartimepointsduringtheservice’s
duration.BasedonTimestamps,wecancalculatemanyservice tions, the SEs of a trace are divided into SREs and SIEs. For
|     |     |     |     |     |     |     |     | the former, | the | structured | log | messages | on a | span | are directly |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ---------- | --- | -------- | ---- | ---- | ------------ |
metricsthatdescribeservices’executionstatus.BasedonPar-
|          |                      |     |     |               |     |       |      | treated as      | SREs. | For     | the latter, | they | are constructed |     | by the      |
| -------- | -------------------- | --- | --- | ------------- | --- | ----- | ---- | --------------- | ----- | ------- | ----------- | ---- | --------------- | --- | ----------- |
| ent Span | ID,serviceinvocation |     |     | relationships |     | canbe | got. |                 |       |         |             |      |                 |     |             |
|          |                      |     |     |               |     |       |      | API information |       | in Span | Attributes. |      | Besides,        | 14  | metrics are |
III. APPROACH calculated asSEMs based on thespan information todescribe
|     |     |     |     |     |     |     |     | the operating | environment |     | status | when | traces | are | generated. |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | ----------- | --- | ------ | ---- | ------ | --- | ---------- |
A. Definitions
|     |     |     |     |     |     |     |     | Its role | is similar | to the | response |     | time in STV | [9], | but it is |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ---------- | ------ | -------- | --- | ----------- | ---- | --------- |
Based on the OpenTelemetry specifications [8], some con- more fine-grained than the response time. When microservice
cepts are defined to better describe our proposed approach. systemsarenormal,itwillnotcauseinaccuratetracerepresen-
Theseconcepts aregiven asfollows. tations.Whenmicroservicesystemsareabnormal,itcanmake
(cid:129) Service Event (SE). It is an event that denotes a mean- tracerepresentationbetterexpresstheanomalies.TableIgives
| ingful,singularpointintimeduringtheservice’sduration. |     |     |     |     |     |     |     | thesemetrics. |     |     |     |     |     |     |     |
| ----------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- |
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on March 20,2026 at 23:38:31 UTC from IEEE Xplore.  Restrictions apply.

TIANetal.:ITCRL:CAUSAL-INTERVENTION-BASEDTRACECONTRASTIVEREPRESENTATIONLEARNING 2585
Fig.1. OverviewofiTCRL.
TABLEI
SERVICEEVENTMETRICS
Metrics Descriptions
Apdex Applicationperformanceindex.
CPM Thecallnumberofaserviceinstanceperminute.
SLA Thecallsuccessrateofaserviceinstance.
ART Thepercentileofresponsetimeofaserviceinstance,whichcontainsP50,P75,P90,P95andP99.
RTP Thepercentileofresponsetimeofaserviceinstance,whichcontainsP50,P75,P90,P95andP99.
CCPM Thecallnumberofaserviceinstanceperminutedetectedontheclient.
SCPM Thecallnumberofaserviceinstanceperminutedetectedontheserver.
CART Theaverageresponsetimeofaserviceinstancedetectedontheclient.
SART Theaverageresponsetimeofaserviceinstancedetectedontheserver.
CSLA Thecallsuccessrateofaserviceinstancedetectedontheclient.
SSLA Thecallsuccessrateofaserviceinstancedetectedontheserver.
NL Thenetworklatencybetweenserviceinstances.
CRTP Thepercentileofresponsetimeofaserviceinstancedetectedontheclient,whichcontainsP50,P75,P90,P95andP99.
SRTP Thepercentileofresponsetimeofaserviceinstancedetectedontheserver,whichcontainsP50,P75,P90,P95andP99.
2) Span Data Parsing: Span Data Parsing includes three 3) Vector Representation: Vector Representation trans-
components: SEMParsing,SIEParsingand SREParsing. formsSERMs,SEIMs,IECTs,IEVTs,RECTsandREVTsinto
SEM Parsing divides SEMs into SERMs and SEIMs ac- vector representations.
cording to their meanings and effects. The first five metrics in For SERMs and SEIMs, they are directly transformed
TableIareclassifiedasSERMs,andtheremainingmetricsare into vector representations, where each dimension represents
classifiedas SEIMs. ametric.
SIE Parsing obtains IECTs and IEVTs from SIEs. Specif- For IECTs, they are transformed into vector representations
ically, it extracts IECTs from SIEs by the Drain algorithm followingtheexistingresearch[11],[12].Indetail,eachIECT
[10]. Then, it obtained IEVTs by comparing SIEs with isfirstpreprocessed,suchasremovingstopwords,andsplitting
its corresponding IECTs. For example, given a SIE ‘INFO compoundwords.Then,apre-trainedGloVemodel[13]isused
query 200’ and its IECT ‘INFO query <∗>’, its IEVT to obtain vector representations of its each word. Finally, TF-
is‘200’. IDF[14]isusedtocalculateitsvectorrepresentationbyaggre-
SRE Parsing obtains RECTs and REVTs from SREs. Its gating the vector representations of its all words. For RECTs,
process issameas SIEParsing. theirvector representation process issameasIECTs.
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on March 20,2026 at 23:38:31 UTC from IEEE Xplore. Restrictions apply.

2586 IEEETRANSACTIONSONSOFTWAREENGINEERING,VOL.50,NO.10,OCTOBER2024
Fig.2. AnexampleofSETG.
For IEVTs, they are first divided into the word group ThisgraphwelldescribesSEsinatraceandtherelationships
and number group. Then, the same process as IECT vec- betweenthem,whichisextremelyhelpfulfortracerepresenta-
tor representation is used to get vector representation of tions. In detail, the functional patterns of a trace can be well
word group. Afterwards, the vector representation of number described by SEs and the relationships between them while
group is directly generated, where each dimension denotes its performance pattern can be well described by SERMs and
| a numerical | variable. | Finally,         | the vector     | representation     | of an   | SEIMs. |     |     |     |     |     |
| ----------- | --------- | ---------------- | -------------- | ------------------ | ------- | ------ | --- | --- | --- | --- | --- |
| IEVT is     | obtained  | by concatenating | the two        | vector representa- |         |        |     |     |     |     |     |
| tions. For  | REVTs,    | their vector     | representation | process            | is same |        |     |     |     |     |     |
asIEVTs. D. Causal-Intervention-Based Trace Contrastive Learning
4) GraphConstruction: Graph-baseddataispowerfultools Trace representation model needs to be trained with an un-
fordescribingcomplexrelationships[15].Therefore,eachtrace supervisedorself-supervisedmannersincetheamountoftrace
| is first | constructed | as a | SETG. In SETGs, | nodes | represent |               |         |         |          |               |            |
| -------- | ----------- | ---- | --------------- | ----- | --------- | ------------- | ------- | ------- | -------- | ------------- | ---------- |
|          |             |      |                 |       |           | data is large | and the | cost of | labeling | data is high. | Graph con- |
SEs that denote meaningful, singular points in time during trastivelearning[16],[17],[18]isanexcellentself-supervised
the services’duration, which are described by IECT (RECT), learning framework and very suitable for trace representation
IEVT (REVT) and SERM. Edges represent relationships be- learning.However,itoftencreatestracesthatdonotexistinreal
tween SEs, which are described by SEIM. The relationship world when directly applied to trace representation learning.
| construction | consists | of  | the connection | between SEs | in the |     |     |     |     |     |     |
| ------------ | -------- | --- | -------------- | ----------- | ------ | --- | --- | --- | --- | --- | --- |
Therefore,Causal-intervention-basedTraceContrastiveLearn-
samespanand theconnection between SEs indifferentspans. ing(iTCL)approachisproposed,whichlearnstracerepresen-
For the former, SEs in the same span are sequentially con- tation from causal perspective. Fig. 3 gives the structure of
nected according to their timestamp. For the latter, we di- iTCL. As shown in Fig. 3, this approach consists of Causal-
rectly use span-linking method proposed in DeepTraLog [11]. intervention-based trace data augmentation (iTDA), Heteroge-
| Different | to DeepTraLog, |     | we refine synchronous | request | rela- |             |                       |     |       |         |           |
| --------- | -------------- | --- | --------------------- | ------- | ----- | ----------- | --------------------- | --- | ----- | ------- | --------- |
|           |                |     |                       |         |       | neous graph | neural networks-based |     | trace | encoder | (HTE) and |
tionships into same process synchronous request relationships Direct causal effect-based trace contrastive loss (DCE-TCL).
and cross process synchronous request relationships, and syn- Among them, iTDA defines three direct causes of traces and
chronousresponserelationshipsintosameprocesssynchronous uses causal intervention to generate contrastive views, which
responserelationshipsandcrossprocesssynchronousresponse canavoidthecreationoftracesthatdonotexistinrealworld.
relationships.
|     |     |     |     |     |     | HTE gets | trace representations |     | by aggregating |     | the structure |
| --- | --- | --- | --- | --- | --- | -------- | --------------------- | --- | -------------- | --- | ------------- |
Fig. 2 gives an example of SETG. In this graph, rectangles information and attribute information on SETGs. DCE-TCL
representSEsandtheelementsinthemrepresenttheattributes guides the training of HTE based on the direct causal effect
of the corresponding SE. Dashed rounded rectangles indicate between contrastive views.
spans. Gray rectangles denote SREs and green rectangles de- 1) Causal-Intervention-Based Trace Data Augmentation:
noteSIEs.Differentarrowsindicatedifferenttypesofrelation- Graph data augmentations are used to generate contrastive
shipsshowninthelegend. views, which are crucial for graph contrastive learning [17].
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on March 20,2026 at 23:38:31 UTC from IEEE Xplore.  Restrictions apply.

TIANetal.:ITCRL:CAUSAL-INTERVENTION-BASEDTRACECONTRASTIVEREPRESENTATIONLEARNING 2587
Fig.3. StructureofiTCL.
There have been many different strategies,such as node drop- (cid:129) do(G =GSIS).ItremovesallSREsandtherelatededges
|     |     |     |     |     |     |     |     |     | i i |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
fromG
| ping, | edge perturbation, |     | attribute |     | masking | and subgraph. | Al- |     | i . |     |     |     |     |
| ----- | ------------------ | --- | --------- | --- | ------- | ------------- | --- | --- | --- | --- | --- | --- | --- |
though these strategies are useful in general graph contrastive (cid:129) do(G =GSRS).ItremovesallSIEsandtherelatededges
|           |      |        |      |        |       |               |      |       | i i |     |     |     |     |
| --------- | ---- | ------ | ---- | ------ | ----- | ------------- | ---- | ----- | --- | --- | --- | --- | --- |
| learning, | some | traces | that | do not | exist | in real world | will | fromG | .   |     |     |     |     |
i
|     |     |     |     |     |     |     |     | do(G | =GIEIS). |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | -------- | --- | --- | --- | --- |
be generated when they are directly applied to microservice (cid:129) It removes edges connecting same type
|     |     |     |     |     |     |     |     |     | i i |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
trace representation learning. To solve this problem, Causal- ofSEsand theresultingisolatednodes fromG .
i
intervention-basedtracedataaugmentation(iTDA)isproposed. Figs.4–6givetheexamplesofthreecausalinterventionsfor
According to the running mechanism of microservice sys- thetraceinFig.2.
tems,iTDAdefinesthreedirectcausesoftraces.Thethreedirect 2) HeterogeneousGraphNeuralNetworks-BasedTraceEn-
causes aregiven asfollows. coder: Fortraceencodingtask,wedesignHTE,atraceencoder
(cid:129) Service Invocation Status (SIS).Itdescribestheinvoca- basedonheterogeneousgraphneuralnetworks.Thisapproach
|     | tionstatusbetween |     | services. |     |     |     |     |         |                       |     |               |             |     |
| --- | ----------------- | --- | --------- | --- | --- | --- | --- | ------- | --------------------- | --- | ------------- | ----------- | --- |
|     |                   |     |           |     |     |     |     | encodes | traces by aggregating |     | the structure | information | and |
(cid:129) Service Runtime Status (SRS).Itdescribestheruntime attribute information on SETGs. It consists of three compo-
statusofservices. nents: node attribute aggregation, inter-neighbor aggregation,
(cid:129) Internal and External Interaction Status (IEIS). It and tracepooling and projection.
describestheinteractionstatusinsideandoutsideservices. a) Node Attribute Aggregation: In SETGs, a node is
Toavoidthecreationoftracesthatdonotexistinrealworld,
describedbyIECT(RECT),IEVT(REVT)andSERM.Theylie
iTDAdefinestracecontrastiveviewandcausalcontrastiveview, indifferentfeaturespacesandhavedifferentfeaturedimensions
and designcontrastive lossfunctionbased onthem. [22].Differentdimensionsofvectorrepresentationsaretrouble-
For trace contrastive views, the SETG of a trace is directly somewhenprocessingtheminaunifiedframework.Therefore,
treated as its trace contrastive view. The specific generation an attribute-specific linear transformation is applied for each
process isgiven bythefollowingequation. attribute vector representation of a node to project them into
T (G )=G thesamelatentspacebeforenodeattributeaggregation.Forthe
|     |     |     | 1   | i   | i   |     | (1) |                                                      |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------------------------------------------- | --- | --- | --- | --- | --- |
|     |     |     |     |     |     |     |     | attributeiofthenodev,itslatentvectorrepresentationht |     |     |     |     | is  |
v,i
| where                          | G denotes |     | the SETG | of trace | i; T                       | (G ) represents | the |            |                         |     |     |     |     |
| ------------------------------ | --------- | --- | -------- | -------- | -------------------------- | --------------- | --- | ---------- | ----------------------- | --- | --- | --- | --- |
|                                | i         |     |          |          |                            | 1 i             |     | calculated | bythefollowingequation: |     |     |     |     |
| tracecontrastiveviewoftracei;T |           |     |          |          | (·)representsthegeneration |                 |     |            |                         |     |     |     |     |
1
|                                                        |                  |             |        |        |              |       |       |         |             | ht      | Xt        |                 |     |
| ------------------------------------------------------ | ---------------- | ----------- | ------ | ------ | ------------ | ----- | ----- | ------- | ----------- | ------- | --------- | --------------- | --- |
| strategyof                                             | tracecontrastive |             |        | views. |              |       |       |         |             | =W      | +b        |                 | (3) |
|                                                        |                  |             |        |        |              |       |       |         |             | v,i     | i v,i i   |                 |     |
|                                                        | For causal       | contrastive | views, | causal | intervention | [19], | [20], |         |             |         |           |                 |     |
|                                                        |                  |             |        |        |              |       |       | where t | denotes the | type of | node v; W | and b represent | the |
| [21]isusedtogeneratethembasedontraces’directcauses.The |                  |             |        |        |              |       |       |         |             |         | i         | i               |     |
specificgenerationprocessisgivenbythefollowingequation. parametricweightmatrixandparametricbiasmatrixofattribute
|     |      |          |                       |     |     |     |     | i, respectively; | Xt  | describes | the vector | representation | of at- |
| --- | ---- | -------- | --------------------- | --- | --- | --- | --- | ---------------- | --- | --------- | ---------- | -------------- | ------ |
|     | T (G | ,k)=do(G | =Gk),k∈{SIS,SRS,IEIS} |     |     |     | (2) |                  | v,i |           |            |                |        |
|     | 2 i  |          | i                     | i   |     |     |     | tributeiofnode   | v.  |           |            |                |        |
T (G
where 2 i ,k) denotes trace i’s causal contrastive view; Next, node attribute aggregation is conducted. For a node,
T (·,·) represents thegeneration strategy ofcausal contrastive different attributes have different importance. Hence, the soft-
2
views; Gk describes the SETG of trace i’s direct cause k. The attention mechanism is applied to describe the importance of
i
specific detailsof causalinterventions aregiven asfollows. differentattributes.Indetail,welearnanormalizedimportance
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on March 20,2026 at 23:38:31 UTC from IEEE Xplore.  Restrictions apply.

2588 IEEETRANSACTIONSONSOFTWAREENGINEERING,VOL.50,NO.10,OCTOBER2024
Anexampleofdo(G i=G SIS).
Fig.4. i
eoi
(cid:2)
|     |     |     |     | a = |     |     |     |     |     |     | (5) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     | i   |     | eoj |     |     |     |     |     |
j∈A(cid:3)
|     |     |     |     | ht     |     | ×ht |     |     |     |     |     |
| --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     | =tanh( |     | a i | )   |     |     |     | (6) |
|     |     |     |     | v      |     |     | v,i |     |     |     |     |
i∈A
|     |     |     | where      | o denotes |             | the attention | coefficient    |            | matrix        | of node | at- |
| --- | --- | --- | ---------- | --------- | ----------- | ------------- | -------------- | ---------- | ------------- | ------- | --- |
|     |     |     | tributes;  | W         | and         | b are         | the parametric |            | weight        | matrix  | and |
|     |     |     |            |           | f           | f             |                |            |               |         |     |
|     |     |     | parametric |           | bias matrix | of            | attribute      | attention, | respectively; |         | o   |
i
|     |     |     | and | a i represent |     | the attention | coefficient |     | and the | normalized |     |
| --- | --- | --- | --- | ------------- | --- | ------------- | ----------- | --- | ------- | ---------- | --- |
Fig.5. Anexampleofdo(G i=G SRS).
i attenti oncoefficientofattributei,respectively;Arepresentsthe
node attributeset.
|     |     |     |               | b) Inter-Neighbor |           | Aggregation: |           | Inspired | by            | HEAT      | [23], |
| --- | --- | --- | ------------- | ----------------- | --------- | ------------ | --------- | -------- | ------------- | --------- | ----- |
|     |     |     | the           | inter-neighbor    |           | aggregation  | mechanism |          | is            | designed. | In    |
|     |     |     | SETGs,        | nodes             | represent | service      | events    | and      | edges         | describe  | the   |
|     |     |     | relationships |                   | between   | them.        | They      | need to  | be considered |           | sepa- |
ratelyintheinter-neighboraggregationsincetheyhavedifferent
meanings.
Fornodes,differenttypesofnodesmaylieindifferentfeature
|     |     |     | space                 | and            | have different | feature                             |     | dimensions | [22]. | Therefore, |        |
| --- | --- | --- | --------------------- | -------------- | -------------- | ----------------------------------- | --- | ---------- | ----- | ---------- | ------ |
|     |     |     | a type-specific       |                | linear         | transformation                      |     | is applied |       | for nodes  | to     |
|     |     |     | project               | their          | vector         | representations                     |     | into the   | same  | latent     | space  |
|     |     |     | before                | inter-neighbor |                | aggregation.                        |     | For the    | node  | v, its     | latent |
|     |     |     | vectorrepresentationh |                |                | iscalculatedbythefollowingequation: |     |            |       |            |        |
v
|     |     |     |     |     |     | h =W | ht  | +b  |     |     | (7) |
| --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- |
|     |     |     |     |     |     | v    | t v | t   |     |     |     |
Fig.6. Anexampleofdo(G i=G IEIS).
i where W t and b t represent the parametric weight matrix and
|     |     |     | parametric |     | bias matrix | of  | type t; | ht is | the attribute |     | vector |
| --- | --- | --- | ---------- | --- | ----------- | --- | ------- | ----- | ------------- | --- | ------ |
v
|     |     |     | representation |     | of nodev. |     |     |     |     |     |     |
| --- | --- | --- | -------------- | --- | --------- | --- | --- | --- | --- | --- | --- |
weighta foreachattributeandthenweightedsumallattributes
i
Foredges,theirattributesandtypeshavedifferentmeanings,
togetnodes’vectorrepresentations.Theattributevectorrepre-
|     |     |     | and | lie in different |     | feature | space [23]. | Therefore, |     | they | need to |
| --- | --- | --- | --- | ---------------- | --- | ------- | ----------- | ---------- | --- | ---- | ------- |
sentationht ofnodeviscalculatedbythefollowingequations:
v beprojectedintothesamelatentspacebeforetheinter-neighbor
| [ht ,··· | ,ht ,··· ,ht |     |     |     |     |     |     |     |     | ˆetype |     |
| -------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- |
o=ReLU(W ]+b ) (4) aggregation. The latent type vector representation and
| f v,0 | v,i v,|A| | f   |     |     |     |     |     |     |     | vu  |     |
| ----- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on March 20,2026 at 23:38:31 UTC from IEEE Xplore.  Restrictions apply.

TIANetal.:ITCRL:CAUSAL-INTERVENTION-BASEDTRACECONTRASTIVEREPRESENTATIONLEARNING 2589
latentattributevectorrepresentationˆeattr fromnodeutonode 3) Direct Causal Effect-Based Trace Contrastive Loss:
vu
v arecalculated bythefollowingequations: Inspired by Moco [24], iTCL treats trace contrastive learning
asadictionaryquerytask.Specifically,iTCLtakescausalcon-
ˆet v y u pe=LeakyReLU(W type et v y u pe+b type ) (8) trastive view as a query, its corresponding trace contrastive
ˆeattr=LeakyReLU(W eattr+b ) (9) view as positive key and its irrelevant trace contrastive view
vu attr vu attr
asnegativekey.Thismethodcaneffectivelyavoidtheadverse
where W type and b type are the parametric weight matrix and effects of artificially defined contrastive views on trace repre-
parametricbiasmatrixofedgetype;W attr andb attr represent sentation learning. Trace contrastive views T 1 (G i ) and causal
theparametricweightmatrixandparametricbiasmatrixofedge contrastive views T (G ,k) share the same trace encoder. The
2 i
attribute; etype denotes the vector representation of the edge specific calculation process of their vector representations is
vu
typefromnodeutonodev;eattr describestheattributevector given asfollows.
vu
representation oftheedge fromnodeutonode v. (cid:8)
H = f(T (G ))
Next, the inter-neighbor aggregation is conducted. In this i 1 i
process, the soft-attention mechanism is used to describe the Hˆk =f(T (G ,k)),k∈{SIS,SRS,IEIS} (15)
i 2 i
importance of different nodes. In detail, the aggregation mes-
wheref(·)representsthetraceencoderbasedonheterogeneous
sageisfirstcalculatedbasedonnodevectorrepresentationsand
edge vector representations. And then, we learn a normalized graphneuralnetworks;H i
andHˆk
i arethevectorrepresentation
importance weight for each neighbor and weighted sum all ofT 1 (G i ) andT 2 (G i ,k), respectively.
neighbors’aggregationmessage.Besides,theresidualisusedto Basedonthedirectcausaleffectbetweencausalcontrastive
avoidoverfitting.Thespecificprocessisgivenbythefollowing viewandtracecontrastiveview,Directcausaleffect-basedtrace
equations: contrastive loss(DCE-TCL)isdesigned asfollows.
M =W [h ,ˆeattr]+b (10) 1 (cid:3)m exp(DCE(Hˆk ,H )/τ)
vu r u vu (cid:4) r (cid:5) (cid:6) (cid:7) L=− log (cid:2) i i (16)
o vu =LeakyReLU W A h v ,h u ,ˆet v y u pe,ˆea vu ttr +b A (11) m i=1 m j=1 exp(DCE(Hˆk i ,H j )/τ)
a = (cid:2) eovu (12) whereLdenotesthetracecontrastiveloss;τ isthetemperature
h vu =h p + ∈ε t ( a v n ) h eo ( vp (cid:3) a ×M ) (13) p D a C ra E m ( e H t ˆ e k i r; , m H i r ) ep re r p es re e s n e ts nt t s he th n e um di b re e c r t o c f a s u a s m al pl e e f s fe i c n t a b m et i w ni e - e b n at H c ˆ h k i ;
v v vu vu
and H .
u∈ε(v) i
AsshowninEquation14and15,H istheattentionpooling
i
where M vu denotes the aggregation message from node u result of SEs belonging to T 1 (G i ) while Hˆk i is the attention
to node v; W r and b r are the parametric weight matrix and pooling result of SEs belonging to T 2 (G i ,k). According to
parametric bias matrix of inter-neighbor aggregation, respec- Equation1and2,T (G ,k)isasubgraphofT (G ).Therefore,
2 i 1 i
tively;W
A
andb
A
representtheparametricweightmatrixand
thereisalinearcausalrelationshipbetweenH
andHˆk
,which
parametricbiasmatrixofneighborattention,respectively;o i i
vu isgiven asfollows.
and a are the attention coefficient and normalized attention
vu (cid:3)
coefficient from node u to node v, respectively; ε(v) denotes H = α ×Hˆk (17)
i k i
theneighbornodesetofnodev;h isthevectorrepresentation
v k∈{SIS,SRS,IEIS}
ofnode v.
where α denotes the direct causal effect parameter between
c) Trace Pooling and Projection: After inter-neighbor k
aggregation, trace representations need to be calculated based H i and
Hˆk
i .According to Equation 17, the direct causal effect
on the vector representations of all nodes in a trace. To reflect parameter α k canbecalculated asfollows.
differentcontributionsofnodesforatrace,theattentionpooling
is applied to calculate trace representations. The trace pooling α =
(cid:5)H
i
(cid:5)×(cid:5)Hˆk
i
(cid:5)
×cos(H ,Hˆk )
resultiscalculated bythefollowingequation: k Hˆk·Hˆk i i
(cid:3) (cid:2) i i
H= ReLU(W g [ht v ,h v ]+b g )(cid:4)ReLU(W p [ht v ,h v ]+b p ) − l∈{SIS,SRS,IEIS}∧l(cid:4)=k α l
×Hˆl
i
·Hˆk
i (18)
v∈V Hˆk·Hˆk
(14) i i
AsshowninEquation18,thereisalinearrelationshipbetween
whereHisthetracepresentation;W g andb g aretheparamet- thedirectcausaleffectparameterα betweenH andHˆk andthe
ric weight matrix and parametric bias matrix of node feature k i i
cosinesimilaritybetweenthem.Therefore,thecosine-similarity
transformation, respectively; W and b are the parametric
p p is used to describe the direct causal effect. Equation 16 is
weight matrix and parametric bias matrix of node attention,
modified as follows.
respectively.
Finally,followingpreviousresearch[16],[17],[18],iTCRL 1 (cid:3)m exp(cos(Hˆk ,H )/τ)
appliesatwo-layerperceptrontoenhancetheexpressionability L=− m log (cid:2) m exp(cos i (Hˆk i ,H )/τ) (19)
oftracerepresentations. i=1 j=1 i j
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on March 20,2026 at 23:38:31 UTC from IEEE Xplore. Restrictions apply.

2590 IEEETRANSACTIONSONSOFTWAREENGINEERING,VOL.50,NO.10,OCTOBER2024
| AsshowninEquation19,thereisalargeoverlapofpositive |     |     |     |     |     |     |     |     |     | TABLEII |     |     |     |     |
| -------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- |
samplepairsandnegativesamplepairssincedifferenttracesare DETAILSOFDATASETS
likelytohavesamecausalcontrastiveviews.Thisproblemleads
to conflicting optimization direction. To solve this problem, Datasets Instances Normal Anomalous Classes
| Equation19needstobeadjusted.AsshowninEquation17,H |     |     |                                  |     |     |     | j   |     |     |     |        |       |     |     |
| ------------------------------------------------- | --- | --- | -------------------------------- | --- | --- | --- | --- | --- | --- | --- | ------ | ----- | --- | --- |
|                                                   |     |     |                                  |     |     |     |     | TT  |     | 45  | 151911 | 15138 |     | 57  |
| istheweightedsumofallHˆk                          |     |     | .Therefore,thedirectcausaleffect |     |     |     |     |     |     |     |        |       |     |     |
|                                                   |     |     | j                                |     |     |     |     | SN  |     | 21  | 13612  | 1106  |     | 10  |
Hˆk
minimization between and H j can be indirectly ensured OB 11 56920 11882 12
i
|               |              |            |            |        |         | Hˆk | Hˆl       |     |     |     |     |     |     |     |
| ------------- | ------------ | ---------- | ---------- | ------ | ------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
| by minimizing |              | the direct | causal     | effect | between |     | i and j . |     |     |     |     |     |     |     |
| Equation      | 19isadjusted |            | asfollows. |        |         |     |           |     |     |     |     |     |     |     |
(cid:3)m exp(cos(Hˆk (cid:129) TrainTicket (TT). This dataset is collected from the
|     |     | 1   |     |     | ,H  | )/τ) |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
L=− log i i (20) Train Ticket microservice system [11], [27], [28] com-
(cid:2)
|     |     | m   | m   | exp(cos(Hˆk |     | ,Hˆl )/τ) |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | ----------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
i=1 i j posed of 45 microservices, which is currently the largest
j=1
|     |     |     |     |     |     |     |     | andmostcomplex |     | open | sourcemicroservicesystemwith |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ---- | ---------------------------- | --- | --- | --- |
IV. EVALUATION our knowledge. Based on this system, we implement a
|     |     |     |     |     |     |     |     | normal | version | and five | fault | versions | (including | Mono- |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | ------- | -------- | ----- | -------- | ---------- | ----- |
iTCRLisimplementedusingPython3.7,PyTorch1.11.0and
|               |           |              |       |          |                      |     |          | lithic Fault, | Configuration |             | Fault,       | CPU      | Exhaustion | Fault,      |
| ------------- | --------- | ------------ | ----- | -------- | -------------------- | --- | -------- | ------------- | ------------- | ----------- | ------------ | -------- | ---------- | ----------- |
| PyTorch       | Geometric | 2.1.0.       | Based | on       | this implementation, |     | the      |               |               |             |              |          |            |             |
|               |           |              |       |          |                      |     |          | Network       | Fault,        | and Mixture |              | Fault of | CPU and    | Network),   |
| effectiveness | of        | the proposed |       | approach | is evaluated         |     | with the |               |               |             |              |          |            |             |
|               |           |              |       |          |                      |     |          | and deployed  |               | them on     | a Kubernetes | cluster  |            | composed of |
followingthreetasks:
|                 |                 |         |            |                |               |                  |          | 6 machines | with       | Intel     | Core   | i7-4790 | 3.60GHz        | CPU and   |
| --------------- | --------------- | ------- | ---------- | -------------- | ------------- | ---------------- | -------- | ---------- | ---------- | --------- | ------ | ------- | -------------- | --------- |
| (cid:129) Trace | Classification. |         | Trace      | Classification |               | aims             | to accu- |            |            |           |        |         |                |           |
|                 |                 |         |            |                |               |                  |          | 8GB RAM.   | 151911     | normal    | traces | and     | 15138          | anomalous |
| rately          | identify        | traces  | according  |                | to trace      | representations, |          |            |            |           |        |         |                |           |
|                 |                 |         |            |                |               |                  |          | traces are | collected. | According |        | to the  | root operation | and       |
| which           | benefits        | various | downstream |                | traceanalysis |                  | tasks.   |            |            |           |        |         |                |           |
(cid:129) TraceAnomalyDetection.Traceanomalydetectionaims span number of traces, traces are divided into 57 classes.
Fortracecontrastivelearning,traceclassificationandtrace
toaccuratelydetectanomalyofmicroservicesystemsac-
|                 |                         |          |       |            |        |               |        | sampling,       | the                          | normal traces | are | divided   | into    | the training, |
| --------------- | ----------------------- | -------- | ----- | ---------- | ------ | ------------- | ------ | --------------- | ---------------------------- | ------------- | --- | --------- | ------- | ------------- |
| cording         | totracerepresentations. |          |       |            |        |               |        |                 |                              |               |     |           |         |               |
|                 |                         |          |       |            |        |               |        | validation      | andtestingsetsof121529(80%), |               |     |           |         | 15191(10%)    |
| (cid:129) Trace | Sampling.               |          | Trace | sampling   | aim    | to collect    | traces |                 |                              |               |     |           |         |               |
|                 |                         |          |       |            |        |               |        | and 15191(10%), |                              | respectively. |     | For trace | anomaly | detec-        |
| as few          | as                      | possible | while | preserving | system | observability |        |                 |                              |               |     |           |         |               |
according totracerepresentations. tiontask,allanomalous traces areputintotestingset.
|            |     |                    |     |                   |     |     |         | (cid:129) SocialNetwork |     | (SN)[25].Thisdatasetprovidedby[25]. |            |         |     |              |
| ---------- | --- | ------------------ | --- | ----------------- | --- | --- | ------- | ----------------------- | --- | ----------------------------------- | ---------- | ------- | --- | ------------ |
| Bythethree |     | tasks,thefollowing |     | researchquestions |     |     | need to |                         |     |                                     |            |         |     |              |
|            |     |                    |     |                   |     |     |         | It is collected         |     | from                                | the Social | Network |     | microservice |
beanswered:
|                |     |          |                      |     |     |           |         | system        | [29], | which is             | a broadcast-style |     | social | network      |
| -------------- | --- | -------- | -------------------- | --- | --- | --------- | ------- | ------------- | ----- | -------------------- | ----------------- | --- | ------ | ------------ |
| (cid:129) RQ1: | How | much     | does hyperparameters |     |     | influence | the ef- |               |       |                      |                   |     |        |              |
|                |     |          |                      |     |     |           |         | site composed |       | of 21 microservices. |                   | In  | this   | experiments, |
| fectiveness    |     | ofiTCRL? |                      |     |     |           |         |               |       |                      |                   |     |        |              |
|                |     |          |                      |     |     |           |         | 13612         |       |                      | 1106              |     |        |              |
(cid:129) RQ2:HoweffectiveisiTCRLintraceclassificationcom- normal traces and anomalous traces of this
|       |                |     |     |     |     |     |     | dataset     | are used. | According |        | to the      | root operation | and         |
| ----- | -------------- | --- | --- | --- | --- | --- | --- | ----------- | --------- | --------- | ------ | ----------- | -------------- | ----------- |
| pared | withbaselines? |     |     |     |     |     |     |             |           |           |        |             |                |             |
|       |                |     |     |     |     |     |     | span number | of        | traces,   | traces | are divided | into           | 10 classes. |
(cid:129) RQ3:HoweffectiveisiTCRLintraceanomalydetection
|          |     |                |     |     |     |     |     | For trace       | contrastive |            | learning, | trace      | classification | and      |
| -------- | --- | -------------- | --- | --- | --- | --- | --- | --------------- | ----------- | ---------- | --------- | ---------- | -------------- | -------- |
| compared |     | withbaselines? |     |     |     |     |     |                 |             |            |           |            |                |          |
|          |     |                |     |     |     |     |     | trace sampling, |             | the normal |           | traces are | divided        | into the |
(cid:129) RQ4:HoweffectiveisiTCRLintracesamplingcompared
|     |     |     |     |     |     |     |     | training, | validation | and | testing | sets | of 10890(80.00%), |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ---------- | --- | ------- | ---- | ----------------- | --- |
withbaselines?
1361(10.00%)and1361(10.00%),respectively.Fortrace
(cid:129) RQ5:HowrobustisiTCRLinthreeevaluationtaskscom-
|       |                |     |     |     |     |     |     | anomaly | detection | task, | all anomalous |     | traces | are put into |
| ----- | -------------- | --- | --- | --- | --- | --- | --- | ------- | --------- | ----- | ------------- | --- | ------ | ------------ |
| pared | withbaselines? |     |     |     |     |     |     |         |           |       |               |     |        |              |
testingset.
| (cid:129) RQ6: | How | much | does | iTCL contribute |     | to the | effective- |     |     |     |     |     |     |     |
| -------------- | --- | ---- | ---- | --------------- | --- | ------ | ---------- | --- | --- | --- | --- | --- | --- | --- |
(cid:129) OnlineBoutique(OB)[26].Thisdatasetprovidedby[26].
nessofiTCRLcomparedwithtraditionalgraphcontrastive
ItiscollectedfromtheOnlineBoutiquemicroservicesys-
| learning | approaches? |     |     |     |     |     |     |           |       |       |            |              |     |        |
| -------- | ----------- | --- | --- | --- | --- | --- | --- | --------- | ----- | ----- | ---------- | ------------ | --- | ------ |
|          |             |     |     |     |     |     |     | tem [30], | which | is an | e-commerce | microservice |     | system |
composedof11microservices.Inthisexperiments,56920
| A. Experimental |     | Setup |     |     |     |     |     |     |     |     |     |     |     |     |
| --------------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
normaltracesand11882anomaloustracesofthisdataset
1) Datasets: Experimentswereconductedonthreedatasets areused.Accordingtotherootoperationandspannumber
collected from Train Ticket microservice system, the Social oftraces,tracesaredividedinto12classes.Fortracecon-
Network microservice system and the Online Boutique mi- trastive learning, trace classification and trace sampling,
croservicesystem.Thesethreemicroservicesystemshavebeen the normal traces are divided into the training, validation
widely used in previous studies [11], [25], [26], [27], [28]. and testing sets of 45536(80.00%), 5692(10.00%) and
Among them, the Train Ticket microservice system has com- 5692(10.00%), respectively. For trace anomaly detection
plexservicedependencies,whichmakesserviceruntimeevents task,allanomalous tracesareput intotestingset.
more important for trace analysis. The last two microservice 2) EvaluationMetrics: Fortraceclassificationtask,Macro-
systems have simple service dependencies, which makes ser- F1andMicro-F1areusedtoevaluateitseffectiveness.Fortrace
vice invocation events more important for trace analysis. The anomaly detection task, F1-Score is used to evaluate its effec-
detailsofthedatasets areshown inTableII. tiveness. For trace sampling task, Coverage [31] and Entropy
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on March 20,2026 at 23:38:31 UTC from IEEE Xplore.  Restrictions apply.

TIANetal.:ITCRL:CAUSAL-INTERVENTION-BASEDTRACECONTRASTIVEREPRESENTATIONLEARNING 2591
Fig.7. ImpactofhyperparameterLonTTdataset.
[31] are used to evaluate its effectiveness. For the impact of (cid:129) SETG-HTE-AutoGCL. It is derived by replacing the
hyperparameters, all evaluation tasks need to be comprehen- iTCLofiTCRLwithAutoGCL.
sively considered. Therefore, an impact score function is de- For the above baselines, GraphCL, JOAO and AutoGCL
finedbasedonallevaluationmetrics,whichisgivenasfollows. provide open-source implementations. Therefore, we directly
usethem.Forotherbaselines,wedevelopthembasedontheir
|           | (cid:3)C | (cid:3)C | −min   |         | papers.                           |
| --------- | -------- | -------- | ------ | ------- | --------------------------------- |
|           | 1        | × 1      | m i,j  | k m k,j |                                   |
| Score(i)= | m        |          |        |         |                                   |
|           | C i,j    | C max    | m −min | m       |                                   |
|           |          |          | k k,j  | k k,j   |                                   |
|           | j=1      | j=1      |        |         |                                   |
|           |          |          |        | (21)    | B. RQ1: Impact of Hyperparameters |
iTCRLhasfourimportanthyperparameters:thehiddenlayer
where i is the hyperparameter value; j denotes an evaluation number L, the temperature parameter τ, the embedding di-
metric;C representsthenumberofevaluationmetrics;kisthe mension D and the learning rate η. They determine the itera-
number ofhyperparameter values. tionsofinter-neighboraggregationonSETGs,theattentionfor
3) Settings: To ensure the fairness of experiments, all ex- causal contrastive views, the size of trace representation vec-
periments were conducted on a server with Intel Core i7- torsandtheconvergencestatusoftracerepresentationmodels,
| 127002.10GHzCPU,64GBRAM,RTX4080with16GBGPU |     |     |     |     | respectively.                                  |
| ------------------------------------------ | --- | --- | --- | --- | ---------------------------------------------- |
| memory.                                    |     |     |     |     | Figs.7–10showtheimpactofhyperparameterLoniTCRL |
4) Baselines: To evaluate the effectiveness of iTCRL, four when other hyperparameters are fixed. As show in Figs. 7–9,
theeffectivenessoftraceclassificationdropswithL,andtheef-
| tracerepresentation | approaches | areselected | asbaselines. |     |     |
| ------------------- | ---------- | ----------- | ------------ | --- | --- |
(cid:129) OperationCountVector(OCV)[32].Arule-basedtrace fectivenessoftraceanomalydetectionfirstrisesandthendrops
representation approach. This approach represents traces withL.TheeffectivenessoftracesamplingdropswithLonTT
basedonserviceinvocationoperations,whereeachdimen- dataset and retains stable on other datasets. The reason is that
sionrepresentsaserviceinvocationoperationanditsvalue bigger L leads iTCRL to over-smoothing, but the information
istheinvocation number ofthecorresponding operation. lossinsomeextentleadsabnormaltracestodeviatefurtherfrom
(cid:129) ServiceTraceVector(STV)[9].Arule-basedtracerepre- the normal pattern, which benefits trace anomaly detection.
sentationapproach.Thisapproachrepresentstracesbased As shown in Fig. 10, the best comprehensive performance is
onserviceinvocationpathsandresponsetime,whereeach achieved atL=1onthethreedatasets.
dimensiondenotesaserviceinvocationpathanditsvalue Figs. 11–14showtheimpactofhyperparameterτ oniTCRL
isthecorresponding response time. when other hyperparameters are fixed. As show in Figs. 11–
(cid:129) TraceCRL [27]. A GNN-based trace representation ap- 13, the effectiveness of trace classification decreases with τ.
proach. This approach combines graph neural network The effectiveness of trace anomaly detection first rises and
withcontrastive learning tolearntracerepresentations. then drops with τ on OB dataset while dropping with τ on
(cid:129) STEAM [31]. A GNN-based trace representation ap- other datasets. The effectiveness of trace sampling rises with
proach.Thisapproachincorporatesgraphneuralnetwork τ on TT dataset, and retains stable on other datasets. The
withdomainknowledgeoftracecomparisonthroughlog- reason is that bigger τ leads iTCRL to allocate less attention
ical clauses tolearntracerepresentations. for direct causes difficult to learn, which makes trace rep-
ToverifythecontributionofiTCL,wederivethreevariants resentations indistinguishable. As shown in Fig. 14, the best
of iTCRL by replacing iTCL with GraphCL [17], JOAO [18] comprehensive performance is achieved at τ =0.05 on the
| and AutoGCL | [16]. |     |     |     | threedatasets. |
| ----------- | ----- | --- | --- | --- | -------------- |
(cid:129) SETG-HTE-GraphCL. It is derived by replacing the Figs.15–18showtheimpactofhyperparameterDoniTCRL
iTCLofiTCRLwithGraphCL. whenotherhyperparametersarefixed.AsshowinFigs.15–17,
(cid:129) SETG-HTE-JOAO. It is derived by replacing the iTCL theeffectivenessoftraceclassificationfirstrisesandthendrops
ofiTCRLwithJOAO. with D on TT dataset and SN dataset while it first drops and
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on March 20,2026 at 23:38:31 UTC from IEEE Xplore.  Restrictions apply.

2592 IEEETRANSACTIONSONSOFTWAREENGINEERING,VOL.50,NO.10,OCTOBER2024
Fig.8. ImpactofhyperparameterLonSNdataset.
Fig.9. ImpactofhyperparameterLonOBdataset.
| differently | with η on     | different    | datasets |       | and their | best per-   |
| ----------- | ------------- | ------------ | -------- | ----- | --------- | ----------- |
| formance    | is achieved   | at different |          | η. As | shown     | in Fig. 22, |
| the best    | comprehensive | performance  |          | is    | achieved  | at η=       |
10−4,10−5,10−4
|             | onTT,SNand |               | OBdataset,respectively. |     |       |             |
| ----------- | ---------- | ------------- | ----------------------- | --- | ----- | ----------- |
| In summary, | the best   | configuration |                         | of  | iTCRL | is given in |
Table III.
| C. RQ2:         | Effectiveness     | for Trace | Classification |                 |          |           |
| --------------- | ----------------- | --------- | -------------- | --------------- | -------- | --------- |
| To evaluate     | the effectiveness |           | of             | iTCRL           | in terms | of trace  |
| classification, | we provide        | the       | trace          | representations |          | generated |
Fig.10. ComprehensiveImpactofhyperparameterLonthreedatasets. by each trace representation approach for the SVM classifier.
| To minimize | the impact          | of  | randomness, |        | the SVM | classifier   |
| ----------- | ------------------- | --- | ----------- | ------ | ------- | ------------ |
| is run 10   | times independently |     | and         | report | their   | average. The |
then rises on OB dataset. The effectiveness of trace anomaly experimental resultsaregiven inTableIV.
detection firsts drops and then rises with D on OB dataset As shown in Table IV, iTCRL outperforms all baselines on
while rising with D on other datasets. The effectiveness of TT dataset. This is because it considers service events that
trace sampling retains stable on OB dataset, and rises with denotesmeaningful,singularpointintimeduringtheservice’s
D on other datasets. The reason is that bigger representation duration, which makes trace representation more distinguish-
dimensionleadsmodeltooverfitting,buttheoverfittinginsome able. On SN dataset and OB dataset, it is slightly worse than
extentmakesthemodelmoresensitivetounseentraces,which the best baseline, ranking second and fourth respectively. The
helps trace anomaly detection. As shown in Fig. 18, the best reason is that the scale of the Social Network microservice
comprehensive performance is achieved at D=64,32,64 on system and the Online Boutique microservice system is so
TT,SNand OBdataset,respectively. small that their traces can be distinguished by root operation
Figs.19–22showtheimpactofhyperparameterηoniTCRL alone, and the less the additional information, the better trace
when other hyperparameters are fixed. As show in Figs. classification. Comprehensively considering the effectiveness
19–21, the performance of three evaluation tasks changes ofallapproachesonthethreedatasets,iTCRLisabout3.28%
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on March 20,2026 at 23:38:31 UTC from IEEE Xplore.  Restrictions apply.

TIANetal.:ITCRL:CAUSAL-INTERVENTION-BASEDTRACECONTRASTIVEREPRESENTATIONLEARNING 2593
Fig.11. Impactofhyperparameterτ onTTdataset.
Fig.12. Impactofhyperparameterτ onSNdataset.
Fig.13. Impactofhyperparameterτ onOBdataset.
and 1.19% better than the best baseline (STEAM) in terms of
Macro-F1 andMicro-F1,respectively.
D. RQ3: Effectiveness for Trace Anomaly Detection
To evaluate the effectiveness of iTCRL in terms of trace
anomaly detection, we provide the trace representations gen-
erated by each trace representation approach for the LOF al-
gorithm. To minimize the impact of randomness, the LOF
algorithmisrepeated10timesandreporttheiraverage.TableV
shows the effectiveness evaluation results of trace anomaly
detection.
As shown in Table V, iTCRL outperforms all baselines on
Fig.14. ComprehensiveImpactofhyperparameterτ onthreedatasets. threedatasets.Indetail,itisabout24.62%,18.73%and36.7%
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on March 20,2026 at 23:38:31 UTC from IEEE Xplore. Restrictions apply.

2594 IEEETRANSACTIONSONSOFTWAREENGINEERING,VOL.50,NO.10,OCTOBER2024
Fig.15. ImpactofhyperparameterD onTTdataset.
Fig.16. ImpactofhyperparameterD onSNdataset.
Fig.17. ImpactofhyperparameterD onOBdataset.
| better than | the best | baseline (STV, | STV | and | STEAM) | on TT |
| ----------- | -------- | -------------- | --- | --- | ------ | ----- |
dataset,SNdatasetandOBdataset,respectively.Theimprove-
| ment is     | because iTCRL | considers | service     | events | that      | denotes |
| ----------- | ------------- | --------- | ----------- | ------ | --------- | ------- |
| meaningful, | singular      | point in  | time during | the    | service’s | dura-   |
tion,theirrelatedmetricsandtherelationshipsbetweenservice
events,whichallowstracerepresentationtoreflectavarietyof
| anomalies | such as                    | CPU exhaustion, | memory          |          | exhaustion | and        |
| --------- | -------------------------- | --------------- | --------------- | -------- | ---------- | ---------- |
| network   | delays, etc.               | Comprehensively |                 | consider | the        | effective- |
| ness of   | all approaches             | on the          | three datasets, |          | iTCRL      | is about   |
| 31.11%    | better thanthebestbaseline |                 | (STV).          |          |            |            |
| E. RQ4:   | Effectiveness              | for Trace       | Sampling        |          |            |            |
ToevaluatetheeffectivenessofiTCRLintermsoftracesam-
Fig.18. ComprehensiveImpactofhyperparameterD onthreedatasets. pling,wefeedthetracerepresentationsgeneratedbyeachtrace
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on March 20,2026 at 23:38:31 UTC from IEEE Xplore.  Restrictions apply.

TIANetal.:ITCRL:CAUSAL-INTERVENTION-BASEDTRACECONTRASTIVEREPRESENTATIONLEARNING 2595
Fig.19. Impactofhyperparameterη onTTdataset.
Fig.20. Impactofhyperparameterη onSNdataset.
Fig.21. Impactofhyperparameterη onOBdataset.
TABLEIII
CONFIGURATIONOFITCRL
|     | Dataset | L τ | D η |     |
| --- | ------- | --- | --- | --- |
10−4
|     | TT  | 1 0.05 | 64  |     |
| --- | --- | ------ | --- | --- |
10−5
|     | SN  | 1 0.05 | 32      |     |
| --- | --- | ------ | ------- | --- |
|     | OB  | 1 0.05 | 64 10−4 |     |
representationapproachtotheDPP[31]algorithmandsample
| 1% traces | from datasets. | To minimize | the impact of | random- |
| --------- | -------------- | ----------- | ------------- | ------- |
10
| ness, the DPP | algorithm | is repeated | times and report | their |
| ------------- | --------- | ----------- | ---------------- | ----- |
average.TableVIshowstheeffectivenessevaluationresultsof
tracesampling.AsshowninTableVI,iTCRLoutperformsall
Fig.22. ComprehensiveImpactofhyperparameterη onthreedatasets.
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on March 20,2026 at 23:38:31 UTC from IEEE Xplore.  Restrictions apply.

2596 IEEETRANSACTIONSONSOFTWAREENGINEERING,VOL.50,NO.10,OCTOBER2024
TABLEIV
EFFECTIVENESSEVALUATIONRESULTSOFTRACECLASSIFICATION
|     |     | Datasets | Metrics  | OCV STV       | TraceCRL | STEAM  | iTCRL  |
| --- | --- | -------- | -------- | ------------- | -------- | ------ | ------ |
|     |     |          | Macro-F1 | 0.7499 0.7216 | 0.4540   | 0.7919 | 0.8630 |
TT
|     |     |     | Micro-F1 | 0.7315 0.7141 | 0.6434 | 0.9215 | 0.9357 |
| --- | --- | --- | -------- | ------------- | ------ | ------ | ------ |
|     |     |     | Macro-F1 | 1.0000 0.5444 | 0.8161 | 0.9504 | 0.9862 |
SN
|     |     |     | Micro-F1 | 1.0000 0.6608 | 0.7916 | 0.9596 | 0.9879 |
| --- | --- | --- | -------- | ------------- | ------ | ------ | ------ |
|     |     |     | Macro-F1 | 1.0000 0.9976 | 0.9864 | 0.9992 | 0.9821 |
OB
|     |     |     | Micro-F1 | 1.0000 0.9984 | 0.9802 | 0.9994 | 0.9913 |
| --- | --- | --- | -------- | ------------- | ------ | ------ | ------ |
|     |     |     | Macro-F1 | 0.9166 0.7545 | 0.7522 | 0.9138 | 0.9438 |
Average
|     |     |     | Micro-F1 | 0.9105 0.7911 | 0.8051 | 0.9602 | 0.9716 |
| --- | --- | --- | -------- | ------------- | ------ | ------ | ------ |
TABLEV
EFFECTIVENESSEVALUATIONRESULTSOFTRACE
ANOMALYDETECTION
|     |     |     | Datasets OCV   | STV TraceCRL | STEAM         | iTCRL  |     |
| --- | --- | --- | -------------- | ------------ | ------------- | ------ | --- |
|     |     |     | TT 0.2594      | 0.7624       | 0.4156 0.5894 | 0.9501 |     |
|     |     |     | SN 0.1098      | 0.7855       | 0.3238 0.5387 | 0.9326 |     |
|     |     |     | OB 0.1692      | 0.6286       | 0.3966 0.7103 | 0.9710 |     |
|     |     |     | Average 0.1795 | 0.7255       | 0.3787 0.6128 | 0.9512 |     |
TABLEVI
EFFECTIVENESSEVALUATIONRESULTSOFTRACESAMPLING
|     |     | Datasets | Metrics  | OCV STV       | TraceCRL | STEAM  | iTCRL  |
| --- | --- | -------- | -------- | ------------- | -------- | ------ | ------ |
|     |     |          | Coverage | 0.5965 0.8596 | 0.7018   | 0.8421 | 0.8947 |
TT
|     |     |     | Entropy  | 2.1300 5.1744 | 2.8690 | 5.2043 | 3.1684 |
| --- | --- | --- | -------- | ------------- | ------ | ------ | ------ |
|     |     |     | Coverage | 1.0000 0.9000 | 1.0000 | 1.0000 | 1.0000 |
SN
|     |     |     | Entropy  | 2.6592 2.6007 | 2.9623 | 3.0724 | 3.0347 |
| --- | --- | --- | -------- | ------------- | ------ | ------ | ------ |
|     |     |     | Coverage | 1.0000 0.9167 | 1.0000 | 1.0000 | 1.0000 |
OB
|     |     |     | Entropy  | 2.0335 2.6403 | 2.2202 | 2.9819 | 3.0905 |
| --- | --- | --- | -------- | ------------- | ------ | ------ | ------ |
|     |     |     | Coverage | 0.8655 0.8921 | 0.9006 | 0.9474 | 0.9649 |
Average
|     |     |     | Entropy | 2.2742 3.4718 | 2.6838 | 3.7529 | 3.0979 |
| --- | --- | --- | ------- | ------------- | ------ | ------ | ------ |
baselinesonthreedatasetsintermsofCoverage.Thisisbecause F. RQ5: Robustness of iTCRL
| it considers | service events | that | denotes meaningful, | singular |     |     |     |
| ------------ | -------------- | ---- | ------------------- | -------- | --- | --- | --- |
ToevaluatetherobustnessofiTCRL,weaddnoiseto20%,
pointintimeduringtheservice’sdurationandlearntracerep-
resentations from causal perspective, which makes trace more 40% and 60% of traces in datasets and conduct comparison
distinguishable. In terms of Entropy, iTCRL is best on OB experiments. Experimental results on TT dataset, SN dataset
dataset while ranking third and second on TT dataset and SN and OBdatasetareshown inFigs.23–25, respectively.
dataset,respectively.Thereasonisthatthenumberofdifferent AsshowninFigs.23–25,iTCRLchangesalittlewithnoise
types of traces is unbalanced in TT dataset and SN dataset, ratioonthreedatasetsinallevaluationmetrics.OnTTdataset,
which makes a finer-grained trace representation mean higher the change of iTCRL with noise ratio is smaller than allbase-
CoverageandlowerEntropy.Comprehensivelyconsideringthe lines in terms of Macro-F1, F1-score, Coverage and Entropy
effectivenessofallapproachesonthethreedatasets,iTCRLis while slightly larger than STEAM in terms of Micro-F1. On
about1.85%betterthanthebestbaseline(STEAM)intermsof SN dataset, the change of iTCRL with noise ratio is smaller
Coverage whileranking thirdintermsofEntropy. thanallbaselinesinallevaluationmetrics.OnOBdataset,the
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on March 20,2026 at 23:38:31 UTC from IEEE Xplore.  Restrictions apply.

TIANetal.:ITCRL:CAUSAL-INTERVENTION-BASEDTRACECONTRASTIVEREPRESENTATIONLEARNING 2597
Fig.23. RobustnessofiTCRLonTTdataset.
Fig.24. RobustnessofiTCRLonSNdataset.
change of iTCRL with noise ratio is smaller than all base- The reason is that iTCRL learns trace representations from
lines in terms of F1-score and Coverage while slightly larger causalperspectiveandnoisedatacannotchangetraces’causal
than STEAM in terms of Macro-F1, Micro-F1 and Entropy. relationships.
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on March 20,2026 at 23:38:31 UTC from IEEE Xplore. Restrictions apply.

2598 IEEETRANSACTIONSONSOFTWAREENGINEERING,VOL.50,NO.10,OCTOBER2024
Fig.25. RobustnessofiTCRLonOBdataset.
G. RQ6: Contribution of iTCL isstillsmallerthanindustrialmicroservicesystems.Therefore,
|                |                   |                   |              |       |             |     | it is yet unknown |            | whether      | our    | evaluation      | results can  | be gen- |
| -------------- | ----------------- | ----------------- | ------------ | ----- | ----------- | --- | ----------------- | ---------- | ------------ | ------ | --------------- | ------------ | ------- |
| To evaluate    | the               | contribution      | of iTCL,     | iTCRL | is compared |     |                   |            |              |        |                 |              |         |
|                |                   |                   |              |       |             |     | eralized to       | industrial | microservice |        | systems.        | We alleviate | this    |
| with its three | variants          | SETG-HTE-GraphCL, |              |       | SETG-HTE-   |     |                   |            |              |        |                 |              |         |
|                |                   |                   |              |       |             |     | threat from       | two        | aspects.     | First, | all fault cases | are typical  | faults  |
| JOAO and       | SETG-HTE-AutoGCL. |                   | Experimental |       | results     | are |                   |            |              |        |                 |              |         |
inindustrialmicroservicesystems.Second,thesizeofcollected
given inTableVII.
|                      |          |             |                   |            |               |     | traces iscomparable |     | toindustrialsystems. |     |     |     |     |
| -------------------- | -------- | ----------- | ----------------- | ---------- | ------------- | --- | ------------------- | --- | -------------------- | --- | --- | --- | --- |
| As shown             | in Table | VII,        | iTCRL outperforms |            | all baselines |     |                     |     |                      |     |     |     |     |
| when comprehensively |          | considering | three             | evaluation | tasks.        | On  |                     |     |                      |     |     |     |     |
V. RELATEDWORKS
| TT dataset | and OB | dataset, | iTCRL outperforms |     | all baselines |     |     |     |     |     |     |     |     |
| ---------- | ------ | -------- | ----------------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
Inthissection,wefocusontherelatedworkongraphneural
intermsofMacro-F1,Micro-F1,F1-scoreandCoveragewhile
ranking second in terms of Entropy. On SN dataset, iTCRL networks,causalinference,graphcontrastivelearningandtrace
| outperformsallbaselinesinallevaluation |     |     |     | metrics.Thereason |     |     | representation. |        |           |     |              |          |     |
| -------------------------------------- | --- | --- | --- | ----------------- | --- | --- | --------------- | ------ | --------- | --- | ------------ | -------- | --- |
|                                        |     |     |     |                   |     |     | Graph           | Neural | Networks. |     | Graph Neural | Networks | aim |
isthatourproposedapproachlearnstracerepresentationsfrom
causal perspective, which avoid the creation of traces that do to learn a low-dimensional vector representation for nodes or
graphs.Brunaetal.[33]firstextendconvolutionstographdata
notexistinrealmicroservicesystems.
|            |             |     |     |     |     |     | by graph        | Laplacian | matrix.    | ChebNet | [34]              | uses a | polynomial |
| ---------- | ----------- | --- | --- | --- | --- | --- | --------------- | --------- | ---------- | ------- | ----------------- | ------ | ---------- |
|            |             |     |     |     |     |     | filter to solve | the       | efficiency | problem | of spectral-based |        | GNNs.      |
| H. Threats | to Validity |     |     |     |     |     |                 |           |            |         |                   |        |            |
Kipfetal.[35]improveChebNetbysimplifyingitsparameters
For the threats to internal validity, it mainly comes from toalleviatetheoverfittingproblem.Huangetal.[36]firstintro-
the implementation of baselines. In these baselines, GraphCL, duce random filters into graph convolution neural networks to
JOAO and AutoGCL provide open-source implementations achieve the fast build of graph convolutional network model.
[16], [17], [18]. Therefore, we directly use them. For other Hamilton et al. [37] first propose spatial-based graph neural
baselines, we can only develop them based on their papers. network framework, which effectively improve generalization
To alleviate this threat, we use same libraries to implement tounseendata.Velickovicetal.[38]firstintroducetheattention
them strictly in accordance with its paper and apply the best mechanism into graph neural networks to reflect the impor-
configuration ofhyperparameters toconduct experiments. tanceofdifferentneighbors.Fuetal.[39]extendgraphneural
Forthethreatstoexternalvalidity,itmainlycomesfromthe networks from homogeneous graphs to heterogeneous graphs
generalization ability of iTCRL. In this paper, we use experi- by metapaths. Li et al. [40] design PEGFAN to achieve the
mentaldatasetsfromtheTrainTicketmicroservicesystem,the accurate node classification in heterophilous graphs. Mo et al.
Social Network microservice system and the Online Boutique [23] propose a heterogeneous edge-enhanced graph attention
microservice system, respectively. Although they are the most networktosolvethemulti-agenttrajectorypredictionproblem.
commonly used benchmark microservice systems, their scale Li et al. [41] propose a multimodal graph learning approach
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on March 20,2026 at 23:38:31 UTC from IEEE Xplore.  Restrictions apply.

TIANetal.:ITCRL:CAUSAL-INTERVENTION-BASEDTRACECONTRASTIVEREPRESENTATIONLEARNING 2599
TABLEVII
CONTRIBUTIONSOFITCL
Datasets Metrics SETG-HTE-GraphCL SETG-HTE-JOAO SETG-HTE-AutoGCL iTCRL
| Macro-F1    | 0.6713 | 0.7878 | 0.6742 | 0.8630 |
| ----------- | ------ | ------ | ------ | ------ |
| Micro-F1    | 0.8869 | 0.8981 | 0.8464 | 0.9357 |
| TT F1-score | 0.9486 | 0.9497 | 0.9484 | 0.9501 |
| Coverage    | 0.7368 | 0.6491 | 0.7895 | 0.8947 |
| Entropy     | 3.1540 | 3.3761 | 3.6191 | 3.1684 |
| Macro-F1    | 0.9832 | 0.9703 | 0.8508 | 0.9862 |
| Micro-F1    | 0.9842 | 0.9696 | 0.8637 | 0.9879 |
SN
| F1-score    | 0.9106 | 0.8916 | 0.9158 | 0.9326 |
| ----------- | ------ | ------ | ------ | ------ |
| Coverage    | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| Entropy     | 2.9666 | 2.9794 | 3.0129 | 3.0347 |
| Macro-F1    | 0.9495 | 0.7962 | 0.8501 | 0.9821 |
| Micro-F1    | 0.9538 | 0.7837 | 0.8961 | 0.9913 |
| OB F1-score | 0.9645 | 0.9657 | 0.8190 | 0.9710 |
| Coverage    | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| Entropy     | 3.0924 | 3.0881 | 3.0222 | 3.0905 |
| Macro-F1    | 0.8680 | 0.8514 | 0.7917 | 0.9438 |
| Micro-F1    | 0.9416 | 0.8838 | 0.8687 | 0.9716 |
Average
| F1-score | 0.9412 | 0.9357 | 0.8944 | 0.9512 |
| -------- | ------ | ------ | ------ | ------ |
| Coverage | 0.9123 | 0.8830 | 0.9298 | 0.9649 |
| Entropy  | 3.0710 | 3.1479 | 3.2181 | 3.0979 |
to achieve the accurate student engagement prediction. These contrastive learning framework for recommender systems. It
researchaboutgraphneuralnetworksprovidetheoreticalbasis constructs positive/negative pairs from two simple graph
formicroservice tracerepresentation learning. augmentations, which can help recommendation in causes of
Causal Inference. Causal Inference aims to find the causal complex topology or sparse labels. Yin et al. [16] propose an
relationships between things. At present, it has been applied automated graph contrastive learning framework. It uses joint
in many domains. For example, Gan et al. [1] use Causal training strategy to learn graph view generators, which can
BayesianNetworkstocapturethecausalrelationshipsbetween dynamically suit input data. However, the above approaches
microservices, and counterfactual theory to analyze the root often create traces that do not exist in real world when they
causes of microservice systems. Ma et al. [2] apply causal aredirectlyapplied totracerepresentation learning.
inferencetoextractcausalrelationshipsbetweenmicroservices Trace Representation. Existing trace representation ap-
andidentifytherootcausesofmicroservicesystemanomalies. proaches can be divided into the rule-based approach and the
Zhang et al. [42] formulate a notion of counterfactual memo- GNN-based approach. The first usually uses the artificial de-
rization, and apply it to describe the predictions change when fined features to represent traces. This type of approaches is
aparticulardocumentismissinginNLP.Theseresearchabout veryeasytoimplementandhasgoodinterpretability.Forexam-
causalinferenceprovidetheoreticalbasisformicroservicetrace ple,OperationCountVector(OCV)[32]usesserviceinvocation
representation learning. operations and their number to represent traces. Service Trace
Graph Contrastive Learning. Existing graph contrastive Vector (STV) [9] uses service invocation paths and their re-
learning approaches usually learns graph representation sponsetimetorepresenttraces.Thesecondusuallyusemachine
vectors by maximizing the agreement between two learning based methods to learn trace representations. This
contrastive views of the same graph. You et al. [17] design type of approaches can well use the structure information and
four types of graph augmentation strategies and propose a attribute information of traces. For example, Zhang et al. [27]
graph contrastive learning framework based on them, which proposeatracerepresentationapproachbasedongraphneural
can produce graph representations of high generalization, networkandcontrastivelearning,whichcaneffectivelyusethe
transferability and robustness. The same authors [18] propose graph structured information of traces. He et al. [31] propose
aunifiedbi-leveloptimizationframeworkforGraphCL[17]to atracerepresentationapproachbasedongraphneuralnetwork
select data augmentation strategies automatically, adaptively andthedomainknowledgeoftracecomparison.Itincorporates
and dynamically, which can effectively improve the general graph neural network and domain knowledge by defining log-
applicability of GraphCL. Li et al. [43] propose a graph ical clauses, which can avoid the generation of traces that do
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on March 20,2026 at 23:38:31 UTC from IEEE Xplore.  Restrictions apply.

2600 IEEETRANSACTIONSONSOFTWAREENGINEERING,VOL.50,NO.10,OCTOBER2024
notexistinrealworld.However,theaboveapproachesrequire [8] “Opentelemetry,” OpenTelemetry.io. 2024. Accessed: Mar. 27, 2024.
well-designed graph neural network models and unsupervised [Online].Available:https://opentelemetry.io/
|     |     |     |     |     |     |     | [9] P. Liu | et al., | “Unsupervised | detection | of  | microservice | trace anomalies |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ------- | ------------- | --------- | --- | ------------ | --------------- |
learningstrategies.
throughservice-leveldeepBayesiannetworks,”inProc.IEEE31stInt.
Symp.Softw.Rel.Eng.(ISSRE),2020,pp.48–58.
VI. CONCLUSIONANDFUTUREWORK [10] P.He,J.Zhu,Z.Zheng,andM.R.Lyu,“Drain:Anonlinelogparsing
approachwithfixeddepthtree,”inProc.IEEEInt.Conf.WebServices
In summary, we propose a trace contrastive representation (ICWS),2017,pp.33–40.
learningapproachbasedoncausalintervention.Thisapproach [11] C. Zhang et al., “DeepTraLog: Trace-log combined microservice
|                   |                       |                |     |                |     |        | anomaly     | detection | through | graph-based | deep      | learning,” | in Proc. 44th |
| ----------------- | --------------------- | -------------- | --- | -------------- | --- | ------ | ----------- | --------- | ------- | ----------- | --------- | ---------- | ------------- |
| first constructs  | a Service-Event-based |                |     | Trace Graph    | for | each   |             |           |         |             |           |            |               |
|                   |                       |                |     |                |     |        | Int. Conf.  | Softw.    | Eng.    | (ICSE),     | New York, | NY, USA:   | ACM, 2022,    |
| trace to describe | the                   | runtime status | of  | service events | in  | traces | pp.623–634. |           |         |             |           |            |               |
and the complex relationships between them. Then, Causal- [12] X. Zhang et al., “Robust log-based anomaly detection on unstable log
intervention-based Trace Contrastive Learning is proposed to data,” in Proc. 27th ACM Joint Meeting Eur. Softw. Eng. Conf. Symp.
|             |                 |      |        |              |       |     | Found.      | Softw. | Eng. (ESEC/FSE), |     | New York, | NY, | USA: ACM, 2019, |
| ----------- | --------------- | ---- | ------ | ------------ | ----- | --- | ----------- | ------ | ---------------- | --- | --------- | --- | --------------- |
| learn trace | representations | from | causal | perspective, | which | can | pp.807–817. |        |                  |     |           |     |                 |
effectively aggregate the structure information and attribute [13] J.Pennington,R.Socher,andC.D.Manning,“Glove:Globalvectorsfor
wordrepresentation,”inProc.Conf.EmpiricalMethodsNaturalLang.
informationonService-Event-basedTraceGraphs.Finally,we
Process.(EMNLP),2014,pp.1532–1543.
evaluatetheeffectivenessofiTCRL,robustnessofiTCRLand [14] G. Salton and C. Buckley, “Term-weighting approaches in automatic
contributionofiTCLwiththreetasks.Experimentalresultson textretrieval,”Inf.Process.Manage.,vol.24,no.5,pp.513–523,1988.
[15] L.Baietal.,“HAQJSK:Hierarchical-alignedquantumJensen-Shannon
| three datasets | show | iTCRL outperforms |     | all baselines | in  | terms |         |           |                  |     |             |        |                  |
| -------------- | ---- | ----------------- | --- | ------------- | --- | ----- | ------- | --------- | ---------------- | --- | ----------- | ------ | ---------------- |
|                |      |                   |     |               |     |       | kernels | for graph | classification,” |     | IEEE Trans. | Knowl. | Data Eng., early |
oftraceclassification,traceanomalydetection,tracesampling
access,Apr.16,2024,doi:10.1109/TKDE.2024.3389966.
|     |     |     |     |     |     |     | [16] Y. Yin, | Q. Wang, | S.  | Huang, H. | Xiong, | and X. | Zhang, “AutoGCL: |
| --- | --- | --- | --- | --- | --- | --- | ------------ | -------- | --- | --------- | ------ | ------ | ---------------- |
andnoiserobustness,andalsovalidatethecontributionofiTCL.
|              |     |                    |     |              |          |     | Automated | graph | contrastive | learning | via | learnable | view generators,” |
| ------------ | --- | ------------------ | --- | ------------ | -------- | --- | --------- | ----- | ----------- | -------- | --- | --------- | ----------------- |
| Limitations. | We  | note that although |     | our proposed | approach |     |           |       |             |          |     |           |                   |
inProc.AAAIConf.Artif.Intell.,vol.36,no.8,2022,pp.8892–8900.
achievesbesteffectivenessinlarge-scalemicroservicesystems
|     |     |     |     |     |     |     | [17] Y. You, | T. Chen, | Y.  | Sui, T. Chen, | Z. Wang, | and | Y. Shen, “Graph |
| --- | --- | --- | --- | --- | --- | --- | ------------ | -------- | --- | ------------- | -------- | --- | --------------- |
andbestcomprehensiveresultsonalldatasets,itseffectiveness contrastive learning with augmentations,” in Proc. Adv. Neural Inf.
Process.Syst.,vol.33,2020,pp.5812–5823.
| in small-scale | microservice | systems | is  | slightly | worse than | the |              |          |          |        |       |        |                      |
| -------------- | ------------ | ------- | --- | -------- | ---------- | --- | ------------ | -------- | -------- | ------ | ----- | ------ | -------------------- |
|                |              |         |     |          |            |     | [18] Y. You, | T. Chen, | Y. Shen, | and Z. | Wang, | “Graph | contrastive learning |
bestbaselinesintermsoftraceclassification.Thissuggeststhat automated,”inProc.Int.Conf.Mach.Learn.,PMLR,2021,pp.12121–
| ourproposedapproachmoresuitableforlarge-scalemicroser- |     |     |     |     |     |     | 12132. |     |     |     |     |     |     |
| ------------------------------------------------------ | --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- |
[19] L.Yao,Z.Chu,S.Li,Y.Li,J.Gao,andA.Zhang,“Asurveyoncausal
| vice systems,and | further | improvements |     | are needed | toadapt | it  |     |     |     |     |     |     |     |
| ---------------- | ------- | ------------ | --- | ---------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
inference,”ACMTrans.Knowl.Discov.Data,vol.15,no.5,pp.1–46,
| forvarious | scaleofmicroservicesystems. |     |     |     |     |     | May2021. |     |     |     |     |     |     |
| ---------- | --------------------------- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- |
FutureWork.Severalpathsforfutureresearchesexist.First, [20] J.PearlandD.Mackenzie,TheBookofWhy:TheNewScienceofCause
andEffect.NewYork,NY,USA:BasicBooks,2018.
a more fine-grained generation method of causal contrastive [21] J.Pearl,M.Glymour,andN.P.Jewell,CausalInferenceinStatistics:
views needs to be designed based on the background of mi- APrimer.Hoboken,NJ,USA:Wiley,2016.
croservice systems. This improvement is crucial for adapting [22] X.Fu,J.Zhang,Z.Meng,andI.King,“MAGNN:Metapathaggregated
graphneuralnetworkforheterogeneousgraphembedding,”inProc.Web
theproposedapproachtovariousscaleofmicroservicesystems.
|     |     |     |     |     |     |     | Conf.(WWW), |     | NewYork,NY,USA:ACM,2020,pp.2331–2341. |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ------------------------------------- | --- | --- | --- | --- |
Second, it is essential to enhance the interpretability of the [23] X.Mo,Z.Huang,Y.Xing,andC.Lv,“Multi-agenttrajectoryprediction
model.Thisimprovementhasfar-reachingimplicationsonen- with heterogeneous edge-enhanced graph attention network,” IEEE
Trans.Intell.Transp.Syst.,vol.23,no.7,pp.9554–9567,Jul.2022.
hancingcredibilityforvariousdownstreamtasks,suchanomaly
[24] K.He,H.Fan,Y.Wu,S.Xie,andR.Girshick,“Momentumcontrastfor
detection androotanalysis.
unsupervisedvisualrepresentationlearning,”inProc.IEEE/CVFConf.
Comput.Vis.PatternRecognit.,2020,pp.9729–9738.
REFERENCES [25] C. Lee, T. Yang, Z. Chen, Y. Su, and M. R. Lyu, “Eadro: An end-
|     |     |     |     |     |     |     | to-end | troubleshooting |     | framework | for microservices |     | on multi-source |
| --- | --- | --- | --- | --- | --- | --- | ------ | --------------- | --- | --------- | ----------------- | --- | --------------- |
[1] Y. Gan, M. Liang, S. Dev, D. Lo, and C. Delimitrou, “Sage: Practical data,” in Proc. IEEE/ACM 45th Int. Conf. Softw. Eng. (ICSE), 2023,
| and scalable | ml-driven | performance | debugging | in  | microservices,” | in  | pp.1750–1762. |     |     |     |     |     |     |
| ------------ | --------- | ----------- | --------- | --- | --------------- | --- | ------------- | --- | --- | --- | --- | --- | --- |
Proc.26thACMInt.Conf.Archit.SupportProgram.Lang.Oper.Syst. [26] G. Yu, P. Chen, Y. Li, H. Chen, X. Li, and Z. Zheng, “Nezha:
(ASPLOS),NewYork,NY,USA:ACM,2021,pp.135–151. Interpretable fine-grained root causes analysis for microservices on
[2] M. Ma, W. Lin, D. Pan, and P. Wang, “ServiceRank: Root cause multi-modalobservabilitydata,”ACMJointEur.Softw.Eng.Conf.Symp.
identification of anomaly in large-scale microservice architectures,” Found.Softw.Eng.(ESEC/FSE),ser.ESEC/FSE2023,NewYork,NY,
IEEETrans.DependableSecureComput.,vol.19,no.5,pp.3087–3100, USA:ACM,2023,pp.553–565.
Sep./Oct.2022. [27] C. Zhang et al., “TraceCRL: Contrastive representation learning for
[3] A. Sriraman and T. F. Wenisch, “μ suite: A benchmark suite for microservicetraceanalysis,”inProc.30thACMJointEur.Softw.Eng.
microservices,” in Proc. IEEE Int. Symp. Workload Characterization Conf.Symp.Found.Softw.Eng.,2022,pp.1221–1232.
(IISWC),2018,pp.1–12. [28] X.Zhouetal.,“Faultanalysisanddebuggingofmicroservicesystems:
[4] L.Suresh,P.Bodik,I.Menache,M.Canini,andF.Ciucu,“Distributed Industrialsurvey,benchmarksystem,andempiricalstudy,”IEEETrans.
resourcemanagementacrossprocessboundaries,”inProc.Symp.Cloud Softw.Eng.,vol.47,no.2,pp.243–260,Feb.2021.
Comput.(SoCC),NewYork,NY,USA:ACM,2017,pp.611–623. [29] Y. Gan et al., “An open-source benchmark suite for microservices and
[5] S.Nedelkoski,J.Cardoso,andO.Kao,“Anomalydetectionfromsystem theirhardware-softwareimplicationsforcloud&edgesystems,”inProc.
tracing data using multimodal deep learning,” in Proc. IEEE 12th Int. 24th Int. Conf. Archit. Support Program. Lang. Oper. Syst. (ASPLOS),
Conf. Cloud Comput. (CLOUD), Piscataway, NJ, USA: IEEE Press, NewYork,NY,USA:ACM,2019,pp.3–18.
2019,pp.179–186. [30] “Online boutique,” Google, 2024. Accessed: Mar. 27, 2024. [Online].
[6] G. Yu et al., “MicroRank: End-to-end latency issue localization with Available:https://github.com/GoogleCloudPlatform/microservices-demo
extendedspectrumanalysisinmicroserviceenvironments,”inProc.Web [31] S. He et al., “STEAM: Observability-preserving trace sampling,” in
Conf.(WWW),NewYork,NY,USA:ACM,2021,pp.3087–3098. Proc.31stACMJointEur.Softw.Eng.Conf.Symp.Found.Softw.Eng.
[7] S. Luo et al., “Characterizing microservice dependency and perfor- (ESEC/FSE),NewYork,NY,USA:ACM,2023,pp.1750–1761.
mance: Alibaba trace analysis,” in Proc. ACM Symp. Cloud Comput. [32] P.Las-Casas,J.Mace,D.Guedes,andR.Fonseca,“Weightedsampling
(SoCC),NewYork,NY,USA:ACM,2021,pp.412–426. of execution traces: Capturing more needles and less hay,” in Proc.
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on March 20,2026 at 23:38:31 UTC from IEEE Xplore.  Restrictions apply.

TIANetal.:ITCRL:CAUSAL-INTERVENTION-BASEDTRACECONTRASTIVEREPRESENTATIONLEARNING 2601
ACMSymp.CloudComput.,(SoCC),NewYork,NY,USA:ACM,2018, Tiangang Li is currently working toward the
| pp.326–332. |     |     |     |     |     |     |     |     |     | Ph.D.degreewiththeSchoolofComputerScience, |     |     |     |     |     |
| ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------ | --- | --- | --- | --- | --- |
[33] J.Bruna,W.Zaremba,A.Szlam,andY.LeCun,“Spectralnetworksand Wuhan University, Wuhan, China. His research
locallyconnectednetworksongraphs,”2013,arXiv:1312.6203. interests include cloud computing, software engi-
[34] M.Defferrard,X.Bresson,andP.Vandergheynst,“Convolutionalneural neering, resource management, and reinforcement
networksongraphswithfastlocalizedspectralfiltering,”inProc.Adv. learning.
NeuralInf.Process.Syst.,vol.29,D.Lee,M.Sugiyama,U.Luxburg,I.
Guyon,andR.Garnett,Eds.,Barcelona,Spain:CurranAssociates,Inc.,
2016.
[35] T.N.KipfandM.Welling,“Semi-supervisedclassificationwithgraph
| convolutional |     | networks,” | in Proc. | Int. | Conf. Learn. | Representations, |     |     |     |     |     |     |     |     |     |
| ------------- | --- | ---------- | -------- | ---- | ------------ | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
2016,pp.2713–2726.
| [36] C. Huang, | M.  | Li, F.   | Cao, H. | Fujita, Z.     | Li, and    | X. Wu, | “Are graph |     |     |          |      |     |             |          |           |
| -------------- | --- | -------- | ------- | -------------- | ---------- | ------ | ---------- | --- | --- | -------- | ---- | --- | ----------- | -------- | --------- |
|                |     |          |         |                |            |        |            |     |     | Mengting | Yuan | is  | a Professor | with the | School of |
| convolutional  |     | networks | with    | random weights | feasible?” | IEEE   | Trans.     |     |     |          |      |     |             |          |           |
PatternAnal.Mach.Intell.,vol.45,no.3,pp.2751–2768,Mar.2023. ComputerScience,WuhanUniversity.Hisresearch
interestsincludeprogramminglanguages,compiler
| [37] W. Hamilton, |     | Z. Ying, | and | J. Leskovec, | “Inductive | representation |     |     |     |     |     |     |     |     |     |
| ----------------- | --- | -------- | --- | ------------ | ---------- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
technology,andsoftwareengineering.
| learning         | on large  | graphs,” | in          | Proc. Adv. | Neural      | Inf. Process. | Syst.,     |     |     |     |     |     |     |     |     |
| ---------------- | --------- | -------- | ----------- | ---------- | ----------- | ------------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
| vol. 30,         | I. Guyon, | U.       | V. Luxburg, | S. Bengio, | H.          | Wallach,      | R. Fergus, |     |     |     |     |     |     |     |     |
| S. Vishwanathan, |           | and      | R. Garnett, | Eds.,      | Long Beach, | USA:          | Curran     |     |     |     |     |     |     |     |     |
Associates,Inc.,2017.
[38] P.Velicˇkovic´,G.Cucurull,A.Casanova,A.Romero,P.Liò,andY.Ben-
| gio, “Graph | attention |     | networks,” | in Int. | Conf. Learn. | Representations, |     |     |     |     |     |     |     |     |     |
| ----------- | --------- | --- | ---------- | ------- | ------------ | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
2018.
[39] X.Wangetal.,“Heterogeneousgraphattentionnetwork,”inProc.World
WideWebConf.,(WWW),NewYork,NY,USA:ACM,2019,p.2022–
| 2032. |     |     |     |     |     |     |     |     |     | Ruijin | Wang | is an | Associate | Professor | with the |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | ---- | ----- | --------- | --------- | -------- |
[40] J. Li, R. Zheng, H. Feng, M. Li, and X. Zhuang, “Permutation School of Information and Software Engineering,
equivariant graph framelets for heterophilous graph learning,” IEEE UniversityofElectronicScienceandTechnologyof
China,Chengdu,China.HeisaSeniorMemberof
| Trans. | Neural | Netw. Learn. | Syst., | early | access, | Mar. 14, | 2004, doi: |     |     |     |     |     |     |     |     |
| ------ | ------ | ------------ | ------ | ----- | ------- | -------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
10.1109/TNNLS.2024.3370918. the China Computer Federation, a member of the
[41] M. Li, X. Zhuang, L. Bai, and W. Ding, “Multimodal graph learning Asia-PacificArtificialIntelligenceAssociation,and
based on 3D Haar semi-tight framelet for student engagement predic- theSecretary-GeneraloftheChengduBranchofthe
tion,”Inf.Fusion,vol.105,2024,Art.no.102224. InternationalComputerSociety.Additionally,heis
[42] C.Zhang,D.Ippolito,K.Lee,M.Jagielski,F.Tramer,andN.Carlini, aVisitingScholarwiththeNorthwesternUniversity,
“Counterfactualmemorizationinneurallanguagemodels,”inProc.Adv. United States and a high-level overseas talent in
NeuralInf.Process.Syst.,vol.36,A.Oh,T.Naumann,A.Globerson,K. Sichuan Province. His research interests include
Saenko, M. Hardt, and S. Levine, Eds., Curran Associates, Inc., 2023, cloud-edge intelligent computing, data processing, artificial intelligence, in-
formationsecurity,andblockchain.
pp.39321–39362.
[43] M.Li,L.Zhang,L.Cui,L.Bai,Z.Li,andX.Wu,“BLoG:Bootstrapped
| graph | representation | learning |     | with local | and global | regularization | for |     |     |     |     |     |     |     |     |
| ----- | -------------- | -------- | --- | ---------- | ---------- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
recommendation,”PatternRecognit.,vol.144,2023,Art.no.109874. YishiZhaoreceivedtheM.Sc.andPh.D.(Distinc-
tion)degreesincomputingsciencefromNewcastle
|     |     |     |     |     |     |     |     |     |     | University, |     | in 2006 | and 2011, | respectively. | He is |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ------- | --------- | ------------- | ----- |
Xiangbo Tian is currently working toward the a Lecturer with the School of Computer Science,
|     |     |     |     |     |     |     |     |     |     | China | University | of  | Geosciences, | Wuhan, | China. |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | ---------- | --- | ------------ | ------ | ------ |
Ph.D.degreewiththeSchoolofComputerScience,
Hisresearchinterestsincludesoftwareperformance
WuhanUniversity,Wuhan,China.Hisresearchin-
engineering,intelligentdecision-making,andappli-
terestsincludemicroservicesandAIOps.
cationsofblockchainanddigitaltwin.
|     |     |     |      |                |      |            |         |     |     | Jianga   | Shang(Member,IEEE)receivedthePh.D. |          |            |                 |          |
| --- | --- | --- | ---- | -------------- | ---- | ---------- | ------- | --- | --- | -------- | ---------------------------------- | -------- | ---------- | --------------- | -------- |
|     |     |     |      |                |      |            |         |     |     | degree   | in                                 | computer | system     | architecture    | from     |
|     |     |     |      |                |      |            |         |     |     | Huazhong | University                         |          | of Science | and Technology. |          |
|     |     |     |      |                |      |            |         |     |     | He       | is a Professor                     |          | with the   | School of       | Computer |
|     |     | Shi | Ying | is a Professor | with | the School | of Com- |     |     |          |                                    |          |            |                 |          |
ScienceandaSeniorResearcherwiththeNational
puter Science, Wuhan University, Wuhan, China. EngineeringResearchCenterforGeographicInfor-
Hisresearchinterestsincludesoftwareengineering,
|     |     |     |     |     |     |     |     |     |     | mation | System, | China | University | of Geosciences, |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | ------- | ----- | ---------- | --------------- | --- |
intelligentoperationandmaintenancemanagement,
|     |     |       |           |     |               |           |     |     |     | Wuhan.   | He       | is also | the Director | of Human–Cyber– |          |
| --- | --- | ----- | --------- | --- | ------------- | --------- | --- | --- | --- | -------- | -------- | ------- | ------------ | --------------- | -------- |
|     |     | cloud | computing | and | cloud service | software, | and |     |     |          |          |         |              |                 |          |
|     |     |       |           |     |               |           |     |     |     | Physical | Software |         | for Smart    | Spaces Lab      | with the |
artificialintelligence.
CUGandamemberoftheACM,SpecialCommit-
teeonSoftwareEngineeringwithChinaComputer
|     |     |     |     |     |     |     |     | Federation. | His research | interests | include | mobile | and | pervasive | computing, |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ------------ | --------- | ------- | ------ | --- | --------- | ---------- |
softwaretechnologyforhuman–cyber–physicalsystems,positioningandnav-
igationofpedestrian,androboticsforsmartspaces.
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on March 20,2026 at 23:38:31 UTC from IEEE Xplore.  Restrictions apply.