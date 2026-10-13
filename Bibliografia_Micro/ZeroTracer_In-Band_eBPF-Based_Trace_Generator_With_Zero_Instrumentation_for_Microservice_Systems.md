1478 IEEETRANSACTIONSONPARALLELANDDISTRIBUTEDSYSTEMS,VOL.36,NO.7,JULY2025
| ZeroTracer: |      |     |                 | In-Band   |              | eBPF-Based |                        |              | Trace |     | Generator |         |     |
| ----------- | ---- | --- | --------------- | --------- | ------------ | ---------- | ---------------------- | ------------ | ----- | --- | --------- | ------- | --- |
| With        | Zero |     | Instrumentation |           |              |            | for                    | Microservice |       |     |           | Systems |     |
|             |      |     |                 | WanqiYang | ,PengfeiChen |            | ,KaiLiu,andHuxingZhang |              |       |     |           |         |     |
Abstract—Microservice enables agility in modern cloud-native and resolution for microservice applications, particularly in
applicationsbutintroduceschallengesinfaulttroubleshootingdue scenarioswhereanomalypropagationoccurs[11],[18].
toitscomplexservicecoordinationandcooperation.Totacklethese
|     |     |     |     |     |     |     | Distributed | tracing | systems | are | typically | implemented | in an |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ------- | ------- | --- | --------- | ----------- | ----- |
challenges,distributedtracinghasemergedforend-to-endrequest
|         |            |                |     |          |          |         | invasive | manner | to track | end-to-end |     | requests in | large-scaled |
| ------- | ---------- | -------------- | --- | -------- | -------- | ------- | -------- | ------ | -------- | ---------- | --- | ----------- | ------------ |
| tracing | and system | understanding. |     | However, | existing | tracing | so-      |        |          |            |     |             |              |
microserviceapplications,likeZipkin[12],Jaeger[13],Open-
lutionsoftensufferfromcodeinstrumentation,tracelossandin-
accuracy.Toovercometheselimitations,weintroduceZeroTracer, Telemetry [14], OpenTracing [15], X-Trace [10] and Dap-
an in-kernel online distributed tracing system equipped with an per[11],butsufferfromhighmaintenancecost.Sincearequest
| eBPF-based | (extended |     | Berkeley | Packet Filter) | trace | generator. |     |     |     |     |     |     |     |
| ---------- | --------- | --- | -------- | -------------- | ----- | ---------- | --- | --- | --- | --- | --- | --- | --- |
maytraversenumerousservicesdeployedondifferentphysical
ZeroTracertailorsfortrackingHTTPrequestsduetoitspopularity
machinesandgeographicallocations,andcodedinvarioushigh-
inmicroservicesystems.Inourevaluations,ZeroTracerachieves
levelprogramminglanguages,theseinvasiveapproachesrequire
remarkabletraceaccuracy(i.e.,over91%)andmaintainsstable
performance under different workload concurrency. Moreover, developerstoweavetracingcodesdirectlyintothemicroservice
ZeroTraceroutperformsothernon-invasiveapproacheswhichfail applications or third-party libraries to automatically generate
toreconcileaccuraterequestcausality.Notably,ZeroTracereffec-
|               |            |     |          |                   |     |              | traces when     | applications |                 | handle | requests.      | Nevertheless, | code  |
| ------------- | ---------- | --- | -------- | ----------------- | --- | ------------ | --------------- | ------------ | --------------- | ------ | -------------- | ------------- | ----- |
| tively tracks | end-to-end |     | requests | in multi-threaded |     | microservice |                 |              |                 |        |                |               |       |
|               |            |     |          |                   |     |              | instrumentation |              | in applications |        | or third-party | libraries     | lacks |
applications,whichisabsentinexistinginvasivedistributedtracing
supportforhotupdatesthusrequiringhighmaintenancecosts.
| systems | with third-party |     | library | instrumentation. |     | Moreover, | Ze- |     |     |     |     |     |     |
| ------- | ---------------- | --- | ------- | ---------------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
roTracerintroducesanegligibleoverhead,withlatencyincreasing Version updates can lead to incompatibilities, introducing po-
byonly0.5%–1.2%andamodest3%–5.8%increaseinCPUand tentialsecurityrisks,programbugs,orevenfatalerrors.
memoryconsumption. Non-invasive distributed tracing systems are being studied
Index Terms—Distributed system, microservice, distributed as an alternative approach to reduce the maintenance cost in-
tracing,eBPF,observability. troduced by the invasive ones, but have shortcomings in trace
|     |     |     |     |     |     |     | loss and | inaccuracy. | Existing | non-invasive |     | distributed | tracing |
| --- | --- | --- | --- | --- | --- | --- | -------- | ----------- | -------- | ------------ | --- | ----------- | ------- |
systems[19],[20]implementaggregationalgorithmsbasedon
|     |     |     | I. INTRODUCTION |     |     |     |                 |     |         |         |               |          |       |
| --- | --- | --- | --------------- | --- | --- | --- | --------------- | --- | ------- | ------- | ------------- | -------- | ----- |
|     |     |     |                 |     |     |     | their collected |     | network | metrics | and metadata. | Although | these |
MODERNlarge-scaleddistributedsystemsoftenadopta
|     |     |     |     |     |     |     | non-invasive | implementations |     | eliminate |     | code instrumentation, |     |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --------------- | --- | --------- | --- | --------------------- | --- |
microservicearchitecturetoenhancescalabilityandreli-
|     |     |     |     |     |     |     | they often | fail | to capture | accurate | request | causality | in com- |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ---- | ---------- | -------- | ------- | --------- | ------- |
ability[1],[2],[3],[4],[5],[6],[7],[8].However,managingsuch
plexmicroserviceapplications.Moreover,theiradoptedoffline
complexsystemspresentssignificantchallenges.Whenafailure
analysisisnotreal-timeandcannotsupportdownstreamservice
occurs, the complex interactions between services along with orchestration,suchasgrayreleaseandrequestrouting.
| anomaly | propagation |     | complicate | troubleshooting. |     | To expedite |             |     |            |                |     |                |      |
| ------- | ----------- | --- | ---------- | ---------------- | --- | ----------- | ----------- | --- | ---------- | -------------- | --- | -------------- | ---- |
|         |             |     |            |                  |     |             | As outlined |     | above, the | implementation |     | of a practical | non- |
troubleshooting,distributedtracingsystems[9],[10],[11],[12],
invasivedistributedtracingsystemcapableofeffectivelytrack-
| [13], [14], | [15],      | [16],         | [17] are | proposed    | and are | now widely      |                |     |          |                  |     |         |            |
| ----------- | ---------- | ------------- | -------- | ----------- | ------- | --------------- | -------------- | --- | -------- | ---------------- | --- | ------- | ---------- |
|             |            |               |          |             |         |                 | ing end-to-end |     | requests | for microservice |     | systems | encounters |
| used in     | production | environments. |          | The latency |         | of each service |                |     |          |                  |     |         |            |
severalchallengesasfollows.
(cid:2)
operationinend-to-endrequestscollectedbydistributedtracing Compatible with various high-level languages: Modern
systemssignificantlyenhancestheefficiencyoftroubleshooting
microservicesystemsaredevelopedinvarioushigh-level
languages,includingJava,Python,andGolang.Ensuring
Received22April2024;revised5April2025;accepted11May2025.Date compatibilitywiththesecommonlyusedlanguageswhile
ofpublication19May2025;dateofcurrentversion9June2025.Thiswork minimizing maintenance costs poses a significant chal-
was supportedin partbytheNational Natural Science FoundationofChina lengeintrackingend-to-endrequests.
| underGrant62272495andinpartbytheGuangdongBasicandAppliedBasic |     |     |     |     |     |     | (cid:2) |     |     |     |     |     |     |
| ------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- |
Research FoundationGrant 2023B1515020054.Thisworkwas supportedin Zero instrumentation withaccurate traces: In large-scale
partbyAlibabaProjectunderGrant20925056,forwhichwearedeeplygrate- microservicesystems,refactoringcomplexrequestcausal-
ful.RecommendedforacceptancebyS.Al-Kiswany.(Correspondingauthor: itywithoutanycodeinstrumentationpresentsaformidable
PengfeiChen.)
Wanqi Yang and Pengfei Chen are with the School of Computer Science challenge,particularlyincontainerizedcloud-nativeenvi-
andEngineering,SunYat-senUniversity,Guangzhou510275,China(e-mail: ronments. Moreover, microservice systems utilize either
yangwq23@mail2.sysu.edu.cn;chenpf7@mail.sysu.edu.cn).
single-threadedormulti-threadedmodels,includingthread
KaiLiuandHuxingZhangarewithAlibabaGroup,Hangzhou311121,China
(e-mail:qianlu.lk@alibaba-inc.com;huxing.zhx@alibaba-inc.com). poolsorcoroutines,furthercomplicatingnon-invasivere-
DigitalObjectIdentifier10.1109/TPDS.2025.3571934 questtracing.
1045-9219©2025IEEE.Allrightsreserved,includingrightsfortextanddatamining,andtrainingofartificialintelligenceandsimilartechnologies.
Personaluseispermitted,butrepublication/redistributionrequiresIEEEpermission.Seehttps://www.ieee.org/publications/rights/index.htmlformoreinformation.
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on March 20,2026 at 23:38:08 UTC from IEEE Xplore.  Restrictions apply.

YANGetal.:ZEROTRACER:IN-BANDeBPF-BASEDTRACEGENERATORWITHZEROINSTRUMENTATIONFORMICROSERVICESYSTEMS 1479
real-time observability of microservice systems, distin-
guishing our system from existing non-invasive tracing
systems that typically use eBPF as a monitor or span
generator.
(cid:2)
We propose a non-invasive in-band distributed tracing
system,namedZeroTracer.Wehaveconductedextensive
experimentsanddeployedZeroTracerinareal-worlden-
vironment. Experiment results show that ZeroTracer can
achieve impressive tracing accuracy over 91% with neg-
ligibleoverhead,0.5%–1.2%increasesinlatencyandan
additional3%–5.8%inCPUandmemoryconsumption.
Fig.1. Anexampletoshowthetracecontextpropagationacrossthenetwork
andthroughservicesforgeneratingatrace.
II. BACKGROUNDANDMOTIVATIONS
(cid:2) A. RequestTracingWithZeroInstrumentation
Online request tracing: Online tracing offers real-time
visibility into how requests flow through a distributed 1) Distributed Tracing System: Distributed tracing sys-
system, facilitating quick issue identification and resolu- tems[9],[10],[11]enabletrackingend-to-endrequestsacross
tion.However,trackingrequestsonlinewithoutanycode large-scaled microservice systems. They provide insights into
instrumentationposesconsiderabledifficulty. thelatencycontributedbyeachoperationwithinanend-to-end
To address these challenges, we introduce ZeroTracer, an request and illustrate the request causality, which can be dis-
in-kernel non-invasive distributed tracing system leveraging played invisualrepresentations suchas tracetrees.Analyzing
eBPF (extended Berkeley Packet Filter) [21], [22]. With the thesetracetreeshelpsdeveloperspinpointbottlenecksandtrou-
widespreaduseofHTTP(HyperTextTransferProtocol)inmod- bleshootperformanceissuesassociatedwithanomalousend-to-
ern microservices [23],[24],ZeroTracer is designed torealize endrequests.Asthemicroservicearchitecturegainspopularity,
real-time end-to-end HTTP request tracing for microservice distributedtracingsystemshavebecomeindispensabletoolsfor
applications implemented in various high-level languages. By effectivesystemmanagement.
interceptingrequestsandresponses,injectingcustomtracecon- Fig. 1 illustrates how a distributed tracing system works
texts (e.g., trace ID) as tags into the messages, and extracting to help with fault troubleshooting. Traces are generated by
thosecontextsfrommessages,ZeroTracerpropagatestracecon- tracecontextpropagationalongsidetheend-to-endrequests.For
textswithinthekernelwithitsautomateddiscoveryofparent- example, service B extracts the parent trace context from the
childrelationshipsamongthreadsorcoroutines.Consequently, request coming from A and injects child trace context into its
ZeroTracer can automatically track end-to-end requests in the requesttoD,tofacilitatetracecontextpropagationandassociate
kernelwithoutuserawareness.Ourevaluationdemonstratesthat these two requests with their causality. Each service operation
ZeroTracer effectively tracks over 91% of end-to-end requests intheend-to-endrequestgeneratesaspan.Byaggregatingthe
forbothsingle-threadedandmulti-threadedmicroserviceappli- generatedspanswiththesametraceID(0inthiscase)fromall
cations,evenunderhighconcurrency.Furthermore,ZeroTracer services,thedistributedtracingsystemcanvisualizeanend-to-
exhibits minimal impact on service performance, with just a end request in a trace tree as shown in the dashed box. When
0.5%–1.2%increaseinservicelatencyandadditionalconsump- afailureonrequestlatencyhappensinserviceD,itpropagates
tion of 3% –5.8% in CPU and memory resources. Moreover, toserviceBandthentofront-endA.Wecantraversethetrace
we have successfully integrated ZeroTracer into a real-world treefromtherootspan(span1)toitschildrenspans(span2and
cloudtracingconsole,demonstratingitspracticalapplicability thenspan4),comparingthelatencyofeachspanalongtheway
andeffectiveness. todiagnosethefailure.Thisexamplehighlightsthesignificance
Contributionsofourworkcanbesummarizedasfollows. of propagating trace contexts for effective request tracing and
(cid:2)
We implemented a generic distributed tracing system in faulttroubleshooting.
the kernel to facilitate request tracing for microservice 2) Drawbacks of Existing Implementations: Existing dis-
applications developed in diverse high-level languages, tributed tracing systems are commonly implemented in an
reducing the maintenance cost associated with frequent invasive manner [11], [12], [13], [14], [15], requiring code
updatestothird-partytracinglibrariesorapplicationsource instrumentation in applications or third-party libraries to gen-
codes. erate traces manually or automatically. While these systems
(cid:2)
We study how microservice applications serve a user re- can track requests to enhance troubleshooting efficiency, they
(cid:2)
quest, and implement in-kernel automated trace context are accompanied by certain drawbacks: 1 High maintenance
propagation through single-threaded and multi-threaded cost:Microserviceapplicationsaredevelopedacrossaspectrum
containerized services with our automated discovered of high-level programming languages. As a result, traditional
parent-childrelationshipsamongthreadsandcoroutines. distributedtracingsystemsoftennecessitatetheprovisionofin-
(cid:2)
WeutilizeeBPFtoimplementanin-kerneltracegenerator strumentedthird-partylibrariesinmultiplehigh-levellanguages
tosupportonlinerequesttracingwithzeroinstrumentation to facilitate end-to-end request tracing. This process of instru-
into microservice applications. This capability provides menting libraries is notably time-consuming, especially when
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on March 20,2026 at 23:38:08 UTC from IEEE Xplore. Restrictions apply.

