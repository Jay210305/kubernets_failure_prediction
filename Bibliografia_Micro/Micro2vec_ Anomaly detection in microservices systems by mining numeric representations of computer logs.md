JournalofNetworkandComputerApplications208(2022)103515
ContentslistsavailableatScienceDirect
JournalofNetworkandComputerApplications
journalhomepage:www.elsevier.com/locate/jnca
Micro2vec:Anomalydetectioninmicroservicessystemsbyminingnumeric
representationsofcomputerlogs
MarcelloCinquea,1,RaffaeleDellaCortea,∗,1,AntonioPecchiab,1
aDipartimentodiIngegneriaElettricaedelleTecnologiedell’Informazione,UniversitàdegliStudidiNapoliFedericoII,ViaClaudio21,Napoli,80125,Italy
bDipartimentodiIngegneria,UniversitàdegliStudidelSannio,PalazzoBoscoLucarelliC.soGaribaldi107,Benevento,82100,Italy
A R T I C L E I N F O A B S T R A C T
Keywords: This paper describes a study on log mining in the domain of microservices technologies. We focus on the
Logmining detectionofanomaliesfromlogs,i.e.,eventsrequiringdeeperinspectionbyanalysts.Logminingischallenging
Anomalydetection in microservices systems due to the high number of heterogeneous logs. We present Micro2vec, a novel
Microservice approach to mine numeric representations of computer logs without making assumptions on the format of
Monitoring
underlyingdataandrequiringnoapplicationknowledge;representationscomputedbyMicro2vec aresuited
for anomaly detection. To cope with the lack of publicly-available datasets of labeled logs from production
systems, we validate our approach by means of a mixture of direct measurements from logs, one-class
classification experiments and generation of log variants. The study has been conducted in the context of a
ClearwaterIPMultimediaSubsystemsetupconsistingofmicroservicesdeployedinDockercontainers,andona
real-worldcriticalinformationsystemfromtheAirTrafficControldomain,whichimplementsacommunication
modeltypicallyusedwithmicroservices.
1. Introduction forththecompositionofmicroservicesbydifferentvendors–andthus
differently skilled development teams – that exacerbates format and
Microservices represent an evolution of the service-oriented archi- semantic heterogeneity of logs. In consequence, it becomes hard for
tecture (SOA) paradigm (Wolff, 2016). They put forth reduced size, practitioners to maintain exhaustive catalogues of keywords, regular
independency, flexibility and modularity principles, which well cope expressions or correlation rules, which are typically used to monitor
with ever-changing business environments; as such, they are strongly runtime logs in many state-of-art log management and SIEM2 tools,
intertwined with the current industry mainstream in Agile and De- such as Logstash3 or Splunk.4 Microservices ‘‘bring heterogeneity of
vOps (Bass et al., 2015). We observe that architectural advantages distributedsystemstoitsmaximumexpression’’(Dragonietal.,2017):
broughtbymicroservicesposenovelchallengestologanalysis,which areal-worlddeploymentcaneasilyreachtensofmicroservicesand–in
hasbeenextensivelyusedoverthepastdecadestoevaluateproduction turn–logfiles.
systems (Oliner et al., 2012; Cinque et al., 2016, 2020b). A log is a This paper describes our study on log mining in microservice sys-
sequence of text lines stored in a file, reporting information on the tems. We take a different perspective from current research trends
runtimebehaviorofacomputersystem. in microservices, which leverage OS metrics, e.g., CPU usage and free
Microservice systems’ deployments tend to create a distinct log memory, as opposite to text logs (Fadda et al., 2016; Thalheim et al.,
per-microservice, which causes substantial cognitive work by human 2017).Weclaimthat microservicesexacerbatetheroleof eventlogs:
expertsintraversingthelogsinordertopinpointandcorrelaterelevant theiranalysisisextremelyrelevanttopractitionerssincetheyprovide
linesforforensicsandtroubleshooting.Moreover,currenttrendsput morefine-graineddatawithrespecttoOSmetrics.Tothebestofour
knowledge there is a lack of approaches that leverage logs in this
∗ Correspondingauthor.
E-mailaddresses: macinque@unina.it(M.Cinque),raffaele.dellacorte2@unina.it(R.DellaCorte),antonio.pecchia@unisannio.it(A.Pecchia).
1 Allauthorsequallycontributedtothiswork.
2 SecurityInformationandEventManagement(Kavanaghetal.,2016;Cardenasetal.,2013).
3 https://www.elastic.co/products/logstash.
4 http://www.splunk.com/.
5 Thelabel–alsoknownasgroundtruth–pertainstotheknowledgeoftheeventsoccurredinacertainsystemwhenthelogswerecollected.
6 Wedenotebyeventanoperatingcondition,i.e.,eithernormaloranomalous,ofagivensystem;theoccurrenceofaneventmaybereportedbyoneormore
linesinthelog(s)ofthesystem.
https://doi.org/10.1016/j.jnca.2022.103515
Received30May2022;Receivedinrevisedform19August2022;Accepted6September2022
Availableonline1October2022
1084-8045/©2023TheAuthors.PublishedbyElsevierLtd.ThisisanopenaccessarticleundertheCCBY-NC-NDlicense(http://creativecommons.org/licenses/by-
nc-nd/4.0/).

M.Cinqueetal. JournalofNetworkandComputerApplications208(2022)103515
domain.Moreimportantly,nopublicly-availabledatasetsoflabeled5logs The rest of the paper is organized as follows. Section 2 covers
are available in this context. The label is particularly important, as the related work in the area. Section 3 discusses Micro2vec, while
it is typically used to train/test classifiers for anomaly detection. We Section 4 introduces the Clearwater case study. Section 5 describes
present a specific application in this context, related to the detection the datasets collected in Clearwater, and the procedure to generate
ofanomalies(oranomalousevents)fromlogs,i.e.,events6 requiring logvariants.Section6presentsadiscussionoftheimplicationsofthe
deeper inspection by analysts (D’Amico and Whitley, 2008; Cinque approach,whileSection7describestheresultsobtainedinthecontext
et al., 2020a), such as failures and misuse. According to D’Amico and of Clearwater. Section 8 describes the ATC case study and related
Whitley (2008), the detection of anomalies is one of the first steps results. Section 9 discusses the threats to validity, while Section 10
foreseenincomputersecuritydefenseanalysis.Theautomaticdetection concludesthework.
oftheseeventsallowsreducingthemanualworkrequiredtodiginto
logs, in case of incidents. The proposed approach has been applied 2. Relatedwork
in a Clearwater IP Multimedia Subsystem (IMS) setup consisting of
microservices deployed in Docker containers, which well-represents This section summarizes the related work in the area of microser-
a typical microservices setup. Further, to address threats to validity vices monitoring, mining metrics for event detection and security ap-
concerns, the proposal has been applied in the context of a critical plications.
informationsystemfromtheAirTrafficControl(ATC)domain,which
implementsacommunicationmodeltypicallyusedwithmicroservices. 2.1. Microservicesmonitoring
The contribution of the paper is twofold. First, we propose Mi-
cro2vec, a novel log mining approach that embeds no application Commercial and open-source tools are available for microservices
knowledge,makesnoassumptionsontheformat/semanticsoflogs,and monitoring.Forexample,Dynatrace,AppDynamics,CAandNewRelic
are commercial Application Performance Management (APM) tools
requiresnoa-prioricataloguesofanomalies’symptoms/patternstocope
that leverage source code instrumentation to monitor microservices.
withthechallengesmentionedabove.Thisispursuedbycomputingnu-
Instana is a commercial APM solution that leverages the span data
mericrepresentationsofheterogeneouscomputerlogs,whichallows
model (Benjamin et al., 2010) to trace all the requests generated by
inferring‘‘actionable’’relationshipsforanomalydetection.Second,we
properlyinstrumentedmicroservices.
aim to overcome the scarceness of publicly available labeled logs in
A similar approach is used in Zipkin (2022), the open-source dis-
thiscontext,whichisalong-standingresearchchallengeinmanyfield
tributedtracerformicroservicesdevelopedbyTwitter.Sysdig(Sysdig,
datastudies.Inthisrespect,weaddressthevalidationoftheproposed
2022)isacontainer-nativemonitoringsolution,whichallowscollect-
approachthroughamixtureofexperimentsthatinvolveboth(i)direct
ing resource usage, network statistics, as well as tracing applications
collectionoflogsrelatedtonormalandanomalouseventsinacontrolled
running inside containers. Netflix Hystrix (Netflix Hystrix, 2022) is a
testbed,and(ii)thesynthesisoflogvariantsbymeansofperturbation
latencyandfaulttoleranceJavalibrarydesignedtopreventcascading
of the content of the normal logs. Log variants are generated by
failuresindistributedsystems.
solelylookingatnormallogs,withnoknowledgeonanomalies.Most
A transparent tracing for microservice-based applications is pre-
notably,wegeneratedacomprehensivesampleoflabeledlogs,which
sented in Santana et al. (2019), which leverages proxies for relieving
we made publicly available for research purposes. We mitigate the
theburdenoftracingactivitiesfromapplications.TheworkNooretal.
threatstovalidityofourdetectionapproachbyanalyzingthedatawith
(2019)presentsagenericmonitoringframeworkforapplicationsbased
differenttechniques,includingmulti-classandone-classclassification,
onmulti-virtualization(e.g.,containers/VMs).Theframeworkincludes
andclassificationdoneonthetopoflogvariants.Thekeyoutcomes
agents, collecting system-level statistics, and a manager that retrieves
and findings of our study – with respect to the data and systems in
andanalyzesthecollecteddata.
hand–are:
A microservices monitoring tool, named MetroFunnel, is presented
inCinqueetal.(2022).Thetoolaimstoaccompanymicroserviceslogs
• Micro2vec,anovelminingapproachthatisabletocapitalizeonthe
withpassivetracinginordertosupportinformeddecisionsbypracti-
availability of multiple – potentially distributed – logs. At the time
tioners. In Brandón et al. (2020) a root cause analysis framework for
being,microservicesareoftendesignedtotrusteachother;once
microservicearchitecturesispresented.Itperformsanomalydetection
gainedaccesstoonemicroservice,anattackermightbringdown
leveragingagraphrepresentationofthesystemarchitecture,obtained
an entire application (Dragoni et al., 2017). Nevertheless, real-
bydifferentdatasources,e.g.,networkactivityandresourceusage.
life anomalies will likely involve many microservices within an
MicroRCAdetectsperformanceissueandlocatestheirrootcausesin
application(e.g.,theNetflixcompromisedescribedinSunetal. microservicesusingapplicationandsystemlevelmetrics,e.g.,resource
(2015)). As such, we claim that the ability to read ‘‘across the usage and response time (Wu et al., 2020). Sage (Gan et al., 2020)
lines’’ofmultiplelogsisacrucialfeatureinthiscontextaswell performsrootcauseanalysisforcloudmicroservices,leveragingCausal
asinanydistributedsystem. Bayesian Networks and Graphical Variational Auto-Encoder to model
• Anomaliesdoreflectintotherelationshipsofthemetricsacrossdiffer- dependencies between microservices, latency propagation, and detect
entlogs.Asaconfirmationofthefirstfinding,wediscoveredthat QoS violations. In Srirama et al. (2020) a microservices scheduling
different events are characterized by precise signatures, which strategy for cloud environments is proposed. The approach leverages
reflectintocomplexpatternsacrossmicroservices’logs.Wepave amonitoringmechanismbasedonsystem-levelmetrics(i.e.,CPUand
thewayfordiscoveryapproachesininferringexplicabledetection memoryusage)tomonitortheresourcesusedbymicroservices(onboth
rulesthatcannotbecaughtbyhumanexperts. physicalandvirtualmachines)forresourcescaling.
• Variantsobtainedfromnormallogscanbeusedtodetectrealanoma-
lies.Differentlyfromsomerecentcontributionsinthisarea(Cao 2.2. Miningnumericmetricsforanomalydetection
et al., 2016; Xie et al., 2018), we generate log variants with no
knowledge of anomalies, which makes our approach potentially Extracting OS, middleware and application metrics from logs and
independentfromtheavailabilityoflabeledlogs.Moreover,the other monitoring tools is valuable for many applications. In Farshchi
obtainedresultssuggestthattheusageoflogvariantsprovidesan etal.(2018)ispresentedananomalydetectiontechniqueforsporadic
advantagewithrespecttoone-classapproachesindetectingreal cloudoperation.Thetechniquecorrelateseventlogsandcloudmetrics
anomalies. todetectanomaliesduringoperation.Ananomalydetectiontechnique
2

