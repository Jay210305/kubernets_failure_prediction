Empirical Software Engineering (2023) 28:143
https://doi.org/10.1007/s10664-023-10382-z
StudyingthecharacteristicsofAIOpsprojectsonGitHub
Roozbeh Aghili1 ·Heng Li1·Foutse Khomh1
Accepted:14August2023 / Published online: 18 October 2023
©TheAuthor(s),underexclusivelicencetoSpringerScience+BusinessMedia,LLC,partofSpringerNature2023
Abstract
Artificial Intelligence for IT Operations (AIOps) leverages AI approaches to handle the
massive amount of data generated during the operations of software systems. Prior works
haveproposedvariousAIOpssolutionstosupportdifferenttasksinsystemoperationsand
maintenance,suchasanomalydetection.Inthisstudy,weconductanin-depthanalysisof
open-sourceAIOpsprojectstounderstandthecharacteristicsofAIOpsinpractice.Wefirst
carefullyidentifyasetofAIOpsprojectsfromGitHubandanalyzetheirrepositorymetrics
(e.g., the used programming languages). Then, we qualitatively examine the projects to
understandtheirinputdata,analysistechniques,andgoals.Finally,weassessthequalityof
theseprojectsusingdifferentqualitymetrics,suchasthenumberofbugs.Toprovidecontext,
we also sample two sets of baseline projects from GitHub: a random sample of machine
learningprojectsandarandomsampleofgeneral-purposedprojects.Bycomparingdifferent
metrics between our identified AIOps projects and these baselines, we derive meaningful
insights. Our results reveal a recent and growing interest in AIOps solutions. However,
thequalitymetricsindicatethatAIOpsprojectssufferfrommoreissuesthanourbaseline
projects.WealsopinpointthemostcommonissuesinAIOpsapproachesanddiscusspotential
solutionstoaddressthesechallenges.Ourfindingsoffervaluableguidancetoresearchersand
practitioners, enabling them to comprehend the current state of AIOps practices and shed
lightondifferentwaysofimprovingAIOps’weakeraspects.Tothebestofourknowledge,
thisworkmarksthefirstattempttocharacterizeopen-sourceAIOpsprojects.
Keywords AIOps·Datamining·Repositorymining·Qualitativeanalysis·
Temporaltrends·Sourcecodeanalysis
Communicatedby: MarkusBorg
B
RoozbehAghili
roozbeh.aghili@polymtl.ca
HengLi
heng.li@polymtl.ca
FoutseKhomh
foutse.khomh@polymtl.ca
1 DepartmentofComputerEngineeringandSoftwareEngineering,PolytechniqueMontreal,Montreal,
QC,Canada
123
0123456789().: V,-vol

143 Page 2 of 49 Empirical Software Engineering (2023) 28:143
1 Introduction
Withtheprevalenceofgenerateddatainlarge-scalesystems,monitoringthisdataandtrans-
formingitintopracticalinsightsisbecomingacomplexchallenge.ArtificialIntelligencefor
ITOperations(AIOps)hasbeenintroducedtocopewiththischallenge.Itcombinesbigdata,
machinelearning(ML)approaches,andotheradvancedanalysistechniques(e.g.,statistical
analysis)toanalyzesystemperformancepatternstobeabletoimproveservicequalityand
reduceoperationalcosts(Dangetal.2019;PrasadandRich2018).ByutilizingAIOpstech-
niques,organizationsarenowabletocollectandcombinedifferentsourcesofsystemdata
andusethemtoperformvarioustasks(e.g.,anomalydetectionorfailureprediction)intheir
DevOpsoroperationsenvironment(Dangetal.2019;PrasadandRich2018).
A considerable amount of research has been performed on the topic of AIOps. Prior
workhasproposedAIOpssolutionsforvariousmaintenanceandoperationstasks,suchas
predictingnodefailures(Linetal.2018;Lietal.2020b),predictingtaskorjobfailures(Gao
etal.2020;El-Sayedetal.2017;Rosáetal.2015),anomalydetection(Heetal.2018b;Lim
etal.2014),andselfhealing(Dingetal.2012, 2014).However,noworkhassystematically
studiedAIOpspracticesinreal-worldprojects(e.g.,publicGitHubprojects).
Studying AIOps practices in real-world projects is important and has several benefits,
including(1)helpingresearchersandpractitionersunderstandthecurrentstatusofAIOps
solutionsandthecharacteristicsofAIOpsprojects;(2)providingguidanceforresearchersand
practitionerstoadoptbest–performingAIOpssolutionsfortheirapplicationscenarios;and(3)
identifyingproblemsinAIOpspracticesandsheddinglightsonfutureresearchopportunities.
Therefore,thisworkidentifiesandstudiesasetofAIOpsprojectspubliclyavailableon
GitHub. We also compare the selected AIOps projects with two baselines: traditional ML
projectsandGeneral–purposeprojects.Ourgoalistounderstandthecharacteristicsofthese
AIOpsprojectsinthecontextofthebaselineprojects.Specifically,wefirstinvestigatethe
overallcharacteristicsoftheseAIOpsprojectsintermsoftheirGitHubmetrics(RQ1),then
wedigdeeperintotheindividualprojectstounderstand“what”goalstheseprojectsaimto
achieve(RQ2),andfinally,weexaminehowwellthesegoalsareachievedintermsofthe
codequalityoftheseprojects(RQ3).Ourresearchquestionsareasfollows.
RQ1 What are the characteristics of AIOps projects in terms of their GitHub metrics?
We analyze the GitHub metrics of AIOps and baseline projects to understand the
current status of AIOps projects and also compare them with baselines in terms of
theirGitHubmetrics,suchastheprogramminglanguagesandthenumberofstars.We
observethatAIOpssolutionsarebeingdevelopedwithafastergrowthratecompared
tothebaselines.AIOpsprojectsalsohaveahigherdistributionofpopularitymetrics
(e.g.,numberofstarsandforks),andalsomorepullrequestsandissuescomparedto
baselines.
RQ2 WhatarethecharacteristicsofAIOpsprojectsintermsoftheirinputdata,analysis
techniques,andgoals?InordertounderstandthecharacteristicsofAIOpsprojects
(i.e., their input data, analysis techniques, and goals), we manually investigate each
project.Wefindthatmonitoringdata(e.g.,logsandperformancemetrics)isthemost
usedinputdata,classicalmachinelearningtechniquesarethemostadoptedanalysis
techniques,andanomalydetectionistheprimarygoalofmanyAIOpsprojects.
RQ3 WhatisthecodequalityofAIOpsprojects?Wefurtheranalyzethesourcecodeof
AIOpsandbaselineprojectstoidentifyanyinterestingpatternsrelatedtotheirquality.
WefindthatAIOpsprojectshaveahigherissuerate,specificallyintermsofbugs,code
smells,andtechnicaldebt,thanthebaselines.
123

Empirical Software Engineering (2023) 28:143 Page 3 of 49 143
WeshareourreplicationpackageonGitHub1sothatfutureworkcanreproduceorextend
ourstudy.Ourworkmakesseveralimportantcontributions:
1. AsthefirststudyonAIOpspracticesinreal-worldprojects,ourworkhelpspractitioners
andresearchersunderstandthestatusofAIOpsfromapracticalpointofview.
2. Ourqualitativeanalysisoftheinputdata,analysistechniques,andgoalsoftheAIOps
projectscanhelppractitionersandresearchersconsiderandadoptAIOpssolutionsthat
fitintotheirspecificapplicationscenarios.
3. OurworkidentifiesproblemsinAIOpspractices(e.g.,codequality)andshedslighton
futureresearchopportunitiesinAIOps.
The rest of the paper is organized as follows. Section2 describes the experiment setup
of our study, including the collection and preparation of the AIOps project data used for
answeringourresearchquestions.Section3presentsourapproachandresultsforanswering
theresearchquestions.Section4providesfurtherdiscussionsofourresults.Section5dis-
cussesthethreatstothevalidityofourfindings.Section6summarizespriorresearchrelated
toourwork,andfinally,Sect.7concludesourpaper.
2 ExperimentSetup
ThissectiondescribesourapproachforcollectingtheAIOpsandbaselineprojects.Wefirst
presenttheoverviewofourstudy,thendescribethestepsforcollectingandverifyingAIOps
andbaselineprojects,respectively.
2.1 OverviewofOurStudy
Figure1presentsanoverviewofourapproachtostudythecharacteristicsofAIOpsprojects.
WeuseGitHubasthemainsourcetoextracttheneededdataforouranalysis.AsofJanuary
2023,GitHubhasover100millionregistereddevelopersandover372millionrepositories
(GitHub2023).GitHubisalsoconsideredthelargesthostingserviceforopen-sourcesoftware
systems(Lietal.2020a).Hence,projectsfoundonGitHubarelikelytoreflectthediversityof
existingAIOpsprojects.Manyexistingstudiesalsoextracttheneededinformationfortheir
analysisfromGitHub(e.g.,Dakheletal.2023;Foalemetal.2023;Majidietal.2022;Openja
etal.2022).Westartbysearchingtheprojectswiththekeyword“AIOps”.Then,through
manualverification(e.g.,removingnon-AIOpsprojects),keywordexpansion(i.e.,through
patternmining),second-roundsearchandmanualverification,andthreshold-basedfiltering
(e.g.,bythenumberofstars),wecollectatotalof119AIOpsprojectsthatareusedtoanswer
ourresearchquestions.InordertobetterunderstandthecharacteristicsofAIOpsprojectsin
abiggercontext,wealsocompareouridentifiedAIOpsprojectswithtwobaselines:
1. randomlysampledmachinelearning(ML)projects;
2. randomlysampledgeneralprojects
WechoosetheMLbaselinebecausemostoftheAIOpsprojectsleverageMLtechniques.We
choosetheGeneralbaselinetocompareourAIOpsprojectswithgeneralsoftwareapplications
onGitHub.Finally,weperformqualitativeandquantitativeanalysesonthecollecteddata
toanswerourresearchquestions.Below,wedescribethedetailsofourdatacollection.The
detailedapproachesforansweringourresearchquestionsarepresentedinSect.3.
1 https://github.com/roozbehaghili/studying_aiops_github
123

143 Page 4 of 49 Empirical Software Engineering (2023) 28:143
Fig.1 Anoverviewofourstudy
2.2 CollectingAIOpsProjects
ThroughtworoundsofsearchingAIOps-relatedkeywordsonGitHub,wecollectatotalof
1016candidateprojects.Throughfilteringandmanualverification,weendupwith119of
them as our final set of AIOps projects. The methodology we use to select these projects
followsthesystematicapproachrecommendedbyBasilietal.(1986)andisdescribedinthe
followingsections.
2.2.1 SearchAIOpsProjects(FirstRound)
Intheinitialstepofidentifyingsuitableprojects,weutilizetheGitHubinterfacetosearch
forrepositoriesspecificallylabeledasAIOpsprojects.Todothis,weemploythekeyword
“AIOps” and search across four key sections of each repository: the repository name, the
“about”section,the“topics”section,andthecontentsofthe“readme”file.Aftersearching
forthekeyword“AIOps”,wefindatotalof542repositoriesthatmatchourcriteria.These542
repositoriesrepresentalltheavailableprojectsonGitHubthathavebeenlabeledasAIOps
projects.
2.2.2 ManualVerification(FirstRound)
BasedonexistingdefinitionsofAIOps(Dangetal.2019;PrasadandRich2018),weconsider
AIOpsprojectsas:anyprojectthatusesITOperations-relateddata,utilizesadvancedanal-
ysistechnologiessuchasmachine-learningorstatisticalanalysistoreachvaluableinsights
orenhancethesystem’squalitybyactionssuchasmonitoringandautomation.
Therefore,notallthe542discoveredrepositoriesaregoodAIOpscandidatesandsuitable
forourstudy.Wehenceselectoursubjectprojectsbasedonthreecriteria:
1. TheprojectshouldbeaboutAIOps,notsimilartopicssuchasMachineLearningOper-
ations(MLOps)2 orDevelopmentandOperations(DevOps).3 Therefore,wedeletethe
projectsthataremainlyaboutothertopics.
2 Asetofpracticestomaintainanddeploymachinelearningmodels.
3 Asetofpracticesthataimtoshortenthesystemdevelopmentlifecyclewhilepreservinghighquality.
123

Empirical Software Engineering (2023) 28:143 Page 5 of 49 143
2. Theprojectsshouldcontainsufficientcode.Therefore,wedeletetherepositoriesthatdo
nothaveanycodeoronlycontainafewlinesofcode.Wealsodeleteprojectsthatare
acollectionofpapers,slides,orotherrepositories.However,weaccepttheprojectsthat
havecreatedadatasetsothatotherdevelopersandresearcherscanuseitintheirwork.
3. Theprojectsshouldnotbetoyprojects:wedeletetheprojectsthatarehomeworkassign-
mentsoruniversityprojects.
Toselectthedesirableprojectsbasedontheexplainedcriteria,thefirsttwoauthorsofthe
paper(i.e.,coders)independentlyperformacodingprocess,addingaYES(AIOpsprojects)
orNO(non-AIOpsprojects)tagtoeachproject.Weperformthecodingprocessasbelow.
Step1:Coding.Eachcoderstudiesandanalyzesallthe542repositoriesandindepen-
dentlydecidesifeachprojectshouldbeaddedtothefinallistofprojects.
Step2:Discussion.Thecoderssharetheirresponsesanddiscusstheirapproachesfor
selectingaproject.Thediscussionsession’sgoalistoreachthesameunderstandingof
theinclusioncriteriaamongthecoders.
Step3:Revision.Basedonthediscussion,eachcoderrevisestheirresponsesfromstep
1.
Step4:Resolvingdisagreements.Inthelaststep,thecodersdiscussanyconflictsthat
mayremainandtrytoresolvethem.Ifanagreementcannotbereached,thethirdauthor
wouldanalyzetheproject,andavoteisperformed.
Afterperformingthemanualverificationprocess,weobtainatotalof99candidateAIOps
projectsfromthe542projectsderivedfromthesearchresults,whichcorrespondstoaselec-
tionrateof18%.
2.2.3 KeywordExtraction(PatternMining)
Expanding our search to gain a more comprehensive view of real-world AIOps projects
is necessary as the term “AIOps” was only introduced in 2018 (Prasad and Rich 2018).
Asaresult,someprojectsmighthaveexistedpriortotheintroductionofthisterminology,
implementingAIOpssolutionswithoutexplicitlyusingtheexactterm.Toachieveabroader
scope, we extend our search to include additional projects that may not explicitly label
themselvesasAIOpsrepositoriesbutare,infact,implementingAIOpssolutions.Toachieve
this,weextractallthetopicsassociatedwitheachofthe99AIOpsprojectsresultingfromthe
previousstep.Thesetopicscanbefoundinthe“topics”sectionofeachGitHubrepository.
We then use frequent pattern mining (Han et al. 2007), a method aimed at discovering
associationsandpatternswithinagivendataset.Specifically,weutilizethefrequentpattern
growthtechnique(Hanetal.2000, 2004)toidentifythemostcommontopicsamongGitHub
repositories. To conduct this analysis, we set the support parameter to 2, indicating that a
patternshouldappearinatleasttwoprojectsforconsideration.Throughthisapproach,we
identifyatotalof194patternsamongthetopicspresentintherepositories.Next,weperform
adiscussionsessioninvolvingallthreeauthorstodecidewhichpatternsholdpotentialfor
identifyingadditionalAIOpsprojects.Fromthisdiscussion,wenarrowdownourselection
to fourpairs oftwo-item patterns: “anomalydetection” and“loganalysis”, “loganalysis”
and“machinelearning”,“anomalydetection”and“machinelearning”,aswellas“machine
learning”and“metrics”.Alltheselectedkeywordpairsareamongthemostfrequentlyused
topicsintheprojects.WeusethesefoursetsofkeywordstofindmoreAIOpsrepositories.
123

143 Page 6 of 49 Empirical Software Engineering (2023) 28:143
2.2.4 SearchAIOpsProjects(SecondRound)
Usingthefourpairsofkeywordsobtainedinthepreviousstep,weconductthesecondround
of search on the GitHub interface to identify more projects related to AIOps. We follow
thesameprocessasdescribedinSect.2.2.1.Aftercompletingthissecond-roundsearchand
removinganyduplicatedprojectsthatwerealreadyidentifiedinthefirst-roundsearchresults,
wefindatotalof474uniqueprojects.
2.2.5 Filtering
Basedontheknowledgethatwehavegainedfromourfirst-roundmanualverification,we
applyafilteringphasetoremovethetoyprojects.Toachievethis,weemploytwofiltering
criteriabasedonthenumberofstarsandforksforeachproject.Specifically,weonlyconsider
projectsthathavebothstarsandforksgreaterthanorequalto1(stars:>=1&forks:>=1).
Thepurposeofremovingtoyprojectsistohaverelativelymatureprojectsandnotsoilour
results with small repositories (Munaiah et al. 2017). Given the limited number of AIOps
projects on GitHub, adding stricter filtering criteria would result in much fewer projects.
Therefore,wechoosealow-barfilteringapproachtoreducethemanualeffortofanalyzing
alltheprojectswithstarsorforksof0.
Weutilizethefilteringprocessforboththeprojectsfromthefirstandsecondroundsof
searches.Inthefirstround,wemanuallyverifyalltheprojectsbeforeapplyingthefiltering
step.Thisdeliberateapproachallowsustogainacomprehensiveunderstandingofthestatus
oftheAIOpsprojects.Followingthefilteringprocess,theinitiallyverified99projectsare
reducedto55.Fortheprojectsfromthesecondround,weopttoapplythefilteringbefore
themanualverificationprocess.Thisdecisionsavesunnecessarymanualeffortbyexcluding
projectsthatdonotmeetthefilteringcriteriafromthebeginning.
2.2.6 ManualVerification(SecondRound)
As detailed in Sect.2.2.2, not all of the repositories obtained from our initial search are
suitableforourstudy.Tocarefullyselecttheprojectsthatalignwithourresearchobjectives,
wecarryoutamanualverificationprocess,repeatingthestepsoutlinedinSect.2.2.2.During
thisverification,thecodersexamineall474projectsthatresultedfromtheexpandedkeyword
searchtodeterminetheirsuitabilityasrealAIOpsprojects.Afterstepsofseparatecoding,
discussion,revision,andresolvingdisagreements,weidentify64projectsfromtheexpanded
keyword search. This corresponds to a selection rate of 14%, Finally, we combine the 55
projectsidentifiedusingthe“AIOps”keywordwiththe64projectsdiscoveredthroughthe
expanded keywords. The final set of 119 AIOps projects is used to answer our research
questions.TheapproachesforansweringourresearchquestionsaredetailedinSect.3.
2.2.7 MeasuringtheReliabilityofOurManualVerification
Reliability is vital to ensure the validity of the coding results (Artstein and Poesio 2008).
Thecodingresultsarereliableifthereexistsacertainlevelofagreementbetweenthecoders,
knownasinter-coderagreement.Inthisstudy,weuseCohen’skappa(Cohen1960)tomeasure
thereliabilityoftheagreementsbetweentwocoders.Cohen’skappaisoneofthemostcom-
monapproachestomeasuringtheinter-coderagreement(ArtsteinandPoesio2008).Table1
123

