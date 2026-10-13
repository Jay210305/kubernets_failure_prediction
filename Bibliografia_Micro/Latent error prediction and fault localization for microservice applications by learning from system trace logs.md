PDF Download
3338906.3338961.pdf
01 April 2026
Total Citations: 225
. Total Downloads: 2658
.
Latest updates: hps://dl.acm.org/doi/10.1145/3338906.3338961 .
.
Published: 12 August 2019
.
. .
RESEARCH-ARTICLE .
Citation in BibTeX format
Latent error prediction and fault localization for microservice
.
.
applications by learning from system trace logs ESEC/FSE '19: 27th ACM Joint European
Soware Engineering Conference and
Symposium on the Foundations of
XIANG ZHOU, Fudan University, Shanghai, China Soware Engineering
August 26 - 30, 2019
. XIN PENG, Fudan University, Shanghai, China Tallinn, Estonia
.
. TAO XIE, University of Illinois Urbana-Champaign, Urbana, IL, United States . Conference Sponsors:
SIGSOFT
.
JUN SUN, Singapore Management University, Singapore City, Singapore
.
CHAO JI, Fudan University, Shanghai, China
.
DEWEI LIU, Fudan University, Shanghai, China
.
View all
.
.
Open Access Support provided by:
.
Singapore Management University
.
Fudan University
.
University of Illinois Urbana-Champaign
.
ESEC/FSE 2019: Proceedings of the 2019 27th ACM Joint Meeting on European Soware Engineering Conference and Symposium on the Foundations of Soware Engineering (August 2019)
hps://doi.org/10.1145/3338906.3338961
ISBN: 9781450355728
.

Latent Error Prediction and Fault Localization for Microservice
Applications by Learning from System Trace Logs
XiangZhou∗ XinPeng∗† TaoXie
FudanUniversity FudanUniversity UniversityofIllinoisat
China China Urbana-Champaign
USA
JunSun ChaoJi∗ DeweiLiu∗
SingaporeManagementUniversity FudanUniversity FudanUniversity
Singapore China China
QilinXiang∗ ChuanHe∗
FudanUniversity FudanUniversity
China China
ABSTRACT resultsindicatethatMEPFLcanachievehighaccuracyinintra-
Intheproductionenvironment,alargepartofmicroservicefailures applicationpredictionoflatenterrors,faultymicroservices,and
arerelatedtothecomplexanddynamicinteractionsandruntime fault types, and outperforms a state-of-the-art approach of fail-
environments,suchasthoserelatedtomultipleinstances,environ- urediagnosisfordistributedsystems.Theresultsalsoshowthat
mentalconfigurations,andasynchronousinteractionsofmicroser- MEPFLcaneffectivelypredictlatenterrorscausedbyreal-world
vices.Duetothecomplexityanddynamismofthesefailures,it faultcases.
isoftenhardtoreproduceanddiagnosethemintestingenviron-
CCSCONCEPTS
ments.Itisdesirableyetstillchallengingthatthesefailurescanbe
detectedandthefaultscanbelocatedatruntimeoftheproduction •Softwareanditsengineering→ Cloudcomputing;testing
environmenttoallowdeveloperstoresolvethemefficiently.Toad- anddebugging.
dressthischallenge,inthispaper,weproposeMEPFL,anapproach
oflatenterrorpredictionandfaultlocalizationformicroservice KEYWORDS
applicationsbylearningfromsystemtracelogs.Basedonasetof
microservices,errorprediction,faultlocalization,tracing,debug-
featuresdefinedonthesystemtracelogs,MEPFLtrainsprediction
ging,machinelearning
modelsatboththetracelevelandthemicroservicelevelusingthe
systemtracelogscollectedfromautomaticexecutionsofthetarget ACMReferenceFormat:
applicationanditsfaultyversionsproducedbyfaultinjection.The XiangZhou,XinPeng,TaoXie,JunSun,ChaoJi,DeweiLiu,QilinXiang,
predictionmodelsthuscanbeusedintheproductionenvironment andChuanHe.2019.LatentErrorPredictionandFaultLocalizationfor
topredictlatenterrors,faultymicroservices,andfaulttypesfor MicroserviceApplicationsbyLearningfromSystemTraceLogs.InPro-
ceedingsofthe27thACMJointEuropeanSoftwareEngineeringConference
traceinstancescapturedatruntime.WeimplementMEPFLbased
andSymposiumontheFoundationsofSoftwareEngineering(ESEC/FSE’19),
ontheinfrastructuresystemsofcontainerorchestratorandservice
August26–30,2019,Tallinn,Estonia.ACM,NewYork,NY,USA,12pages.
mesh,andconductaseriesofexperimentalstudieswithtwoopen-
https://doi.org/10.1145/3338906.3338961
sourcemicroserviceapplications(oneofthembeingthelargest
open-sourcemicroserviceapplicationtoourbestknowledge).The
1 INTRODUCTION
∗X.Zhou,X.Peng,C.Ji,D.Liu,Q.Xiang,andC.HearewiththeSchoolofComputer Industrialmicroserviceapplicationshavedozenstothousandsof
ScienceandShanghaiKeyLaboratoryofDataScience,FudanUniversity,Chinaand microservicesrunningonhundredstotensofthousandsmachines.
theShanghaiInstituteofIntelligentElectronics&Systems,China.
Intheproductionenvironment,microserviceapplicationstypically
†X.Pengisthecorrespondingauthor(pengxin@fudan.edu.cn).
arefragile[26],oftenfailingduetoinfrastructure(e.g.,network,
hardware)failuresorapplicationfaults,anditischallengingto
Permissiontomakedigitalorhardcopiesofallorpartofthisworkforpersonalor
reproduceanddiagnosethesemicroserviceapplicationfailuresin
classroomuseisgrantedwithoutfeeprovidedthatcopiesarenotmadeordistributed
forprofitorcommercialadvantageandthatcopiesbearthisnoticeandthefullcitation testingenvironments.Infrastructurefailurescanbepredictedatthe
onthefirstpage.CopyrightsforcomponentsofthisworkownedbyothersthanACM cloudinfrastructurelayerandhandledviainfrastructure-leveladap-
mustbehonored.Abstractingwithcreditispermitted.Tocopyotherwise,orrepublish,
tationssuchastheallocationandmigrationofvirtualmachines[32].
topostonserversortoredistributetolists,requirespriorspecificpermissionand/ora
fee.Requestpermissionsfrompermissions@acm.org. Applicationfaultstraditionallyrelyondeveloperstodetectand
ESEC/FSE’19,August26–30,2019,Tallinn,Estonia fixviacodereview,testing,anddebugging.However,microservice
©2019AssociationforComputingMachinery.
applicationfaultsarecomplicatedduetothecomplexanddynamic
ACMISBN978-1-4503-5572-8/19/08...$15.00
https://doi.org/10.1145/3338906.3338961 interactionsandruntimeenvironments[61].Amicroservicecan
683

ESEC/FSE’19,August26–30,2019,Tallinn,Estonia XiangZhou,XinPeng,TaoXie,JunSun,ChaoJi,DeweiLiu,QilinXiang,andChuanHe
haveseveraltothousandsofinstancesthataredynamicallycre-
atedanddestroyedaccordingtothescalingrequirements.These
instancesrunwithcomplexenvironmentalconfigurationssuch
asmemory/CPUlimitsofmicroservicesandcontainers[62,63].
Microserviceapplicationsusuallyhavecomplexinvocationchains,
eachinvolvingseveraltodozensofmicroserviceinvocations,most
ofwhichareasynchronous.Improperenvironmentalconfigura-
Figure1:BasicConcepts
tionsorcoordinationofmicroserviceinstancesorasynchronous
interactionsmayresultinfailuresatruntime. MEPFLcombinestrace-levelandmicroservice-levelprediction.The
Toallowdeveloperstoresolvemicroserviceapplicationfailures trace-levelpredictionutilizesapplication-specificcontext(e.g.,mi-
efficientlyintheproductionenvironment,itisdesirableandyet croservicesinvolvedinanapplication)initsfeaturevectorsand
challengingthatthesemicroserviceapplicationfailurescanbede- treatsatraceinstance(whichrecordstheprocessofmicroservice
tectedandthefaultscanbelocatedatruntimeoftheproduction invocationsforauserrequest)asawholeduringtrainingandpre-
environment,e.g.,basedonapplicationlogsorsystemlogs.Applica- diction.Itincludesthreemodelstopredictlatenterrors,relevant
tionlogsrecordtheinternalstatusandeventsduringtheexecution microservices,andfaulttypes,respectively.Themicroservice-level
ofanapplication.Theseapplicationlogsareproducedbylogging prediction uses a set of general features for microservices in a
statementswrittenbydevelopersintheapplication.However,ap- context-freeway.Itisbasedonamodeltopredictwhattypeof
plicationloggingisoftendoneinanarbitraryandadhocmanner faultthetargetmicroservicehas.Alltheseprecedingmodelsused
andthelogmessagesoftencontainlimitedinformationforfailure intrace-levelormicroservice-levelpredictionaredefinedonaset
diagnosis[56,57].Ontheotherhand,someexistingapproaches oftracelogfeaturesselectedbycorrelationanalysis.
usesystemlogstodetectanomaliesorpredictfailuresofcloud- Withtwoopen-sourcemicroserviceapplications(SockShop[48]
basedsystems.Thesesystemlogsareproducedbyinfrastructure andTrainTicket[36],whichisthelargestopen-sourcemicroservice
systemssuchasoperatingsystems(e.g.,CentOS[42]),distributed applicationtoourbestknowledge),weconductaseriesofexperi-
file systems (e.g., HDFS [11]), and container orchestrators (e.g.,
mentalstudiestoevaluatetheeffectivenessofMEPFL1.Theresults
Kubernetes [30]). However, these approaches can only uncover showthatMEPFLcanachievehighrecall/precision(0.982/0.998and
anomaliesorfailureswithinthecloudinfrastructuresuchascom- 0.896/0.995)andlowfalsepositiverate(0.009and0.014)inlatent
putingnodes[32]andstorage[24]. errorprediction,highTop-1accuracy(0.933and0.937)infaulty
Toaddressthischallenge,inthispaper,bylearningfromsystem microserviceprediction,andhighrecall/precision(0.952/0.983and
tracelogs,inshortastracelogs(aspecialtypeofsystemlogs),we 0.930/0.986)infaulttypeprediction.MEPFLsubstantiallyoutper-
focusonpredictingthreecommontypesofmicroserviceapplica- formsPhametal.’sapproach[40]intermsoftheaccuracyofthe
tionfaultsthatarespecificallyrelevanttomicroserviceinteractions predictionoffaultymicroservicesandfaulttypes.Withtheincrease
andruntimeenvironments,i.e.,multi-instancefaults,configuration ofthecoverageoftracetypesinthetrainingdata,theoverallpre-
faults,asynchronousinteractionfaults.Accordingtoanexistingem- dictionmoreandmorereliesonthetrace-levelprediction,andthe
piricalstudy[61],almosthalfofallstudiedmicroserviceapplication prediction accuracy substantially increases. To further evaluate
faultsareofthesethreetypes.Differentfrominternal-logicfaults, theeffectivenessofMEPFLinlocalizingreal-worldmicroservice
whicharelocalizedoftenbasedonanalyzinginternalstatesand applicationfaults,weconductanexperimentalstudywiththefault
logics,thesethreetypesoffaultsareusuallyrelevanttoexternal cases[10]providedbytheTrainTicketbenchmark;thesefaultcases
characteristicsoftracelogssuchasthenumberofmicroservicein- arereplicatedfromindustrialfaultcases.Theresultsshowthat
stances,accessesofglobalvariables/localcache,resourceconsump- MEPFLcanaccuratelypredictthelatenterrorscausedbythese
tion,invocationandexecutionorders.RecentlyPhametal.[40] faultcaseswitharecallof0.647-0.983(0.821onaverage)anda
proposeafailurediagnosisapproachfordistributedsystems.This precisionof0.586-0.984(0.891onaverage).
approachlocatesfaultsbymatchingsimilarfailuretracesproduced Inthispaper,wemakethefollowingmaincontributions.
usingfaultinjection.Thismatching-basedapproachhasverylim- • Asetoffeaturesandpredictionmodelsforpredictinglatent
itedgeneralizationabilityandcannotsupportfailurerecognition. errors,faultymicroservices,andfaulttypesformicroservice
Incontrast,inourwork,weextractasetoffeaturesthatreflect applicationsbasedonsystemtracelogs.
thedynamicenvironmentsandinteractionsofmicroservicesfrom • Alearning-basedapproachforlatenterrorpredictionand
tracelogsandtrainasetofpredictionmodelsbasedonthefeatures. faultlocalizationofmicroserviceapplicationsbasedonfault
Thepredictionmodelscanbeusedtonotonlylocatethefaultsbut injectionandtesting.
alsorecognizethefailuresbypredictinglatenterrorscausedbythe • Aseriesofexperimentalstudieswithtwoopen-sourcemi-
faults. croservicebenchmarkstoevaluatetheeffectivenessofthe
Inparticular,inthispaper,weproposeMEPFL(Microservice approach.
ErrorPredictionandFaultLocalization),anovelapproachforlatent
errorpredictionandfaultlocalizationofmicroserviceapplications 2 PRELIMINARIES
bylearningfromtracelogs.WedesignMEPFLtopredictlatent
Ourapproachisdefinedbasedonaseriesofconceptsaboutmi-
errorsofamicroserviceapplicationcausedbytheprecedingthree
croservice.Figure1showstherelationshipsbetweentheseconcepts.
commontypesofmicroserviceapplicationfaults.MEPFLfurther
predictsthelocations(i.e.,microservices)andtypesofthefaults. 1Allthedataofthestudiescanbefoundinourreplicationpackage[46].
684

