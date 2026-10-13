A Survey of AIOps Methods for Failure Management
PAOLONOTARO,ChairofComputerArchitectureandParallelSystems,TechnicalUniversityofMunich,
GermanyandHuaweiMunichResearchCenter,Germany
JORGE CARDOSO, Department of Informatics Engineering/CISUC, University of Coimbra, Portugal
andHuaweiMunichResearchCenter,Germany
MICHAELGERNDT,ChairofComputerArchitectureandParallelSystems,TechnicalUniversity
ofMunich,Germany
Modern society is increasingly moving toward complex and distributed computing systems. The increase
inscaleandcomplexityofthesesystemschallengesO&Mteamsthatperformdailymonitoringandrepair
operations,incontrastwiththeincreasingdemandforreliabilityandscalabilityofmodernapplications.For
thisreason,thestudyofautomatedandintelligentmonitoringsystemshasrecentlysparkedmuchinterest
acrossappliedITindustryandacademia.ArtificialIntelligenceforITOperations(AIOps)hasbeenproposed
totacklemodernITadministrationchallengesthankstoMachineLearning,AI,andBigData.However,AIOps
asaresearchtopicisstilllargelyunstructuredandunexplored,duetomissingconventionsincategorizing
contributionsfortheirdatarequirements,targetgoals,andcomponents.Inthiswork,wefocusonAIOps
forFailureManagement(FM),characterizinganddescribing5differentcategoriesand14subcategoriesof
contributions, based on their time intervention window and the target problem being solved. We review
100FMsolutions,focusingonapplicabilityrequirementsandthequantitativeresultsachieved,tofacilitate
aneffectiveapplicationofAIOpssolutions.Finally,wediscusscurrentdevelopmentproblemsintheareas
coveredbyAIOpsanddelineatepossiblefuturetrendsforAI-basedfailuremanagement.
CCSConcepts:•Computingmethodologies→Artificialintelligence;•Appliedcomputing→Service-
orientedarchitectures;Datacenters;•Computersystemsorganization→Dependableandfault-tolerant
systemsandnetworks;
Additional Key Words and Phrases: AIOps, IT operations and maintenance, failure management, artificial
intelligence
ACMReferenceformat:
PaoloNotaro,JorgeCardoso,andMichaelGerndt.2021.ASurveyofAIOpsMethodsforFailureManagement.
ACMTrans.Intell.Syst.Technol.12,6,Article81(November2021),45pages.
https://doi.org/10.1145/3483424
81
Authors’ addresses:P.Notaro,ChairofComputerArchitectureandParallelSystems,TechnicalUniversityofMunich,
Boltzmannstr.3,Garchingb.München,Bavaria,Germany,85748andHuaweiMunichResearchCenter,Riessstr.25,Mu-
nich,Bavaria,Germany,80992;email:paolo.notaro@tum.de;J.Cardoso,DepartmentofInformaticsEngineering/CISUC,
UniversityofCoimbra,PortugalandHuaweiMunichResearchCenter,Riessstr.25,Munich,Bavaria,Germany,80992;
email:jorge.cardoso@huawei.com;M.Gerndt,ChairofComputerArchitectureandParallelSystems,TechnicalUniversity
ofMunich,Boltzmannstr.3,Garchingb.München,Bavaria,Germany,85748;email:gerndt@in.tum.de.
Permissiontomakedigitalorhardcopiesofallorpartofthisworkforpersonalorclassroomuseisgrantedwithoutfee
providedthatcopiesarenotmadeordistributedforprofitorcommercialadvantageandthatcopiesbearthisnoticeand
thefullcitationonthefirstpage.Copyrightsforcomponentsofthisworkownedbyothersthantheauthor(s)mustbe
honored.Abstractingwithcreditispermitted.Tocopyotherwise,orrepublish,topostonserversortoredistributetolists,
requirespriorspecificpermissionand/orafee.Requestpermissionsfrompermissions@acm.org.
©2021Copyrightheldbytheowner/author(s).PublicationrightslicensedtoACM.
2157-6904/2021/11-ART81$15.00
https://doi.org/10.1145/3483424
ACMTransactionsonIntelligentSystemsandTechnology,Vol.12,No.6,Article81.Publicationdate:November2021.

81:2 P.Notaroetal.
1 INTRODUCTION
SocietyisnowadayshighlyreliantoncriticalInformationTechnology(IT)infrastructures.To
satisfy the technological needs required by organizations to conduct their business, IT systems
havegrownlargerandmorecomplex.Aimsforhigherscalabilityandefficientresourceutilization
havealsomovedattentiontowarddecentralizedsystems,introducingadditionallayersofabstrac-
tionandcomplexity.Moreover,duetotheircriticalityinday-to-dayoperations,ITinfrastructures
oftodayarerequiredtohavehigherstandardsofavailabilityandreliabilitytoconfrontmodern
challengessuchastheInternetofThings,5G,AutonomousDriving,andSmartCities.Systemfail-
ures can cause a significant amount of disruption during the normal operation of an IT service,
which can rapidly turn into customer dissatisfaction. Because of the very nature of these new
distributedsystems,theiradministrationhasbecomemoredifficultandpronetotheappearance
offailuresandperformanceissues.OperationsandMaintenance(O&M)teamsareparticularly
strainedbythescaleandcomplexityofmodernsystems,wherethelargequantityandmultimodal-
ityofmonitoringdatatooverseeinreal-timecaneasilybeoverwhelmingeventospecializedIT
operators.UnexpectedfaultsalsocauseIToperatorstostoptheirmonitoringoperationsandde-
votetheirtimetosolvetheencounteredissues.Atthesametime,thenewdimensionofmodern
systemsraisesthequestionofhowtoallocateandefficientlydistributeallkindsofresources(com-
putational,physical,andenergetic)inlarge-scalesharedcomputingenvironments.
Current O&M solutions have strong limitations in providing reliable and scalable IT services.
Theyheavilyrelyonthemanualinterventionofhumanoperators,whocannolongercopewith
appearingissuesrapidlyandefficientlyduetothelargescaleofmodernsystems.Typicalhuman
interventionwindowsspanseveralhours,comparedtotheminute-scaleinterventionofautomated
systems. Current automated approaches, however, often exhibit other limitations, especially in
terms of applicability (as they cannot adapt to new problems and situations) and scalability (as
theycannothandlelargedatavolumesinreal-time).Forthisreason,inrecentyearsmuchresearch
interesthasbeendirectedtowarddevelopingintelligentsoftwaresystemstotackleO&Mproblems
effectively,groupedunderthetermArtificialIntelligenceforITOperations(AIOps).AIOps
investigatestheuseof ArtificialIntelligence(AI)fortheautomatedmanagementofITservices
[17,36,74,75,79,96,107,116,129,133].AIOpshelpsSRE,DevOps,andO&Mteamsenhancethe
qualityandreliabilityofITserviceofferings,byusingintelligentalgorithmsandthelargequantity
ofdataavailablethankstomonitoringinfrastructures.AIOpsreliesondata-driventechnologies
(MachineLearning,BigData,DataMining,Analytics,andVisualization)toobservetheoperational
status of the infrastructure, minimize the impact of failures during day-to-day operations, and
manage the allocation of computer resources proactively. Compared to traditional approaches,
AIOpsis:
• fast, because it reacts independently and automatically to real-time problems, without re-
quiringlongmanualdebuggingandanalysissessions;
• efficient,becauseittakesadvantageofthemonitoringinfrastructureholistically,removing
data silos and improving issue visibility. By forecasting workload requirements and
modeling request patterns, AIOps improves resource utilization, identifies performance
bottlenecks,andreduceswastages.ByrelievingIToperatorsfrominvestigationandrepair
burdens,AIOpsenablesin-housepersonneltoconcentratemoreeffortonothertasks;
• effective, because it allocates computer resources proactively and can offer a large set of
actionableinsightsforroot-causediagnosis,failureprevention,faultlocalization,recovery,
andotherO&Mactivities.
Several companies have started to deliver AIOps tools as products over the past few years
[17, 96, 116, 129, 133], while several tech leaders have adopted AIOps algorithms to maintain
ACMTransactionsonIntelligentSystemsandTechnology,Vol.12,No.6,Article81.Publicationdate:November2021.

ASurveyofAIOpsMethodsforFailureManagement 81:3
Fig.1. TotalnumberofpublicationsrelatedtoAIOpsanalyzedinthissurveybyyearofpublication.
theiron-premisecomputingfacilitiesefficiently[36,75,79,82].Intheacademiccontext,several
research groups are taking advantage of the recent advances in Machine Learning (ML) and
AI to explore open problems related to AIOps, such as online failure prediction [27, 79, 148], or
anomaly detection[22, 107, 150]. Despitetheserecentadvances, theconceptof using AI for im-
provingITofferingsisnotnew.Startinginthemid-1970s,differentcomputerscientistshavepro-
posedtolocatesoftwarefaultsinsourcecodeusingstatisticalmodelsandcodecomplexitymetrics
[16,19,28,53,66,90].Sincetheearly1990s,severalonlinesoftware[34,56,65,134]andhardware
[58,100,101]failurepredictionmodelshavebeenproposed.Otherfailurepreventionmethodsalso
datebacktothesameperiod[5,48,49,55,57,135,136].OtherareasofAIOps,likeanomalydetec-
tion,eventcorrelation,orproblemidentification,haveattestedcontributionsforatleast20years
[2,15,20,24,40,68,144].Therefore,thereliabilityandefficiencyofcomputersystemshavealways
beenaresearchfocussincethebirthofInternet-basedservices.Ratherthanasteadyflowofre-
searchcontributions,whatweobserveisanincreasingtrendreachingahighpointinrecentyears
[113] (see Figure 1), motivated also by the rise in interest toward AI and Big Data technologies
duringthelastdecade.
BecauseAIOpsisamodernconceptbridgingresearchandindustry,thereisnowidelyadopted
definitionyet[36].ThetermAIOpswasoriginallycoinedbyGartnerin2017[74],forwhich“AIOps
platforms utilize big data, modern Machine Learning and other advanced analytics technolo-
giestodirectlyandindirectlyenhanceIToperations.”Somesourceshaveadoptedthisdefinition
[75,129,133],whileothershavecomplementeditorhaveproposedadifferentvisiononthetopic
[17, 36, 79, 96, 107, 116]. Table 1 provides an overview of the available sources defining AIOps.
All these definitions share two common objectives: (1) enhance IT services for customers and
(2) provide full visibility and understanding into the operational state of IT systems. Some defi-
nitions also highlight the importance of data collection [74, 75], real-time automated operation
[36,96],andscalability[17,116].
The most cited AIOps problems are anomaly detection [36, 75, 107, 129], root-cause analysis
[17, 75, 96, 116], resource provisioning [36, 107, 116, 129], failure remediation [17, 96, 116], and
failurepredictionandprevention[17,75,79].Wecanobservehowasignificantfractionofthese
classestreatstheoccurrenceoffailures.WecanthendivideAIOpsintotwomacro-areas:failure
managementandresourceprovisioning.Failuremanagementdealswiththeappearanceoffailures,
ACMTransactionsonIntelligentSystemsandTechnology,Vol.12,No.6,Article81.Publicationdate:November2021.

81:4 P.Notaroetal.
Table1. AvailableAIOpsDefinitionswithCorrespondingMentionsofRelatedTechnologiesandFocuses
Source(s) Definition Technologies Focus
Gartner[74] “collectlogs,tracesandtelemetrydata,andanalyzethecollected
Levinetal. datato[...]directlyandindirectlyenhanceIToperations[...] Datacollection,
BigData,ML,
[75] identifypatternsinmonitoring,capacity,servicedesk,and Real-time
DataAnalytics
BMC[129] automationdata[...]theapplicationofmachinelearning(ML) understanding
Resolve[133] anddatasciencetoIToperationsproblems”
Broadcom “establishproactive,automatedremediationcapabilitiesthathelp Issuevisibility,
ML,DataScience
[17] ITteamsdeliversuperiorcustomerexperiences” Automation,CI/CD
“efficientlyandeffectivelybuildandoperateservicesthatareeasy
Dangetal. tosupportandmaintain[...]solvingeverydayIToperational
AI,ML, Real-time
[36] problemsatscale[...]includingintelligentalerting,alert
NetworkScience,understanding,
OpsRamp correlation,alertescalation,auto-remediation,root-causeanalysis
Combinatorial CI/CD,Scaleand
[116] andcapacityoptimization[...]assistDevOpsengineersto
Optimization efficiency
Lietal.[79] improvethequalityofcomputingplatformsinacost-effective
manner”
“providefullvisibilityintothestateandperformanceoftheIT
systems[...]giveIToperationsteamsareal-timeunderstanding
Moogsoft[96] Real-time
ofanyissuesaffectingtheavailabilityorperformance[...] AI,ML,
Nedelkoskiet understanding,
replaceabroadrangeofITOperationstasksincludingavailability,BigData
al.[107] Issuevisibility
performance,andmonitoringofservice[...]enabledetectionof
faultsandissuesofservices”
inallavailablemeansandpossiblewindowsofinterventions,bothindynamicaspects(suchasthe
runtimebehaviorofthesystemorthenetworkresponsiveness)andstaticaspects(likethesource
codeorthedatacenterconfiguration).Ratherthanahomogeneousandwell-definedresearcharea,
it is a wide and heterogeneous space of contributions coming from different specialized areas.
Resourceprovisioningoptimizestheallocationofthediversesetofresourcesnecessarytoprovide
ITservices,suchaspower,computationtime,networkbandwidthandvirtualmemory.
Being a recent and cross-disciplinary field, AIOps is still a largely unstructured area of study.
Theexistingcontributionsarescatteredacrossdifferentconferences,applydifferenttermsforthe
sameconcepts,orusethesametermsfordifferentconcepts.Moreover,thehighnumberofappli-
cationareasrendersthesearchandcollectionofrelevantpapersdifficult.Theadditionalscarcity
ofpreviouscomparisonstudiesandsurveysmotivatestheneedforacomprehensivestudy,able
tocollect,categorizeandsummarizepastcontributions,tofacilitatethecomparisonandsharing
ofallavailableapproachesforeachO&Mtask.
Inourpreviouswork[113],weconductedasystematicmappingstudytoanalyzeandcatego-
rizethewholespectrumofpastAIOpscontributions,todelineateataxonomyoftopicsandopen
problems, and to draw quantitative results about publications by topic and time. In this article,
weconcentrateononeofthetwoidentifiedmacro-areas,i.e.,failuremanagement,toanalyzeand
organizecontributionsaccordingtotargetproblemsandapplicability.Thisenablesourreadersto:
• gather a comprehensive overview of failure management in AIOps, by the definition of a
taxonomyofapproachesandthedescriptionofthecurrentlandscapeofproblems;
• obtainareferenceindexforsolutionsofproblemsagainstrequirements.Requirementsex-
pressedintheformofavailabledatasourcesandtargethigh-levelcomponents(sourcecode,
software,hardware,network,anddatacenter)canbemappedtoalistofavailablesolutions
thankstotheindexingmadeavailableinouranalysis;
• understandthecurrentstateoffailuremanagement,whichproblemshavebeenlonginves-
tigatedandwhichrequirenewresearch.Tothisend,wealsopresentanoutlineofpossible
futuredirectionsforthefieldsofAIOpsandfailuremanagement.
ACMTransactionsonIntelligentSystemsandTechnology,Vol.12,No.6,Article81.Publicationdate:November2021.

ASurveyofAIOpsMethodsforFailureManagement 81:5
The remainder of this article is organized as follows. Section 2 describes previous related re-
viewstudiesinAIOpsandfailuremanagement.Section3presentsthemethodologyofthiswork,
summarizingtheplanningchoicesofsystematicmappingstudyusedtoidentifythepaperslater
presented,aswellastheterminologyandmetricconventions.Section4delineatesthestructure
offailuremanagementinAIOpsandpresentsaselectionofpapersdividedinthematicsections,
describingtheirlineofwork,contribution,approach,inputsource,targetcomponent,andappli-
cationfield.Section5summarizestheresultsandoutcomesdrawnfromourdiscussion.
2 RELATEDWORK
As the AIOps areas mentioned above are large both in number and range of applications, it is
reasonabletoexpectnumerousworksfocusingonfilteringandcategorizingbestapproachesand
practices. Several other surveys and mapping studies have been in fact conducted in the areas
covered by AIOps [22, 24, 39, 46, 47, 60, 63, 70, 71, 91, 99, 106, 109, 111, 112, 122, 125, 130, 139,
146,152].However,nopreviousworkhasprovidedanupdated,comprehensivereviewofAIOps
approachesforfailuremanagement.
Table2summarizesthemostrelevantsurveyandsystematicreviewcontributionsregardingIT
OperationsandArtificialIntelligence,organizedbymaintopicandotherfocuses.Mostworkstreat
singletasks[22,24,39,60,63,91,106,111,112,122,139,152]orgeneralgoals[46,47,125,130,146]
insideAIOps,whicharespecifictoparticularinterventionmethods.
Asecondcategoryofworks[70,71,99,109]treatfailuremanagementintegrally,butsomeof
theworksinsidethisgroupareoutdatedanddonotreflectthecurrentprogressofthefield,while
themostrecentworksdonotfocusonAI-basedapproachesordonotofferacomprehensivelist
ofcontributions.TheclosestmatchtoouranalysisisrepresentedbytheworkofMukwevhoand
Celik[99],whopresentasurveyonfaultmanagementincloudsystems.Differentlyfromthem,we
donotfocusonanyparticularcomputingsystem,andwefocusonthemanifestationoffaults(i.e.,
errors and failures) rather than root causes (see Section 3.3 for terminology). We also choose to
integrateAIandMachinelearningapproachesintheconventionalschemeoffailuremanagement
approaches,ratherthantreatingtheminaseparatecategory.Alltheseconsiderations,including
theobservationsaboutthemissingstructureandterminologyconventionspresentedinSection1,
motivatetheneedforanin-depthstudyinthisarea,liketheoneherepresented.
3 METHODOLOGY
3.1 SystematicMappingStudy
Asystematicmappingstudy(SMS)wasconductedtoobtainrelevantandrepresentativeliter-
ature in the field of AIOps. Different from a systematic literature review (SLR), the ultimate
goalofasystematicmappingstudyistoprovideanoverviewofaspecificresearcharea,toobtain
asetofrelatedpapers,andtodelineatetrendspresentinsidesucharea[67].Relevantpapersare
collectedviawell-definedsearchandselectioncriteria,whileresearchtrendsareidentifiedusing
categorizationschemescoveringdifferentaspects,e.g.,suchmaintopic,origin,ortypeofcontri-
bution. We choose this instrument because we are interested in gathering contributions for the
surveyandobtaininginsightsintothefield,suchasthedistributionofworksindifferentAIOps
subareas and the temporal evolution of the interest toward specific topics. An in-depth discus-
sionofthemappingstudymethodology,thecategorizationscheme,andtheselectionstrategyof
contributionisavailableinaworkseparatelypublished[113],accessibleonline.1
1https://arxiv.org/abs/2012.09108.
ACMTransactionsonIntelligentSystemsandTechnology,Vol.12,No.6,Article81.Publicationdate:November2021.

81:6 P.Notaroetal.
Table2. RelatedAISurveysandSystematicMappingStudies(SMS)Conductedin
AreasCoveredbythisWork
| Ref. Year | Type | MainTopic |     | Focuses |
| --------- | ---- | --------- | --- | ------- |
ITOperations
| [71] 2007 | Survey ITOperations |     | AI,OperationalResearch |     |
| --------- | ------------------- | --- | ---------------------- | --- |
| [70] 2011 | Survey ITOperations |     | AI,OperationalResearch |     |
[109] 2013 SMS FailureManagement Temporal&GeographicalTrends,ServiceLevel,Others
| [99] 2018 | Survey FailureManagement |     | CloudComputing |     |
| --------- | ------------------------ | --- | -------------- | --- |
FailurePrevention
| [112] 2011 | Survey FailurePrevention           |     | CombinatorialTesting |     |
| ---------- | ---------------------------------- | --- | -------------------- | --- |
| [39] 2015  | Survey FailurePrevention/Detection |     | Software             |     |
| [106] 2016 | Survey FaultInjection              |     | Software             |     |
[91] 2017 Survey SoftwareDefectPrediction MachineLearning,PROMISEdataset
FailurePrediction
| [125] 2007 | Survey FailurePrediction |     | AI,IntegratedSystems     |     |
| ---------- | ------------------------ | --- | ------------------------ | --- |
| [152] 2007 | Survey FailurePrediction |     | Clusters                 |     |
| [122] 2010 | Survey FailurePrediction |     | OnlineMethods            |     |
| [63] 2019  | Survey FailurePrediction |     | HighPerformanceComputing |     |
FailureDetection
| [60] 2015  | Survey AnomalyDetection |     | BottleneckIdentification |     |
| ---------- | ----------------------- | --- | ------------------------ | --- |
| [24] 2009  | Survey AnomalyDetection |     | -                        |     |
| [22] 2019  | Survey AnomalyDetection |     | DeepLearning             |     |
| [139] 2013 | Survey AnomalyDetection |     | Network                  |     |
[111] 2008 Survey InternetTrafficClassification MachineLearning,IPNetworks
Root-causeAnalysis(RCA)
| [130] 2017 | Survey Root-causeAnalysis |     | -        |     |
| ---------- | ------------------------- | --- | -------- | --- |
| [146] 2016 | Survey FaultLocalization  |     | Software |     |
[46] 2015 Survey FaultDiagnosis Model-andsignal-basedapproachesinIndustrialSystems
[47] 2015 Survey FaultDiagnosis Knowledge-basedandhybridapproachesinIndustrialSystems
Thanks to our mapping study, we collected 1,086 AIOps contributions and inferred an AIOps
taxonomy based on thematic areas and commonly treated tasks (see Figure 2). Our taxonomy
groupscontributionsinthetwomainmacro-areas:failuremanagementandresourceprovisioning.
Each macro-area divides contributions into different categories, based on end-goals and target
problems.Wealsoclassifytherelevantpapersaccordingtothefollowingcategorizationaspects:
targetcomponents,inputdatasources,AImethods(seeTables4and8).
Forthefailuremanagementmacro-area,thefocusofoursurvey,wealsodivideapproachcat-
egories into proactive and reactive, based on the window of intervention (red box in Figure 2).
Moreover, we introduce a second level of categorization for failure management, which divides
eachcategoryintoseveralsubcategoriesbasedonthespecifictargetproblemsolved.Examplesof
subcategoriesaresoftwaredefectpredictionforfailureprevention(Section4.1.1)andlogenhance-
mentforfailuredetection(Section4.3.3).Foroursurveydiscussion,weselect100mostprominent
contributionsinfailuremanagementfromthetotalresultsetof1,086,coveringallcategoriesand
subcategoriesdefinedforthisfieldofstudy.Fortheexhaustivelistofpaperscovered,dividedinto
categoriesandsubcategories,seeTable4inthenextsection.
3.2 EvaluationMetrics
In our analysis, we provide quantitative results for the papers under investigation. This section
providesanoverviewoftheevaluationmetricsemployedforcomparisonthroughoutthesurvey
discussion.
ACMTransactionsonIntelligentSystemsandTechnology,Vol.12,No.6,Article81.Publicationdate:November2021.

ASurveyofAIOpsMethodsforFailureManagement 81:7
Fig.2. TaxonomyofAIOpsasobservedintheidentifiedcontributions.Intheredbox,thefocusofthissurvey.
Table3. ContingencyTableforPredictionTasks
PredictedClass
|                         | PositiveClass      |     | NegativeClass      |     |     |
| ----------------------- | ------------------ | --- | ------------------ | --- | --- |
| ssalClaeR PositiveClass | TruePositives(TP)  |     | FalseNegatives(FN) |     |     |
| NegativeClass           | FalsePositives(FP) |     | TrueNegatives(TN)  |     |     |
Forscalarprediction(orregression)tasks,awidelyadoptedmetricistheMean-squaredError
(MSE),definedastheaveragesquareddifferencebetweentargetandpredictedvalues:
|     |       | (cid:2)N (cid:3) | (cid:4) |     |     |
| --- | ----- | ---------------- | ------- | --- | --- |
|     | 1     | pred             | 2       |     |     |
|     | MSE = | y −y             | .       |     | (1) |
|     | N     | i                | i       |     |     |
i
A measure adopted across all classification problems (software defect prediction, root-cause
diagnosis, recovery, etc.) is accuracy, i.e., the ratio of classified samples assigned to the correct
class. In some contexts, however, accuracy may appear as a misleading metric to evaluate the
qualityofprediction.Thisisthecase,forexample,forproblemswithahighpredominanceofone
class,wheretrivialmodelscanbeconstructedtoreachhighaccuracyjustexploitingdataskewness.
Asimilarconsiderationappliestodetectionproblems(analyzed,e.g.,inSections4.2and4.3),where
thepositiveclass,i.e.,thedetectedfailure,mayappearlessfrequentlythanthenegativeclass,even
though it constitutes the most critical aspect from an evaluation point of view. In such cases, it
iscommontoadoptmorerepresentativemeasures,derivedfromthenotionofcontingencytable
[122]:
Usingthisconvention,accuracycanbewrittenas
TP +TN
|     | ACC = |     | .   |     |     |
| --- | ----- | --- | --- | --- | --- |
(2)
|     | TP  | +TN +FP | +FN |     |     |
| --- | --- | ------- | --- | --- | --- |
Toquantifytheabilityofapredictortoidentifypositivesamplescorrectly,theprecisionmeasure
isusuallyemployed,whiletomeasuretheabilityofadetectortoreporttruepositivesamples,the
recallmeasure(alsoknownastruepositiverateorsensitivity)isused.Theyaredefinedasfollows:
|     | TP  |     | TP     |     |     |
| --- | --- | --- | ------ | --- | --- |
| P = | ,   |     | R =    | .   | (3) |
| TP  | +FP |     | TP +FN |     |     |
ACMTransactionsonIntelligentSystemsandTechnology,Vol.12,No.6,Article81.Publicationdate:November2021.

