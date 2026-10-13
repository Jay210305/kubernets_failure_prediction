PDF Download
3725783.3764387.pdf
31 March 2026
Total Citations: 0
. Total Downloads: 164
.
Latest updates: hps://dl.acm.org/doi/10.1145/3725783.3764387 .
.
Published: 11 October 2025
.
. .
RESEARCH-ARTICLE .
Citation in BibTeX format
Generating Representative Macrobenchmark Microservice Systems
.
.
from Distributed Traces with Palee APSys '25: 16th ACM SIGOPS Asia-
Pacific Workshop on Systems
October 12 - 13, 2025
VAASTAV ANAND, Max Planck Institute for Soware Systems, Saarbrucken, Saarland, Seoul, Republic of Korea
.
Germany .
Conference Sponsors:
. SIGOPS
MATHEUS STOLET, Max Planck Institute for Soware Systems, Saarbrucken, Saarland,
Germany
.
JONATHAN MACE, Microso Research, Redmond, WA, United States
.
ANTOINE KAUFMANN, Max Planck Institute for Soware Systems, Saarbrucken, Saarland,
Germany
.
.
.
Open Access Support provided by:
.
Max Planck Institute for Soware Systems
.
Microso Research
.
APSys '25: Proceedings of the 16th ACM SIGOPS Asia-Pacific Workshop on Systems (October 2025)
hps://doi.org/10.1145/3725783.3764387
ISBN: 9798400715723
.

|              | Generating |     |     | Representative |     |      |             | Macrobenchmark |     |     |        |      |
| ------------ | ---------- | --- | --- | -------------- | --- | ---- | ----------- | -------------- | --- | --- | ------ | ---- |
| Microservice |            |     |     | Systems        |     | from | Distributed |                |     |     | Traces | with |
Palette
|     |     | Vaastav |     | Anand |     |     |     |     | Matheus |     | Stolet |     |
| --- | --- | ------- | --- | ----- | --- | --- | --- | --- | ------- | --- | ------ | --- |
MaxPlanckInstituteforSoftwareSystems MaxPlanckInstituteforSoftwareSystems
|     |     | Saarbrücken,Germany |             |      |     |     |     |                                      | Saarbrücken,Germany |          |     |     |
| --- | --- | ------------------- | ----------- | ---- | --- | --- | --- | ------------------------------------ | ------------------- | -------- | --- | --- |
|     |     | Jonathan            |             | Mace |     |     |     |                                      | Antoine             | Kaufmann |     |     |
|     |     | MicrosoftResearch   |             |      |     |     |     | MaxPlanckInstituteforSoftwareSystems |                     |          |     |     |
|     |     |                     | Seattle,USA |      |     |     |     |                                      | Saarbrücken,Germany |          |     |     |
Abstract
ACMReferenceFormat:
VaastavAnand,MatheusStolet,JonathanMace,andAntoineKauf-
Microservicesarethedominantdesignfordevelopingcloud
mann.2025.GeneratingRepresentativeMacrobenchmarkMicroser-
systemstoday.Advancementsformicroserviceneedtobe
viceSystemsfromDistributedTraceswithPalette.In16thACM
evaluatedinrepresentativesystems,e.g.withmatchingscale,
SIGOPSAsia-PacificWorkshoponSystems(APSys’25),October12–13,
topology,andexecutionpatterns.Unfortunatelyinpractice,
2025,Seoul,RepublicofKorea.ACM,NewYork,NY,USA,8pages.
| researchers | and | practitioners | alike | often | do not | have ac- |     |     |     |     |     |     |
| ----------- | --- | ------------- | ----- | ----- | ------ | -------- | --- | --- | --- | --- | --- | --- |
https://doi.org/10.1145/3725783.3764387
cesstorepresentativesystems.Thustheyhavetoresortto
sub-optimalnon-representativealternatives,e.g.smalland 1 Introduction
oversimplifiedsyntheticbenchmarksystemsorsimulated
Moderncloudsystemsaredevelopedasmicroservicesys-
systemmodelsinstead.
|           |           |          |                |            |             |         | tems. | They        | have been | adopted | by many   | large companies  |
| --------- | --------- | -------- | -------------- | ---------- | ----------- | ------- | ----- | ----------- | --------- | ------- | --------- | ---------------- |
| We        | propose   | to solve | this issue     | using      | distributed | trace   |       |             |           |         |           |                  |
|           |           |          |                |            |             |         | such  | as Facebook | [16],     | Netflix | [6], Uber | [14], among oth- |
| datasets, | available | from     | large internet | companies, |             | to gen- |       |             |           |         |           |                  |
ers[5,15]sincetheenableindividualservicestobedevel-
eraterepresentativemicroservicesystems.Todoso,intro-
oped,deployed,andscaledindependently.
| duce | a novel abstraction |     | of a system | topology | which | uses |     |     |     |     |     |     |
| ---- | ------------------- | --- | ----------- | -------- | ----- | ---- | --- | --- | --- | --- | --- | --- |
Validatingandtestingnewadvancementsformicroser-
GraphicalCausalModels(GCMs)tomodeltheunderlying
vicesoftenrequiresdeveloperstoexperimentwithinterven-
systembyincorporatingbranchingprobabilities,execution
tions—thatischangeaspectsofthesystemwithnewdesign
orderofoutgoingcallstoeverydependency,andexecution
decisions,architecturalchoices,algorithms,backendcompo-
times.WethenincorporatethistopologyinPalette,asys-
nents,andotherstrategies—inordertoestimateandassess
temthatgeneratesrepresentativeflexiblemacrobenchmarks
theirimpactonthesystem.
microservicesystemsfromdistributedtraces. Ideally,developersandresearcherswouldexecutethese
interventionexperimentsonproductionsystemstomake
CCSConcepts claimsaboutthetechnique’sscalabilityandgeneralizabil-
• Networks → Cloud computing; • Software and its ity.However,accesstoproductionsystemsislimitedtoa
engineering→Cloudcomputing. select few. Even if one could procure access, the scope of
experimentationislimitedtominimizedisruptions.
|     |     |     |     |     |     |     | Despite |     | the limited | access | to production | systems, dis- |
| --- | --- | --- | --- | --- | --- | --- | ------- | --- | ----------- | ------ | ------------- | ------------- |
Keywords
tributedtracesareoftenreadilyavailableandresearchers
Microservices,DistributedTracing,MicroserviceBenchmarks
canusethemtogleaninsightintothesesystems.Distributed
tracescapturerichstructuralandtemporalinformationabout
theexecutionofthesystem,suchaslatency,executionpat-
terns,branchprobabilities,andcallprobabilities.
|     |     |     |     |     |     |     | We  | posit | that distributed |     | traces can support | general pur- |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | ---------------- | --- | ------------------ | ------------ |
ThisworkislicensedunderaCreativeCommonsAttribution4.0Interna-
poseinterventionexperimentsgiventherichvolumeofsystem
tionalLicense.
behaviortheycapture.
APSys’25,Seoul,RepublicofKorea
|     |     |     |     |     |     |     | However, |     | we believe | that | currently there | are three key |
| --- | --- | --- | --- | --- | --- | --- | -------- | --- | ---------- | ---- | --------------- | ------------- |
©2025Copyrightheldbytheowner/author(s).
ACMISBN979-8-4007-1572-3/2025/10 challengesthatpreventdistributedtracesfrombeingused
https://doi.org/10.1145/3725783.3764387 forinterventionexperiments.First,whiledistributedtraces
147

