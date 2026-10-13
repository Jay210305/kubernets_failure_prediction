IEEETRANSACTIONSONDEPENDABLEANDSECURECOMPUTING,VOL.21,NO.5,SEPTEMBER/OCTOBER2024 4921
MicroFI: Non-Intrusive and Prioritized Request-Level
Fault Injection for Microservice Applications
HongyangChen ,GraduateStudentMember,IEEE,PengfeiChen ,GuangbaYu ,StudentMember,IEEE,
XiaoyunLi ,andZilongHe ,GraduateStudentMember,IEEE
Abstract—Microserviceisawidely-adoptedarchitectureforcon-
structingcloud-nativeapplications.Totestapplicationresiliency,
chaos engineering is widely used to inject faults proactively in
applications. However, the searching space formed by possible
injectionlocationsishugeduetothescaleandcomplexityofthe
application. Although some methods are proposed to effectively
exploreinjectionspace,theycannotprioritizehigh-impactinjec-
tionsolutions.Additionally,theblastradiusoffaultsinjectedby Fig.1. Severalcallchainsofthreeapplicationfunctions.Serviceinstances
existingmethodsistypicallyfullofuncertainty,causingfaultsof communicatewithothersthroughproxieswhichareequippedwithforwarding
multipleapplicationfunctions.Althoughsometoolsaredesigned rulesfordifferentAPIinvocations.AnAPI-levelfaultoftheProductservice
toconductrequest-levelinjection,theyrequireinstrumentationon affectsrequestsissuedtotwootherAPIfunctions,namelySearchProductand
application code. To tackle these problems, this paper presents Checkout.
MicroFI, a non-intrusive fault injection framework, aiming to
efficiently test different application functions with request-level
applications. Therefore, service mesh [3], a communication
injection.Request-levelinjectionlimitstheblastradiustospecified
infrastructure, is proposed to resolve this problem by provid-
requestswithoutanysourcecodemodification.Additionally,Mi-
croFIleverageshistoricalinjectionresultsandparalleltechnique ing proxies to manage network traffic between services. For
toacceleratethesearching.Moreover,AnenhancedPageRankis example,inFig.1,theproxiesmanagethetrafficamongservice
used to measure the impact of faults and prioritize high-impact instances.Asaresult,thescaleofapplicationsincreases,leading
faultsthatfailmorefunctions.Evaluationsonthreemicroservice
to a higher level of network complexity [4], [5]. However,
applicationsshowthatMicroFIpreciselyinjectsfaultsandreduces
thecomplexinteractions,interferenceanddependenciesamong
upto91%redundantfaultsonaverage.Additionally,byemploy-
ingprioritization,MicroFIreducesanaverageof47.3%injection componentsrenderapplicationsmorefragile [6],[7],[8],[9].
budgetstocoverallhigh-impactfaults. Postmortem reports published by Gremlin [10] that the ab-
sence or inadequacy of resiliency (i.e., fault-handling) mecha-
IndexTerms—Microservice,faultinjection,chaosengineering,
servicemesh,tracing. nisms would probably lead to user-visible faults, and result in
a huge economic loss and serious user experience violations.
I. INTRODUCTION For example, a defective resiliency logic had led to failures
of instance creation in Google Compute Engine in 2018 [11],
MICROSERVICE architecture has become a popular ar-
impactingtheservicesdeployedonit.Therefore,itisacritical
chitecture to implement a large-scale, cloud-native ap-
tasktoverifywhethertheresiliencymechanismsactasexpected
plication.Withthisarchitecture,theapplicationisdecomposed
allthetime.
intodozensofsmall,loosely-coupledservicesthatcommunicate
Today, to assure applications are resilient to various faults,
throughsimpleAPIs[1],[2].Eachservicecomprisesseveralto
chaosengineering[12]iswidelyadoptedinITcompanies(e.g.,
hundredsofinstances.Withtherapidevolutionofuserrequire-
Netflix[13],Google[14],Microsoft[15],Linkedin[16]).Itisa
ments,thequantityofapplicationfunctions(e.g.,Login,Search)
disciplineofrandomlyinjectingfaultsintoaproductionsystem
as well as the kind of services increases, and the dependent
tobuildconfidenceintheresiliency [17].IthelpsITcompanies
relationshipsbetweenservicesbecomecomplex.Suchcomplex-
toalleviatecostlyoutagesbypreparingtheirteamsforunknowns
ity hinders the development and orchestration of microservice
andprotectingthecustomerexperience[18].
Generally,chaosengineeringismanuallyperformedinpro-
Manuscriptreceived19January2023;revised9January2024;accepted5 duction, and faults are typically injected according to domain
February2024.Dateofpublication8February2024;dateofcurrentversion4 knowledge[10],[13],[19].Forexample,Netflixhasexploited
September2024.ThisworkwassupportedinpartbytheNationalKeyResearch
theknowledgefromdomainexpertisewithineachteamrespon-
and Development Program of China under Grant 2019YFB1804002, in part
bytheGuangdongBasicandAppliedBasicResearchFoundationunderGrant sible for developing individual service to generate heuristics
2023B1515020054,inpartbytheNationalNaturalScienceFoundationofChina to guide the injection [13]. However, such a routine brings
underGrant62272495,andinpartbyAlibabaprojectunderGrant20925056.
someproblems.i)Thechaosexperimentmaycauseunintended
(Correspondingauthor:PengfeiChen.)
The authors are with the School of Computer Science and En- impactsonproductionapplicationsiftheblastradius[12]isnot
gineering, Sun Yat-Sen University, Guangzhou 510275, China (e-mail: controlled.Theblastradiusreferstothescopeoftheimpactthat
chenpf7@mail.sysu.edu.cn).
fault injection may have. The injection of service-level faults,
DigitalObjectIdentifier10.1109/TDSC.2024.3363902
1545-5971©2024IEEE.Personaluseispermitted,butrepublication/redistributionrequiresIEEEpermission.
Seehttps://www.ieee.org/publications/rights/index.htmlformoreinformation.
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on November 13,2025 at 00:55:27 UTC from IEEE Xplore. Restrictions apply.

4922 IEEETRANSACTIONSONDEPENDABLEANDSECURECOMPUTING,VOL.21,NO.5,SEPTEMBER/OCTOBER2024
TABLEI To address these challenges, we design MicroFI, a non-
AVERAGERESPONSETIME(MS)OFDIFFERENTTYPESOFREQUESTSIN
intrusive and fine-grained fault injection framework for cal-
DIFFERENTCASES(WITHOUTANYFAULTS(I.E.NORMAL)ANDWITH
DIFFERENTSERVICE-INSTANCE-LEVELFAULTSINJECTED) culating fault injection solutions in microservice applications.
Eachinjectionsolutioncontainsmultipleinjectionpoints.Since
MicroFI aims to break down invocations to service’s API, the
injectionpointconsistsofthetargetserviceandthetargetAPI.
i) To address the first challenge, we design the non-intrusive
request-level fault injection, which precisely restricts the blast
radius to the specific type of requests without causing unex-
pectedfaultsinapplications.ii)Toaddressthesecondchallenge,
includingfaultsattheservice-instance-levelandAPI-level,may we propose a new injection strategy by combining Lineage
affectrequeststhatinvokedifferentapplicationfunctionswhich DrivenFaultInjection(i.e.,LDFI)[31]andPageRank[32].With
utilize the same malfunctioning service (service instance or theextensions,ourmethodsupportstestingmultiplefunctionsin
API). For example, Table I shows the response time of var- parallelandprioritizinghigh-impactfaultsthatsimultaneously
ious types of requests in an open-source application Hipster break down multiple functions. Experimental results on three
Shop [20]. It can be seen that the blast radius of the injected representativeopen-sourcemicroserviceapplicationsshowthat
service-instance-level fault is not controlled, leading to an in- MicroFIsupportsnon-intrusiveinjectionwithapreciselycon-
creaseintheresponsetimeofalltypesofrequeststhatinvoke trolled blast radius. MicroFI reduces execution time by up to
thetargetinstance.Suchinjectedfaultswithuncontrolledblast 76%onaverageincalculatinginjectionsolutions,andbringsan
radius typically cause unintended impacts to the application. averagereductionof47.3%inthenumberofinjectionbudgetto
Forexample,asshowninFig.1,aninjectedAPI-levelfaultcan exposeallhigh-impactfaults.
aborttheinvocationoftheAPI/GetProductfortheproposeof Contributionsofthispaperare:i)Tocontroltheblastradiusof
testingtheSearchProductfunction.However,ifotherfunctions faults,weutilizeservicemeshanddistributedtracingtechnique
also invoke the same API, the injected fault may also impact to implement the non-intrusive request-level fault injection.
requests to those functions, such as the Checkout function. ii) Only pre-configured requests are affected. This method can
Thechaosexperimentinproductionrequiresoperatorstocon- readilybeappliedtovariousapplicationswithoutanyknowledge
centrateontheapplicationsincasesomefaultsraiseunnecessary of application source code. ii) We propose a lightweight and
customerpain.iii)Theknowledge-basedinjectionisinefficient online injection strategy. It automatically calculates injection
and unscalable. Considering an application with 100 services, solutionswithoutredundantfailureexploration,andprioritizes
thepotentialsolutionsspaceoffaultinjection—combinationsof high-impactfaultswithinlimitedinjections.iii)Wedesignand
faultlocations—is2100−1.Insuchahugespace,expertsneed implementMicroFI.Evaluationsonthreeopen-sourcemicroser-
toinvestsignificanttimeandefforttochooseinjectionsolutions vice applications, namely Hipster Shop [20], TrainTicket [33]
andfindafeasiblefault. and Hotel Reservation [34] demonstrate the effectiveness of
Facing these problems, we argue that chaos engineering MicroFI.
shouldbeefficientlyperformedwithaminimizedblastradius, This paper is organized as follows. Section II introduces
withafocusonrestrictingtheimpacttotargetrequests.Itisnot the related work and Section III presents the preliminaries of
a novel concept toconduct operations on the specified type of main techniques in MicroFI and introduces the motivations.
requests. For example, “Critical User Interaction attribution” Sections IV and V outline and specify our approach. In Sec-
has been introduced by Google [21] to provide aggregated tionVI,weevaluateourapproachonthreemicroserviceappli-
observability for the specified type of requests using tracing cations.SectionVIIdiscussesthelimitationsofMicroFIandthe
technique.Similarly,itisimportanttoconsidertheblastradius threatstovalidity.SectionVIIIconcludesthispaper.
in chaos engineering to control unintended consequences and
ensurethesafetyoftheapplicationundertest.However,chaos
engineeringwithaminimizedblastradiusrequiresanewinjec-
II. RELATEDWORK
tiontoolsincemostofpriortoolsonlysupportservice-level[22],
service-instance-level[23],[24]orAPI-levelfaultinjection[25]. Table II presents a comprehensive comparison amongst ex-
Faultsinjectedbythesetoolsaffectallrequeststhatpassthrough isting methods on fault injection from different perspectives.
thetargetservice,thetargetinstanceorthetargetAPI.Although Different columns represent different perspectives and their
some prior tools are designed to support request-level fault definitionsareshownasfollows.Explorationstandsforinjection
injection,theyallrequireinstrumentationonapplicationsource spaceexplorationmethods.TargetSystempresentsthekindof
code.Additionally,efficientchaosengineeringrequiresanewin- systems where the tools target. Fault Model defines the kind
jectionstrategysincepriorstrategiesexploreinjectionspaceby of injected faults. Pruning indicates the optimization of the
exhaustiveorknowledge-basedsearching[19],[22],[26],[27], explorationthatprunesthefaultspace.Prioritizationindicates
[28],[29],[30].Theserequirementsposechallenges,including if injection solutions are prioritized. Blast radius presents the
i)Howtocontroltheblastradiusoftheinjectedfaultwithoutany minimum impact scope of faults generated by these tools. In-
instrumentationtoapplicationcodes.ii)Howtoutilizeruntime strumentationindicateswhetherthetoolsneedtomodifysource
informationtotesttheapplicationefficientlyevenifthequantity code. Multiple Functions indicates whether the tools support
ofapplicationfunctionsandthefaultinjectionspacearehuge. jointinjectionspaceexplorationforallapplicationfunctions.
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on November 13,2025 at 00:55:27 UTC from IEEE Xplore. Restrictions apply.

CHENetal.:MICROFI:NON-INTRUSIVEANDPRIORITIZEDREQUEST-LEVELFAULTINJECTIONFORMICROSERVICEAPPLICATIONS 4923
TABLEII
COMPARISONSBETWEENEXISTINGWORKSFROMDIFFERENTPERSPECTIVES
FaultInjectionTools:Recently,severaltoolshavebeenpro- Explorationmethods:Existingexplorationmethodscanbedi-
posed to inject faults to the microservice application, general videdintothreecategories,namelyexhaustivesearch,developer
distributed systems or cloud infrastructure, shown in Table II. specifiedandLDFI.Exhaustivesearchbasedmethods[26],[27],
Some of tools [27], [28] support injecting performance faults [28]areinefficientbecausetheyexplorethefaultspaceexhaus-
(CPUoverload,memoryexhaustion,networkfailure,diskfail- tivelyandcheckwhetherallthecombinationsoffaultscanlead
ure, etc.) and crash failures (node crash, instance termination, tofailures.Specifically,ChaosBlade[27]andChaosMesh[28]
etc.) into the infrastructure (nodes, containers, etc.) hosting enableuserstoinjectmultiplefaultsinparallelandorchestrate
themicroserviceapplication.Theyalsomanipulatenetworkto them by manually defining chaos experiment workflow. It al-
inject performance faults (HTTP request delay, etc.) or crash lows users to prioritize which fault should be injected more.
failures(serviceunavailable,etc.)totheapplication.[19],[30], However, since the minimum blast radius of ChaosBlade and
[36] supports injecting network failure, disk failure and crash ChaosMesh is service instance, the impact of simultaneously
failure to distributed systems by interposing failure logic into injected faults is mixed, hindering the precise control of fault
I/Orelatedsystemcalls.Othertools[10],[13],[22],[35],[38] injections.Moreover,thefaultorchestrationmechanismrequires
manipulate network interactions between services to simulate manualconfiguration.Developerspecifiedbasedmethods[10],
theinjectionofperformanceandfunctionalfaultstomicroser- [19],[22],[30],[36]arenotflexibleenoughbecausetheyrequire
viceapplication.Amongthem,sometools[10],[35],[37]enable expertknowledgetoguidethesearch.LDFIbasedmethods[13],
injection to affect specific requests, but their usages require [38]areefficientandscalablebysearchingthepotentialfaults
instrumentationonsourcecode.Sinceservicesareusuallyim- withruntimeinformation.LDFI-Netflix[13]explorestheinjec-
plementedindifferentprogramminglanguages,userscouldnot tionspaceusingthebasicLDFIwhileIntelliFT[38]optimizes
afford to add additional code to the source code appropriately LDFI by pruning exploration space with heuristics rules and
withoutanypriorknowledge,hinderingthewidespreadadoption prioritizingfaultswithintegrationtesttechnique.Theobjective
ofthesetools.Toaddresstheissue,3MileBeach[35]supports ofIntelliFTissimilartoMicroFI,buttheexecutionofIntelliFT
request-levelfaultinjectionbyinterposingatthemessageseri- wouldbeslowandhardtoconvergeifthequantityofapplication
alizationlibrary.Whilethisapproachavoidstheneedforappli- functionsislarge.Further,itsprioritizationrequiresknowledge
cation code instrumentation in some cases (e.g. Java, Python), encodedheuristicsruleswhileMicroFIautomaticallyprioritizes
applications implemented in certain languages (e.g., Go) may faultswithruntimeinformation.
stillrequirecodemodificationtosupportrequest-levelinjection.
Moreover, 3MileBeach requires modifications to the message
III. BACKGROUNDANDMOTIVATION
serializationlibraryfordifferentlanguages,whichcanbecostly
andtime-consuming.Sinceexistingrequest-levelinjectiontools A. Background
conduct modifications to the application code, they require a 1) Preliminaries: ServiceMesh[3]:Asthetransitionfroma
restartoftheapplication,leadingtoaperiodofserviceunavail- monolithicapplicationtoamicroserviceapplicationcanresult
ability unavoidably. In production, such service unavailability in increased maintenance cost, service mesh has been widely
isnotacceptableasitwouldcauseuserexperienceviolation.In adopted to facilitate the development and orchestration of mi-
contrast,MicroFIsupportsnon-intrusiverequest-levelinjection croservice applications [39]. Specifically, the popular cloud
whichlimitstheblastradiustothetargetrequestwithoutrequir- providers (e.g., Alibaba [40], Tencent [41], Google [42], etc)
inganyinstrumentationandwithoutrestartingtheapplication. haveprovidedtheirservicemeshplatformstotheircustomers.
Thesimplicityandeffectiveness ofnon-intrusiverequest-level Service mesh serves as a networking infrastructure that en-
injectionmakeMicroFIapplicabletovariousapplications. ables inter-service communication, offering a transparent and
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on November 13,2025 at 00:55:27 UTC from IEEE Xplore. Restrictions apply.