81:8 P.Notaroetal.
Moreover,thefalse-positiverate (FPR,alsocalledfalsealarmdate),whichidentifiesthepro-
portionofwronglyreportedfailures,isdefinedasfollows:
FP
FPR = . (4)
FP +TN
Sinceprecisionandrecalldonottakeintoaccountthenumberoftruenegatives,somepapers
compareresultsintermsoftrue-negativerate(TNR,orspecificity)andrecall.Thetrue-negative
rateisdefinedasfollows:
TN
TNR = . (5)
TN +FP
Precisionandrecallcanoftenbetradedoffwitheachotherbyadjustingsensitivitythresholds
inside algorithms, so that an increase in precision can be obtained by reducing recall and vice
versa. One possibility to evaluate both measures at the same time is to use the F1-score (or F-
score/F-measure),computedastheharmonicmeanofprecisionandrecall:
P ·R
F =2· . (6)
1 P +R
Afinalpossibilityistousereceiveroperatingcharacteristic(ROC)curves,parametricline
plotswhichdescribethevariationoftwometricsinrelationtochangesinthesensitivitythreshold.
Precision-recallcurvesarepossible,butitiscommontoplottherecallagainstthefalse-positive
rate.FromthistypeofcurvestheAreaundertheROCcurve(AUCROC)measurecanbecom-
puted.AhigherAUCROCscorethenindicatesabetterclassifier.
3.3 Terminology
In our discussion, we also adopt a variety of error-related terms such as fault, failure and root
cause.Fromaterminologypointofview,weadopttheconventionofSalfneretal.[122]forthe
characterizationoffaultybehavior.Accordingthisconvention:
• errorsaredeviationsfromthecorrectsystemstate;
• failuresaremanifestationsofundesireddeviationsinthedeliveryofaservice;
• faults(orrootcauses)aretheprimarycausesofundesiredbehavior(i.e.,theerrors).
Moreover,weoftenencounterdifferenttermsrelatedtodatasourcesthatmayhaveanambigu-
ousmeaningdependingonthecontext,suchaslogsortraces.Tobeconsistentinourdiscussion,
wegrouptheobserveddatasourcesaccordingtothisconvention:
• sourcecoderepresentsanyunitofsoftwaresourcecodeusedasinputtoapredictionsystem,
independentlyoftheformandextension(e.g.,function,file,module,class,etc.);
• testingresourcescomprisetoolsusedtoperformin-andpost-releasesoftwaredebugging,in
particularunittestsuites,executionprofilesorrundescriptionreports;
• systemmetricsmeasurevariousnumericalquantitiesatthehardware,OS,softwareanden-
vironmentlevel,describingresourceutilizationandtheoverallprocessstateofthesystem;
• keyperformanceindicators(KPI)provideinformationaboutthestatusofservicesandthe
associatedrequirementsthatneedtobemetduringruntimeoperations.Theyquantitatively
measurethequalityofservedrequestswithparameterssuchaslatency,uptime,failurerate,
availability,andsoon;
• networktrafficisthecollectionofnetworkpacketsexchangedoverInternetbydifferenthosts.
Itincludesthepayloadandcontrolinformationsuchasports,addresses,protocolstandards
andotherparameters;
• topology isanyinformationdescribingthespatialrelationsinsideaworkingsystem,when
usedasainput;
ACMTransactionsonIntelligentSystemsandTechnology,Vol.12,No.6,Article81.Publicationdate:November2021.

ASurveyofAIOpsMethodsforFailureManagement 81:9
• incidentreportsarecollectedwiththehelpofservicedeskandinternalproblemmanagement
systems to identify common problems and facilitate resolution. Usually, they describe the
problemwithtextandcategoricalattributesandtheymaybeassociatedtoaresolutionteam
orroutingsequence;
• eventlogs(orsimplylogs)arecollectionsofhuman-interpretableprintingstatementsdescrib-
ingsoftwareeventsoccurringinruntimeoperations.Theyaretypicallystoredasindepen-
dentfilesandlogentries(i.e.,lines)areassociatedtoapredefinedformat(orlogkey);
• execution (distributed) traces are hierarchical descriptions of the modules and services in-
vokedtosatisfyauserrequest.Theyareusuallyannotatedwiththeservicenameorcategory
andthetimedurationofeachmodule(calledspan).
4 AIAPPROACHESINFAILUREMANAGEMENT
FailureManagement(FM)isthestudyoftechniquesdeployedtominimizetheappearanceand
impact of failures. In large-scale systems failures are inevitable, so adequate protection mecha-
nismsneedtobeputuptominimizetheirandsatisfyService-levelObjectives(SLO)[26].Fol-
lowinganestablishedconvention[10,21,99,119,160],wedifferentiatebetweenproactive(failure
avoidance)andreactive(failuretolerance)approaches(differentlyfromReference[99],wedonot
endorsethe“resilientapproaches”categoryforAIapproaches).Inourhierarchicalscheme,failure
avoidancecomprisesanyapproachaimingtoaddressfailuresinanticipationoftheiroccurrence,
eitherbypredictingtheappearanceoferrorsbasedonthesystemstate,orbytakingpreventive
actions to minimize their future incidence. Failure avoidance is divided into failure prevention
(Section 4.1) and online failure prediction (Section 4.2). Failure tolerance techniques, however,
deal with errors after their appearance to assist humans and improve mean-time-to-recovery
(MTTR).Failuretoleranceincludesfailuredetection(Section4.3),root-causeanalysis(Section4.4),
andremediation(Section4.5).
ThefivecategoriesabovementioneddivideFMbasedonthetemporalwindowofintervention.
Inourpreviouswork[113],wequantifiedthefrequencyofFMpublicationsinourfivecategories.
TheFMareawiththehighestnumberofcontributionsisfailuredetection(226,33.7%),followed
by root-cause analysis (179, 26.7%) and online failure prediction (177, 26.4%). However, failure
preventionandremediationaretheareaswiththesmallestnumberofattestedcontributions(71
and17,respectively).Thesetrendsareconfirmedandevenmoreaccentuatedwhenwelookatthe
mostrecentpublicationperiod(2018onwards):only11(5)publicationshavebeenfoundforfailure
prevention(remediation)inthistimeframe.
Withineachofthesefivecategories,wecangroupcurrentcontributionsbasedontargetsprob-
lems(ortasks)thatacontributionaimstosolve(e.g.,failurepreventionincludessoftwaredefect
prediction,faultinjection,softwarerejuvenation,andcheckpointing).Table4categorizestheFM
contributionsanalyzedinthisworkbycategory,taskandAImethodsused.
While we consider our five-category scheme for FM comprehensive and stable over time (al-
thoughtherelativeproportionofworksineachcategorymaychange),weenvisionthatlandscape
oftasksandtargetproblemswithineachcategorymayevolvemorequickly,byexpandingsome
ofthecurrentminoritytasksandbypresentingnewproblemsandchallengesintheyearstocome
(see discussion in Section 5.1). Table 8 (at the end of the section) present the same list of works
groupedbytask,AImethod,employeddatasources,andhigh-leveltargetcomponents.
4.1 FailurePrevention
Animportant(andyetnosocommon)possibilitytodealwithfailuresproactivelyisfailurepre-
vention,treatedinthissection.Failurepreventionmechanisms,tendtominimizetheoccurrence
andimpactoffailures,byanalyzingtheconfigurationofthesystem,bothinstaticaspects(likethe
ACMTransactionsonIntelligentSystemsandTechnology,Vol.12,No.6,Article81.Publicationdate:November2021.

81:10 P.Notaroetal.
Table4. PapersAnalyzedinthisSurveybyCategory,Task,andAIMethod
| Category | Task           |                                  | AIMethod                  |
| -------- | -------------- | -------------------------------- | ------------------------- |
|          |                | LinearModels:[35,52,102,117,153] | NaiveBayes:[38,94,98,141] |
|          | SoftwareDefect | Tree-based:[38,50,94,98,141]     | SVM:[42,50]               |
Prediction(SDP) BayesianNetworks:[38,50,115,141] Others:[76,102,153]
LogisticRegression:[35,98,103,141]
FailurePrevention FaultInjection Clustering:[105,128] LinearModels:[128]
Tree-based:[105]
|     | SoftwareAgingand | MarkovModels:[21,136,137]         | Tree-based:[4]     |
| --- | ---------------- | --------------------------------- | ------------------ |
|     | Rejuvenation     | LinearModels:[4,21,49]            |                    |
|     | Checkpointing    | MarkovModels:[62,95,114]          |                    |
|     |                  | Tree-based:[77,78,89,104,138,148] | NaiveBayes:[54,88] |
HardwareFailure NeuralNetworks:[37,78,89,149,165,167] Clustering:[54,101]
|               | Prediction | SVM:[89,164,167]       | LogisticRegression:[89]       |
| ------------- | ---------- | ---------------------- | ----------------------------- |
| OnlineFailure |            | MarkovModels:[161,164] | Others:[33,143]               |
| Prediction    |            | SVM:[44,81,160]        | AutoregressiveModels:[23,119] |
SystemFailure
|     | Prediction | BayesianNetworks:[31,119]    | NeuralNetworks:[61,160] |
| --- | ---------- | ---------------------------- | ----------------------- |
|     |            | MarkovModels:[123]           | Others:[81,160]         |
|     |            | Clustering:[11,45,72,127]    | PCFG:[11,26]            |
|     |            | Autoencoders:[7,131,150,159] | FSM:[12,45]             |
AnomalyDetection
|                  |     | MarkovModels:[110,127] | Tree-based:[86,151]      |
| ---------------- | --- | ---------------------- | ------------------------ |
| FailureDetection |     | PCA:[72,73,151]        | Others:[29,31,86,87,127] |
OtherNeuralNetworks:[18,41,45,92,162]
|     | InternetTraffic   | NeuralNetworks:[8,142] | SVM:[43]           |
| --- | ----------------- | ---------------------- | ------------------ |
|     | Classification    | NaiveBayes:[97]        |                    |
|     | LogEnhancement    | Tree-based:[168]       | Others:[163]       |
|     | FaultLocalization | GraphMining:[9,30,156] | Search:[30,80,132] |
Others:[1,72,83,85,110,121,145]
Root-cause Root-cause PatternMatching:[6,127] Others:[25,26,64,124,154]
| Analysis | Diagnosis  | BayesianNetworks:[31,64]    |                  |
| -------- | ---------- | --------------------------- | ---------------- |
|          |            | Clustering:[32,84,120]      | Others:[3,14,32] |
|          | RCA-Others | LogisticRegression:[14,120] |                  |
IncidentTriage MarkovModels:[126] BayesianDecisionTheory:[158]
|     | Solution | TextAnalysis:[82,140,166] | Similarity-based:[140] |
| --- | -------- | ------------------------- | ---------------------- |
Remediation
Recommendation
|     | Recovery | MarkovModels:[124] |     |
| --- | -------- | ------------------ | --- |
sourcecode)anddynamicaspects(e.g.,theavailabilityofcomputingresourcesinphysicalhosts).
Thecommongoalistotakeorsuggestpreventiveactions;however,thestrategiestoachievethis
endgoalvaryextensivelyintargetsandmodeofapplication.Moreover,wecandistinguishpre-
ventiveoperationsinaofflinesettingandanonlinesetting.Fortheformer,weobservealargepre-
dominance of software debugging techniques, usually categorized under the name of software
defect prediction (SDP), determined to evaluate failure risks from source code analysis; fault
injectiontechniquesarealsosporadicallypresent,withtheobjectiveofstress-testingthesystem
togainadditionalinsightsandpreventfuturefailures.Inanonlinesetting,weobservedmethods
dealingwiththeproblemofsoftwareaging,categorizedunderthenameofsoftwarerejuvenation;
andcheckpointingtechniques,todeliverefficientrestartstrategiesinthepresenceofirreversible
errors.
4.1.1 Software Defect Prediction. SDP determines the probability of running into a software
bug(ordefect)withinafunctionalunitofcode(i.e.,afunction,aclass,afile,oramodule).The
fundamentalassumption,whichconnectsSDPtotheoccurrenceoffaults,istheobservationthat
defect-pronecodegeneratesfailureswhenexecuted.Therefore,estimatingtheremainingdensity
ofbugsinafunctionalunitofcodeallowssoftwaremaintainerstoprioritizetheirefforts,concen-
tratingonthemostvulnerablemodules,files,andmethods.
ACMTransactionsonIntelligentSystemsandTechnology,Vol.12,No.6,Article81.Publicationdate:November2021.

ASurveyofAIOpsMethodsforFailureManagement 81:11
A traditional method to identify fault-prone software consists in constructing defect predic-
torsfromcodemetrics.Codemetricsarehandcraftedfeaturesobtaineddirectlyfromsourcecode,
which potentially have the power to predict fault proneness in software. Over the last decades,
differentgroupsofcodemetricshavebeenproposed:theoriginalmodule-levelmetrics,designed
during the 1970s for procedural languages, describing graph complexity (McCabe metrics [90])
andreadingcomplexity(Halsteadmetrics[53]);ChidamberandKemerer[28]laterdefinedasuite
ofmetricsforobject-orientedsoftwareonaclasslevel,usuallyreferredtoas“CKmetrics”(from
theauthors’initials);Briandetal.[16]haveintroducedcouplingmetricsasameasureofintercon-
nection between software modules; finally, the Lines-of-Code (LOC) metric is widely adopted
acrosstheresearchcommunity.
Nagappanetal. [102]investigateanSDPapproachemploying codecomplexitymetrics.They
however argue that multicollinearity (or inter-correlation) between some of these metrics ren-
der the problem more complex. They apply Principal Component Analysis (PCA) to obtain
a smaller set of uncorrelated features. Then, they construct linear regression models to predict
post-releasedefectsinfivedifferentdatasets.Theyalsoattempttoapplymodelslearnedonone
projectontootherprojectstotestcross-projectapplicability,obtainingmixedresults,andtherefore
arguingforthesimilarityofprojectsasarequirementfortransferlearning.
In Reference [94], Menzies et al. discuss the use of static code metrics (like McCabe and Hal-
stead’s),arguingintheirfavorandrejectingcommonclaims,suchastheoneofbeinguninforma-
tive(becauseofcross-correlationofvalueswithinthecodefeatureset)orsuboptimalcomparedto
otherfeatures.Inparticular,theyarguefortheirpracticality,popularity,andusefulness.Attention
ismovedfromthechoiceofmetricstothechoiceoflearners:byapplyingdecisiontreesandNaïve
Bayes models, software modules are classified as defect-prone or defect-free. The authors argue
in favor of Naïve Bayes with the use of logarithmic features, which obtains the best detection
performance(71%recalland25%falsealarmrate).
Elishetal.[42]useSupportVectorMachines(SVM)forsoftwaredefectprediction.Failure-
pronenessispredictedatthefunctionlevel,fromacompositesetofMcCabe,Halstead,andLOCfea-
tures.TheapproachappliesGaussiankernelstoenablenon-linearmodelingandistestedonfour
softwareprojectsfromtheNASAMDPdataset[93].AcomparisonwithotherMachineLearning
methods (logistic regression, multilayer perceptron,k-NN,k-means, Bayesian Networks (BN),
NaïveBayes,RandomForest,andDecisionTree)iscarriedout,wheretheSVMapproachoutper-
forms all the models in terms of recall (≥0.994), at the expense of a lower precision (≥0.8495).
SVMsexhibitaccuracies(≥0.8459)andF-scores(≥0.916)comparabletotheothermethods.
AnothercommonclassofmethodsforSDPisconstitutedbyBN,duetotheirpositivequalities
suchasaccuracy,interpretability,andmodifiability.Dejaegeretal.[38]consider15differentBN
classifiers,includingNaïveBayesasaspecialcase.Theapproachisvalidatedontwodatasets(the
alreadymentionedNASAMDP[93]andtheEclipseprojectrepository[157])anditiscompared
to other Machine Learning algorithms using AUC and H-measure. The results show how more
interpretablemodelstendtobelesseffectivethancomplex,discriminativestructures.Okutanet
al.[115]integrateestablishedcodemetricswithtwonewlyintroducedmeasures,theNumberof
DevelopersandtheLackofCodingQuality(LOCQ),anduseBayesianNetworkstomodelthe
causalrelationshipsamongmetrics,aswellasbetweenmetricsanddefectproneness.Experiments
conducted on the PROMISE data repository [93] highlight the prediction effectiveness of three
metrics:LOC,LOCQ,andResponseforClass,aCKmetric.
A potential indication of the presence of software faults may also come from the change his-
toryofsourcecode.Inparticular,thecodeageandthenumberofpreviousdefectscanbeindica-
tive to estimate the presence of new bugs [52]. This type of analysis better reflects a software
model where changes are continuously applied to a code repository and where new defects are
ACMTransactionsonIntelligentSystemsandTechnology,Vol.12,No.6,Article81.Publicationdate:November2021.

81:12 P.Notaroetal.
potentiallyintroducedwitheachnewrelease.WhilethemajorityofearlySDPcontributionshave
approached the problem from a single-release perspective, a second category of works (the so-
calledchangelogapproaches)haveconcentratedtheireffortsaroundsoftwarehistory,considered
amoredeterminingfactorthancodemetricstoestimatedefectdensity.Gravesetal.[52]divide
softwarequalitypredictorsintoproductmeasures(likecodemetrics)andprocessmeasures,which
quantitativelydescribethechangehistoryofasoftwareproject,advocatingforthelattercategory
(product measures are considered inconclusive from a correlation analysis). Generalized linear
modelsareconstructedfromprocessmeasurestopredictthedefectcountinthesoftwarereposi-
toryofatelephoneswitchingsystem.Aweighted-timedampmodelisalsointroduced,wherecode
changesaredown-weightedbasedonage,showingthebestperformancesoverall.
Ostrandetal.[117]examinechangesinlargesoftwaresystemsandtheirrelationtopastfaults
to predict the number of defects in the next release. As in Reference [52], they adopt a Poisson
generalizedlinearmodelfromwhichthemaximumlikelihoodestimatesofthemodelparameters
are used to interpret the relevance of the different metrics. The model is tested on the release
cycleofanin-houseinventorysystemwithawiderangeofnewmetricsatthefilelevel,including
programming language, edit flags, and age. According to the results, the top 20% files with the
highestpredictedfaultcountcontainedonaverage83%ofthelateridentifiedfaults.Acomparative
analysisofthetwosetsofSDPmetrics(codeandchangemetrics)wasconductedbyMoseretal.
[98]ontheEclipseprojectrepository.ThecomparisonisperformedusingthreedifferentMachine
Learning approaches: Naïve Bayes, logistic regression, and decision trees. Change metrics used
individuallyareshowntobemoreefficientthancodemetricsalonefordetectingdefectivesource
files. Moreover, a combined approach slightly improves or has comparable results to a change
metric approach. Giger et al. [50] also utilize a combination of source code and change metrics
to tackle defect prediction at the method level by applying four different ML algorithms. Using
aninvestigationmethodologysimilartoReference[98],resultsareagainpresentedbythesetof
input metrics used with similar conclusions: change-metric approaches outperform code-metric
approaches,whiletheadvantageofahybridsetofmetricsisobservablebutlimited.
InadditiontointroducingthebenchmarkSDPdatasetAEEEM,D’Ambrosetal.[35]compute
several change-related metrics, such as the number of revisions, refactorings, and bug fixes per
file,whicharecorrelatedwiththenumberoffuturedefects.Mostlybasedontheconceptsofcode
entropyandchurn,thesemetricsarethenappliedwithgeneralizedregressionmodelstoclassify
andrankfilesbyprobabilitydefect.Theproposedrankingapproachcanconsiderthenecessary
revieweffortoffilesaswell.Learning-to-Rank(LTR)isalsothefocusoftheworkofYangetal.
[153],wherealinearmodelistrainedviacompositedifferentialevolution(CoDE)andinput
metrics are selected using the information gain criterion. According to the authors, maximizing
therankingperformancedirectly,ratherthanrelyingonthepredictednumberoffaults,provides
benefits such as robustness for SDP models focusing on ranking. This claim is verified by com-
paringLTRapproacheswithtraditionalleast-squaresregressionapproachesbasedonbugcount
prediction,whereLTRapproachesareinfactpredominantlymoreaccuratefortherankingtask,
especiallyinprojectswithahighnumberofmetricsandreleases.
Cross-projecttransferability,i.e.,theabilitytolearnasoftwaredefectmodelonsourceprojects
differentfromthetargetdomain,representsthemajorapplicationobstacletosomeauthors.Nam
etal.[103]studytheproblemoftransferlearningforsoftwaredefectsbyapplyinganextendedver-
sionof TransferComponentAnalysis(TCA)tolearncommonlatentfactorsbetweensource
andtargetprojects.Theextension(TCA+)improvescross-projectpredictionbyselectinganappro-
priatenormalizationoptionforsourceandtarget.TCA+featuresarethenusedasinputofalogistic
regressionclassifiertopredictfaultymodulefiles.Theapproachisvalidatedontwodatasets(Re-
link [147] and the already mentioned AEEEM [35]): documents are represented by the different
ACMTransactionsonIntelligentSystemsandTechnology,Vol.12,No.6,Article81.Publicationdate:November2021.

| ASurveyofAIOpsMethodsforFailureManagement |     |     |     |     |     |     |     |     | 81:13 |
| ----------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |
Table5. SummaryofDescribedMethodsforSDP,CategorizedbyDataSources,SDPTask,
andTargetCodeUnit
|          | DataSources |     |         | SDPTypology  |               |          | TargetCodeUnit |      |        |
| -------- | ----------- | --- | ------- | ------------ | ------------- | -------- | -------------- | ---- | ------ |
| Paper(s) | CodeMetrics |     |         |              |               |          |                |      |        |
|          |             |     | atadTSA | tcejorp-emaS | tcejorp-ssorC | noitcnuF | ssalC          | eliF | eludoM |
citatS -egnahC
detaler
| [102] | •   |     |     | •   | •   |     |     |     | •   |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|       | •   |     |     | •   |     |     |     | •   | •   |
[38]
| [94]  | •   |     |     | •   |     |     |     |     | •   |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [115] | •   |     |     | •   |     |     | •   |     |     |
|       | •   |     |     | •   |     | •   |     |     |     |
[42]
| [117] |     | •   |     | •   |     |     |     | •   |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [50]  | •   | •   |     | •   |     | •   |     |     |     |
|       | •   | •   |     | •   |     |     |     | •   |     |
[35,98]
|     | •   | •   |     | •   |     |     |     |     | •   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
[153]
| [52] |     | •   |     | •   |     |     |     |     | •   |
| ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|      | •   | •   | •   | •   |     |     |     | •   |     |
[76]
|     | •   | •   |     | •   | •   |     |     | •   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
[103]
| [141] |     |     | •   | •   | •   |     |     | •   |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
softwaremetricsavailableforeachdataset,andresultsarecomparedtootherpredictionmethods
usingtheF-measure(forcross-projectprediction,0.61onRelinkand0.41onAEEEM).
Acritiqueoftraditionalcodemetricsisthattheyaretoohandcraftedandsimplistic.Analter-
nativeistodirectlyparsethesourcecodeusingAbstractSyntaxTrees(AST).Wangetal.[141]
debatetheabilityofcodemetricstomodelsemanticsandthusdiscriminatebetweencoderegions
with the same structure and different semantics, arguing in favor of latent semantic representa-
tions.Intheirwork,afterparsingthecodewithASTs,aDeepBeliefNetwork(DBN)istrained
tolearnsemanticfeaturesinanunsupervisedfashionviastochasticfirst-orderoptimization.Then,
NaïveBayes,DecisionTrees,andLogisticRegressionmodelsareusedtopredictfaultsfromthe
latentrepresentationsinbothwithin-andcross-projectsettings.ResultsobtainedonJavaprojects
ofthePROMISErepositorydatasetarecomparedwithTCA+[103]andshowasignificantimprove-
mentintermsofF-scoreinthecross-projectsetting(0.568,+9.1%over[103]).
Li et al. [76] explore Convolutional Neural Networks (CNN) for SDP. During the parsing
step,asubsetofASTnodescorrespondingtodifferenttypesofsemanticoperationsisextracted.
Thesetokensaremappedtonumericalfeaturesusingembeddingsandfedintoa1Dconvolutional
architecture,whichisusedtolearnintermediaterepresentationsoftheinputcode,andlaterinte-
gratedwithhandcraftedfeaturesforthefinalprediction.Resultsobtainedonasmallersubsetof
projectsofthesamePROMISEdatasetarecomparedwithatraditionallogisticregressionmodel
and the DBN approach of Reference [141], exhibiting again a substantial F-score improvement
(0.608,+0.084overtraditionalmethodsand+0.065overReference[141]forwithin-projectSDP).
4.1.2 FaultInjection. Faultinjectionisthedeliberateintroductionoffaultsintoatargetwork-
ing system [5] to evaluate the level of fault tolerance reached. In traditional computer systems,
thisevaluationrepresentsavalidationofthereactivecapabilitiesofasystemoff-the-shelf.Inthe
specificcaseofAIOpsandfailuremanagement,faultinjectionalsoallowsonetoevaluatetheeffi-
cacyofexternallydeployedreactivemechanisms.Severalworkspresentedinlatersectionshave
ACMTransactionsonIntelligentSystemsandTechnology,Vol.12,No.6,Article81.Publicationdate:November2021.