Empirical Software Engineering (2023) 28:143 Page 7 of 49 143
Table1 InterpretationofCohen’s
ValueofCohen’sk LevelofAgreement
kappa
0-.20 None
.21-.39 Minimal
.40-.59 Weak
.60-.79 Moderate
.80-.90 Strong
.90-1 AlmostPerfect
indicatestherelationbetweenthevalueofCohen’skappaandthelevelofagreement(McHugh
2012).
OurmanualverificationforchoosingtheproperAIOpsprojectsachievesaCohen’skappa
of0.68beforethediscussionsession.Afterthediscussionsessionbetweenthecoders,the
kappascoreincreasedto0.84.AsshowninTable1,kappa≥0.80indicatesastrongagreement.
2.3 CollectingBaselineProjects
TounderstandhowAIOpsprojectsdifferfromtraditionalsoftwareprojects,wecreatetwo
baselines and compare the AIOps projects with them. We select Machine Learning (ML)
projectsasourfirstbaselineandGeneralprojectsasoursecondbaseline.
2.3.1 MachineLearningProjects
Forourinitialbaseline,wechooseMLprojects.WeselectMLforthefirstbaselinebecause
AIOpscanbeconsideredasanapplicationdomainofmachinelearning.Insimilarstudies,
researcherstypicallysearchforspecificframeworkstogatherMLprojectsonGitHub.For
example,Zhangetal.(2018)selecttheirprojectsetbysearchingthekeyword“TensorFlow”,
whileIslametal.(2019)gathertheirprojectsusingvariouskeywordssuchas“TensorFlow”
and“Keras”.However,asourfocusisnotlimitedtoanyspecificframework,weusemore
general keywords. To gather our set of ML baseline projects, we utilize two keywords:
“machinelearning”and“deeplearning.”Thisapproachallowsustocastabroadernetand
captureacomprehensiverangeofrelevantMLprojectsforcomparisonandanalysis.
TocomparetheAIOpsprojectswiththebaselinesinasimilarcontext,weapplyasimilar
filteringprocesstothebaselineprojects.LiketheAIOpsprojects,weonlyextractMLprojects
thathaveatleastonestarandonefork.Additionally,wetakeintoaccountthatMLprojects
generally have a longer history than AIOps projects. To address this difference, we apply
thesamedaterangeforthecreationoftheMLbaselineprojectsasobservedintheAIOps
set.Specifically,theearliestandlatestcreationdatesintheAIOpsprojectsare2012/12/25
and2022/10/27,respectively.Thus,weapplythesamedaterangetofiltertheMLbaseline
projects.Followingthesearchandremovalofduplicateprojectsintwoqueries,weobtain
a total of 87,276 unique repositories for the ML baseline. Due to time and computational
resourcelimitations,extractingandanalyzingalltheseprojectsbecomesimpractical.Hence,
followingpriorwork(e.g.,Chenetal.2020aandZhangetal.2019),asampleof383projects
isneededtorepresentthepoolof87,275MLrepositorieswithaconfidencelevelof95%and
aconfidenceintervalof5%.
123

143 Page 8 of 49 Empirical Software Engineering (2023) 28:143
2.3.2 GeneralProjects
Asoursecondbaseline,wechoosegeneralprojectsfromGitHub,meaningthatwedonot
focusonanyparticulartopicinoursearch.WealsodonotlimittheGeneralbaselinetoa
specificprogramminglanguage(e.g.,Python)sinceAIOpsprojectsarenotlimitedtoasingle
language as well. In this way, the General baseline captures the general characteristics of
allGitHubprojects.WethenapplythesamefilteringphaseaswedidfortheMLbaseline,
butwithoutindicatinganyspecifictopic.Aftercompletingthefiltering,weobtain4,358,342
public and available repositories for the General baseline. Similar to the ML baseline, a
sampleof385projectsisrequiredtorepresentthepoolof4,358,342Generalrepositories
withaconfidencelevelof95%andconfidenceintervalof5%.
2.3.3 ManualVerification
In order to maintain consistency with our methodology for selecting AIOps projects, we
applymanualverificationtoourtwobaselinesetsaswell.Theselectionofbaselineprojects
isbasedontwokeycriteria:
1. Theprojectsshouldcontainsufficientcodeandbemature.Therefore,wedeletetherepos-
itoriesthatdonothavecodeandareacollectionofpapers,slides,orotherrepositories.
2. Theprojectsshouldnotbetoyprojects:wedeletetheprojectsthatarehomeworkassign-
mentsoruniversityprojects.
Toconstructourbaselinesets,werandomlyextract500projectsfrombothMLandGeneral
poolofrepositories.Wethendivideeachsetofbaselineprojectsintotwopartsof20%and
80%portions.SimilartoSect.2.2.2,thetwocodersindependentlylabel20%ofeachbaseline
toensureareliableassessment.WethenmeasurethereliabilityofourcodingusingCohen’s
kappa(Cohen1960).TheresultsofourmanualverificationforchoosingtheMLandGeneral
baselinesindicateastrongagreementbetweenthecoders,withCohen’skappascoresof0.81
and0.91,respectively.Asthemeasurementshowsastrongagreementbetweencoders,the
restofbaselineprojects(the80%portions)arelabeledbythefirstcoder.
Wecontinueourmanuallabelingprocessuntilweobtainthestatisticalrepresentativeset
foreachbaseline.InthecaseofMLprojects,wethoroughlyanalyze477projects,ultimately
selecting383ofthemtocreateourfinalsetofMLbaseline.Similarly,fortheGeneralprojects,
wethoroughlyanalyze439projects,resultingintheselectionof385projectsasourfinalset
ofGeneralbaseline.
AsshowninFig.1,wecompareourAIOpsprojectswiththebaselineprojectsinRQ1
wherewestudytherepositoriesstatisticsoftheprojects,aswellasinRQ3wherewestudythe
codequalityoftheprojects.InRQ2,weperformaqualitativestudyfortheAIOpsprojects
only, since the research question is specifically about AIOps projects (i.e., the input data,
analysistechniques,andgoalsofAIOpssolutions).
3 ResearchQuestionsandResults
Thissectionpresentsthedetailsofourresearchquestions(RQs)andtheresults.Weorganize
eachRQbyitsmotivation,approach,andresults.
123

Empirical Software Engineering (2023) 28:143 Page 9 of 49 143
3.1 RQ1.WhataretheCharacteristicsofAIOpsProjectsinTermsoftheirGitHub
Metrics?
3.1.1 Motivation
Prior studies proposed AIOps solutions that leverage AI technologies to support various
softwareoperationefforts(DiStefanoetal.2021;Lietal.2022a, 2020b).However,nowork
hasinvestigatedreal-worldAIOpsprojectsandtheircharacteristics.Thus,thisRQbridges
thegaptostudythecharacteristicsofAIOpsprojectsandcomparethemwiththebaseline
projectsintermsoftheirGitHubmetrics.Withthiscomparison,wecanunderstandthesimilar
anddifferentpatternsbetweenthecharacteristicsofAIOpsprojectsandthebaselines.Our
findings can help AIOps researchers and practitioners understand the state of AIOps in
practice.
3.1.2 Approach
InthisRQ,weanalyzetherepositorycharacteristicsofAIOpsprojectsandcomparethem
withthebaselineprojects.WeuseWewriteascripttoextractthemetricsofbothAIOpsand
baselineprojects.WeuseGitHubRESTAPI(GitHub2022)toretrievetherepositorychar-
acteristicsoftheseprojects.Inparticular,weanalyzethecharacteristicsofAIOpsprojects
andthebaselineprojectsfromthreeperspectives:growthofrepositories,programminglan-
guages,andrepositorymetrics.
Growthofrepositories TounderstandtheevolutionofthepopulationofAIOpsprojects,we
analyzethedistributionoftheAIOpsprojectsbasedontheircreationtime.Wealsocompare
thecreationtimedistributionwiththatofthebaselineprojects.
Programminglanguages DevelopersmayusedifferentprogramminglanguagesforAIOps
projects.Understandingthedistributionoftheprogramminglanguagescanprovideinsights
forfutureworktosupportAIOpsprojectdevelopment.Eachprojectmayusemultiplepro-
gramming languages. In this work, we extract and present the primary language of each
project.
Repositorymetrics We study the repository metrics of the AIOps projects, including the
number of stars, forks, commits, contributors, releases, pull requests, issues, size, and the
statusofbeingarchived.Similarly,fortheissues,wesumtheopenandclosedissues.
Statisticaltests Wefurtherperformstatisticalteststoevaluatethestatisticallysignificant
differencebetweenmetricsforAIOpsandbaselineprojects.WefirstconducttheShapiro-
Wilk test (Shapiro and Wilk 1965) to test the normality of our metrics. Using the widely
accepted0.05significancethreshold,theShapiro-WilktestshowsthattheGitHubmetrics
of AIOps and baseline projects do not follow a normal distribution. Since our data is not
normally distributed, we select nonparametric tests. We use Mann–Whitney U test (Mann
andWhitney1947)tocompareoursamples.WealsouseCliff’sdeltatest(Cliff1993)totest
theeffectsizebetweenoursamples.RegardingMann-WhitenyUtest,weusethesignificance
thresholdof0.05.RegardingCliff’sdeltatest,weusethescalepresentedbyRomanoetal.
(2006),thateffectof|d|=0.147issmall,|d|=0.33ismedium,and|d|=0.474islarge.
123

143   Page 10 of 49 Empirical Software Engineering (2023) 28:143
Fig.2 ThecumulativedistributionofthecreationtimeofAIOpsandbaselineprojects
3.1.3 Results
Compared to the ML and General baselines, AIOps projects are relatively new and
exhibitrapidgrowthinrecentyears Fig.2representsthepercentageofprojectscreated
inandbeforeeachyearfortheAIOpsandbaselineprojects.AsmentionedinSect.2.3,the
creationdateofalltheprojectsisbetween2012/12/25and2022/10/27.AsshowninFig.2,
inthefirstfewyears(from2012to2017),thenumberofAIOpsprojectsisverysmall.In
recentyears(from2017to2022),theAIOpsprojectsexperienceafastergrowthcomparedto
theMLandGeneralbaselines.Ascanbeseen,theMLprojectsalsoexhibitafastergrowth
thantheGeneralbaselineprojects.
Like in ML projects, Python is the dominant programming language in the AIOps
projects; however, unlike in ML projects, Java is also a major programming lan-
| guage used | in AIOps projects |          |                    |                  |          |
| ---------- | ----------------- | -------- | ------------------ | ---------------- | -------- |
|            |                   | As shown | in Table 2, Python | is the most used | language |
among all the groups; however, the usage of Python is much higher in AIOps and ML
repositoriesthanintheGeneralbaseline(71.4%and81.7%incontrastto21.6%).Another
interestingfindingistherelativelyhighusageofJavainAIOpsprojects(10.1%),whileJava
isnotamongthetop-5popularlanguagesintheMLbaseline.
On average, AIOps projects are more popular and active than the baselines Fig.3
representstheboxplotsofGitHubmetricsfortheAIOpsprojectsandthebaselines.Table3
Table2 Thetop-5languagesofAIOpsandbaselineprojects
| AIOps      |          | ML         |          | General    |          |
| ---------- | -------- | ---------- | -------- | ---------- | -------- |
| Language   | Usage(%) | Language   | Usage(%) | Language   | Usage(%) |
| Python     | 71.4     | Python     | 81.7     | Python     | 21.6     |
| Java       | 10.1     | HTML       | 2.6      | JavaScript | 16.4     |
| Go         | 3.4      | R          | 1.8      | Java       | 8.1      |
| HTML       | 2.5      | C++        | 1.8      | TypeScript | 4.7      |
| JavaScript | 1.7      | JavaScript | 1.8      | PHP        | 4.4      |
123

Empirical Software Engineering (2023) 28:143 Page 11 of 49 143
Fig.3 BoxplotsofGitHubmetricsforAIOpsandbaselineprojects.Themediannumberof0forthereleases,
pullrequests,andissuesindicatethatmorethanhalfoftheprojectsdonothaveanyrelease,pullrequest,or
issue
123

143 Page 12 of 49 Empirical Software Engineering (2023) 28:143
Table3 Detailedresultsof
Metric AIOpsvs.ML AIOpsvs.General
Mann–WhitneyUandCliff’s
p-value effectsize p-value effectsize
deltatestsonprojects’GitHub
metrics Stars 0.00 ** 0.00 ***
Forks 0.00 ** 0.00 ***
Commits 0.34 - 0.92 -
Contributors 0.00 ** 0.02 *
Releases 0.04 * 0.87 -
Pullrequests 0.00 ** 0.59 -
Issues 0.00 ** 0.01 *
Size 0.02 * 0.00 ***
Mann–WhitneyUresultsareshowninp-valuecolumns.Ifthesetshave
statisticallydifferentdistributions,theCliff’sdeltaresultsareshownin
effectsizecolumns
*:negligibleeffect**:smalleffect***:mediumeffect
showsthep-valueandeffectsizeoftheGitHubmetricsofAIOpsprojectscomparedtothe
baselines.
Considering the number of stars and forks, AIOps projects are more popular than the
baselines,asbothmedianandmeanvaluesinAIOpsprojectsarehigherthanthebaselines.
In terms of the median value, AIOps projects have 4 times more stars and forks than the
Generalbaseline(medianvaluesofstarsinAIOpsandGeneralprojectsare17and4,and
medianvaluesofforksinAIOpsandGeneralprojectsare8and2).Regardingthestatistical
test results in Table 3, the p-value of stars and forks indicate that AIOps projects have
statisticallydifferentdistributionsfromMLandGeneralbaselines.Forbothofthemetrics,
theeffectsizeissmallcomparedtotheMLbaselineandismediumcomparedtotheGeneral
baseline.
Regardingthenumberofcommits,asshowninthestatisticaltestresultsinTable3,thereis
notastatisticallysignificantdifferencebetweenAIOpsandbaselines.Regardingthenumber
ofcontributors,itseemsthatAIOpsprojectsaremorecollaborative(medianof2inAIOps
and 0 in baselines). Statistical results also corroborate this finding, with the effect size of
small compared to ML baseline and negligible (with a statistically significant difference)
comparedtoGeneralbaseline.Regardingthenumberofreleases,thereisnotasignificant
differencebetweenAIOpsandGeneralbaseline;however,AIOpsprojectshaveastatistically
significantdifferencecomparedtoMLbaseline.
Comparingthenumberofpullrequestsandissues,asshowninFig.3fand3g,wenotice
thatAIOpsprojectsexperiencemorepullrequestsandissues.Statisticalresultsalsoconfirm
thisfinding,asp-valuesofpullrequestsandissuesarelessthan0.05(exceptpullrequests
for General baseline). This may be explained in three ways. First, the AIOps projects are
moreactiveandpopular(i.e.,moredevelopersproactivelydevelopthem),leadingtoamore
significantnumberofpullrequestsandissues.ThesecondinterpretationmightbethatAIOps
projectsareinthefirststagesofformationandnotmatureenough,havingmoredefectsand
flawsandmoredeveloperstryingtofixtheseproblems.ThethirdexplanationisthatAIOps
projectsareonaveragelargerthanthetwo baselineprojects(asshowninFig.3h),which
mayleadtomorepullrequestsandissues.
Comparingthesizeoftheprojects,AIOpsprojectstendtobelargerthanGeneralbaseline
asthestatisticaltestsindicateamediumeffectsize.AIOpsprojectsalsoarelargerthanML
123

Empirical Software Engineering (2023) 28:143 Page 13 of 49 143
projects;however,thedifferenceisnotaslargeasGeneralbaseline,asthestatisticaltests
resultinanegligible(withastatisticallysignificantdifference)effectsize.Comparingthe
medianvalues,thesizeofAIOpsprojectsis7timeslargerthanGeneralbaseline(7.6MB
forAIOpsprojectscomparedto1.0MBforGeneralbaseline).
Wefurtheranalyzethepercentageofprojectsthathavebeenarchived.Theresultsindicate
thatonly1.7%ofAIOpsprojectshavebeenarchived,whilethisamountforMLandGeneral
baselineis1.8%and4.2%,respectively.
Overall,takingintoconsiderationallthementionedmetrics,AIOpsprojectsseemtobe
moreactiveandpopularthanbothbaselines.
SummaryofRQ1
Onaverage,AIOpsprojectsarereceivingmoreattentionthantheMLandGeneral
baselines. The primary language used in them is Python, followed by Java. They
are growing faster than the baselines in recent years, demonstrating the growing
needsandactivepracticesinthisarea.ThesizeofAIOpsprojectsislargerthanthe
baselines,andfocusingonotherGitHubmetricssuchasnumberofstars,forks,and
releases,AIOpsprojectsseemtobemorepopularandactivethanbothbaselines.
3.2 RQ2.WhataretheCharacteristicsofAIOpsProjectsinTermsoftheirInputData,
AnalysisTechniques,andGoals?
3.2.1 Motivation
AIOpsresearchersandpractitionersleveragedifferenttechniquestoanalyzedifferenttypes
ofoperationaldataandachievedifferentgoals.However,itisunclearhowrealAIOpsprojects
leveragedataandtechnologiestoachievethegoals.InthisRQ,wequalitativelyanalyzeour
setofAIOpsprojectstounderstandthecharacteristicsoftheseprojects’inputdata,analysis
techniques,andgoals.Ourresultscanhelpresearchersandpractitionersfurtherunderstand
thestatusofAIOpspracticesandthecharacteristicsofAIOpsprojects.Ourresultscanalso
provideinsightsforfutureworktoprovidesupportfordifferentAIOpsapplicationscenarios.
3.2.2 Approach
WemanuallyexamineeachAIOpsprojecttounderstanditsinputdata,analysistechniques,
andgoals.Foreachproject,wemanuallyinvestigatefoursourcesofinformation;the“about”
section,the“readme”file,thesourcecode,andtheadditionaldocumentationsifavailable.
Figure4illustratesthethreekeyconceptsofourmanualanalysis(inputdata,analysistech-
niques,andgoals)andtheirrelationship.
– Inputdata:Thetypesofdata(e.g.,logdata)thatanAIOpsprojecttakesasinputsto
achieveitsobjectives.
Fig.4 Thethreekeyconceptsofourmanualanalysis
123