4924 IEEETRANSACTIONSONDEPENDABLEANDSECURECOMPUTING,VOL.21,NO.5,SEPTEMBER/OCTOBER2024
setofdistinctcallpathsandeachpathcorrespondstoanalterna-
tivecomputationthatcanservetherequest.Moreover,MicroFI
utilizesthepropagationmechanismoftracingtopropagatethe
requesttokenforimplementingrequest-levelfaultinjection.
CNFformula[47]:AConjunctiveNormalForm(CNF)for-
mula is a Boolean formula that is a disjunction of clauses.
A clause is a conjunction of literals and a literal is either a
propositionalvariableorthenegationofapropositionalvariable.
ACNFformularepresentsalogicalpropositionthatcanbeeither
Fig.2. Traceexamplewithfourspansanditscallgraphinonerequest. True or False, depending on the assignment of truth values to
itsvariables.AllclausesinaCNFformulamustbesatisfiedfor
theoverallCNFformulatobeTrue.
language-agnosticmeansfordynamicallyconfiguringnetwork- SATSolving[48]:TheBooleanSatisfiabilityProblem(SAT)
ing and security functions. Typically, service mesh is imple- isadecisionproblemthataskswhetheragivenlogicalformula,
mentedastwolayers,acontrolplaneresponsibleformanaging represented in Conjunctive Normal Form, can be satisfied by
the configuration and behavior of the mesh, and a data plane atruthassignmentofitsvariables.GivenaCNFformulaF =
implementedasanetworkproxy(e.g.Envoy[43])deployedas f1 ∧···∧fn,theSATproblemanswerswhetherthereexistsa
asidecaralongsideeachserviceinstance.Alltheinboundand solutionsuchthattheformulaequalstoTrue.ASATsolveris
outboundtrafficforeachserviceinstancemustfirstpassthrough atoolthatcanbeusedtodeterminethesatisfiabilityofagiven
itsproxy,whichhandlestaskssuchasrouting,loadbalancing, CNFformula.Ifasatisfyingtruthassignmentexists,thesolver
healthchecking,faultinjection.AsshowninFig.1,eachservice canfindoneormoresuchassignments.
instanceisdeployedwithaproxythathandlesallrequestswithin Specifically, the failure of any node within the call path
thesystem,makingitsimpletoconductfaultinjectiontoimpact invalidates the whole path. Therefore, in the context of this
inter-serviceinvocations. research,thecallpathisencodedintoaclauseandsolutionsthat
Inthisresearch,MicroFIutilizestheservicemeshframework, satisfytheclausecaneffectivelyinvalidatethepath.Ifallpathsin
Istio[25],toinjectfaultstoaffectnetworkinteractionsbetween acallgrapharedestroyed(i.e.,allclausesinF becomesTrue),
services.Actually,MicroFIisnottightlydependentonIstio,it the request can not be served and a failure occurs. Therefore,
canalsobeappliedtootherframeworks. identifyingafailurescenariocorrespondstofindingasolution
Tracing [44]: End-to-end distributed tracing is a valuable totheCNFformulaF.
tool for profiling and understanding the execution of requests Davis-Putnam-Logemann-Loveland algorithm [49]: DPLL
inmicroservicesystems.Atracedepictstheexecutionprocess is a well-known method for determining the satisfiability and
of a request through services, which can be represented as a calculating the solutions of the CNF formula. The algorithm
call path of the request. As shown in Fig. 2, a trace consists is the pillar of most modern SAT solvers (e.g. Z3 Solver [50],
of a set of spans (colored blocks in Fig. 2) organized in a tree MiniSAT[51]).Duetoitsabilitytoquicklydeducethevalues
structureandeachspanrepresentsaremoteserviceinvocation.A ofcertainvariables,itcansignificantlyreducethesearchspace
tracedenotesasT =(s1,s2,...,sn ),wheresidenotesthespan. andimprovetheoverallperformanceofthesolver.Specifically,
EachtracehasauniquetraceIDwhileeachspanhasaunique given a CNF formula F =f1 ∧···∧fn, DPLL aims to find
spanIDandrecordsthecontextofeachserviceinvocation.The a truth assignment of the variables in F such that the formula
trace context includes trace ID, span ID, parent ID and any evaluatestoTrue,ortoconcludethatnosuchassignmentexists.
user-specific key-value pairs such as the service name and in- DPLLrunsiterativelybysimplifyingtheformulaandmaking
vokedAPIs.Thepropagationmechanismsupportscorrelating decisions about the truth values of its variables through the
events across services. The context is bundled and propagated adoption of three rules, namely unit propagation, pure literal
acrossservices,oftenviaHTTPprotocol.Specifically,thereare elimination,andsplitting.Unitpropagationstatesthatifaclause
twopopulartracingstandards,namelyOpenTelemetry[45]and containsasingleliteral,theliteralvaluecanbedirectlydeduced.
OpenTracing[46].ThetracecontextofOpenTelemetrycontains Pure literal elimination states that if a literal appears in the
Traceparent (Tp) and Tracestate (Ts). Traceparent identifies formulabutitsnegationdoesnot,thevalueofthatliteralcanbe
the incoming request and consists of version (v), trace-id (t), deducedandclausesthatcontainthatliteralcanbeeliminated.
parent-id (p), and trace-flag (f). Tracestate provides additional Iftherearenoliteralsthatcanbededucedusingtheaboverules,
vendor-specific trace information. The trace context of Open- thesplittingrulewouldchoosealiteralandsplittheformulainto
TracingcontainsBaggagewhichisakey-valuepairthatcould two branches. The first branch assumes that the literal is True
recorduser-specificinformation.Withthetracinglogic,Trace- and the other branch assumes that it is False. DPLL will then
parentandTracestateofOpenTelemetryaswellasBaggageof solveeachbranchseparatelyandcombinetheresultsfinally.
OpenTracing are injected into requests as request headers and 2) ProblemStatement: Afterintroducingseveralpreliminar-
implicitlypropagatedacrossservices. ies,theproblemstatementisformulatedasfollows.
In this research, MicroFI utilizes the collected trace data to Different application functions have different types
constructtheAPIcallgraphforeachrequest,whichisthenused of requests. Given AF ={af1,af2,...,afn } and
tocalculatetheinjectionsolutions.TheAPIcallgraphcontainsa R={r1,r2,...,rn }, we use afi to denote an application
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on November 13,2025 at 00:55:27 UTC from IEEE Xplore. Restrictions apply.

CHENetal.:MICROFI:NON-INTRUSIVEANDPRIORITIZEDREQUEST-LEVELFAULTINJECTIONFORMICROSERVICEAPPLICATIONS 4925
| function     | and ri      | to denote | the           | corresponding  |        | type              | of request. |     |     |     |     |     |     |
| ------------ | ----------- | --------- | ------------- | -------------- | ------ | ----------------- | ----------- | --- | --- | --- | --- | --- | --- |
| By analyzing | the         | trace     | of the        | request        | r      | ∈R, we            | can obtain  |     |     |     |     |     |     |
| a complete   | execution   |           | process       | and            | the    | corresponding     | API         |     |     |     |     |     |     |
| call graph   | G=(X,E),    |           | which         | contains       | one    | call path.        | x∈X         |     |     |     |     |     |     |
| denotes      | the invoked |           | API extracted |                | from   | the corresponding |             |     |     |     |     |     |     |
| span and     | e∈E         | denotes   | the           | call relation. |        | Given the         | call graph  |     |     |     |     |     |     |
| G=(X,E)      | for         | one type  | of            | request        | r, the | nodes             | x∈X can     |     |     |     |     |     |     |
x(cid:4).
be represented as different literals We represent the call Fig.3. OverviewofMicroFI.
| path in | the graph | using | a clause, |     | which | can be | constructed |     |     |     |     |     |     |
| ------- | --------- | ----- | --------- | --- | ----- | ------ | ----------- | --- | --- | --- | --- | --- | --- |
x(cid:4).
| with a conjunction |     | of  | all literals |     | The | clause is | denoted as |     |     |     |     |     |     |
| ------------------ | --- | --- | ------------ | --- | --- | --------- | ---------- | --- | --- | --- | --- | --- | --- |
=x(cid:4) ∨x(cid:4) ∨···∨x(cid:4) which defines the number of times the application is allowed
| f   |     |     | .Ifthere | existadditional |     | callpaths | for |     |     |     |     |     |     |
| --- | --- | --- | -------- | --------------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
1 2 n to fail. Therefore, given the limited resources and time, it is
rsuchasg(cid:4),thecorrespondingclausef(cid:4)canbecombinedwith
essentialtoprioritizehigh-impactfaults.Moreover,newappli-
| f using                     | the logical | “and” | relation. |     | The final | CNF           | formula for |                  |     |                 |          |     |                 |
| --------------------------- | ----------- | ----- | --------- | --- | --------- | ------------- | ----------- | ---------------- | --- | --------------- | -------- | --- | --------------- |
|                             |             |       |           |     |           |               |             | cation functions |     | are continually | deployed | or  | updated to meet |
| thecallgraphofrisdenotedasF |             |       |           | =f1 | ∧f2       | ∧···∧fn,where |             |                  |     |                 |          |     |                 |
f1,...,fn representtheclausesforthecallpathsg1,...,gn. thebusinessanduserdemands.Thus,thescaleandcomplexity
|       |              |     |     |         |     |          |             | of the applications |     | are changed            | dynamically. |                | The complexity |
| ----- | ------------ | --- | --- | ------- | --- | -------- | ----------- | ------------------- | --- | ---------------------- | ------------ | -------------- | -------------- |
| After | constructing | the | CNF | formula | F   | for each | type of re- |                     |     |                        |              |                |                |
|       |              |     |     |         |     |          |             | and dynamics        |     | impede knowledge-based |              | prioritization | because        |
quest,theobjectiveoftheproblemistoefficientlyfindinjection
∈BF experts need to constantly encode their knowledge into rules
| solutionsP | foreachapplicationfunctionbf |     |     |     |     |     | bysolving |          |            |             |     |          |              |
| ---------- | ---------------------------- | --- | --- | --- | --- | --- | --------- | -------- | ---------- | ----------- | --- | -------- | ------------ |
|            |                              |     |     |     |     |     |           | whenever | a function | is deployed | or  | updated. | Thus, we are |
Fandprioritizethesolutions.Thesetofallsolutionsforagiven
formulaF isdenotedasP =[p1,...,pk ],whereeachsolution motivatedtoautomaticallyprioritizeinjectionsolutionsduring
=[x(cid:4) ,...,x(cid:4) ] faultspaceexplorationbasedonruntimeinformation.
| pi  |     | represents |     | a truth | assignment | in  | which the |     |     |     |     |     |     |
| --- | --- | ---------- | --- | ------- | ---------- | --- | --------- | --- | --- | --- | --- | --- | --- |
| i   |     | j          |     |         |            |     |           |     |     |     |     |     |     |
variablesinpiareassignedtoTrueandtheremainingvariables
| areassignedtoFalse. |     |     |     |     |     |     |     |     |     | IV. SYSTEMDESIGN |     |     |     |
| ------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | --- | --- |
A. MicroFIOverview
B. Motivations
|     |     |     |     |     |     |     |     | Fig. 3 | provides | an overview | of  | MicroFI. | For each target |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | -------- | ----------- | --- | -------- | --------------- |
Motivation#1.Unexpectedimpactscausedbyfaultswithan requesttype(e.g.,Req1,Req2inFig.3),usersneedtowritea
uncontrolledblastradiushindertheadoptionofchaosengineer- recipe,whichconfiguresthefaulttypetoinjectandthetypeofre-
inginproduction:Arecentstudy[18]hasreportedthatonly30% questtoaffect.Initially,withtherecipe,Coordinator(markedas
| ofchaosexperimentswereperformedinproductionenvironment |     |     |     |     |     |     |     | (cid:6) |     |     |     |     |     |
| ------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- |
1 )firsttranslatesitintothefailurescenario—thecombination
whileotherswereperformedindevelopmentorstagingenviron- ofthetypeofinjectedfaultandthetargetrequesttotest.Thenit
ments. However, testing in the last two environments without sendsattributesofthetargetrequesttoRequestMarker(marked
(cid:6)
productionworkloadisinsufficienttofinddefectsinresiliency as 2 ).Sincetherearetwotypesofrequestsfortesting,Coor-
mechanisms.Oneoftheinhibitorstoperformchaosexperiments dinatorbootstrapstwocorrespondingInjectionRecommenders
in production is that some unexpected faults might happen. (marked as (cid:6) ) which automatically and parallelly calculate
3
Moreover,itisinevitablefortheapplicationtoexperiencepartial hypothesesfortargetrequests.Whilerequestsaregeneratedby
failure [52], where only some of its functions are broken. It theclient,theserequestswillbeinterceptedbyRequestMarker
| could be | precisely | simulated |     | by failing |     | the specific | type of |             |        |                 |     |                |             |
| -------- | --------- | --------- | --- | ---------- | --- | ------------ | ------- | ----------- | ------ | --------------- | --- | -------------- | ----------- |
|          |           |           |     |            |     |              |         | before they | invoke | user functions, |     | which utilizes | the tracing |
requestscorrespondingtothetargetapplicationfunction.Prior technique to mark the target request. Subsequently, Injection
tools either demand code instrumentation or cannot precisely Recommender retrieves tracing data of the target request to
simulatepartialfailurebecauseoftheincapabilityoflimitingthe calculateandprioritizetheinjectionhypotheses.Thesehypothe-
blastradiustothespecificrequests.Therefore,wearemotivated ses are then utilized by Injection Executor (marked as (cid:6) 5 ) to
todesignnon-intrusiverequest-levelfaultinjectiontolimitthe
constructserviceroutingrulesforrequest-levelfaultinjection.
blastradiustothespecifiedrequests. Afterinjection,InjectionRecommendercheckstheobservation
Motivation#2.Testingdifferentfunctionsencountersredun- data to determine whether the injected fault fails the target
dant injection calculations, causing the testing to be time- request. During parallel calculation, fault injection results are
(cid:6)
consuming:Microserviceapplicationsimplementvariousappli- recordedintoHistoricalInjectionResults(markedas 4 ),and
cationfunctionsusingdifferentlogicandinternalserviceinvo-
theyaresharedbyalltheInjectionRecommenderstoaccelerate
cations.However,somefunctionsmultiplexsameservicesand thesubsequentcalculation.Finally,failuresolutions(markedas
APIstoimplementdifferentoperations.Duringone-by-oneex- (cid:6) )foreachtargetrequestaresortedandsenttousers.
6
plorationfortestingmultiplefunctions,theexistingexploration
methodsneverutilizehistoricalinjectionresultstoalleviatethe
B. FaultModel
repetitiveinjectionsandcalculationsforthesubsequentapplica-
tionfunctionstesting.Therefore,wearemotivatedtousehistor- In a microservice application, services need to cooperate
icalresultstoprunethefaultspaceintestingdifferentfunctions. to process user requests. The cooperation is achieved through
Motivation#3.Complexandversatileapplicationshinderthe invocations between services, which is implemented with
fault prioritization: In practice, software reliability engineers communication protocols like Restful API [54] and Remote
(i.e.,SREs)usuallysetanerrorbudget[53]foreachapplication, ProcedureCalls(i.e.,RPCs)[55].Theresponsetoanindividual
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on November 13,2025 at 00:55:27 UTC from IEEE Xplore.  Restrictions apply.