81:14 P.Notaroetal.
appliedfaultinjectiontechniquesforthispurpose[25,87,110,119,124,127].Importantdefinitions
infaultinjectionarethesetofinjectedfaultsorfaultload(F);thesetofactivationsoffaultsinthe
system(A);theset(R)ofreadoutsfromthesystemandtheset(M)ofmeasuredvalues.FandA
modeltheinjectionprocedurefromtheinput,RandMfromtheoutput[5].
Astheconceptoffaultinjectionisdisconnectedfromthespecifictypeofsystemundertest,its
useisnotrestrictedtoasingleapplicabilityscenario.Faultinjectioncanbeappliedatthehardware
level,toemulatetheappearanceoffaultsinphysicalcomponents,suchasharddrivesandCPUs,as
itisinfeasibleandcostlytoinducerealfaultsinthisdomain.Atthesoftwarelevel,faultinjections
are used to understand the effect of bugs in the behavior of computer software or to model the
causaldynamicsofoneormoresoftwarecomponentsinashared-resourceenvironment,suchas
anoperatingsystemandtheexecutingprocesses.SoftwareFaultInjection(SFI)istheautomated
andplannedinsertionofsoftwarefaults(whichinthiscaseconstitutethefaultload)[105].Software
faults can be inserted directly or can be simulated to model the consequences of their injection.
For instance, the injection of erroneous data in a program introduces a failure, representing an
undesired behavior, but not a root-cause problem (i.e., a fault), therefore modeling the problem
indirectly.Anothercommontargetfordatacorruptionisfunctioninterfaces,suchasAPIs.
AconceptconnectedtoSFIisMutationTesting(MT),i.e.,theintroductionofsmallmodifica-
tionsinthesourcecodetoevaluatethequalityofcodecoverageachievedbytestcases.MTcomes
closer to mimicking faults compared to error injection, because it introduces software faults di-
rectly rather than their consequences (the errors). However, introducing random code changes,
targeting variable assignments and function calls, can become inefficient if the procedureis not
guided,duetotheexpensivecostofrunningthetestcasesuiteforeachoftheexponentiallynu-
merous mutated versions of the program. It is therefore fundamental to reduce the number of
mutations to the minimum essential, without losing the discernment ability of mutation opera-
tions.Nowadays,manyavailabletoolstrytoidentifycodechangesthatcanberepresentativeof
realsoftwarefaults.While,ontheonehand,MToperatestoimprovethequalityandcoverageof
testcases,SFI,ontheotherhand,attemptstoidentifyandemulatefaultsthatcannotbediscovered
bytestsuites,becausetestingisperformedinsandboxedscenarios,divergingconsiderablyfrom
realoperationworkloads.SFIcoversthisgapbystressingtheoperatingconditionsofaproduction
environmentwhileexaminingtheconsequences.
In a distributed computing environment, fault injection can also be applied at the cluster or
datacenterscale,forexample, torandomly terminateoperationsattheinstancelevel and stress-
test the resiliency of the distributed service under investigation. This is the case with software
toolssuchasChaosMonkeyandKongbyNetflix[13]orFacebook’sProjectStorm[69].Finally,
faultinjectiontechniquescanbeappliedatthenetworklevelbasedonprinciplesthataresimilar
tothehardwareandsoftwarelevelpreviouslycited.
Nowadays,approachesperformingfaultinjectionaremostlyoutoftherealmofAI,asfaultinjec-
tion predominantly consists of switching off mechanisms and fault insertion procedures, where
the problem is purely algorithmic and the necessity of intelligent agents is unjustified. The few
available contributions of AI to the field are concentrated around the implementation selection
policiesforthefaultload,wherethenumberofappliedfaultsneedstobereducedforcomputation
reasons.
In the context of MT, Siami Namin et al. [128] use a regression-based model to estimate the
efficacy of a subset of mutation operators in predicting the mutation adequacy ratio (AM), a
measureoftestcoverageinMT.Inparticular,foreachmutationoperator,theycomputetheindi-
vidualAManduseitasaregressionfeaturetoestimatetheoverallAMofthetestsuite.Theyargue
thataminimalsubsetofmutatorsabletopredicttheAMmeasurewillalsorepresenttheideal,re-
ducedsubsetofoperatorstoapplyformutationtesting.Theyalsoapplyotherstatisticalanalysis
ACMTransactionsonIntelligentSystemsandTechnology,Vol.12,No.6,Article81.Publicationdate:November2021.

ASurveyofAIOpsMethodsforFailureManagement 81:15
techniques,suchasclusteringandcorrelation,toidentifygroupsofsimilarvariablesandeliminate
theone with thehighestcomputationcostfrom theselectiondomain. Using thistechnique,the
setofcodemutantsisreducedto8%oftheinitialsize,drasticallyreducingtheestimationtimefor
theAMmeasure,whichisinturnnecessarytoestimatecodefailurecoverage.
Motivated by the strong presence of unrepresentative faults that are obtained with state-of-
the-artSFIapproaches,Natellaetal.[105]usetwoMachineLearningapproachestoimprovethe
faultloadset.Theyapplydecisiontreesforclassifyingcomponentsintohigherandlowerfaultrisk
(MRandLR,MostandLeastRepresentative,respectively)forconsequentfaultselection.Moreover,
startingfromtheobservationthatlowfan-inandfan-outcomponentshavefaultsthataremore
difficulttodetect,theauthorsapplyanunsupervisedlearningapproachusingthecodemetricsof
softwarecomponents(seealsoSection4.1.1).Specifically,k-meansclusteringisusedtoseparate
targetcomponentsintotwoclustersbasedontheirinteraction.Faultsareinjectedintocomponents
of the cluster with the lowest fan-in and fan-out. The approach is tested on different software
components(MySQL,RTEMS,PostgreSQL)atdifferentgranularitiesandcanreducefaultloadsize
(−22%to−69%)whileincreasingfaultrepresentativeness(+4%to+26%).
4.1.3 SoftwareAgingandRejuvenation. Softwareagingdescribestheprocessofaccumulationof
errorsduringtheexecutionofaprogramthateventuallyresultsinterminalfailures,suchashangs,
crashes,orheavyperformancedegradations[49].Knowncausesofsoftwareagingincludememory
leaksandbloats,unreleasedfilelocks,datafragmentation,andnumericalerroraccumulation[21].
SeveralMachineLearningtechniqueshavebeenappliedtopredicttheexhaustionofresources
preemptively.Gargetal.[49]estimatetime-to-exhaustionofsystemresources,suchasfreemem-
ory,fileandprocesstablesizes,andusedswapspace,usinginstrumentationtoolsavailableunder
theUNIXoperatingsystem.Resourcemeasurementsarecollectedonseveraloperatingworksta-
tionstoconstructtimeseries,whichareannotatedwiththefailurecauseincaseofoutage.Trends
aredetectedandexhaustiontimeisquantifiedusingregressiontechniquesandseasonaltesting.
Inadditiontothetime-basedmeasurementofresources,Vaidyanathanetal.[136]investigate
theeffectofsoftwareagingduetothecurrentsystemworkload.Asemi-Markovrewardmodelis
fittedfromtheavailableworkloadandresourcedataunderUNIX,wherethemodelstatesrepre-
sent different workload scenarios, and the association to a specific state is identified employing
Hartigan’sk-meansclustering.Time-to-exhaustionofmemoryandswapspaceisestimatedwith
a non-parametricregression techniquefor each workload state separately. Alonso et al. [4] con-
siderthecaseofnon-linearandpiecewiselinearresourceconsumptionadoptinganensembleof
linearregressionmodels,selectedusingadecisiontreeonthesameinputfeaturesoftheregres-
sion model (a combined set of hardware and software host metrics). Decision trees are chosen
becausetheyofferatrade-offbetweenaccuracyandinterpretability.Theauthorsproposetouse
theirinterpretabilityforroot-causediagnosisaswell(Section4.4.2).
Softwareagingcanbecontrastedwithsoftwarerejuvenation[57],acorrectivemeasurewhere
theexecutionofapieceofsoftwareistemporarilysuspendedtocleanitsinternalstate.Software
rejuvenationcanbeperformedatthesoftwareandOSlevel.Commoncleaningoperationsinclude
garbagecollection,flushingkerneltables,re-initializinginternaldatastructures[136].According
to Castelli et al. [21], software rejuvenation fits naturally inside a cluster environment (but sim-
ilar considerations are true for any distributed computation system, e.g., cloud), because of the
already present node failover mechanisms and the possibility to schedule rejuvenation and ag-
ing prediction routines. To this end, authors distinguish between periodic (or synchronous) and
prediction-based (or asynchronous) rejuvenation policies, where the latter requires a prediction
modelforfuturesoftwarefailures.Thefailurepredictionmodelcanbelongto(butisnotlimited
to)thecategoryofresourceexhaustionpredictorsdescribedabove.
ACMTransactionsonIntelligentSystemsandTechnology,Vol.12,No.6,Article81.Publicationdate:November2021.

81:16 P.Notaroetal.
AI has been used in the past to suggest efficient rejuvenation scheduling policies. The same
Castellietal.[21]applystochasticrewardnetstomodelservicedowntimesanddrawconclusions
ontheefficiencyofrejuvenationpolicies.Theiranalysisconsidersbothtime-basedandprediction-
basedpolicies.Forthelatter,theyresorttoresourceexhaustionpredictionalgorithmstoestimate
futurefailureperiods,idealforrefreshingtheinternalstateandexaminetheexpecteddowntimeas
afunctionofthepredictionmodelaccuracy(orpredictioncoverage).Bothperiodicandprediction-
basedpoliciesareshowntobeabletoreducedowntimesignificantly,withprediction-basedmeth-
odshavingalargerimprovementoverall(−60%downtimeat90%coverageversus−25%withopti-
maltime-based),whilehigh-frequencyperiodicpoliciescanbettertoleratesimultaneousfailures
(−95%versus−85%ofprediction-basedmethods).
InReference[137],Vaidyanathanetal.buildupontheirworkload-inclusiveMarkovprediction
approach[136]toderiveoptimalperiodicrejuvenationpolicies.Tocapturethemanifestationof
rejuvenationandfailurebehavior,theydevelopacomprehensivetransition-basedmodelbetween
three states (working, failure, and rejuvenation). The model parameters (such as the period of
rejuvenation)areoptimizedtoreachdifferentobjectives(e.g.,maximumsteady-stateavailability
orminimumdowntimecost).Asimilarstrategyallowsonetoimprovethepreventivestrategies
ofadistributedsystemduringitsdesignstage.
4.1.4 Checkpointing. A concept linked to software rejuvenation is checkpointing, i.e., the
continuousandpreemptiveprocessofsavingthesystemstatebeforetheoccurrenceofafailure.
Similar to software rejuvenation, checkpointing tolerates failures by occasionally interrupting
the execution of a program to take precautionary actions. Different from software rejuvenation,
during checkpointing the interruption period is used to save the internal state of the system
to persistent storage. In case a fatal failure occurs, the created checkpoint file can be used to
resume the program and reduce failure overhead. Checkpointing techniques are common in
distributed computing, Checkpointing is also frequently used in large-scale computing systems,
although with the increase of scale the higher error rates make it less practical [62, 95]. To this
end,theconceptofmulti-levelcheckpointingwasintroduced:checkpointsarecreatedatdifferent
component levels, and based on the component resiliency and the permissible time overhead, a
differentcheckpointingstrategyisselectedforeachlevel.
Asinthecaseofsoftwarerejuvenation,AIisusedtomodelafaultyexecutionworkloadunder
differentcheckpointingstrategiesandselectthemostsuitablestrategyaccordingtodifferentobjec-
tives.Again,checkpointingcanbestaticordynamicdependingontheschedulingofcheckpoints.
AllthepapersinvestigatedoperatewithintheframeworkofMarkovprocesses[62,95,114].Oka-
muraetal.[114]developadynamiccheckpointingschemeforsingle-processapplicationsbased
onreinforcementlearning.Inparticular,Q-learningisusedtoobtaintheoptimalcheckpointingby
studyingtheasymptoticbehaviorofpolicies.Theapproachisespeciallyusefulinscenarioswith
unknownfailurecharacteristics.
Moodyet al. [95] describea multi-level checkpointingsystem forlarge HPC systems. To esti-
mateexecutiontimesunderdifferentconfigurations,themulti-levelsystemisexpressedasajoint
StochasticMarkovModelwiththedefinitionofcomputationandrecoverystatesandtheintroduc-
tionofassumptionssuchasthecostofcheckpointingandthefailurerateofthesystem.Thefinal
checkpointing schemes are claimed to offer high recovery efficiencies (85%) at a 50× increased
failurerate.
Jangjaimonetal.[62]presentanincrementalcheckpointingstrategyformulti-threadedappli-
cationsinacloudenvironment.TheirsystemmakesuseofanAdjustedMarkovModeltopredict
turnaroundtimeintheexecutionofprograms,incorporatingboththeeffectofhardwarefailures
and potential resource revocation events. The model also takes into account monetary aspects
ACMTransactionsonIntelligentSystemsandTechnology,Vol.12,No.6,Article81.Publicationdate:November2021.

ASurveyofAIOpsMethodsforFailureManagement 81:17
startingfromcostandunavailabilityassumptions.Accordingtotheirexperimentalresults,anadap-
tivemulti-levelcheckpointingschemeisbeneficialforcloudparadigmswithresourcerevocation,
allowing reduced checkpoint sizes, shorter execution times (up to −25%), and lower down costs
(upto−20%).
4.2 OnlineFailurePrediction
The fundamental idea behind failure avoidance is the anticipation of errors. The prediction of
failuresisthereforeanessentialactionforproactivemanagementoffailures.Theprevioussection
hasillustratedhowestimatingthedistributionoffuturefailuresisvaluabletooperatepreemptively
againstthem.Inallpreviousinstancesofprediction,however,forecastingwasstrictlyconnected
tothespecificpreventiontaskundertakenandalsolargelydependentontheavailablepreventive
actions(e.g.,softwarerejuvenation).Moreover,exceptresourceexhaustionpredictionanddynamic
checkpointing,allpreviousinstancesofpredictionoperateusingassumptionsderivedinanoffline
setting,estimatingtheprobabilityoffailuresoccurringinabsoluteratherthanestimatingthetime
to the next failure. A prediction of failures on-the-fly allows one to be aware of future failures
butalsotoknowinadvancetheremainingusefultorecovery,vitaltotimelydeployrecoveryand
failovermechanisms.
This section discusses this second category of proactive approaches, which are specialized in
predictionofcomputersystemfailuresinthisonlinefashion.Onlinefailurepredictionidentifies
futureruntimeerrorsbyassessingthecurrentstateofthesystem[122].Howfarintimetheseer-
rorscanbeforeseendependsontheleadtimeofthepredictor,i.e.,thetimebetweentheprediction
and the instant when the failure occurs; the validity of the prediction information also depends
onthepredictiontime,whichisthelengthofthetimewindowwherethefailuremayoccur.To
thesepredictionqualitymeasures,wealsoaddthewarningtime,ametricdescribingthetimere-
quiredtoperforminferenceandsignalafuturefailure.Naturally,apredictionisusefulonlyifit
can warn operators with sufficient advance before the failure occurs (i.e.,t warn < t lead). From
a functional perspective, an online failure predictor is comparable to a detector and is, as such,
evaluatedintermsofaccuracy,precision,recallandtheotherassociatedmeasures.Wediscusson-
linefailurepredictionapproachesintotwosubcategories:hardwarefailurepredictionandsystem
failureprediction.
4.2.1 HardwareFailurePrediction. Inlarge-scalecomputinginfrastructures,hardwarereliabil-
ityrepresentsoneofthemostrelevantpracticestoachieveserviceavailabilitygoalsindistributed
services.Duetothemagnifyingeffectofthelargenumbersinvolvedandthecommercialnecessity
todeploycommoditycomponentsindatacenters,hardwarerepresentsthemostvulnerableaspect
fromafailureperspective.AccordingtoVishawanathetal.[138],8serversof100areexpectedto
encounteratleastonehardwareerrorperyearofoperation.Moreover,themachinesaffectedby
errorsarelikelytorequiremorethanonerepairperyear(withanaverageoftworepairs),showing
asuccessivecorrelationpatternbetweenfailures.Accordingtothesamework,hardwarerepairs
fora100k-scaledatacentercanamounttomillionsofdollars.Itisthereforecrucialfromtheindus-
trialperspectivetoinvestigatewhichfactorsinfluencetheappearanceofhardwarefaultsforthe
endgoalofimprovingdesignchoicesanddeployingfailurepredictors.
Harddrivesarethemostreplacedcomponentsinsidelargecloudcomputingsystems(78%)and
oneofthedominantreasonsforserverfailure[138].Machineswithahighernumberofdisksare
alsomorepronetoexperienceadditionalfaultsinafixedtimeperiod.Thisfacthasledhard-drive
manufacturerstoadoptcommonself-monitoringtechnologies(suchasSelf-monitoringAnaly-
sisandReportingTechnology(SMART))intheirstorageproductssince1994[100].Therefore,
ACMTransactionsonIntelligentSystemsandTechnology,Vol.12,No.6,Article81.Publicationdate:November2021.

81:18 P.Notaroetal.
itshouldnotbesurprisingthatharddrivefailurepredictionrepresentsthemostinvestigatedtarget
forfailureprediction.
Severalstudieshaveinvestigatedthefailurecharacteristicsofharddrivestoidentifycommon
patterns.Forinstance,Pinheiroetal.[118]conductedalarge-scalestudyonoverahundredthou-
sanddiskdrivesusedinproductionbyGoogleandvaryinginstoragesize,speed,andmanufacturer.
Theresultsofthisstudycouldnotidentifyanyconsistentcorrelationbetweenfailurerateandhigh
temperatureorhighutilizationlevels.However,someSMARTfeatureswereshowntocorrelate
wellwithahigherfailurerate.However,SMARTmetricswerealsoshowntobelikelyinsufficient
forsingle-diskpredictions,asthemajorityoffaileddrivesdidnotmanifestanySMARTerrorsig-
nal before faults. A predictor based solely on SMART attributes is therefore likely to have good
specificitybutlowsensitivityunlessadditionalfeaturesareintroduced.SMARTdataisstillcon-
sideredusefultoevaluatereliabilityandrisktrendsinsideadiskdrivepopulation.Intheworkof
Vishwanath et al. [138], different other attributes are investigated from a population of disks in
Microsoftservers.Byconstructingdecisiontreesforfailurepredictiontwodiscriminationfactors
areidentified,datacenterandmanufacturer,whilethetypeofworkload,thepositioninrack,the
serverage,andtheconfigurationareallfoundtobeofnosignificanceforpredictingfuturedrive
faults.
Hamerlyetal.[54]presenttwodifferentBayesianlearningapproachesfordiskfailureprediction
fromSMARTattributescollectedonareal-worlddatasetof1936drives.Thefirstmethodworksas
anunsupervisedanomalydetector,whereamixtureofNaïveBayesdiscretesubmodelsistrained
toestimatetheposteriorprobabilityofobservation,andahard-setthresholdisusedtoseparate
anomalouseventsfromnormalbehavior.ThesecondmethodconsistsofasupervisedNaïveBayes
classifier with binned continuous variables. The approach achieves a recall of 0.33 with a false-
positiverateof0.0067.Bothmethodsoperatebypredictingafailureatthesnapshotlevel,sothe
temporalevolutionisnottakenunderconsideration.
Different from previous works [54, 101], Zhao et al. [164] treat SMART data as a time series,
arguing for the importance of temporal information. Their approach employs Hidden Markov
andSemi-Markov Models(HMM/HSMM)toestimatethesequenceoflikelyeventsfromthe
disk metric observations, which are obtained from a dataset of approximately 300 disks (where
approximatelytwo-thirdswerehealthy).Onemodelistrainedfromhealthydisksequences,one
fromfaultydisksequences.Attesttime,thetwomodelsareusedtheestimatethesequencelog-
likelihoodand thecorrespondingclassisselectedbasedonthehighestscore. Bycombining the
HMMapproachwithanSVM,theyclaimtoobtainarecallof0.52at0falsealarmrate.
Murrayetal.[101]testtheapplicabilityofseveralMachineLearningmethodsusingasliding
window approach, where the last n samples constitute the observation for predicting an immi-
nent failure. Naïve Bayes, kernel SVMs, and Naïve Bayes Expectation-Maximization as already
proposed by Reference [54] are implemented and compared. Features are selected from SMART
datausingstatisticalrelevancetests.SVMsachievetheirhighestperformancewitha50.6%recall
and 100% precision. The approach was tested on a dataset composed of 369 drives (with an ap-
proximate 50/50 split), which is then also used in a work by Wang et al. [143] where an online,
similarity-baseddetectionalgorithmispresented.RelevantSMARTfeaturesareselectedviaMin-
imum Redundancy Maximum Relevance (mRMR), then the input data is projected into a
Mahalanobisspaceconstructedfromthehealthydiskpopulationsothatfaultydisksdeviatemore
fromthedistribution.Faultydisksareagainrecognizedwithaslidingwindowapproachsothat
when the mean deviation inside a window appears anomalous an alarm is raised. An anomaly
is identified with four different statistical tests. This approach improves, at 0 false-positive rate,
the detection rate up to 67%, on the same dataset with less computational effort. Moreover, it is
shown how for 56% of the faulty cases it was possible to intervene with an advance of at least
ACMTransactionsonIntelligentSystemsandTechnology,Vol.12,No.6,Article81.Publicationdate:November2021.

ASurveyofAIOpsMethodsforFailureManagement 81:19
20hbeforethefailure.ComparableresultsareobtainedbyZhuetal.[167],wheremultilayerper-
ceptronandSVMmodelsareconstructedandtrainedonanin-house(Baidu)datasetofSMART
datacomprising23,395drives(433faulty).Assuminga12-hrecoverywindow,theirSVMmodel
obtainsafailuredetectionrateof68.5%witha0.03%falsealarmrate.Theneuralnetworkmethod
achievesfarhigherdetectionrates(94.62–100%),attheexpenseofahigherfalsealarmrateaswell
(0.48–2.26%)anditisthereforeindicatedformonitoringwiththehighestreliabilityrequirements.
ThesameSMARTdatasetisusedbyXuetal.inapaper[149]thatintroducesRecurrentNeural
Networks(RNN)toharddrivefailureprediction.SimilartoReference[164],themethodcanana-
lyzesequencesdirectlyandtomodelthelong-termrelationshipstakesadvantageofthetemporal
dimensionoftheproblem.Differentlyfrompreviousapproachesthatapplybinaryclassification,
themodelistrainedtopredictthehealthstatusofthedisk,providingadditionalinformationon
theremainingusefullifeofdisks.Onthefailurepredictiontask,however,theapproachstillout-
performstheotherevaluatedmodelsintermsofdetectionrate(96.08–97.78%)andfalsealarmrate
(0.004–0.03%).
Inawork[78]relatedtoReference[167],twonewevaluationmetrics(migrationandmismigra-
tionrate)areintroducedtomeasuretheefficiencyofdatamigrationconcerningforecastedfaults.
RNNsandGradient-boostedDecisionTrees(GBRT)areimplemented(regressiontreesorigi-
nally proposedinReference[77])toaccomplishthreetasks:predictfaultydisks,asintheusual
setting;measuretherateofwrongfulandmissedmigrationsperformedusingtheinformationof
theclassifier;estimatetheresiduallifeofthedisks,bypredictingtherisklevelofeachdisk(1to
5forfaultydisks,6forhealthyones).Forresiduallifeprediction,resultsarecomparedusingthe
newlydefinedmetricsatvariablemigrationrate.TheRNNapproachshowsahigherfaulty-level
predictionaccuracy(27.02–39.90%)andtheGBRTmodelbetterprotectionfromdatalosswitha
highersuccessfulmigrationrate(84.91–87.54%).
Mahdisoltani et al. [89] tackle failure prediction in storage media at the sector level. Their
method employs a few SMART features as target prediction variables rather than explanatory
variables. They experiment both with HDD and SSD data, with five different Machine Learning
approaches. For HDD data the analysis illustrates detection rates of sector errors similar to the
onesoftraditionaldiskfailureprediction(70–90%at2%false-positiverate).InSSDs,whereRan-
domforestsobtainthebestcomparativeresults,thepredictionisnotaspromising(50–60%detec-
tionrateat2%).SSDfailurecharacterizationisalsothefocusofNarayananetal.’swork[104],a
large-scalestudyconductedon2.5yearsofproductiondataandcoveringover500,000solid-state
disksfromdifferentMicrosoftdatacenters.SSDfailuresarecorrelatedtodatacenter,workload,and
device-levelfeaturesviastatisticallearning.Thebestandonlyreportedpredictionmodel(random
forest) obtains a precision of 87% and a recall of 71%. Features directly representing underlying
problems (such as count of data errors and reallocation sectors), number of NAND writes and
workloadfactorsarereportedasthemostimportantdiscriminatorsoffailures.Accordingtothe
sameauthors,theclassificationrulesobtainedbytheanalysisenabletheidentificationoflikely-
to-faildeviceswithsufficientadvancetotakepreventiveactions,especiallyinthecaseofissues
heavilydependentontheworkload.
All previous approaches are used in an online setting after an initial setup or training step is
performedoffline.Thisposestheproblemofhowtointegrateadditionaldata,especiallyinthose
caseswherethescarcityofpositivetrainingexamplesimposesanonlinelearningapproach,able
to update the characteristics of faulty disks as soon as new failures appear. To this end, Xiao et
al. [148] propose the use of Online Random Forests, a model able to evolve and behave adap-
tively to the change in the data distribution via online labeling. The approach is tested on a
datasetcoveringover10,000disks,wheretheresultsshowhowthealgorithmcanincreaseperfor-
manceover20months,reachingdetectionratesof93%andmorewithreasonablylowalarmrates
ACMTransactionsonIntelligentSystemsandTechnology,Vol.12,No.6,Article81.Publicationdate:November2021.

