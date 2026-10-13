PDF Download
3534678.3539176.pdf
17 March 2026
Total Citations: 21
. Total Downloads: 559
.
Latest updates: hps://dl.acm.org/doi/10.1145/3534678.3539176 .
.
Published: 14 August 2022
.
. .
RESEARCH-ARTICLE .
Citation in BibTeX format
Multi-task Hierarchical Classification for Disk Failure Prediction in
.
.
Online Service Systems KDD '22: The 28th ACM SIGKDD
Conference on Knowledge Discovery and
Data Mining
YUDONG LIU, Microso Research, Redmond, WA, United States August 14 - 18, 2022
Washington DC, USA
.
HAILAN YANG, Microso Research, Redmond, WA, United States .
.
Conference Sponsors:
. PU ZHAO, Microso Research, Redmond, WA, United States SIGMOD
SIGKDD
.
MINGHUA MA, Microso Research, Redmond, WA, United States
.
CHENGWU WEN, Microso Research, Redmond, WA, United States
.
HONGYU ZHANG, The University of Newcastle, Australia, Callaghan, NSW, Australia
.
View all
.
.
Open Access Support provided by:
.
Microso Research
.
Microso Corporation
.
The University of Newcastle, Australia
.
KDD '22: Proceedings of the 28th ACM SIGKDD Conference on Knowledge Discovery and Data Mining (August 2022)
hps://doi.org/10.1145/3534678.3539176
ISBN: 9781450393850
.

Multi-task Hierarchical Classification for Disk Failure Prediction
|                   | in Online | Service           | Systems |                          |                     |     |
| ----------------- | --------- | ----------------- | ------- | ------------------------ | ------------------- | --- |
| YudongLiu         |           | HailanYang        |         |                          | PuZhao              |     |
| MicrosoftResearch |           | MicrosoftResearch |         |                          | MicrosoftResearch   |     |
| Beijing,China     |           | Beijing,China     |         |                          | Beijing,China       |     |
| MinghuaMa         |           | ChengwuWen        |         |                          | HongyuZhang         |     |
| MicrosoftResearch |           | MicrosoftResearch |         | TheUniversityofNewcastle |                     |     |
| Beijing,China     |           | Beijing,China     |         |                          | Newcastle,Australia |     |
QingweiLin∗
| ChuanLuo          |     |                   |     |     | ChangYi           |     |
| ----------------- | --- | ----------------- | --- | --- | ----------------- | --- |
| MicrosoftResearch |     | MicrosoftResearch |     |     | Microsoft365      |     |
| Beijing,China     |     | Beijing,China     |     |     | Suzhou,China      |     |
| JiaojianWang      |     | ChenjianZhang     |     |     | PaulWang          |     |
| Microsoft365      |     | Microsoft365      |     |     | Microsoft365      |     |
| Suzhou,China      |     | Suzhou,China      |     |     | Suzhou,China      |     |
| YingnongDang      |     | SaravanRajmohan   |     |     | DongmeiZhang      |     |
| MicrosoftAzure    |     | Microsoft365      |     |     | MicrosoftResearch |     |
| Seattle,USA       |     | Seattle,USA       |     |     | Beijing,China     |     |
ABSTRACT ourexperimentsalsopresentthatthehierarchical-awaremecha-
nismunderlyingMTHCcanalleviatethedataimbalanceproblem
Oneofthemostcommonthreatstoonlineservicesystem’srelia-
bilityisdiskfailure.Manydiskfailurepredictiontechniqueshave andthusimprovethepracticalperformanceofvariousdiskfail-
beendevelopedtopredictfailuresbeforetheyactuallyoccur,allow- urepredictionmodels.Experimentsforonlineindustrialdatasetin
Microsoft365alsodemonstratestheeffectivenessofourMTHC.
ingproactivestepstobetakentominimizeservicedisruptionand
increaseservicereliability.Existingapproachesfordiskfailurepre-
CCSCONCEPTS
dictiondonotdifferentiateamongvarioustypesofdiskfailure.In
industrialpractice,however,differentproductteamstreatdistinct •Computersystemsorganization→Cloudcomputing;•Com-
typesofdiskfailuresasdifferentpredictiontasksinlarge-scale putingmethodologies→Neuralnetworks.
onlineservicesystemslikeMicrosoft365.Forexample,teamAis
concernedwithphysicaldiskerrors,whileteamBfocusesonI/O KEYWORDS
delay.Inthispaper,weproposeMTHC(Multi-TaskHierarchical
Diskfailureprediction;Multi-task;Hierarchicalclassification
Classification)toenhancetheperformanceofdiskfailureprediction
foreachtaskviamulti-tasklearning.Inaddition,MTHCintroduces ACMReferenceFormat:
anovelhierarchy-awaremechanismtodealwiththedataimbal- YudongLiu,HailanYang,PuZhao,MinghuaMa,ChengwuWen,Hongyu
Zhang,ChuanLuo,QingweiLin,ChangYi,JiaojianWang,ChenjianZhang,
anceproblem,whichisasevereissueintheareaofdiskfailure
|     |     |     | Paul Wang, Yingnong | Dang, Saravan | Rajmohan, | and Dongmei Zhang. |
| --- | --- | --- | ------------------- | ------------- | --------- | ------------------ |
prediction.WeshowthatMTHCcanbeeasilyutilizedtoenhance
2022.Multi-taskHierarchicalClassificationforDiskFailurePredictionin
moststate-of-the-artdiskfailurepredictionmodels.Ourexperi-
OnlineServiceSystems.InProceedingsofthe28thACMSIGKDDConfer-
mentsonbothindustrialandpublicdatasetsdemonstratethatsuch
enceonKnowledgeDiscoveryandDataMining(KDD’22),August14–18,
diskfailurepredictionmodelsenhancedbyMTHCperformsmuch
2022,Washington,DC,USA.ACM,NewYork,NY,USA,9pages.https:
betterthanthosemodelsworkingwithoutMTHC.Furthermore, //doi.org/10.1145/3534678.3539176
∗QingweiLinisthecorrespondingauthorofthispaper.
1 INTRODUCTION
Permissiontomakedigitalorhardcopiesofallorpartofthisworkforpersonalor
Onlineservicesystems,suchasFacebook,Microsoft365,andGmail,
classroomuseisgrantedwithoutfeeprovidedthatcopiesarenotmadeordistributed
forprofitorcommercialadvantageandthatcopiesbearthisnoticeandthefullcitation areresponsibleforprovidingonlineservicesformillionsofcus-
onthefirstpage.CopyrightsforcomponentsofthisworkownedbyothersthanACM tomers[2,31].Enhancinghighservicereliabilityisofgreatim-
mustbehonored.Abstractingwithcreditispermitted.Tocopyotherwise,orrepublish, portancetoimproveuserexperienceandpreventfinancialloss[7].
topostonserversortoredistributetolists,requirespriorspecificpermissionand/ora
fee.Requestpermissionsfrompermissions@acm.org. However,failuresofthesesystemsarestillinevitable.Diskfailures
KDD’22,August14–18,2022,Washington,DC,USA
areoneofthemostcommontypesoffailuresinonlineservicesys-
©2022AssociationforComputingMachinery.
tems[5,19,20,25,28],whichcouldresultinserviceinterruptions
ACMISBN978-1-4503-9385-0/22/08...$15.00
https://doi.org/10.1145/3534678.3539176 andpotentiallyfinancialloss.Forexample,diskfailureaccounts
3438