1480 IEEETRANSACTIONSONPARALLELANDDISTRIBUTEDSYSTEMS,VOL.36,NO.7,JULY2025
TABLEI
FEATURECOMPARISONBETWEENZEROTRACERANDEXISTINGDISTRIBUTED
TRACINGSYSTEMS
Fig.2. AnexampleofgeneratedtracesbyZeroTracer,Deepflow,andJaeger
|     |     |     |     |     |     |     |     | these offline | analysis | algorithms, | leading to increased | runtime |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | -------- | ----------- | -------------------- | ------- | --- |
withthird-partylibraryinstrumentationwhenpostingarequesttothemulti-
overheads.
threadedTravelserviceoftheTrainticketapplication.
|               |     |          |             |     |            |     |           | 3) GoalsofZeroTracer: |         | Theprosandconsofexistingdis- |                   |     |       |
| ------------- | --- | -------- | ----------- | --- | ---------- | --- | --------- | --------------------- | ------- | ---------------------------- | ----------------- | --- | ----- |
|               |     |          |             |     |            |     |           | tributed              | tracing | systems analyzed             | above put forward | the | goals |
| accommodating |     | emerging | programming |     | languages. |     | Moreover, |                       |         |                              |                   |     |       |
forZeroTracersummarizedasfollows.Adetailedcomparison
the incessant updates to third-party libraries and applications betweenZeroTracerandexistingdistributedtracingsystemsis
exacerbate the challenge of maintaining instrumented tracing presentedinTableI.
(cid:2)
codes.Forexample,OpenTelemetrynecessitatesinstrumenting
Goal1:Zeroinstrumentation.ZeroTracermusttrackend-
atleast8linesofcodesformanualtracecontextpropagationfor to-endrequestswithzeroinstrumentationintoapplications
eachspaninaC++application[25].IfaC++programgenerates
|                                                         |     |     |     |     |     |     |     | or     | third-party | libraries, | thereby minimizing | maintenance |     |
| ------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ------ | ----------- | ---------- | ------------------ | ----------- | --- |
| atracewithonehundredspans,itrequiresatleasteighthundred |     |     |     |     |     |     |     | costs. |             |            |                    |             |     |
(cid:2)
linesofinstrumentedcodes,allofwhichneedtobemaintained. Goal 2: High-level language support. ZeroTracer should
(cid:2) Lowaccuracywiththird-partylibraryinstrumentation:Trace
| 2   |     |     |     |     |     |     |     | integrate |     | with commonly | used high-level | languages | in  |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | ------------- | --------------- | --------- | --- |
accuracyreferstoitsabilitytopreciselyreflectrequestcausality microservicesystems,suchasC,Python,andJava,etc.
(cid:2)
| as defined | in  | application | source | codes. | Existing |     | invasive dis- |     |     |     |     |     |     |
| ---------- | --- | ----------- | ------ | ------ | -------- | --- | ------------- | --- | --- | --- | --- | --- | --- |
Goal3:Highaccuracy.ZeroTracershouldensureaccurate
tributed tracing systems can produce accurate traces by man- requesttracingthroughmicroserviceapplications,evenif
ually propagating trace contexts through requests (Fig. 1), but theyareimplementedinmulti-threadedorcoroutine-based
| fall short | in trace | accuracy | when | applications |     | handle | requests |     |     |     |     |     |     |
| ---------- | -------- | -------- | ---- | ------------ | --- | ------ | -------- | --- | --- | --- | --- | --- | --- |
architectures.
(cid:2)
across multiple threads or coroutines with third-party library Goal 4: Low overhead. ZeroTracer should track requests
instrumentation.Forinstance,asillustratedinFig.2(b),Jaeger
(cid:2) withalowoverhead.
withthird-partylibraryinstrumentationfragmentsanend-to-end Goal 5: Online tracing. ZeroTracer should provide real-
requestservedbythemulti-threadedTrainticketapplication(see timeobservabilityofmicroservicesystems,enablingrapid
SectionV).
identificationandresolutionofperformanceissues.
Given the drawbacks of current invasive distributed tracing Note: As HTTP is widely used in 54% -87.5% of existing
systems, developers are exploring the implementation of gen- microservice systems, provided by the top-2 Chinese cloud
| eral non-invasive |     | distributed |     | tracing | systems. | These | systems |     |     |     |     |     |     |
| ----------------- | --- | ----------- | --- | ------- | -------- | ----- | ------- | --- | --- | --- | --- | --- | --- |
platformprovider,ZeroTraceraimstoimplementHTTPrequest
| operate  | independently |              | of high-level |            | languages, | aiming           | to re-      | tracing.    |     |     |     |     |     |
| -------- | ------------- | ------------ | ------------- | ---------- | ---------- | ---------------- | ----------- | ----------- | --- | --- | --- | --- | --- |
| duce the | maintenance   |              | costs         | on tracing | code       | instrumentation. |             |             |     |     |     |     |     |
| However, | these         | non-invasive |               | systems    | also       | exhibit          | some short- |             |     |     |     |     |     |
|          | (cid:2)       |              |               |            |            |                  |             | B. WhyeBPF? |     |     |     |     |     |
| comings. | 1 Inaccuracy  |              | in inferred   |            | request    | causality:       | Existing    |             |     |     |     |     |     |
non-invasive distributed tracing systems [19], [20] commonly BPF (Berkeley Packet Filter) [26] was designed for packet
rely on algorithms to infer request causality without requiring filteringandlaterextendedaseBPF(extendedBPF)[21],[22]
any code instrumentation in microservice applications. How- toenableuser-definedevent-triggeredprogramstoexecuteinthe
ever, their refactored request causality may be inaccurate due Linuxkernel.eBPFprovidesasetofnetworkhooksforeBPF
to their lack of insights into application implementations. For programs to be attached, thereby enhancing network capabili-
instance, Deepflow [20] fails to track certain end-to-end re- ties[27],[28],[29],[30],[31],[32],[33].
quests under specific workloads or within complex microser- ZeroTracer utilizes eBPF rather than LKM (Linux Ker-
viceapplicationsduetolimitationsinitsaggregationalgorithm nel Module) [34] to execute customized lightweight programs
(see Sections V-C and V-D). Fig. 2(c) illustrates one of the withintheLinuxkernel,aseBPFhaspredefinedhooksonLinux
inaccuratetracesgeneratedbyDeepflowforthemulti-threaded network kernel functions and owns strict security verification.
Trainticket application. (cid:2) Lack of support for online tracing: In contrast to existing non-invasive tracing systems that em-
2
Existingnon-invasivedistributedtracingsystemsrelyonoffline ploy eBPF solely as a monitor or span generator, ZeroTracer
analysisandcannotsupportreal-timerequesttracing.Moreover, adoptseBPFasatracegeneratorforonlinein-bandend-to-end
the significant volume of data gathered within a large-scale request tracing. By attaching eBPF programs to kernel and
microservice system can adversely impact the performance of user functions as well as sockets, ZeroTracer propagates trace
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on March 20,2026 at 23:38:08 UTC from IEEE Xplore.  Restrictions apply.

YANGetal.:ZEROTRACER:IN-BANDeBPF-BASEDTRACEGENERATORWITHZEROINSTRUMENTATIONFORMICROSERVICESYSTEMS 1481
|     |     |     |     |     |     |     |     | Fig.4. Tracecontextinjectionandextraction. |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------ | --- | --- | --- | --- | --- | --- |
thiscontextalongsidemessagesthroughthenetwork,andthen
throughtheservicesthemselves.
Fig.3. AnoverviewoftheworkflowofZeroTracer. 1) ContextGeneration:
Inspiredbyexistingdistributedtrac-
|     |     |     |     |     |     |     |     | ing systems  | [12], [14], | [15], | ZeroTracer      | divides | a request  | into    |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ----------- | ----- | --------------- | ------- | ---------- | ------- |
|     |     |     |     |     |     |     |     | two separate | operations: | the   | client requests |         | the server | and the |
contextsthroughrequestsinthekernel.Thisapproachenables
ZeroTracer to achieve end-to-end request tracing without any serverrespondstotheclient.Eachofthesetwooperationscanbe
viewedasaspaninanend-to-endrequest.Thelatencyofthese
instrumentationintomicroserviceapplications,therebysupport-
twospansismeasuredbytimestampsrecordedwhenmessages
| ing their | implementations |     | across | various | high-level | languages |     |     |     |     |     |     |     |     |
| --------- | --------------- | --- | ------ | ------- | ---------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
(Goal 1, 2). Notably, ZeroTracer predominantly utilizes the aresentandreceived.Thespangeneratedbytheentryservice
whenitisservingtheentryrequestisregardedastherootspan
| hash eBPF | Maps, | which | serve | as  | efficient | hash tables, | for |     |     |     |     |     |     |     |
| --------- | ----- | ----- | ----- | --- | --------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
temporarykey-valuedatastores.BenefitingfromexistingeBPF of a trace. The other operations to serve that entry request are
wrappers[35],[36],ZeroTraceisimplementedbylibbpfforits allconsideredaschildrenspansofthatrootspan.
Tomakeend-to-endrequestsdistinguishable,ZeroTraceras-
lowoverhead(Goal4).
signsauniqueidentifierknownasthetraceIDtoeachend-to-
|     |     |      |              |     |     |     |     | end request. | Similarly,        | individual | operations |            | in an end-to-end |     |
| --- | --- | ---- | ------------ | --- | --- | --- | --- | ------------ | ----------------- | ---------- | ---------- | ---------- | ---------------- | --- |
|     |     | III. | SYSTEMDESIGN |     |     |     |     |              |                   |            |            |            |                  |     |
|     |     |      |              |     |     |     |     | request      | are distinguished | by         | span IDs.  | ZeroTracer | generates        |     |
A. Overview theseuniquetracecontextsaccordingtoestablishedrulesused
inproductionenvironments,adheringtothewidelyrecognized
| In this | paper, | we propose |     | a non-invasive |     | eBPF-based | dis- |     |     |     |     |     |     |     |
| ------- | ------ | ---------- | --- | -------------- | --- | ---------- | ---- | --- | --- | --- | --- | --- | --- | --- |
OpenTelemetrystandard.TraceIDisa16-bytevalueincluding
tributedtracingframework,namelyZeroTracer.Fig.3showsthe
|     |     |     |     |     |     |     |     | a 32-bit | host IP address, | a 52-bit | timestamp |     | indicating | when |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ---------------- | -------- | --------- | --- | ---------- | ---- |
workflowofZeroTracer,whereredlinesrepresentthedirection
ofmessagetransmissionandblacklinesrepresentthedataflow the end-to-end request entries, a 16-bit sequence number rep-
|                |     |            |       |          |      |          |        | resenting | the order of | requests | to  | the entry | service, | a 4-bit |
| -------------- | --- | ---------- | ----- | -------- | ---- | -------- | ------ | --------- | ------------ | -------- | --- | --------- | -------- | ------- |
| of ZeroTracer. |     | ZeroTracer | first | attaches | eBPF | programs | to the |           |              |          |     |           |          |         |
debuggingtagusedbydevelopers,anda24-bitrunningprocess
kernelfunctionsofeachhostonmessagetransferring,suchas
sendmsg recvmsg. ID.Meanwhile,spanIDisan8-bytevaluecomprisingthe16-bit
|     | and |     | When | a   | service | receives a | request |     |     |     |     |     |     |     |
| --- | --- | --- | ---- | --- | ------- | ---------- | ------- | --- | --- | --- | --- | --- | --- | --- |
IPaddressesoftheclientandserver,aswellasa32-bitsequence
| from its | downstream, |     | the eBPF | program | on  | the receiving | side |     |     |     |     |     |     |     |
| -------- | ----------- | --- | -------- | ------- | --- | ------------- | ---- | --- | --- | --- | --- | --- | --- | --- |
numberdenotingtheorderofthespanwithintheentiretrace.
| parses | and extracts | a   | trace context | from | the | received | message |     |     |     |     |     |     |     |
| ------ | ------------ | --- | ------------- | ---- | --- | -------- | ------- | --- | --- | --- | --- | --- | --- | --- |
ifithas,orgeneratesatracecontextifnot(step❶).TheeBPF 2) Inter-Service Context Propagation: After generating a
uniquetracecontextforeachoperationinanend-to-endrequest,
| program | then stores | the | context | into | an eBPF | map as | a parent |     |     |     |     |     |     |     |
| ------- | ----------- | --- | ------- | ---- | ------- | ------ | -------- | --- | --- | --- | --- | --- | --- | --- |
trace context (step ❷). When the service sends a request to ZeroTracer has to propagate these contexts between services.
ByanalyzingtheformatofHTTPrequests,ZeroTracerutilizes
| its upstream, | the | eBPF | program | on  | the sending | side | queries |     |     |     |     |     |     |     |
| ------------- | --- | ---- | ------- | --- | ----------- | ---- | ------- | --- | --- | --- | --- | --- | --- | --- |
thekey-valueheaderofHTTPrequestsastheoptimallocation
theparenttracecontext(step❸),thengeneratesitschildtrace
context(step❹),andinjectsthechildcontextintothesending for carrying trace contexts, thereby facilitating online request
|     |     |     |     |     |     |     |     | tracing | (Goal 5). Along | with | HTTP | requests, | trace contexts |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | --------------- | ---- | ---- | --------- | -------------- | --- |
message(step❺).Ifarequestisfinished,theeBPFprogramswill
pushthegeneratedtracesandspansintoaringbuffer,aneBPF can easily travel across the network, transferred between two
❻). services.Moreover,sincetheinjectionoftracecontextsdoesnot
| map (step |     | An agent | is deployed |     | on each | host to | facilitate |     |     |     |     |     |     |     |
| --------- | --- | -------- | ----------- | --- | ------- | ------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
alterthepayload,itensuresthatthenormalprocessingoforiginal
accesstothegeneratedtraces.Thisagentretrievestracesfrom
requestsbymicroserviceapplicationsremainsundisturbed.
| the ringbuffer |     | and exports | them | to  | databases | following | the |     |     |     |     |     |     |     |
| -------------- | --- | ----------- | ---- | --- | --------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
AsdepictedinFig.4,whenaservicesendsanHTTPrequest
| OpenTelemetry |     | standard. | Users | can | then access | and | visualize |     |     |     |     |     |     |     |
| ------------- | --- | --------- | ----- | --- | ----------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
thesetracesthroughacustomizeduserinterfacetailoredtotheir to its upstream, ZeroTracer injects a trace context as custom
|     |     |     |     |     |     |     |     | key-value | pairs into the | header | of  | the HTTP | request | before |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | -------------- | ------ | --- | -------- | ------- | ------ |
needs.
|     |     |     |     |     |     |     |     | transmission. | This injection |          | increases | the    | message length | by  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | -------------- | -------- | --------- | ------ | -------------- | --- |
|     |     |     |     |     |     |     |     | 32 bytes,     | from 244       | bytes to | 276       | bytes. | Upon receiving | an  |
B. TraceGeneration
HTTPrequestfromthedownstreamcontainingourcustomized
In order to track end-to-end requests and generate traces, tracecontext,ZeroTracerinterceptstherequestandextractsthe
ZeroTracerfirstgeneratesauniquetracecontextforeachoper- context without impacting the message length, which remains
| ationwithintheend-to-endrequest.Subsequently,itpropagates |     |     |     |     |     |     |     | at276bytes. |     |     |     |     |     |     |
| --------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- |
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on March 20,2026 at 23:38:08 UTC from IEEE Xplore.  Restrictions apply.

1482 IEEETRANSACTIONSONPARALLELANDDISTRIBUTEDSYSTEMS,VOL.36,NO.7,JULY2025
3) Intra-Service Context Propagation: To achieve accurate
end-to-endrequesttracing,ZeroTracershouldeffectivelyprop-
agate the trace context through each service of a microservice
applicationfromitsdownstreamrequesttoitsupstreamrequest
(Goal3).
While existing invasive distributed tracing systems rely on
instrumenting tracing codes in applications or third-party li-
brariestoimplementcontextpropagation,ZeroTracerfacesthe
challenge of achieving trace context propagation in the kernel
withoutanycodeinstrumentation,sinceZeroTracerhaslimited
knowledgeofhowarunningapplicationservesitsuserrequest.
Toaddressthischallenge,weanalyzetheworkflowofservices
inmicroserviceapplicationstounderstandhowtheyserveauser
request. As one service is scheduled on one user process to
executebytheoperatingsystem,weobservethatthescheduling
of a running service on a user process remains consistent.
Leveragingthisinsight,ZeroTracercanmonitortheuserthread
creationandexecutioninthekerneltounderstandtheexecution
ofuserthreadsaswellastheirparent-childrelationshipswithin
theserviceprocess.Asaresult,ZeroTracergainsthecapability
Fig.5. Implementationsofmicroservicesonhowtheyservearequest.
topropagatetracecontextwiththerelationshipsamongthreads
andwithoutanycodeinstrumentationinthekernel,regardless
ofthevarioushigh-levellanguageimplementations(Goals1,2, parent-childrelationshipsamongthreads.Leveragingthesere-
and3). lationships,ZeroTracercanimplementcontextpropagationfor
Servicesprimarilyserverequestsintwomodes. suchmulti-threadedservices.ZeroTracerfirststoresthereceived
(cid:2)
Single-threaded mode: Single-threaded services serve a tracecontextastheparenttracecontextwiththeparentthread
requestwithinasinglethread.Iftheservingthreadrequires ID as the key. When the child thread sends a message to the
requestingitsupstreams,itwillsendtherequestandwait upstream,ZeroTracerqueriesitsparentthreadID,retrievesthe
fortheresponsewithinthesamethread. parenttracecontext,generatesachildtracecontext,andinjects
(cid:2)
Multi-threaded mode: Multi-threaded services always itintothethesendingmessage.
servearequestwithmultiplecollaboratingthreadsoreven Inmorecomplexscenarios,multi-threadedservicespreferto
coroutines.Whentheservingthreadrequestsitsupstream utilizethreadpools,evencoroutinestoenhanceperformance
forservices,theservicecreatesorschedulesoneofitsidle by mitigating the system resource overhead associated with
threadstorequesttheupstreamandcontinuestoservethe frequentthreadcreationanddestruction.Fig.5(c)displayshow
userrequestwithnowait. a thread-pool service serves requests. When serving a down-
Basedonthesetwoimplementations,wediscusshowZero- stream request, the service creates some collaborative tasks or
Tracerpropagatestracecontextsthroughservicesasfollows. coroutinestoexecutevarioustasks,suchasrequestingupstream
For single-threaded services, ZeroTracer propagates trace servicesorreadingafile.Thesecreatedtasksorcoroutinesare
contextsusingtheuniqueidentifierofeachthread,knownasthe thenputintoaqueue,waitingtobescheduledonanidlethread
thread ID. Since a thread serves a request synchronously and in the thread pool to execute. If a thread finishes its running
individually(seeFig.5(a)),ZeroTracerfirststorestheextracted task, it will be recycled back into the thread pool and remain
trace context with the thread ID as a key when receiving a idle until another task is scheduled on it. Although tasks and
request from the downstream. Subsequently, when the service coroutinesofferfine-grainedresourceallocationandscheduling
forwards a request to its upstream to fulfill the downstream inuserspacetooptimizeserviceperformance,propagatingtrace
request, ZeroTracer retrieves the trace context associated with contextthroughsuchacomplexthread-poolservicepresentsa
thesamethreadIDastheparenttracecontext.ZeroTracerthen formidablechallengeinthekernel.
generates a child trace context and injects it into the outgoing Fig.6showstheworkflowofZeroTracertopropagatetrace
upstream request. Withthe samethread ID,tracecontexts can contexts through thread-pool services. In thread-pool environ-
be propagated through the single-threaded services to achieve ments,wheredifferenttaskscanbescheduledonthesamethread
end-to-endrequesttracinginsingle-threadedservices. forexecution,theconventionalapproachofpropagatingcontext
Formulti-threadedservices,wheretasksareparallelizedto usingthreadIDs,asemployedinsimplemulti-threadedscenar-
enhance service performance, ZeroTracer encounters a more ios, proves inadequate. To accurately propagate trace contexts
complexscenario.Inthesimplestscenarioofamulti-threaded in thread-pool services, ZeroTracer has to gain insights into
service, when a thread serves a downstream request, it forks the scheduling of tasks or coroutines on threads. By attaching
or clones a new thread to request its upstream (see Fig. 5(b)). aneBPFprogramontaskcreationevents,ZeroTracercaptures
By monitoring the thread creation, ZeroTracer establishes the theparent-childrelationshipsamongtasks.Theschedulingand
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on March 20,2026 at 23:38:08 UTC from IEEE Xplore. Restrictions apply.