M.Cinqueetal.
JournalofNetworkandComputerApplications208(2022)103515
leveraging Natural Language Processing is proposed in Bertero et al. leverages reinforcement learning techniques to perform the analysis
(2017);analysisisperformedthroughtheGoogleword2vecalgorithm. of MPI logs for anomalous user detection. The Authors also present
An approach for mining console logs to detect runtime problems a synthetic data generation method based on Generative Adversarial
in large-scale systems is presented by Xu et al. (2008). The approach Networks(GAN)tofacethelackofanomalousdatafortraining.Simi-
| extracts | structured | information |     | from console | logs | and | constructs vec- |     |     |     |     |     |     |     |
| -------- | ---------- | ----------- | --- | ------------ | ---- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- |
larly,inCaoetal.(2016)ispresentedaframeworkforthegeneration
torsoffeatures.InCamposetal.(2018)astudyontheuseofmachine
|     |     |     |     |     |     |     |     | of attack | variants. | An attack is | represented | by an | event | sequence. |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | --------- | ------------ | ----------- | ----- | ----- | --------- |
learningforsupportingfailurepredictionispresented.Thestudyuses
Givenasequenceofeventsinanattack,theseeventsarereplacedwith
datasets containing failure and non-failure data, which consist of nu- interchangeable events to generate new sequences, which represent
| meric features | representing |     | the | system | behavior. | Zoppi | et al. (2016) | attackvariants. |     |     |     |     |     |     |
| -------------- | ------------ | --- | --- | ------ | --------- | ----- | ------------- | --------------- | --- | --- | --- | --- | --- | --- |
presentsananomalydetectionapproachforService-OrientedArchitec- AsimilarmethodisintroducedinXieetal.(2018),usinganexisting
tures(SOAs),whichcopeswithSOAsdynamicity,bycollectingmetrics attack dataset for training a GAN, which is then used for the attack
atdifferentsystemlayers. variants generation. It is important to note that, differently from our
In Ahuja et al. (2021) a number of metrics (e.g., per flow packet logvariantsgenerationmethod,Luoetal.(2020)generatesvariantsin
| count, packet | rate) | are extracted |     | from network |     | flows, | which are then |     |     |     |     |     |     |     |
| ------------- | ----- | ------------- | --- | ------------ | --- | ------ | -------------- | --- | --- | --- | --- | --- | --- | --- |
termsoffeaturevectorsinsteadoflogentries,Caoetal.(2016)requires
| used to | detect DDoS | attacks | in  | software | defined | networks | by using |     |     |     |     |     |     |     |
| ------- | ----------- | ------- | --- | -------- | ------- | -------- | -------- | --- | --- | --- | --- | --- | --- | --- |
adetailedanalysisofpastobservedattacks,whileCaoetal.(2016)and
machinelearningmodels.TheworkinBehaletal.(2018)proposesa
Xieetal.(2018)generatevariantsfromexistingattackdatainsteadof
DDoSattackdetectionapproachthatleveragesthegeneralizedentropy
usingnormaldata.
metric.NetworkflowscollectedatdifferentpointsofanInternetSer-
viceProvidernetworkaretranslatedinentropyobservations,whichare
2.4. Ourcontribution
thencombinedtodetectDDoSattacks.
2.3. Securityapplications Notwithstanding the amount of work and tools for microservices
monitoring,tothebestofourknowledgethereisalackofapproaches
Several approaches have been proposed for retaining relevant se- that leverage logs in this domain. Recent work started to address
curity data by means of feature extraction, attribute enrichment and monitoring challenges in deploying Virtual Machines (VMs), which –
various classifiers. For example, the filtering technique in Spathoulas similarly to containers – can be used to host microservices. Given the
andKatsikas(2010)makesuseofastatisticalapproachtocombinedif- large availability of Cloud providers, Authors in Fadda et al. (2016)
|     |     |     |     |     |     |     |     | propose a | multi-objective | mixed | integer | linear optimization |     | approach |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | --------------- | ----- | ------- | ------------------- | --- | -------- |
ferentfeatures,suchasnumberofoccurrences,frequencyofsignatures,
and prior knowledge regarding the alerts. Alerts are filtered using a tomaximizethequalityofmonitoring,addressingthecollectionofmet-
threshold-based approach. The work (Bakar et al., 2005) proposes an rics,suchasCPUusage,freememory andpowerconsumption.Similarly,
attributeenrichmentapproach.Itleveragesasetofqualityparameters inThalheimetal.(2017)ispresentedSieve,i.e.,aplatformtoanalyze
among traditional features, which are used to compute a score for the communication between containers hosting microservices. Sieve
classifyingalerts. capitalizes on OS metrics and sysdig, which requires a kernel module
TheoutlierdetectionalgorithminFuetal.(2010)addressesfilter- to observe the system calls used by microservices. While metrics are
ingthroughtheuseofweights,whichhighlighttheimportanceofthe widely-usedinnetworkedsystemsforanomalydetection(Ibidunmoye
attributes of alerts, e.g., the destination port or type. Frequent pairs etal.,2018),wetakeadifferentperspectivebyanalyzingtextlogs.In
of attribute-value are used as features to discriminate false positives. thisrespect,mostmicroservicesmonitoringapproachesrequireservice
Differentlyfromthisliterature,JulischandDacier(2002)putsforththe
|           |               |     |           |        |     |           |               | instrumentation | to              | pinpoint anomalies. |     | On the other     | hand, | logs are a |
| --------- | ------------- | --- | --------- | ------ | --- | --------- | ------------- | --------------- | --------------- | ------------------- | --- | ---------------- | ----- | ---------- |
| idea that | alerts belong | to  | a limited | number | of  | clusters, | which are in- |                 |                 |                     |     |                  |       |            |
|           |               |     |           |        |     |           |               | by-product      | of the system’s | execution           | and | are ubiquitously |       | emitted by |
ferredthroughageneralizationhierarchy.WorkbyValeuretal.(2004)
almostanysoftwarecomponents,suchasmicroservices.Forexample,
| discards | irrelevant | events | based | on active | monitoring; |     | every time an |     |     |     |     |     |     |     |
| -------- | ---------- | ------ | ----- | --------- | ----------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- |
theframeworkinZuoetal.(2020)usessystemlogstodetectanomalies
alertistriggered,itisanalyzedtoidentifypotentialvulnerabilitiesthe
inmicroservicearchitectures,butitalsoneedsthecollectionofquery
attackeristryingtoexploit.
|     |     |     |     |     |     |     |     | traces, which | requires | instrumentation |     | or placement | of  | a collector |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | -------- | --------------- | --- | ------------ | --- | ----------- |
InCinqueetal.(2017)ispresentedanentropy-basedsecurityana-
|     |     |     |     |     |     |     |     | inside each | microservice. | Our contribution, |     | instead, | is a | non intrusive |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ------------- | ----------------- | --- | -------- | ---- | ------------- |
lytics approach, which aims to measure the occurrence of interesting approach,basedontheuseofunmodifiedlogs.
| activities.    | A hierarchical |           | approach   | to mine | high   | threat       | alarms from |     |     |     |     |     |     |     |
| -------------- | -------------- | --------- | ---------- | ------- | ------ | ------------ | ----------- | --- | --- | --- | --- | --- | --- | --- |
| logs generated | by             | Intrusion | Prevention |         | System | is presented | in Meng     |     |     |     |     |     |     |     |
3. Proposedapproach
| et al. (2018). | The        | approach  | in Du    | et al.     | (2017), | named        | DeepLog, uses   |               |                |                   |         |                  |              |             |
| -------------- | ---------- | --------- | -------- | ---------- | ------- | ------------ | --------------- | ------------- | -------------- | ----------------- | ------- | ---------------- | ------------ | ----------- |
| a deep neural  | network    | to        | model    | a system   | log     | as a natural | language        |               |                |                   |         |                  |              |             |
|                |            |           |          |            |         |              |                 | Our approach, |                | named Micro2vec,7 |         | consists in      | transforming | dis-        |
| sequence.      | DeepLog    | learns    | patterns | from       | normal  | executions   | in order        |               |                |                   |         |                  |              |             |
|                |            |           |          |            |         |              |                 | tributed      | microservices  | logs into         | numeric | representations. |              | This is     |
| to detect      | anomalies. | In        | Yang et  | al. (2019) | is      | proposed     | nLSALog, an     |               |                |                   |         |                  |              |             |
|                |            |           |          |            |         |              |                 | done with     | no application | knowledge,        |         | no assumptions   |              | on the for- |
| anomaly        | detection  | framework | that     | leverages  | log     | files        | as data source. |               |                |                   |         |                  |              |             |
Theframeworkmodelsthelogasanaturallanguagesequenceanduses mat/semanticsoflogs,andnoa-prioricataloguesofanomalies.
(1≤j≤
LongShort-TermMemory(LSTM),builtusingnominaltrainingdata,to LetusconsiderasystemcomposedbythemicroservicesM 𝑗
detectsecurityanomalies. S),suchasshownbyFig.1.Overallthemicroservicesgenerateagiven
The work in Liu et al. (2019) presents a heterogeneous graph numberoflogsdenotedbyL (1≤i≤N).Logsareseenasstreamsof
𝑖
embeddingbasedapproachforcyberthreatsdetection,namedlog2vec. textlinesandundergothreetasks,i.e.,sampling,scoring anddetection.
Theapproachconvertslogentriesintoaheterogeneousgraph,whichis Samplingisaperiodictaskwherelogsarecontinuouslysampledat
usedtodetectmaliciouslogentries.OmegaLog (Hassanetal.,2020)is regularintervals.GivenalogL,every𝑇 timeunitsthetaskacquires
𝑖
atrackerthatmergesapplicationandsystemlogstobuildaUniversal the new lines in L generated by the microservice during the past 𝑇,
𝑖
Provenance Graph (UPG). The UPG combines the causal reasoning creatingachunk.Thespecificchoiceof𝑇
forourstudyisdiscussedin
strengths of whole-system logging with the rich semantic context of Section4.SamplingisdoneindividuallyforeachL:therefore,thetask 𝑖
| application | logs | to improve | the | reasoning | of investigators |     | about the |     |     |     |     |     |     |     |
| ----------- | ---- | ---------- | --- | --------- | ---------------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
natureofattacks.
ADA (Adaptive Deep Log Anomaly Detection) (Yuan et al., 2020) 7 The2vecsuffixisusedsincetheproposalleveragesvectorrepresentation
allowsthedetectionofsecurity-relatedanomaliesinsystemlogs,lever- asdonebyotherexisting*2vecapproaches(Mikolovetal.,2013;DeKoninck
| agingLSTManddynamicadaptivethresholds.ReLog |     |     |     |     |     | (Luoetal.,2020) |     | etal.,2018). |     |     |     |     |     |     |
| ------------------------------------------- | --- | --- | --- | --- | --- | --------------- | --- | ------------ | --- | --- | --- | --- | --- | --- |
3