KDD’22,August14–18,2022,Washington,DC,USA YudongLiuetal.
for76-95percentofallhardwarefailedcomponentsindatacen- featureembeddings.Theintuitionisthatdisksfromdifferenttasks
ters,accordingtoarecentstudy[18].Therefore,itisimportantto areusuallyinthesamedataformat,andtherearenon-negligible
proactivelypredictdiskfailures. relationsamongdifferenttypesofdiskfailures,whichcanhelp
Toeliminatethelosscausedbydiskfailures,manyapproaches enhancetheperformanceofeachtask.Inthisway,comparedto
[5,12–14,27,28,32–34,37,38]havebeenproposedtopredictdisk dealingwitheachsingletaskindividually,multi-taskmechanism
failuresinadvance.Currentstate-of-artdiskfailurepredictionap- sharescommonfeatureembeddingsamongtasksandcouldhelp
proachesbasedontemporalsequentialmodels,suchasLSTM[34], improvethepredictionaccuracyofeachtask.
RNN[32],Transformer[16],andTCNN[28].Theseapproaches Todealwiththedataimbalanceprobleminthescenarioofdisk
usuallyregardthetaskofdiskfailurepredictionasabinaryclas- failure prediction [5, 12, 27, 28, 33, 34], we propose to conduct
sificationproblem,andbuildamodeltopredictwhetheradisk two-stephierarchicalclassification.Wefirstlypredictwhetherthe
willfailornotinthenearfuture.Theinputoftheclassification machineisunhealthy,i.e.,containsfailuredisks.Comparedtodisks,
modelistypicallySMART(Self-Monitoring,AnalysisandReport- thenumbersofunhealthymachinesandhealthyonesarenotso
ingTechnology)data[1],whichrecordsstatusofdisksandprovides imbalanced.Ifthemachineispredictedasunhealthy,wethenpre-
importantindicatorsduringthewholelifetimeofdisks.Engineers dicteachdiskonthemachine.Thatis,ourproposedMTHCcan
maytakeproactiveactionsinresponsetothediskfailureprediction. alleviatethedataimbalanceproblemofdiskfailurepredictionand
Existingmethodsgenerallyconcernadiskwillfailornotin enhancethepredictionperformance.
thenearfuture,withoutdifferentiatingamongvariousdiskfailure NotedthatMTHCisorthogonalwithpreviousmodels,i.e.,previ-
types.However,ourfirstinsightisthatpredictingdifferenttypes ousmodelscanbeveryeasilyintegratedintoourMTHCframework.
ofdiskfailuresisanurgentneedinindustrialpractice.Specifically, Forthepurposeofevaluatingtheeffectivenessandrobustnessof
inthelarge-scaleMicrosoft365(shortasM365)onlineservicesys- MTHC, based on industrial dataset and two public datasets, we
tems,differentteamsfocusondifferenttypesofdiskfailures.For conduct extensive experiments to compare various disk failure
example,teamAmainlycareaboutphysicaldiskerrors,whileteam predictionmodelsenhancedbyMTHCwiththosemodelswork-
BconcentrateonI/Olatency.Intuitively,thecurrentsolutionis ingwithoutMTHC.Theexperimentsonthreedatasetsindicate
tobuildmultiplediskfailurepredictionmodelsforeachteam’s thatMTHCconsiderablyenhancestheperformanceofdiskfailure
specificpredictiontask.Theseindependentmodels,ontheother prediction.
hand,ignorethecorrelationamongdifferenttypesofdiskfailure Themaincontributionsofthispaperareasfollows:
prediction.Forexample,diskfailurescausedbyintensiveI/Ooper-
ationsmayalsoresultinphysicaldiskdamage.Thatis,considering • We reveal disk failure prediction challenges in industrial
differenttasksispursuedinpractice,whichmotivatesustoadopt practice,i.e.,differentdiskfailuretasksanddataimbalanced
multi-tasklearning. problem.WedesignaframeworkMTHCbasedondomain-
Inaddition,sincedisksusuallykeephealthyforseveralmonths specificinsights.
andevenseveralyearsuntilfailure,thenumbersoffaileddisksand • We point out that different disk failure tasks are of high
healthyonesareextremelyimbalanced,whichsignificantlyaffects correlationandthusproposemulti-taskmechanismtoen-
failurepredictionaccuracy[16].Toalleviatethedataimbalance, hancetheperformanceofeachtask.Besides,wepropose
existingapproachesutilizeunder-samplingorover-samplingmeth- hierarchy-awaremechanismtodealwiththedataimbalance
odstobalancetheratiobetweenthenumbersoffaileddisksand issueinthescenarioofdiskfailureprediction.
healthyones.However,thesesamplingmethodschangethedata • Extensiveexperimentsonindustrialdatasetandpublicdatasets
distributionandtendtocauseoverfitting,sotheycannotachieve demonstratethatourproposedMTHCframeworkconsider-
goodperformanceinrealscenario.Also,wegainanotherinsight ablyenhancestheperformancevariousdiskfailurepredic-
frompracticethatdiskphysicalstructureneedstobeconsidered. tionmodels.
Thatis,disksinthesamemachineshareanidenticalcomputing
environment,thustheirstatusiscorrelated.Intuitively,whenadisk 2 BACKGROUNDANDMOTIVATION
fails,thestatusofthecorrespondingmachinewillbeunhealthy.
2.1 DiskFailurePrediction
Becauseamachinetypicallycontainsmultipledisks,thenumbers
ofhealthyandunhealthymachinesaremoreevenlydistributed Inpractice,diskfailuresarenotonlycausedbyhardwarebreak-
thanthenumbersofhealthyandunhealthydisks.Thus,wecan down,butalsorelatedtoheavyusage,suchasintensiveI/Oand
leveragemachine-levelpredictiontohandlethedataimbalance overheating[15,17].
problem. Diskfailurepredictionhasbeenarousingwideconcernwith
Inthispaper,todealwiththetwoissuesdiscussedabove,wepro- therapidexpansionofstoragesystemsindatacenters.Withthe
poseaMulti-TaskHierarchicalClassification(MTHC)framework. developmentofdeeplearning,nowadaysmanyresearchersderive
MTHC consists of two mechanisms, i.e., multi-task mechanism diskfailurepredictionmodelsusingdeeplearningtechniquesbased
and hierarchy-aware mechanism. Different from existing meth- onSMARTdata[15].SMARTisaself-monitoringsystemsupported
ods,whichdonotdifferentiateamongvarioustypesofdiskfailures, bymostdiskmanufacturers,andrecordsdiskattributessuchas
ourmulti-taskmechanismaimstocapturethesharedinformation "Raw_Read_Error_Rate"and"Power_On_Hours",whichmonitorthe
amongdifferenttypesofdiskfailures,andthusappliesmulti-task internalhealthstatusofdisks[1].Deeplearningbasedmethods
learningtechnique.Althoughdifferenttaskscorrespondtodifferent regarddiskfailurepredictionasabinaryclassificationproblem,
typesofdiskfailures,theycansharenetworkstoextractcommon leveragingneuralnetworkssuchasrecurrentneuralnetwork(RNN)
3439

