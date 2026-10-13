PDF Download
3680256.3721316.pdf
31 March 2026
Total Citations: 2
. Total Downloads: 827
.
Latest updates: hps://dl.acm.org/doi/10.1145/3680256.3721316 .
.
Published: 05 May 2025
.
. .
RESEARCH-ARTICLE .
Citation in BibTeX format
Investigating Performance Overhead of Distributed Tracing in
.
.
Microservices and Serverless Systems ICPE '25: 16th ACM/SPEC International
Conference on Performance Engineering
May 5 - 9, 2025
ANDERS NÕU, Free University Amsterdam, Amsterdam, Noord-Holland, Netherlands Toronto ON, Canada
.
. .
SACHEENDRA TALLURI, Free University Amsterdam, Amsterdam, Noord-Holland, Conference Sponsors:
SIGMETRICS
Netherlands
SIGSOFT
.
ALEXANDRU IOSUP, Free University Amsterdam, Amsterdam, Noord-Holland, Netherlands
.
DANIELE BONETTA, Free University Amsterdam, Amsterdam, Noord-Holland, Netherlands
.
.
.
Open Access Support provided by:
.
Free University Amsterdam
.
ICPE '25: Companion of the 16th ACM/SPEC International Conference on Performance Engineering (May 2025)
hps://doi.org/10.1145/3680256.3721316
ISBN: 9798400711305
.

Investigating Performance Overhead of Distributed Tracing in
Microservices and Serverless Systems
AndersNõu SacheendraTalluri DanieleBonetta
VrijeUniversiteitAmsterdam AlexandruIosup VrijeUniversiteitAmsterdam
Amsterdam,TheNetherlands VrijeUniversiteitAmsterdam Amsterdam,TheNetherlands
anders.nou@gmail.com Amsterdam,TheNetherlands d.bonetta@vu.nl
{s.talluri,a.iosup}@vu.nl
Abstract trackingrequestsastheyflowthroughvariousservicesandcompo-
Distributedtracingiscrucialtoachieveobservabilityinmodern nents,distributedtracingprovidesinsightsintothebehaviorand
distributedsystems.However,itsadoptionintroducesperformance interactionswithinapplications[11,26].Thislevelofobservability
trade-offs, impacting throughput and latency. This paper inves- isnecessarytoidentifyperformancebottlenecks,understandsys-
tigatestheoverheadofdistributedtracinginmicroservicesand temdependencies,andensurethereliableoperationofdistributed
serverlessapplications.WeprovideananalysisofthepopularOpen- applications[22].Despiteitsbenefits,distributedtracingintroduces
TelemetryandElasticAPMdistributedtracingframeworks,eval- additionaloverhead,whichcannegativelyimpactthethroughput
uatingtheirperformanceimpactonmicroservicesandserverless andlatencyoftheapplicationsbeingmonitored[14,16,20,27,28].
workloads. We highlightand categorize the primary sources of Understandingtheperformanceimplicationsofdistributedtrac-
overheadandmeasuretheircontributiontoperformancedegrada- ingiscrucial[11].Applicationsthatpartitionworkintoindepen-
tion.Theresultsrevealsignificantthroughputreductions(19-80%) dentlyprocessedtaskscanbeparticularlysensitivetotheover-
andlatencyincreases(upto175%)dependingonapplicationcon- head introduced by tracing [17, 31]. These applications involve
figurationsandexecutionenvironments.Ourfindingsrevealthat low-latencyoperations,whereevensmallincreasesinlatencycan
serializingtracedataforexportisthelargestcauseofoverhead. significantlyimpactoverallperformance.Asaresult,itisessential
toquantifytheperformanceoverheadofdistributedtracingand
identifythemaincontributorstothisoverhead.
CCSConcepts
Thispaperaimstofillthegapintheunderstandingofdistributed
•Computersystemsorganization→Cloudcomputing;•Gen-
tracingoverhead,providingadetailedevaluationoftheimpactof
eralandreference→Measurement.
tracingondifferentsystemtypes.
Thispapermakesthefollowingcontributions:
Keywords
distributedtracing,instrumentation,performance,opentelemetry (1) Weintroduceasystematicframeworkformeasuringtracing
overheadacrossdiverseapplicationsandenvironmentsin
ACMReferenceFormat: Section3.
AndersNõu,SacheendraTalluri,AlexandruIosup,andDanieleBonetta.
(2) WecomparativelyanalyzetheOpenTelemetryandElastic
2025.InvestigatingPerformanceOverheadofDistributedTracinginMi-
APMinstrumentationtoolsandanalyzetheirperformance
croservicesandServerlessSystems.InCompanionofthe16thACM/SPEC
formicroservicesinSection4.
InternationalConferenceonPerformanceEngineering(ICPECompanion’25),
May5–9,2025,Toronto,ON,Canada.ACM,NewYork,NY,USA,5pages. (3) WeanalyzetheinstrumentationoverheadofOpenTelemetry
https://doi.org/10.1145/3680256.3721316 forserverlessapplicationsinSection5.
(4) Weprovideinsightsintothemaincontributorstotracing
1 Introduction overhead,includingtheconfiguration,instrumentation,and
exportstagesinSection6.
Moderncloudsoftwareoftencontainsmicroservicesandserverless
applications[19,23].Thesenewarchitectureshavebeenadoptedin
variousdomains,includingwebdevelopment,dataprocessing,and 2 Background:DistributedTracinginServerless
microservicearchitectures[10].However,thecomplexintercon- Applications
nectednatureofthesearchitecturesdemandshighobservabilityto
Distributedtracingisatechniquetomonitorandtrackrequestsas
ensurereliabilityandperformance[25].
theymovethroughdifferentelementsinadistributedsystem(e.g.,
Distributedtracinghasemergedasanecessarytoolformon-
messagesinaserverlessapplication).Capturingarequest’slifecycle
itoring and diagnosing the performance of distributed systems,
providesinsightsintohowservicesinteract,thesequenceofoper-
includingmicroservicesandserverlessapplications[22,24].By
ations,andwheretimeisspentwithinthesystem.Theresulting
visibilityoffersseveralkeybenefits.First,itenables(End-to-End
Traceability),allowingcomprehensivemonitoringincomplexdis-
ThisworkislicensedunderaCreativeCommonsAttribution4.0InternationalLicense. tributedarchitectures.Subsequently,itenablesPerformanceInsights
ICPECompanion’25,May5–9,2025,Toronto,ON,Canada byevaluatingperformancemetrics,includingrequestlatencyand
©2025Copyrightheldbytheowner/author(s). executiontimeofspecificoperationswithintheapplications.It
ACMISBN979-8-4007-1130-5/2025/05
https://doi.org/10.1145/3680256.3721316 favorsRootCauseAnalysis,asitprovidesadditionalcontextfor
162