4926 IEEETRANSACTIONSONDEPENDABLEANDSECURECOMPUTING,VOL.21,NO.5,SEPTEMBER/OCTOBER2024
Fig.4. Executionprocessofrequestmarking(tracecreation&tokenpropagation)&requestfailing.
TABLEIII weinject two differentfaults (i.e.,Delay and Abort) to fail
RESPONSETIMEOFREQUESTSTOTHEPRODUCTCATALOGSERVICEINHIPSTER
inter-serviceinvocationsbyleveragingservicemesh.
SHOPUNDERTWOCONDITIONS
C. Non-IntrusiveRequest-LevelInjection
As Motivation #1 highlights that the injected faults with
an uncontrolled blast radius always cause unexpected impacts
to the microservice application. Consequently, MicroFI aims
user request is a composition of responses from separate to mitigate this issue by controlling the impact of injected
invocationstodifferentservices. faultonthetargetrequestwithoutcausinganyimpacttoother
TableIIIpresentstheresponsetimeofrequestssenttothePro- business functions. The fault injection mechanism is designed
ductCatalogserviceintheHipsterShopundertwoconditions. with Request Marker (Section IV-C2) and Injection Executor
Allservicesintheapplicationaredeployedwithoneinstance. (SectionIV-C3).RequestMarkermarksrequeststhroughtrace
The response time is calculated as the duration between the creationandtokenpropagation,presentedinFig.4(a)and(b).
momentaclientsendarequesttotheProductCatalogserviceand Injection Executor injects faults by failing target invocations
themomentitreceivesaresponsefromit.So,inthisexperiment, betweenservices,presentedinFig.4(c).
theapplicationwasdeployedwithIstioanditsobservabilityfor 1) Challenge of Non-Intrusive Request-Level Injection: To
application performance was utilized to measure the response ensure the injected fault only affects the specified function,
time. During the experiment, a bunch of requests belonging it is crucial to mark the request invoking the function and its
tothesametype(i.e.,http://hs-url/product/*)andinvokingthe subsequentAPIinvocationsservingthefunction.
same API of the ProductCatalog were uniformly generated. It MicroFImarksanindividualrequestanditssubsequentAPI
ensures that the requests invoke the same business function, invocations by adding a token to the request and propagating
thereby eliminating any interference caused by variations in italongwiththeAPIinvocations.However,ensuringthetoken
functionlogicthatmayimpactthemeasurement.Underanormal propagation across services during the subsequent invocations
condition, we measured the response time of the request and isnon-trivial.Astraightforwardsolutionistomanuallyaddthe
obtainnormalresponsetime.Underanabnormalcondition,we tokenpropagationcodesintheapplicationcodes.However,the
injected4typesoffaultsintotheinstanceoftheProductCatalog methodnecessitatesappropriateapplicationcodesmodification,
showninTableIII,andmeasuredtheircorrespondingresponse which can be inefficient. Alibaba(cid:2) proposes an non-intrusive
timeduringinjection.Indetails,weutilizedChaosBlade[27]to solutionbyleveragingtracing.Specifically,Alibabaestablishes
inject CPU exhaustion, memory exhaustion, and crash faults a mapping table that correlates the trace ID of the marked
respectively. The CPU exhaustion fault occupied 50% CPU request with the corresponding added token [57]. Then, with
resourceswithintheservice,thememoryexhaustionfaultoccu- servicemesh,theproxyofeachserviceinstanceverifieswhether
pied50%memoryresourcesandthecrashfaultsuspendedthe the trace ID of each incoming request exists in the table. If it
service. Additionally, Strace [56] was used to inject 2-second does,theproxyaddsthetokentotheoutcomingrequestheader.
delaytosystemcalls(i.e.,sys_readandsys_write). Althoughthismethodsupportsnon-intrusivetokenpropagation,
Ithasbeenobservedthatinjectingfaultsintotheserviceoften thetablequeryoperationforeachrequestintroducesadditional
leadstoanincreaseinresponsetimeandtheinvocationmaybe computationoverhead.
abortedinsomecases.Thisbehaviorcanbeattributedtothefact 2) Process of Non-Intrusive Request Marking: To address
that these faults consume computational resources within the thischallenge,weleveragethepropagationmechanismoftrace
serviceorprolongtheexecutiontimeofessentialsystemcalls context, which has been introduced in Section III-A1. In this
(e.g., sys_read, sys_write), hindering the service to efficiently study,weuseOpenTelemetrytointroduceourmethod.Fig.4(a)
handleincomingrequests.Moreover,theinjectionofthesefaults and (b) show the details of how Request Marker marks the
alwayshasvaryingimpactontherequests.Thus,asthesefaults requestandpropagatesthetokenthroughthetracingmechanism.
ultimately impact inter-service invocations, we simulate them Trace creation: The first step is to mark the target request
and emulate the desired failure effects by manipulating the bycreatingthetracefortherequestandaddthetokenintothe
networkinteractionsbetweenservices.Therefore,inthisstudy, trace context. As shown in Fig. 4(a), before the target request
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on November 13,2025 at 00:55:27 UTC from IEEE Xplore. Restrictions apply.

CHENetal.:MICROFI:NON-INTRUSIVEANDPRIORITIZEDREQUEST-LEVELFAULTINJECTIONFORMICROSERVICEAPPLICATIONS 4927
Algorithm1:FailureSolutionsRecommendation.
Fig.5. ExampleofAlgorithm1.
|     |     |     |     |     |     |     |     | of fault locations) |     | is huge, | making | it challenging |     | to  | determine |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------- | --- | -------- | ------ | -------------- | --- | --- | --------- |
whichAPIsMicroFIshouldtargetfirstintestingtheapplication.
|     |     |     |     |     |     |     |     | To address     | this | issue,     | MicroFI | introduces | the          | fault | injection |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | ---- | ---------- | ------- | ---------- | ------------ | ----- | --------- |
|     |     |     |     |     |     |     |     | recommendation |      | algorithm, |         | depicted   | in Algorithm |       | 1, which  |
helpstoovercomethisproblem.
R,
|     |     |     |     |     |     |     |     | For a                      | target type | of  | request | Injection                     | Recommender |     | first |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------------- | ----------- | --- | ------- | ----------------------------- | ----------- | --- | ----- |
|     |     |     |     |     |     |     |     | collectstracedataδforRandT |             |     |         | forallrequests(line6).Withthe |             |     |       |
tracedata,thealgorithmconsistsoffoursteps:i)Byanalyzing
|     |     |     |     |     |     |     |     | thecallpathrecordedbyδ,theclausef |     |     |     |     | isobtainedandtheCNF |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------------------------- | --- | --- | --- | --- | ------------------- | --- | --- |
F forRisupdated(line7).Thedetailsoftracecollectionare
providedinSectionIV-D1.ii)BypassingF
intoanSATsolver,
|     |     |     |     |     |     |     |     | a set of | minimal | candidate | hypotheses |     | can be | generated | (line |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------- | --------- | ---------- | --- | ------ | --------- | ----- |
flowsintotheapplicationandinvokesanapplicationfunction,
|           |        |       |      |       |          |     |             | 8), as described |     | in Section | IV-D2. | Specifically, |     | the | hypothesis |
| --------- | ------ | ----- | ---- | ----- | -------- | --- | ----------- | ---------------- | --- | ---------- | ------ | ------------- | --- | --- | ---------- |
| a Request | Marker | agent | will | start | to trace | the | request and |                  |     |            |        |               |     |     |            |
istheminimalinjectionsolutiononlywhenithastheabilityto
| add a token, | a   | key-value | pair | (“T=/indexJason”), |     |     | to the |     |     |     |     |     |     |     |     |
| ------------ | --- | --------- | ---- | ------------------ | --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
causethetargetrequesttofail,whileanysubsetofitisnotable
Tracestate.Then,theagentforwardsthemarkedrequesttothe
tofailtherequest.Then,anyhypothesesthathavealreadybeen
application.Theaddedkey-valuepairispassedacrossservices
recordedinHistoricalInjectionResultsHareremoved(line9–
asarequestheader.
10).Theprocessofeliminatingredundanthypothesesisdepicted
| Token | propagation: |     | Since | the | trace context | is  | propagated |                      |     |     |                                    |     |     |     |     |
| ----- | ------------ | --- | ----- | --- | ------------- | --- | ---------- | -------------------- | --- | --- | ---------------------------------- | --- | --- | --- | --- |
|       |              |     |       |     |               |     |            | inSectionIV-D3.iii)T |     |     | isusedtoupdatetheimportancescoresS |     |     |     |     |
acrossservicesautomatically,MicroFIutilizesthetracingtech-
ofAPIsusingAPIRank.WithS,candidateinjectionhypotheses
niquetoimplementthepropagationofthegeneratedtokenacross
τarerankedandthehighest-impacthypothesisφisselected(line
| services. | Unlike    | the method |     | used | by Alibaba,     | we  | embed the |         |                    |     |         |          |     |         |        |
| --------- | --------- | ---------- | --- | ---- | --------------- | --- | --------- | ------- | ------------------ | --- | ------- | -------- | --- | ------- | ------ |
|           |           |            |     |      |                 |     |           | 11–12). | The prioritization |     | process | is shown | in  | Section | IV-D4. |
| token in  | the trace | context    | and | use  | the propagation |     | mechanism |         |                    |     |         |          |     |         |        |
iv)Afaultisinjectedbasedonφ,andtheapplicationisobserved
| to propagate | the | token | without | creating |     | the table. | As shown |     |     |     |     |     |     |     |     |
| ------------ | --- | ----- | ------- | -------- | --- | ---------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
todecidewhethertheinjectedfaultcausestherequesttofail,as
| in Fig. | 4(b), we | embed | the | token | into the | field | “Tracestate” |     |     |     |     |     |     |     |     |
| ------- | -------- | ----- | --- | ----- | -------- | ----- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
introducedinSectionIV-D5.Iftherequestfails,φiswrittentoH
andleverageittoconveythetoken.Whentheserviceinstance andrecordedinFinalInjectionSolutionsΣ(line13–16).These
| receives | the incoming |     | request, | the | trace | context | is implicitly |                                       |     |     |     |     |                       |     |     |
| -------- | ------------ | --- | -------- | --- | ----- | ------- | ------------- | ------------------------------------- | --- | --- | --- | --- | --------------------- | --- | --- |
|          |              |     |          |     |       |         |               | processes(line6–15)continuesuntilallτ |     |     |     |     | isempty.Specifically, |     |     |
propagatedtotheoutcomingrequestthroughtracecontextprop-
itisnecessarytoupdateHiftheimplementationlogicofatested
agationmechanism. API(§)isupdated.Duringupdating,thesolutionsinHwhich
| 3) ProcessofRequestFailing: |     |     |     | Combiningtheaddedheader, |     |     |     |     |     |     |     |     |     |     |     |
| --------------------------- | --- | --- | --- | ------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
arerelatedto§shouldberemovedfromH.
| the fault | injection | solution |     | computed | from | Injection | Recom- |        |             |     |              |     |         |              |     |
| --------- | --------- | -------- | --- | -------- | ---- | --------- | ------ | ------ | ----------- | --- | ------------ | --- | ------- | ------------ | --- |
|           |           |          |     |          |      |           |        | Before | introducing |     | the details, | an  | example | of Algorithm | 1   |
mender,andthetypeofinjectedfault,InjectionExecutorcon-
|     |     |     |     |     |     |     |     | is illustrated. | Fig. | 5 shows | two | types | of requests |     | (Req1 and |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | ---- | ------- | --- | ----- | ----------- | --- | --------- |
structsaserviceroutingrule(e.g.,theruleinFig.8(c)).Then,
Req2)anddepictstheprocessofcalculatingoneofthesolutions
InjectionExecutorsendstheruletotheproxyofthetargetservice {Rec.LsR,Rec.DefR}).
|     |     |     |     |     |     |     |     | for failing | Req1 | (i.e., |     |     |     | Note | that, this |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ---- | ------ | --- | --- | --- | ---- | ---------- |
instance.
processisfollowedbytheprocessofobtainingthefirstsolution
| Theruleofeachserviceinstance’sproxyinstructstheproxy |     |     |     |     |     |     |     | {Frt.Index}, |     |       |                |     |           |            |     |
| ---------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ----- | -------------- | --- | --------- | ---------- | --- |
|                                                      |     |     |     |     |     |     |     |              |     | which | is prioritized | as  | the first | hypothesis | and |
to inspect invocation messages between services and perform (cid:6)
|     |     |     |     |     |     |     |     | evaluatedasthefirstinjectionsolution. |     |     |     |     | 1 showsthefailure-free |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------- | --- | --- | --- | --- | ---------------------- | --- | --- |
injectionactionsifamessagematchesthespecifiedcriteria.As
|     |     |     |     |     |     |     |     | API-level | service | call | path of | Req1. It | can be | converted | into a |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------- | ---- | ------- | -------- | ------ | --------- | ------ |
Fig.4(c)shows,theruleofAdescribesthatAshouldnormally formulawhichonlycontainsoneclause:Frt.Index∨Rec.LsR∨
| forward | all the      | requests | that     | pass to | A. Therefore, |     | the marked |           |                                                   |     |     |     |     |     |     |
| ------- | ------------ | -------- | -------- | ------- | ------------- | --- | ---------- | --------- | ------------------------------------------------- | --- | --- | --- | --- | --- | --- |
|         |              |          |          |         |               |     |            | Prod.LsP( | (cid:6) 2 ).Then,theformulaisfedintoanSATsolverto |     |     |     |     |     |     |
| request | is forwarded |          | normally | by      | A. However,   | the | rule of    | B         |                                                   |     |     |     |     |     |     |
generateasetofminimalhypotheses,eachofwhichrepresents
| describes | that | B should | abort | the | request | that has | a header, |     |     |     |     |     |     |     |     |
| --------- | ---- | -------- | ----- | --- | ------- | -------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
faultpointsthatshouldbetestedviafaultinjection.Basedonthe
| “T=/indexJason”. |     |     | Therefore, |     | B aborts | the forwarding | of  |                                      |     |     |     |     |                           |     |     |
| ---------------- | --- | --- | ---------- | --- | -------- | -------------- | --- | ------------------------------------ | --- | --- | --- | --- | ------------------------- | --- | --- |
|                  |     |     |            |     |          |                |     | currentformula,theminimalhypotheses( |     |     |     |     | (cid:6) )are:{Frt.Index}, |     |     |
3
themarkedrequest. {Rec.LsR}and{Prod.LsP}.Notethat,sincewehavevalidated
|                                     |     |     |     |     |     |     |     | that Frt.Index |             | is an injection |     | solution,  | we eliminate |       | the hy-  |
| ----------------------------------- | --- | --- | --- | --- | --- | --- | --- | -------------- | ----------- | --------------- | --- | ---------- | ------------ | ----- | -------- |
| D. InjectionSolutionsRecommendation |     |     |     |     |     |     |     |                | {Frt.Index} |                 |     |            |              |       |          |
|                                     |     |     |     |     |     |     |     | pothesis       |             | from            | the | hypotheses | set.         | Next, | with the |
Asanapplicationmayconsistofhundredsofmicroservices, tracedatageneratedbyReq1andReq2,thescoresofAPIsare
thepotentialsolutionspaceoffaultinjection(i.e.,combinations calculated. The hypotheses are ranked ( (cid:6) ) according to the
4
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on November 13,2025 at 00:55:27 UTC from IEEE Xplore.  Restrictions apply.

4928 IEEETRANSACTIONSONDEPENDABLEANDSECURECOMPUTING,VOL.21,NO.5,SEPTEMBER/OCTOBER2024
MicroFIusestheSATsolvertocalculatesolutionstotheCNF
formula.
|     |     |     |     |     |     |     | CNF         | formula | construction: |       | Given     | the     | call        | graph       | G that   |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ------- | ------------- | ----- | --------- | ------- | ----------- | ----------- | -------- |
|     |     |     |     |     |     |     | comprises   | a set   | of call       | paths | g1,...,gn |         | for serving |             | one type |
|     |     |     |     |     |     |     | of request, | the     | corresponding |       | CNF       | formula | is          | constructed | as       |
Fig.6. Storeoperationonastoragesystem. F =f1 ∧···∧fn,wheref1,...,fnrepresenttheclausescor-
relatedwiththecallpathsg1,...,gn.
|     |     |     |     |     |     |     | Hypotheses |     | calculation: |     | Solutions | that | satisfy | the | CNF for- |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --- | ------------ | --- | --------- | ---- | ------- | --- | -------- |
scores.Then,thetop-1hypothesis({Rec.LsR})isselectedanda
|     |     |     |     |     |     |     | mula and | make | the formula |     | as True | indicate | potential |     | failures |
| --- | --- | --- | --- | --- | --- | --- | -------- | ---- | ----------- | --- | ------- | -------- | --------- | --- | -------- |
faultisinjected.Aftersendingthesametypeofrequest(Req1’),
|     |     |     |     |     |     |     | in serving | the | request. | Therefore, |     | with | the constructed |     | CNF |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --- | -------- | ---------- | --- | ---- | --------------- | --- | --- |
theapplicationstillrespondssuccessfullyandanewservicecall
formula,MicroFIcalculatesthesetofminimalhypothesesusing
(cid:6)
graphexistsas 5 .Rec.DefRprovidesanalternativecomputa- theSATsolver,whosekeyistheDPLLalgorithmthathasbeen
tionwhenRec.LsRfails.Thenewcallpathistransformedinto
|             |           |             |     |       |              |              | introduced   | in  | Section | III-A1.  | After | calculation, |     | the redundant |     |
| ----------- | --------- | ----------- | --- | ----- | ------------ | ------------ | ------------ | --- | ------- | -------- | ----- | ------------ | --- | ------------- | --- |
| the clause: | Frt.Index | ∨ Rec.DefR, |     | which | is connected | with (cid:6) |              |     |         |          |       |              |     |               |     |
|             |           |             |     |       |              |              | 2 hypotheses | are | removed | (Section |       | IV-D3)       | and | the remaining |     |
(cid:6)
to get 7 . By solving the updated formula, the obtained latest hypothesesareranked(SectionIV-D4).Faultsareinjectedbased
minimalhypothesesare:{Frt.Index},{Rec.LsR,Rec.DefR}and
ontheprioritizedhypotheses.Ifanewcallpathisdiscovered,
| {Prod.LsP} |     | (cid:6) |     |     | {Frt.Index} |     |     |     |     |     |     |     |     |     |     |
| ---------- | --- | ------- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
shown in 8 . The hypothesis is also indicating that the injected faults do not fail the request, the
eliminatedfromthehypothesesset.Withtheupdatedscores,the correspondingclauseiscombinedwithF.
hypothesesarerankedandthehypothesis{Rec.LsR,Rec.DefR}
|     |     |     |     |     |     |     | 3) EliminationofRedundantHypotheses: |     |     |     |     |     | AsMotivation#2 |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------------ | --- | --- | --- | --- | --- | -------------- | --- | --- |
isselectedwhichfinallycauses Req1tofailandregarded asa presents,therearesomeredundantsolutionsinmultipleappli-
solution.TheprocessinFig.5willcontinuetorepeatuntilall
cationfunctionstesting.Therefore,aheuristicruleisintroduced
| hypotheseshavebeenvalidated. |      |           |                             |               |       |       | tooptimizetheprocess. |            |           |         |         |          |              |     |          |
| ---------------------------- | ---- | --------- | --------------------------- | ------------- | ----- | ----- | --------------------- | ---------- | --------- | ------- | ------- | -------- | ------------ | --- | -------- |
| 1) CallGraphConstruction:    |      |           | InjectionRecommenderfirstly |               |       |       |                       |            |           |         |         |          |              |     |          |
|                              |      |           |                             |               |       |       | When                  | multiple   | functions |         | invoke  | the same | API          | of  | the same |
| collects trace               | data | generated | from                        | all requests. | Then, | among |                       |            |           |         |         |          |              |     |          |
|                              |      |           |                             |               |       |       | service,              | the result | of        | testing | the API | in       | the previous |     | function |
R
the full trace data, trace data of are filtered based on the testing is used to prune the searching space of the subsequent
propagatedtokenaddedintherequestheader.Withtheaggre-
|     |     |     |     |     |     |     | function | testing. | In  | subsequent | function |     | testing, | retesting | the |
| --- | --- | --- | --- | --- | --- | --- | -------- | -------- | --- | ---------- | -------- | --- | -------- | --------- | --- |
gationofthefilteredtracedata,thecorrespondingcallgraphis
|     |     |     |     |     |     |     | same API | is unnecessary |     | and | the | previous | result | can | be used |
| --- | --- | --- | --- | --- | --- | --- | -------- | -------------- | --- | --- | --- | -------- | ------ | --- | ------- |
extracted.
|        |         |           |            |     |              |     | as the solution. |       | The    | principle | behind | this   | rule | is that | the fault |
| ------ | ------- | --------- | ---------- | --- | ------------ | --- | ---------------- | ----- | ------ | --------- | ------ | ------ | ---- | ------- | --------- |
| 2) The | Minimal | Candidate | Hypotheses |     | Calculation: | As  |                  |       |        |           |        |        |      |         |           |
|        |         |           |            |     |              |     | handling         | logic | of the | same      | API    | is the | same | even in | distinct  |
R
Section III-A1 presents, the request can not be served and invocations. Therefore, after obtaining candidate hypotheses,
afailureoccursintheapplicationifthecorrespondingextracted
|     |     |     |     |     |     |     | Injection | Recommender |     | checks | if  | the same | hypotheses |     | exist |
| --- | --- | --- | --- | --- | --- | --- | --------- | ----------- | --- | ------ | --- | -------- | ---------- | --- | ----- |
callgraphisdestroyed.However,itisnon-trivialtofindallmin-
|                                                         |     |     |     |     |     |     | in H. If | so, the  | corresponding |     | solutions |     | of existed |              | hypothe- |
| ------------------------------------------------------- | --- | --- | --- | --- | --- | --- | -------- | -------- | ------------- | --- | --------- | --- | ---------- | ------------ | -------- |
| imalinjectionsolutionsthatcandestroythecallgraphandfail |     |     |     |     |     |     |          |          |               | H   |           |     |            |              |          |
|                                                         |     |     |     |     |     |     | ses are  | obtained | through       |     | directly  | and | will       | be validated | by       |
therequestduetoapplicationcomplexity.Onestraightforward
|     |     |     |     |     |     |     | injection. | For | example, | in  | Fig. 1, | both the | SearchProduct |     | and |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --- | -------- | --- | ------- | -------- | ------------- | --- | --- |
method is to simply traverse each call path in the graph and Checkout functions invoke the same API (/GetProduct). If the
injectfaultsateachedgetodestroythegraph.However,itisnot
testingfortheCheckoutfunctionhascalculatedthefinalsolution
efficienttogiveallminimalsolutions,especiallyinacomplex
|     |     |     |     |     |     |     | corresponding |     | to the | API | (/GetProduct), |     | then | another | testing |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ------ | --- | -------------- | --- | ---- | ------- | ------- |
application.ForacallgraphwithN nodes,theinjectionspace for the SearchProduct function should skip the calculation for
canbeaslargeas:
|     |     |     |                 |     |     |     | the API        | and | directly | validate | whether |     | the solution |     | fails the |
| --- | --- | --- | --------------- | --- | --- | --- | -------------- | --- | -------- | -------- | ------- | --- | ------------ | --- | --------- |
|     |     |     | (cid:3) (cid:4) |     |     |     | SearchProduct. |     |          |          |         |     |              |     |           |
(cid:2)
|     |     |     | N =2N |     |     |     |                   |     |     |          |           |             |     |     |          |
| --- | --- | --- | ----- | --- | --- | --- | ----------------- | --- | --- | -------- | --------- | ----------- | --- | --- | -------- |
|     |     |     |       | −1  |     |     | 4) Prioritization |     |     | of Fault | Injection | Hypotheses: |     |     | As Moti- |
k
|     |     |     |     |     |     |     | vation | #3 presents, |     | due to | the high | demand |     | for prioritizing |     |
| --- | --- | --- | --- | --- | --- | --- | ------ | ------------ | --- | ------ | -------- | ------ | --- | ---------------- | --- |
1≤k≤N
|     |     |     |     |     |     |     | high-impact | injection |     | solutions | with | a limited |     | error | budget as |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --------- | --- | --------- | ---- | --------- | --- | ----- | --------- |
For example, Fig. 6 shows a storage system with replication, well as the difficulty in manual prioritization in complex ap-
where data is stored on two replicas and the store is per- plications,InjectionRecommenderusesanenhancedPageRank
formed by two broadcasts. To fail the store operation, faults (i.e.,APIRank)toprioritizehypotheseswithhigherimpactbased
mustbesimultaneouslyinjectedintobothreplicasorintoboth onruntimeinformation.
broadcast services. It is important to note that the potential Inamicroserviceapplication,theimpactscopeislargeonce
24−1,
injection solution space of Fig. 6 is which may seem allinvocationstoanAPIfail.Thus,theproblemofcomputing
feasibletoexplore.However,astheapplicationscaleexpands, theimpactvalueforeachAPIisconvertedintocomputingthe
the exhaustive exploration becomes challenging. Moreover, importanceforeachAPI.Theevaluationfortheimportanceof
the solutions that calculates by injecting fault at each edge each API is based on two insights. i) If the API is invoked by
are not minimal. To efficiently identify all minimal solutions, moreservices,itismoreimportant.Onceafaultisinjectedinto
MicroFI employs the Boolean Satisfiability theorem. MicroFI it,allservicesdependingonitwouldbeaffected.ii)IftheAPI
firstconstructstheCNFformulaforthegeneratedcallgraphs. iscoveredbymorerequesttraces,itismoreimportant.Oncea
Then, the objective of identifying a failure scenario is con- faultisinjectedintoit,allrequestsdependingonitwouldfail.
verted into finding a solution to the generated CNF formula. Inspired by MicroRank [58], which measures the anomalous
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on November 13,2025 at 00:55:27 UTC from IEEE Xplore.  Restrictions apply.