143 Page 14 of 49 Empirical Software Engineering (2023) 28:143
Fig.5 ThecategorizationoftheinputdatausedinAIOpsprojects.Thehighlevelcategoriesarehighlighted
indark
– Analysistechniques:Themainanalysistechniques(e.g.,machinelearningtechniques)
thatanAIOpsprojectadoptstoanalyzetheinputdataandachieveitsobjectives.
– Goals:Theobjectives(e.g.,anomalydetection)thatanAIOpsprojectaimstoachieve
throughitsinputdataandanalysistechniques.
Manual coding process We use open coding approach (Khandkar 2009) to extract the
informationrelatedtothethreekeyconceptsshowninFig.4.Opencodingiswidelyused
amongsoftwareengineeringresearcherstoconcludeahigh-levelabstractionfromlower-level
data(Stoletal.2016;WohlinandAurum2015).Tolabeltheprojects,thefirsttwoauthors
ofthepaper(i.e.,coders)jointlyperformacodingprocess,determiningeachproject’sinput
data,analysistechniques,andgoals.Weperformafive-stepcodingprocessasfollows.
Step1:Coding.Eachcoderanalyzesthe97AIOpsprojectsandassignlabelsforeach
concept(inputdata,techniques,andgoals)ofeachproject.Multiplelabelscanbeassigned
toaconceptofaproject.Thissteptakesafewdaysforeachcodertocomplete.
Step2:Discussion.Thecoderssharetheirresponsesanddiscussthecreatedlabels.The
maingoalofthediscussionsessionistoobtainacommonunderstandingofthelabelsforthe
inputdata,techniques,andgoals.Basedontheseparatelabelsofthecoders,wejoinrelated
labelstogetherandtakeapartsomehigh-levellabelsintosmallerones.Afterthissession,we
finalizethelabelsforeachconcept(inputdata,techniques,andgoals).
Step 3: Revision. Based on the results of the discussion session and the agreed-upon
labels,eachcoderreviseshisresponsesfromStep1.
Step 4: Resolving disagreements. The coders compare their final results from step 3
anddiscussanyconflictthatmayremain.Thecoderstrytoresolvetheconflicts,butifan
agreementcannotbereached,thethirdauthoranalyzestheproject,andthefinaldecisionis
made.
Step5:Finalrevision.Inthefinalstage,wecreateamindmapfromalltheproduced
labels. We then discuss the labels and form an hierarchy, change some labels’ names for
clarity,andmergesomesmallcategoriestobecohesive.
3.2.3 Results
Figs.5,6,and7presentourcategorizationoftheinputdata,analysistechniques,andgoalsof
theAIOpsprojects,process,respectively.WefurtherdefineourcodinglabelsinTables4,5,
and6.Itisimportanttonotethateachprojectmayhavemultipleinputdata,analysistech-
niques,orgoals.
123

Empirical Software Engineering (2023) 28:143 Page 15 of 49 143
Fig. 6 The categorization of the analysis techniques (LSTM approaches can be used in a supervised or
unsupervisedmanner(Chenetal.2021).Inoursetofprojectsandprimarilyforanomalydetection,projects
useLSTMintheunsupervisedform)usedinAIOpsprojects.Thehighlevelcategoriesarehighlightedindark
Inputdata:Monitoringdata(e.g.,logs,performancemetrics,andnetwork-trafficdata)is
thedominanttypeofinputdataoftheAIOpsprojects,withlogsbeingthemostcom-
monlyusedinputdatatype The categorization of the input data is illustrated in Fig. 5.
WedividetheinputdataofAIOpsprojectsintofivemaincategories:monitoringdata,multi-
media,codebase,technicalquestion-answer(QA)data,andalarm.Wedefinethesecategories
Fig.7 ThecategorizationofthegoalsoftheAIOpsprojects.Thehighlevelcategoriesarehighlightedindark
123

143 Page 16 of 49 Empirical Software Engineering (2023) 28:143
andprovideanexampleforeachinTable4.Amongthem,monitoringdataisthemostpopular,
usedin87%oftheprojects.Themonitoringdataisdividedinto6sub-categories:log,per-
formancemetric,network-trafficdata,KeyPerformanceIndicator(KPI),InternetofThings
(IoT)sensordata,andtrace.Amongthem,logdataisthemostcommonlyused.Thesedata
typescouldbeusedfordifferentpurposessuchasextensivemonitoring,debugging,perfor-
manceanalysis,testanalysis,andbusinessanalytics(ChenandJiang2021;Svobodaetal.
2015).Inthispaper,weusetheumbrellatermof“monitoringdata”tonamethesedatatypes.
WefindtwointerestinginputdatatypesfortheAIOpsprojects:networktrafficandIoT
sensordata.Aconsiderableproportionoftheprojects(21%)usenetworktrafficdataastheir
input.Also,8%ofprojectsuseIoTsensordata.
ThesecondpopularcategoryofinputdataforAIOpsapproachesismulti-media(image,
video,oraudio)(5%),followedbycodebase(5%),technicalQ/Adata(2%),andalarm(1%).
Wedefinetheinputofaprojectas“codebase”ifitanalyzesthesourcecodeorconfiguration
filesofothersoftware.Wedefinetheinputas“technicalQ/Adata”iftheprojectanalyzes
datafromQ/AwebsiteslikeStackOverflow.
Analysistechniques:Classicalmachinelearningmodelsarethemostcommonlyused
analysis techniques, followed far behind by deep learning, statistical analy-
sis,andtimeseriesmodels Wepresentourcategorizationoftheappliedanalysistechniques
of AIOps projects in detail in Fig. 6. We derive 9 high-level categories: classic machine
learning(54%),deeplearning(14%),statisticalanalysis(9%),timeseriesmodels(7%),log
parsing(7%),others(3%),naturallanguageprocessing(2%),unknown(2%),andN/A(2%).
DefinitionsandexamplesforeachcategorycanbefoundinTable5.
Boththeclassicmachinelearninganddeeplearningcategoriesarefurtherdividedinto
supervisedandunsupervisedlearningalgorithms.
Overall, considering supervised and unsupervised usage in classical machine learning
anddeeplearningapproaches,37%oftheprojectsinourstudyemploysupervisedlearning,
while 31% utilize unsupervised approaches. Hence, the difference between the adoption
ofsupervisedandunsupervisedmethodsisnotsubstantial.Therefore,wecouldnotfinda
strongcorrelationwithDangetal.(2019),wheretheystatethatinmanyAIOpscases,only
unsupervisedmachinelearningmodelsare practical.However,we findthat someprojects
in our study explore a combination of supervised and unsupervised models, conducting
comparisonstoassesstheirperformanceforspecifictasks.Whileunsupervisedtechniques
outperforms the supervised approaches in scenarios where data labeling is limited or new
patternsofdatacanemerge,therearealsoinstanceswheresupervisedapproachesachieve
betterresults.Forexample,asmentionedbyHeetal.(2016);Chenetal.(2021),supervised
machinelearningalgorithmsusuallyoutperforminanomalydetectionusecases.
Thefollowingthreecommontechniquesarestatisticalanalysis,timeseriesmodels,and
logparsing.Wefindthreemajorstatisticalanalysistechniques:descriptiveanalysis,outlier
detection,andexploratoryanalysis.Wecategorizethetechniqueofaprojectasdescriptive
analysisifitanalyzesthedatanumerically,andwegroupitasexploratoryifitusesvisual-
izationtoanalyzethedata.Usually,theexploratoryanalysiswillbedoneafterperforming
thedescriptiveanalysis.
Asmostoftheinputdataistimeseries(e.g.,logs,performancemetrics,networktraffic
data),itisnotsurprisingthatsomeprojectsusetimeseriestechniquestomodeltheirdata.
123

Empirical Software Engineering (2023) 28:143 Page 17 of 49    143
Table4 Differenttypesofinputdata,theirdefinitions,andexamples
| Inputdata      | Definition                     | Repositoryexample |
| -------------- | ------------------------------ | ----------------- |
| MonitoringData | Differenttypesofdatathatrecord |                   |
theruntimestatusofasystem.
| Log | System-generateddatathat | Repository(58811148)useslog |
| --- | ------------------------ | --------------------------- |
|     | recordsruntimeeventsthat | dataasinputtoperform        |
|     | havehappened.            | anomalydetection.           |
Performancemetric Quantitativemeasurementsused Repository(160285839)uses
|     | totracktheperformanceofa    | differentperformancemetrics |
| --- | --------------------------- | --------------------------- |
|     | system.Thesemetricsareoften | suchasCPUandmemory          |
|     | operational,suchasCPUusage. | usagetoperformvarioustasks  |
suchasanomalydetectionand
timeseriesforecasting.
Network-trafficdata Monitoringdatathatrecords Repository(79239275)uses
|     | networkactivities. | network-trafficdatatoidentify |
| --- | ------------------ | ----------------------------- |
maliciousbehaviorsand
attacks.
| KPI | Measurementsrelatedtokey | Repository(142442484)uses    |
| --- | ------------------------ | ---------------------------- |
|     | businessgoalsofasystem.  | differentKPIsintimeintervals |
|     | Thesemetricsareoften     | toidentifyimpactfulsystem    |
|     | strategic.               | problems.                    |
IoTsensordata Datacollectedbydevices Repository(142325304)uses
|     | connectedtoanIoTnetwork. | real-timeIoTsensordatato |
| --- | ------------------------ | ------------------------ |
detectanomalies.
Trace Aspecializeduseofloggingto Repository(397983735)gathers
|     | recordinformationabouta | adatasetoftracesthatcanbe |
| --- | ----------------------- | ------------------------- |
|     | system’sexecutionwith   | usedtoanalyzeoperations   |
|     | comprehensivedetails.   | problems.                 |
Multi-media Differenttypesofmulti-media Repository(287642401)
|     | data,includingimages,videos, | generatessummariesofdata   |
| --- | ---------------------------- | -------------------------- |
|     | andaudios.                   | typesincludingimagedatafor |
monitoringpurposes
Codebase Sourcecodeandconfiguration Repository(201529303)canbe
|     | filesofsoftwaresystems. | installedonKubernetessource |
| --- | ----------------------- | --------------------------- |
codeandprovide
self-monitoringand
self-healing.
TechnicalQ/Adata Datacollectedfromtechnical Repository(345320486)extracts
|     | Q/AwebsitessuchasStack | informationfromStack        |
| --- | ---------------------- | --------------------------- |
|     | Overflow.              | Overflowtofindfastsolutions |
forfaultsintheirplatform.
| Alarms | Alarmsgeneratedduringsystem | Repository(160285839)uses  |
| ------ | --------------------------- | -------------------------- |
|        | runtime.                    | alarmstofindtheassociation |
rulesbetweenthem.
TofindaGitHubrepositorywithitsID,onecaneitherclickthehyperlinkorusethelinkhttps://api.github.
com/repositories/{ID}where{ID}isreplacedbyaspecificrepositoryID
123

143   Page 18 of 49 Empirical Software Engineering (2023) 28:143
Table5 Differenttypesofanalysistechniques,theirdefinitions,andexamples
| Analysistechniques     | Definition             | Repositoryexample |
| ---------------------- | ---------------------- | ----------------- |
| Classicmachinelearning | Classicmachinelearning |                   |
techniquessuchasLogistic
RegressionandDecisionTree.
Supervised-learning Aleaningtechniquethatuses Repository(165321356)uses
|     | labeleddatasets. | variousclassicsupervised |
| --- | ---------------- | ------------------------ |
approachessuchasRandom
ForestandDecisionTreeto
detectanomaliesinKPIdata.
Unsupervised-learning Anapproachthatsystemlearns Repository(58811148)
|     | withoutusinglabeleddatasets. | implementsmultiple |
| --- | ---------------------------- | ------------------ |
unsupervisedapproachessuch
asIsolationForestandInvariant
Minertodetectanomalies.
| Deeplearning | Asubfieldofmachinelearning |     |
| ------------ | -------------------------- | --- |
thatusesartificialneural
networkswithmultiplelayers
(i.e.,deepneuralnetworks).
Supervised-learning Aleaningtechniquethatuses Repository(187774599)uses
|     | labeleddatasets. | ArtificialNeuralNetworkto |
| --- | ---------------- | ------------------------- |
findanomalousbehavioronIoT
sensordata.
Unsupervised-learning Atechniquethatlearnspatterns Repository(246569386)uses
|     | fromunlabelleddata. | LongShort-TermMemoryto |
| --- | ------------------- | ---------------------- |
detectanomaliesfromlogdata.
| Statisticalanalysis | Analyticaltechniquesto |     |
| ------------------- | ---------------------- | --- |
understand,analyzeand
interprettheinputdata.
Descriptiveanalysis Describingthefeaturesofdata Repository(114942949)uses
|     | andsummarizedataina   | descriptiveanalysissuchas |
| --- | --------------------- | ------------------------- |
|     | quantitativelymanner. | measuringminimumand       |
maximumvaluesandplotting
scatterfigurestointerprettheir
IoTsensordata.
Statisticaloutlierdetection Applyingstatisticaltestssuchas Repository(156308650)uses
|     | z-scoretoidentifyoutlier | z-scoretesttodetectanomalies |
| --- | ------------------------ | ---------------------------- |
|     | values.                  | onCPUusagedata.              |
Exploratoryanalysis Exploringdatatoidentifynew Repository(123162193)uses
|     | connections,inspectmissing | exploratoryanalysissuchas  |
| --- | -------------------------- | -------------------------- |
|     | data,orcheckhypotheses.    | plottinganddescribingtheir |
logdatatoinspectand
understandtheirinputdata.
Timeseriesmodel Techniquesthataimtomodel Repository(302842095)applies
|     | timeseriesdata,mainlyused | differenttimeseriesmodels |
| --- | ------------------------- | ------------------------- |
|     | forfindingtrendsand       | suchasAutoRegressionand   |
|     | forecasting.              | Holt-winterstodetect      |
anomaliesandanalyzeroot
causes.
Logparsing Techniquesthatanalyzeand Repository(345575577)uses
|     | extractinformationfromlog | Draintodologparsing.Itthen  |
| --- | ------------------------- | --------------------------- |
|     | data.                     | usestheextractedinformation |
toperformanomalydetection.
123

Empirical Software Engineering (2023) 28:143 Page 19 of 49 143
Table5 continued
Analysistechniques Definition Repositoryexample
Naturallanguageprocessing Techniquesthataimtoanalyze Repository(316407231)
andmodeltextdata. leveragesBidirectional
EncoderRepresentationsfrom
Transformers(BERT),a
pre-trainedlanguagemodelas
oneoftheirtechniquesto
performanomalyprediction.
OthersUnknown Othertechniquesthatcouldnot Repository(146802240)uses
becategorizedinprevious fuzzymatchingtoclassifyweb
categories. queries.Projectsforwhichwe
couldnotfindanyspecific
techniques.
N/A Projectsthatonlyprovide Repository(238914477)isa
datasetsordonotuseany datasetofKPIdataanddoes
analysistechniques. notuseanyanalysistechniques.
TofindaGitHubrepositorywithitsID,onecaneitherclickthehyperlinkorusethelinkhttps://api.github.
com/repositories/{ID}where{ID}isreplacedbyaspecificrepositoryID
AutoRegressiveIntegratedMovingAverage(ARIMA)isthemostcommontime-seriestech-
niquefollowedbyExponentiallyWeightedMovingAverage(EWMA).
AsshowninFig.5,logsarethemost-usedinputdatainAIOpsprojects.Tohandlelogs,
projectseitheruselogparsingtechniquesorNaturalLanguageProcessing(NLP)approaches.
Regardinglogparsingtechniques,developerstendtowritetheircustomizedversionoflog
parsers(with64%).Aftercomingupwithcustomizedlogparsers,themostcommonlogparser
thatisusedamongAIOpsprojectsisDrain(with20%).RegardingNLPapproaches,only
2%ofAIOpsprojectsusethem,withWord2vecandBERTasthemostcommontechniques.
withtherecentdevelopmentsintheNLPfield,forexamplegeneratinglanguagemodelssuch
asBERT(Devlinetal.2018)andCodeBERT(Fengetal.2020),webelieveAIOpssolutions
canalsobenefitmorefromNLPtechniques.Wediscussthispointinmoredetailin
Goals:AnomalydetectionisthemostpopulargoalofthestudiedAIOpsprojects,fol-
lowedbymonitoring,anomalyprediction,rootcause analysis,andAIOpsinfrastructure
Wefind9categoriesforthegoalsoftheAIOpsprojectswhichareshowninFig.7andare
described in Table 6. Anomaly detection (60%) and monitoring (12%) are the most com-
monreasonsforusingAIOpssolutions.Anomalyprediction,rootcauseanalysis,andAIOps
infrastructure arethenextmaingoalsofoursetofprojects.Wecategorizetheprojectsas
“providing datasets” if they mainly provide public AIOps data that can be used by other
practitionersorresearchers.Wecategorizeprojectsas“AIOpsinfrastructure”iftheyprovide
infrastructuralsupportsuchaslogparsing.
Wefindthatfortaskssuchasanomalydetectionandrootcauseanalysis,developersusually
use logs as their main source. However, for monitoring and anomaly prediction tasks, the
mainsourceofdataisperformancemetrics.Wealsofindthatonly1%ofprojectsdoself-
healingastheirfinalgoal.Itmeans,intheotherprojects,afterachievingthefinalgoal,for
example, anomaly detection, an agent (e.g., developer) should decide what to do with the
foundedanomalies.Thisnotcompletelyautomatedprocedurewillleadtoalossoftimeand
resources.WediscussthispointinmoredetailinSect.4.
123