ICPECompanion’25,May5–9,2025,Toronto,ON,Canada AndersNõu,SacheendraTalluri,AlexandruIosup,&DanieleBonetta
troubleshootingerrors,makingiteasiertopinpointthecauseofa andCPUutilizationindifferenttracingconfigurations.Theresults
performanceproblem.Finally,itallowsabetterunderstandingof wereaggregatedandanalyzedtoidentifypatternsandoutliers.
ServiceDependencies,offeringaclearpictureofservicerelation-
shipsandinteractions[22]. 3.2 Experimentalsetup
Giventheimportanceofdistributedtracing,severalframeworks
Allexperimentswereconductedonadedicatedclusternodewith
haveemergedinthelastfewyearsthatintegratewiththemost
thefollowinghardwarespecifications:Intel®Xeon®Silver4416+
popularprogramminglanguagesusedtoimplementserverlessap-
Processorat2.00GHz,with20coresand40threads;256.0GBof
plications.Inthispaper,wefocusonthetwomostprominentframe-
DDR4RAM,consistingoffourRAMunitsconfiguredtooperate
works,namelyOpenTelemetryandElasticAPM.Inthefollowing
at1200MHz(2400MT/s);1.5TBofSSDstorage;Ubuntu22.04.4
sections,webrieflyintroducethemainpropertiesofbothframe-
LTS.Regardinglangaugeruntimes,theversionsusedare:Python
works.
v3.9,Node.jsv18,Java17,andGo1.21.Allexperimentshavebeen
OpenTelemetry[8]isanopensourceobservabilityframework
deployedonaKubernetescluster(v1.20)runningDocker27.2.1.
thatprovidesstandardizedmethodsforcollecting,processing,and
WehaveusedthemostrecentstableversionsofOpenTelemetry
exportingtelemetrydata,includingtraces,metrics,andlogs.Open-
APIs(1.25.1forJavaScriptandPython)andlikewiseforElasticAPM
Telemetry provides standardized APIs and SDKs for trace data
(6.22.0)witharecentinstallationoftheFlaskframework(3.0.3).
collection,supportedinmultiplelanguagesandframeworks.
ElasticAPM[1]isanapplicationperformancemonitoringsys-
4 Experiment1:Microservices
temdesignedtoprovidedetailedperformancedataandend-to-end
Inourfirstexperiment,weexploredhowdistributedtracinginflu-
distributedtracingforapplications.ItispartofElasticStack[2],an
encestheperformanceofsimplemicroservicesimplementedusing
observabilityframeworkdesignedtocollect,analyze,andvisualize
popularprogramminglanguages.Thisfirstexperimentaimedto
logs,metrics,andtraces.
quantifytheoverheadacrossdifferentpopularframeworksused
formicroservicesdevelopment,namelyPythonFlask,JavaSpring,
3 DistributedTracingOverheadsAnalysis
Gohttp,andNode.js.Forthispurpose,weassessedthesefourweb
Inthiswork,weaimtostudytheperformancetrade-offsassociated frameworksinrelationtofourseparatemicroservices.Bytesting
withdistributedtracingframeworksandevaluatetheirpotential thesediverseframeworks,weaimtocoverawiderangeofuse
influenceonsystemperformance.Tothisend,wemeasuredthe casesprevalentinsoftwaredevelopmentduetotheirwidespread
overheadoftracingframeworksusingcontrolledexperimentsin use[3,4,6].Thevarietyalsoensuresin-depthanalysisofhowdis-
avarietyofpopularapplicationsanddeployments.Wefocuson tributedtracingperformsacrossdifferentprogrammingparadigms
quantifyingtheimpactoftracingonthroughput,latency,andre- and runtime environments, and reduces the risk that overhead
sourceutilization,aswellasonidentifyingthemainsourcesof measurementsareimpactedbylanguage-specificaspects.Inthis
overhead.Wehavedesignedandexecutedthreesetsofexperiments experiment,weevaluatedtheperformanceimpactofdistributed
thatfocusedondifferentapplicationsandpurposes.First,wefo- tracingbymeasuringRequestsPerSecond(RPS)underrealistic
cusedontheperformanceofstandalonemicroservices.Thishad conditionssimulatingpeaktraffic.Weestablishedtheimpactof
thegoalofmeasuringtheinstrumentationoverheadofasingleweb instrumentationontheapplicationsbydeterminingthemaximum
service(e.g.,asingleHTTPrequesthandler).Second,wefocusedon RPSeachapplicationcanhandlewhilemaintainingaconstantCPU
serverlessapplicationsandplatforms.Thissecondexperimenthad utilization.
thegoalofmeasuringtheimpactoftracingandinstrumentationin
morerealisticclouddeploymentscenarios.Finally,weexpanded
4.1 Applicationsundertest
onthetwopreviousexperimentsandanalyzedthesourcesofthe
Thisfirstexperimentisbasedonfourdifferentmicroservicesin-
performanceoverheadmeasuredinourexperimentswiththegoal
cluded in TechEmpower [5]. TechEmpower is a comprehensive
ofidentifyingtherootcausesofperformancedegradation.
benchmarkingsuitedesignedtomeasuretheperformanceofweb
frameworks.Itprovidesastandardizedmethodologyforafaircom-
3.1 ExperimentalWorkloadsandFrameworks parison between different web technologies. The suite includes
WebasedourmicroserviceperformanceevaluationontheTech- seventesttypes:JSONserialization,singleandmultipledatabase
EmpowerFramework[7].Forserverlessapplications,weusedthe queries,server-sidetemplating,databaseupdates,plaintextpro-
ServerlessBenchmarkSuite[13](SeBS).Bothbenchmarkingframe- cessing,andcachingmechanisms.Theseendpointscovervarious
worksprovideavarietyofworkloadsandimplementationsindif- applicationworkflows,enablingarobustevaluationofapplications
ferentprogramminglanguages.Ineveryexperiment,thebaseline underdifferentworkloads.Weselectedfourendpointsforourex-
consistedofunmodifiedapplicationswithoutinstrumentation.We periments,coveringmultipleusecasestothoroughlycomparethe
utilizedOpenTelemetryandElasticAPMtoinstrumentallservices, applicationsundervariousworkloads.Theimplementedendpoints
allowingustoevaluatethroughputandlatencyacrossdifferent arejson,db,object,andqueries.Theseendpointsaredescribedin
workloads.TheexperimentswereexecutedwithinaKubernetesen- theTechempowerbenchmarkdocumentation[5].
vironment,usingcontainerizationtoensureconsistentandrepeat- Inthisexperiment,wecomparedOpenTelemetryandElastic
ableconfigurations.Theexperimentalsetupinvolvedmultipleitera- APMwithabaselineuninstrumentedapplication.Automaticinstru-
tionsofteststoaccountforvariabilityinsystemperformance.Each mentationwasappliedtoOpenTelemetryandElasticAPMsetups
iterationmeasuredkeymetricssuchasrequestlatency,throughput, acrossallwebframeworksassessed.Additionally,weemployed
163