CHENetal.:MICROFI:NON-INTRUSIVEANDPRIORITIZEDREQUEST-LEVELFAULTINJECTIONFORMICROSERVICEAPPLICATIONS 4929
| scores  | for each | service | with    | PageRank | to         | localize | faults, we |     |     |     |     |     |     |     |     |
| ------- | -------- | ------- | ------- | -------- | ---------- | -------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
| propose | APIRank  | which   | assigns | a        | importance | score    | for each   |     |     |     |     |     |     |     |     |
APIbycombiningthestaticapplicationtopologyanddynamic
requestpaths.
| Personalized |             | PageRank |         | (PPR):    | APIRank          | is          | based on |     |     |     |     |     |     |     |     |
| ------------ | ----------- | -------- | ------- | --------- | ---------------- | ----------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
| PPR          | [59], which | analyzes |         | the graph | of heterogeneous |             | nodes    |     |     |     |     |     |     |     |     |
| (i.e.,       | APIs and    | traces   | in this | study).   | Given            | an oriented | graph    |     |     |     |     |     |     |     |     |
G =(V,E),where|V|=Nrepresentsthenumberofnodesand
|E|=M representsthenumberofedges,PPRfirstlyconstructs Transitionmatrixfor(cid:6)
|     |     |     |     |     |     |     |     | Fig.7. |     |     | 5 inFig.5. |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | --- | ---------- | --- | --- | --- | --- |
atransitionmatrixA∈RN×N.ThematrixelementA
stdenotes
| theprobability |     | thatarandom |     | walk | froms | totand | itsvalue | is  |     |     |     |     |     |     |     |
| -------------- | --- | ----------- | --- | ---- | ----- | ------ | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
scoreofeachhypothesisiscalculated.Inthecaseofhypothesis
computedusingtheleftequationin(1),whereO(s)represents
withmultipleinjectionpoints,thehighestscoreamongthemis
theout-neighborofs.Withtheconstructedtransitionmatrixand
selectedasthescoreforthathypothesis.Withthescoresofthe
agivenpreferencevectoru,thePPRequationcanbesolvedas
candidatehypotheses,InjectionRecommenderrankshypotheses
v =c·Av+(1−c)·u,wherecisthedampingfactorranging
andrecommendsthehypothesiswiththehighestscore.
| from0to1andvisthePersonalizedPageRankvector(PPV)for |     |     |     |     |     |     |     |            | (cid:6) |      |        |     |            |     |            |
| --------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------- | ---- | ------ | --- | ---------- | --- | ---------- |
|                                                     |     |     |     |     |     |     |     | We utilize |         | 5 in | Fig. 5 | as  | an example | to  | illustrate |
u.Thesolutiontothisequationcanbeapproximatedthroughan
|     |     |     |     |     |     |     |     | the prioritization: |     | Candidate |     | hypotheses |     | are {Frt.Index}, |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------- | --- | --------- | --- | ---------- | --- | ---------------- | --- |
iterativealgorithm.Theq-thiterationisshownas(2).Thefinal {Rec.LsR,Rec.DefR} {Prod.LsP}.
|     |     |     |     |     |     |     |     |     |     |     | and |     | Fig. | 7 displays | the |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | ---------- | --- |
solutioncorrespondstoscoresofallnodes.
|     |         |         |         |     |         |     |         | call graph       | and | the API-trace |            | graph, | which | are     | the basis |
| --- | ------- | ------- | ------- | --- | ------- | --- | ------- | ---------------- | --- | ------------- | ---------- | ------ | ----- | ------- | --------- |
|     | (cid:5) |         |         |     | (cid:6) |     | (cid:7) |                  |     |               |            |        |       |         |           |
|     |         |         |         |     |         |     |         | for constructing |     | the           | transition | matrix | A     | in Fig. | 7. Since  |
|     |         | 1 ,     | ∃t∈O(s) |     | A       |     | A       |                  |     |               |            |        |       |         |           |
| A   | =       | |O (s)| |         | ;   | A=      | a a | at      |                  |     |               |            |        |       |         |           |
st A 0 (1) t h e re a r e 3 d ist i n c t k i n d s o f t ra ce s a n d e ac h k i nd o n ly h as
|     |     | 0 , | otherwise     |     |     | ta  |     |              |           |            |           |           |           |         |                 |
| --- | --- | --- | ------------- | --- | --- | --- | --- | ------------ | --------- | ---------- | --------- | --------- | --------- | ------- | --------------- |
|     |     |     |               |     |     |     |     | o n e tr a c | e, th e p | r e f er e | n c e v e | ct o r fo | r t r ace | s u i s | [1 , 1 , 1 ]T . |
|     |     |     |               |     |     |     |     |              |           |            |           |           |           | t       | 3 3 3           |
|     |     | (q) | (q−1)+(1−c)·u |     |     |     |     |              |           |            |           |           |           |         |                 |
v =c·Av (2) Combined with the preference vector for APIs ua which is
|     |     |     |     |     |     |     |     |                  |                |     |        |     |                  |     | 1 1 1]. |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | -------------- | --- | ------ | --- | ---------------- | --- | ------- |
|     |     |     |     |     |     |     |     | set to (cid:5)0, | the preference |     | vector | u   | is [0,0,0,0,0,0, |     | , ,     |
|     |     |     |     |     |     |     |     |                  |                |     |        |     |                  |     | 3 3 3   |
Construction of the transition matrix in APIRank: In this Given that the number of APIs (i.e., Na) is 6 and the number
| research,APIRankusesthetransitionmatrixAtoaddressboth |     |     |     |     |     |     |     |          |           |        |     |       |             |     | v(0) |
| ----------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | -------- | --------- | ------ | --- | ----- | ----------- | --- | ---- |
|                                                       |     |     |     |     |     |     |     | of kinds | of traces | (i.e., | Nt) | is 3, | the initial | PPV | is   |
insightsmentionedabove.Thematrixispartitionedastheright [1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1]. With a 20 iteration following (2)
|          |     |         |         |                |     |           |         | 6 6 6   | 6 6 6     | 3 3   | 3         |        |     |          |          |
| -------- | --- | ------- | ------- | -------------- | --- | --------- | ------- | ------- | --------- | ----- | --------- | ------ | --- | -------- | -------- |
| equation | in  | (1). To | profile | the invocation |     | frequency | of APIs |         |           |       |           |        |     |          |          |
|          |     |         |         |                |     |           |         | where c | is set to | 0.85, | the final | scores | of  | APIs are | given as |
calledbyotherservices(tomeetinsighti)),APIRankconstructs S(Frt.GetR,Prod.GetP,Frt.Index,Rec.LsR,Rec.DefR,
A aabasedontherealtimecallgraph,generatedfromthetrace Prod.LsP)=[0.158,0.161,1,0.517,0.477,0.354]. Given
dataT.Sincethecallgraphcapturestheinvocationrelationship {Frt.Index}
|     |     |     |     |     |     |     |     | that |     | has been | previously |     | identified | as an | injection |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | -------- | ---------- | --- | ---------- | ----- | --------- |
amongAPIsfromdifferentserviceinstance,A aa profilestran- solution,itwillnotbeconsideredasfurthertesting.Therefore,
sitionsbetweenAPIs.ToprofilethecoverageofAPIsinvoked {Rec.LsR,Rec.DefR}
|     |     |     |     |     |     |     |     | the prioritized |     | hypothesis |     | is  |     |     | which |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- | ---------- | --- | --- | --- | --- | ----- |
bydifferentrequests(insightii)),APIRankconstructsA {Frt.Index}.
|     |     |     |     |     |     |     | at and | has the | highest | score | except |     |     | Then, the | selected |
| --- | --- | --- | --- | --- | --- | --- | ------ | ------- | ------- | ----- | ------ | --- | --- | --------- | -------- |
A tabasedontheAPI-tracegraph,whosenodesrepresentAPIs hypothesiswillbedeterminedwhetheritfailsthetargetrequest
andtracesrespectively.Notethattracesgeneratingthesamecall byinjection.Ifso,thehypothesisisconsideredasasolution.
pathareidentifiedasthesamekindoftrace.SincetheAPI-trace 5) Failure Effect Observation: To evaluate whether the in-
graphdescribestherelationshipbetweentracesofrequestsand jectedfaultinvalidatestargetrequests,threerulesaredesigned
|     |     |     |     |     | A   | A   |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
the corresponding invoked APIs, at and ta describe the basedontheresponse.Firstly,wecheckthestatuscodeofthe
transitionsbetweenAPIsandtraces. response.Iftherequestisrespondedwithouta200statuscode,
| Construction             |     | of preference |     | vector:                    | APIRank | constructs | the |                     |     |     |         |             |     |                  |     |
| ------------------------ | --- | ------------- | --- | -------------------------- | ------- | ---------- | --- | ------------------- | --- | --- | ------- | ----------- | --- | ---------------- | --- |
|                          |     |               |     |                            |         |            |     | it fails. Secondly, |     | we  | observe | the payload |     | of the response. | If  |
| preferencevectoruasu=[uT |     |               |     | ,uT ]T,whereuaisforAPIsand |         |            |     |                     |     |     |         |             |     |                  |     |
thepayloadcontainskeywordslikeerrorortimeout,therequest
a t
utisfortraces.SinceAPIRankhasnopreferenceforAPIs,uais fails.Thirdly,wemeasuretheresponsetimeoftherequest.Ifthe
setas(cid:5)0.Forthepreferencevectorfortraces,APIRankconsiders
responsetimeexceedsthethresholdpresetinthe“timeout-retry”
thenumberoftracesthatbelongtothesamekind.Ifaparticular mechanism,therequestfails.
typeofrequestisinvokedfrequently,thecorrespondingkindof
traces will have a larger number of occurrences and deserves E. ParallelCalculation
| moreattention.Thus,ut |     |     | issetas[θ1,θ2,...,θm |     |     | ]T  | andθi isset |                                                        |     |     |     |     |     |     |     |
| --------------------- | --- | --- | -------------------- | --- | --- | --- | ----------- | ------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- |
| n−1                   |     |     |                      |     |     |     |             | Withrequest-levelfaultinjection,theimpactofeachtesting |     |     |     |     |     |     |     |
as (cid:2) i ,wheremisthenumberofkindsoftracesandniisthe
n −1 is isolated to a single type of requests, without affecting other
j
numberoftracesbelongingtothekindoftracei.
|     |     |     |     |     |     |     |     | requests. | Therefore, | if  | multiple | types | of requests |     | need to be |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ---------- | --- | -------- | ----- | ----------- | --- | ---------- |
CalculationofeachAPI’sscoreandtherankofhypotheses: tested, a group of Injection Recommender instances can be
v(0)
After the calculation of A and u, the initial PPV is set launched simultaneously to calculate fault injection solutions
| as [v | T,v T]T. | va is set | as [ | 1 , 1 ,..., | 1 ] | where | Na denotes |                                 |     |     |     |     |     |     |     |
| ----- | -------- | --------- | ---- | ----------- | --- | ----- | ---------- | ------------------------------- | --- | --- | --- | --- | --- | --- | --- |
|       | a t      |           |      | N N         | N   |       |            | foreachtypeofrequestinparallel. |     |     |     |     |     |     |     |
|       |          |           |      | a a         | a   |       |            |                                 |     |     |     |     |     |     |     |
the number of APIs. vt is set as [ 1 , 1 ,..., 1 ] where Nt Indetails,whenmultipletypesofrequestsneedtobetested,
|     |     |     |     |     | N N | N   |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     | t t | t   |     |     |     |     |     |     |     |     |     |
denotes the number of trace kinds. The estimated importance CoordinatorfirstinitializesagroupofInjectionRecommender
scores of all APIs are obtained by iteratively solving (2) until instances, which are responsible for calculating the injection
the convergence is achieved. With the estimated scores, the solutionsforeachtypeofrequest.Then,Coordinatorgenerates
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on November 13,2025 at 00:55:27 UTC from IEEE Xplore.  Restrictions apply.