143   Page 20 of 49 Empirical Software Engineering (2023) 28:143
Table6 Differenttypesofgoals,theirdefinitions,andexamples
| Goal | Definition | Repositoryexample |
| ---- | ---------- | ----------------- |
Anomalydetection Identifyinganomaliesthatdeviate Repository(134266587)useslogdata
|     | fromthenormalbehavior. | andanalyzethemtofindanomalous |
| --- | ---------------------- | ----------------------------- |
ehavior.Itthendisplayanomalies
usingdynamicgraphics.
Monitoring Collectingandobservingthe Repository(221989665)providesdata
|     | real-timestreamofdatato | monitoringandalerting. |
| --- | ----------------------- | ---------------------- |
understandsystemruntime
status.
Anomalyprediction Analyzinghistoricaldatato Repository(169132015)usesmetric
|     | forecastfutureanomalies. | dataofharddrivestopredictthe |
| --- | ------------------------ | ---------------------------- |
failuresinthenearfuture.
Rootcauseanalysis Identifyingtherootcausesof Repository(238914477)analyzesthe
|     | faultsorproblems. | logsofKubernetescontainerstofind |
| --- | ----------------- | -------------------------------- |
therootcausesofissues.
AIOpsinfrastructure Providinginfrastructuresupport Repository(244678163)provides
|     | orutilityfunctionssuchaslog | automatedparsingofrawlogs. |
| --- | --------------------------- | -------------------------- |
parsing.
Providingdatasets Providingdatasetstobeusedin Repository(60705895)collectsvarious
|     | otherAIOpsprojects. | systemlogdatasetsthatcanbeused |
| --- | ------------------- | ------------------------------ |
forloganalysis.
Knowledgerepresentation Extractingandsummarizing Repository(345320486)extracts
|     | knowledgefromdatasetsor | informationfromStackOverflowto    |
| --- | ----------------------- | --------------------------------- |
|     | websites.               | findfastsolutionsforfaultsintheir |
platform.
Automatedclassification Classifyingdifferentinputdata Repository(238914477)classifiesweb
|     | instancebasedontheir | queriestofindsimilarimportant |
| --- | -------------------- | ----------------------------- |
|     | similarities.        | informationandtrends.         |
Selfhealing Conductinghealthchecksand Repository(238914477)aimsto
|     | automaticallyfixingtheissues. | providesoftwaresystemswith |
| --- | ----------------------------- | -------------------------- |
monitoringandself-healing.
TofindaGitHubrepositorywithitsID,onecaneitherclickthehyperlinkorusethelinkhttps://api.github.
com/repositories/{ID}where{ID}isreplacedbyaspecificrepositoryID
TherelationbetweentheinputdataandthegoalsoftheAIOpsprojectsisshowninFig.8.
Asshowninthisfigure,logdataandnetworktrafficdataarethemostuseddatatypesfor
achieving the goal of anomaly detection, while performance metric data is the most used
datatypeforanomalyprediction.Logdataandperformancemetricdataarealsothemost
commondatasourcesforthegoalofrootcauseanalysis.
SummaryofRQ2
LogsarethemostcommonlyusedinputdatainthestudiedAIOpsprojects,followed
byperformancemetricsandnetwork-trafficdata.Classicalmachinelearningtech-
niquesarethemostusedanalysistechniques,followed(farbehind)bydeeplearning,
statisticalanalysis,timeseriesmodels,andlogparsing.Themostpopulargoalsofthe
AIOpsprojectsareanomalydetection,followedbymonitoring,anomalyprediction,
rootcauseanalysis,andAIOpsinfrastructure.
123

Empirical Software Engineering (2023) 28:143 Page 21 of 49 143
Fig.8 The relation between the input data and goals of the AIOps projects. The sizes of the circles are
proportionaltothenumberofprojectsthatuseacertaininputforacertaingoal
3.3 RQ3.WhatistheCodeQualityofAIOpsProjects?
3.3.1 Motivation
aboutthehealthoftheITinfrastructure...etc..EnsuringthequalityofAIOpsprojectsisvital
forthesoftwareoperationtaskstheyaredesignedfor.Otherwise,theinsightsderivedfrom
theiranalysiswouldnotbereliable.Thus,inthisRQ,weaimtounderstandthecodequality
of the AIOps projects. We analyze different metrics in order to come to a comprehensive
conclusion.WealsocomparethecodequalityofAIOpsprojectswithourbaselinestofind
similarpatternsordifferences.Ourresultscanprovideinsightsforfutureworktoimprove
thequalityofAIOpsprojects.
3.3.2 Approach
We use SonarQube,4 a static code analysis tool that supports a large number of program-
minglanguages,includingPython,Java,JavaScript,andGo,tostaticallymeasurethequality
oftheAIOpsprojectsandthebaselines,asAIOpsprojectsaredevelopedbydifferentlan-
guages(RQ1).ManyrecentstudieshaveutilizedorevaluatedSonarQubeforcodequality
measurement(Busingeetal.2019;Lomioetal.2021;Saarimakietal.2019).
Codequalitymetrics To understand the code quality of AIOps projects, we measure the
metricsofeachstudiedprojectalongfourdimensions:size,reliability,maintainability,and
security.Thedetailedlistofthemeasuredmetricsinclude:LinesofCode(LOC),comment
4 https://www.sonarqube.org/
123

snoitinfiedriehtdnascirtemytilauqedocehT
7elbaT
noitinfieD
cirteM
.tcejorpafoezisehtstneserpertahtscirtemehT
eziS
ecapsetihwatonsihcihwretcarahcenotsaeltaniatnoctahtsenilforebmuN
)COL(edoCfoseniL
tnemmocafotrapro,noitalubata
tnemmocytpme(stnemmoctnacfiingis-noN.stnemmocgniniatnocsenilforebmuN
seniltnemmoC
deredisnoctonera).cte,sretcarahclaicepsgnivahylnoseniltnemmoc,senil detaluclacsitI.edocfosenilotderapmocstnemmocfosenilfotnuomaehT
stnemmocfoytisneD
alumrofgniwollofehtnodesab
001*)seniltnemmoC+edocfoseniL(/seniltnemmoC=stnemmocfoytisneD
sawrepolevedehtsayltnereffidevahebedocehtekamtahtseussiehT
ytilibaileR
.dednetni
stneserpertahteussinasadenfiedsigubA.tcejorpanisgubforebmunlatoT
sgubforebmuN
edocehtnignorwgnihtemos
.dluohstinahtetadpuottlucfifideromedocehtekamtahtseussiehT
ytilibaniatniaM
ngisedfonoitaloivasillemsedocA.tcejorpanisllemsedocforebmunlatoT
sllemsedocforebmuN
)5102(dahsrAdnaloosaR.ytilauqerawtfostcapmiylevitagenyamtahtsnrettap nettirweraseulavehtfI.sllemsedocehtllaxfiotderiuqeremitdetamitseehT
emittbedlacinhceT
demussasiyadruoh-8na,syadni
esehT.ytirucesfosmretnisessenkaewlaitnetopekamtahtseussiehT
ytiruceS
.srekcahybdetfienebebthgimseussi
tahtedocfoeceipasiytirabenluvA.tcejorpaniseitilibarenluvforebmunlatoT
seitilibarenluvforebmuN
rekcahaybtiolpxeebdluoc
foseceipehtsitopstohytirucesA.tcejorpanistopstohytirucesforebmunlatoT
stopstohytirucesforebmuN
evitisnes-ytiruceseratahtedoc snoitatnemucodebuQranoSnodnuofebdluocnoitinfieddeliatederomA.ebuQranoSmorfdetcartxeerasnoitinfiedehtllA
143 Page 22 of 49 Empirical Software Engineering (2023) 28:143
123

Empirical Software Engineering (2023) 28:143 Page 23 of 49 143
lines,densityofcomments,numberofbugs,numberofcodesmells,numberofvulnerabilities,
numberofsecurityhotspots,andtechnicaldebttime.Allthesequalitymetricsareextracted
usingSonarQube.WedefinethesemetricsinTable7.
SonarQubealsoassignsaseverityleveltoeachoftheissues.Itcategorizestheseverities
intofourgroups;Minor,Major,Critical,andBlocker,fromthelowesttothehighestseverity.5
Findingthemostviolatedrulesandrulecategories Toprovideinsightsintotheprimary
codequalityissuesamongtheAIOpsprojects,wecounteachissue’sassignedrulesandrule
categories (i.e., tags) and report the most repeated ones. SonarQube evaluates the source
code against its set of rules to detect specific issues. Also, rule categories are a way to
categorize trivial rules into higher-level concepts. SonarQube rules include code smells,
bugs,vulnerabilities,andsecurityhotspots.Eachruleisrelatedtoaspecificdefinedissue,
anddifferentrulescanbepartofonerulecategory.
Tofindthemostviolatedissues(i.e.,rulesandrulecategories),itisessentialtoconsider
twoaspects:theoccurrenceofanissueineachprojectandthepercentageofprojectsthat
havethatissue.Hence,wecalculatetheweightofviolatedissues(“W”inTables9and10)
tofindthemostviolatedissues.Eachprojectcanhavemultipleviolatedissues.Wecalculate
theweightofissueiinprojectjusingthefollowingformula,
n
w = ij
ij
n
pj
where n is the frequency of issue i in project j and n is the total number of issues in
ij pj
projectj.Then,tocalculatetheweightofissueiinalltheprojects,wecalculateitsaverage
inalltheprojects. (cid:2)
n w
w = j=1 ij
i
n
PreparingprojectdataandrunningSonarQube Weexecutethefollowingthreestepsto
analyzethequalityofeachoftheAIOpsandbaselineprojects.preprocessingneededforthem,
needtomentionit);3)ExecuteSonarQube(maybrieflyexplainsomesetup/configuration).
Step1.ClonetheprojectsfromGitHub.WeclonetheGitHubrepositoriesonthelocal
machinesothatwecananalyzetheirsourcecode.
Step2.Preprocesstheprojectdata.Fortwoofthepopularlanguagesamongourprojects
(i.e.,PythonandJava),wehavetoperformapreprocessingphasebeforeperformingthesource
codeanalysisusingSonarQube.Wedonotneedtoperformthisphaseforotherlanguages.
Pythoncode.SonarQubedoesnotsupportthe.ipynbformatwhichisthefileformatof
Jupyter notebooks. To overcome this limitation, we first convert the .ipynb files in each
projecttothe.pyformatusingthenbconvertlibrary(Jupyter2022)inPython.Wethenuse
SonarQubetoanalyzetheresulting.pyfiles.
Javacode.ToanalyzetheJavacode,SonarQuberequiresthecompiledfiles(.classfiles).
However,inmostcases,developersdonotuploadthe.classfilesintheirGitHubrepositories
andonlyputthe.javafiles.Toaddressthisissue,wecompilethe.javafilesinto.classfiles.
Weprimarilyleveragethebuildautomationtool(i.e.,Gradle,ApacheMaven,andApache
ANT)oftheprojecttocompiletheprojectfiles.Forexample,forMavenprojects,weuse
mvncompile.Ifwecouldnotfindabuildautomationtool,weusejavactocompilethe.java
files.
5 https://docs.sonarqube.org/latest/user-guide/rules/
123

143 Page 24 of 49 Empirical Software Engineering (2023) 28:143
Fig.9 BoxplotsofcodequalitymetricsforAIOpsandbaselineprojects
123

Empirical Software Engineering (2023) 28:143 Page 25 of 49    143
Step3.ExecuteSonarQube.Wewriteascriptthatsendsthesourcecodeofeachproject
toaSonarQubewebserverthatisinstalledlocally.AfterSonarQubefinishestheanalysis,
weextracttheresults.
Weareabletoanalyzethesourcecodeof770outofthe887projects(87%)inallthree
groupsofprojects(AIOpsprojectsandthetwobaselines).Thesuccessratiois93%,92%,
and79%forAIOps,ML,andGeneralprojects,respectively.Themainreasonsoffailures
includeremovedGitHubrepositoriesandfailuresincompilingtheJavaprojects.Analyzing
thesourcecodeofprojectsatthisscaleisrarelyreportedintheliterature,andperforming
theSonarQubeanalysisexperimentstookseveralweeks.
Statisticaltests SimilartothefirstRQ,weperformstatisticalteststovalidateourresults
andensuretheirstatisticalsignificance.WeuseMann–WhitneyU
test(MannandWhitney
1947)tocomparethedistributionofthemetricsbetweenAIOpsandbaselineprojects.We
alsouseCliff’sdeltatest(Cliff1993)tomeasuretheeffectsizeofthedifferencebetween
thedistributions.Weusethesameapproachandscale(i.e.,effectof|d|=0.147issmall,|d|
=0.33ismedium,and|d|=0.474islarge)asdescribedinSect.3.1.2.
3.3.3 Results
AIOpsprojectshavepoorerqualitythantheMLandGeneralbaselines Fig.9represents
the box plots of code quality metrics extracted from SonarQube for AIOps and baseline
projects.Table8illustratesthep-valueandeffectsizeofthecodequalitymetricsofAIOps
projectscomparingtothebaselines.Forbugs,codesmells,vulnerabilities,securityhotspots,
andtechnicaldebt,wefurtherreportthevaluesnormalizedbytheLOCofeachproject.We
reportthesenormalizedvaluesinFig.10toensurethatourfindingsarerobustandnotbiased
bythesizeoftheprojects.
According to the p-values of Mann–Whitney U test shown in Table 8, the difference
betweenmostofthecodequalitymetricsofAIOpsprojectscomparedtobaselinesissig-
nificant.Consideringthenumberofbugsandcodesmells,AIOpsprojectsarestatistically
differentfromthebaselines,andtheeffectsizeoftheirdifferencesissmallornegligible.As
showninFig.9a,AIOpsprojectshaveahighernumberofbugsintermsofbothmeanand
median,withamedianof3bugs,whilethemedianis1inbothbaselines.Thispatternisalso
| Table8 Detailedresultsof | Metric | AIOpsvs.ML | AIOpsvs.General |
| ------------------------ | ------ | ---------- | --------------- |
Mann–WhitneyUandCliff’s
|     |     | p-value effectsize | p-value effectsize |
| --- | --- | ------------------ | ------------------ |
deltatestsonprojects’code
quality
|     | Bugs             | 0.01 ** | 0.03 *   |
| --- | ---------------- | ------- | -------- |
|     | Codesmells       | 0.00 ** | 0.00 **  |
|     | Vulnerabilities  | 0.00 *  | 1.00 -   |
|     | Securityhotspots | 0.03 *  | 0.18 -   |
|     | Technicaldebt    | 0.00 ** | x0.00 ** |
|     | LOC              | 0.01 ** | 0.02 *   |
|     | Commentlines     | 0.01 ** | 0.00 *** |
|     | Commentdensity   | 0.42 -  | 0.00 *** |
Mann–WhitneyUresultsareshowninp-valuecolumns.Ifthesetshave
statisticallydifferentdistributions,theCliff’sdeltaresultsareshownin
effectsizecolumns.
*:negligibleeffect**:smalleffect***:mediumeffect
123

143 Page 26 of 49 Empirical Software Engineering (2023) 28:143
seeninthenormalizedversioninFig.10a.ThenumberofcodesmellsisalsohigherinAIOps
projectsbasedonbothoriginalandnormalizedversionspresentedinFigs.9band10b.The
mediannumberofcodesmellsinAIOpsprojectsis51.0,twicetheMLbaselineswith26.5
andmorethan3.5timestheGeneralbaselinewith14.0.
Fig.10 BoxplotsofcodequalitymetricsforAIOpsandbaselineprojects.ThevaluesarenormalizedbyLOC
ofeachproject
123

Empirical Software Engineering (2023) 28:143 Page 27 of 49 143
Regarding the number of vulnerabilities and security hotspots among the projects, no
statisticallysignificantdifferenceisseenbetweenAIOpsandGeneralprojects,accordingto
Table8.However,AIOpsandMLbaselinearestatisticallydifferent,withaneffectsizeof
negligible.AsFigs.9cand10cshow,mostoftheAIOpsandbaselineprojectsdonothave
anyvulnerabilities.However,asFig.9drepresents,themediannumberofsecurityhotspots
in AIOps is 1 while it is 0 in ML baseline; and the mean number of security hotspots in
AIOpsis22.4whileitisonly5.1inMLbaseline.
Technicaldebtisthenextanalyzedsecuritymetric.Table8suggeststhatthereisastatisti-
callysignificantdifferencebetweenAIOpsandbaselineswithasmalleffectsize.AsFig.9e
shows,boththemeanandmedianofAIOpstechnicaldebtarehigherthanthebaselines.The
meanvalueoftechnicaldebtfortheAIOpssetis80.5h,whileitis26.8and57.3hforML
andGeneralbaselines,respectively.ThemedianvalueoftechnicaldebtinAIOps(5.4h)is2
timestheMLbaseline(2.9h)and3timestheGeneralbaseline(1.7h).AsFig.10esuggests,
technicaldebtinAIOpsprojectsishigherthanthebaselines,eveninthenormalizedversion.
ThesefindingsareinlinewiththehighvolumeofissuesobservedinAIOpsrepositories,as
showninFig.3.
AIOpsprojectshavemorelinesofcodethanbaselinesandthesameamountofcom-
mentsastheMLbaseline Table8showsthatAIOpssetisstatisticallydifferentfromthe
baselines in terms of number of lines of code and number of comment lines. According
toFig.9f,themeanvalueofLOCforAIOpsprojectsis21.2k,3timestheMLbaseline(with
7.0k) and 2 times the General baseline (10.7k). The median value also indicates a similar
pattern,with1.4kforAIOpsprojectsand0.8kforthebaselines.Theamountofcomments
writteninAIOpsprojectsisalsohigherthanthebaselines,withamedianof0.3kcompared
to0.2kand0.1kfortheMLandGeneralbaselines.Figure9hshowsthecommentdensity
betweenthethreesets.ThedensityofcommentsinAIOpsandMLprojectsaresimilar,with
themediansof19.0%and20.9%,respectively.ThecommentdensityfortheGeneralbaseline
islessthanhalfoftheAIOpsset,withonly8.4%.
AIOpsprojectssufferfromcodesmellsmorethanothertypesofissues Fig.11illustrates
thedistributionofbugs,codesmells,vulnerabilities,andsecurityhotspotsamongtheprojects.
Thepercentageofvulnerabilitiesismuchsmallerthanothertypesofissuesinalltheprojects.
In AIOps projects, the main issue is related to code smells, which account for 85% of all
issues,13%morethantheMLbaseline.Aftercodesmells,themostcommontypeofissue
isbugs,with10%,andthensecurityhotspots,with5%.
AIOpsandMLprojectshavesimilartypesofissuesintermsofviolatedSonarQuberules
andrulecategories WereportthemostviolatedrulesandrulecategoriesinTables9and10.
WealsodefinetheseviolatedrulesandrulecategoriesinAIOpsfield(basedonSonarQube
website67)inTables11and12.
As shown in the tables, AIOps and ML projects have similar rule and rule category
violations.Intermsofviolatedrules,9outofthetop-10violatedrulesarecommonbetween
AIOps and ML projects. Furthermore, the first two most violated rules (i.e., python:S117
andpython:S125)arethesameinAIOpsandMLprojects,withsimilarweights(17.6%and
14.6%forAIOps,and16.8%and15.5%forMLprojects).Also,intermsofmostviolated
6 https://rules.sonarsource.com/
7 https://docs.sonarqube.org/latest/user-guide/built-in-rule-tags/
123