Multi-taskHierarchicalClassificationforDiskFailurePredictioninOnlineServiceSystems KDD’22,August14–18,2022,Washington,DC,USA
[32],longshort-termmemory(LSTM)[34],andtemporalconvolu- deploymentandmanagement,disksfromthesamemachineare
tionalneuralnetwork(TCNN)[28]. usuallyinthesameconfigurations.Secondly,disksonthesame
machineobviouslysharemanyresources,suchaspowerandpe-
2.2 DifferentTypesofDiskFailures ripheraldevices.Thesetwoaspectsindicatethatthestatusofdisks
Previousdiskfailurepredictionmethodsonlyconcernwhether fromthesamemachinearemoresimilarthanthosefromdifferent
diskswillfailornotinthenearfuture.Inpractice,however,dif- machines.
ferentteamsintheM365onlineservicesystemsfocusondistinct Sincedisksusuallystayhealthyforseveralmonthsandeven
diskproblemsandmitigationmethods,resultingindifferentper- severalyearsuntilfailure,thenumberoffaileddisksandhealthy
spectivesonfailure.Thebelowaretwoimportanttypesofdisk onesisextremelyimbalanced.Thusdiskfailurepredictionmethods
failures. havebeenfacingtheimbalanceproblem,whichcouldaffectthe
performanceofpredictionmodels.Consideringthecommonprop-
• Hardwarefailure[17]:Physicaldiskerrors,suchasdiskag-
ertiesmentionedabove,wecanalleviatetheimbalanceissuevia
ing,missingfilesystemfields,andread-writeheaderdamage,
thehierarchicalinfrastructureinM365onlineservicesystems.As
aretheprimaryconcernsofteamA.
illustratedbefore,disksfromthesamemachinehavestrongcorrela-
• Performancefailure[15]:I/Odelay,whichisfrequently
tions.Insteadofpredictingthefailureofeachdiskindividually,we
causedbyoverload,ismoreimportanttoteamB.
firstlypredictwhetherthemachineisunhealthy.Wecontinually
Therefore,inpractice,especiallyinlarge-scalecompanies,to predicteachdiskonthemachineifsoandstopifnot.Tothisend,
dealwiththeirowndiskfailureproblems,eachteammaintains weregarddiskfailurepredictionasahierarchicalclassification
adisk"failure"predictionmodel.Eachmodeldealswithabinary problembyreducingthedataimbalance,whichcanenhancethe
classificationproblem,wheretheclasscorrespondstothespecific performanceofdiskfailureprediction.
typeofdiskfailure,suchasphysicaldiskerrorsandhighI/Olatency.
Althoughthediskfailurepredictionmodelsfromdifferentteams
3 METHOD
dealwithdifferentfailureissues,theyarecommoninsomeaspects.
Firstly,differentteamsutilizethesamedataformat,i.e.SMART 3.1 ProblemDefinition
data(Self-Monitoring,Analysis,andReportingTechnology)[1]. Inourproposedmodel,weformulatediskfailurepredictioninto
Secondly,basedonthesamedataformat,differentteamsusually amulti-taskhierarchicalclassificationproblem.Inpractice,each
utilizesimilarmodels,i.e.,temporalsequencemodelssuchasLSTM teamfocusesononespecifictypeofdiskfailure,whichisregarded
topredictdiskfailures.Thirdly,nonnegligiblecorrelationexists asatask.Thetotalnumberoftasksisdenotedas𝐾.Generally,
amongdiskswithdifferenttypesofdiskfailures,whichcanbe disksaredeployedinphysicalmachines.Thereare𝑁 machines
utilized[6].Forexample,forbothdiskswithphysicalfailuresand intotalandeachmachinecontainsseveraldisks.Foreachdisk,
highI/Olatency,therelatedfeaturevaluesindiskdata,suchas a feature vector of𝑛 attributes of a disk’s status is recorded at
read/writetimemightbothdeviatefromnormalinterval.Adisk eachtimestamp.Specifically,𝑋 𝑖,𝑗 denotesthefeatureof 𝑗𝑡ℎ disk
withphysicalerrorscouldusuallyleadtohighI/Olatency. onthe𝑖𝑡ℎ machine,whichrecordsfeaturevectorfromtimestamp
Consideringthecommonpropertiesmentionedabove,instead 𝑡 𝑖 totimestamp𝑡 𝑖 +ℎ(𝑡 𝑖 isthebeginningtimestamp).Therefore,
ofbuildinganindividualmodelforeachteam,wecanregardthe theshapeof𝑋
𝑖,𝑗
isℎ×𝑛.Thetrainingsetconsistsofpairsinthe
predictionforeachteamasataskandintegratetasksfromdifferent formatof{𝑋 𝑖,𝑗 ,𝑌 𝑖,𝑗}.Asmentionedabove,𝑋 𝑖,𝑗 denotesthetime
teamsasamulti-taskproblem.Specifically,weaggregatediskdata seriesfeatureofcorrespondingdisk.𝑌 𝑖,𝑗 isaone-hotvectorwhose
from different teams and feed the whole data into a multi-task lengthequalstothenumberoftasks.𝑌 𝑖,𝑗,𝑘 =1meansthediskwill
model.Themodelcontainsseveraltasks,andeachtaskdealwith encounterwiththe𝑘𝑡ℎ
typeofdiskfailure.Ourgoalistomaximize
thespecifictypeofdiskfailurefromcorrespondingteam.Toutilize
theaccuracyofestimatingwhetheradiskwillfailornotforeach
the feature similarity among disks with different types of disk
task.
failures,wesharetheembeddinglayerstoextractcommonfeatures
fordisks,i.e.,hardparametersharing.Inthisway,basedonmulti-
3.2 Overview
tasklearning,eachtasklearnsembeddedfeaturefromothertasks,
andtheperformanceofeachindividualtaskwillbeenhanced. Asintroducedbefore, MTHC enhancestheperformanceofdisk
failurepredictionfromtwoaspects:multi-taskandhierarchical
2.3 Hierarchicalinfrastructure classification.Inthissection,webrieflyoverviewtwomechanisms
ofourmethod:multi-taskmechanismandhierarchy-awaremecha-
Previousdiskfailurepredictionmethodsjustdealwitheachdisk
nism.TheframeworkofMTHCisshownasFigure1.
individually,withoutconsideringthecorrelationamong"similar"
disks.However,inM365onlineservicesystems,disksaredeployed • Multi-taskmechanismforVariousTypesofDiskFail-
inahierarchicalinfrastructure.Specifically,thetop-downhierar- ures:theinputofmulti-taskmechanismconsistsofdiskfea-
chicalstructureinM365onlineservicesystemscanbeformulated turesfromdifferenttasks.Thismechanismutilizesashared
as:datacenter,rack,server,anddisk.Diskswiththesameserver timeseriesmodeltoencodethediskfeaturesfromdiffer-
fielddenotesthattheyaredeployedonthesamemachine,andeach enttasks.Basedonthesharedencodingvectors,multi-task
machinecontainsanumberofdisks. mechanismoutputsabinaryclassificationforeachtask.
Underthecircumstance,disksonthesamemachinesharesome • Hierarchy-awaremechanismforImbalancedData:the
commonpropertiesintwoaspects.Firstly,fortheconvenienceof inputofthismechanismconsistsfeaturesofdisksontarget
3440

KDD’22,August14–18,2022,Washington,DC,USA YudongLiuetal.
state-of-the-artdiskfailurepredictionmodelscanbeveryeasily
integratedintomostmulti-taskmechanism.TakingLSTMasan
example,arawdiskfeaturewiththeshapeofℎ∗𝑛isfedintoa
bidirectionalLSTMnetworktocapturethesequenceinformation
[21].ThehiddenstatesatalltimestepsofLSTMareaggregatedas
thefinalencodingvector.Basedonsharingencodingvector,task-
awarebinaryclassificationsareimplementedviafull-connected
layers.Foreachtypeofdiskfailure,afull-connectedlayeroutputsa
2-dimensionfeature,followedbyasoftmaxlayerastheprediction
result.Fordisk𝑋 𝑖,𝑗,thelabelforthe𝑘𝑡ℎ taskbranchisexactly𝑌 𝑖,𝑗,𝑘.
Duringinferencephrase,eachtaskonlyfocusesonthecorrespond-
ingpredictionresultofmulti-taskmechanism,regardlessofresults
Figure1:MTHCframework
fromothertaskbranches.
machine.Insteadofdirectlyclassifyingthestateofeachdisk, 3.4 Hierarchy-awaremechanism
hierarchy-awaremechanismclassifieswhetherthemachine
Almostalltheexistingapproachesneglectthephysicallocation
containsfailuredisk(s).Ithasnoneedtoassesseachdiskif
informationamongdisks.However,disksaredeployedinphysical
themechanismdeterminesthatthemachineis"healthy",and
machines,andeachmachinecontainsanumberofdisks.Disks
disksonthemachinewillonlybereviewedifthemechanism
deployedonthesamemachineareusuallyinthesameconfigura-
determinesthatthemachineincludesfailuredisk(s).
tionsandsharevariousresources,suchasCPU,power,andsoon.
Followingtwomechanisms,toaggregatetwopredictionresults Therefore,thesedisksarehighlyrelatedintheirfeatures.
frommulti-taskmechanismandhierarchy-awaremechanism,we
multiplythemasthefinalpredictionscore.
3.3 Multi-Taskmechanism
Previousdiskfailurepredictionmethodsdonotconsiderspecific
typesofdiskfailures.However,inrealpractice,differentteams
inM365onlineservicesystemsfocusondifferenttypesofdisk
X
failures. For example, team A mainly cares about physical disk i,1
X
errors,whileteamBcaresmoreaboutI/Olatency.Generally,each i,2
teammaintainstheirowndiskfailurepredictionmodel.Thatis
tosay,theproblemisregardedasseveralsingletasks,andthere X i,D
isnointeractionsbetweenthesetasks.However,asillustratedin
section2,disksfromdifferentteamsareinthesamedataformat,
i.e.,SMARTdata,andnonnegligiblecorrelationexistsamongdisks
withdifferenttypesofdiskfailures.Consideringtheseproperties,
MTHCintegratesdifferenttaskstogetherandpredictfailurefor
typesofdiskfailuresthroughonemodel,whichperformsasamulti-
taskfailurepredictionmodel.Inthisway,theperformanceofeach
singletaskwillbeenhancedviamulti-tasklearning.
Task A
Feature Task B
Encoding
e.g., LSTM, etc.
Task C
Disk Data Encoding Full-Connected Task-Specific Layer Layer Layer
Figure2:Multi-taskmechanism
Thearchitectureofmulti-taskmechanismisshowninFigure2.
Theencodinglayerisusuallyatimeseriesmodel,whichextracts
sharedfeaturefordisksfromdifferenttypesofdiskfailures.The
…
a
i,1
a
i,2
a i,D
…
Network
m i Q
Network
K
softmax
Feature M P(M)
Encoding i i
Machine
Failure
Probability
Disk Data
Figure3:Hierarchy-awaremechanism
Ifweaggregatefeaturesfromallthedisksfromthesamema-
chine,theaggregatedfeaturescouldactonbehalfofthestateof
thewholemachine.Utilizingmachine-levelinformation,wecan
implementhierarchicalclassificationandalleviatetheimbalance
classificationproblemofdiskfailureprediction.Specifically,via
theaggregatedfeatures,wecanfirstlypredictwhetherthewhole
machineisunhealthy.Amachineisunhealthyifthereisatleastone
diskonthemachinewillfailinthenearfuture.Whenthemachine
isconsideredhealthy,thereisnoneedtopredicteachdiskonthe
machine.Andonlywhenthemachineispredictedasunhealthy
willwecheckeachdisk.Thelabelfor𝑖𝑡ℎ
machinecanbecalculated
as:
𝑌 𝑚𝑖 = 
1, (cid:205)
𝑧
𝐷
=1
𝑌
𝑖,𝑧
>0