InvestigatingPerformanceOverheadofDistributedTracinginMicroservicesandServerlessSystems ICPECompanion’25,May5–9,2025,Toronto,ON,Canada
|     |      |         |     |     |     |     |     | )sm( noitaruD tseuqeR Endpoint: json |     | )sm( noitaruD tseuqeR Endpoint: db |     |
| --- | ---- | ------- | --- | --- | --- | --- | --- | ------------------------------------ | --- | ---------------------------------- | --- |
|     | 2500 | Max:    |     |     |     |     |     |                                      |     |                                    |     |
|     |      | 2400.00 |     |     |     |     |     |                                      |     | 4                                  |     |
dnoceS rep stseuqeR
|     |     |     |     |     |     |     |     | 2   |     | 3   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
2000
|     |     |     |      |     | Max: |     |     |                                        |     | Median: 1.77Median: 1.96Median: 1.80 |     |
| --- | --- | --- | ---- | --- | ---- | --- | --- | -------------------------------------- | --- | ------------------------------------ | --- |
|     |     |     | Max: |     |      |     |     | 1 Median: 0.62Median: 0.74Median: 0.67 |     | 2                                    |     |
1480.00
|     | 1500 |     | 1580.00 |     |     |     |     |     |     | 1   |     |
| --- | ---- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
0
1000 Mean: Non- OpenTel. Elastic APM Non- OpenTel. Elastic APM
|     |     |        |     |       |     |     |     | Instr. Instr. | Instr. | Instr. Instr. | Instr. |
| --- | --- | ------ | --- | ----- | --- | --- | --- | ------------- | ------ | ------------- | ------ |
|     |     | 691.88 |     | Mean: |     |     |     |               |        |               |        |
M e d i a n: Mean: )sm( noitaruD tseuqeR Endpoint: updates )sm( noitaruD tseuqeR Endpoint: queries
|     | 500 |         |         | 442.56 |         | 382.50 |     |     |     |     |     |
| --- | --- | ------- | ------- | ------ | ------- | ------ | --- | --- | --- | --- | --- |
|     | 39  | 5 . 0 0 | Median: |        | Median: |        |     |     |     |     |     |
|     |     |         | 242.50  |        | 200.00  |        |     | 15  |     |     |     |
|     |     | Min:    |         | Min:   |         | Min:   |     |     |     | 10  |     |
|     | 0   | 40.00   |         | 32.00  |         | 20.00  |     |     |     |     |     |
10
|     |     | Non-         | OpenTelemetry |     | Elastic APM  |     |     | Median: 3.52Median: 4.10Median: 5.01 |     |                            |     |
| --- | --- | ------------ | ------------- | --- | ------------ | --- | --- | ------------------------------------ | --- | -------------------------- | --- |
|     |     |              |               |     |              |     |     | 5                                    |     | 5 Median: 4.02Median: 4.11 |     |
|     |     | Instrumented | Instrumented  |     | Instrumented |     |     |                                      |     | Median: 2.88               |     |
0
Figure1:Throughputofmicroservicesbenchmarkswithdif- Non- OpenTel. Elastic APM Non- OpenTel. Elastic APM
|     |     |     |     |     |     |     |     | Instr. Instr. | Instr. | Instr. Instr. | Instr. |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | ------ | ------------- | ------ |
ferentinstrumentationframeworks.
Figure2:Latencyofmicroserviceendpointswithdifferent
PostgreSQL5,awidely-usedopen-sourceobject-relationaldatabase instrumentationframeworks.
system.ItsprevalentusageandsupportwithintheTechEmpower
Frameworkmadeitanappropriatechoiceforourexperimental tracingisenabled,throughputdecreasessignificantly.WithOpen-
architecture. Telemetry,themedianthroughputdecreasesby38.6%compared
tothenon-instrumentedmedian.Themeanthroughputdropsby
4.1.1 Loadgeneration. Togeneratetheexperimentalrequestswork- 36.0%andthemaximumthroughputdropsto1,580RPS(decreased
load,weusedk6[9],anopensourceloadtestingtooldesignedto by34.20%).TheelasticAPMinstrumentedconfigurationhasan
| test | the performance | and | reliability | of  | web applications. | k6 of- |     |     |     |     |     |
| ---- | --------------- | --- | ----------- | --- | ----------------- | ------ | --- | --- | --- | --- | --- |
evengreaterimpactonthroughput,withthemedianfallingto200
fersscriptingcapabilitiesandavarietyofexecutorstosimulate
RPS,a49.4%decrease.Themeanthroughputdropsto382.5RPS,
real-worldtrafficpatternsandstresstestwebapplications.Wese-
markingareductionof44.7%,whilethemaximumvalueofRPSis
lectedk6becauseitcangenerateconsistentandcustomizableload reducedto1,480RPS.WeobservethatelasticAPMintroducesa
patternsandsupportsdistributedandlarge-scaleperformancetest- moresignificantperformanceoverheadwithrespecttothroughput
ing.Inourexperiment,weconfiguredk6tousescenariosandthe thanOpenTelemetry.
constant-arrival-rateexecutortoruntheloadtests.Thisconfigura-
tionallowedustomaintainaconsistentrequestratethroughout 4.2.2 Latency. section4.2.2illustratesthedistributionandmedian
|     |     |     |     |     |     |     | latency | in milliseconds | for different | instrumentation | configura- |
| --- | --- | --- | --- | --- | --- | --- | ------- | --------------- | ------------- | --------------- | ---------- |
thedurationofthetest,ensuringthattheapplicationsaresubjected
tions(non-instrumented,OpenTelemetryinstrumented,andElastic
toasteadyloadforstableresults.Wedefinedak6testscenario
APMinstrumented)forthefourbenchmarkendpoints(json,db,
foreachendpoint,instrumentationmethod,andcombinationof
framework.Eachscenarioisconfiguredwithduration,numberof updates,andqueries).Thedataisaggregatedovertheevaluated
virtualusers,warmupperiod,andcoolingperiod. frameworkstopresentageneralviewoflatencyoverheadacrossdif-
ferentrequests.Thefigureshowsthatenablingdistributedtracing
consistentlyincreaseslatencycomparedtothenon-instrumented
4.2 Resultsoverview
configuration.Theextentofoverheadhighlyvariesdependingon
Themainfindingsforthisexperimentcanbesummarizedasfol-
lows. theendpoint.Forthejsonendpoint,latencyincreasesbyapproxi-
mately19%,fromamedianof0.62to0.74mswithOpenTelemetry,
|     | • Distributed | tracing | reduces | throughput | across | all frame- |     |     |     |     |     |
| --- | ------------- | ------- | ------- | ---------- | ------ | ---------- | --- | --- | --- | --- | --- |
whileelasticAPMintroducesalowerincrease7%.Theupperquar-
works,withdeclinesrangingfrom19.55%to80.18%.
tilevalueisalsosignificantlyhigherforOpenTelemetry.Theimpact
JavaSpringexhibitsthelowestoverheadwithmicroservice
|     | •   |     |     |     |     |     | ismoresignificantfortheendpointsforupdatesandqueries.The |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------------------------------------------------------- | --- | --- | --- | --- |
applications,whileNode.jsshowsthemostsignificantim-
medianlatencyfortheupdateendpointincreasesby16.5%forOpen-
pactonthroughput.
Telemetryandapproximately42%forElasticAPM.Forqueries,the
• OpenTelemetrygenerallydelivershigherthroughputthan
performanceoverheadforbothinstrumentationtoolsissimilar:
ElasticAPMacrossmostframeworks.
39.6%forOpenTelemetryand42.7%forElasticAPM.Overall,the
Theresultsunderscoretheimportanceofselectingappropriate lessintensiveendpointsjsonanddbincurredlessoverheadoverall
| tracing | configurations |     | based on | application | characteristics | and |     |     |     |     |     |
| ------- | -------------- | --- | -------- | ----------- | --------------- | --- | --- | --- | --- | --- | --- |
andlessoverheadwithElasticAPMcomparedtoOpenTelemetry.
programminglanguages.Forexample,frameworkswithhigh-level
However,moreintensivebenchmarkupdatesandqueriesexhibited
abstractions,suchasPythonFlask,exhibitedgreatersensitivityto
lessoverheadwithOpenTelemetryincomparisontoElasticAPM
tracingoverhead.Incontrast,lower-levelframeworkslikeGohttp
demonstratedmorestableperformanceundersimilarconditions. 5 Experiment2:ServerlessApplications
Figure1showstheaggregatedthroughputinre- Weperformedasecondexperimenttoevaluatetheperformance
4.2.1 Throughput.
questspersecondacrossthreeconfigurations.Thenon-instrumented overheadintroducedbydistributedtracinginserverlessapplica-
configurationhasthehighestthroughput,withamedianof395RPS tions.Weexaminehowtracingimpactsapplicationlatencyand
andameanof691.88RPS,reachingamaximumof2,400RPS.When comparetheseeffectsacrossdifferentprogrammingframeworks.
164

ICPECompanion’25,May5–9,2025,Toronto,ON,Canada AndersNõu,SacheendraTalluri,AlexandruIosup,&DanieleBonetta
Theanalysisaimstoprovideinsightintothetrade-offsinvolvedin dynamic-html uploader thumbnailer
implementingtracinginserverlessapplications. Median: 160
6 6.96 35
140
30
5.1 Applicationundertest 4 M 2 e 8 d . i 8 a 0 n: 120 Median: 25 Median: Median: 121.94
Wedesignedaseriesoftestscenariosacrossmultipleconfigurations Median: 25.39 100 112.61
andenvironmentstoevaluatetheperformanceoverheadoftracing 2 2.53 20
80
inserverlessapplications.Theexperimentsarecenteredontwo Non- Instr. Non- Instr. Non- Instr.
ofthemostpopularprogrammingframeworksformicroservices, Instr. Instr. Instr.
namelyPythonFlaskandNode.js,usingfivedistinctbenchmark video-processing graph-pagerank
applications.Eachapplicationisexecutedintwoconfigurations:in- 1800 Median: 8000
1797.24
strumented(withtracingenabled)andnon-instrumented(without 1600 6000
t d r i a ff c e in re g n ). t T a h p e p s li e c t a u t p io a n ll s o a w n s d u f s r t a o m a e n w al o y r z k e s t , h r e es i u m l p ti a n c g to in ft 2 r 0 ac i i n n d g iv a i c d r u os a s l 1400 1 M 4 e 1 d 1 ia .5 n 7 : 4000 4 M 5 e 7 d 9 ia .3 n 3 : 4 M 8 e 8 d 5 ia .6 n 9 :
benchmarkexecutions(10perframework:5instrumentedandfive 1200 2000
non-instrumented).
Non- Instr. Non- Instr.
Thebenchmarkapplicationsrepresentarangeofmicroservices Instr. Instr.
workloads,includinglow-andhigh-latencyservices.Weaimto Configuration
isolatetheoverheadintroducedbytracingandassesshowitvaries
acrossdifferentframeworksandworkloads.
AllexperimentsarebasedontheServerlessBenchmarkSuite
(SeBS), a framework designed to evaluate the performance and
cost-efficiencyofserverlessplatformsandfunctions[13].SeBSfa-
cilitatesthedeployment,execution,andmeasurementofserverless
functionsacrossmultiplecloudplatforms,includingAWSLambda,
AzureFunctions,GoogleCloudFunctions,andApacheOpenWhisk.
Theframeworkprovidesvariousbenchmarkapplicationsthatre-
flecttypicalserverlessworkloads.WeusedfiveSeBSapplications,
eachselectedtorepresentdifferenttypesofworkloadtoassessthe
performanceimpactoftracingcomprehensively.Thebenchmarks
includewebapplicationtasks,multimediaprocessing,andasci-
entificcomputationtask.Thisdiversityhelpstoevaluatetracing
overheadacrossawiderangeofscenarios.
AllapplicationsareimplementedinPythonandNode.js.For
benchmarkswithoutanativeNode.jsversion,wedevelopedNode.js
implementationsbasedonthePythonversionandexistingcode
examples.Eachapplicationhasbothinstrumented(tracingenabled)
andnon-instrumentedversions,resultingin20differentconfigura-
tions(10perprogramminglanguage).
TheapplicationsusedinthisexperimentaredynamicHTML,
uploader,thumbnailer,videoprocessing,andgraphpagerank.These
applicationsaredescribedintheSeBSpaper[13].
Byevaluatingthesebenchmarks,wecananalyzehowtracing
affectsvariousserverlesstasks,providinginsightsintoitssuitability
fordifferentapplications.
5.2 Resultsoverview
Serverlessfunctionsexhibiteddifferentanddiverseoverheadpat-
terns.Short-durationtasks,oftenreliantoncoldstarts,facedlatency
increasesupto175%.Thisoverheadmainlystemmedfromthetrac-
ingconfigurationanddataexportstages.Long-durationtasks,on
thecontrary,showedmodestincreasesof6.7%,highlightingarel-
ativemarginalimpactoftracingwhenapplicationsperformlong
operations.
Cold-startlatencywasparticularlypronouncedinenvironments
with extensive configuration requirements: the initialization of
tracingcomponentscontributedsignificantlytocoldstartoverhead,
)sm(
emiT
kramhcneB
naeM
Figure3:Meanexecutiontimeofdifferentapplicationsfrom
theSeBSbenchmark.
andoptimizingtheseinitializationprocessescouldmitigatethe
impactonshort-durationtasks.
5.2.1 Impactondifferentapplications. Figure3presentsboxplots
forfiveserverlessworkloadsacrossnon-instrumentedandinstru-
mentedconfigurations.Theresultsofthebenchmarksareaggre-
gatedoverbothPythonandNode.jsevaluations.
Theresultsindicatethattheperformanceimpactoftracingin-
strumentationvarieswidelydependingontheworkloadtype.For
example,dynamic-htmlworkload,witharelativelylowbaseline
latencyof2.53ms,showsanincreaseinmedianlatencyto6.96ms
wheninstrumented,showinganoverheadofapproximately175%.
Asthemedianrequestdurationincreases,theoverheadgener-
allydecreases.Forexample,theuploaderandthumbnailerwith
moderatemedianrequestdurationsshowamoremodestincrease
-13.43%overheadfortheuploaderand8.29%forthethumbnailer.
However,thevideo-processingworkloadwithamedianlatencyof
approximately1,411msexhibitsasubstantialincreaseof27.32%.
Thisconsiderableincreaseistheresultofthe70.69%overheadin
PythonasTable4.3shows.Thegraphpagerankworkload,which
hasthehighestbaselinelatencyamongworkloadswithamedian
of4,579.33ms,showsthelowestoverheadwith6.69%.
Thedatahighlightthattracingintroducesaconsiderableperfor-
manceimpactacrossworkloads.Thefunctionswithlowerrequest
durationshowthehighestincreasebutstillthelowestincrease
inabsolutevalues.Themorecompute-intensiveworkloadsincur
loweroverheadinpercentagebuthigherintermsofabsolutevalues.
6 OverheadAnalysis
In distributed tracing, various sources contribute to the overall
overheadobservedintheapplicationanditsinstrumentation.Ina
finalexperiment,weevaluatedtheoverheadsourcesinthecompu-
tationalpartofdistributedtracing[21].Theprimarycontributors
tooverheadcanbecategorizedandquantifiedasfollows:
• Configuration:Initializationandsetupoftracingcompo-
nents,includingmetadatageneration,contributedsignifi-
cantlytocold-startlatencyinserverlessenvironments.
165

InvestigatingPerformanceOverheadofDistributedTracinginMicroservicesandServerlessSystems ICPECompanion’25,May5–9,2025,Toronto,ON,Canada
100
80
60
40
20
0
0 20 40 60 80 100
Runs
emiT
latoT
fo
egatnecreP
availableathttps://github.com/atlarge-research/serverless-tracing-
Configuration Instrumentation Export Task
Endpoint: db Endpoint: updates overhead.
Acknowledgements
ThisworkwassupportedbytheEUHorizonGraphMassivizerand
theEUMSCACloudstarsprojects.Thisresearchwaspartlysup-
portedbyaNationalGrowthFundthroughtheDutch6Gflagship
project“FutureNetworkServices".
References
0 20 40 60 80 100
Runs [1] 2024. ApplicationPerformanceMonitoring(APM). https://www.elastic.co/
observability/application-performance-monitoring. Accessed:2024-05-20.
Figure4:Contributionofdifferenttracingstagestothein-
[2] 2024.ElasticStack.https://www.elastic.co/elastic-stack. Accessed:2024-09-22.
strumentationoverheadformicroserviceapplications. [3] 2024. FlaskSTackoverflow. https://stackoverflow.com/questions/tagged/flask.
Accessed:2024-09-28.
• Instrumentation: Capturing trace points and enriching [4] 2024.Node.jsStackoverflow.https://stackoverflow.com/questions/tagged/node.js.
Accessed:2024-09-28.
metadataintroducedcomputationaloverhead,particularly
[5] 2024. ProjectInformationFrameworkTestsOverview. https://github.com/
inframeworksrelyingonruntimeinstrumentation.Detailed TechEmpower/FrameworkBenchmarks/wiki/Project-Information-Framework-
profilingrevealedthatthefrequencyandgranularityoftrace Tests-Overview. Accessed:2024-05-05.
[6] 2024.SpringFrameworkStackoverflow.https://stackoverflow.com/questions/
pointswerekeyfactorsinfluencingthisoverhead. tagged/spring. Accessed:2024-09-28.
• Export:Transmittingtracedatatoexternalstoragesystems, [7] 2024.WebFrameworkBenchmarks.https://www.techempower.com/benchmarks.
Accessed:2024-09-05.
suchasElasticsearch,accountedforthemajorityofnetwork-
[8] 2024. What is OpenTelemetry? https://opentelemetry.io/docs/what-is-
relatedperformancecosts.Batchprocessingandcompres- opentelemetry/. Accessed:2024-09-21.
siontechniqueswereexploredaspotentialoptimizationsto [9] 2025.k6loadtestingtool.https://k6.io/.
[10] GojkoAdzicandRobertChatley.2017. Serverlesscomputing:economicand
reduceexportoverhead.
architecturalimpact.InFSE2017.884–889.
Anoverviewofthedifferentimpactofsuchoverheadsourceson [11] EricAndersonetal.2009.Efficienttracingandperformanceanalysisforlarge
distributedsystems.InIEEEMASCOTS2009.IEEE,1–10.
themicroservicesofSection4isdepictedinFigure4.Asthefigure [12] AndreBentoetal.2021.Automatedanalysisofdistributedtracing:Challenges
shows, exporting data to an external service is the largest con- andresearchdirections.JournalofGridComputing19,1(2021),9.
[13] MarcinCopiketal.2021.Sebs:Aserverlessbenchmarksuiteforfunction-as-a-
tributortooverheadformicroservices.Forserverlessapplications
servicecomputing.InMiddleware2021.64–78.
thesourcesofoverheaddependverymuchonworkload-specific [14] ÚlfarErlingssonetal.2012.Fay:Extensibledistributedtracingfromkernelsto
aspectsofanapplication,andarenotdirectlyinfluencedbythe clusters.ACMTOCS30,4(2012),1–35.
[15] RodrigoFonsecaetal.2007.{X-Trace}:Apervasivenetworktracingframework.
frameworkbeingused.
InNSDI2007.
[16] LoïcGelleetal.2021.Combiningdistributedandkerneltracingforperformance
7 RelatedWork
analysisofcloudapplications.Electronics10,21(2021),2610.
[17] FrancisGiraldeauandMichelDagenais.2015.Waitanalysisofdistributedsystems
Severalstudiesmeasuredeitherthroughputorlatency[15,17,20, usingkerneltracing.IEEETPDS27,8(2015),2450–2461.
[18] AndreaJanes,XiaozhouLi,andValentinaLenarduzzi.2023.Opentracingtools:
28–30]ofdistributedtracing.However,manystudiesdonotreport
Overviewandcriticalcomparison.JournalofSystemsandSoftware(2023),111793.
theabsoluteperformancevalues,makingitdifficulttoperform [19] EricJonasetal.2019. Cloudprogrammingsimplified:Aberkeleyviewon
directcomparisonsbetweentools. serverlesscomputing.arXivpreprintarXiv:1902.03383(2019).
[20] JonathanKaldoretal.2017.Canopy:Anend-to-endperformancetracingand
Giventheimpactofinstrumentationoverhead,severalmitiga- analysissystem.InSOSP2017.34–50.
tionstrategieshavebeenproposed.GoogleDapper[28]samples [21] PedroLas-Casasetal.2019. Sifter:Scalablesamplingfordistributedtraces,
0.1%ofrequests,resultingin16.3%latencyand1.5%throughput withoutfeatureengineering.InSoCC2019.312–324.
[22] JonathanMace.2017.End-to-EndTracing:AdoptionandUseCases.Survey.Brown
overhead.Canopy[20]usessampling,withan8.15%overheadfor University.
shortdurationapplicationsand0.76%forlongones.NanoLog[29] [23] GarrettMcGrathandPaulRBrenner.2017.Serverlesscomputing:Design,imple-
leadstoa4%increaseinlatencyanda19%reductioninthroughput.
mentation,andperformance.InICDCSWorkshops2017.IEEE,405–410.
[24] AustinParkerandother.2020. Distributedtracinginpractice:Instrumenting,
PopulartoolssuchasOpenTelemetry,Jaeger,Zipkin,andElastic analyzing,anddebuggingmicroservices.O’ReillyMedia.
APMvarysignificantlyintheoverheadtheyintroduceandinthe [25] RajaRSambasivanetal.2014.So,youwanttotraceyourdistributedsystem?
Keydesigninsightsfromyearsofpracticalexperience.CMU-PDL14(2014).
integrationcomplexitywithdifferentsystems[12,18,22]. [26] BoSangetal.2010.Precise,Scalable,andOnlineRequestTracingforMultitier
ServicesofBlackBoxes.IEEETPDS23(2010),1159–1167.
[27] JunxianShenetal.2023. Network-centricdistributedtracingwithdeepflow:
8 Conclusion
Troubleshootingyourmicroservicesinzerocode.InSIGCOMM2023.420–437.
Distributed tracing is essential for observability but introduces [28] BenjaminHSigelmanetal.2010.Dapper,alarge-scaledistributedsystemstracing
infrastructure.(2010).
significantperformanceoverhead.Ourstudyquantifiestheseim-
[29] StephenYang,SeoJinPark,andJohnOusterhout.2018.{NanoLog}:ANanosec-
pacts,categorizesthesourcesofoverhead,andprovidesactionable ondScaleLoggingSystem.InATC2018.335–350.
insightsformitigatingperformancepenaltieswhilemaintaining [30] LeiZhangetal.2023.TheBenefitofHindsight:Tracing{Edge-Cases}inDis-
tributedSystems.InNSDI2023.321–339.
systemvisibility.Futureworkincludesexploringlightweighttrac- [31] ZoltánZvara,PéterGNSzabó,BarnabásBalázs,andAndrásBenczúr.2019.Opti-
ingmethodologies,dynamicsamplingstrategies,andintegrating mizingdistributeddatastreamprocessingbytracing.FGCS90(2019),578–591.
machinelearningmodelstopredictandoptimizetracingconfig-
urations in real-time. Our experiment code is open-source and
166