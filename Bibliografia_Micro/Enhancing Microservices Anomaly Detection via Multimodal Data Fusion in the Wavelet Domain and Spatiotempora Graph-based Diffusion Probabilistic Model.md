PDF Download
3711896.3736938.pdf
18 March 2026
Total Citations: 0
. Total Downloads: 1923
.
Latest updates: hps://dl.acm.org/doi/10.1145/3711896.3736938 .
.
Published: 03 August 2025
.
. .
RESEARCH-ARTICLE .
Citation in BibTeX format
Enhancing Microservices Anomaly Detection via Multimodal Data
.
.
Fusion in the Wavelet Domain and Spatiotemporal Graph-based KDD '25: The 31st ACM SIGKDD
Conference on Knowledge Discovery and
Diffusion Probabilistic Model Data Mining
August 3 - 7, 2025
Toronto ON, Canada
KAIQI DING, Peking University, Beijing, China .
.
. Conference Sponsors:
YUANMU MA, Beijing Institute of Technology, Beijing, China SIGMOD
SIGKDD
.
ZIJIAN SONG, Peking University, Beijing, China
.
KAIGUI BIAN, Peking University, Beijing, China
.
.
.
Open Access Support provided by:
.
Peking University
.
Beijing Institute of Technology
.
KDD '25: Proceedings of the 31st ACM SIGKDD Conference on Knowledge Discovery and Data Mining V.2 (August 2025)
hps://doi.org/10.1145/3711896.3736938
ISBN: 9798400714542
.

Enhancing Microservices Anomaly Detection via Multimodal
Data Fusion in the Wavelet Domain and Spatiotemporal
Graph-based Diffusion Probabilistic Model
KaiqiDing YuanmuMa
SchoolofCS,PekingUniversity BeijingInstituteofTechnology
Beijing,China Beijing,China
2301112519@stu.pku.edu.cn 3220220949@bit.edu.cn
ZijianSong KaiguiBian∗
SchoolofCS,PekingUniversity SchoolofCS,PekingUniversity
Beijing,China Beijing,China
2201111590@stu.pku.edu.cn bkg@pku.edu.cn
Abstract CCSConcepts
Microservicesarchitecturehasbecomeincreasinglypopularinmod- •Computingmethodologies→Anomalydetection;•Soft-
ernsoftwaresystems,yetitscomplexityalsoposeschallengesfor wareanditsengineering→Softwareperformance.
failurediagnosis.Existingliteraturehasdeficienciesinmultimodal
datamining,mainlyintwoaspects:first,theminingofmultimodal Keywords
dataisinsufficient,failingtofullyexploittherichinformationcon-
MicroservicesAnomalyDetection;MultimodalDataFusion;Wavelet
tainedindifferenttypesofdata;second,theanalysisofspatiotem-
DomainAttentionMechanism
poralfeaturesofmultimodaldataisnotthorough,failingtofully
explorethepotentialassociationsofdatainthetemporalandspa-
ACMReferenceFormat:
tialdimensions.Toaddresstheseissues,thispaperproposesanew
KaiqiDing,YuanmuMa,ZijianSong,andKaiguiBian.2025.EnhancingMi-
methodforanomalydetectioninmicroservices.Wetransformthree
croservicesAnomalyDetectionviaMultimodalDataFusionintheWavelet
typesofmodaldataintothewaveletdomainandachievefusion DomainandSpatiotemporalGraph-basedDiffusionProbabilisticModel.In
amongmodalitiesbasedonanattentionmechanism,fullyutilizing Proceedingsofthe31stACMSIGKDDConferenceonKnowledgeDiscovery
theinherentcharacteristicsofmultimodaldatainthefrequencyand andDataMiningV.2(KDD’25),August3–7,2025,Toronto,ON,Canada.ACM,
temporaldomains.Thisfusionprocesscanextractnewinformation NewYork,NY,USA,11pages.https://doi.org/10.1145/3711896.3736938
thatdoesnotexistintheoriginalmodalities,therebyenhancing
themodel’sabilitytodetectanomalies.Inaddition,weproposea
newdiffusionprobabilisticmodel(DDPM)basedonspatiotempo- 1 Introduction
ralgraphs,whichcombinesspatiotemporallearningcapabilities
Microservicearchitecturecommunicatesthroughlightweightmech-
withtheuncertaintymeasurementofDDPMtogeneratefuture
anismsandhasgainedsignificantpopularityinrecentyears[2,7].
samplesinanon-autoregressivemanner,achievingmulti-horizon
However,thelargescaleofmicroservicesystemspresentschal-
prediction.Experimentalresultsshowthatourmethodsignificantly
lenges,particularlyinanomalydetection.Anomaliesinthesesys-
improvesanomalydetectionperformanceonthreepublicdatasets
temscanleadtodataloss,businessdisruptions,financiallosses,and
andareal-worldproductionsystem,demonstratingitseffectiveness
reducedoperationalefficiency[1].Recognizingtheimportanceof
inmicroservicesanomalydetection.
servicereliability,majorcloudproviderssuchasAmazonWebSer-
vices(AWS)andMicrosoftAzurehavemadesignificantinvestments
∗Correspondingauthor. inanomalydetectionformicroservices[20,31].
To ensure effective anomaly detection, current research pre-
KaiqiDing,ZijianSongandKaiguiBianareaffiliatedwithSchoolofCS,AIInnovation dominantlyreliesonanalyzingthreecriticaldatamodalities:met-
Center,NationalEngineeringLaboratoryforBigDataAnalysisandApplications, rics (time-seriesdata), logs (textual structureddata), and traces
NationalKeyLaboratoryforMultimediaInformationProcessing,PekingUniversity.
(graph-structureddata).Mostexistinganomalydetectionmethods
arebasedonsingle-modalitydata[28].However,previousstud-
Permissiontomakedigitalorhardcopiesofallorpartofthisworkforpersonalor
ies [15, 19, 26] have highlighted that these methods are unable
classroomuseisgrantedwithoutfeeprovidedthatcopiesarenotmadeordistributed
forprofitorcommercialadvantageandthatcopiesbearthisnoticeandthefullcitation tocaptureanomalyinformationrelatedtocertainfaults.Toad-
onthefirstpage.Copyrightsforcomponentsofthisworkownedbyothersthanthe dressthelimitationsofsingle-modaldata,methods[11,22,32]use
author(s)mustbehonored.Abstractingwithcreditispermitted.Tocopyotherwise,or
multimodaldatatoachievemoreeffectivefailurediagnosis.They
republish,topostonserversortoredistributetolists,requirespriorspecificpermission
and/orafee.Requestpermissionsfrompermissions@acm.org. firstpreprocessheterogeneousdatatoextractamorereasonable
KDD’25,Toronto,ON,Canada representationofmultimodalfeatures[11,15,22,26,32].These
©2025Copyrightheldbytheowner/author(s).PublicationrightslicensedtoACM.
unifiedfeaturesarethenusedasinputsfordeeplearningorother
ACMISBN979-8-4007-1454-2/2025/08
https://doi.org/10.1145/3711896.3736938 machine learning models to detect anomalies. Multimodal data
510

KDD’25,August3–7,2025,Toronto,ON,Canada KaiqiDing,YuanmuMa,ZijianSong,andKaiguiBian
integratesinformationfromvarioussources,offeringamorecom- Table1:ComparedtoFUSION,existingmethodsdidnotcom-
prehensivereflectionofthesystem’soperationalstate;however, prehensivelyaddressmultimodalanomalydetection(Temp
severallimitationspersistinexistingmethods: forTemporal,SpatforSpatio,andFreqforFrequency).
• Limitation1:Insufficientexploitationonmulti-modaldata.
Modality FeatureExtraction
Currentmultimodalanomalydetectionapproachesinadequately Approach
MetricLogTrace Modalfusion Modalattention TempSpatFreq
explorecross-modalrelationships.Mostapproaches[22,32]em-
DeepTraLog
ployearlyfusionbysimplyconcatenatingmultimodaldataas
Hades Laterfusion cross-attention
multiplechannels.However,theyfailtocapturecomplexinter- MADMM Laterfusion cross-attention
modalrelationshipsinsophisticatedmultimodaldatasets.While MISP Laterfusion cross-attention
Medicine Laterfusion channelattention
laterfusionmethods[15,19,25,26]inTable1primarilyfocus
AnoFusion EarlyFusion
onattention-basedfusionofmetricsandlogs,theygenerally Triple EarlyFusion
neglectthree-modalfusionscenarios.Morecritically,existing MSTGAD
researchoverlooksfrequency-domainanalysisofmultimodal FUSION Laterfusion waveletfusion
data.Temporalanalysisfocusesondirectobservationsatspecific
timepoints,potentiallymissingperiodicpatternsthatfrequency
tocapturetemporaldependenciesandspatialcorrelations.Unlike
analysiscouldreveal.Thislimitationisparticularlyproblematic
traditionalDDPMs,FUSIONemploysrandomizeddiffusionstepsto
fornon-stationarymicroservicedata,wheretemporal-domain
moreeffectivelycapturespatiotemporaldynamicsandimprovede-
analysisalonemaybeinsufficienttocapturethefullcomplexity
noisingduringthereverseprocess.Furthermore,FUSIONgenerates
ofthedata.
• Limitation2:Lackofspatiotemporalfeaturelearning.Ac- futuresamplesinanon-autoregressivemanner,enablingefficient
multi-horizonpredictionsallatonce.Thismodeloffersbothhis-
curatelyidentifyinganomalouspatternsrequiresmodelingboth
toricaldatareconstructionandfutureprediction,providingkey
spatialrelationships(e.g.,serviceinvocationdependencies)and
benefitsforfaultdiagnosis.Reconstructingpastdatahelpsanalyze
temporaldynamics(e.g.,variationsovertime).However,existing
failuretrendsandsupportsproblem-solving.Itspredictiveabilities
approachesexhibitcriticalgapsinthisregard.Forinstance,Deep-
provideearlyfaultwarnings,enablingpreventivemaintenancethat
tralog[30]failstoincorporatetemporalfeatures,disregarding
reducesrisksandimprovessystemstability.
essentialtemporalvariationsintraces.Similarly,studiessuch
WeconductedextensivestudiestoevaluateFUSIONonthree
as[15,19,32]neglectspatialdependenciesacrossmodalitiesin
open-sourceplatforms:AIOPS2022[4],GAIA[5],andSocialNet-
Table1.Currentspatiotemporalmodeling[11,22,25,26]predom-
work[9],andareal-worldproductionmicroservicesystem.Benefit-
inantlyreliesondeterministicapproaches,whichcomputefuture
ingfromtheuseofmultimodaldata,FUSIONachievesanotableim-
stateswithoutaccountingforrandomness.Microservicearchitec-
provement,increasingF1-scoreby2.70%–129.27%,3.62%–137.37%,
turescreatedatauncertaintyfromdiversesourcesandcomplex
2.70%–86.16%,and10.21%–168.83%onfourdatasets,respectively.In
dependencies.Spatiotemporalmodelsformultimodalmicroser-
summary,thispaperhasmadethefollowingprimarycontributions.
vicedatashouldincorporateuncertaintybyusingprobability
distributionsinsteadofdeterministicoutputs. • Wearethefirsttoproposefeaturefusionformultimodaldatain
thewaveletdomain,leveragingaPearsoncorrelation-basedat-
To systematically address the two identified limitations, we
tentionmechanismtoenhanceanomalydetectionbycombining
proposeFUSION,anovelframeworkthatintegratesFrequency-
bothtemporalandfrequencyfeatures.
domainmultimodalfusionbasedonattentionmechanismswith
• Wetackletheproblemofprobabilisticspatiotemporalanomaly
Uncertainty-awareSpatiotemporalIntegrationforOnlineanomaly
detectionfromaconditionaldiffusionperspectivewiththefirst
detectioN.Thispaperisthefirsttoaddressthechallengesofmulti-
shot.FUSIONcaneffectivelymodelthecomplexspatiotemporal
modaldatafusionandanomalydetectiononspatiotemporalgraphs.
dependenciesandintrinsicuncertaintieswithinmultimodaldata.
Limitation1isapproachedthroughFUSION’sfeaturefusioninthe
• WeconductextensiveexperimentstodemonstratethatFUSION
waveletdomain,whicheffectivelycapturesbothfrequency-domain
ismoreeffectivethanstate-of-the-artanomalydetectors.We
andtime-domainfeaturesofmultimodaldata.Morespecifically,
havemadetheimplementationcodepubliclyavailableathttps:
we decompose multimodal data into different frequency bands
//github.com/AmadeusClo/FUSION.
(wavelets)withdifferentresolutionsrepresentedaswaveletcoeffi-
cientstoenablemoresophisticatedtimeseriesfeatureextraction. 2 Motivation
Then,weapplyacorrelation-basedattentionmechanismbycal-
2.1 WhyFusioninWaveletDomain?
culatingPearsonCorrelationCoefficientsamongvariablesacross
modalities.Themechanismadjuststheweightsoftheirwavelet DiscreteWaveletTransform(DWT)effectivelydecomposesnon-
coefficientsforhighlycorrelatedvariables,emphasizingthemost stationary multimodal data into wavelet coefficients across fre-
usefulinformationfromthewaveletdomain.Finally,werecon- quencybands,capturingbothshort-termfluctuations(detailco-
structtheweightedcoefficientsintoafrequency-enhancedfeature efficients)andlong-termtrends(approximationcoefficients).Our
representation.ForLimitation2,weemployanovelspatiotempo- analysisrevealsasignificantcorrelationbetweenhigh-frequency
ralgraph-basedDenoisingDiffusionProbabilisticModel(DDPM), and low-frequency components across multimodal data, which
whichcombinesspatiotemporallearningwithuncertaintymea- exhibitconsistentperiodicityandsynchronizedpeak-valleyvari-
surements.FUSIONleveragesaU-structure-basedarchitecture[23] ations in Figure 1(a). The wavelet domain feature fusion offers
511

