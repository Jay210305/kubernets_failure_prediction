ADAPTIVEROOTCAUSELOCALIZATIONFORMICROSERVICESYSTEMSWITHMULTI-AGENTRECURSION-OF-THOUGHT 1
Adaptive Root Cause Localization for Microservice
Systems with Multi-Agent Recursion-of-Thought
Lingzhe Zhang, Tong Jia∗, Kangjin Wang, Weijie Hong, Chiming Duan,
Minghua He, and Ying Li∗, Member, IEEE
Abstract—As contemporary microservice systems become in- within microservice systems [11]–[18]. Each request typically
creasingly popular and complex—often comprising hundreds or follows complex invocation chains, with each chain involving
eventhousandsoffine-grained,interdependentsubsystems—they
multiplecomponents—suchasservices,serviceinstances,and
are facing more frequent failures. Ensuring system reliability hosts—and the interactions between them, including service
thus demands accurate root cause localization. While traces and
metrics have proven to be effective data sources for this task, calls,databasequeries,andotherinter-componentcommunica-
existing methods either heavily rely on pre-defined schemas, tions.Moreover,thedynamicnatureoftheseinteractions,com-
which struggle to adapt to evolving operational contexts, or bined with the heterogeneity of system components, makes
lack interpretability in their reasoning process, thereby leaving
pinpointing the root cause a highly non-trivial task.
Site Reliability Engineers (SREs) confused. In this paper, we
To enable fine-grained root cause localization of these
conduct a comprehensive study on how SREs localize the root
issues, extensive work leverages both trace and metrics data
cause of failures, drawing insights from multiple professional
SREs across different organizations. Our investigation reveals from software systems. Metrics data provides aggregate in-
thathumanrootcauseanalysisexhibitsthreekeycharacteristics: sightsintosystemperformance(e.g.,responsetimes,through-
recursiveness,multi-dimensionalexpansion,andcross-modalrea- put, and resource utilization), as exemplified by approaches
soning.Motivatedbythesefindings,weintroduceRCLAgent,an
such as Microscope [19], which constructs causality graphs
adaptiverootcauselocalizationmethodformicroservicesystems
and employs a depth-first search strategy to identify front-
that leverages a multi-agent recursion-of-thought framework.
RCLAgent employs a novel recursion-of-thought strategy to end anomalies; CIRCA [20], which builds a causal Bayesian
guide the LLM’s reasoning process, effectively integrating data network using regression-based hypothesis testing and de-
from multiple agents and tool-assisted analysis to accurately scendant adjustment to infer problematic components; and
pinpoint the root cause. Experimental evaluations on various
RUN [21], which employs time series forecasting for neu-
public datasets demonstrate that RCLAgent achieves superior
ral Granger causal discovery and integrates a personalized
performance by localizing the root cause using only a single
request—outperformingstate-of-the-artmethodsthatdependon PageRank algorithm to efficiently recommend the top-k root
aggregatingmultiplerequests.Theseresultsunderscoretheeffec- causes. Meanwhile, trace data offers a more granular view by
tiveness of RCLAgent in enhancing the efficiency and precision tracking the execution paths of individual requests and inter-
of root cause localization in complex microservice environments.
component interactions, as demonstrated by MicroRank [22],
which designs a trace coverage tree to capture dependencies
Index Terms—Root Cause Localization, Trace, Multi-Agent,
betweenrequestsandserviceinstancesandappliesthePageR-
Recursion-of-Thought.
ank algorithm to score potential root causes; TraceRank [23],
which combines spectrum analysis with a PageRank-based
I. INTRODUCTION random walk to pinpoint abnormal services; CRISP [24],
which performs critical path analysis tailored to drill down
Modern microservice systems have become increasingly
latency issues; and TraceConstract [25], which uses sequence
complex due to dynamic interactions and evolving runtime
representations along with contrast sequential pattern mining
environments[1]–[3].Thesesystemsoftenconsistofhundreds
andspectrumanalysistoefficientlylocalizemulti-dimensional
or even thousands of fine-grained, interdependent subsystems,
root causes. Some approaches integrate multimodal data,
where issues in any one component can easily lead to perfor-
particularly LLM-based methods. For instance, mABC [26]
mance problems at the top level [4]–[8]. Therefore, to ensure
introduces a multi-agent, blockchain-inspired collaboration
system reliability, it is crucial to localize the root cause of
framework where multiple LLM-based agents follow a struc-
these issues in a timely manner [9], [10].
tured workflow and coordinate through blockchain-inspired
However, localizing the root cause of these issues is chal-
voting mechanisms. RCAgent [27] leverages log and code
lenging due to the intricate dependencies between subsystems
data in a tool-augmented LLM framework to perform root
LingzheZhang,TongJia,WeijieHong,ChimingDuan,MinghuaHe,and causeanalysistaskssuchaspredictingrootcauses,identifying
YingLiarewithPekingUniversity,Beijing,China. solutions,gatheringevidence,anddeterminingresponsibilities.
Email:{zhang.lingzhe,hongwj,duanchiming,hemh2120}@stu.pku.edu.cn
Although these root cause localization methods have
and{jia.tong,li.ying}@pku.edu.cn
KangjinWangiswithAlibabaGroup,China,e-mail:(kangjin.wkj@alibaba- demonstratedpromisingoutcomes,theystillfacethefollowing
inc.com) practical challenges when applied to real-world microservice
*Correspondingauthor:TongJia,e-mail:(jia.tong@pku.edu.cn);YingLi,
systems:
e-mail:(li.ying@pku.edu.cn)
ManuscriptreceivedMay28,2025;revisedxxx. • Heavy Reliance on Pre-defined Schemas. Most ap-
5202
guA
82
]ES.sc[
1v07302.8052:viXra

ADAPTIVEROOTCAUSELOCALIZATIONFORMICROSERVICESYSTEMSWITHMULTI-AGENTRECURSION-OF-THOUGHT 2
proaches depend on pre-defined service causal graphs, • WeconductacomprehensivestudyonhowSREslocalize
fixed statistical models of fault-symptom relation- the root cause an abnormal request. Our findings reveal
ships, or implicitly learned associations from training thathumanrootcauseanalysisexhibitsthreekeycharac-
data—essentially relying on static, one-time analyses. teristics:recursiveness,multi-dimensionalexpansion,and
Whilesuchschemasprovideabaselinecapabilityforroot cross-modal reasoning.
causelocalization,theyalsoimposesignificantlimitations • Inspired by these findings, we propose RCLAgent, an
on generalizability. The effectiveness of these models is adaptive root cause localization method for microservice
strictlytiedtotheirunderlyingassumptions;anychanges systems, leveraging a multi-agent recursion-of-thought
in service dependencies or predefined anomaly models framework.
can severely compromise performance. Consequently, • WeevaluateRCLAgentonsixdatasets,demonstratingits
these rigid methods struggle to adapt to evolving opera- effectiveness. Experimental results show that RCLAgent
tional contexts. achieves superior performance by analyzing a single
• Lack of Interpretability in the Reasoning Process. request, surpassing state-of-the-art methods that rely on
Although some models use deep learning to dynamically multiple requests for analysis.
capture service dependencies and their correlation with
rootcauses,theyoftensufferfromalackoftransparency II. BACKGROUND
compared to graph-based approaches. Given a formatted
In this section, we present the essential background of
input, these models can produce a list of potential root
this paper, including the formal definition of the root cause
causes but typically fail to explain how or why these
localization problem, an overview of traditional root cause
conclusions are reached. In contrast, an interpretable
localizationmethods,andanintroductiontodistributedtracing
reasoningprocessiscrucialforSiteReliabilityEngineers
as the primary data source for root cause localization.
(SREs), as it enables rapid verification of the root cause
and facilitates timely remediation.
A. Root Cause Localization
Recognizing this gap, we first conduct an empirical study
to investigate how SREs localize the root causes, drawing Failurediagnosisindistributedsystemsisgenerallydivided
insights from multiple professional SREs across different into two categories: failure category classification and root
organizations. This study reveals three key characteristics of cause localization. The former determines the failure type,
manualrootcauseanalysis:recursiveness(whenadeeper-level such as CPU or memory anomalies, while the latter pinpoints
root cause is identified, SREs iteratively refine their analysis the specific node, service, or pod responsible for the issue.
by examining lower-layer manifestations), multi-dimensional Root cause localization is particularly critical for minimizing
expansion (broadening the search across different dimensions, downtime and ensuring system stability.
such as pods, services, and infrastructure, to account for Traditional root cause localization methods typically ana-
all potential root causes), and cross-modal reasoning (once lyze a collection of anomalous requests within a predefined
a potential root cause is identified through trace data, it is time window. These methods construct a dependency graph
validated by analyzing fluctuations in relevant metrics). where nodes represent system components, and edges capture
Building on these insights, we introduce RCLAgent1, an causal relationships inferred from request traces or system
adaptive root cause localization method for microservice sys- logs. Graph-based algorithms, such as PageRank, are then
tems with multi-agent recursion-of-thought. RCLAgent com- appliedtorankcomponentsbasedontheirlikelihoodofbeing
prises two types of agents: data agents, which integrate trace the root cause.
and metrics data, and thought agents, which mainly employ
recursion-of-thought to iteratively infer and refine the root C∗ =C∗ =argmaxs(C,G,M) (1)
C∈C
cause. These agents are coordinated by a central coordinator,
Formally, given a set of anomalous requests R =
whichorchestratestheprocessthroughthreekeyphases:initial
{r ,r ,...,r },acomponentgraphG=(C,E)isconstructed,
reasoning, critical reflection, and final review. 1 2 n
where C is the set of components, and E represents their
Our experiments demonstrate that RCLAgent significantly
dependencies. The root cause component C∗ is identified as
outperforms existing state-of-the-art root cause localization
Equation 1, where s(C,G,M) represents the computed score
methods. The evaluation results show that RCLAgent delivers
incorporating graph topology and observed anomalies.
superior performance by analyzing a single request, outper-
forming alternative methods that require multiple requests for
analysis. Notably, RCLAgent’s recall@1 even surpasses the B. Distributed Tracing
recall@10ofcompetingapproaches.Furthermore,whenasim-
Tosupportfine-grained faultdiagnosisinsoftwaresystems,
ple majority voting strategy is employed, RCLAgent’s group
distributed tracing has been widely adopted in industrial
ranking MRR exhibits a substantial improvement, surpassing
environments, becoming an integral part of modern software
thesecond-bestmethodbyanaverageof32.53%.Insummary,
infrastructures [28]–[30]. A distributed trace provides a de-
the key contributions of this work are as follows:
tailed execution record of a request as it propagates through
the system, capturing timing, dependencies, and performance
1CodeRepository:https://github.com/LLMLog/RCLAgent characteristics. Each trace consists of multiple structured log

ADAPTIVEROOTCAUSELOCALIZATIONFORMICROSERVICESYSTEMSWITHMULTI-AGENTRECURSION-OF-THOUGHT 3
span_id: b711142c1d8f7fd9
|     |     |     |     |     | Span A |     |     |     | timestamp: 1647772917728 |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | ------ | --- | --- | --- | ------------------------ | --- | --- | --- | --- | --- | --- |
cmdb_id: frontend2-0
operation_name:
hipstershop.Frontend/Recv.
| timestamp,cmdb_id,span_id,trace_id,duration,type,status_code,operation_name,parent_span 1 6 4 7 7 4 7 3 5 4 0 3 8 , p r o d u c t ca | t a l o g s e rv i c e - 1 , 0 2 5 a 8 6                                       | 6 5 c 0 c 5 9 c 0 4 , a e 2 6 5 c 5 b                                        | 0 7 a c fe 6 c b 3 5 4 8eb855                     |     |     |     |     |     |                    |     |     |     |     |     |     |
| ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ---------------------------------------------------------------------------- | ------------------------------------------------- | --- | --- | --- | --- | --- | ------------------ | --- | --- | --- | --- | --- | --- |
| aa 1 3 5 7 , 3 0 ,r p c ,0 , h i p s t er s h                                                                                        | o p . P r o d u c t C a t a l o g S e r v                                      | ic e / L is t P r o d u c t s ,1 2 5 b 4                                     | b b e 9 4 d 2 7 a 4 7                             |     |     |     |     |     | duration: 60000438 |     |     |     |     |     |     |
| 1 a1 6 3 4 5 7 7 7 , 4 4 7 3 3 8 5 3 4 ,r 0 p 5 c 0 ,0 ,p ,h ro ip d s u t c e t r c s                                               | a h t o a p lo .P g r s o e d rv u i c c t e C -1 at , a 8 l 6 o f g 3 S 4 e 6 | r 1 v f i e c 4 e 2 /G f3 e 4 tP 84 ro ,a d e u 2 c 6 t, 5 1 c 8 5 8 b 7 0 7 | 7 e a b c 5 f 5 e6 b c a b 2 3 cb 5 d 4 f 8eb855a |     |     |     |     |     | status_code: 13    |     |     |     |     |     |     |
1647747354075,adservice-0,6bd44260603f2742,ae265c5b07acfe6cb3548eb855aa1357,23,r
| p 1 c 6 , 4 O 7 K 74 ,h 7 i 3 p 4 s 0 te 6 r 9 sh 3 o ,f p ro .a n d t s e e n r d v | - i 2 c , e d / 1 g b e 3 ta f d 2 s 3 , 8 7 e 5 5 0 4 9 4 c e 7 3 a f 7 0 9 , 2 ae | 7 2 d 6 3 5 d c f9 5b07acfe6cb3548eb855aa1357,13385 |     |     | Span B | Span E |     | Span F |     |     |     |     |     |     |     |
| ------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------- | --------------------------------------------------- | --- | --- | ------ | ------ | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
835,http,0,hipstershop.Frontend/Recv.,
1647747354043,frontend-2,ed794292138f3a8d,ae265c5b07acfe6cb3548eb855aa1357,6733, rpc,0,hipstershop.ProductCatalogService/GetProduct,d1b3f238e544e3f0
1647747354055,frontend-2,0537acbf70acd7ab,ae265c5b07acfe6cb3548eb855aa1357,5677,r
pc,0,hipstershop.ProductCatalogService/GetProduct,d1b3f238e544e3f0 1647747354067,frontend-2,fd645f9fb5de1c44,ae265c5b07acfe6cb3548eb855aa1357,5987,r
pc,0,hipstershop.ProductCatalogService/GetProduct,d1b3f238e544e3f0
|     |     |     |     |     |     |     |     |     | span_id: 993bc2a93345fd7d |     | span_id: 6a214f194590145c |     |     | span_id: b0cb19d677f6c002 |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------------- | --- | ------------------------- | --- | --- | ------------------------- | --- |
|     |     |     |     |     |     |     |     |     | timestamp: 1647772917731  |     | timestamp: 1647772917733  |     |     | timestamp: 1647772917728  |     |
Span C Span D …… cmdb_id: frontend2-0 cmdb_id: frontend2-0 cmdb_id: frontend2-0
|     |     |     |     |     |     |     |     |     | operation_name:          |     | operation_name:           |     |     | operation_name:             |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------------ | --- | ------------------------- | --- | --- | --------------------------- | --- |
|     |     |     |     |     |     |     |     |     | hipstershop.CartService/ |     | hipstershop.Recommendatio |     |     | hipstershop.CurrencyService |     |
|     |     |     |     |     |     |     |     |     | GetCart                  |     | nService/List             |     |     | /GetSupportedCurrencies     |     |
|     |     |     |     |     |     |     |     |     | duration: 2196           |     | duration: 59995303        |     |     | duration: 2579              |     |
Fig.1. ExampleofTraceLog status_code: 0 status_code: 1 status_code: 0
entries,knownasspans,whichdocumentindividualoperations
span_id: 14fd34682899647e
| along the | request’s | execution |     | path. |     |     |     |     |     |     |     |     |     |     |     |
| --------- | --------- | --------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
timestamp: 1647772933205
cmdb_id: recommendationservice2-0
As illustrated in Figure 1, a complete trace represents the operation_name: hipstershop.RecommendationService/ListRecommendations
| end-to-end | journey | of  | a request, |     | detailing | every | intermediate |     | duration: 59994374 |     |     |     |     |     |     |
| ---------- | ------- | --- | ---------- | --- | --------- | ----- | ------------ | --- | ------------------ | --- | --- | --- | --- | --- | --- |
status_code: 0
| operation   | and         | its corresponding |               |        | latency. | Each  | span        | records |                           |     |     |     |     |     |     |
| ----------- | ----------- | ----------------- | ------------- | ------ | -------- | ----- | ----------- | ------- | ------------------------- | --- | --- | --- | --- | --- | --- |
| crucial     | information |                   | such          | as the | service  | name, | operations, |         |                           |     |     |     |     |     |     |
| timestamps, | and         | causal            | relationships |        | between  |       | operations. | By      | span_id: e263bcab8b7b1036 |     |     |     |     |     |     |
timestamp: 1647772933205
analyzing the timing and dependencies of spans, distributed cmdb_id: recommendationservice2-0
operation_name: hipstershop.ProductCatalogService/ListProducts
tracingenablespreciseperformancemonitoringandfacilitates
duration: 59990939
| anomaly    | detection      | in      | large-scale |                 | distributed |              | systems. | This  | status_code: 0 |     |     |     |     |     |     |
| ---------- | -------------- | ------- | ----------- | --------------- | ----------- | ------------ | -------- | ----- | -------------- | --- | --- | --- | --- | --- | --- |
| structured | representation |         |             | is particularly |             | valuable     | for      | diag- |                |     |     |     |     |     |     |
| nosing     | latency        | issues, | identifying |                 | service     | bottlenecks, |          | and   |                |     |     |     |     |     |     |
span_id: b9652003336464ed
timestamp: 1647773054130
| uncovering | failure | propagation |     | patterns |     | across | microservices. |     |     |     |     |     |     |     |     |
| ---------- | ------- | ----------- | --- | -------- | --- | ------ | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
cmdb_id: productcatalogservice-0
Eachtracecontainsanentryspanthatrepresentstheoverall operation_name: hipstershop.ProductCatalogService/ListProducts
duration: 12
| execution | status | of  | the request. |     | In this | paper, | we  | define |     |     |     |     |     |     |     |
| --------- | ------ | --- | ------------ | --- | ------- | ------ | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
status_code: 0
| a request | as  | having | an issue | if  | its entry | span | exhibits | an  |     |     |     |     |     |     |     |
| --------- | --- | ------ | -------- | --- | --------- | ---- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
excessively high execution latency—specifically, exceeding Fig.2. TraceGraphExample-1
100timesthenormalaveragelatency.Insuchcases,rootcause
| localization | is  | necessary | to  | identify | the | underlying | source | of  |     |     |     |     |     |     |     |
| ------------ | --- | --------- | --- | -------- | --- | ---------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
the anomaly.
|     |     |     |     |     |     |     |     |     | For instance, |     | we extracted | a   | typical | case from | the real- |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ------------ | --- | ------- | --------- | --------- |
III. EMPIRICALSTUDY world AIOPS 2022 dataset, as shown in Figure 2. In this
|          |          |     |          |       |                 |             |     |          | case, a          | request | with the   | cmdb id   | ’frontend2-0’ | experienced   |      |
| -------- | -------- | --- | -------- | ----- | --------------- | ----------- | --- | -------- | ---------------- | ------- | ---------- | --------- | ------------- | ------------- | ---- |
| In this  | section, | we  | conduct  |       | a comprehensive |             |     | study on |                  |         |            |           |               |               |      |
|          |          |     |          |       |                 |             |     |          | severe timeouts, |         | ultimately | resulting | in an         | error (status | code |
| how SREs | localize |     | the root | cause | of              | an abnormal |     | request, |                  |         |            |           |               |               |      |
=13).AsSREs,wefirstanalyzedthetracedataforthisrequest
withinsightsgatheredfrommultipleprofessionalSREsacross
differentorganizations.Tosystematicallyanalyzethisprocess, and identified three primary operations: CartService/GetCart,
|                |     |               |        |                |          |            |     |        | RecommendationService/List, |           |             | and        | CurrencyService/GetSup-   |             |        |
| -------------- | --- | ------------- | ------ | -------------- | -------- | ---------- | --- | ------ | --------------------------- | --------- | ----------- | ---------- | ------------------------- | ----------- | ------ |
| we investigate |     | the following |        | three          | research | questions: |     |        |                             |           |             |            |                           |             |        |
|                |     |               |        |                |          |            |     |        | portedCurrencies.           |           | Notably,    | only       | the RecommendationService |             |        |
| • RQ1:         | How | do            | SREs   | initially      | narrow   | down       | the | search |                             |           |             |            |                           |             |        |
|                |     |               |        |                |          |            |     |        | operation                   | exhibited | a timeout,  | indicating |                           | that it was | likely |
| space          | for | the root      | cause? |                |          |            |     |        |                             |           |             |            |                           |             |        |
|                |     |               |        |                |          |            |     |        | responsible                 | for       | the overall | request    | failure.                  |             |        |
| • RQ2:         | How | do            | they   | systematically |          | expand     | the | search |                             |           |             |            |                           |             |        |
scope to encompass all potential root causes? We then conducted a deeper investigation into the down-
| RQ3: | How | do  | they | differentiate |     | the actual | root | cause |                 |     |           |      |                           |     |     |
| ---- | --- | --- | ---- | ------------- | --- | ---------- | ---- | ----- | --------------- | --- | --------- | ---- | ------------------------- | --- | --- |
| •    |     |     |      |               |     |            |      |       | stream services |     | and found | that | the RecommendationService |     |     |
from other potential but non-causal anomalies? operation with cmdb id ’recommendationservice2-0’ also ex-
|     |     |     |     |     |     |     |     |     | perienced | a timeout. | Further    | analysis               | revealed | that | the sub- |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | ---------- | ---------- | ---------------------- | -------- | ---- | -------- |
|     |     |     |     |     |     |     |     |     | sequent   | downstream | operation, | ProductCatalogService, |          |      | under    |
A. Recursiveness
|     |     |     |     |     |     |     |     |     | the same | cmdb | id, also timed | out. | However, | a later | operation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | ---- | -------------- | ---- | -------- | ------- | --------- |
Deep-seatedissuesoftenmanifestasarequestthatisexcep-
|              |         |       |          |           |       |      |                 |       | onthecomponentwithcmdb |     |         | id’productcatalogservice-0’did |     |     |     |
| ------------ | ------- | ----- | -------- | --------- | ----- | ---- | --------------- | ----- | ---------------------- | --- | ------- | ------------------------------ | --- | --- | --- |
| tionally     | slow or | even  | fails.   | To narrow | down  | the  | search          | space |                        |     |         |                                |     |     |     |
|              |         |       |          |           |       |      |                 |       | not exhibit            | any | issues. |                                |     |     |     |
| for the root | cause,  | human | analysts |           | begin | with | the problematic |       |                        |     |         |                                |     |     |     |
request and examine its trace data to identify the invoked This recursive investigation process effectively narrows
services and executed operations. If anomalies are detected in down the potential root causes to the components with
theseservices,theyfurtherinvestigatethedownstreamservices cmdb id ’frontend2-0’ and ’recommendationservice2-0’, sig-
they call, recursively refining the search until the true root nificantly reducing the search space for identifying the under-
| cause is | isolated. |     |     |     |     |     |     |     | lying performance |     | issue. |     |     |     |     |
| -------- | --------- | --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | ------ | --- | --- | --- | --- |

ADAPTIVEROOTCAUSELOCALIZATIONFORMICROSERVICESYSTEMSWITHMULTI-AGENTRECURSION-OF-THOUGHT 4
Summary.Byanalyzingtracedata,SREsnarrowdownthe
|     |     |     |     |     |     |     |     | pods |     |     |     | service |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | ------- | --- | --- | --- |
search space for the root cause by starting from the entry frontend2-0 re c o m m e n d at
i o n se rv i c e
| span of | a high-duration |     | request | and | recursively |     | examining |             |     |     |     |               |     |     |     |
| ------- | --------------- | --- | ------- | --- | ----------- | --- | --------- | ----------- | --- | --- | --- | ------------- | --- | --- | --- |
|         |                 |     |         |     |             |     |           | recommendat |     |     |     | productcatalo |     |     |     |
downstream operations until the anomalous component is ionservice2-0 gservice
identified.
node
node-5
| B. Multi-Dimensional |     |          | Expansion |     |        |       |           |     |     |     |     |     |     |     |     |
| -------------------- | --- | -------- | --------- | --- | ------ | ----- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
| The previous         |     | analysis | narrowed  | the | search | space | by focus- |     |     |     |     |     |     |     |     |
Fig.4. MetricsInspectionofTraceGraphExample-1
| ing on cmdb                | id, | which | represents | individual                    |     | pods. | However, |     |     |     |     |     |     |     |     |
| -------------------------- | --- | ----- | ---------- | ----------------------------- | --- | ----- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
| identifyingproblematiccmdb |     |       |            | idsaloneisinsufficientforpin- |     |       |          |     |     |     |     |     |     |     |     |
pointingallrootcauses.Therefore,SREsexpandtheiranalysis
|                                            |     |     |     |     |     |            |     | For example,          |     | in Figure | 2,                          | the potentially |     | problematic |     |
| ------------------------------------------ | --- | --- | --- | --- | --- | ---------- | --- | --------------------- | --- | --------- | --------------------------- | --------------- | --- | ----------- | --- |
| beyondindividualpodsbyconsideringoperation |     |     |     |     |     | name,which |     |                       |     |           |                             |                 |     |             |     |
|                                            |     |     |     |     |     |            |     | pod is ’frontend2-0’, |     | and       | ’recommendationservice2-0’, |                 |     |             | the |
helps identify the associated services. From the recursive potentially problematic services are ’recommendationservice’
| analysis above,           |     | it is evident |       | that both | recommendationservice |     |              |                              |               |              |       |                 |      |             |          |
| ------------------------- | --- | ------------- | ----- | --------- | --------------------- | --- | ------------ | ---------------------------- | ------------- | ------------ | ----- | --------------- | ---- | ----------- | -------- |
|                           |     |               |       |           |                       |     |              | and ’productcatalogservice’, |               |              | and   | the potentially |      | problematic |          |
| and productcatalogservice |     |               | could | also      | be potential          |     | root causes. |                              |               |              |       |                 |      |             |          |
|                           |     |               |       |           |                       |     |              | node is ’node-5’.            |               | By analyzing |       | the metrics     |      | data, as    | shown    |
|                           |     |               |       |           |                       |     |              | in Figure                    | 4, it becomes |              | clear | that there      | were | no          | fluctua- |
span_id: b562d708ca6f300f span_id: 054f7d75b8311308 span_id: 054f7d75b8311308 tions in ’frontend2-0’, ’productcatalogservice’, or ’node-5’.
| timestamp: 1647782291301 |     |     | timestamp: 1647782291301 |     |     | timestamp: 1647782291302 |     |     |     |     |     |     |     |     |     |
| ------------------------ | --- | --- | ------------------------ | --- | --- | ------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
cmdb_id: frontend2-0 cmdb_id: frontend2-0 cmdb_id: checkoutservice2-0 However, both ’recommendationservice2-0’ and ’recommen-
| operation_name:  |     |     | operation_name:  |     |     | operation_name:  |     |     |     |     |     |     |     |     |     |
| ---------------- | --- | --- | ---------------- | --- | --- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
hipstershop.Frontend hipstershop.CheckoutService hipstershop.CheckoutService dationservice’ exhibited fluctuations, with ’recommendation-
| /Recv. |     |     | /PlaceOrder |     |     | /PlaceOrder |     |     |     |     |     |     |     |     |     |
| ------ | --- | --- | ----------- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
duration: 60000409 duration: 60000008 duration: 59999988 service’ showing more significant variations. The fluctuations
| status_code: 13                |     |     | status_code: 1              |     |     | status_code: 0              |     |                               |          |             |        |                 |       |                |        |
| ------------------------------ | --- | --- | --------------------------- | --- | --- | --------------------------- | --- | ----------------------------- | -------- | ----------- | ------ | --------------- | ----- | -------------- | ------ |
|                                |     |     |                             |     |     |                             |     | in ’recommendationservice2-0’ |          |             |        | were propagated |       | from           | ’rec-  |
|                                |     |     |                             |     |     |                             |     | ommendationservice’.          |          | Ultimately, |        | the root        | cause | is identified  |        |
|                                |     |     |                             |     |     |                             |     | as ’recommendationservice’,   |          |             | which  | aligns          | with  | the            | ground |
| span_id: 3cc93d9c055ced50      |     |     | span_id: 1181d6fda8205d49   |     |     | span_id: 8ffca52f27dd84ec   |     |                               |          |             |        |                 |       |                |        |
| timestamp: 1647782291324       |     |     | timestamp: 1647782291335    |     |     | timestamp: 1647782291331    |     |                               |          |             |        |                 |       |                |        |
|                                |     |     |                             |     |     |                             |     | truth—network                 | resource |             | packet | corruption      | in    | the Kubernetes |        |
| cmdb_id: checkoutservice2-0    |     |     | cmdb_id: checkoutservice2-0 |     |     | cmdb_id: checkoutservice2-0 |     |                               |          |             |        |                 |       |                |        |
| operation_name:                |     |     | operation_name:             |     |     | operation_name:             |     | container.                    |          |             |        |                 |       |                |        |
| …… hipstershop.PaymentService/ |     |     | hipstershop.EmailService/   |     |     | hipstershop.CartService/    |     |                               |          |             |        |                 |       |                |        |
| Charge                         |     |     | SendOrderConfirmation       |     |     | EmptyCart                   |     |                               |          |             |        |                 |       |                |        |
duration: 3265 duration: 59967600 duration: 4007 Summary. SREs differentiate the actual root cause from
| status_code: 0 |     |     | status_code: 1 |     |     | status_code: 0 |     |                 |           |     |              |     |       |            |     |
| -------------- | --- | --- | -------------- | --- | --- | -------------- | --- | --------------- | --------- | --- | ------------ | --- | ----- | ---------- | --- |
|                |     |     |                |     |     |                |     | other potential | anomalies |     | by analyzing |     | other | modalities | of  |
Fig.3. TraceGraphExample-2 data, particularly metrics data, and identifying the compo-
|              |               |         |                          |              |     |                  |            | nent with | the most | significant |          | or earliest | fluctuation |     | as the |
| ------------ | ------------- | ------- | ------------------------ | ------------ | --- | ---------------- | ---------- | --------- | -------- | ----------- | -------- | ----------- | ----------- | --- | ------ |
| A more       | evident       | example |                          | is shown     | in  | Figure           | 3. In this |           |          |             |          |             |             |     |        |
|              |               |         |                          |              |     |                  |            | true root | cause.   |             |          |             |             |     |        |
| trace, the   | root          | cause   | is clearly               | linked       | to  | the EmailService |            |           |          |             |          |             |             |     |        |
| operation    | under         | cmdb    | id ’checkoutservice2-0’. |              |     | This             | suggests   |           |          |             |          |             |             |     |        |
|              |               |         |                          |              |     |                  |            |           |          | IV.         | RCLAGENT |             |             |     |        |
| that further | investigation |         | into                     | emailservice |     | is necessary     | for        | a         |          |             |          |             |             |     |        |
deeper analysis.
|     |     |     |     |     |     |     |     | Our empirical |     | study | demonstrates | the | process | by  | which |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ----- | ------------ | --- | ------- | --- | ----- |
Beyond service-level expansion, SREs also consider the human SREs localize the root cause of abnormal requests.
underlying physical infrastructure. Forinstance, in both traces However, the time and effort of human experts are valuable,
above, ’recommendationservice2-0’ and ’checkoutservice2-0’ andlargelanguagemodelscaneffectivelysimulatethisprocess
run on node-5, which can be readily obtained in real-time for automated root cause localization.
frommetricsdata.Thisindicatesthatfurtherinvestigationinto Therefore, in this section, we introduce RCLAgent, an
the physical machine node-5 is required to assess its potential adaptive method for root cause localization for microservice
contribution to the issue. systems through multi-agent recursion-of-thought. Figure 5
|     |     |     |     |     |     |     |     | illustrates | the architecture |     | of RCLAgent. |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ---------------- | --- | ------------ | --- | --- | --- | --- |
Summary. SREs systematically expand the scope of root RCLAgent consists of two types of agents: data agents and
cause analysis across multiple dimensions—correlating thought agents. Data agents are responsible for data retrieval
| anomalous | cmdb | ids | with | associated | services | and | under- |                |            |     |           |     |       |        |        |
| --------- | ---- | --- | ---- | ---------- | -------- | --- | ------ | -------------- | ---------- | --- | --------- | --- | ----- | ------ | ------ |
|           |      |     |      |            |          |     |        | and processing | (currently |     | including | the | Trace | Agent, | Metric |
lying physical infrastructure—to comprehensively identify Agent, and Format Agent), while thought agents focus on in-
| all potential  | sources    |           | of issues.  |                  |            |          |           |                      |              |                 |         |             |           |              |     |
| -------------- | ---------- | --------- | ----------- | ---------------- | ---------- | -------- | --------- | -------------------- | ------------ | --------------- | ------- | ----------- | --------- | ------------ | --- |
|                |            |           |             |                  |            |          |           | depth reasoning      | based        | on              | the     | provided    | data      | (including   | the |
|                |            |           |             |                  |            |          |           | Recursion            | Agent        | and Cross-Modal |         | Agent).     | The       | coordination |     |
|                |            |           |             |                  |            |          |           | between              | these agents | is              | managed | by          | a central | coordinator, |     |
| C. Cross-Modal |            | Reasoning |             |                  |            |          |           |                      |              |                 |         |             |           |              |     |
|                |            |           |             |                  |            |          |           | which operates       | through      |                 | three   | key phases: | initial   | reasoning,   |     |
| Through        | the        | analysis  |             | of recursiveness |            | and      | multi-    |                      |              |                 |         |             |           |              |     |
|                |            |           |             |                  |            |          |           | critical reflection, |              | and final       | review. |             |           |              |     |
| dimensional    | expansion, |           | SREs        | have             | identified |          | potential |                      |              |                 |         |             |           |              |     |
| root causes    | across     | three     | dimensions: |                  | pod,       | service, | and node. |                      |              |                 |         |             |           |              |     |
| However,       | the exact  |           | root cause  | remains          | uncertain. |          | At this   | A. Data Agents       |              |                 |         |             |           |              |     |
stage, SREs often integrate other modalities of data, with Data agents provide various types of data to other agents
metrics data being the most commonly used, to pinpoint the based on input, along with preprocessing and filtering capa-
final root cause. bilities. They can encompass any form of data retrieval and

ADAPTIVEROOTCAUSELOCALIZATIONFORMICROSERVICESYSTEMSWITHMULTI-AGENTRECURSION-OF-THOUGHT 5
Data Agents Thought Recursion-of-Thought
Agents
Trace Input
Query
Agent
Recursion
Agent
Metric
Agent
Intermodal
Inference backtrace
Format Return Call
Agent
Agent
Coordinator
Stages
Initial Critical Final
Reasoning Reflection Review + | |
Fig.5. ArchitectureofRCLAgent
processing functions. In this work, we primarily utilize three m∈M(C), let µ and σ represent its historical mean and
m m
agents: the Trace Agent, Metrics Agent, and Format Agent. standard deviation, respectively. The Metric Agent examines
However, in practical applications, the number and types of the metric values over the interval [t −δ,t +δ] and applies
0 0
agents can be flexibly adjusted as needed. an n-sigma test: if there exists a time t in this interval, as
1) Trace Agent: Trace data is the most fundamental source defined in Equation 3, an anomaly is detected. In such cases,
for root cause localization, as it records the sequence of the agent returns the corresponding fluctuation data over a
calls between various services. However, since each request period of length delta, as formulated in Equation 4.
generatesacompleteinvocationpath,thevolumeoftracedata
canbeenormous,makingitdifficultforlargelanguagemodels (cid:26) (cid:12) (cid:27)
to process such extensive context. To address this, the trace Q(t 0 ,δ,C)= m(t) (cid:12) (cid:12) (cid:12) m∈ | M m( ( t C )− ), µ t m ∈ | [ > t 0 n − × δ, σ t 0 m +δ],
agent isdesigned tofilter and retrieveonly the relevantsubset (4)
of trace data. 3) Format Agent: Large language models generate exten-
sive natural language outputs that often contain key infor-
T(s)={⟨t,s′,svc,op,d,σ⟩|s′ ∈C(s)} (2) mation. However, this abundance of unstructured text can
Formally, given a span identifier s, the trace agent returns hinder subsequent automated processing, making it difficult
to produce a definitive final result. To address this issue, we
a set of child spans along with their associated metadata.
We denote this function as Equation 2, where t denotes the designedaFormatAgentspecificallytosummarizethegener-
timestamp, s′ represents the child span identifier, svc is the ated text and output it in a standardized format. For instance,
servicename, op isthe operationname, d isthe duration,σ is when presenting the final results, the Format Agent ensures
the status code, and C(s) is the set of all child spans for the that exactly two fields are output: one for the root cause
given span s. (root_cause) and one for the corresponding explanation
2) MetricAgent: Metricsdatarepresenttheruntimestateof
(reason).
system components. In a mature microservices environment,
there are thousands of distinct metrics continuously recording B. Thought Agents
values, often resulting in a data volume that exceeds that
Thought agents are designed based on insights from our
of trace data. Moreover, our empirical study reveals that
empirical study, specifically leveraging recursiveness, multi-
during system anomalies, most metrics remain stable without
dimensional expansion, and cross-modal reasoning. Since
significant fluctuations. Consequently, we have developed a
largelanguagemodelsinherentlypossesstheabilitytoextract
specialized Metric Agent that selectively retrieves only those
key information from vast amounts of data without excessive
metrics exhibiting notable deviations within a predefined time
deliberation, this section focuses primarily on the design of
window for LLM analysis.
recursiveness and cross-modal reasoning.
1) IntermodalInferenceAgent: Tracedataandmetricsdata
|m(t)−µ |>n×σ (3)
m m exhibit a semantic gap, making direct correlation challenging.
Formally, given an input timestamp t and a target key To address this, the Intermodal Inference Agent is designed
0
component C (e.g., a pod or service), let M(C) denote the to bridge the gap between trace analysis and metrics querying
set of metrics associated with C and its related components bysynthesizingqueryparametersfrommulti-modalcontextual
(including the node corresponding to a pod). For each metric data.Thisagentextractsthemostrelevantkeywords(potential

ADAPTIVEROOTCAUSELOCALIZATIONFORMICROSERVICESYSTEMSWITHMULTI-AGENTRECURSION-OF-THOUGHT 6
root causes) and temporal windows from the trace context. Algorithm 1 Recursion-of-Thought Algorithm
These parameters are then utilized to query the metrics data, Require: Trace data T for a high-duration request.
ensuring that only those metrics corroborating the anomalies Ensure: Formatted potential root cause(s) R f .
detected in trace data are retrieved. 1: Initialize candidate set Q←{T entry }
2: Initialize potential root cause set R←∅.
q =I(X)=(K,τ) (5) 3: while Q̸=∅ do
4: Remove a candidate span s from Q.
Formally, let X denote the contextual embedding derived
5: Generate reasoning instruction I ←f(s)
from trace analysis. The intermodal inference agent computes
6: Retrieve associated data D ←TraceAgent(I).
a query tuple q = (K,τ), as shown in Equation 5, where K
7: if s is deemed a potential root cause based on D then
represents the set of key metric identifiers (i.e., keywords),
8: Compute query tuple q ←I intermodal (X)=(K,τ)
and τ denotes the inferred time window during which anoma-
9: Retrieve metrics data M ←A metric (q).
lies are expected. The function I(·) encapsulates the agent’s
10: if Metrics analysis confirms anomaly for s then
inferenceprocess,modelingthecomplexinteractionsbetween
11: R←R∪{s}
different data modalities.
12: else
2) Recursion Agent: As previously discussed, professional
13: Discard s
SREs employ a recursive approach when using trace data for
14: end if
rootcauselocalization.Toreplicatethisprocess,wedesigneda
15: else
dedicatedRecursionAgentthatfollowsarecursion-of-thought
16: Let C be the set of child spans of s.
paradigm.
17: Q←Q∪C.
Unlike traditional chain-of-thought reasoning, which fol-
18: end if
lows a linear progression, recursion-of-thought relies on gen-
19: if s yields no further viable path and backtracing is
erating step-by-step reasoning instructions based on the in-
feasible then
formation from the previous step. Each generated instruction
20: Backtracetoapreviouslyuninspectedcandidatein
triggers subordinate agents to retrieve the necessary data for
Q.
furtheranalysis.Moreover,ifaparticularanalyticalpathyields
21: end if
no further potential for identifying a root cause, the agent
22: end while
automaticallybacktracestoapreviouslyencounteredcandidate
23: R f ←FormatAgent(R)
that has not been thoroughly inspected, and continues the
24: return R f .
recursive analysis.
Inthispaper,therecursion-of-thoughtmechanismisprimar-
ilyappliedtotracedataanalysis,withmetricsdataverification
usedtoconfirmfindings.Thisprocessinvolvesthecoordinated the actual process of querying data agents, processing their
interaction of all agents in our framework, as illustrated in returned results, and transmitting the information to thought
Algorithm 1. agentsforfurtherexecutionisorchestratedbythecoordinator.
Specifically, the process begins with the trace agent identi- Moreover,beyondmanagingtheseinteractions,thecoordinator
fying the entry span of a high-duration request, which serves alsooverseestheexecutionofAlgorithm1acrossthreedistinct
as the starting point for recursive analysis. At each step, phases,ensuringiterativecoordinationthroughouttheprocess.
an LLM-based reasoning instruction is generated based on 1) Initial Reasoning: This stage is responsible for initial-
the current candidate span. The trace agent then retrieves izing the entire inference process. Given an initial task, the
the associated trace data, and if the candidate is deemed a model is induced to consider the problem from a recursive
potentialrootcause,theintermodalinferenceagentsynthesizes perspective and begin a preliminary assessment of potential
queryparameters(keywordsandatemporalwindow)fromthe rootcauses.Toexpeditereasoningatthisstage,wedeliberately
tracecontext.Theseparametersaresubsequentlypassedtothe hide the presence of the Metrics Agent.
metrics agent, which retrieves the corresponding metrics data
to verify whether the observed anomaly is corroborated. If
the metrics analysis confirms the anomaly, the candidate is System:
added to the potential root cause set; otherwise, the algorithm You are a software operations engineer. Your task is to
expands the search by exploring the candidate’s child spans. systematically diagnose and identify the root cause of
Moreover, if a particular analysis path fails to yield a viable software failures.
candidate, the system automatically backtraces to previously User:
uninspected candidates for further investigation. Finally, the Please read the following root trace and identify the corre-
format agent consolidates and standardizes the identified po- sponding root cause service.
tential root causes into a structured final output. A possible approach is to recursively search for the traces
you suspect have issues. {T }
entry
C. Coordinator You have the following agents to call: {A\{A metric }}
Although the recursion agent has outlined the invocation
relationships between agents from an algorithmic perspective, Fig.6. ThePromptforInitialReasoning