YANGetal.:ZEROTRACER:IN-BANDeBPF-BASEDTRACEGENERATORWITHZEROINSTRUMENTATIONFORMICROSERVICESYSTEMS 1483
TABLEII
IMPORTANTMOUNTINGHOOKSOFEBPFPROGRAMSINZEROTRACER
Fig.6. ThesolutionofZeroTracertopropagatetracecontextsthroughthread-
poolservices.
executionoftasksonthreadsaremonitoredtogatherscheduling A. ContextGeneration
details.Whenathreadreceivesadownstreamrequestalongside ByparsingandmatchingmessagesinHTTPrequestformat
atracecontext,ZeroTracerstoresthiscontextastheparenttrace
|     |     |     |     |     |     |     |     | when a service |     | sends | a request | to its | upstream | or  | receives a |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ----- | --------- | ------ | -------- | --- | ---------- |
context,associatingitwithauniqueidentifieroftheexecuting
requestfromitsdownstream,ZeroTracergenerates8-bytespan
| task as | the key, known | as  | the task | ID. | Subsequently, |     | when | a       |         |       |     |          |           |           |     |
| ------- | -------------- | --- | -------- | --- | ------------- | --- | ---- | ------- | ------- | ----- | --- | -------- | --------- | --------- | --- |
|         |                |     |          |     |               |     |      | IDs and | 16-byte | trace | IDs | based on | the rules | mentioned | in  |
threadisrequestinganupstreamservice,ZeroTracerfirstqueries
|     |     |     |     |     |     |     |     | Section III-B1. |     | In addition, |     | thanks to | the service | management |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- | ------------ | --- | --------- | ----------- | ---------- | --- |
whether the executing task owns a trace context. If so, this provided by Kubernetes [37], each service and its instances
| context    | will be treated | as  | the parent | trace | context.      | Otherwise, |     |            |             |         |            |           |      |            |            |
| ---------- | --------------- | --- | ---------- | ----- | ------------- | ---------- | --- | ---------- | ----------- | ------- | ---------- | --------- | ---- | ---------- | ---------- |
|            |                 |     |            |       |               |            |     | have their | IP address. |         | By message | filtering |      | with IP    | addresses, |
| ZeroTracer | will query      | for | the parent |       | trace context | associated |     |            |             |         |            |           |      |            |            |
|            |                 |     |            |       |               |            |     | ZeroTracer | can         | further | reduce     | the time  | cost | on message | pars-      |
with the parent task of the executing task. Then ZeroTracer ingandrequesttracingfornon-targetrequests,thusimproving
| generates | a child | trace context |     | and injects | it  | into the | sending |     |     |     |     |     |     |     |     |
| --------- | ------- | ------------- | --- | ----------- | --- | -------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
theperformanceofend-to-endrequesttracingformicroservice
message.Byleveragingfine-grainedschedulinginformationand applications(Goal4).
| parent-child | relationships |     | among | tasks, | ZeroTracer | effectively |     |     |     |     |     |     |     |     |     |
| ------------ | ------------- | --- | ----- | ------ | ---------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
propagatescontextthroughthread-poolservices.
B. Inter-ServiceContextPropagation
|     |     |     |     |     |     |     |     | For trace    | context |     | propagation | between     |      | services, | the gen- |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ------- | --- | ----------- | ----------- | ---- | --------- | -------- |
|     |     |     |     |     |     |     |     | erated trace | context |     | must        | be injected | into | outgoing  | re-      |
C. TraceCollectionandVisualization
|      |                |      |      |           |     |                |     | quests to         | upstreams |         | and extracted | from                  | incoming |     | requests  |
| ---- | -------------- | ---- | ---- | --------- | --- | -------------- | --- | ----------------- | --------- | ------- | ------------- | --------------------- | -------- | --- | --------- |
| Once | trace contexts | have | been | generated |     | and propagated |     |                   |           |         |               |                       |          |     |           |
|      |                |      |      |           |     |                |     | from downstreams. |           | Details |               | on the implementation |          |     | of inter- |
acrossthenetworkandthroughservices,ZeroTracerconstructsa
|     |     |     |     |     |     |     |     | service | context | propagation |     | are illustrated |     | in  | Fig. 7. To |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ------- | ----------- | --- | --------------- | --- | --- | ---------- |
uniquetraceforeachfinishedend-to-endrequest.Tracesalong
|                  |            |           |       |               |          |                 |          | achieve                 | this seamlessly, |          | ZeroTracer |           | implements    |               | a sk_msg    |
| ---------------- | ---------- | --------- | ----- | ------------- | -------- | --------------- | -------- | ----------------------- | ---------------- | -------- | ---------- | --------- | ------------- | ------------- | ----------- |
| with their       | spans are  | pushed    | into  | a ringbuffer, |          | an eBPF         | map,     |                         |                  |          |            |           |               |               |             |
|                  |            |           |       |               |          |                 |          | program                 | to intercept     |          | outbound   | HTTP      | requests      | and           | inject cus- |
| and subsequently |            | retrieved | by an | agent         | deployed | on the          | host.    |                         |                  |          |            |           |               |               |             |
|                  |            |           |       |               |          |                 |          | tomized                 | trace            | contexts | without    | user      | intervention. |               | Benefiting  |
| For long-term    | storage,   | the       | agent | exports       | these    | traces          | to local |                         |                  |          |            |           |               |               |             |
|                  |            |           |       |               |          |                 |          | from bpf_msg_push_data, |                  |          |            | an eBPF   | helper        | function,     | the         |
| or external      | databases. | Traces    | in    | the databases |          | can be accessed |          |                         |                  |          |            |           |               |               |             |
|                  |            |           |       |               |          |                 |          | sk_msg                  | program          | first    | splits     | a message | into          | two fragments | in          |
andvisualizedwithadashboardtobetterhelpdevelopersdebug
|            |            |          |               |                  |      |            |       | a scatter       | list, then | injects | our      | customized | trace | context | as the       |
| ---------- | ---------- | -------- | ------------- | ---------------- | ---- | ---------- | ----- | --------------- | ---------- | ------- | -------- | ---------- | ----- | ------- | ------------ |
| anomalous  | end-to-end | requests |               | and troubleshoot |      | faults.    | To be |                 |            |         |          |            |       |         |              |
|            |            |          |               |                  |      |            |       | first key-value |            | data in | the HTTP | header     | after | the     | request line |
| compatible | with the   | existing | visualization |                  | user | interface, | our   |                 |            |         |          |            |       |         |              |
inthefirstfragment(Line9-10).Aftercontextinjection,these
| agent transforms |     | the generated |     | traces | into the | standard | format |     |     |     |     |     |     |     |     |
| ---------------- | --- | ------------- | --- | ------ | -------- | -------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
twofragmentsaremergedbackintoarequesttobesent.When
ofOpenTelemetrybeforeexportingthemintodatabases.
|     |     |     |     |     |     |     |     | the service | receives | the | downstream | request |     | alongside | a trace |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | -------- | --- | ---------- | ------- | --- | --------- | ------- |
context,ourkprobeandkretprobeprogramshookedonthe
|     |     |                    |     |     |     |     |     | kernel function |         | sock_recvmsg |          | help  | parse   | that downstream |            |
| --- | --- | ------------------ | --- | --- | --- | --- | --- | --------------- | ------- | ------------ | -------- | ----- | ------- | --------------- | ---------- |
|     |     | IV. IMPLEMENTATION |     |     |     |     |     |                 |         |              |          |       |         |                 |            |
|     |     |                    |     |     |     |     |     | request and     | extract | our          | injected | trace | context | (Line           | 1-3), then |
ZeroTracer is implemented in C/C++ with about 2000 lines storethecontextwiththethreadIDortaskIDforintra-service
for the in-kernel eBPF programs and about 1500 lines for the contextpropagation(Line4-7).
hostagent.ZeroTracerutilizessixtypesoftheeBPFprogramsto In our implementation, the request line can be recognized
realize a non-invasive distributed tracing system: sock_ops, by the hexadecimal ending symbol 0x0d0a of each line in
sk_msg,kprobe,kretprobe,uprobe,anduretprobe.
|     |     |     |     |     |     |     |     | an HTTP | request | (Line | 4-8). | By injecting |     | trace | contexts in |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ------- | ----- | ----- | ------------ | --- | ----- | ----------- |
TableIIshowstheirfunctionalitiesindetail. the first place of the header after the request line, ZeroTracer
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on March 20,2026 at 23:38:08 UTC from IEEE Xplore.  Restrictions apply.