4930 IEEETRANSACTIONSONDEPENDABLEANDSECURECOMPUTING,VOL.21,NO.5,SEPTEMBER/OCTOBER2024
TABLEIV
DESCRIPTIONOFTHREEEVALUATIONAPPLICATIONS
invocationreturnswithhttpStatus.ForthetypeofDelayfault,
Fig.8. Exampleofarecipeandthecorrespondinggloballyuniquetokenand users can increase the request latency of the target invocation
serviceroutingrule. withdelayTime.
Fig.8(a)showsanexampleoftherecipe.Therecipeinstructs
aglobaluniquetokenforeachtypeoftargetrequest,whichwill MicroFI to affect requests that Jason calls whose URL are
beusedbyRequestMarkertodifferentiaterequestsandimple- “/index”. During testing, MicroFI aborts all invocations to the
ment request-level fault injection. With global unique tokens target_service_API of target_service which are
generatedfordifferenttypesofrequests,InjectionExecutorcan calculatedbyInjectionRecommender.
constructthecorrespondingrulesforfailingeachtypeofrequest
accordingly. During the calculation of injection solutions for
VI. EVALUATION
differenttypesofrequest,thefaultinjectionresultsvalidatedby
Our evaluation seeks to address the questions. RQ1: Can
Injection Recommender are recorded into Historical Injection
MicroFI precisely control the blast radius of fault injection?
results.Thishistoricalrecordsarethensharedbyallinstancesof
(SectionVI-B)RQ2:IstheoptimizationofMicroFIeffectiveto
InjectionRecommendertosupporttheeliminationofredundant
accelerateinjectionsolutionscalculation?(SectionVI-C)RQ3:
hypotheses,whichisintroducedindetailsinSectionIV-D3.
Is MicroFI helpful to expose high-impact injection solutions
throughprioritization?(SectionVI-D)RQ4:Whatistheover-
V. IMPLEMENTATION
headofMicroFIincontrollingtheblastradiusoffaultinjection?
We have implemented MicroFI based on Kubernetes [60]
(SectionVI-E)
andIstio[25],twooftheleadingmicroserviceinfrastructures.
MicroFI is implemented in Python language and chooses Z3
A. EvaluationSetup
solver [50] as theSAT solver. MicroFI has been containerized
tosupportdirectlydeployedinaKubernetescluster.Moreover, Ourprototypeisevaluatedwith3representativeopen-source
MicroFIimplementsRequestMarkerintwoversionstosupport microserviceapplicationsaspresentedinTableIV.Specifically,
injectingrequest-levelfaultintheapplicationthatutilizeseither Hotel Reservation is a relatively small-scale benchmark de-
theOpenTelemetryorOpenTracingtracingstandards. signedtosimulateanonlinesystemforbookinghotels.Hipster
Specifically,MicroFIimplementsCoordinatortotranslatea Shopisamedium-scaleapplicationthatservesasaweb-based
recipe into the failure scenario and activate a corresponding e-commerce that allows users to browse, order, and purchase
InjectionRecommenderforeachscenario.Therecipethatusers products. TrainTicket is larger and more complex, providing
need to configure contains two parts. The first part is the def- various business functions for booking railway tickets. These
inition of the target request. The functions of an application applicationsreflectthecharacteristicsofindustrialmicroservice
are always triggered by different user requests. Requests are applications [33], [34], encompassing not only their scale and
definedbydifferentrequestURLs.Moreover,therearedifferent complexity but also in their programming languages, commu-
users invoking requests to an application. The requests are nication protocols (gRPC and HTTP), and tracing standards.
distinguished by different user information in the header of Therefore,theseapplicationarerepresentativeandwidelyused
requests.Therefore,thedefinitionofthetargetrequestshouldbe as the experiment benchmarks [4], [38], [58], [61], [62], [63],
denotedwithrequestattributes,suchasitsURL,thecallerand [64].
querystringparameters.Withrequestattributestranslatedfrom Sincetherearenotimeouthandlinglogicintheseapplications,
the recipe, a globally unique token (T) for the target request weuseIstiotosettimeoutfortheseservices.Togenerateexternal
isobtainedbyconcatenatingallrequestattributestogether.For requestsandinvokecorrespondingbusinessfunctionsinappli-
example,thegloballyuniquetokenfortherecipeinFig.8(a)is cations,weutilizetheworkloadgeneratorLocust[65].Asshown
/indexJason. inFig.9,wehavebuiltadistributedtestbedthatcomprises12
Thesecondpartoftherecipeisthetypeofinjectedfault.As virtualmachines(VM)anda3-nodeElasticSearch[66]cluster.
Section IV-B presents, MicroFI supports two primitive faults Each VM is equipped with a 4-core CPU, 16 GB memory,
(DelayandAbort)andtheycanbeconfiguredwithdifferent and runs with the Ubuntu 18.04 operating system. All VMs
parameters.Forbothfaults,userscanspecifythepossibilityof are located within the same local area network to elimintate
thetargetinvocationbeingaffectedbythefaultwithpercentage. networkjitter.WiththeseVMs,wehavecreated aKubernetes
ForAbortfault,userscanspecifytheerrorcodethatthetarget cluster (v1.20.1) with Istio (v1.12.0) installed. We utilize an
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on November 13,2025 at 00:55:27 UTC from IEEE Xplore. Restrictions apply.

CHENetal.:MICROFI:NON-INTRUSIVEANDPRIORITIZEDREQUEST-LEVELFAULTINJECTIONFORMICROSERVICEAPPLICATIONS 4931
TABLEV
DETAILSOFDIFFERENTFAULTINJECTIONEXPERIMENTSTOANSWERRQ1
faults,utilizeIstio(IST)toinjectAPI-levelfaults[25]anduse
MicroFI(MFI)toinjectrequest-levelfaults.Gremlin(GM)and
3MileBeach(3MB)arealsousedtoinjectrequest-levelfaults
tocomparewithMicroFI.
Duringevaluation,wedeploy1to3instancesforeachservice
inthreebenchmarkapplicationsandleveragetheloadbalancer
inIstiotodistributerequestsequallytoeachinstance.Intotal,
thereare9groupsofexperimentsinthisevaluation.Theexperi-
Fig.9. Topologyofexperimentplatform. mentindexesinthreedifferentcolorsareshowninTableVand
(cid:6) (cid:6)
Table VI presents experiments in three applications ( 1 - 3 in
(cid:6) (cid:6) (cid:6) (cid:6)
Hipster Shop, 1 - 3 in TrainTicket, 1 - 3 in Hotel Reserva-
open-source tracing system Jaeger [67] to collect tracing data.
tion).Eachexperimentincludesthreedifferentlevelsofinjection
ThemicroservicebenchmarkandJaegercollectorsaredeployed
experiments.Foreachexperiment,Locustuniformlygenerates
within the cluster. Service instances first send trace data to
requeststoinvokedifferentbusinessfunctionsevenlyfor36min-
the Jaeger collector on each node, which then forwards the
utes,withaconcurrencylevelsetas100.Ineachexperiment,we
aggregatedtracedatatotheElasticSearchclusterforpersistent
conduct7injectionexperimentssequentiallyandeachinjected
storage.ComponentsofMicroFIarealsodeployedintheKuber-
faultlastsfor3minutes.Moreover,a2-minutes-recoveryperiod
netescluster.ThenumberofRequestMarkerinstancesisscaled
issetbetweentwoconsecutiveinjectionexperiments,ensuring
outaccordingtothebenchmarkapplicationworkload,whereas
that the application can recover from the previous fault before
othercomponentsofMicroFIaredeployedasasingleinstance.
injectingnextfault.
TheinstanceofInjectionRecommenderreceivestracedatafrom
Fault configurations are shown in Table V, where each row
theElasticSearchandcomputesinjectionsolutionsthatwillbe
correspondstosettingsofthreelevelsofinjectionsexperiment
sent to the instance of Injection Executor to construct routing
(i.e., SI-level, API-level, request-level) in the same group of
rules.Theroutingrulesarethendistributedtothetargetservice
experiments.ChaosBladeisusedtointermittentlydrop50%of
viaIstio.
thetargetserviceinstance’snetworkpacketstoaffectrequests
For RQ2 and RQ3, since most services in these three ap-
passingthroughthetargetinstance.Istioisusedtoabort100%
plications have no fault handling logic, timeout error message
oftargetAPIinvocationsintargetservices.MicroFIandGrem-
would propagate backwards to upstream services along the
lin are used to either abort or delay 100% of the target API
service call chain. As a result, injected faults cause failures in
invocationrequestswhenthetargetbusinessfunctioniscalled,
application functions easily. Therefore, we use version-based
with a delay time set to 1.5s. Since 3MileBeach injects faults
request routing that Istio provides to handle faults, which is
bymanipulatingserializationlibrariestomodifystatuscodeof
the same way as in [38]. In details, when the error message
requests,itlacksthecapabilitytodelayrequests.Thus,itisonly
ispropagatedfromtheinjectedservicetotheupstreamservice,
(cid:6)
usedtoinjectAbortfaults.Forexample,experiment 1 includes
the upstream service will invoke another backup service that
7 injection experiments on Hipster Shop. The SI-level fault is
has the same function as the injected service. In this study, a
todrop50%packetofCartserviceinstanceandtheAPI-level
small-scale application hr-3 is constructed by adding 2 repli-
faultistoabort100%requeststhatinvoke/GetCartAPIinCart.
cas (i.e., backup service) for services in Hotel Reservation. A
The request-level Abort fault is to abort 100% requests that
medium-scaleapplicationhipster-2isconstructedbyadding1
invoke the /GetCart API when the function (http://hs-url/cart)
replicaforservicesinHipsterShop.Alargerscaleapplication
isinvokedwhiletherequest-levelDelayfaultistodelaythese
hipster-3 is constructed by adding 2 replicas in Hipster Shop.
invocationrequestsfor1.5s.
Anotherlargerscaleapplicationtt-2isconstructedbyadding1
Moreover, each application service may provide multiple
replicaforservicesinTrainTicket.
callable APIs, with each API being invoked by different re-
quests. For example, the Cart service in Hipster Shop of-
B. ControloftheBlastRadius fers multiple APIs (/GetCart, /AddCart, etc.), where the /Get-
Inthisevaluation,wecomparetheblastradiusofthreelevels Cart API is invoked by different business function requests
of faults to show the capability of MicroFI to limit fault im- (e.g., http://hs-url/, http://hs-url/cart/checkout, etc.). Due to
pactonspecifiedrequests.Werespectivelyselecttheinjection the possibility of multiple business function requests call-
toolChaosBlade(CB)toinjectService-Instance-level(SI-level) ing the same service or the same API, the blast radius
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on November 13,2025 at 00:55:27 UTC from IEEE Xplore. Restrictions apply.

4932 IEEETRANSACTIONSONDEPENDABLEANDSECURECOMPUTING,VOL.21,NO.5,SEPTEMBER/OCTOBER2024
TABLEVI
COMPARISONOFTHEFAILURERATIOSOFAPPLICATIONFUNCTIONSREQUESTSUNDERDIFFERENTLEVELSOFFAULTINJECTION
Fig.10. SuccessrateandP99latencyofdifferentapplicationfunctionrequestsinHipsterShopduringexperiment(cid:6) 2.
of injected faults varies depending on the level of fault theimpactsoffaultsinjectedbythemaresimilar.iv)Particularly,
injection. in Fig. 10(a), during the injection of an SI-level fault, since
To measure the blast radius of different injection level, we the service has two instances, the success rates of the affected
assessthenumberofbusinessfunctionsthatareaffectedduring requestsdonotdropto0.Further,asshowninFig.10(b),because
injections. The impact on each function is characterized by the API-level and request-level Abort faults abort all target
measuringchangesinitssuccessrate,responsetimeofrequests, requests, we can find that the response time of those failed
and number of failed requests. Note that, in each experiment, requestsdecreases.Duetothespacelimitation,oneapplication
differentfaultsareinjectedrespectivelyandtheblastradiusof isselectedtopresentchangesofsuccessratesandresponsetime.
eachfaultismeasuredseparately. CompleteresultsforallapplicationsarepresentedinTableVI.
Fig. 10 presents changes in success rate and P99 latency of TableVIdemonstratesthefailureratiosofrequestsforeach
different application functions requests during the experiment application function during fault injection experiments with
(cid:6) (cid:6) (cid:6) (cid:6) (cid:6) (cid:6) (cid:6)
2 , where three levels of faults (7 faults) are injected into the experiment index 1 - 3 , 1 - 3 , 1 - 3 . Since request-level
ProductCatalogservice.Theblockswithdifferentcolorspresent Delay fault does not trigger the timeout logic in services,
the time periods during which different faults are injected. therearenofailedrequests.Thus,wepresentresultsofAbort
Specifically, lines with different colors in Fig. 10(a) present fault. Table VI reveals the same conclusions as in Fig. 10.
changesinsuccessrateofdifferentfunctionsrequestsduringthe i) As CB columns show, SI-level faults cause failures across
experimentwhilelineswithdifferentcolorsinFig.10(b)present almost all different types of external requests (i.e, different
changes of p99 latency of different function requests. i) As business functions). However, due to the presence of another
showninFig.10(a),requestsofalmostallfunctionsarebroken replica instance for the injected service instance, failure rates
downbytheSI-levelfault,andrequestsoffourdifferentbusiness oftheaffectedfunctionsdonotreach100%.ii)AsISTcolumn
functions are broken down completely by the API-level fault. shows,API-levelfaultsfailmultipletypesofexternalrequests
This is because ProductCatalog service is usually invoked to completelybecauseallinvocationsthatpassthroughthetarget
serveallapplicationfunctionsandthetargetAPI(/GetProduct) API are broken down. iii) As MFI/ 3 MB/ GM column shows,
is invoked to serve 4 functions. ii) In contrast, request-level request-levelfaultsonlyfailAPIinvocationsthataretriggered
faults injected by MFI, GM and 3 MB only affect one target byspecifiedrequests,leadingthetargettypeofrequeststofail
type of requests due to their capability of blast radius control. completely.
Specifically,therequest-levelAbortfaultonlyfailsallrequests Summary:UnlikeSI-levelandAPI-levelfaultswhichcausea
that invoke one business function (http://hs-url/product/∗) in lesscontrolledimpactonmicroservicesystemswithahigherde-
Fig. 10(a) and the request-level Delay fault only delays re- greeofrandomness(i.e.,potentiallyfailmultiplebusinessfunc-
quests that invoke the same function in Fig. 10(b). Since the tions), MicroFI achieves a fine-grained and accurate request-
request-level Delay fault does not trigger the timeout logic, levelinjectionbypreciselycontrollingtheblastradiusofafault
the target requests respond successfully with longer responses into the target request. The benefit of the fine-grained control
andthesuccessratesofallrequestsremainunchanged.iii)Since is similar to that of other request-level injection tools, while
theserequest-levelinjectiontoolsonlyaffectspecificrequests, MicroFIrequiresnoinstrumentationtoapplicationsourcecode.
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on November 13,2025 at 00:55:27 UTC from IEEE Xplore. Restrictions apply.