EnhancingMicroservicesAnomalyDetectionviaMultimodalDataFusionintheWaveletDomainand
SpatiotemporalGraph-basedDiffusionProbabilisticModel KDD’25,August3–7,2025,Toronto,ON,Canada
|               |                  |                 |     | 1.0              |             |     | 3.1 MultimodalDataSerialization |     |     |     |     |
| ------------- | ---------------- | --------------- | --- | ---------------- | ----------- | --- | ------------------------------- | --- | --- | --- | --- |
| 0.08          |  Trace_duration  |  N etw ork_drop |     |    Probabilistic |             |     |                                 |     |     |     |     |
| ycneuqerF-hgi |  M em ory_usage  |                 |     | 0.8    G         | round-truth |     |                                 |     |     |     |     |
0.04 egasu_    D eterm inistic  3.1.1 MetricSerialization. Microserviceshaveasetofmetricsrep-
0.6
0.00 resentingamultivariatetimeseries.Inthispaper,wefocusonmulti-
| (cid:5)(cid:2)(cid:1)(cid:2)(cid:3) |     |     |     | UP 0.4 |     |     |     |     |     |     |     |
| ----------------------------------- | --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
C 0.2 variatetime-seriesdata,denotedas𝐻ˆ 𝑀 ={ℎ 𝑀 ,...,ℎ 𝑀 }∈R𝐹𝑀×𝑇
| H (cid:5)(cid:2)(cid:1)(cid:2)(cid:4) |              |                                  |     |             |                        |       |                                                       |     | 𝑖 𝑖 ,0 | 𝑖 ,𝑇 | ,   |
| ------------------------------------- | ------------ | -------------------------------- | --- | ----------- | ---------------------- | ----- | ----------------------------------------------------- | --- | ------ | ---- | --- |
|                                       |              |                                  |     | 0.0         |                        |       | representingasequenceoftimestampedobservationsofsize𝑇 |     |        |      |     |
| 1.60                                  | 300 400      | 500 600                          | 700 | 0 5         | 10 15                  | 20 25 |                                                       |     |        |      | for |
|                                       |   T r a ce _ | d u r a t io n    N etw ork_drop |     | 2 4 0     P | r o b a b i l i s ti c |       |                                                       |     |        |      |     |
1.40   M e m o r y _ u s a g e 2 1 0     G r o u n d - t r u t h the𝑖-thinstanceand𝐹 𝑀 isthenumberofmetrics.
| ycneuqerF- 1.20 |     |     |     | 180    D           | eterm inistic  |     |     |     |     |     |     |
| --------------- | --- | --- | --- | ------------------ | -------------- | --- | --- | --- | --- | --- | --- |
| 1.00            |     |     |     | noitarud_ecarT 150 |                |     |     |     |     |     |     |
| 0.80            |     |     |     | 120                |                |     |     |     |     |     |     |
woL 0.60 90 3.1.2 LogSerialization. FUSIONusestheDrain3[25]algorithm,
| 0.40 |     |     |     | 60  |     |     |     |     |     |     |     |
| ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
30 whichexcelsinperformanceandefficiencyforlogtemplateextrac-
| 0.20 |     |     |     | 0   |     |     |     |     |     |     |     |
| ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
300 400 500 600 700 0 5 10 15 20 25 tion.Theserializationprocessconsistsoftwomainsteps:
|     |                    | Tim estam p      |               |                | Tim estam         | p                      |     |     |     |     |     |
| --- | ------------------ | ---------------- | ------------- | -------------- | ----------------- | ---------------------- | --- | --- | --- | --- | --- |
|     | (a )W a v e le t d | o m a in  d a ta |  a n a ly sis | (b ) M o tiv a | tio n  o f p ro b | a b ilistic  m o d e l |     |     |     |     |     |
(1)LogTemplateClustering.Tomanagediverselogvariations,
weclusterlogtemplatestogroupsimilarentriesandreduceredun-
Figure1:Multimodaldataanalysisandprobabilisticpredic-
dancy.Whensoftwareupdates,weclassifynewlogtemplatesby
tion.(a)Thewaveletdecompositionofmultimodaldataem-
comparingthemtoexistingclustercentroidstodeterminetheir
phasizesthecorrelationofwaveletdomain.(b)Comparingde-
membershiportheneedfornewclusters.Weutilizethebert-base-
terministicmethods(e.g.,Spatiotemporalconvolution)with
uncased[8]modelforembeddingvectorsandapplyingtheDB-
probabilisticapproaches(e.g.,DDPM)anddemonstratingthe SCAN[24]algorithm,resultingin𝐹
𝐿−1clusters.
superiorityofprobabilisticmethodsparticularlywhenCPU
(2)LogEntrySerialization.Thesystemcalculatesthedistance
ortracelatencyspikesoccurintheblackdottedboxarea.
betweenthesentenceembeddingvectorsoflogentriesandcluster
centroidstodeterminetheircategories.Ifalogentrydoesn’tmatch
acluster,it’sidentifiedasananomaloustemplateandassigned
toaseparatecategory,resultingin𝐹
𝐿 totalcategories.Toalign
|                                                            |     |     |     |     |     |     | this analysis                                          | with system metrics, | we count | the occurrences | of  |
| ---------------------------------------------------------- | --- | --- | --- | --- | --- | --- | ------------------------------------------------------ | -------------------- | -------- | --------------- | --- |
| twokeyadvantages:First,itpreservestheuniquecharacteristics |     |     |     |     |     |     |                                                        |                      |          |                 | 𝐿   |
|                                                            |     |     |     |     |     |     | eachlogcategoryovertime,generatingalogrepresentation𝐻ˆ |                      |          |                 | =   |
𝑖
o f e a c h m o d al i t y w h il e l e ve ra g i n g th e i r c o m p l e m e n t ar y r e l a ti o n - {ℎ 𝐿 ,...,ℎ 𝐿 }∈R𝐹𝐿×𝑇
|          |             |                  |            |                  |                   |                      | 𝑖 ,0 | 𝑖 ,𝑇 . |     |     |     |
| -------- | ----------- | ---------------- | ---------- | ---------------- | ----------------- | -------------------- | ---- | ------ | --- | --- | --- |
| sh i p s | . Se co n d | , i t e nh a n c | e s th e s | y s te m ’ s r e | s ili e n c e t o | n o is e , a s t h e |      |        |     |     |     |
presenceofmultiplemodalitiesensuresthatvaluableinsightscan
stillbeextractedevenwhenonemodalityiscompromised.This 3.1.3 TraceSerialization. Inamicroservicesystem,atracecaptures
dualadvantageimprovesthemodel’srobustness,particularlyin user request executions as spans, which include attributes like
traceID,requesttype,spanID,parentspanID,serviceinstance
complexanddynamicsignalenvironmentswheredataqualityand
ID,starttime,andduration.Weanalyzethesespanssequentially
consistencymayvary.
toextractstructuralinformationanddependencies.Durationis
thentransformedintoamultivariatetimeseriesbycalculatingthe
2.2 WhyDDPM?
|     |     |     |     |     |     |     | average | latency, total requests, | and status code | frequencies | per |
| --- | --- | --- | --- | --- | --- | --- | ------- | ------------------------ | --------------- | ----------- | --- |
Recentmultimodalanomalydetectiontechniquesaremainlydeter- minute.Theresultingtracemultivariatetimeseriesisrepresented
|     |     |     |     |     |     |     | 𝑇𝑟  | {ℎ𝑇 𝑟,...,ℎ𝑇 𝑟} | R𝐹𝑡𝑟×𝑇 |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | ------ | --- | --- |
ministic,accuratelypredictingfuturedata[11,22,26,32].However, as𝐻ˆ = ∈ ,where𝐹 𝑡𝑟 isthenumberof
|     |     |     |     |     |     |     | 𝑖   | 𝑖,0 𝑖,𝑇 |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- |
spansforinstance𝑖.
thesemethodsfacechallengeswithspatiotemporaluncertainties,
affectingtheirreal-worlddecision-makingeffectiveness.Weadopt
probabilisticmodelsoverdeterministiconesfortheuncertainty 3.1.4 Multimodal Data Construction. We perform z-score stan-
modelingability.Microservicemultimodaldatainherentlyinvolves
dardization[26]usingaslidinghistoricalwindowonatimese-
uncertaintyduetodiversedatasources,complexdependencies, riesmodal.Foreachinstance𝑖 attime𝑡,weconcatenatethefea-
(cid:16) 𝑇𝑟(cid:17)
varyingenvironments,anddatanoiseorincompleteness.Proba- tures into a fused feature vector 𝐻 𝑚𝑜𝑑𝑎𝑙 = 𝐻ˆ 𝑀∥𝐻ˆ 𝐿∥𝐻ˆ =
|     |     |     |     |     |     |     |     |     | 𝑖   | 𝑖 𝑖 | 𝑖   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
bilisticmodelsaddressthisbyrepresentingdatastatesthrough
|     |     |     |     |     |     |     | {𝑥 𝑚 𝑜𝑑𝑎𝑙,...,𝑥 | 𝑚 𝑜𝑑𝑎𝑙}∈R𝐹𝑚𝑜𝑑𝑎𝑙×𝑇 | ,where𝐹 | =𝐹 𝑀+𝐹 | 𝐿+𝐹 𝑇𝑟. |
| --- | --- | --- | --- | --- | --- | --- | --------------- | ----------------- | ------- | ------ | ------- |
probabilitydistributionsratherthanasingledeterministicvalue, 𝑖 ,0 𝑖 ,𝑇 𝑚𝑜𝑑𝑎𝑙
naturallycapturingtheuncertaintyasshowninFigure1(b). Thisachievesserializationacrossmetrics,logs,andtraces.
3.2 MultimodalWaveletFusion
3 ProposedApproach
|     |     |     |     |     |     |     | 3.2.1 DiscreteWaveletTransform. |     | TheDWTmoduletransforms |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------- | --- | ---------------------- | --- | --- |
Figure2presentstheoverallarchitectureofFUSION,whichcon-
|     |     |     |     |     |     |     | featurevectors𝐻 | 𝑚𝑜𝑑𝑎𝑙 |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------------- | ----- | --- | --- | --- |
sistsof multimodaldataserialization,multimodalwavelet 𝑖 intomulti-scalefrequencyrepresentations
fusionandconditionaldiffusionnetwork.First,preprocessthe bybreakingdowninputsignalsintowavelets.Thisprocesscaptures
multimodaldata.Next,thesethreemodalitiesarecombinedinthe theoriginaldata’sfrequencyandtimecharacteristics.Asdepictedin
waveletdomainbasedonanattention-basedmechanism.Thethird Figure2(b),DWTcanbeperformedmultipletimes,andeachDWT
usesahigh-passfilterfandalow-passfiltergtodecomposeatime
stageistheintegrationofaU-structure-baseddenoisingprocess
|     |     |     |     |     |     |     | seriessignal𝐻 | 𝑚𝑜𝑑𝑎𝑙 |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------- | ----- | --- | --- | --- |
duringthediffusionphase.Thisenhancestheprecisionofthede- 𝑖 intodifferentresolutions.Theoutputsofthe
|     |     |     |     |     |     |     | high-passandlow-passfiltersatlayer𝑙aredenotedas𝑐𝐷 |     |     |     | and𝑐𝐴 |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------- | --- | --- | --- | ----- |
noisingandeffectivelycapturesthespatiotemporaldependencies 𝑙 𝑙,
𝑚𝑜𝑑𝑎𝑙
withinthemultimodaldata.Next,weelaborateonthesestages. respectively.𝑙 indicatesthe𝑙-thdecompositionand𝑐𝐴 =𝐻 .
0 𝑖
512