81:20 P.Notaroetal.
(0.73–0.76%intheofflinesetting).ThepredictionperformancesarecomparabletoaRandomForest
andoutperformtheotherapproachestested(SVMsanddecisiontrees).
Althoughmostofthescientificinterestisconcentratedarounddiskfailures,aminorgroupof
contributions,focusingonfailurepredictionforothercomponents,ispresent.Maetal.[88]elevate
thediscussiononstoragereliabilitytothelevelofRAIDgroups.Theymodelthefailureprobability
of a vulnerable RAID group using a Naïve Bayes assumption, where the failure of whole disks
inside the group is independent of the others and is estimated from metrics such as reallocated
sectorcounts.Astatisticalmodelisbuiltfromdatacollectedon5,000RAIDgroups.Resultsshow
howthepresentin-placemechanismswereabletopreventavastmajorityofconsecutivefailures
(98%fortriplefailures).
Costaetal.[33]investigatetheoccurrenceofmain-memoryerrorsforHPCapplications.They
proposeandevaluatemethodsfortemporalandspatialcorrelationamongmemoryfailures.Tem-
poral correlation analyses logs to estimate the prior rate of errors that, integrated with timing
information,allowsonetoestimatetheremainingnumberoferrorsatthejoblevel.Spatialcorre-
lationmeasurestheprobabilitytoexperienceafailureafterobservingerrorsinadjacentbits.In
thesamepaper,amemorymigrationapproach,basedontheavailableinformationatruntime,is
presentedandevaluated.Theresultsshowhow63%ofmemory-inducedfailurescouldbeavoided
thankstothepredictionandmigrationmechanismsdeployed.
Davisetal.[37]presentFailureSim,aCloudsim-based[51]simulatorforstatusassessmentof
hardwareinclouddatacentersusingdeeplearning.MultilayerPerceptronsandRNNsareusedto
assess13 different host failing states, each associatedwith a specificcomponent (CPU, memory,
I/O,etc.).Thesystem,testedbyassigningavariableworkloadtoascalablenumberofVMs,can
identify50%offailinghostsaccurately,andpredict89%offuturefailsbeforetheiroccurrence.
Zhangetal.[161]dealwiththeproblemsoffailurepredictionanddiagnosisinnetworkswitches.
Theirmethod,basedonsystemloghistory,proposestoextracttemplatesfromlogsandcorrelate
themwithfaultybehavior.Theirextractionmethodandsimilarapproachesarecomparedonthe
extractiontasks,andthetemplatesthereobtainedareusedtotrainaHiddensemi-MarkovModel.
Theproposedmodel,whichshowsthebestperformancefigures,achieves32%precisionand95%
recall,demonstratinghighsensitivitytoclearfault-signalingmessages,butlowprecision(andthus
highfalsealarmrate)overall.
Zheng et al. [165] propose a method based on RNN to estimate the Remaining Useful Life of
systemcomponents.Theyarguethatthetemporalnatureofsensordatajustifiestheuseof long
short-termmemory(LSTM)-basedRNNs,duetotheirabilitytomodellongterm-dependencies.
TheyexperimentwiththreeRULpublicdatasetsandcomparetheirmethodwithotherMachine
Learning approaches in terms of Root Mean-squared Error (RMSE), showing how their ap-
proach obtains the best RUL prediction performance (RMSE = 2.80, 54.47% improvement over
CNNs).
4.2.2 SystemFailurePrediction. Insteadofinvestigatingtheoccurrenceofphysicalcomponent
failures,futuresystemavailabilitycanalsobeestimatedthroughsymptomaticevidenceanddepen-
dencymodelingassumptionsatthesoftwarelevel.Pastapproachesforsystemfailureprediction
aremostlybasedontheobservationoflogs,whichconstitutethemostfrequentdatasource,KPIs
andhardwaremetrics,whicharetypicallyusedinshorterpredictionwindowsandaremorefre-
quentlyassociatedwiththefailuredetectionproblemaswell.Systemfailurepredictionareapplied
on different abstraction levels depending on the target software component under investigation
(job,task,container,VM,ornode).
SomeearlycontributionsareassociatedwithfailurepredictionintheIBMsupercomputerBlue-
Geneproject.Liangetal.[81],forinstance,applydifferentclassificationalgorithmsforBlueGene,
ACMTransactionsonIntelligentSystemsandTechnology,Vol.12,No.6,Article81.Publicationdate:November2021.

ASurveyofAIOpsMethodsforFailureManagement 81:21
usingrealeventlogstopredictfatalfailuresinsidefixedtimewindowsofobservation.Inputfea-
tures are parsed from structured logs based on the severity, total count, and distribution of log
events inside an observation window. Features obtained from the previous window are used to
predictfailureinthenextone.Intheevaluationphase,fourclassificationalgorithms(SVM,RIP-
PER,BMNN,k-NN)arecomparedusingprecision,recall,andF-score.Thesizeoftheprediction
windowappearstohavealargeimpactonthefinaldetectionperformance.Fromtheexperiments,
theidealwindowsizeisestimatedbetween6and12htobalanceutilityeffectivenessandaccuracy.
TheBi-modalnearestneighborapproachproposedinthepaperprovidesthebestresultsoverall,
leadingtoanF-measureof70%(and50%)with12-h(and6-h)predictionwindows,respectively.
Cohen et al. [31] investigate an approach based on Tree-augmented Bayesian Networks
(TANs)toassociateobservedvariableswithabstractservicestates,forecastanddetectSLOvio-
lations and failures in three-tiered Web services. The system is based on the observation of sys-
temmetrics,suchCPUtime,diskreads,swapspace,andKPI-relatedmeasures,likethenumberof
servedrequests,allinterdependentlymodeled(inadditiontothedependentvariable,thepredicted
state).Theoptimalgraphstructure,includingtheidealsubsetofinputmetrics,isselectedutilizing
agreedystrategy.Theapproach,originallydevelopedfordetection,canalsobeusedtodiagnose
failuresthankstotheinterpretabilitypropertiesofTANs(seeSection4.4.2).Twoseparateexperi-
mentsareusedforvalidation,amulti-tieredJavaserverapplication,andanApacheservertestbed,
bothinjectedwithsyntheticworkloadsvaryinginconnections,requestrate,andtype.Theresults
forforecasting,applied1or5mininadvanceoffailures,showhighdetectionrates(83–93%)and
false-alarmratesvaryingbetween9.1%and24%dependingontheexperiments.
Salfner et al. [123] train HSMM for online prediction of failures in event sequences collected
fromerrorlogs.OneHSMMistrainedonfailingsequences,asecondoneonnon-failingsequences.
Then,thesequencelikelihoodofthemodelsdetermineswhichofthetwoscenariosismorelikelyto
occur.Theapproachisevaluatedonlogsofacommercialtelecommunicationsystemandcompared
withotherpredictiontechniques,achievinganF-measureof0.7419(precision0.852,recall0.657).
Theobservedfalse-positiverateis0.0145.
Chalermarrewongetal.[23]proposeasystemavailabilitypredictionframeworkfordatacenters,
basedonautoregressivemodelsandfault-treeanalysis.Theirautoregressiveintegratedmovingav-
erage(ARIMA)modelworksontimeseriesofworkloadandhardwaremetrics,wherethresholds
arefixedtodetectcomponent-levelsymptoms(suchashighCPUtemperature,baddisksectors,
memoryexhaustion),whichalsoconstitutetheleavesofthefaulttree.Usingthesesymptomsand
thetreestructure,amodelofdependenciesincombinationallogicdeterminestheavailabilitystate
deterministically.Anadvantageoftheseapproachesthatitimplicitlyprovidesgranularinforma-
tionfordiagnosis.Theexperimentalresultsshowhighpredictionaccuracy(97%)butahighrate
offalsealarmsaswell(precisionis53%).
TheHORApredictionsystem[119]adoptsaholisticapproach,wherearchitecturalknowledgeis
usedwithonlinetime-seriesdatatopredictQoSviolationsandservicefailuresindistributedsoft-
ware systems. Component dependency and failure propagation models, in the form of Bayesian
Networks,areusedtoassociatecomponentfailures,predictedfromsystemmetricswithautore-
gressivepredictors,tosystem-wideproblems.Testedonamicroservice-basedapplication,thenew
approach is compared to a monolithic approach (not using architectural knowledge) by inject-
ing memory leaks, node crashes, and system overloads during execution. The HORA approach
achievesahigherrecall(83.3%versus69.2%)andAUCROC(0.920versus0.837,+9.9%)compared
tothemonolithicapproach.Theproposedapproachisalsomoreviablewhenahighfalsealarm
rate(≥10%)isacceptable,whilethemonolithicapproachismoreadequateforpredictionsinthe
0–10%falsealarmrange.
ACMTransactionsonIntelligentSystemsandTechnology,Vol.12,No.6,Article81.Publicationdate:November2021.

81:22 P.Notaroetal.
Fronzaetal.[44]describeafailurepredictionapproachbasedontext-analysisofsystemlogsand
SVMs.First,logfilesareparsedandencodedusingatechniquecalledRandomIndexing,wherefor
eachoperationinsidealogline,indexvectorsareassignedtoobtainalatentrepresentationofthe
text.Then,byscanningthroughthelogcorpus,contextvectorsforeachoperationarecomputed,
so that co-occurrence of operations can be taken into account. Finally, sequences of operations
arerepresentedastheweightedsumofcontextvectorscorrespondingtotheoperationsencoded
inside.TheserepresentationsofsequencesconstitutetheinputofaweightedSVM,trainedwiththe
objectiveofminimizingfalsenegatives.Resultsshowhowaweightedapproachcancompensate
foradecreaseinspecificity(alwaysgreaterthan80%)toimproverecall(50%).
Similarly,inReference[160]RNNsareappliedforfailurepredictionfromlogs.Theapproachis
composedofaclusteringalgorithmusedtogroupsimilarlogs,apatternmatcherusedtoidentify
commontemplatesinsidesimilarlogs,alogfeatureextractorbasedonnaturallanguageprocess-
ing,andasequentialneuralnetworkarchitecturebasedonLSTMcells,usedtopredictthefailure
statuswithinthepredictiveperiod.TheuseofLSTMsisalsomotivatedbytheirsequentialmod-
elingabilitiesandtherarityoffailures.Theapproachiscompared,usingrealdatacollectedfrom
two enterprise server clusters, with other Machine Learning methods (SVM, logistic regression,
randomforest)intermsofprecision-recallAUC.At70%precision,theLSTMmethodshowsthe
highest failure sensitivity with a recall value of 0.909. LSTMs are able to detect signs of failures
earlierthanothermethods(73minonaverage).
LSTM networks are also used by Islam et al. in Reference [61], a large characterization study
ofjobfailuresconductedonaworkloadtracedatasetbyGoogle.Failuresarepredictedatthejob
andtasklevel,whereajobisacollectionoftasksandeachtaskisasingle-machinecommandor
program.Failuresarepredictedfromresourceusagemeasures,performancedata,andtaskinfor-
mation(completionstatus,user/node/jobattributes).Fortaskfailureprediction,thefinalF1-score
ofthesystemis0.87(precision=0.89,recall=0.85,FPR=0.11).Forjobfailureprediction,theap-
proachachievesaF1-scoreof0.81(precision=0.80,recall=0.83,FPR=0.20).Thepredictionalgo-
rithmcanbeusedtoreduceresourcewaste(downby12–20%intheexperiments)byre-submission
oflikely-to-failjobsandtasks.
4.3 FailureDetection
Inthissection,westartdiscussingreactivefailuremanagementmethods,whichoperatetolimit
theconsequencesoffailuresaftertheyhaveoccurred.Theyaremotivatedbythefactthat,even
withthemostadvancedpreventionandpredictiontechniques,theoccurrencerateoffailurescan
neverbefullyreducedto0.Somereactiveapproaches,forexampleinroot-causeanalysisoranom-
alydetection,canalsobeusedtogetabetterunderstandingofhowfailuresarecausallyrelated
andpropagateovertime,ortocomprehendwithwhichtemporalcharacteristics(variance,burst
frequency,periodicity,seasonality)failuresareassociated.
Thedetectionoffailuresviamonitoringoperationscanbeacomplexandtedioustaskforhu-
manoperators.Chenetal.[26]reporthowintheadministrationofacommercialwebsite,75%of
the recovery time was spent on average for detection. The automatic discovery of performance
problems and errors allows operators to dedicate less time identifying service-related problems
whileprovidinginsightsonwhichfailuresmustbeprioritizedinthediagnosisstepbasedonthe
frequency observed in the detection phase. Automated failure detection is based on a variety of
monitoring tools, ranging from simple print statements (which constitute the fundamental unit
ofsystemlogs)tomorecomplexinstrumentationtechniquesorentireframeworks.Wedivideour
discussionoffailuredetectioninanomalydetection,Internettrafficclassification,andlogenhance-
menttechniques.
ACMTransactionsonIntelligentSystemsandTechnology,Vol.12,No.6,Article81.Publicationdate:November2021.

ASurveyofAIOpsMethodsforFailureManagement 81:23
4.3.1 Anomaly Detection. According to our quantitative results [113], failure detection is
treatedasananomalydetectionprobleminthelargemajorityofcontributionsrelatedtoITsystem
management.Anomalydetectionisamultidisciplinarytaskthatdealswithfindingpatternsindata
thatdonotconformtotheexpectedbehavior[24].Theinterestinanomalydetectionismotivated
bythepossibilitytoobtainactionableinformationtodealwithdiseases,frauds,cyber-attacks,sys-
temoutages,andfaults,dependingonthetargetdomain.Anomalydetectionoperatesbyderiving
amodelofnormalbehavior,andbytestingnewobservationsagainstthismodel.AnomalyDetec-
tionisappliedintheAIOpscontextundertheassumptionthatfailuresgenerateirregularbehavior
inITsystems(errors)acrossasetofmeasurableentities(orsymptoms),suchasKPIs,metrics,logs,
orexecutiontraces.Anomalydetectionisalsousedtodetectcyber-attacks,congestion,andsub-
optimalresourceutilization,whichcanallbecausesoffuturefailures.Becauseobtaininglabeled
examplesistime-consuming,anomalydetectionsystemstypicallyrelyonunsupervisedlearning.
Threearethemostprominenttechniquesusedinsuchcontext:clustering[11,127],dimensionality
reduction[72,151]andneuralnetworkautoencoders[7,131,150,159].Oneoftheearliestexam-
plesofunsupervisedlearningforsystemworkloadcharacterizationisMagpie[11],abehavioral
modelingtoolchainfordistributedsystems.Magpie’sinstrumentationisbasedonfine-grained,in-
kerneleventloggingtoolsavailableunderWindows,abletomeasureresourceconsumptionand
executiontimesaccurately.Theeventsregisteredwiththistoolareusedtoreconstructrequests
andapplybehavioralclusteringtoobtainasmallsetofuniquerequesttypes,eachassociatedwith
aspecificworkloadmodel.Inthepaper,behavioralclusteringallowsonetomodelrealisticwork-
loadsmorepreciselythanbygroupingrequestsbyURL.Arealisticworkloadmodelisbeneficialto
identifyanomalousresourceconsumption,besidesenhancingcapacityplanningandperformance
testing.
At the network level, Lakhina et al. [72] monitor network links via SNMP data to detect and
diagnoseanomaliesinnetworktraffic.TheapplyPCAonlinkflowmeasurementscollectedover
timetoseparatetrafficinnormalandanomaloussubspaces.Theyclassifyprincipalcomponents
innormalandabnormal(settingathresholdontheexplainedvariance),thenidentifyanomalies
byreconstructingthenewobservationsusingabnormalcomponents.Ifthereconstructionerror
exceedsapredefinedthreshold,thenthenewdatapointisconsideredanomalous.Theirapproach
isvalidatedusingsyntheticandrealvolumeanomalies,thelatterdetectedwithtraditionalclass
forecastingalgorithms.Inafollow-upwork[73],asimilarapproachbasedontrafficfeaturedistri-
butionentropyisproposed.Thepapershowshowthesamesubspacemethodcanexploitpacket
information,suchassourceandtargetdestinationaddressorport,todetectsecuritythreatsand
serviceoutages,aswellastoprovidepreliminarydiagnosticinformation.
SeveralapproachesapplyunsupervisedlearningonunivariatetimeseriesconstructedfromKPI
and metric observations [127, 150]. Sharma et al. [127] propose CloudPD, an end-to-end failure
tolerance system performing failure detection, diagnosis, and classification in virtualized cloud
environments(seealsoSection4.4.2).Thepaperproposestocollectavarietyofmeasuresatthe
VM and physical machine level, including resource utilization, operating system variables, and
applicationperformancemetrics.ThepaperthenproposesthreedifferentunsupervisedMachine
Learningapproachesforanomalydetection:k-nearestneighbors(k-NN),HMMs,andk-means
clustering. The k-NN detection approach is evaluated on three different benchmarks, where it
beatsfourproposedbaselineswithanaveragehigherrecall(83–87%)andalowerfalsealarmrate
(12–17%).Donut[150]performsanomalydetectiononseasonalKPItimeseriesusingdeepVaria-
tionalAutoencoders(VAE)andwindowsampling.Theapproachiscomparedonthreedifferent
datasetsof18KPIstoOpprentice[86]andabaselineVAEperformanceintermsofF-score(ranging
from0.75to0.9),AUC(0.7–0.9)andaveragealertdelay(4to12min).Oneoftheconclusionsofthe
ACMTransactionsonIntelligentSystemsandTechnology,Vol.12,No.6,Article81.Publicationdate:November2021.

81:24 P.Notaroetal.
authorsisthatautoencoderapproachesrequireabnormalsamplesinadditiontonormalbehavior
samples.
Themostrecenttime-seriesapproachesfocusonmultivariateanomalydetectionusingautoen-
coders[7,131,159].Twoadvantagesofamulti-dimensionalanalysisaretheabilitytomodelthe
inter-correlationsbetweendifferentmetrics/components,andtoprovideinterpretableresultsfor
root-cause analysis, by attributing the detected anomaly to a specific metric or component. MS-
CRED[159]usesaconvolutional-recurrent(ConvLSTM)autoencoderarchitecturetocapturetem-
poral patterns at different scales and thus identify abnormal time steps. In the evaluation study,
MSCRED outperforms the baselines (SVM, ARMA, GMM, CNN) with an F1-score of 0.82–0.89,
whilebeingabletoidentifyanomaliesonscalesw =10,30,60s.Bycomputingthereconstruction
errorsonindividualtimesequences,MSCREDcanalsoidentifyrootcausesmoreeffectively(top-3
recall=0.75–0.80).OmnyAnomaly[131]proposesarecurrentVAEmodelusingstochasticvariable
connectionandplanarnormalizingflow.AsforMSCRED,thereconstructionerrorcanbeusedto
interpret anomalies and connect back to individual time series. OmniAnomaly achieves a detec-
tionF1-scoreof0.8599onthreerealdatasets,includingservermetricdata(SMD[108])collected
fromalarge-scaleInternetcompany.SMDisalsousedforevaluationinUSAD[7],whichapplies
adversarial-basedtechniquestotheautoencoderarchitectureforfasterandmorestabletraining.
In USAD, the anomaly score is parametrized so that the sensitivity can be adjusted rapidly and
on multiple levels for real industrial applications. On five real datasets, USAD achieves results
comparabletoOmniAnomaly(F1=0.791forboth),whilereducingtrainingtimeby547timeson
average.
Althoughinthemajorityofcasesreallabeledsamplesarenotavailable,itmaybepossibleto
obtain behavioral set of rules or an execution model for the system. The model information be-
comesalsoveryrelevantwhenfailuresneedtobediagnosed(seeSection4.4.2).Withtheuseof
a behavioral model, different pattern-matching approaches can be developed. For example, hav-
ing access to a probabilistic context-free grammar (PCFG), which defines the likelihood of
event chains to occur in sequential input, allows an anomaly detection algorithm to single out
unlikelystructuresanddetectanomalies.Magpie[11]alreadyproposestheuseofPCFGstomodel
eventsequencesanddetectanomalousrequests.AsimilarapproachisusedinReference[26]to
detectfailuresbysearchingforanomaliesinexecutionpaths(i.e.,traces).Thispathinformation
is especially valuable to localize and diagnose failures (see also discussion of Reference [26] in
Section4.4.2).
More often, a behavioral model of the system is inferred from the past execution history, of-
ten expressed in the form of logs. An example of such a model is constituted by Finite State
Machines(FSM)[12,45].InaworkbyFuetal.[45],logentriesarefirstmappedtotheircorre-
spondingtemplateversion,calledlogkey.Similarlogentries,usedtoidentifylinetemplates,are
groupedviaclustering.Then,FSMsarelearnedtomodelprogramworkflowsfromlogevidence.
The model so obtained can be later used to verify the correct execution of programs and detect
softwareproblems.Theentireapproachpipelineistestedonlogfilesfromtwodistributedcom-
putingframeworks,achieving95%accuracyonlogkeyextractionduringthedetectionofdifferent
typesoffailuresmanuallyinserted.Beschastnikhetal.adoptasimilarapproachwiththeirsystem
CSight[12].Asthemaingoaloffailuredetectionistoenableroot-causeanalysis,theauthorsalso
performedauserstudyontheusefulnessofFSMdiagramscomparedtoothergraphicaldebugging
toolsforidentifyingexecutionerrors.FSMdiagramsenabledstudysubjectstoidentifyproblems
moreoften(+11%)comparedtosubjectswhowereshown6/8time-spacediagrams,consideredless
understandable by them. In Reference [29], a causal model of request executions is constructed
fromtheavailablecomponent-leveltracelogs.Themodel,calledTheMysteryMachine,identifies
different types of predefined causal relationships between components via iterative refinement,
ACMTransactionsonIntelligentSystemsandTechnology,Vol.12,No.6,Article81.Publicationdate:November2021.

ASurveyofAIOpsMethodsforFailureManagement 81:25
Table6. SummaryofDescribedAnomalyDetectionMethods,CategorizedbyDataSourcesandAlgorithm,
withCorrespondingAdvantagesandDisadvantages
DataSources
Paper(s) KPIs&Metrics secarT srehtO Algorithm Advantages/Disadvantages
sgoL
etairavinU etairavitluM
|      | •   |     |     | interpretability,applicabilityto |
| ---- | --- | --- | --- | -------------------------------- |
| [31] |     |     | TAN |                                  |
othertasks/requiressupervision
|     | •   |     | Random | highaccuracy,onlinere-training/ |
| --- | --- | --- | ------ | ------------------------------- |
[86]
|     |     |     | Forest | requiressuperviseddata       |
| --- | --- | --- | ------ | ---------------------------- |
|     | •   |     | Markov | unsupervised,onlinelearning/ |
[110]
|     |     |     | Chain        | black-boxmonitoring              |
| --- | --- | --- | ------------ | -------------------------------- |
|     | •   |     | Unsupervised | generalpurpose,nolabelsrequired/ |
[127,150]
|             |     |     | Learning    | univariateanalysisonly       |
| ----------- | --- | --- | ----------- | ---------------------------- |
|             | •   |     |             | multi-dimensionalanalysis,no |
| [7,131,159] |     |     | Autoencoder |                              |
labelsrequired/trainingstep
|         |     | •   |     | enablesRCA/requirestemplate |
| ------- | --- | --- | --- | --------------------------- |
| [12,45] |     |     | FSM |                             |
discoverystep
| [18,41,92,162] |     | •   | RNN | robust,accurate,unsupervised/ |
| -------------- | --- | --- | --- | ----------------------------- |
requiresparsing,trainingstep
simple,unsupervisedmethodfor
| [151] |     | •   | • PCA | free-textdata/requiresparsing,low |
| ----- | --- | --- | ----- | --------------------------------- |
interpretability
|         |     |     | Clustering/ | enablesmultipleAIOpstasks/ |
| ------- | --- | --- | ----------- | -------------------------- |
| [11,26] |     | •   |             |                            |
|         |     |     | PCFG        | requiresend-to-endtracing  |
interpretability,enablesRCA/
Causal
| [29] |     | •   |     | applicableinsequentialsystems |
| ---- | --- | --- | --- | ----------------------------- |
Inference
only
high-level,largeapplicability/
| [87] |     | •   | SVM |     |
| ---- | --- | --- | --- | --- |
requiressuperviseddata,tracing
|         |     |     | PCA/Feature  | specific/exclusivefor           |
| ------- | --- | --- | ------------ | ------------------------------- |
| [72,73] |     |     | •            |                                 |
|         |     |     | Distribution | network-trafficanomalydetection |
supportedbythepasttracehistory.Accordingtotheauthors,TheMysteryMachinecanbeused
to conduct an anomaly analysis of service requests based on segment features. In particular, it
can used to aggregate similar requests by structure and latency via comparison of the segment
structure of anomalous requests. Thanks to this inspection, it was possible to identify unneces-
sarydebuggingcomponentsreturnedoccasionallyinuserrequests.InaworkbyXuetal.[151],
textanalysisandinformationretrievaltechniquesareappliedonconsolelogsandsourcecodeto
findabnormalpatternsduringtheoperationoflarge-scaledatacenters.Inparticular,statevariables
andobjectidentifiersareextractedautomaticallyfromparsedlogs,andtheirfrequencyindiffer-
entdocuments(expressedinterminverse-documentfrequency,TF-IDF)isanalyzedwithPCAto
detectanomalieswithathreshold-basedruleonthereconstructionerror,similartoReference[72].
AnomaliesdetectedwiththePCAapproacharealsousedtotrainsuperviseddecisiontrees,useful
foroperatorstointerpretanomaliesandacceleratetheidentificationofproblems.
In recent years, RNN have been applied for log-based anomaly detection [18, 41, 92, 162]. Du
et al.’s DeepLog [41] uses RNNs based on LSTM layers to learn patterns from logs and detect
anomalies.AsinFuetal.[45],logentriesareinitiallymappedtocorrespondinglogkeys.Then,
DeepLogpredictstheprobabilitydistributionofthenextlogkeyfromtheobservationofprevious
ACMTransactionsonIntelligentSystemsandTechnology,Vol.12,No.6,Article81.Publicationdate:November2021.