1484 IEEETRANSACTIONSONPARALLELANDDISTRIBUTEDSYSTEMS,VOL.36,NO.7,JULY2025
|     |     |     |     |     |     |     |     | Fig.8. ThreadIDassignmentinLinux.EachthreadIDinthechildnamespace |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
hasauniqueIDineachofitsparentnamespaces.
|     |     |     |     |     |     |     |     | ZeroTracer | needs | toknowabout |     | theparent-childrelationships |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ----- | ----------- | --- | ---------------------------- | --- | --- | --- |
amongthreads,tasks,andcoroutines,aswellasthescheduling
informationoftasksandcoroutinesonthreads.
|     |     |     |     |     |     |     |     | In microservice |            | systems,         | services   |          | are deployed | in        | contain- |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | ---------- | ---------------- | ---------- | -------- | ------------ | --------- | -------- |
|     |     |     |     |     |     |     |     | ers to achieve  |            | fast deployment. |            | However, | resource     | isolation | in       |
|     |     |     |     |     |     |     |     | container       | namespaces |                  | [38] makes | it       | a challenge  | to        | build up |
parent-childrelationshipsamongthreadsinthekernel.Threads
ofacontainerizedserviceexecuteintheircontainernamespace
andareassigneduniqueIDsofthatnamespaceandsodoinits
parentnamespaces,suchastheroot(host)namespace.TheIDs
ofathreadaredifferentfromnamespaces.Insteadofdeploying
ZeroTracerineachcontainernamespace,whichconsumesmore
|             |                |              |            |         |                   |               |               | system resources, |     | ZeroTracer |          | operates   | in the          | root namespace, |     |
| ----------- | -------------- | ------------ | ---------- | ------- | ----------------- | ------------- | ------------- | ----------------- | --- | ---------- | -------- | ---------- | --------------- | --------------- | --- |
| Fig. 7.     | Implementation | of           | the sk_msg | program | and               | the kretprobe | pro-          |                   |     |            |          |            |                 |                 |     |
|             |                |              |            |         |                   |               |               | while services    |     | execute    | in their | respective | child           | namespaces.     |     |
| gram hooked | on the         | sock_recvmsg | function   |         | for inter-service |               | trace context |                   |     |            |          |            |                 |                 |     |
|             |                |              |            |         |                   |               |               | This disparity    |     | in thread  | IDs      | introduces | inconsistencies |                 | and |
propagation.
|     |     |     |     |     |     |     |     | inaccuracies | in  | establishing | parent-child |     | relationships |     | among |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ------------ | ------------ | --- | ------------- | --- | ----- |
threadswhenmonitoringthekernelfunctionforkandclone
decreasesthenumberofoperatinginstructionsneededtolocate
|                 |     |          |            |     |             |            |     | in the root | namespace. |     | Since different |     | threads | may utilize | the |
| --------------- | --- | -------- | ---------- | --- | ----------- | ---------- | --- | ----------- | ---------- | --- | --------------- | --- | ------- | ----------- | --- |
| other key-value |     | pairs in | the header |     | for context | injection, | as  |             |            |     |                 |     |         |             |     |
samethreadIDintheirrespectivenamespaces,retrievingthread
eBPFhasanupperlimitonthenumberofinstructionsforeach
|     |     |     |     |     |     |     |     | IDs within | child | namespaces |     | using | these functions |     | can lead |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ----- | ---------- | --- | ----- | --------------- | --- | -------- |
eBPFprogramduetoitssecurityconsiderations.Wechooseto
ZeroTracertotheinaccuracyinestablishingparent-childthread
implementtracecontextinjectionatthesocketlayerratherthan
|     |     |     |     |     |     |     |     | relationships. | To  | meet | this problem, |     | we try to | figure | out how |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ---- | ------------- | --- | --------- | ------ | ------- |
thetransportlayerandlowertoavoidtheimpactofthetransport
|            |            |     |          |      |           |                |     | ZeroTracer | can | obtain | the thread | IDs | of the containerized |     | ser- |
| ---------- | ---------- | --- | -------- | ---- | --------- | -------------- | --- | ---------- | --- | ------ | ---------- | --- | -------------------- | --- | ---- |
| mechanisms | on request |     | tracing, | such | as packet | subcontracting |     |            |     |        |            |     |                      |     |      |
vicesintherootnamespace.Fig.8showsthedatastructureof
andretransmission.
|     |     |     |     |     |     |     |     | a thread | in Linux, | where | a thread | is  | regarded | as a process | to  |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | --------- | ----- | -------- | --- | -------- | ------------ | --- |
Inpractice,thelengthoftherequestlineinanHTTPrequest
|     |     |     |     |     |     |     |     | execute. | Each | thread records | its | namespace | level | in a | variable |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ---- | -------------- | --- | --------- | ----- | ---- | -------- |
isvariable,soeBPFprogramshavetotraversetheHTTPrequest
calledlevelandmaintainsitsthreadIDsforeachnamespace
| messages | to figure | out the | first | ending | symbol | 0x0d0a | (Line |     |     |     |     |     |     |     |     |
| -------- | --------- | ------- | ----- | ------ | ------ | ------ | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
inanarraynamednumber.TheseIDsarerecordedfollowing
4-8)andinjectthegeneratedcontexts(Line9-10).However,the
theparent-childrelationshipsofnamespaces,startingfromthe
traversalforthelongerrequestlineinoneeBPFprogrammakes
parentnamespaceandendingwiththecurrentnamespace.When
itoutofitslimitationonthenumberofrunninginstructions.To
anewthreadisforked,itisallocatednewIDsinallitslocated
meetthisproblem,ZeroTraceremploysthetailcallmechanism
|     |     |     |     |     |     |     |     | namespaces | by  | calling | the kernel | function | alloc_pid. |     | The |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | ------- | ---------- | -------- | ---------- | --- | --- |
ofeBPFtoincreasethenumberofavailableeBPFinstructions,
kprobeprogramonthatfunctioncanhelpZeroTracertoobtain
| as highlighted | by  | the orange | boxes |     | in Fig. | 7. ZeroTracer | di- |     |     |     |     |     |     |     |     |
| -------------- | --- | ---------- | ----- | --- | ------- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
thestructureofathreadandparseitsIDintherootnamespace,
| vides the | process | of injecting |     | a trace | context | into | three parts: |     |     |     |     |     |     |     |     |
| --------- | ------- | ------------ | --- | ------- | ------- | ---- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
thusZeroTracerisabletokeeptheconsistencywhenestablishing
| generating | the context | to  | be injected |     | (Line | 1-3), | finding the |     |     |     |     |     |     |     |     |
| ---------- | ----------- | --- | ----------- | --- | ----- | ----- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
theparent-childrelationshipsofthreads(usedinLine20,Fig.
| injection | location | (Line | 4-8), | and injecting |     | the context | (Line |     |     |     |     |     |     |     |     |
| --------- | -------- | ----- | ----- | ------------- | --- | ----------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
9).
| 9-10). Each       | is implemented |        | by       | an eBPF   | program.     |     | By calling   |               |        |               |         |          |              |            |         |
| ----------------- | -------------- | ------ | -------- | --------- | ------------ | --- | ------------ | ------------- | ------ | ------------- | ------- | -------- | ------------ | ---------- | ------- |
|                   |                |        |          |           |              |     |              | To facilitate |        | intra-service | context |          | propagation, | ZeroTracer |         |
| the bpf_tail_call |                | helper |          | function, | ZeroTracer   |     | can easily   |               |        |               |         |          |              |            |         |
|                   |                |        |          |           |              |     |              | utilizes      | uprobe | and uretprobe |         | programs |              | attached   | to task |
| utilize these     | three          | eBPF   | programs | to        | successfully |     | inject trace |               |        |               |         |          |              |            |         |
schedulingandcreationfunctions.TheseprogramsenableZe-
contextsintorequestsandthenpropagatethemacrossservices.
roTracertogatherparent-childrelationshipsamongtasks,along
withtheirschedulingdetailsonthreads(usedinLine1,Line6,
C. Intra-ServiceContextPropagation
andLine11inFig.9).Duringcontextpropagation,ZeroTracer
As analyzed in Section III-B3, propagating trace contexts initiallystorestheextractedparenttracecontextusingthetask
through services requires implementing the lookupCon- ID as the key. If no running task is present, it changes to
textByThreadID
function used in the sk_msg program use the thread ID as the key. When a service sends requests
(Line 2 in Fig. 7, with details in Fig. 9). To achieve this, to upstreams, ZeroTracer queries the parent trace context and
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on March 20,2026 at 23:38:08 UTC from IEEE Xplore.  Restrictions apply.

YANGetal.:ZEROTRACER:IN-BANDeBPF-BASEDTRACEGENERATORWITHZEROINSTRUMENTATIONFORMICROSERVICESYSTEMS 1485
|     |     |     |     |     |     |     |     | Fig.10. | AnexampleofaservingfunctioninGolangwithitsgeneratedparent- |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ---------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
childtreeofcoroutines.
functionaddresses.Toovercomethis,ZeroTracercanleverage
bytecodeinstrumentationtoolslikejavaagent[39]tohookkey
userfunctions,suchastaskschedulingandtaskcreation.This
|     |     |     |     |     |     |     |     | enables     | ZeroTracer | to understand |         | scheduling      |     | relationships | be- |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ---------- | ------------- | ------- | --------------- | --- | ------------- | --- |
|     |     |     |     |     |     |     |     | tween tasks | and        | threads,      | as well | as parent-child |     | relationships |     |
betweentasks,facilitatingintra-servicecontextpropagation.
|     |     |     |     |     |     |     |     | As shown       | in  | Fig. 10,   | a Golang   | service  | using   | “net/http”  | li-      |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ---------- | ---------- | -------- | ------- | ----------- | -------- |
|     |     |     |     |     |     |     |     | brary employs  |     | multiple   | coroutines | to serve | an      | HTTP        | request. |
|     |     |     |     |     |     |     |     | Once receiving |     | a request, | the        | service  | creates | a coroutine | to       |
Fig.9. Implementationofthefunctiononlookingupthetracecontextby
|     |     |     |     |     |     |     |     | execute | the serving | function | shown | in  | Fig. 10(a). | The | serving |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ----------- | -------- | ----- | --- | ----------- | --- | ------- |
threadID.
|     |     |     |     |     |     |     |     | coroutinethencreateschildcoroutines |     |     |     |     | tohandlevarious |     | tasks |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------------------------- | --- | --- | --- | --- | --------------- | --- | ----- |
suchasreadingrequestcontent,sendingrequeststoupstreams,
generatesacorrespondingchildtracecontextforinjection.The
|                                                  |         |     |     |            |       |            |       | processing | responses, | and            | other | operations. | This         | hierarchy | of      |
| ------------------------------------------------ | ------- | --- | --- | ---------- | ----- | ---------- | ----- | ---------- | ---------- | -------------- | ----- | ----------- | ------------ | --------- | ------- |
| lookupprocedureisshowninFig.9.Ifathreadscheduled |         |     |     |            |       |            | for   |            |            |                |       |             |              |           |         |
|                                                  |         |     |     |            |       |            |       | coroutines | forms      | a parent-child |       | tree,       | illustrating | the       | flow of |
| an upstream                                      | request | has | an  | associated | task, | ZeroTracer | first |            |            |                |       |             |              |           |         |
operationswithintheservice,asshowninFig.10(b).Toprop-
| searches | for the | trace | context | using | the task | ID (Line | 3-4). | If  |     |     |     |     |     |     |     |
| -------- | ------- | ----- | ------- | ----- | -------- | -------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
agatecontextthroughsuchaGolangservice,ZeroTracerhooks
notfound,itcontinuestotraverseuptheparent-childhierarchy
uprobeanduretprobeprogramsontheuserfunctionrun-
| until a valid | trace | context | is  | found | or the | predefined | level of |     |     |     |     |     |     |     |     |
| ------------- | ----- | ------- | --- | ----- | ------ | ---------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
time.newproc1tocaptureparent-childrelationshipamong
(L)
hierarchy is reached (Line 6-14). If the trace context of run-
|               |       |          |               |     |       |            |             | coroutines   | (used | in Line   | 6 and     | 11 in | Fig. 9)    | and         | on  |
| ------------- | ----- | -------- | ------------- | --- | ----- | ---------- | ----------- | ------------ | ----- | --------- | --------- | ----- | ---------- | ----------- | --- |
| the L-parent  | task  | is still | unrecognized, |     | it is | considered | that no     |              |       |           |           |       |            |             |     |
|               |       |          |               |     |       |            |             | time.execute |       | to obtain | coroutine |       | scheduling | information |     |
| trace context | needs | to       | be propagated |     | (Line | 15). If    | the current |              |       |           |           |       |            |             |     |
onthreads(usedinLine1,Fig.9).Inaddition,theuserfunction
threadisnotperformingatask,ZeroTracerretrievestheparent
HandlerFunc.ServeHTTPishookedbyZeroTracertofind
| trace context | using | the | current | thread | ID  | (Line 17-18), | or  | if  |     |     |     |     |     |     |     |
| ------------- | ----- | --- | ------- | ------ | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
theserving(root)coroutineofeachparent-childtreeofcorou-
| unavailable, | the       | parent | thread   | ID (Line | 20-21). | Once  | the trace   |             |         |     |            |          |     |      |           |
| ------------ | --------- | ------ | -------- | -------- | ------- | ----- | ----------- | ----------- | ------- | --- | ---------- | -------- | --- | ---- | --------- |
|              |           |        |          |          |         |       |             | tines. When | serving | a   | downstream | request, | the | root | coroutine |
| context      | is found, | it is  | regarded | as the   | parent  | trace | context and |             |         |     |            |          |     |      |           |
extractsatracecontextfromthedownstreamrequestandstores
| used to | generate | a child | trace | context | to be | injected | into the |     |     |     |     |     |     |     |     |
| ------- | -------- | ------- | ----- | ------- | ----- | -------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
itwiththerootcoroutineidentifier(coroutineID)asakey.When
requesttotheupstreamtoenablecontextpropagation.Sinceup-
|     |     |     |     |     |     |     |     | a child coroutine |     | sends | a request | to the | upstream, | it  | first finds |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | ----- | --------- | ------ | --------- | --- | ----------- |
streamrequestsaretypicallyparallelizedata1-levelparent-child
|     |     |     |     |     |     |     |     | its belonging | trace | context | with | its coroutine |     | ID. If | it has, its |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | ----- | ------- | ---- | ------------- | --- | ------ | ----------- |
threadrelationship,ZeroTraceronlysearchesfortracecontext
belongingtracecontextisregardedastheparenttracecontext.
atthislevel.Conversely,taskhierarchiestendtobedeeper,so
Ifnot,ZeroTracerqueriesfortheparenttracecontextofitsparent
| ZeroTracer | extends | the | search | to a predefined |     | maximum | level |     |     |     |     |     |     |     |     |
| ---------- | ------- | --- | ------ | --------------- | --- | ------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
coroutinesuntiltherootcoroutine,asillustratedinFig.9.Then
(e.g.,10)fortask-relatedcontexts.
ZeroTracergeneratesachildtracecontextofthefoundedparent
tracecontextandinjectsitintotheupstreamrequest.
D. GolangExampleofIntra-ServiceContextPropagation
|     |     |     |     |     |     |     |     | To keep | the | parent-child |     | relationships | of  | coroutines, | we  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | ------------ | --- | ------------- | --- | ----------- | --- |
TobetterexplainwhichuserfunctionsZeroTracerchoosesto observe that keep-alive connections in the “net/http” library
attachandhowZeroTracerpropagatestracecontextsinthread- may cause wrong parent-child relationships of coroutines. As
poolservices,weshowourimplementationinaGolangservice shown in Fig. 11, the write and read coroutines work with
as an example, which natively implements thread pools in its the keep-alive connections. However, a keep-alive connection
runtime.ForJavaandPython,unlikeGolang,whichallowseBPF canbeacquiredbydifferentcoroutinesforrequestingthesame
programs to hook user functions using the function address, upstream. For example in Fig. 11, a keep-alive connection to
theirpackagedexecutionenvironments,suchastheJavaVirtual anupstreamcanbeacquiredbycoroutine1,andthenreleased
Machine(JVM)andthePythonVirtualMachine(PVM),makeit bycoroutine1andacquiredbycoroutine2.ZeroTracerhasto
challengingforeBPFprogramstoretrieveandattachtodynamic maintainaccurateparent-childrelationshipsofcoroutinesinthis
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on March 20,2026 at 23:38:08 UTC from IEEE Xplore.  Restrictions apply.