ADAPTIVEROOTCAUSELOCALIZATIONFORMICROSERVICESYSTEMSWITHMULTI-AGENTRECURSION-OF-THOUGHT 7
As shown in Figure 6, the initial prompt, denoted as P , is expansion of the candidate set Q via agent A (such as the
|     |     |     |     |     |     |     | 0   |     |     |     |     | i   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
constructed from the entry trace T entry and a set of available Trace or Metrics Agent), and R(·) encapsulates the recursive
agentsA\{A }.TheinitialreasoningstateS isformally refinement process.
|         | metric      |     |       |                 |     | 0   |           |          |         |     |       |              |            |     |            |
| ------- | ----------- | --- | ----- | --------------- | --- | --- | --------- | -------- | ------- | --- | ----- | ------------ | ---------- | --- | ---------- |
| defined | as Equation | 6,  | where | Φ(·) represents |     | the | inference |          |         |     |       |              |            |     |            |
|         |             |     |       |                 |     |     |           | 3) Final | Review: |     | After | the critical | reflection |     | stage, the |
process executed by the large language model. RCLAgent performs in-depth inspections of both trace and
|     |     |          |     |     |     |                 |     | metrics | data. | However, | in  | practice, | large language |     | models |
| --- | --- | -------- | --- | --- | --- | --------------- | --- | ------- | ----- | -------- | --- | --------- | -------------- | --- | ------ |
|     |     | (cid:16) |     |     |     | (cid:1)(cid:17) |     |         |       |          |     |           |                |     |        |
(cid:0)
S =Φ P T , A\{A } (6) tend to focus more on the recent context when generating
|                | 0           |        | 0 entry |                 | metric |                 |       |                 |              |           |                |      |               |        |            |
| -------------- | ----------- | ------ | ------- | --------------- | ------ | --------------- | ----- | --------------- | ------------ | --------- | -------------- | ---- | ------------- | ------ | ---------- |
|                |             |        |         |                 |        |                 |       | results.        | As a result, | potential |                | root | causes that   | appear | earlier    |
| 2) Critical    | Reflection: |        | Initial | reasoning       | can    | quickly         | yield | a               |              |           |                |      |               |        |            |
|                |             |        |         |                 |        |                 |       | in the analysis |              | might     | be overlooked. |      | For example,  |        | as shown   |
| rough judgment |             | of the | root    | cause; however, |        | our experiments |       |                 |              |           |                |      |               |        |            |
|                |             |        |         |                 |        |                 |       | in Figure       | 2, after     | deeper    | inspection,    |      | the potential |        | root cause |
reveal that the model tends to terminate its analysis prema- could be identified as productcatalogservice. How-
| turely. For | example, | as        | shown | in Figure        | 3, during |                 | the initial |                               |        |      |          |      |           |        |           |
| ----------- | -------- | --------- | ----- | ---------------- | --------- | --------------- | ----------- | ----------------------------- | ------ | ---- | -------- | ---- | --------- | ------ | --------- |
|             |          |           |       |                  |           |                 |             | ever, the                     | actual | root | cause in | this | case lies | in the | shallower |
| reasoning   | phase    | the model |       | often identifies |           | the problematic |             |                               |        |      |          |      |           |        |           |
|             |          |           |       |                  |           |                 |             | level, recommendationservice, |        |      |          |      | which     | might  | be missed |
podascheckoutservice2-0afterjusttworecursivetrace
|          |             |        |       |           |     |           |     | if the model |             | prematurely | concludes |     | the investigation. |           | This  |
| -------- | ----------- | ------ | ----- | --------- | --- | --------- | --- | ------------ | ----------- | ----------- | --------- | --- | ------------------ | --------- | ----- |
| queries. | In reality, | if the | model | continues | the | recursion | for | a            |             |             |           |     |                    |           |       |
|          |             |        |       |           |     |           |     | scenario     | illustrates | that,       | while     | the | initial            | reasoning | might |
fewmoresteps,itdiscoversthattheactualanomalyoriginates suggest recommendationservice, the critical reflection
| from emailservice. |     |     | This | observation | highlights |     | the need |             |          |     |                        |     |     |     |         |
| ------------------ | --- | --- | ---- | ----------- | ---------- | --- | -------- | ----------- | -------- | --- | ---------------------- | --- | --- | --- | ------- |
|                    |     |     |      |             |            |     |          | stage could | indicate |     | productcatalogservice, |     |     |     | leading |
foradeeper,morerigorousanalysistoavoidearlytermination
|                       |     |     |     |           |        |     |     | to conflicting |     | conclusions. |     |            |         |        |        |
| --------------------- | --- | --- | --- | --------- | ------ | --- | --- | -------------- | --- | ------------ | --- | ---------- | ------- | ------ | ------ |
| and misidentification |     | of  | the | true root | cause. |     |     |                |     |              |     |            |         |        |        |
|                       |     |     |     |           |        |     |     | To address     |     | this issue,  | we  | introduced | a final | review | stage, |
whereonlytheFormatAgentisinvoked.Thisagentallowsthe
Step 1: modeltoreviewtheentirereasoningprocess,startingfromthe
| We think | it’s | better | to inspect | more | deeper | into | the trace |     |     |     |     |     |     |     |     |
| -------- | ---- | ------ | ---------- | ---- | ------ | ---- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
initialstage,andconsolidateitsfindingstodeterminethefinal
tree. So, even you have already define the root cause, you rootcause.Byrevisitingthepriorreasoning,themodelensures
| must use | the | following | tool | to inspect | more | deeper | to  |          |         |           |      |        |         |             |     |
| -------- | --- | --------- | ---- | ---------- | ---- | ------ | --- | -------- | ------- | --------- | ---- | ------ | ------- | ----------- | --- |
|          |     |           |      |            |      |        |     | that any | earlier | potential | root | causes | are not | overlooked, | and |
confirm that there are no deeper root cause. the final decision is based on the entire diagnostic process.
You have the following agents to call: {A\{A }} This structured review helps the model arrive at the most
format
Step ¿1:
|         |          |            |     |              |      |         |          | accurate | and reliable |     | root cause | conclusion. |     |     |     |
| ------- | -------- | ---------- | --- | ------------ | ---- | ------- | -------- | -------- | ------------ | --- | ---------- | ----------- | --- | --- | --- |
| Please  | continue | to further |     | identify the | root | cause   | service. |          |              |     |            |             |     |     |     |
| You may | inspect  | deeper     | by  | Trace Agent  | or   | combine | with     |          |              |     |            |             |     |     |     |
Context:
Metrics Agent to confirm the root cause. Pleaserethinktheabovethinkprocessandreturnthecorrect
IfyouusetheTraceAgent,weoftenfindthattherootcause
|     |     |     |     |     |     |     |     | root cause | and | reason | by the | A   | agent. |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | ------ | ------ | --- | ------ | --- | --- |
originates from a specific downstream trace. If you have format
Input:
| already | define | the root | cause | service, | just | call the | Format |     |     |     |     |     |     |     |     |
| ------- | ------ | -------- | ----- | -------- | ---- | -------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
{Think Process}
Agent.
| You have | the | following | agents | to call: | {A} |     |     |                                |     |     |     |     |     |     |     |
| -------- | --- | --------- | ------ | -------- | --- | --- | --- | ------------------------------ | --- | --- | --- | --- | --- | --- | --- |
|          |     |           |        |          |     |     |     | Fig.8. ThePromptforFinalReview |     |     |     |     |     |     |     |
Fig.7. ThePromptforCriticalReflection
AsshowninFigure8,thefinalreviewstageisimplemented
|            |      |              |     |              |     |            |         | as a consolidation |     | process | where | the | reasoning | results | from |
| ---------- | ---- | ------------ | --- | ------------ | --- | ---------- | ------- | ------------------ | --- | ------- | ----- | --- | --------- | ------- | ---- |
| To address | this | shortcoming, |     | we introduce |     | a critical | reflec- |                    |     |         |       |     |           |         |      |
boththeinitialreasoningandcriticalreflectionstagesarecom-
tionstagethatforcesthemodeltoconductfurtherinvestigation
|                   |          |     |           |             |           |       |       | bined. This             | is    | mathematically |                                 | represented | by         | the Equation | 8,       |
| ----------------- | -------- | --- | --------- | ----------- | --------- | ----- | ----- | ----------------------- | ----- | -------------- | ------------------------------- | ----------- | ---------- | ------------ | -------- |
| before finalizing |          | its | decision. | In this     | stage,    | the   | model | is                      |       |                |                                 |             |            |              |          |
|                   |          |     |           |             |           |       |       | where                   | R(R ) | represents     | the                             | initial     | root cause | set          | from the |
| explicitly        | prompted | to  | delve     | deeper into | the trace | tree, | even  | if                      | 0     |                |                                 |             |            |              |          |
|                   |          |     |           |             |           |       |       | initialreasoning,andR(S |       |                | )istherefinedsetfromthecritical |             |            |              |          |
1
aninitialrootcausecandidatehasbeenidentified.Asdepicted
|                 |        |                   |          |          |           |           |     | reflection | stage. |        |      |         |       |     |     |
| --------------- | ------ | ----------------- | -------- | -------- | --------- | --------- | --- | ---------- | ------ | ------ | ---- | ------- | ----- | --- | --- |
| in Figure       | 7, the | model             | receives | a prompt | that      | instructs | it  | to         |        |        |      |         |       |     |     |
| either continue |        | its investigation |          | using    | the Trace | Agent     | or  | to         |        |        |      |         |       |     |     |
|                 |        |                   |          |          |           |           |     |            |        | R f =A | (R(R | 0 )∪R(S | 1 )), |     | (8) |
incorporate insights from the Metrics Agent for additional format
verification.Thisadditionallayerofscrutinyhelpsensurethat
the model does not overlook deeper anomalies that may be V. EVALUATION
| hidden beneath |     | the initial | candidate. |     |     |     |     |     |     |     |     |     |     |     |     |
| -------------- | --- | ----------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ToevaluateRCLAgent,weconductaseriesofexperimental
|     |     |     |     |     |     |     |     | studies | to investigate |     | the following |     | research | questions: |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | -------------- | --- | ------------- | --- | -------- | ---------- | --- |
n
(cid:91)
S 1 =R(R 0 )= Q(Q i−1 ,A) (7) RQ1: How accurate is RCLAgent in root cause localiza-
•
i=1
|     |     |     |     |     |     |     |     | tion | when | compared | with | baseline | approaches? |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | ---- | -------- | ---- | -------- | ----------- | --- | --- |
Formally, let R denote the initial set of potential root • RQ2: How does the choice of different LLM backbones
0
causesidentifiedduringtheinitialreasoningstage.Thecritical affect the root cause localization performance of RCLA-
| reflection | stage, | denoted | as  | S , refines | R   | by recursively |     | gent? |     |     |     |     |     |     |     |
| ---------- | ------ | ------- | --- | ----------- | --- | -------------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
|            |        |         |     | 1           | 0   |                |     |       |     |     |     |     |     |     |     |
expandingthecandidateset.Specifically,wedefinetherefined RQ3: What is the contribution of each stage of RCLA-
•
set R f as Equation 7, where Q(Q i−1 ,A) represents the gent to its overall accuracy?