CHENetal.:MICROFI:NON-INTRUSIVEANDPRIORITIZEDREQUEST-LEVELFAULTINJECTIONFORMICROSERVICEAPPLICATIONS 4933
Fig.11. Quantityofinjectionsforcalculatingalltheminimalsolutions.
Thiscapabilityfacilitateschaosengineeringinproductionand
thesimulationofpartialfailures,removingconcernsproposed
inMotivation#1.
C. EffectivenessofCalculatingInjectionSolutions
In RQ2, MicroFI is compared with other methods to prove
its efficiency in calculating injection solutions. Moreover, in
this evaluation, MicroFI calculates injection solutions without Fig.12. Comparisonsofdifferentmethodsgiventhesamequantityofinjec-
prioritization. In addition to choosing the basic LDFI and the tions.
LDFI optimized by IntelliFT as baselines for comparison, we
have also implemented a random strategy called RandomFI to provides the request-level injection, the testings for multiple
prove the effectiveness of LDFI. RandomFI follows a similar functions are performed in parallel. Therefore, the time used
process to LDFI but gives injection hypotheses randomly. In inparalleltestingonlydependsonthetimeusedinthelongest
eachiteration,itselectsarandomvaluevrangingfrom1tothe testing. ii) The execution efficiency improvement achieved by
number of explored APIs. Then it selects v APIs randomly to MicroFIcomparedtoLDFI(basic)variesacrossdifferentappli-
constructinjectionhypothesisandinjectfaultsintothem.Ifthe cations. In Fig. 12(b), for applications with services deployed
targetrequestfails,thehypothesisisconsideredasoneinjection with one replica service (i.e., hipster-2 and tt-2), the improve-
solution. Otherwise, RandomFI updates the list of explored ment in found solutions per second is 10.6x in hipster-2 and
APIsandrepeatsinjections.Theprocesscontinuesuntilallthe 11.6xintt-2.iii)Theexecutionefficiencyimprovementachieved
minimal solutions have been obtained or the given number of byMicroFI,relativetoLDFI(basic),becomesmoresignificantas
injectionsisreached. thescaleoftestedapplicationsincreases.Testingfunctionsone
ToprovetheeffectivenessofMicroFIingivingalltheminimal byonewithMicroFIreduces49%injectionsinhipster-2whileit
solutions for multiple application functions, we compare the reduces75%inalargerapplication(hipster-3).Paralleltesting
number of injections used by MicroFI with those of baselines by MicroFI reduces 78% execution time in hipster-2 while it
when calculating all the minimal solutions for each function. reduces87%inhipster-3.Thisimprovement iscloselyrelated
Additionally,weconductacomparisonwithbaselinesusingthe tothecomplexityoftheapplication.Whendealingwithcomplex
samequantityofinjectionswhichequalstotheinjectionquantity application,LDFI(basic)requiresmoreinjectionstovalidatethe
requiredbyMicroFI.Theevaluationisbasedonthreeaspects, calculatedhypotheses.Thisincreasedcomplexityleadstolonger
namelyexecutiontime,thenumberoffoundminimalsolutions time spent on SAT solving due to the construction of tedious
per second and solutions coverage. The solutions coverage is CNF formulas corresponding to the application functions. In
calculatedastheratioofsolutionsobtainedbyeachmethodto contrast, MicorFI accelerates testing for multiple functions by
the total number of solutions. The execution time comprises sharinghistoricalinjectionresults,whichfurthersimplifiesthe
the time spent on calculation, trace collection and injection constructedCNFformula.Thesimplificationreducesinjection
execution.Themeasurementsarerepeatedforfivetimes. quantityandexecutiontimeneededtoobtainallsolutions.
Fig.11presentsthenumberofinjectionsusedtocalculateall Figs.11and12alsoprovetheeffectivenessofSATsolvingin
injection solutions by different methods. Fig. 12(a) shows the calculatingtheminimalsolutions.i)InFig.11,itisprovedthat
executiontimeusedbydifferentmethodswiththesameinjection RandomFIrequiresmoreinjectionstogetallsolutionsduetoits
quantity.i)ComparedwithLDFI(basic),theinjectionquantity adoptionofarandomstrategytoguideinjection.Itintroduces
andtheexecutiontimearereducedthroughthepruningandthe plenty of redundant injections. ii) Given same injections as
paralleltechnique.About48%injectionsonaveragearereduced MicroFI,RandomFIneedslessexecutiontimewithouttheneed
withthepruningtechniqueandabout76%executiontimeonav- of SAT solving as shown in Fig. 12(a). However, it exhibits
eragearereducedwiththeparalleltechnique.ThisisbecauseMi- significantlylowersolutioncoverageandfindsfewersolutions
croFIskipsthecalculationandinjectionsusedtogettheknown per second in Fig. 12(b). These findings indicate that while
solutions.Byusingtheresultsfromprevioustestings,MicroFIis RandomFI may be faster in terms of execution time, it lacks
abletodirectlyvalidatewhethersolutionsforapreviouslytested theeffectivenessandefficiencyinidentifyingsolutions.
APIarealsosolutionsforthecurrenttesting,withouttheneed Fig.12alsodemonstratesthatIntelliFTsignificantlyreduces
foradditionalinjectionexecutions.Furthermore,sinceMicroFI the injection quantity and the execution time. Since most
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on November 13,2025 at 00:55:27 UTC from IEEE Xplore. Restrictions apply.

4934 IEEETRANSACTIONSONDEPENDABLEANDSECURECOMPUTING,VOL.21,NO.5,SEPTEMBER/OCTOBER2024
services in the call chain lack recovery logic, the same error TABLEVII
message is propagated throughout the call chain. Therefore,
NUMBEROFFAILEDFUNCTIONSWITH3PRIORITIZEDMETHODSIN3
APPLICATIONS
the heuristic rules employed by IntelliFT effectively prune
the injection space. However, since IntelliFT requires more
injectionsthanMicroFItogetallminimalsolutions,thesolution
coverageofIntelliFTis5.25%onaveragelowerthanMicroFI.
To mitigate the interference caused by the randomness
in the evaluation (i.e., time measurement, random selection
of RandomFI), we conduct a Mean Difference T-test with
a significance level 5% to investigate potential significant
differences in the measurement results of each method. The
analysis indicates that in the case of relative small-scale
application (hr-3), MicroFI exhibits similar performance to
IntelliFT in terms of obtained solutions/s and coverage (with DynamicneedsTop1-Top5hypotheses.Thisdiscrepancyarises
p−value≥0.05). However, for other measurements on fromthelimitationofrelyingsolelyoneitherstatictopologyor
differentapplications,MicroFIsignificantlyoutperformsother dynamic traces, as they provide incomplete information about
methods(withp−value≤0.05).Moreover,themeasurement therunningapplication.Solelyrelyingonstatictopologyforpri-
results in other evaluations have been subjected to a statistical oritizationfallsshortincapturingtheserviceinvocationrelation-
testwithasignificancelevelsetto5%. shipsinservingdifferentapplicationfunctions.Prioritizingwith
Summary:ComparedwithLDFI(basic)andRandomFI,Mi- dynamic traces prefers hypotheses whose injection points are
croFI removes about 48% and 91% redundant injections on coveredbyalargenumberofrequests.However,ifthevolumeof
average, while decreasing execution time by 76% and 28% requestsissignificantlyskewedtowardsanapplicationfunction,
on average given the same injection quantity. Compared with Dynamic might neglect other functions with fewer requests.
IntelliFT,MicroFIdecreasestimeby51%onaverageandobtains Specifically, Static needs fewer high-ranking solutions to fail
a higher coverage improved by 5.25% on average. Moreover, allfunctionsintt-2.ThisisbecausetheperformanceofStaticis
MicroFI always obtains more solutions during execution. It relatedtotheapplicationtopology.InTrainTicket,allapplication
provesthatMicroFIaddressesthetime-consumingproblemin functions invoke the same two services that are depended by
testingmultiplefunctionspresentedinMotivation#2. the largest number of other services. The preference for them
contributes to the improvement in prioritization capabilities
of Static. In contrast, APIRank prioritizes solutions based on
D. EffectivenessofPrioritizingInjectionHypotheses
runtimeinformation,makingitlesssensitivetotheapplication
InRQ3,wedemonstrateMicroFI’seffectivenessinprioritiz- implementationandtopology.
ing hypotheses that can be high-impact solutions, considering Then,wecompareMicroFIwithothermethodsintestingmul-
twoperspectives.i)Toprovetheeffectivenessofprioritization tiple functions within limited injections. Motivation #3 claims
throughtheintegrationofbothstaticapplicationtopologyand that SREs always set an error budget for each application to
dynamicrequesttraces,weperformacomparisonbetweenAPI- definethenumberoffailures,makingitimportantforprioriti-
Rankandtwomethods.Thesemethodssolelyrelyoneitherthe zation method to prioritize high-impact faults within a limited
statictopology(Static)orthedynamictraces(Dynamic).ii)We injection budget. Thus, we evaluate the performance of differ-
alsocompareMicroFIwithothermethodstoevaluatetheiref- ent methods in prioritizing injection solutions within limited
fectivenessregardingtheprioritizationofinjectionhypotheses. injection budgets (quantity of injections). Given a sufficient
Inthefirstevaluation,APIRankiscomparedwithStaticand number of injections, hypotheses prioritized by these methods
Dynamic.Staticrankscandidateinjectionhypothesesusingthe can always fail all functions, hindering the valid evaluation
application topology. It relies on the topology to rank each for these methods. Consequently, the injection budgets in the
service API based on the number of other APIs that depend evaluationhavebeensetwithinarangefromabout0%to40%of
onit.ThenStaticprioritizeshypothesiswhoseinjectionpoints theminimuminjectionquantityrequiredforhr-3(41),hipster-3
arerankedonthetop.Dynamicreliesondynamictraces.Itfirst (102), tt-2 (117), shown in Fig. 11. We select IntelliFT and a
calculatesthenumberofinvocationsforeachAPIandthenranks rules-based method R-rules as baseline methods. IntelliFT is
each API based onthenumber ofinvocations. Dynamicprior- tailored to IntelliFT* in this study in two aspects to ensure
itizes injection hypothesis whose injection points are invoked fair and focused comparisons. i) The initial set of injection
bymostrequests.Forcomparisons,wemeasurethenumberof hypotheses for each request is directly provided by LDFI (the
business functions failed by Top1-Top8 hypotheses ranked by same as IntelliFT) at the initialization stage. The modification
eachmethod. ismadetoensuretheinjectionbudgetsonlyincludethenumber
Table VII shows the comparison results in different appli- of injections used in prioritization. So, the focus of the eval-
cations.TheseresultsshowthatAPIRankrequiresfewerhigh- uation lies in the performance of prioritization strategies. ii)
rankinghypothesestofailallfunctions.Forexample,APIRank The second aspect of the modification is about the mutation
fails all functions in hr-3 by injecting faults based on Top1- processinconstructingeachtest.Wehaverestrictedthemutation
Top2hypotheseswhileStaticneedsTop1-Top4hypothesesand of IntelliFT* to changing the request type and the injection
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on November 13,2025 at 00:55:27 UTC from IEEE Xplore. Restrictions apply.