1486 IEEETRANSACTIONSONPARALLELANDDISTRIBUTEDSYSTEMS,VOL.36,NO.7,JULY2025
haveusedFortio[40]togenerateuser-definedworkloadstoour
benchmarks,whilethesarcommandhasbeenutilizedtoobtain
theCPUandmemoryusageofeachmachine.
|     |     |     |     |     |     |     |     | 2) Benchmark:   |          | For our      | experiments, |             | we         | have | deployed |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | -------- | ------------ | ------------ | ----------- | ---------- | ---- | -------- |
|     |     |     |     |     |     |     |     | two open-source |          | microservice |              | application | benchmarks |      | as our   |
|     |     |     |     |     |     |     |     | testbed.        | Bookinfo | [41] serves  | as           | an online   | bookstore, |      | written  |
invariousprogramminglanguages,includingPython,andJava.
Trainticket[42]isalarge-scaledistributedtrainticketbooking
systemconsistingof41microservices,writteninJava.Eachser-
Fig.11. Parent-childrelationshipsofcoroutineschangeonakeep-alivecon-
viceofthesetwobenchmarksownsonereplica.Sincethesetwo
nectioninaGolangservice.
benchmarksonlyprovidesingle-threadedexamples,wemodify
thesourcecodesoftheProductpageserviceofBookinfoandthe
| case to achieve |     | trace context | propagation |     | (used in | Line | 6 and |     |     |     |     |     |     |     |     |
| --------------- | --- | ------------- | ----------- | --- | -------- | ---- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
TravelserviceofTraintickettobuildupsimplemulti-threaded
| 11 in Fig. | 9). In | our implementation, |     | ZeroTracer |     | monitors | the |     |     |     |     |     |     |     |     |
| ---------- | ------ | ------------------- | --- | ---------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
applications.
user functions writeloop and readloop to establish the Furthermore, we conducted benchmarks in both single-
owningrelationshipbetweenthereadandwritecoroutinesand
|     |     |     |     |     |     |     |     | threaded | and | multi-threaded | environments |     |     | using | commonly |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | -------------- | ------------ | --- | --- | ----- | -------- |
thekeep-aliveconnections.TheuserfunctionroundTripthen
|                  |     |            |         |           |     |          |     | used high-level |             | languages       | such | as PHP, | Java,         | Python, | and       |
| ---------------- | --- | ---------- | ------- | --------- | --- | -------- | --- | --------------- | ----------- | --------------- | ---- | ------- | ------------- | ------- | --------- |
| helps ZeroTracer |     | know which | serving | coroutine |     | acquires | the |                 |             |                 |      |         |               |         |           |
|                  |     |            |         |           |     |          |     | Golang          | to evaluate | the performance |      |         | of ZeroTracer |         | on track- |
keep-aliveconnection,therebymaintaininganaccurateparent-
|     |     |     |     |     |     |     |     | ing requests | in  | various high-level |     | languages. |     | Each | benchmark |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ------------------ | --- | ---------- | --- | ---- | --------- |
child relationship between the serving coroutine and the read comprises three services: a frontend service, a middle service,
| and write | coroutine | of that | keep-alive | connection. |     | In Fig. | 11, |     |     |     |     |     |     |     |     |
| --------- | --------- | ------- | ---------- | ----------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
andabackendservice.IntheGolangexample,wesimulateda
whenthekeep-aliveconnectionisacquiredbycoroutine1,the multi-threadedenvironmentusingathread-poolmodel.
writeandreadcoroutines5and6recordtheirparentcoroutine
|     |     |     |     |     |     |     |     | 3) Baselines: |     | Jaeger [13] | stands | for | a typical | commonly- |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ----------- | ------ | --- | --------- | --------- | --- |
as1.Whencoroutine2obtainsthesameconnection,coroutine
|     |     |     |     |     |     |     |     | used invasive |     | distributed | tracing | system, | which | adheres | to the |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ----------- | ------- | ------- | ----- | ------- | ------ |
5and6changetheirparentcoroutineto2. OpenTelemetry and OpenTracing standards. It directly instru-
|     |     |     |     |     |     |     |     | ments tracing |     | codes into | applications |     | and third-party |     | libraries, |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ---------- | ------------ | --- | --------------- | --- | ---------- |
E. TracesExportation
|     |     |     |     |     |     |     |     | making | it a highly | accurate | baseline |     | for comparison. |     | Deep- |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | ----------- | -------- | -------- | --- | --------------- | --- | ----- |
Our eBPF programs export traces and spans to a ringbuffer flow[20]isthestate-of-the-artnon-invasiveapproachfortrack-
when the service receives the response from its upstream or ingrequests.Itimplementsanaggregationalgorithmbasedon
themetadatacapturedbyeBPF,whereeBPFprogramsperform
sendaresponsetoitsdownstream.Toensurecompatibilitywith
existingtracinguserinterfaces,anagentdeployedoneachhost asaspangenerator.ComparingZeroTracerwithDeepflowpro-
reads the generated traces and spans from the ringbuffer. Sub- videsinsightsintoourperformanceandeffectiveness.
sequently, it exports them to external databases in compliance 4) EvaluationMetrics: Tobetterevaluatetheeffectivenessof
withtheOpenTelemetrystandard. ZeroTracer,weadoptaccuracyasourprimarymetric.Accuracy
reflectsthesimilaritybetweenthetracesgeneratedbydifferent
V. EVALUATION tracingsystemsandtheactualend-to-endrequestpathsfromthe
applicationsourcecodes.Theaccuracyisobtainedbycalculat-
| To evaluate | the | performance |     | of ZeroTracer, | we  | conduct | a   |     |     |     |     |     |     |     |     |
| ----------- | --- | ----------- | --- | -------------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ingtheproportionofaccuratetraces.Thehighertheaccuracy,
seriesofexperimentstoanswerthefollowingquestions.
themoreeffectivethetracingsystem.Tomeasuretheimpactof
| Q1: How | does | ZeroTracer | perform | in  | tracking | end-to-end |     |     |     |     |     |     |     |     |     |
| ------- | ---- | ---------- | ------- | --- | -------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ZeroTraceronserviceperformance,weusetwometrics:request
| requests | for applications |     | developed | in various | high-level |     | lan- |         |                      |     |        |     |         |         |         |
| -------- | ---------------- | --- | --------- | ---------- | ---------- | --- | ---- | ------- | -------------------- | --- | ------ | --- | ------- | ------- | ------- |
|          |                  |     |           |            |            |     |      | latency | and query-per-second |     | (QPS). |     | Request | latency | is used |
guages?(SectionV-B)
|          |        |      |            |          |             |     |      | to show | the impact | of ZeroTracer |     | on  | service | response | time. |
| -------- | ------ | ---- | ---------- | -------- | ----------- | --- | ---- | ------- | ---------- | ------------- | --- | --- | ------- | -------- | ----- |
| Q2: What | impact | does | the kernel | function | ”alloc_pid” |     | have |         |            |               |     |     |         |          |       |
QPSisusedtomeasurethethroughputofservices.Inaddition,
| on improving | the | effectiveness | of  | ZeroTracer | in containerized |     |     |     |     |     |     |     |     |     |     |
| ------------ | --- | ------------- | --- | ---------- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
wealsomeasuretheconsumptionofCPUandmemorytohelp
microserviceapplications?(SectionV-C)
understandtheresourceconsumptionofZeroTraceronthehosts.
| Q3: How | does | ZeroTracer | perform | under | different | concur- |     |     |     |     |     |     |     |     |     |
| ------- | ---- | ---------- | ------- | ----- | --------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
rencylevels?(SectionV-D)
Q4: How much is the overhead incurred by ZeroTracer on B. (Q1)Multi-LanguageSupporting
resourceconsumptionandserviceperformance?(SectionV-E)
ToevaluatetheperformanceofZeroTracerintrackingend-to-
endrequestsofmicroserviceapplicationsdevelopedinmultiple
A. ExperimentSettings
|     |     |     |     |     |     |     |     | high-level | languages, | we  | use Fortio | to  | generate | a   | continuous |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ---------- | --- | ---------- | --- | -------- | --- | ---------- |
1) Environment: We have set up our test environment on andsequentialworkloadoftenthousandrequestsforoursingle-
a Kubernetes [37] platform with 5 physical machines, each threaded and multi-threaded benchmarks. The comparison re-
having 16 GB RAM and eight 4-core 2.50 GHz Intel Xeon sultsarepresentedinFig.12(a).PHPapplicationsaretestedonly
Platinum8269CPUs.ThemachinesrunonCentos-8-basedOS insingle-threadedmodeduetoitswidespreaduse.Conversely,
andhaveLinuxkernelversion5.10.134.TocompiletheeBPF Golangapplicationsarenativelyimplementedwiththreadpools
| programs, | we have | opted | for clang | and LLVM | version | 13. | We  | inruntime. |     |     |     |     |     |     |     |
| --------- | ------- | ----- | --------- | -------- | ------- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on March 20,2026 at 23:38:08 UTC from IEEE Xplore.  Restrictions apply.

YANGetal.:ZEROTRACER:IN-BANDeBPF-BASEDTRACEGENERATORWITHZEROINSTRUMENTATIONFORMICROSERVICESYSTEMS 1487
Fig.12. EffectivenesscomparisonamongJaeger,Deepflow,andZeroTracerontrackingend-to-endrequests.Inthesefigures,“S”representsthesingle-threaded
services,while“M”representsthemulti-threadedservices.
As depicted in Fig. 12(a), Jaeger can always achieve per- Deepflow fails to refactor request causality with zero accu-
fect performance in tracking end-to-end requests by directly racy, whose results are not displayed in Fig. 12(b). The tag
instrumenting tracing codes into microservice applications. In syscall_trace_id of trace logs collected by Deepflow
contrast, Deepflow relies on its monitored network metadata ownszerovalue,resultinginthelossofchildrenrequestsassoci-
to analyze request causality, regardless of application imple- atedwithitsparentrequests.Moreover,foranend-to-endrequest
mentations.WhileDeepflowsuccessfullyaggregatesnearlyall to the Travel service of Trainticket spanning 97 operations in
requestcausalityforPHP,Golang,andmulti-threadedJavami- atrace,theofflineaggregationalgorithmappliedbyDeepflow
croserviceapplications,itstrugglestotrackend-to-endrequests onlyrefactorspartoftheentirerequestcausality.Thislimitation
forPythonandsingle-threadedJavaapplications.Analyzingthe arisesduetothepresenceofnestedrequestsandtheextensive
trace log collected from Deepflow, we discover that requests lengthoftherequestpath,causingDeepflowtosplittheentire
can not be correctly associated with the value of a tag named end-to-endrequestsintoseveraltraces.
syscall_trace_id. In our experiments, over 75% of that ZeroTraceroutperformsDeepflowwhentrackingend-to-end
valueiszero,indicatingalackofcausalityrelationshipsamong requestsofcontainerizedmicroservices.Sinceacontainerexe-
requestsandresultinginafailuretorefactorend-to-endtraces. cutesasaprocessinthehost,ZeroTracercaneffortlesslydiscern
ZeroTracer enables tracking nearly 100% of end-to-end re- theparent-childrelationshipamongthreadsandpropagatetrace
questsofmulti-languageapplications,includingthoseoperating contextthroughtheservice.Consequently,ZeroTracerachieves
in multi-threaded mode. By monitoring parent-child relation- accuracyexceeding92%intrackingend-to-endrequests,even
ships among threads and tasks, ZeroTracer identifies the own- forcomplexscenariossuchasanend-to-endrequestcomprising
ership of requests to the threads or tasks or coroutines in the 97spansintotalforTrainticket.However,someinaccurateand
Linuxkernel,thuspropagatingtracecontextsthroughservices incomplete traces may be generated when some services of
withoutdetailedinvasiveinformationofapplications.Fig.12(a) Bookinfo and Trainticket fail to generate their spans properly.
illustratesthatZeroTracerperformswellintrackingend-to-end ObservingtheeBPFlogs,weunderstandthattheeBPFprogram
requestswithzeroinstrumentation,regardlessofthehigh-level failstogenerateaspanwhentheservicesendsaresponsetoits
languagesemployedinmicroserviceapplications. downstream.ThisissuearisesbecauseeBPFprogramsstartwith
the inserted instruction int 3 into the hooked functions, but
theymaybeinterruptedandre-enteredbyothereventsinvoking
C. (Q2)EffectivenessinMicroserviceExamples
the same function [43], [44], [45]. Consequently, ZeroTracer
ToassesstheperformanceofZeroTracerontrackingend-to- mayoverlookakprobeifaninterruptisalreadyprocessingthe
endrequestsofcontainerizedmicroservices,weselectBookinfo samekprobe,leadingtothelossofaspan.
andTrainticketasourbenchmarks.Fortioissettogenerateacon- From Fig. 12(b), it is convincing that the eBPF program
tinuousandsequentialworkloadoftenthousandrequestsforthe attached to the alloc_pid function significantly helps Ze-
single-threaded and multi-threaded Bookinfo and Trainticket. roTracerestablishparent-childrelationshipsamongthreadsfor
ThecomparisonresultsonaccuracyareshowninFig.12(b). containerizedserviceonthehost,regardlessofthenamespace
Jaegerkeepstrackingend-to-endrequestsforBookinfoaccu- resource isolation. In scenarios where the function clone
rately,thankstoitsdirectinstrumentationintoapplicationcodes. is monitored instead of alloc_pid, ZeroTracer effectively
However, when it comes to TrainTicket, which utilizes instru- tracks end-to-end requests for the single-threaded Bookinfo
mented third-party libraries, Jaeger performs well in tracking andTrainticketapplication,whereathreadprocessesarequest
requestsforthesingle-threadedTrainticketbutencountersdiffi- individually.However,duetothenamespaceresourceisolation,
cultieswiththemulti-threadedversion.Thisdiscrepancyarises ZeroTracerencountersdifficultiesinidentifyingtheparent-child
becauseinstrumentationsinthird-partylibrariesfortracingtend relationshipsbetweenthreadsresidingindifferentnamespaces,
to split a request processed by different threads into different so ZeroTracer without monitoring alloc_pid fails to track
traces. end-to-endrequestsofmulti-threadedBookinfoandTrainticket.
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on March 20,2026 at 23:38:08 UTC from IEEE Xplore. Restrictions apply.