ADAPTIVEROOTCAUSELOCALIZATIONFORMICROSERVICESYSTEMSWITHMULTI-AGENTRECURSION-OF-THOUGHT 8
TABLEI
OVERALLEVALUATIONRESULTSCOMPAREDWITHNON-LLM-BASEDMETHODS(RECALL@K)
CRISP TraceConstract TraceRank MicroRank RUN MicroScope RCLAgent
Dataset
R1 R5 R10 R1 R5 R10 R1 R5 R10 R1 R5 R10 R1 R5 R10 R1 R5 R10 -
A 0.00 28.14 28.14 1.69 22.71 24.07 0.68 0.68 15.93 0.00 26.10 34.93 3.73 13.22 42.03 9.68 36.92 68.46 71.13
B 0.00 60.54 61.88 56.05 75.78 75.78 75.78 75.78 75.78 0.90 60.54 76.23 0.00 0.00 0.00 1.47 7.35 14.22 78.57
Γ 2.51 48.62 51.62 46.35 78.92 88.98 23.95 43.35 56.65 15.45 80.84 89.70 23.83 24.55 24.55 20.95 59.76 81.18 90.24
∆ 1.15 52.87 56.05 2.19 2.92 3.13 59.44 60.06 63.48 2.82 3.34 3.34 0.42 14.18 17.52 7.61 20.75 26.07 64.34
E 15.20 62.33 63.06 33.26 34.14 35.68 23.79 51.76 59.69 27.09 35.68 35.68 0.00 6.39 31.28 8.81 37.44 54.19 65.42
Z 4.68 40.76 45.32 4.81 11.65 17.22 34.94 35.70 39.75 4.43 16.96 17.47 0.13 12.91 39.49 6.86 37.98 63.39 72.41
A. Experimental Setup thetop-10resultlist,therankcanberegardedaspositive
1) Dataset: Our experiments are conducted using the infinity. Given a set of fault instances A, Rank i is the i
|                     |                |            |          |       |          |                |        | rank      | of the | root | cause in   | the returned | list     | of  | the ith fault |
| ------------------- | -------------- | ---------- | -------- | ----- | -------- | -------------- | ------ | --------- | ------ | ---- | ---------- | ------------ | -------- | --- | ------------- |
| AIOPS               | 2022 companion |            | dataset, | which | is       | a large-scale, | real-  |           |        |      |            |              |          |     |               |
|                     |                |            |          |       |          |                |        | instance, | MRR    | is   | calculated | by           | Equation | 9.  |               |
| world dataset       |                | collected  | from     | an    | actively | running,       | mature |           |        |      |            |              |          |     |               |
| microservices-based |                | e-commerce |          |       | system.  | This dataset   | is di- |           |        |      |            |              |          |     |               |
|A|
videdintosixdistinctsubsets.Forthesakeofclarityandease 1 (cid:88) 1
|              |     |             |     |       |       |             |          |     |     | MRR= |     |          |     |     | (9) |
| ------------ | --- | ----------- | --- | ----- | ----- | ----------- | -------- | --- | --- | ---- | --- | -------- | --- | --- | --- |
| of reference | in  | this paper, | we  | label | these | six subsets | as A, B, |     |     |      |     |          |     |     |     |
|              |     |             |     |       |       |             |          |     |     |      |     | |A| Rank | i   |     |     |
i=1
| Γ, ∆, E, | and | Z.  |     |     |     |     |     |     |     |     |     |     |     |     |     |
| -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
2) Baseline Approaches: We compared TraceContrast with Since many existing methods are limited to localizing the
|               |             |            |       |              |              |             |          | root cause | only      | at the   | pod | level, we | assume        | that | if these |
| ------------- | ----------- | ---------- | ----- | ------------ | ------------ | ----------- | -------- | ---------- | --------- | -------- | --- | --------- | ------------- | ---- | -------- |
| the following |             | eight root | cause | localization |              | approaches, | which    |            |           |          |     |           |               |      |          |
|               |             |            |       |              |              |             |          | methods    | correctly | identify | the | pod, the  | corresponding |      | service  |
| can be        | categorized | into       | three | groups:      | trace-based, |             | metrics- |            |           |          |     |           |               |      |          |
based, and LLM-based methods. towhichthepodbelongsisconsideredtherootcause,andwe
|              |     |       |      |                  |     |     |               | treat such | predictions |     | as correct. |     |     |     |     |
| ------------ | --- | ----- | ---- | ---------------- | --- | --- | ------------- | ---------- | ----------- | --- | ----------- | --- | --- | --- | --- |
| Trace-based: |     | CRISP | [24] | representstraces |     | as  | criticalpaths |            |             |     |             |     |     |     |     |
4) ImplementationandSettings:
and applies a lightweight heuristic to identify root cause in- WeimplementRCLAgent
inPython3.10.Unlessotherwisespecified,weuseClaude-3.5
| stances. | TraceContrast |     | [25] | utilizes | sequence | representations, |     |           |         |        |     |         |             |           |     |
| -------- | ------------- | --- | ---- | -------- | -------- | ---------------- | --- | --------- | ------- | ------ | --- | ------- | ----------- | --------- | --- |
|          |               |     |      |          |          |                  |     | Sonnet as | our LLM | engine |     | and set | the n-sigma | threshold | in  |
contrastivesequentialpatternmining,andspectrumanalysisto
|                |                   |          |      |                  |           |        |           | the metrics | agent  | to n=3.  |      | All experiments |         | are conducted | on         |
| -------------- | ----------------- | -------- | ---- | ---------------- | --------- | ------ | --------- | ----------- | ------ | -------- | ---- | --------------- | ------- | ------------- | ---------- |
| localize       | multi-dimensional |          | root | causes.          | TraceRank |        | [23] com- |             |        |          |      |                 |         |               |            |
|                |                   |          |      |                  |           |        |           | a Linux     | server | equipped | with | 24 Intel(R)     | Xeon(R) |               | processors |
| bines spectrum |                   | analysis | with | a PageRank-based |           | random | walk      |             |        |          |      |                 |         |               |            |
(2.90GHz),400GBRAM,andtwoA800GPUswith80GBof
| algorithm  | to pinpoint |          | anomalous |         | services. | MicroRank    | [22] |             |     |         |        |     |     |     |     |
| ---------- | ----------- | -------- | --------- | ------- | --------- | ------------ | ---- | ----------- | --- | ------- | ------ | --- | --- | --- | --- |
|            |             |          |           |         |           |              |      | GPU memory, |     | running | CentOS | 8.  |     |     |     |
| constructs | a trace     | coverage |           | tree to | capture   | dependencies | be-  |             |     |         |        |     |     |     |     |
tweenrequestsandserviceinstances,leveragingthePageRank
algorithm to score potential root causes. B. Overall Evaluation
| Metrics-based: |         | RUN    | [21] | employs   | time | series     | forecasting |          |         |          |     |      |             |         |     |
| -------------- | ------- | ------ | ---- | --------- | ---- | ---------- | ----------- | -------- | ------- | -------- | --- | ---- | ----------- | ------- | --- |
|                |         |        |      |           |      |            |             | We first | compare | RCLAgent |     | with | trace-based | methods | and |
| for neural     | Granger | causal |      | discovery | and  | integrates | a per-      |          |         |          |     |      |             |         |     |
metrics-basedmethods.AsshowninTableI,alloftheseSOTA
sonalized PageRank algorithm to efficiently recommend the methods rely on initial service relationships and predefined
| top-k root   | causes. | Microscope  |        | [19]     | builds | causality | graphs    |              |              |          |             |                  |            |          |         |
| ------------ | ------- | ----------- | ------ | -------- | ------ | --------- | --------- | ------------ | ------------ | -------- | ----------- | ---------------- | ---------- | -------- | ------- |
|              |         |             |        |          |        |           |           | causal graph | construction |          | approaches. |                  | Therefore, | they     | require |
| and utilizes | a       | depth-first | search | strategy |        | to detect | front-end |              |              |          |             |                  |            |          |         |
|              |         |             |        |          |        |           |           | collecting   | multiple     | requests |             | and constructing |            | a causal | graph   |
anomalies.
beforerankingpotentialrootcausesbasedontheirweights.In
| LLM-based: |     | mABC |     | [26] | proposes | a   | multi-agent, |     |     |     |     |     |     |     |     |
| ---------- | --- | ---- | --- | ---- | -------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
contrast,RCLAgentonlyanalyzesasinglerequestanddirectly
blockchain-inspired collaboration framework where multiple identifies the exact root cause. Thus, the results presented for
| LLM-based | agents |     | follow | a   | structured | workflow | and |          |        |       |            |     |          |       |          |
| --------- | ------ | --- | ------ | --- | ---------- | -------- | --- | -------- | ------ | ----- | ---------- | --- | -------- | ----- | -------- |
|           |        |     |        |     |            |          |     | RCLAgent | in the | table | correspond | to  | Recall@1 | (R1), | since it |
collaborate through blockchain-inspired voting mechanisms. determines the exact root cause with just one request.
| Additionally,    |     | we implement |                        | a CoT-based |     | Approach | [31]      |          |            |             |         |           |      |           |          |
| ---------------- | --- | ------------ | ---------------------- | ----------- | --- | -------- | --------- | -------- | ---------- | ----------- | ------- | --------- | ---- | --------- | -------- |
|                  |     |              |                        |             |     |          |           | From     | the table, | we          | observe | that even | when | analyzing | only     |
| which implements |     | a            | naive chain-of-thought |             |     | (CoT)    | reasoning |          |            |             |         |           |      |           |          |
|                  |     |              |                        |             |     |          |           | a single | request    | to identify |         | the exact | root | cause,    | RCLAgent |
method for root cause localization. outperforms the SOTA methods’ Recall@10 (R10) results by
| 3) EvaluationMetrics: |     |     | Weusethetop-krecall(Recall@k) |     |     |     |     |               |     |       |     |              |          |     |          |
| --------------------- | --- | --- | ----------------------------- | --- | --- | --- | --- | ------------- | --- | ----- | --- | ------------ | -------- | --- | -------- |
|                       |     |     |                               |     |     |     |     | approximately |     | 2% to | 9%. | Furthermore, | compared |     | to other |
and mean reciprocal rank (MRR) to evaluate the accuracy of methods achieving the same Recall@1 (R1) performance,
rootcauselocalizationfollowingexistingworks[2],[19],[22], RCLAgent shows an average improvement of 30.44%. This
[25].
|     |     |     |     |     |     |     |     | demonstrates | the | superior | effectiveness |     | of  | RCLAgent, | even |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | -------- | ------------- | --- | --- | --------- | ---- |
Recall@k: Measures the likelihood that the true root when working with a single request.
•
cause appears within the top-k results in the ranked list. Next, we compare the performance of RCLAgent with
Specifically, it indicates whether the root cause is found LLM-based methods. As shown in Table II, when evaluating
within the first k predictions. In this paper, we evaluate on Recall@1 (R1), RCLAgent outperforms mABC by an
Recall@1, Recall@5, and Recall@10. averageof15.60%inaccuracy.Additionally,mABCcombines
MRR:isthemultiplicativeinverseoftherankoftheroot log data analysis alongside trace and metric data, and with a
•
causeintheresultlist.Iftherootcauseisnotincludedin highernumberofagentsinvolved,itsinferencespeedisslower