81:26 P.Notaroetal.
log keys, similar to a natural language model that predicts the next token from the observation
of the rest of the sentence. A log key is considered abnormal if it does not appear in the topk
keys ranked by probability. The paper also proposes an online learning strategy based on user
feedback.Theapproachisvalidatedonself-generateddatasetsfromHDFSandOpenStack,where
itiscomparedtoothermethodsforthesametask.At100%recall,DeepLogdramaticallyreduces
thefalse-alarmrate(from38.2–40.1%to1.1–1.7%)usingonlyasmallfractionofdatafortraining
(1–10%).Brownetal.[18]alsoworkonlog-basedanomalydetection,presentinganword-token
RNN language model for raw logs based on five attention mechanisms (reaching AUCROC ≥
0.963). The paper also proposes to analyze attention weights to provide statistical insights, un-
derstand global behavior and improve decision making. Although their work is tested for intru-
sion detection tasks, it can be used for other detection tasks, e.g., detect failures at the request
andserverlevel.Thesameauthorsalsorecognizeitspotentialtopredicthardwarefailuresonline.
LogAnomaly [92], while adopting the language model approach, proposes the use of template
embeddings(template2vec)tobetterextractsemanticinformation,bywhichsimilarlogkeyscan
be matched and merged automatically, without requiring human feedback. Thanks to template
vectors,OmniAnomalycanalsolearnquantitativepatternsinadditiontosequentialpatterns.All
theseimprovementsenabletofurtherreducefalsealarmratecomparedtoDeepLog(F1=0.8632).
LogRobust[162]dealswiththeproblemofloginstability,causedbythechanginglogstatements
overtimeandnoiseinlogprocessing.Toaddressthis,LogRobustalsoemploysLSTMlayers,se-
manticvectorsandattention,butdifferentlyfromlanguagemodelapproaches,itdirectlypredicts
anomaliesbycomputingananomalyscore.Theapproachisvalidatedonindustrialandsynthetic
HDFSdata,withanaverageF1-scoreof0.81(+0.29)onunstablelogdata.
Whileunsupervisedlearningapproachesaregenerallymoreapplicable,supervisedlearningap-
proachesforanomalydetectionareviableinscenarioswherelabelsareavailableforbothnormal
andanomaloussamples.Moreover,alltypesofanomaliesneedtobeknownbeforehandandsuffi-
cientsamplesforeachtypemustarenecessary.Loetal.[87]investigatethedetectionoffailures
insoftwareasaclassificationproblem.Theirapproachminessetsofdiscriminativefeaturesfrom
executiontracesandusethemtotrainaSVMforclassifyingsoftwarebehaviorintonormaland
abnormal.Theapproachisvalidatedbyperformingseveralcontrolledexperimentswithrealtrace
data,obtainedfromprogramsoftheSiemenstestsuite[59]andMySQLdatabaseserver.Inboth
scenarios,faultsareinjectedartificiallywithdifferenttechniques.Theapproachshowsveryhigh
levelsofdetection,withAUCROCrangingfrom0.82to1.00.
AnothersupervisedclassificationapproachisproposedwithOpprentice[86].Opprenticeana-
lyzes KPI time series with Machine Learning to automatically detect anomalies online. Random
ForestsareappliedtoclassifyKPIpointobservations(composedofthreevariables)innormaland
abnormal behavior classes, with the possibility to set up a sensitivity threshold online. The ap-
proachalsoincludesanofflinealgorithmtoselecttheoptimalthresholdsatisfyingcustomlinear
constraints on the Precision-Recall plane. Finally, to overcome the labeling effort required by a
supervisedapproach,alabelingtoolforKPItimeseriesliketheonesobservedinthepaper.
AnotherinstanceofsupervisedanomalydetectionistheTANapproachofCohenetal.[31](the
algorithmandexperimentalsetuparediscussedinSection4.4.2).SLOcompliancyinWebserversis
usedassupervisiondatatolearnasystembehavioralmodelfromcombinationsofmetrics,applica-
bletoperformforecasting,detection,anddiagnosis.Whenusedforonlinedetectiononsynthetic
workloads,theTANapproachwasabletodetect91.9%–93%offailureswithafalsealarmrateof
6.4–16.9%.
Inconclusion,wereporttheworkofNguyenetal.[110],laterdescribedinSection4.4.1.While
designedforblack-boxfaultlocalization,theproposedsystemisdeeplyintegratedwithanabnor-
malchangepointdetectionalgorithmforsubsequentroot-causeanalysis.Thisdetectionapproach
ACMTransactionsonIntelligentSystemsandTechnology,Vol.12,No.6,Article81.Publicationdate:November2021.

ASurveyofAIOpsMethodsforFailureManagement 81:27
is based on Markov chains with dynamic thresholding and operates at the component level to
pinpointirregularsystemmetricvalues.TheMarkovmodelisalsoaninstanceofonlinelearning
andsoitisindicatedforapplicationscenarioswithvariabletimecharacteristics.
4.3.2 InternetTrafficClassification(ITC). AtaskconnectedtonetworkfailuredetectionisIn-
ternet Traffic Classification (ITC). ITC allows categorizing packets exchanged by a network
systemtoidentifynetworkproblems,tooptimizeresourceprovisioningandimproveQuality-of-
Service[43,97].Itcanbeappliedtoanalyzethelocalnetworkflow,theincomingserverrequests
from the outside, or the outgoing response. ITC is also widely used for cybersecurity purposes,
suchasintrusiondetection[97,142].Allthesesupportedareasareconnectedtotheappearance
offailuresandthisfactmotivatesthediscussionofITCaspartoffailuremanagement.ITCcanbe
seenasaparticularinstanceofnetworkanomalydetection.However,inpractice,thedifferences
inmethodology(emblematicofaclassificationproblemratherthanadetectionproblem)anddata
sources(networktrafficratherthanKPIsandmetrics)justifyaseparatediscussion.
Moore et al. [97] propose to use Supervised Machine Learning to classify the observed Inter-
net traffic. Their work selects relevant features from a set of 248 discriminative variables (such
aspayloadsize,TCPport,etc.)totrainaNaïveBayesclassifierandseparatetrafficaccordingto
differentcategorysets(e.g.,application-wise,maliciousnessvs.legitimacy,etc.).Theapproachis
lateraugmentedwithkernelestimationtoovercomethelimitationsoftheGaussianassumption
introduced.Inafollowingwork[8],theBayesianframeworkisextendedtoBayesianNeuralNet-
works,inthearchitecturalformofMultilayerPerceptrons,reaching95–99%accuracy,depending
onthespecifictestcase.
Este et al. [43] develop a framework based on SVM models for TCP traffic classification. TCP
communication is analyzed at the flow level rather than at the individual packet level: single-
direction traffic flows between nodes are classified with multi-class kernel SVMs, depending on
theapplication-levelprotocoltheyutilize.Single-class(oneversusall)modelsarealsotrainedto
obtaindecisionboundariesandsetapartoutlierpackets.Themodelsurpassescorrectprediction
ratesof90%onthreedatasetsundertest.
Wang et al. [142] propose an end-to-end classification method for encrypted traffic based on
1DCNN.TheinputoftheCNNisrepresentedbyrawpacketdatagroupedaccordingtodifferent
conventions,suchasflowandsession.Theapproachisevaluatedonapublicdataset(ISCX)con-
tainingbothVPNandnon-VPNdata,whereitisusedtoassigntheobservedtrafficinoneofthe14
categories,definedbasedontheapplication(e.g.,E-mail,streaming,chat,etc.).The1DCNNmodel
improvesthestateoftheartonthedescribeddatasetbyapproximately10%intermsofprecision
and8%intermsofrecall.
4.3.3 Log Enhancement. Another task connected to failure detection is log enhancement. Its
goal is to improve the quality and expressiveness of system logs, which are frequently used for
detectionanddiagnosistasksbyIToperatorsandAIOpsalgorithms.
Zhuetal.[168]proposealoggingsuggestiontool,calledLogAdvisor,tolearnpracticallogging
suggestionsfromexistingloginstances.Incodesnippets,severalstructural,syntactical,andtextual
featuresareextractedandfilteredbasedoninformationgain,fromwhichadecisiontreeislater
trainedtosuggestloggingofsnippetsasabinaryclassificationproblem.Theapproachiscompared
to several other baselines, including a random 50% predictor, a previous algorithmic approach
calledErrLog[155],andotherMachineLearningmodels.LogAdvisorisshowntoreducelogging
overheadcomparedtoErrLogwhenloggingisnotrequired,eventhoughitislesspreciseandit
mayoccasionallynotplacesomeinformativeprintstatementscomparedtothemoreconservative
ErrLog.
ACMTransactionsonIntelligentSystemsandTechnology,Vol.12,No.6,Article81.Publicationdate:November2021.

81:28 P.Notaroetal.
In Reference [163], an approach for automated placement of log printing statements (Log20)
basedoninformationtheoryisproposed.First,entropyisshowntobeaninformativemeasurefor
theplacementofprintingstatements.Then,agreedydynamicprogrammingalgorithmforplacing
printingstatementsisimplemented.Theoverallapproachistestedonfourpopulardistributedsys-
tems,whereLog20canbeasinformativeasdifferentlog-levelpolicies,whilesignificantlyreducing
theprintoverhead(from1.58entriesperrequestdownto0.08fortheINFOloglevel).
4.4 Root-causeAnalysis(RCA)
Failuredetectionistheprocessofcollectionofsymptoms,i.e.,observationsthatareindicativeof
failures.Root-causeanalysisis,instead,theprocessofinferringthesetoffaultsthatgenerateda
givensetofsymptoms[130].Inacomplexanddistributedsystem,itisfirstrequiredtoisolateto
restricttheanalysistotheresponsiblecomponentorfunctionalsubsystem,ataskthatwecallfault
localization.Onlythenananalysisofthepossibleerrorsourcescanbeperformedwithroot-cause
diagnosis.Asinthecaseofanomalydetection,wetreatsomeassociatedtasks,usefultosupport
root-causeanalysisinthelocalizationanddiagnosisprocedures.
4.4.1 FaultLocalization. Faultlocalizationisaboutidentifyingthesetofcomponents(devices,
network links, hosts, software modules, etc.) interested by a fault that caused a specific failure.
Whentreatingthisproblem,itisimportanttoclarifythescopeoflocalization,asscaleandtargets
maybeambiguousinthiscontextseveralreasons.First,becausefaultlocalizationcanoperateat
various physical, hierarchical scales, from the entirety of a datacenter down to single chips. In
large-scaleservices,inthepresenceofhundredsofthousandsofmachines,itisimportanttore-
stricttheoriginofamanifestederrortotheindividualserverlevel.Itisalsopossibletoperform
problemdeterminationatthephysicaldevicelevel,suchasharddrivesandprocessorchips.Finally,
thehighestlevelofgranularityisreachedbyroot-causediagnosis,wheretheindividualfailurerea-
sonsareinvestigated(seenextsection).Second,fromafunctionalperspective,faultlocalization
mayimplyinvestigatingwhichmoduleinabstract,functionalcomponents(e.g.,thenetwork,or
thesourcecode)isaffectedbyafault.Inthissecondperspective,thelocalizationscaleisdiscon-
nected from the physical scale. Software fault localization is applied to analyze the source code,
regardless of whether the interested piece of software is deployed on thousands or tens of ma-
chines.Inthenetworkcase,itmaybesufficienttounderstandiffaultsarepresentinthenetwork
sothatspecializednetworkoperatorscanidentifytherootcausesindependently.
Some works describe general-purpose fault localization techniques. For instance, Nguyen
et al. [110] present FChain, a black-box fault localization system to pinpoint faulty components
inanonlinecloudsetting.FChainreliesonlow-levelsystemmetricstodetectperformanceanom-
alies,thenobserveshowsuchanomalypatternspropagatetoidentifyfaultycomponents.Perfor-
manceanomaliesareidentifiedviaonlinemetricforecastingusingadiscreteMarkovmodelwith
anadjustabledetectionthreshold.Then,allcomponentsdisplayingananomalyaresortedbyman-
ifestationtimeadexaminedinsequencetofilteroutspuriouscorrelationsaccordingtodifferent
techniques, such as looking at interdependency between components or examining the overall
propagation trend. The approach is tested on different commercial frameworks for distributed
computing.Inthissetting,thelocalizationperformanceoftheapproachiscomparedwithexisting
black-boxlocalizationschemes,whereanimprovementbothintermsofprecision(+90%)andre-
call(+20%)isobserved.Accordingtotheauthors,FChainimposesanoverheadof1%onthecloud
systemperformance.
Severalapproaches[80,83,132]addressfaultlocalizationbycorrelatingabnormalchangesin
KPIvaluestoparticularcombinationsofattributes(representing,e.g.,geographicalregions,ISPs,
hosts,buckets,etc.).Thiscombinationsofvaluesarethensymptomaticofafaultforthatparticular
ACMTransactionsonIntelligentSystemsandTechnology,Vol.12,No.6,Article81.Publicationdate:November2021.

ASurveyofAIOpsMethodsforFailureManagement 81:29
cornercase.Hotspot[132]appliesMonteCarloTreeSearchandhierarchicalpruningtoefficiently
examineattributecombinationsandmeasurehowtheyrelatetosuddenchangesinthePageView
metric. This approach allows one to reduce hours-long manual efforts down to 20 s on average
(300×speedup).Squeeze[80]proposesasimilarapproachbasedonacombinedtop-down,bottom-
upsearchstrategyandanewlydefinedcorrelationmetric(generalizedpotentialscore,GPS).These
improvementsenableSqueezetolocalizerootcausesincasesoflowerstatisticalsignificance,when
testedonsynthetically-injectedreal-worlddatasets(F1=0.86–0.90).Linetal.[83]applypattern
miningtechniquesonstructuredlogstodiscoverassociationrulesX →Y,whereY isapredefined
attributecombinationdescribingafailure.Theyapplyefficientprocessingtechniquesasrowpre-
aggregation, in-memory databases and the FP-growth mining algorithm to render the runtime
complexityofassociationruleminingfeasible.Theirworkalsoproposesfivedifferentusecases
applicableinlarge-scaleserviceinfrastructures.
Other works apply fault localization techniques specifically to the network infrastructure of
computersystems.TheworkofLakhinaetal.[72],alreadypresentedinSection4.3.1fornetwork
anomalydetection,appliesthesamePCA-basedtechniquepreviouslydescribedtoidentifyfaulty
linksaswell.Forthediagnosistask,insteadofconsideringthesubspacedistanceofreconstructed
datapoints(whichwasthereusedasameasureofanomaly),thedirectionofdivergenceisunder
examination. The routing matrix defines the direction of divergence from normal behavior for
eachlink,whilethemostlikelyfaultylinkisselectedastheonewiththelowestreconstruction
errorafterremovingtheestimateddivergenceeffectcausedbythatlink.
WithSherlock[9],Bahletal.localizesourcesofperformanceproblemsinenterprisenetworks
byconstructingprobabilisticinferencegraphsfromtheobservationofpacketsexchangedinthe
network infrastructure. Nodes of the inference graph are divided into root-cause nodes (corre-
sponding to internal IP entities), observation nodes (corresponding to clients), and meta-nodes,
which model the dependencies between the first two types of nodes. Each node is also associ-
atedwithacategoricalrandomvariablemodelingthecurrentstate(up,troubled,down),whichis
influencedbyothernodesvia thedependencyprobabilities.Learning theinferencegraph corre-
spondstolearnthedependencyprobabilitiesforeachedgeinthegraphbyobservingthepackets
exchanged between nodes during normal operation. Once the graph is available, measurements
fromtheobservationnodecanbeusedtoretrieveasetofstate-nodeassignmentvectors,corre-
spondingtotheestimatedoperationalstateofthenetwork.Accordingtotheresultsofthepaper,
Sherlock was able to narrow down more than 87% of the failures from 350 to 16 possible root
causes,whileidentifying32%morefaultsthantheirpreviousworkShrink[64].ThesameShrink
(seeSection4.4.2),althoughtechnicallyaroot-causediagnosistool,canalsobeappliedtolocalize
physical-layerfaultsinnetworks.
SoftwareFaultLocalization(SFL)isfaultlocalizationinsoftwarecomponentsthroughsource
codeanalysis.AnSFLsystemtypicallyreturnsareportcontainingalistofsuspiciousstatements
orcomponents.Itcanbeconsideredsimilartosoftwaredefectprediction(Section4.1.1),becauseof
thesimilarityofinvestigationtargetsandanalysistools;however,differentlyfromSDP,SFLrelies
onobservedfailurepatternsobtainedfromproductionrunsandtestcases,ratherthanpredictions
offuturefaultybehaviorbasedoncodemetrics.
Renierisetal.[121]implementamethodforSFLbasedonsimilaritybetweenprogramexecution
profiles(orspectra),whichareobtainedfromexecutiontracestorepresentsuccessfulandfaulty
runs of programs. In the described approach, successful runs are stored as spectra in a nearest-
neighborquerydatabase.Afaultyrunisthenusedasasearchterminthisdatabase,sothatthe
nearestneighborrunsreturnedbythequery(inparticular,theirdifferencesfromthefaultyrun
intermofcodecoverage)canbeusedtoproduceafaultlocalizationreportwithplausibletarget
codeareasresponsibleforthefault.Thespectralrepresentationofrunsishereconstitutedbysets
ACMTransactionsonIntelligentSystemsandTechnology,Vol.12,No.6,Article81.Publicationdate:November2021.

81:30 P.Notaroetal.
of executed program blocks, on which the Hamming distance is computed to perform neighbor
queries.Inthesamepaper,ameasurequantifyingtheexaminationeffortrequiredtofindabug,
calledtheT-score,isintroducedanditislaterusedbyotherapproachesasacomparisonmeasure
[30,85,145].
Zelleretal.[156]proposeDeltaDebugging,analgorithmforthedeterminationofstatevariables
causing a change in the outcome of execution runs. Via graph modeling techniques, the state
differences between failing and passing runs are examined to understand how state alterations
influencetheoutcomeofruns.Inthisway,itispossibletoextractthevariableinterestedbythe
faultfromthevariationspace.Inthespecificcaseofthepaper,theprogramstateisrepresentedas
amemorygraph.Inafollowingwork[30],thepreviouslyproposedsearch-in-spaceapproachis
complementedbyasearch-in-timeapproach,forthosesituationswhereafailuredependsonwhen
variablesareassignedwrongvalues,aneventcalled“causetransition.”Throughthisconsideration,
programmers can reduce the amount of code that needs to be examined. During the evaluation
phaseconductedontheSiemenstestsuite[59],thecause-transition(CT)approachiscompared
toReference[121]intermsofT-score,whereCTcanpinpointdefectsfor5.43%ofalltheruns,with
more than one-third (35.66%) of these runs requiring examination of less than 10% of the entire
code.Thedescribedapproachalsoprovidesinsightsaboutthecausesbehinderrorsandtherefore
supportsroot-causediagnosisaswell.
Liuetal.[85]adoptastatisticaldebuggingapproach(SOBER)basedontheanalysisofpredicate
evaluations in failing and passing runs. In predicate-basedstatistical debugging, the conditional
probabilityofobservingafailuregiventheobservationofaparticularpredicateisestimatedfor
amultitudeofpredicatespresentinthecode.Predicateswithahigherprobabilityaremorelikely
tocontainasoftwarebugortobeintheproximityofone.Inthispaper,aprobabilisticmodelof
predicatesisintroduced,includingarankingcriteriontoevaluatetheconnectionofpredicatesto
softwarebugs.TheapproachistestedontheSiemenstestsuiteandcomparedusingT-scoreand
detectionratetotheCTapproachofCleveandZeller[30],pushingstate-of-the-artresults:when
adeveloperiswillingtoanalyze1%oftheinterestedcode,SOBERcancapture8.46%ofthebugs
(4.65%forCT);at20%coverage,thedetectionrateclimbsto73.85%(39%forCT).
Abreu et al. [1] propose a Bayesian reasoning approach (BARINEL) based on the analysis of
programspectra,thistimeincorporatedinaprobabilisticframeworkusedtoestimatethehealth
probabilityofcomponents.InBARINEL,whichcanbeappliedtolocalizemultiplefaultssimultane-
ously,coverageflagsareusedasaspectralrepresentationoftestsoncomponents.Amodel-based
reasoning system, founded on propositional logic, is constructed from the interaction between
components.Thismodelisthenaugmentedwithfailureprobabilitiesthatareestimatedviamaxi-
mumlikelihoodtoobtainanapproximatereasoningapproach,completedbyacandidateranking
heuristicstodealwiththehighdimensionalityoftheproblem.BARINELcanfind60%ofsoftware
faultsbyexamininglessthan10%ofthesourcecode.
Wongetal.[145]proposeDStar(D*),atechniquetoautomaticallysuggestsuspiciouslocations
forfaultlocalization.Inparticular,D*adoptsanewmethodtocomputesuspiciousnesscoefficients
fromtestcoveragedataandrunoutcomes.ThismethodisbasedonamodificationoftheKulczyn-
skicoefficientswiththeadditionofavariableexponentiationfactor(denotedbysuperscript*,as
inthename).TheapproachiscomparedwithseveralpreviousSFLtechniquesacross24programs
and38techniques,whereD*isshowntobemoreeffectiveonsinglefaultlocalizationthanprevious
coefficient-basedmethods.
4.4.2 Root-cause Diagnosis. Root-cause diagnosis identifies the causes of behavior leading to
failures,byrecognizingtheprimaryformoffault.Forthisreason,itistypicallytreatedasaclas-
sificationproblem.Duetotheinherentcomplexityandinter-dependencybetweencomponentsin
ACMTransactionsonIntelligentSystemsandTechnology,Vol.12,No.6,Article81.Publicationdate:November2021.

ASurveyofAIOpsMethodsforFailureManagement 81:31
Table7. SummaryofDescribedFaultLocalizationMethods,CategorizedbyDataSourcesandTarget
Component,withCorrespondingAdvantagesandDisadvantages
|               | DataSources |              | Targets  |            |                              |
| ------------- | ----------- | ------------ | -------- | ---------- | ---------------------------- |
| Paper(s)      |             |              |          |            | Advantages/Disadvantages     |
| edoCecruoS    |             | cffiarT.wteN |          |            |                              |
|               |             | noitacilppA  | erawdraH | retnecataD |                              |
|               | scirteM     |              | krowteN  |            |                              |
|               | sIPK        | sgoL         |          |            |                              |
| [1,30,85,121, |             |              |          |            | pointsdirectlytorootcause/   |
| •             |             | •            |          |            |                              |
| 145,156]      |             |              |          |            | applicableonlytosoftwarebugs |
unsupervised,onlinelearning/
| [110] | •   |     | •   | •   |     |
| ----- | --- | --- | --- | --- | --- |
black-boxmonitoring
general-purpose,unsupervised/
| [80,132] | •   |     |     | •   | complexanalysis,requiresspace |
| -------- | --- | --- | --- | --- | ----------------------------- |
pruningtechniques
|     | •   | •   | • • |     | unsupervised,accurate,robust/ |
| --- | --- | --- | --- | --- | ----------------------------- |
[9]
requirestopologyandtrafficinfo
general-purpose,unsupervised/
| [83] |     | •   |     | •   | complexanalysis,requiresspace |
| ---- | --- | --- | --- | --- | ----------------------------- |
pruningtechniques
specific/exclusivefor
| [72] |     | •   | •   |     |     |
| ---- | --- | --- | --- | --- | --- |
network-trafficfaultlocalization
softwaresystems,itisconsideredachallengingtask[6].Inthecontextofrequesttracinganddiag-
nosis,thePinpointsystem[25]isoneoftheearliestandmostsalientcontributions.Theapproachis
basedontheanalysisofend-to-endtracesofclientrequests,throughwhichrequestsareclustered.
Thislaterenablesthecorrelationofsimilarfailureswithcomponentscausingthem.Themethod
istestedonasimulatedwebe-commerceenvironmentwhereartificialfaultsinvolvingsingleand
multiplecomponents,areinjected.Inafollowingwork[26](seealsoSection4.3.1),decisiontrees
and association rules are learned to correlate failed requests with root causes. Both approaches
identifythegreatmajorityoffailures(93%),withvariablefalse-positivepredictionrates(23%and
50%,respectively).
Kandulaetal.[64]developShrink,afailurediagnosistooldesignedforopticallinksinIPnet-
works,butcertainlyextendabletoothernetworkingscenarios(theauthorsmention,forexample,
thediagnosisofroutersandservers).Shrinktakesasinputtheconfigurationofthenetwork(both
physicalandsoftware-defined)andthecurrentIPlinkstatustoestimatethemostlikelyexplana-
tionfor theobservedfailure. Thediagnosis taskismodeled usinga bipartiteBayesianNetwork,
connectingthesetofIPlinkswiththesetofphysicalcomponentsonwhichtheyrelytooperate;
thenetworkisthenaugmentedwithlow-probabilityedgesbetweenunrelatednodestoimprove
robustness.Diagnosesareinferredbyfindingthemaximum-likelihoodstateinthephysicallink
spacegiventheobservationfromtheIPlinkstatus.TheNP-hardsearchproblemisapproximated
usingagreedyinferencealgorithm.SinceShrinkperformsbothdetectionanddiagnosis,thesuc-
cessrateandfalse-positive/-negativeratearemeasuredintheevaluationphase.Shrinkexcelsat
the diagnosis task (99.5%) in the presence of an accurate configuration description, while other
approachesoutperformitfordetection[9].
SherLog [154] performs post-mortem analysis of logs and source code to diagnose software
faults(suchascodebugsandconfigurationerrors).SherLogconsistsofthreemainbuildingblocks:
alogparser,whichextractstructurefromlogmessagesandidentifiescorrespondingprintstate-
ments(logpoints)inthesourcecode;apathinferenceengine,whichreconstructsexecutionpaths
ACMTransactionsonIntelligentSystemsandTechnology,Vol.12,No.6,Article81.Publicationdate:November2021.