1488 IEEETRANSACTIONSONPARALLELANDDISTRIBUTEDSYSTEMS,VOL.36,NO.7,JULY2025
Fig.13. PercentageofmissingprobesinZeroTracerunderdifferentconcurrentworkloadsforsingle-threadedandmulti-threadedBookinfo.
thencomparethetriggeredcountofeBPFprogramsfortenthou-
D. (Q3)ConcurrencyImpactonEffectiveness
sandrequestsundervaryingconcurrencywiththenormalcount
To evaluate the performance of ZeroTracer under different of triggered eBPF programs for a single request, calculating
concurrencies,weselectBookinfoasourbenchmarksinceitcan the difference as the count of missing probes. The results are
process up to six hundred concurrent requests simultaneously showninFig.13.Astheconcurrencyincreases,thenumberof
with a ten-second timeout. Fortio is configured to generate missingprobesrises,particularlywhentheconcurrencyreaches
a total of ten thousand requests for both single-threaded and 500 and 600, withmissingprobes ranging from7.1%to7.3%
multi-threadedBookinfo,with100,200,300,400,500,and600 forsingle-threadedBookinfoandfrom12%to18%formulti-
concurrentusers,respectively.Comparisonresultsarepresented threadedBookinfo.TheissuearisessinceeBPFprogramsrely
inFig.12(c). ontheinsertedinstructionint 3forentry,whichcanbeinter-
Jaeger keeps tracking all the end-to-end requests for ei- ruptedandre-enteredbyothereventsinvokingthesameeBPF
thersingle-threadedormulti-threadedBookinfounderdifferent programs[43],[44],[45].Forexample,aneBPFprogrammay
concurrent user workloads. With explicit instrumentation in be triggered by a user-space application through system calls,
sourcecodesofBookinfo,Jaegercaneasilydistinguishwhich butitcanalsobeinvokedbyahardwareIRQ(InterruptRequest)
downstream request causes an upstream request, thus tracking orasoftIRQ,bothofwhichhavehigherinterruptpriority.Ifan
accuraterequestcausality. eBPFprogramtriggeredbyauser-spaceapplicationisrunning,
Whentrackingconcurrentuserrequests,Deepflowprovesin- it can be interrupted and re-entered by a soft IRQ, leading to
effectiveintrackinganyoftheend-to-endrequestsforBookinfo. the loss of execution context. Consequently, ZeroTracer may
AlthoughDeepflowaggregates partoftheend-to-endrequests misstheexecutionofakprobeifakprobeprogramisrunning
of Bookinfo, it falls short in aggregating the entire end-to-end and gets re-entered by another event, resulting in the loss of
requests due to its metadata-based algorithm. For instance, thatspan.Astheconcurrencyincreases,thelikelihoodofspan
the Productpage service of Bookinfo requires requesting to loss escalates accordingly, thereby impacting the effectiveness
the Detail service and the Reviews service to fulfill a user of ZeroTracer. When comparing the count of missing probes
request. Deepflow prefers to treat these two requests within in single-threaded and multi-threaded Bookinfo, the hooked
an end-to-end request as two separate traces rather than as eBPF programs in multi-threaded Bookinfo miss more probes
part of the same trace. Deepflow assigns zero value to the (over 12% ) compared to those in the single-threaded version
tag syscall_trace_id, so it fails to properly associate (nearly7.3%).Asthenumberofconcurrentthreadsincreases,
therequest fromProductpage toDetails withtherequestfrom thelikelihoodofexecutingmultipleprobessimultaneouslyalso
Productpage to Reviews. Furthermore, Deepflow applies the rises,leadingtoahigherchanceofmissinggeneratedspansor
policy that where multiple requests in the same transmission failingtopropagatecontextinformation.
direction share the same trace ID, further muddles the causal In non-invasive methods such as DeepFlow, the trace loss
relationshipofrequests.Consequently,Deepflowfailsinaggre- occurs due to incorrect correlation between spans. In such
gatingaccurateend-to-endrequests. methods,allspansarecaptured,buttheircausalrelationshipsare
ZeroTracer demonstrates remarkable accuracy, exceeding not well reconstructed, resulting in incomplete request traces.
91% when tracing concurrent end-to-end requests for both ZeroTracer does not suffer from such inaccuracies in request
single-threaded and multi-threaded Bookinfo applications. causalityduetoitsprecisecausalpropagation.Instead,thetrace
Leveraging the parent-child relationships among threads for loss in ZeroTracer occurs when certain hooked functions are
tracecontextpropagation,ZeroTracerconsistentlydeliverssta- nottriggeredorareinterruptedduringexecution,preventingthe
ble performance in request tracing. However, it falls short of generation of corresponding spans. Consequently, the parent-
achieving100%accuracyastheeBPFprogramshookedonthe childrelationshipsamongtheremainingspansremainaccurate,
sendingandreceivingkernelfunctionscannotperformproperly althoughsomespansmaybelost.
andfailtogeneratespans,particularlyunderhighconcurrency ToensurethatZeroTracerdoesnotexperiencethespanloss
scenarios. To identify the cause of the accuracy decline, we when exporting spans from eBPF programs to the agent via
record the triggered count of each hooked eBPF program. We the ringbuffer, we compare the number of spans generated
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on March 20,2026 at 23:38:08 UTC from IEEE Xplore. Restrictions apply.

YANGetal.:ZEROTRACER:IN-BANDeBPF-BASEDTRACEGENERATORWITHZEROINSTRUMENTATIONFORMICROSERVICESYSTEMS 1489
Fig.14. OverheadofZeroTracercomparedwithDeepflowonserviceperformanceandresourceconsumption.
and exported by eBPF programs with the number received by request.However,asconcurrencyincreases,themulti-threaded
the agent during the ten thousand concurrent workload testing Bookinforequiresmoretimetoserveconcurrentuserrequests
undervaryingconcurrency.Wefindthatthesecountsarealways thanitssingle-threadedcounterpart.Thisisbecausethemulti-
consistent.Topreventbufferoverflow,wesettheringbuffersize threadedversionreliesonasynchronousthreadstohandleuser
to128MB,whichcanholdupto1,248spanssimultaneously.In requests,whichintroducesthreadwaitingtime.Asconcurrency
ourtests,ZeroTracerexportsspanstotheringbufferandretrieves rises, these waiting time, along with the scheduling overhead
thematthespeedrangingfrom10MB/sto35MB/s.Therefore, of the newly generated threads, further increase the execution
any span loss in ZeroTracer is not caused by missing spans in delays.
theringbuffer.Theringbuffersizecanbeconfiguredbasedon Regarding resource consumption, ZeroTracer has increased
actualrequirements. CPUusageby0.35%–0.51%(3%–5.8%relativetothenormal)
forsingle-threadedBookinfoand0.48%–0.68%(3.9%–5.4%
relativetothenormal)formulti-threadedBookinfo,duetothe
E. (Q4)SystemOverhead
execution of eBPF programs in the Linux kernel. The multi-
In this experiment, we assessed the overhead of ZeroTracer threadedBookinforequiresadditionalCPUresourcesforthread
intrackingrequestsforthesingle-threadedandmulti-threaded schedulingcomparedtothesingle-threadedversion.Intermsof
Bookinfo application compared to Deepflow. Workloads are memoryusage,ZeroTracerneedsadditional3.2%–3.7%(about
generatedwithvaryinglevelsofconcurrency:100,200,400,and 524MB–602MB)memoryforsingle-threadedBookinfototem-
600concurrentusers.Theexperimentsrunfortenminutesand porarily store partial message data, generated trace contexts,
arerepeatedfivetimesonfivephysicalmachines.Theaverage and other relevant information. For multi-threaded Bookinfo,
resultsareillustratedinFig.14. the additional memory usage increases to 3.7% –4.2% (ap-
First, we examine the impact of ZeroTracer on the service proximately602MB–688MB)toaccommodatetemporarydata
performance. As shown in Fig. 14, ZeroTracer increases the storage. The multi-threaded case demands more memory than
request latency for single-threaded Bookinfo by about 5–25 thesingle-threadedcasebecauseitmustalsotrackparent-child
milliseconds(ms)(0.5%–0.9%)comparedtothenormalcase, relationshipsbetweenthreads.
and reduces the QPS of the service by about 0.5–1.1 (0.4% In the meantime, Deepflow increases request latency and
–0.9% ), even under 600 concurrent user requests. For multi- reducesQPSby3.0%–5.8%forsingle-threadedBookinfoand
threaded Bookinfo, ZeroTracer increases service latency by 3.0% –5.3% for multi-threaded Bookinfo. This overhead is
7–61 ms (0.7% –1.2% ) and reduces QPS by 0.8–1.6 (0.7% higherthanthatofZeroTracer,asDeepflowmountsmoreeBPF
–1.3% ). The additional latency comes from the execution programs in the kernel. Additionally, it consumes 22% –37%
of our customized eBPF programs for intercepting and pars- more of CPU and 12.5% –14.6% more of memory resources,
ing the sending and receiving messages in the Linux ker- duetotheexecutionofitsserverandthehookedeBPFprograms.
nel. In our implementation, the multi-threaded Bookinfo pro- To gain insights into the overhead imposed by our attached
cesses a request in 9.54 ms, which is faster than the single- eBPF programs, we measured the average execution time re-
threadedversionat10.83mswhenhandlingasingleconcurrent quired for each type of eBPF program mounted in the kernel.
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on March 20,2026 at 23:38:08 UTC from IEEE Xplore. Restrictions apply.

1490 IEEETRANSACTIONSONPARALLELANDDISTRIBUTEDSYSTEMS,VOL.36,NO.7,JULY2025
F. DeploymentExperience:DemonstrationinaReal-World
CloudTracingConsole
We have successfully deployed ZeroTracer in a real-world
containerizedenvironmentandexportedthecollecteddatatoa
tracing console provided by the largest e-commerce company
inChinaforvisualization.Atracetreeanditsspansgenerated
by ZeroTracer when a user requests Bookinfo is depicted in
Fig. 17(a). Additionally, the trace is displayed in a tracing
consoleinFig.17(b).Whenservingarequestfromauser,the
ProductpageserviceofBookinfocallstheDetailserviceandthe
Fig.15. TimeoverheadoftheattachedeBPFprogramsofZeroTracer.
Review-v1service,resultinginatotalof5generatedspans.This
tracetreedoeshelpintroubleshootingfaults.Forinstance,when
theentryspan1exhibitsanomalouslatency,trackingthroughthe
tracetreewithspan2andspan3facilitatestheidentificationof
theabnormalDetailservice.
G. Discussion
ZeroTracer implements an online non-invasive distributed
tracingsystemformicroserviceapplicationsservingtheHTTP
requests. But there exist some limitations that need to be dis-
cussed.
Multi-protocol Supports: When transmitting contexts be-
Fig.16. TimeoverheadofZeroTracerwhenparsingrequestlineswithdiffer- tweenservices,ZeroTracerembedsthecontextinthemessage
entlengths.
header to maintain request causality. However, for certain en-
cryptionprotocolswheremessagesareencryptedbeforetrans-
This measurement is conducted by repeatedly requesting the mission,ZeroTracerinterceptsonlytheencryptedpacketsrather
Bookinfo application 20000 times and invoking the hooked thanplaintextcontent.Insuchcases,determiningtheappropriate
functions over 20000 times. The average latency results are locationforaddingcontextbecomeschallenging,asZeroTracer
depictedinFig.15.TheadditionallatencyintroducedbyeBPF cannot effectively parse encrypted or unstructured requests.
programs of ZeroTracer ranges from 550 ns (nanoseconds) to Incorrectly injecting context may disrupt the transmission and
6640 ns. Notably, the sk_msg program exhibits the highest interpretationoftheoriginalpacket.Toaddressthechallenges
overhead at 6640 ns. This is attributed to its task of parsing posed by encryption protocols, we plan to fix the context in-
outgoing messages and injecting trace contexts, which incurs jectionplaceatthebeginningofthesendingpackets(offset0)
significant processing time. It is important to note that eBPF anddeployanadditionaleBPFprogramonthereceivingservice
imposes limitations on the number of instructions of an eBPF toextractandremovethecontextbeforepacketprocessing,as
program,therebylimitingthelatencyofaneBPFprogram. showninFig.18.Thisensuresthattheoriginalpacketremains
Since ZeroTracer employs the tail call mechanism of eBPF intactandcanbecorrectlyparsedbythereceivingservice.By
to parse messages with long request lines, we conduct tests doing so, ZeroTracer eliminates the need for message parsing
toevaluateitsperformanceundervaryingrequestlinelengths. during context injection, making it protocol-independent and
We generate 20,000 workloads with 100 concurrent users for applicabletovariousprotocols,includingencryptionprotocols,
BookinfotomeasurethetimerequiredforZeroTracertoparse likegRPCandHTTPS.Alternatively,thecontextcanbeinjected
requestlinesofvaryinglengths.TheresultsareshowninFig.16. into the original message before encryption, allowing us to
Asobserved,ZeroTracertakeslongertimetoparserequestlines modifytheplaintextmessageandembedthetracecontextbefore
as their length increases. On average, it processes a 100-byte encryption. For example, the Invoke function in gRPC can
request line in 14,896 ns, whereas a 2,500-byte request line provide insights into the message-sending procedure to help
takes 34,039 ns. The time overhead for parsing request lines injecttracecontexts.
increases almost linearly with length, as ZeroTracer requires RuntimeRequirements:eBPFprogramscanonlybedeployed
moreiterationstolocatetheendoftherequestlineasitslength byprivilegedusers.ButLinuxhastheplantomakethemavail-
grows. abletounprivilegedusers[46],andthereexistssomeworkon
Concluded above, ZeroTracer exhibits stable effects on ser- unleashingunprivilegedeBPFprograms[47].Therequirement
vice performance and resource consumption, regardless of the to root privilege of eBPF programs may be alleviated in the
numberofconcurrentrequestshandledbytheservices.Among future.Inaddition,ZeroTracerrequiresaLinuxkernelversion
the attached eBPF programs, the sk_msg programs spends ofatleast5.2[48]toexecute.
themosttimeparsingmessagesandinjectingtracecontextsin FunctionUpdates:ThemountingofeBPFprogramstosome
ZeroTracer.Theparsingtimeincreasesastherequestlinelength user functions requires ZeroTracer to obtain the addresses of
grows. the user functions in different third-party libraries. To achieve
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on March 20,2026 at 23:38:08 UTC from IEEE Xplore. Restrictions apply.