APSys’25,October12–13,2025,Seoul,RepublicofKorea VaastavAnand,MatheusStolet,JonathanMace,andAntoineKaufmann
capture a variety of metrics, they are observations of the Use-case Meaningfulproperties
intrinsicbehaviorofthesystem.Thesystembehaviorthat
𝜇Service Performance[33, Varyinggraphsizes,executionpaths,
causedtheseobservationsisnotexplicitlycapturedindis-
34,37] topology
tributedtraces.Thus,weneedamechanismthatcanusethe
NetworkStacks[12,19,38] Requestsizes,serviceexecutiontime,
distributedtracestoderiveamodeloftheintrinsicbehav-
calldepth,andcallwidth
iorofthesystem.Second,currentlythereisnomechanism Congestion Varyingtopology,timeoutvalues
toconvertinterventionexperimentsintotargetedmodifica- Control[21,43]
tionsofthesystemwithoutmodifyingtherestofthesystem Res.Management[27,32] Varying execution paths, large ser-
behavior.Thefundamentaltenetofaninterventionexperi- vicegraphs
mentrequiresthatalltheotherfactorsinthesystemmust TracingFramework[11,22, Varyingexecutionpaths,largenum-
beheldconstanttoisolatetheimpactoftheintervention. 35,39] berofservices
RPCFramework[18,20] Varyingrequestsizes
Third, converting distributed traces to a runnable system
forsupportinggeneralpurposeinterventionexperimentsis Table 1: Research use-cases and the ideal properties
non-trivialasdifferentinterventionexperimentsmightwish fromabenchmarksystem.
topreservedifferentcharacteristicsofthesystems.
Toovercomethesechallenges,weproposePalette,asys-
temdesignedfornativelysupportinginterventionexperi-
Differentuse-cases,asevidencedinTable1,willcareabout
mentsusingdistributedtraces.Paletteprovidesanewab-
differentpropertieswhenintroducinginterventionstothe
stractioncalledsystemtopologythatmodelssystembehavior
system.Nosinglepointsolutionsystemderivedfromtraces
capturedbygeneratingagraphicalcausalmodel(GCM).To
cansupportallpossibleinterventionscorrectly.
supporttargetedmodificationsforinterventions,Palettepro-
videsasetofprimitiveoperationsthatallowdevelopersto
2.2 TheRoleofDistributedTracing
makelocalizedchangesinthesystemtopologyforagiven
intervention.Finally,Paletteprovidesagenerationmecha- Distributed tracing is a critical monitoring component in
nismforconvertingasystemtopologytoarunnablesystem. moderncloudsystems.Itprovidestroubleshootingsupport
Our solution leverages the GCM at runtime to model the fordevelopersandoperatorsduringincidentroot-causeanal-
causaldependenciesfromtheoriginalsystemandusesitto ysisandpost-mortems.Distributedtracingsupportsthisby
morefaithfullysamplemetricsforexecutionbehavior,such generatinganexecutiontraceofeachrequestacrossallcom-
astheamountofworktobedoneinaserviceorthepayload ponentsofthesystem.Additionally,anonymizedtraceshave
sizetobeusedbetweentwoservicesgiventhecurrentstate beenoneofthefewwaysforlarge-scalesystemoperators
ofthesystem. tosharemeaningfuldetailsabouttheirsystemsandwork-
loads[23,24].Wethusbelievethatthedata-richnatureof
distributedtracedatasetsrepresentsanopportunityforad-
2 BackgroundandMotivation
dressingthestructuraldiversityissueinexistingopen-source
2.1 ResearchUseCases microservicesystemsforresearchuse-cases.
Microservices have a large design space owing to its het- Trace Details. A distributed trace contains the partially-
ereogeneous nature. Consequently, the set of all possible ordered list of all APIs (referred to as spans) executed by
interventionsaresearchercanperformisalsolarge.Forin- thesystemtoservicetherequest.Foreachspan,thetrac-
stance, researchers building a new network stack may be ingframeworkcapturesthetotalamountofexecutiontime
interested in confirming that their design maintains low andthespecificservice(orcomponent)atwhichthespan
taillatencyunderloadsothatrequestsmeettheirSLOs.To wasexecuted.Thetracingframeworksencodescaller-callee
testtheirhypothesistheyneedasystemthatmatchesthe relationshipsbetweenAPIsasparent-childrelationships.
characteristicsofarealsystemsuchasrequestsize,service DistributedTracingWorkloadGeneration.Distributed
executiontimes,andcallgraphdepthandwidth.Request tracingcanalsobeusedtogeneraterealisticworkloadsto
sizemattersbecausesystemsoptimizedifferentlybasedon testsolutionsatlargescalebecauseofitsrichcollectionof
its average. Service execution is critical because services executiondata[9,28].
withlongexecutiontimesmayseenegligiblebenefitsfroma
2.3 GraphicalCausalModels(GCMs)
fasternetworkstack.Similarly,benefitsmaybeamplifiedin
deepcallgraphsoroffsetbyslowservicesinthecriticalpath. Graphical Causal Models [10] are directed acyclic graphs
Therefore,generatedsystemsshouldbeabletomodifyand which encode causal relationships between the different
preservethesepropertiessothatinterventionscanbeadded nodesinthegraph.Eachnoderepresentsavariable,i.e.some
whilestillmaintainingrealisticperformancecharacteristics. observabledata,andtheedgesrepresentcausality.Adirected
148