M.Cinqueetal.
JournalofNetworkandComputerApplications208(2022)103515
|     |     |     |     |     |     |     |     |     |     | Fig.2. | Scoringtaskdetails. |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | ------------------- | --- | --- | --- |
Fig.1. OverviewofthetasksofMicro2vec.
*Statussip_connect:RecycleTCPconnectionslot*
|                     |                          |         |     |             |      |          | The presence |           | of variable   | fields | might distort | the    | scoring          | task, which |
| ------------------- | ------------------------ | ------- | --- | ----------- | ---- | -------- | ------------ | --------- | ------------- | ------ | ------------- | ------ | ---------------- | ----------- |
| generates           | a new set of chunks      | – chunk | set | hereinafter | – at | every 𝑇, |              |           |               |        |               |        |                  |             |
|                     |                          |         |     |             |      |          | aims         | to assign | larger scores | to     | infrequent    | terms. | Data preparation | is          |
| encompassingchunksC | correspondingtothelogsL. |         |     |             |      |          |              |           |               |        |               |        |                  |             |
𝑖 𝑖 a core component and a well-consolidated practice in log analysis.
| The scoring | task computes |     | a quantitative |     | metric | – score |     |     |     |     |     |     |     |     |
| ----------- | ------------- | --- | -------------- | --- | ------ | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
Forinstance,inthescoringapproachproposedinStearleyandOliner
hereinafter–foreachchunkinthechunkset.Thereexistmanymeth-
(2008)alltermsthatoccuroncearediscarded;similarconsiderations
| ods for extracting | metrics | from logs, | such | as (Farshchi | et  | al., 2018; |     |     |     |     |     |     |     |     |
| ------------------ | ------- | ---------- | ---- | ------------ | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
areinLimetal.(2008)andKobayashietal.(2018).
Berteroetal.,2017;Xuetal.,2008;Cinqueetal.,2017;Stearleyand
|                |                |           |           |          |                |        | The    | scoring | task (i)       | removes | special  | non-alphanumeric |     | characters  |
| -------------- | -------------- | --------- | --------- | -------- | -------------- | ------ | ------ | ------- | -------------- | ------- | -------- | ---------------- | --- | ----------- |
| Oliner, 2008). | After having   | reviewed  | the       | methods, | we selected    | the    |        |         |                |         |          |                  |     |             |
|                |                |           |           |          |                |        | (e.g., | #, ?,   | ;, and %) from | the     | logs and | (ii) implements  |     | a stop-word |
| log.entropy,   | i.e., the term | weighting | technique |          | used in Cinque | et al. |        |         |                |         |          |                  |     |             |
list
(2017)andStearleyandOliner(2008),whichwasdemonstratedtobe toavoidconventionalterms,suchasnamesofdays/months.More
effective for handling text logs. Although other methods might have important, the scoring task replaces each line with the corresponding
beenadoptedforscoring,digging intothesemethodsisnotthepurpose pattern, leveraging a replacements base, which is populated offline
|     |     |     |     |     |     |     | (offlinetuning |     | inFig.2)withthepatternsautomaticallyinferredfrom |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ------------------------------------------------ | --- | --- | --- | --- | --- |
ofourstudy;ratherwefocusontheuseoflog-drivennumericmetrics
|     |     |     |     |     |     |     | the logs | generated | by  | the system | under | normal | activity.8 | Each line |
| --- | --- | --- | --- | --- | --- | --- | -------- | --------- | --- | ---------- | ----- | ------ | ---------- | --------- |
inanovelapplicationdomain.
|                                                         |     |     |     |     |     |     | is replaced |     | with the corresponding |     | pattern, | if available |     | in the base; |
| ------------------------------------------------------- | --- | --- | --- | --- | --- | --- | ----------- | --- | ---------------------- | --- | -------- | ------------ | --- | ------------ |
| Fig.2detailsthescoringtaskofMicro2vec.ForeachchunkC,the |     |     |     |     |     | 𝑖   |             |     |                        |     |          |              |     |              |
otherwiseitisleftunchanged.
scoringtask(i)performsadatapreparation(whichconsistsofparsing
| the logs and | clearing special | characters, | as  | described | in Section | 3.1), |     |     |     |     |     |     |     |     |
| ------------ | ---------------- | ----------- | --- | --------- | ---------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
(ii)extractsalltheterms–atermisasequenceofcharactersseparated 3.2. Computationofthescore
bywhitespace(s)–fromthechunk,(iii)countstheoccurrencesofeach
term within the chunk, and (iv) computes a numeric score, i.e., the Each chunk C 𝑖 sampled from L 𝑖 is ‘‘prepared’’ as described above.
log.entropy. Wethenextractthepairsterms-counts,i.e.,thenumberofoccurrences
The output of the scoring task is a vector of scores S (1 ≤ i ofeachdistinctterminthechunkafterpreparation.Let𝑥 denotethe
|     |     |     |     |     |     | 𝑖   |     |     |     |     |     |     |     | 𝑡   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
≤ N), i.e., one score per chunk in the chunk set; a new vector is countoftheterm𝑡inthechunkC ,with1≤t≤Wand𝑊 thetotal
𝑖
generated at every 𝑇. Each score of the vector summarizes the past number of distinct terms in C. We obtain the log.entropy of C as
|     |     |     |     |     |     |     |     |     | √   |     | 𝑖   |     |     | 𝑖   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
𝑇 time unit of one log. The vector organizes the scores computed ∑𝑊 ≥
|     |     |     |     |     |     |     | 𝑙𝑜𝑔.𝑒𝑛𝑡𝑟𝑜𝑝𝑦 | =   | (𝑒  | ⋅log (1+𝑥))2, | where | log.entropy |     | 0. Please |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- | ------------- | ----- | ----------- | --- | --------- |
during the same sampling round, which gives Micro2vec the ability 𝑡=1 𝑡 2 𝑡
|                  |           |         |            |        |            |     | notethat𝑒      | istheentropyoftheterm𝑡overasetof𝑀preparedchunks |           |      |             |            |          |        |
| ---------------- | --------- | ------- | ---------- | ------ | ---------- | --- | -------------- | ----------------------------------------------- | --------- | ---- | ----------- | ---------- | -------- | ------ |
| to read ‘across’ | the logs. | The use | of vectors | allows | leveraging | the |                | 𝑡                                               |           |      |             |            |          |        |
|                  |           |         |            |        |            |     | (term-by-chunk |                                                 | matrix in | Fig. | 2), i.e., C | plus (M-1) | baseline | chunks |
𝑖
relationshipsacrossthelogstodetectanomalies.Thedetectiontaskis stored in a database of normal logs produced offline by microservices
continuouslyfedwithvectorsofscores,witheachvectorrepresenting undernormaloperations.Indetail,let𝑥 denotethecountoftheterm
𝑡,𝑘
a chunk set; it determines whether a chunk set represents normal or 𝑡inthechunk𝑘,with1≤k≤Mand𝑥 =𝑥 (i.e.,thecountextracted
|     |     |     |     |     |     |     |     |     |     |     | 𝑡,𝑀 | 𝑡   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
anomalouseventsbasedonthevaluesofthescores.Theproposalisnot fromC).Theentropyiscomputedasfollows:
𝑖
tailoredtoaspecificdetectionalgorithm.Thereexistmanymethodsfor
𝑀
detectinganomaliesfromscores,e.g.,threshold-basedapproaches,use 1 ∑
|     |     |     |     |     |     |     | 𝑒 =1+ |     | 𝑝   | log (𝑝 | )   |     |     | (1) |
| --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | ------ | --- | --- | --- | --- |
ofclassifiers.WediscussthedetectionapproachinSection6. 𝑡 log (𝑀) 𝑡,𝑘 2 𝑡,𝑘
2 𝑘=1
𝑥 𝑡,𝑘
| 3.1. Datapreparation |     |     |     |     |     |     | 𝑝 = |      |     |     |     |     |     | (2) |
| -------------------- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- |
|                      |     |     |     |     |     |     | 𝑡,𝑘 | ∑𝑀 𝑥 |     |     |     |     |     |     |
|                      |     |     |     |     |     |     |     | 𝑘=1  | 𝑡,𝑘 |     |     |     |     |     |
Thedatapreparationstepaimstomitigatetheinherentvariability where𝑝 representstheprobabilitytohavetheterm𝑡inthechunk𝑘.
𝑡,𝑘
| of log lines, | which are fraught | with | very | infrequent | terms | (often oc- |     |     |     |     |     |     |     |     |
| ------------- | ----------------- | ---- | ---- | ---------- | ----- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
AsitcanbeinferredfromEqs.(1)and(2),termsthatoccurregularly
curringjustonce),suchastimestamps,valueofvariables,andprocess
acrossthe𝑀chunkshavealowscore.Theresultofthescoringtaskfor
identifiers.
|                                      |     |     |     |                         |     |     | agivenlogC |           | 𝑖 isanewobservationofthescoreS,whichisforwarded |      |            | 𝑖        |     |               |
| ------------------------------------ | --- | --- | --- | ----------------------- | --- | --- | ---------- | --------- | ----------------------------------------------- | ---- | ---------- | -------- | --- | ------------- |
| Atypicalloglinecontainsbothinvariant |     |     |     | andvariablefields,ascan |     |     |            |           |                                                 |      |            |          |     |               |
|                                      |     |     |     |                         |     |     | to the     | detection | task along                                      | with | the scores | computed | for | all the logs. |
beseeninthefollowingexample:
16:29:39Statussip_connect:RecycleTCPconnectionslot14
16:29:43Statussip_connect:RecycleTCPconnectionslot2 8 Patterns are automatically obtained through log parsing. We implement
Itcanbenotedthattheloglinesshareacommonpattern,whichcan an iterative token-sanitization algorithm consistent with state-of-the-art ap-
beinferredbyremovingthevariablefields,i.e.,thetimestampandthe proaches (Vaarandi, 2008), which leverages a clustering-based approach to
slotnumberintheexample: identifyvariablefieldsandinferpatterns.
4

M.Cinqueetal.
JournalofNetworkandComputerApplications208(2022)103515
Table1
Clearwater’slogfilesbymicroservice.
|     |     |     |     |     |     |     | Microservice   |        | Logsources                        |        | Microservice   |          | Logsources  |          |
| --- | --- | --- | --- | --- | --- | --- | -------------- | ------ | --------------------------------- | ------ | -------------- | -------- | ----------- | -------- |
|     |     |     |     |     |     |     | astaire        |        | astaire.txt                       |        | bono           |          | bono.txt    |          |
|     |     |     |     |     |     |     | cassandra      |        | system.log                        |        | chronos        |          | chronos.txt |          |
|     |     |     |     |     |     |     | ellis          |        | ellis.txt                         |        | homer          |          | homer.txt   |          |
|     |     |     |     |     |     |     | Microservice   |        | Logsources                        |        |                |          |             |          |
|     |     |     |     |     |     |     | homestead-prov |        | homesteadprov.txt                 |        |                |          |             |          |
|     |     |     |     |     |     |     | homestead      |        | homestead.txt,homesteadaccess.txt |        |                |          |             |          |
|     |     |     |     |     |     |     | ralf           |        | ralf.txt,ralfaccess.txt           |        |                |          |             |          |
|     |     |     |     |     |     |     | sprout         |        | sprout.txt,sproutaccess.txt       |        |                |          |             |          |
|     |     |     |     |     |     |     | requests,      | status | messages,                         | errors | and exceptions | occurred | at          | runtime, |
andsoforth.Examplesofcollectednormalandanomalousloglinesare
|     |     |     |     |     |     |     | shown in | Fig. 4. | It is important |     | to note that | the anomalous |     | log lines, |
| --- | --- | --- | --- | --- | --- | --- | -------- | ------- | --------------- | --- | ------------ | ------------- | --- | ---------- |
i.e.,theonesfrombono.txt(lines6–7)andsprout.txt(lines9–
11),havebeencollectedduringanomalouseventssettings(whichwill
Fig.3. ExperimentalsetupofClearwater.
bedetailedinSection5),andreportoccurrederror/failure.Logsarepe-
riodicallysampledtogeneratethechunksetsforourscoring/detection
approachasdescribedinSection3.Inourstudy,thesamplingperiod
| The value | of (M-1), i.e., | the number | of  | baseline | chunks, | has been |     |     |     |     |     |     |     |     |
| --------- | --------------- | ---------- | --- | -------- | ------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
issetto𝑇 =30s,whichrepresentsatradeoffbetweenthelatencyof
| sized in         | such a way that | the normal | chunks’ | log.entropy |     | mean can     |               |     |          |              |              |     |        |          |
| ---------------- | --------------- | ---------- | ------- | ----------- | --- | ------------ | ------------- | --- | -------- | ------------ | ------------ | --- | ------ | -------- |
|                  |                 |            |         |             |     |              | the detection | and | the need | for ensuring | a reasonable |     | number | of lines |
| be characterized | with 10%        | accuracy   | at 90%  | confidence, |     | according to |               |     |          |              |              |     |        |          |
perchunk,whilethesamplesizeissetto(M-1)=120.
proceduresinJain(1991).
5. Datacollection
4. Experimentalsetup
Ourdatasetsencompass(i)logscollectedbymeansofdirectobser-
We use a Clearwater IMS setup as main case study. Clearwater vationsofClearwaterduringnormalandanomalousevents,and(ii)log
implements the standard IMS architecture, which is adopted by large variantsthatwesynthesizebyperturbingthecontentofnormallogsfor
| telcos for | IP-based voice, | video | and messaging | services |     | (Clearwater, |     |     |     |     |     |     |     |     |
| ---------- | --------------- | ----- | ------------- | -------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
validationpurposes.
| 2022). Clearwater | and IMS-related |             | technologies | have        | been | also used |        |      |        |          |                 |     |           |      |
| ----------------- | --------------- | ----------- | ------------ | ----------- | ---- | --------- | ------ | ---- | ------ | -------- | --------------- | --- | --------- | ---- |
|                   |                 |             |              |             |      |           | Please | note | that – | although | the experiments | are | conducted | in a |
| in research       | studies, such   | as Cotroneo | et           | al. (2017), | Di   | Mauro and |        |      |        |          |                 |     |           |      |
controlledenvironment–wereproduceamixtureofrealisticoperating
Liotta(2019)andNguyenetal.(2018).WeuseaversionofClearwater
scenariosbymeansofawell-consolidatedtestsuite,i.e.,Clearwater-live-
composedby11microservicesdeployedinasmanyDockercontainers
test.Thisisdonetoovercomethelackofpublicly-availabledatasetsfor
| on the same | virtual machine. | We  | describe | some | of the microservices |     |                  |     |                   |     |     |     |     |     |
| ----------- | ---------------- | --- | -------- | ---- | -------------------- | --- | ---------------- | --- | ----------------- | --- | --- | --- | --- | --- |
|             |                  |     |          |      |                      |     | thesystemin-hand |     | asmentionedabove. |     |     |     |     |     |
referencedbythispaper,whileacomprehensivearchitecturalviewof
ClearwatercanbefoundatClearwater(2022): 5.1. Normaleventsandanomalies
• bonoistheSessionInitiationProtocol(SIP)edgeproxyproviding
|     |     |     |     |     |     |     | Normal | logs | are obtained | by  | exercising | Clearwater | with | the live- |
| --- | --- | --- | --- | --- | --- | --- | ------ | ---- | ------------ | --- | ---------- | ---------- | ---- | --------- |
aWebRTCinterfacetoclients;
|          |                                                |     |     |     |     |     | test suite. | All the | collected | chunk | sets are labeled | as  | normal, | and used |
| -------- | ---------------------------------------------- | --- | --- | --- | --- | --- | ----------- | ------- | --------- | ----- | ---------------- | --- | ------- | -------- |
| • sprout | istheSIProuterthathandlesclientauthentication; |     |     |     |     |     |             |         |           |       |                  |     |         |          |
• cassandraisthedatabaseofprofiledata; to build the replacements base. Fig. 5 shows the scores of 4 out of
• homesteadisaRESTfulCRUDserverthatallowsretrievingauthen- 13Clearwater’slogs–forthesakeofbetterreadability–overaround
ticationcredentialsandusersprofile; one hour of normal operations; the 𝑥-axis is the progressive id of the
• chunkset sincethebeginningofthecollection.Itcanbenotedthatthe
| homer | isastandardXDMS(XMLDocumentManagementServer) |             |            |     |         |          |                                              |     |             |     |                        |                      |     |            |
| ----- | -------------------------------------------- | ----------- | ---------- | --- | ------- | -------- | -------------------------------------------- | --- | ----------- | --- | ---------------------- | -------------------- | --- | ---------- |
|       |                                              |             |            |     |         |          | mixtureoftestcaseswithinClearwater-live-test |     |             |     |                        | exposesvariousnormal |     |            |
| used  | to store MMTEL                               | (MultiMedia | TELephony) |     | service | settings |                                              |     |             |     |                        |                      |     |            |
|       |                                              |             |            |     |         |          | combinations                                 | of  | the scores. | For | example, homesteadprov |                      | is  | reasonably |
documents;
stablethroughalltheexecutionifnotforfewsporadicspikes;elliscan
• ellisrepresentstheprovisioningportal.
beeitherornotclosetohomesteadprov,asshowninbetweenthechunk
We use Clearwater-live-test (Clearwater test, 2022) to generate a sets30and70;finally,thescoreofhomerappearsgenerallyhigherthan
representative load for exercising Clearwater. Clearwater-live-test is a ellis.Wecapitalizeonmodelingtheserelationshipsacrossthelogsfor
well-consolidated suite of Ruby test programs. The tests used for our anomalydetection.
experimentsconsistin:(i)testsetup,i.e.,registeringacertainnumber Other than normal operations, we also collect logs during further
oftelephoneaccounts;(ii)issuingtheactualsequenceofserviceinvo- five settings, where each collection setting reproduces an anomaly,
cationstoClearwater(thenumberandtypeofinvocationsvaryacross suchasabruteforceauthentication,misuseofClearwater’sfunctionsor
thetests);(iii)testfinalization,whichdeletesthetelephoneaccounts. tampering withOSprocessesandresources.Allthechunksetscollected
The experimental setup is shown in Fig. 3. Clearwater’s Docker duringasettingarelabeledwiththerelatedanomaly.Overall,wecol-
microservices are hosted by an Ubuntu 16.04.03 LTS OS, Intel Xeon lectedaround387Mbofdata,whichaccountformorethan2millions
E5-2630Lv32.9GHz,4GbRAMserver.Microservicesareconnected of log entries. We reproduce the anomalies during the execution of
throughthedockerLAN172.18.0.*,whichisbridgedwiththephys- Clearwater-live-test (configured using default values for its parameters
icalLAN10.0.30.*.Assuch,clientshostedonadifferentmachine, in both normal and anomalous events settings), so that these events
which run instances of the above-mentioned Clearwater-live-test, are areoverlappedwithregularoperationsasitwouldoccurinproduction.
allowedtoreachthemicroservices. The choice of the events is inspired by previous studies, such as the
Overall 13 log files by Clearwater’s microservices are considered securityattackphasesinRuiu(1999)andSharmaetal.(2011).Table2
in this setup, as listed in Table 1 by microservice generating at least summarizes anomalies; each anomaly is mapped to the attack phase
onelog.Eachlogcontainsavarietyoflines,whichencompassreceived anditisaccompaniedbyadescriptionthatexplainshowtheanomaly
5

M.Cinqueetal.
JournalofNetworkandComputerApplications208(2022)103515
Table2
AnomalouseventssettingsinClearwater.
| Anomaly                        |     | PhaseasinRuiu(1999)andSharmaetal.(2011) |     |     |     |     |     |     |     |     |     |
| ------------------------------ | --- | --------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Bruteforceauthentication(AUTH) |     | Penetration                             |     |     |     |     |     |     |     |     |     |
Description:Theattackerattemptstogainunauthorizedaccesstothesystem;thisisemulatedthroughbruteforceloginattempts.
| Logdeletion(DEL) |     | Control |     |     |     |     |     |     |     |     |     |
| ---------------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Description:Theattackerattemptstocoverhis/hertracesbydeletinglogs;thisisemulatedbyremovingthelogofhomer.
| Registration(REG) |     | Embedding/Attackrelay |     |     |     |     |     |     |     |     |     |
| ----------------- | --- | --------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Description:Theattackerattemptsensuringthathe/shecanretaincontrolofthesystemevenifhim/heractionsarediscovered;thisisemulatedbyregisteringmultiple
accountsinthesystem-anewaccountisregisteredevery5s.
| Denialofservice(DoS) |     | Attackrelay |     |     |     |     |     |     |     |     |     |
| -------------------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Description:Theattackeroverloadsthesysteminordertoslowdowntheperformance;thesystemisexercisedwith10concurrentclients,witheachclientrunningan
instanceofClearwater-live-test.
| Killcontainer(KILL) |     | Attackrelay |     |     |     |     |     |     |     |     |     |
| ------------------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Description:Theattackerattemptstoblockthesystemoperationbykillingsomeservices;thisisemulatedthroughthekillofthebonocontainer,whichistheanchor
pointfortheclient’sconnectiontotheClearwatersystem.
Fig.4. Exampleofnormalandanomalousloglines.
|     |     |     |     |     |     | 5.2. Logvariants                                   |                   |                                           |           |            |                 |
| --- | --- | --- | --- | --- | --- | -------------------------------------------------- | ----------------- | ----------------------------------------- | --------- | ---------- | --------------- |
|     |     |     |     |     |     | Log variants                                       | are perturbations |                                           | of normal | logs. The  | idea of using   |
|     |     |     |     |     |     | such variants                                      | arises from       | the consideration                         |           | that it is | hard to foresee |
|     |     |     |     |     |     | how real-life                                      | events will       | practically                               | reflect   | across the | logs. Overall,  |
|     |     |     |     |     |     | theinherentuncertainty                             |                   | ofrealoperationallogsinreportinganomalies |           |            |                 |
|     |     |     |     |     |     | isathreatforobtainingaccuratedetectors.Infact,poor |                   |                                           |           |            | traininglogs    |
(i.e.,logsthatfailincoveringanexhaustivenumberofrealoperating
|     |     |     |     |     |     | conditions)     | will likely return | an       | ineffective | detector.    | As such, we are |
| --- | --- | --- | --- | --- | --- | --------------- | ------------------ | -------- | ----------- | ------------ | --------------- |
|     |     |     |     |     |     | aware that      | the sole settings  | shown    | in Table    | 2 – although | useful for      |
|     |     |     |     |     |     | some of         | the considerations | later    | on in this  | study –      | cannot provide  |
|     |     |     |     |     |     | a comprehensive | picture            | on the   | accuracy    | that can be  | expected with   |
|     |     |     |     |     |     | our approach.   | Please note        | that the | lack of     | data points  | from real-life  |
|     |     |     |     |     |     | anomalies       | is a challenge     | in many  | domains.    | For example, | in Sharma       |
etal.(2011)isshownthatmanysecurityincidentclasses,e.g.,spamand
infectedhosts,hadveryfewoccurrencesoveraverylongtimeframe.
|     |     |     |     |     |     | We propose | a systematic | procedure |             | to model  | the effects that |
| --- | --- | --- | --- | --- | --- | ---------- | ------------ | --------- | ----------- | --------- | ---------------- |
|     |     |     |     |     |     | anomalies  | may have in  | the logs  | through log | variants. | This is done by  |
Fig. 5. Scores of four logs over around one hour of normal operations (a chunk meansofanexperimentaldesignandcontrollablefactors(Jain,1991).
correspondsto30s). Letusintroducetheprocedureforgeneratingonevariant,beforehand;
|     |     |     |     |     |     | we then | discuss the generation |     | of the dataset | of  | variants for our |
| --- | --- | --- | --- | --- | --- | ------- | ---------------------- | --- | -------------- | --- | ---------------- |
experiments.
|     |     |     |     |     |     | A log | variant is generated | by  | randomly | selecting | a normal chunk |
| --- | --- | --- | --- | --- | --- | ----- | -------------------- | --- | -------- | --------- | -------------- |
isaccomplished.Thesesettingsarenotmeanttobeexhaustiveforall‘‘real-
|     |     |     |     |     |     | set, at first. | Within the | chunk set, | we then | randomly | select a number |
| --- | --- | --- | --- | --- | --- | -------------- | ---------- | ---------- | ------- | -------- | --------------- |
life’’anomaliesthatmayoccurinpractice.However,theyaimtoresemble
ofchunks𝑛(1≤𝑛≤N)toperturb.Foreachselectedchunk,perturbation
thestagesofpotentialsecurityattacksandtoshowhowsystemmisuses
consistsin:(i)modifyingthesize,i.e.,thenumberoflines,ofthechunk
maygeneratesuspiciouslogentries,whichcanbecaughtthroughthe byeitherclearingthechunk,orleavingthesizeunchanged,ordoubling
| proposal. While | we use them | in some of the | experiments | hereinafter, |     |     |     |     |     |     |     |
| --------------- | ----------- | -------------- | ----------- | ------------ | --- | --- | --- | --- | --- | --- | --- |
itbyduplicatingeachlineofthechunk;(ii)appendingacertainamount
| the key findings | of our paper | are supported | by a model | consisting | of  |     |     |     |     |     |     |
| ---------------- | ------------ | ------------- | ---------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
(i.e.,1%,5%or10%ofthesizeofthechunk)ofanomalouslinestothe
logvariants,asfollows. chunk.Ananomalouslineisasequenceofunknownterms,i.e.,terms
6

M.Cinqueetal.
JournalofNetworkandComputerApplications208(2022)103515
Table4
SummaryofthedatasetsfromClearwater.
|     |     |     |     |     |     |     |     | DatasetID |     | Eventstype |     | Nature    |     |     | #Chunksets |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | ---------- | --- | --------- | --- | --- | ---------- |
|     |     |     |     |     |     |     |     | D1        |     | NORMAL     |     | Real      |     |     | 2757       |
|     |     |     |     |     |     |     |     | D2        |     | NORMAL     |     | Real      |     |     | 127        |
|     |     |     |     |     |     |     |     | D3        |     | ANOMALOUS  |     | Real      |     |     | 81         |
|     |     |     |     |     |     |     |     | D4        |     | ANOMALOUS  |     | Synthetic |     |     | 2632       |
|     |     |     |     |     |     |     |     | D5        |     | ANOMALOUS  |     | Synthetic |     |     | 129        |
Table5
Metricsobtainedwiththetestset(FNNdenotesafeedforwardneuralnetwork).
Fig.6. Representationofthefactors. Precision Recall F-measure Accuracy
|     |     |     |     |     |     |     |     | AdaBoost.M1 |     | 0.974 |     | 0.973 | 0.973 |     | 97.3% |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ----- | --- | ----- | ----- | --- | ----- |
|     |     |     |     |     |     |     |     | Randomtree  |     | 0.973 |     | 0.973 | 0.973 |     | 97.3% |
Table3
|     |     |     |     |     |     |     |     | Autoencoder |     | 0.969 |     | 0.953 | 0.961 |     | 96.1% |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ----- | --- | ----- | ----- | --- | ----- |
Factorsandlevelsusedforlogvariants.
|        |                |     |     |                 |     |     |               | Decisiontree       |     | 0.960 |     | 0.957 | 0.957 |     | 95.7% |
| ------ | -------------- | --- | --- | --------------- | --- | --- | ------------- | ------------------ | --- | ----- | --- | ----- | ----- | --- | ----- |
| Factor | Level          |     |     |                 |     |     |               | FNN(4hiddenlayers) |     | 0.947 |     | 0.961 | 0.954 |     | 95.3% |
|        | LOW            |     |     | MEDIUM          |     |     | HIGH          | FNN(1hiddenlayer)  |     | 0.935 |     | 0.934 | 0.934 |     | 93.4% |
|        |                |     |     |                 |     |     |               | Bayesiannetwork    |     | 0.915 |     | 0.906 | 0.906 |     | 90.6% |
| IMPACT | 1              |     |     | 3               |     |     | 6             |                    |     |       |     |       |       |     |       |
| SIZE   | ×0             |     |     | ×1              |     |     | ×2            |                    |     |       |     |       |       |     |       |
|        | (chunkcleared) |     |     | (sizeunchanged) |     |     | (sizedoubled) |                    |     |       |     |       |       |     |       |
SNR 1% 5% 10% theyaresynthetic.Wemadeacomprehensivesampleoflogscollected
duringnormalandanomalouseventspubliclyavailable.9
6. Micro2vec:Validationandpracticalimplications
thatneveroccurinthedatabaseofnormallogs;eachunknowntermis
obtainedbyconcatenatingarandomstringtoagivennormalterm.
with1≤i≤Ndenotethechunksinachunk Numeric representations produced by Micro2vec can be conve-
| Moreformally,let𝐶 |     | 𝑖   |     |     |     |     |     |              |          |        |                 |     |        |      |           |
| ----------------- | --- | --- | --- | --- | --- | --- | --- | ------------ | -------- | ------ | --------------- | --- | ------ | ---- | --------- |
|                   |     |     |     |     |     |     |     | niently used | to infer | models | to discriminate |     | normal | from | anomalous |
set.Thefactorsaccountedforgeneratingthevariantsareindicatedin
events.Modelscanbeobtainedthroughwell-consolidatedmachineand
thefollowinganddepictedinFig.6:
|     |     |     |     |     |     |     |     | deep learning              | techniques | by  | the data                          | mining | community. |     | It is worth |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------------- | ---------- | --- | --------------------------------- | ------ | ---------- | --- | ----------- |
|     |     |     |     |     |     |     |     | notingthatMicro2vecdoesnot |            |     | mandateaspecificminingtechniqueto |        |            |     |             |
• impact(𝐼𝑀𝑃𝐴𝐶𝑇):numberofchunks–outoftotal𝑁–thatare
handletherepresentations:inordertodemonstratethevalidityofour
targetedbytheperturbation;
approachweuseavarietyoftechniquesrangingfromdecisiontreesto
• size(𝑆𝐼𝑍𝐸):numberoflinesofthechunk;
deepneuralnetworks.Foreachtechniqueassessed–giventhedatasets
| • signal-to-noise-ratio |     |     | (𝑆𝑁𝑅): | percentage |     | of anomalous | lines (al) |     |     |     |     |     |     |     |     |
| ----------------------- | --- | --- | ------ | ---------- | --- | ------------ | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
inTable4–D1∪D4servesastrainingset,whileD2∪D5isthetestset;
withrespecttothesizeofthechunk.
asubsetof20%datapointsofthetrainingsetservesasvalidationset,
𝑆𝐼𝑍𝐸 𝑆𝑁𝑅, whichisusedtoselectandtunethehyperparametersofthetechniques
| Given       | the value           | of  | and |       | the number |     | of anomalous  |          |                    |     |        |            |     |         |            |
| ----------- | ------------------- | --- | --- | ----- | ---------- | --- | ------------- | -------- | ------------------ | --- | ------ | ---------- | --- | ------- | ---------- |
|             |                     |     |     |       |            |     |               | in hand. | For the assessment |     | of the | techniques | we  | refrain | from using |
| lines is al | = ((𝑆𝐼𝑍𝐸∕100)⋅𝑆𝑁𝑅), |     |     | while | the number | of  | regular lines |          |                    |     |        |            |     |         |            |
D3(i.e.,thedatasetofrealanomalies)toavoidanybiasthatcouldbe
| (rl) is (𝑆𝐼𝑍𝐸−𝑎𝑙) |     | as shown | in  | Fig. 6. | As usually | done | in empirical |     |     |     |     |     |     |     |     |
| ----------------- | --- | -------- | --- | ------- | ---------- | ---- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
causedbythesettingsinTable2.
| assessments, | we  | categorize | the factors |     | through | a smaller | number of |             |     |           |          |     |              |        |       |
| ------------ | --- | ---------- | ----------- | --- | ------- | --------- | --------- | ----------- | --- | --------- | -------- | --- | ------------ | ------ | ----- |
|              |     |            |             |     |         |           |           | The results | are | presented | in Table | 5;  | the leftmost | column | shows |
levels(Jain,1991),e.g.,LOW,MEDIUM,HIGH.Table3summarizesthe
|              |            |           |        |             |        |          |             | the techniques    | assessed. | We       | compute           | the | typical    | metrics | of precision, |
| ------------ | ---------- | --------- | ------ | ----------- | ------ | -------- | ----------- | ----------------- | --------- | -------- | ----------------- | --- | ---------- | ------- | ------------- |
| value of     | the levels | in our    | study. | We generate | log    | variants | for all the |                   |           |          |                   |     |            |         |               |
|              |            |           |        |             |        |          |             | recall, F-measure | and       | accuracy | (Makhoul          | et  | al., 1999) | to      | quantify the  |
| combinations | of         | values in | IMPACT | × SIZE      | × SNR; | the only | exception   |                   |           |          |                   |     |            |         |               |
|              |            |           |        |             |        |          |             | effectiveness     | of the    | models   | at discriminating |     | normal     | from    | anomalous     |
occurswithSIZE =×0,whereSNRdoesnotapplybecausethevariant events. Results are based on WEKA10 and Keras11 implementations of
is obtained by clearing a number of chunks equal to IMPACT. As theautoencoderandthemultilayerfeedforwardneuralnetwork(FNN).
| such, we | obtain | total 21 | rather | than 27 | combinations |     | of the levels. |           |            |         |            |         |            |     |             |
| -------- | ------ | -------- | ------ | ------- | ------------ | --- | -------------- | --------- | ---------- | ------- | ---------- | ------- | ---------- | --- | ----------- |
|          |        |          |        |         |              |     |                | It can be | noted that | all the | techniques | achieve | remarkable |     | classifica- |
Giventhatrandomchoicesareperformedinconstructingthevariants,
|             |        |     |          |        |         |     |             | tion figures, | which | means | the numeric | representations |     |     | generated by |
| ----------- | ------ | --- | -------- | ------ | ------- | --- | ----------- | ------------- | ----- | ----- | ----------- | --------------- | --- | --- | ------------ |
| we generate | around | 120 | variants | (which | account | for | one hour of |               |       |       |             |                 |     |     |              |
Micro2veccanbeusedinconjunctionwithdifferenttechniques.Most
anomalousoperations)foreachcombinationofthelevels.Itisworthto
|     |     |     |     |     |     |     |     | notably, | the results | indicate | that | deep learning |     | models | can be used |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ----------- | -------- | ---- | ------------- | --- | ------ | ----------- |
notethattheproposedproceduredoesnotaimtoproducelogvariants
|     |     |     |     |     |     |     |     | to handle | the scores. | For | example, | in case | of  | the autoencoder | we  |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ----------- | --- | -------- | ------- | --- | --------------- | --- |
that resemble the logs generated during anomalies; rather, it aims to use a semi-supervised approach to learn a model of the normal data
mimictheeffectsthatanomaliesmayhaveonthelogs. points,beforehand;giventhepointsofthetestset,anomalydetectionis
pursuedbymeasuringthedistance–alsoknownasreconstructionerror
|     |     |     |     |     |     |     |     | – of the points | with | respect | to the | model. | The autoencoder |     | achieves |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | ---- | ------- | ------ | ------ | --------------- | --- | -------- |
5.3. Availabledatasets
0.969precisionand0.953recall,whichareamongthetopperforming.
We collect total 5 datasets of logs – and thus scores – which are As for the FNN with 4 hidden layers, we obtain 0.947 precision and
|     |     |     |     |     |     |     |     | 0.961 recall. | As a further |     | remark, | in order | to check | if  | our data are |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | ------------ | --- | ------- | -------- | -------- | --- | ------------ |
summarizedinTable4.EachdatasetisassignedanIDthatwillbeused
|     |     |     |     |     |     |     |     | affected by | class imbalance |     | issues, | we used | the AdaBoost.M1 |     | (Freund |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --------------- | --- | ------- | ------- | --------------- | --- | ------- |
throughtherestofthepaperforthesakeofclarity.D1andD2contain
andSchapire,1997)classifier.ItisimportanttonotethatAdaBoost.M1
NORMALvectorsofscores,whicharecollectedbymeansofindependent
isnotameantocheckifadatasetisimbalancedornot,butisusually
runsofClearwater-live-test;ontheotherhand,D3containsANOMALOUS
adoptedtoclassifyimbalanceddatasets(YuanandAbouelenien,2015).
| scores obtained | by  | emulating | the | settings | in Table | 2, which | are emu- |     |     |     |     |     |     |     |     |
| --------------- | --- | --------- | --- | -------- | -------- | -------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
latedinindependentexperiments.Noteworthy,scoresinD1,D2andD3
arecomputedfromlogsobtainedbydirectobservationsofClearwater– 9 www.dessert.unina.it/JNCA2022EventLogs.zip.
i.e.,real,inthe‘‘Nature’’columnofTable4–whileD4andD5contain 10 https://www.cs.waikato.ac.nz/ml/weka/.
vectors of ANOMALOUS scores obtained with log variants. Therefore, 11 https://keras.io/.
7

M.Cinqueetal.
JournalofNetworkandComputerApplications208(2022)103515
Table6
ResultsofANOVA(SST=0.0107;R-square=0.97;imp=importance).
|             |     | SS     | imp   |     | F-stat |     | p-value |     |     |     |     |     |     |     |
| ----------- | --- | ------ | ----- | --- | ------ | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
| IMPACT      |     | 0.0098 | 91.6% |     | 86.85  |     | 0.0005  |     |     |     |     |     |     |     |
| SIZE        |     | ≈0     | 0.0%  |     | 0.36   |     | 0.5822  |     |     |     |     |     |     |     |
| SNR         |     | 0.0003 | 2.8%  |     | 2.99   |     | 0.1622  |     |     |     |     |     |     |     |
| IMPACT⋅SIZE |     | ≈0     | 0.0%  |     | 0.17   |     | 0.8470  |     |     |     |     |     |     |     |
| IMPACT⋅SNR  |     | 0.0003 | 2.8%  |     | 1.45   |     | 0.3644  |     |     |     |     |     |     |     |
| SIZE⋅SNR    |     | ≈0     | 0.0%  |     | 0.24   |     | 0.7940  |     |     |     |     |     |     |     |
| Total       |     | 0.0104 | 97.2% |     | –      |     | –       |     |     |     |     |     |     |     |
Therefore,sinceAdaBoost.M1performanceiscomparablewiththebest Fig.7. ProfilerforSNRandIMPACT bySIZE.
performingclassifier,i.e.,randomtree,itcanbereasonablystatedthat
ourdataarenotaffectedbytheclassimbalanceissue.
Table7
Usageofthedatasets.
| Without | loss of generality, |     | we  | will focus | on  | the decision | tree: |     |     |     |     |     |     |     |
| ------- | ------------------- | --- | --- | ---------- | --- | ------------ | ----- | --- | --- | --- | --- | --- | --- | --- |
(i) it performs reasonably well in our context, as shown in Table 5, Section Trainingset Testset Notes
and(ii)muchmoreimportant,itproducesanoutputthatiscompact, 7.1 Notapplicable D2∪D3 K-foldcrossvalidation
comprehensible and useful to practitioners, which is crucial to the 7.2 D1 D2∪D3 One-classmodel
|     |     |     |     |     |     |     |     | 7.3 | D1∪D4 |     | D2∪D3 |     | Variant-based | model |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | ----- | --- | ------------- | ----- |
objectiveofautomatingthegenerationofdetectionrulesthatcancom-
plementexistingSIEMtools.Evenifdecisiontreescanbeaffectedby
theinstabilityissue(LiandBelford,2002),thisdoesnothappeninour
| settingsasweachievesimilarresultswithbothoriginalandperturbed |                   |     |          |       |         |       |             | 7. Results |     |     |     |     |     |     |
| ------------------------------------------------------------- | ----------------- | --- | -------- | ----- | ------- | ----- | ----------- | ---------- | --- | --- | --- | --- | --- | --- |
| datasets,                                                     | i.e., considering | log | variants | as it | will be | shown | later on in |            |     |     |     |     |     |     |
Wepresenttheresultsconcerninganomalydetection.Ouraimisto
thepaper.Weaimtoassesshowtheavailabilityofmeasurementsfrom
investigateboth(i)therelationshipsacrossmicroservices’logsforthe
differentlogsisbeneficialtothedetectionofanomaliesbymeansofthe
systeminhand,and(ii)theeffectivenessofourvariant-basedapproach
decisiontree.Thekeyadvantageinhavinglogvariantsobtainedunder
|              |                  |     |                    |     |            |     |          | as a workaround | to  | learn a model | in those | datasets | that lack | real-life |
| ------------ | ---------------- | --- | ------------------ | --- | ---------- | --- | -------- | --------------- | --- | ------------- | -------- | -------- | --------- | --------- |
| controllable | factors consists |     | in the possibility |     | to conduct | an  | ANalysis |                 |     |               |          |          |           |           |
anomalousdatapoints,whichisincreasinglycommoninpractice.Our
OfVAriance(ANOVA)(Jain,1991)togaininsightsintothestatistical analysis is supplemented by a comparison with one-class classifiers,
significanceoffactors–andtheirinteractions–onaresponsevariable. whichcanbeconvenientlyusedinthosesettingswhereonlyoneclass
In this study we use the F-measure as response variable because canbelearnedaccurately.
precisionandrecalloftheclassifiersarereasonablyclose. Forthesakeofclarity,Table7indicateshowthedatasetsdescribed
inSection5.3havebeenusedtoobtaintheresultspresentedthrough
ANOVAisdoneasfollows.Wesplitthevariantsintodisjointgroups
based on the levels of the factors that were used to obtain them12; the following subsections. For all the cases, the test set consists of
foreachgroupofvariantswecomputetheF-measureobtainedbythe normal/anomalousscorescomputedfromthelogsobtainedbymeans
ofdirectcollectionsfromClearwater,i.e.,D2∪D3.
| decision     | tree at classifying | the    | variants      | belonging |            | to a certain | group        |                                 |     |     |     |     |     |     |
| ------------ | ------------------- | ------ | ------------- | --------- | ---------- | ------------ | ------------ | ------------------------------- | --- | --- | --- | --- | --- | --- |
| with respect | to the normal       |        | logs. Results | are       | summarized |              | in Table 6.  |                                 |     |     |     |     |     |     |
|              |                     |        |               |           |            |              |              | 7.1. Relationshipsacrossthelogs |     |     |     |     |     |     |
| The total    | variability         | of the | F-measure     | across    | the        | groups       | of variants, |                                 |     |     |     |     |     |     |
i.e.,sumofsquarestotal(SST)inANOVA,is0.0107.Foreachfactorand
Ourproposaldevelopsaroundtheintuitionthatrelationshipsacross
interaction,Table6showsthesumofsquares(SS),i.e.,theportionof microservices’ logs can be leveraged for detection purposes. In this
SSTexplainedbythefactor/interaction.WeobservethatIMPACTisthe experimentweuseadecisiontreeandaK-foldcrossvalidationapproach
mostimportant:itexplains91.6%ofthevariabilityanditisstatistically tomodelthescoresfrombothnormalandanomalousevents,i.e.,D2∪
significant(i.e.,p-value<0.05). D3.InthiscaseD2∪D3issplitinto10disjointfoldsF(with1≤F≤10).
|           |               |     |          |             |     |        |         | Foreachfold𝑓,wetrainadecisiontreewith9folds(𝑓 |     |     |     |     | ≠F)andtestit |     |
| --------- | ------------- | --- | -------- | ----------- | --- | ------ | ------- | --------------------------------------------- | --- | --- | --- | --- | ------------ | --- |
| Practical | implications. |     | Based on | the results | of  | ANOVA, | the de- |                                               |     |     |     |     |              |     |
withtheheld-outfold(𝑓==F);thus,‘‘trainingset’’,isnotapplicable–
| tector is | sensitive to | small | percentages | of  | anomalous | lines. | In fact, |     |     |     |     |     |     |     |
| --------- | ------------ | ----- | ----------- | --- | --------- | ------ | -------- | --- | --- | --- | --- | --- | --- | --- |
asstatedinTable7–becausetraining/testareinherentlyintertwined.
havingmorethan1%anomalouslines–e.g.,5%,10%SNR–doesnot
InthisfirstexperimentweuseaK-foldapproachinordertoleverage
| necessarily | reflect into | higher | F-measure, | such | as shown | in  | Fig. 7(a). |     |     |     |     |     |     |     |
| ----------- | ------------ | ------ | ---------- | ---- | -------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
allthevectorsinD2∪D3:infact,weaimtocomputeanupperbound
| This means | that the | detector | does | not depend | on  | the verbosity | of  |     |     |     |     |     |     |     |
| ---------- | -------- | -------- | ---- | ---------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
fortherecallandprecisionmetricsthatwillserveasreferencetoassess
| anomalous       | events in | the logs,   | which | is strongly | desirable |      | in practice. |                              |     |     |         |     |     |     |
| --------------- | --------- | ----------- | ----- | ----------- | --------- | ---- | ------------ | ---------------------------- | --- | --- | ------- | --- | --- | --- |
|                 |           |             |       |             |           |      |              | theone-classandvariant-based |     |     | models. |     |     |     |
| More important, | the       | observation | that  | IMPACT      | explains  | most | of the       |                              |     |     |         |     |     |     |
Fig.8showstherelationshipsbymeansoftheobtaineddecisiontree
variability, indicates that the detector is able to capitalize on the (pleaserefertoTable2fortheacronymsoftheevents);boldcharacters
availability of multiple measurements from different microservices; highlight the path that catches the vast majority of normal vectors of
we also note that, differently from the SNR, F-measure improves as scores(line12).Regardinganomalousevents,wefoundoutthataround
IMPACT increases(Fig.7(b)).Thisisanotherimportantoutcome,given 82% vectors from the AUTH setting reflect into abnormal activity by
the distributed nature of microservice systems and related security ellis(line17 inFig.8);similarly,90%vectorsobtainedduringtheDoS
settingarecharacterizedbyabnormalactivityinhomesteadaccess(line
| implications. | Having        | diverse | points of | observation, |              | i.e., log | sources, is |                 |       |         |              |      |           |             |
| ------------- | ------------- | ------- | --------- | ------------ | ------------ | --------- | ----------- | --------------- | ----- | ------- | ------------ | ---- | --------- | ----------- |
|               |               |         |           |              |              |           |             | 18). The reader | might | further | inspect Fig. | 8 to | see other | interesting |
| beneficial    | for automated | anomaly | detection |              | and reflects |           | into higher |                 |       |         |              |      |           |             |
correlations.
F-measure.
Thesecorrelationsacrossthelogsarehardtobecaughtbyhuman
|     |     |     |     |     |     |     |     | experts, who | are typically | responsible |                 | for manually | crafting      | security |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ------------- | ----------- | --------------- | ------------ | ------------- | -------- |
|     |     |     |     |     |     |     |     | compromise   | indicators,   | e.g.,       | the correlation | rules        | of up-to-date | SIEM     |
12 We exclude from this analysis the variants obtained with SIZE = ×0 tools (Bhatt et al., 2014). This practice closely resembles traditional
becausetheSNRdoesnotapply,suchasexplainedinSection5.1. business intelligence, where humans must know what they wish to
8

M.Cinqueetal.
JournalofNetworkandComputerApplications208(2022)103515
Fig.8. Decisiontreemodelandrelationshipsamongthescoresofnormal(NORM)andanomalousevents.
|        |     |     | Fig.9. | WorstthreeROCcurvesfordecisiontree. |        |     |     |     |     |
| ------ | --- | --- | ------ | ----------------------------------- | ------ | --- | --- | --- | --- |
| Table8 |     |     |        |                                     | Table9 |     |     |     |     |
Metricsoftheclassifiertrainedwithreallogs. Metricsoftheone-classclassifiers.
Precision Recall F-measure ROCarea Accuracy Precision Recall F-measure Accuracy
| 0.948 | 0.942 | 0.944 | 0.965 | 94.2% | ApproachinHempstalketal.(2008) |     |     |     |     |
| ----- | ----- | ----- | ----- | ----- | ------------------------------ | --- | --- | --- | --- |
Recall/ROCareabyanomaly
|     |      |     |     |      | Randomtree   | 0.553 | 0.953 | 0.699 | 54.8% |
| --- | ---- | --- | --- | ---- | ------------ | ----- | ----- | ----- | ----- |
| DoS | KILL | DEL | REG | AUTH | Decisiontree | 0.552 | 1.000 | 0.711 | 55.2% |
0.90/0.98 0.90/0.95 0.93/0.94 0.94/0.95 0.82/0.99 Bayesiannet. 0.897 0.890 0.893 88.3%
|     |     |     |     |     | Multilayerperc. | 0.724 | 0.929 | 0.814 | 76.5% |
| --- | --- | --- | --- | --- | --------------- | ----- | ----- | ----- | ----- |
|     |     |     |     |     | AdaBoost.M1     | 0.552 | 0.949 | 0.696 | 64.9% |
ApproachinSchölkopfetal.(2000)
look for, beforehand. Differently, our work puts forth the concept of One-classSVM 0.750 0.520 0.614 63.9%
datadiscoverytocomplementthetaskoffindingeffectivecompromise
detectionrules.
Wenotethatbothnormalandanomalouseventsarecharacterized
byaprecisesignatureintherelationshipsofthescores.Table8provides (2008)and(ii)theone-classSupportVectorMachine(SVM)(Schölkopf
overallprecisionandrecallofthedecisiontree,bothhigherthan0.94. et al., 2000) implemented in Chang and Lin (2011). Both approaches
Moreover, the bottom row of the table also shows the breakdown of arereferenceworkinone-classclassificationstudiesastheyhavebeen
the recall and ROC area by anomaly, which are in the range 0.82 largelyusedforcomparisonpurposes(Anderkaetal.,2012;Barbhuiya
| (AUTH) - | 0.94 (REG) and | 0.94 (DEL) - | 0.99 (AUTH), | respectively— | etal.,2018). |     |     |     |     |
| -------- | -------------- | ------------ | ------------ | ------------- | ------------ | --- | --- | --- | --- |
thusreasonablyhigh.ThegoodresultsarealsohighlightedbytheROC In this study the scores computed from normal logs are the target
curves depicted in Fig. 9, which are reasonably near to the optimal class: only vectors of scores representing normal events are used to
curve(assuggestedbytheROCareavaluesinTable8),albeittheyare traintheone-classclassifiers.Anomaliesareexpectedtobeclassifiedas
theworstthreeobtainedones.Thesefiguresareusedasareferencein outlier.WeusethedatasetD1totraintheclassifierswithrealnormal
assessingtheone-classandvariant-based models. scores,andtestitagainstD2∪D3,asshowninTable7.Table9shows
|     |     |     |     |     | the obtained results. | The approach | in Hempstalk | et al. (2008), | after |
| --- | --- | --- | --- | --- | --------------------- | ------------ | ------------ | -------------- | ----- |
7.2. Detectionthroughone-classclassification having transformed the problem into a binary classification, can be
|     |     |     |     |     | used in conjunction | with any | existing classifier: | Table 9 presents | the |
| --- | --- | --- | --- | --- | ------------------- | -------- | -------------------- | ---------------- | --- |
One-classclassifiersrepresentaviablesolutiontocopewiththelack results obtained with the most promising we found after sensitivity
of real anomalies. One-class approaches leverage the assumption that analyses. Results indicate that the Bayesian network reaches the max-
onlyoneclass–namedtarget class–iswellcharacterizedinatraining imumoverallmetrics,withanF-measureof0.893andanaccuracyof
set. Any arbitrary data point that does not resemble the only class 88.3%.Itcanbenotedthat,inspiteofthequitehighrecallforalmost
learnedduringtrainingisdeemedasoutlier.Weexploretwoone-class all the classifiers, only the Bayesian one obtains acceptable precision
classificationapproaches:(i)theapproachproposedinHempstalketal. andrecall,whicharehoweverlowerifcomparedtothecorresponding
9

M.Cinqueetal.
JournalofNetworkandComputerApplications208(2022)103515
|     |     |     |     | Fig.10. | ScoresoffourClearwater’slogsanddetector’soutputintwoanomalousevents. |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | ------- | -------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Table10 biasing the results towards a specific anomalous setting and to inves-
MetricsofHempstalketal.(2008)withtheBayesiannetwork. tigate a more general research direction, which does not rely on the
Precision Recall F-measure Accuracy availability of labeled data for generating the variants. Interestingly,
|     | 0.897 |     | 0.890 |     | 0.893 |     | 88.3% |             |        |         |               |       |      |             |       |
| --- | ----- | --- | ----- | --- | ----- | --- | ----- | ----------- | ------ | ------- | ------------- | ----- | ---- | ----------- | ----- |
|     |       |     |       |     |       |     |       | the loss is | caused | by only | one anomalous | event | type | (i.e., REG, | as it |
Recallbyanomaly canbenotedbycomparingthebottomrowsofTables8and11),which
DoS KILL DEL REG AUTH means that – based on the findings of our study – variants obtained
0.87 1.00 1.00 0.62 1.00 with no knowledge of real anomalous events are potentially useful
|     |     |     |     |     |     |     |     | to support | the detection. | More | importantly, |     | the variant-based |     | model |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | -------------- | ---- | ------------ | --- | ----------------- | --- | ----- |
Table11 improvesoverone-classclassification,whoseresultswereinTable10.
Metricsoftheclassifiertrainedwithlogvariants. Wecloselylookintothemodelsinordertointerprettheimprove-
Precision Recall F-measure ROCarea Accuracy mentobtainedwithvariantsovertheone-classapproach.Fig.11shows
0.913 0.901 0.907 0.917 90.7% themodelobtainedbymeansofHempstalketal.(2008)inconjunction
Recallbyanomaly withadecisiontree(wediscussthedecisiontreeinlieuof theBayesian
DoS KILL DEL REG AUTH networkforthesakeofvisualcomparison);similarly,Fig.12showsthe
0.97 0.90 0.93 0.75 0.91 pathofthevariant-basedmodelcatchingthemajorityofnormalvectors
ofscores(line18).Fig.11indicatesthatthemodelobtainedwiththe
|     |     |     |     |     |     |     |     | one-class approach |     | leverages | only | 2 out of | 13 log sources, |     | i.e., logs |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------ | --- | --------- | ---- | -------- | --------------- | --- | ---------- |
referencemetricsinTable8.Thisisexplainedbythebreakdownofthe ofcassandraandralfaccess.PleasenotethatnegativescoresinFig.11
recallovertheanomaliescollectedbydirectobservationsofClearwater result from the internal mathematical transformations of Hempstalk
≥0.
inTable10.Theone-classclassifierachievesarecallof1.00forKILL, et al. (2008), since – by construction – our log.entropy is always
DELandAUTH;however,itdropssharplyto0.87and0.62forDoSand Ontheotherhand,themodelobtainedwithlogvariantscapitalizeson
manymorelogsources,asshowninFig.12,whichprovidesfiner-grain
| REG, respectively, |     | which | means | that one-class | classification |     | is rather |           |              |        |      |           |         |                |     |
| ------------------ | --- | ----- | ----- | -------------- | -------------- | --- | --------- | --------- | ------------ | ------ | ---- | --------- | ------- | -------------- | --- |
|                    |     |       |       |                |                |     |           | leaves to | discriminate | normal | from | anomalous | events. | Interestingly, |     |
ineffectiveinsomeanomalousscenarios.
mostofthelogsusedforthedecisionarethesameasinFig.8,which
wereobtainedfromreallogs.
7.3. Detectionbymeansofthelogvariants
|            |            |           |            |            |      |              |            | 8. ApplicationtotheATCcasestudy |           |              |             |              |      |           |         |
| ---------- | ---------- | --------- | ---------- | ---------- | ---- | ------------ | ---------- | ------------------------------- | --------- | ------------ | ----------- | ------------ | ---- | --------- | ------- |
| We aim     | to address | the       | following  | question:  | can  | the variants | be used    |                                 |           |              |             |              |      |           |         |
| to train a | model for  | detecting | real       | anomalies? | This | is strongly  | relevant   |                                 |           |              |             |              |      |           |         |
|            |            |           |            |            |      |              |            | In order                        | to assess | the proposal |             | with another | case | study, we | apply   |
| because,   | as stated  | above,    | a training | database   | of   | real logs    | will never |                                 |           |              |             |              |      |           |         |
|            |            |           |            |            |      |              |            | it to a real-world              |           | critical     | information | system       | from | the Air   | Traffic |
coveralltheanomaliesthatcanoccurinproduction;onthecontrary,
Control(ATC)domain.Thesysteminstallationhasbeenmadeavailable
| variants | emulate | a wide | spectrum | of settings | by  | experimental | design, |                  |     |            |         |               |     |             |     |
| -------- | ------- | ------ | -------- | ----------- | --- | ------------ | ------- | ---------------- | --- | ---------- | ------- | ------------- | --- | ----------- | --- |
|          |         |        |          |             |     |              |         | by a top-leading |     | industrial | company | in electronic | and | information |     |
although they are not directly related to anomalies. To explore this technologiesfordefenseandaerospace,inthecontextofanacademia-
proposition we train a decision tree with D1 ∪ D4 and test it on D2 industryproject.Thesystemencompassesanumberofnodesrunning
∪D3,asshowninTable7,i.e.,weattempttoclassifyscorescomputed distributed applications, which cooperate to implement ATC-related
fromrealnormal/anomalouslogswithamodellearnedfromvariants. capabilities,suchasaircrafttrajectorymonitoringandcollisionpreven-
ResultsareshowninTable11.Bothrecallandprecisionarehigher
tion/detection.Thecooperationisenabledbymeansofmessagepass-
| than 0.90, | which | is reasonably |     | satisfactory. | In  | Fig. 10 we | plot the |     |     |     |     |     |     |     |     |
| ---------- | ----- | ------------- | --- | ------------- | --- | ---------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
ingbetweenapplications,accordingtothepublish–subscribeparadigm,
outputofthedetectorduringtheprogressionoftwoanomalousevents,
|     |     |     |     |     |     |     |     | widely adopted | in  | microservice |     | architectures. | More | important, | the |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ------------ | --- | -------------- | ---- | ---------- | --- |
i.e., registration and authentication, respectively. The detector is super- systemencompassesmanyheterogeneouslogsources,withapplications
imposedasadottedlinetothescoresoffourmicroservices’logs,where generating multiple logs per node, similarly to the Clearwater case.
thetransitionlow-highdenotesthattheanomalouseventisdetected;in Overall, 16 log files sources are available, encompassing legacy logs
bothcasestheanomalouseventstartsaroundthechunkset id20.For implemented by means of a variety of custom formats; the collected
example,intheregistrationsettingthedetectortakesfewcyclesbefore logfilesarelistedinTable12byoriginatingnode.
itstabilizesathigh. AsdoneforClearwater,wecollectlogsencompassingbothnormal
WithrespecttoTable8–i.e.,trainingdonewithreallogs–wenote and anomalous events. Normal logs are collected by exercising the
alossinrecallandprecision,whichdroproughlyby0.05.Suchadrop
|     |     |     |     |     |     |     |     | system with | test suites, | which | are | used by | the industry | provider | to  |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ------------ | ----- | --- | ------- | ------------ | -------- | --- |
isexpectedbecause,differentlyfromrecentcontributionsinthisarea, emulatethesystemusagebyrealATCoperators.Theworkloadcontains
such as Cao et al. (2016) and Xie et al. (2018), our variants are not several operations, ranging from Flight Data Plan creation/update,
generated by perturbing the anomalous events. This is done to avoid which contains the data of a given flight (such as expected route,
10

M.Cinqueetal.
JournalofNetworkandComputerApplications208(2022)103515
|     |     |     | Fig.11. | ModelobtainedwithHempstalketal.(2008)andthedecisiontree. |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | ------- | -------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Fig.12. Extractofthedecisiontreemodelobtainedfromvariantsandrelationshipsamongthescoresofnormal(NORM)andanomalousevents(ANOM).
| Table12 |     |     |     |     |     |     | Table13 |     |     |     |     |     |     |     |
| ------- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
LogfilesbyATCsystemnode. MetricsofthedecisiontreetrainedwithreallogsfromtheATCcasestudy.
Node Nameofthelogfile Precision Recall F-measure ROCarea Accuracy
|     |     |               |     |     |     |     | 0.959 | 0.959 |     | 0.959 |     | 0.980 | 95.9% |     |
| --- | --- | ------------- | --- | --- | --- | --- | ----- | ----- | --- | ----- | --- | ----- | ----- | --- |
| D02 |     | D02PAN,D02msg |     |     |     |     |       |       |     |       |     |       |       |     |
| DB1 |     | DB1PAN,DB1msg |     |     |     |     |       |       |     |       |     |       |       |     |
Recall/ROCareabyanomaly
| FP1 |     | FP1PAN,FP1NTN,FP1LNR,FP1AFS,FP1msg |     |     |     |     |              |            |            |           |             |               |            |     |
| --- | --- | ---------------------------------- | --- | --- | --- | --- | ------------ | ---------- | ---------- | --------- | ----------- | ------------- | ---------- | --- |
|     |     |                                    |     |     |     |     | DoS          | KILL       |            | DEL       |             | RER           | AUTH       |     |
| MN1 |     | MN1PAN,MN1MNA,MN1msg               |     |     |     |     |              |            |            |           |             |               |            |     |
|     |     |                                    |     |     |     |     | 0.90/0.96    | 0.99/0.99  |            | 0.97/0.99 |             | 0.96/0.98     | 1.00/1.00  |     |
| MS1 |     | MS1PAN,MS1msg                      |     |     |     |     |              |            |            |           |             |               |            |     |
| SFN |     | SFNPAN,SFNmsg                      |     |     |     |     |              |            |            |           |             |               |            |     |
|     |     |                                    |     |     |     |     | set to (M-1) | = 120.     | We collect | total     | 3 datasets, | i.e.,         | (i) D1-ATC | and |
|     |     |                                    |     |     |     |     | (ii) D2-ATC, | containing | NORMAL     | scores,   | and         | (iii) D3-ATC, | containing |     |
trajectory),toFlightre-routing,whichallowstomodifythetrajectory
ANOMALOUSscores.AsdonefortheClearwatercasestudy,wepresent
ofaflight.Normallogsarealsousedtobuildthereplacementsbase13
theresultsconcerningthedetectionofanomalouseventswiththeATC
| Anomalous | events are collected |     | by emulating | different | settings | that |     |     |     |     |     |     |     |     |
| --------- | -------------------- | --- | ------------ | --------- | -------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
systeminvolvingbothmulti-classandone-classclassifiers.
| resemble | operations occurring | under | different | attack | phases, | as done |     |     |     |     |     |     |     |     |
| -------- | -------------------- | ----- | --------- | ------ | ------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
tree14
forClearwater.Weemulate5settings:(i)DenialofService(DoS),where Multi-class classification. We use a decision and a K-fold
theattackerstartsmisusingthesystemcreatinganewflighteverysec- crossvalidationapproach(with𝐾=10)tomodelthescoresfromboth
ondtoslowdownthesystemresponse:(ii)Killservice(KILL),wherethe normal and anomalous events contained in the D2-ATC and D3-ATC,
attackerattemptstoblockthesystemoperationbykillingthedatabase respectively.AsseenfortheClearwatercasestudy,wenotethatboth
|     |     |     |     |     |     |     | normal and | anomalous | events | are characterized |     | by a | precise signature |     |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --------- | ------ | ----------------- | --- | ---- | ----------------- | --- |
service;(iii)LogDeletion(DEL),wheresomeapplicationlogsaredeleted
|                |          |        |               |         |             |     | in the relationships |     | of the | scores. Fig. | 13 shows | the relationships |     | by  |
| -------------- | -------- | ------ | ------------- | ------- | ----------- | --- | -------------------- | --- | ------ | ------------ | -------- | ----------------- | --- | --- |
| by an attacker | with the | aim to | cover his/her | traces, | (iv) Flight | re- |                      |     |        |              |          |                   |     |     |
meansoftheobtaineddecisiontree.Itcanbenotedthataround93%
| routing (RER), | where the | attacker | modifies | the data | in the system | by  |              |     |             |         |      |          |          |        |
| -------------- | --------- | -------- | -------- | -------- | ------------- | --- | ------------ | --- | ----------- | ------- | ---- | -------- | -------- | ------ |
|                |           |          |          |          |               |     | vectors from | the | DEL setting | reflect | into | abnormal | activity | by the |
re-routingaflighteveryfivesecondstowardsthesamedestination;(v)
Brute-force authentication (AUTH), where an attacker attempts to gain D02PAN log (line 17), which also involves other log files, such as
unauthorizedaccesstothesystemthroughbrute-forceloginattemptsat D02msg,FP1PAN,MN1MNA,SFNPAN,FP1AFS,asindicatedbythebold
theD02node,i.e.,thefront-endoftheATCsystem.Wereproducethese characters.Similarly,wefoundoutthataround99%vectorsobtained
scenariosduringtheexecutionofthenormalworkloadofthesystem, during the KILL setting are characterized by abnormal activity in
sothatanomalouseventsareoverlappedwithregularoperationsasit FP1PAN log files (line 2). It is important to note that in this case
wouldoccurinproduction. the abnormal activity is represented by the absence of events in the
|                    |          |              |           |             |            |         | log, which | is coherent       | with | the emulated |        | KILL scenario. | Table | 13     |
| ------------------ | -------- | ------------ | --------- | ----------- | ---------- | ------- | ---------- | ----------------- | ---- | ------------ | ------ | -------------- | ----- | ------ |
| The collected      | logs are | periodically | sampled   | to generate | the        | chunk   |            |                   |      |              |        |                |       |        |
|                    |          |              |           |             |            |         | provides   | overall precision |      | and recall   | of the | decision tree, | both  | higher |
| sets; the sampling | period   | is set to    | 𝑇 = 10 s, | while       | the sample | size is |            |                   |      |              |        |                |       |        |
than0.95,aswellastheoverallROCareavalue,i.e.,0.980.Thehigh
| 13 Patterns | included in the | replacements | base | have | been made | publicly |     |     |     |     |     |     |     |     |
| ----------- | --------------- | ------------ | ---- | ---- | --------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
available-www.dessert.unina.it/JNCA2022ATCLogs-Regex.zip. 14 Weusethesameclassifierofthefirstcasestudyforcomparisonpurposes.
11

M.Cinqueetal.
JournalofNetworkandComputerApplications208(2022)103515
Extractofthedecisiontreemodelandrelationshipsamongthescoresofnormal(NORM)andanomalouseventsfromtheATCsystem.
Fig.13.
|     |     |     | Fig.14. | WorstthreeROCcurvesfordecisiontree—ATC. |     |     |     |     |
| --- | --- | --- | ------- | --------------------------------------- | --- | --- | --- | --- |
Table14 metricsshowninTable13.Thisisexplainedbythebreakdownofthe
| Metricsofone-classSVM—ATC. |           |        |           |          | recalloveranomalyinTable14.       |     |     |     |
| -------------------------- | --------- | ------ | --------- | -------- | --------------------------------- | --- | --- | --- |
|                            | Precision | Recall | F-measure | Accuracy |                                   |     |     |     |
|                            | 0.925     | 0.408  | 0.566     | 85.8%    | 9. Discussionandthreatstovalidity |     |     |     |
Recallbyanomaly
| DoS | KILL | DEL | RER | AUTH |     |     |     |     |
| --- | ---- | --- | --- | ---- | --- | --- | --- | --- |
Thedetectionfiguresthatweobtainbyminingthenumericrepre-
| 0.99 | 0.93 | 0.90 | 1.00 | 1.00 |               |                       |                    |                            |
| ---- | ---- | ---- | ---- | ---- | ------------- | --------------------- | ------------------ | -------------------------- |
|      |      |      |      |      | sentations    | produced by Micro2vec | with commonly-used | machine and                |
|      |      |      |      |      | deep learning | algorithms            | are up to 0.97     | and 0.96 recall, precision |
andF-measure,forthemicroservicesandATCcasestudy,respectively.
ROC area value is explained by the ROC curves depicted in Fig. 14, The performance achieved is inline with existing work in the area.
whicharereasonablyneartotheoptimalcurvealbeittheyaretheworst For example, the Authors in Meng et al. (2019) propose a method,
threeobtainedones,assuggestedbytheROCareavaluesinTable13. LogAnomaly, based on template2Vec, i.e., a template representation
Interestingly,achievedresultsareinlinewiththeonesobtainedinthe methodtoextractsemanticandsyntaxinformationfromlogtemplates
inspiredbywordembedding.TheF-measureofourtechniqueissimilar
| Clearwater | case. Let us add | that also for | this case study | we evaluate |               |            |                         |                    |
| ---------- | ---------------- | ------------- | --------------- | ----------- | ------------- | ---------- | ----------------------- | ------------------ |
|            |                  |               |                 |             | to LogAnomaly | applied to | the BG/L log benchmark, | i.e., 0.96. As for |
theAdaBoost.M1performance,whichperformssimilarlytothedecision
tree,confirmingthatalsotheATCdatasetisnotaffectedbytheclass otherapproachesthatimplysequentialembedding,theworkGuoetal.
imbalanceissue. (2021) applies BERT, i.e., the Bidirectional Encoder Representations
One-classclassification.Inordertoapplyone-classclassification fromTransformersdevelopedbyGoogle,andachieves0.92recalland
approaches, the scores computed from normal logs are considered as 0.89 precision with the BG/L log: both the figures are lower than
thetargetclassandtheyareusedfortraining,asdoneintheClearwater Micro2vec. As for other related approaches using BERT, it is worth
casestudy.WeusethedatasetD1-ATCtotraineachone-classclassifier mentioning (Hirakawa et al., 2020), which achieves 0.89 F-measure
usedforClearwaterwithrealnormalscores,andtestitagainstD2-ATC with BG/L, again lower than Micro2vec. SwissLog (Li et al., 2020),
∪D3-ATC.Resultsindicatethat–withrespecttoourdata–theone-class whichisappliedinconjunctionwithLongshort-termmemory(LSTM),
SVMclassifierreachesthemaximumoverallmetrics,withanF-measure Bidirectional LSTM (BiLSTM) and Attention-based BiLSTM, achieves
of 0.566 and an accuracy of 85.8%. Moreover, differently from the 0.95, 0.96 and 0.99 F-measure in BG/L, respectively: the F-measure
otherclassifiers,theone-classSVMclassifieristheonlyoneexhibiting of Micro2vec is in line with the first two SwissLog variants, although
an acceptable precision. Table 14 summarizes the metrics of the one- lowerthanthelatter.ItshouldbenotedthatSwissLogisconceivedfora
class SVM classifier. Overall, it achieves precision and recall of 0.925 specificfaultmodeloflogsequenceorderchangesandlogtimeinterval
and0.408,whicharelowerifcomparedtothecorrespondingreference changes:mostnotably,Micro2vecisnotconstrainedbyspecifictypes
12

M.Cinqueetal.
JournalofNetworkandComputerApplications208(2022)103515
offaults.Finally,therecallandprecisionofMicro2vecareintherange normal logs can support detecting real anomalies, and they improve
ofAutoLog(Catilloetal.,2022),whichachievesavalueoftherecall overone-classclassifiers.
between0.96and0.99,andprecisionwithin0.93and0.98appliedto In the future we aim to extend our experiments to production
thelogsoffoursystems. systemsandtodifferentapplicationdomains.Infact,theproposalisnot
| As for | any measurement |     | study, | there | may | be concerns | regarding |     |              |            |        |          |            |              |        |
| ------ | --------------- | --- | ------ | ----- | --- | ----------- | --------- | --- | ------------ | ---------- | ------ | -------- | ---------- | ------------ | ------ |
|        |                 |     |        |       |     |             |           |     | tailored for | a specific | mining | approach | or system. | In addition, | future |
validity and generalizability of the proposal and results. We briefly work will also be devoted to inspect other methods for log variants.
discussthem,basedontheaspectsinWohlinetal.(2000). Further,wewillinvestigatetheactionsthatmalicioususersmighttake
Construct validity. Our work builds on the intuition that rela- toevadedetectionaswellastheuseofretrainingmechanismstoupdate
tionships across microservices’ logs can be leveraged for detection thenormalmodelwhenthesystemchanges.Finally,theimpactofboth
purposes.Thisispursuedbyinstantiatingourexperimentsinthecon- logqualityandparsingontheproposalwillbealsoassessed,sincethey
text of two systems, i.e., Clearwater IMS, which well represents an canpotentiallyaffecttheeffectivenessofthescoringtaskandthenof
importantcategoryofmicroservicesystems,andtheATCcriticalinfor- theanomalydetection.
| mation system, |     | which leverages |     | microservices-related |     |     | communication |     |     |     |     |     |     |     |     |
| -------------- | --- | --------------- | --- | --------------------- | --- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
technologies. We devoted special attention to exercise both systems Declarationofcompetinginterest
accordingtorepresentativeoperations.Bothsystemsare:(i)deployed
| according | to the | settings | provided | by  | the developers, |     | (ii) | fed with |             |         |      |           |     |                 |        |
| --------- | ------ | -------- | -------- | --- | --------------- | --- | ---- | -------- | ----------- | ------- | ---- | --------- | --- | --------------- | ------ |
|           |        |          |          |     |                 |     |      |          | The authors | declare | that | they have | no  | known competing | finan- |
realistic input data, and (iii) exercised with the test suite used by cial interests or personal relationships that could have appeared to
developers to emulate their nominal usage. Regarding the anomalies, influencetheworkreportedinthispaper.
| we rely | on events | that | resemble | the | security | attack | phases | in Ruiu |     |     |     |     |     |     |     |
| ------- | --------- | ---- | -------- | --- | -------- | ------ | ------ | ------- | --- | --- | --- | --- | --- | --- | --- |
(1999)andSharmaetal.(2011).Theconsideredeventsarenotmeant Dataavailability
tobeexhaustiveforallanomaliesthatmayoccurinpractice.However,
althoughtheycannotprovideacomprehensivepictureontheaccuracy Data from one dataset is available via the link provided in the
| that can       | be expected | with          | our     | approach, | the        | considered   | anomalies |         | manuscript. |     |     |     |     |     |     |
| -------------- | ----------- | ------------- | ------- | --------- | ---------- | ------------ | --------- | ------- | ----------- | --- | --- | --- | --- | --- | --- |
| allow pointing | out         | the potential |         | of the    | approach.  | Finally,     | we        | rely on |             |     |     |     |     |     |     |
| well-funded    | log         | analysis      | methods | for       | extracting | quantitative |           | metrics |             |     |     |     |     |     |     |
Acknowledgments
fromlogs;findingshavebeeninferredwithanapproachencompassing
designofexperimentsandassessmentofthemeasurementerror.
ThisworkhasbeenpartiallysupportedfromtheEuropeanUnion’s
| Internal | and | conclusion | validity. |     | We use | a mixture | of  | datasets |         |               |     |            |           |       |           |
| -------- | --- | ---------- | --------- | --- | ------ | --------- | --- | -------- | ------- | ------------- | --- | ---------- | --------- | ----- | --------- |
|          |     |            |           |     |        |           |     |          | Horizon | 2020 research | and | innovation | programme | under | the Marie |
consisting of real logs and variants to provide evidence of the actual Skłodowska-CuriegrantagreementNo871342.
| relationships                                                   | across | the       | metrics.    | Experiments     |          | include            | multi-class | and   |            |                           |     |            |     |                 |             |
| --------------------------------------------------------------- | ------ | --------- | ----------- | --------------- | -------- | ------------------ | ----------- | ----- | ---------- | ------------------------- | --- | ---------- | --- | --------------- | ----------- |
| one-classclassification,andclassificationdoneonthetopoflogvari- |        |           |             |                 |          |                    |             |       | References |                           |     |            |     |                 |             |
| ants. We                                                        | assess | different | classifiers | and             | generate | the                | variants    | under |            |                           |     |            |     |                 |             |
| differentconfigurationsofthekey                                 |        |           |             | factors.Metrics |          | ofprecision,recall |             |       |            |                           |     |            |     |                 |             |
|                                                                 |        |           |             |                 |          |                    |             |       | Ahuja, N., | Singal, G., Mukhopadhyay, |     | D., Kumar, | N., | 2021. Automated | DDOS attack |
andF-measurearecomputedwithbothreallogsandvariantswiththe detectioninsoftwaredefinednetworking.J.Netw.Comput.Appl.187,103108.
aim of avoiding any favorable setting to our proposal. Overall, this Anderka, M., Stein, B., Lipka, N., 2012. Predicting quality flaws in user-generated
mitigates internal validity threats and provides a reasonable level of content: The case of wikipedia. In: Proc. of the 35th Intl. ACM SIGIR Conf. on
confidenceontheconclusions. Research and Development in Information Retrieval. ACM, New York, NY, USA,
| External | validity. | Results | observed |     | on two | case | studies | are not | pp.981–990. |     |     |     |     |     |     |
| -------- | --------- | ------- | -------- | --- | ------ | ---- | ------- | ------- | ----------- | --- | --- | --- | --- | --- | --- |
Bakar,N.,Belaton,B.,Samsudin,A.,2005.Falsepositivesreductionviaintrusionalert
| statistically | generalizable. |     | However, | the | reported | findings, | which | are |     |     |     |     |     |     |     |
| ------------- | -------------- | --- | -------- | --- | -------- | --------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
qualityframework.In:200513thIEEEIntl.ConferenceonNetworksJointlyHeld
strongly supported by data, are still useful to get an overall un- withthe2005IEEE7thMalaysiaIntl.ConferenceonCommunications.p.6.
derstanding on the potential of the proposal. Our proposal should Barbhuiya, S., Papazachos, Z., Kilpatrick, P., Nikolopoulos, D.S., 2018. RADS: Real-
be easily applicable to other similar systems. We require no mi- time anomaly detection system for cloud data centres. CoRR, abs/1811.04481
arXiv:1811.04481.
| croservices/applications |            |     | modifications. |          | Practitioners | are   | not        | expected |                  |          |           |         |            |             |              |
| ------------------------ | ---------- | --- | -------------- | -------- | ------------- | ----- | ---------- | -------- | ---------------- | -------- | --------- | ------- | ---------- | ----------- | ------------ |
|                          |            |     |                |          |               |       |            |          | Bass, L., Weber, | I., Zhu, | L., 2015. | DevOps: | A Software | Architect’s | Perspective. |
| to spend                 | any effort | in  | using our      | proposal | since         | it is | inherently | non      |                  |          |           |         |            |             |              |
Addison-WesleyProfessional.
| intrusive; | moreover, | we  | do not | embed | knowledge | of  | the application. |     |            |                      |     |           |         |                  |             |
| ---------- | --------- | --- | ------ | ----- | --------- | --- | ---------------- | --- | ---------- | -------------------- | --- | --------- | ------- | ---------------- | ----------- |
|            |           |     |        |       |           |     |                  |     | Behal, S., | Kumar, K., Sachdeva, |     | M., 2018. | D-FACE: | An anomaly based | distributed |
Thedetailsprovidedshouldreasonablysupportthereplicationofour
approachforearlydetectionofDDoSattacksandflashevents.J.Netw.Comput.
study by other researchers. Noteworthy, we made a comprehensive Appl.111,49–63.
sampleoflogs/scorespubliclyavailableforresearchpurposes. Benjamin, H.S., et al., 2010. Dapper, a Large-Scale Distributed Systems Tracing
Infrastructure.TechnicalReport,Google,Inc..
10. Conclusion Bertero,C.,Roy,M.,Sauvanaud,C.,Trédan,G.,2017.ExperienceReport:Logmining
usingnaturallanguageprocessingandapplicationtoanomalydetection.In:IEEE
28thIntl.SymposiumonSoftwareReliabilityEngineering.pp.351–360.
Thispaperpresentedourstudyonmininglogsforanomalydetec- Bhatt, S., Manadhata, P.K., Zomlot, L., 2014. The operational role of security
tion in the context of systems leveraging microservices-related tech- informationandeventmanagementsystems.IEEESecur.Priv.12(5),35–41.
nologies. We propose Micro2vec, a novel approach to mine numeric Brandón, Á., et al., 2020. Graph-based root cause analysis for service-oriented and
representations of computer logs, which allow inferring ‘‘actionable’’ microservicearchitectures.J.Syst.Softw.159,110432.
Campos,J.R.,Vieira,M.,Costa,E.,2018.Exploratorystudyofmachinelearningtech-
| relationships | for | anomaly | detection. | The | approach | embeds |     | no appli- |     |     |     |     |     |     |     |
| ------------- | --- | ------- | ---------- | --- | -------- | ------ | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
niquesforsupportingfailureprediction.In:14thEuropeanDependableComputing
| cation knowledge, |     | makes | no assumptions |     | on  | the format/semantics |     | of  |     |     |     |     |     |     |     |
| ----------------- | --- | ----- | -------------- | --- | --- | -------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Conference.pp.9–16.
| underlying | logs, | and requires | no  | catalogues |     | of anomalies | symptoms. |     |     |     |     |     |     |     |     |
| ---------- | ----- | ------------ | --- | ---------- | --- | ------------ | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
Cao,P.,Badger,E.C.,Kalbarczyk,Z.T.,Iyer,R.K.,2016.Aframeworkforgeneration,
| We conduct | our | experiments | with | a Clearwater |     | IMS | installation | and |     |     |     |     |     |     |     |
| ---------- | --- | ----------- | ---- | ------------ | --- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
replay,andanalysisofreal-worldattackvariants.In:Proc.oftheSymposiumand
withareal-worldATCcriticalinformationsystem. BootcampontheScienceofSecurity.ACM,NY,USA,pp.28–37.
Webelievethattheobtainedfindingsshouldbeextremelyusefulto Cardenas, A.A., et al., 2013. Big Data Analytics for Security Intelligence. Technical
practitioners and to drive future research directions. Results indicate Report,CloudSecurityAlliance,URL: https://downloads.cloudsecurityalliance.org/
initiatives/bdwg/Big_Data_Analytics_for_Security_Intelligence.pdf.
thatanalyzingmetricsinferredbydifferentlogsfacilitatesthedetection
|     |     |     |     |     |     |     |     |     | Catillo, M., | Pecchia, A., | Villano, | U., 2022. | AutoLog: | Anomaly detection | by deep |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ------------ | -------- | --------- | -------- | ----------------- | ------- |
ofanomalies,whicharecharacterizedbysignatureinvolvingmultiple autoencodingofsystemlogs.ExpertSyst.Appl.191,116263.
logs;italsoallowsinferringexplicabledetectionrulesthatarehardto Chang, C.-C., Lin, C.-J., 2011. LIBSVM: A library for support vector machines. ACM
be caught by human experts. In addition, log variants obtained from Trans.Intell.Syst.Technol.(TIST)2,27:1–27:27.
13

M.Cinqueetal.
JournalofNetworkandComputerApplications208(2022)103515
Cinque, M., Cotroneo, D., Della Corte, R., Pecchia, A., 2016. Characterizing direct Lim, C., Singh, N., Yajnik, S., 2008. A log mining approach to failure analysis of
monitoringtechniquesinsoftwaresystems.IEEETrans.Reliab.65(4),1665–1681. enterprise telephony systems. In: Proc. Intl. Conf. on Dependable Systems and
| Cinque, M., | Della | Corte, R., Pecchia, | A., | 2017. Entropy-based |     | security | analytics: | Networks. |     |     |     |     |     |     |     |
| ----------- | ----- | ------------------- | --- | ------------------- | --- | -------- | ---------- | --------- | --- | --- | --- | --- | --- | --- | --- |
Measurementsfromacriticalinformationsystem.In:47thAnnualIEEE/IFIPIntl. Liu,F.,etal.,2019.Log2vec:Aheterogeneousgraphembeddingbasedapproachfor
Conf.onDependableSystemsandNetworks.pp.379–390. detectingcyberthreatswithinenterprise.In:Proc.oftheACMSIGSACConference
onComputerandCommunicationsSecurity.AssociationforComputingMachinery,
Cinque,M.,DellaCorte,R.,Pecchia,A.,2020a.Contextualfilteringandprioritizationof
| computerapplicationlogsforsecuritysituationalawareness.FutureGener.Comput. |     |     |     |     |     |     |     | pp.1777–1794. |     |     |     |     |     |     |     |
| -------------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- |
Syst.111,668–680. Luo, Z., Hou, T., Nguyen, T.T., Zeng, H., Lu, Z., 2020. Log analytics in HPC:
Cinque, M., Della Corte, R., Pecchia, A., 2020b. An empirical analysis of error A data-driven reinforcement learning framework. In: IEEE Conf. on Computer
propagationincriticalsoftwaresystems.Empir.Softw.Eng.25(4),2450–2484. CommunicationsWorkshops.pp.550–555.
Makhoul,J.,Kubala,F.,Schwartz,R.,Weischedel,R.,1999.Performancemeasuresfor
| Cinque, M., | Della Corte, | R., Pecchia, | A., 2022. | Microservices |     | monitoring | with event |             |             |        |             |          |           |                |     |
| ----------- | ------------ | ------------ | --------- | ------------- | --- | ---------- | ---------- | ----------- | ----------- | ------ | ----------- | -------- | --------- | -------------- | --- |
|             |              |              |           |               |     |            |            | information | extraction. | In: In | Proceedings | of DARPA | Broadcast | News Workshop. |     |
logsandblackboxexecutiontracing.IEEETrans.Serv.Comput.15(1),294–307.
| 2022.Clearwater.https://www.metaswitch.com/products/clearwater-core-ims. |     |     |     |     |     |     |     | pp.249–252. |     |     |     |     |     |     |     |
| ------------------------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
2022.Clearwatertest.https://github.com/Metaswitch/clearwater-live-test/. Meng, W., Liu, Y., Zhu, Y., Zhang, S., Pei, D., Liu, Y., Chen, Y., Zhang, R., Tao, S.,
Cotroneo, D., Natella, R., Rosiello, S., 2017. NFV-Throttle: An overload control Sun, P., Zhou, R., 2019. LogAnomaly: Unsupervised detection of sequential and
|           |     |                  |                 |      |        |       |              | quantitative | anomalies | in unstructured |     | logs. In: Proc. | International | Joint | Conf. |
| --------- | --- | ---------------- | --------------- | ---- | ------ | ----- | ------------ | ------------ | --------- | --------------- | --- | --------------- | ------------- | ----- | ----- |
| framework | for | network function | virtualization. | IEEE | Trans. | Netw. | Serv. Manag. |              |           |                 |     |                 |               |       |       |
onArtificialIntelligence.InternationalJointConferencesonArtificialIntelligence
14(4),949–963.
Organization,pp.4739–4745.
D’Amico,A.,Whitley,K.,2008.Therealworkofcomputernetworkdefenseanalysts.
In:VizSEC2007.Springer,pp.19–37. Meng, Y., Qin, T., Liu, Y., He, C., 2018. High threat alarms mining for effective
DeKoninck,P.,vandenBroucke,S.,DeWeerdt,J.,2018.Act2vec,trace2vec,log2vec, securitymanagement:Modeling,experimentandapplication.In:IEEESymposium
onComputersandCommunications.
| and model2vec: |            | Representation | learning | for business | processes. | In:     | Weske, M.,  |              |            |           |              |       |           |                   |     |
| -------------- | ---------- | -------------- | -------- | ------------ | ---------- | ------- | ----------- | ------------ | ---------- | --------- | ------------ | ----- | --------- | ----------------- | --- |
|                |            |                |          |              |            |         |             | Mikolov, T., | Sutskever, | I., Chen, | K., Corrado, | G.S., | Dean, J., | 2013. Distributed |     |
| Montali,       | M., Weber, | I., vom        | Brocke,  | J. (Eds.),   | Business   | Process | Management. |              |            |           |              |       |           |                   |     |
representationsofwordsandphrasesandtheircompositionality.Adv.NeuralInf.
SpringerInternationalPublishing,Cham,pp.305–321.
Process.Syst.26.
DiMauro,M.,Liotta,A.,2019.StatisticalassessmentofIPmultimediasubsystemina
softwarizedenvironment:Aqueueingnetworksapproach.IEEETrans.Netw.Serv. 2022.Netflixhystrix.https://github.com/Netflix/Hystrix.
Manag.16(4),1493–1506. Nguyen, D.T., Nguyen, K.K., Cheriet, M., 2018. NFV-based architecture for the in-
|     |     |     |     |     |     |     |     | terworking | between | WebRTC | and IMS. | IEEE Trans. | Netw. Serv. | Manag. | 15 (4), |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------- | ------ | -------- | ----------- | ----------- | ------ | ------- |
Dragoni,N.,etal.,2017.Microservices:Yesterday,today,andtomorrow.In:Present
1363–1377.
| and Ulterior | Software | Engineering. | Springer | International |     | Publishing, | Cham, pp. |           |               |             |     |            |                       |     |       |
| ------------ | -------- | ------------ | -------- | ------------- | --- | ----------- | --------- | --------- | ------------- | ----------- | --- | ---------- | --------------------- | --- | ----- |
|              |          |              |          |               |     |             |           | Noor, A., | et al., 2019. | A framework | for | monitoring | microservice-oriented |     | cloud |
195–216.
applicationsinheterogeneousvirtualizationenvironments.In:IEEE12thIntl.Conf.
Du,M.,Li,F.,Zheng,G.,Srikumar,V.,2017.DeepLog:Anomalydetectionanddiagnosis
fromsystemlogsthroughdeeplearning.In:Proc.oftheACMSIGSACConference onCloudComputing.pp.156–163.
|     |     |     |     |     |     |     |     | Oliner, A., | Ganapathi, | A., Xu, W., | 2012. Advances | and | challenges | in log | analysis. |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ---------- | ----------- | -------------- | --- | ---------- | ------ | --------- |
onComputerandCommunicationsSecurity.ACM,NY,USA,pp.1285–1298.
Commun.ACM55(2),55–61.
| Fadda, E., | Plebani, | P., Vitali, | M., 2016. | Optimizing | monitorability |     | of multi-cloud |                 |            |        |         |             |            |          |       |
| ---------- | -------- | ----------- | --------- | ---------- | -------------- | --- | -------------- | --------------- | ---------- | ------ | ------- | ----------- | ---------- | -------- | ----- |
|            |          |             |           |            |                |     |                | Ruiu, D., 1999. | Cautionary | tales: | stealth | coordinated | attack how | to. URL: | http: |
applications.In:AdvancedInformationSystemsEngineering.SpringerInternational
//www.ouah.org/stealthhowto.html.
Publishing,pp.411–426.
|     |     |     |     |     |     |     |     | Santana, M., | Sampaio | Jr., A., Andrade, | M., | Rosa, N.S., | 2019. Transparent | tracing | of  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ------- | ----------------- | --- | ----------- | ----------------- | ------- | --- |
Farshchi,M.,Schneider,J.-G.,Weber,I.,Grundy,J.,2018.Metricselectionandanomaly microservice-basedapplications.In:Proc.ofthe34thACM/SIGAPPSymposiumon
| detection | for cloud | operations | using log | and metric | correlation | analysis. | J. Syst. |     |     |     |     |     |     |     |     |
| --------- | --------- | ---------- | --------- | ---------- | ----------- | --------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
AppliedComputing.NewYork,NY,USA,pp.1252–1259.
Softw.137,531–549.
Schölkopf,B.,Williamson,R.C.,Smola,A.,Shawe-Taylor,J.,Platt,J.,2000.Support
Freund,Y.,Schapire,R.E.,1997.ADecision-Theoreticgeneralizationofon-linelearning
vectormethodfornoveltydetection.In:AdvancesinNeuralInformationProcessing
andanapplicationtoboosting.J.Comput.SystemSci.55(1),119–139.
Systems.
Fu, X., Shi, J., Xie, L., 2010. A novel data mining-based method for alert reduction Sharma,A.,Kalbarczyk,Z.,Barlow,J.,Iyer,R.,2011.Analysisofsecuritydatafrom
andanalysis.J.Netw.5(1),88. alargecomputingorganization.In:The41stIEEE/IFIPIntl.Conf.onDependable
| Gan, Y., Dev, | S., Lo, | D., Delimitrou, | C., | 2020. Sage: | Leveraging | ML  | to diagnose |     |     |     |     |     |     |     |     |
| ------------- | ------- | --------------- | --- | ----------- | ---------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
SystemsandNetworks.
unpredictableperformanceincloudmicroservices.MLComput.Archit.Syst..
|                |         |           |          |             |           |     |              | Spathoulas, | G.P., Katsikas, | S.K., | 2010. Reducing | false positives | in intrusion | detection |     |
| -------------- | ------- | --------- | -------- | ----------- | --------- | --- | ------------ | ----------- | --------------- | ----- | -------------- | --------------- | ------------ | --------- | --- |
| Guo, H., Yuan, | S., Wu, | X., 2021. | LogBERT: | Log anomaly | detection | via | BERT. arXiv: |             |                 |       |                |                 |              |           |     |
systems.Comput.Secur.29(1),35–44.
2103.04475.
|     |     |     |     |     |     |     |     | Srirama, S.N., | Adhikari, | M., Paul, | S., 2020. | Application | deployment | using containers |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --------- | --------- | --------- | ----------- | ---------- | ---------------- | --- |
Hassan, W.U., Noureddine, M.A., Datta, P., Bates, A., 2020. Omegalog: High-fidelity withauto-scalingformicroservicesincloudenvironment.J.Netw.Comput.Appl.
| attack | investigation | via transparent | multi-layer |     | log analysis. | In: | Network and | 160,102629. |     |     |     |     |     |     |     |
| ------ | ------------- | --------------- | ----------- | --- | ------------- | --- | ----------- | ----------- | --- | --- | --- | --- | --- | --- | --- |
DistributedSystemSecuritySymposium.
Stearley,J.,Oliner,A.J.,2008.Badwords:Findingfaultsinspirit’ssyslogs.In:IEEE
| Hempstalk, | K., Frank, | E., Witten, | I.H., 2008. | One-class | classification |     | by combin- |     |     |     |     |     |     |     |     |
| ---------- | ---------- | ----------- | ----------- | --------- | -------------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
Intl.SymposiumonClusterComputingandtheGrid.pp.765–770.
| ing density | and | class probability | estimation. | In: | Daelemans, | W., | Goethals, B., |     |     |     |     |     |     |     |     |
| ----------- | --- | ----------------- | ----------- | --- | ---------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
Sun,Y.,Nanda,S.,Jaeger,T.,2015.Security-as-a-serviceformicroservices-basedcloud
Morik,K.(Eds.),MachineLearningandKnowledgeDiscoveryinDatabases.Berlin, applications.In:IEEE7thIntl.Conf.onCloudComputingTechnologyandScience.
Heidelberg,pp.505–519. 2022.Sysdig.https://sysdig.com/opensource/.
Hirakawa,R.,Tominaga,K.,Nakatoh,Y.,2020.Softwareloganomalydetectionthrough Thalheim, J., et al., 2017. Sieve: Actionable insights from monitored metrics in
| one class | clustering | of transformer | encoder | representation. |     | In: Stephanidis, | C., |     |     |     |     |     |     |     |     |
| --------- | ---------- | -------------- | ------- | --------------- | --- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
distributedsystems.In:Proc.ofthe18thACMMiddlewareConference.Association
Antona,M.(Eds.),Proc.HCIInternational-Posters.Springer,pp.655–661.
forComputingMachinery,pp.14–27.
Ibidunmoye, O., Rezaie, A., Elmroth, E., 2018. Adaptive anomaly detection in Vaarandi, R., 2008. Mining event logs with SLCT and LogHound. In: IEEE Network
performancemetricstreams.IEEETrans.Netw.Serv.Manag.15(1),217–231. OperationsandManagementSymposium.
Jain,R.,1991.TheArtofComputerSystemsPerformanceAnalysis.JohnWiley&Sons Valeur,F.,Vigna,G.,Kruegel,C.,Kemmerer,R.A.,2004.Comprehensiveapproachto
NewYork. intrusiondetectionalertcorrelation.IEEETrans.DependableSecureComput.1(3).
Julisch,K.,Dacier,M.,2002.Miningintrusiondetectionalarmsforactionableknowl- Wohlin, C., et al., 2000. Experimentation in Software Engineering: An Introduction.
edge.In:Proc.oftheEighthACMSIGKDDIntl.Conf.onKnowledgeDiscoveryand
KluwerAcademic.
DataMining.ACM,NewYork,NY,USA,pp.366–375. Wolff, E., 2016. Microservices: Flexible Software Architecture. Addison-Wesley
| Kavanagh, | K.M., et | al., 2016. | Magic Quadrant | for | Security | Information | and Event | Professional. |     |     |     |     |     |     |     |
| --------- | -------- | ---------- | -------------- | --- | -------- | ----------- | --------- | ------------- | --- | --- | --- | --- | --- | --- | --- |
Management.TechnicalReport,GartnerReasearch. Wu, L., Tordsson, J., Elmroth, E., Kao, O., 2020. MicroRCA: Root cause localization
Kobayashi, S., Otomo, K., Fukuda, K., Esaki, H., 2018. Mining causality of network of performance issues in microservices. In: IEEE/IFIP Network Operations and
eventsinlogdata.IEEETrans.Netw.Serv.Manag.15(1),53–67.
ManagementSymposium.pp.1–9.
Li,R.-H.,Belford,G.G.,2002.Instabilityofdecisiontreeclassificationalgorithms.In: Xie,H.,Lv,K.,Hu,C.,2018.Aneffectivemethodtogeneratesimulatedattackdata
Proc.ofthe8thACMSIGKDDIntl.Conf.onKnowledgeDiscoveryandDataMining. basedongenerativeadversarialnets.In:17thIEEEIntl.Conf.onTrust,Security
In:KDD2002,AssociationforComputingMachinery,NewYork,USA,pp.570–575. andPrivacyinComputingandCommunications.pp.1777–1784.
http://dx.doi.org/10.1145/775047.775131. Xu, W., Huang, L., Fox, A., Patterson, D.A., Jordan, M.I., 2008. Mining console logs
Li, X., Chen, P., Jing, L., He, Z., Yu, G., 2020. SwissLog: Robust and unified deep forlarge-scalesystemproblemdetection.SysML8,4.
learning based log anomaly detection for diverse faults. In: Proc. International Yang, R., Qu, D., Gao, Y., Qian, Y., Tang, Y., 2019. nLSALog: An anomaly de-
SymposiumonSoftwareReliabilityEngineering.IEEE,pp.92–103.http://dx.doi. tection framework for log sequence in security management. IEEE Access 7,
| org/10.1109/ISSRE5003.2020.00018. |     |     |     |     |     |     |     | 181152–181164. |     |     |     |     |     |     |     |
| --------------------------------- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- |
14

M.Cinqueetal.
JournalofNetworkandComputerApplications208(2022)103515
Yuan, X., Abouelenien, M., 2015. A multi-class boosting method for learning from RaffaeleDellaCortereceivedtheB.S.andM.S.degreesin
imbalanceddata.Int.J.Granul.Comput.RoughSetsIntell.Syst.4(1),13–29. computer engineering and Ph.D. degree from the Federico
Yuan, Y., et al., 2020. ADA: Adaptive deep log anomaly detector. In: IEEE Conf. on II University of Naples, Italy in 2009, 2012, and 2016,
ComputerCommunications.pp.2449–2458. respectively. He is currently an Assistant Professor with
|     |     |     |     | the Department | of Electrical Engineering | and Information |     |
| --- | --- | --- | --- | -------------- | ------------------------- | --------------- | --- |
2022.Zipkin.https://github.com/openzipkin/zipkin.
Zoppi, T., Ceccarelli, A., Bondavalli, A., 2016. Context-awareness to improve Technologies,FedericoIIUniversityofNaples.Hisresearch
anomalydetectionindynamicserviceorientedarchitectures.In:ComputerSafety, interests include data-driven failure analysis, on-line mon-
|     |     |     |     | itoring of software | systems, and | security. Dr. Della | Corte |
| --- | --- | --- | --- | ------------------- | ------------ | ------------------- | ----- |
Reliability,andSecurity.SpringerInt’lPublishing,pp.145–158.
|     |     |     |     | serves as | Reviewer in several | dependability conferences |     |
| --- | --- | --- | --- | --------- | ------------------- | ------------------------- | --- |
Zuo,Y.,Wu,Y.,Min,G.,Huang,C.,Pei,K.,2020.Anintelligentanomalydetection
scheme for micro-services architectures with temporal and spatial data analysis. and workshops, and he is involved in industrial projects
IEEETrans.Cogn.Commun.Netw.6(2),548–561. developing techniques for the analysis and monitoring of
criticalsystems.
AntonioPecchiareceivedtheB.S.(2005),M.S.(2008)and
MarcelloCinquereceivedtheGraduate(Hons.)degreeand
Ph.D. degree from the Federico II University of Naples, Ph.D.(2011)inComputerEngineeringfromtheFedericoII
Italy, in 2003 and 2006, respectively. He is currently UniversityofNaples,Italy.HeisnowanAssistantProfessor
|              |                  |               |          | of data science | at the University | of Sannio, Italy. | He is |
| ------------ | ---------------- | ------------- | -------- | --------------- | ----------------- | ----------------- | ----- |
| an Associate | Professor at the | Department of | Computer |                 |                   |                   |       |
|              |                  |               |          | a co-founder    | of the Critiware  | spin-off company  | (www. |
andSystemsEngineering,FedericoIIUniversityofNaples,
Italy. His interests include field failure data analysis of critiware.com).HeservesasTPCmemberandreviewerin
|             |                         |               |        | conferences | and workshops on | software engineering | and |
| ----------- | ----------------------- | ------------- | ------ | ----------- | ---------------- | -------------------- | --- |
| distributed | systems, and middleware | solutions for | mobile |             |                  |                      |     |
dependability,suchasISSRE,EDCC,LADCandICTSS.His
| ubiquitous | systems. Dr. Cinque | is the Chair and/or | TPC |     |     |     |     |
| ---------- | ------------------- | ------------------- | --- | --- | --- | --- | --- |
memberofseveraltechnicalconferencesandworkshopson researchinterestsincludedeeplearning,loganalysis,empir-
dependable,mobile,andpervasivesystems,includingIEEE ical software engineering, intrusion detection, dependable
andsecuredistributedsystems.
| Personal, Indoor | and Mobile Radio | Communications | and |     |     |     |     |
| ---------------- | ---------------- | -------------- | --- | --- | --- | --- | --- |
ACMInternationalConferenceProceedingSeries.
15