LatentErrorPredictionandFaultLocalizationforMicroserviceApplications ESEC/FSE’19,August26–30,2019,Tallinn,Estonia
Table1:FaultCasesReportedbyOurPreviousWork[61] resource(e.g.,memoryandCPU)limits.Theyareoftendue
FaultType FaultCases Example toimproperorinconsistentconfigurationsofmicroservices
Monolithic F6,F9,F10,F14- F22:awrongcolumnnameincludedintheconstructed
22 SQLstatement and/ortheirresidingenvironments(e.g.,containersandvir-
Multi-Instance F8,F11,F12 F12:unexpectedoutputofamicroservicewhenitisina
specialstate tualmachines(VMs)).
Configuration F3,F4,F5,F7 F3:improperconfigurationsofJVMandDocker • Asynchronous Interaction Faults. These faults are re-
Asynchronous F1,F2,F13 F1:asynchronousmessagedeliverythatlackssequence
Interaction control latedtotheasynchronousinvocationsamongmicroservices
Amicroserviceapplicationincludesasetofscenariosandeachsce- andmaycausefailureswhenasynchronousinvocationsare
narioincludesmultipletypesofuserrequests(e.g.,differentclicks executedorreturnedinanunexpectedorder.Theyareoften
onthesame“OK”buttononthesamewebpageresultindifferent duetomissingorimpropercoordinationofthesequences
userrequestsofthesameuserrequesttype).Eachuserrequesttype ofasynchronousinvocations.
ismappedtoatracetype.Eachtraceinstancerecordstheprocess
ofmicroserviceinvocationsforauserrequest.Thetracetypefor
thetraceinstanceisthetracetypemappedfromthetypeofthe Themechanismsofmonolithicfaultsaresimilartothoseoffaults
userrequest.Thetraceinstanceincludesaseriesofspansandeach inmonolithicapplications.Forexample,F22isamonolithicfault
spanrepresentsaninvocationbetweentwomicroserviceinstances causedbyanincorrectSQLstatement.Thefailurescausedbythese
(i.e.,acallerandacallee). faultscanbereproducedanddebuggedonasinglemachine.
Forexample,theTrainTicketapplicationhasaTicketReserva- Multi-instancefaultsaremainlyrelatedtoinconsistentstates
tionscenariothatincludesseveraluserrequesttypes(i.e.,trace betweendifferentinstancesofthesamemicroservice.Forexample,
types)suchasQueryAvailableTickets,ConfirmTicketSelection, F12iscausedbyaninconsistentstateofamicroservice.Whenanin-
andPay.ThetraceinstancesofConfirmTicketSelectionincludea vocationchaininvolvestwoinstancesofthesameserviceandtheir
seriesofmicroserviceinvocations,e.g.,theReserveserviceinvokes statesaredifferent,therequestwillbedeniedwithanunexpected
theTicketInfoservice,Foodservice,andseveralotherservices, output.Tofixthefault,thedeveloperscanaddasynchronization
andtheTicketInfoserviceinturninvokesthePriceserviceand mechanismfortheinvolvedstatevariableormoveittoexternal
otherservices. storage(e.g.,Redis).Statelessnessisarecommendedpracticeformi-
Arecenttrendofmicroserviceapplicationsistheintroductionof croservicedevelopment.However,manymicroserviceapplications
containerorchestratorandservicemesh.Acontainerorchestrator inpracticearemigratedfromlegacymonolithicapplications,which
suchasKubernetes(k8s)[30]dynamicallyschedulesandmanagesa areoftenstatefulwithstatevariabledefinitions(i.e.,in-memory
largenumberofcontainerinstances.Inoursystemimplementation, sessionstates)[20].Duetothedifficultyofrefactoring,themigra-
Kubernetesisusedtodynamicallydeploymicroserviceapplica- tionsareoftenhalfway,andstatefulmicroservicesarecommonin
tionsandmanagemicroserviceinstancesandtheirenvironmental enterpriseapplications.
configurationsduringtheofflinetrainingphase.Servicemesh[37] Configuration faults are related to the complex environmen-
isintroducedasaseparatelayerthathandlesservice-to-service tal settings of microservices. A microservice is associated with
communication.ThemostrecognizedimplementationisIstio[25]. a series of application-level environmental configurations such
OursystemimplementationusesIstiotomanageasynchronous astheconfigurationsofJVM(e.g.,max/minheapmemory,stack
microserviceinteractionsduringofflinetrainingandcollecttrace memory,garbagecollectionstrategy),threadpool,anddatabase
logsduringbothofflinetrainingandonlineprediction. connectionpool.Amicroserviceisalsoassociatedwithaseries
ofinfrastructure-levelenvironmentalconfigurationssuchasthe
3 PREDICTIONMODELS configurationsofcontainers(e.g.,memorylimit,CPUlimit,health
check,communicationsecurity)andVMs.Reconcilingthesecon-
3.1 FaultTypes
figurations is a challenging task and often incurs mistakes. For
Collectedinanindustrialsurvey,ourpreviouswork[61]reported example,F3isduetoaconflictbetweenthememorylimitsofJVM
22representativemicroservicefaultcases(seeTable1).Thesefault andDocker;thisconflictcancausetheJVMprocesstobekilled.
casescanbecategorizedintothefollowingfourtypes. Asynchronousinteractionfaultsareusuallycausedbyanunex-
• Monolithic Faults. These faults can cause failures even pectedorderofexecutingasynchronousmicroserviceinvocations.
whentheapplicationisdeployedinamonolithicmode,i.e., Whenamicroserviceinvokesseveralothermicroservicesasyn-
allthemicroservicesaredeployedononenode,eachmi- chronously,theordersoftherequests,executions,andresponses
croservicehasonlyoneinstance,anddifferentmicroservices oftheinvokedmicroservicesareuncertain.Ifthedevelopershave
interactsynchronously.Thesefaultsareusuallyduetofaults unrealisticassumptions,e.g.,theinvokedmicroservicesshallbeexe-
intheinternalimplementationofmicroservicesandareir- cutedandreturnedinthesameorderofinvocations,thedevelopers
relevanttotheruntimeenvironmentsoftheapplication. mayintroduceasynchronousinteractionfaultsintotheapplica-
• Multi-InstanceFaults.Thesefaultsarerelatedtotheex- tions.Forexample,F1liesinanunexpectedorderofexecutions
istenceofmultipleinstancesofthesamemicroserviceat andreturningofmultipleasynchronouslyinvokedmicroservices
runtime.Theyareoftenduetolackingcoordinationamong andcancauseaninvokedmicroservicetobeinanabnormalstatus.
differentinstancesofthesamemicroservice(e.g.,tokeep Table1showsthat12outofthe22faultcases(54.5%)aremono-
theminconsistentstates). lithicfaults,whiletheother10faultcases(45.5%)arerelatedto
• ConfigurationFaults.Thesefaultsarerelatedtotheen- multi-instance,environmentalconfiguration,orasynchronousin-
vironmental configurations of microservices, such as the teraction.Monolithicfaultscanbefoundonasinglemachineby
685