APSys’25,October12–13,2025,Seoul,RepublicofKorea
1.0
0.8
0.6
0.4
0.2
0.0
0 5 10 15 20 25
Latency (ms)
FDC
Original
Regenerated
(a)ServiceA
1.0
0.8
0.6
0.4
0.2
0.0
0 5 10 15 20 25
Latency (ms)
FDC
eachAPIaswellastheexecutionprobabilityforeachdown-
streamdependencycall.However,thisapproachfailswhena
downstreamAPIhasmultiplecallerseachofwhichisprovid-
ingadifferentamountofwork.Let’sconsiderthescenario
withthreeservices,wherebothServiceAandServiceCmake
callstoadownstreamServiceBtoperformsomeamount
ofwork.ServiceCperformsanorderofmagnitudehigher
workthanServiceAwhichresultsinServiceClatencyto
beanorderofmagnitudehigherthanServiceA.However,
whenwecollectstatisticsaboutthedownstreamServiceB,
thisinformationislostasweonlyget1statisticwhichisthe
mean.Ifweweretore-generatethesystemusingjustthis
simple statistic, then we would find that Service B would
almosttakethesameamountoftimeforcallsoriginating
fromServiceCbuttakealmostanorderofmagnitudehigher
Original
amountoftimeforcallsoriginatingfromServiceA.Figure1
Regenerated
showsexactlythisscenariowherewefindthatthelatency
distribution of Service A is shifted by almost an order of
magnitude.Thereasonwhythisapproachfailsisbecause
thelatencyofserviceBdoesnotconditionthesamplingof
(b)ServiceC
thelatencyontheupstreamcaller.
Open-sourcemicroservicebenchmarks.Theseopen-source
Figure1:LatencyCDFmismatchwithsimplestatistical
systemsaresinglepointsolutionsinthelargedesignspace
approach
of microservice systems. While these systems [13, 26, 44]
areusefultargetsforvalidationandgoodtargetsforsome
use-cases,thesystemsdonotcoverarepresentativeenough
edgebetweentwonodessignifiesthatavariableinfluences
designspaceforresearcherstoexplore[30].Thus,theseare
thevalueoftheothervariable.
onlyusefulforthespecificusecaseswhichdonotrequire
These models are useful for understanding the causal
characteristicsfromthedesignspacethesesystemsdonot
effects of one variable on another [3] and have been ex-
represent.Forexample,performinganinterventionexperi-
tensively used in root cause analysis of microservice sys-
menttotesttheefficacyofanewdistributedtracingsystem
tems[4,8,17,36,42].GCMshelppreservethepropertiesof
requiresthesystemtopreservethepropertyofalargenum-
theoriginalsystemancangeneratenewsamples(i.e.traces)
berofservicesandlargefan-insandfan-outsthatarecom-
basedonthecausalstructureofthesystem.AsGCMsinter-
monlyseeninproductionsystems[16,23,24,29,41].How-
nallyuseinferredcausaleffectsfromtheobserveddata,any
ever,thisisnotpossiblewithexistingopensourcesystems
newsamplegeneratedbytheGCMwillberepresentativeof
aseventhelargestavailableopen-sourcemicroservicesys-
theoriginaldata.Duetothisrepresentativenessretention
tem,TrainTicket[44],hasonly45servicesexcludingcaches
propertyGCMshavebeenusedinconjunctionwithtracesfor
and databases. Researchers may instead opt for synthetic
performinginterventionexperimentsinsimulation[1,40]. benchmarkgeneratorssuchas𝜇Bench[7]orMicrosim[31]
forsomeoftheirexperimentsbutthesesyntheticgenera-
2.4 ExistingApproaches
torsoftenlacktherepresentativenessandflexibilitytotruly
TraceReplay.Asystemthatreplaysexacttracesgenerated support all possible intervention experiments that the re-
fromtheoriginalsystemguaranteesthatsystembehavior searchersmightwishtoperform.
will be representative. However, the issue arises when a
researcherperformsaninterventionandchangessomecom-
3 PaletteDesign
ponentoraspectofthesystem.Inthatsituation,thesystem
willnolongerhavetheabilitytoreplayapriorexecutionbe- Figure2showsthedesignpipelineofPalette.Palettepro-
causethatexecutionisnotpresentintheavailabletraces.As cessestracedatasetstogenerateasystemtopologythaten-
aresult,thesystemcoulddivergefromtheoriginalsystem codesstructuralrelationships,executionpatterns,andperfor-
beyondthetrueimpactoftheintervention. mancecharacteristicsoftheobservedsystem.Thistopology
SimpleStatisticalModels.Anotherpossiblestrawmanso- isconvertedintospecificationsthatencodesmechanismsto
lutionistocalculateanaggregatestatistic(e.g.mean)for ensurethepreservationofthelearnedcharacteristics.Palette
149