YANGetal.:ZEROTRACER:IN-BANDeBPF-BASEDTRACEGENERATORWITHZEROINSTRUMENTATIONFORMICROSERVICESYSTEMS 1491
Fig.17. Visualizationinreal-worldtracingconsoleofageneratedtraceofBookinfowithitstraceIDas9e01f10abe23f10198f30e00104c5607.
channelsbyhookingsock_sendmsgandsock_recvmsg.
Additionally,byattachingtotheseuser-spacefunctions,Zero-
|     |     |     |     |     |     | Tracer can | track | which thread | processes | each | request, such | as  |
| --- | --- | --- | --- | --- | --- | ---------- | ----- | ------------ | --------- | ---- | ------------- | --- |
sendingorreceivinganHTTPrequest,enablingpreciseparent-
|     |     |     |     |     |     | child thread | relationship |     | tracking | and facilitating | intra-service |     |
| --- | --- | --- | --- | --- | --- | ------------ | ------------ | --- | -------- | ---------------- | ------------- | --- |
contextpropagation.Inaddition,ZeroTraceriscompatiblewith
|                        |     |         |             |                   |             | the existing            | OpenTelemetry |           | and        | does not   | affect the request |     |
| ---------------------- | --- | ------- | ----------- | ----------------- | ----------- | ----------------------- | ------------- | --------- | ---------- | ---------- | ------------------ | --- |
| Fig. 18. Inter-service |     | context | propagation | through a message | using other |                         |               |           |            |            |                    |     |
| protocolsthanHTTP.     |     |         |             |                   |             | tracingofOpenTelemetry. |               |           |            |            |                    |     |
|                        |     |         |             |                   |             | Multi-language          |               | Supports: | ZeroTracer |            | requires attaching |     |
|                        |     |         |             |                   |             | eBPF programs           |               | to user   | functions  | to capture | task scheduling    |     |
accurateend-to-endrequesttracing,ZeroTracermusttrackuser- andcreationinformation,enablingcontextpropagationthrough
spaceproceduressuchascoroutinescheduling,threadcreation, multi-threaded applications. For Golang and C++ programs,
andrequestconnectionhandling(asshowninTableI).Unlike locating the addresses of hooked functions is straightforward.
existinginvasivedistributedtracingmethodsthatrequiresource However, for Java and Python, which run on virtual ma-
code modifications when third-party libraries or applications chines, retrieving dynamic function addresses to attach eBPF
are updated, ZeroTracer only needs to update the addresses of programs is challenging. In such cases, ZeroTracer leverages
the hooked user functions without altering the source code or bytecode instrumentation tools, such as javaagent [39], to
simplyaddneweBPFprogramswhenuser-spaceprocedureslike hook user functions and extract task scheduling and creation
| coroutine | scheduling, | thread | creation, | and request | connection | details. |     |     |     |     |     |     |
| --------- | ----------- | ------ | --------- | ----------- | ---------- | -------- | --- | --- | --- | --- | --- | --- |
handling update. The eBPF programs hooked by ZeroTracer Extended Use Cases: ZeroTracer supports online key-value
on such user-space procedures are always decoupled from the data injection into in-band requests and can be extended as a
applications. toolforserviceorchestration.Forexample,wecanimplement
Compatibility: For certain hardware or kernel bypass meth- fine-grained grayscale release by injecting specific key-value
ods, such as DPDK, eBPF programs can be attached to user- tagsintotheend-to-endrequestsinpractice.
spacefunctionsresponsibleforsendingandreceivingmessages,
|            |            |         |          |            |             |     |     | VI. | RELATEDWORK |     |     |     |
| ---------- | ---------- | ------- | -------- | ---------- | ----------- | --- | --- | --- | ----------- | --- | --- | --- |
| similar to | the socket | channel | example, | to capture | transmitted |     |     |     |             |     |     |     |
messages.ThisallowsZeroTracertoparsetracecontextsfrom eBPF-enabled observability: eBPF is widely used to en-
incoming requests and inject them into outgoing requests for able fine-grained monitoring and improve system observabil-
inter-service context propagation. Even though some kernel ity. Rolando Brondolin [49] proposed an eBPF-based non-
bypassmethodsusededicatedhardwareandlibraries,itremains transparentmonitoringapproach.WeaveScope[50]tracksTCP
feasibletohookeBPFprogramsontotheirmessagetransmission connectionandimprovestheobservabilityofKubernetesclus-
functions, just as ZeroTracer does with socket-based message ters.bpftrace[51]helpstraceinkernel.TaekhoNametal.[52]
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on March 20,2026 at 23:38:08 UTC from IEEE Xplore.  Restrictions apply.

1492 IEEETRANSACTIONSONPARALLELANDDISTRIBUTEDSYSTEMS,VOL.36,NO.7,JULY2025
implementeBPF-basedpackettracingonmultiplenetworkin- microserviceimplementationsandvarioushigh-levellanguages,
terfacesinLinux.ChangLiuetal.[53]collectuserapplication whilemaintaininghightraceaccuracy.
| L7/L4 layer | network |     | protocol | interaction |     | information | based |     |     |     |     |     |     |     |     |
| ----------- | ------- | --- | -------- | ----------- | --- | ----------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
oneBPF.vNetTracer[54],[55]providesprogrammablepacket VII. CONCLUSION
tracingbasedoneBPF.Elastic[56]proposesauniversalandcon-
Inthispaper,weproposeZeroTracertoachieveonlineend-
tinuousprofilingtoolusingeBPF.SinceeBPFenablesefficient,
to-endrequesttracinginalarge-scaledistributedsystemwithout
| real-time | monitoring | and | tracing | at  | the kernel | level, | providing |          |                  |     |       |     |       |            |        |
| --------- | ---------- | --- | ------- | --- | ---------- | ------ | --------- | -------- | ---------------- | --- | ----- | --- | ----- | ---------- | ------ |
|           |            |     |         |     |            |        |           | any code | instrumentation. |     | Built | on  | eBPF, | ZeroTracer | adapts |
deepsysteminsightswithoutalteringapplicationcode,itmakes
|     |     |     |     |     |     |     |     | to tracking | requests | for | microservice |     | application | implementa- |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | -------- | --- | ------------ | --- | ----------- | ----------- | --- |
tracegenerationinZeroTracerfeasible.
|        |          |        |         |         |     |         |             | tions across | various | high-level |     | languages. |     | Our comprehensive |     |
| ------ | -------- | ------ | ------- | ------- | --- | ------- | ----------- | ------------ | ------- | ---------- | --- | ---------- | --- | ----------------- | --- |
| Packet | tracing: | Packet | tracing | capture |     | packets | between two |              |         |            |     |            |     |                   |     |
evaluationsdemonstratethatZeroTracercantrackover91%of
| services | and helps | generate |     | traces | for | single-hop | requests. |     |     |     |     |     |     |     |     |
| -------- | --------- | -------- | --- | ------ | --- | ---------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
requestswithreliabletracingperformance,evenwhenmicroser-
| Inkle [57]   | tracks | single-hop  |     | gRPC    | requests | for  | microservice |              |          |     |                   |     |      |                |     |
| ------------ | ------ | ----------- | --- | ------- | -------- | ---- | ------------ | ------------ | -------- | --- | ----------------- | --- | ---- | -------------- | --- |
|              |        |             |     |         |          |      |              | vices handle | requests |     | in multi-threaded |     | mode | with increased |     |
| applications | on     | Kubernetes. |     | tcpdump | [58],    | [59] | and Wire-    |              |          |     |                   |     |      |                |     |
concurrency.Furthermore,ourexperimentsindicatethatZero-
Shark[60]areabletosniffpacketsonphysicallinks.Istio[61]
|           |         |         |      |         |     |          |          | Tracer has | little     | impact   | on service | performance, |          | causing      | only |
| --------- | ------- | ------- | ---- | ------- | --- | -------- | -------- | ---------- | ---------- | -------- | ---------- | ------------ | -------- | ------------ | ---- |
| allows to | collect | tracing | data | through | its | deployed | proxies. |            |            |          |            |              |          |              |      |
|           |         |         |      |         |     |          |          | a slight   | 0.5% –1.2% | increase |            | in service   | latency. | For resource |      |
INT-Label[62]introducesalightweighttelemetryarchitecture
consumption,ZeroTracerconsumesanadditional3%–5.8%of
| by periodically |     | labeling | packets. |     | Pixie [63] | enables | tracking |     |     |     |     |     |     |     |     |
| --------------- | --- | -------- | -------- | --- | ---------- | ------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
CPUandmemoryresources.Thiscombinationofeffectiveness
| packets | by monitoring |     | sending | and | receiving | functions | with |     |     |     |     |     |     |     |     |
| ------- | ------------- | --- | ------- | --- | --------- | --------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
andefficiencypositionsZeroTracerasapromisingsolutionfor
eBPF.Thecollectedpacketscanhelpgeneratesingle-hoptraces
trackingend-to-endrequestsinmicroservicesystems.
| and serve         | as  | a data     | source | for | multi-hop | trace       | generation |     |     |      |                  |     |     |     |     |
| ----------------- | --- | ---------- | ------ | --- | --------- | ----------- | ---------- | --- | --- | ---- | ---------------- | --- | --- | --- | --- |
| using aggregation |     | algorithms |        | in  | existing  | distributed | tracing    |     |     |      |                  |     |     |     |     |
|                   |     |            |        |     |           |             |            |     |     | VII. | DATAAVAILABILITY |     |     |     |     |
systems.
Existing distributed tracing systems: Invasive tracing sys- All the data and results of ZeroTracer can be found
tems require developers to instrument tracing codes into ap- in the Github repository as follows: https://github.com/
| plication | codes | to generate |     | traces. | Zipkin | [12], | Jaeger [13], |     |     |     |     |     |     |     |     |
| --------- | ----- | ----------- | --- | ------- | ------ | ----- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
IntelligentDDS/zerotracer.
| SkyWalking   | [17],    | OpenTracing |             | [15], | OpenTelemetry |         | [14] are |     |     |     |     |     |     |     |     |
| ------------ | -------- | ----------- | ----------- | ----- | ------------- | ------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
| some typical | examples |             | of invasive |       | tracing       | systems | commonly |     |     |     |     |     |     |     |     |
ACKNOWLEDGMENT
| used inpractice. |        | X-Trace        | [10]       | provides | acomprehensive |      | view          |               |            |            |            |        |            |                  |      |
| ---------------- | ------ | -------------- | ---------- | -------- | -------------- | ---- | ------------- | ------------- | ---------- | ---------- | ---------- | ------ | ---------- | ---------------- | ---- |
|                  |        |                |            |          |                |      |               | The authors   | greatly    |            | appreciate | the    | insightful | feedback         | from |
| of systems       | as     | a tracing      | framework. |          | Pinpoint       | [9]  | tracks client |               |            |            |            |        |            |                  |      |
|                  |        |                |            |          |                |      |               | the anonymous |            | reviewers. | Special    | thanks | are        | also extended    | to   |
| requests         | in its | communications |            | layer.   | Dapper         | [11] | implements    |               |            |            |            |        |            |                  |      |
|                  |        |                |            |          |                |      |               | Guangba       | Yu (School | of         | Computer   |        | Science    | and Engineering, |      |
alow-overheaddistributedsystembysampling.REPTrace[64]
|          |              |     |            |           |     |       |              | Sun Yat-sen | University; |     | yugb5@mail.sysu.edu.cn), |     |     | Zilong | He  |
| -------- | ------------ | --- | ---------- | --------- | --- | ----- | ------------ | ----------- | ----------- | --- | ------------------------ | --- | --- | ------ | --- |
| captures | the complete |     | end-to-end | execution |     | paths | by utilizing |             |             |     |                          |     |     |        |     |
(SchoolofComputerScienceandEngineering,SunYat-senUni-
| the transferring |     | messages. |     | Pedro | Las-Casas, | et  | al. [65] and |     |     |     |     |     |     |     |     |
| ---------------- | --- | --------- | --- | ----- | ---------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
versity;hezlong@mail2.sysu.edu.cn)fortheirusefulcomments
| Hindsight | [66] | explore | and optimize |     | the | sampling | mechanism |     |     |     |     |     |     |     |     |
| --------- | ---- | ------- | ------------ | --- | --- | -------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
onwritingofthispaper,andtoHaibinZhang(AlibabaGroup;
| of distributed | tracing |     | systems. | Castanheira, |     | Lucas | et al. [67] |     |     |     |     |     |     |     |     |
| -------------- | ------- | --- | -------- | ------------ | --- | ----- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
zhb192729@alibaba-inc.com)forhisassistanceinsettingupthe
| proposed | a flexible | distributed |     | tracing | workflow |     | based on in- |     |     |     |     |     |     |     |     |
| -------- | ---------- | ----------- | --- | ------- | -------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
experimentalenvironment.ThecorrespondingauthorisPengfei
| strumented | annotations |     | and | preemptive | tracing | for | debugging. |     |     |     |     |     |     |     |     |
| ---------- | ----------- | --- | --- | ---------- | ------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
Chen.
| JCallGraph | [18]         | realizes | a distributed |               | tracing | system    | for mi-  |     |     |     |     |     |     |     |     |
| ---------- | ------------ | -------- | ------------- | ------------- | ------- | --------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
| croservice | applications |          | by            | instrumenting |         | the cloud | platform |     |     |     |     |     |     |     |     |
REFERENCES
middlewares.ChunghanLeeetal.[68]enhancethesingle-hop
requestlatencymeasurementwitheBPFbasedontheinvasive [1] G. F. Coulouris, J. Dollimore, and T. Kindberg, Distributed Systems:
tracecontextsinHTTPpayloads.Existingnon-invasivetracing ConceptsandDesign.London,U.K.:PearsonEducation,2005.
systemsgeneratetraceswithoutanyinstrumentationintoappli- [2] S.Mullender,DistributedSystems.NewYorkCity,NY,USA:ACM,1990.
[3] M.VanSteenandA.S.Tanenbaum,“Abriefintroductiontodistributed
cationsandthird-partylibraries.Cha,Donghun,etal.[19]con- systems,”Computing,vol.98,pp.967–1009,2016.
structedtherequesttracesbasedontheinformationcollectedby [4] J.Waldo,G.Wyant,A.Wollrath,andS.Kendall,“Anoteondistributed
computing,”inProc.MobileObjectSyst.TowardsProgram.Internet:2nd
theserviceproxiesintheservicemesh.DeepFlow[20]mounts
Int.Workshop,2005,pp.49–64.
eBPFprogramstocollectcommonlyusedmetricsandgenerate [5] J. Thönes, “Microservices,” IEEE Softw., vol. 32, no. 1, pp. 116–116,
| tracesbyaggregationalgorithms.OpenTelemetry[69]provides |     |     |     |     |     |     |     | Jan.2015. |     |     |     |     |     |     |     |
| ------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
[6] G.Kakivayaetal.,“Servicefabric:Adistributedplatformforbuilding
| instrumentation |     | for Go | libraries | using | eBPF. | Odigos | [70] im- |     |     |     |     |     |     |     |     |
| --------------- | --- | ------ | --------- | ----- | ----- | ------ | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
microservicesinthecloud,”inProc.13thEuroSysConf.,2018,pp.1–15.
| plements | non-invasive |     | tracing | by  | integrating | OpenTelemetry |     |            |         |              |       |                 |     |            |          |
| -------- | ------------ | --- | ------- | --- | ----------- | ------------- | --- | ---------- | ------- | ------------ | ----- | --------------- | --- | ---------- | -------- |
|          |              |     |         |     |             |               |     | [7] S. Luo | et al., | “An in-depth | study | of microservice |     | call graph | and run- |
timeperformance,”IEEETrans.ParallelDistrib.Syst.,vol.33,no.12,
Golangautomaticinstrumentation[69]andJavathird-partyli-
pp.3901–3914,Dec.2022.
braryinstrumentation.However,thesenon-invasiveapproaches
[8] K.Chengetal.,“ProScale:Proactiveautoscalingformicroservicewith
| suffer from | trace | loss, | dependency |     | on third-party |     | libraries, or |     |     |     |     |     |     |     |     |
| ----------- | ----- | ----- | ---------- | --- | -------------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
time-varyingworkloadattheedge,”IEEETrans.ParallelDistrib.Syst.,
vol.34,no.4,pp.1294–1312,Apr.2023.
donotsupportvarioushigh-levellanguages.Comparedwiththe
|          |              |     |             |     |            |          |        | [9] M. Chen, | E.  | Kiciman, | E. Fratkin, | A.  | Fox, and | E. Brewer, | “Pinpoint: |
| -------- | ------------ | --- | ----------- | --- | ---------- | -------- | ------ | ------------ | --- | -------- | ----------- | --- | -------- | ---------- | ---------- |
| existing | non-invasive |     | approaches, |     | ZeroTracer | supports | online |              |     |          |             |     |          |            |            |
Problemdeterminationinlarge,dynamicinternetservices,”inProc.Int.
non-invasive request tracing and can be adapted to different Conf.DependableSyst.Netw.,2002,pp.595–604.
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on March 20,2026 at 23:38:08 UTC from IEEE Xplore.  Restrictions apply.