0, (cid:205)
𝑧
𝐷
=1
𝑌
𝑖,𝑧
<0
where𝐷denotesthenumberofdisksonthemachine.Obviously,
thewholeclassificationprocessishierarchical.Consideringthat
thereexistshugeimbalancebetweenpositivesamplesandnegative
samples,hierarchicalclassificationcouldalleviatetheissueand
reducetheclassificationdifficulties.
3441

Multi-taskHierarchicalClassificationforDiskFailurePredictioninOnlineServiceSystems KDD’22,August14–18,2022,Washington,DC,USA
Toobtainmachine-levelfeatures,ahierarchy-awaremechanism Table1:Summaryofthebackblazedataset.
combinesallthediskfeaturesonthemachine.However,instead
oftreatingeachdiskequally,itisexpectedtofocusmoreonthose Task1 Task2 Task3
| failuredisks.Tosolvetheissue,weutilizeattentionmechanism[11] |     |     |     |     |     |     |     | Dataset |      |          |     |      |      |      |     |
| ------------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | ------- | ---- | -------- | --- | ---- | ---- | ---- | --- |
|                                                              |     |     |     |     |     |     |     |         | #Pos | #Neg#Pos |     | #Neg | #Pos | #Neg |     |
tocapturetheimportanceofeachdisk.Thefinalhierarchy-aware
featureisaweightedaccumulationofdiskfeatures.Theprocessis TrainingSet 70 6,998 531 45,176 125 12,512
| showninFigure3.Onthe𝑖𝑡ℎ |     |     |     | machine,encodedvector𝑎 |     |     |         |         |     |       |     |        |     |       |     |
| ----------------------- | --- | --- | --- | ---------------------- | --- | --- | ------- | ------- | --- | ----- | --- | ------ | --- | ----- | --- |
|                         |     |     |     |                        |     | 𝑖,𝑗 | fordisk | TestSet | 29  | 2,999 | 108 | 19,361 | 52  | 5,363 |     |
𝑗 isobtainedviasharingencodinglayer.𝑚
𝑖 isacombinationofall
| the𝑎 𝑖,𝑗.Thequeryvectoris𝑞 |     |     |     | 𝑖 = 𝑄(𝑚 | 𝑖),andthekeyvectorfor |     |     |     |     |     |     |     |     |     |     |
| -------------------------- | --- | --- | --- | ------- | --------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
the𝑖𝑡ℎ
𝑗𝑡ℎ diskis𝑘 =𝐾(𝑥 𝑖,𝑗),[30],whereQandKarefullyconnected where 𝑃 𝑚𝑖 denotes the failure prediction probability of
𝑖,𝑗
networks.Theweight𝑤 for𝑗𝑡ℎ machine,and𝑌 𝑚𝑖 denotesthecorrespondinggroundtruth.Recall
|     |     |     | 𝑖,𝑗 | diskiscalculatedas: |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | ------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
thatthefunction𝐶𝐸denotesthecrossentropylossdefinedinEq.5.
|     |     |     |     | e x p ( 𝑞 𝑖 · | 𝑘 𝑖 ,𝑗 ) |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | ------------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
𝑤 = (1) T h e t o t a l lo s s is a co m b i n a t io n o f m u lti-tasklossandhierarchy-
𝑖,𝑗 (cid:205) 𝐷
|                                             |     |     |     | e x p ( 𝑞 | 𝑖 · 𝑘 𝑖,𝑧) |     |     | aw ar e l o s | s , w h i ch c | an b e c a l | c u la te d | a s : |     |     |     |
| ------------------------------------------- | --- | --- | --- | --------- | ---------- | --- | --- | ------------- | -------------- | ------------ | ----------- | ----- | --- | --- | --- |
|                                             |     |     | 𝑧   | = 1       |            |     |     |               |                |              |             |       |     |     |     |
| Theweightedaccumulationofdiskfeaturesfor𝑖𝑡ℎ |     |     |     |           |            |     |     |               |                | L=L𝑑         | +L𝑚         |       |     |     | (7) |
machinecanbe
calculatedas: Itisnotedthat,sincehierarchy-awareinformationdidnotattract
|     |     |     | 𝐷    |          |     |     |     | muchattentioninpreviousmethods,publicdatasetsdidnotcon- |     |     |     |     |     |     |     |
| --- | --- | --- | ---- | -------- | --- | --- | --- | ------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     | 𝑀 ∑︁ | (𝑤 𝑖,𝑧·𝑥 |     |     |     |                                                         |     |     |     |     |     |     |     |
𝑖 = 𝑖,𝑧) (2) tainhierarchy-awarelabels.Forthesedatasets,ourmodelcannot
𝑧=1 implementhierarchicalclassification,andourlossfunctiononly
Followingtheattentionmechanism,thecalculatedhierarchy- includesmulti-tasklossinthissituation.
awarefeature𝑀
𝑖 isfedintoafullyconnectedlayerandsoftmax
|     |     |     |     |     |     |     |     | 4 EXPERIMENTS |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- |
layertooutputthepredictionofthemachine,whichissimilarto
theoneinmulti-taskmechanism.Thelabelforthemachineis0if ToevaluatetheeffectivenessandefficiencyofMTHC,weconduct
allthedisksonthe𝑖𝑡ℎ
machinearehealthy.Thelabelis1ifatleast
|     |     |     |     |     |     |     |     | extensive | experiments | on public | datasets |     | and online | industrial |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ----------- | --------- | -------- | --- | ---------- | ---------- | --- |
onefailurediskexists,regardlessofthekindofdiskfailure.
datasets.Inthissection,wefirstdescribetheexperimentalsettings.
Then,weintroduceanindustrialdatasetandtwopublicdatasets.
| 3.5 | LossFunction |     |     |     |     |     |     | TheexperimentsresultsarepresentedinSec.4.3. |     |     |     |     |     |     |     |
| --- | ------------ | --- | --- | --- | --- | --- | --- | ------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
Inthissection,weillustratethelossfunctionofMTHC.Thereare
|          |           |     |            |            |     |                     |     | 4.1 ExperimentalSettings |     |     |     |     |     |     |     |
| -------- | --------- | --- | ---------- | ---------- | --- | ------------------- | --- | ------------------------ | --- | --- | --- | --- | --- | --- | --- |
| two loss | functions | in  | our model: | multi-task |     | loss and hierarchy- |     |                          |     |     |     |     |     |     |     |
awareloss. TodemonstratetherobustnessofMTHC,weadoptMTHConfour
|       |                 |     |                                       |     |     |     |     | state-of-the-art | methods | which | are | widely | used | in the | context |
| ----- | --------------- | --- | ------------------------------------- | --- | --- | --- | --- | ---------------- | ------- | ----- | --- | ------ | ---- | ------ | ------- |
| 3.5.1 | Multi-taskloss. |     | Thetotalmulti-tasklossiscalculatedas: |     |     |     |     |                  |         |       |     |        |      |        |         |
ofdiskfailureprediction:RNN[32],LSTM[34],Transformer[16],
𝐾
|     |     |     |      | 1 ∑︁ |     |     |     | andTCNN[28].Allexperimentsareconductedonaworkstation |     |     |     |     |     |     |     |
| --- | --- | --- | ---- | ---- | --- | --- | --- | ---------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     | L𝑑 = | L𝑑𝑘  |     |     | (3) |                                                      |     |     |     |     |     |     |     |
|     |     |     |      | 𝐾    |     |     |     | equippedwithNVIDIATeslaP100GPUandCUDA10.2.Thecode    |     |     |     |     |     |     |     |
𝑘=1
isimplementedbasedonPyTorch1.8.Duringthetrainingprocess,
where𝐾denotesthenumberoftasks.For𝑘𝑡ℎ weutilizeAdamoptimizerandsettheinitiallearningrateas2e-3.
task,thetask-specific
lossiscalculatedas: Inaddition,thetrainingepochissetto100andthebatchsizeis64.
(cid:205) 𝐶𝐸(𝑌 , 𝑃 )·𝑌 N o t e d t h a t th e p u b li c d a t a se t s d o n o t c o n ta i n m a c h i n e -le v el la b e ls,
|     |     |     | 𝑖,𝑗 | 𝑖, 𝑗,𝑘 | 𝑑𝑖,𝑗,𝑘 | 𝑚𝑖  |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | ------ | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
L𝑑𝑘 =− (4) th e r e fo r e , w e d o n o t c o n d u c t h ie r ar c h i c al c l as si fi c a t io n o n th e m .
𝐷 · 𝑁
where𝑁 denotesthenumberofmachines,𝐷denotesthenumber Table2:SummaryoftheAlidataset.
| ofdiskspermachine,𝑃 |     |     | denotesthefailurepredictionprobabil- |     |     |     |     |     |     |     |     |     |     |     |     |
| ------------------- | --- | --- | ------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
𝑑𝑖,𝑗,𝑘
|                                        | 𝑗𝑡ℎ diskon𝑖𝑡ℎ | machinefor𝑘𝑡ℎ |     |     |           |                  |     |         |      |          |     |          |     |       |     |
| -------------------------------------- | ------------- | ------------- | --- | --- | --------- | ---------------- | --- | ------- | ---- | -------- | --- | -------- | --- | ----- | --- |
| ityof                                  |               |               |     |     | task,and𝑌 | 𝑖,𝑗,𝑘 denotesthe |     |         |      |          |     |          |     |       |     |
|                                        |               |               |     |     |           |                  |     |         |      | Task1    |     | Task2    |     | Task3 |     |
| correspondinggroundtruth.Thefunction𝐶𝐸 |               |               |     |     |           | denotesthecross  |     | Dataset |      |          |     |          |     |       |     |
|                                        |               |               |     |     |           |                  |     |         | #Pos | #Neg#Pos |     | #Neg#Pos |     | #Neg  |     |
entropylossbetweenpredictionscoreandgroundtruth,whichis
|     |     |     |     |     |     |     |     | TrainingSet | 56  | 9,908 | 96  | 9,868 | 64  | 9,900 |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ----- | --- | ----- | --- | ----- | --- |
calculatedas:
|             |           |                          |                        |     |                       |     |     | TestSet | 85  | 8,505 | 65  | 8,525 | 43  | 8,547 |     |
| ----------- | --------- | ------------------------ | ---------------------- | --- | --------------------- | --- | --- | ------- | --- | ----- | --- | ----- | --- | ----- | --- |
|             | 𝐶𝐸(𝑌,𝑃)=𝑌 |                          | ·log(𝑃)+(1−𝑌)·log(1−𝑃) |     |                       |     | (5) |         |     |       |     |       |     |       |     |
| Recallthat𝑌 |           | representsthelabelfor𝑖𝑡ℎ |                        |     |                       |     |     |         |     |       |     |       |     |       |     |
|             | 𝑚𝑖        |                          |                        |     | machine,andwemultiply |     |     |         |     |       |     |       |     |       |     |
thelossby𝑌
|     | 𝑚𝑖  | sinceweonlytraindiskswhenthecorresponding |     |     |     |     |     | 4.2 Datasets |     |     |     |     |     |     |     |
| --- | --- | ----------------------------------------- | --- | --- | --- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- |
machineindeedcontainsfailuredisks.
|       |                      |     |                                |     |     |     |     | 4.2.1 IndustrialDataset. |     | InMicrosoft365onlineservicesystem, |     |     |     |     |     |
| ----- | -------------------- | --- | ------------------------------ | --- | --- | --- | --- | ------------------------ | --- | ---------------------------------- | --- | --- | --- | --- | --- |
| 3.5.2 | Hierarchy-awareloss. |     | Thehierarchy-awarelossisbelow: |     |     |     |     |                          |     |                                    |     |     |     |     |     |
severalteamsfocusondiskproblems.TeamAfocusesonphysical
|     |     |     |     | 𝑁   |     |     |     | diskerrors,suchasagingofdisks,missingfieldsoffilesystems |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
1 ∑︁
L𝑚 =− 𝐶𝐸(𝑌 ,𝑃 ) anddamagetoread-writeheaders.WhileteamBcaresmoreabout
|     |     |     | 𝑁   |     | 𝑚𝑖 𝑚𝑖 |     | (6) |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
I/Olatency,whichisusuallycausedbyoverload.Weregarddisk
𝑖=1
3442