APSys’25,October12–13,2025,Seoul,RepublicofKorea VaastavAnand,MatheusStolet,JonathanMace,andAntoineKaufmann
|     |              |     |           | Trace  |          | Topology  |     |     | Spec      |     |        |            |     |
| --- | ------------ | --- | --------- | ------ | -------- | --------- | --- | --- | --------- | --- | ------ | ---------- | --- |
|     |              |     | Processor |        |          | Modifier  |     |     | Generator |     |        |            |     |
|     |              |     |           |        |          |           |     |     |           |     | System | Generated  |     |
|     | Distributed  |     |           |        | Topology |           |     |     |           |     |        |            |     |
Generator
|     | Traces |     |     |     |     |     |     |     |     |     |     | System |     |
| --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- |
Interventions
Figure2:PalettePipeline
0.9
| Behavior |     |     | CausalEquation |     |     |     |     |     |     |     |     |     |     |
| -------- | --- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
𝐶
| Probability(𝑐) |     |           | 𝑝 𝑎 ∼𝐵𝑒𝑟𝑛𝑜𝑢𝑙𝑙𝑖(𝑐) |           |       |        |     |     |     |     |     |     |     |
| -------------- | --- | --------- | ----------------- | --------- | ----- | ------ | --- | --- | --- | --- | --- | --- | --- |
| Sequential(𝑎   |     | ,...,𝑎 𝑛) | 𝑝 ∗𝜆              | ∗𝑎 +···+𝑝 | ∗𝜆    | ∗𝑎 𝑛+𝐶 |     |     |     |     |     |     |     |
|                |     | 1         | 𝑎 1               | 𝑎 1 1     | 𝑎𝑛 𝑎𝑛 |        |     |     |     | 0.5 | 0.1 |     |     |
( 𝑎 , . . .,𝑎 𝑛) 𝑚 𝑎 𝑥 ( 𝑝 ∗ 𝜆 ∗𝑎 , . . . , 𝑝 ∗ 𝜆 ∗ 𝑎 𝑛) + 𝐶 𝐷||𝐸 𝑓𝑖𝑛𝑖𝑠ℎ
| C o                                           | n c u r r e n | t 1       |        | 𝑎 𝑎                | 1 𝑎 𝑛 𝑎 𝑛         |         |     | 𝑠𝑡𝑎𝑟𝑡 |     |     |     |     |     |
| --------------------------------------------- | ------------- | --------- | ------ | ------------------ | ----------------- | ------- | --- | ----- | --- | --- | --- | --- | --- |
|                                               | 𝑎 ,           | . . . , 𝑎 | 𝑝      | 𝜆 1 𝑎 1            | 𝑝 𝜆               | 𝑎 𝐶     |     |       |     | 0.1 |     | 1.0 |     |
| C h                                           | oi c e ( 1    | 𝑛 )       | 𝑎 ∗    | 𝑎 ∗ 1 +            | · · · + 𝑎 𝑛 ∗ 𝑎 𝑛 | ∗ 𝑛 + , |     |       |     |     |     |     |     |
|                                               |               |           | 1      | 1                  |                   |         |     |       | 0.4 |     | 0.2 |     |     |
|                                               |               |           | su c h | t h a t , 𝑝 𝑎      | + · · · + 𝑝 𝑎 = 1 |         |     |       |     | 𝐵   |     |     |     |
|                                               |               |           |        | 1                  | 𝑛                 |         |     |       |     |     |     |     |     |
| Table2:CausalEquationformodelinglatenciesused |               |           |        |                    |                   |         |     |       |     |     |     | 0.8 |     |
| foragivenGCMnodewhere𝑎                        |               |           |        | isthelatencyforAPI |                   |         |     |       |     |     |     |     |     |
𝑖
| 𝑖,𝜆 |     |     |     |     | for𝑎 | 𝑖,𝐶 |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
𝑎𝑖 is the coefficient in the GCM model is Figure3:ExamplePFAgeneratedbyPalette
| the           | intercept | extracted                      | from | fitting | the GCM | linear |     |     |     |     |     |     |     |
| ------------- | --------- | ------------------------------ | ---- | ------- | ------- | ------ | --- | --- | --- | --- | --- | --- | --- |
| equation,and𝑝 |           | isavalueof0or1signallingifAPI𝑖 |      |         |         |        |     |     |     |     |     |     |     |
𝑎𝑖
and𝐸
| wascalled. |     |     |     |     |     |     |                                      | isthesetofalledgesbetweenallAPIs.Eachpartition |                                         |     |     |            |     |
| ---------- | --- | --- | --- | --- | --- | --- | ------------------------------------ | ---------------------------------------------- | --------------------------------------- | --- | --- | ---------- | --- |
|            |     |     |     |     |     |     | inthegraph,𝑝                         |                                                | ∈𝑃,encodesasingleserviceuniquelyidenti- |     |     |            |     |
|            |     |     |     |     |     |     | fiedbyitsname.Eachvertexinthegraph,𝑣 |                                                |                                         |     |     | ∈𝑉,encodes |     |
asingleuniqueAPIinthesystemanduniquelybelongsto
thenusesBlueprint[2]togenerateafullimplementationof a single partition. Each vertex is uniquely identified by a
thesystemfromthesespecifications.
combinationofitsnameandthepartitionitbelongsto.Each
ThegeneratedsystemisaugmentedwithaGCM-based edgeinthegraph,𝑒 ∈𝐸,encodesacaller-calleerelationship
runtimethatsteersexecutiontoreflecttheoperationofthe
|     |     |     |     |     |     |     | between |     | any two | APIs in the | system. | Edges between | ver- |
| --- | --- | --- | --- | --- | --- | --- | ------- | --- | ------- | ----------- | ------- | ------------- | ---- |
originalsystem.Ourproposedsystemsupportsinterventions
ticesinthesamepartitionencodelocalfunctioncallswhile
byallowinguserstomodifytheseabstractionstotailorthe edgesbetweenverticesindifferentpartitionsencoderemote
| generated |     | system to | their experimental |     | needs, while | still |     |     |     |     |     |     |     |
| --------- | --- | --------- | ------------------ | --- | ------------ | ----- | --- | --- | --- | --- | --- | --- | --- |
procedurecalls.
beingrepresentativeoftheoriginalsystem.
PFAEncodesExecutionBehavior.PaletteusesaPFAto
modelthevariousexecutionbehaviorsexhibitedbyanAPI
3.1 SystemTopology
wheninvokingitsdependencies.Forinstance,itcanbeused
Palettegeneratesasystemtopologyfromthestatisticscol- todistinguishbetweensequentialandconcurrentcallsfrom
lected during trace processing; the topology encodes the oneAPItoanother;thisinformationisnotcapturedbythe
calculatedstatisticalinformationintoanabstractrepresenta- directed graph and the GCM. Figure 3 shows an example
tionwhichcanbeexposedtotheuserforfurthermodifica- PFAgeneratedbyPalette.ThePFAforeachAPIconsistsof
tion.Itmodelsthestructuralrelationshipswithinthesystem differentstateswhichtheexecutioncanbein.EveryPFAhas
throughadirectedgraphthatencodesthecaller-calleein- astartstatethatrepresentsthestartoftheAPIexecutionand
teractionsbetweenservicesandAPIs,whileaProbabilistic afinishstatewhichrepresentstheendoftheAPIexecution.
FiniteAutomaton(PFA)capturesthediverseexecutionpath- Additionally,thePFAcontainsotherstates,eachofwhich
ways of each API. The topology models the performance representsalocalstepintheAPIexecution.Eachstatein
propertiesofthesystembyusingagraphicalcausalmodel thePFAcanmakeoneormoreconcurrentoutgoingcalls
(GCM).Bothstructuralandperformancepropertiesofthe (with some probability) to dependencies. For example, in
originalsystemmustbepreservedtogenerateandexecutea Figure3,nodesBandConlymakeonecallwhereasnode
newrepresentativesystem. D∥E make two concurrent outgoing calls. Once the calls
DirectedGraphRepresentsTopology.Thesystemtopol- end, the state can then transition into another state. The
| ogyisadirectedgraph,𝐺 |     |     | (𝑃,𝑉,𝐸),where𝑃isthesetofall |     |     |     |            |     |       |            |            |           |         |
| --------------------- | --- | --- | --------------------------- | --- | --- | --- | ---------- | --- | ----- | ---------- | ---------- | --------- | ------- |
|                       |     |     | =                           |     |     |     | transition |     | edges | encode the | sequential | nature of | the API |
servicesinthesystem,𝑉 isthesetofallAPIsinthesystem, execution.Astatemaytransitionintooneofmanypossible
150