81:32 P.Notaroetal.
fromlogentriesandknownlogpoints;avalueinferenceengine,whichexecutestheprogramsym-
bolicallytore-computethevalueofvariablesalongtheinferredpath.Thistypeofinformationis
directly applicable to diagnosis by programmers. SherLog is designed as a general tool, applica-
blewithoutpreviousknowledgeofthesystem(e.g.,thestructureoflogs)required.Thereforeits
validityhighlyreliesontheinformationobtainablefromsystemlogs.Moreover,theapproachde-
scribed is designed for single-machine, non-concurrent programs where the log information is
self-enclosedinoneuniquesource.Fordistributedandmulti-processapplications,considerations
maydiffer.
Attariyanetal.[6]introduceX-Ray,atooltodiagnoseperformanceanomaliesinproductionsoft-
ware.X-rayimplementsperformancesummarization,anewlyintroducedtechniqueforroot-cause
diagnosis.Performancesummarizationassociatesexecutioncoststofine-grainedoperations(such
assystemcalls)andthenassignscoststorootcausesemployingcontrolflowanalysismodeledad
theeventlevel.Theoutputcorrespondstoalistofrootcausesrankedbyassociatedperformance
costs.Thesystemisdesignedtoidentifyconfigurationerrorsanduserinputproblems.Duringthe
evaluation,measuringresponsetime,root-causeidentificationability,andnecessarycomputation
overhead,X-Raywasabletoidentifythefirstrootcausein16of17testsperformedonfourdif-
ferent server frameworks (Apache, Postfix, PostgreSQL, and lighttpd), with an average runtime
overheadof2.3%inproductionandanaverageidentificationtimeof2min.
WiththeirsystemCloudPD[127],Sharmaetal.automaticallyconstructfaultsignaturesfrom
the observation of past failures in the cloud. These signatures, which are composed of pairs of
tracked variables and thresholds, are used at runtime to diagnose problems identified with the
behavioralmodelingengine(seeSection4.3.1)previouslydiscussed.Thesystemcandiagnosesev-
eralcloudandVM-relatedanomalies,suchasinvalidresourcesizing,VMfaultyreconfiguration,
orworkloadmixchange.Theaccuracyoftheirapproachrangesbetween83%and88%,depending
ontheemployedbenchmark.
Samiretal.[124]utilizeHierarchicalHiddenMarkovModels(HHMM)toassociateresource
anomaliestorootcausesinclusteredresourceenvironments,onthedifferentlevelsofcontainer,
node,andcluster.Markovmodelsareconstructedondifferentlevels,trainedwiththeBaum-Welch
algorithmusingresponsetimesequencesasobservations.Theidentificationapproachisevaluated
intermsofaccuracyandcomparedtotwootheralgorithms.Thepredictionsobtainedduringthe
identificationsteparealsofedintoarecoverycomponentforautomatichealing(seeSection4.5.3).
Inconclusion,thealreadymentionedapproachofCohenetal.[31](seeSections4.2.2and4.3.1)
can also be used to diagnose observed failures. The described TAN model correlates observable
metricstoSLOviolations.Ifduringthediagnosisthesameinputmetricsaremeasured,thenitis
possibletousetheprobabilisticmodeltoobtainalistofmetricscorrelatingwithspecificevents
orproblems.Whilethisinformationmaynotalwaysconstitutethefinaldiagnosis,theapproach
supportshumandiagnosiswithviablehypothesesandevidence.
4.4.3 Other Tools Supporting RCA. This section analyses other smart software tools that, al-
thoughtheydonotdiagnoseorlocalizefaultybehavior,canassistoperatorsanddeveloperswhile
investigatingdetectedproblemsandcan,thereforebeseenasancillaryresourcesforthemainroot-
causeanalysistask[3].Thesetoolsmayinclude,forexample,informationretrievalmechanismsto
quicklygatherevidenceofrecurrentproblems,liketheirrelativefrequency;ordependencymodels
fordistributedsystemsusedtounderstandcausalrelationshipsbetweeneventsand/orcomponents
toacceleratefuturediagnoses.
Aguileraetal.[3]describeseveralapproachestoidentifyperformanceproblemsindistributed
systemsbyanalyzingcausalpathdependenciesbetweenblack-boxcomponents.Causalpathpat-
ternsareextractedfrommessagetracesusingtwodifferentalgorithms,thefirstapplyingasearch
ACMTransactionsonIntelligentSystemsandTechnology,Vol.12,No.6,Article81.Publicationdate:November2021.

ASurveyofAIOpsMethodsforFailureManagement 81:33
heuristiconsinglemessagestoidentifynestedcallpairs,thesecondbasedonsignalprocessing.
Thealgorithmsarecomparedindifferentapplicabilityscenariosandtestedondifferentcategories
oftraces,bothsyntheticandreal.Theoff-lineanalysisproposed,whilenotdirectlyfocusingon
failures,canproveusefulfromtheperspectiveofIToperators,willingtoacquireacomponentde-
pendencymodel.Suchamodelcanthereforerepresentavaluabletooltodiagnosefailures.Similar
conclusionscanbedrawnforotherdependencymodelingapproaches[9,29].
Podgurskietal.[120]proposetouseMachineLearningalgorithmstoclassifyandgroupsoft-
warefailurestofacilitateerrorprioritizationanddiagnosis.Programsareinstrumentedtocollect
executionprofiledata,whicharethenusedtotrainalogisticregressionclassifiertopredictfailure
causes.Thefeaturecoefficientsobtainedduringthistrainingprocedureareusedtoselectrelevant
featuresfortheclusteringtask,whererelatedfailuresaregroupedusingthek-medoidsalgorithm.
Intheexperimentalphase,failurescollectedfromthreelargecompilerprogramsaregroupedac-
cording to the described method and the corresponding clusters are visualized in combination
with results from the classification phase. The experimental evaluation shows, with various ex-
periments,howforalargenumberofclusters(≥71%)themajorityoffailuresoriginatedfromthe
samecausewereassignedtothesamecluster.
Cohenetal.[32]presentamethodforextractingsignaturesdescribingthestateofarunning
system,whichcanbelaterusedtoretrievesimilarpreviousstates.Thesamemethodcanbeused
togroupsimilarproblemsandquantifythefrequencyofrecurringproblemsforprioritizationpur-
poses. Starting from the observation that recording raw system metrics as state representation
isineffectivefromaretrievalperspective,intheproposedapproachstatesignaturesincorporate
informationabouttherelationbetweentheService-levelAgreement(SLA)stateandtheabnor-
malitylevelofthemetricsmeasuredduringthestateobservation.Inparticular,relevantmetrics
areselectedandtheirvaluesarecharacterizedastypicaloratypical,bylearningajointdescriptive
modelofmetricandSLAstate(aspreviouslydoneinReference[31]).Individualmetricsarealso
marked as attributed, not attributed, or irrelevant to the SLA state, based on the interpretation
givenbythemodelforeachspecificmetric.Theseflagsconstitutethefinalsignaturerepresenta-
tion,incombinationwiththeSLAstatepredictedbythemodel.Thesignaturerepresentationsof
states are clustered using thek-means andk-medians algorithms. The approach is validated on
tracesfromtwodistributedapplications,servingsyntheticandrealproductionworkloads,show-
ingtheretrievalsystemtobesuccessfulinrecognizingdifferentperformanceproblems.Asimilar
approachisproposedinReference[14],wherethevaluesofperformancemetricsarecategorized
indifferentclasses(“hot,”“cold,”and“normal”)basedontheirquantiledistribution.Relevantmet-
ricsareselectedbymeasuringtheirpredictivepowerwhentrainingalogisticregressionclassifier
topredictSLAviolations.Fingerprintsareconstructedbothattheepochandcrisislevel,indicating
different durations in time for non-conformant episodes, and are compared using distance func-
tions.Theapproachcanassociatenewcrisestopastbehaviorin80%ofthecaseswithanaverage
runningtimeof10min.
With LogCluster [84], Lin et al. use a knowledge base, obtained via clustering, to quickly re-
trievelogsofrecurrentproblemsandfacilitateproblemidentification.Logs,whichareinterpreted
assequencesofdiscretelogevents,arefirsttransformedtoavectorrepresentationusingInverse
Document Frequency (IDF), where events represent terms. Then, logs are clustered using ag-
glomerative hierarchical clustering and one element for each cluster is selected as the represen-
tativeinstance.Atruntime,thesystemperformsqueriesontherestrictedsetofrepresentatives,
ratherthantheentireknowledgebase,reducingeffortsforsimilarity-basedretrieval.Intheevalu-
ationperformedonHadoopapplications(WordCount,PageRank)andMicrosoftinternalservices,
LogCluster outperforms previous approaches in retrieval relevance (measured in precision) and
numberoflogsequencesneededtobeexaminedtoidentifyfailures.
ACMTransactionsonIntelligentSystemsandTechnology,Vol.12,No.6,Article81.Publicationdate:November2021.

81:34 P.Notaroetal.
4.5 Remediation
Thankstotheproblem-specificknowledgegatheredduringthediagnosisstep,liketheidentifica-
tionofrootcausesortheisolationofafaultycomponent,itispossibletoinitiateasequenceof
automatic repair actions, which are here described as remediation. Remediation approaches are
oftenlinkedwithcertainconceptsofservicedeskmanagement,suchasticketroutingorticketso-
lutionrecommendation.RemediationhasexperiencedlessscientificcontributionslinkedwithAI
comparedtotheprevention,prediction,detection,anddiagnosistasks.Thisispossiblyduetothe
above-mentionedfactthat,oncethenatureoftheunderlyingproblemhasbeenclarifiedthrough
diagnosis, the recovery steps are almost immediately identifiable and attainable without resort-
ing to complex models. We divide the available contributions into three categories, constituting
successivestepstowardresolution:incidenttriage,solutionrecommendation,andrecovery.
4.5.1 IncidentTriage. Incidenttriageisthestepinproblemresolutiondealingwithcategorizing
areportedproblem.Thepurposeoftriageisoftentheassignmenttothecorrectexpertresolution
group[126,158].Triagecanalsobeusedtoselectasuitablediagnosisandremediationalgorithm.
Shao et al. [126] propose to mine resolution sequences, i.e., the steps followed by a problem
ticketfromreportingtoresolution,toimprovefutureticketroutingandspeeduprecovery.Ticket
routingsequencesareanalyzedemployingaMarkovModel,fromwhichseveralroutingalgorithms
aredevelopedandlatertestedintermsofeffectiveness,robustness,andapplicability.TheMean
numberofStepstoResolveisreducedfrom3.94to2.58(−34.52%)on2,634tickets.Theapproach
isentirelybasedontheobservationofresolutionsequencesanddoesnotrelyonticketcontent.
Zengetal.[158],however,proposewithKilotoclassifyticketdataonmultiplelevelsbyana-
lyzingsymptomdescriptionsofproblems.Theirworkdealswiththeticketlabelingproblemfrom
ahierarchicalperspective,whereticketsareassignedtoincreasinglyspecificsubclassesinatree
hierarchy.Theclassificationalgorithm,basedonBayesiandecisiontheory,introducesanewhier-
archicallossfunctionminimizingtheexpectedmisclassificationriskwhenmakingnon-leafpredic-
tionsinthetreelabelstructure.Agreedypredictionalgorithmisdeployedtoperformhierarchical
classification,withtheabilitytointegrateavailabledomainexpertknowledgeintheformofprior
probabilities.
4.5.2 SolutionRecommendation. Theapproachesheredescribedprovideimplementationsfor
recommending solutions to occurring problems. Most solutions are based on past incident his-
tory and rely on the annotation of solutions in a previous resolution window. Therefore, these
approaches mostly operate as retrieval systems that resemble the ones described for root-cause
analysisinSection4.4.3.Inthepresenceofannotatedsolutions,thoseapproachescanequallybe
aviablesolutionforthistask.
Zhou et al. [166] propose similarity-based algorithms to suggest the resolution of repeating
problemsfromincidenttickets.Thebasicapproachconsistsinretrievingk ticketresolutionsug-
gestionsusingak-NNapproach.Thesimilaritybetweenticketsisevaluatedbasedonamixtureof
theavailablenumerical,categorical,andtextualdata,forwhichindividualandaggregatesimilar-
itymeasuresaredefined.Thebasicsolutionisextendedtodealwiththeproblemoffalse-positive
tickets,presentinthehistoricalticketdataaswellintheincomingticketsrequiringanewsolution.
Tosolvethis,eachticketisclassifiedasrealorfalseusingabinaryclassifierwithak-NNapproach
andthenbyweighingticketimportancebasedonthepredictionoutcome.Thefinalsolutionrecom-
mendationtakesintoaccountbothimportanceandsimilarity.Thepaperalsoincorporatesother
ideasforimprovingfeatureextractionsuchastopicdiscoveryandmetriclearning.
Wang et al. [140] propose a cognitive framework based on the use of ontologies to construct
domain-specific knowledge and suggest recovery actions for tickets in IT service management.
ACMTransactionsonIntelligentSystemsandTechnology,Vol.12,No.6,Article81.Publicationdate:November2021.

ASurveyofAIOpsMethodsforFailureManagement 81:35
The approach is based on the analysis of free-form text present in summary and resolution de-
scriptionsintickets.First,domain-specificphrasesareextractedfromtextfieldsusingdifferentlan-
guageprocessingtechniques;then,anontologymodelisdevelopedtoprovidedefinitions,classes,
andinterconnectingrelationsofkeywords,forwhichahierarchyisalsoestablished;theobtained
modelcanthenbeusedtorecommendresolutionactionsbymatchingconceptpatternsextracted
in incoming and historical tickets via similarity functions (such as the Jaccard distance). In the
experimentalphase,theextractingaccuracyofconceptpatternsistestedwithgroundtruthlabels,
reachingthevalueof86.2%forthepredictionofrequiredactions.
InaworkpresentedbyFacebook[82],naturallanguageprocessingtechniquesaredeployedto
predictrepairactionsfromclosedtickets.Uptofiverepairactionsarerecommendedbyanalyzing
rawtextlogsasinputfeatures,withaccuracyrangingfrom50%to80%(noexperimentalevalua-
tionisdescribed).Inthesamepaper,otherin-housefailuremanagementsystemsareillustrated,
includinganonlineanomalydetectionalgorithmandanautomaticrepairengine.
4.5.3 Recovery. We define as recovery approaches those methods taking direct and indepen-
dent actions toward the resolution of a diagnosed problem. According to the analysis derived
fromourmappingstudy,nodistinctivecontributionhasbeenproposedtoperformdirectrecov-
ery actions with AI. The closest match is represented by the work of Samir et al. [124], where
acombineddetection/RCA/remediationframeworkassociatesdetectedanomaliestorootcauses
utilizingHHMM(seeSection4.4.2).Thelaststepoftheirpipelineconsistsinperformingrecovery
actionsbasedontheinsightsobtainedintheidentificationstep.Specificrecoveryactionsarede-
finedforeachfailurecaseinapredefinedmanner.Theefficiencyoftherecoverystepisassessed
viaMTTRandrecoveryrate.
By applying the term in a broader sense, we may consider as recovery all those preventive
actionsthatdonotrequirediagnosisinformationtobeundertaken.Thisisthecase,forexampleof
reactivemechanismsappliedincombinationwithonlinefailurepredictionmechanisms(described
inSection4.2),toperformdatamigrationorcheckpointing[33,78]preemptively.
5 CONCLUSION
5.1 CurrentandFutureTrendsinFailureManagement
Intheprevioussection,wedescribedmanyAIcontributionstodealwithfailuresinAIOps.Inthis
finalsection,wefocusonthelargepictureandanalyzethecurrentstatusoffailuremanagement
ofAIOps.Wealsomakeuseofourobservationstoexaminethecurrentlyopenchallengessuggest
futuredirectionsforresearch.
AIOpshasshownasteadygrowingtrendinthelastyears,manifestedbothinthenumberandva-
rietyofcontributionspresent.Inthelastfiveyears,atleast100contributionshavebeenproposed
on a yearly average. We can expect the field to continue its growth, due to increasing demand
for reliability and efficiency in large-scale computing systems. The evolution of cloud technolo-
gies (e.g., in virtualization, monitoring tools) will provide large space for future improvements
andtheexperimentationofnewtechniques.Tofulfillthesegreatexpectations,thefieldmustbe
able to provide a solid ground for experimentation, based on a more formal standardization of
problemsandstrongerattitudetowardbenchmarks,neededforcomparisonandevaluationofthe
resultsachieved.Effortsincreatingstandardproblemsandbenchmarkdatasetswouldthereforebe
rewarding.
TheanalysisofthetopicsandtasksinthecurrentAIOpslandscape,asobservedanddescribed
inSection4,equallyallowsonetoinvestigatepossiblefuturedirections.First,Table8showshow
themajorityofworksutilizeonlyoneorfewtypesofdata.Multimodalapproaches,abletotake
ACMTransactionsonIntelligentSystemsandTechnology,Vol.12,No.6,Article81.Publicationdate:November2021.

81:36 P.Notaroetal.
Table8. PapersAnalyzedintheSurveyGroupedbyEmployedDataSources,Targets,andCategories
DataSources Targets
Paper(s) Category
edoCecruoS
secruoseRgnitseT scirteMmetsyS atadOLS/sIPK cffiarTkrowteN
ygolopoT
stropeRtnedicnI
sgoLtnevE
secarTnoitucexE
edoCecruoS noitacilppA erawdraH krowteN retnecataD
[35,38,52,94,102,117,153] • • SoftwareDefectPrediction
[42,50,76,98,103,115,141] • • SoftwareDefectPrediction
[105,128] • • • FaultInjection
[4,49,136] • • • SoftwareRejuvenation
[21,137] • • • • SoftwareRejuvenation
[62,95,114] • • Checkpointing
[77,78,89,104,138] • • HardwareFailurePrediction
[54,88,143,165,167] • • HardwareFailurePrediction
[101,148,149,164] • • HardwareFailurePrediction
[37] • • • HardwareFailurePrediction
[33] • • • HardwareFailurePrediction
[161] • • • HardwareFailurePrediction
[23] • • • SystemFailurePrediction
[31] • • • SystemFailurePrediction
[61] • • • • SystemFailurePrediction
[119] • • • • SystemFailurePrediction
[81] • • • SystemFailurePrediction
[123] • • • • • SystemFailurePrediction
[44,160] • • SystemFailurePrediction
[151] • • • AnomalyDetection
[7,131,159] • • • AnomalyDetection
[86,150] • • AnomalyDetection
[127] • • • • AnomalyDetection
[72] • • • AnomalyDetection
[73] • • • • AnomalyDetection
[12,18,41,45,92,162] • • AnomalyDetection
[29] • • • • AnomalyDetection
[11] • • • AnomalyDetection
[26,87] • • AnomalyDetection
[8,43,97,142] • • • InternetTrafficClassification
[163,168] • • • LogEnhancement
[1,30,85,121,145,156] • • • • FaultLocalization
[110] • • • • FaultLocalization
[80,132] • • FaultLocalization
[83] • • FaultLocalization
[9] • • • • FaultLocalization
[154] • • • Root-causeDiagnosis
[6] • • • • Root-causeDiagnosis
[64] • • • Root-causeDiagnosis
[25] • • • Root-causeDiagnosis
[120] • • • RCA-Others
[14,32] • • • • RCA-Others
[84] • • • RCA-Others
[3] • • • RCA-Others
[126,158] • • • IncidentTriage
[140,166] • • • SolutionRecommendation
[82] • • • • SolutionRecommendation
[124] • • • • Recovery
ACMTransactionsonIntelligentSystemsandTechnology,Vol.12,No.6,Article81.Publicationdate:November2021.

ASurveyofAIOpsMethodsforFailureManagement 81:37
advantage of different data sources, may prove more effective and robust to new observations,
thankstotheincreaseinsystemvisibility.
Wealsoobservedhowsomeareasoffailuremanagementhaveexperiencedlessscientificinter-
estcomparedtoothers.Aclearexampleistherecoverytask,which,althoughafundamentaland
concretesteptodealwithfailures,stillpresentsaminutegroupofcontributions.Asimilarcon-
siderationappliesforfailureprevention,whereallthecontributionsareconcentratedaroundfew
tasks(wepresentedfoursubcategories).However,failurepreventioncanbeperformedinmany
otherways,someofwhicharestilltobeexplored.Currently,themajorityofapproachesforfailure
preventionareappliedonlineandconcentrateexclusivelyonthecurrent-futurestatecharacteris-
tics.Introducingassumptionsandinformationaboutthesystemworkingprinciplesmaysetthe
groundformuchmoreactionableinsights.Forexample,model-basedpreventionwouldallowop-
eratorstoestimateinadvancetherisksassociatedwithparticularactions,suchasacanaryrelease
oraservershutdown.
Inaddition,theadventofvirtualizationtechnologiesrequiresnewresearchfocusingonspecific
targets(e.g.,hypervisors,virtualmachines,containers,etc.),creatingnewtasks,suchashypervisor
anomalydetection,containerfailurepredictionandsoon.
Finally,theapplicationofnovelAIapproachesmayprovebeneficialtoadvanceAIOps.Inthe
decade, the rise of Deep Learning methods has translated into a variety of new approaches for
failureprediction,anomalydetectionandroot-causeanalysis.Thismayoccuragainwithfuture
breakthroughs.
5.2 ConcludingRemarksandFutureWork
In this work, we explored a variety of AIOps approaches for the management of failures in IT
systems.Toconductourresearch,theAIOpsconcepthasbeenexploredstartingfromtheavailable
definitions,allowingustocaptureaprecisecharacterizationofthetopicintermsofgoals,sources,
andmethods.Oursurveystudyfocusingonfailuremanagementanalyzed100contributions,across
allidentifiedcategories,datasources,andtargetcomponents.Whenpossible,wehavefocusedour
attentiononthelimitationsofcurrentapproachesandthepossibilitiestoexpandandintegratethe
currentareasofresearchinAIOps.Wehopethattheresultsherepresentedcanactivelysupport
researchers and engineers working with AIOps by providing a comprehensive overview of the
topictosupportfutureinvestigations.AsAIOpsisanactiveandincreasinglypopularresearcharea,
weexpectfutureworkstoupdatethisarticlewithnewreferencesandcontributetoexpandingthe
discussionwithnewlyestablishedtopics.
REFERENCES
[1] RuiAbreu,PeterZoeteweij,andArjanJ.C.vanGemund.2009.Spectrum-basedmultiplefaultlocalization.InPro-
ceedingsoftheIEEE/ACMInternationalConferenceonAutomatedSoftwareEngineering.IEEE,88–99.https://doi.org/
10.1109/ASE.2009.25
[2] ArmenAghasaryan,EricFabre,AlbertBenveniste,RenéeBoubour,andClaudeJard.1998.Faultdetectionanddiag-
nosisindistributedsystems:Anapproachbypartiallystochasticpetrinets.DiscreteEventDynam.Syst.8,2(1998),
203–231.https://doi.org/10.1023/a:1008241818642
[3] MarcosK.Aguilera,JeffreyC.Mogul,JanetL.Wiener,PatrickReynolds,andAthichaMuthitacharoen.2003.Per-
formancedebuggingfordistributedsystemsofblackboxes.ACMSIGOPSOperat.Syst.Rev.37,5(Dec.2003),74–89.
https://doi.org/10.1145/1165389.945454
[4] JavierAlonso,JordiTorres,JosepLl.Berral,andRicardGavalda.2010.Adaptiveon-linesoftwareagingprediction
basedonmachinelearning.InProceedingsoftheIEEE/IFIPInternationalConferenceonDependableSystemsNetworks
(DSN’10).IEEE,507–516.https://doi.org/10.1109/dsn.2010.5544275
[5] J.Arlat,M.Aguera,L.Amat,Y.Crouzet,J.-C.Fabre,J.-C.Laprie,E.Martins,andD.Powell.1990.Faultinjectionfor
dependabilityvalidation:Amethodologyandsomeapplications.IEEETrans.Softw.Eng.16,2(Feb.1990),166–182.
https://doi.org/10.1109/32.44380
ACMTransactionsonIntelligentSystemsandTechnology,Vol.12,No.6,Article81.Publicationdate:November2021.

