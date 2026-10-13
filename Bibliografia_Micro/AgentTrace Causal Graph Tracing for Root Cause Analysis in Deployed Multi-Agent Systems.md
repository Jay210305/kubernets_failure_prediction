PublishedasaworkshoppaperatICLR2026AIWILDWorkshop
| AGENTTRACE: |     |     | CAUSAL |     | GRAPH |     | TRACING |     |     | ROOT |
| ----------- | --- | --- | ------ | --- | ----- | --- | ------- | --- | --- | ---- |
FOR
| CAUSE | ANALYSIS |     |     | DEPLOYED |     |     | MULTI-AGENT |     |     | SYS- |
| ----- | -------- | --- | --- | -------- | --- | --- | ----------- | --- | --- | ---- |
IN
TEMS
ZhaohuiGeoffreyWang
USCViterbiSchoolofEngineering
zwang000@usc.edu
ORCID:0009-0006-1187-1903
6202 raM 61  ]GL.sc[  1v88641.3062:viXra
ABSTRACT
Asmulti-agentAIsystemsareincreasinglydeployedinreal-worldsettings—from
|     | automated                                               | customer        | support        | to         | DevOps        | remediation—failures |              | become            |           | harder |
| --- | ------------------------------------------------------- | --------------- | -------------- | ---------- | ------------- | -------------------- | ------------ | ----------------- | --------- | ------ |
|     | to diagnose                                             | due             | to cascading   | effects,   | hidden        | dependencies,        |              | and long          | execution |        |
|     | traces.                                                 | We present      | AGENTTRACE,    |            | a lightweight |                      | causal       | tracing framework |           | for    |
|     | post-hocfailurediagnosisindeployedmulti-agentworkflows. |                 |                |            |               |                      |              | AGENTTRACEre-     |           |        |
|     | constructs                                              | causal          | graphs from    | execution  | logs,         | traces               | backward     | from              | error     | mani-  |
|     | festations,                                             | and             | rankscandidate | rootcauses |               | usinginterpretable   |              | structuraland     |           | po-    |
|     | sitional                                                | signals—without |                | requiring  | LLM           | inference            | at debugging | time.             | Across    | a      |
|     | diverse                                                 | benchmark       | of multi-agent |            | failure       | scenarios            | designed     | to reflect        | common    |        |
deploymentpatterns,AGENTTRACElocalizesrootcauseswithhighaccuracyand
|     | sub-second | latency,                                                       | significantly |     | outperforming |     | both heuristic | and | LLM-based |     |
| --- | ---------- | -------------------------------------------------------------- | ------------- | --- | ------------- | --- | -------------- | --- | --------- | --- |
|     | baselines. | Ourresultssuggestthatcausaltracingprovidesapracticalfoundation |               |     |               |     |                |     |           |     |
forimprovingthereliabilityandtrustworthinessofagenticsystemsinthewild.
1 INTRODUCTION
Multi-agent systems powered by large language models (LLMs) have emerged as a powerful
paradigm for solving complex tasks through agent collaboration (Wu et al., 2023; Hong et al.,
2024). Inthesesystems,specializedagents—suchasplanners,coders,reviewers,andexecutors—
coordinatethroughmessagepassingtoaccomplishgoalsthatwouldbedifficultforasingleagent.
Indeployedagentsystems—suchasautomatedcustomersupport,DevOpsremediation,orresearch
assistants—failures often surface far downstream from their root causes. By the time an error is
observed, multiple agents may have already acted on corrupted assumptions, making manual de-
bugging slow and unreliable. The distributed and emergent nature of these workflows means that
traditionaldebuggingapproaches,whichexamineindividualcomponentsinisolation,failtocapture
thecross-agentcausaldependenciesthatleadtosystem-levelfailures.
WeproposeAGENTTRACE,alightweightframeworkthataddressesthischallengethroughthreekey
contributions:
1. CausalGraphConstruction: Wemodelmulti-agentexecutionasadirectedgraphwhere
nodesrepresentagentactionsandedgescaptureinformationflowandcausaldependencies.
2. Backward Tracing Algorithm: Starting from the point of error manifestation, we trace
backwardthroughthecausalgraphtoidentifyallpotentiallyrelevantupstreamdecisions.
3. EmpiricalStudyofFailureLocalization:Wedemonstratethatlightweightcausaltracing
with interpretable positional and structural features can substantially improve debugging
accuracyandlatencyinsettingsthatresemblereal-worldagentdeployments—withoutre-
quiringexpensiveLLMinferenceatdebuggingtime.
Whileourbenchmarkscenariosaresyntheticallyconstructed,theyaredesignedtocapturecommon
failurepatternsobservedindeployedmulti-agentsystems,suchasearlyplanningerrorscascading
1

PublishedasaworkshoppaperatICLR2026AIWILDWorkshop
throughexecution. Ourevaluationacross550failurescenariosin10domainsshowsthat AGENT-
TRACE achieves high localization accuracy with sub-second latency, significantly outperforming
bothheuristicandLLM-basedbaselines.
2 RELATED WORK
Multi-AgentSystems. RecentframeworkslikeAutoGen(Wuetal.,2023)andMetaGPT(Hong
etal.,2024)enablesophisticatedmulti-agentcollaboration,oftenbuildingonreasoning-and-acting
paradigms(Yaoetal.,2023). However, debuggingsupportinthesesystemsremainslimited, typi-
callyrelyingonmanualloginspection.
AI System Debugging. Prior work on AI interpretability has focused on neural network inter-
nals(Simonyanetal.,2014;Kimetal.,2018)orreasoningchains(Weietal.,2022).Self-debugging
approaches(Chenetal.,2024)useLLMstoidentifyerrorsbutrequireexpensiveinferencecallsand
strugglewithcross-agentissues.
Distributed Tracing. Systems like Jaeger (Technologies, 2017) and Zipkin (Twitter, 2012) pro-
videdistributedtracingformicroservices. Weadapttheseconceptsformulti-agentLLMsystems,
where“messages”betweenagentscarrysemanticcontentratherthanjustrequestmetadata.
Root Cause Analysis. Traditional RCA approaches use statistical methods (Soldani & Brogi,
2022) or graph algorithms (Page et al., 1999). Recent work explores LLM-based agents for root
causeanalysisincloudsystems(Royetal.,2024),butthesemethodsarenotdesignedforthespe-
cificstructureofmulti-agentworkflows.
3 AGENTTRACE FRAMEWORK
3.1 PROBLEMDEFINITION
Given a multi-agent execution trace T that terminates in an error state, our goal is to identify the
rootcausenode—theearliestdecisionpointwhosecorrectionwouldpreventtheerror. Formally,let
G=(V,E)beadirectedacyclicgraphwhere:
• V ={v ,v ,...,v }representsagentactions(toolcalls,messages,decisions)
1 2 n
• E ⊆V ×V representscausaldependenciesbetweenactions
• v ∈V isthenodewheretheerrormanifests
error
• v ∈V istheground-truthrootcause
root
3.2 CAUSALGRAPHCONSTRUCTION
Weconstructthecausalgraphfromexecutionlogsbyidentifyingthreetypesofedges:
Sequential edges connect consecutive actions by the same agent, capturing the agent’s reasoning
flow.
Communication edges connect message-send events to message-receive events between different
agents.
Datadependencyedgesconnectactionsthatproducedatatoactionsthatconsumethatdata,iden-
tifiedthroughvariablereferencetracking.
3.3 BACKWARDTRACING
Givenanerrornodev ,weperformbreadth-firstbackwardtraversaltocollectallancestornodes
error
withinaspecifieddepthlimit:
2

PublishedasaworkshoppaperatICLR2026AIWILDWorkshop
Algorithm1BackwardTracing
| Require: Errornodev | ,graphG,maxdepthd |     |     |     |
| ------------------- | ----------------- | --- | --- | --- |
error
Ensure: CandidatesetC
| 1: C ←{v } |     |     |     |     |
| ---------- | --- | --- | --- | --- |
error
| 2: frontier←{v | }   |     |     |     |
| -------------- | --- | --- | --- | --- |
error
3: fori=1toddo
| new frontier←∅ |     |     |     |     |
| -------------- | --- | --- | --- | --- |
4:
| 5: forv ∈frontierdo |     |     |     |     |
| ------------------- | --- | --- | --- | --- |
6: foru∈parents(v)do
| 7: ifu∈/ | C then       |              |     |     |
| -------- | ------------ | ------------ | --- | --- |
| 8: C     | ←C∪{u}       |              |     |     |
| new      | frontier←new | frontier∪{u} |     |     |
9:
| 10: endif |     |     |     |     |
| --------- | --- | --- | --- | --- |
11: endfor
12: endfor
| 13: frontier←new | frontier |     |     |     |
| ---------------- | -------- | --- | --- | --- |
14: endfor
| return C |     |     |     |     |
| -------- | --- | --- | --- | --- |
15:
3.4 NODERANKINGALGORITHM
Werankcandidatenodesusingaweightedlinearcombinationoffivefeaturegroups:
(cid:88)
|     |     | score(v)= | w i ·F i (v) | (1) |
| --- | --- | --------- | ------------ | --- |
i∈{p,s,c,f,e}
| EachgroupscoreF | (v)isthemeanofitsconstituentnormalizedfeatures: |     |     |     |
| --------------- | ----------------------------------------------- | --- | --- | --- |
i
1 (cid:88)
fˆ(v)
|     |     | F i (v)= | j   | (2) |
| --- | --- | -------- | --- | --- |
|G |
i j∈Gi
isthesetoffeaturesingroupiandfˆ(v)∈[0,1]isthemin-maxnormalizedfeaturevalue
whereG i j
(seeAppendixB).
whereeachF (v)aggregatesnormalizedfeaturesforgroupi,andtheweightsw aredeterminedvia
i i
gridsearchonaheld-outvalidationsetof50scenarios(detailsinAppendixB).Thefeaturegroups
andtheirlearnedweightsare:
Position Features (w = 0.70). Position-based features capture where the node occurs in the
p
execution:
| • Normalizedposition: |                  | pos(v)/|V| |     |     |
| --------------------- | ---------------- | ---------- | --- | --- |
| • Distancetoerror:    | Hopcountfromvtov |            |     |     |
error
| • Depthintrace: | Stepsfromtheinitialnode |     |     |     |
| --------------- | ----------------------- | --- | --- | --- |
StructureFeatures(w =0.20). Graphtopologyfeaturesindicatingnodeimportance:
s
| • Out-degree:         | Numberofdownstreamnodesaffected      |                                         |     |     |
| --------------------- | ------------------------------------ | --------------------------------------- | --- | --- |
| • Betweenness:        | Fractionofpathspassingthroughv       |                                         |     |     |
| • Fanoutratio:        | Proportionoftotalnodesreachablefromv |                                         |     |     |
| ContentFeatures(w     | c =0.05).                            | Semanticindicatorsofproblematiccontent: |     |     |
| • Errorkeywords:      | Presenceoftermslike“error”,“failed”  |                                         |     |     |
| • Uncertaintymarkers: |                                      | Termslike“maybe”,“notsure”              |     |     |
| • Contentlength:      | Unusuallyshortorlongoutputs          |                                         |     |     |
3

PublishedasaworkshoppaperatICLR2026AIWILDWorkshop
FlowFeatures(w =0.03). Agentinteractionpatterns:
f
• Agentswitch: Whethernodeinvolvescross-agentcommunication
• Rolecriticality: Importanceoftheagent’srole
ConfidenceFeatures(w =0.02). Model-reportedconfidencewhenavailable:
e
• Statedconfidence: Explicitconfidencescores
• Hedginglanguage: Implicituncertaintyindicators
4 BENCHMARK
4.1 SCENARIOGENERATION
Wecreatedabenchmarkof550syntheticmulti-agentfailurescenariosacross10domains(Table1).
Eachscenarioincludes:
• Acompleteexecutiontracewith8-15agentactions
• Asystematicallyinjectedbugataspecificnode
• Ground-truthannotationoftherootcausenode
Table1: Benchmarkdomainsandscenariocounts
Domain Scenarios
SoftwareDevelopment 52
CustomerService 51
ResearchAnalysis 51
Planning&Scheduling 46
FinancialTrading 50
HealthcareCoordination 60
LegalDocumentAnalysis 60
EducationalTutoring 60
FinancialAdvisory 60
DevOpsAutomation 60
Total 550
4.2 BUGTYPES
Weinjectfivecategoriesofbugs:
• Logicerrors: Incorrectconditionaldecisions
• Communicationfailures: Messagemisinterpretation
• Datacorruption: Incorrectdatatransformation
• Missingvalidation: Skippedverificationsteps
• Roleconfusion: Agentactingoutsideitsexpertise
4.3 GROUNDTRUTHANNOTATION
Eachscenario’sgroundtruthwasestablishedthrough: (1)controlledbuginjectionataknownstep,
(2)verificationthatremovingthebugpreventstheerror,and(3)confirmationthatthebug’seffects
propagatetotheerrornode.
4

PublishedasaworkshoppaperatICLR2026AIWILDWorkshop
5 EXPERIMENTS
5.1 EVALUATIONMETRICS
• Hit@k: Proportionofscenarioswheregroundtruthappearsintop-kpredictions
MeanReciprocalRank(MRR):Averageof1/rank
•
5.2 BASELINES
• Random: Uniformlyrandomnodeselection
• FirstNode: Alwaysselectthefirstnode
• LastNode: Selectthenodeimmediatelybeforeerror
• LLMAnalysis: GPT-4withfulltraceandpromptengineering
5.3 MAINRESULTS
Table2showsthatAGENTTRACEsignificantlyoutperformsallbaselines.
Table 2: Root cause localization accuracy on 550-scenario benchmark. 95% confidence intervals
frombootstrapresampling.
| Method      | Hit@1       | Hit@3       | MRR  |
| ----------- | ----------- | ----------- | ---- |
| Random      | 9.1%        | 27.3%       | 0.18 |
| FirstNode   | 3.6%        | 10.9%       | 0.07 |
| LastNode    | 12.7%       | 38.2%       | 0.25 |
| LLMAnalysis | 68.5%       | 81.4%       | 0.74 |
| AGENTTRACE  | 94.9%       | 98.4%       | 0.97 |
|             | [92.9,96.7] | [96.9,99.4] |      |
StatisticalsignificancetestingusingMcNemar’stestconfirmsthatAGENTTRACEsignificantlyout-
performsallbaselines(p<0.001). Theeffectsize(Cohen’sh)comparedtoLLMAnalysisis0.77,
indicatingalargepracticaldifference.
5.4 ABLATIONSTUDY
Table 3 shows Hit@1 when using each feature group in isolation. Position features alone achieve
87.3%accuracy,confirmingthatbuglocationpatternsarehighlypredictiveinourbenchmark.
| Table3: Ablationstudy: | Hit@1witheachfeaturegroupalone |       |     |
| ---------------------- | ------------------------------ | ----- | --- |
| FeatureGroup           |                                | Hit@1 |     |
| Positiononly           |                                | 87.3% |     |
| Structureonly          |                                | 34.5% |     |
| Contentonly            |                                | 28.7% |     |
| Flowonly               |                                | 15.2% |     |
| Confidenceonly         |                                | 12.1% |     |
| Allfeatures            |                                | 94.9% |     |
5.5 PERFORMANCEBYDOMAIN
Table 4 shows consistent performance across domain groups, with technical domains (Software,
DevOps)slightlyoutperformingothers.
5

PublishedasaworkshoppaperatICLR2026AIWILDWorkshop
Table4: Performancebydomaingroup
DomainGroup Hit@1 Scenarios
Technical(Dev,DevOps) 96.4% 112
Business(Trading,Finance) 93.6% 110
Service(Customer,Healthcare) 93.7% 111
Knowledge(Research,Legal,Education) 96.5% 171
Planning 91.3% 46
5.6 RUNTIMEPERFORMANCE
AGENTTRACEprocessestracesin0.12secondsonaverage,comparedto8.3secondsforLLM-based
analysis. This69×speedupenablesinteractivedebuggingworkflows.
6 DISCUSSION
Why Position Features Dominate. Importantly, the dominance of positional signals should not
be interpreted solely as a benchmark artifact. In many deployed agent systems, early planning or
routingdecisionsshapetheentiredownstreamexecution, makingearly-stageerrorsdisproportion-
ately impactful. Our analysis reveals that bugs occurring earlier in execution traces tend to cause
errorsthatmanifestlater—apatternthatreflectsafundamentalpropertyofhierarchicalmulti-agent
workflowswhereupstreamdecisionsconstraindownstreamactions.
Limitations. Ourcurrentevaluationfocusesonsyntheticscenarioswithsinglerootcauses. Real
multi-agentfailuresofteninvolvemultiplecontributingfactorsandmorecomplexcausalstructures.
Additionally, ourbenchmarkassumesaccurateexecutionlogging, whichmaynotalwaysbeavail-
ableinproductionsystems.
ImplicationsforAgentSafety. Asmulti-agentsystemsaredeployedinhigh-stakesdomains,the
abilitytoquicklyidentifyandunderstandfailuresbecomescriticalformaintainingtrustandsafety.
AGENTTRACEprovidesafoundationforpost-hocanalysisthatcaninformbothimmediatefixesand
systematicimprovementstoagentdesign.
7 CONCLUSION
We presented AGENTTRACE, a causal graph-based framework for root cause localization in de-
ployed multi-agent systems. Our approach achieves high accuracy on a diverse benchmark while
maintainingsub-secondlatency. Theframework’srelianceoninterpretablestructuralandpositional
features—rather than expensive LLM inference—makes it practical for interactive debugging in
productionenvironments. Futureworkwillextendtheapproachtohandlemultipleconcurrentroot
causesandvalidateonproductiontraces.WehopeAGENTTRACEcanserveasapracticaldiagnostic
layerforagenticsystemsdeployedinreal-world,reliability-criticalenvironments.
REPRODUCIBILITYSTATEMENT
Our benchmark generation code, evaluation scripts, and all experimental results are available at
https://github.com/zwang000/AgentTrace. The benchmark includes complete exe-
cutiontraces,groundtruthannotations,andbaselineimplementations.
REFERENCES
XinyunChen,MaxwellLin,NathanaelScha¨rli,andDennyZhou. Teachinglargelanguagemodels
toself-debug. InInternationalConferenceonLearningRepresentations,2024.
6

PublishedasaworkshoppaperatICLR2026AIWILDWorkshop
SiruiHong, MingchenZhuge, JonathanChen, XiawuZheng, YuhengCheng, CeyaoZhang, Jinlin
Wang,ZiliWang,StevenYau,ZijuanLin,etal. Metagpt: Metaprogrammingforamulti-agent
collaborativeframework. InInternationalConferenceonLearningRepresentations,2024.
BeenKim,MartinWattenberg,JustinGilmer,CarrieCai,JamesWexler,FernandaViegas,andRory
Sayres. Interpretability beyond feature attribution: Quantitative testing with concept activation
vectors(tcav). InInternationalConferenceonMachineLearning,pp.2668–2677,2018.
LawrencePage,SergeyBrin,RajeevMotwani,andTerryWinograd. Thepagerankcitationranking:
Bringingordertotheweb. InStanfordInfoLabTechnicalReport,1999.
DevjeetRoy,XuchaoZhang,RashiBhave,ChetanBansal,PedroLas-Casas,RodrigoFonseca,and
SaravanRajmohan. Exploringllm-basedagentsforrootcauseanalysis. InCompanionProceed-
ings of the 32nd ACM International Conference on the Foundations of Software Engineering,
2024.
Karen Simonyan, Andrea Vedaldi, and Andrew Zisserman. Deep inside convolutional networks:
Visualisingimageclassificationmodelsandsaliencymaps. InICLRWorkshop,2014.
Jacopo Soldani and Antonio Brogi. Anomaly detection and failure root cause analysis in (micro)
service-basedcloudapplications: Asurvey. ACMComputingSurveys,55(3):1–39,2022.
Uber Technologies. Jaeger: Open source, end-to-end distributed tracing. https://www.
jaegertracing.io/,2017.
Twitter. Zipkin: Adistributedtracingsystem. https://zipkin.io/,2012.
JasonWei,XuezhiWang,DaleSchuurmans,MaartenBosma,BrianIchter,FeiXia,EdChi,Quoc
Le, and Denny Zhou. Chain-of-thought prompting elicits reasoning in large language models.
AdvancesinNeuralInformationProcessingSystems,35:24824–24837,2022.
Qingyun Wu, Gagan Bansal, Jieyu Zhang, Yiran Wu, Beibin Li, Erkang Zhu, Li Jiang, Xiaoyun
Zhang,andChiWang.Autogen:Enablingnext-genllmapplicationsviamulti-agentconversation.
arXivpreprintarXiv:2308.08155,2023.
Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, and Yuan Cao.
React: Synergizing reasoning and acting in language models. In International Conference on
LearningRepresentations,2023.
A BENCHMARK GENERATION DETAILS
Each scenario in our benchmark simulates a multi-agent system with 3–5 specialized agents: a
Coordinator(taskdecompositionanddelegation),Specialists(domain-specifictasks),aReviewer
(outputvalidation),andanExecutor(finalactions).Table5liststhedomain-specificconfigurations.
Table5: Domain-specificagentconfigurations
Domain Agents InteractionPattern N
SoftwareDev Planner,Coder,Reviewer,Executor Sequential+ReviewLoop 52
CustomerService Router,Specialist,Resolver,Logger HierarchicalDispatch 51
Research Searcher,Analyzer,Synthesizer,Writer Pipeline+Feedback 51
Planning Scheduler,Optimizer,Validator,Notifier IterativeRefinement 46
Trading Analyst,Strategist,RiskManager,Executor ParallelAnalysis 50
Healthcare Triager,Specialist,Pharmacist,Coordinator ConsultationChain 60
Legal Researcher,Analyst,Drafter,Reviewer DocumentPipeline 60
Education Assessor,Tutor,ContentGenerator,Evaluator AdaptiveLoop 60
Finance DataCollector,Analyst,Advisor,Reporter AggregationPattern 60
DevOps Monitor,Diagnoser,Remediator,Verifier IncidentResponse 60
EachscenariofollowsastandardizedJSONschemaencodingtheexecutionsteps, agentmetadata,
andgroundtruthannotations:
7

PublishedasaworkshoppaperatICLR2026AIWILDWorkshop
| { "scenario_id":      |                                            | "cod_034b23",     |              | "domain":   |            | "coding",      |     |     |
| --------------------- | ------------------------------------------ | ----------------- | ------------ | ----------- | ---------- | -------------- | --- | --- |
| "agents":             | ["Planner","Coder","Reviewer","Executor"], |                   |              |             |            |                |     |     |
| "steps":              | [{"step_id":                               |                   | 1, "agent":  |             | "Planner", |                |     |     |
| "action_type":        |                                            | "plan",           | "input":     |             | "...",     |                |     |     |
| "output":             | "...",                                     |                   | "timestamp": |             | "..."},    | ...],          |     |     |
| "ground_truth":       |                                            | {"error_node_id": |              |             | 8,         |                |     |     |
| "root_cause_node_id": |                                            |                   | 3,           | "bug_type": |            | "logic_error", |     |     |
| "bug_description":    |                                            |                   | "Incorrect   |             | comparison | operator"}}    |     |     |
Bug Injection. We employ a five-step injection process: (1) generate a correct execution trace
fromdomaintemplates;(2)selectabuglocation(earlysteps2–3:60%,middlesteps4–6:30%,late
steps 7+: 10%); (3) assign a bug type per the distribution in Table 6; (4) inject erroneous content
(e.g.,flippedcomparisonoperatorsforlogicerrors,messagetruncationforcommunicationfailures,
swappedvariablenamesfordatacorruption);(5)propagatecascadingeffectstodownstreamsteps.
To prevent methods from exploiting explicit bug markers, we also produce a blind version with
anonymizedIDsandseparatedgroundtruth.
|     |     |                      | Table6: Bugtypedistributioninbenchmark |     |     |                  |     |     |
| --- | --- | -------------------- | -------------------------------------- | --- | --- | ---------------- | --- | --- |
|     |     | BugType              |                                        |     |     | Count Percentage |     |     |
|     |     | LogicError           |                                        |     |     | 165 30.0%        |     |     |
|     |     | CommunicationFailure |                                        |     |     | 110 20.0%        |     |     |
|     |     | DataCorruption       |                                        |     |     | 110 20.0%        |     |     |
|     |     | MissingValidation    |                                        |     |     | 88 16.0%         |     |     |
|     |     | RoleConfusion        |                                        |     |     | 77 14.0%         |     |     |
|     |     | Total                |                                        |     |     | 550 100%         |     |     |
Causal Graph Statistics. The constructed causal graphs have on average 10.8 nodes (σ=2.1)
and 14.2 edges (σ=3.5), with average degree 2.6, diameter 6.3, and mean path length 3.2. Edges
are predominantly sequential (61.3%), followed by communication (26.8%) and data dependency
(11.9%).
| B FEATURE | EXTRACTION |     | AND | WEIGHT |     | LEARNING |     |     |
| --------- | ---------- | --- | --- | ------ | --- | -------- | --- | --- |
Table 7 lists all features used in the ranking algorithm. All features are normalized to [0,1] via
min-maxnormalizationwithineachscenario:
|     |     |     |        | f   | (v)−min   | f (u)   |     |     |
| --- | --- | --- | ------ | --- | --------- | ------- | --- | --- |
|     |     |     | fˆ(v)= |     | i         | u∈V i   |     |     |
|     |     |     | i      |     |           |         |     | (3) |
|     |     |     | max    |     | f (u)−min | f (u)+ϵ |     |     |
|     |     |     |        | u∈V | i         | u∈V i   |     |     |
whereϵ=10−8preventsdivisionbyzero.
WeightLearning. Featuregroupweightsweredeterminedthroughgridsearchonaheld-outval-
idationsetof50scenarios(notincludedinthe550-scenariobenchmark):
50
(cid:88)
|     |     |     | w∗ =argmax |     | ⊮[rank(v(i)|w)=1] |     |     | (4) |
| --- | --- | --- | ---------- | --- | ----------------- | --- | --- | --- |
root
w
i=1
The search space was w ∈ {0.5,0.6,0.7,0.8}, w ∈ {0.1,0.15,0.2,0.25}, w ∈
|     |     |     | p   |     |     | s   | (cid:80) | c   |
| --- | --- | --- | --- | --- | --- | --- | -------- | --- |
{0.03,0.05,0.07,0.1},w ∈{0.02,0.03,0.05},w ∈{0.01,0.02,0.03},subjectto w =1.
|               |     | f        |         |     |     | e   | i i |     |
| ------------- | --- | -------- | ------- | --- | --- | --- | --- | --- |
| C STATISTICAL |     | ANALYSIS | DETAILS |     |     |     |     |     |
Bootstrap Confidence Intervals. We compute 95% CIs using bootstrap resampling with
B=10,000 iterations. For each bootstrap sample r(b), we compute θˆ(b) = mean(r(b)), then take
the2.5thand97.5thpercentilesasintervalbounds.
8

PublishedasaworkshoppaperatICLR2026AIWILDWorkshop
|          | Table7:            | Completefeaturelistwithcomputationmethods |       |          |     |       |
| -------- | ------------------ | ----------------------------------------- | ----- | -------- | --- | ----- |
| Group    | Feature            | Formula                                   |       |          |     | Range |
|          | NormalizedPosition | pos(v)/|V|                                |       |          |     | [0,1] |
|          | DistancetoError    | d(v,v                                     | )/max | d(u,v )  |     | [0,1] |
| Position |                    |                                           | error | u error  |     |       |
|          | DepthRatio         | depth(v)/max                              |       | depth(u) |     | [0,1] |
u
|     | ReversePosition | 1−pos(v)/|V|      |     |               |     | [0,1] |
| --- | --------------- | ----------------- | --- | ------------- | --- | ----- |
|     | Out-degree      | |{u:(v,u)∈E}|/max |     | |{u:(w,u)∈E}| |     | [0,1] |
w
|           | In-degree   | |{u:(u,v)∈E}|/max |        | |{u:(u,w)∈E}| |     | [0,1] |
| --------- | ----------- | ----------------- | ------ | ------------- | --- | ----- |
| Structure |             |                   |        | w             |     |       |
|           | Betweenness | (cid:80)          | σst(v) | (normalized)  |     | [0,1] |
s̸=v̸=t σst
|     | Reachability | |descendants(v)|/|V| |     |     |     | [0,1] |
| --- | ------------ | -------------------- | --- | --- | --- | ----- |
⊮[“error”∈content(v)]
|     | ErrorKeywords |     |     |     |     | {0,1} |
| --- | ------------- | --- | --- | --- | --- | ----- |
⊮[“maybe”∈content(v)]
|     | Uncertainty |     |     |     |     | {0,1} |
| --- | ----------- | --- | --- | --- | --- | ----- |
Content
|     | LengthAnomaly  | |len−µ|/(3σ)(clipped)       |     |     |     | [0,1] |
| --- | -------------- | --------------------------- | --- | --- | --- | ----- |
|     | KeywordDensity | count(keywords)/len         |     |     |     | [0,1] |
|     |                | ⊮[agent(v)̸=agent(prev(v))] |     |     |     | {0,1} |
AgentSwitch
|      |                 |                      | weight(agent(v)) |     |     | [0,1] |
| ---- | --------------- | -------------------- | ---------------- | --- | --- | ----- |
| Flow | RoleCriticality | role                 |                  |     |     |       |
|      |                 | ⊮[type(v)=“message”] |                  |     |     | {0,1} |
Communication
|     |     | conf(v)ifavailable,else0.5 |     |     |     | [0,1] |
| --- | --- | -------------------------- | --- | --- | --- | ----- |
StatedConfidence
| Confidence |     | count(hedge |     | words)/10(clipped) |     | [0,1] |
| ---------- | --- | ----------- | --- | ------------------ | --- | ----- |
HedgingScore
McNemar’sTest. ForcomparingtwomethodsAandB,weconstructa2×2contingencytable
of concordant/discordant predictions. The test statistic is χ2 = (|n −n |−1)2/(n +n ),
|     |     |     |     | 01  | 10  | 01 10 |
| --- | --- | --- | --- | --- | --- | ----- |
followingaχ2distributionwith1degreeoffreedom.
|     |     |     | √   | √   |     |     |
| --- | --- | --- | --- | --- | --- | --- |
Effect Size. We use Cohen’s h = 2arcsin( p ) − 2arcsin( p ), where |h| < 0.2 is small,
|     |     |     | 1   | 2   |     |     |
| --- | --- | --- | --- | --- | --- | --- |
0.2≤|h|<0.5ismedium,and|h|≥0.5isalargeeffect.
Table8providesthecompletestatisticalcomparisons.
Table8: CompletestatisticalcomparisonofAGENTTRACEvs.baselines
|     | Baseline | Hit@1 n | n   | χ2 p-value | Cohen’sh |     |
| --- | -------- | ------- | --- | ---------- | -------- | --- |
01 10
|     | Random    | 9.1% 478 | 6   | 459.2 <10−10 | 2.41 |     |
| --- | --------- | -------- | --- | ------------ | ---- | --- |
|     | FirstNode | 3.6% 503 | 2   | 497.0 <10−10 | 2.72 |     |
<10−10
|     | LastNode | 12.7% 460 | 8   | 436.5 | 2.29 |     |
| --- | -------- | --------- | --- | ----- | ---- | --- |
<10−10
|            | LLMAnalysis  | 68.5% 173 | 28  | 102.5 | 0.77 |     |
| ---------- | ------------ | --------- | --- | ----- | ---- | --- |
| D DETAILED | EXPERIMENTAL | RESULTS   |     |       |      |     |
Table9providesper-domainperformance. Tables10–12stratifyresultsbybugtype, tracelength,
andbugposition.
| E ABLATION | STUDY | DETAILS |     |     |     |     |
| ---------- | ----- | ------- | --- | --- | --- | --- |
Table 13 shows Hit@1 for all feature group combinations. Position features alone reach 87.3%,
while each additional group provides incremental gains. Table 14 shows that the optimal position
weight w = 0.70 balances the strong predictive power of position features with discriminative
p
informationfromothergroups.
9

PublishedasaworkshoppaperatICLR2026AIWILDWorkshop
|     |                        | Table9:              | Detailedperformancemetricsbydomain |               |        |      |     |
| --- | ---------------------- | -------------------- | ---------------------------------- | ------------- | ------ | ---- | --- |
|     | Domain                 |                      | N                                  | Hit@1 Hit@3   | Hit@5  | MRR  |     |
|     | SoftwareDevelopment    |                      | 52                                 | 94.2% 96.2%   | 100.0% | 0.96 |     |
|     | CustomerService        |                      | 51                                 | 92.2% 96.1%   | 100.0% | 0.94 |     |
|     | ResearchAnalysis       |                      | 51                                 | 96.1% 98.0%   | 100.0% | 0.97 |     |
|     | Planning&Scheduling    |                      | 46                                 | 91.3% 95.7%   | 100.0% | 0.94 |     |
|     | FinancialTrading       |                      | 50                                 | 90.0% 98.0%   | 100.0% | 0.94 |     |
|     | HealthcareCoordination |                      | 60                                 | 95.0% 100.0%  | 100.0% | 0.97 |     |
|     | LegalDocumentAnalysis  |                      | 60                                 | 100.0% 100.0% | 100.0% | 1.00 |     |
|     | EducationalTutoring    |                      | 60                                 | 93.3% 100.0%  | 100.0% | 0.96 |     |
|     | FinancialAdvisory      |                      | 60                                 | 96.7% 100.0%  | 100.0% | 0.98 |     |
|     | DevOpsAutomation       |                      | 60                                 | 98.3% 98.3%   | 100.0% | 0.99 |     |
|     | Overall                |                      | 550                                | 94.9% 98.4%   | 99.8%  | 0.97 |     |
|     |                        | Table10:             | Performancebybugtype               |               |        |      |     |
|     |                        | BugType              |                                    | N Hit@1       | MRR    |      |     |
|     |                        | LogicError           |                                    | 165 95.8%     | 0.98   |      |     |
|     |                        | CommunicationFailure |                                    | 110 93.6%     | 0.96   |      |     |
|     |                        | DataCorruption       |                                    | 110 94.5%     | 0.97   |      |     |
|     |                        | MissingValidation    |                                    | 88 94.3%      | 0.96   |      |     |
|     |                        | RoleConfusion        |                                    | 77 94.8%      | 0.97   |      |     |
Table11: Performancebytracelength Table12: Performancebybugpositionintrace
| TraceLength |          | N Hit@1                | MRR                                         | BugPosition |         | N Hit@1 | MRR  |
| ----------- | -------- | ---------------------- | ------------------------------------------- | ----------- | ------- | ------- | ---- |
| 8–9steps    |          | 132 95.5%              | 0.97                                        | Early(2–3)  | 330     | 96.1%   | 0.98 |
| 10–11steps  |          | 198 95.0%              | 0.97                                        | Middle(4–6) | 165     | 93.3%   | 0.96 |
| 12–13steps  |          | 154 94.2%              | 0.96                                        | Late(7+)    | 55      | 92.7%   | 0.95 |
| 14–15steps  |          | 66 93.9%               | 0.96                                        |             |         |         |      |
|             | Table13: | Ablationstudy:         | Performancewithdifferentfeaturecombinations |             |         |         |      |
|             |          | FeatureCombination     |                                             | Hit@1       | ∆vsFull |         |      |
|             |          | Allfeatures(P+S+C+F+E) |                                             | 94.9%       | –       |         |      |
|             |          | Positiononly(P)        |                                             | 87.3%       | -7.6%   |         |      |
|             |          | Structureonly(S)       |                                             | 34.5%       | -60.4%  |         |      |
|             |          | Contentonly(C)         |                                             | 28.7%       | -66.2%  |         |      |
|             |          | Flowonly(F)            |                                             | 15.2%       | -79.7%  |         |      |
|             |          | Confidenceonly(E)      |                                             | 12.1%       | -82.8%  |         |      |
|             |          | P+S                    |                                             | 92.4%       | -2.5%   |         |      |
|             |          | P+C                    |                                             | 90.9%       | -4.0%   |         |      |
|             |          | P+F                    |                                             | 89.5%       | -5.4%   |         |      |
|             |          | P+E                    |                                             | 88.7%       | -6.2%   |         |      |
|             |          | S+C                    |                                             | 45.6%       | -49.3%  |         |      |
|             |          | S+F                    |                                             | 38.2%       | -56.7%  |         |      |
|             |          | P+S+C                  |                                             | 93.8%       | -1.1%   |         |      |
|             |          | P+S+F                  |                                             | 93.3%       | -1.6%   |         |      |
|             |          | P+S+C+F                |                                             | 94.5%       | -0.4%   |         |      |
10

PublishedasaworkshoppaperatICLR2026AIWILDWorkshop
|     |     | Table14: | SensitivityofHit@1topositionweightw |     |     |     |     |
| --- | --- | -------- | ----------------------------------- | --- | --- | --- | --- |
p
|     |     | w   | 0.50 | 0.60 | 0.70 | 0.80 | 0.90 |
| --- | --- | --- | ---- | ---- | ---- | ---- | ---- |
p
|       |          | Hit@1   | 91.3% | 93.5% | 94.9% | 93.8% | 91.1% |
| ----- | -------- | ------- | ----- | ----- | ----- | ----- | ----- |
| F LLM | BASELINE | DETAILS |       |       |       |       |       |
We use GPT-4 (gpt-4-0613) with temperature 0.0, max tokens 1024, top-p 1.0, and zero fre-
quency/presencepenalties. Thepromptinstructsthemodeltoanalyzethefullexecutiontrace,iden-
tifycausalrelationships,andoutputonlythestepnumberoftherootcause:
| You are      | an expert | debugger    |       | analyzing   | a multi-agent |              | system       |
| ------------ | --------- | ----------- | ----- | ----------- | ------------- | ------------ | ------------ |
| execution    | trace.    | The system  |       | encountered | an            | error.       |              |
| Your task    | is        | to identify | the   | ROOT        | CAUSE -       | the earliest |              |
| step where   | something | went        | wrong | that        | led           | to the       | final error. |
| ## Execution |           | Trace:      |       |             |               |              |              |
{trace_content}
| ## Error   | Description: |         |               |     |                     |     |     |
| ---------- | ------------ | ------- | ------------- | --- | ------------------- | --- | --- |
| The system | failed       | at step | {error_step}: |     | {error_description} |     |     |
## Instructions:
| 1. Analyze   | the          | execution     | trace      | carefully         |       |       |     |
| ------------ | ------------ | ------------- | ---------- | ----------------- | ----- | ----- | --- |
| 2. Identify  | causal       | relationships |            | between           |       | steps |     |
| 3. Find      | the EARLIEST | step          | that       | caused            | the   | error |     |
| 4. Consider: |              | logic errors, |            | miscommunication, |       |       |     |
| data         | issues,      | missing       | validation |                   |       |       |     |
| ## Output    | Format:      |               |            |                   |       |       |     |
| Respond      | with         | ONLY the      | step       | number,           | e.g., | "3"   |     |
| Root cause   | step:        |               |            |                   |       |       |     |
Table 15 categorizes the 173 errors made by the LLM baseline. The most common failure mode
(47.4%)isselectingtheerrormanifestationnoderatherthantracingbacktotheactualrootcause.
|           |                                     | Table15:    |     | ErroranalysisforLLMbaseline |     |       |            |
| --------- | ----------------------------------- | ----------- | --- | --------------------------- | --- | ----- | ---------- |
|           | ErrorType                           |             |     |                             |     | Count | Percentage |
|           | Selectederrornodeinsteadofrootcause |             |     |                             |     | 82    | 47.4%      |
|           | Off-by-one(adjacenttocorrectnode)   |             |     |                             |     | 45    | 26.0%      |
|           | Selectedintermediatepropagationstep |             |     |                             |     | 31    | 17.9%      |
|           | Completelyincorrect                 |             |     |                             |     | 15    | 8.7%       |
|           | TotalErrors                         |             |     |                             |     | 173   | 100%       |
| G RUNTIME |                                     | PERFORMANCE |     | DETAILS                     |     |       |            |
Tables16and17breakdownruntimebycomponentandshowscalingwithtracelength. Runtime
scalesapproximatelylinearly: T ≈12.5n+5ms,wherenisthenumberofsteps. Allexperiments
wereconductedonanAMDRyzen95950X(16-core,3.4GHz),128GBDDR4RAM,NVMeSSD,
Ubuntu24.04LTS,Python3.13.
| H EXAMPLE |                      | SCENARIOS |                |           |                              |     |     |
| --------- | -------------------- | --------- | -------------- | --------- | ---------------------------- | --- | --- |
| Example1: | SoftwareDevelopment. |           |                | Task:     | Implementaveragecalculation. |     |     |
| Step 1    | [Planner]:           | Analyze   | requirements   |           |                              |     |     |
| -> "Sum   | all                  | numbers,  | count          | elements, | divide"                      |     |     |
| Step 2    | [Coder]:             | Write     | implementation |           |                              |     |     |
| -> "def   | average(nums):       |           | ..."           |           |                              |     |     |
11

PublishedasaworkshoppaperatICLR2026AIWILDWorkshop
Table16: Component-wiseruntimebreakdown Table17: Runtimescalingwithtracelength
| Component         |                  |       | Mean(ms)  |       | Std(ms)   |     |        | Steps Mean(ms) | P95(ms) |
| ----------------- | ---------------- | ----- | --------- | ----- | --------- | --- | ------ | -------------- | ------- |
| GraphConstruction |                  |       | 15.2      |       | 3.1       |     |        | 5 68           | 89      |
| BackwardTracing   |                  |       | 8.4       |       | 2.8       |     |        | 10 115         | 148     |
| FeatureExtraction |                  |       | 62.3      |       | 12.4      |     |        | 15 162         | 201     |
| NodeRanking       |                  |       | 28.6      |       | 5.2       |     |        | 20 218         | 267     |
|                   |                  |       |           |       |           |     |        | 25 283         | 342     |
| Total             |                  |       | 114.5     |       | 18.3      |     |        |                |         |
| Step              | 3 [Coder]:       |       | Add edge  | case  | handling  |     | [BUG]  |                |         |
|                   | -> "if nums      | =     | []: #     | BUG:  | = instead |     | of ==" |                |         |
| Step              | 4 [Reviewer]:    |       | Review    | code  |           |     |        |                |         |
|                   | -> "Code         | looks | correct." |       |           |     |        |                |         |
| Step              | 5 [Executor]:    |       | Run       | tests | [ERROR]   |     |        |                |         |
|                   | -> "SyntaxError: |       | invalid   |       | syntax    | at  | line   | 2"             |         |
Root cause: Step 3 (logic error). AGENTTRACE correctly identifies Step 3; LLM selects Step 5
(errornode).
| Example2: | CustomerService. |     |               | Task:        | Handledelayedshipmentcomplaint. |         |           |          |     |
| --------- | ---------------- | --- | ------------- | ------------ | ------------------------------- | ------- | --------- | -------- | --- |
| Step      | 1 [Router]:      |     | Classify      | request      |                                 | ->      | "Shipping | Issue"   |     |
| Step      | 2 [Specialist]:  |     | Look          | up           | order                           | ->      | "In       | Transit" |     |
| Step      | 3 [Specialist]:  |     | Misread       |              | delivery                        |         | date      | [BUG]    |     |
|           | -> "Expected:    |     | March         | 15 (actually |                                 | March   | 5)"       |          |     |
| Step      | 4 [Resolver]:    |     | Compose       |              | response                        |         |           |          |     |
|           | -> "On track     | for | March         | 15..."       |                                 |         |           |          |     |
| Step      | 5 [Logger]:      |     | Send          | response     |                                 | [ERROR] |           |          |     |
|           | -> "Customer:    |     | ’Was supposed |              | to                              | arrive  | March     | 5!’"     |     |
Rootcause: Step3(datacorruption). BothAGENTTRACEandLLMcorrectlyidentifyStep3.
Example3: ResearchAnalysis. Task: Analyzetransformerarchitecturepublications.
| Step | 1 [Searcher]:    |     | Query         | databases |          | ->        | "150      | papers" |     |
| ---- | ---------------- | --- | ------------- | --------- | -------- | --------- | --------- | ------- | --- |
| Step | 2 [Searcher]:    |     | Filter        | ->        | "25      | relevant  |           | papers" |     |
| Step | 3 [Analyzer]:    |     | Extract       |           | findings |           | [BUG]     |         |     |
|      | -> "Attention    |     | being         | replaced  | by       | MLPs"     |           |         |     |
|      | (actually:       |     | attention     | being     |          | enhanced) |           |         |     |
| Step | 4 [Synthesizer]: |     |               | "Field    | moving   | away      | from      |         |     |
|      | attention-based  |     | models..."    |           |          |           |           |         |     |
| Step | 5 [Writer]:      |     | "Transformers |           | becoming |           | obsolete" |         |     |
| Step | 6 [Writer]:      |     | Finalize      | report    |          | [ERROR]   |           |         |     |
|      | -> "Contradicts  |     | recent        | SOTA      | results" |           |           |         |     |
Root cause: Step 3 (communication failure). AGENTTRACE correctly identifies Step 3; LLM se-
lectsStep4(propagationstep).
| I   | FAILURE | CASE | ANALYSIS |     |     |     |     |     |     |
| --- | ------- | ---- | -------- | --- | --- | --- | --- | --- | --- |
Among the 28 scenarios (5.1%) where AGENTTRACE failed to rank the correct root cause first,
Table18categorizesthefailuretypes.
Thedominantfailuremodeismultipleplausiblerootcauses:inscenariores 3867e9,bothStep2
(incorrect search query) and Step 3 (overly strict filter) contributed to the error; AGENTTRACE
selected Step 2 while ground truth was Step 3. The second mode is bugs at unusual positions:
scenarios with late-stage bugs (step 7+) have feature distributions that differ from the majority,
causing AGENTTRACE to over-prioritize earlier steps. Potential improvements include position-
adaptiveweights,semanticsimilaritybetweenerrordescriptionsandnodecontent,andmulti-root-
causedetection.
12

PublishedasaworkshoppaperatICLR2026AIWILDWorkshop
Table18: FailurecaseanalysisforAGENTTRACE
| FailureType                 | Count | Percentage |
| --------------------------- | ----- | ---------- |
| Multipleplausiblerootcauses |       | 12 42.9%   |
| Bugatunusualposition        |       | 8 28.6%    |
| Atypicalcausalstructure     |       | 5 17.9%    |
| Featureextractionissues     |       | 3 10.7%    |
| Total                       |       | 28 100%    |
J REPRODUCIBILITY
All code, data, and evaluation scripts are available at https://github.com/zwang000/
AgentTrace,includingbenchmarkgenerationscripts,550scenarioJSONfileswithgroundtruth,
allbaselineimplementations,andstatisticalanalysisscripts.Table19listsallhyperparameters.Ran-
domseeds: benchmarkgeneration(42),bootstrapresampling(12345),train/validationsplit(2024).
Table19: Completehyperparametersettings
| Parameter               |     | Value |
| ----------------------- | --- | ----- |
| Maxbackwardtracingdepth |     | 10    |
| Positionweight(w        | )   | 0.70  |
p
| Structureweight(w | )   | 0.20 |
| ----------------- | --- | ---- |
s
| Contentweight(w | )   | 0.05 |
| --------------- | --- | ---- |
c
| Flowweight(w | )   | 0.03 |
| ------------ | --- | ---- |
f
| Confidenceweight(w  | e ) | 0.02   |
| ------------------- | --- | ------ |
| Normalizationϵ      |     | 10−8   |
| Bootstrapiterations |     | 10,000 |
| Confidencelevel     |     | 95%    |
13