APSys’25,October12–13,2025,Seoul,RepublicofKorea
finishes,PalettecoarsensthePFAbymergingsimilarstates.
B_called B_latency
PalettethenusesthebuiltPFAtogenerateacausalgraph
A_called A_latency foreachAPIandgeneratesacausalequationforeachnode
C_called C_latency inthecausalgraph.Thecausalequationisentirelydepen-
dentonthespecificperformancepropertybeingmodeledby
Figure4:Examplelatencycausalgraph theGCM.Table2showshowtheequationwillbebuiltfor
latencynodes,theoperationsmightbeentirelydifferentfor
adifferentpropertysuchaspayloadsizes.Palettethenfitsa
stateswithadifferentprobability.Forexample,inFigure3, linearregressionforthelatenciesusingtheobservedtrace
thestartstatetransitionsintostateBwithprobability0.4, datatofindthecoefficients(thevarious𝜆 𝑎)usedtoestimate
stateCwithprobability0.5,andstateD∥Ewithprobability
thecausaleffectofeachparentonagivennodeinthegraph.
0.1. The PFA restricts state transitions such that the total Ourprototypeusesalinearmodel,butusersofPalettemay
probabilityofalloutgoingtransitionsforastatesumtoone. overridethisbyusingnon-linearmodelstorepresentmore
Theprobabilistictransitionbetweenmanystatesencodes complexdistributionsbyadjustingtheequationsinTable2
theabilityofdifferentexecutionpaths. torepresentthenewmodel.
GCMCapturesPerformanceProperties.Paletteincludes TopologytoSpecifications.Palettethenconvertsthetopo-
aGCMinthetopologystructureofeachAPItoencodethe logicalmodelintoactualsourcecodethatencodestheper-
performance properties of the observed system. Suppose formance properties of the system. For each API, Palette
we want to model the latency of an API, A, which calls convertsitscorrespondingPFAintoasetoflocalfunctions
twodownstreamAPIs,BandCwithdifferingprobabilities. toencodePFAstatesandtransitions.Palettealsoencodes
EachAPI’slatencyisrepresentedasaseparatenode,andthe aGCMmodelfortheAPIandlinksittotheGCM-enabled
latencyofAdependsonthelatenciesofBandC,inadditional runtime. For certain performance properties, Palette also
tosomelocalwork.Figure4showsthecausalgraphforthis encodeshowthatpropertyshouldbeachieved.Forexample,
simplescenario.ThelatencyofAPIAisdirectlyinfluenced toachieveasampledamountoflatency,Palettechoosesto
bythelatenciesofBandC,sotherearecausaledgesfrom performmatrixmultiplicationsforthatamountoftime.
theirlatencynodestoA’s,thatcapturethecombinedimpact ImplementationGeneration.WecombinePalettewith
oftheirlatencyonA’slatency.Moreover,asBandCmay Blueprint[2]togenerateafullimplementationofthesystem.
not always be called, this is represented as ‘called’ nodes Blueprintprovidestheinfrastructuralpiecesnecessaryfor
in the graph which represent the probability of B and C generatingadeployableversionofthesystem.
beingcalled.Here,Palettemodelseach‘called’nodecanbe
modeled as a simple Bernoulli distribution by default but
userscanoverridethistousemoresophisticatedorcustom
distributions.However,thecausalgraphdoesnotdistinguish 3.3 SupportingInterventions
betweensequentialcallstoBandCfromconcurrentcalls Palettesupportsinterventionsbyallowinguserstoexecute
toBandC.ThisinformationisprovidedbythePFAforthe interventionsatfourdifferentstages.
API, which determines how to combine the values of the Trace Processing Interventions. Users can modify the
parentsinthecausalequation.Forexample,Table2shows traceprocessingsteptofilteroutinvalidorirrelevantedge
thecausalequationbuiltforeverylatencynodeinthegraph cases.Moreover,userscanaugmentthedatadimensionspro-
basedonthebehaviorofitsimmediateparents.Notethat cessedbyPaletteandupdatetheGCMgenerationprocedure
differentperformancepropertieswouldresultindifferent toincludethesedimensions.Newnodescanbeaddedtothe
setofequations. graphtorepresentnewdimensionsofdataandtheycanbe
connectedtoexistingnodesthattheyinfluence.Forinstance,
3.2 Generationmechanism
ifanoperatorstartscollectingdataonthepayloadsizeof
GeneratingTopologyFromTraces.Paletteprocessesthe differentAPIcalls,andthepayloadsizeaffectsthelatency
tracedatasettocalculatestatisticalinformationabouteach ofdownstreamcalls,anedgebetweenthepayloadsizeof
servicefromthetracesincludingalistofallitsAPIs,theex- thecallingservicecanbeaddedtothevertexrepresenting
ecutiontimeforeachAPI,theprobabilityofeveryoutgoing the latency of the callee service. Another example is that
callforeachAPI,andthedependenciesforeachservice.The researchersinterestedinanewcongestioncontrolalgorithm
collectedinformationcanbefurtheraugmentedwithmore canaugmentthedatadimensionstoincludetimeoutvalues
statisticsdependingontheinformationavailableintraces. thatarethenreflectedintheGCMandgeneratedsystem,
Duringtheprocessing,PalettealsobuildsaPFAforeachAPI sotheycanunderstandhowtheiralgorithmbehavesina
whileitprocessesthetracedata.Oncethetraceprocessing large-scalemicroservice.
151