ESEC/FSE’19,August26–30,2019,Tallinn,Estonia XiangZhou,XinPeng,TaoXie,JunSun,ChaoJi,DeweiLiu,QilinXiang,andChuanHe
unitorintegrationtesting,andcanbelocatedusingtraditionaltech- wedevelopthefollowingconventionfortheAITandCEOfeatures:
niquesoffaultlocalizationsuchasassertionsandbreakpoints[55]. (1)assumingthatthereareN microservicesasynchronouslyin-
Therefore,wefocusontheotherthreetypesoffaultsinthispaper. vokedbythecurrentmicroservice,sorttheinvokedmicroservices
bytheinvocationorderandnumberthemfrom1toN;(2)foreach
3.2 FeatureDefinition invokedmicroservice,extractafeatureAIT-i(1≤i ≤N)forcap-
MEPFLaimstopredictwhetheralatenterrorhasoccurred,the turingitsexecutiontime;(3)foreachpairofinvokedmicroservices,
faultymicroservice,andthefaulttype.MEPFLsystematicallyex- setafeatureCEO-i-j (1 ≤ i,j ≤ N)forcapturingwhethertheir
tracts a set of features from trace instances. Figure 2 shows an executionorderisconsistentwiththeirinvocationorder.Forex-
exampleoftraceinstance,whichstartsfromarootmicroservice ample,forA1inFigure2,thereare3AITfeatures,andAIT-1for
R.Inthefigure,eacharrowrepresentsaninvocation(i.e.,span) capturingtheexecutiontimeofD1;thereare3CEOfeatures,and
anddifferentsubscriptsofthesamecapitalletter(e.g.,D1andD2) CEO-1-2forcapturingwhethertheexecutionorderofD1andE1
representdifferentinvocationsofthesamemicroservice(thesame isconsistentwiththeirinvocationorder.Thesefeaturescanbe
ordifferentinstances).Forthistraceinstance,themicroservice relevanttoasynchronousinteractionfaults.
featuresarecalculatedforeachofthe11microserviceinvocations Theprecedingfeaturescanbeusedinthemicroservice-levelpre-
(e.g.,R,A1,D1,andD2). dictionmodel.Tosupporttrace-levelprediction,wefurtherderive
asetoftrace-levelfeaturesforeachtraceinstancebyabsorbing
thefeaturesofeachmicroserviceinvolvedinthetraceinstance.If
amicroserviceisinvokedmultipletimesinthetraceinstance,we
treatthefeaturevaluesofthelastinvocationasthevaluesofthe
correspondingtrace-levelfeatures.Becausetheinfluencesofmany
Figure2:AnExampleofTraceInstance
faultsarecumulativeandsomeotherfaultsterminatetracesatthe
Basedonthedatacollectedinapreviouslyreportedempirical lastinvocation,thelastinvocationofamicroservicemayprovide
study[61],wesummarizeacomprehensivesetofmicroservicefea- themostsignificantindicationforlatenterrors.Forexample,for
turesfromdifferentaspects(i.e.,configuration,resource,instance, thetraceinstanceinFigure2,thereare8RSCfeatures(i.e.,R.RSC,
andinteraction).Thesefeaturescanbeextractedfromtracelogs.A A.RSC,B.RSC,C.RSC,D.RSC,E.RSC,F.RSC,andG.RSC),eachcorre-
featureisdefinedinoneofthreescopes:“global”indicatesthatthe spondingtoaninvolvedmicroservice;andD.RSCistheRSCvalue
featureisaglobalpropertyofthemicroserviceandisirrelevantto ofD2.Thesetrace-levelfeaturesincorporateapplication-specific
thecurrenttraceinstance;“trace”indicatesthatthefeatureisan context,andthuscanbetterpredictlatenterrorsandfaultlocations
overallpropertyofthemicroserviceinthecurrenttraceinstance; ifthemodelshavebeentrainedwithtraceinstancesofsimilartrace
“invocation”indicatesthatthefeatureisapropertyofthecurrent types.Inadditiontothesederivedfeatures,wealsodefine3trace-
microserviceinvocation.Forexample,forthetraceinstanceshown levelfeaturesthataggregatetheexecutioninformationofinvolved
inFigure2,a“global”featureofD1dependsonalltheinstances microservices,i.e.,TET(theexecutiontimeofthecurrenttrace
ofthemicroserviceDatthattime;a“trace”featureofD1depends instance),TMN(thenumberofmicroservicesthatareinvokedin
onD1andD2inthetraceinstance;an“invocation”featureofD1 thecurrenttraceinstance),andTIN(thenumberofmicroservice
dependsononlyD1 itselfinthetraceinstance.Table2showsa instancesthatareinvokedinthecurrenttraceinstance).
completelistofthecandidatefeatures.Detaileddescriptionsofthe
featurescanbefoundinourreplicationpackage[46].
3.3 ModelDesign
Configurationfeaturesreflecttheenvironmentalconfigurations
ofthemicroserviceinstance.Resourcefeaturesreflecttheresource MEPFLsupportsfourpredictionmodels,whichallowustocom-
consumptions(e.g.,memoryandCPU)ofthemicroserviceinstance binebothtrace-levelandmicroservice-levelprediction.Trace-level
anditsresidingnode.Thesefeaturesmayberelevanttothevalidity predictionincludeslatenterrorprediction,faultymicroservicepre-
ofmicroserviceconfigurations.Volumesupport,whichenablesthe diction,andfaulttypeprediction,eachsupportedbyaprediction
microservicetoaccessthepersistentdataofthenode,mayalsobe model(i.e.,theLEmodel,FMmodel,andFTmodel).Microservice-
relevanttomulti-instancefaults. levelpredictionincludesamicroservice-statuspredictionmodel(in
Instance features reflect the status of the deployment of the shortasanMSmodel).
instancesofthemicroserviceandtheirinvolvementinthecurrent Trace-levelpredictionmodelsaredefinedontrace-levelfeatures.
traceinstance.Thesefeaturesmayberelevanttomulti-instance Thesemodelsincorporateapplication-specificmicroservicesand
problems. theirinteractionsintheirfeaturedefinitions,andthuscanutilize
Interactionfeaturesreflectthestatusofinteractions(especially application-specificcontextinthepredictionwhensimilartrace
asynchronousinteractions)withothermicroservices.Amongthese instances(e.g.,traceinstancesthatsharecommonmicroservices
features,ETandRSCreflectthestatusofthecurrentmicroservice withthecurrenttraceinstance)havebeenincludedinthetrain-
invocationitself;AITandCEOreflectthestatusofasynchronous ingcorpus.Themicroservice-levelpredictionmodel,ontheother
invocationstoothermicroservices.Forexample,forA1inFigure2, hand,isdefinedonmicroservice-levelfeaturesinanapplication-
theETandRSCfeaturesreflecttheexecutiontimeandresponse independentway,andthusgeneralizesacrossdifferentapplications.
codeofA1itself;theAITandCEOfeaturesreflectthestatusofthe Allthefourpredictionmodelsareclassificationmodels.The
invocations(whichareasynchronousinvocations)fromA1toD1, threetrace-levelmodelstreatthegiventraceinstanceasawhole.
E1,andF1.Toprovideaunifiedencodingfordifferentmicroservices, TheLEmodelisabinary-classificationmodelthatclassifiesthe
686

LatentErrorPredictionandFaultLocalizationforMicroserviceApplications ESEC/FSE’19,August26–30,2019,Tallinn,Estonia
Table2:FeatureDefinition
| Category Feature |                                                                           | Description | Scope      |
| ---------------- | ------------------------------------------------------------------------- | ----------- | ---------- |
| ML               | memorylimitofthecurrentmicroservicerelativetothenodememorylimit           |             | Invocation |
| Configuration CL | CPUlimitofthecurrentmicroservicerelativetothenodeCPUlimit                 |             | Invocation |
| VS               | whethervolumesupportisenabledforthecurrentmicroservice                    |             | Global     |
| MC               | memoryconsumptionofthecurrentmicroserviceinstancerelativetoitsmemorylimit |             | Invocation |
| CC               | CPUconsumptionofthecurrentmicroserviceinstancerelativetoitsCPUlimit       |             | Invocation |
Resource
| NMC             | memoryconsumptionofthecurrentnoderelativetoitsmemorylimit                                    |     | Invocation |
| --------------- | -------------------------------------------------------------------------------------------- | --- | ---------- |
| NCC             | CPUconsumptionofthecurrentnoderelativetoitsCPUlimit                                          |     | Invocation |
| IN              | numberofinstancesforthecurrentmicroserviceinthewholesystem                                   |     | Global     |
| IIN             | numberofinstances(forthecurrentmicroservice)invokedinthecurrenttraceinstance                 |     | Trace      |
| SVA             | ratioofthesharedvariablesthatareaccessedinthecurrentinvocation                               |     | Invocation |
| CA              | whetherthecacheisaccessedinthecurrentinvocation                                              |     | Invocation |
| Instance SA     | whetherthethird-partystorage(e.g.,database)isaccessedinthecurrentinvocation                  |     | Invocation |
| TN              | numberofthreadsofthecurrentmicroserviceinstance                                              |     | Invocation |
| LT              | lifetimeofthecurrentmicroserviceinstancesinceitscreation                                     |     | Invocation |
| NIN             | numberofmicroserviceinstancesresidinginthecurrentnode                                        |     | Invocation |
| NMN             | numberofmicroserviceswhoseinstancesresideinthecurrentnode                                    |     | Invocation |
| ET              | executiontimeofthecurrentmicroserviceinvocation                                              |     | Invocation |
| Interaction RSC | HTTPresponsestatuscodeofthecurrentmicroserviceinvocation                                     |     | Invocation |
| AIT             | timeofanasynchronousinvocationinthecurrentmicroserviceexecution                              |     | Invocation |
| CEO             | whethertheexecutionorderofapairofasynchronousinvocationsisconsistentwiththeirinvocationorder |     | Invocation |
traceinstanceintotwoclasses(witherrorornot);theFMmodel
isamulti-labelclassificationmodelthatpredictsoneormultiple
microservicesinthetraceinstancetobefaulty;andtheFTmodel
isamulti-labelclassificationmodelthatpredictsoneormultiple
faulttypes.Themicroservice-levelmodeltreatsthemicroservices
involvedinthegiventraceinstanceindividually.TheMSmodelisa
single-labelclassificationmodelthatpredictsanerrorstatus,which
canbeoneofthethreefaulttypesoraspecialtype“NoFault”. Figure3:ApproachOverview
4.1 FaultInjection
Faultinjectionproducesaseriesoffaultyversionsofthetarget
4 APPROACH
microserviceapplicationbyintroducingdifferenttypesoffaults
Figure3providesanoverviewofMEPFL,whichincludesanoffline intodifferentpartsoftheapplication.Foreachfaultyversion,we
trainingphaseandanonlinepredictionphase.Theofflinetraining injectaspecifictypeoffaultintoaspecificmicroserviceinasemi-
phaseexecutesthetargetmicroserviceapplicationinthetestingen- automaticway.Wedesignafaultinjectionstrategyforeachtypeof
vironmentandtrainsthepredictionmodelsbasedonthecollected fault.Eachfaultinjectionstrategyisparameterizedwiththefollow-
tracelogs.Totrainthemodels,weneednotonlytracelogsunder inginformation:(1)apreconditionthatspecifiestheconditionsto
successfulexecutionsbutalsotracelogsundererroneousexecu- bemetbythelocationofamicroservicewherethefaultisinjected;
tions.Therefore,wedesignaseriesoffaultinjectionstrategiesto (2)acodetransformationmethodthatspecifieshowtogener-
systematicallyobtainaseriesoffaultyversionsoftheapplication. ateapatchtotransformamicroserviceintoafaultyone;(3)an
Weuseexistingautomatedtestcasestodrivetheapplicationandits expectedfailuresymptomthatspecifiestheexpectedsymptom
faultyversionstoexecuteandproducetracelogs.Thesetestcases iftheinjectedfaulthascausedafailure.
simulateuserrequestsfromtheclients(e.g.,browsersandmobile Wenextpresentdetailsoftheparametersforeachfaulttype.
apps)andtriggermicroserviceinvocationchains.Toensurethe Multi-InstanceFaults.Thepreconditionisthatthemicroser-
diversityoftraces,anadditionalcontrolisimposedontheruntime viceaccessesthird-partycachedatabasessuchasRedis[44].The
environmenttomaketheapplicationexecutedunderdifferentset- codetransformationmethodistoreplacethedataaccessestothird-
tings.Wethenprepareatrainingcorpusforthepredictionmodels partycachedatabaseswithdataaccessestoglobalvariablesorlocal
bycollectingandanalyzingtracelogsfromtheexecutions.Foreach cache.Asmulti-instancefaultsusuallycauseincorrectdataaccesses,
traceinstance,weautomaticallyconstructatrace-leveltraining theexpectedfailuresymptomincludesinjectedfailureresponse,
sampleandasetofmicroservice-leveltrainingsamplesbyfeature incorrectoutput,orvariousassertionfailuresorexceptions(e.g.,
extractionanderror/faultlabeling.Basedonthetrainingcorpus,we nullpointerexceptions).
usemachinelearningtechniques(e.g.,RandomForests,K-Nearest ConfigurationFaults.Configurationfaultsareusuallyrelated
Neighbors,Multi-LayerPerceptron)totrainthreepredictionmod- toconsumptionofvariousresources(e.g.,memoryandCPU)and
elsthatcanpredictforeachtracewhetheralatenterroroccurs, irrelevanttothebusinesslogicsofmicroservices.Therefore,con-
whichmicroservicethefaultresidesin,andwhattypeoffaultitis, figurationfaultscanbeinjectedintoanypartofanymicroservice.
respectively. Thecodetransformationmethodistoinjectresource-intensive
Theonlinepredictionphasemonitorstheexecutionoftheap- codeintotargetlocationsofmicroservices,e.g.,memory-intensive
plicationintheproductionenvironmentandpredictslatenterrors codethatloadsalotofdataintomemoryorcomputing-intensive
andfaultlocations(faultymicroservicesandfaulttypes).Itcontinu- codethatincludesalotofiterations.Theexpectedfailuresymp-
ouslycollectsandanalyzestracelogsfromtherunningapplication. tomincludesmicroserviceinstancerestarted,timeoutexception,
Foreachtraceinstance,itextractsfeaturesinasimilarwaytowhat orresource-consumption-relatedexceptions(e.g.,out-of-memory
hasbeendoneinpreparingthetrainingcorpus,andthenusesthe exceptions).
predictionmodelstopredictwhetheralatenterroroccurs,which AsynchronousInteractionFaults.Thepreconditionforasyn-
microservicethefaultresidesin,andwhattypeoffaultitis. chronousinteractionfaultsisthatthemicroserviceinvokesmultiple
687