CHENetal.:MICROFI:NON-INTRUSIVEANDPRIORITIZEDREQUEST-LEVELFAULTINJECTIONFORMICROSERVICEAPPLICATIONS 4935
Fig.13. Evaluationofprioritizationmethodsinhr-3.
|     |     |     |     |     |     |     |     | Fig.16. | Performanceinhipster-2underdifferentworkloads. |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ---------------------------------------------- | --- | --- | --- | --- | --- |
prioritizedbyMicroFIalwayscausemorefailuresandfailmore
applicationfunctionsthanhypothesesprioritizedbyIntelliFT*
andR-rules.ii)AlthoughhypothesesprioritizedbyIntelliFT*
|     |     |     |     |     |     |     |     | cause fewer | failures | and | fail fewer | functions | when | the given |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | -------- | --- | ---------- | --------- | ---- | --------- |
Fig.14. Evaluationofprioritizationmethodsinhipster-3. injectionbudgetsarefew,itsperformanceimprovesasinjection
|     |     |     |     |     |     |     |     | budgets           | increase.  | The explanations |               | for i) | and ii)   | are shown as   |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | ---------- | ---------------- | ------------- | ------ | --------- | -------------- |
|     |     |     |     |     |     |     |     | follows.          | IntelliFT* | needs            | accumulation  |        | of test   | history, which |
|     |     |     |     |     |     |     |     | could guide       | the        | constructions    | of subsequent |        | testings. | Specifi-       |
|     |     |     |     |     |     |     |     | cally, IntelliFT* |            | randomly         | constructs    | fault  | tests     | and executes   |
theminitially.Thenitreliesonthetesthistorytoguidethefault
spaceexploration,includingselectingwhichattributes(Request
orInjectionpoint)tomutateandhowtomutate.Ifthetesthistory
Fig.15. Evaluationofprioritizationmethodsintt-2.
isnotenough,theexplorationandthemutationwillbeperformed
randomly.Asaresult,IntelliFT*causesfewerfailuresandfails
| hypothesis. | Unlike | IntelliFT, | which | also | mutates | fault | types |                 |     |                   |     |           |     |             |
| ----------- | ------ | ---------- | ----- | ---- | ------- | ----- | ----- | --------------- | --- | ----------------- | --- | --------- | --- | ----------- |
|             |        |            |       |      |         |       |       | fewer functions |     | at the beginning, |     | hindering | the | achievement |
andtestcases,IntelliFT*doesnotchangethefaulttype.Only
|     |     |     |     |     |     |     |     | of good | performance. | Incontrast,MicroFI |     |     | relieson | trace data |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ------------ | ------------------ | --- | --- | -------- | ---------- |
Abortfaultisselectedinthisevaluationtodirectlyfailthetarget
|     |     |     |     |     |     |     |     | rather than | test | history to | prioritize | high-impact |     | injection hy- |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ---- | ---------- | ---------- | ----------- | --- | ------------- |
invocation.Additionally,sinceeachapplicationfunctionisonly
potheses,renderingittoalwayscausefailureatthebeginning.
invokedbyonetypeofrequest,themutationoftherequesttype
|               |     |          |          |       |           |           |     | Since R-rules | does | not consider | historical |     | injection | results, it |
| ------------- | --- | -------- | -------- | ----- | --------- | --------- | --- | ------------- | ---- | ------------ | ---------- | --- | --------- | ----------- |
| is equivalent | to  | changing | the test | case. | Thus, the | reduction | of  |               |      |              |            |     |           |             |
conductsmanyduplicateinjectionsandthusperformsworse.
| mutation | attributes | does | not increase | the | number | of injections |     |     |     |     |     |     |     |     |
| -------- | ---------- | ---- | ------------ | --- | ------ | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
Summary:Motivation#3claimsthattheapplicationcomplex-
requiredduringprioritization.
ityanddynamichinderthemanualprioritization.Theevaluation
| Moreover, | we  | also | implement | another | method, | R-rules, |     |     |     |     |     |     |     |     |
| --------- | --- | ---- | --------- | ------- | ------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
provestheeffectivenessoftheprioritizationstrategyofMicroFI.
whichprioritizesfaultswithtwoheuristicrules.Eachheuristic
Comparedwithothermethods,MicroFIreducesanaverageof
rulecorrespondstooneintuitionrespectively.i)R-rulesprefers
47.3%injectionbudgetstoprioritizehypothesesforfailingall
| to inject | faults | to APIs | that have | more dependencies. |     |     | A failed |     |     |     |     |     |     |     |
| --------- | ------ | ------- | --------- | ------------------ | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
businessfunctions.Theseprioritizedhypothesescanberecom-
| API only | affects | services | that | invoke it | and invocations |     | cause |     |     |     |     |     |     |     |
| -------- | ------- | -------- | ---- | --------- | --------------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
mendedashigh-impactsolutions.
| dependencies | between |        | services. | Therefore,  | the   | dependencies |     |     |     |     |     |     |     |     |
| ------------ | ------- | ------ | --------- | ----------- | ----- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
| of service   | APIs    | can be | used to   | approximate | their | failure      | im- |     |     |     |     |     |     |     |
E. OverheadofRequest-LevelFaultInjection
| pact [68], | [69]. | ii) R-rules | prefers | to inject | faults | to injection |     |     |     |     |     |     |     |     |
| ---------- | ----- | ----------- | ------- | --------- | ------ | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
hypotheses that contains APIs that belong to the same service InRQ4,weevaluatetherequest-levelinjectionoverheadon
or locate on the same node. This rule is derived based on the hipster-2. We first use Locust to uniformly generate requests
likelihood of injection solutions [13]. As the resiliency logic without any request-level injection capacity in different con-
remains similar among APIs within the same service [13], the currency, andthen compare theresultsonaverage latency and
probability of simultaneous failures in those APIs is higher. RPS(i.e.,requestpersecond)ofrequestsasshowninFig.16.
Additionally, considering that single-node crashes are more The generation at each concurrency lasts for five minutes. As
likelythanthesimultaneousfailureofmultiplenodes[70],APIs we can see, the curve of average latency becomes steeper and
onthesamenodearemorepronetofail.Thelikelihoodofeach thecurveofRPSbecomesflatterwhentheconcurrencyreaches
solutionisusedtodeterminetheorder. 100.Meanwhile,whentheconcurrencyreaches150,hipster-2
Figs. 13, 14, and 15 show the evaluations on different pri- servesabnormallyandfailstohandlesomegeneratedrequests.
oritization methods. Quantity of failures denotes the count of Thus,themaximumconcurrencyis100andconcurrencylevels
triggered failures within the system, reflecting the times when are set to 10, 20, 50, 100. Under these different concurrency
businessfunctionsareobservedasfailedwhenfaultsareinjected levels, we uniformly generate requests to hipster-2 for five
based on prioritized hypotheses. Furthermore, to capture the minutes and measure the average latency in four cases. The
diversity of distinct failed functions, we use the percentage first case is for hipster-2 without any deployment of injection
of failed functions as an additional metric. It indicates the toolsandotherthreecasesareforhipster-2withthedeployment
percentageofbusinessfunctionsexternallyobservedasfailed, ofMicroFI,Gremlinand3MileBeach.Asinjectedfaultsaffect
which is calculated as the proportion of failed functions in all theresponsetimeofrequests,wemeasuretheresponsetimeof
functions. i) Given limited injection budgets, the hypotheses requestswhichexperienceallnecessarystepsforinjectionbut
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on November 13,2025 at 00:55:27 UTC from IEEE Xplore.  Restrictions apply.

4936 IEEETRANSACTIONSONDEPENDABLEANDSECURECOMPUTING,VOL.21,NO.5,SEPTEMBER/OCTOBER2024
Fig.17. Averageresponsetimeofhipster-2indifferentconcurrencyunderdifferentcases(withoutrequest-levelinjection(i.e.RL-Injection),withRL-Injection
usingMicroFI,Gremlinand3MileBeach).
stillrespondnormally.Eachmeasurementlastsforfiveminutes
andisrepeatedforfivetimes.
Fig.17showsaverageresponsetimeatdifferentconcurrency
levels.Itisevidentthattheresponsetimeincreasesintherangeof
43%–75%withtheuseofrequest-levelfaultinjection,regardless
ofthetoolemployed(e.g.,MicroFI,Gremlin,or3MileBeach).
There are several reasons. Firstly, all these tools necessitate
the use of Request Marker to mark the target requests. This Fig.18. ComparisonresultsonCPUandmemoryusageofMicroFIwithand
withoutworkload.
introducesadditionaloverheadasthetargetrequestmusttraverse
theRequestMarkerbeforereaching theapplication. However,
more memory on nodes. On the contrary, the deployment of
thisoverheadcanbeminimizedinproductionbyintegratingthe
MicroFI does not increase the CPU usage. As shown in Fig.
RequestMarkerlogicintotheexistinggateway.Secondly,both
18(b),theaverageCPUusagepernodeinthecasewherenodes
MicroFIandGremlinrelyontheproxyprovidedbytheservice
are deployed with MicroFI is almost equal to the case where
meshtoinjectfaults,andproxiesofservicesneedtosequentially
nodes are deployed without MicroFI. The generated workload
checkroutingrulestodetermineifincomingrequestsshouldbe
doesnotincreasetheconsumptionofCPU.
affectedbythefault.Therefore,additionallatencyisintroduced,
Summary: To support request-level injection, the response
whichcanbemitigatedthroughservicemeshoptimizationtech-
time of the request is prolonged by MicroFI in the range
niques,suchasCilium[71].AsGremlindoesnotrequiretracing
of 71%–75% due to the introduction of Request Marker and
topropagatetherequesttokenand3MileBeachavoidsinterac-
service mesh. Compared to other request-level injection tools,
tionoverheadscausedbytheservicemesh,Gremlin(48%–52%)
MicroFIincreaseslatencyby18%–23%tosupportnon-intrusive
and3MileBeach(43%–51%)increaselowerlatencycompared
injection.Moreover,thedeploymentofMicroFIconsumesap-
to MicroFI (71%–75%). However, to enable the capability of
proximately250MBofmemorywithoutincurringanysignifi-
request-levelfaultinjection,theyrequirethetargetapplication
cantoverheadintermsofCPUusage.
toberestarted,resultinginaperiodofserviceunavailability.In
contrast,MicroFIdoesnotintroducethisoverhead.Additionally,
VII. DISCUSSIONS
Gremlinand3MileBeachrequireapplication-levelinstrumenta-
tion,whereasMicroFIdoesnot. Limitations:(i)OnepotentialproblemisthatMicroFIrelies
Toevaluatetheresourceoverheadintroducedbytherequest- on distributed tracing. Powered by the observablility infras-
levelinjectionofMicroFI,weconductexperimentsonhipster-2 tructures [72], [73], [74], tracing has been widely adopted in
andtheconcurrencyissetas100.Then,werecordtheCPUand industrialmicroserviceapplications[75],renderingMicroFIto
memoryusageofeachnodeeverysecondduringexperiments. be easily utilized in these systems. However, MicroFI cannot
Linux commands sar and free are used to measure CPU and work in applications without tracing. Firstly, the request-level
memoryrespectively.OnceweobtaintheCPUusageandmem- fault injection relies on the trace propagation mechanism to
oryusageofeachnode,wecalculatetheaverageusagepernode. markspecifiedrequestsandtheirsubsequentinvocations.Some
Theresourceusagesarecapturedinfourcases,namelyMicroFI instrumentationtoapplicationcodeisrequiredtopropagatethe
deployedwithworkload,MicroFIdeployedwithoutworkload, request token for applications without tracing. Secondly, the
MicroFInotdeployedwithworkload,andMicroFInotdeployed faultinjectionstrategyreliesontracedatatocalculateinjection
withoutworkload.Eachmeasurementlastsfor3minutesandis solutions.Tracedataiscrucialasitrecordstheexecutionprocess
repeatedforfivetimes.Fig.18showstheresults. ofeachbusinessfunction.Thoughapplicationtopologycanbe
AswecanseeinFig.18(a),thedeploymentofrequest-level consideredasanalternativetocalculatesolutions,itisunableto
injectionofMicroFIalwaysconsumesmorememory.Whenno accuratelycalculatesolutionsandtheobtainedsolutionswould
workloadisgenerated,thedeploymentofMicroFIconsumesan failtheentireapplicationratherthanaspecificbusinessfunction.
additional 256 MB of memory per node compared to the case (ii)Itisbeyondthescopeofthisstudytodiscusshowtoconduct
whereMicroFIisnotdeployed.Whentheworkloadisgenerated, SATsolvingmoreefficiently.Sincethetimeusedincalculating
the case where MicroFI is deployed consumes 282 MB more solutionsisoccupiedbySATsolving,theexecutiontimewould
memorypernodethanthecasewhereMicroFiisnotdeployed. increase as the application grows larger. However, MicroFI is
This increase in memory consumption is attributed to the de- still more efficient than other works. (iii) MicroFI targets at
ploymentofservicemeshandRequestMarker,whichrequires injectingfaultstodirectlyfailordelaytherequeststoapplication
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on November 13,2025 at 00:55:27 UTC from IEEE Xplore. Restrictions apply.