81:38 P.Notaroetal.
[6] MonaAttariyan,MichaelChow,andJasonFlinn.2012.X-Ray:Automatingroot-causediagnosisofperformance
anomaliesinproductionsoftware.InProceedingsofthe10thUSENIXConferenceonOperatingSystemsDesignand
Implementation(OSDI’12).USENIXAssociation,307–320.https://doi.org/10.5555/2387880.2387910
[7] JulienAudibert,PietroMichiardi,FrédéricGuyard,SébastienMarti,andMariaA.Zuluaga.2020.USAD:UnSuper-
visedanomalydetectiononmultivariatetimeseries.InProceedingsofthe26thACMSIGKDDInternationalConference
onKnowledgeDiscoveryandDataMining(KDD’20).ACM,NewYork,NY,3395–3404.https://doi.org/10.1145/3394486.
3403392
[8] TomAuld,AndrewW.Moore,andStephenF.Gull.2007.Bayesianneuralnetworksforinternettrafficclassification.
IEEETrans.NeuralNetw.18,1(Jan.2007),223–239.https://doi.org/10.1109/tnn.2006.883010
[9] ParamvirBahl,RanveerChandra,AlbertGreenberg,SrikanthKandula,DavidA.Maltz,andMingZhang.2007.To-
wardshighlyreliableenterprisenetworkservicesviainferenceofmulti-leveldependencies.InProceedingsofthe
ConferenceonApplications,Technologies,Architectures,andProtocolsforComputerCommunications(SIGCOMM’07).
ACM,NewYork,NY,13–24.https://doi.org/10.1145/1282380.1282383
[10] ChetanBansal,SundararajanRenganathan,AshimaAsudani,OlivierMidy,andMathruJanakiraman.2020.DeCaf:
Diagnosingandtriagingperformanceissuesinlarge-scalecloudservices.InProceedingsoftheACM/IEEE42ndIn-
ternationalConferenceonSoftwareEngineering:SoftwareEngineeringinPractice(ICSE-SEIP’20).ACM,NewYork,NY,
201–210.https://doi.org/10.1145/3377813.3381353
[11] PaulBarham,RebeccaIsaacs,RichardMortier,andDushyanthNarayanan.2003.Magpie:Onlinemodellingand
performance-awaresystems.InProceedingsofthe9thConferenceonHotTopicsinOperatingSystems,Vol.9.USENIX
Association,15.https://doi.org/10.5555/1251054.1251069
[12] IvanBeschastnikh,YuriyBrun,MichaelD.Ernst,andArvindKrishnamurthy.2014.Inferringmodelsofconcurrent
systemsfromlogsoftheirbehaviorwithCSight.InProceedingsofthe36thInternationalConferenceonSoftware
Engineering(ICSE’14).ACM,NewYork,NY,468–479.https://doi.org/10.1145/2568225.2568246
[13] NetflixTechnologyBlog.2016.NetflixChaosMonkeyUpgraded.Retrievedfromhttps://netflixtechblog.com/netflix-
chaos-monkey-upgraded-1d679429be5d.
[14] PeterBodik,MoisesGoldszmidt,ArmandoFox,DawnB.Woodard,andHansAndersen.2010.Fingerprintingthedat-
acenter:Automatedclassificationofperformancecrises.InProceedingsofthe5thEuropeanConferenceonComputer
Systems(EuroSys’10).ACM,NewYork,NY,111–124.https://doi.org/10.1145/1755913.1755926
[15] A.T.Bouloutas,S.Calo,andA.Finkel.1994.Alarmcorrelationandfaultidentificationincommunicationnetworks.
IEEETrans.Commun.42,2/3/4(21994),523–533.https://doi.org/10.1109/tcomm.1994.577079
[16] L.C.Briand,J.W.Daly,andJ.K.Wust.1999.Aunifiedframeworkforcouplingmeasurementinobject-oriented
systems.IEEETrans.Softw.Eng.25,1(11999),91–121.https://doi.org/10.1109/32.748920
[17] Broadcom.2020.AIOps—Broadcom.Retrievedfromhttps://www.broadcom.com/products/software/aiops.
[18] AndyBrown,AaronTuor,BrianHutchinson,andNicoleNichols.2018.Recurrentneuralnetworkattentionmech-
anismsforinterpretablesystemloganomalydetection.InProceedingsofthe1stWorkshoponMachineLearningfor
ComputingSystems(MLCS’18).ACM,NewYork,NY,Article1,8pages.https://doi.org/10.1145/3217871.3217872
[19] LisaBurnellandEricHorvitz.1995.Structureandchance:Meldinglogicandprobabilityforsoftwaredebugging.
Commun.ACM38,3(Mar.1995),31–ff.https://doi.org/10.1145/203330.203338
[20] K.L.ButlerandJ.A.Momoh.1999.Aneuralnetbasedapproachforfaultdiagnosisindistributionnetworks.In
ProceedingsoftheIEEEPowerEngineeringSociety,Vol.1.IEEE,353–356.https://doi.org/10.1109/PESW.1999.747478
[21] V.Castelli,R.E.Harper,P.Heidelberger,S.W.Hunter,K.S.Trivedi,K.Vaidyanathan,andW.P.Zeggert.2001.
Proactivemanagementofsoftwareaging.IBMJ.Res.Dev.45,2(Mar.2001),311–332.https://doi.org/10.1147/rd.452.
0311
[22] RaghavendraChalapathyandSanjayChawla.2019.DeepLearningforAnomalyDetection:ASurvey.Retrievedfrom
http://arxiv.org/abs/1901.03407.
[23] ThanyalakChalermarrewong,TiraneeAchalakul,andSimonChongWeeSee.2012.Failurepredictionofdatacenters
usingtimeseriesandfaulttreeanalysis.InProceedingsoftheIEEE18thInternationalConferenceonParalleland
DistributedSystems.IEEE,794–799.https://doi.org/10.1109/icpads.2012.129
[24] VarunChandola,ArindamBanerjee,andVipinKumar.2009.Anomalydetection:Asurvey.Comput.Surveys41,3
(July2009),15:1–15:58.https://doi.org/10.1145/1541880.1541882
[25] M.Y.Chen,E.Kiciman,E.Fratkin,A.Fox,andE.Brewer.2002.Pinpoint:Problemdeterminationinlarge,dynamic
Internetservices.InProceedingsoftheInternationalConferenceonDependableSystemsandNetworks.IEEE,595–604.
https://doi.org/10.1109/DSN.2002.1029005
[26] MikeY.Chen,AnthonyAccardi,EmreKiciman,JimLloyd,DavePatterson,ArmandoFox,andEricBrewer.2004.
Path-basedfailureandevolutionmanagement.InProceedingsofthe1stConferenceonSymposiumonNetworked
SystemsDesignandImplementation (NSDI’04).USENIXAssociation,23.Retrievedfromhttps://dl.acm.org/doi/10.
5555/1251175.1251198.
ACMTransactionsonIntelligentSystemsandTechnology,Vol.12,No.6,Article81.Publicationdate:November2021.

ASurveyofAIOpsMethodsforFailureManagement 81:39
[27] XinChen,Charng-DaLu,andKarthikPattabiraman.2014.Failureanalysisofjobsincomputeclouds:AGoogle
clustercasestudy.InProceedingsoftheIEEE25thInternationalSymposiumonSoftwareReliabilityEngineering.IEEE,
167–177.https://doi.org/10.1109/issre.2014.34
[28] S.R.ChidamberandC.F.Kemerer.1994.Ametricssuiteforobjectorienteddesign.IEEETrans.Softw.Eng.20,6
(61994),476–493.https://doi.org/10.1109/32.295895
[29] MichaelChow,DavidMeisner,JasonFlinn,DanielPeek,andThomasF.Wenisch.2014.Themysterymachine:End-to-
endperformanceanalysisoflarge-scaleinternetservices.InProceedingsofthe11thUSENIXConferenceonOperating
SystemsDesignandImplementation(OSDI’14).USENIXAssociation,217–231.https://dl.acm.org/doi/10.5555/2685048.
2685066
[30] HolgerCleveandAndreasZeller.2005.Locatingcausesofprogramfailures.InProceedingsofthe27thInternational
ConferenceonSoftwareEngineering(ICSE’05).ACM,NewYork,NY,342–351.https://doi.org/10.1145/1062455.1062522
[31] IraCohen,MoisesGoldszmidt,TerenceKelly,JulieSymons,andJeffreyS.Chase.2004.Correlatinginstrumentation
datatosystemstates:Abuildingblockforautomateddiagnosisandcontrol.InProceedingsofthe6thConference
onSymposiumonOperatingSystemsDesignandImplementation(OSDI’04).USENIXAssociation,16.Retrievedfrom
https://dl.acm.org/doi/10.5555/1251254.1251270.
[32] IraCohen,SteveZhang,MoisesGoldszmidt,JulieSymons,TerenceKelly,andArmandoFox.2005.Capturing,in-
dexing,clustering,andretrievingsystemhistory.InProceedingsofthe20thACMSymposiumonOperatingSystems
Principles(SOSP’05).ACM,NewYork,NY,105–118.https://doi.org/10.1145/1095810.1095821
[33] CarlosH.A.Costa,YoonhoPark,BryanS.Rosenburg,Chen-YongCher,andKyungDongRyu.2014.Asystem
softwareapproachtoproactivememory-erroravoidance.InProceedingsoftheInternationalConferenceforHigh
PerformanceComputing,Networking,StorageandAnalysis(SC’14).IEEE,12pages.https://doi.org/10.1109/SC.2014.63
[34] A.Csenki.1990.Bayespredictiveanalysisofafundamentalsoftwarereliabilitymodel.IEEETrans.Reliabil.39,2
(June1990),177–183.https://doi.org/10.1109/24.55879
[35] MarcoD’Ambros,MicheleLanza,andRomainRobbes.2011.Evaluatingdefectpredictionapproaches:Abenchmark
andanextensivecomparison.Empir.Softw.Eng.17,4–5(Aug.2011),531–577.https://doi.org/10.1007/s10664-011-
9173-9
[36] YingnongDang,QingweiLin,andPengHuang.2019.AIOps:Real-worldchallengesandresearchinnovations.In
ProceedingsoftheIEEE/ACM41stInternationalConferenceonSoftwareEngineering:CompanionProceedings(ICSE’19).
IEEE,4–5.https://doi.org/10.1109/icse-companion.2019.00023
[37] NickolasAllenDavis,AbdelmounaamRezgui,HamdySoliman,SkylerManzanares,andMilagreCoates.2017.Fail-
ureSim:Asystemforpredictinghardwarefailuresinclouddatacentersusingneuralnetworks.InProceedingsofthe
IEEE10thInternationalConferenceonCloudComputing(CLOUD’17).IEEE,544–551.https://doi.org/10.1109/cloud.
2017.75
[38] KarelDejaeger,ThomasVerbraken,andBartBaesens.2013.Towardcomprehensiblesoftwarefaultpredictionmodels
usingBayesiannetworkclassifiers.IEEETrans.Softw.Eng.39,2(Feb.2013),237–257.https://doi.org/10.1109/tse.2012.
20
[39] B.Dhanalaxmi,G.ApparaoNaidu,andK.Anuradha.2015.Areviewonsoftwarefaultdetectionandprevention
mechanisminsoftwaredevelopmentactivities.J.Comput.Eng.17,6(2015),25–30.
[40] PeterA.DindaandDavidR.O’Hallaron.1999.Anevaluationoflinearmodelsforhostloadprediction.InProceedings
ofThe8thInternationalSymposiumonHighPerformanceDistributedComputing.IEEE,87–96.
[41] MinDu,FeifeiLi,GuinengZheng,andVivekSrikumar.2017.DeepLog:Anomalydetectionanddiagnosisfrom
systemlogsthroughdeeplearning.InProceedingsoftheACMSIGSACConferenceonComputerandCommunications
Security.ACM,1285–1298.https://doi.org/10.1145/3133956.3134015
[42] KarimO.ElishandMahmoudO.Elish.2008.Predictingdefect-pronesoftwaremodulesusingsupportvectorma-
chines.J.Syst.Softw.81,5(May2008),649–660.https://doi.org/10.1016/j.jss.2007.07.040
[43] AliceEste,FrancescoGringoli,andLucaSalgarelli.2009.SupportvectormachinesforTCPtrafficclassification.Com-
put.Netw.53,14(Sep.2009),2476–2490.https://doi.org/10.1016/j.comnet.2009.05.003
[44] IleniaFronza,AlbertoSillitti,GiancarloSucci,MikkoTerho,andJelenaVlasenko.2013.Failurepredictionbasedon
logfilesusingrandomindexingandsupportvectormachines.J.Syst.Softw.86,1(12013),2–11.https://doi.org/10.
1016/j.jss.2012.06.025
[45] QiangFu,Jian-GuangLou,YiWang,andJiangLi.2009.Executionanomalydetectionindistributedsystemsthrough
unstructuredloganalysis.InProceedingsofthe9thIEEEInternationalConferenceonDataMining.IEEEComputer
Society,149–158.https://doi.org/10.1109/icdm.2009.60
[46] ZhiweiGao,CarloCecati,andStevenX.Ding.2015.Asurveyoffaultdiagnosisandfault-toleranttechniques—
PartI:Faultdiagnosiswithmodel-basedandsignal-basedapproaches.IEEETrans.Industr.Electr.62,6(June2015),
3757–3767.https://doi.org/10.1109/tie.2015.2417501
ACMTransactionsonIntelligentSystemsandTechnology,Vol.12,No.6,Article81.Publicationdate:November2021.

81:40 P.Notaroetal.
[47] ZhiweiGao,CarloCecati,andStevenX.Ding.2015.Asurveyoffaultdiagnosisandfault-toleranttechniques—Part
II:Faultdiagnosiswithknowledge-basedandhybrid/activeapproaches.IEEETrans.Industr.Electr.62,6(June2015),
3768–3774.https://doi.org/10.1109/TIE.2015.2419013
[48] S.Garg,A.Puliafito,M.Telek,andK.S.Trivedi.1995.AnalysisofsoftwarerejuvenationusingMarkovregenerative
stochasticpetrinet.InProceedingsofthe6thInternationalSymposiumonSoftwareReliabilityEngineering(ISSRE’95)
(1995).IEEE,180–187.https://doi.org/10.1109/issre.1995.497656
[49] S.Garg,A.vanMoorsel,K.Vaidyanathan,andK.S.Trivedi.1998.Amethodologyfordetectionandestimationof
softwareaging.InProceedingsofthe9thInternationalSymposiumonSoftwareReliabilityEngineering.IEEE,283–292.
https://doi.org/10.1109/issre.1998.730892
[50] EmanuelGiger,MarcoD’Ambros,MartinPinzger,andHaraldC.Gall.2012.Method-levelbugprediction.InProceed-
ingsoftheACM-IEEEInternationalSymposiumonEmpiricalSoftwareEngineeringandMeasurement(ESEM’12).ACM,
NewYork,NY,171–180.https://doi.org/10.1145/2372251.2372285
[51] TarunGoyal,AjitSingh,andAakankshaAgrawal.2012.Cloudsim:Simulatorforcloudcomputinginfrastructure
andmodeling.Proc.Eng.38(Nov.2012),3566–3572.https://doi.org/10.1016/j.proeng.2012.06.412
[52] T.L.Graves,A.F.Karr,J.S.Marron,andH.Siy.2000.Predictingfaultincidenceusingsoftwarechangehistory.IEEE
Trans.Softw.Eng.26,7(July2000),653–661.https://doi.org/10.1109/32.859533
[53] MauriceH.Halstead.1977.ElementsofSoftwareScience(OperatingandProgrammingSystemsSeries).ElsevierScience
Inc..
[54] GregHamerlyandCharlesElkan.2001.Bayesianapproachestofailurepredictionfordiskdrives.InProceedingsof
the18thInternationalConferenceonMachineLearning(ICML’01).MorganKaufmann,SanFrancisco,CA,202–209.
https://doi.org/10.5555/645530.655825
[55] SeungjaeHan,K.G.Shin,andH.A.Rosenberg.1995.DOCTOR:Anintegratedsoftwarefaultinjectionenvironment
fordistributedreal-timesystems.InProceedingsoftheIEEEInternationalComputerPerformanceandDependability
Symposium.IEEE,204–213.https://doi.org/10.1109/IPDS.1995.395831
[56] J.L.Hellerstein,FanZhang,andP.Shahabuddin.1999.Anapproachtopredictivedetectionforservicemanagement.
InProceedingsofthe6thIFIP/IEEEInternationalSymposiumonIntegratedNetworkManagement.IEEE,309–322.https:
//doi.org/10.1109/inm.1999.770691
[57] Y.Huang,C.Kintala,N.Kolettis,andN.D.Fulton.1995.Softwarerejuvenation:Analysis,moduleandapplications.
InProceedingsofthe25thInternationalSymposiumonFault-TolerantComputing.DigestofPapers.IEEE,381–390.
https://doi.org/10.1109/FTCS.1995.466961
[58] G.F.Hughes,J.F.Murray,K.Kreutz-Delgado,andC.Elkan.2002.Improveddisk-drivefailurewarnings.IEEETrans.
Reliabil.51,3(Sep.2002),350–357.https://doi.org/10.1109/TR.2002.802886
[59] Monica Hutchins, Herb Foster, Tarak Goradia, and Thomas Ostrand. 1994. Experiments on the effectiveness of
dataflow-andcontrol-flow-basedtestadequacycriteria—IEEEconferencepublication.InProceedingsofthe16thIn-
ternationalConferenceonSoftwareEngineering.IEEE,191–200.Retrievedfromhttps://ieeexplore.ieee.org/document/
296778.
[60] OlumuyiwaIbidunmoye,FranciscoHernández-Rodriguez,andErikElmroth.2015.Performanceanomalydetection
andbottleneckidentification.Comput.Surveys48,1(Sep.2015),1–35.https://doi.org/10.1145/2791120
[61] TariqulIslamandDakshnamoorthyManivannan.2017.Predictingapplicationfailureincloud:Amachinelearning
approach.InProceedingsoftheIEEEInternationalConferenceonCognitiveComputing(ICCC’17).IEEE,24–31.https:
//doi.org/10.1109/ieee.iccc.2017.11
[62] ItthichokJangjaimonandNian-FengTzeng.2015.Effectivecostreductionforelasticcloudsunderspotinstance
pricingthroughadaptivecheckpointing.IEEETrans.Comput.64,2(Feb.2015),396–409.https://doi.org/10.1109/tc.
2013.225
[63] DavidJauk,DaiYang,andMartinSchulz.2019.Predictingfaultsinhighperformancecomputingsystems:Anin-
depthsurveyofthestate-of-the-practice.InProceedingsoftheInternationalConferenceforHighPerformanceCom-
puting,Networking,StorageandAnalysis(SC’19).ACM,NewYork,NY,Article30,13pages.https://doi.org/10.1145/
3295500.3356185
[64] SrikanthKandula,DinaKatabi,andJean-PhilippeVasseur.2005.Shrink:AtoolforfailurediagnosisinIPnetworks.
InProceedingoftheACMSIGCOMMWorkshoponMiningNetworkData(MineNet’05).ACM,NewYork,NY,6pages.
https://doi.org/10.1145/1080173.1080178
[65] N.Karunanithi,D.Whitley,andY.K.Malaiya.1992.Predictionofsoftwarereliabilityusingconnectionistmodels.
IEEETrans.Softw.Eng.18,7(July1992),563–574.https://doi.org/10.1109/32.148475
[66] TaghiM.KhoshgoftaarandDavidL.Lanning.1995.Aneuralnetworkapproachforearlydetectionofprogram
moduleshavinghighriskinthemaintenancephase.J.Syst.Softw.29,1(Apr.1995),85–91.https://doi.org/10.1016/
0164-1212(94)00130-f
ACMTransactionsonIntelligentSystemsandTechnology,Vol.12,No.6,Article81.Publicationdate:November2021.

ASurveyofAIOpsMethodsforFailureManagement 81:41
[67] BarbaraA.Kitchenham,DavidBudgen,andO.PearlBrereton.2010.Thevalueofmappingstudies-Aparticipant-
observercasestudy.InProceedingsofthe14thInternationalConferenceonEvaluationandAssessmentinSoftware
Engineering(EASE’10).BCSLearning&Development,25–33.https://doi.org/10.14236/ewic/EASE2010.4
[68] S.Kliger,S.Yemini,Y.Yemini,D.Ohsie,andS.Stolfo.1995.ACodingApproachtoEventCorrelation.SpringerUS,
Boston,MA,266–277.https://doi.org/10.1007/978-0-387-34890-2_24
[69] Yevgeniy Sverdlik Data Center Knowledge. 2016. What Facebook Has Learned from Regularly Shutting Down
EntireDataCenters.Retrievedfromhttps://www.datacenterknowledge.com/archives/2016/08/31/facebook-learned-
regularly-shutting-entire-data-centers.
[70] KhairyA.H.KobbacyandSunilVadera.2011.AsurveyofAIinoperationsmanagementfrom2005to2009.J.
Manufact.Technol.Manage.22,6(July2011),706–733.https://doi.org/10.1108/17410381111149602
[71] K.A.H.Kobbacy,SVadera,andM.H.Rasmy.2007.AIandORinmanagementofoperations:Historyandtrends.J.
Oper.Res.Soc.58,1(Jan.2007),10–28.https://doi.org/10.1057/palgrave.jors.2602132
[72] AnukoolLakhina,MarkCrovella,andChristopheDiot.2004.Diagnosingnetwork-widetrafficanomalies.InPro-
ceedingsoftheConferenceonApplications,Technologies,Architectures,andProtocolsforComputerCommunications
(SIGCOMM’04).ACM,NewYork,NY,219–230.https://doi.org/10.1145/1015467.1015492
[73] AnukoolLakhina,MarkCrovella,andChristopheDiot.2005.Mininganomaliesusingtrafficfeaturedistributions.In
ProceedingsoftheConferenceonApplications,Technologies,Architectures,andProtocolsforComputerCommunications
(Philadelphia,Pennsylvania)(SIGCOMM’05).ACM,NewYork,NY,217–228.https://doi.org/10.1145/1080091.1080118
[74] AndrewLerner.2017.AIOpsPlatforms—Gartner.Retrievedfromhttps://blogs.gartner.com/andrew-lerner/2017/08/
09/aiops-platforms/.
[75] Anna Levin, Shelly Garion, Elliot K. Kolodner, Dean H. Lorenz, Katherine Barabash, Mike Kugler, and Niall
McShane.2019.AIOpsforacloudobjectstorageservice.InProceedingsoftheIEEEInternationalCongressonBig
Data(BigDataCongress’19).IEEE,165–169.https://doi.org/10.1109/BigDataCongress.2019.00036
[76] JianLi,PinjiaHe,JiemingZhu,andMichaelR.Lyu.2017.Softwaredefectpredictionviaconvolutionalneuralnet-
work.InProceedingsoftheIEEEInternationalConferenceonSoftwareQuality,ReliabilityandSecurity(QRS’17).IEEE,
318–328.https://doi.org/10.1109/qrs.2017.42
[77] JingLi,XinpuJi,YuhanJia,BingpengZhu,GangWang,ZhongweiLi,andXiaoguangLiu.2014.Harddrivefailurepre-
dictionusingclassificationandregressiontrees.InProceedingsofthe44thAnnualIEEE/IFIPInternationalConference
onDependableSystemsandNetworks.IEEE,383–394.https://doi.org/10.1109/dsn.2014.44
[78] JingLi,RebeccaJ.Stones,GangWang,ZhongweiLi,XiaoguangLiu,andKangXiao.2016.Beingaccurateisnot
enough:Newmetricsfordiskfailureprediction.InProceedingsoftheIEEE35thSymposiumonReliableDistributed
Systems(SRDS’16).IEEE,71–80.https://doi.org/10.1109/srds.2016.019
[79] YangguangLi,ZhenMing(Jack)Jiang,HengLi,AhmedE.Hassan,ChengHe,RuiruiHuang,ZhengdaZeng,Mian
Wang,andPinanChen.2020.Predictingnodefailuresinanultra-large-scalecloudcomputingplatform:AnAIOps
solution.ACMTrans.Softw.Eng.Methodol.29,2(2742020),13:1–13:24.https://doi.org/10.1145/3385187
[80] ZeyanLi,ChengyangLuo,YiweiZhao,YongqianSun,KaixinSui,XipingWang,DapengLiu,XingJin,QiWang,
andDanPei.2019.Genericandrobustlocalizationofmulti-dimensionalrootcauses.InProceedingsoftheIEEE30th
InternationalSymposiumonSoftwareReliabilityEngineering(ISSRE’19).IEEE,IEEE,47–57.
[81] YinglungLiang,YanyongZhang,HuiXiong,andRamendraSahoo.2007.FailurepredictioninIBMbluegene/levent
logs.InProceedingsofthe7thIEEEInternationalConferenceonDataMining(ICDM’07).IEEE,583–588.https://doi.
org/10.1109/icdm.2007.46
[82] FanLin,MattBeadon,HarishDattatrayaDixit,GauthamVunnam,AmolDesai,andSriramSankar.2018.Hardware
remediationatscale.InProceedingsofthe48thAnnualIEEE/IFIPInternationalConferenceonDependableSystemsand
NetworksWorkshops(DSN-W’18).IEEE,14–17.https://doi.org/10.1109/dsn-w.2018.00015
[83] FredLin,KeyurMuzumdar,NikolayPavlovichLaptev,Mihai-ValentinCurelea,SeunghakLee,andSriramSankar.
2020.Fastdimensionalanalysisforrootcauseinvestigationinalarge-scaleserviceenvironment.Proc.ACMMeas.
Anal.Comput.Syst.4,2,Article31(June2020),23pages.https://doi.org/10.1145/3392149
[84] QingweiLin,HongyuZhang,Jian-GuangLou,YuZhang,andXueweiChen.2016.Logclusteringbasedproblem
identificationforonlineservicesystems.InProceedingsofthe38thInternationalConferenceonSoftwareEngineering
Companion(ICSE’16).ACM,NewYork,NY,102–111.https://doi.org/10.1145/2889160.2889232
[85] ChaoLiu,XifengYan,LongFei,JiaweiHan,andSamuelP.Midkiff.2005.SOBER:Statisticalmodel-basedbuglocal-
ization.ACMSIGSOFTSoftw.Eng.Notes30,5(Sep.2005),286.https://doi.org/10.1145/1095430.1081753
[86] DapengLiu,YoujianZhao,HaowenXu,YongqianSun,DanPei,JiaoLuo,XiaoweiJing,andMeiFeng.2015.Oppren-
tice:Towardspracticalandautomaticanomalydetectionthroughmachinelearning.InProceedingsoftheInternet
MeasurementConference.ACM,NewYork,NY,211–224.https://doi.org/10.1145/2815675.2815679
[87] DavidLo,HongCheng,JiaweiHan,Siau-ChengKhoo,andChengnianSun.2009.Classificationofsoftwarebehaviors
forfailuredetection:Adiscriminativepatternminingapproach.InProceedingsofthe15thACMSIGKDDInternational
ACMTransactionsonIntelligentSystemsandTechnology,Vol.12,No.6,Article81.Publicationdate:November2021.