KDD’22,August14–18,2022,Washington,DC,USA YudongLiuetal.
Table3:ComparativeresultsofvariousdiskfailurepredictionmodelswithandwithoutMTHConindustrydata.Notethatsingle
denotessingle-task,multidenotesusingmulti-taskmechanism,andhierarchydenotesusinghierarchy-awaremechanism.
Task-1 Task-2
Approach
Precision Recall F1-score Precision Recall F1-score
single-LSTM[34] 69.59% 65.37% 67.41% 65.13% 58.62% 61.71%
multi-LSTM 66.53% 70.56% 68.49% 67.84% 59.66% 63.49%
single-hierarchy-LSTM 74.29% 67.53% 70.75% 70.90% 59.80% 64.88%
multi-hierarchy-LSTM 75.71% 68.83% 72.11% 75.44% 59.31% 66.41%
single-RNN[32] 62.93% 70.56% 66.53% 62.66% 50.34% 55.83%
multi-RNN 63.57% 71.00% 67.08% 71.23% 52.07% 60.16%
single-hierarchy-RNN 67.87% 73.16% 70.42% 61.74% 56.21% 58.84%
multi-hierarchy-RNN 72.00% 70.13% 71.05% 70.04% 54.83% 61.51%
single-Trans[16] 63.77% 73.16% 68.15% 63.39% 55.52% 59.19%
multi-Trans 64.31% 74.89% 69.20% 66.12% 55.17% 60.15%
single-hierarchy-Trans 65.67% 76.19% 70.54% 62.37% 61.72% 62.05%
multi-hierarchy-Trans 67.57% 75.76% 71.43% 67.97% 60.00% 63.74%
single-TCNN[28] 68.42% 67.53% 67.97% 59.41% 55.52% 57.40%
multi-TCNN 69.78% 67.97% 68.86% 58.42% 61.03% 59.70%
single-hierarchy-TCNN 65.87% 71.86% 68.84% 61.31% 57.93% 59.57%
multi-hierarchy-TCNN 70.80% 69.26% 70.02% 58.02% 64.83% 61.24%
failurepredictionforeachteamasatask.Differentfrompublic prediction.ThepublicAlidatacontainsthetimestamp,serialnum-
datasetswhichdonotcontainmachine-levelinformation,disksin ber,diskmanufacturer,diskmodel,normalizedSMARTattributes,
Microsoft365onlineservicesystemsaredeployedonmachines, rawSMARTattributesandfaulttypeofeachdisk.Werandomly
andeachmachinecontainsanumberofdisks.Diskdataisinthe selectthreetasksaccordingtothefaulttype,allofwhichareto
format of SMART and the attributes are collected hourly. Note predictthespecifictypeofdiskfailure.Weadoptthedatasetfrom
thatthemachine-levelinformationisincludedinourdataset.We July2017toFebruary2018asthetrainingset,andtreatMarch2018
predictthefailurestatusofdisksbasedonthelatest72-hourdata. toJuly2018asthetestset.Moredetailedinformationforthepublic
WecollectonlinedatafromtwoteamsfromJune2021toDecember datasetislistedinTable2.
2021,whichcontainsmillionsofdisks.Wetreatthefirstfive-month Thetwodatasetsabovearebothcollectedonadailybasis.We
dataasthetrainingsetandthelastmonthasthetestset. useconsecutive30daysofSMARTdataofeachdiskfollowingthe
standardpractice3.Specifically,weremoveall-emptyfeaturesand
4.2.2 PublicDatasets.
single-valuedfeaturesfromtherawSMARTattributes,andtake
BackblazeDataset: Backblaze1[3]takesasnapshotofeachop- therestasthefinalrepresentationofdisk.
erationalharddrive,whichincludesbasicdriveinformationinthe
4.3 ExperimentalResults
formatofSMARTstatistics.Itcontainsthree-yeardata(October
2018toJune2021),whereeachfeaturevectorcontainstimestamp, 4.3.1 IndustrialDataset. WeimplementMTHConMicrosoft365
diskID,VendorID,SMARTattributes.Wedividethewholedata onlineservicesystems,andTable3presentsthecomparativeresults
bythemodelfieldthatdenotesdifferentmanufacturers,andregard ofMTHCwithitscorrespondingsinglemodelofstate-of-the-art
diskfailurepredictionforeachmanufacturerasonetask.Weexpect competitors on the dataset. To explore the effectiveness of two
toenhancethefailurepredictionaccuracyforeachtypeofmanufac- mechanismsofMTHC,weconductexperimentsforeachmecha-
turerviamulti-tasklearning.WetreatthedatafromOctober2018 nism.
toSeptember2019asthetrainingsetandthedatafromOctober Basedononlymulti-taskmechanism,fourapproachesalloutper-
2019toJune2021asthetestset.Moredetailedinformationforeach formsoneswithsingletask.Specifically,fortask1(physicaldisk
datasetispresentedinTable1. errors),multi-taskmechanismexceedssingletaskbyanaverage
AliDataset:weadoptthepubliclyavailableAli2dataset,areal
of0.89percentofF1score,and2.34percentofF1scorefortask2
industrialdatacollectedbytheAlibabaCloud’sdatacentersand (I/Olatency).Theresultdemonstratestheeffectivenessandrobust-
widelyusedtoevaluatetheperformanceofmethodsfordiskfailure nessofmulti-taskmechanism.Besides,wenoticethattask2(I/O
1https://www.backblaze.com/b2/hard-drive-test-data.html 3https://tianchi.aliyun.com/competition/entrance/231775/information?lang=en-us
2https://tianchi.aliyun.com/dataset/dataDetail?dataId=70251 4https://tianchi.aliyun.com/competition/entrance/231775/rankingList/1
3443

Multi-taskHierarchicalClassificationforDiskFailurePredictioninOnlineServiceSystems KDD’22,August14–18,2022,Washington,DC,USA
Table4:Comparativeresultsofvariousdiskfailurepredictionmodelswithsingle-taskandmulti-taskonBackBlazeDataset.
Task-1 Task-2 Task-3
Approach
Precision Recall F1-Score Precision Recall F1-Score Precision Recall F1-Score
single-LSTM[34] 88.00% 75.86% 81.48% 82.69% 79.63% 81.13% 71.43% 67.31% 69.31%
multi-LSTM 88.46% 79.31% 83.64% 90.11% 75.93% 82.41% 80.00% 69.23% 74.23%
single-RNN[32] 82.61% 65.52% 73.08% 92.31% 77.78% 84.42% 69.31% 60.31% 67.31%
multi-RNN 91.30% 72.41% 80.77% 94.31% 76.85% 84.69% 77.78% 67.31% 72.16%
single-Trans[16] 95.24% 68.97% 80.00% 89.36% 77.78% 83.17% 75.56% 65.38% 70.10%
multi-Trans 95.46% 72.41% 82.35% 88.54% 78.70% 83.33% 86.84% 63.46% 73.33%
single-TCNN[28] 81.82% 62.07% 70.59% 91.95% 74.07% 82.05% 68.89% 59.62% 63.92%
multi-TCNN 80.00% 68.97% 74.07% 93.27% 76.85% 84.26% 76.32% 55.77% 64.44%
Table5:Comparativeresultsofvariousdiskfailurepredictionmodelswithsingle-taskandmulti-taskonAliDataset.Notethat
duetothedifficultyofalltasksonthisdataset,thepredictionresultsinthisdatasetarelow.Thefirstontheleaderboardonly
achieves49.07%F1-score4.
Task-1 Task-2 Task-3
Approach
Precision Recall F1-Score Precision Recall F1-Score Precision Recall F1-Score
single-LSTM[34] 39.80% 45.88% 42.62% 42.11% 61.54% 50.00% 40.00% 46.51% 43.01%
multi-LSTM 38.57% 63.53% 48.00% 37.76% 83.53% 51.92% 45.24% 44.19% 44.71%
single-RNN[32] 39.17% 55.29% 45.85% 38.81% 80.00% 52.26% 39.34% 55.81% 46.15%
multi-RNN 37.59% 58.82% 45.87% 39.53% 78.46% 52.58% 48.94% 53.49% 51.11%
single-Trans[16] 35.77% 51.76% 42.31% 42.48% 73.85% 53.93% 50.00% 46.51% 48.19%
multi-Trans 40.68% 56.47% 47.29% 41.67% 76.92% 54.05% 46.30% 58.14% 51.55%
single-TCNN[28] 42.45% 52.94% 47.12% 34.65% 67.69% 45.83% 48.89% 51.16% 50.00%
multi-TCNN 46.08% 55.29% 50.27% 35.16% 69.23% 46.63% 60.00% 48.84% 53.85%
latency)obtainsmuchmoreenhancementthantask1(physicaldisk singletaskbyanaverageof3.64percentofF1score,and4.69per-
errors).Becausediskswithphysicaldiskerrorscouldusuallylead centofF1scorefortask2(I/Olatency).NotedthattheF1-scoreof
tohighI/Olatency,whichhelpimprovetheperformanceoftask onlinediskfailurepredictionisusuallylow,anditisnoteasyto
2.Incontrast,diskswithhighI/Olatencydonotalwaysindicates improveitduetoseverelymissingdataandextremedataimbalance
physicalerrors,whichareusuallycausedbyoverload. probleminpractice[16].
Basedononlyhierarchy-awaremechanism,fourapproaches Inall,MTHCbasedapproachessignificantlyoutperformscorre-
exceedoneswithsingletaskbyalargemargin.Specifically,fortask spondingsingle-modelones,whichdemonstratestheeffectiveness
1(physicaldiskerrors),thehierarchy-awaremechanismexceeds androbustnessofourMTHC.
thesingletaskbyanaverageof2.62percentofF1score,and2.80
percentofF1scorefortask2(I/Olatency).Theresultdemonstrates
4.3.2 PublicDatasets. Wealsousethepublicdatasets(theBack-
thathierarchy-awaremechanismreducestheimbalanceproblem
blazeandAlidatasets)toevaluatetheperformanceoftheproposed
ofpositiveandnegativesamplesandenhancestheperformanceof
approach.Notethatweonlyevaluatethemulti-taskmechanism
diskfailurepredictionviahierarchicalclassification.Inaddition,
hereduetothemissingofmachine-levelinformationinthedatasets.
comparedtomulti-taskmechanism,hierarchy-awaremechanism
TheresultsontheBackblazedatasetarepresentedinTable4.All
obtainscomparableimprovementfortask1(physicaldiskerrors)
themulti-taskbasedapproachesoutperformcorrespondingsingle-
and task 2 (I/O latency). Because disk infrastructures from two
taskones.Onaverage,multi-taskbasedapproachesachievestheF1-
teamsareveryisomorphic,i.e.,hierarchical,andthemachinesfrom
scorevalueswith80.21%,83.67%and71.04%,whichare3.92%,0.98%
bothteamscontainanumberofdisks.
and3.38%greaterthancorrespondingsingle-taskapproachforeach
Combiningmulti-taskmechanismandhierarchy-awaremecha-
task.Inaddition,accordingtoTable4,Task1andTask3contain
nism,theperformanceofdiskfailurepredictionisfurtherenhanced.
fewer positive samples than the Task 2, while the performance
Specifically,fortask1(physicaldiskerrors),MTHCModuleexceeds
enhancementofTask1andTask3ishigherthanthatofTask2.
3444