YANGetal.:ZEROTRACER:IN-BANDeBPF-BASEDTRACEGENERATORWITHZEROINSTRUMENTATIONFORMICROSERVICESYSTEMS 1493
[10] R.Fonseca,G.Porter,R.H.Katz,andS.Shenker,“X-trace:Apervasive [35] Bcc,“BCC:ToolsforBPF-basedLinuxIOanalysis,networking,mon-
networktracingframework,”inProc.4thUSENIXSymp.NetworkedSyst. itoring,andmore,”Accessed:Feb.06,2023.[Online].Available:https:
Des.Implementation,2007,Art.no.20. //github.com/iovisor/bcc
[11] B.H.Sigelmanetal.,“Dapper,alarge-scaledistributedsystemstracing [36] libbpf,“LIBBPF:AuserspacelibraryforloadingandinteractingwithBPF
infrastructure,”GoogleInc.,Tech.Rep.,2010.[Online].Available:https: programs,”Accessed:Feb.06,2023.[Online].Available:https://github.
//research.google.com/archive/papers/dapper-2010-1.pdf com/libbpf/libbpf
[12] Zipkin,“Zipkinisadistributedtracingsystem,”2023.[Online].Available: [37] D.Bernstein,“Containersandcloud:FromLXCtodockertokubernetes,”
https://zipkin.io/ IEEECloudComput.,vol.1,no.3,pp.81–84,Sep.2014.
[13] Jaeger,“Jaeger:Opensource,end-to-enddistributedtracing,”2023.[On- [38] R. Rosen, “Resource management: Linux kernel namespaces and
line].Available:https://www.jaegertracing.io/ cgroups,”Haifux,vol.186,Art.no.70,2013.
[14] OpenTelemetry,“Opentelemetry:High-quality,ubiquitous,andportable [39] “Java agent,” Accessed: Mar. 02, 2025. [Online]. Available: https://
telemetry to enable effective observability,” 2023. [Online]. Available: opentelemetry.io/docs/zero-code/java/agent/
https://opentelemetry.io/ [40] Fortio, “Fortio load testing library, command line tool, advanced echo
[15] OpenTracing,“Opentracing:Vendor-neutralAPIsandinstrumentationfor serverandwebUIinGO(golang),”Accessed:Feb.06,2023.[Online].
distributedtracing,”2023.[Online].Available:https://opentracing.io/ Available:https://github.com/fortio/fortio
[16] U. Erlingsson, M. Peinado, S. Peter, M. Budiu, and G. Mainar-Ruiz, [41] Bookinfo,“Bookinfo,”Accessed:Feb.06,2023.[Online].Available:https:
“Fay:Extensibledistributedtracingfromkernelstoclusters,”ACMTrans. //istio.io/latest/docs/examples/bookinfo/
Comput.Syst.,vol.30,no.4,pp.1–35,2012. [42] FudanSELab, “Train ticket - a benchmark microservice system,”
[17] Apache, “Skywalking: Application performance monitor tool for dis- Accessed: Feb. 06, 2023. [Online]. Available: https://github.com/
tributed systems, especially designed for microservices, cloud native FudanSELab/train-ticket
andcontainer-based(kubernetes)architectures,”2023.https://skywalking. [43] U.Saqib,“eBPFre-entrancy,”ineBPFSubmit,2023.[Online].Available:
apache.org/ https://ebpf.io/summit-2023-talks/
[18] H. Liu et al., “JCallGraph: Tracing microservices in very large scale [44] “Kprobesmissingissue,”Accessed:Mar.28,2025.[Online].Available:
containercloudplatforms,”inProc.CloudComput.:12thInt.Conf.,Held https://github.com/iovisor/bcc/issues/4198
PartServ.Conf.Federation,SanDiego,CA,USA,2019,pp.287–302. [45] Linux,“Kprobeimplementationsinlinux,”Accessed:Mar.28,2025.[On-
[19] D. Cha and Y. Kim, “Service mesh based distributed tracing sys- line]. Available: https://github.com/torvalds/linux/blob/master/kernel/
tem,” in Proc. Int. Conf. Inf. Commun. Technol. Convergence, 2021, kprobes.c#L1210
pp.1464–1466. [46] J.Corbet,“UnprivilegedBPF(),”2015.Accessed:Sep.06,2023.[Online].
[20] J.Shenetal.,“Network-centricdistributedtracingwithdeepflow:Trou- Available:https://lwn.net/Articles/660331/
bleshootingyourmicroservicesinzerocode,”inProc.ACMSIGCOMM [47] S. Y. Lim, X. Han, and T. Pasquier, “Unleashing unprivileged eBPF
2023Conf.,2023,pp.420–437. potentialwithdynamicsandboxing,”inProc.1stWorkshopeBPFKernel
[21] J.Corbet,ExtendingExtendedBPF.LinuxWeeklyNews,2014.[Online]. Extensions,NewYork,NY,USA,2023,pp.42–48.[Online].Available:
Available:https://lwn.net/Articles/603983/ https://doi.org/10.1145/3609021.3609301
[22] eBPF,“eBPF,”2023.[Online].Available:https://ebpf.io [48] Bcc, “Bpf features by Linux kernel version,” 2023. Accessed:
[23] J.KazanavicˇiusandD.Mažeika,“Evaluationofmicroservicecommuni- Sep.06,2023.[Online].Available:https://github.com/iovisor/bcc/blob/
cationwhiledecomposingmonoliths,”Comput.Inform.,vol.42,no.1, master/docs/kernel-versions.md
pp.1–36,2023. [49] R.BrondolinandM.D.Santambrogio,“Ablack-boxmonitoringapproach
[24] N. Hamo and S. Saberian, “Evaluating the performance andusability tomeasuremicroservicesruntimeperformance,”ACMTrans.Archit.Code
of http vs grpc in communication between microservices,” 2023. [On- Optim.,vol.17,no.4,pp.1–26,Nov.2020,doi:10.1145/3418899.
line]. Available: https://www.diva-portal.org/smash/get/diva2:1768795/ [50] D.CalaveraandL.Fontana,“LinuxobservabilitywithBPF:Advanced
FULLTEXT02.pdf programming for performance analysis and networking. o’reilly me-
[25] OpenTelemetry, “Manual instrumentation for opentelemetry c,” 2023. dia,” 2019. [Online]. Available: https://books.google.com.hk/books?id=
Accessed: Oct. 18, 2023. [Online]. Available: https://opentelemetry.io/ jtS-DwAAQBAJ
docs/instrumentation/cpp/manual/ [51] bpftrace, “BPFtrace: High-level tracing language for linux eBPF,” Ac-
[26] S.McCanneandV.Jacobson,“TheBSDpacketfilter:Anewarchitecture cessed: Mar. 01, 2023. [Online]. Available: https://github.com/iovisor/
for user-level packet capture,” in Proc. USENIX Winter Conf., 1993, bpftrace
Art.no.2. [52] T. Nam and J. Kim, “Open-source io visor eBPF-based packet tracing
[27] Z.Ahmed,M.H.Alizai,andA.A.Syed,“Inkev:In-kerneldistributednet- onmultiplenetworkinterfacesofLinuxboxes,”inProc.Int.Conf.Inf.
workvirtualizationfordcn,”SIGCOMMComput.Commun.Rev.,vol.46, Commun.Technol.Convergence,2017,pp.324–326.
no.3,pp.1–6,2018. [53] C.Liu,Z.Cai,B.Wang,Z.Tang,andJ.Liu,“Aprotocol-independent
[28] S.JouetandD.P.Pezaros,“BPFabric:Dataplaneprogrammabilityfor containernetworkobservabilityanalysissystembasedoneBPF,”inProc.
softwaredefinednetworks,”inProc.ACM/IEEESymp.ArchitecturesNetw. IEEE26thInt.Conf.ParallelDistrib.Syst.,2020,pp.697–702.
Commun.Syst.,2017,pp.38–48. [54] K.Suo,Y.Zhao,W.Chen,andJ.Rao,“Demo/posterabstract:Efficient
[29] S. Baidya, Y. Chen, and M. Levorato, “eBPF-based content and andflexiblepackettracingforvirtualizednetworksusingeBPF,”inProc.
computation-aware communication for real-time edge computing,” in IEEEConf.Comput.Commun.Workshops,2018,pp.1–2.
Proc.IEEEConf.Comput.Commun.Workshops(INFOCOMWKSHPS), [55] K.Suo,Y.Zhao,W.Chen,andJ.Rao,“vNetTracer:Efficientandpro-
2018,pp.865–870. grammablepackettracinginvirtualizednetworks,”inProc.IEEE38th
[30] Facebook,“Katran:Ahighperformancelayer4loadbalancer,”Accessed: Int.Conf.Distrib.Comput.Syst.,2018,pp.165–175.
Feb.06,2023.[Online].Available:https://github.com/facebookincubator/ [56] Elastic,“Driveoptimizationandsustainabilitywithcontinuousprofiling,”
katran Accessed: Mar. 02, 2025. [Online]. Available: https://www.elastic.co/
[31] M. Xhonneux, F. Duchene, and O. Bonaventure, “Leveraging eBPF observability/universal-profiling
for programmable network functions with ipv6 segment rout- [57] A.PerdanaputraandA.I.Kistijantoro,“Transparenttracingsystemon
ing,” in Proc. 14th Int. Conf. Emerg. Netw. Exp. Technol., 2018, GRPCbasedmicroserviceapplicationsrunningonkubernetes,”inProc.
pp.67–72. 7thInt.Conf.Adv.Inform.:Concepts,TheoryAppl.,2020,pp.1–5.
[32] Y. Choe, J.-S. Shin, S. Lee, and J. Kim, ““eBPF/XDP based network [58] tcpdump,“TCPDUMP&LIBPCAP,”Accessed:Mar.01,2023.[Online].
trafficvisualizationanddosmitigationforintelligentserviceprotection,” Available:https://www.tcpdump.org/
in Proc. Int. Conf. Emerg. Internetworking, Data Web Technol., 2020, [59] P.GoyalandA.Goyal,“Comparativestudyoftwomostpopularpacket
pp.458–468. sniffingtools-TcpdumpandWireshark,”inProc.9thInt.Conf.Comput.
[33] S. Qi, L. Monis, Z. Zeng, I.-C. Wang, and K. K. Ramakrishnan, Intell.Commun.Netw.,2017,pp.77–81.
“SPRIGHT: Extracting the server from serverless computing! high- [60] WireShark, “The world’s most popular network protocol analyzer,”
performance eBPF-based event-driven, shared-memory processing,” in Accessed:Mar.01,2023.[Online].Available:https://www.wireshark.org/
Proc.ACMSIGCOMM2022Conf.,2022,pp.780–794. [61] Istio, “Istio: Simplify observability, traffic management, security, and
[34] S.-C.OhandS.-W.Kim,“AnefficientLinuxkernelmodulesupporting policywiththeleadingservicemesh,”Accessed:Feb.06,2023.[Online].
TCP/IPoffloadengineongrid,”inProc.5thInt.Conf.GridCooperative Available:https://istio.io
Comput.,2006,pp.228–235.
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on March 20,2026 at 23:38:08 UTC from IEEE Xplore. Restrictions apply.

1494 IEEETRANSACTIONSONPARALLELANDDISTRIBUTEDSYSTEMS,VOL.36,NO.7,JULY2025
[62] E.Songetal.,“INT-label:Lightweightin-bandnetwork-widetelemetry PengfeiChenreceivedthegraduationdegreefrom
viadistributedlabeling,”IEEETrans.ParallelDistrib.Syst.,vol.35,no.5, the Department of Computer Science, Xi’an Jiao-
pp.751–767,May2024. tong University and the PhD degree, in 2016. He
[63] Pixie, “Pixie: Open source kubernetes observability for developers,” iscurrentlyaprofessorintheSchoolofComputer
Accessed:Mar.02,2025.[Online].Available:https://px.dev ScienceandEngineeringofSunYat-senUniversity.
[64] Y. Yang, L. Wang, J. Gu, and Y. Li, “Capturing request execution Meanwhile,heisaPhDadvisor.Heisinterestedin
pathforunderstandingservicebehavioranddetectinganomalieswithout distributed systems, AIOps, cloud computing, Mi-
code instrumentation,” IEEE Trans. Services Comput., vol. 16, no. 2, croserviceandBlockChain.Especially,hehasstrong
pp.996–1010,Mar./Apr.2023. skillsincloudcomputing.Sofar,Dr.Chenhaspub-
[65] P.Las-Casas,J.Mace,D.Guedes,andR.Fonseca,“Weightedsampling lished more than 60 papers in some international
ofexecutiontraces:Capturingmoreneedlesandlesshay,”inProc.ACM conferencesincludingACM/IEEEASE,ACM/IEEE
Symp.CloudComput.,2018,pp.326–332. ICSE,IEEEINFOCOM,WWWandjournalsincludingIEEETransactionson
[66] L. Zhang, Z. Xie, V. Anand, Y. Vigfusson, and J. Mace, “The benefit DependableandSecureComputing,IEEETransactionsonNeuralNetworks
of hindsight: Tracing edge-cases in distributed systems,” in Proc. 20th andLearningSystems,IEEETransactionsonReliability,IEEETransactionson
USENIXSymp.Netw.Syst.Des.Implementation,2023,pp.321–339. ServicesComputing.Heservesasofprogramcommitteememberofmultiple
[67] L.Castanheira,T.A.Benson,andA.Schaeffer-Filho,“Thecaseformore conferences and reviewers of some internal journals such as IEEE Transac-
flexibledistributedtracing,”inProc.StudentWorkshop,2020,pp.27–28. tions on Parallel and Distributed Systems, ACM Transactions on Software
[68] C.Lee,R.Yoshitani,andT.Hirotsu,“Enhancingpackettracingofmi- EngineeringandMethodology,IEEETransactionsonDependableandSecure
croservices in container overlay networks using eBPF,” in Proc. 17th Computing,IEEETransactionsonComputers.
Asian Internet Eng. Conf., New York, NY, USA, 2022, pp. 53–61,
doi:10.1145/3570748.3570756.
[69] OpenTelemetry,“OpentelemetryautoinstrumentationusingeBPF,”2023.
KaiLiureceivedthemaster’sdegreeinelectronicand
Accessed: Oct. 18, 2023. [Online]. Available: https://github.com/open-
communicationengineeringfromtheBeijingUniver-
telemetry/opentelemetry-go-instrumentation/
sityofPostsandTelecommunications,in2020.He
[70] Odigos,“ODIGOS:Generatedistributedtracesforanyapplicationwith-
iscurrentlyaseniorsoftwareengineerwithAlibaba
outcodechanges,”Accessed:Mar.02,2025.[Online].Available:https:
Cloud.Hisresearchinterestsencompasscloud-native
//github.com/odigos-io/odigos
architectures,microservices,andobservability.
Huxing Zhang received the master’s degree from
Shanghai Jiaotong University. He is currently a
Wanqi Yang received the BS degree in computer
staff engineer with Alibaba Cloud. His research
scienceandtechnologyfromSunYat-SenUniversity,
interests include cloud native, microservices, and
Guangzhou,China.Sheiscurrentlyworkingtoward
observability.
the PhD degree in computer science and technol-
ogywiththeSchoolofComputerScienceandEn-
gineering,SunYat-SenUniversity.Herresearchin-
terestsincludeeBPF,cloudcomputing,andcomputer
network.
Authorized licensed use limited to: Universidad Catolica Santa Maria. Downloaded on March 20,2026 at 23:38:08 UTC from IEEE Xplore. Restrictions apply.