KDD’25,August3–7,2025,Toronto,ON,Canada KaiqiDing,YuanmuMa,ZijianSong,andKaiguiBian
|     |     | Trace |     |     |     | Log |     |     |     |     |     |     |     |     |     |
| --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Metric
|     |     |     |     |     | Info| login success.... |     |     | Variable Diffusion Length |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | ----------------------- | --- | --- | ------------------------- | --- | --- | --- | --- | --- | --- | --- |
Err | ***service refuse
Noise Schedule
......
|     | Time | ...... | Time |     | ...... Time |     | ...... |     |     |     |     |     |     |     |     |
| --- | ---- | ------ | ---- | --- | ----------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
Conditional Noise
|     |     |     |     |     |     |     |     | ...... |     |     | Predictor |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | --- | --------- | --- | --- | --- | --- |
Span3
|     |     |       |     |     | Net |      | Log3 | ...... |     |     |     |     |            |     |     |
| --- | --- | ----- | --- | --- | --- | ---- | ---- | ------ | --- | --- | --- | --- | ---------- | --- | --- |
|     |     | Span2 |     |     | Mem |      | Log2 |        |     |     |     |     |            |     |     |
|     |     | Span1 |     | CPU |     | Log1 |      |        |     |     |     |     | Condition: |     |     |
(a) Multimodal Serialization
......
|     |     | Approx.      |     | Pearson correlation |     |     |     |                   |     |     |                   | Up/Down Sample |     |     |     |
| --- | --- | ------------ | --- | ------------------- | --- | --- | --- | ----------------- | --- | --- | ----------------- | -------------- | --- | --- | --- |
|     |     |              |     |                     |     |     |     | ST-Residual Block |     |     | ST-Residual Block |                |     |     |     |
|     |     | coefficients |     |                     |     |     |     |                   |     |     | FC                |                |     |     |     |
Att.
Graph
|     | Node1 |     |     |     |     |     |     | ST-Residual Block |     | ST-Residual Block |     | Graph Conv |     |     |     |
| --- | ----- | --- | --- | --- | --- | --- | --- | ----------------- | --- | ----------------- | --- | ---------- | --- | --- | --- |
DWT
|     | ...... |     |     |      | IDWT |             |       |     |             |     |     | Layer Norm    |     |      |     |
| --- | ------ | --- | --- | ---- | ---- | ----------- | ----- | --- | ----------- | --- | --- | ------------- | --- | ---- | --- |
|     |        |     |     | Att. |      | Concatenate |       |     | ST-Residual |     |     |               |     |      |     |
|     |        |     | ... |      |      |             | Node1 |     |             |     |     | Temporal Conv |     | Date |     |
Block
......
|     |     | Detail |     |     |     |     |     |     |     |     |     |     | emb |     |     |
| --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Att.
|     |        | coefficients |     |     |     |     |        |     |     |     |     | Temporal Conv |     | Step |     |
| --- | ------ | ------------ | --- | --- | --- | --- | ------ | --- | --- | --- | --- | ------------- | --- | ---- | --- |
|     | Node N |              |     |     |     |     | Node N |     |     |     |     |               |     |      |     |
(b) Multimodal Wavenet Fusion (c) Conditional Diffusion Network
Figure2:TheoverviewtraininganddiagnosisframeworkofFUSION.(a)multimodaldataserialization:prepareforthefuture
graphstructure’sconstructionintotimeseries;(b)multimodalwaveletfusion:decomposemultimodaldataintowavelet
coefficients,whicharethenfusedviaPearsonCorrelation-BasedAttentiontoidentifysignificantfeatureswithinandacross
the modalities. (c) conditional diffusion model: model uncertainties with multi-scale temporal dependencies and spatial
correlationsenablingefficientnon-autoregressiveprediction.
|                     |     |     |     |     |     |     |     |       |        | 𝐹𝑖,x 𝐹𝑗)/(𝜎 |     |              | 𝐹𝑖,x | 𝐹𝑗)denotesthe |           |
| ------------------- | --- | --- | --- | --- | --- | --- | --- | ----- | ------ | ----------- | --- | ------------ | ---- | ------------- | --------- |
| Specifically,wehave |     |     |     |     |     |     |     | 𝑅     | =cov(x |             | 𝜎   | ),wherecov(x |      |               |           |
|                     |     |     |     |     |     |     |     | 𝐹𝑖,𝐹𝑗 |        | 𝑖 𝑖         | 𝐹𝑖  | 𝐹𝑗           | 𝑖    | 𝑖             |           |
|                     |     |     |     |     |     |     |     |       |        |             | x𝑖  | x𝑖           |      |               |           |
|                     |     |     |     |     |     |     |     |       |        |             |     | 𝐹 𝐹          |      |               | 𝑚 𝑜 𝑑 𝑎 𝑙 |
𝑇 𝑤 c o v a r ia n c e b e t w e e n v a r i a b le s 𝑖 a n d 𝑗 o f f e a t u r e m a t r i x H 𝑖
|     |     |     | ∑︁2 𝑙 − 1 |     |     |     | 𝑇   |     |     |     |     |     |     |     |     |
| --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
f[2𝑠−𝑚]cA𝑙−1 [𝑚], 𝑠 =1,···, 𝑤 fo r i n s ta n c e 𝑖 , 𝜎 i s t h e i r s ta n d a r d d e v ia t io n s o p e r a t i o n .
|     | cD𝑙 =f∗cA𝑙−1 | =   |       |     |     |     |     |                                                              |           |             |                  |            |             |                 |            |
| --- | ------------ | --- | ----- | --- | --- | --- | --- | ------------------------------------------------------------ | --------- | ----------- | ---------------- | ---------- | ----------- | --------------- | ---------- |
|     |              |     |       |     |     |     | 2 𝑙 | B a                                                          | s e d o n | t h e c o r | re l a t i o n m | a t ri x 𝑅 | , T h i s m | e c h a n i s m | l ea r n s |
|     |              |     | 𝑚 = 1 |     |     |     |     |                                                              |           |             |                  | 𝐹          | 𝑖, 𝐹 𝑗      |                 |            |
|     |              |     |       |     |     |     | (1) | theattentionweightsforeachwaveletcoefficientbetweenvariables |           |             |                  |            |             |                 |            |
𝑇𝑤
∑︁2𝑙−1
|     |              |     |              |     |      |           | 𝑇 𝑤 | throughtraining,dynamicallyintegratingthewaveletcoefficients |     |     |     |     |     |     |     |
| --- | ------------ | --- | ------------ | --- | ---- | --------- | --- | ------------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- |
|     | cA𝑙 =g∗cA𝑙−1 | =   | g[2𝑠−𝑚]cA𝑙−1 |     | [𝑚], | 𝑠 =1,···, |     |                                                              |     |     |     |     |     |     |     |
|     |              |     |              |     |      |           | 2𝑙  | ofothervariableswithitselftocomputeavectorthatincorporates   |     |     |     |     |     |     |     |
𝑚=1
informationfromothervariables.Theattentionweightsarelearned
where𝑇 representsthelengthof𝐻 𝑚𝑜𝑑𝑎𝑙 throughmodeltraining,enablingthemodeltomoreflexiblycapture
|                | 𝑤   |     |                                        |     | 𝑖 inawindowsize,the |     |     |        |             |            |               |               |                      |              |             |
| -------------- | --- | --- | -------------------------------------- | --- | ------------------- | --- | --- | ------ | ----------- | ---------- | ------------- | ------------- | -------------------- | ------------ | ----------- |
|                |     |     |                                        |     |                     |     |     | co m p | l e x d e p | en d e n c | ie s b e tw e | e n v a r iab | le s . S pe ci fi ca | lly , f or t | h e 𝑘 - t h |
| lengthchangeto |     | 𝑇 𝑤 | afterdecomposing𝑙−1timesand𝑠represents |     |                     |     |     |        |             |            |               |               |                      |              |             |
|                |     | 𝑙   |                                        |     |                     |     |     |        |             |            | ( 𝑘 )         |               |                      |              |             |
2 w a ve l e t c o e ffi c ie n t c D at t h e 𝑙 -t h la y e r ,w e l ea rn t h e at t e n ti o n
| thescale.Thechoiceoffiltersfandgisbasedonthewaveletbasis;  |     |     |     |     |     |     |     |          |         |                                           | 𝑙   |     |     |     |     |
| ---------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | -------- | ------- | ----------------------------------------- | --- | --- | --- | --- | --- |
|                                                            |     |     |     |     |     |     |     | weights𝛼 |         | betweenitandthewaveletcoefficientsofother |     |     |     |     |     |
| onceit’sdefined,theformsoffandgarealsodetermined.Thedetail |     |     |     |     |     |     |     |          | 𝐹𝑖,𝐹𝑗,𝑙 |                                           |     |     |     |     |     |
variablesthroughtraining.
coefficientscDcaptureshort-termtrendsandnuances,whilethe
approximatecoefficientscAindicatelong-termtrends.Moreover,
|                                                    |     |        |         |     |     |     |     |     |     |     | (cid:16) |                | (𝐹𝑗) | (cid:17) |     |
| -------------------------------------------------- | --- | ------ | ------- | --- | --- | --- | --- | --- | --- | --- | -------- | -------------- | ---- | -------- | --- |
|                                                    |     |        |         |     |     |     |     |     |     |     |          | Att(cD (𝐹𝑖),cD | )    |          |     |
| deeperdecompositionenhancesthefrequencyresolution. |     |        |         |     |     |     |     |     |     |     | exp      | 𝑙              | 𝑙    |          |     |
|                                                    |     | ,C , . | .. , ,C |     |     |     |     |     | 𝛼   | =   |          |                |      | ,        |     |
L e t C = { C 1 2 C 𝑙 𝑙+ 1 } r e p re s e n t t h e la y e r e d w a v el e t c o - 𝐹𝑖,𝐹𝑗,𝑙 𝐹 ′ (cid:16) (cid:17) (3)
|     |     |     |     |     |     |     |     |     |     |     | (cid:205) 𝑚 𝑜 𝑑𝑎𝑙 |     | (𝐹𝑖),cD (𝑚) |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | ----------- | --- | --- |
effi c ie n ts w h er e e a c h la y e r co n t ai n s e a c h v a r i ab le ’ s c o rr e sp o n d i n g 𝑚 = exp Att(cD 𝑙 𝑙 )
1
coefficients,denotedasfollows:
𝐹
(𝐹𝑚𝑜𝑑𝑎𝑙) 𝐹𝑚𝑜𝑑𝑎𝑙×𝑇 𝑤 w h e r e A tt (c D (𝐹 𝑖 ) ,c D ( 𝑗) ) i s a le a r n a b le w e ig h t fu n c t io n t ha t m e a -
|     | cD𝑙 = | [cD (1) ;...;cD |     | ] ∈R     | 𝑙        | , 𝑙 ∈ | [1,𝐿] |          |           | 𝑙         | 𝑙               |               |                   |            |           |
| --- | ----- | --------------- | --- | -------- | -------- | ----- | ----- | -------- | --------- | --------- | --------------- | ------------- | ----------------- | ---------- | --------- |
|     |       | 𝑙               | 𝑙   |          | 2        |       |       |          |           |           |                 |               |                   | 𝐹          | 𝐹         |
|     |       |                 |     |          |          |       | (2)   | su r e s | t he s tr | e n g t h | o f t h e c o r | re la t i o n | b et w e e n v ar | i a b le 𝑖 | a n d 𝑗 . |
|     |       |                 |     | (𝐹𝑚𝑜𝑑𝑎𝑙) | 𝐹𝑚𝑜𝑑𝑎𝑙×𝑇 | 𝑤     |       |          |           |           |                 |               |                   |            |           |
cA𝐿 = [cA (1) ;cA (2) ;...;cA ] ∈R 𝑙 Theattentionweight𝛼 𝐹𝑖,𝐹𝑗,𝑙 reflectstheimportanceofvariable𝐹 𝑖
|     |     | 𝐿   | 𝐿   | 𝐿   |     | 2   |     |             |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     |     |     |     | tovariable𝐹 |     | 𝑗.  |     |     |     |     |     |
3.2.2 FusionwithPearsonCorrelation-BasedAttention. Weintro- Next,weuseaweightedsumtointegratethewaveletcoefficients
| duceanattentionmechanismbasedonthePearsoncorrelation |     |     |     |     |     |     |     |     |     |     |     |     |     |     | (𝐹𝑖) |
| ---------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |
ofothervariableswithitself,computingthecontextvector𝒗𝑫
coefficienttocapturethecorrelationwithinandacrossthemodali- 𝑙
forvariable𝑘:
ties.First,wecomputethePearsoncorrelationcoefficientmatrix
| betweenthevariables𝑅 |     |     | ∈R𝐹𝑚𝑜𝑑𝑎𝑙×𝐹𝑚𝑜𝑑𝑎𝑙,ofwhich𝐹 |     |     |       |       |     |     |     |     |            |     |     |     |
| -------------------- | --- | --- | ------------------------ | --- | --- | ----- | ----- | --- | --- | --- | --- | ---------- | --- | --- | --- |
|                      |     |     |                          |     |     | 𝑚𝑜𝑑𝑎𝑙 | isthe |     |     |     |     | 𝐹′         |     |     |     |
|                      |     |     |                          |     |     |       |       |     |     |     |     | 𝑚 ∑︁𝑜 𝑑 𝑎𝑙 |     |     |     |
n u m b e r o f v a r i a b l e s. T h e Pe a r so n c o rr e la ti o n c o e ffi c i e nt m e a s u re s (𝐹𝑖) =cD (𝐹𝑖) + 𝛼 ·cD (𝑚).
|     |              |                    |          |               |                  |              |                   |     |     | 𝒗𝑫 𝑙 | 𝑙   |     | 𝐹𝑖,𝐹𝑗,𝑙 𝑙 |     | (4) |
| --- | ------------ | ------------------ | -------- | ------------- | ---------------- | ------------ | ----------------- | --- | --- | ---- | --- | --- | --------- | --- | --- |
| th  | e li n e a r | c o r r e l a t io | n b e tw | e e n v ar ia | b le s a n d i s | d e fi n e d | a sf o l lo w s : |     |     |      |     |     |           |     |     |
𝑚 = 1
513

EnhancingMicroservicesAnomalyDetectionviaMultimodalDataFusionintheWaveletDomainand
SpatiotemporalGraph-basedDiffusionProbabilisticModel KDD’25,August3–7,2025,Toronto,ON,Canada
𝐹 ′
(𝐹𝑖) isthecoefficientofvariable𝐹 𝑖itself,while(cid:205) 𝑚 𝑜 𝑑𝑎𝑙𝛼 𝐹𝑖,𝐹𝑗,𝑙· requireexecutingthereversediffusionprocess𝑇 timestopredict
| Here,cD | 𝑙   |     |     |     |     | 𝑚 = |     |     |     |     |     | 𝑝   |     |     |
| ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|         |     |     |     |     |     | 1   |     | 𝑇   |     |     |     |     |     |     |
(𝑚) representsthecontributionofvariables𝑚tovariable𝐹 th e fu t u r e 𝑝 s te p s , FU S I O N o n l y r e q u ir e s a si n g l e r e v e r s e d iff u -
| cD  | 𝑙   |     |     |     |     | 𝑖.  |              |                  |            |              |             |                |              |           |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ---------------- | ---------- | ------------ | ----------- | -------------- | ------------ | --------- |
|     |     |     |     |     |     |     | s io n p r o | c es s t o m a k | e it s p r | ed ic t i on | s . T h i s | a pp r o a c h | s i g n i fi | ca n tl y |
Finally,weconcatenatethecontextvectorsfromalllayersto
acceleratestheinferencespeed.
obtainthefeaturevectorrepresentingthemulti-scalefrequency:
(1) (𝐹𝑚𝑜𝑑𝑎𝑙) 𝐹𝑚𝑜𝑑𝑎𝑙×𝑇 𝑤 3 . 3. 2 Co n di ti o n a l G e ne r a t i on w ith U ne t -b a se d D e n o is i n gN et w o rk .
|     | vD𝑙 = [vD | ;...;vD | ] ∈R |     | 2 𝑙 , | 𝑙 ∈ [1,𝐿] |     |     |     |     |     |     |     |     |
| --- | --------- | ------- | ---- | --- | ----- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
𝑙 𝑙 F U S ION e m p l o y s a n U n e t - b as ed ar ch it e ct u re i n t h e t e m po r al d i-
(5)
(1) (𝐹𝑚𝑜𝑑𝑎𝑙) 𝐹𝑚𝑜𝑑𝑎𝑙×𝑇 𝑤 mensiontocapturetemporaldependenciesatvariousgranular-
|     | vA𝐿 = [vA | ;...;vA | ] ∈R |     | 2 𝑙 |     |     |     |     |     |     |     |     |     |
| --- | --------- | ------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
𝐿 𝐿 ities and utilizes GNN to model the spatial correlations. In Fig-
weapplytheInverseDiscreteWaveletTransform(IDWT)tore-
ure2(c),weillustrateourdenoisingnetworkthatprocessesfive
|     |     |     |     |     |     |     |     | 𝑎𝑙 𝑙 | 𝑤𝑖𝑛 |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- |
constructtheircorrespondingsequenceinthetimedomain.The dynamicinputs:𝑥 𝑚 𝑒 𝑟𝑔𝑒,𝑥 𝑛 ,𝑛,G,and𝑇,producingaclearoutput
processcanbeformulatedasfollows: 𝜖. The process begins by combining𝑥 𝑤𝑖𝑛 ∈ R𝐹𝑚𝑜𝑑𝑎𝑙×𝑉×𝑇 with
𝑛
|     |     |     |     | ′★vD𝑙 | ′★vA𝑙 |     | 𝑥 𝑤 𝑖𝑛 ∈R𝐹𝑚𝑜𝑑𝑎𝑙×𝑉×𝑇 |     |     |     |     |     |     |     |
| --- | --- | --- | --- | ----- | ----- | --- | ------------------- | --- | --- | --- | --- | --- | --- | --- |
vA𝑙−1 =𝐼𝐷𝑊𝑇(vD𝑙 ,vA𝑙)=f +g (6) 𝑚 𝑒 𝑟𝑔𝑒 alongthetemporaldimension,resultingin
|        |      |                                         |     |     |     |       | a n ew te | n s o r, 𝑥 𝑤 𝑖 𝑛 ∈ | R 𝐹 𝑚 𝑜𝑑 | 𝑎 𝑙 × 𝑉 × 2 𝑇 | . T hi st | en s or is t | h en p r o | je ct e d |
| ------ | ---- | --------------------------------------- | --- | --- | --- | ----- | --------- | ------------------ | -------- | ------------- | --------- | ------------ | ---------- | --------- |
|        | ′    | ′ arethesynthesisversionsoffandg.Then,𝐻 |     |     |     | 𝑚𝑒𝑟𝑔𝑒 |           | (cid:101)𝑛         |          |               |           |              |            |           |
| wheref | andg |                                         |     |     |     | 𝑖 =   |           |                    |          |               | 𝑋 ∈       | R 𝐶 ×𝑉 ×     | 2 𝑇        |           |
vA0isthereconstructedtimeseriesofthe𝑖-thinstance. to a hig h e r -d im e n si on a l re p r e s en t a t io n us i n g a li n -
|     |     |     |     |     |     |     | earlayer,where𝐶 | istheprojecteddimension.𝑋 |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------------- | ------------------------- | --- | --- | --- | --- | --- | --- |
issubsequently
processedthroughSpatio-temporalResidualBlocks(ST-Residual
3.3 ConditionalDiffusionNetwork
Blocks),designedtocapturetemporalandspatialdependencies.The
3. 3 .1 Fr a m e w o r k o f C o nd i ti on al D i ff u sio n M o d e l. A fte r o b t a in in g i n p u t t o th e 𝑘- t h bl o c k i s d e no te d a s 𝑋 ∈R𝐶×𝑉×𝑇 ,with𝑋 =𝑋,
| 𝑚   | 𝑒𝑟𝑔𝑒 |     |     |     |     |     |     |     |     |     | 𝑘   |     |     | 0   |
| --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
𝐻 a n d 𝐻 𝑚 𝑜 𝑑 𝑎𝑙 , w e c a n in te g r a te th e se t h r ee m o d a li t ie s to - 𝑇
𝑖 𝑖 r efl e c t i ng th e ti m e d i m e n s io n le n gt h .
getherbyconstructingamicroservicegraphtovirtuallyrepresent
|     |     |     |     |     |     |     | Temporal | Dependency |     | Modeling. | In  | Figure | 2(c), each | ST- |
| --- | --- | --- | --- | --- | --- | --- | -------- | ---------- | --- | --------- | --- | ------ | ---------- | --- |
thestatusandschedulingrelationshipsamongserviceinstancesof ResidualBlockprocessestheinput𝑋 𝑘 throughaTCN[22]tocap-
areal-worldmicroservicesystem.Inthisgraph,nodesrepresent ture temporal dependencies. This TCN uses a one-dimensional
serviceinstances,andedgesrepresentschedulingrelationshipsbe- gatedcausalconvolutionwithkernelsize𝐾 andpaddingtoensure
tweendifferentinstances.LetG={V,A}representagraphwith
theoutputmatchestheinputdimensions.Theconvolutionkernel
𝑉 nodes,whereVisthenodesetandA∈R𝑉×𝑉 isaweightedad- ∈R𝐾×𝐶 𝑡 ×𝐶 𝑡 inR𝐶 𝑡 ×𝑉×𝑇
|     |     |     |     |     |     |     | Γ 𝑇 | i n o ut maps𝑋 | 𝑘   | tooutputs𝑃 | 𝑖 and𝑄 | 𝑖   | o ut | .The |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ---------- | ------ | --- | ---- | ---- |
∈R𝐹𝑚𝑜𝑑𝑎𝑙×𝑉
jacencymatrixtodescribethegraphtopology.Letx𝑡 temporalgatedconvolutioncanbedefinedas:
denote𝐹 𝑚𝑜𝑑𝑎𝑙-dimensionalsignalsgeneratedbythe𝑖-thnodesat
ℎ
time𝑡.Givenhistoricalgraphsignalsx = [x1 ,···,x𝑇ℎ ]of𝑇 ℎtime Γ 𝑇(𝑋 𝑘)=𝑃 ⊙𝜎(𝑄 ∈R𝐶 𝑡 ×𝑉×𝑇,
|     |     |     |     |     |     |     |     |     | 𝑖   | 𝑖)  | o ut |     |     | (8) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- |
stepsandthegraphGasinputs,weaimsatlearningafunctionF
|                              |     |     | 𝑝                     |     |     |     | ⊙representstheHadamardproduct,and𝜎isthesigmoidactivation |     |     |     |     |     |     |     |
| ---------------------------- | --- | --- | --------------------- | --- | --- | --- | -------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
| topredictfuturegraphsignalsx |     |     | ,whichisformulatedas: |     |     |     |                                                          |     |     |     |     |     |     |     |
ℎ 𝑝, f u n cti o n . T h e t er m 𝜎 ( 𝑄 𝑖 ) is a g a t e t h a t fi l te r s re lev an t in f o r m a t io n
|     |     | F :(x ;G)→ | [x𝑇ℎ+1 ,···,x𝑇ℎ+𝑇𝑝 |     | ] :=x | (7) |            |                   |          |             |               |             |           |         |
| --- | --- | ---------- | ------------------ | --- | ----- | --- | ---------- | ----------------- | -------- | ----------- | ------------- | ----------- | --------- | ------- |
|     |     |            |                    |     |       |     | f ro m 𝑃 t | o t h e n e xt la | y e r .T | h e o u t p | u t o f t h e | T C N is de | n o t e d | a s 𝑋 . |
|     |     |            |                    |     |       |     | 𝑖          |                   |          |             |               |             |           | 𝑘       |
where𝑇 istheforecastinghorizon.Inthisstudy,wefocusonthe
|     | 𝑝   |     |     |     |     |     | Spatial | Dependency | Modeling. |     | Graph | Convolutional |     | Net- |
| --- | --- | --- | --- | --- | --- | --- | ------- | ---------- | --------- | --- | ----- | ------------- | --- | ---- |
taskofprobabilisticspatiotemporalgraph(STG)forecasting,which works(GCNs)areusedtoextractmeaningfulfeaturesinthespatial
aimstoestimatethedistributionoffuturegraphsignals. domain[22].Thegraphconvolutionisdefinedas:
TheoriginalDDPMisdesignedtogenerateimagesfromwhite
|     |     |     |     |     |     |     |     |     |     | (cid:16) (cid:16) | (cid:17) | (cid:17) |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | -------- | -------- | --- | --- |
noisewithoutanyconditions.However,thisapproachdoesnot Γ 𝐺(𝑋 𝑘)=𝜎 Φ 𝐴 ,𝑋 ,
|     |     |     |     |     |     |     |     |     |     |     | gcn 𝑘 | W𝑖  |     | (9) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- |
alignwithourtask,wherefuturesignalsaregeneratedbasedon
t h e ir h i s to r ic al d at a . T o a d d re s s t h i s f o r S T G f o re c as ti n g (S T G ), w e R𝐶 𝑔 ×𝐶 𝑔
|     |                |               |                           |             |           |                      | where W𝑖 | ∈ i n         | o ut is     | a trainable | parameter, | and𝜎          | is  | an ac- |
| --- | -------------- | ------------- | ------------------------- | ----------- | --------- | -------------------- | -------- | ------------- | ----------- | ----------- | ---------- | ------------- | --- | ------ |
| e x | te n d t h e D | D P M t o c r | ea t e a c o n d i t io n | a l v e rsi | o n b y m | a k in g s ev e ra l |          |               |             |             |            |               |     |        |
|     |                |               |                           |             |           |                      | tivation | function. The | aggregation |             | function   | Φ(·) combines |     | fea-   |
modificationstothereverseprocess.
|     |                                        |     |             |       | 𝑚𝑒𝑟𝑔𝑒 |            | tures from  | neighboring | nodes   | into | the target  | node.      | We use | the  |
| --- | -------------------------------------- | --- | ----------- | ----- | ----- | ---------- | ----------- | ----------- | ------- | ---- | ----------- | ---------- | ------ | ---- |
|     | Training.Giventhemultimodalfusiondata𝐻 |     |             |       |       | ,construct |             |             |         |      |             |            |        |      |
|     |                                        |     |             |       | 𝑖     |            | vanilla GCN | [27], which | defines |      | a symmetric | normalized |        | sum- |
|     |                                        |     | w i n [ , · | · · , | ]     |            |             |             |         |      |             |            |        |      |
t h e o b s e r v e d v a l u e s x m e r g e = x 1 x 𝑇 ℎ + 𝑇 𝑝 i n t i m e w i n d o w (cid:16) (cid:17)
|     |     |     |     |     |     |     | m a t i o n f | u n c t i o n a s | : Φ | 𝐴 , 𝑋 | = 𝐴 | 𝑋 , w | h e r e 𝐴 | =   |
| --- | --- | --- | --- | --- | --- | --- | ------------- | ----------------- | --- | ----- | --- | ----- | --------- | --- |
𝑇 + 𝑇 𝑝 f o r n od e 𝑖 . T h u s , t h e c o n d i t i o n i s 𝑥 w i n , g r a p h G , a n d t h e g c n g c n 𝑘 g c n 𝑘 g c n
| ℎ   |     |     |     | m e | r√ g e | √   |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
𝑥 w i n 𝑥 w i n 𝛼 𝑥 w i n 𝛼 𝜖 𝐷 − 1 (𝐴 + 𝐼 ) 𝐷 − 1 ∈ R 𝑉 × 𝑉 is t h e n o r m a l iz e d a d j a c e n c y m a t r i x o f
| t a r | g e t | , w e s a m p l e | n o i se t a r g e t s | 𝑛 = | 𝑛   | + 1 − 𝑛 , | 2   | 2   |     |     |     |     |     |     |
| ----- | ----- | ----------------- | ---------------------- | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
|       | 0     |                   |                        |     | 0   |           |     | 𝐼   |     |     | 𝐷   |     |     |     |
a n d t h e n t r a i n 𝜖 𝜃 u s i n g t h e l o s s f u n c t i o n d e fi n e d i n E q u a ti o n ? ? . T h e gr a p h G . H e r e , is t h e i d e n t i ty m a tr i x a n d is th e d i a g o n al d e g re e
|                                                             |     |     |     |     |     |     | matrixwith𝐷 |      | (cid:205) 𝑗(𝐴+𝐼)𝑖𝑗.WealsoreshapetheTCNlayer |     |     |     |     |     |
| ----------------------------------------------------------- | --- | --- | --- | --- | --- | --- | ----------- | ---- | ------------------------------------------- | --- | --- | --- | --- | --- |
| lossfunctionintegratesthereconstructionofhistoricaldatawith |     |     |     |     |     |     |             | 𝑖𝑖 = |                                             |     |     |     |     |     |
futureestimations,maximizingtheuseofhistoricalinformation outputinto𝑋 R𝑉×𝐶 𝑔 n,where𝐶 𝑔 𝑇 ×𝐶 𝑡
|     |     |     |     |     |     |     |     | 𝑘 ∈ | i   |     | =   | 𝑖 ,andfeedthis |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | --- |
|     |     |     |     |     |     |     |     |     |     |     | in  | o ut           |     |     |
foreffectivedatadistributionmodeling.Additionally,itprovidesa featureintotheGCN.
unifiedframeworkforarangeofspatiotemporalgraph(STG)tasks, DiffusionStepsEmbedding.FUSIONutilizestherandomness
suchasprediction,generation,andinterpolation[21]. ofdiffusionsteps,whichenhancesthemodel’sgenerativeabili-
Inference.Theinferenceprocessemploysthetraineddenoising
ties,diversity,androbustness,especiallywithcomplexandnoisy
| function𝜖 |     | tosample𝑥 | w in stepbystepaccordingtoEquation(13), |     |     |     |     |     |     |     |     |     |     |     |
| --------- | --- | --------- | --------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
𝜃 𝑛 − 1 datasets.Tooptimizeperformance,weincorporatediffusionsteps
undertheguidanceof𝑥win
andG.Itisimportanttonotethat, asauxiliaryinformation,usingpositionalencodingtorepresentthe
merge
unlikepreviousdiffusion-basedmodelslikeTimeGrad[21],which noiselevel𝑛∈ [1,𝑁]andprocessitthroughtransformerpositional
514

KDD’25,August3–7,2025,Toronto,ON,Canada KaiqiDing,YuanmuMa,ZijianSong,andKaiguiBian
| embedding. |     |          |     |                   |          |          |           | Table2:Basicinformationaboutthreedatasets. |     |     |     |     |     |     |     |
| ---------- | --- | -------- | --- | ----------------- | -------- | -------- | --------- | ------------------------------------------ | --- | --- | --- | --- | --- | --- | --- |
|            |     | (cid:20) |     | (cid:18) (cid:19) | (cid:18) | (cid:19) | (cid:21)𝑇 |                                            |     |     |     |     |     |     |     |
|            |     |          |     | 𝑛                 | 𝑛        |          |           |                                            |     |     |     |     |     |     |     |
𝐷𝑠(𝑛)= ...,cos ,sin ,... , (10) DataFailuretype CasesPercentDataFailuretype CasesPercent
|     |     |     |     | 𝑟−2 𝑑 | 𝑟−2 | 𝑑   |     |                |     |     |        |              |     |     |        |
| --- | --- | --- | --- | ----- | --- | --- | --- | -------------- | --- | --- | ------ | ------------ | --- | --- | ------ |
|     |     |     |     | 𝐷     |     | 𝐷   |     | Filesystemread |     | 21  | 12.07% | Networkdelay |     | 42  | 29.37% |
where𝑑 =1,···,𝐷/2isthedimensionoftheembedding(typically Filesystemwrite 14 8.05% NS Networkloss 47 32.87%
setto32),and𝑟 2202SPOIA Networkdelay 19 10.92% CPUstress 54 37.76%
isalargeconstant(e.g.,10000).Thisembedding
|     |     |     |     |     |     |     |     | Networkcorruption |     | 20  | 11.49% | CPUoverload |     | 26  | 9.81% |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | --- | ------ | ----------- | --- | --- | ----- |
methodcapturesthestochasticityofthediffusionstepsandincor- Networkduplicate 23 13.22% Memorystress 19 7.17%
poratesitasaconditionalinputtothemodel,therebyenhancing Networkdroppacket 26 14.94% Highdisk 24 9.06%
|     |     |     |     |     |     |     |     | CPUload |     | 20  | 11.49% | Diskpartitionfull |     | 36  | 13.58% |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | ------ | ----------------- | --- | --- | ------ |
itsgenerativecapabilityanddiversity.
|                                                   |     |     |     |     |     |     |     | Memoryload     |     | 19  | 10.92% | I/Olatency      |     | 23  | 8.68% |
| ------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | --- | ------ | --------------- | --- | --- | ----- |
| RelativeTimeEmbedding.Weintroducearelativetimeem- |     |     |     |     |     |     |     |                |     |     | SMM    |                 |     |     |       |
|                                                   |     |     |     |     |     |     |     | Containerpause |     | 12  | 6.90%  | Databasefailure |     | 14  | 5.28% |
beddingtechniquetoaddressirregulartimeintervals.Thistech- loginfailure 527 47.95% Resourceexhaustion 38 14.34%
|                                                          |     |     |     |     |     |     |     | Memoryanomalies   |     | 505 | 45.95% | Highpacketloss      |     | 22  | 8.30% |
| -------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | --- | ------ | ------------------- | --- | --- | ----- |
| niquecapturestherelativetemporalrelationshipsbetweentime |     |     |     |     |     |     |     | AIAG              |     |     |        |                     |     |     |       |
|                                                          |     |     |     |     |     |     |     | Filemovingprogram |     | 36  | 3.28%  | Networkpartitioning |     | 18  | 6.79% |
serieselementsthroughmulti-resolutionembeddings(days,hours,
|     |     |     |     |     |     |     |     | Memoryfreedlabel |     | 16  | 1.46% | HardwareFailures |     | 32  | 12.08% |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | --- | ----- | ---------------- | --- | --- | ------ |
minutes).Specifically,thecomprehensiveembeddingofatimese- Accessdenied 15 1.36% ConfigurationErrors 13 4.91%
rieselementisrepresentedas:
|     |     | 𝑇𝑒(𝑡)=𝐸 | 𝐷(𝑡𝑑 | )+𝐸 𝐻(𝑡ℎ | )+𝐸 | 𝑀(𝑡𝑚 |      |                                               |     |     |     |     |                 |     |     |
| --- | --- | ------- | ---- | -------- | --- | ---- | ---- | --------------------------------------------- | --- | --- | --- | --- | --------------- | --- | --- |
|     |     |         |      |          |     | )    | (11) | distributionfromthetrainedmodel,i.e.,getting𝑃 |     |     |     |     | 𝑠 samples,wecan |     |     |
𝑡𝑑 𝑡ℎ 𝑡𝑚 reducethenumberofreversediffusionprocessesfrom𝑃 to𝑃 𝑠/𝛼.
| where | days | , hours | ,   | and minutes |     | can | be calculated |     |     |     |     |     |     | 𝑠   |     |
| ----- | ---- | ------- | --- | ----------- | --- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
𝑡, 𝐸 (cid:104) (cid:16) 2𝜋𝑡𝑑(cid:17) ,cos (cid:16) 2𝜋𝑡𝑑(cid:17)(cid:105) 𝐸 We utilize the Continuous Ranked Probability Score (CRPS)
| from | respectively. |     | 𝐷   | = sin |     |     | , 𝐻 = |     |     |     |     |     |     |     |     |
| ---- | ------------- | --- | --- | ----- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
365 365 [13]astheabnormalscoreforeachinstanceduringthetesting
| (cid:104) (cid:16) | 2𝜋𝑡ℎ(cid:17) | (cid:16) 2𝜋𝑡ℎ(cid:17)(cid:105) |     | (cid:104) | (cid:16) 2𝜋𝑡𝑚(cid:17) |     | (cid:16) 2𝜋𝑡𝑚(cid:17)(cid:105) |     |     |     |     |     |     |     |     |
| ------------------ | ------------ | ------------------------------ | --- | --------- | --------------------- | --- | ------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- |
sin ,cos and𝐸 = sin ,cos rep- process.CRPSquantifiesthedegreeofcompatibilitybetweena
|     | 365 | 365 |     | 𝑀   | 365 |     | 365 |            |              |          |       |     |        |              |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------------ | -------- | ----- | --- | ------ | ------------ | --- |
|     |     |     |     |     |     |     |     | cumulative | distribution | function | (CDF) | 𝐹   | and an | observation𝑥 |     |
resenttheembeddingfunctionsfordays,hours,andminutes.This
|     |     |     |     |     |     |     |     | for each modal | data | serialization | and | is  | calculated | as  | (𝐹,𝑥) = |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | ---- | ------------- | --- | --- | ---------- | --- | ------- |
embeddingapproachcapturestheperiodicnatureoftimewhilepre-
|     |     |     |     |     |     |     |     | ∫ (𝐹(𝑧) −I{𝑥 | ≤   | 𝑧})2d𝑧. |     |     | of𝑖-instance |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ------- | --- | --- | ------------ | --- | --- |
servingitsrelativeaspects,allowingthemodeltobetterunderstand R The abnormal score can
becalculatedbysummingthe(𝐹,𝑥)ofthreemodalities[6],result-
complextemporalrelationshipsintimeseriesdataandenhancing
|                           |                   |     |     |     |     |     |     | ingin𝐹ˆ                                                | (𝑡)foreachtimepoint.Thefindingsaresubsequently |     |                     |     |     |     |     |
| ------------------------- | ----------------- | --- | --- | --- | --- | --- | --- | ------------------------------------------------------ | ---------------------------------------------- | --- | ------------------- | --- | --- | --- | --- |
| itsanalyticalperformance. |                   |     |     |     |     |     |     | sum                                                    |                                                |     |                     |     |     |     |     |
|                           |                   |     |     |     |     |     |     | calculatedastheaverageoverthepredictionhorizon.𝐴𝑏𝑆𝑐𝑜𝑟𝑒 |                                                |     |                     |     |     |     | =   |
|                           |                   |     |     |     |     |     |     | E (cid:104) (cid:16)                                   | 𝐹ˆ (𝑡),(cid:205)                               | 𝐷 𝑥 | (cid:17)(cid:105) . |     |     |     |     |
| 3.4                       | AnomalyEvaluation |     |     |     |     |     |     | 𝑡 CRPS                                                 | sum                                            | 𝑖   | 𝑖,𝑡                 |     |     |     |     |
=1
Anomaliesareobservationsthatdeviatefromexpectedpatterns
Inpracticalfaultprediction,toobtainthereconstructedhistorical
values and future predictions, we sample the 𝑃 𝑠 data from the inhistoricaldata.Theyoccurwhentheexpectedconditionaldis-
tributionprobabilityofapredictionlength𝑇
probabilitydistributioninthereversepredictionprocessofthe 𝑝 significantlydiffers
diffusionmodelover𝑃 𝑠/𝛼steps.Weemployasamplingacceleration fromtheactualvalue.FUSIONcalculatestheanomalyseverityus-
ingtheAbScore.Totriggerananomalyevent,it’scrucialtoselecta
strategytoenhancethisprocess’sefficiency.
Usingalargenumberofdiffusionsteps𝑁 (e.g.,𝑁 threshold.Inthisstudy,weuseanon-parametric,dynamicunsuper-
=1000[10])
helpstheforwardprocessapproximateaGaussiandistribution, visedthresholdselectionmethod(NDT)asintroducedin[12].NDT
firstcreatesthesetegivenasetofabnormalscores𝑠ofhistorical
whichisusefulforthereversedenoisingprocess.However,ahigh
𝑁 canleadtoinefficientsamplingduetotheneedtoexecuteall observations,where𝑧isanorderedsetofpositivevalues.
iterationssequentially.Toimproveefficiency,weadopttheselective
|                                                |     |     |     |     |     |     |        |     |     | e=𝜇(𝑠)+z𝜎(𝑠). |     |     |     |     | (13) |
| ---------------------------------------------- | --- | --- | --- | --- | --- | --- | ------ | --- | --- | ------------- | --- | --- | --- | --- | ---- |
| samplingstrategyfrom[33],whichsamplesasubset{𝜏 |     |     |     |     |     |     | ,···,𝜏 |     |     |               |     |     |     |     |      |
|                                                |     |     |     |     |     |     | 1 𝑀}   |     |     |               |     |     |     |     |      |
of𝑀diffusionsteps.Theacceleratedsamplingprocessisdefined Then,thethreshold𝑇ℎiscalculatedby
asfollows:
(Δ𝜇(𝑠)/𝜇(𝑠))+(Δ𝜎(𝑠)/𝜎(𝑠))
|     |     |     |     |     |     |     |     | 𝑇ℎ=𝑎𝑟𝑔𝑚𝑎𝑥(e)= |     |     |     |     |     |     | (14) |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | --- | --- | --- | --- | --- | ---- |
2
|     |     |     | 𝑥   | −√︁  | 𝛼 𝜖  | (𝜏𝑚) |     |     |     |     |     | |s𝑎|+|E𝑠 | 𝑒𝑎| |     |     |
| --- | --- | --- | --- | ---- | ---- | ---- | --- | --- | --- | --- | --- | -------- | --- | --- | --- |
|     |     | √   |     | 𝜏𝑚 1 | − 𝜏𝑚 | 𝜃    |     |     |     |     |     |          |     |     |     |
𝑥 = 𝛼 (cid:169) √ (cid:170) where Δ𝜇(𝑠) = 𝜇(𝑠) −𝜇(𝑠 < 𝑇ℎ) and Δ𝜎(𝑠) = 𝜎(𝑠) −𝜎(𝑠 <
|     | 𝜏𝑚−1 |     | 𝜏𝑚−1 (cid:173) |     | 𝛼   | (cid:174) |     |     |     |     |     |     |     |     |     |
| --- | ---- | --- | -------------- | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
𝜏𝑚 (12) 𝑇ℎ),NDTalsoconsiderspreventinggeneratingalargenumberof
|     |     |     | (cid:171) |      |      | (cid:172) |      |                   |     | ={𝑠 | >𝑇ℎ}andanomaloussequences|E𝑠 |     |     |     | 2    |
| --- | --- | --- | --------- | ---- | ---- | --------- | ---- | ----------------- | --- | --- | ---------------------------- | --- | --- | --- | ---- |
|     |     | √︃  |           |      | (𝜏𝑚) |           |      | anomalousvaluess𝑎 |     |     |                              |     |     |     | 𝑒𝑎|. |
|     |     | +   | 1−𝛼 𝜏𝑚−1  | −𝜎 𝜏 | 2 ·𝜖 | +𝜎 𝜏𝑚     | 𝜖 𝜏𝑚 |                   |     |     |                              |     |     |     |      |
𝑚 𝜃 NDTaimstoidentifyathresholdthatresultsinthemostsignificant
𝜖 ∼ N(0,𝐼) denotesindependentstandardGaussiannoisere- decrease in the average and variability of s by eliminating any
𝜏𝑚
| latedto𝑥 | 𝑛,whiletheparameter𝜎 |     |     |     |     |     |     | valuesoverthethreshold. |     |     |     |     |     |     |     |
| -------- | -------------------- | --- | --- | --- | --- | --- | --- | ----------------------- | --- | --- | --- | --- | --- | --- | --- |
𝜏𝑚 governsthestochasticnature
|                                 |     |     |     |     | √︃  |            | √︃         |              |     |     |     |     |     |     |     |
| ------------------------------- | --- | --- | --- | --- | --- | ---------- | ---------- | ------------ | --- | --- | --- | --- | --- | --- | --- |
| ofthedenoisingprocess.Wedefine𝜎 |     |     |     |     | =   | 1 − 𝛼 𝑛 −1 | 1− 𝛼 𝑛 for |              |     |     |     |     |     |     |     |
|                                 |     |     |     |     | 𝑛   | 1 − 𝛼      | 𝛼          | 4 Evaluation |     |     |     |     |     |     |     |
|                                 |     |     |     |     |     | 𝑛          | 𝑛 −1       |              |     |     |     |     |     |     |     |
alldiffusionstepstocomplywiththeDenoisingDiffusionProb-
4.1 ExperimentSetting
abilisticModel(DDPM).Whenthesamplingtrajectorylengthis
muchshorterthan𝑁,computationalefficiencyincreasessignifi-
|                                     |     |     |     |     |                |     |          | 4.1.1 Dataset.                                           | Weconductedexperimentalresearchonbothopen- |     |     |     |     |     |     |
| ----------------------------------- | --- | --- | --- | --- | -------------- | --- | -------- | -------------------------------------------------------- | ------------------------------------------ | --- | --- | --- | --- | --- | --- |
| cantly.Moreover,thedatafromthelast𝛼 |     |     |     |     | reversesteps,𝑥 |     | win(with |                                                          |                                            |     |     |     |     |     |     |
|                                     |     |     |     |     |                |     | 𝑖        | sourcedatasetsanddatasetsgeneratedfromreal-worldsystems. |                                            |     |     |     |     |     |     |
𝑖 ∈ {1,...,𝑃 𝑠/𝛼}),providesagoodapproximationofthetarget, Open-source Microservice System: We utilize three open-
improvingoverallapproximationquality.Thus,toestimatethedata sourcemicroservicebenchmarks,namelyAIOPS2022[4],Generic
515

EnhancingMicroservicesAnomalyDetectionviaMultimodalDataFusionintheWaveletDomainand
SpatiotemporalGraph-basedDiffusionProbabilisticModel KDD’25,August3–7,2025,Toronto,ON,Canada
Table3:TheeffectivenessofFUSIONincomparisonwithdifferentmethodsonthreedatasets.
AIOps2022 GAIA SN MMS
Approach
Precision Recall F1-score Precision Recall F1-score Precision Recall F1-score Precision Recall F1-score
TraceVAE 0.423 0.406 0.414 0.411 0.396 0.403 0.532 0.511 0.521 0.375 0.321 0.346
DeepTraLog 0.689 0.652 0.670 0.715 0.694 0.704 0.721 0.706 0.713 0.521 0.503 0.512
Hades 0.712 0.694 0.703 0.728 0.719 0.723 0.733 0.724 0.728 0.534 0.521 0.527
MADMM 0.727 0.731 0.729 0.749 0.758 0.753 0.754 0.763 0.758 0.563 0.544 0.553
MISP 0.758 0.736 0.747 0.772 0.761 0.766 0.786 0.767 0.776 0.594 0.547 0.570
AnoFusion 0.783 0.769 0.776 0.794 0.785 0.789 0.784 0.752 0.768 0.694 0.708 0.701
Medicine 0.808 0.793 0.800 0.814 0.797 0.805 0.817 0.804 0.810 0.727 0.711 0.719
Triple 0.843 0.829 0.836 0.854 0.832 0.843 0.918 0.907 0.912 0.827 0.815 0.821
MSTGAD 0.932 0.918 0.925 0.921 0.927 0.924 0.952 0.938 0.945 0.857 0.831 0.844
FUSIONw/oWavelet 0.842 0.834 0.838 0.863 0.873 0.868 0.896 0.872 0.884 0.778 0.763 0.770
FUSIONw/oTemporal 0.724 0.713 0.718 0.734 0.727 0.730 0.718 0.704 0.711 0.657 0.621 0.638
FUSIONw/oSpatial 0.793 0.779 0.786 0.784 0.768 0.776 0.828 0.813 0.820 0.727 0.735 0.731
FUSIONw/oU-structure 0.648 0.618 0.633 0.692 0.682 0.687 0.739 0.716 0.727 0.618 0.603 0.610
FUSION 0.959 0.941 0.950 0.963 0.952 0.957 0.978 0.963 0.970 0.939 0.921 0.930
Table4:ComparisonofefficiencybetweenFUSIONanddifferentmethods.Trainingtime(Offline(min))andaveragetimeto
diagnoseafailurecase(Online(s)).
Dataset TraceVAE DeepTraLog Hades MADMM MISP Medicine AnoFusion Triple MSTGAD FUSION
Offline 19.25 77.28 39.00 34.45 112.46 43.91 106.96 47.80 68.32 41.23
AIOps2022
Online 8.41 148.15 10.52 14.38 193.71 15.11 184.91 18.96 21.01 14.22
Offline 17.42 68.26 28.91 24.63 109.00 31.45 97.06 32.61 54.98 29.75
GAIA
Online 6.51 125.71 5.68 7.03 164.41 10.45 157.60 14.64 17.30 11.61
Offline 5.06 56.57 8.30 14.16 87.49 17.73 82.25 19.83 46.58 20.68
SN
Online 1.21 118.95 2.38 4.89 134.88 6.59 125.10 8.10 10.23 6.17
Offline 26.23 89.36 49.47 58.90 148.97 64.12 137.01 69.63 78.67 65.45
MMS
Online 13.45 167.77 37.16 43.05 232.92 59.82 221.56 67.77 85.57 47.22
AIOpsAtlas(GAIA)[5],andSocialNetwork[9](SN,)whichhas Table5:PerformanceComparisonofFUSIONandBaseline
beenwidelyusedintheexistingwork[3,14,17,18,29].AIOPS2022
MethodsunderNoise𝜎 =0.1AcrossDifferentModalities.
isconstructedbyChinaConstructionBankbasedonhiptershop
system.GAIAiscollectedfromasystemutilizedbybothmobileand Metric_noise Log_noise Trace_noise
Approach
PCusers.SNisderivedfromanopen-sourcemicroservicesystem F1 Decrease F1 Decrease F1 Decrease
thatimplementsabroadcast-stylesocialnetworkingplatform. TraceVAE × × 0.331 -4.31%
Microservices-basedMailSystem: Thissystemisareal-world DeepTraLog × 0.469 -8.37% 0.434 -15.21%
mailsystem(MMS)with56microservicesinalargeInternetcom- Hades 0.468 -11.27% 0.471 -10.70% ×
panywithmorethantwomillionusers(partofitswholesystem). MADMM 0.477 -13.80% 0.492 -11.08% ×
MISP 0.493 -13.44% 0.502 -11.86% ×
Thetypicalfaultsincludethefollowing:CPUstress,memorystress,
AnoFusion 0.632 -9.83% 0.634 -9.55% 0.588 -16.11%
highdiskI/Olatency,diskpartitionfull,databasefailure,resource
Medicine 0.672 -6.53% 0.671 -6.66% 0.639 -11.12%
exhaustion,highpacketlossrate,etc. Triple 0.747 -9.01% 0.623 -24.11% 0.734 -10.59%
MSTGAD 0.809 -4.12% 0.722 -14.43% 0.774 -8.27%
4.1.2 Evaluation Metrics & Baselines. To evaluate the accuracy
FUSION 0.913 -1.82% 0.879 -5.48% 0.908 -2.36%
ofanomalydetection,followingthecommonpracticeinanomaly
detection[19,22,26,32],wechoosePrecision,Recall,andF1to
evaluatetheeffectivenessofanomalymethodsbasedonTP(True
Positive),FP(FalsePositive),andFN(FalseNegative). multimodalprocessingandfeatureextractionintheoriginalmethod
Tocomprehensivelyevaluatetheanomalydetectionperformance andreplacedthefinalfullyconnectedlayerwithanunsupervised
ofthemodel,weselectedninerepresentativebaselinesforcompar- clusteringapproach,thesameasDeepTraLog[30].
ison:TraceVAE[28],DeepTraLog[30],Hades[15],MADMM[26],
MISP[19],Medicine[25],AnoFusion[32],Triple[22]andMST- 4.1.3 ImplementationDetails. Asforhyperparameters,wesetthe
GAD[11].Itisimportanttonotethattheoriginalmethodissu- batchsizeas32andusetheAdamoptimizer.Inourmulti-resolution
pervisedintheMedicine[25]baseline.Weretainedthestepsfor analysisofmultimodaldatausingDWT,wechosetheHaar[16]
516

KDD’25,August3–7,2025,Toronto,ON,Canada KaiqiDing,YuanmuMa,ZijianSong,andKaiguiBian
Table6:PerformanceComparisonofFUSIONandBaseline NoiseAnalysis.FUSIONdemonstratesthebestperformance
MethodsunderNoise𝜎 =0.2AcrossDifferentModalities.
whendealingwithGaussiannoiseacrossvariousmodalities,high-
lightingitsrobustnessandeffectivenessinTable5and6.When
Metric_noise Log_noise Trace_noise noiseisaddedtotracedata,TraceVAErankssecondbestdueto
Approach
F1 Decrease F1 Decrease F1 Decrease itsabilitytocapturelatentstructuresanduncertainty,providing
TraceVAE × × 0.328 -5.18% noiserobustness.Incontrast,whennoiseaffectsmetricdata,MST-
DeepTraLog × 0.458 -10.52% 0.412 -19.51% GADperformssecondbest,leveragingitsspatio-temporalattention
Hades 0.448 -15.06% 0.462 -12.40% × andsemi-supervisedlearning.Additionally,Medicinemitigateslog
MADMM 0.439 -20.66% 0.483 -12.71% × noisebyassigningdifferentattentionweightstomodalities.FU-
MISP 0.423 -25.73% 0.479 -15.90% ×
SIONcombinesmultimodaldatainthewaveletdomain,integrating
AnoFusion 0.583 -16.82% 0.605 -13.69% 0.558 -20.39% featureswhilepreservinguniqueinformationfromeachmodality.
Medicine 0.613 -14.73% 0.645 -10.28% 0.613 -14.73%
Evenifonemodalityexperiencesnoiseorinterference,information
Triple 0.689 -16.07% 0.553 -32.64% 0.684 -16.68%
fromothermodalitiescanstillsupportaccurateanomalydetection
MSTGAD 0.751 -11.00% 0.698 -17.28% 0.745 -11.71%
FUSION 0.892 -4.08% 0.864 -7.09% 0.889 -4.40%
4.3 AblationStudy
We perform an ablation study using four datasets to assess the
waveletasthebasisfunctionandconductedathree-leveldecomposi- impactofeachcomponent.Wehavedevelopedfourvariantsof
tionofthetimeseriesdata,employinghigh-passandlow-passfilters FUSION and compared them to the full version of FUSION, as
toproduceapproximationanddetailcoefficientsatdifferentresolu- showninTable3.Thedistinctionsaredetailedbelow:
tions.Asforthediffusionnetwork,weadoptthefollowingquadratic
• w/oWavelet:Removethewaveletfusion.Themultimodalseri-
scheduleforvarianceschedule𝛽 𝑛 = (cid:16)𝑁 𝑁 − − 𝑛 1 √︁𝛽 1 + 𝑁 𝑛− − 1 1 √︁𝛽 𝑁 (cid:17)2 .We alizationisdirectlysenttothediffusionnetwork.
settheminimumnoiselevel𝛽
1
=0.0001andhiddensize𝐶 =96 • w/oTemporal:RemovetheTCNcomponentfromtheU-structure
andsearchthemaximumnumberofthediffusionstep𝑁 andthe withoutmodelingthetemporalcorrelation.
maximum noise level 𝛽 𝑁 from a given parameter space (𝑁 ∈ • w/oSpatial:RemovetheGNNcomponentfromtheU-structure
[50,100,200],and𝛽 𝑁 ∈ [0,1,0.2,0.3,0.4]),andeachmodel’sbest withoutmodelingthespatialcorrelation.
performanceisreportedintheexperiment.Thehistorylength𝑇 ℎ • w/oU-structure:RemovetheUnet-basedstructureanduseonly
andpredictionlength𝑇 𝑝 aresetto100and80foralldatasets. oneTCNforfeatureextraction.
The U-structure greatly influences model performance, with
4.2 PerformanceComparison
its removal leading to a notable decline. This highlights the U-
Weconductedexperimentscomparingmultiplebaselinemethods structure’sstrengthincapturingspatiotemporaldependencies.Ad-
acrossfourdatasets.AsshowninTable3,FUSIONoutperformed ditionally,neglectingeitherspatialortemporaldependencylearn-
allprobabilisticbaselines,improvingtheF1-scoreby2.70%,3.62%, ing significantly impacts performance, reinforcing the need to
2.70%,and10.21%ontherespectivedatasets.Bimodalmethodsusu- modelspatiotemporalcorrelations.Theremovalofwavelet-domain
allyunderperformduetotheirlimitedanalysisofmultimodaldata. featurefusionhasthemostsignificanteffectontheMMSdataset,as
AllapproachesperformedbestontheSNdataset,whichissimpler real-worldmodaldataissusceptibletonoiseorinterference.How-
andlowerindimensionality,whilethePMSdatasetshowedthe ever,waveletdomainmultimodaldatafusioneffectivelyintegrates
worstresultsduetoitscomplexityandnoise.MSTGADranked information,allowingthemodeltomaintainaccuracyinanomaly
secondonmostdatasetsduetoitssemi-supervisedlearningand detectionevenwhenonemodalityiscompromised.
attentionmechanisms,butFUSIONconsistentlyachievedthebest
performancebyeffectivelyextractingmultimodalfeaturesandin-
4.4 InterpretabilityofFailureDiagnosis
corporatinguncertaintythroughdiffusionmodels.
InferenceTime.Wecomparedthetraininganddetectiontimes WeillustratetheperformanceofFUSIONusingtheMMSdataset:
ofbaselinemodelsinTable3.TraceVAE,Hades,andMADMMare (1)Solutionstolimitation1.WevalidateFUSION’sabilityto
fasterduetoprocessingfewermodalities,whileMISPandAnoFu- learnfrommultiplemodalitiesbyvisualizingnetworkbytedistri-
sionanalyzemultimodaldata,resultinginlongertimes.DeepTra- butionsandspandurationsinFigure3(a).Evenwithnoiseinthe𝑇 ℎ
Log’sapproachoftrainingonindividualtracesbeforeanomaly timeseries,themodelretainsuniqueinformationfromeachmodal-
detectionalsoincreasestimeconsumption.Diffusion-basedmodels itythroughfrequency-domainfeaturefusion,ensuringthatifone
likeTimeGrad[21]andDDPM[10]areslowerbecauseoftheir modalityfails,theothersstillsupportanomalydetection.(2)Solu-
iterativedenoisingprocessbutshowpromisingperformance.Our tionstolimitation2.WecomparedFUSIONwithMSTGADusing
proposedFUSIONacceleratesbyusinganon-autoregressivear- theSTGCNframework.FUSIONoffersatighterpredictioninterval,
chitectureandrandomizeddiffusionsteps.Increasing𝛼 improves showninFigure3(b),indicatinggreaterreliabilityincapturingav-
efficiencywithoutcompromisingperformancewhen𝑃 𝑠 islarge. eragebehavioranddatavariability.Additionally,itmoreaccurately
WhileFUSIONmaynotsignificantlyspeedupcomparedtothe representsdatadistributionthanVAE-basedmodelslikeTraceVAE
modelsinTable3,itmeetstherequirementsforonlinediagnostics, inFigure3(c),thankstoitsdiffusionmodel’seffectivestep-by-step
showcasingitspotentialforpracticalapplications. denoisingprocessthatcapturescomplexmultimodalpatterns.(3)
517

EnhancingMicroservicesAnomalyDetectionviaMultimodalDataFusionintheWaveletDomainand
SpatiotemporalGraph-basedDiffusionProbabilisticModel KDD’25,August3–7,2025,Toronto,ON,Canada
0006
               N etw ork B ytes              Span duration 042 ST G C N O bservation  0042                 V A E -based   anom alies                  FU SIO N anom alies
0042                O bservation                   O bservation 0021             FU SIO N                    O bservation
|     |     |     |     |     |     |     |     |                 FU | SIO N | 0005 |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------ | ----- | ---- | --- | --- | --- |
)s( noitraud nap )s( noitraud nap 002 )s( noitraud nap                 O bservation )s( noitraud nap
| 0002 |     |     |     | )spb |     |     |     | 0012 |     |     | R econstruction  | P rediction |     |
| ---- | --- | --- | --- | ---- | --- | --- | --- | ---- | --- | --- | ---------------- | ----------- | --- |
0004
| 0061 |                    |     |     | 009     |     |     |     |      |     |      | of history | of future |     |
| ---- | ------------------ | --- | --- | ------- | --- | --- | --- | ---- | --- | ---- | ---------- | --------- | --- |
|      |                    |     |     | M( sety | 061 |     |     |      |     |      |            |           |     |
|      | N oisy historical  |     |     |         |     |     |     | 0081 |     | 0003 |            |           |     |
0021
|     | data |     |     | 006 B | 021 |     |     | S    |     | S    |     |     |     |
| --- | ---- | --- | --- | ----- | --- | --- | --- | ---- | --- | ---- | --- | --- | --- |
| S   |      |     |     |       | S   |     |     | 0051 |     | 0002 |     |     |     |
008
0001
|     |     |     |     | 003 | 08  |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
20 40 60 80 25 30 35 40 45 50 55 60 25 30 35 40 45 50 55 60 65 5 10 15 20 25 30 35 40 45 50
|     |     | T im e (m in) |     |     |     | T   | im e (m in) |     | T im e (m in) |     |     | T im e (m in) |     |
| --- | --- | ------------- | --- | --- | --- | --- | ----------- | --- | ------------- | --- | --- | ------------- | --- |
(a ) M o d a lity  c o rre la tio n  le a rn in g (b ) D e te rm in istic  v s. p ro b a b ilistic  m o d e ls (c ) D a ta  d istrib u tio n  c a p tu re  c o m p a riso n (d ) F a ilu re  d ia g n o sis c a p a b ility
Figure3:SuccessfulcasesofFUSIONinforecastingandanomalyevaluation.
|     |     | M A E |     |     | C R P S |     | F 1 |     |     |     |     |     |     |
| --- | --- | ----- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
19 0.4 0.93 afterwhichitdeclines.Optimalsizesvarybydataset:32forSN,
| 4.0 | 13.18 10.89 | 11.47 | 4 0.28 | 0.21 0.19 |     | 4 . 0.85 0.91 | 0.93 |                                                   |     |     |     |     |     |
| --- | ----------- | ----- | ------ | --------- | --- | ------------- | ---- | ------------------------------------------------- | --- | --- | --- | --- | --- |
|     |             | 17    | . 0    |           |     | 0             |      | 96forAIOPSandGAIA,and128forMMS(Figure4(b)).TheMMS |     |     |     |     |     |
| 3.0 |             |       | 3      |           | 0.3 | 3             | 0.89 |                                                   |     |     |     |     |     |
15.44 11.09 11.52 . 0 0.31 0.25 0.21 . 0 0.84 0.87 0.91 dataset requires a larger hidden layer due to its complexity. In
15
2.0 17.27 11.18 11.32 2 . 0.38 0.26 0.22 2 . 0.83 0.86 0.91 TCN,theconvolutionkernelsize(𝐾 = 2,3,4,5)affectstimestep
|     |     | 13  | 0   |     | 0.3 | 0   | 0.85 |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- |
1.0 1 1 coverage(Figure4(c)).Largerkernelscapturelongerdependencies
|     | 19.39 13.31 | 11.06 | . 0 0.41 | 0.27 0.24 |     | . 0 0.81 0.83 | 0.89 |     |     |     |     |     |     |
| --- | ----------- | ----- | -------- | --------- | --- | ------------- | ---- | --- | --- | --- | --- | --- | --- |
11 0.2 0.81 butincreasecomputation.For𝑁 =200and𝛽 =0.4,akernelsize
|     | 50 100 | 200 N             | 50        | 100           | 200 N           | 50            | 100 200 N |     |     |     |     | 𝑁   |     |
| --- | ------ | ----------------- | --------- | ------------- | --------------- | ------------- | --------- | --- | --- | --- | --- | --- | --- |
|     |        | (a ) T h e  e ffe | c t o f d | iffu sio n  s | te p s a n d  n | o ise  le v e | l         | of𝐾 |     |     |     |     |     |
=3isoptimalfortheMMSdataset.
| 5.0 |     |     | 00  |     | 12.5 |     | 0.4 1.0 |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | ---- | --- | ------- | --- | --- | --- | --- | --- | --- |
 AIOps    GAIA .1  AIOps    GAIA  M AE  CRPS  F1 Effectofhiddensizeandkernelsize.Theparameter𝛼issug-
| 4.0 |  SN |  M M S |     |  SN |  M M S 12.0 |     | 0.3 0.9 |     |     |     |     |     |     |
| --- | --- | ------ | --- | --- | ----------- | --- | ------- | --- | --- | --- | --- | --- | --- |
59 gestedtoimprovebothdiversityandperformanceinmodeltraining.
| SPRC 3.0 |     |     | S .0 |     | 11.5 |     |     |     |     |     |     |     |     |
| -------- | --- | --- | ---- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
PRC 11.0 0.2 0.8 AsshowninFigure4(d),increasingsamplesize𝑃 enhancesaccu-
| 2.0 |     |     | 09.0 |     |      |     |         |     |     |     |     | 𝑠   |     |
| --- | --- | --- | ---- | --- | ---- | --- | ------- | --- | --- | --- | --- | --- | --- |
|     |     |     |      |     | 10.5 |     | 0.1 0.7 |     |     |     |     |     |     |
1.0 racy,particularlybetweensizes20and30,withdiminishingreturns
|     |     |     |     |     | 10.0 |     |     | beyond40.Inreversediffusion,𝛼 |     |     |     |     |     |
| --- | --- | --- | --- | --- | ---- | --- | --- | ----------------------------- | --- | --- | --- | --- | --- |
58 32 64 96 128 156 K =2 K =3 K =4 K =5 0.0 0.6 affectsdiversityandefficiency.A
|     | 32 64H 96 | 128 156 | .0  |     |     | K ernel size |     |     |     |     |     |     |     |
| --- | --------- | ------- | --- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- |
idden size H idden size smaller𝛼 promotesgreaterdiversityanddataexploration,whilea
|     | (b  | ) T h e  e ffe | c t o f h id | d e n  siz e | (c  | ) T h e  e ffe | c t o f k e rn e l siz e |     |     |     |     |     |     |
| --- | --- | -------------- | ------------ | ------------ | --- | -------------- | ------------------------ | --- | --- | --- | --- | --- | --- |
0.45 larger𝛼 increasesefficiencybyprocessingfewersamples,which
|     |     |     | 24  |     | 2.0 |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
0.40 C R P S    a =1=2 22 M A E    a =1=2    a =1=2 T im e isusefulforquickpredictions.Figure4(d)compares𝛼 = 1and
|      |     |    a |     |     |    a 1.5 |    a |     |                              |     |     |         |             |     |
| ---- | --- | ---- | --- | --- | -------- | ---- | --- | ---------------------------- | --- | --- | ------- | ----------- | --- |
| 0.35 |     |      | 20  |     |          |      |     | 𝛼 = 2.Forlargersamplesizes(𝑃 |     |     | > 40),𝛼 | = 2matches𝛼 | = 1 |
|      |     |      | 18  |     | 1.0      |      |     |                              |     | 𝑠   |         |             |     |
| 0.30 |     |      | 16  |     |          |      |     |                              |     |     |         |             |     |
inperformancebutis1.5timesfaster.Forsmallersamplesizes,a
| 0.25 |       |           | 14             |               | 0.5           |         |           | smaller𝛼     |                                                  |     |     |     |     |
| ---- | ----- | --------- | -------------- | ------------- | ------------- | ------- | --------- | ------------ | ------------------------------------------------ | --- | --- | --- | --- |
|      |       |           | 12             |               |               |         |           |              | isadvisabletoenhancebothdiversityandperformance. |     |     |     |     |
| 0.20 |       |           |                |               | 0.0           |         |           |              |                                                  |     |     |     |     |
| 0    | 20 40 | 60 80 100 | 0 20           | 40 60         | 80 100        | 0 20 40 | 60 80 100 |              |                                                  |     |     |     |     |
|      | P     | s         |                | P s           |               |         | P s       |              |                                                  |     |     |     |     |
|      |       | (d        | ) T h e  e ffe | c t o f s a m | p lin g  stra | te g y  |           | 5 Conclusion |                                                  |     |     |     |     |

Thisstudyunderscoresthecriticalroleofmultimodaldataanalysis
Figure4:Theeffectofhyperparameters.
indiagnosinganomalieswithinmicroservices.Wedecomposeand
fusemultimodaldatainthewaveletdomain.We’vedevelopedan
Failurediagnosiscapability. ThemodelinFigure3(d)recon- attentionmechanismthatenhanceskeyfeaturesbasedonPear-
structshistoricaldataandpredictsfuturestates.Thisdualfunc- soncorrelationcoefficients.Thesecoefficientsarethenprocessed
tionalityfacilitatestracingfaultcauses,providesearlywarnings, and reconstructed into enhanced feature representations using
andsupportsinformedpreventivemaintenance,therebyenhancing IDWT.Weproposeaspatiotemporalgraph-basedDenoisingDif-
fusionProbabilisticModelthatintegratesspatiotemporallearning
systemreliabilityandoperationalefficiency.
withDDPM’suncertaintyquantificationtocapturespatiotempo-
4.5 HyperparametersSensitivity ralfeatures.FUSION,utilizingaU-structurearchitecture,captures
multi-scaletemporaldependenciesandmodelsspatialcorrelations
Effectofthediffusionnetworkhyperparameters.Weexplore
howthemaximumnumberofdiffusionsteps𝑁 withGraphNeuralNetworks.FUSION’snon-autoregressiveap-
andthemaximum
proachefficientlygeneratesmulti-horizonpredictions,enhancing
| noiselevel𝛽 |     | 𝑁 fromtheparameterspace(𝑁 |     |     |     | ∈{50,100,200},𝛽 | 𝑁 ∈ |     |     |     |     |     |     |
| ----------- | --- | ------------------------- | --- | --- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- |
{0,0.2,0.3,0.4})impactourresults.Increasingdiffusionstepsen- faultdiagnosisinmicroservices.Ourexperimentsshowthatthisap-
hancesgenerationqualitybutalsoraisescomputationalcostsand proacheffectivelydealswithcomplexdatapatternsandnoisefound
inreal-worldmicroserviceenvironments.FUSIONoffersastrong
trainingtime.Reducingstepsspeedsupprocessesbutmaycompro-
andefficientsolutionfordetectinganddiagnosinganomaliesby
misequality.Largernoiseincreasesrobustnessanddiversitybut
combiningdifferentdataanalysismethodsandadvancedmodeling,
introducesuncertainty,whilesmallernoiseimprovesstabilityand
qualitybutlimitsexploration.Figure4(a)showsthatwith𝑁 =50 leadingtomorereliableandscalablemicroserviceoperations.
| diffusionstepsand |     | 𝛽   | = 0.1,modelperformancedropssignifi- |     |     |     |     |     |     |     |     |     |     |
| ----------------- | --- | --- | ----------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
𝑁
Acknowledgments
cantlyduetoinsufficientsteps,leadingtoapoorapproximationof
theGaussiandistributionanddegradedperformance. ThisworkispartiallysponsoredbyNationalKeyR&DProgramof
Effectofhiddensizeandkernelsize.Experimentsshowthat ChinaunderGrant2022YFB3104200,NSFCU24A20235and62032003.
modelperformanceimproveswithhiddenlayersizeuptoapoint,
518

KDD’25,August3–7,2025,Toronto,ON,Canada KaiqiDing,YuanmuMa,ZijianSong,andKaiguiBian
References
[17] ZeyanLi,JunjieChen,RuiJiao,NengwenZhao,ZhijunWang,ShuweiZhang,
[1] T.Alsop.2019.Averagecostperhourofenterpriseserverdowntimeworldwidein YanjunWu,LongJiang,LeiqinYan,ZikaiWang,ZhekangChen,WenchiZhang,
2019.https://www.statista.com/statistics/753938/worldwide-enterprise-server- XiaohuiNie,KaixinSui,andDanPei.2021.PracticalRootCauseLocalizationfor
hourly-downtime-cost/. MicroserviceSystemsviaTraceAnalysis.In2021IEEE/ACM29thInternational
[2] GaodeChen,YuezihanJiang,RuiHuang,KuoCai,YunzeLuo,RuinaSun,Qi SymposiumonQualityofService(IWQOS).1–10.doi:10.1109/IWQOS52092.2021.
Zhang,HanLi,andKunGai.2024.MissingInterestModelingwithLifelongUser 9521340
BehaviorDataforRetrievalRecommendation.InProceedingsofthe33rdACM [18] PingLiu,HaowenXu,QianyuOuyang,RuiJiao,ZhekangChen,ShenglinZhang,
InternationalConferenceonInformationandKnowledgeManagement(Boise,ID, JiahaiYang,LinlinMo,JiceZeng,WenmanXue,andDanPei.2020.Unsupervised
USA)(CIKM’24).AssociationforComputingMachinery,NewYork,NY,USA, DetectionofMicroserviceTraceAnomaliesthroughService-LevelDeepBayesian
4390–4396. doi:10.1145/3627673.3680019 Networks.In2020IEEE31stInternationalSymposiumonSoftwareReliability
[3] JianChen,FaguiLiu,JunJiang,GuoxiangZhong,DishiXu,ZhuanglunTan,and Engineering(ISSRE).48–58.doi:10.1109/ISSRE5003.2020.00014
ShangsongShi.2023.TraceGra:Atrace-basedanomalydetectionformicroservice [19] XiantingLu,YunongWang,YuFu,QiSun,XuhuaMa,XudongZheng,andCheng
usinggraphdeeplearning.Comput.Commun.204,C(apr2023),109–117. doi:10. Zhuo.2024. MISP:AMultimodal-basedIntelligentServerFailurePrediction
1016/j.comcom.2023.03.028 ModelforCloudComputingSystems.InProceedingsofthe30thACMSIGKDD
[4] CloudWise.2022.InternationalAIOpsChallenge. http://iops.ai/ ConferenceonKnowledgeDiscoveryandDataMining(Barcelona,Spain)(KDD
[5] CloudWise.2023.GAIA-DataSet. https://github.com/CloudWise-OpenSource/ ’24).AssociationforComputingMachinery,NewYork,NY,USA,5509–5520.
GAIA-DataSet doi:10.1145/3637528.3671568
[6] Emmanuel de Bézenac, Syama Sundar Rangapuram, Konstantinos Benidis, [20] YunzeLuo,YuezihanJiang,YinjieJiang,GaodeChen,JingchiWang,Kaigui
MichaelBohlke-Schneider,RichardKurle,LorenzoStella,HilafHasson,Patrick Bian,PeiyiLi,andQiZhang.2025. OnlineItemCold-StartRecommendation
Gallinari,andTimJanuschowski.2020. Normalizingkalmanfiltersformulti- withPopularity-AwareMeta-Learning.InProceedingsofthe31stACMSIGKDD
variatetimeseriesanalysis.InProceedingsofthe34thInternationalConference ConferenceonKnowledgeDiscoveryandDataMiningV.1(TorontoON,Canada)
onNeuralInformationProcessingSystems(Vancouver,BC,Canada)(NIPS’20). (KDD’25).AssociationforComputingMachinery,NewYork,NY,USA,927–937.
CurranAssociatesInc.,RedHook,NY,USA,Article252,13pages. doi:10.1145/3690624.3709336
[7] ShuiguangDeng,HailiangZhao,BinbinHuang,ChengZhang,FeiyiChen,Yinuo [21] KashifRasul,CalvinSeward,IngmarSchuster,andRolandVollgraf.2021.Au-
Deng,JianweiYin,SchahramDustdar,andAlbertY.Zomaya.2024.Cloud-Native toregressiveDenoisingDiffusionModelsforMultivariateProbabilisticTime
Computing:ASurveyFromthePerspectiveofServices.Proc.IEEE112,1(2024), SeriesForecasting.InInternationalConferenceonMachineLearning. https:
12–46.doi:10.1109/JPROC.2024.3353855 //api.semanticscholar.org/CorpusID:231719657
[8] JacobDevlin,Ming-WeiChang,KentonLee,andKristinaToutanova.2019.BERT: [22] RuiRen,YangWang,FengruiLiu,ZhenyuLi,andGaogangXie.2023.Triple:The
Pre-trainingofDeepBidirectionalTransformersforLanguageUnderstanding.In InterpretableDeepLearningAnomalyDetectionFrameworkbasedonTrace-
Proceedingsofthe2019ConferenceoftheNorthAmericanChapteroftheAssociation Metric-LogofMicroservice.In2023IEEE/ACM31stInternationalSymposiumon
forComputationalLinguistics:HumanLanguageTechnologies,Volume1(Longand QualityofService(IWQoS).1–10.doi:10.1109/IWQoS57198.2023.10188773
ShortPapers),JillBurstein,ChristyDoran,andThamarSolorio(Eds.).Association [23] OlafRonneberger,PhilippFischer,andThomasBrox.2015.U-Net:Convolutional
forComputationalLinguistics,Minneapolis,Minnesota,4171–4186.doi:10.18653/ NetworksforBiomedicalImageSegmentation.InInternationalConferenceon
v1/N19-1423 MedicalImageComputingandComputer-AssistedIntervention.
[9] YuGan,YanqiZhang,DailunCheng,AnkithaShetty,PriyalRathi,NayanKatarki, [24] ErichSchubert,JörgSander,MartinEster,HansPeterKriegel,andXiaowei
ArianaBruno,JustinHu,BrianRitchken,BrendonJackson,KelvinHu,Meghna Xu.2017.DBSCANRevisited,Revisited:WhyandHowYouShould(Still)Use
Pancholi,YuanHe,BrettClancy,ChrisColen,FukangWen,CatherineLeung, DBSCAN. ACMTrans.DatabaseSyst.42,3,Article19(July2017),21pages.
SiyuanWang,LeonZaruvinsky,MateoEspinosa,RickLin,ZhonglingLiu,Jake doi:10.1145/3068335
Padilla,andChristinaDelimitrou.2019.AnOpen-SourceBenchmarkSuitefor [25] LeiTao,ShenglinZhang,ZedongJia,JinruiSun,MinghuaMa,ZhengdanLi,
MicroservicesandTheirHardware-SoftwareImplicationsforCloud&EdgeSys- YongqianSun,CanqunYang,YuzhiZhang,andDanPei.2024. GivingEvery
tems.InProceedingsoftheTwenty-FourthInternationalConferenceonArchitectural ModalityaVoiceinMicroserviceFailureDiagnosisviaMultimodalAdaptive
SupportforProgrammingLanguagesandOperatingSystems(Providence,RI,USA) Optimization.InProceedingsofthe39thIEEE/ACMInternationalConferenceon
(ASPLOS’19).AssociationforComputingMachinery,NewYork,NY,USA,3–18. AutomatedSoftwareEngineering(Sacramento,CA,USA)(ASE’24).Association
doi:10.1145/3297858.3304013 forComputingMachinery,NewYork,NY,USA,1107–1119. doi:10.1145/3691620.
[10] JonathanHo,AjayJain,andPieterAbbeel.2020.Denoisingdiffusionprobabilistic 3695489
models.InProceedingsofthe34thInternationalConferenceonNeuralInformation [26] P.Wang,X.Zhang,Z.Cao,etal.2024.MADMM:microservicesystemanomaly
ProcessingSystems(Vancouver,BC,Canada)(NIPS’20).CurranAssociatesInc., detectionviamulti-modaldataandmulti-featureextraction.NeuralComput&
RedHook,NY,USA,Article574,12pages. Applic36(2024),15739–15757.doi:10.1007/s00521-024-09918-1
[11] JunHuang,YangYang,HangYu,JianguoLi,andXiaoZheng.2024.TwinGraph- [27] ZhebinWu,LinShu,ZiyueXu,YaominChang,ChuanChen,andZibinZheng.
BasedAnomalyDetectionviaAttentiveMulti-ModalLearningforMicroservice 2022. RobustTensorGraphConvolutionalNetworksviaT-SVDbasedGraph
System.InProceedingsofthe38thIEEE/ACMInternationalConferenceonAuto- Augmentation.InProceedingsofthe28thACMSIGKDDConferenceonKnowledge
matedSoftwareEngineering(Echternach,Luxembourg)(ASE’23).IEEEPress, DiscoveryandDataMining(WashingtonDC,USA)(KDD’22).Associationfor
66–78. doi:10.1109/ASE56229.2023.00138 ComputingMachinery,NewYork,NY,USA,2090–2099. doi:10.1145/3534678.
[12] KyleHundman,ValentinoConstantinou,ChristopherLaporte,IanColwell,and 3539436
TomSoderstrom.2018.DetectingSpacecraftAnomaliesUsingLSTMsandNon- [28] ZheXie,HaowenXu,WenxiaoChen,WanxueLi,HuaiJiang,LiangfeiSu,
parametricDynamicThresholding.InProceedingsofthe24thACMSIGKDD HanzhangWang,andDanPei.2023. UnsupervisedAnomalyDetectionon
InternationalConferenceonKnowledgeDiscovery&DataMining(London,United MicroserviceTracesthroughGraphVAE.InProceedingsoftheACMWebConfer-
Kingdom)(KDD’18).AssociationforComputingMachinery,NewYork,NY,USA, ence2023(Austin,TX,USA)(WWW’23).AssociationforComputingMachinery,
387–395. doi:10.1145/3219819.3219845 NewYork,NY,USA,2874–2884. doi:10.1145/3543507.3583215
[13] AlexanderI.Jordan,FabianKruger,andSebastianLerch.2017. Evaluating [29] ZhengranZeng,YuqunZhang,YongXu,MinghuaMa,BoQiao,WentaoZou,
ProbabilisticForecastswithscoringRules.JournalofStatisticalSoftware(2017). QingjunChen,MengZhang,XuZhang,HongyuZhang,XuedongGao,Hao
https://api.semanticscholar.org/CorpusID:88515280 Fan,SaravanRajmohan,QingweiLin,andDongmeiZhang.2023. TraceArk:
[14] CherylLee,TianyiYang,ZhuangbinChen,YuxinSu,andMichaelR.Lyu.2023. TowardsActionablePerformanceAnomalyAlertingforOnlineServiceSystems.
Eadro:AnEnd-to-EndTroubleshootingFrameworkforMicroservicesonMulti- In2023IEEE/ACM45thInternationalConferenceonSoftwareEngineering:Software
sourceData.In2023IEEE/ACM45thInternationalConferenceonSoftwareEngi- EngineeringinPractice(ICSE-SEIP).258–269.doi:10.1109/ICSE-SEIP58684.2023.
neering(ICSE).1750–1762.doi:10.1109/ICSE48619.2023.00150 00029
[15] CherylLee,TianyiYang,ZhuangbinChen,YuxinSu,YongqiangYang,and [30] ChenxiZhang,XinPeng,ChaofengSha,KeZhang,ZhenqingFu,XiyaWu,
MichaelR.Lyu.2023.HeterogeneousAnomalyDetectionforSoftwareSystems QingweiLin,andDongmeiZhang.2022. DeepTraLog:Trace-LogCombined
viaSemi-supervisedCross-modalAttention.In2023IEEE/ACM45thInternational MicroserviceAnomalyDetectionthroughGraph-basedDeepLearning.In2022
ConferenceonSoftwareEngineering(ICSE).1724–1736.doi:10.1109/ICSE48619. IEEE/ACM44thInternationalConferenceonSoftwareEngineering(ICSE).623–634.
2023.00148 doi:10.1145/3510003.3510180
[16] LingLi,SiyuanDou,ZixinMu,BingYu,SifengZeng,andQiangRen.2025.Anoise [31] XuZhang,ChaoDu,YifanLi,YongXu,HongyuZhang,SiQin,ZeLi,Qingwei
reductionalgorithmforindustrialCTimagesincorporatingwaveletdenoising Lin,YingnongDang,AndrewZhou,SaravanakumarRajmohan,andDongmei
andguidedfiltering.InProceedingsofthe2024InternationalConferenceonArtificial Zhang.2021. HALO:Hierarchy-awareFaultLocalizationforCloudSystems.
IntelligenceofThingsandComputing(AITC’24).AssociationforComputing InProceedingsofthe27thACMSIGKDDConferenceonKnowledgeDiscovery&
Machinery,NewYork,NY,USA,143–148. doi:10.1145/3708282.3708309 DataMining(VirtualEvent,Singapore)(KDD’21).AssociationforComputing
Machinery,NewYork,NY,USA,3948–3958. doi:10.1145/3447548.3467190
519

EnhancingMicroservicesAnomalyDetectionviaMultimodalDataFusionintheWaveletDomainand
SpatiotemporalGraph-basedDiffusionProbabilisticModel KDD’25,August3–7,2025,Toronto,ON,Canada
[32] ChenyuZhao,MinghuaMa,ZhenyuZhong,ShenglinZhang,ZhiyuanTan,Xiao andDataMining(LongBeach,CA,USA)(KDD’23).AssociationforComputing
Xiong,LuLuYu,JiayiFeng,YongqianSun,YuzhiZhang,DanPei,QingweiLin,and Machinery,NewYork,NY,USA,5639–5649. doi:10.1145/3580305.3599902
DongmeiZhang.2023.RobustMultimodalFailureDetectionforMicroserviceSys-
tems.InProceedingsofthe29thACMSIGKDDConferenceonKnowledgeDiscovery
520