KDD’22,August14–18,2022,Washington,DC,USA YudongLiuetal.
Thisdemonstratesthatmulti-taskarchitectureisverysuitablefor 5.2 LessonsLearned
thefailurepredictiontaskwithfewpositivesamples. DuringthedeploymentofMTHC,wefoundthatmissingdatais
The results on the Alibaba Cloud’s dataset are shown in Ta- aseriousproblemthatcanleadtopoorpredictionmodelperfor-
ble5.Thefourmulti-taskbasedapproachesexceedcorresponding mance.Missingdataisfrequentlycausedbypoordatacollection
single-taskonesbyalargemargin.Onaverage,multi-taskbased andtransmissionquality.Besides,whenadiskisunhealthy,itmay
approachesachievestheF1-scorevalueswith47.86%,51.30%and failtoprovideSMARTdata,whichmightsignalafailuredueto
50.31%,whichare3.38%,0.79%and3.47%greaterthancorrespond- missingdata.Inotherwords,wecanutilizedatamissingtopredict
ingsingle-taskapproachforeachtask.Itisnotedthattheresult failures.However,wecurrentlyjustpopulatezerobasedonthe
ofvariousmethodsforAlibabaCloud’sdataarealllowduetothe standardprocessingofdiskfailureprediction.Inthefuture,weaim
difficultyofthedataset.Thefirstontheleaderboardonlyachieves tohandlethemissingdatasystematically.
theF1-scorevaluewith49.07%4.
6 RELATEDWORK
5 DEPLOYMENTANDDISCUSSION
6.1 Diskfailureprediction
Inthissection,weintroducethedeploymentofourMTHCand
Inrecentyears,asdiskfailureshavereceivedincreasingattention,
lessonslearned.WehaverunourMTHCpipelineonM365large
manymethodsofdiskfailurepredictionhavebeenproposed.These
scaleonlineservicesystems,whichcontainsmillionsofdisksto
methodscanberoughlydividedintotwocategories:traditional
serveahugenumberofcustomers.Thewholepipelineisrunon
machinelearningbasedanddeeplearningbased.
Azuredatabrick,whichconsistsofthreephases:datafetchingphase,
To improve the prediction performance, traditional machine
dataprocessingphaseandmodelprocessingphase.
learning-basedmodelssuchassupportvectormachines[34]and
tree-basedmachinelearningmodels[5,12,13,27,33]utilizeSMART
datafordiskfailureprediction.However,thesetraditionalmachine
5.1 Deployment learningbasedapproachescan’thandlethetemporalinformation
Datafetchingphase:Inthisphase,serviceSmart_ctl iscalled well[28],whiledeeplearningbasedapproachescanmakebetter
hourlytocollectSMARTdatafromeachserverintwoteams.The useofthetemporalinformation.Deeplearningbasedapproaches,
collectedSMARTdataisstoredinAzure,andistransferredbya includingrecurrentneuralnetwork(RNN)[32],longshort-term
distributedandreliablestreamingdatamovingtooltoensurethe memory(LSTM)[34]andtemporalconvolutionalneuralnetwork
consistenceandcompletenessofdata. (TCNN) [28], perform better than traditional machine learning
Dataprocessingphase:Thisphasecontainsdatacleaningand basedonesfordiskfailureprediction.
featureengineering.Datacleaningisfirstlyscheduledtodealwith Comparedtoexistingdiskfailurepredictionapproacheswhich
missingdata.Thenfeatureengineeringjobsarescheduledtoobtain donotfocusonspecificfailuretypes,ourproposedMTHCframe-
diskfeaturevectors[26,29],whicharetheinputofMTHC.Fea- workintegratesdisksfromeachteamandutilizemulti-tasklearning
tureengineeringjobscontainseveraloperations,suchasfiltering toenhancetheperformanceforeachsingletaskandintroduces
irrelevantattributes,concatenatingdifferenttypeofattributes,and anovelnodehierarchicalclassificationapproachtodealwiththe
appendingmachine-levelinformationfordisks.Weacceleratethe extremedataimbalanceofdiskfailurepredictionproblem.Note
featureengineeringprocessviaSpark. thatourproposedMTHCisorthogonalwithpreviousmodels,i.e.,
Modelprocessingphase:Inthisphase,weutilizediskfeature itcanbeveryeasilytointegratedpreviousmodelsintoMTHCand
vectorsobtainedindataprocessingphaseandtrainthediskfailure enhancestheperformanceofdiskfailureprediction.
predictiontaskswithMTHCLSTMmodel.Thetrainedmodelgives
thefailurescoresforeachdiskandeachtask.Notethateachtask
6.2 Multi-tasklearning
onlyfocusesonthecorrespondingfailuretype.Diskswithhigh
failureprobabilityarestoredinAzureTable.Engineersfromeach Multi-tasklearninghasbeenusedsuccessfullyacrossmanyapplica-
teamqueryhalfanhourandselectdiskswithcorrespondinghigh tionsofmachinelearning,fromnaturallanguageprocessing[8]and
failureprobabilityfromAzureTableandtakeproactiveactions. speechrecognition[10]tocomputervision[23]anddrugdiscovery
Forexample,teamAcouldselectdiskswithhighphysicalerror [22,24].Andtherearemanyopportunitiesformulti-tasklearning
probabilityandtransferthedataonthediskstohealthyones,i.e., onreal-worldproblems[6].Inareasofmulti-tasklearning,shared
livemigration. representationsareutilizedtoexplorecommonpatternsamonga
ToevaluatetheeffectivenessofMTHCfromthebusinessimpact collectionofrelatedtasks.Comparedtotrainingthemodelssep-
pointofview,weemployA/Btestingtomeasurethenumberof arately,thesesharedrepresentationscanhelpimprovelearning
virtualmachineinterruptionssavedthroughproactivemitigation efficiencyandpredictionaccuracyforthetask-specificmodels.[6].
basedon failureprediction signals. According tothe testingre- Inthecontextofdeeplearning,themethodsofmulti-tasklearn-
sult,comparedtosingle-taskbasedapproach,ourproposedMTHC ing [24, 35, 36] can be divided into two groups: soft parameter
notablyreducedthenumberofvirtualmachineinterruptionsper sharing and hard parameter sharing. In soft parameter sharing,
monthforM365onlineservicesystems,whichwasofgreatenhance- eachtaskmaintainsitsownmodelwithitsownparameters,and
mentfortheservicereliabilityofM365onlineservicesystemsand thedistancebetweenthemodelparametersofdifferenttasksregu-
broughtconsiderablebenefits. larizedinordertoencouragetheparametersfromdifferenttasks
3445