APSys’25,October12–13,2025,Seoul,RepublicofKorea VaastavAnand,MatheusStolet,JonathanMace,andAntoineKaufmann
Topological Interventions. The user can apply custom LiveCorrections.Duringthesystemexecution,systems
modificationstothetopologythroughasetofmodification maydeviatefromtheexpectedbehaviorofthesystem.For
primitives. For example, a researcher can add new edges example,atimeoutmaybetriggeredinoneoftheAPIsdue
andverticestorepresentnewcausalrelationshipsbetween todifferentperformancecharacteristicsofthedeployedhard-
microservices.Largetopologiescanalsobedownscaledtofit ware.GCMsenablelivecorrectionsduringruntimewhen
thephysicaltestbedavailabletotheresearcherbyremoving executiondivergesfromthebehaviorobservedintheoriginal
edges and vertices representing the different APIs. These traces.Themodelenablesmoreinformedsamplingdecisions
interventionscanbeusefulforsomeoneinvestigatinghow aboutsystembehaviorbyconditioningthesamplingprocess
theirnewresourcemanagerbehaveswhenthecallgraphfor on the underlying causal relationships that influence the
aserviceincreasesindepthorwidth,possiblyaffectingthe generatedmetrics.
outcomeofallocationdecisions.
SpecificationInterventions.Theusercanchangehowa 4 Conclusions
performancepropertyisachieved.Forexample,toachieve
Inthispaper,wehavepresentedthedesignofanextensible
desiredlatency,dependentontheusecase,theusermight
systemforgeneratingrepresentativemacrobenchmarkmi-
wantitsservicestosleepandnotdoanyworkortheymight
croservicesystemsfromdistributedtracedatasetsthatuses
wanttheservicestoaddworkthatismemorybound.
GraphicalCausalModels(GCMs)formodelingsystembe-
InstantiationInterventions.Userscanaddfurtherinter-
haviortopreservethedesiredrepresentativecharacteristics
ventions to the system by modifying the Blueprint IR to
ofamicroservicesystems.WebelievethatPaletteprovides
modifyconcreteserviceimplementations.Forexample,the
aflexiblewayforuserstoconductinterventionexperiments
IRcanbemodifiedtosupportdifferentRPCframeworksthat
tovalidateandtestnewadvancementsformicroservices.
changehowtheactualbenchmarksystemgetsinstantiated.
Acknowledgments
3.4 GCM-BasedRuntime
Wewouldliketothanktheanonymousreviewersfortheir
EachAPIleveragesthecausalequationandcoefficientspro- invaluablefeedbackandforhelpingusshapethefinalversion
duced by Palette to drive system execution in a way that ofthepaper.
resemblestheoriginalsystembehavior.Forexample,therun-
timesamplestheGCMateachAPItoobtainvaluessuchas
References
theexecutiontimeorthepayloadsizeforoutgoingmessages.
[1] AbdullahAlomar,PouyaHamadanian,ArashNasr-Esfahany,Anish
Thesesamplesareconditionedonthecausalrelationships
Agarwal,MohammadAlizadeh,andDevavratShah. {CausalSim}:A
encodedintheGCM,allowingthesystemtobettercapture causalframeworkforunbiased{Trace-Driven}simulation. In20th
dependenciesthansamplingfromtheobserveddistributions. USENIXSymposiumonNetworkedSystemsDesignandImplementation
LiveMeasurements.Palettemakesmeasurementsfordif- (NSDI23),pages1115–1147,2023.
ferentnodesofthecausalgraphduringtheexecutionand [2] VaastavAnand,DeepakGarg,AntoineKaufmann,andJonathanMace.
Blueprint:Atoolchainforhighly-reconfigurablemicroserviceappli-
usesthesemeasurementsintothelocalcausalequationsat
cations. InProceedingsofthe29thSymposiumonOperatingSystems
everyAPItomakepredictionsabouttheexpectedbehavior.
Principles,pages482–497,2023.
For example, consider the latency scenario from Figure 4. [3] KailashBudhathoki,DominikJanzing,PatrickBloebaum,andHoiyi
IntheimplementationofAPIA,Palettewillinsertcodeto Ng.Whydidthedistributionchange?InInternationalConferenceon
measurethelatencyoftheoutgoingcallstoBandC.Palette ArtificialIntelligenceandStatistics,pages1666–1674.PMLR,2021.
[4] KailashBudhathoki,LenonMinorics,PatrickBlöbaum,andDominik
willthenplugtheactualmeasured/observedvaluesintothe
Janzing. Causalstructure-basedrootcauseanalysisofoutliers. In
causalequationtofindtheexpectedlatencyofA.
Internationalconferenceonmachinelearning,pages2357–2369.PMLR,
CausalBaggagePropagation.Thecausalgraphsofsome 2022.
APIs might require measurements made higher up in the [5] Adrian Cockcroft. The evolution of microservices. (April
call chain that are not directly measurable at the service 2016). Retrieved October 2020 from https://www.slideshare.net/
adriancockcroft/evolution-of-microservices-craft-conference,2016.
executingthespecificAPI.Toensurethatalltherelevant
[6] Adrian Cockcroft. Microservices workshop: Why, what, and
informationiscorrectlypropagatedbyupstreamnodestothe
how to get there. (April 2016). Retrieved October 2020 from
downstreamnodes,Paletteusesbaggagepropagation[25] https://www.slideshare.net/adriancockcroft/microservices-
topropagatetherequiredmeasurementstothedownstream workshop-craft-conference,2016.
nodesexecutingtheAPI.Palettecancompileandinjectthe [7] AndreaDetti,LudovicoFunari,andLucaPetrucci.𝜇bench:Anopen-
sourcefactoryofbenchmarkmicroserviceapplications.IEEETransac-
exactcodeforaddingthecausaldataintothebaggageand
tionsonParallelandDistributedSystems,34(3):968–980,2023.
propagateitdownstreamalongwiththerequestbecausethe
[8] DoWhydocumentationv0.8. Rootcauseanalysis(rca)oflatencies
dependencygraphisknownatgenerationtime. inamicroservicearchitecture.https://www.pywhy.org/dowhy/v0.8/
152