ADAPTIVEROOTCAUSELOCALIZATIONFORMICROSERVICESYSTEMSWITHMULTI-AGENTRECURSION-OF-THOUGHT 9
TABLEII Recall@1(R1)ensuresthatevenwithasimplemajorityvoting
EVALUATIONRESULTSCOMPAREDWITHLLM-BASEDMETHODS algorithm, RCLAgent delivers impressive results.
Approach A B Γ ∆ E Z
CoT 11.90 21.43 39.95 16.25 20.20 25.47 D. LLM Backbone Impact
mABC 51.87 62.22 74.23 56.35 52.08 51.65
Next, we address the second research question. To eval-
RCLAgent 71.13 78.57 90.24 64.24 65.42 72.41
uate the performance of RCLAgent across different LLM
backbones, we conducted experiments with four additional
compared to RCLAgent. In comparison with the naive CoT state-of-the-art LLMs beyond Claude-3.5-Sonnet: DeepSeek-
strategy, RCLAgent demonstrates a much more significant R1-Qwen,whichistheQwen2.5-32Bmodelfine-tunedondis-
advantage, outperforming it by up to 60% on certain datasets. tilled data released by DeepSeek; Qwen-2.5-Max and Qwen-
This result highlights that root cause localization is not a 2.5-Plus, both of which are closed-source models accessed
problem that can be easily solved by merely using LLMs, viaAPI;andLlama-3.1-70B, theoriginalopen-sourceversion
furtheremphasizingthenecessityofthedesignofRCLAgent. released by Meta.
TABLEIV
C. Group Ranking Evaluation
RCLAGENTWITHDIFFERENTLLMS
The previous experiments demonstrated that RCLAgent, by
analyzing a single request to provide the exact root cause, Model A B Γ ∆ E Z
can outperform SOTA methods. To further assess the supe- Claude-3.5-sonnet 71.13 78.57 90.24 64.34 65.42 72.41
riority of RCLAgent, we introduced a naive majority voting DeepSeek-R1-qwen 33.33 58.73 67.55 69.17 45.06 61.36
Qwen-2.5-max 13.17 21.23 33.66 13.17 33.66 13.68
algorithm. Specifically, for a set of multiple requests within a
Qwen-2.5-plus 39.79 70.45 52.78 49.48 35.46 52.06
time window, RCLAgent analyzes each request to identify its Llama-3.1-70B 7.92 22.42 17.51 18.14 6.97 8.76
correspondingrootcause.Therootcausesarethenaggregated
using a majority voting mechanism to determine the final root As shown in Table IV, the performance of RCLAgent is
cause,inamanneranalogoustoSOTAmethods,whichrelyon closely tied to the reasoning capabilities of the underlying
constructing a causal graph and ranking potential root causes. LLM backbone. In our experiments, Claude-3.5-Sonnet con-
Formally,themajorityvotingprocedurecanbedescribedas sistently achieved the best results, followed by DeepSeek-
follows.Let{r 1 ,r 2 ,...,r k }representtherootcausesidentified R1-Qwen. However, due to its relatively smaller size (32B),
forkrequestswithinatimewindow.Themajorityvoteisgiven DeepSeek-R1-Qwen underperformed on datasets A and B
by Equation 10, where Rˆ is the final predicted root cause, comparedtoQwen-2.5-Plus.Overall,RCLAgentwithClaude-
I(r i =r)istheindicatorfunctionthatequals1ifthei-throot 3.5-Sonnetoutperformedthesecond-bestmodelbyanaverage
cause r i matches the candidate root cause r, and 0 otherwise. of 14.79%.
The root cause Rˆ is the one that receives the highest number Additionally, we experimented with other models such as
of votes. GPT-4o and Llama-3-70B, but their performance was even
lower than the weakest models listed in Table IV. These
(cid:32) k (cid:33)
Rˆ =argmax (cid:88) I(r =r) (10) findings highlight that RCLAgent effectively leverages the
r i semantic understanding and logical reasoning capabilities of
i=1
large language models, achieving better results when paired
with more powerful inference engines.
TABLEIII
MRRCOMPARISON
E. Ablation Study
Approach A B Γ ∆ E Z
Then, to address the third research question, we recorded
CRISP 8.27 20.13 18.13 17.34 31.08 17.14 the complete reasoning path of RCLAgent during the experi-
TraceConstract 13.07 65.74 58.55 2.48 33.77 8.15
ments. Additionally, we extracted intermediate results at three
TraceRank 6.26 76.76 34.41 61.54 35.79 38.36
MicroRank 11.38 18.12 38.10 2.98 30.81 9.15 distinct stages and evaluated their effectiveness in root cause
RUN 11.72 3.12 25.65 5.62 7.58 8.95 localization.
MicroScope 23.76 4.55 37.46 13.24 21.38 21.33
RCLAgent 77.63 78.57 94.44 84.98 76.02 78.31 As shown in Figure 9, CR denotes Critical Reflection, and
FRrepresentsFinalReview.Thefiguredemonstratesthatthese
After applying the aforementioned majority voting algo- three stages significantly enhance RCLAgent’s root cause
rithm, we conducted a detailed analysis of RCLAgent and localizationperformance.Forinstance,ondatasetA,applying
the SOTA methods in terms of MRR, as shown in Table III. CriticalReflectionimprovedtheresultsofInitialReasoningby
From the table, it is evident that RCLAgent outperforms all approximately 34.51%. Similarly, Final Review consistently
the SOTA methods in terms of MRR. On average, RCLA- contributedtoperformancegains,albeittoalesserextentthan
gent achieves a 32.53% improvement over the second-best CriticalReflection.OndatasetsBandΓ,FinalReviewfurther
method. This demonstrates the superiority of RCLAgent in improved the results by approximately 6% beyond the gains
the group ranking evaluation. Its excellent performance in from Critical Reflection.