Multi-taskHierarchicalClassificationforDiskFailurePredictioninOnlineServiceSystems KDD’22,August14–18,2022,Washington,DC,USA
tobesimilar[9].Comparedtosoftparametersharing,hardparam- [14] SidiLu,BingLuo,TirthakPatel,YongtaoYao,DeveshTiwari,andWeisongShi.
etersharingmethodssharethehiddenlayers(i.e.,representations) 2020. MakingDiskFailurePredictions{SMARTer}!.InProceedingsofFAST.
151–167.
amongtaskswhilekeepingtask-specificoutputlayersforeach [15] SidiLu,BingLuo,TirthakPatel,YongtaoYao,DeveshTiwari,andWeisongShi.
task.Andthelossfunctionforhardparametersharingistypically 2020.MakingDiskFailurePredictionsSMARTer!.InProceedingsofFAST.USENIX
Association,151–167.
acombinationofmultiplelossfunctionscorrespondingtomultiple
[16] ChuanLuo,PuZhao,BoQiao,YoujiangWu,HongyuZhang,WeiWu,Weihai
tasks.Comparedtosoftparametersharing,hardparametersharing Lu,YingnongDang,SaravanakumarRajmohan,QingweiLin,andDongmei
greatlyreducestheriskofoverfitting[4],andourMTHCutilizes Zhang.2021.NTAM:Neighborhood-TemporalAttentionModelforDiskFailure
PredictioninCloudPlatforms.InProceedingsofWWW.1181–1191.
hardparametersharing. [17] AoMa,FredDouglis,GuanlinLu,DarrenSawyer,SurendarChandra,andWind-
sorW.Hsu.2015. RAIDShield:Characterizing,Monitoring,andProactively
7 CONCLUSION ProtectingAgainstDiskFailures.InProceedingsofFAST.USENIXAssociation,
241–256.
Diskfailureisoneofthemostfrequentlyfailingcomponentsin [18] IoannisManousakis,SriramSankar,GreggMcKnight,ThuD.Nguyen,andRi-
onlineservicesystems,whichcouldreducetheservicereliability. cardoBianchini.2016.EnvironmentalConditionsandDiskReliabilityinFree-
cooledDatacenters.InProceedingsofATC.USENIXAssociation.
Diskfailurepredictionhasbeenattractingextensiveattention.In [19] JustinMeza,QiangWu,SanjeevKumar,andOnurMutlu.2015.ALarge-Scale
thispaper,weproposeaMulti-TaskHierarchyClassificationframe- StudyofFlashMemoryFailuresintheField.InProceedingsofSIGMETRICS.
177–190.
worknamedMTHCfordiskfailureprediction,whichconsistsof
[20] MollyS.Quinn,KatherineCampbell,andMarkT.Keane.2019.TheExpected
twomainmechanisms,i.e.,multi-taskmechanismandhierarchy- Unexpected&UnexpectedUnexpected.InProceedingsofCogSci.2627–2633.
awaremechanism.Comparedtoexistingapproacheswhichdonot [21] JackW.Rae,AnnaPotapenko,SiddhantM.Jayakumar,andTimothyP.Lilli-
crap.2020.CompressiveTransformersforLong-RangeSequenceModelling.In
focusonspecificfailuretypes,weemphasizethatdifferentteams
ProceedingsofICLR.
focusesondifferenttypesofdiskfailuresinrealpractice.Multi-task [22] BharathRamsundar,StevenKearnes,PatrickRiley,DaleWebster,DavidKonerd-
mechanismintegratesdisksfromeachteamandutilizemulti-task ing,andVijayPande.2015.Massivelymultitasknetworksfordrugdiscovery.
[23] ShaoqingRen,KaimingHe,RossGirshick,andJianSun.2015. Fasterr-cnn:
learningtoenhancetheperformanceforeachsingletask.Moreover, Towardsreal-timeobjectdetectionwithregionproposalnetworks.Advancesin
hierarchy-awaremechanismintroducesanovelnodehierarchical NeuralInformationProcessingSystems28.
[24] SebastianRuder.2017. AnOverviewofMulti-TaskLearninginDeepNeural
classificationapproachtodealwiththeextremedataimbalanceof
Networks.CoRRabs/1706.05098.
diskfailurepredictionproblem.Ourexperimentsonbothindustrial [25] SriramSankar,MarkShaw,KushagraVaid,andSudhanvaGurumurthi.2013.
andpublicdatasetsdemonstratethatmulti-taskbasedapproaches DatacenterScaleEvaluationoftheImpactofTemperatureonHardDiskDrive
Failures.ACMTransactionsonStorage9,2,1–24.
achievemuchbetterperformancethancorrespondingsingle-task
[26] HuasongShan,YuanChen,HaifengLiu,YunpengZhang,XiaoXiao,XiaofengHe,
basedones.Further,experimentsalsodemonstratethathierarchy- MinLi,andWeiDing.2019.𝜖-Diagnosis:UnsupervisedandReal-timeDiagnosis
awaremechanismcanalleviatetheimbalanceproblemandenhance ofSmall-windowLong-tailLatencyinLarge-scaleMicroservicePlatforms.In
ProceedingsofWWW.3215–3222.
theperformanceofvariousdiskfailurepredictionapproaches. [27] JingShen,JianWan,Se-JungLim,andLifengYu.2018.Random-Forest-Based
FailurePredictionforHardDiskDrives. InternationalJournalofDistributed
REFERENCES SensorNetworks14,11.
[28] XiaoyiSun,KrishnenduChakrabarty,RuiruiHuang,YiquanChen,BingZhao,
[1] BruceAllen.2004.MonitoringHardDiskswithSMART.LinuxJournal. HaiCao,YinheHan,XiaoyaoLiang,andLiJiang.2019.System-LevelHardware
[2] DaniloArdagna,BarbaraPanicucci,andMauroPassacantando.2011.AGame FailurePredictionusingDeepLearning.InProceedingsofDAC.20.
TheoreticFormulationoftheServiceProvisioningProbleminCloudSystems.In [29] AmoghavarshaSureshandAnshulGandhi.2019.UsingVariabilityasaGuiding
ProceedingsofWWW.177–186. PrincipletoReduceLatencyinWebApplicationsviaOSProfiling.InProceedings
[3] Backblaze.2019. TheBackblzaeHardDriveDataandStats. https://www. ofWWW.1759–1770.
backblaze.com/b2/hard-drive-test-data.html. [30] AshishVaswani,NoamShazeer,NikiParmar,JakobUszkoreit,LlionJones,
[4] JonathanBaxter.1997.ABayesian/informationtheoreticmodeloflearningto AidanN.Gomez,LukaszKaiser,andIlliaPolosukhin.2017. AttentionisAll
learnviamultipletasksampling.Machinelearning28,1,7–39. youNeed.InProceedingsofNIPS.5998–6008.
[5] MirelaMadalinaBotezatu,IoanaGiurgiu,JasminaBogojeska,andDorothea [31] ChangjunWang,WeidongMa,TaoQin,XujinChen,XiaodongHu,andTie-Yan
Wiesmann.2016.PredictingDiskReplacementtowardsReliableDataCenters.In Liu.2015. SellingReservedInstancesinCloudComputing.InProceedingsof
ProceedingsofKDD.39–48. IJCAI.224–231.
[6] RichCaruana.1997.Multitasklearning.Machinelearning28,1,41–75. [32] ChangXu,GangWang,XiaoguangLiu,DongdongGuo,andTie-YanLiu.2016.
[7] YujunChen,XianYang,QingweiLin,HongyuZhang,FengGao,ZhangweiXu, HealthStatusAssessmentandFailurePredictionforHardDriveswithRecurrent
YingnongDang,DongmeiZhang,HangDong,YongXu,HaoLi,andYuKang. NeuralNetworks.IEEETransactionsonComputers65,11,3502–3508.
2019.OutagePredictionandDiagnosisforCloudServiceSystems.InProceedings [33] YongXu,KaixinSui,RandolphYao,HongyuZhang,QingweiLin,YingnongDang,
ofWWW.2659–2665. PengLi,KecengJiang,WenchiZhang,Jian-GuangLou,MuraliChintalapati,and
[8] RonanCollobertandJasonWeston.2008.Aunifiedarchitecturefornaturallan- DongmeiZhang.2018. ImprovingServiceAvailabilityofCloudSystemsby
guageprocessing:Deepneuralnetworkswithmultitasklearning.InProceedings PredictingDiskError.InProceedingsofATC.USENIXAssociation,481–494.
ofICML.160–167. [34] JianguoZhang,JiWang,LifangHe,ZhaoLi,andPhilipS.Yu.2018. Layer-
[9] MichaelCrawshaw.2020.Multi-TaskLearningwithDeepNeuralNetworks:A wisePerturbation-BasedAdversarialTrainingforHardDriveHealthDegree
Survey.ArXivabs/2009.09796. Prediction.InProceedingsofICDM.1428–1433.
[10] LiDeng,GeoffreyHinton,andBrianKingsbury.2013.Newtypesofdeepneural [35] YuZhang.2015.Multi-TaskLearningandAlgorithmicStability.InProceedingsof
networklearningforspeechrecognitionandrelatedapplications:Anoverview. AAAI.3181–3187.
InProceedingsofICASSP.IEEE,8599–8603. [36] YuZhangandQiangYang.2017. ASurveyonMulti-TaskLearning. CoRR
[11] ChenyouFan,YuzeZhang,YiPan,XiaoyueLi,ChiZhang,RongYuan,DiWu, abs/1707.08114.
WenshengWang,JianPei,andHengHuang.2019.Multi-HorizonTimeSeries [37] YingZhao,XiangLiu,SiqingGan,andWeiminZheng.2010. PredictingDisk
ForecastingwithTemporalAttentionLearning.InProceedingsofKDD.2527– FailureswithHMM-andHSMM-BasedApproaches.InProceedingsofICDM.
2535. 390–404.
[12] XiaohongHuang.2017. HardDriveFailurePredictionforLargeScaleStorage [38] BingpengZhu,GangWang,XiaoguangLiu,DianmingHu,ShengLin,andJingwei
System.Ph.D.Dissertation.UCLA. Ma.2013.ProactiveDriveFailurePredictionforLargeScaleStorageSystems.In
[13] JingLi,XinpuJi,YuhanJia,BingpengZhu,GangWang,ZhongweiLi,andXi- ProceedingsofMSST.1–5.
aoguangLiu.2014.HardDriveFailurePredictionUsingClassificationandRe-
gressionTrees.InProceedingsofDSN.383–394.
3446