APSys’25,October12–13,2025,Seoul,RepublicofKorea
example_notebooks/rca_microservice_architecture.html,2024.[Ac- InProceedingsoftheACMSymposiumonCloudComputing,pages
cessed05-06-2025]. 412–426,2021.
[9] FanrongDu,JiuchenShi,QuanChen,LiLi,andMinyiGuo. Ami- [25] JonathanMaceandRodrigoFonseca.Universalcontextpropagation
croservicegraphgeneratorwithproductioncharacteristics,2024. fordistributedsysteminstrumentation.InProceedingsofthethirteenth
[10] FelixElwert.Graphicalcausalmodels.InHandbookofcausalanalysis EuroSysconference,pages1–18,2018.
forsocialresearch,pages245–273.Springer,2013. [26] microservicesdemo. Sockshop. RetrievedAugust2022fromhttps:
[11] RodrigoFonseca,GeorgePorter,RandyHKatz,andScottShenker. //github.com/microservices-demo/microservices-demo,2016.
{X-Trace}:Apervasivenetworktracingframework.In4thUSENIX [27] HaoranQiu,SubhoSBanerjee,SaurabhJha,ZbigniewTKalbarczyk,
SymposiumonNetworkedSystemsDesign&Implementation(NSDI07), andRavishankarKIyer. {FIRM}:Anintelligentfine-grainedresource
2007. managementframeworkfor{SLO-Oriented}microservices.In14th
[12] JoshuaFried,GoharIrfanChaudhry,EnriqueSaurez,EshaChoukse, USENIXsymposiumonoperatingsystemsdesignandimplementation
ÍñigoGoiri,SamehElnikety,RodrigoFonseca,andAdamBelay.Making (OSDI20),pages805–825,2020.
kernelbypasspracticalforthecloudwithjunction. In21stUSENIX [28] Sultan Mahmud Sajal, Timothy Zhu, Bhuvan Urgaonkar, and Sid-
SymposiumonNetworkedSystemsDesignandImplementation(NSDI dharthaSen. Traceupscaler:Upscalingtracestoevaluatesystems
24),pages55–73,2024. athighload.InProceedingsoftheNineteenthEuropeanConferenceon
[13] YuGan,YanqiZhang,DailunCheng,AnkithaShetty,PriyalRathi, ComputerSystems,pages942–961,2024.
NayanKatarki,ArianaBruno,JustinHu,BrianRitchken,Brendon [29] KorakitSeemakhupt,BrentEStephens,SamiraKhan,SihangLiu,Has-
Jackson,etal.Anopen-sourcebenchmarksuiteformicroservicesand sanWassel,SoheilHassasYeganeh,AlexCSnoeren,ArvindKrishna-
theirhardware-softwareimplicationsforcloud&edgesystems. In murthy,DavidECuller,andHenryMLevy.Acloud-scalecharacteri-
ProceedingsoftheTwenty-FourthInternationalConferenceonArchi- zationofremoteprocedurecalls.InProceedingsofthe29thSymposium
tecturalSupportforProgrammingLanguagesandOperatingSystems, onOperatingSystemsPrinciples,pages498–514,2023.
pages3–18,2019. [30] VishwanathSeshagiri,DarbyHuye,LanLiu,AvaniWildani,andRajaR
[14] EinasHaddad. Service-orientedarchitecture:Scalingtheuberengi- Sambasivan. [sok] identifying mismatches between microservice
neeringcodebaseaswegrow. (September2015).RetrievedOctober testbedsandindustrialperceptionsofmicroservices.JournalofSystems
2020fromhttps://eng.uber.com/service-oriented-architecture/,2015. Research,2(1),2022.
[15] Mazdak Hashemi. (January 2017). Retrieved February 2021 from [31] YuriShkuro.Microsim-microservicessimulator.AccessedJune2025
https://blog.twitter.com/engineering/en_us/topics/infrastructure/ fromhttps://github.com/yurishkuro/microsim,2018.
2017/the-infrastructure-behind-twitter-scale.html,2017. [32] GaganSomashekar,KaranTandon,AnushKini,Chieh-ChunChang,
[16] DarbyHuye,YuriShkuro,andRajaRSambasivan.Liftingtheveilon PetrHusak,RanjitaBhagwan,MayukhDas,AnshulGandhi,andNa-
{Meta’s}microservicearchitecture:Analysesoftopologyandrequest garajanNatarajan. {OPPerTune}:{Post-Deployment}configuration
workflows.In2023USENIXAnnualTechnicalConference(USENIXATC tuningofservicesmadeeasy.In21stUSENIXSymposiumonNetworked
23),pages419–432,2023. SystemsDesignandImplementation(NSDI24),pages1101–1120,2024.
[17] DominikJanzing,KailashBudhathoki,LenonMinorics,andPatrick [33] AkshithaSriraman,AbhishekDhanotia,andThomasFWenisch.Soft-
Blöbaum.Causalstructurebasedrootcauseanalysisofoutliers.arXiv sku:Optimizingserverarchitecturesformicroservicediversity@scale.
preprintarXiv:1912.02724,2019. InProceedingsofthe46thInternationalSymposiumonComputerArchi-
[18] AnujKalia,MichaelKaminsky,andDavidAndersen.DatacenterRPCs tecture,pages513–526,2019.
canbegeneralandfast. In16thUSENIXSymposiumonNetworked [34] AkshithaSriramanandThomasFWenisch. {𝜇Tune}:{Auto-Tuned}
SystemsDesignandImplementation,NSDI,2019. threadingfor{OLDI}microservices.In13thUSENIXSymposiumon
[19] AntoineKaufmann,TimStamler,SimonPeter,NaveenKr.Sharma, OperatingSystemsDesignandImplementation(OSDI18),pages177–194,
ArvindKrishnamurthy,andThomasAnderson.TAS:TCPacceleration 2018.
asanOSservice. In14thACMEuropeanConferenceonComputer [35] MertToslali,EmreAtes,AlexEllis,ZhaoqiZhang,DarbyHuye,Lan
Systems,EuroSys,2019. Liu,SamanthaPuterman,AyseKCoskun,andRajaRSambasivan.
[20] MariosKogias,GeorgePrekas,AdrienGhosn,JonasFietz,andEdouard Automatinginstrumentationchoicesforperformanceproblemsindis-
Bugnion.R2P2:MakingRPCsfirst-classdatacentercitizens.In2019 tributedapplicationswithvaif.InProceedingsoftheACMSymposium
USENIXAnnualTechnicalConference,ATC,2019. onCloudComputing,pages61–75,2021.
[21] Gautam Kumar, Nandita Dukkipati, Keon Jang, Hassan MG Was- [36] ZhiqiangXie,YujiaZheng,LiziOttens,KunZhang,ChristosKozyrakis,
sel,XianWu,BehnamMontazeri,YaogongWang,KevinSpringborn, andJonathanMace.Cloudatlas:Efficientfaultlocalizationforcloud
ChristopherAlfeld,MichaelRyan,etal. Swift:Delayissimpleand systemsusinglanguagemodelsandcausalinsight. arXivpreprint
effectiveforcongestioncontrolinthedatacenter.InProceedingsofthe arXiv:2407.08694,2024.
AnnualconferenceoftheACMSpecialInterestGrouponDataCommu- [37] HaoranZhang,KonstantinosKallas,SpyrosPavlatos,RajeevAlur,
nicationontheapplications,technologies,architectures,andprotocols SebastianAngel,andVincentLiu. {MuCache}:Ageneralframework
forcomputercommunication,pages514–528,2020. forcachinginmicroservicegraphs. In21stUSENIXSymposiumon
[22] PedroLas-Casas,GiorgiPapakerashvili,VaastavAnand,andJonathan NetworkedSystemsDesignandImplementation(NSDI24),pages221–
Mace. Sifter:Scalablesamplingfordistributedtraces,withoutfea- 238,2024.
tureengineering. InProceedingsoftheACMSymposiumonCloud [38] IreneZhang,AmandaRaybuck,PratyushPatel,KirkOlynyk,Jacob
Computing,pages312–324,2019. Nelson,OmarSNavarroLeija,AshlieMartinez,JingLiu,AnnaKo-
[23] I-TingAngelinaLee,ZhizhouZhang,AbhishekParwal,andMilind rnfeldSimpson,SujayJayakar,etal. Thedemikerneldatapathos
Chabbi.Thetaleoferrorsinmicroservices.ProceedingsoftheACMon architectureformicrosecond-scaledatacentersystems.InProceedings
MeasurementandAnalysisofComputingSystems,8(3):1–36,2024. oftheACMSIGOPS28thSymposiumonOperatingSystemsPrinciples,
[24] ShutianLuo,HuanleXu,ChengzhiLu,KejiangYe,GuoyaoXu,Lip- pages195–211,2021.
ingZhang,YuDing,JianHe,andChengzhongXu. Characterizing [39] LeiZhang,ZhiqiangXie,VaastavAnand,YmirVigfusson,andJonathan
microservicedependencyandperformance:Alibabatraceanalysis. Mace.Thebenefitofhindsight:Tracing{Edge-Cases}indistributed
153