143 Page 28 of 49 Empirical Software Engineering (2023) 28:143
Fig.11 ThedistributionofthequalityissuesamongtheAIOpsandbaselineprojects
rulecategories,9outofthetop-10violatedrulecategoriesarecommonbetweenAIOpsand
MLprojects.
ComparingissuesbetweentheAIOpsprojectsandtheGeneralbaseline,4ofthetop-10
violatedrulesand7ofthetop-10violatedruletagsarecommon.However,theweightand
percentageofprojectshavingtheseissuesinAIOpsprojectsaremuchhigher.Asanexample,
Python:S117 is the most violated rule in both AIOps and General projects. However, the
weightandpercentageofprojectshavingthisviolatedruleinAIOpsare17.6%and59.1%
butintheGeneralbaselineare5.2%and19.7%,respectively.
WeprovidethecompletelistofviolatedrulesandrulecategoriesinAIOpsprojectsand
otherbaselinesinourreplicationpackage.
Naming convention, commented-out code, duplicated string literals, high complex-
ityoffunctions,andwildcardimportsareamongthetopviolatedrulesinAIOpsprojects
RegardingthemostviolatedrulesinAIOps,thefirstthreearepython:S117,python:S125,
and python:S1192. The first one has a minor severity and is about the non compliance of
naming convention. Shared naming conventions are vital and allow teams to collaborate
effectively. The second one has a major severity and is about commenting out the unused
sectionsofcodewhichreducesreadability.Instead,unusedcodeshouldbedeleted.Thethird
onehasacriticalseverityandisaboutusingduplicatedstringliterals.Itmakestheprocess
ofrefactoringerror-pronebecausetheprogrammermustbesuretoupdatealloccurrencesof
thestring.
In addition to these violated rules, three more rules with critical severity exist in the
top 10 violated rules of AIOps projects; python:S3776, python:S2208, and python:S5754.
Python:S3776 isaboutthecognitivecomplexityofcode.Itmeasureshowhardthecontrol
flowofafunctionistounderstand.Functionswithhighcognitivecomplexitywillbedifficult
to maintain. Python:S2208 is about using wildcard imports (i.e., from module import *).
Importingallpublicnamesfromamodulehasmultipledisadvantages.Itcanleadtoconflicts
between local names and imported ones, or same names between two different packages.
Italsoreducescodereadabilityandmaycauseconfusionaboutwhichclassesareimported
123