ESEC/FSE’19,August26–30,2019,Tallinn,Estonia XiangZhou,XinPeng,TaoXie,JunSun,ChaoJi,DeweiLiu,QilinXiang,andChuanHe
faultymicroserviceforagivennumber(e.g.,10)oftimestoget
multipletrace instancesunderthesame setting.The automatic
deployment,executionmanipulation,andtracelogcollectionare
implementedbasedontheinfrastructuresupportofcontaineror-
chestratorandservicemesh(seeSection5).
Forafaultyversionwithaninjectedmulti-instancefault,the
controllermanipulatesthenumberofinstancesofthefaultymi-
croservice.Thecontrollerexecutesthefaultymicroservicewith1to
agivennumber(e.g.,10)ofinstanceswhiletheothermicroservices
runningwiththedefaultnumbersofinstances.
Forafaultyversionwithaninjectedconfigurationfault,thecon-
trollermanipulatestheenvironmentalconfigurations(e.g.,memory
limit,CPUlimit)ofthefaultymicroservice,e.g.,withthemem-
orylimitorCPUlimitincreasedfrom1%to10%,whiletheother
microservicesrunningwithdefaultconfigurations.
Forafaultyversionwithaninjectedasynchronousinteraction
fault,thecontrollermanipulatestheexecutionsequencesofasyn-
chronousinvocations.Thecontrollercausesthemicroservicesthat
Figure4:InjectionofAsynchronousInteractionFault areasynchronouslyinvokedbythefaultymicroservicetobeex-
microservicesinsuccession.Thecodetransformationmethodisto ecutedindifferentorders.Forexample,foramicroserviceAthat
introducedatadependenciesbetweendifferentmicroserviceinvoca- asynchronouslyinvokesthreemicroservicesB,C,andD inthat
tions.Iftheinvocationsaresynchronous,weneedtofirsttransform order,thecontrollerfirstforcestheinvokedmicroservicestobeex-
themintoasynchronousones.Theexpectedfailuresymptomin- ecutedinthesameorderofinvocation(i.e.,B,C,D)andthenforces
cludesinjectedfailureresponse,orvariousassertionfailuresor themtobeexecutedinotherorders(e.g.,D,C,B).Asthemicroser-
exceptions(e.g.,null-pointerexceptions). vicesthatareasynchronouslyinvokedbyamicroserviceinatrace
Figure4showsanexampleofinjectinganasynchronousinter- instanceareusuallynotsomany(e.g.,fewerthan6),thecontroller
actionfault,wheretheredcodeisintroducedforfaultinjection. cantrydifferentexecutionorderstoachievecertaincoverage,e.g.,
Thisexampleincludestwosynchronousmicroserviceinvocations. coveringallthepartialordersofanypairofmicroservices.
Thecodetransformationchangestheinvocationstoasynchronous Duringtheexecutionsoftheapplicationanditsfaultyversions,
onesusingJavaCompletableFutureandintroducesobjects(crList thecontrollercontinuallycollectsthetracelogs.Toprovidethe
andcoList)tostorethereturnvalues.Itintroducesadatadepen- featuresrequiredbythepredictionmodels,thetracelogsrecord
dencybetweenthetwoasynchronousinvocationsviathevariable notonlythesequenceofthespans(i.e.,microserviceinvocations)
checkResult.Duetothedependency,theprogramcanenteranun- ofeachtraceinstance,butalsotheenvironmentalconfigurations,
expectedstateifthetwoinvokedmicroservicesareexecutedina resourceconsumptions,andnumberoftheinstancesoftheinvolved
differentorder. microservices.
Toinjectafaultofaspecifictypeintothetargetapplication,
wefirstidentifyalocation(intheapplication)thatsatisfiesthe
preconditionandusethecodetransformationmethodtointroduce 4.3 PreparationofTrainingCorpus
afaultatthelocation.Thenwecheckwhethertheresultingfaulty Foreachtraceinstance,wegenerateatrace-leveltrainingsample
microservicecanbesuccessfullycompiledandifnotwemanually byextractingtrace-levelfeaturesandlabelingitserrorstatus,fault
repairthecompilationproblem.Afterthat,wefurtherverifythe type, and fault location. For each microservice involved in the
fault injection result by executing the corresponding test cases traceinstance,wegenerateamicroservice-leveltrainingsampleby
multipletimes(e.g.,30times).Asthefailurescausedbythesefaults extractingmicroservice-levelfeaturesandlabelingitsfaultstatus.
areprobabilistic,thefaultinjectionisregardedtobesuccessfulifthe Weextractthefeaturesbasedonthefeaturedefinitionsgivenin
expectedfailuresymptomisobservedinoneoftheexecutions.Each Section3.2.Wefirstextractmicroservice-levelfeaturesbasedon
successfullyinjectedfaultisincorporatedintothetargetapplication thespansincludedinthetraceinstance,andthenaggregatethese
toproduceafaultyversion. microservice-levelfeaturesintotrace-levelfeatures.
Theerrorstatusofatraceinstancecanbe0or1.0indicates
4.2 ExecutionControl
thatthetraceinstancehasalatenterrorcausedbyoneofthethree
Theexecutioncontrollerautomaticallydeploysthetargetapplica- typesoffaults,and1indicatestheothercases.Notethattheother
tionanditsfaultyversions,executesdifferentapplicationversions casesincludethatthetraceinstancehasnoerrorsorhasother
withexistingautomatedtestcases,andcollectstracelogs.Forfaulty unknownerrors(e.g.,errorscausedbymonolithicfaults).Wela-
versions,thecontrollerfurthermanipulatestheruntimeenviron- beltheerrorstatusofatraceinstanceas0ifthefollowingfour
mentoftheapplicationsothatitisexecutedunderdifferentsettings, conditionsaresatisfied.First,theresultofthetraceinstanceisnot
includingdifferentnumbersofmicroserviceinstances,environmen- consistentwiththeexpectedresultinthetestcase.Second,the
talconfigurations,andasynchronousinteractionsequences.For traceinstanceisproducedbyafaultyversionoftheapplication,
eachsetting,thecontrollerexecutesthetestcasesinvolvingthe andthefaultymicroserviceisincludedinthetraceinstance.Third,
688

LatentErrorPredictionandFaultLocalizationforMicroserviceApplications ESEC/FSE’19,August26–30,2019,Tallinn,Estonia
thetraceinstanceisproducedinafaultysetting,i.e.,foramulti-
instancefault,thefaultymicroservicehasmorethanoneinstance;
foraconfigurationfault,thefaultymicroservicerunswithresource
limits(e.g.,memoryorCPUlimit);foranasynchronousinteraction
Figure5:MEPFLPredictionProcess
fault,theexecutionorderofthemicroservicesasynchronouslyin-
vokedbythefaultymicroserviceisnotthesameastheirinvocation • K-NearestNeighbors(KNN):anon-parametricclassification
order.Fourth,theerrorisnotcausedbymonolithicfaults.Tocheck techniquethatdeterminestheclassofanobjectbyaplurality
whetherthefourthconditionissatisfied,weautomaticallydeploy voteofitsneighbors.
thesameapplicationversioninamonolithicenvironmentandrun • Multi-LayerPerceptron(MLP):afeed-forwardartificialneu-
thesametestcase;ifthetestcasepasses,weconcludethattheerror ralnetworkmodelthatmapsasetofinputdataontoaset
isnotcausedbymonolithicfaults. ofappropriateoutputs.
If the trace error status is 1, we label the error status of the
Tooptimizetheseclassificationmodels,weusethegridsearch
correspondingtrace-leveltrainingsampleas1andthefaultstatus
techniquetosearchthehyper-parameter(e.g.,“hidden_layer_sizes”
ofeachmicroservice-leveltrainingsampleto“NoFault”.
forMLP)spaceforthebestcross-validationscore.Thetechnique
If the trace error status is 0, we label the error status of the
exhaustivelygeneratescandidatesfromagridofparameterval-
correspondingtrace-leveltrainingsampleto0,itsfaulttypetothe
uesspecifiedwithsomeinitialparameters,andthenscansallthe
injectedfaulttype,anditsfaultlocationtothefaultymicroservice.
possiblecombinationstofindthebestcross-validationscore.
Foreachmicroservice-leveltrainingsample,welabelitsfaultstatus
totheinjectedfaulttypeifithasaninjectedfaultand“NoFault”if
4.5 FeatureExtractionandPrediction
ithasnoinjectedfault.
Theonlinepredictionphaseincludestwosteps.Thefeatureex-
tractionstepextractsmicroservice-andtrace-levelfeaturesfrom
4.4 Training
tracelogs.Thepredictionstepusesthepredictionmodelstopredict
Toselectrelevantfeaturesforthetraining,weconductacorrelation latenterrors,faultlocations,andtypes.
analysisbetweentheerrorscausedbythethreetypesoffaultsand Figure5showsthepredictionprocess,whichcombinesthetrace-
thecandidatefeatures(seeTable2)basedonTrainTicket[36].For andmicroservice-levelpredictionmodels.Givenatraceinstance
eachtracetype,weusethecorrespondingtestcasestorunthe capturedonline,MEPFLfirstusestheLEmodeltopredictwhether
originalapplicationanditsfaultyversionswithdifferenttypesof thetraceinstancehaslatenterrorsanddetermineswhethertrace-
injectedfaults1,000times.Duringtheprocess,wemanipulatethe levelpredictionhastherequiredconfidencelevel(obtainedalong
runningsystemsothatitisexecutedwithdifferentsettings(e.g.,the withthepredictionfromtheLEmodel).Iftheconfidenceisnot
numbersofinstances,environmentalconfigurations,andexecution lowerthanapredefinedthreshold,MEPFLusestheFMmodeland
ordersofasynchronousinvocations). theFTmodeltopredictthefaultymicroservicesandthefaulttypes,
Table3liststhePearsoncorrelationcoefficient[8]betweenthe respectively.Otherwise,MEPFLusestheMSmodeltopredictlatent
errorscausedbydifferenttypesoffaultsandthecandidatefeatures errors,faultlocations,andtypes.NotethattheMSmodelpredicts
forfivetracetypes.Thecompletecorrelationanalysisresultscan thefaultstatusofeachmicroserviceinvolvedinthegiventracein-
befoundinourreplicationpackage[46].Wechoosethefeatures stance.Ifanymicroserviceispredictedtobefaulty,MEPFLregards
whosecorrelationcoefficientsarehigherthan0.3foratleastone thetraceinstanceaserroneousandallthefaultymicroservices
faulttypeandonetracetype.Basedonthecriterion,weselectallthe togetherwiththeirfaulttypesastheresultsoffaultlocationand
candidatefeaturesexceptVS,SA,LT,NMNandtheircorresponding typeprediction.
trace-levelfeaturesforthetraining.
Beforetrainingthepredictionmodels,wefollowastandardpro- 5 IMPLEMENTATION
cesstopreprocessthetrainingdata,includingimputation,category
Ourimplementationincludesfourmajorcomponents:thefault
encoding,discretization,andfeaturescaling.Imputationreplaces
injector,executioncontroller,logprocessor,andpredictor.
missingdatainthetrainingsampleswithtypicalvalues,i.e.,the
ThefaultinjectorcurrentlysupportsthefaultinjectionofJava
meansforcontinuousvaluesandthemostfrequentvaluesforother
microservices.ItusesJavaParser3.8[27]toparseandmanipulate
kindsofvalues.Categoryencodingtransformscategorizationval-
thesourcecodeofmicroservicestoimplementfaultinjection.Other
ues(e.g.,RSC)intointegervaluesfrom0toN-1(N isthenumber
parserscanbeintroducedinthefuturetosupportfaultinjectionof
ofcategoriesofafeature).Discretizationtransformscontinuous
microservicesimplementedinotherlanguages.
values(e.g.,TN)intointegervaluesfrom0toK-1bydividingthe
TheexecutioncontrollerintegratesTestNG6.8[51]toimple-
rangeofthevaluesintoK partitions.Featurescalingnormalizes
ment automated scheduling and execution of test cases. At the
therangesoffeaturevaluesinto[0,1].
systeminfrastructurelevel,theexecutioncontrollerintegratesKu-
Wechoosethefollowingthreemachinelearningtechniquesto
bernetes1.10andIstio1.0toimplementautomaticmicroservice
trainthepredictionmodels.
applicationdeployment,configuration,andruntimemanipulation
• RandomForests(RF):anensemblelearningtechniquefor intheofflinetraining.ItusesKubernetesRESTAPIstodynami-
classificationthatconstructsamultitudeofdecisiontreesat callydeploymicroserviceapplicationsandmanagemicroservice
trainingtimeandoutputstheclassthatisthemodeofthe instancesandtheirenvironmentalconfigurations.Itcustomizesthe
classes(classification)oftheindividualtrees. Istioimplementationtocontroltheexecution/returningsequences
689