ADAPTIVEROOTCAUSELOCALIZATIONFORMICROSERVICESYSTEMSWITHMULTI-AGENTRECURSION-OF-THOUGHT 10
100
80
60
40
20
0
A B E Z
)%(
1@llaceR
Beyond machine learning-based methods, some researchers
RCLAgent w/o CR & FR RCLAgent w/o FR RCLAgent
have extended spectrum analysis techniques to improve the
practicality of trace-based root cause localization. For ex-
ample, Yu et al. [22] proposed MicroRank, which was later
extendedintoTraceRank[23]byintegratingspectrumanalysis
with a random walk-based method. Li et al. [38] combined
spectrum analysis with frequent pattern mining to identify
root cause service instances. More recently, Zhang et al. [25]
introduced TraceConstruct, which leverages sequence repre-
sentations along with contrast sequential pattern mining and
spectrumanalysistoefficientlylocalizemulti-dimensionalroot
causes.
Fig.9. AblationExperiment
B. LLM-based Failure Management
Overall,InitialReasoningaloneachievedanR1(Recall@1)
Large language models, with their advanced semantic un-
score of approximately 57.52%. Incorporating Critical Reflec-
derstanding and logical reasoning capabilities, have signifi-
tion led to an average improvement of 13.31%, while Final
cantly improved the field of failure management [2] and are
Review provided an additional 2.96% boost. These findings
increasingly becoming a focal point of research. Numerous
highlight the effectiveness and rationality of RCLAgent’s
LLM-basedapproacheshavebeenproposedtoaddressvarious
three-stage design.
aspects of failure management, including anomaly detection,
failure diagnosis, and automated mitigation [39]–[65].
VI. THREATSTOVALIDITY
Some studies have developed foundation models specifi-
Despite the promising results demonstrated by RCLAgent, cally for failure management. For example, Lag-Llama [39],
several limitations should be acknowledged. First, the imple- Timer [40], and TimesFM [41] pretrain foundation models
mentation and configuration of baseline approaches: CRISP, formetrics-basedanomalydetection.Similarly,ShellGPT[42]
MicroRank, and mABC have publicly available source code, trainsamodelcapableofautomaticallygeneratingshellscripts
which we directly utilized. For other state-of-the-art methods, for automated mitigation.
we implemented them based on the descriptions in their Otherapproachesadoptfine-tuningstrategiestotailorLLMs
respective papers. After implementation, we fine-tuned the forfailuremanagementtasks.Forinstance,AnomalyLLM[43]
results and selected the best configurations for all baselines and UniTime [44] employ full fine-tuning for anomaly detec-
through experimentation. Second, our evaluation primarily tion, while OWL [45] and LogLM [46] leverage parameter-
relies on the AIOps 2022 dataset, which, while extensive efficient fine-tuning techniques to build log analysis models.
and derived from real-world microservice systems, may not Since these fine-tuning approaches require significant com-
fully capture the diversity of failure scenarios encountered in putational resources and time, an increasing number of meth-
different operational contexts. Third, although our empirical ods,includingourwork,relyonprompt-basedtechniques.For
studybenefitsfrominsightsprovidedbymultipleprofessional example, RCACopilot [47] and Xpert [48] utilize in-context
SREs, the inherent subjectivity in their diagnostic processes learning (ICL) to structure diagnostic processes, ensuring
may introduce bias. accurate root cause analysis. LM-PACE [49] applies chain-
of-thought (CoT) reasoning to enhance GPT-4’s ability to
VII. RELATEDWORK analyze incident reports, while Hamadanian et al. [50] extend
A. Trace-Based Root Cause Localization this approach to generate mitigation solutions from incident
reports. Additionally, RAGLog [51] and LogRAG [52] use
With the advancement of distributed tracing and its sup-
retrieval-augmented generation (RAG) to enhance log-based
portinginfrastructure,researchershaveexploredvarioustrace-
anomaly detection through historical log retrieval.
based techniques for root cause localization. Several stud-
ies [1], [32], [33] have analyzed the role of distributed tracing
in diagnosing failures in large-scale microservices systems,
VIII. CONCLUSION
highlighting the importance of automated trace analysis for In this paper, we study the problem of adaptive root cause
effective root cause localization. localization for microservice systems. Initially, we conduct a
Recently, machine learning techniques have been widely comprehensive study on how SREs localize the root causes
adopted for trace-based root cause localization. For instance, of an abnormal request. This study reveals that human root
Zhou et al. [34] proposed MEPFL, a supervised learning- cause analysis exhibits three key characteristics: recursive-
based approach. Gan et al. [35] introduced Seer, a model ness, multi-dimensional expansion, and cross-modal reason-
leveraging CNNs and LSTMs for root cause analysis. Liu et ing. Based on our study, we introduce RCLAgent, an adap-
al. [36] proposed TraceAnomaly, an unsupervised approach tive root cause localization method for microservice systems
for anomaly detection in traces. Additionally, Gan et al. [37] that leverages a multi-agent recursion-of-thought framework.
developedSage,whichutilizesgraphneuralnetworksforroot RCLAgent employs a novel recursion-of-thought approach to
cause localization. guide the LLM’s reasoning process, effectively utilizing data

ADAPTIVEROOTCAUSELOCALIZATIONFORMICROSERVICESYSTEMSWITHMULTI-AGENTRECURSION-OF-THOUGHT 11
| from multiple | agents | and tool-assisted |     | analysis to | achieve | ac- |              |           |            |                 |      |                |         |              |
| ------------- | ------ | ----------------- | --- | ----------- | ------- | --- | ------------ | --------- | ---------- | --------------- | ---- | -------------- | ------- | ------------ |
|               |        |                   |     |             |         |     | [16] Z. Xie, | S. Zhang, | Y.         | Geng, Y. Zhang, | M.   | Ma, X.         | Nie, Z. | Yao, L. Xu,  |
|               |        |                   |     |             |         |     | Y. Sun,      | W.        | Li et al., | “Microservice   | root | cause analysis |         | with limited |
curaterootcauselocalization.Ourexperimentalevaluationson
|                |          |             |     |               |          |     | observability |     | through | intervention | recognition | in         | the latent | space,” in |
| -------------- | -------- | ----------- | --- | ------------- | -------- | --- | ------------- | --- | ------- | ------------ | ----------- | ---------- | ---------- | ---------- |
| various public | datasets | demonstrate |     | that RCLAgent | achieves |     |               |     |         |              |             |            |            |            |
|                |          |             |     |               |          |     | Proceedings   |     | of the  | 30th ACM     | SIGKDD      | Conference | on         | Knowledge  |
superiorperformancebyanalyzingasinglerequest,surpassing
DiscoveryandDataMining,2024,pp.6049–6060.
state-of-the-art methods that rely on multiple requests for [17] T. Wang, G. Qi, and T. Wu, “Kgroot: A knowledge graph-enhanced
methodforrootcauseanalysis,”ExpertSystemswithApplications,vol.
analysis.
255,p.124679,2024.
Infuturework,wewillfurtherexplorehowtoachievemore [18] L.Zhang,T.Jia,X.Tan,X.Huang,M.Jia,H.Liu,Z.Wu,andY.Li,
accurate and efficient root cause localization using smaller- “E-log:Fine-grainedelasticlog-basedanomalydetectionanddiagnosis
fordatabases,”IEEETransactionsonServicesComputing,2025.
scale models. Additionally, we are considering extending our [19] J.Lin,P.Chen,andZ.Zheng,“Microscope:Pinpointperformanceissues
approach to cover the entire failure management process. withcausalgraphsinmicro-serviceenvironments,”inService-Oriented
|     |     |     |     |     |     |     | Computing: |          | 16th International |       | Conference, | ICSOC | 2018,     | Hangzhou, |
| --- | --- | --- | --- | --- | --- | --- | ---------- | -------- | ------------------ | ----- | ----------- | ----- | --------- | --------- |
|     |     |     |     |     |     |     | China,     | November | 12-15,             | 2018, | Proceedings | 16.   | Springer, | 2018, pp. |
3–20.
REFERENCES [20] M. Li, Z. Li, K. Yin, X. Nie, W. Zhang, K. Sui, and D. Pei, “Causal
|              |          |            |         |                |          |        | inference-based |     | root          | cause analysis | for | online service | systems  | with   |
| ------------ | -------- | ---------- | ------- | -------------- | -------- | ------ | --------------- | --- | ------------- | -------------- | --- | -------------- | -------- | ------ |
|              |          |            |         |                |          |        | intervention    |     | recognition,” | in Proceedings |     | of the         | 28th ACM | SIGKDD |
| [1] X. Zhou, | X. Peng, | T. Xie, J. | Sun, C. | Ji, W. Li, and | D. Ding, | “Fault |                 |     |               |                |     |                |          |        |
ConferenceonKnowledgeDiscoveryandDataMining,2022,pp.3230–
| analysis | and debugging | of  | microservice | systems: Industrial |     | survey, |     |     |     |     |     |     |     |     |
| -------- | ------------- | --- | ------------ | ------------------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
3240.
benchmarksystem,andempiricalstudy,”IEEETransactionsonSoftware [21] C.-M.Lin,C.Chang,W.-Y.Wang,K.-D.Wang,andW.-C.Peng,“Root
Engineering,vol.47,no.2,pp.243–260,2018. causeanalysisinmicroserviceusingneuralgrangercausaldiscovery,”in
[2] L.Zhang,T.Jia,M.Jia,Y.Wu,A.Liu,Y.Yang,Z.Wu,X.Hu,P.S. ProceedingsoftheAAAIConferenceonArtificialIntelligence,vol.38,
Yu,andY.Li,“Asurveyofaiopsforfailuremanagementintheeraof no.1,2024,pp.206–213.
largelanguagemodels,”arXivpreprintarXiv:2406.11213,2024. [22] G. Yu, P. Chen, H. Chen, Z. Guan, Z. Huang, L. Jing, T. Weng,
[3] L.Zhang,T.Jia,M.Jia,Y.Wu,A.Liu,Y.Yang,Z.Wu,X.Hu,P.Yu, X. Sun, and X. Li, “Microrank: End-to-end latency issue localization
andY.Li,“Asurveyofaiopsintheeraoflargelanguagemodels,”ACM with extended spectrum analysis in microservice environments,” in
ComputingSurveys,2025. ProceedingsoftheWebConference2021,2021,pp.3087–3098.
[4] N. C. Mendonc¸a, P. Jamshidi, D. Garlan, and C. Pahl, “Developing [23] G.Yu,Z.Huang,andP.Chen,“Tracerank:Abnormalservicelocalization
|               |              |          |     |                             |     |      | with | dis-aggregated |     | end-to-end | tracing | data in cloud | native | systems,” |
| ------------- | ------------ | -------- | --- | --------------------------- | --- | ---- | ---- | -------------- | --- | ---------- | ------- | ------------- | ------ | --------- |
| self-adaptive | microservice | systems: |     | Challenges and directions,” |     | IEEE |      |                |     |            |         |               |        |           |
Software,vol.38,no.2,pp.70–79,2019. JournalofSoftware:EvolutionandProcess,vol.35,no.10,p.e2413,
| [5] M.Waseem,P.Liang,M.Shahin,A.DiSalle,andG.Ma´rquez,“Design, |     |     |     |     |     |     | 2023. |     |     |     |     |     |     |     |
| -------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
monitoring, and testing of microservices systems: The practitioners’ [24] Z. Zhang, M. K. Ramanathan, P. Raj, A. Parwal, T. Sherwood, and
perspective,” Journal of Systems and Software, vol. 182, p. 111061, M. Chabbi, “{CRISP}: Critical path analysis of {Large-Scale} mi-
croservicearchitectures,”in2022USENIXAnnualTechnicalConference
2021.
(USENIXATC22),2022,pp.655–672.
[6] L.Zhang,T.Jia,M.Jia,H.Liu,Y.Yang,Z.Wu,andY.Li,“Towards
close-to-zeroruntimecollectionoverhead:Raft-basedanomalydiagnosis [25] C. Zhang, Z. Dong, X. Peng, B. Zhang, and M. Chen, “Trace-based
onsystemfaultsfordistributedstoragesystem,”IEEETransactionson multi-dimensionalrootcauselocalizationofperformanceissuesinmi-
ServicesComputing,2024. croservicesystems,”inProceedingsoftheIEEE/ACM46thInternational
ConferenceonSoftwareEngineering,2024,pp.1–12.
[7] L.-Z.Zhang,X.-D.Huang,Y.-K.Wang,J.-L.Qiao,S.-X.Song,andJ.-
|          |             |             |     |                    |        |     | [26] W. Zhang, | H.  | Guo, | J. Yang, Z. | Tian, | Y. Zhang, | Y. Chaoran, | Z. Li, |
| -------- | ----------- | ----------- | --- | ------------------ | ------ | --- | -------------- | --- | ---- | ----------- | ----- | --------- | ----------- | ------ |
| M. Wang, | “Time-tired | compaction: | An  | elastic compaction | scheme | for |                |     |      |             |       |           |             |        |
T.Li,X.Shi,L.Zhengetal.,“mabc:Multi-agentblockchain-inspired
lsm-treebasedtime-seriesdatabase,”AdvancedEngineeringInformatics,
vol.59,p.102224,2024. collaboration for root cause analysis in micro-services architecture,”
[8] Y. Kang, X. Huang, S. Song, L. Zhang, J. Qiao, C. Wang, J. Wang, in Findings of the Association for Computational Linguistics: EMNLP
2024,2024,pp.4017–4033.
andJ.Feinauer,“Separationornot:Onhandingout-of-ordertime-series
[27] Z.Wang,Z.Liu,Y.Zhang,A.Zhong,J.Wang,F.Yin,L.Fan,L.Wu,
| data in | leveled lsm-tree,” | in  | 2022 IEEE | 38th International | Conference |     |     |     |     |     |     |     |     |     |
| ------- | ------------------ | --- | --------- | ------------------ | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
andQ.Wen,“Rcagent:Cloudrootcauseanalysisbyautonomousagents
| onDataEngineering(ICDE). |     |     | IEEE,2022,pp.3340–3352. |     |     |     |      |                |     |                |          |     |             |        |
| ------------------------ | --- | --- | ----------------------- | --- | --- | --- | ---- | -------------- | --- | -------------- | -------- | --- | ----------- | ------ |
|                          |     |     |                         |     |     |     | with | tool-augmented |     | large language | models,” | in  | Proceedings | of the |
[9] L.Zhang,T.Jia,M.Jia,Y.Li,Y.Yang,andZ.Wu,“Multivariatelog- 33rd ACM International Conference on Information and Knowledge
| based | anomaly detection | for | distributed | database,” in | Proceedings | of  |     |     |     |     |     |     |     |     |
| ----- | ----------------- | --- | ----------- | ------------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Management,2024,pp.4966–4974.
the30thACMSIGKDDConferenceonKnowledgeDiscoveryandData
|     |     |     |     |     |     |     | [28] K. Wang, | Y.  | Li, C. | Wang, T. Jia, | K. Chow, | Y. Wen, | Y.  | Dou, G. Xu, |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ------ | ------------- | -------- | ------- | --- | ----------- |
Mining,2024,pp.4256–4267.
C.Hou,J.Yaoetal.,“Characterizingjobmicroarchitecturalprofilesat
| [10] L. Zhang, | T. Jia, | K. Wang, | M. Jia, | Y. Yang, and Y. | Li, “Reducing |     |        |         |                |     |             |        |      |               |
| -------------- | ------- | -------- | ------- | --------------- | ------------- | --- | ------ | ------- | -------------- | --- | ----------- | ------ | ---- | ------------- |
|                |         |          |         |                 |               |     | scale: | Dataset | and analysis,” | in  | Proceedings | of the | 51st | International |
events to augment log-based anomaly detection models: An empirical ConferenceonParallelProcessing,2022,pp.1–11.
study,”inProceedingsofthe18thACM/IEEEInternationalSymposium
[29] Y.Yang,L.Wang,J.Gu,andY.Li,“Capturingrequestexecutionpath
| on Empirical | Software | Engineering | and | Measurement, | 2024, pp. | 538– |     |     |     |     |     |     |     |     |
| ------------ | -------- | ----------- | --- | ------------ | --------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
forunderstandingservicebehavioranddetectinganomalieswithoutcode
548.
|     |     |     |     |     |     |     | instrumentation,” |     | IEEE | Transactions | on  | Services | Computing, | vol. 16, |
| --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | ---- | ------------ | --- | -------- | ---------- | -------- |
[11] D.Wang,Z.Chen,J.Ni,L.Tong,Z.Wang,Y.Fu,andH.Chen,“Inter-
no.2,pp.996–1010,2022.
dependentcausalnetworksforrootcauselocalization,”inProceedings [30] J. Shen, H. Zhang, Y. Xiang, X. Shi, X. Li, Y. Shen, Z. Zhang,
of the 29th ACM SIGKDD Conference on Knowledge Discovery and Y. Wu, X. Yin, J. Wang et al., “Network-centric distributed tracing
DataMining,2023,pp.5051–5060.
|     |     |     |     |     |     |     | with | deepflow: | Troubleshooting |     | your microservices |     | in zero | code,” in |
| --- | --- | --- | --- | --- | --- | --- | ---- | --------- | --------------- | --- | ------------------ | --- | ------- | --------- |
[12] S.Zhang,S.Xia,W.Fan,B.Shi,X.Xiong,Z.Zhong,M.Ma,Y.Sun,
ProceedingsoftheACMSIGCOMM2023Conference,2023,pp.420–
andD.Pei,“Failurediagnosisinmicroservicesystems:Acomprehensive
437.
survey and analysis,” ACM Transactions on Software Engineering and [31] J.Wei,X.Wang,D.Schuurmans,M.Bosma,F.Xia,E.Chi,Q.V.Le,
Methodology,2024. D. Zhou et al., “Chain-of-thought prompting elicits reasoning in large
[13] Q.Yu,N.Zhao,M.Li,Z.Li,H.Wang,W.Zhang,K.Sui,andD.Pei,“A languagemodels,”Advancesinneuralinformationprocessingsystems,
surveyonintelligentmanagementofalertsandincidentsinitservices,”
vol.35,pp.24824–24837,2022.
JournalofNetworkandComputerApplications,p.103842,2024.
[32] B.Li,X.Peng,Q.Xiang,H.Wang,T.Xie,J.Sun,andX.Liu,“Enjoy
[14] Y. Sun, Z. Lin, B. Shi, S. Zhang, S. Ma, P. Jin, Z. Zhong, L. Pan, your observability: an industrial survey of microservice tracing and
Y.Guo,andD.Pei,“Interpretablefailurelocalizationformicroservice analysis,”EmpiricalSoftwareEngineering,vol.27,pp.1–28,2022.
systems based on graph autoencoder,” ACM Transactions on Software [33] S. Luo, H. Xu, C. Lu, K. Ye, G. Xu, L. Zhang, Y. Ding, J. He,
EngineeringandMethodology,vol.34,no.2,pp.1–28,2025. andC.Xu,“Characterizingmicroservicedependencyandperformance:
[15] Z. Zhu, C. Lee, X. Tang, and P. He, “Hemirca: Fine-grained root Alibabatraceanalysis,”inProceedingsoftheACMsymposiumoncloud
causeanalysisformicroserviceswithheterogeneousdatasources,”ACM computing,2021,pp.412–426.
TransactionsonSoftwareEngineeringandMethodology,vol.33,no.8, [34] X. Zhou, X. Peng, T. Xie, J. Sun, C. Ji, D. Liu, Q. Xiang, and
pp.1–25,2024. C. He, “Latent error prediction and fault localization for microservice

ADAPTIVEROOTCAUSELOCALIZATIONFORMICROSERVICESYSTEMSWITHMULTI-AGENTRECURSION-OF-THOUGHT 12
applications by learning from system trace logs,” in Proceedings of [53] L.Zhang,T.Jia,M.Jia,Y.Wu,H.Liu,andY.Li,“Xraglog:Aresource-
the 2019 27th ACM joint meeting on European software engineering efficient and context-aware log-based anomaly detection method using
conferenceandsymposiumonthefoundationsofsoftwareengineering, retrieval-augmentedgeneration,”inAAAI2025WorkshoponPreventing
2019,pp.683–694. andDetectingLLMMisinformation(PDLM),2025.
[35] Y. Gan, Y. Zhang, K. Hu, D. Cheng, Y. He, M. Pancholi, and [54] ——, “Scalalog: Scalable log-based failure diagnosis using llm,” in
C. Delimitrou, “Seer: Leveraging big data to navigate the complexity ICASSP2025-2025IEEEInternationalConferenceonAcoustics,Speech
of performance debugging in cloud microservices,” in Proceedings of andSignalProcessing(ICASSP). IEEE,2025,pp.1–5.
the twenty-fourth international conference on architectural support for [55] L. Zhang, Y. Zhai, T. Jia, X. Huang, C. Duan, and Y. Li, “Agentfm:
programminglanguagesandoperatingsystems,2019,pp.19–33. Role-awarefailuremanagementfordistributeddatabaseswithllm-driven
[36] P. Liu, H. Xu, Q. Ouyang, R. Jiao, Z. Chen, S. Zhang, J. Yang, multi-agents,”arXivpreprintarXiv:2504.06614,2025.
L.Mo,J.Zeng,W.Xueetal.,“Unsuperviseddetectionofmicroservice [56] L.Zhang,Y.Zhai,T.Jia,C.Duan,S.Yu,J.Gao,B.Ding,Z.Wu,and
traceanomaliesthroughservice-leveldeepbayesiannetworks,”in2020 Y. Li, “Thinkfl: Self-refining failure localization for microservice sys-
IEEE31stInternationalSymposiumonSoftwareReliabilityEngineering tems via reinforcement fine-tuning,” arXiv preprint arXiv:2504.18776,
(ISSRE). IEEE,2020,pp.48–58. 2025.
[37] Y. Gan, M. Liang, S. Dev, D. Lo, and C. Delimitrou, “Sage: practical [57] L. Zhang, T. Jia, M. Jia, and Y. Li, “Logdb: Multivariate log-based
and scalable ml-driven performance debugging in microservices,” in failure diagnosis for distributed databases (extended from multilog),”
Proceedingsofthe26thACMInternationalConferenceonArchitectural arXivpreprintarXiv:2505.01676,2025.
SupportforProgrammingLanguagesandOperatingSystems,2021,pp. [58] C.Duan,T.Jia,Y.Yang,G.Liu,J.Liu,H.Zhang,Q.Zhou,Y.Li,and
135–151. G.Huang,“Eagerlog:Activelearningenhancedretrievalaugmentedgen-
[38] Z.Li,J.Chen,R.Jiao,N.Zhao,Z.Wang,S.Zhang,Y.Wu,L.Jiang, eration for log-based anomaly detection,” in ICASSP 2025-2025 IEEE
L.Yan,Z.Wangetal.,“Practicalrootcauselocalizationformicroservice International Conference on Acoustics, Speech and Signal Processing
systems via trace analysis,” in 2021 IEEE/ACM 29th International (ICASSP). IEEE,2025,pp.1–5.
SymposiumonQualityofService(IWQOS). IEEE,2021,pp.1–10. [59] M. He, T. Jia, C. Duan, H. Cai, Y. Li, and G. Huang, “Weakly-
[39] K. Rasul, A. Ashok, A. R. Williams, A. Khorasani, G. Adamopoulos, supervised log-based anomaly detection with inexact labels via multi-
R. Bhagwatkar, M. Bilosˇ, H. Ghonia, N. Hassen, A. Schneider et al., instance learning,” in 2025 IEEE/ACM 47th International Conference
“Lag-llama: Towards foundation models for time series forecasting,” on Software Engineering (ICSE). IEEE Computer Society, 2025, pp.
inR0-FoMo:RobustnessofFew-shotandZero-shotLearninginLarge 726–726.
FoundationModels,2023. [60] C.Duan,Y.Yang,T.Jia,G.Liu,J.Liu,H.Zhang,Q.Zhou,Y.Li,and
[40] Y. Liu, H. Zhang, C. Li, X. Huang, J. Wang, and M. Long, “Timer: G.Huang,“Famos:Faultdiagnosisformicroservicesystemsthroughef-
generative pre-trained transformers are large time series models,” in fectivemulti-modaldatafusion,”in2025IEEE/ACM47thInternational
Proceedingsofthe41stInternationalConferenceonMachineLearning, ConferenceonSoftwareEngineering(ICSE). IEEEComputerSociety,
2024,pp.32369–32399. 2025,pp.610–610.
[41] A. Das, W. Kong, R. Sen, and Y. Zhou, “A decoder-only foundation [61] P. Xiao, T. Jia, C. Duan, H. Cai, Y. Li, and G. Huang, “Logcae:
model for time-series forecasting,” in Forty-first International Confer- Anapproachforlog-basedanomalydetectionwithactivelearningand
enceonMachineLearning,2024. contrastive learning,” in 2024 IEEE 35th International Symposium on
[42] J.Shi,S.Jiang,B.Xu,J.Liang,Y.Xiao,andW.Wang,“Shellgpt:Gener- SoftwareReliabilityEngineering(ISSRE). IEEE,2024,pp.144–155.
ative pre-trained transformer model for shell language understanding,” [62] M. He, T. Jia, C. Duan, H. Cai, Y. Li, and G. Huang, “Llmelog:
in 2023 IEEE 34th International Symposium on Software Reliability Anapproachforanomalydetectionbasedonllm-enrichedlogevents,”
Engineering(ISSRE). IEEE,2023,pp.671–682. in 2024 IEEE 35th International Symposium on Software Reliability
[43] S. Liu, D. Yao, L. Fang, Z. Li, W. Li, K. Feng, X. Ji, and J. Bi, Engineering(ISSRE). IEEE,2024,pp.132–143.
“Anomalyllm: Few-shot anomaly edge detection for dynamic graphs [63] C. Duan, T. Jia, H. Cai, Y. Li, and G. Huang, “Afalog: A general
usinglargelanguagemodels,”arXivpreprintarXiv:2405.07626,2024. augmentation framework for log-based anomaly detection with active
[44] X.Liu,J.Hu,Y.Li,S.Diao,Y.Liang,B.Hooi,andR.Zimmermann, learning,” in 2023 IEEE 34th International Symposium on Software
“Unitime:Alanguage-empoweredunifiedmodelforcross-domaintime ReliabilityEngineering(ISSRE). IEEE,2023,pp.46–56.
series forecasting,” in Proceedings of the ACM Web Conference 2024, [64] C. Duan, T. Jia, Y. Li, and G. Huang, “Aclog: An approach to
2024,pp.4095–4106. detecting anomalies from system logs with active learning,” in 2023
[45] H.Guo,J.Yang,J.Liu,L.Yang,L.Chai,J.Bai,J.Peng,X.Hu,C.Chen, IEEEInternationalConferenceonWebServices(ICWS). IEEE,2023,
D.Zhangetal.,“Owl:Alargelanguagemodelforitoperations,”arXiv pp.436–443.
preprintarXiv:2309.09298,2023. [65] L. Zhang, L. Fang, C. Duan, M. He, L. Pan, P. Xiao, S. Huang,
[46] Y.Liu,Y.Ji,S.Tao,M.He,W.Meng,S.Zhang,Y.Sun,Y.Xie,B.Chen, Y. Zhai, X. Hu, P. S. Yu et al., “A survey on parallel text generation:
andH.Yang,“Loglm:Fromtask-basedtoinstruction-basedautomated From parallel decoding to diffusion language models,” arXiv preprint
loganalysis,”arXivpreprintarXiv:2410.09352,2024. arXiv:2508.08712,2025.
[47] Y. Chen, H. Xie, M. Ma, Y. Kang, X. Gao, L. Shi, Y. Cao, X. Gao,
H.Fan,M.Wenetal.,“Automaticrootcauseanalysisvialargelanguage
modelsforcloudincidents,”inProceedingsoftheNineteenthEuropean
ConferenceonComputerSystems,2024,pp.674–688.
[48] Y.Jiang,C.Zhang,S.He,Z.Yang,M.Ma,S.Qin,Y.Kang,Y.Dang,
S.Rajmohan,Q.Linetal.,“Xpert:Empoweringincidentmanagement
withqueryrecommendationsvialargelanguagemodels,”inProceedings
oftheIEEE/ACM46thInternationalConferenceonSoftwareEngineer-
ing,2024,pp.1–13.
[49] D.Zhang,X.Zhang,C.Bansal,P.Las-Casas,R.Fonseca,andS.Raj-
mohan,“Lm-pace:Confidenceestimationbylargelanguagemodelsfor
effectiverootcausingofcloudincidents,”inCompanionProceedingsof
the32ndACMInternationalConferenceontheFoundationsofSoftware
Engineering,2024,pp.388–398.
[50] P. Hamadanian, B. Arzani, S. Fouladi, S. K. R. Kakarla, R. Fonseca,
D.Billor,A.Cheema,E.Nkposong,andR.Chandra,“Aholisticview
ofai-drivennetworkincidentmanagement,”inProceedingsofthe22nd
ACMWorkshoponHotTopicsinNetworks,2023,pp.180–188.
[51] J.Pan,W.S.Liang,andY.Yidi,“Raglog:Loganomalydetectionusing
retrievalaugmentedgeneration,”in2024IEEEWorldForumonPublic
SafetyTechnology(WFPST). IEEE,2024,pp.169–174.
[52] W. Zhang, Q. Zhang, E. Yu, Y. Ren, Y. Meng, M. Qiu, and J. Wang,
“Lograg: Semi-supervised log-based anomaly detection with retrieval-
augmentedgeneration,”in2024IEEEInternationalConferenceonWeb
Services(ICWS). IEEE,2024,pp.1100–1102.