CHENetal.:MICROFI:NON-INTRUSIVEANDPRIORITIZEDREQUEST-LEVELFAULTINJECTIONFORMICROSERVICEAPPLICATIONS 4937
functions. A full discussion of how to inject an appropriate [8] D. Cotroneo et al., “How bad can a bug get? an empirical analysis of
resourceexhaustionfault(e.g.,whichtypeoffaultstoinjectand softwarefailuresintheopenstackcloudcomputingplatform,”inProc.
27thACMJointMeetingEur.Softw.Eng.Conf.Symp.Found.Softw.Eng.,
howmuchintensityoftheinjectedresourceexhaustionfault)to
NewYork,NY,USA,2019,pp.200–211.
preciselyfailordelaytherequestsarenotdiscussedinthisstudy.
[9] X.Li,G.Yu,P.Chen,H.Chen,andZ.Chen,“Goingthroughthelifecycle
offaultsinclouds:Guidelinesonfaulthandling,”inProc.IEEE33rdInt.
| Threats | to Validity: | The | internal | threat | to validity | mainly |     |     |     |     |     |     |     |     |
| ------- | ------------ | --- | -------- | ------ | ----------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
Symp.Softw.Rel.Eng.,2022,pp.121–132.
| lies in the | robustness | to distributed |     | tracing | standards. | MicroFI |     |     |     |     |     |     |     |     |
| ----------- | ---------- | -------------- | --- | ------- | ---------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
[10] V.Heorhiadi,S.Rajagopalan,H.Jamjoom,M.K.Reiter,andV.Sekar,
| supports | two popular | tracing | standards | (i.e., | OpenTracing | and |     |     |     |     |     |     |     |     |
| -------- | ----------- | ------- | --------- | ------ | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
“Gremlin:Systematicresiliencetestingofmicroservices,”inProc.IEEE
36thInt.Conf.Distrib.Comput.Syst.,2016,pp.57–66.
OpenTelemetry)amongthem.Toalleviatethisthreat,MicroFI
|          |            |           |        |     |         |               | [11] “Google | compute | engine | incident | #18012,” | 2022. | [Online]. | Available: |
| -------- | ---------- | --------- | ------ | --- | ------- | ------------- | ------------ | ------- | ------ | -------- | -------- | ----- | --------- | ---------- |
| provides | a flexible | extension | method | to  | support | other tracing |              |         |        |          |          |       |           |            |
https://status.cloud.google.com/incident/compute/18012
standards as necessary. The external threat to validity mainly [12] H. Tucker, L. Hochstein, N. Jones, A. Basiri, and C. Rosenthal, “The
liesintheapplicationsselectedinthisstudy.Theymaynotrep- businesscaseforchaosengineering,”IEEECloudComput.,vol.5,no.3,
pp.45–54,May/Jun.2018.
resenttheexistingmicroserviceapplications.Wetrytocoverthe
[13] P.Alvaroetal.,“Automatingfailuretestingresearchatinternetscale,”
implementation differences of microservice applications, such in Proc. 7th ACM Symp. Cloud Comput., New York, NY, USA, 2016,
| ascommunicationprotocol,applicationscaleandprogramming |     |     |     |     |     |     | pp.17–28. |     |     |     |     |     |     |     |
| ------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
languages.However,MicroFIstillrequiresalittlecustomization [14] J. Cahoon,“Google dirt: Disaster recovery testing,”, 2019. [Online].
|     |     |     |     |     |     |     | Available: |     | https://www.oreilly.com/library/view/chaos-engineering/ |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --- | ------------------------------------------------------- | --- | --- | --- | --- | --- |
toadoptthecasesthatwehavenottakenintoaccount. 9781492043850/ch05.html
[15] “Azurechaosstudio,”2021.[Online].Available:https://azure.microsoft.
com/en-us/services/chaos-studio/#overview
|     |     | VIII. | CONCLUSION |     |     |     |             |             |     |           |                 |     |                   |       |
| --- | --- | ----- | ---------- | --- | --- | --- | ----------- | ----------- | --- | --------- | --------------- | --- | ----------------- | ----- |
|     |     |       |            |     |     |     | [16] “Chaos | engineering | at  | linkedin: | The “linkedout” |     | failure injection | test- |
ingframework,”2021.[Online].Available:https://www.infoq.com/news/
| We propose | MicroFI—a |     | fine-grained |     | fault injection | frame- |     |     |     |     |     |     |     |     |
| ---------- | --------- | --- | ------------ | --- | --------------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
2018/06/linkedout-failure-injection/
work for microservice applications, which tests the resiliency [17] A.Basirietal.,“Chaosengineering,”IEEESoftw.,vol.33,no.3,pp.35–41,
formultipleapplicationbusinessfunctionsbasedontherequest- May/Jun.2016.
level fault injection and prioritizes high-impact faults. We de- [18] Gremlin,“state-of-chaos-engineering,”2022.[Online].Available:https:
//www.gremlin.com/state-of-chaos-engineering/2021/?ref=blog
sign the non-intrusive request-level fault injection that limits [19] P. Joshi, H. S. Gunawi, and K. Sen, “Prefail: A programmable tool
the blast radius into the target requests with the tracing and formultiple-failureinjection,”inProc.ACMInt.Conf.ObjectOriented
servicemeshtechnique.ThenweextendLDFIalgorithmwith Program.Syst.Lang.Appl.,NewYork,NY,USA,2011,pp.171–188.
|     |     |     |     |     |     |     | [20] “Hipstershop,” |     | 2021. | [Online]. | Available: |     | https://github.com/ |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------- | --- | ----- | --------- | ---------- | --- | ------------------- | --- |
injection space pruning technique and parallel technique to GoogleCloudPlatform/microservices-demo
acceleratemultiplebusinessfunctionstestingwithoutredundant [21] K.Lee,“Beyonddistributedtracing,”inSREConSanFrancisco,CA,USA:
USENIXAssociation,2022.
injections.AnenhancedPageRankalgorithmisalsoemployedto
[22] C.S.Meiklejohn,A.Estrada,Y.Song,H.Miller,andR.Padhye,“Service-
supporthigh-impactfaultssearching.Theevaluationsonthree levelfaultinjectiontesting,”inProc.ACMSymp.CloudComput.,New
representative open-source microservice applications confirm York,NY,USA,2021,pp.388–402.
|     |     |     |     |     |     |     | [23] L. Zhang, | B.  | Morin, B. | Baudry, | and M. | Monperrus, | “Maximizing | er- |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | --------- | ------- | ------ | ---------- | ----------- | --- |
theeffectivenessofMicroFI.Inthefuture,weplantoimprove
|     |     |     |     |     |     |     | ror injection |     | realism for | chaos | engineering | with | system calls,” | IEEE |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ----------- | ----- | ----------- | ---- | -------------- | ---- |
MicroFIinconsideringmoreinformationtoconstructfaulttests.
|     |     |     |     |     |     |     | Trans. | Dependable | Secure | Comput., | vol. | 19, no. | 4, pp. 2695–2708, |     |
| --- | --- | --- | --- | --- | --- | --- | ------ | ---------- | ------ | -------- | ---- | ------- | ----------------- | --- |
Jul./Aug.2022.
[24] J.Simonssonetal.,“Observabilityandchaosengineeringonsystemcalls
ACKNOWLEDGMENT
forcontainerizedapplicationsindocker,”FutureGener.Comput.Syst.,
The authors appreciate the insightful feedback from the vol.122,pp.117–129,2021.
|                                                           |     |     |     |     |     |     | [25] Istio, | “Istio | Documention,” | 2020. | [Online]. | Available: | https://istio.io/ |     |
| --------------------------------------------------------- | --- | --- | --- | --- | --- | --- | ----------- | ------ | ------------- | ----- | --------- | ---------- | ----------------- | --- |
| anonymousreviewers.Especially,weareparticularlygratefulto |     |     |     |     |     |     | latest/docs |        |               |       |           |            |                   |     |
HuxingZhangcomingfromAlibaba.Hisgreatadviseimproves [26] Netflix,“Chaosmonkey,”2015.[Online].Available:https://github.com/
Netflix/chaosmonkey
thisworkalot.
|     |     |     |     |     |     |     | [27] Chaosblade, |     | “An easy | to use and | powerful | chaos | engineering | toolkit,” |
| --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | -------- | ---------- | -------- | ----- | ----------- | --------- |
2020.[Online].Available:https://github.com/chaosblade-io/chaosblade
REFERENCES [28] Chaosmesh,“Breakyoursystemconstructively,”2019.[Online].Avail-
able:https://chaos-mesh.org/
[1] J.Lin,P.Chen,andZ.Zheng,“Microscope:Pinpointperformanceissues [29] Litmus,“Opensourcechaosengineeringplatform,”2019.[Online].Avail-
withcausalgraphsinmicro-serviceenvironments,”inProc.16thInt.Conf. able:https://github.com/litmuschaos/litmus
Serv.-OrientedComput.,2018,pp.3–20. [30] P. Joshi et al., “SETSUDO: Perturbation-based testing framework
[2] H.Zhouetal.,“Overloadcontrolforscalingwechatmicroservices,”in for scalable distributed systems,” in Proc. First ACM SIGOPS
Proc.ACMSymp.CloudComput.,NewYork,NY,USA,2018,p.149–161. Conf. Timely Results Operating Syst., New York, NY, USA, 2013,
| [3] O. Sheikh | et al., | “Modernize | digital | applications | with | microservices | pp.1–14. |     |     |     |     |     |     |     |
| ------------- | ------- | ---------- | ------- | ------------ | ---- | ------------- | -------- | --- | --- | --- | --- | --- | --- | --- |
managementusingtheistioservicemesh,”inProc.28thAnnu.Int.Conf. [31] P.Alvaro,J.Rosen,andJ.M.Hellerstein,“Lineage-drivenfaultinjection,”
inProc.ACMSIGMODInt.Conf.Manage.Data,NewYork,NY,USA,
Comput.Sci.Softw.Eng.,2018,p.359–360.
[4] Y.Ganetal.,“Seer:LeveragingBigDatatonavigatethecomplexityof 2015,pp.331–346.
performancedebuggingincloudmicroservices,”inProc.24thInt.Conf. [32] L.Page,S.Brin,R.Motwani,andT.Winograd,“Thepagerankcitation
ArchitecturalSupportProgram.Lang.OperatingSyst.,NewYork,NY, ranking:Bringingordertotheweb,”inProc.WebConf.,1999.[Online].
USA,2019,pp.19–33. Available:https://api.semanticscholar.org/CorpusID:1508503
[5] X.Zhouetal.,“Latenterrorpredictionandfaultlocalizationformicroser- [33] X.Zhouetal.,“Benchmarkingmicroservicesystemsforsoftwareengi-
viceapplicationsbylearningfromsystemtracelogs,”inProc.27thACM neeringresearch,”inProc.40thInt.Conf.Softw.Eng.,CompanionProc.,
JointMeetingEur.Softw.Eng.Conf.Symp.Found.Softw.Eng.,NewYork, NewYork,NY,USA,2018,pp.323–324.
NY,USA,2019,pp.683–694. [34] Y.Ganetal.,“Anopen-sourcebenchmarksuiteformicroservicesandtheir
[6] P.Huangetal.,“Grayfailure:Theachilles’heelofcloud-scalesystems,” hardware-softwareimplicationsforcloud&edgesystems,”inProc.24th
inProc.16thWorkshopHotTopicsOperatingSyst.,NewYork,NY,USA, Int. Conf. Architectural Support Program. Lang. Operating Syst., New
| 2017,pp.150–155. |     |     |     |     |     |     | York,NY,USA,2019,pp.3–18. |     |     |     |     |     |     |     |
| ---------------- | --- | --- | --- | --- | --- | --- | ------------------------- | --- | --- | --- | --- | --- | --- | --- |
[7] H.S.Gunawietal.,“Whydoesthecloudstopcomputing?lessonsfrom [35] J.Zhang,R.Ferydouni,A.Montana,D.Bittman,andP.Alvaro,“3Mile-
hundredsofserviceoutages,”inProc.7thACMSymp.CloudComput., Beach:Atracerwithteeth,”inProc.ACMSymp.CloudComput.,New
| NewYork,NY,USA,2016,pp.1–16. |     |     |     |     |     |     | York,NY,USA,2021,pp.458–472. |     |     |     |     |     |     |     |
| ---------------------------- | --- | --- | --- | --- | --- | --- | ---------------------------- | --- | --- | --- | --- | --- | --- | --- |
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on November 13,2025 at 00:55:27 UTC from IEEE Xplore.  Restrictions apply.

4938 IEEETRANSACTIONSONDEPENDABLEANDSECURECOMPUTING,VOL.21,NO.5,SEPTEMBER/OCTOBER2024
[36] H.S.Gunawietal.,“Fateanddestini:Aframeworkforcloudrecovery [69] J.Yinetal.,“CloudScout:Anon-intrusiveapproachtoservicedependency
testing,”inProc.8thUSENIXConf.NetworkedSyst.Des.Implementation, discovery,”IEEETrans.ParallelDistrib.Syst.,vol.28,no.5,pp.1271–
2011,pp.238–252. 1284,May2017.
[37] A. Basiri, L. Hochstein, N. Jones, and H. Tucker, “Automating chaos [70] A.RainaandR.Ellupuru,Madaari:OrderingfortheMonkeys.Brooklyn,
experimentsinproduction,”inProc.41stInt.Conf.Softw.Eng.:Softw. NY,USA:USENIXAssociation,2019.
Eng.Pract.,2019,pp.31–40. [71] “Cilium,”2022.[Online].Available:https://cilium.io/
[38] Z. Long et al., “Fitness-guided resilience testing of microservice- [72] Datadog,“Cloudmonitoringasaservice,”2023.[Online].Available:https:
based applications,” in Proc. IEEE Int. Conf. Web Serv., 2020, //www.datadoghq.com/
pp.151–158. [73] Apache, “Skywalking,” 2023. [Online]. Available: https://skywalking.
[39] A.O.Duqueetal.,“Aqualitativeevaluationofservicemesh-basedtraffic apache.org/
managementformobileedgecloud,”inProc.IEEE22ndInt.Symp.Cluster [74] Alibaba, “Application real-time monitoring service,” 2023. [Online].
CloudInternetComput.,2022,pp.210–219. Available:https://www.alibabacloud.com/es/product/arms
[40] “Alibabacloud service mesh,” 2023. [Online]. Available: https://www. [75] C.Zhangetal.,“DeepTraLog:Trace-logcombinedmicroserviceanomaly
alibabacloud.com/es/product/servicemesh detectionthroughgraph-baseddeeplearning,”inProc.IEEE/ACM44th
[41] “Tencent cloud mesh,” 2023. [Online]. Available: https://www. Int.Conf.Softw.Eng.,2022,pp.623–634.
tencentcloud.com/products/tcm
[42] “Anthosservicemesh,”2023.[Online].Available:https://cloud.google. HongyangChen(GraduateStudentMember,IEEE)
com/anthos/service-mesh?hl=es received the BE degree from Sun Yat-sen Univer-
[43] “Envoy,”2022.[Online].Available:https://www.envoyproxy.io/ sity,China,in2020.Heiscurrentlyworkingtoward
[44] B.H.Sigelmanetal.,“Dapper,alarge-scaledistributedsystemstracing thePhDdegreeintheSchoolofComputerScience
infrastructure,”2010.[Online].Available:https://api.semanticscholar.org/ andEngineering,SunYat-senUniversity.Hiscurrent
CorpusID:14271421 research areas focus on distributed system, cloud
[45] “Opentelemetry,”2022.[Online].Available:https://opentelemetry.io/ computing,chaosengineeringandsoftwaredefined
[46] “Opentracing,”2022.[Online].Available:https://opentraicng.io/ networking.
[47] P.JacksonandD.Sheridan,“Clauseformconversionsforbooleancir-
cuits,”inProc.7thInt.Conf.TheoryAppl.SatisfiabilityTesting,Berlin,
Heidelberg,2004,pp.183–198.
[48] T.Schoning,“AprobabilisticalgorithmforK-satandconstraintsatisfac- PengfeiChenreceivedthegraduateddegreefromthe
tionproblems,”inProc.40thAnnu.Symp.Found.Comput.Sci.,1999, department of computer science of Xi’an Jiaotong
pp.410–414. UniversitywiththePhDdegreein2016.Heiscur-
[49] M. Davis, G. Logemann, and D. Loveland, “A machine program for rentlyanassociatedprofessorintheSchoolofCom-
theorem-proving,”Commun.ACM,vol.5,no.7,pp.394–397,Jul.1962. puterScienceandEngineeringofSunYat-senUniver-
[50] Z3,“TheZ3theoremprover,”2019.[Online].Available:https://github. sity.Meanwhile,heisaPhDadvisor.Now,heisinter-
com/Z3Prover/z3 estedindistributedsystems,AIOps,cloudcomput-
[51] “Theminisatpage,”2022.http://minisat.se ing,Microserviceandnetworksystems.Especially,
[52] C.Lou,P.Huang,andS.Smith,“Understanding,detectingandlocalizing hehasstrongskillsincloudcomputing.Sofar,Hehas
partialfailuresinlargesystemsoftware,”inProc.17thUSENIXSymp. publishedmorethan80papersinsomeinternational
Netw.Syst.Des.Implementation,SantaClara,CA,USA,2020,pp.559– conferencesincludingACMASE/ICSE/FSE,IEEE
574. INFOCOM, WWW, ACM/IEEE CCGRID,IEEE ISSRE, IEEE ICWS, IEEE
[53] Littleknownwaystobetteruseyourerrorbudgets.[Online].Available: DSN,ICPPandjournalsincludingIEEETDSC,IEEETNNLS,IEEETR,IEEE
https://www.blameless.com/blog/4-surprising-error-budget-use-cases TSC,IEEETETC,andIEEETCC.Heservesasofprogramcommitteemember
[54] R.T.FieldingandR.N.Taylor,“Architecturalstylesandthedesignof ofmultipleconferencesandreviewersofsomeinternaljournalssuchasIEEE
network-basedsoftwarearchitectures,”Ph.D.dissertation,Universityof TDSC,IEEETC,andInformationScience.
California,Irvine,2000,aAI9980887.
[55] A.D.BirrellandB.J.Nelson,“Implementingremoteprocedurecalls,”
GuangbaYu(StudentMember,IEEE)receivedthe
ACMTrans.Comput.Syst.,vol.2,no.1,pp.39–59,Feb.1984.
master’sdegreefromSunYat-SenUniversity,China,
[56] “Strace,” 2023. [Online]. Available: https://man7.org/linux/man-pages/
in 2020. He is currently working toward the PhD
man1/strace.1.html
degree with the School of Computer Science and
[57] “Realizingthenewvalueofservicemesh:Accuratelycontrollingtheblast
EngineeringwithSunYat-SenUniversity,China.His
radius(chinese),”2023.[Online].Available:https://developer.aliyun.com/
current research areas include distributed system,
article/878287
cloudcomputing,andAIdrivenoperations.
[58] G. Yu et al., “MicroRank: End-to-end latency issue localization with
extendedspectrumanalysisinmicroserviceenvironments,”inProc.Web
Conf.2021,pp.3087–3098.
[59] G.JehandJ.Widom,ScalingPersonalizedWebSearch.NewYork,NY,
USA:ACM,2003,pp.271–279. Xiaoyun Li received the BEng degree from Sun
[60] “Kubernetes,”2021.[Online].Available:https://kubernetes.io/ Yat-senUniversity,in2019.Sheiscurrentlyworking
[61] X.Zhouetal.,“Faultanalysisanddebuggingofmicroservicesystems: towardthePhDdegreeintheSchoolofComputer
Industrialsurvey,benchmarksystem,andempiricalstudy,”IEEETrans. Science and Engineering, Sun Yat-sen University,
Softw.Eng.,vol.47,no.2,pp.243–260,Feb.2021. Guangzhou, China. Her current research areas fo-
[62] Z.Huangetal.,“Sieve:Attention-basedsamplingofend-to-endtracedata cusonensuringcloudsystemreliabilitybyapplying
indistributedmicroservicesystems,”inProc.IEEEInt.Conf.WebServ., AItechniques,especiallyinloganalysisandmutli-
2021,pp.436–446. modalfaultdiagnosis.
[63] Z.Heetal.,“Graphbasedincidentextractionanddiagnosisinlarge-scale
online systems,” in Proc. IEEE/ACM 37th Int. Conf. Automated Softw.
Eng.,NewYork,NY,USA,2023,pp.1–3.
[64] Y. Gan et al., “Sage: Practical and scalable ML-Driven performance Zilong He (Graduate Student Member, IEEE) re-
debugginginmicroservices,”inProc.26thInt.Conf.ArchitecturalSupport ceived the BE and MS degree from Sun Yat-sen
Program.Lang.OperatingSyst.,2021,pp.135–151. University,China,in2019and2021.Heiscurrently
[65] LocustIO, “Locust: An open source load testing tool,” 2019. [Online]. workingtowardthePhDdegreewiththeSchoolof
Available:https://locust.io/ ComputerScienceandEngineeringofSunYat-sen
[66] elasticsearch. (2015) elasticsearch/elasticsearch. 2022. [Online]. Avail- University,China.Hiscurrentresearchareasinclude
able:https://github.com/elasticsearch/elasticsearch anomalydetectionalgorithms,AIdrivenoperations.
[67] “Jaeger,”2022.[Online].Available:https://www.jaegertracing.io/
[68] T. Yang et al., “AID: Efficient prediction of aggregated intensity of
dependencyinlarge-scalecloudsystems,”inProc.IEEE/ACM36thInt.
Conf.AutomatedSoftw.Eng.,2021,pp.653–665.
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on November 13,2025 at 00:55:27 UTC from IEEE Xplore. Restrictions apply.