81:42 P.Notaroetal.
ConferenceonKnowledgeDiscoveryandDataMining(KDD’09).ACM,NewYork,NY,557–566.https://doi.org/10.1145/
1557019.1557083
[88] AoMa,FredDouglis,GuanlinLu,DarrenSawyer,SurendarChandra,andWindsorHsu.2015.RAIDShield:Charac-
terizing,monitoring,andproactivelyprotectingagainstdiskfailures.InProceedingsofthe13thUSENIXConference
onFileandStorageTechnologies(FAST’15).USENIXAssociation,241–256.https://www.usenix.org/conference/fast15/
technical-sessions/presentation/ma
[89] FarzanehMahdisoltani,IoanStefanovici,andBiancaSchroeder.2017.Proactiveerrorpredictiontoimprovestorage
systemreliability.InProceedingsoftheUSENIXAnnualTechnicalConference(USENIXATC’17).USENIXAssociation,
391–402.Retrievedfromhttps://www.usenix.org/conference/atc17/technical-sessions/presentation/mahdisoltani.
[90] T.J.McCabe.1976.Acomplexitymeasure.IEEETrans.Softw.Eng.SE-2,4(Dec.1976),308–320.https://doi.org/10.
1109/TSE.1976.233837
[91] Meiliana,SyaefulKarim,HarcoLeslieHendricSpitsWarnars,FordLumbanGaol,EdiAbdurachman,andBenfano
Soewito.2017.Softwaremetricsforfaultpredictionusingmachinelearningapproaches:Aliteraturereviewwith
PROMISErepositorydataset.InProceedingsoftheIEEEInternationalConferenceonCyberneticsandComputational
Intelligence(CyberneticsCom’17).IEEE,19–23.https://doi.org/10.1109/cyberneticscom.2017.8311708
[92] WeibinMeng,YingLiu,YichenZhu,ShenglinZhang,DanPei,YuqingLiu,YihaoChen,RuizhiZhang,ShiminTao,
PeiSun,etal.2019.LogAnomaly:Unsuperviseddetectionofsequentialandquantitativeanomaliesinunstructured
logs.InProceedingsofthe28thInternationalJointConferenceonArtificialIntelligence(IJCAI’19).4739–4745.https:
//doi.org/10.24963/ijcai.2019/658
[93] Tim Menzies. 2004. PROMISE DATASETS PAGE. Retrieved from http://promise.site.uottawa.ca/SERepository/
datasets-page.html.
[94] TimMenzies,JeremyGreenwald,andArtFrank.2007.Dataminingstaticcodeattributestolearndefectpredictors.
IEEETrans.Softw.Eng.33,1(Jan.2007),2–13.https://doi.org/10.1109/TSE.2007.256941
[95] AdamMoody,GregBronevetsky,KathrynMohror,anddeBronisR.Supinski.2010.Design,modeling,andevaluation
ofascalablemulti-levelcheckpointingsystem.InProceedingsoftheACM/IEEEInternationalConferenceforHigh
PerformanceComputing,Networking,StorageandAnalysis.IEEE,1–11.https://doi.org/10.1109/sc.2010.18
[96] Moogsoft. 2020. What Is AIOps? Moogsoft. Retrieved from https://www.moogsoft.com/resources/aiops/guide/
everything-aiops/.
[97] AndrewW.MooreandDenisZuev.2005.Internettrafficclassificationusingbayesiananalysistechniques.InPro-
ceedingsoftheACMSIGMETRICSInternationalConferenceonMeasurementandModelingofComputerSystems(SIG-
METRICS’05).ACM,NewYork,NY,50–60.https://doi.org/10.1145/1064212.1064220
[98] RaimundMoser,WitoldPedrycz,andGiancarloSucci.2008.Acomparativeanalysisoftheefficiencyofchange
metricsandstaticcodeattributesfordefectprediction.InProceedingsofthe13thInternationalConferenceonSoftware
Engineering.ACM,NewYork,NY,181–190.https://doi.org/10.1145/1368088.1368114
[99] MukosiAbrahamMukwevhoandTurgayCelik.2021.Towardasmartcloud:Areviewoffault-tolerancemethodsin
cloudsystems.IEEETrans.Serv.Comput.14,2(2021),589–605.https://doi.org/10.1109/tsc.2018.2816644
[100] JosephF.Murray,GordonF.Hughes,andKennethKreutz-Delgado.2003.Harddrivefailurepredictionusingnon-
parametricstatisticalmethods.Retrievedfromhttp://dsp.ucsd.edu/~jfmurray/publications/Murray2003.pdf.
[101] JosephF.Murray,GordonF.Hughes,andKennethKreutz-Delgado.2005.Machinelearningmethodsforpredicting
failuresinharddrives:Amultiple-instanceapplication.J.Mach.Learn.Res.6(Jan.2005),783–816.https://doi.org/10.
5555/1046920.1088699
[102] NachiappanNagappan,ThomasBall,andAndreasZeller.2006.Miningmetricstopredictcomponentfailures.In
Proceedingofthe28thInternationalConferenceonSoftwareEngineering(ICSE’06).ACM,NewYork,NY,452–461.
https://doi.org/10.1145/1134285.1134349
[103] JaechangNam,SinnoJialinPan,andSunghunKim.2013.Transferdefectlearning.InProceedingsofthe35thInter-
nationalConferenceonSoftwareEngineering(ICSE’13).IEEE,382–391.https://doi.org/10.1109/icse.2013.6606584
[104] IyswaryaNarayanan,KushagraVaid,DiWang,MyeongjaeJeon,BikashSharma,LauraCaulfield,AnandSivasub-
ramaniam,BenCutler,JieLiu,andBadriddineKhessib.2016.SSDfailuresindatacenters:What?When?andWhy?
InProceedingsofthe9thACMInternationalonSystemsandStorageConference(SYSTOR’16).ACM,NewYork,NY,
Article7,11pages.https://doi.org/10.1145/2928275.2928278
[105] RobertoNatella,DomenicoCotroneo,JoaoA.Duraes,andHenriqueS.Madeira.2013.Onfaultrepresentativeness
ofsoftwarefaultinjection.IEEETrans.Softw.Eng.39,1(Jan.2013),80–96.https://doi.org/10.1109/tse.2011.124
[106] RobertoNatella,DomenicoCotroneo,andHenriqueS.Madeira.2016.Assessingdependabilitywithsoftwarefault
injection:Asurvey.Comput.Surveys48,3(Aug.2016),44:1–44:55.https://doi.org/10.1145/2841425
[107] SashoNedelkoski,JorgeCardoso,andOdejKao.2019.Anomalydetectionandclassificationusingdistributedtracing
anddeeplearning.InProceedingsofthe19thIEEE/ACMInternationalSymposiumonCluster,CloudandGridComputing
(CCGRID’19).IEEE,241–250.https://doi.org/10.1109/ccgrid.2019.00038
ACMTransactionsonIntelligentSystemsandTechnology,Vol.12,No.6,Article81.Publicationdate:November2021.

ASurveyofAIOpsMethodsforFailureManagement 81:43
[108] NetManAIOps. 2019. SMD Dataset—OmniAnomaly. Retrieved from https://github.com/NetManAIOps/
OmniAnomaly.
[109] ClodoaldoBrasilinoLeiteNeto,PedroBatistaDeCarvalhoFilho,andAlexandreNÃşbregaDuarte.2013.Asystematic
mappingstudyonfaultmanagementincloudcomputing.InProceedingsoftheInternationalConferenceonParallel
andDistributedComputing,ApplicationsandTechnologies.IEEE,332–337.https://doi.org/10.1109/PDCAT.2013.59
[110] HiepNguyen,ZhimingShen,YongminTan,andXiaohuiGu.2013.FChain:Towardblack-boxonlinefaultlocalization
forcloudsystems.InProceedingsoftheIEEE33rdInternationalConferenceonDistributedComputingSystems.IEEE,
21–30.https://doi.org/10.1109/icdcs.2013.26
[111] ThuyT.T.NguyenandGrenvilleArmitage.2008.Asurveyoftechniquesforinternettrafficclassificationusing
machinelearning.IEEECommun.SurveysTutor.10,4(2008),56–76.https://doi.org/10.1109/surv.2008.080406
[112] Changhai Nie and Hareton Leung. 2011. A survey of combinatorial testing. Comput. Surveys 43, 2 (Apr. 2011),
11:1–11:29.https://doi.org/10.1145/1883612.1883618
[113] PaoloNotaro,JorgeCardoso,andMichaelGerndt.2020.AsystematicmappingstudyinAIOps.InProceedingsof
theInternationalConferenceonService-orientedComputing(ICSOC’20).Workshops:AIOps,CFTIC,STRAPS,AI-PA,
AI-IOTS,andSatelliteEvents.Springer,110–123.Retrievedfromhttp://arxiv.org/abs/2012.09108.
[114] H.Okamura,Y.Nishimura,andT.Dohi.2004.Adynamiccheckpointingschemebasedonreinforcementlearning.
InProceedingsofthe10thIEEEPacificRimInternationalSymposiumonDependableComputing.IEEE,151–158.https:
//doi.org/10.1109/PRDC.2004.1276566
[115] AhmetOkutanandOlcayTanerYıldız.2012.Softwaredefectpredictionusingbayesiannetworks.Empir.Softw.Eng.
19,1(Aug.2012),154–181.https://doi.org/10.1007/s10664-012-9218-8
[116] OpsRamp. 2020. AIOps (AI for IT Operations)—OpsRamp. Retrieved from https://www.opsramp.com/solutions/
service-centric-aiops/.
[117] T.J.Ostrand,E.J.Weyuker,andR.M.Bell.2005.Predictingthelocationandnumberoffaultsinlargesoftware
systems.IEEETrans.Softw.Eng.31,4(Apr.2005),340–355.https://doi.org/10.1109/tse.2005.49
[118] EduardoPinheiro,Wolf-DietrichWeber,andLuizAndréBarroso.2007.Failuretrendsinalargediskdrivepopula-
tion.InProceedingsofthe5thUSENIXConferenceonFileandStorageTechnologies(FAST’07).USENIXAssociation,2.
Retrievedfromhttps://www.usenix.org/conference/fast-07/failure-trends-large-disk-drive-population.
[119] TeeratPitakrat,DušanOkanović,AndrévanHoorn,andLarsGrunske.2018.Hora:Architecture-awareonlinefailure
prediction.J.Syst.Softw.137(Mar.2018),669–685.https://doi.org/10.1016/j.jss.2017.02.041
[120] A.Podgurski,D.Leon,P.Francis,W.Masri,M.Minch,JiayangSun,andBinWang.2003.Automatedsupportfor
classifyingsoftwarefailurereports.InProceedingsofthe25thInternationalConferenceonSoftwareEngineering.IEEE,
465–475.https://doi.org/10.1109/icse.2003.1201224
[121] M.RenierisandS.P.Reiss.2003.Faultlocalizationwithnearestneighborqueries.InProceedingsofthe18thIEEEInter-
nationalConferenceonAutomatedSoftwareEngineering.IEEE,30–39.https://ieeexplore.ieee.org/document/1240292
[122] FelixSalfner,MarenLenk,andMiroslawMalek.2010.Asurveyofonlinefailurepredictionmethods.Comput.Surveys
42,3(Mar.2010),1–42.https://doi.org/10.1145/1670679.1670680
[123] FelixSalfnerandMiroslawMalek.2007.Usinghiddensemi-Markovmodelsforeffectiveonlinefailureprediction.
InProceedingsofthe26thIEEEInternationalSymposiumonReliableDistributedSystems(SRDS’07).IEEE,161–174.
https://doi.org/10.1109/srds.2007.35
[124] AreegSamirandClausPahl.2019.AControllerArchitectureforAnomalyDetection,RootCauseAnalysisandSelf-
AdaptationforClusterArchitectures.Retrievedfromhttps://orbilu.uni.lu/handle/10993/42062.
[125] MarkSchwabacherandKaiGoebel.2007.Asurveyofartificialintelligenceforprognostics.InProceedingsofthe
AAAIFallSymposiumonArtificialIntelligenceforPrognostics.AAAI,108–115.Retrievedfromhttps://www.aaai.org/
Library/Symposia/Fall/2007/fs07-02-016.php.
[126] QihongShao,YiChen,ShuTao,XifengYan,andNikosAnerousis.2008.Efficientticketroutingbyresolutionse-
quencemining.InProceedingsofthe14thACMSIGKDDInternationalConferenceonKnowledgeDiscoveryandData
Mining(KDD’08).ACM,NewYork,NY,605–613.https://doi.org/10.1145/1401890.1401964
[127] BikashSharma,PraveenJayachandran,AkshatVerma,andChitaR.Das.2013.CloudPD:Problemdetermination
anddiagnosisinshareddynamicclouds.InProceedingsofthe43rdAnnualIEEE/IFIPInternationalConferenceon
DependableSystemsandNetworks(DSN’13).IEEE,1–12.https://doi.org/10.1109/dsn.2013.6575298
[128] AkbarSiamiNamin,JamesH.Andrews,andDuncanJ.Murdoch.2008.Sufficientmutationoperatorsformeasuring
testeffectiveness.InProceedingsofthe13thInternationalConferenceonSoftwareEngineering(ICSE’08).ACM,New
York,NY,351–360.https://doi.org/10.1145/1368088.1368136
[129] BMCSoftware.2020.AIOps—BMC.Retrievedfromhttps://www.bmc.com/it-solutions/aiops.html.
[130] MarcSolé,VictorMuntés-Mulero,AnnieIbrahimRana,andGiovaniEstrada.2017.SurveyonModelsandTechniques
forRoot-CauseAnalysis.Retrievedfromhttp://arxiv.org/abs/1701.08546.
ACMTransactionsonIntelligentSystemsandTechnology,Vol.12,No.6,Article81.Publicationdate:November2021.

81:44 P.Notaroetal.
[131] YaSu,YoujianZhao,ChenhaoNiu,RongLiu,WeiSun,andDanPei.2019.Robustanomalydetectionformultivari-
atetimeseriesthroughstochasticrecurrentneuralnetwork.InProceedingsofthe25thACMSIGKDDInternational
ConferenceonKnowledgeDiscoveryandDataMining(KDD’19).ACM,NewYork,NY,2828–2837.
[132] YongqianSun,YoujianZhao,YaSu,DapengLiu,XiaohuiNie,YuanMeng,ShiwenCheng,DanPei,ShenglinZhang,
XianpingQuetal.2018.Hotspot:Anomalylocalizationforadditivekpiswithmulti-dimensionalattributes.IEEE
Access6(2018),10909–10923.
[133] ResolveSystems.2020.WhatisAIOps?—Resolve.Retrievedfromhttps://resolve.io/what-is-aiops.
[134] D.TangandR.K.Iyer.1993.Dependabilitymeasurementandmodelingofamulticomputersystem.IEEETrans.
Comput.42,1(1993),62–75.https://doi.org/10.1109/12.192214
[135] TimothyK.TsaiandRavishankarK.Iyer.1995.FTAPE:AfaultinjectiontooltomeasurefaultTolerance.NASA
STI/ReconTechnicalReport.25333pages.https://doi.org/10.2514/6.1995-1041
[136] K.VaidyanathanandK.S.Trivedi.1999.Ameasurement-basedmodelforestimationofresourceexhaustioninop-
erationalsoftwaresystems.InProceedingsofthe10thInternationalSymposiumonSoftwareReliabilityEngineering.
IEEE,84–93.https://doi.org/10.1109/issre.1999.809313
[137] K.VaidyanathanandK.S.Trivedi.2005.Acomprehensivemodelforsoftwarerejuvenation.IEEETrans.Depend.
SecureComput.2,2(Feb.2005),124–137.https://doi.org/10.1109/tdsc.2005.15
[138] KashiVenkateshVishwanathandNachiappanNagappan.2010.Characterizingcloudcomputinghardwarereliability.
InProceedingsofthe1stACMSymposiumonCloudComputing(SoCC’10).ACM,NewYork,NY,193–204.https://doi.
org/10.1145/1807128.1807161
[139] JingWang,DanielRossell,ChristosG.Cassandras,andIoannisCh.Paschalidis.2013.Networkanomalydetection:A
surveyandcomparativeanalysisofstochasticanddeterministicmethods.InProceedingsofthe52ndIEEEConference
onDecisionandControl.IEEE,182–187.https://doi.org/10.1109/CDC.2013.6759879
[140] QingWang,WubaiZhou,ChunqiuZeng,TaoLi,LarisaShwartz,andGenadyYa.Grabarnik.2017.Constructingthe
knowledgebaseforcognitiveITservicemanagement.InProceedingsoftheIEEEInternationalConferenceonServices
Computing(SCC’17).IEEE,410–417.https://doi.org/10.1109/scc.2017.59
[141] Song Wang, Taiyue Liu, and Lin Tan. 2016. Automatically learning semantic features for defect prediction. In
Proceedingsofthe38thInternationalConferenceonSoftwareEngineering (ICSE’16).ACM,NewYork,NY,297–308.
https://doi.org/10.1145/2884781.2884804
[142] WeiWang,MingZhu,JinlinWang,XuewenZeng,andZhongzhenYang.2017.End-to-endencryptedtrafficclassi-
ficationwithone-dimensionalconvolutionneuralnetworks.InProceedingsoftheIEEEInternationalConferenceon
IntelligenceandSecurityInformatics(ISI’17).IEEE,43–48.https://doi.org/10.1109/isi.2017.8004872
[143] YuWang,QiangMiao,EdenW.M.Ma,Kwok-LeungTsui,andMichaelG.Pecht.2013.Onlineanomalydetectionfor
harddiskdrivesbasedonmahalanobisdistance.IEEETrans.Reliabil.62,1(Mar.2013),136–145.https://doi.org/10.
1109/tr.2013.2241204
[144] AmyWard,PeterGlynn,andKathyRichardson.1998.Internetserviceperformancefailuredetection.ACMSIGMET-
RICSPerform.Eval.Rev.26,3(Dec.1998),38–43.https://doi.org/10.1145/306225.306237
[145] W.EricWong,VidrohaDebroy,RuizhiGao,andYihaoLi.2014.TheDStarmethodforeffectivesoftwarefaultlocal-
ization.IEEETrans.Reliabil.63,1(Mar.2014),290–308.https://doi.org/10.1109/tr.2013.2285319
[146] W.EricWong,RuizhiGao,YihaoLi,RuiAbreu,andFranzWotawa.2016.Asurveyonsoftwarefaultlocalization.
IEEETrans.Softw.Eng.42,8(Aug.2016),707–740.https://doi.org/10.1109/tse.2016.2521368
[147] RongxinWu,HongyuZhang,SunghunKim,andShing-ChiCheung.2011.ReLink:Recoveringlinksbetweenbugs
andchanges.InProceedingsofthe19thACMSIGSOFTSymposiumandthe13thEuropeanConferenceonFoundations
ofSoftwareEngineering(ESEC/FSE’11).ACM,15–25.https://doi.org/10.1145/2025113.2025120
[148] JiangXiao,ZhuangXiong,SongWu,YushengYi,HaiJin,andKanHu.2018.Diskfailurepredictionindatacenters
viaonlinelearning.InProceedingsofthe47thInternationalConferenceonParallelProcessing(ICPP’18).ACM,New
York,NY,Article35,10pages.https://doi.org/10.1145/3225058.3225106
[149] ChangXu,GangWang,XiaoguangLiu,DongdongGuo,andTie-YanLiu.2016.Healthstatusassessmentandfailure
predictionforharddriveswithrecurrentneuralnetworks.IEEETrans.Comput.65,11(Nov.2016),3502–3508.https:
//doi.org/10.1109/tc.2016.2538237
[150] HaowenXu,YangFeng,JieChen,ZhaogangWang,HonglinQiao,WenxiaoChen,NengwenZhao,ZeyanLi,Jiahao
Bu,ZhihanLietal.2018.Unsupervisedanomalydetectionviavariationalauto-encoderforseasonalKPIsinweb
applications.InProceedingsoftheWorldWideWebConference(WWW’18).ACM,NewYork,NY,187–196.https:
//doi.org/10.1145/3178876.3185996
[151] WeiXu,LingHuang,ArmandoFox,DavidPatterson,andMichaelI.Jordan.2009.Detectinglarge-scalesystem
problemsbyminingconsolelogs.InProceedingsoftheACMSIGOPS22ndSymposiumonOperatingSystemsPrinciples
(SOSP’09).ACM,NewYork,NY,117–132.https://doi.org/10.1145/1629575.1629587
ACMTransactionsonIntelligentSystemsandTechnology,Vol.12,No.6,Article81.Publicationdate:November2021.

ASurveyofAIOpsMethodsforFailureManagement 81:45
[152] ZhenghuaXue,XiaosheDong,SiyuanMa,andWeiqingDong.2007.Asurveyonfailurepredictionoflarge-scale
serverclusters.InProceedingsofthe8thACISInternationalConferenceonSoftwareEngineering,ArtificialIntelligence,
Networking,andParallel/DistributedComputing(SNPD’07).IEEE,733–738.https://doi.org/10.1109/snpd.2007.284
[153] XiaoxingYang,KeTang,andXinYao.2015.Alearning-to-rankapproachtosoftwaredefectprediction.IEEETrans.
Reliabil.64,1(32015),234–246.https://doi.org/10.1109/tr.2014.2370891
[154] Ding Yuan, Haohui Mai, Weiwei Xiong, Lin Tan, Yuanyuan Zhou, and Shankar Pasupathy. 2010. SherLog: Er-
rordiagnosisbyconnectingcluesfromrun-timelogs.ACMSIGARCHComput.Architect.News38,1(Mar.2010),
143–154.https://doi.org/10.1145/1735970.1736038
[155] Ding Yuan, Soyeon Park, Peng Huang, Yang Liu, Michael M. Lee, Xiaoming Tang, Yuanyuan Zhou, and Stefan
Savage.2012.Beconservative:Enhancingfailurediagnosiswithproactivelogging.InProceedingsofthe10thUSENIX
ConferenceonOperatingSystemsDesignandImplementation(OSDI’12).USENIXAssociation,293–306.
[156] AndreasZeller.2002.Isolatingcause-effectchainsfromcomputerprograms.InProceedingsofthe10thACMSIGSOFT
SymposiumonFoundationsofSoftwareEngineering(SIGSOFT’02/FSE’10).ACM,NewYork,NY,1–10.https://doi.org/
10.1145/587051.587053
[157] AndreasZeller.2006.EclipseBugData!—SoftwareEngineeringChair(Prof.Zeller)—SaarlandUniversity.Retrieved
fromhttps://www.st.cs.uni-saarland.de/softevo/bug-data/eclipse/.
[158] ChunqiuZeng,WubaiZhou,TaoLi,LarisaShwartz,andGenadyYaGrabarnik.2017.Knowledgeguidedhierarchical
multi-labelclassificationoverticketdata.IEEETrans.Netw.ServiceManage.14,2(62017),246–260.https://doi.org/
10.1109/tnsm.2017.2668363
[159] ChuxuZhang,DongjinSong,YuncongChen,XinyangFeng,CristianLumezanu,WeiCheng,JingchaoNi,BoZong,
HaifengChen,andNiteshV.Chawla.2019.Adeepneuralnetworkforunsupervisedanomalydetectionanddiag-
nosisinmultivariatetimeseriesdata.InProceedingsoftheAAAIConferenceonArtificialIntelligence,Vol.33.AAAI,
1409–1416.
[160] KeZhang,JianwuXu,MartinRenqiangMin,GuofeiJiang,KonstantinosPelechrinis,andHuiZhang.2016.Auto-
matedITsystemfailureprediction:Adeeplearningapproach.InProceedingsoftheIEEEInternationalConferenceon
BigData(BigData’16).IEEE,1291–1300.https://doi.org/10.1109/bigdata.2016.7840733
[161] ShenglinZhang,WeibinMeng,JiahaoBu,SenYang,YingLiu,DanPei,JunXu,YuChen,HuiDong,XianpingQu,
andetal.2017.Syslogprocessingforswitchfailurediagnosisandpredictionindatacenternetworks.InProceedings
oftheIEEE/ACM25thInternationalSymposiumonQualityofService(IWQoS’17).IEEE,1–10.https://doi.org/10.1109/
iwqos.2017.7969130
[162] XuZhang,YongXu,QingweiLin,BoQiao,HongyuZhang,YingnongDang,ChunyuXie,XinshengYang,Qian
Cheng, Ze Li, Junjie Chen, Xiaoting He, Randolph Yao, Jian-Guang Lou, Murali Chintalapati, Furao Shen, and
DongmeiZhang.2019.Robustlog-basedanomalydetectiononunstablelogdata.InProceedingsofthe27thACM
JointMeetingonEuropeanSoftwareEngineeringConferenceandSymposiumontheFoundationsofSoftwareEngineer-
ing(ESEC/FSE’19).ACM,NewYork,NY,807–817.https://doi.org/10.1145/3338906.3338931
[163] XuZhao,KirkRodrigues,YuLuo,MichaelStumm,DingYuan,andYuanyuanZhou.2017.Log20:Fullyautomatedop-
timalplacementoflogprintingstatementsunderspecifiedoverheadthreshold.InProceedingsofthe26thSymposium
onOperatingSystemsPrinciples(SOSP’17).ACM,NewYork,NY,565–581.https://doi.org/10.1145/3132747.3132778
[164] YingZhao,XiangLiu,SiqingGan,andWeiminZheng.2010.PredictingdiskfailureswithHMM-andHSMM-based
approaches.InProceedingsofthe10thIndustrialConferenceonAdvancesinDataMining:ApplicationsandTheoretical
Aspects(ICDM’10).Springer-Verlag,Berlin,390–404.
[165] ShuaiZheng,KostaRistovski,AhmedFarahat,andChetanGupta.2017.Longshort-termmemorynetworkforre-
mainingusefullifeestimation.InProceedingsoftheIEEEInternationalConferenceonPrognosticsandHealthManage-
ment(ICPHM’17)(2017–06).IEEE,88–95.https://doi.org/10.1109/icphm.2017.7998311
[166] WubaiZhou,LiangTang,TaoLi,LarisaShwartz,andGenadyYa.Grabarnik.2015.Resolutionrecommendationfor
eventticketsinservicemanagement.InProceedingsoftheIFIP/IEEEInternationalSymposiumonIntegratedNetwork
Management(IM’15).IEEE,287–295.https://doi.org/10.1109/inm.2015.7140303
[167] BingpengZhu,GangWang,XiaoguangLiu,DianmingHu,ShengLin,andJingweiMa.2013.Proactivedrivefailure
predictionforlargescalestoragesystems.InProceedingsoftheIEEE29thSymposiumonMassStorageSystemsand
Technologies(MSST’13).IEEE,1–5.https://doi.org/10.1109/msst.2013.6558427
[168] JiemingZhu,PinjiaHe,QiangFu,HongyuZhang,MichaelR.Lyu,andDongmeiZhang.2015.Learningtolog:Help-
ingdevelopersmakeinformedloggingdecisions.InProceedingsoftheIEEE/ACM37thIEEEInternationalConference
onSoftwareEngineering.IEEE,415–425.https://doi.org/10.1109/icse.2015.60
ReceivedApril2021;revisedJuly2021;acceptedAugust2021
ACMTransactionsonIntelligentSystemsandTechnology,Vol.12,No.6,Article81.Publicationdate:November2021.