Empirical Software Engineering (2023) 28:143 Page 29 of 49    143
ehtsi”N“dna,selurfothgiewehtstneserper”W“,seussifoytirevesehtsetacidni”veS“.senilesabehtdnastcejorpspOIArofselurebuQranoSdetaloiv01-potehT )%(N
| 7.91 | 3.02 3.91 7.02 0.91 7.61 0.81 | 4.21 |
| ---- | ----------------------------- | ---- |
2.5 5.7
)%(W
| 2.5                                                                                                                  | 9.3 4.3 0.3 6.2 3.2 9.1          | 8.1 7.1 7.1      |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------- | ---------------- |
| veS nM                                                                                                               | nM                               |                  |
|                                                                                                                      | jM jM jM rC jM                   | jM jM lB         |
| rekcolBrofsdnats”lB“dna,lacitirCrofsdnats”rC“,rojaMrofsdnats”jM“,roniMrofsdnats”nM“.elurtahthtiwstcejorpfoegatnecrep | 7111S:tpircsavaj 521S:tpircsavaj | 3072S:tpircsavaj |
|                                                                                                                      | 2911S:nohtyp 1841S:nohtyp        |                  |
711S:nohtyp 521S:nohtyp
|     | 4525S:beW | 7281S:beW |
| --- | --------- | --------- |
521S:lmx
lareneG
eluR
)%(N
| 3.95 | 8.36 7.72 4.55 5.25 0.14 5.34 | 4.32 4.52 |
| ---- | ----------------------------- | --------- |
8.8
)%(W
8.61 5.51
|     | 7.7 3.7 9.5 0.4 2.3 | 8.2 4.2 1.2 |
| --- | ------------------- | ----------- |
veS
| nM  | jM jM rC nM jM rC                                   | jM rC rC                               |
| --- | --------------------------------------------------- | -------------------------------------- |
|     | 2911S:nohtyp 1841S:nohtyp 2451S:nohtyp 6773S:nohtyp | 0232S:nohtyp 8022S:nohtyp 4575S:nohtyp |
711S:nohtyp 521S:nohtyp 509S:nohtyp
LM eluR
| )%(N 1.95 | 3.66 3.76 5.52 6.35 1.84 5.44 | 4.52 4.53 9.02 |
| --------- | ----------------------------- | -------------- |
)%(W
6.71 6.41
|             | 8.7 0.7 2.4 3.3 2.3                                 | 3.2 2.2 1.2               |
| ----------- | --------------------------------------------------- | ------------------------- |
| veS nM      | jM jM nM jM                                         | nM                        |
|             | rC rC                                               | rC rC                     |
|             | 2911S:nohtyp 1841S:nohtyp 6773S:nohtyp 2451S:nohtyp | 8022S:nohtyp 4575S:nohtyp |
| 711S:nohtyp | 521S:nohtyp 509S:nohtyp                             | 001S:nohtyp               |
9elbaT
spOIA
eluR
123

stcejorpfoegatnecrepehtsi”N“dna,sgatfothgiewehtstneserper”W“.senilesabehtdnastcejorpspOIArof)seirogetacelur(sgatebuQranoSdetaloiv01-potehT
01elbaT
gattahthtiw
lareneG
LM
spOIA
)%(N
)%(W
gaT
)%(N
)%(W
gaT
)%(N
)%(W
gaT
3.26
1.51
desunu
6.38
7.62
desunu
4.67
7.52
noitnevnoc
0.04
8.01
noitnevnoc
8.76
9.12
noitnevnoc
6.39
2.42
desunu
5.25
5.7
suoicipsus
0.65
7.6
ewc
1.97
1.9
ngised
9.74
5.7
llaftip
6.75
5.6
ngised
4.66
3.8
ewc
5.05
1.6
ewc
0.84
4.4
suoicipsus
4.66
6.5
suoicipsus
4.83
1.5
ngised
8.93
4.3
llaftip
9.06
2.4
daolrevo-niarb
2.92
5.4
ytilibissecca
2.94
3.3
daolrevo-niarb
7.24
3.3
llaftip
6.34
6.3
daolrevo-niarb
6.31
0.2
etelosbo
1.94
1.2
gnildnah-rorre
5.72
5.3
a-2gacw
9.73
0.2
ecitcarp-dab
8.15
0.2
ecitcarp-dab
0.83
1.3
gnisufnoc
6.33
0.2
gnildnah-rorre
4.63
6.1
ysmulc
143 Page 30 of 49 Empirical Software Engineering (2023) 28:143
123

Empirical Software Engineering (2023) 28:143 Page 31 of 49 143
Table11 ThemostviolatedSonarQuberulesandtheirdefinitionsinAIOpsprojects
Rules
Name Definition
python:S117 Localvariableandfunctionparameternamesshould
complywithanamingconvention
python:S125 Sectionsofcodeshouldnotbecommentedout
python:S1192 Stringliteralsshouldnotbeduplicated
python:S905 Non-emptystatementsshouldchangecontrolfloworhave
atleastoneside-effect
python:S1481 Unusedlocalvariablesshouldberemoved
python:S3776 CognitiveComplexityoffunctionsshouldnotbetoohigh
python:S1542 Functionnamesshouldcomplywithanamingconvention
python:S2208 Wildcardimportsshouldnotbeused
python:S5754 SystemExitexceptionshouldbere-raisedimmediately
python:S100 Methodnamesshouldcomplywithanamingconvention
and used. python:S5754 is about handling exceptions. This rule indicates that SystemExit
exceptionshouldbere-raisedimmediately.
Namingconvention,unusedorcommented-outcode,andpoordesignareamongthe
topviolatedrulecategories RegardingthemostviolatedrulecategoriesinAIOpsrepos-
itories, convention, unused, anddesign are the worst issues. Convention category is about
Table12 ThemostviolatedSonarQubetags(rulecategories)andtheirdefinitionsinAIOpsprojects
Tags
Name Definition
convention Codingconvention-typicallyformatting,naming,whitespace
unused Unusedcode;e.g.,aprivatevariablethatisneverused
design Thereissomethingquestionableaboutthedesignofthecode
cwe RelatestoaruleintheCommonWeaknessEnumeration
Formoreinformation,visithttps://cwe.mitre.org/
suspicious It’snotguaranteedthatthisisabug,butitlookssuspiciously
likeone.Attheveryleast,thecodeshouldbere-examined
andlikelyrefactoredforclarity
brain-overload Thereistoomuchtokeepinyourheadatonetime
pitfall Nothingiswrongyet,butsomethingcouldgowronginthe
future;atraphasbeensetforthenextperson,andthey’ll
probablyfallintoitandscrewupthecode
error-handling IssuesrelatedtohandlingtheerrorssuchasExceptionmethods
bad-practice Thecodelikelyworksasdesigned,butthewayitwasdesigned
iswidelyrecognizedasbeingabadidea
clumsy Extrastepsareusedtoaccomplishsomethingthatcouldbe
donemoreclearlyandconcisely
123

143 Page 32 of 49 Empirical Software Engineering (2023) 28:143
fulfillingcodingconventions,includingnamingfunctionsandvariables,complyingwhite-
spaces and indentations. The second most violated rule category is unused. This category
isaboutunusedcodethatdecreasestheperformanceofthesystem.Someexamplesofthis
category are unused assignments, unused private classes, and empty test cases. The third
mostignoredrulecategory,design,isaboutthebaddesignofthesoftware.Someexamples
ofthisgroupareunstabletests,duplicatedstringliterals,andusingrandomizeddataintest
cases.
Having rule category issues such as naming conventions, unused code, and bad design
indicatethatdeveloperstendtowriteAIOpscodeinanadhocmanner,whichhinderstheir
project’s reusability and maintainability. Also, looking at the most violated rules and rule
categories, we realize paying more attention to details can increase the quality of AIOps
solutions.Forexample,3outofthetop-10violatedrulesarerelatedtonamingconventions.
Onlyfollowingthenamingconventionscanreducethenumberofissuesheavily.Furthermore,
sincemostoftherules(9oftop-10)andrulecategories(9oftop-10)arecommoninAIOpsand
MLprojects,AIOpsprojectscanbenefitfromthequalityassessmentandqualityassurance
toolsandtechniquesthathavebeendevelopedforMLsystems.Theabovepointsarediscussed
inmoredetailinSect.4.
SummaryofRQ3
AlthoughAIOpsprojectshaveanadequateamountofcommentscomparedtotheML
andGeneralbaselines,AIOpsprojectsexhibitpoorerqualitythanthetwobaselines
intermsofavarietyofqualitymetrics(e.g.,bugs,codesmells,andtechnicaldebt).
Inparticular,codesmellsarethedominanttypeofissueinAIOpsprojects.Wealso
identify the most common issues in AIOps projects: naming convention, unused
code,andbaddesignarethetop-3violatedrulecategories.Moreover,weobserve
thesimilarityofviolatedrulesbetweenAIOpsandMLprojects.Futureeffortsare
neededtoreducetheissuesidentifiedinthisworkandimprovethequalityofAIOps
projects,e.g.,bydesigningtoolsforfixingbugs/smellsorderivingcodingguidelines.
WealsoencouragefutureAIOpsprojectstoreducethead-hocnessoftheircodeto
improvereusabilityandmaintainability.
4 Discussion
Basedonthefindingsofourstudy,inthissection,wediscussthestateofAIOpsinopen-
source projects. We then discuss the current challenges of developing AIOps applications
and foresee possible future directions for AIOps researchers and practitioners. Finally, to
assesstherobustnessofourfindings,weaddastricterfilteringcriterionandreportthemain
resultsconsideringonlymorematureprojects.Wecomparetheresultsobtainedfromthese
projectswithourmainfindingstomakesureourfindingsarerobustenough.
4.1 AIOps:WhereisitNow?
The number of AIOps applications is growing fast, and they are receiving a lot of
attentionfromtheopen-sourcecommunity.RegardingtheresultsofSect.3.1.3,wefind
that the speed of growth for AIOps applications is faster than that for general-purposed
123

Empirical Software Engineering (2023) 28:143 Page 33 of 49 143
projects on GitHub. We further find that AIOps applications are receiving more attention
regardingGitHubmetricscomparedtomachinelearningandgeneral-purposedapplications.
ThisattentiontowardstheAIOpsareaencouragesresearchersandpractitionerstodevelop
newtechnicalinnovationsinvariousareasofAIOps.Wediscusssomeofthepotentialfuture
directionsbelow.
Monitoring data-especially logs, performance metrics, and network-traffic data-
are the most common data types of AIOps applications Regarding the results of
Sect.3.2.3,wefindthatalmost70%oftheprojectsuselogs,performancemetrics,ornetwork-
trafficdata.Theusageofothertypesofinputdata(e.g.,alarms)islimitedinopen-source
AIOpsapplications.ThisfindingisinlinewithNotaroetal.(2021b)thatmanyAIOps-related
papersalsouseeventlogsandperformancemetricsastheirdatasources.Futureeffortsmay
be invested to investigate how to optimally process these common data types in various
downstream tasks. For example, time-series data representation techniques (Wilson 2017)
and time-series segmentation techniques (Lovric´ et al.2014) may be explored to improve
datarepresentationsofsuchtime-seriesdata.
ClassicalmachinelearningisthemostcommontechniqueinAIOpsapplications Wefind
thatoverhalf(54%)oftheAIOpsapplicationsuseclassicalmachinelearningastheirprimary
technique,whileonly14%usedeeplearningtechniques.AIOpspractitionersalsodevelop
AIOpsapplicationsusingavarietyofmethods,includingtime-seriesandstatisticalmodels.
However,sometechniques(e.g.,naturallanguageprocessing)arenotusedfrequently.We
suggestthatfutureAIOpssolutionsmayfurtherutilizemoresophisticatedtechniquesofdeep
learningandnaturallanguageprocessing.However,assuggestedbyLietal.(2020b);Lyu
etal.(2021),AIOpsmodelsshouldbetrustable andinterpretable; hence,usingblack-box
modelswithouttheabilitytointerpretisnotrecommended.Therefore,wealsosuggestthat
futureAIOpssolutionsshouldalwaysexperimentwithclassicalsolutionsinsteadofsimply
assumingdeeplearningtechniquesaretheoptimalsolution.
AnomalydetectionisthemostcommongoalofAIOpsapplications 60%ofopen-source
AIOpsapplications’primarygoalistodetectanomalies.Monitoring,anomalyprediction,
rootcauseanalysis,andprovidingAIOpsinfrastructurearetheothercommongoalsofAIOps
applications.Only5%ofprojectsprovideapublicAIOpsdataset,andonly1%ofprojects
provide self-healing features. Our results align with the findings of Notaro et al. (2021b),
where they observe that 62% of AIOps papers are associated with failure management,
includingfailuredetection,failureprediction,androotcauseanalysis.
AIOps applications suffer from more code quality issues than machine learn-
ing and general-purpose-based projects Considering our results in Sect.3.3.3, AIOps
applicationshaveahighernumberofqualityissues(e.g.,bugsandcodesmells)compared
tothebaselines.WelistthemostcommonviolatedissuesinAIOpsapplicationsinTables9
and10.AIOpspractitionersmaypayattentiontotheseissuesintheirapplicationsandaddress
themtoreducetheriskoffutureproblems.
4.2 AIOps:ChallengesandFutureDirections.
MorebenchmarkingdatasetscouldbedesignedforAIOpsapplications.Wefindthatonly
5%oftheprojectsaimtodesignandpublishAIOpsbenchmarkdatasets.Asalsomentioned
123

143 Page 34 of 49 Empirical Software Engineering (2023) 28:143
byBogatinovskietal.(2021),thereisalackofgoodandpublicAIOpsbenchmarks,where
different AIOps approaches could be compared. As most of the AIOps applications use
logs, performance metrics, and network-traffic data as their input data source, we suggest
AIOpsresearchersdesignandpublishreal-worldandpublicdatasetsofthesedatatypesso
otherAIOpspractitionersandresearcherscouldleveragethemintheirapplications.Inthe
future,wealsoplantodesignabenchmarkingframeworkthatcanhelpfutureworkgenerate
customizeddatasets.
NaturalLanguageProcessing(NLP)techniquescanreceivemoreattentioninAIOpsin
thecomingyears OurresultsinSect.3.2indicatethatonly2%ofthestudiedprojectsuse
NLPtechniques.Ontheotherhand,approximatelyone-thirdoftheprojectsuselogsastheir
inputdata.Priorresearchhasshownthatlogscanbeapproximatelyrepresentedasnatural
languagetextsincethelogsaregeneratedbyloggingstatementsinthesourcecodewrittenby
humans(Hindleetal.2016).Otherworksalsoillustratethatlogsareevenmorepredictable
andrepetitivethannaturallanguages,suchasEnglish(Heetal.2018a;Tuetal.2014;Yao
etal.2020).Hence,wesuggestthatAIOpsprojectscanbenefitfromleveragingtheadvances
inNLPtechniquestoanalyzeandmodeltheinputdatasuchaslogs.
More attention should be paid to increasing automation and reducing human inter-
ventionsinAIOpssolutions Regardingthegoalofthestudiedprojects,mostprojectsaim
todetectandpredictanomalies,monitor,andanalyzetherootcausesoffailures.Allthese
systemsneedhumaninterventionswhenthegoalisreached.Forexample,whenananomaly
is detected, an operator should decide the next required action to handle the situation. As
demonstratedinFig.7,only1%ofprojectsaimforself-healing,meaningthatthesystem
canmakenecessarychangeswhenneededwithouthumaninterventions.WebelieveAIOps
solutionsshouldmovetowardbecomingmoreautomated,detecting/predictingtheincidents
andresolvingthemautonomously.Self-healingtechniquesmaygetmoreattentionandbe
integratedwithdetection/predictiontechniques(Dingetal.2012, 2014;Louetal.2017).
PayingmoreattentiontosimpledetailscanincreasethequalityofAIOpssolutions We
identifythemostcommonissuesinAIOpsprojectsinSect.3.3.3.Whenlookingatthemost
violatedrules,someofthemarechallengingandtime-consumingtofixandneedstructural
changesincode,suchaspython:S3776(cognitivecomplexityoffunctions)andpython:S1192
(duplicationofstringliterals).Ontheotherhand,someareeasytohandle.3ofthe10most
violated rules are related to naming conventions. Only following the naming conventions
can reduce the number of issues heavily. Furthermore, rules such as python:S2208 (using
wildcardimports)andpython:S1481(removingunusedvariables)arequicktodetermineand
easytofix.Identifyingthemostcommonissueshelppractitionersandresearchersinthefield
tobecomeawareofthemandtakemeasurementstoreducethem.
Mostofthetoolsandtechniquesusedforthequalityassuranceofmachinelearningsys-
temscanalsobeusedforAIOpssolutions Ourresultsindicatethatahighproportionof
issuesinMLandAIOpstechniquesarethesame(90%ofmostviolatedrulesand90%of
mostviolatedrulecategoriesareshared).Besides,thequalityassuranceofMLsystemshas
received special attention in the previous years, and different approaches have been built
to preserve the quality of ML-based systems (Braiek and Khomh 2022; Nakajima 2018;
Nikanjametal.2021;Pothetal.2020;Tambonetal.2023).Hence,webelievemostofthe
123

Empirical Software Engineering (2023) 28:143 Page 35 of 49    143
Fig.12 ThecumulativedistributionofthecreationtimeofAIOpsandbaselineprojectswiththenewfiltering
criterion
developedtoolsandtechniquesforqualityassuranceinMLsystemscanbeutilizedinAIOps
techniques.Applyingthesetoolsandtechniquesmayreducethequalityissuesmentionedin
Sect.3.3.3.
Open-source AIOps solutions can benefit from broader use-cases and scenarios As
describedinpreviousworks(Dangetal.2019;PrasadandRich2018),AIOpscanencompass
a wide range of scenarios, from predicting the future status of systems to improving the
productivityofengineers.However,thescopeofcurrentAIOpsprojectsavailableonGitHub
appearstobelimited,focusingprimarilyoncertainaspectswithaskeweddistribution.For
example,wefindthatanomalydetectionisthedominantgoalofAIOpsprojectswith60%
ofusecases.Toaddressthisdisparity,AIOpsresearchersandpractitionersmaypaymore
attentiontootherAIOpsscenarios,suchasminimizingengineers’tedioustasksandbetter
systemautomation.Thiscancontributetoadvancingthisinterdisciplinaryfieldandrealizing
itsfullpotentialacrossdiverseusecasesandapplications.
4.3 TheImpactofUsingaStrongerFilteringCriterion
Toassesstherobustnessofourfindings,weaddanextrafiltertobothAIOpsandbaseline
projectsanddiscussthemainfindingsofRQ1andRQ3.Theintentionistoconfirmthatthe
obtainedresultsaremeaningfulinsightsandarerobust.Todoso,weanalyzethedistribution
of the AIOps projects based on their number of stars. Then, we use the elbow curve to
Table13 Thetop-5languagesofAIOpsandbaselineprojectswiththenewfilteringcriterion
| AIOps      |          | ML         |          | General    |          |
| ---------- | -------- | ---------- | -------- | ---------- | -------- |
| Language   | Usage(%) | Language   | Usage(%) | Language   | Usage(%) |
| Python     | 65.9     | Python     | 81.4     | Python     | 18.6     |
| Java       | 10.6     | C++        | 2.3      | JavaScript | 15.3     |
| Go         | 4.7      | HTML       | 2.3      | Java       | 7.7      |
| HTML       | 3.5      | JavaScript | 1.9      | Typescript | 6.6      |
| JavaScript | 2.4      | MATLAB     | 1.4      | C          | 6.0      |
123

143 Page 36 of 49 Empirical Software Engineering (2023) 28:143
determineathresholdtofiltertheprojects,similartopriorworkwhichusestheelbowcurve
tofiltertheAutoMLtoolstobestudied(Majidietal.2022).Specifically,wecreatealinechart
ofthesortednumberofstarsoftheprojectsandfindtheelbowpoint.Theelbowpointisthe
distinctbendor“elbow”inalinechartthatindicatesachangeinthedistribution(Kodinariya
et al. 2013). We find that the elbow point in the number of stars of AIOps projects is 5.
Hence,weaddextrafilteringandonlyconsiderprojectsthathavethenumberofstarsgreater
orequalto5(stars:>=5).WealsoaddthisfilteringcriteriontotheMLandGeneralbaselines
toensureconsistency.AddingthiscriterionreducesthenumberofAIOpsprojectsfrom119
to85,MLbaselinefrom383to215,andGeneralbaselinefrom385to183.
Results of RQ1 with the new filtering criterion We report the main results of RQ1 in
regard to the new filtering criterion. Figure12 presents the percentage of projects created
inandbeforeeachyearforAIOpsandbaselineprojects.Asillustrated,AIOpsprojectsare
growing faster than ML and General baselines, which is also the same trend in our initial
results(cf.Figure2).
Table13showsthetop-5mostcommonlanguagesintheAIOpsandbaselinesets.The
dominantprogramminglanguageinAIOpsprojectsisPython,withusageof65.9%,followed
byJavawith10.6%.ThemostusedlanguageintheMLprojectsisPythonwith81.4%,and
Fig.13 BoxplotsofGitHubmetricsforAIOpsandbaselineprojectswiththenewfilteringcriterion
123

Empirical Software Engineering (2023) 28:143 Page 37 of 49 143
Table14 Detailedresultsof
Metric AIOpsvs.ML AIOpsvs.General
Mann–WhitneyUandCliff’s
p-value effectsize p-value effectsize
deltatestsonprojects’GitHub
metricswiththenewfiltering Stars 0.02 ** 0.00 ***
criterion
Forks 0.01 ** 0.00 ***
Pullrequests 0.02 ** 0.81 -
Size 0.14 - 0.00 ***
Mann–WhitneyUresultsareshowninp-valuecolumns.Ifthesetshave
statisticallydifferentdistributions,theCliff’sdeltaresultsareshownin
effectsizecolumns.
*:negligibleeffect**:smalleffect***:mediumeffect
themostcommonlanguageinGeneralbaselineisPythonwith18.6%,followedbyJavaScript
with15.3%.Allthesetrendsarealsovisibleinourinitialresults(cf.Table2).
Fig.13depictstheboxplotsofsomeoftheGitHubmetricsfortheAIOpsandbaseline
projects.Table14illustratesthep-valueandeffectsizeofthesamemetricsofAIOpsprojects
comparedtothebaselines.Regardingthenumberofstarsandforks,AIOpsprojectsdemon-
stratehigherpopularitythanthebaselines,asevidencedbyboththemedianandmeanvalues.
ThemedianvalueofstarsinAIOps,ML,andGeneralsetsare33,20,and13,respectively.
Also,themedianvalueofforksinAIOps,ML,andGeneralsetsare14,8,and5,respectively.
Table14showsthatthenumberofstarsandforkshaveasmalleffectsizecomparedto
theMLbaselineandamediumeffectsizecomparedtotheGeneralbaseline.Considering
thenumberofpullrequests,asshowninFig.13c,AIOpsprojectsexperiencemoreofthem,
withamedianvalueof2,comparedto0inMLand1inGeneral.Themeanvalueofpull
requestsinAIOpsprojectsisalsomuchhigherthanthebaselines.Statisticaltestssuggestthat
theeffectsizeofpullrequestsinAIOpscomparedtotheMLbaselineissmall,andthereis
notasignificantdifferencebetweenAIOpsandtheGeneralbaseline.AccordingtoFig.13d,
AIOpsprojectshavealargersizecomparedtothebaselines.Withamediansizeof9.0MB
inAIOpsprojects,theytendtobe9timeslargerthanGeneralbaselineswithamediansize
of1.1MB.StatisticaltestssuggestthatthedifferencebetweenAIOpsandGeneralbaseline
intermsoftheirsizeismedium.However,thereisnosignificantdifferencebetweenAIOps
andMLbaseline.Allthementionedresultsandtrendsareconsistentwithourinitialresults
(cf.Figure3andTable3).Insummary,whenweapplyastricterprojectfilteringcriterion,
ourmainfindingsinRQ1stillhold,indicatingtherobustnessofourfindings.
ResultsofRQ3withthenewfilteringcriterion We also report the main results of RQ3
withthemorematureprojectsthatareselectedwiththestricterfilteringcriterion.Figure14
showstheboxplotsofsomeofthecodequalitymetricsextractedfromSonarQubeforAIOps
andbaselineprojects.PleasecheckTable7forthedefinitionsofthesecodequalitymetrics.
Besides,Table15presentsthep-valueandeffectsizeofthecodequalitymetricsofAIOps
projectscomparedtothebaselines.AsshowninFig.14,AIOpsprojectsexperiencemore
bugsandcodesmellsthanthebaselines.ThemedianamountofbugsinAIOpsis3,whileit
is1inMLand0inGeneralbaselines.Besides,themedianamountofcodesmellsis57in
AIOps,whileitis27inMLand9inGeneralbaselines.Furthermore,theamountoftechnical
debtinAIOpsprojectsismuchhigherthanthebaselines(themedianvalueof6.5hforthe
AIOpsset,2.9hfortheMLset,and1.2hfortheGeneralset).TheLOCinAIOpsprojects
isalsohigherthanthebaselines.
123

143   Page 38 of 49 Empirical Software Engineering (2023) 28:143
Fig.14 BoxplotsofcodequalitymetricsforAIOpsandbaselineprojectswiththenewfilteringcriterion
Whileallthesetrendsarealsovisibleintheinitialresults(cf.Figure9),itseemsthatthe
more mature AIOps projects (i.e., the projects with the new filtering criterion) have more
LOCandthusmoreissuesintermsofbugs,codesmells,andtechnicaldebt.
ConsideringthestatisticaltestspresentedinTable15,wecanobservethatAIOpsprojects
arestatisticallydifferentfrombothbaselinesinthementionedqualitymetrics(i.e.,number
ofbugs,numberofcodesmells,technicaldebt,andlinesofcode).Besides,theeffectsizes
Table15 Detailedresultsof
| Metric | AIOpsvs.ML | AIOpsvs.General |
| ------ | ---------- | --------------- |
Mann–WhitneyUandCliff’s
|     | p-value effectsize | p-value effectsize |
| --- | ------------------ | ------------------ |
deltatestsonprojects’code
qualitywiththenewfiltering
| Bugs | 0.01 ** | 0.01 ** |
| ---- | ------- | ------- |
criterion
| Codesmells    | 0.00 ** | 0.00 *** |
| ------------- | ------- | -------- |
| Technicaldebt | 0.00 ** | 0.00 *** |
| LOC           | 0.02 ** | 0.01 **  |
Mann–WhitneyUresultsareshowninp-valuecolumns.Ifthesetshave
statisticallydifferentdistributions,theCliff’sdeltaresultsareshownin
effectsizecolumns.
*:negligibleeffect**:smalleffect***:mediumeffect
123

,sgatfothgiewehtstneserper”W“.noiretircgniretlfiwenehthtiwsenilesabehtdnastcejorpspOIArof)seirogetacelur(sgatdnaselurebuQranoSdetaloiv5-potehT
61elbaT
gattahthtiwstcejorpfoegatnecrepehtsi”N“dna
lareneG
LM
spOIA
)%(N
)%(W
eluR
)%(N
)%(W
eluR
)%(N
)%(W
eluR
3.51
7.3
711S:nohtyp
7.06
5.71
711S:nohtyp
7.85
1.71
711S:nohtyp
7.42
2.3
4525S:beW
2.46
4.41
521S:nohtyp
7.66
7.21
521S:nohtyp
0.81
9.2
521S:nohtyp
2.06
8.7
2911S:nohtyp
3.56
7.6
2911S:nohtyp
0.81
8.2
7111S:tpircsavaj
7.75
3.6
1841S:nohtyp
7.22
8.4
509S:nohtyp
0.01
7.2
7281S:beW
9.32
5.5
509S:nohtyp
0.06
9.3
1841S:nohtyp
)%(N
)%(W
gaT
)%(N
)%(W
gaT
)%(N
)%(W
gaT
0.85
1.21
desunu
1.58
0.52
desunu
4.67
7.52
noitnevnoc
7.43
9.8
noitnevnoc
2.96
2.22
noitnevnoc
6.39
2.42
desunu
7.44
3.7
llaftip
2.36
1.7
ngised
1.97
1.9
ngised
0.05
0.7
suoicipsus
2.95
8.5
ewc
4.66
3.8
ewc
7.23
8.4
ytilibissecca
7.55
1.5
suoicipsus
4.66
6.5
suoicipsus
Empirical Software Engineering (2023) 28:143 Page 39 of 49 143
123

143 Page 40 of 49 Empirical Software Engineering (2023) 28:143
ofthedifferencesaresmallormedium.ComparedtotheinitialresultspresentedinTable8,
alargereffectsizecanbeseenwhilecomparingAIOpsandGeneralbaseline.
WealsoreportthemostviolatedrulesandrulecategoriesinTable16.Theserulesand
rulecategoriesaredefinedinTables11and12,respectively.Comparingthenewcriterion
(Table16)withtheinitialcriterion(Tables9and10),nochangeisseenfortheAIOpsprojects.
Thetop-5rulesandrulecategoriesremainthesame,withsimilarweight(i.e.,W(%)column
inTable16)andusage(i.e.,N(%)columninTable16).Anotherfinding(aliketotheinitial
results) is the similarity between AIOps and ML projects in terms of their quality issues.
Overall,theresultsofourstricterfilteringcriterionshowthatourinitialfindingsarerobust,
asthetrendsandmainfindingsremainthesame.
5 ThreatstoValidity
Thissectiondiscussesthreatstothevalidityofourresults.
Externalvalidity Inthiswork,weidentifiedandstudiedasetofAIOpsprojectsonGitHub.
TheseprojectsmaynotcoverallAIOpsprojectsonGitHub,thosehostedonotherplatforms,
orprivateprojects.Besides,as“AIOps”isanewterminology,notallAIOpsprojectsmention
thekeywordof“AIOps”intheirrepositories.FutureworkexaminingothersourcesofAIOps
projects (e.g., those published in the literature or closed-source projects) can complement
ourresults.TobroadenthegeneralizabilityofourworkandmaximizethecoverageofAIOps
projects,wefollowaprocessthatcombinesautomatedsearch(tworounds),keywordexpan-
sion,manualverification,andfiltering.Twoauthorsofthepapercarefullyexaminedeachof
thecandidateprojectstoselecttheonesforourstudy.Thethirdauthorstepsintoresolveany
disagreement.Nevertheless,futureworkcanleverageourreplicationpackageandextendour
studybyanalyzingmoreAIOpsprojects.
Toselecttheprojects,weconsiderrepositorieswithstarsandforksgreaterthanorequal
to1.Weselectedthiscriteriatohaveabalancebetweenfilteringthelow-barprojectsand
havingaproperportionofprojectstostudy.Havingstricterfilteringcriteriawouldheavily
reduce the number of AIOps projects, as there are not many AIOps projects available on
GitHub.However,havinglowfilteringcriteriacouldpotentiallyleadtobiasedresultsand
lackofrobustnessinthefindings.Toaddressthisconcernandenhancetherobustnessofour
findings,weconductedasensitivityanalysis(cf.4.3).Inthissensitivityanalysis,wevalidated
our results using a stricter filtering criterion, providing additional evidence to support the
reliabilityofourfindings.Theanalysisshowsthatourresultsremainconsistentandrobust
evenwithstricterfilteringcriteria.
We also collect the ML baseline based on two keywords of “machine learning” and
“deeplearning”.However,havingthesetwokeywordsmaynotincludeallmachinelearning
repositories on GitHub. Future work can expand our results by analyzing more projects
extractedfrommorediversekeywords.
Internal validity We study the code quality metrics of the AIOps projects using a set of
metrics (e.g., code smells). Nevertheless, these metrics may not accurately represent the
qualityoftheprojects.Toreducetheeffectofthisthreat,weleveragedavarietyofmetrics
thatrepresentdifferentaspectsofeachproject.Thesemetricshavealsobeenusedinother
articlestomeasurecodequality(Busingeetal.2019;Lenarduzzietal.2019;Tanetal.2018).
123

Empirical Software Engineering (2023) 28:143 Page 41 of 49 143
WerelyonthecodeissuesdetectedbySonarQubetoanswerourRQ3.WechooseSonar-
Qubesinceitisoneofthemostusedtoolsforanalyzingcodequality(Lenarduzzietal.2017,
2018).WeareawarethatSonarQubemighthavefalsepositivesorfalsenegatives.Inorder
toevaluatetheaccuracyofcodequalitymetricsextractedthroughSonarQube,weconduct
anmanualverification.Weselectthe10mostviolatedSonarQuberulesinAIOpsprojects
presentedinTable11.Foreachoftherules,werandomlyselect20issuesfrom20different
projects(fromalltheAIOpsandbaselineprojects)wherethatruleviolationispresent.There-
fore,foreachofthe10rules,20instancesareanalyzed,andtotallyweanalyze200issues.
Inouranalysis,welookforfalsepositives(i.e.,anyissuethatSonarQubehasdetectedbutis
notactuallyanissue).Wedidnotfindanyfalsepositivesintheanalyzedissues.Ourresults
alignwithSonarQube’sclaimthatithaszerofalse-positivesforcodesmellsandbugs.8
Construct validity To expand our set of AIOps projects, we perform pattern mining and
choose4outof194pairsofkeywords.Wechoosethese4pairsofkeywordsafterasystematic
processandbasedonthediscussionsbetweentheauthors,inordertoreducethebias.Allof
thekeywordsareamongthemostfrequentlyusedkeywords.
To answer RQ2, we use qualitative analysis to categorize the input data, analysis tech-
niques,andgoalsofeachAIOpsproject.Ourresultsmaybebiasedbypersonaldeductions
like any other qualitative study. In order to mitigate this threat, two authors of the paper
performed the qualitative analysis carefully and followed a 5-step process to deduce the
categories. We achieve a Cohen’s kappa value of 0.84 which shows a strong and reliable
agreement.
6 RelatedWork
ThisworkstudiesAIOpsprojectsonGitHubandanalyzesthequalityoftheprojectsusing
SonarQube.Thus,wediscusstherelatedworkonthefollowingthreeaspects.
6.1 AIOpsSolutions
InrecentyearsandwiththeemergenceofAIOps,moreandmorestudieshavebeenconducted
inthisfield.Priorworkshavecomeupwithdifferentsolutionsforvariousproblems.Anomaly
detection(e.g.,Brownetal.2018;Nedelkoskietal.2019b)failureprediction(e.g.,Notaro
et al. 2021a; Zhao et al.2021) ticket management (e.g., Xue et al. 2016; Xue et al. 2018
self-healing(e.g.,Dingetal.2014;Louetal.2013;Louetal.2017)andissuediagnosis(e.g.,
Louet al.2014)are amongthe most studied topicsin AIOps solutions. Wedivide AIOps
papersbytheirgoalsintofivesectionsanddiscusstheminmoredetail.
AnomalyDetection AnomalydetectionisoneofthemostcommontasksinAIOps(Bogati-
novskietal.2021).Previousstudiesperformanomalydetectionusingdifferentapproaches;
forexample,Fuetal.(2009);Sharmaetal.(2013)useclusteringtofindtheanomalies,Liu
et al. (2015); Xu et al. (2009) use tree-based models, and Brown et al. (2018); Du et al.
(2017) use neural networks to perform the task. To perform anomaly detection, different
datasourceshavebeenused.Eventhougheventlogs(Beschastnikhetal.2014;Brownetal.
2018;Duetal.2017;Fuetal.2009)arethemostcommondatasource,othersourcessuchas
performancemetrics(e.g.,Sharmaetal.2013;Suetal.2019 networktraffic(e.g.,Lakhina
8 https://docs.sonarqube.org/latest/user-guide/rules/
123

143 Page 42 of 49 Empirical Software Engineering (2023) 28:143
etal.2004;Lakhinaetal.2005)andtraces(e.g.,Nedelkoskietal.2019a;Nedelkoskietal.
2019b)havealsobeenemployed.
Failure Prediction Predicting failures is also one of the most common tasks of AIOps
(Notaroetal.2021a).Failurepredictioncanbedividedintotwogroupsofhardwarefailures
andsystemfailures.Comparedtoanomalydetectiontaskswherevariousdatasourceshave
beenemployed,infailureprediction,usuallyonlytheperformancemetricsofthesystemsare
used.Performancemetricsaremeasurementsthataidinidentifyingandanalyzingsystem
bottlenecksanddiagnosingissues.Someofthemostpopularperformancemetricsinclude
CPUutilization,memoryutilization,responsetime,throughput,I/O,andnetworklatency.
Zhaoetal.(2021)usedifferentsystemmetrics,suchasCPUusageandthenumberoflive
threadsofthesystem,topredictperformanceanomaliesatrun-time.Linetal.(2018)leverage
temporaldata(e.g.,CPUandmemoryutilizationmetrics,alerts)andspatialdata(e.g.,rack
locations)andconstructMING,adeeplearning-basedapproach.MINGisabletorankthe
faultynodesofthecloudsystem.MINGisappliedtothemaintenanceofoneofthecloud
servicesystemsinMicrosoft.Lietal.(2020b)trytoenhancetheperformanceofMING,e.g.,
by enriching the data representing node failures through a novel oversampling approach.
They also discuss some criteria for the successful adoption of AIOps solutions, including
trust,interpretation,maintenance,scalability,andin-contextevaluation.
Root Cause Analysis Root cause analysis is the approach of identifying the underlying
causesofproblemsorissuesinthesystem.Theprocessinvolvesidentifyingandanalyzingthe
factorsthatcontributedtotheproblem,determiningtherootcause,anddevelopingsolutions
toaddresstheunderlyingissue.Dingetal.(2021)leveragethegeneratedalarmsofasoftware
systemandfindtherootcausesoftheissuesinanonlinemanner.Wangetal(2021)implement
agraph-basedalgorithmandconstructGROOTtoperformrootcauseanalysis.Theirapproach
uses a combination of different event data (i.e., performance metrics, logs, and developer
activities).GROOTisdeployedintheproductionservicesofeBay.Zhangetal.(2021)propose
arootcauseanalysisframeworkthatalsoleveragesdifferentdatasources:KeyPerformance
Indicators(KPIs),logs,andtopologydata.TheirprimarymodelisahierarchicalBayesian
networkthathelpshandlenoveltypesofrootcauses.
Incidentmanagement Incidentmanagementreferstotheprocessofidentifying,analyz-
ing,andresolvingincidentsthatoccurwithinasoftwaresystem.Althoughthemajorityof
organizationshaveestablisheduniquemethodsforhandlingincidents,criticalserviceinci-
dentsstillhappenunexpectedly,andtheincidentsystemfailstomitigatethem.Chenetal.
(2020b)provideanoverviewofincidentmanagement.Theyanalyzetheincidentmanage-
mentpracticesatMicrosoftovertwoyearsandidentifythedistributionofincidentseverities
foreachsection(e.g.,network,database).SahaandHoi(2022)leveragepastincidentroot
cause analysis reports to manage the incidents. They present an incident causation analy-
sisenginethatextractsinformationfrompreviousrootcauseanalysisreportsandusethat
knowledgefornewincidents.Theyemploypre-trainedNLPmodelsoverreportscollected
overafewyearsatSalesforce.Lietal.(2022b)proposeanAIOpsframeworkforincident
detection.Theirframeworkconsistsoffourmainparts:multi-aspectdetection(whereitis
abletoautomaticallyidentifythecombinationsofdifferentdatatypessuchaslogsandper-
formancemetrics),proactivedetection(whereitcanproactivelysearchforfuturehardware
andsoftwarefailures),incidentrefinement(whereitcanprovideaglobalviewoftheincident
andprioritizehigh-impactincidents),andincidentenrichment(whereitcanlocatethefaulty
scope).
123

Empirical Software Engineering (2023) 28:143 Page 43 of 49 143
AIOpsliteraturereviews ThereexisttwoarticlesthatsurveyexistingAIOpsstudies.Notaro
etal.(2021b)conductasystematicmappingstudytoidentifypastresearchinAIOps.They
provideataxonomyofAIOpspapersinordertoinvestigatethetrendsandalsoacomparison
ofAIOpspapersforspecificproblems.Theirfindingsdemonstrateanon-growingresearch
interestinthefieldofAIOps,particularlyfordownstreamtaskssuchasanomalydetection
androotcauseanalysis.Accordingtotheirpaper,themajorityofstudies(morethan60%)
arerelatedtofailuremanagement(e.g.,failurepredictionandfailuredetection).Resource
managementandschedulingaretwootherpopularareasinAIOps.Tounderstandthetrends
in AIOps articles, similarly, Rijal et al. (2022) perform a literature review about AIOps
works. Their findings support the growing interest in AIOps (Notaro et al. 2021b). Their
resultscountseveralbenefitsofAIOps:bettermonitoringofITwork,efficienttimesaving,
improved human-AI collaborations, proactive IT work, and faster Mean Time To Resolve
(MTTR).ThedevelopmentofAIOpssolutionsalsofacesanumberofdifficulties,including
doubtabouttheefficiencyofAIandML,low-qualitydata,identifyingtheproperusecases,
andtraditionalengineeringapproaches.Theirpaperconcludestheneedforfurtherresearch
toimprovehumanandAIOpsinteractioninordertoenhancehumanproductivity.Theresults
ofourworkcancomplementtheseliteraturereviews.
However, none of the existing work studies real-world AIOps projects. Different from
thesestudies,inthiswork,weperformanempiricalstudytounderstandthepracticesand
characteristicsofreal-worldAIOpsprojectsonGitHub.
6.2 CharacterizingGitHubProjects
Asthebiggesthostingserviceforopen-sourcesoftware,GitHubhasbeenstudiedremarkably
inthepastyears.Somestudiesfocusonthebestapproachesforfindingthemostprominent
repositoriesonGitHub(Dabicetal.2021;Kalliamvakouetal.2014, 2016).Manystudies
also have used GitHub as a source for mining software repositories (Businge et al. 2019;
Coelho et al. 2018; Guzman et al. 2014; Horschig et al. 2018; Kallis et al. 2021; Lopes
etal.2017;ManesandBaysal2021;Subramanianetal.2020;VadlamaniandBaysal2020;
Wessel et al.2018). For example, Vadlamani and Baysal (2020), along with Subramanian
etal.(2020);Horschigetal.(2018)trytocharacterizethedevelopersofopen-sourcesoftware.
Asanotherexample,Kallisetal.(2021)trytopredicttheissuetypesofprojects.Moresimilar
toourstudy,Ghrairietal.(2018)studythestateofVirtualReality(VR)projectsextracted
fromGitHub.Inanotherwork,Coppolaetal.(2019)characterizethepopularityofKotlinin
Androidprojectsbyanalyzing1,232applicationsonGitHub.However,asfarasweknow,
nostudieshavebeenconductedyetonthesubjectofAIOps.Ourworkisthefirststudythat
usesGitHubtocharacterizeandanalyzeAIOpsprojects.
6.3 AnalyzingCodeQualityUsingSonarQube
SonarQubeisoneofthemostpopularstaticcodeanalysesusedbothinacademia(Lenarduzzi
etal.2017, 2018)andindustry(Vassalloetal.2020).Previousresearchhasconductedmany
analyses on the code quality of open-source software projects using SonarQube. Businge
etal.(2019)useSonarQubeandanalysesthesourcecodeof119applicationstofindtheir
numberofbugs.Inanotherwork,Tanetal.(2018)study9Apachesoftwaresystemswritten
in Python to investigate their technical debt. Lenarduzzi et al. (2019) also investigate the
123

143 Page 44 of 49 Empirical Software Engineering (2023) 28:143
technicaldebtof33ApachesystemswritteninJava.Theyfindthattheamountofcodesmell
ismuchhigherthanbugsorvulnerabilitiesintheirsetofprojects.Theyalsoreportthatthe
codesmellswiththeseveritylevelmajortakethelongesttimetogetfixed.Comparedtothe
mentionedstudies,ourpaperanalyzesthequalityof6,101projects,whichismuchhigher
thaninthepreviousstudies,makingourresultsmoreconfidentandrobust.
7 Conclusion
ThisworkstudiesthecharacteristicsofAIOpsprojectsonGitHubandconductsacomparative
analysis with two baseline sets (ML and General projects). We combine both quantitative
andqualitativeanalysestounderstandthecurrentstateofAIOpssolutions.Specifically,we
illustratethestateofAIOpsprojectsonGitHubinRQ1,observingthattheyarerelativelynew
andhavebeengrowingrapidlyinrecentyears.Wedeterminethemostcommoninputdata,
techniques,andgoalsofAIOpssolutionsinRQ2.Byuncoveringthesepatterns,researchers
andpractitionerscanlearnfromsuccessfulapproachesandadoptoptimalAIOpssolutions
fortheirspecificapplicationscenarios.WetheninvestigatethequalityofAIOpsprojectsin
termsofcodequalityandcomparethemtothebaselinesinRQ3.Weobservethatthequality
ofAIOpsprojectsispoorercomparedtothebaselines.Ourfindingshighlighttheneedfor
future efforts to enhance AIOps practices. For example, addressing weak aspects such as
self-healingandreducingthead-hocnessofcodingcanleadtoimprovedAIOpsquality.
Ourstudycouldbeextendedindifferentways.First,westudytheAIOpsprojectspublicly
availableonGitHub.However,theremightbedifferencesbetweenopen-sourceprojectsand
closed-sourceprojectswhichareimplementedforprivatedatasetsincompanies.Thus,one
extensiontoourstudycouldbetogatherandanalyzetheindustrialAIOpssolutionsandreport
anysimilaritiesanddifferenceswithAIOpsprojectsonGitHub.Second,basedonourresults
regardingtheinputs,techniques,andgoalsofAIOpssolutions,futureworkmaydevelopa
pipelinetoautomateoraugmentthedevelopmentofAIOpssolutions.Third,wediscussedthe
potentialofintegratingexistingqualityassurancetechniquesfrommachinelearningsystems
intoAIOpssolutions.Hence,futureresearchcouldimplementthesetechniquesforAIOps
solutions,examiningtheirimpactonenhancingAIOpscodequality.Finally,conductinga
futurestudythatincludesinterviewswithAIOpsresearchersandpractitionerscouldserve
tovalidateandextendthefindingsofourwork.
CodeAvailability Ourdatasets,codeandanalysisarepubliclyavailableonhttps://github.com/roozbehaghili/
studying_aiops_github.
Declarations
Conflictsofinterest Theauthorshavenoconflictsofinteresttodeclarethatarerelevanttothecontentofthis
article.
References
ArtsteinR,PoesioM(2008)Inter-coderagreementforcomputationallinguistics.ComputLinguist34(4):555–
596
BasiliVR,SelbyRW,HutchensDH(1986)Experimentationinsoftwareengineering.IEEETransSoftwEng
7:733–743
123

Empirical Software Engineering (2023) 28:143 Page 45 of 49 143
BeschastnikhI,BrunY,ErnstMD,KrishnamurthyA(2014)Inferringmodelsofconcurrentsystemsfrom
logsoftheirbehaviorwithcsight.In:Proceedingsofthe36thInternationalConferenceonSoftware
Engineering,p468–479
BogatinovskiJ,NedelkoskiS,AckerA,SchmidtF,WittkoppT,BeckerS,CardosoJ,KaoO(2021)Artificial
intelligenceforitoperations(aiops)workshopwhitepaper.arXiv:2101.06054
BraiekHB,KhomhF(2022)Testingfeedforwardneuralnetworkstrainingprograms.ACMTransSoftwEng
Methodol.https://doi.org/10.1145/3529318
Brown A, Tuor A, Hutchinson B, Nichols N (2018) Recurrent neural network attention mechanisms for
interpretablesystemloganomalydetection.In:Proceedingsofthefirstworkshoponmachinelearning
forcomputingsystems,p1–8
BusingeJ,OpenjaM,KavalerD,BainomugishaE,KhomhF,FilkovV(2019)Studyingandroidapppopularity
bycross-linkinggithubandgoogleplaystore.2019IEEE26thInternationalConferenceonSoftware
Analysis.EvolutionandReengineering(SANER),IEEE,pp287–297
ChenB,JiangZM(2021)Asurveyofsoftwareloginstrumentation.ACMComputSurv(CSUR)54(4):1–34
ChenZ,CaoY,LiuY,WangH,XieT,LiuX(2020a)Acomprehensivestudyonchallengesindeploying
deeplearningbasedsoftware.In:Proceedingsofthe28thACMJointMeetingonEuropeanSoftware
EngineeringConferenceandSymposiumontheFoundationsofSoftwareEngineering,p750–762
ChenZ,KangY,LiL,ZhangX,ZhangH,XuH,ZhouY,YangL,SunJ,XuZ,etal.(2020b)Towards
intelligentincidentmanagement:whyweneeditandhowwemakeit.In:Proceedingsofthe28thACM
JointMeetingonEuropeanSoftwareEngineeringConferenceandSymposiumontheFoundationsof
SoftwareEngineering,p1487–1497
ChenZ,LiuJ,GuW,SuY,LyuMR(2021)Experiencereport:deeplearning-basedsystemloganalysisfor
anomalydetection.arXiv:2107.05908
CliffN(1993)Dominancestatistics:Ordinalanalysestoanswerordinalquestions.PsycholBull114(3):494
CoelhoJ,ValenteMT,SilvaLL,ShihabE(2018)Identifyingunmaintainedprojectsingithub.In:Proceedings
ofthe12thACM/IEEEInternationalSymposiumonEmpiricalSoftwareEngineeringandMeasurement,
pp1–10
CohenJ(1960)Acoefficientofagreementfornominalscales.EducPsycholMeas20(1):37–46
CoppolaR,ArditoL,TorchianoM(2019)Characterizingthetransitiontokotlinofandroidapps:astudyon
f-droid,playstore,andgithub.In:Proceedingsofthe3rdACMSIGSOFTInternationalWorkshopon
AppMarketAnalytics,p8–14
DabicO,AghajaniE,BavotaG(2021)Samplingprojectsingithubformsrstudies.In:2021IEEE/ACM18th
InternationalConferenceonMiningSoftwareRepositories(MSR),IEEE,pp560–564
DakhelAM,DesmaraisMC,KhomhF(2023)Dev2vec:Representingdomainexpertiseofdevelopersinan
embeddingspace.InfSoftwTechnol159:107218
DangY,LinQ,HuangP(2019)Aiops:real-worldchallengesandresearchinnovations.In:2019IEEE/ACM
41stInternationalConferenceonSoftwareEngineering:CompanionProceedings(ICSE-Companion),
IEEE,p4–5
DevlinJ,ChangMW,LeeK,ToutanovaK(2018)Bert:Pre-trainingofdeepbidirectionaltransformersfor
languageunderstanding.arXiv:1810.04805
DiStefanoA,DiStefanoA,MoranaG,ZitoD(2021)Prometheusandaiopsfortheorchestrationofcloud-
nativeapplicationsinananke.In:2021IEEE30thInternationalConferenceonEnablingTechnologies:
InfrastructureforCollaborativeEnterprises(WETICE),IEEE,p27–32
Ding J, Wang X, Ye X, Ouyang Y, Chai Y (2021) Ttercl: An onsite real-time alarm root-cause location
algorithm.In:2021IEEEInternationalConferenceonBigData(BigData),IEEE,p4852–4858
DingR,FuQ,LouJG,LinQ,ZhangD,ShenJ,XieT(2012)Healingonlineservicesystemsviamininghistor-
icalissuerepositories.In:Proceedingsofthe27thIEEE/ACMInternationalConferenceonAutomated
SoftwareEngineering,ASE-12,p318–321
DingR,FuQ,LouJG,LinQ,ZhangD,XieT(2014)Mininghistoricalissuerepositoriestoheallarge-
scaleonlineservicesystems.In:201444thAnnualIEEE/IFIPInternationalConferenceonDependable
SystemsandNetworks,IEEE,p311–322
DuM,LiF,ZhengG,SrikumarV(2017)Deeplog:Anomalydetectionanddiagnosisfromsystemlogsthrough
deeplearning.In:Proceedingsofthe2017ACMSIGSACconferenceoncomputerandcommunications
security,p1285–1298
El-SayedN,ZhuH,SchroederB(2017)Learningfromfailureacrossmultipleclusters:Atrace-drivenapproach
tounderstanding,predicting,andmitigatingjobterminations.In:2017IEEE37thInternationalConfer-
enceonDistributedComputingSystems(ICDCS),IEEE,p1333–1344
FengZ,GuoD,TangD,DuanN,FengX,GongM,ShouL,QinB,LiuT,JiangD,etal.(2020)Codebert:A
pre-trainedmodelforprogrammingandnaturallanguages.arXiv:2002.08155
123

143 Page 46 of 49 Empirical Software Engineering (2023) 28:143
Foalem PL, Khomh F, Li H (2023) Studying logging practice in machine learning-based applications.
arXiv:2301.04234
FuQ,LouJG,WangY,LiJ(2009)Executionanomalydetectionindistributedsystemsthroughunstructured
loganalysis.In:2009ninthIEEEinternationalconferenceondatamining,IEEE,p149–158
GaoJ,WangH,ShenH(2020)Taskfailurepredictioninclouddatacentersusingdeeplearning.IEEETrans
ServComput
GhrairiN,KpodjedoS,BarrakA,PetrilloF,KhomhF(2018)Thestateofpracticeonvirtualreality(vr)
applications:Anexploratorystudyongithubandstackoverflow.2018IEEEInternationalConference
onSoftwareQuality.ReliabilityandSecurity(QRS),IEEE,pp356–366
GitHub(2023)GitHub.https://github.com/,LastAccessed:06-June-2023
GitHubI(2022)Tocreateintegrations,retrievedata,andautomateyourworkflows,buildwiththegithubrest
api.https://docs.github.com/en/rest
GuzmanE,AzócarD,LiY(2014)Sentimentanalysisofcommitcommentsingithub:anempiricalstudy.In:
Proceedingsofthe11thworkingconferenceonminingsoftwarerepositories,p352–355
Han J, Pei J, Yin Y (2000) Mining frequent patterns without candidate generation. ACM sigmod record
29(2):1–12
HanJ,PeiJ,YinY,MaoR(2004)Miningfrequentpatternswithoutcandidategeneration:Afrequent-pattern
treeapproach.DataMinKnowlDiscov8(1):53–87
HanJ,ChengH,XinD,YanX(2007)Frequentpatternmining:currentstatusandfuturedirections.DataMin
KnowlDiscov15(1):55–86
HeP,ChenZ,HeS,LyuMR(2018a)Characterizingthenaturallanguagedescriptionsinsoftwarelogging
statements.In:Proceedingsofthe33rdACM/IEEEInternationalConferenceonAutomatedSoftware
Engineering,p178–189
HeS,ZhuJ,HeP,LyuMR(2016)Experiencereport:Systemloganalysisforanomalydetection.In:2016
IEEE27thinternationalsymposiumonsoftwarereliabilityengineering(ISSRE),IEEE,p207–218
HeS,LinQ,LouJG,ZhangH,LyuMR,ZhangD(2018b)Identifyingimpactfulservicesystemproblemsvia
loganalysis.In:Proceedingsofthe201826thACMJointMeetingonEuropeanSoftwareEngineering
ConferenceandSymposiumontheFoundationsofSoftwareEngineering,p60-70
HindleA,BarrET,GabelM,SuZ,DevanbuP(2016)Onthenaturalnessofsoftware.CommunACM59(5):122–
131
HorschigS,MattisT,HirschfeldR(2018)Dojavaprogrammerswritebetterpython?studyingoff-language
codequalityongithub.In:Conferencecompanionofthe2ndinternationalconferenceonart,science,
andengineeringofprogramming,p127–134
IslamMJ,NguyenG,PanR,RajanH(2019)Acomprehensivestudyondeeplearningbugcharacteristics.In:
Proceedingsofthe201927thACMJointMeetingonEuropeanSoftwareEngineeringConferenceand
SymposiumontheFoundationsofSoftwareEngineering,p510–520
JupyterI(2022)nbconvert:ConvertNotebookstootherformats.https://nbconvert.readthedocs.io/en/latest/,
LastAccessed:06-Dec.-2022
KalliamvakouE,GousiosG,BlincoeK,SingerL,GermanDM,DamianD(2014)Thepromisesandperils
ofmininggithub.In:Proceedingsofthe11thworkingconferenceonminingsoftwarerepositories,p
92–101
KalliamvakouE,GousiosG,BlincoeK,SingerL,GermanDM,DamianD(2016)Anin-depthstudyofthe
promisesandperilsofmininggithub.EmpirSoftwEng21(5):2035–2071
KallisR,DiSorboA,CanforaG,PanichellaS(2021)Predictingissuetypesongithub.SciComputProgram
205:102598
KhandkarSH(2009)Opencoding.UniversityofCalgary23:2009
KodinariyaTM,MakwanaPRetal(2013)Reviewondeterminingnumberofclusterink-meansclustering.
IntJ1(6):90–95
LakhinaA,CrovellaM,DiotC(2004)Diagnosingnetwork-widetrafficanomalies.ACMSIGCOMMComput
CommunRev34(4):219–230
LakhinaA,CrovellaM,DiotC(2005)Mininganomaliesusingtrafficfeaturedistributions.ACMSIGCOMM
ComputCommunRev35(4):217–228
LenarduzziV,SillittiA,TaibiD(2017)Analyzingfortyyearsofsoftwaremaintenancemodels.In:2017
IEEE/ACM 39th International Conference on Software Engineering Companion (ICSE-C), IEEE, p
146–148
LenarduzziV,SillittiA,TaibiD(2018)Asurveyoncodeanalysistoolsforsoftwaremaintenanceprediction.
In:InternationalConferenceinSoftwareEngineeringforDefenceApplications,Springer,p165–175
LenarduzziV,SaarimakiN,TaibiD(2019)Onthediffusenessofcodetechnicaldebtinjavaprojectsofthe
apacheecosystem.In:2019IEEE/ACMInternationalConferenceonTechnicalDebt(TechDebt),IEEE,
p98–107
123

Empirical Software Engineering (2023) 28:143 Page 47 of 49 143
Li J, Dai L, Tan F, Shen H, Wang Z, Sheng B, Hu P (2022) Cdx-net: Crossdomain multi-feature fusion
modelingviadeepneuralnetworksformultivariatetimeseriesforecastinginaiops.ICASSP2022–
2022IEEEInternationalConferenceonAcoustics.SpeechandSignalProcessing(ICASSP),IEEE,pp
4073–4077
LiS,WuY,LiuY,WangD,WenM,TaoY,SuiY,LiuY(2020a)Anexploratorystudyofbugsinextended
realityapplicationsontheweb.In:2020IEEE31stInternationalSymposiumonSoftwareReliability
Engineering(ISSRE),IEEE,p172–183
LiY,JiangZM,LiH,HassanAE,HeC,HuangR,ZengZ,WangM,ChenP(2020)Predictingnodefailures
inanultra-large-scalecloudcomputingplatform:anaiopssolution.ACMTransSoftwEngMethodol
(TOSEM)29(2):1–24
LiY,ZhangX,HeS,ChenZ,KangY,LiuJ,LiL,DangY,GaoF,XuZetal(2022)Anintelligentframeworkfor
timely,accurate,andcomprehensivecloudincidentdetection.ACMSIGOPSOperSystRev56(1):1–7
LimMH,LouJG,ZhangH,FuQ,TeohABJ,LinQ,DingR,ZhangD(2014)Identifyingrecurrentandunknown
performanceissues.In:2014IEEEInternationalConferenceonDataMining,IEEE,p320–329
LinQ,HsiehK,DangY,ZhangH,SuiK,XuY,LouJG,LiC,WuY,YaoR,etal.(2018)Predictingnodefailure
incloudservicesystems.In:Proceedingsofthe201826thACMJointMeetingonEuropeanSoftware
EngineeringConferenceandSymposiumontheFoundationsofSoftwareEngineering,p480–490
Liu D, Zhao Y, Xu H, Sun Y, Pei D, Luo J, Jing X, Feng M (2015) Opprentice: Towards practical and
automaticanomalydetectionthroughmachinelearning.In:Proceedingsofthe2015internetmeasurement
conference,p211–224
LomioF,MoreschiniS,LenarduzziV(2021)FaultpredictionbasedonsoftwaremetricsandSonarQuberules.
machineordeeplearning?arXiv:2103.11321
LopesCV,MajP,MartinsP,SainiV,YangD,ZitnyJ,SajnaniH,VitekJ(2017)Déjàvu:amapofcode
duplicatesongithub.ProceedingsoftheACMonProgrammingLanguages1(OOPSLA):1–28
LouJG,LinQ,DingR,FuQ,ZhangD,XieT(2013)Softwareanalyticsforincidentmanagementofonlineser-
vices:Anexperiencereport.In:201328thIEEE/ACMInternationalConferenceonAutomatedSoftware
Engineering(ASE),IEEE,p475–485
LouJG,LinQ,DingR,FuQ,ZhangD,XieT(2017)Experiencereportonapplyingsoftwareanalyticsin
incidentmanagementofonlineservice.AutomSoftwEng24(4):905–941
Lovric´ M,Milanovic´ M,Stamenkovic´ M(2014)Algoritmicmethodsforsegmentationoftimeseries:An
overview.JContempEconBusIssues1(1):31–53
LuoC,LouJG,LinQ,FuQ,DingR,ZhangD,WangZ(2014)Correlatingeventswithtimeseriesforincident
diagnosis.In:Proceedingsofthe20thACMSIGKDDinternationalconferenceonKnowledgediscovery
anddatamining,p1583–1592
LyuY,RajbahadurGK,LinD,ChenB,JiangZM(2021)Towardsaconsistentinterpretationofaiopsmodels.
ACMTransSoftwEngMethodol(TOSEM)31(1):1–38
MajidiF,OpenjaM,KhomhF,LiH(2022)Anempiricalstudyontheusageofautomatedmachinelearning
tools.In:2022IEEEInternationalConferenceonSoftwareMaintenanceandEvolution(ICSME),IEEE,
p59–70
ManesSS,BaysalO(2021)Studyingthechangehistoriesofstackoverflowandgithubsnippets.In:2021
IEEE/ACM18thInternationalConferenceonMiningSoftwareRepositories(MSR),IEEE,p283–294
MannHB,WhitneyDR(1947)Onatestofwhetheroneoftworandomvariablesisstochasticallylargerthan
theother.Theannalsofmathematicalstatisticsp50–60
McHughML(2012)Interraterreliability:thekappastatistic.Biochemiamedica22(3):276–282
MunaiahN,KrohS,CabreyC,NagappanM(2017)Curatinggithubforengineeredsoftwareprojects.Empir
SoftwEng22(6):3219–3253
NakajimaS(2018)Qualityassuranceofmachinelearningsoftware.In:2018IEEE7thGlobalConferenceon
ConsumerElectronics(GCCE),IEEE,p601–604
NedelkoskiS,CardosoJ,KaoO(2019a)Anomalydetectionandclassificationusingdistributedtracingand
deeplearning.In:201919thIEEE/ACMinternationalsymposiumoncluster,cloudandgridcomputing
(CCGRID),IEEE,p241–250
NedelkoskiS,CardosoJ,KaoO(2019b)Anomalydetectionfromsystemtracingdatausingmultimodaldeep
learning.In:2019IEEE12thInternationalConferenceonCloudComputing(CLOUD),IEEE,p179–186
NikanjamA,BraiekHB,MorovatiMM,KhomhF(2021)Automaticfaultdetectionfordeeplearningprograms
usinggraphtransformations.ACMTransSoftwEngMethodol31(1),https://doi.org/10.1145/3470006
NikanjamA,MorovatiMM,KhomhF,BenBraiekH(2022)Faultsindeepreinforcementlearningprograms:
Ataxonomyandadetectionapproach.AutomSoftwEng29(1),https://doi.org/10.1007/s10515-021-
00313-x
NotaroP,CardosoJ,GerndtM(2021)Asurveyofaiopsmethodsforfailuremanagement.ACMTransIntell
SystTechnol(TIST)12(6):1–45
123

143 Page 48 of 49 Empirical Software Engineering (2023) 28:143
NotaroP,CardosoJ,GerndtM(2021b)Asystematicmappingstudyinaiops.In:Service-OrientedComputing-
ICSOC2020Workshops:AIOps,CFTIC,STRAPS,AI-PA,AI-IOTS,andSatelliteEvents,Dubai,United
ArabEmirates,December14-17,2020,Proceedings,Springer,p110–123
OpenjaM,MorovatiMM,AnL,KhomhF,AbidiM(2022)Technicaldebtsandfaultsinopen-sourcequantum
softwaresystems:Anempiricalstudy.JSystSoftw193:111458
PothA,MeyerB,SchlichtP,RielA(2020)Qualityassuranceformachinelearning-anapproachtofunction
andsystemsafeguarding.2020IEEE20thInternationalConferenceonSoftwareQuality.Reliabilityand
Security(QRS),IEEE,pp22–29
PrasadP,RichC(2018)MarketGuideforAIOpsPlatforms.https://www.gartner.com/en/documents/3892967,
LastAccessed:-06-Dec.-2022
RasoolG,ArshadZ(2015)Areviewofcodesmellminingtechniques.JSoftw:EvolProcess27(11):867–895
Rijal L, Colomo-Palacios R, Sánchez-Gordón M (2022) Aiops: A multivocal literature review. Artificial
IntelligenceforCloudandEdgeComputingp31–50
RomanoJ,KromreyJD,CoraggioJ,SkowronekJ,DevineL(2006)Exploringmethodsforevaluatinggroup
differencesonthensseandothersurveys:Arethet-testandcohensdindicesthemostappropriatechoices.
In:annualmeetingoftheSouthernAssociationforInstitutionalResearch,Citeseer,p1–51
RosáA, ChenLY,BinderW(2015)Catchingfailuresoffailures atbig-dataclusters: Atwo-levelneural
networkapproach.In:2015IEEE23rdInternationalSymposiumonQualityofService(IWQoS),IEEE,
p231–236
SaarimakiN,BaldassarreMT,LenarduzziV,RomanoS(2019)OntheaccuracyofSonarQubetechnical
debtremediationtime.In:201945thEuromicroConferenceonSoftwareEngineeringandAdvanced
Applications(SEAA),IEEE,p317–324
SahaA,HoiSC(2022)Miningrootcauseknowledgefromcloudserviceincidentinvestigationsforaiops.
In:Proceedingsofthe44thInternationalConferenceonSoftwareEngineering:SoftwareEngineeringin
Practice,p197–206
Shapiro SS, Wilk MB (1965) An analysis of variance test for normality (complete samples). Biometrika
52(3/4):591–611
SharmaB,JayachandranP,VermaA,DasCR(2013)Cloudpd:Problemdeterminationanddiagnosisinshared
dynamicclouds.In:201343rdAnnualEEE/IFIPInternationalConferenceonDependableSystemsand
Networks(DSN),IEEE,p1–12
StolKJ,RalphP,FitzgeraldB(2016)Groundedtheoryinsoftwareengineeringresearch:acriticalreviewand
guidelines.In:Proceedingsofthe38thInternationalconferenceonsoftwareengineering,p120–131
SuY,ZhaoY,NiuC,LiuR,SunW,PeiD(2019)Robustanomalydetectionformultivariatetimeseriesthrough
stochasticrecurrentneuralnetwork.In:Proceedingsofthe25thACMSIGKDDinternationalconference
onknowledgediscovery&datamining,p2828–2837
SubramanianVN,RehmanI,NagappanM,KulaRG(2020)Analyzingfirstcontributionsongithub:whatdo
newcomersdo.IEEESoftware
SvobodaJ,GhafirI,PrenosilVetal(2015)Networkmonitoringapproaches:Anoverview.IntJAdvComput
NetwSecur5(2):88–93
TambonF,KhomhF,AntoniolG(2023)Aprobabilisticframeworkformutationtestingindeepneuralnetworks.
InfSoftwTechnol155:107129.https://doi.org/10.1016/j.infsof.2022.107129,https://www.sciencedirect.
com/science/article/pii/S0950584922002385
TanJ,LunguM,AvgeriouP(2018)Towardsstudyingtheevolutionoftechnicaldebtinthepythonprojects
fromtheapachesoftwareecosystem.In:BENEVOL,p43–45
TuZ,SuZ,DevanbuP(2014)Onthelocalnessofsoftware.In:Proceedingsofthe22ndACMSIGSOFT
InternationalSymposiumonFoundationsofSoftwareEngineering,p269–280
VadlamaniSL,BaysalO(2020)Studyingsoftwaredeveloperexpertiseandcontributionsinstackoverflow
andgithub.In:2020IEEEInternationalConferenceonSoftwareMaintenanceandEvolution(ICSME),
IEEE,p312–323
VassalloC,PanichellaS,PalombaF,ProkschS,GallHC,ZaidmanA(2020)Howdevelopersengagewith
staticanalysistoolsindifferentcontexts.EmpirSoftwEng25(2):1419–1457
WangH,WuZ,JiangH,HuangY,WangJ,KopruS,XieT(2021)Groot:Anevent-graph-basedapproach
for root cause analysis in industrial settings. In: 2021 36th IEEE/ACM International Conference on
AutomatedSoftwareEngineering(ASE),IEEE,p419–429
WesselM,DeSouzaBM,SteinmacherI,WieseIS,PolatoI,ChavesAP,GerosaMA(2018)Thepowerofbots:
Characterizingandunderstandingbotsinossprojects.ProceedingsoftheACMonHuman-Computer
Interaction2(CSCW):1–19
WilsonSJ(2017)Datarepresentationfortimeseriesdatamining:timedomainapproaches.WileyInterdiscip
RevComputStat9(1):e1392
123

Empirical Software Engineering (2023) 28:143 Page 49 of 49 143
WohlinC,AurumA(2015)Towardsadecision-makingstructureforselectingaresearchdesigninempirical
softwareengineering.EmpirSoftwEng20(6):1427–1455
XuW,HuangL,FoxA,PattersonD,JordanMI(2009)Detectinglargescalesystemproblemsbymining
consolelogs.In:ProceedingsoftheACMSIGOPS22ndsymposiumonOperatingsystemsprinciples,p
117–132
XueJ,BirkeR,ChenLY,SmirniE(2016)Managingdatacentertickets:Predictionandactivesizing.In:2016
46thAnnualIEEE/IFIPInternationalConferenceonDependableSystemsandNetworks(DSN),IEEE,
p335–346
XueJ,BirkeR,ChenLY,SmirniE(2018)Spatial-temporalpredictionmodelsforactiveticketmanagingin
datacenters.IEEETransNetwServManag15(1):39–52
YaoK,LiH,ShangW,HassanAE(2020)Astudyoftheperformanceofgeneralcompressorsonlogfiles.
EmpirSoftwEng25:3043–3085
ZhangT,GaoC,MaL,LyuM,KimM(2019)Anempiricalstudyofcommonchallengesindevelopingdeep
learningapplications.In:2019IEEE30thInternationalSymposiumonSoftwareReliabilityEngineering
(ISSRE),IEEE,p104–115
ZhangY,ChenY,CheungSC,XiongY,ZhangL(2018)Anempiricalstudyontensorflowprogrambugs.In:
Proceedingsofthe27thACMSIGSOFTInternationalSymposiumonSoftwareTestingandAnalysis,p
129–140
Zhang Y, Guan Z, Qian H, Xu L, Liu H, Wen Q, Sun L, Jiang J, Fan L, Ke M (2021) Cloudrca: a root
causeanalysisframeworkforcloudcomputingplatforms.In:Proceedingsofthe30thACMInternational
ConferenceonInformation&KnowledgeManagement,p4373–4382
ZhaoG,HassanS,ZouY,TruongD,CorbinT(2021)Predictingperformanceanomaliesinsoftwaresystems
atrun-time.ACMTransSoftwEngMethodol(TOSEM)30(3):1–33
Publisher’sNote SpringerNatureremainsneutralwithregardtojurisdictionalclaimsinpublishedmapsand
institutionalaffiliations.
SpringerNatureoritslicensor(e.g.asocietyorotherpartner)holdsexclusiverightstothisarticleunder
a publishing agreement with the author(s) or other rightsholder(s); author self-archiving of the accepted
manuscriptversionofthisarticleissolelygovernedbythetermsofsuchpublishingagreementandapplicable
law.
123