APSys’25,October12–13,2025,Seoul,RepublicofKorea VaastavAnand,MatheusStolet,JonathanMace,andAntoineKaufmann
systems.In20thUSENIXSymposiumonNetworkedSystemsDesignand Acausalhypergraphbasedframeworkforrootcauseanalysisinmul-
Implementation(NSDI23),pages321–339,2023. timodalmicroservicesystems,2025.
[40] YazhuoZhang,RebeccaIsaacs,YaoYue,JunchengYang,LeiZhang, [43] RenjieZhou,DezunDong,ShanHuang,andYangBai.Fasttune:Timely
andYmirVigfusson.Latenseer:Causalmodelingofend-to-endlatency andprecisecongestioncontrolindatacenternetwork.In2021IEEEIntl
distributionsbyharnessingdistributedtracing.InProceedingsofthe ConfonParallel&DistributedProcessingwithApplications,BigData
2023ACMSymposiumonCloudComputing,pages502–519,2023. &CloudComputing,SustainableComputing&Communications,So-
[41] ZhizhouZhang,MuraliKrishnaRamanathan,PrithviRaj,Abhishek cialComputing&Networking(ISPA/BDCloud/SocialCom/SustainCom),
Parwal,TimothySherwood,andMilindChabbi. {CRISP}:Critical pages238–245.IEEE,2021.
pathanalysisof{Large-Scale}microservicearchitectures. In2022 [44] XiangZhou,XinPeng,TaoXie,JunSun,ChenjieXu,ChaoJi,and
USENIXAnnualTechnicalConference(USENIXATC22),pages655–672, WenyunZhao.Poster:Benchmarkingmicroservicesystemsforsoft-
2022. wareengineeringresearch.In2018IEEE/ACM40thInternationalCon-
[42] ZimingZhao,ZhenweiWang,TiehuaZhang,ZhishuShen,HaiDong, ferenceonSoftwareEngineering:Companion(ICSE-Companion),pages
ZhenLei,XingjunMa,GaoweiXu,ZhijunDing,andYunYang.Chase: 323–324.IEEE,2018.
154