ESEC/FSE’19,August26–30,2019,Tallinn,Estonia XiangZhou,XinPeng,TaoXie,JunSun,ChaoJi,DeweiLiu,QilinXiang,andChuanHe
Table3:ThePearsonCorrelationCoefficientofMicroserviceLevelFeaturesandLatentErrors
Features Configuration Resource Instance Interaction
TraceTypes ML CL VS MC CC NMC NCC IN IIN SVA CA SA TN LT NIN NMN ET RSC AIT CEO
Instance 0.02 0.12 0.22 0.36 0.12 0.19 0.09 0.83 0.63 0.67 0.78 0.22 0.39 0.05 0.19 0.03 0.58 0.05 0.17 0.23
TraceType1 Config 0.61 0.20 0.11 0.77 0.36 0.46 0.42 0.12 0.03 0.11 0.21 0.25 0.25 0.12 0.15 0.05 0.65 0.43 0.34 0.16
Interaction 0.10 0.22 0.03 0.01 0.18 0.06 0.13 0.07 0.14 0.45 0.12 0.03 0.54 0.16 0.09 0.11 0.70 0.47 0.62 0.79
Instance 0.04 0.09 0.27 0.23 0.05 0.23 0.12 0.79 0.46 0.73 0.66 0.06 0.62 0.15 0.12 0.11 0.54 0.46 0.16 0.14
TraceType2 Config 0.23 0.67 0.20 0.33 0.76 0.48 0.25 0.03 0.23 0.22 0.12 0.03 0.34 0.14 0.15 0.04 0.32 0.66 0.45 0.17
Interaction 0.22 0.18 0.13 0.21 0.13 0.02 0.01 0.16 0.11 0.36 0.46 0.18 0.59 0.07 0.63 0.03 0.47 0.21 0.66 0.68
Instance 0.03 0.17 0.18 0.15 0.11 0.14 0.02 0.87 0.90 0.56 0.78 0.23 0.17 0.17 0.42 0.14 0.46 0.31 0.10 0.19
TraceType3 Config 0.70 0.13 0.13 0.83 0.46 0.36 0.12 0.02 0.22 0.19 0.09 0.12 0.20 0.02 0.14 0.09 0.33 0.45 0.29 0.21
Interaction 0.01 0.09 0.09 0.15 0.03 0.07 0.10 0.04 0.13 0.23 0.33 0.16 0.13 0.11 0.23 0.03 0.45 0.29 0.79 0.72
Instance 0.10 0.10 0.15 0.22 0.04 0.05 0.10 0.69 0.36 0.77 0.66 0.11 0.33 0.01 0.17 0.08 0.28 0.60 0.11 0.23
TraceType4 Config 0.39 0.74 0.19 0.67 0.71 0.49 0.18 0.06 0.33 0.10 0.12 0.24 0.01 0.11 0.23 0.03 0.39 0.17 0.15 0.28
Interaction 0.14 0.21 0.21 0.17 0.11 0.03 0.14 0.11 0.12 0.33 0.43 0.13 0.32 0.09 0.12 0.04 0.50 0.25 0.73 0.47
Instance 0.13 0.07 0.07 0.20 0.12 0.11 0.09 0.70 0.87 0.60 0.56 0.24 0.35 0.03 0.33 0.05 0.21 0.19 0.08 0.12
TraceType5 Config 0.60 0.16 0.22 0.71 0.66 0.63 0.24 0.03 0.21 0.14 0.23 0.23 0.09 0.05 0.08 0.15 0.46 0.30 0.47 0.15
Interaction 0.05 0.09 0.03 0.36 0.16 0.15 0.08 0.09 0.26 0.13 0.22 0.12 0.41 0.16 0.06 0.09 0.36 0.61 0.54 0.63
ofsynchronousmicroserviceinvocationsbasedonitssidecar.Istio inject142faults(including46multi-instancefaults,52configuration
sidecarisakindofintelligentproxiesthatmediateandcontrolthe faults,and44asynchronousinteractionfaults)into86tracetypes.
networkcommunicationbetweenmicroservices[25]. Weobtain1,214,637traceinstances,211,347(17.4%)ofwhichhave
ThelogprocessorusesKubernetesandIstiotocapturetrace latenterrors.Thefaultinjectionprocessisautomated.Butwhen
logs.Tocaptureinformationaboutvariableaccessesrequiredby theinjectedfaultscausecompilationfailureorthetestsfailinunex-
some features such as SVA and CA, we use JDK to capture the pectedways,developersarerequiredtomanuallyanalyze/editcode.
runtimeJVMthreaddumpandheapdump,andanalyzethecall Amongthe174faultsinjectedintothetwoapplications,71.84%
stackandvariablevaluesinthedumps.Thelogprocessorincludes areinjectedautomaticallywithouthumanefforts;28.16%involve
apipelinetocollectandprocesstracelogs.Thepipelinerunsa humanefforts.
RESTfulservicebasedonSpringBoot1.5.9[50]tocollectdistributed Foreachapplication,werandomlydividethetraceinstances
logdataproducedbyIstioandusesKafka2.0.0[28]tostreamthe equallyinto5subsetsandperform5-foldcross-validationtoeval-
logdata.ItthenusesSpark2.3.2[49]toprocessthedatatoproduce uatetheaccuracy.Ineverycross-validation,weuse4subsetsas
trainingsamplesandusesHDFS(HadoopDistributedFileSystem) training data and the remaining subset as testing data. For the
2.7[22]tostoretheprocesseddata. predictionoflatenterrors,weevaluatetherecall,precision,and
Weimplementthepredictorbasedonscikit-learn[47],amachine F1-measure(theharmonicmeanofprecisionandrecall)ofiden-
learninglibraryforPython.Thethresholdoftheconfidencescore tifyingtraceinstancesthathavelatenterrors.Asthenumberof
foradoptingthetrace-levelpredictionis70%. successfultraceinstancesismuchlargerthanthatoferroneous
ones,wealsoevaluatethefalsepositiverate(FPR),i.e.,therate
6 EVALUATION oferror-freetracesthatarepredictedtobeerroneousamongall
thesuccessfultraces.Forthepredictionoffaultymicroservices,we
To evaluate the effectiveness of MEPFL, we conduct a series of
evaluatetheTop-k (withk being1,3,5)accuracyofidentifying
experimentalstudiestoanswerthefollowingresearchquestions.
afaultymicroservicefromanerroneoustraceinstance,i.e.,the
• RQ1:HowaccurateisMEPFLinpredictinglatenterrors,
probabilitythatthefaultymicroserviceisincludedintheTop-k
faultymicroservices,andfaulttypesofmicroserviceappli-
predictionresults.Forthepredictionoffaulttypes,weevaluate
cations?
therecall,precision,andF1-measureofthepredictedfaulttypesof
• RQ2:Howdoesthetrainingcoverageoftracetypesinflu-
erroneoustraceinstances.
encethepredictionaccuracy?
Toourbestknowledge,therearenoexistingapproachesoftrace-
• RQ3: How effective is MEPFL when it is used to predict
log-basederrorpredictionorfaultlocalizationformicroservice
latenterrorscausedbyrealfaultcases?
applications.Therefore,wecompareMEPFLwithastate-of-the-
Thesestudiesarebasedontwoopen-sourcemicroserviceap- artapproach[40]fortrace-basedfailurediagnosisindistributed
plications:SockShop[48]andTrainTicket[36].SockShopisa systems.Theapproachusesfaultinjectiontopopulatethedatabase
small-scalebenchmarkapplicationthatiswidelyusedinmicroser- offailuresforatargetdistributedsystemandlocatetherootcauses
viceresearch[13,31,43].Ithas8microservicesand10tracetypes. ofreportedfailuresbymatchingagainstthefailuresinthedatabase.
TrainTicketisamedium-scalebenchmarkapplicationthathasbeen Inthisstudy,weusethetraceinstancesinthetrainingdataasthe
recentlyreleased,having40microservicesand86tracetypes.It failuredatabasefortheapproachtoidentifythefaultymicroservices
replicatesavarietyoffaultsbasedonastudyofindustrialfault andfaulttypes.Notethatthisstate-of-the-artapproachcannot
casesinmicroserviceapplications.Allthestudiesareconducted identifylatenterrors,asitassumesthatfailurescanbereported
onaprivatecloudwith20virtualmachines. fromtheproductionenvironment.ForMEPFL,weevaluatethree
versions,each withadifferentmachinelearning technique,i.e.,
6.1 PredictionAccuracy(RQ1)
MEPFL-RF,MEPFL-KNN,andMEPFL-MLP.
ToanswerRQ1,weevaluatetheaccuracyofMEPFLusingacorpus Table4showstheaccuracyofintra-applicationerrorprediction
oftracelogswithautomaticallyinjectedfaults.ForSockShop,we and fault localization. It can be seen that for both applications
inject32faults(including10multi-instancefaults,10configuration MEPFL achieves very high accuracy in the prediction of latent
faults,and12asynchronousinteractionfaults)into10tracetypes. errors,faultymicroservices,andfaulttypes.Inparticular,MEPFL-
Weobtain243,606traceinstancesbytest-drivenautomaticexecu- MLPperformsthebest.MEPFL-MLPpredictslatenterrorswitha
tion,32,643(13.4%)ofwhichhavelatenterrors.ForTrainTicket,we recallof0.982(0.896),aprecisionof0.998(0.995),andafalsepositive
690

LatentErrorPredictionandFaultLocalizationforMicroserviceApplications ESEC/FSE’19,August26–30,2019,Tallinn,Estonia
Table4:AccuracyofIntra-ApplicationErrorPredictionandFaultLocalization
SockShop TrainTicket
Methods LatentError FaultyMicroservice FaultType LatentError FaultyMicroservice FaultType
Recall Precision F1 FPR Top1 Top3 Top5 Recall Precision F1 Recall Precision F1 FPR Top1 Top3 Top5 Recall Precision F1
MEPFL-RF 0.949 0.997 0.973 0.015 0.864 0.943 1.000 0.926 0.863 0.893 0.801 0.979 0.881 0.041 0.924 0.934 0.938 0.862 0.986 0.921
MEPFL-KNN 0.961 0.997 0.978 0.013 0.891 0.965 1.000 0.967 0.925 0.946 0.865 0.993 0.924 0.030 0.923 0.938 0.940 0.892 0.978 0.933
MEPFL-MLP 0.982 0.998 0.990 0.009 0.933 0.972 1.000 0.952 0.983 0.967 0.896 0.995 0.943 0.014 0.937 0.939 0.939 0.930 0.986 0.957
Approachin[40] N/A N/A N/A N/A 0.340 0.748 1.000 0.618 0.375 0.467 N/A N/A N/A N/A 0.117 0.189 0.263 0.614 0.794 0.692
rate0.009(0.014),faultymicroserviceswithaTop-1accuracyof possibleexplanationforthetrendisthatwiththeincreaseoftrace
0.933(0.937),andfaulttypeswitharecallof0.952(0.930)anda typecoverage,itismorelikelytofindsimilartraceinstancesinthe
precisionof0.983(0.986)forSockShop(TrainTicket).Theoverall trainingdata.Withtheincreaseoftracetypecoverage,thetraining
predictionaccuracyofSockShopisslightlyhigherthanthatof timelinearlyincreasesfrom8m37sto35m35s,whiletheprediction
TrainTicket.ThisresultmaybeexplainedbythefactthatSockShop timekeepsstable.
hasmuchfewermicroservicesandtracetypes.Forbothapplications,
MEPFLsubstantiallyoutperformsthestate-of-the-artapproach[40] 6.3 EffectivenessforRealFaultCases(RQ3)
inpredictingfaultymicroservicesandfaulttypes.
The purpose of this evaluation is to assess the effectiveness of
WealsoevaluatetheaccuracyofMEPFLforcross-application
MEPFLforreal-worldmicroservicefaults.Tothisend,weeval-
latenterrorpredictionandfaultlocalization.Inthisevaluation,we
uatetheaccuracyofMEPFLforthefaultcases[10]providedby
usethetraceinstancesofanapplication(SockShoporTrainTicket)
theTrainTicketbenchmark.Thesefaultcasesarereplicatedfrom
astrainingdataandthetraceinstancesoftheotherapplicationas
industrialfaultcasesbytransferringthefaultmechanismsfromthe
testingdata.Notethatthestate-of-the-artapproach[40]cannot
originalapplicationstothebenchmarkapplication.From22fault
beusedforcross-applicationprediction,asitreliesonthetrace
cases,wechoosethe10faultcasesthatbelongtothethreefault
instancesofthesameapplicationformatching.ForMEPFL,only
typesfortheevaluation.
themicroservice-levelpredictionworksforthisprediction.
Weusethetraceinstancesproducedwithinjectedfaultstotrain
Table5showstheaccuracyofcross-applicationerrorprediction
thepredictionmodelsusingMEPFL-MLP,andapplythemodels
and fault localization. It can be seen that the accuracy is much
onthe10faultcases.Foreachfaultcase,weapplythepatchinto
lowerthanthatofintra-applicationprediction.Forexample,for
theapplicationtoproduceafaultyversionandthendeploythe
MEPFL-MLP,therecall/precisionoflatenterrorpredictiondrop
version.Fivestudentvolunteersplaytheroleofusersandmanually
from 0.982/0.998 and 0.896/0.995 to 0.451/0.562 and 0.461/0.418.
executethescenariosthatmayinvolvethetargetmicroservice.For
UsingTrainTicketdatatopredictSockShophasahigheraccuracy
eachexecution,wemanuallycheckthesystemlogsandexecution
thanpredictingtheotherwayaround.Thisresultmaybeexplained
resultstoconfirmwhetheritinvolvesalatenterrorandwhether
bythefactthatTrainTickethasmuchmoremicroservicesandtrace
theerroriscausedbythefaultcase.
typesthanSockShop.
Wecollectalltheproducedtraceinstancesandapplythepre-
6.2 InfluenceofTraceTypeCoverage(RQ2) dictionmodelsoneachtraceinstance.Theevaluationresultsare
showninTable7.Foreachfaultcase,weprovidethefaulttype
Faultinjectionandtracecollectioncosttimeandeffort.Therefore,
(Multi-Instance,Configuration,orAsynchronousInteraction),the
apracticalproblemishowtodecidewhetherenoughtrainingdata
numbersoftraceinstances(#TR)anderroneousones(#ET),and
havebeencollected,i.e.,whetherthecoverageoftracetypesinthe
theaccuracymetrics.ItcanbeseenthatMEPFLaccuratelypre-
trainingdatasubstantiallyaffectsthepredictionresults.
dictsthelatenterrorscausedbythesefaultcaseswitharecallof
Inthisevaluation,weusethebestmachinelearningtechniquefor
0.647-0.983(0.821onaverage),aprecisionof0.586-0.984(0.891on
MEPFL(i.e.,MEPFL-MLP)andTrainTicketasthetargetapplication
average),andafalsepositiverateof0.016-0.042(0.030onaverage),
asitismuchlargerthanSockShop.Werandomlydividethetrace
thefaultymicroserviceswithaTop-1accuracyof0.291-1.000(0.788
typesofTrainTicketinto10subsetsanduseapartofthetrace
onaverage),andthefaulttypewitharecallof0.676-0.975(0.828
typesfortrainingandtheothersfortesting.Westartwithone
onaverage)andaprecisionof0.648-0.977(0.820onaverage).
subsetfortrainingandgraduallyincreasethenumberofsubsetsfor
Itcanbeseenthatthepredictionaccuracyforconfiguration
training.Foreachsetting,wecalculatetheaccuracyoflatenterror
faults(F3,F4,F5,F7)islowerthantheaccuracyformulti-instance
predictionandfaultlocalizationalongwiththeratethattrace-level
faults(F8,F11,F12)andasynchronousinteractionfaults(F1,F2,
predictionisadopted(T-Rate),andreportthetrainingtime(TT)
F13).Thisresultmaybeduetothatexecutiontracesarelesssensi-
andpredictiontime(PT).
tivetolatenterrorscausedbyconfigurationfaults.Multi-instance
Table6showstheresultsoftheevaluation.Thegeneraltrend
faultsandasynchronousinteractionfaultshavedirectinfluenceson
is that the prediction accuracy substantially increases with the
executiontraces,e.g.,involvedmicroserviceinstances,interaction
increaseoftracetypecoverage.Forexample,when40%ofthetrace
sequences,oraccessesofsharedvariablesandcache.Incontrast,
typesarecoveredbythetrainingdata,therecallandprecisionof
configurationfaultsareusuallyrelatedtoenvironmentalconfigu-
latenterrorprediction,thetop-1accuracyoffaultymicroservice
rationsandresourceconsumption,andhavenodirectinfluences
prediction,andtherecallandprecisionoffaulttypepredictionare
onexecutiontraces.
allhigherthan80%.Withtheincreaseoftracetypecoverage,the
overallpredictionmoreandmorereliesonthetrace-levelprediction.
6.4 ThreatstoValidity
Whenthetracetypecoveragereaches30%,thetrace-levelprediction
dominatestheoverallprediction.Whenthecoveragereaches90%, Therearethreemajorthreatstotheinternalvalidityofthestudies.
81.3%ofthepredictionismadebythetrace-levelprediction.A The first one lies in the correctness of fault injection and trace
691

ESEC/FSE’19,August26–30,2019,Tallinn,Estonia XiangZhou,XinPeng,TaoXie,JunSun,ChaoJi,DeweiLiu,QilinXiang,andChuanHe
Table5:AccuracyofCross-ApplicationErrorPredictionandFaultLocalization
TrainTicketModelPredictingSockShop SockShopModelPredictingTrainTicket
Methods LE FM FT LE FM FT
Recall Precision F1 FPR Top1 Top3 Top5 Recall Precision F1 Recall Precision F1 FPR Top1 Top3 Top5 Recall Precision F1
MEPFL-RF 0.441 0.510 0.473 0.141 0.316 0.771 1.000 0.394 0.623 0.483 0.410 0.419 0.414 0.189 0.304 0.523 0.662 0.346 0.456 0.394
MEPFL-KNN 0.461 0.530 0.493 0.136 0.326 0.856 1.000 0.400 0.628 0.488 0.415 0.463 0.438 0.160 0.325 0.635 0.737 0.358 0.463 0.404
MEPFL-MLP 0.451 0.562 0.501 0.113 0.335 0.872 1.000 0.415 0.627 0.499 0.461 0.418 0.471 0.169 0.332 0.654 0.799 0.365 0.466 0.409
Table6:InfluenceofTraceTypeCoverage etal.[40]proposedanapproachtoautomatingfailurediagnosisin
Coverage TT PT T-Rate Recall Pr L e a c t i e si n o t n Erro F r 1 FPR F T a o u p1 ltyM To ic p r 3 oser T v o i p c 5 e Recall Fa P u re lt ci T si y o p n e F1 distributedsystemsbycombiningfaultinjectionanddataanalytics.
10% 8min37s 12s 0.329 0.771 0.807 0.789 0.084 0.284 0.626 0.822 0.539 0.665 0.595 Comparedtoourwork,theprecedingpreviousapproachesarede-
20% 11min58s 12s 0.403 0.795 0.846 0.820 0.061 0.299 0.627 0.827 0.676 0.890 0.768
30% 14min15s 12s 0.591 0.824 0.916 0.868 0.062 0.688 0.845 0.931 0.810 0.921 0.862 signedfortraditionaldistributedsystemsorcloudsystems,lacking
40% 16min24s 12s 0.655 0.829 0.945 0.884 0.059 0.813 0.905 0.935 0.803 0.960 0.874
50% 19min58s 12s 0.662 0.884 0.951 0.897 0.054 0.873 0.932 0.938 0.856 0.949 0.901 considerationofcomplexenvironmentalfactorsthatareessential
60% 23min39s 12s 0.766 0.858 0.950 0.902 0.044 0.920 0.941 0.944 0.844 0.937 0.888
70% 27min26s 12s 0.797 0.848 0.954 0.898 0.036 0.926 0.943 0.944 0.818 0.976 0.890 inmicroserviceapplications,e.g.,auto-scalingoftheinstancesof
80% 30min42s 12s 0.830 0.857 0.958 0.905 0.032 0.907 0.939 0.943 0.851 0.995 0.917
90% 35min35s 12s 0.813 0.879 0.950 0.913 0.030 0.926 0.937 0.944 0.860 0.974 0.914 eachservice,tremendousasynchronousinteractions.
Table7:EffectivenessforReal-WorldFaultCases Therearepreviousapproachesonfaultanalysisforcloudsys-
FaultCases Type #TR #ET Recall Precisio L n E F1 FPR Top1 T F o M p3 Top5 Recall Pre F c T ision F1 temsbyconsideringthehighcomplexityanddynamismofcloud
F1 AI 306 61 0.983 0.803 0.884 0.033 0.951 1.000 1.000 0.819 0.655 0.728 computing environments. Lin et al. [32] proposed an approach
F2 AI 322 65 0.738 0.984 0.843 0.031 0.907 1.000 1.000 0.815 0.846 0.830
F3 C 310 48 0.667 0.979 0.793 0.042 0.291 1.000 1.000 0.750 0.771 0.760 forpredictingthefailurepronenessofanodeinacloudservice
F4 C 312 37 0.783 0.918 0.845 0.026 0.486 0.513 1.000 0.918 0.972 0.944
F5 C 328 89 0.685 0.977 0.805 0.034 0.977 0.977 1.000 0.943 0.977 0.960 systembasedonhistoricaldata.Pitakratetal.[41]proposedanap-
F7 C 392 34 0.647 0.882 0.746 0.028 0.558 1.000 1.000 0.676 0.823 0.742
F8 MI 343 75 0.960 0.586 0.728 0.041 1.000 1.000 1.000 0.840 0.826 0.833 proachnamedHora,whichcombinescomponentfailurepredictors
F11 MI 328 40 0.975 0.875 0.922 0.024 0.875 0.975 0.975 0.975 0.975 0.975 witharchitecturalknowledge,andpredictsfailurescausedbythree
F12 MI 369 37 0.837 0.918 0.876 0.027 0.837 1.000 1.000 0.702 0.648 0.674
F13 AI 322 64 0.937 0.984 0.960 0.016 1.000 1.000 1.000 0.843 0.703 0.767 representativetypesoffaults:memoryleak,systemoverload,and
Average - 333 55 0.821 0.891 0.854 0.030 0.788 0.947 0.998 0.828 0.820 0.824
suddennodecrash.Ahmedetal.[5]proposedamachinelearning
labeling.Thefaultinjectionimplementedbyautomaticcodetrans-
approachbasedondetectingmetriccorrelationstabilityviolations
formationmayfailtointroduceafaultasexpectedandtheerror
(CSV)forautomatedlocalizationofperformancefaultsfordata-
statusofatraceinstancemaybeincorrectlylabeled.Thesecondone
centerservicesrunningunderdynamicloadconditions.Deanet
liesinunknownproblemswithinthetwobenchmarkapplications.
al.[17]presentedPerfCompass,anonlinedebuggingapproachfor
Theseproblemsmaycauseunexpectederrorsoftheapplications,
performanceanomalyfaults.PerfCompasscanquantifywhether
thusinfluencingtheerrorstatusoftraceinstances.Thethirdone
aproduction-runperformanceanomalyhasaglobalimpactorlo-
liesintheuncertaintiesofautomaticdeploymentandruntimeman-
calimpact.Theprecedingpreviousapproachessharesomesimilar
agement.
ideasasourapproach.However,theseapproachesdonotsupport
Therearetwomajorthreatstotheexternalvalidityofthestudies.
latenterrorpredictionandtheydonotfocusonmicroservices.Al-
Thefirstoneliesinthelimitationoftwotargetapplicationsused
thoughHoracanbeappliedformicroserviceapplications,itisused
inthestudies.SockShopandTrainTicketaremuchsmallerthan
topredictviolationsofexpectedQoSlevelscausedbysystemlevel
complexindustrialmicroserviceapplications.Thesecondoneliesin
faults(e.g.,memoryleak,systemoverload,andsuddennodecrash).
thelimitationofthefaultcasesusedinthestudies.TheTrainTicket
Incontrast,ourapproachistailoredtomicroservicesandpredicts
faultcasesmaybesimplerthanindustrialfaultsandrepresentonly
latenterrorscausedbythreetypesofmicroservicespecificfaults
alimitedpartofdifferenttypesoffaults.Thusitisnotclearwhether
intheimplementationandconfigurationofmicroservices.
theapproachcanbeeffectivelyappliedformuchlargerindustrial
applicationsandmorecomplexfaultcases.
8 CONCLUSION
7 RELATEDWORK Inthispaper,wehaveproposedMEPFL,anapproachforlatenter-
rorpredictionandfaultlocalizationofmicroserviceapplicationsby
Traditionalfaultlocalizationapproachesincludeslice-basedfault
learningfromsystemtracelogs.Itsupportsthreetypesofmicroser-
localization (e.g., [3, 4, 6, 7, 55]), spectrum-based fault localiza-
viceapplicationfaultsthatarespecificallyrelevanttomicroservice
tion(e.g.,[2,18,21,23,29,38,45],faultlocalizationbasedonan-
interactionsandruntimeenvironments,i.e.,multi-instancefaults,
alyzingprogramstates(e.g.,[58–60]),faultlocalizationbasedon
configurationfaults,andasynchronousinteractionfaults.Based
datamining(e.g.,[15,16,39]),andmodel-basedfaultlocalization
onasetoffeaturesdefinedonsystemtracelogs,MEPFLtrains
(e.g.[1,9,19,35]).Inrecentyears,machinelearningtechniqueshave
predictionmodelsatboththetracelevelandmicroservicelevel
beenappliedforfaultlocalizationindifferentsystems[12,14,33,54].
usingthesystemtracelogscollectedfromautomaticexecutions
Theseapproachesfocusontraditionalprogramsandthusarenot
ofthetargetapplicationanditsfaultyversionsproducedbyfault
applicabletomicroservices.Indeedtheseapproachescanbepo-
injection.Ourexperimentalstudieshavedemonstratedtheeffec-
tentiallyappliedtoapplicationfaultsinmicroserviceapplications,
tivenessofMEPFLwithtwoopen-sourcemicroservicebenchmarks
whereasourapproachfocusesonmicroservice-specificfaults.
andreal-worldfaultcases.
Recently,multipleapproachesonfaultlocalizationfordistributed
systemsorcloudnativesystemshavebeenreported.Whittaker
ACKNOWLEDGMENTS
etal.[53]presentedanapproachthatenablesthedevelopersto
reasonaboutthecausesofeventsindistributedsystems.Leonardo ThisworkwassupportedbytheNationalKeyResearchandDevel-
etal.[34]proposedalightweightapproachoffaultlocalizationfor opmentProgramofChinaunderGrantNo.2018YFB1004803,and
cloudsystems.Wangetal.[52]presentedanonlineapproachofin- NSFundergrantsno.CNS-1513939,CNS-1564274,CCF-1816615,
crementalclusteringforfaultlocalizationinwebapplications.Pham andagrantfromFuturewei.
692

LatentErrorPredictionandFaultLocalizationforMicroserviceApplications ESEC/FSE’19,August26–30,2019,Tallinn,Estonia
REFERENCES
|     |     |     |     | [27] Javaparser.Com.2018. Javaparser. RetrievedFebruary21,2018fromhttps: |
| --- | --- | --- | --- | ------------------------------------------------------------------------ |
//javaparser.org/
[1] RuiAbreuandArjanJ.C.vanGemund.2009.ALow-CostApproximateMinimal
HittingSetAlgorithmanditsApplicationtoModel-BasedDiagnosis.InProc.8th [28] Kafka.Com.2018.Kafka. RetrievedFebruary21,2018fromhttp://kafka.apache.
org/
SymposiumonAbstraction,Reformulation,andApproximation.
|     |     |     |     | [29] BogdanKorel.1988.PELAS-ProgramError-LocatingAssistantSystem.IEEE |
| --- | --- | --- | --- | --------------------------------------------------------------------- |
[2] RuiAbreu,PeterZoeteweij,andArjanJ.C.vanGemund.2006.AnEvaluationof
SimilarityCoefficientsforSoftwareFaultLocalization.InProc.12thIEEEPacific Trans.SoftwareEng.14,9(1988),1253–1260.
|     |     |     |     | [30] Kubernetes.Com.2018. Kubernetes. RetrievedFebruary21,2018fromhttps: |
| --- | --- | --- | --- | ------------------------------------------------------------------------ |
RimInternationalSymposiumonDependableComputing.39–46.
| [3] HiralalAgrawal,RichardA.DeMillo,andEugeneH.Spafford.1993.Debugging |     |     |     | //kubernetes.io/                                                         |
| ---------------------------------------------------------------------- | --- | --- | --- | ------------------------------------------------------------------------ |
|                                                                        |     |     |     | [31] JinJinLin,PengfeiChen,andZibinZheng.2018.Microscope:PinpointPerfor- |
withDynamicSlicingandBacktracking.Softw.,Pract.Exper.23,6(1993),589–616.
manceIssueswithCausalGraphsinMicro-serviceEnvironments.InProc.16th
[4] HiralalAgrawalandJosephRobertHorgan.1990.DynamicProgramSlicing.In
Proc.ACMSIGPLANConferenceonProgrammingLanguageDesignandImplemen- InternationalConferenceonService-OrientedComputing.3–20.
|     |     |     |     | [32] QingweiLin,KenHsieh,YingnongDang,HongyuZhang,KaixinSui,YongXu, |
| --- | --- | --- | --- | ------------------------------------------------------------------- |
tation.246–256.
[5] JawwadAhmed,AndreasJohnsson,FarnazMoradi,RafaelPasquini,Christofer Jian-GuangLou,ChenggangLi,YoujiangWu,RandolphYao,MuraliChintalapati,
andDongmeiZhang.2018.PredictingNodeFailureinCloudServiceSystems.
Flinta,andRolfStadler.2017.OnlineApproachtoPerformanceFaultLocalization
InProc.ACMJointMeetingonEuropeanSoftwareEngineeringConferenceand
forCloudandDatacenterServices.InProc.IFIP/IEEESymposiumonIntegrated
NetworkandServiceManagement.873–874. SymposiumontheFoundationsofSoftwareEngineering.480–490.
|                            |                     |                      |     | [33] YunLin,JunSun,LylyTran,GuangdongBai,HaijunWang,andJinSongDong. |
| -------------------------- | ------------------- | -------------------- | --- | ------------------------------------------------------------------- |
| [6] Zuhoor A. Al-Khanjari, | Martin R. Woodward, | Haider Ali Ramadhan, | and |                                                                     |
NarayanaSwamyKutti.2005. TheEfficiencyofCriticalSlicinginFaultLo- 2018. BreaktheDeadEndofDynamicSlicing:LocalizingDataandControl
OmissionBug.InProc.33rdACM/IEEEInternationalConferenceonAutomated
calization.SoftwareQualityJournal13,2(2005),129–153.
[7] EltonAlves,MilosGligoric,VilasJagannath,andMarcelod’Amorim.2011.Fault- SoftwareEngineering.509–519.
LocalizationUsingDynamicSlicingandChangeImpactAnalysis.InProc.26th [34] LeonardoMariani,CristinaMonni,MauroPezzè,OlivieroRiganelli,andRui
Xin.2018.LocalizingFaultsinCloudSystems.InProc.11thIEEEInternational
IEEE/ACMInternationalConferenceonAutomatedSoftwareEngineering.520–523.
[8] HidenaoAbeandShusakuTsumoto.2008.AnalyzingBehaviorofObjectiveRule ConferenceonSoftwareTesting,VerificationandValidation.262–273.
|     |     |     |     | [35] CristinelMateis,MarkusStumptner,andFranzWotawa.2000.ModelingJava |
| --- | --- | --- | --- | --------------------------------------------------------------------- |
EvaluationIndicesBasedonaCorrelationCoefficient.InProc.12thInternational
ConferenceonKnowledge-BasedIntelligentInformationandEngineeringSystems. ProgramsforDiagnosis.InProc.14thEuropeanConferenceonArtificialIntelligence.
| 758–765. |     |     |     | 171–175.                                                                  |
| -------- | --- | --- | --- | ------------------------------------------------------------------------- |
|          |     |     |     | [36] Microservice.System.Benchmark.2018.TrainTicket. RetrievedDecember25, |
[9] GeorgeK.Baah,AndyPodgurski,andMaryJeanHarrold.2010.TheProbabilistic
ProgramDependenceGraphandItsApplicationtoFaultDiagnosis.IEEETrans. 2018fromhttps://github.com/FudanSELab/train-ticket/
|     |     |     |     | [37] WilliamMorgan.2017. What’saServiceMesh?AndWhyDoINeedOne? |
| --- | --- | --- | --- | ------------------------------------------------------------- |
SoftwareEng.36,4(2010),528–545.
[10] TrainTicketBenchmark.2018.FaultCases. RetrievedDecember25,2018from RetrievedFebruary21,2018fromhttps://buoyant.io/2017/04/25/whats-a-service-
mesh-and-why-do-i-need-one/
https://github.com/FudanSELab/train-ticket-fault-replicate
|                                                  |     |                         |     | [38] LeeNaish,HuaJieLee,andKotagiriRamamohanarao.2011.AModelforSpectra- |
| ------------------------------------------------ | --- | ----------------------- | --- | ----------------------------------------------------------------------- |
| [11] DhrubaBorthakur.2019.HDFSArchitectureGuide. |     | RetrievedJanuary08,2019 |     |                                                                         |
fromhttps://hadoop.apache.org/docs/r1.2.1/hdfs_design.html BasedSoftwareDiagnosis.ACMTrans.Softw.Eng.Methodol.20,3(2011),11:1–
11:32.
[12] LionelC.Briand,YvanLabiche,andXuetaoLiu.2007.UsingMachineLearning
toSupportDebuggingwithTarantula.InProc.18thIEEEInternationalSymposium [39] SyedaNessa,MuhammadAbedin,W.EricWong,LatifurKhan,andYuQi.2008.
SoftwareFaultLocalizationUsingN-gramAnalysis.InProc.3rdInternational
onSoftwareReliabilityEngineering.137–146.
ConferenceonWirelessAlgorithms,Systems,andApplications.548–559.
| [13] AntonioBrogi,LucaRinaldi,andJacopoSoldani.2018. |     | TosKer:ASynergy |     |     |
| ---------------------------------------------------- | --- | --------------- | --- | --- |
betweenTOSCAandDockerforOrchestratingMulticomponentApplications. [40] CuongPham,LongWang,Byung-ChulTak,SalmanBaset,ChunqiangTang,
ZbigniewT.Kalbarczyk,andRavishankarK.Iyer.2017. FailureDiagnosisfor
Softw.,Pract.Exper.48,11(2018),2061–2079.
[14] YuriyBrunandMichaelD.Ernst.2004.FindingLatentCodeErrorsviaMachine DistributedSystemsUsingTargetedFaultInjection.IEEETrans.ParallelDistrib.
Syst.28,2(2017),503–516.
LearningoverProgramExecutions.InProc.26thInternationalConferenceon
|     |     |     |     | [41] TeeratPitakrat,DusanOkanovic,AndrévanHoorn,andLarsGrunske.2018. |
| --- | --- | --- | --- | -------------------------------------------------------------------- |
SoftwareEngineering.480–490.
[15] PeggyCellier,MireilleDucassé,SébastienFerré,andOlivierRidoux.2008.Formal Hora:Architecture-AwareOnlineFailurePrediction. JournalofSystemsand
Software137(2018),669–685.
ConceptAnalysisEnhancesFaultLocalizationinSoftware.InProc.6thInterna-
tionalConferenceonFormalConceptAnalysis.273–288. [42] TheCentOSProject.2019. CentOSLinux. RetrievedJanuary08,2019from
https://www.centos.org/about/
[16] PeggyCellier,MireilleDucassé,SébastienFerré,andOlivierRidoux.2011.Multi-
|     |     |     |     | [43] Peter-ChristianQuintandNaneKratzke.2018. TowardsaLightweightMulti- |
| --- | --- | --- | --- | ----------------------------------------------------------------------- |
pleFaultLocalizationwithDataMining.InProc.23rdInternationalConferenceon
SoftwareEngineering&KnowledgeEngineering.238–243. CloudDSLforElasticandTransferableCloud-nativeApplications.InProc.8th
InternationalConferenceonCloudComputingandServicesScience.400–408.
[17] DanielJosephDean,HiepNguyen,PeipeiWang,XiaohuiGu,AncaSailer,and
AndrzejKochut.2016.PerfCompass:OnlinePerformanceAnomalyFaultLocal- [44] Redis.Io.2016.redis.io. RetrievedJanuary16,2018fromhttps://redis.io/
|     |     |     |     | [45] ManosRenierisandStevenP.Reiss.2003.FaultLocalizationwithNearestNeigh- |
| --- | --- | --- | --- | -------------------------------------------------------------------------- |
izationandInferenceinInfrastructure-as-a-ServiceClouds.IEEETrans.Parallel
borQueries.InProc.18thIEEEInternationalConferenceonAutomatedSoftware
Distrib.Syst.27,6(2016),1742–1755.
| [18] VidrohaDebroy,W.EricWong,XiaofengXu,andByoungjuChoi.2010. |     |     | A   | Engineering.30–39.                                                          |
| -------------------------------------------------------------- | --- | --- | --- | --------------------------------------------------------------------------- |
|                                                                |     |     |     | [46] Replication.Package.2019. LatentErrorPredictionandFaultLocalizationfor |
Grouping-BasedStrategytoImprovetheEffectivenessofFaultLocalization
Techniques.InProc.10thInternationalConferenceonQualitySoftware.13–22. MicroserviceApplications. RetrievedJune30,2019fromhttps://fudanselab.
github.io/Research-ESEC-FSE2019-AIOPS
[19] RichardA.DeMillo,HsinPan,andEugeneH.Spafford.1997.FailureandFault
AnalysisforSoftwareDebugging.InProc.21stInternationalComputerSoftware [47] ScikitLearn.Com.2018. ScikitLearn. RetrievedFebruary21,2018fromhttps:
| andApplicationsConference.515–521. |     |     |     | //scikit-learn.org/                                                      |
| ---------------------------------- | --- | --- | --- | ------------------------------------------------------------------------ |
|                                    |     |     |     | [48] Sockshop.Com.2018.Sockshop. RetrievedMarch8,2018fromhttps://github. |
[20] AndreiFurda,ColinJ.Fidge,OlafZimmermann,WayneKelly,andAlistairBarros.
2018.MigratingEnterpriseLegacySourceCodetoMicroservices:OnMultite- com/microservices-demo/microservices-demo
|     |     |     |     | [49] Spark.Com.2018.Spark. RetrievedFebruary21,2018fromhttp://spark.apache. |
| --- | --- | --- | --- | --------------------------------------------------------------------------- |
nancy,Statefulness,andDataConsistency.IEEESoftware35,3(2018),63–72.
| [21] AlexGroce,SagarChaki,DanielKroening,andOferStrichman.2006. |     |     | Error | org/                                                                    |
| --------------------------------------------------------------- | --- | --- | ----- | ----------------------------------------------------------------------- |
|                                                                 |     |     |       | [50] SpringBoot.Com.2018. SpringBoot. RetrievedFebruary21,2018fromhttp: |
ExplanationwithDistanceMetrics.InternationalJournalonSoftwareToolsfor
//projects.spring.io/spring-boot/
TechnologyTransfer8,3(2006),229–247.
[22] Hadoop.Com.2018.Hadoop. RetrievedFebruary21,2018fromhttp://hadoop. [51] Testng.Com.2018.Testng. RetrievedFebruary21,2018fromhttps://testng.org/
doc/index.html
apache.org/
[23] MaryJeanHarrold,GreggRothermel,KentSayre,RuiWu,andLiuYi.2000.An [52] TaoWang,WenboZhang,ChunyangYe,JunWei,HuaZhong,andTaoHuang.
2016. FD4C:AutomaticFaultDiagnosisFrameworkforWebApplicationsin
EmpiricalInvestigationoftheRelationshipBetweenSpectraDifferencesand
CloudComputing. IEEETrans.Systems,Man,andCybernetics:Systems46,1
RegressionFaults.Softw.Test.,Verif.Reliab.10,3(2000),171–194.
| [24] ShilinHe,JiemingZhu,PinjiaHe,andMichaelR.Lyu.2016.ExperienceReport: |     |     |     | (2016),61–75.                                                                |
| ------------------------------------------------------------------------ | --- | --- | --- | ---------------------------------------------------------------------------- |
|                                                                          |     |     |     | [53] MichaelWhittaker,CristinaTeodoropol,PeterAlvaro,andJosephM.Hellerstein. |
SystemLogAnalysisforAnomalyDetection.InProc.27thIEEEInternational
SymposiumonSoftwareReliabilityEngineering.207–218. 2018.DebuggingDistributedSystemswithWhy-Across-TimeProvenance.In
Proc.ACMSymposiumonCloudComputing.333–346.
| [25] Istio.2018.Istio. RetrievedFebruary21,2018fromhttps://istio.io/ |     |     |     |                                                                     |
| -------------------------------------------------------------------- | --- | --- | --- | ------------------------------------------------------------------- |
|                                                                      |     |     |     | [54] W.EricWong,VidrohaDebroy,RichardGolden,XiaofengXu,andBhavaniM. |
[26] PooyanJamshidi,ClausPahl,NaborC.Mendonça,JamesLewis,andStefanTilkov.
2018.Microservices:TheJourneySoFarandChallengesAhead.IEEESoftware Thuraisingham.2012.EffectiveSoftwareFaultLocalizationUsinganRBFNeural
Network.IEEETrans.Reliability61,1(2012),149–169.
35,3(2018),24–35.
|     |     |     |     | [55] W.EricWong,RuizhiGao,YihaoLi,RuiAbreu,andFranzWotawa.2016. A |
| --- | --- | --- | --- | ----------------------------------------------------------------- |
SurveyonSoftwareFaultLocalization. IEEETrans.SoftwareEng.42,8(2016),
693

ESEC/FSE’19,August26–30,2019,Tallinn,Estonia XiangZhou,XinPeng,TaoXie,JunSun,ChaoJi,DeweiLiu,QilinXiang,andChuanHe
707–740. Engineering.272–281.
[56] DingYuan,SoyeonPark,andYuanyuanZhou.2012. CharacterizingLogging [61] XiangZhou,XinPeng,TaoXie,JunSun,ChaoJi,WenhaiLi,andDanDing.2018.
PracticesinOpen-SourceSoftware.InProc.34thInternationalConferenceon FaultAnalysisandDebuggingofMicroserviceSystems:IndustrialSurvey,Bench-
SoftwareEngineering.102–112. markSystem,andEmpiricalStudy.IEEETransactionsonSoftwareEngineering
[57] DingYuan,JingZheng,SoyeonPark,YuanyuanZhou,andStefanSavage.2012. (2018). https://doi.org/10.1109/TSE.2018.2887384
ImprovingSoftwareDiagnosabilityviaLogEnhancement.ACMTrans.Comput. [62] XiangZhou,XinPeng,TaoXie,JunSun,ChaoJi,WenhaiLi,andDanDing.
Syst.30,1(2012),4:1–4:28. 2019.DeltaDebuggingMicroserviceSystemswithParallelOptimization.IEEE
[58] AndreasZeller.2002.IsolatingCause-EffectChainsfromComputerPrograms. TransactionsonServicesComputing(2019). https://doi.org/10.1109/TSC.2019.
InProc.10thACMSIGSOFTSymposiumonFoundationsofSoftwareEngineering. 2919823
1–10. [63] XiangZhou,XinPeng,TaoXie,JunSun,WenhaiLi,ChaoJi,andDanDing.2018.
[59] AndreasZellerandRalfHildebrandt.2002. SimplifyingandIsolatingFailure- DeltaDebuggingMicroserviceSystems.InProc.33rdACM/IEEEInternational
InducingInput.IEEETrans.SoftwareEng.28,2(2002),183–200. ConferenceonAutomatedSoftwareEngineering.802–807.
[60] XiangyuZhang,NeelamGupta,andRajivGupta.2006.LocatingFaultsthrough
AutomatedPredicateSwitching.InProc.28thInternationalConferenceonSoftware
694