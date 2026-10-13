Resilient Microservice Applications, by
Design, and without the Chaos
Christopher S. Meiklejohn
CMU-S3D-24-104
May 2024
SoftwareandSocietalSystems
SchoolofComputerScience
CarnegieMellonUniversity
Pittsburgh,PA15213
ThesisCommittee:
HeatherMiller,Chair
ClaireLeGoues
RohanPadhye
PeterAlvaro(UniversityofCalifornia,SantaCruz)
Submittedinpartialfulfillmentoftherequirements
forthedegreeofDoctorofPhilosophyinSoftwareEngineering.
Copyright©2024ChristopherS.Meiklejohn
ThisresearchwassponsoredbytheBoozAllenHamiltonaward,aSoftwareEngineeringEducation
Fundfellowship,firstyearfundingfromtheDeanandS3DdepartmentalfundingfromtheSoftware
andSocietalSystemsDepartmentintheSchoolofComputerScienceatCarnegieMellonUniversity.
The views and conclusions contained in this document are those of the author and should not
beinterpretedasrepresentingtheofficialpolicies,eitherexpressedorimplied,ofanysponsoring
institution,theU.S.governmentoranyotherentity.

Keywords: fault prevention, fault injection, faulttolerance, microservice archi-
tectures,microservices,testing,circuitbreakers,remoteprocedurecall,RPC

iii
Abstract
Faultinjectiontestingisvitalforassessingtheresilienceofdistributedmi-
croserviceapplicationsagainstinfrastructureanddownstreamservicefailures.
Typicallyperformedinproduction,wherecustomersmaybeadverselyaffected
bythistesting,itoftenfailstoidentifyapplicationbugs,particularlyinfrequent
ones or those which only affect a subset of customers. While academics rec-
ognizetheproblemofresiliencebugdetection,indevelopment,andpriorto
deploymentofapplicationcodetoproduction,theirresearchhasbeenlimited
byaccesstoindustrialapplications,whichhasresultedinsolutionsthatmayor
maynotbefullyalignedwiththeindustry’sneeds.
This dissertation demonstrates that these types of resilience bugs can be
identifiedduringdevelopment,andbeforedeploymentofapplicationcodetoproduction,
throughtheuseofadeveloper-centricfaultinjectiontechniqueandaprincipled
approachtomicroserviceapplicationtesting. Itthendemonstratesthatitcan
be done in a manner that does align with industrial practitioner’s needs by
co-evolving this fault injection technique and principled approach with an
industrialpartner,oneofthelargestfooddeliveryservicesintheUnitedStates,
whichresultsinthediscoveryofdeep,previouslyundiscovered,resiliencebugs
intheirapplication.
This dissertation begins by first constructing a microservice application
corpusandintroducinganoveltracingtechniquethatcapturesallinter-service
communicationinamicroserviceapplication. Combinedwiththecorpus,this
tracing technique enables the development of an exhaustive fault injection
testing technique designed specifically for microservice environments. This
techniqueisthenrefinedbyimplementinganoveltestcasereductionstrategy
to minimize the exploration of redundant fault injection scenarios, thereby
increasingtheperformanceandusabilityofthetechnique. Thepracticalityof
thesetechniquesisthenvalidatedusingacasestudytakenfromanindustrial
microservice application. While this case study confirms the fault injection
technique’seffectiveness,itbothhighlightsdeficienciesintheapplicationof
thetechniqueandidentifiesemergentbehaviorthatisinherenttoindustrialmi-
croserviceapplicationsandtheirpiecemealapproachtoapplicationresilience.
Theseobservationsinformthedesignofanewprincipledapproachfortesting
microserviceapplicationsforresilience,whichextendsthefaultinjectiontech-
nique’susabilitybyensuringthatdeveloperswritetestsfortheirapplications
thataresufficientforbugidentification.
Withthisprincipledapproach,itisshownthatdeep,previouslyundiscov-
ered, resilience bugs can be identified in large-scale, industrial microservice
applications,indevelopment,andbeforecodeshipstoproduction.

For argv0.

Acknowledgements
“Thishasallbeenwonderful,butnowI’monmyway.”
Anastasio&Marshall,DownwithDisease
First,Iwanttothankmyparents,Deborah(i.e.,Meiklemom)andGordonfor
first introducing me to the Commodore 64 at the age of (probably) 4, and their
continuedsupportwhenIquitcollegetotakean“Internet”job. Iespeciallywantto
thankthemfortheircontinuedsupportwhenIquitmyseniorsoftwareengineering
jobto goto graduateschool andthemanyHitchcockmarathons, everyChristmas
ontheCriterionChannel: essential foravoidingthe ever-present threatof graduate
schoolburnout. Mostnotably,theyonlycomplainedoncethatIspentallsummer
onIRCasateenager–whentheythreatenedtosendmetoasummercampwhich,
thankfully, never happened – if it had, I would not be writing this today. Thanks
tomysister,Haley,forallofthelaughsandbad80’smusicvideoswehaveshared
overtheyears.
Greg and Laura, what can I say? You both have been in my life for almost as
longasIhavebeenworkingoncomputersprofessionally. Youhavebothbeengreat
friends, and I hope that we can continue to rock out to many live Goose shows
togetherformanymoreyearstocomeeverywherebetweenBostonandPittsburgh,
andbeyond.
ThankstoallofmyformercolleaguesatBashoTechnologieswhobothmentored
and pushed me from a mere JavaScript developer to a accomplished, published
Erlangdeveloper: including,butnotlimitedto: JoeBlomstedt,RussellBrown,Tanya
Cashorali,SeanCribbs,ReidDraper,JoeDevivo,BryanFink,ScottFritchie,Andy
Gross,Jon Meredith,JaredMorrow, JohnMuellerleile,Tom Santero,JustinSheehy,
Brian Sparrow, Andrew Stone, Andrew Thompson, Seth Thomas, Steve Vinoski,
JordanWest,RyanZezeski,anymanymore. Wehadsomeextremetimes,weworked
sohard,but neveroncedid itfeellikework. Notonlydid youteach medistributed
systems,youtaughtmetobuildrobust,tested,distributedsystemsandthatformed
the foundation ofthis dissertation. You alsogave me the first opportunity to speak,
v

vi Acknowledgements
on a large stage, on what I was working on, giving me the visibility I needed to
startablogandactuallypursuemyPh.D.Thankstoeveryonewhowastangential
toBashoTechnologiesintheactorspace: JamieAllen,ReubenBond,JonasBoner,
Sergey Bykov, Roland Kuhn, Philipp Haller, Martin Odersky, and David Pollak.
ThankstoeveryoneatBoundary: C.ScottAndreas,KyleKingsbury,CliffMoonand
manyothers.
Thanks to everyone at Erlang Solutions (and beyond, but in arms reach) for
supportduringmydissertation. ThankstoFrancescoCesarini,JohnHughes,Kon-
stantinos Sagonas, Eric Stenman, andUlf Wigerfor their support during my testing
journey with all things Erlang. Thanks to all the organizers of Erlang Workshop,
Erlang User Conference, and Erlang Factory for helping me get established as a
conferencepresenter,instrumentalinmydevelopmentasaconferencespeaker.
Thanks to everyone in the Clojure “house”: but, most notably Chas Emerick,
and Zach Tellman. Zach, you’ve been a great sounding board for ideas and have
alwayshelpedmecriticallythinkthroughideas.
Ben,thanksforallofthegreattimesinSeattle(PearlJam!) thegreatmeals,and
justgenerallybeingagreatfriend.
Thanks to everyone in the SyncFree consortium for teaching me how to do
industrialresearch,butespecially: CarlosBaquero,AnnetteBieniusa,CarlaFerreria,
MarcShapiro, NunoPregucia. Carla, Iam sorrythatI still haveyourcopyof TAPL,
andIpromisetoreturnittoyoupersonallyifIeverreturntoLisbonforaconference.
Thanksto allofmy fellowgraduatestudentcolleagues: DeepthiDevaki Akkoorath,
ManuelBravo,MaryamDabaghchian,ZhongmaioLi,andmanyothers.
Ale,mySyncFree“workshopbrother”,thiswouldnothavebeenpossiblewithout
you. Ourtimes togetheracross Europeand throughoutseveralMicrosoft Research
internshipswasoneofthehighlightsofmyentirePh.D.experienceand,despitethe
constant friendlybickering, areundoubtedly someof thebest moments ofmy life.
I only wish I could celebrate my Ph.D. defense along the banks of the Seine with
wine,cheese,andbreadwithyou,aswedidforyourPh.D.defense.
Thankyoutobothmymentorsand collaboratorsIhadduringmytimeat Mi-
crosoft Research: Tom Ball, Phil Bernstein, Sebastian Burckhardt, and Jonahthan
Goldstein. IthinkquitefondlyofoursummerstogetherassomeofthebesttimesI
hadduringmyPh.D.experience. Phil,ifyouarereadingthis,Istilloweyouacopy
ofyourownbookthatIdestroyedwithaill-placedcupofwater.
Thanks to all of the academic folks along the way who helped me out either
priortoorafterIstartedmyPh.D.,butmostespecially: PeterBailis,NeilConway,
PatHelland,JoeHellerstein,LindsayKuper,andJeanYang.
Thanksto somanyfolksat BerkleeCollegeof Musicfor givingmethechanceto
beaprogrammer: CliffAnderson,ChrisGiroir,MattHoran,JohnMileham,Patrick
McNeill,andRobertGreen. ThankstomycolleaguesatSwipelyforbootstrapping

vii
andsupportingmyjourneyonsoftwaretestingandgettingmetomyfirstsoftware
conerence: AnthonyAccardi,BarnabyClaydon,BrightFulton,MattGillooly,Simon
Hojberg,andJoshuaNapoli.
Thanks toall of my current colleagues for their support throughoutmy Ph.D.:
MoustafaAly,MattAnger,ArmandoCanals,MaggieFang,JustinLee,Venkatara-
manan Kuppuswamy, Aaron Livingstone, Ivy Liu, Amy Lu, Lev Neiman, Ivan
Radakovic,PatrickSalami,AbhishekSharma,RadhaKrishnaRatnala,RyanSokol,
MattZimmerman,andmanyothers. SpecialthankstoCesareCelozziforhismen-
torship,helpwithunderstandinghowallthepiecesmatter,andbeingsuchangreat
colleagueandfriendoverthepasttwoyears.
ThankstoSargunDhillon,JuliaFusco,MikeKing,CaitieMcCaffery,TylerMc-
Mullen, Carin Nuernberg, Genevieve Patterson, Martine Roudaire-Clipet, Ines
Sombra,andAshleyWilliams.
ThankstomyfirstsetofPh.D.advisors,PeterVanRoyandRodrigoRodrigues.
Whilethe situationmaynothavebeenlogisticallyideal, youhelpedto guidemeto
therightpathonhow tofinishthisPh.D.ThankstoMatthiasFelleisenfor beinga
supportivementor,whoIhadnoaffiliationwith,butwasalwaysopentotalkabout
interestingideasandsupportmeduringmyPh.Djourney.
Thanks to all of my colleagues at Carnegie Mellon University: specifically,
Jonathan Aldrich, who helped get me into program analysis; Ben Titzer, for all
ofyourhorriblesci-fimovierecommendations;ElizabethGilbert,foraskinggood
questionsaboutfaultinjection;MatthewWeidner,forcarryingtheCRDTtorchafter
IburnedthebridgethatIcrossedwithit;andMichaelHiltonforallofhishelpon
becomingabetterteacher. Thankstoallthestaff,butmostnotably: AaronCaldwell,
ConnieHerold,andDabneySchlea.
Zeeshan, boy, we we had some times. Thanks for being there as a sounding
boardformanyyearsduringmyperiodwithourlatenight“Butterjoint”sessions. I
wishyouthebestinyourownPh.D.andwishyougreatsuccess.
ThankstoMichaelIssacAssad,EuniceChen,AndreaEstrada,LydiaStark,Yiwen
Song, Haoyang Wu, and Peter Zhong for their work on Filibuster. Michael, your
workonextendingFilibusterfordatabasetestinghelpedmake Filibusterstronger
andimproveitsownfoundations.
Matt,thanksforbeingsuchagreatfriendandcolleague. Obviously,andasyou
know, before we were colleagues we had some great times together. I still recall
onenight manyyearsago, inSanFrancisco, whenyouwere ponderingif“parallel
grep” was a good interview question and asking everyone if they could solve it.
Sincethen,werecordedmusictogether,debuggeddistributedapplicationstogether,
andnowworkonkeepingthosedistributedsystemsreliablethroughtestingand
improvedmicroservicedesigns.

viii Acknowledgements
Thankstomycommitteefortheirsupport: Rohan,Claire,andPeter. Rohan,you
carriedtotorchonhelpinggetDistributedExecutionIndexingoverthelineand I
appreciatethat. Claire,youhelpedtosolidifythingsandkeepmythesisgrounded
(and,withintime,Ihope.)
Peter, I’m not even sure what to say. Our relationship started as two random
folkswho metat abar inthe Tenderloin for abeer becausea mutualfriend saidwe
should. Sincethen,it’sprogressedfromfriend,toalmostbeingyourfirststudent,
toyou being a memberof my thesiscommittee. We havespent many hourstalking
both in bars and on the phone about distributed systems, to discussing research
directions,andfinallymydissertation. Iconsideryouagreatfriendandoneofthe
best memories in my life is meeting you at Magnolia in the Haight for lunch and
hangingout inthePanhandleaftertalking nothing butcrazy distributedsystems
researchideas. Ionlyhopetocontinueourrelationshipformanymoreyears.
Last,and(obviously)notleast,myadvisorHeather. Heather, wehaveknown
eachotherforaverylongtimenow: evenbeforeyouwereaprofessor,atsummer
schoolinOregon,tenyearsago! Firstoff,Icannotthankyouenoughforgettingme
involved in Curry On organization, which helped me to meet many people who
were very valuable to both my industrial and academic career(s). When I finally
quitBashoduetobadcircumstance,youhelpedmefindpossiblejobopportunities,
and when my first Ph.D. was not going well, you helped me find a way out by
gettingme admittedto Northeastern. Then,weended upat CarnegieMellon, and
when Iarrivedat Pittsburgh, you andDaniel found mea place tostay untilI was
ableto findmy own footing. Sincethen, we have hadalot oflaughsand have done
alotofvaluable,high-impact,workandIcannotthankyouenough. Iwouldnotbe
hereifitwasnotforyou.
To everyone else not mentioned here: I apologize. It has been 10 years since
I started down the path of graduate school, and a decade is a long time where
onedoesnotremembereveryonewhocontributedtoone’slife. Ibarelyremember
everythingthathashappenedmyself.

Contents
| Acknowledgements |     | v   |
| ---------------- | --- | --- |
| Contents         |     | ix  |
| 1 Introduction   |     | 1   |
1.1 ThesisStatement . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
1.2 Contributions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
1.3 Outline . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
| 2 BackgroundandRelatedWork |     | 9   |
| -------------------------- | --- | --- |
2.1 Background . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
2.1.1 MicroserviceArchitectures . . . . . . . . . . . . . . . . . . . . 10
2.1.2 Fault,Failures,andErrorsinMicroservices . . . . . . . . . . . 12
2.1.3 FaultInjection . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
2.2 RelatedWork . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
2.2.1 IndustrialPractices . . . . . . . . . . . . . . . . . . . . . . . . . 14
2.2.2 AcademicLiterature . . . . . . . . . . . . . . . . . . . . . . . . 18
2.3 Takeaways . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
| 3 Microservices: | DependencyTypes | 25  |
| ---------------- | --------------- | --- |
3.1 Audible: HardDependencies . . . . . . . . . . . . . . . . . . . . . . . 27
3.1.1 ApplicationStructure . . . . . . . . . . . . . . . . . . . . . . . . 27
3.1.2 ApplicationBehavior . . . . . . . . . . . . . . . . . . . . . . . . 28
3.2 Netflix: HardandSoftDependencies . . . . . . . . . . . . . . . . . . . 30
3.2.1 ApplicationStructure . . . . . . . . . . . . . . . . . . . . . . . . 31
3.2.2 ApplicationBehavior . . . . . . . . . . . . . . . . . . . . . . . . 31
3.3 Takeaways . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32
| 4 MicroserviceApplicationCorpus |     | 35  |
| ------------------------------- | --- | --- |
4.1 CinemaExamples . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38
ix

x Contents
4.2 IndustryExamples . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40
4.2.1 Audible . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40
4.2.2 Expedia . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 41
4.2.3 Mailchimp . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 41
4.2.4 Netflix . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 42
4.3 Takeaways . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 43
5 45
DistributedExecutionIndexing
5.1 AlgorithmRequirements . . . . . . . . . . . . . . . . . . . . . . . . . . 46
5.2 SynchronousDistributedExecutionIndexing . . . . . . . . . . . . . . . 46
5.2.1 SignaturesAreTooCoarse-Grained . . . . . . . . . . . . . . . 47
5.2.2 IncreasingGranularity: InvocationCountorCallStack . . . . 47
5.2.3 IncreasingGranularity: PathtoInvokingRPC . . . . . . . . . . 51
5.3 AsynchronousDistributedExecutionIndexing . . . . . . . . . . . . . . . 53
5.4 Implementation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 57
5.4.1 DebuggingRepresentation . . . . . . . . . . . . . . . . . . . . . 57
5.4.1.1 ProjectionandPartialOrders . . . . . . . . . . . . . . 58
5.4.2 VerboseandCompactRepresentations . . . . . . . . . . . . . . 59
5.4.3 Assignment . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 59
5.5 Takeaways . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 61
6 63
Service-levelFaultInjectionTesting
6.1 Overview . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 64
6.2 Algorithm . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 66
6.3 FaultInjectionPredicates . . . . . . . . . . . . . . . . . . . . . . . . . . 71
6.4 TestingProcess . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 72
6.5 EncapsulatedServiceReduction . . . . . . . . . . . . . . . . . . . . . . . 73
6.5.1 ServiceEncapsulation . . . . . . . . . . . . . . . . . . . . . . . 73
6.5.2 Algorithm . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 75
6.6 Takeaways . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 75
7 EvaluatingSFIT:Corpus 79
7.1 ExperimentalConfiguration . . . . . . . . . . . . . . . . . . . . . . . . 80
7.2 DistributedExecutionIndexing . . . . . . . . . . . . . . . . . . . . . . . 82
7.2.1 Required: InvocationCount,Stack,andPath . . . . . . . . . . 82
7.2.2 NondeterminismisaProblem . . . . . . . . . . . . . . . . . . . 85
7.2.3 PayloadInclusionDistinguishes . . . . . . . . . . . . . . . . . . 86
7.3 Service-levelFaultInjectionTesting . . . . . . . . . . . . . . . . . . . . . 87
7.3.1 TestsGeneratedandIncreasedCoverage . . . . . . . . . . . . . 87
7.3.2 EncapsulatedServiceReduction . . . . . . . . . . . . . . . . . 89

Contents xi
7.3.3 Mocks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 90
7.3.4 ExecutionTime . . . . . . . . . . . . . . . . . . . . . . . . . . . 90
7.3.5 MisconfiguredTimeouts . . . . . . . . . . . . . . . . . . . . . . 91
7.4 Takeaways . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 92
8 IndustrialMicroservices: Foodly 93
8.1 Foodly . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 94
8.2 HowFoodlyisResilientToFaults . . . . . . . . . . . . . . . . . . . . . 94
8.3 WhyNotChaosEngineering? . . . . . . . . . . . . . . . . . . . . . . . 95
8.4 HowChangesatFoodlyareTested . . . . . . . . . . . . . . . . . . . . 96
8.5 Takeaways . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 97
9 EvaluatingSFIT:InPractice 99
9.1 PhilosophicalChallenges . . . . . . . . . . . . . . . . . . . . . . . . . . 99
9.2 ResultsOverview . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 100
9.3 ExperimentalConfiguration . . . . . . . . . . . . . . . . . . . . . . . . 102
9.3.1 ComponentTests . . . . . . . . . . . . . . . . . . . . . . . . . . 102
9.3.2 Re-implementing Filibuster . . . . . . . . . . . . . . . . . . . . 103
9.3.3 Enabling Filibuster . . . . . . . . . . . . . . . . . . . . . . . . . 106
9.3.4 Configuring Filibuster . . . . . . . . . . . . . . . . . . . . . . . 106
9.4 Socio-TechnicalChallenges . . . . . . . . . . . . . . . . . . . . . . . . . 108
9.4.1 EducationandDocumentation . . . . . . . . . . . . . . . . . . 109
9.4.2 DevelopmentProcesses . . . . . . . . . . . . . . . . . . . . . . 109
9.5 Results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 110
9.6 Takeaways . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 114
10 Microservices: DependencyTypeEvolution 117
10.1 ApplicationStructure . . . . . . . . . . . . . . . . . . . . . . . . . . . . 117
10.2 HardDependencies . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 120
10.3 SoftDependencies . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 120
10.4 LatentResilienceBugs . . . . . . . . . . . . . . . . . . . . . . . . . . . 121
10.5 Takeaways . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 122
11 123
PrincipledService-levelFaultInjectionTesting
11.1 Overviewofp-SFITApproach . . . . . . . . . . . . . . . . . . . . . . . 125
11.2 Componentsofp-SFIT . . . . . . . . . . . . . . . . . . . . . . . . . . . 127
11.2.1 StructuredTestInterface . . . . . . . . . . . . . . . . . . . . . . 129
11.2.2 Behavior-Under-FaultEncodingAPI . . . . . . . . . . . . . . . 129
11.2.3 CompositionalReasoning . . . . . . . . . . . . . . . . . . . . . 130
11.2.4 IDEPlugin . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 132

xii Contents
11.3 Implementation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 132
11.3.1 FailureSpecificationAPI . . . . . . . . . . . . . . . . . . . . . . 133
11.3.2 FaultMatchingAPI . . . . . . . . . . . . . . . . . . . . . . . . . 133
11.3.3 IDEPlugin . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 135
11.3.4 p-SFITTestingProcedure . . . . . . . . . . . . . . . . . . . . . . 138
11.3.4.1 HardDependencySubprocedure . . . . . . . . . . . 143
11.3.4.2 SoftDependencySubprocedure . . . . . . . . . . . . 144
11.4 Takeaways . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 145
| 12 Conclusions |     | 147 |
| -------------- | --- | --- |
12.1 Takeaways . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 151
12.2 Discussion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 153
12.3 Conclusion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 161
| A Using | -SFIT:ATutorial | 163 |
| ------- | --------------- | --- |
p
A.1 SingleAdjustmentExample . . . . . . . . . . . . . . . . . . . . . . . . 163
A.1.1 setupBlock: PerformTestSetup . . . . . . . . . . . . . . . . . . 164
A.1.2 stubBlock: StubDownstreamDependencies . . . . . . . . . . 164
A.1.3 executeTestBlock: WritetheFunctionalTest . . . . . . . . . . 166
A.1.4 assertTestBlock: PerformTestAssertions . . . . . . . . . . . . 166
A.1.5 assertStubBlock: VerifyStubInvocations . . . . . . . . . . . . 167
A.1.6 teardownBlock: PerformTestTeardown . . . . . . . . . . . . . 168
A.1.7 failureBlock: ApplicationFailureBehavior . . . . . . . . . . . 168
A.2 MultipleAdjustmentExample . . . . . . . . . . . . . . . . . . . . . . . 171
A.2.1 UpdatingtheHappyPathTest . . . . . . . . . . . . . . . . . . . 171
A.2.2 UpdatingtheApplication’sFailureBehavior . . . . . . . . . . 173
A.3 AddingAnotherSoftDependency . . . . . . . . . . . . . . . . . . . . 175
A.4 Takeaways . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 175
| B Availability    |     | 177 |
| ----------------- | --- | --- |
| ListofFigures     |     | 180 |
| ListofTables      |     | 182 |
| ListofDefinitions |     | 183 |
| Bibliography      |     | 185 |

Chapter 1
Introduction
“Withoutloveinthedream,it’llnevercometrue.”
Garcia&Hunter,HelpOnTheWay
Microservice architectures are currently the dominant architectural style for
most consumer products and services [HSS23; Hil23; RJ20a; Hig20]. This style
involvesbreakingdownapplicationsintovariousservices,addressingtheneedsof
large-scaledevelopment organizations. Theprimaryaim is to enable developers to
rapidlyiterateoncomplexapplications,oftencomprisingmillionsoflinesofcode,
whileworkingindependentlyattheirownpace[Cel20].
Structurally, microservice architectures resemble monolithic ones, where the
applicationisdividedalongmoduleboundaries,termedservices. Inmicroservice
architectures,theseservicesinteractthroughRemoteProcedureCalls(RPC)across
anetworkinsteadofmethodinvocationswithinasinglecodebaseasinmonolithic
architectures. A critical difference introducedby microservice architectures is the
conceptofpartialfailure. Thisoccurswhenaservicetheapplicationreliesonisdown
orunavailableduringacustomerrequest. Developersoftheseapplicationsmust,
therefore,considerandmanagethesefailurescenarios[Deu94;Wal+96].
To assess how microservice applications behave under fault, industry practi-
tionersincreasinglyusecoarse-grainedfaultinjectionexperimentsonmicroservice
applicationsdeployedinproduction,suchaschaosengineering[RJ20a]. Thispro-
cess involves introducing low-level, infrastructure-specific faults (e.g., dropping
network connections or crashing nodes) into the application and monitoring ap-
plication metrics to see if these faults negatively affect the customer experience.
However,thisapproachhasseveralsignificantdrawbacks:
1.
LatentDefectsAdmitted.
First, this approach admits latent defects into an application that will be de-
1

2 Introduction
ployed into production. These defects may then later be activated and ad-
verselyaffectthecustomerexperiencebeforediscoverythroughfaultinjection
experimentation,ifperformedatall.
2.
Cost-ProhibitiveExperimentation.
Second,withmicroserviceapplicationsgrowingtohundredstothousandsof
services,withsingleend-to-endcustomerrequestscontainingupwardsof100
RPCs,exhaustivenessbecomescost-prohibitive,asmostapproachesusedby
practitionerstodayrelyonmanuallydesignedandexecutedexperiments.
3.
Ambiguous“Correct”ApplicationBehavior.
Third, and finally, any approach based on experimentation where metrics
are observed for bug detection will be insufficient when the metrics are not
designed specifically to capture possible latent application bugs. In short,
coarse-grainedapplicationmetricscannotbeusedasareplacementforactual
assertionsontheexpectedbehavioroftheapplication.
Theseproblemsarefarfromunderstoodbyacademicresearchers;however,pre-
viousresearchonsolvingtheseproblemsdoesexist. Todemonstrate,oneexample
isprovidedforeachofthedrawbacksoftheexperimentationapproach.
1.
LatentDefectsAdmitted.
Heorhiadietal.[Heo+16a]exploredtestingmicroserviceapplications,intheir
entirety,inadevelopmentenvironmentwherefaultscouldbeinjectedfreelyto
identifyresiliencebugsinmicroserviceapplications. However,theirapproach
requiredthatapplicationdevelopersspecifyinternalbehaviorofthesystem
underfault: forexample,howmany timesarequestwouldberetriedunder
fault. In short, instead of verifying application behavior as a result of the
fault, the application is checked for both the presence and correct operation
of internal resilience mechanisms: it leaves open the question of what the
application does when these resilience mechanisms do not work (i.e., RPC
retryfails.)
2.
Cost-ProhibitiveExperimentation.
Alvaro et al. [ARH15a] proposed a smarter approach to exploration where,
using a specification of the application behavior, fault injections would be
targetedat locationsintheapplicationcode likelytotrigger resiliencemech-
anismsand exposeapplication bugs. While this approachwasmechanized
atscale[Alv+16a],itstillreliedonspecificationswritteninaspecificspeci-
ficationlanguageoutsideofthereachofapplicationdevelopersworkingon
new application features. In short, it shifts the burden of manually creating
experimentstocreatingthespecificationsthatwillbechecked.

ThesisStatement 3
3.
Ambiguous“Correct”ApplicationBehavior.
Zhang etal. [Zha+19]proposed anapproachwherebyeach locationwhere
an RPC was made wouldbe automatically subject to a fault injection through
automatictestgeneration. However,thisapproachreliesontheapplication
developerspecificallyencoding,foreachtest,ifthelocalapplicationstatein
theserviceitselfwouldeitherbethesame,different,orsomederivativestate
when a fault was not injected. In short, if no local application state change
were performed due to RPC execution, these faults would have no impact,
makingitpossibletomisslatentapplicationbugsduringtesting.
Whatthispreviousresearch,andmostoftheresearchonthemajorityofmicroser-
vicearchitectures,suffersfromisthelackofanindustrialcorpusandperspectiveto
groundtheresearchinhowactualindustrialmicroserviceapplicationsaredesigned,
developed,maintained, deployed,andoperated[Jam+18a; Was+21a]. Therefore,
tomovetheresearchinmicroserviceapplicationresilienceforwardandshowthat
itis possibletoidentifylatentapplication bugsrelatedtoresiliencein development
andbeforedeployment,thisdissertationadvancesthepreviousworkinmicroser-
viceapplicationresiliencethroughboththedesignandimplementationofanovel
resilience testing technique rooted in actual industrial resilience bugs and a co-
evolution of that technique with an industry partner, Foodly1, which operates a
large microservice application comprised of over 500 services behind one of the
largestfooddeliveryserviceintheUnitedStates[Mic23a].
1.1 Thesis Statement
Themaingoalofthisdissertationistoidentifylatentapplicationbugs,relatedto
theresilience of microservice applications, in development, andbeforedeployment of
codetoproduction. Thisshouldbeperformedautomaticallyandwithoutrequiring
that application developers author a specification, written in a specific specification
language,forthepurposesofresiliencetesting.
Theworkinthisdissertationcontributestowardsthisbytakingadeveloper-centric
approach. First, developers should be able toleverage their existingfunctional test
suite — the test suite they are already writing when building new features — to
identifybugsusingfaultinjectionwithminimaladditionaleffort;noothertestsor
specificationsmustberequired. Second,wheninjectedfaultsprovokefunctional
test failures, application developers should only be required to think of the test
failures in terms of the impact of the fault on application behavior, for example,
asderivations ofthefault-free behaviorofthe application. Third, faultsshouldbe
1Nameanonymized.

4 Introduction
automaticallyinjectedwithoutrequiringthatapplicationdevelopersmanuallycraft
faultscenarios, avoidingsituations wherethe developer “misses”critical scenarios
duetotheoverheadintestcreation. Fourth,applicationdevelopersshouldonlyhave
to run a minimal set of tests for fault scenarios that represent unique, interesting
cases. Fifth,andfinally,applicationdevelopersshouldberequiredtothinkabout
theconsequencesofallinjectedfaults: forexample,whenafaulthasno(observable)
impact,thedevelopermustspecificallyindicatethisisthecasetoavoidintroducing
bugsthatarenotimmediatelyvisibleduringexecution,but may laterhave some
effect. Thisnaturallyleadstothefollowingthesisstatement:
Identification of latent application bugs related to resilience in
Thesis Statement:
microservice applications, in development, and before deployment of code to production,
is possible using a developer-centric approach and can surface critical application bugs
inlarge-scale,industrialmicroserviceapplications.
1.2 Contributions
Tosupportthisstatement,thisdissertationmakesthefollowingcontributions:
• MicroserviceApplicationCorpus.
To ground this dissertation in industrial applications and their bugs, first,
a corpus is constructed from publicly available information on the internet
concerningresiliencebugsinindustrialmicroserviceapplications.
• .
DistributedExecutionIndexing
Next, an algorithm called Distributed Execution Indexing (DEI) is presented
foruniquelyanddeterministicallyidentifying alloftheRPCsexecutedbya
microserviceapplication. Thisalgorithmisfundamentaltoanyfaultinjection
approach, as it guarantees that under repeated(re-)execution of anend-user
request,anyresultingRPCtoservicesinsidethemicroserviceapplicationcan
beidentifiedthesameway.
• .
Service-levelFaultInjectionTesting
Next,afaultinjectiontechniquecalledService-levelFaultInjectionTesting(SFIT)
is presented that leverages the existing functional test suite of a microser-
viceapplication toidentifylatent bugsrelatedtoapplicationresilience. SFIT
leverages DEI as its underlying fundamental technique for performing the
necessaryexhaustivesearchfordemonstratingthatapplicationsarefreefrom
latentbugs.

Outline 5
• forSFIT.
EncapsulatedServiceReduction
Then,SFITisimproveduponbyapplyingadynamictestcasereductionstrat-
egy, called Encapsulated Service Reduction(ESR), that leverages how microser-
vice applications are designed, structurally. ESR is then shown to make a
significantperformanceimprovementintheexecutiontimeofSFIT.
• IndustrialEvaluationofSFIT.
Fromthere,acasestudyisperformedatFoodlythatdemonstratestheweak-
nesses in the SFIT approach. However, despite these weaknesses, SFIT is
showntoidentifyactualbugsinFoodly’slarge-scaleindustrialmicroservice
application.
• .
PrincipledService-levelFaultInjectionTesting
Next,anewtestingprocessispresented,PrincipledService-levelFaultInjection
Testing (p-SFIT), whichimproveson the originaldesign and testing process
of SFIT that avoids the weaknesses presented by ensuring that developers
know precisely when faults are injected and encode specifically what their
applicationshoulddowhenfaultsoccur.
• Filibuster: ImplementationofSFITand -SFIT.
p
Finally,Filibuster, theopen source implementation ofboth SFIT andp-SFIT
is presented. Filibuster is implemented in both Python and Java; supports
Google’s gRPC and Netty’s HTTP for RPC; has an associated IntelliJ IDE
plugin, and is currently in use by many developers daily at Foodly in their
development and continuous integration workflows. This implementation
servesasthefoundationoftheevaluationsofthetechniquesandprocesses
presentedinthisdissertation. Toaccompanytheimplementation,adetailed
tutorialisincludedonhowtoapplyFilibustertoanapplicationmodeledafter
anindustrialapplicationscenariodiscoveredcontainingabugatFoodly.
1.3 Outline
Theremainderofthisdissertationisstructuredasfollows:
• Chapter 2 presents both background material on microservice applications
and work directly related to this dissertation. Background material focuses
onmicroservicearchitecturesandfaultinjection,eachwitharichhistory. Re-
latedworktargetsfaultinjectioninmicroserviceapplicationsanddistributed
data systems to compare the history and techniques between both types of
distributed applications to highlight the deficiencies inherent in microservice
architectureresearch.

6 Introduction
• Chapter3presentstwomotivatingexamples,AudibleandNetflix,thatdemon-
strate the impact of failures on microservice applications and one way that
microserviceapplications handlethose failures. Inthecase of Audible, any
userrequest failsifanyofthedependentmicroservicesare down: these are
referredtoashard dependencies. Inthecase ofNetflix, fallbacksareused to
“compensate”forfailureifarequiredserviceisnon-responsiveorunavailable;
otherwise,therequestfails: thesearereferredtoassoft dependenciesandare
usedtoprovidegracefuldegradationintheeventoffailure.
• Chapter 4 presents this dissertation’s first of two foundational components:
a microservice application corpus. This corpus, constructed from publicly
availableinformationonindustrialmicroserviceapplications,containseight
(8) small synthetic examples demonstrating common microservice request
patternsandfour(4)recreationsofindustrialmicroserviceapplicationswhere
coarse-grainedfaultinjectionexperimentationwasusedtoidentify,orrepro-
duce an application bug related to resilience. This corpus is foundational
because it addresses the deficiencies in academic work on microservice re-
silience: a lack of applications that contain resilience bugs or that employ
resiliencetechniquestoevaluatenewfaultinjectiontechniques.
• Chapter 5 presents the second of two foundational components of this dis-
sertation: an algorithm for identifying RPCs in a microservice application.
This algorithm is necessary, as it enables any fault injection technique for
microservice applications to guarantee that an application has been tested
for all possible faults that might occur concerning its downstream dependent
services.
• Chapter6presentsService-levelFaultInjectionTesting (SFIT),atechniquefor
testing microservice applicationsto identify latent application bugsin devel-
opment before deployment of application code to production. SFIT is one
of two core contributions ofthis thesis and addresses several of the notable
drawbacks with existing academic techniques by taking a developer-centric
approach. SFITisthenoptimizedusingEncapsulatedServiceReduction(ESR).
This test case reduction technique avoids redundant fault injections, where
theapplicationhasalreadyexecutedthesameapplicationbehaviorasaresult
ofanotherfaultinjection.
• Chapter7presentsanevaluationofSFITonthesyntheticmicroserviceapplica-
tioncorpuspresentedin Chapter4. ItisdemonstratedthatSFITcan improve
application coverage by exercising RPC-failure related error handling code
pathsanddiscoveringallbugsseededintothesyntheticapplicationcorpus.

Outline 7
It is demonstrated that SFIT with ESR outperforms SFIT without avoiding the
executionofredundanttestcases.
• Chapter8providesanoverviewoftheindustrialmicroserviceapplicationbe-
hindFoodly,oneofthelargestfooddeliveryservicesintheUnitedStates. This
sectionshows howFoodlytestsits microserviceapplication,deployschanges,
andremainsresilienttofaultsofdownstreammicroservicedependencies.
• Chapter 9 presents an evaluation of SFIT on the industrial microservice ap-
plicationbehindFoodly. ItisshownthatwhileSFITcanbeusedtoidentify
resiliencebugsinindustrialmicroserviceapplications, thesemayremainun-
detectedifdevelopersdonotfollowtheSFITtestingpreciselyandinvestigate
bothalltestfailuresinducedbyfaultinjectionandteststhatdonotfailwhen
fault injectionis not applied. Theresults of this evaluationare then used to
identifychangesintheSFITprocessnecessarytoidentifythesebugs.
• Chapter 10 presents a new application for contribution to the microservice
application corpus, inspired by actual programming patterns used by mi-
croserviceapplicationdevelopersatFoodly. Thisapplicationdemonstrates
howharddependenciesareconvertedintosoftdependencies,wheremicroser-
vice applications employ graceful degradation to avoid suffering from the
impactoffaultsinproductionatruntime.
• Chapter11presentsthedesignofp-SFIT.p-SFITimprovesonSFITbyensuring
thatapplicationdevelopersproperlyencodetheirapplication’sfailurebehavior
intotheirfunctionaltestsusinganintegratedtestingprocesswithSFIT.p-SFIT
issupportedbyanewimplementationofSFITwithanintegratedIDEplugin
thatprovidesapplicationdeveloperswithfeedbackduringtestingonhowto
proceedateachstepofthetestingprocess.
• Chapter 12 presents a conclusion to this dissertation and future directions,
someofwhichhavealreadybeenandareactivelybeingexplored.
Containedintheappendices:
• Appendix A presents a tutorial on using p-SFIT with Filibuster. As p-SFIT
is mainly a testingprocess for application developers, this appendix demon-
strateshowonecanusethetestingprocesstoidentifyanapplication’sbehavior
underfaultthroughinteractivepromptsandsupportingtechnology.
• AppendixBcontainsresourcesonthecontributionsincludedinthisdisserta-
tion,allwhichareavailableasopensource.

Chapter 2
Background and Related Work
“Ihavemyownmethods;butIamhuman,andeverytimeIseesomeoneelse’s
filmsImaybetemptedtotrytheirmethodsinsteadofmyown. Theirsseemso
logical. Idoit,andIfail. Theirmethodsmaybegood,butnotforme.”
AlfredHitchcock
As it is important to frame this work in the context of the state-of-the-art in
microserviceknowledgeandfaultinjectiontechniques,thischapterpresentsthis
dissertation’sbackgroundandrelatedwork.
Inthebackgroundmaterial,itisshownthatwhilemicroserviceapplicationsare
wellunderstoodstructurally inacademicliterature,failureswithinamicroservice
applicationandthepotentialimpact ofthosefailures remainalesserunderstood
phenomenon that has only been recently investigated by a limit set of academic
researchers. Itispositedthatonepossiblelimitingfactorofthisisaccesstoindustrial
microserviceapplications.
In the related work material, it is shown that fault injection testing in industry
and academia is converging: practitioners work at the most coarse level where
manual faults are injected inproduction to identify application bugs, and academic
approaches focus at a granular level where faults are automatically injected on
particularRPC(ormessages),indevelopment,andstatederivationsinapplications
areusedtodetectbugs.
This work is then put in contrast to the rich literature that exists in academia
on testing distributed data systems: where techniques are mechanized, automat-
ically applied, and used to find deep bugs in applications when all services are
homogeneous(i.e.,replicasofoneanother.)
9

10 BackgroundandRelatedWork
2.1 Background
First, it is essential to understand what the existing research in microservice ar-
chitecturesunderstandsaboutfailuresinmicroserviceapplications. Then,several
methodsforinjectingfaultsintomicroserviceapplicationsarepresented.
2.1.1 Microservice Architectures
Microservice architectures primarily improve development velocity, as they decom-
pose the application into different services that can be developed independently
by small teams and incrementally deployed as necessary [HSS23; Cel20; Hil23;
RJ20a; Hig20]. However,while microservicearchitectures havebeen thesubject of
qualitativeanalysissincethedefinitionofthetermin2014[LF14]researchfailsto
identifyfaultsasasignificantconcernformicroserviceapplications.
SystematicLiteratureReviews. Sincetheproliferationofapplicationsbuiltusing
microservice architectures, several systematic literature reviews and mapping stud-
ieshaveidentifiedtheemergingconcernsandchallengesinmicroserviceapplication
development. Mostofthesestudieshavereliedonexistingacademicresearchon
microservices.
Pahl & Jamshidi performed a systematic mapping study that examined 21 dif-
ferent publications to identify the emerging concerns of microservice architec-
tures [PJ16]. Out of the 21 publications studied, failure is only mentioned as a
concerninasinglepublication.
Alshuqayranetal. performedasystematicmappingstudyofthechallengesin
microservice applications using 33 publications [AAE16a]. They identified eight
general challenges as part of their study. Of these 33 publications, 28 directly
mentioned fault tolerance; these were identified using the following keywords:
“fault”, “failure”, “recovery”, “tolerance”, and “healing”. However, the author’s
analysis did not go further than identifying that faults and fault tolerance were
crucialchallengesinmicroserviceapplications.
Soldanietal. performedasystematicliteraturestudyof51industrialpublications
toidentifytheprosandconsinvolvedinthe design,development,and operation of
microserviceapplications [STVDH18]. The authors identifiedfailure asanopera-
tionalconcernformicroservicearchitecturesandthenfurtheridentifiedonespecific
technological pattern, circuit breakers, as a tool that can be used contain failures
whentheyoccur.
Waseem et al. performed a systematic literature study focused on testing mi-
croserviceapplicationscomprisingof33publications[WLS20]. Theirresultsdemon-
strate that research interest in testing microservice architectures is increasing. How-

Background 11
ever, they only identify a single paper that explicitly tests applications for their
reliabilityagainstfailure.
Lietal. performedasystematicliteraturereviewof72publicationstoidentify
the quality attributes associated with microservice architectures [Li+21a]. The
authors identified availability as one of the primary quality attributes associated
with microservice architectures and used this more general term, availability, to
encompass reliability and fault tolerance. More specifically, they identified an
increasingtrendtowardsusingfaultmonitoringtoolsandcircuitbreakerstodetect,
react to, and contain failures, thereby increasing the quality attribute of interest:
availability.
Waseemetal. performedasystematicliteraturestudycomprising47publications
toidentifythekeythemesintheintersectionofDevOpspracticesandmicroservice
architectures[WLS20]. Thisstudyidentifiedcircuitbreakersasthepredominant
technologicalpatternfordealingwithcascadingfailures,asignificantconcernin
microservicearchitecturesthatresultinoutages(10.63%,fivestudies.)
All these studies indicate microservice resilience has only recently become of
academic interest since the inception of microservices and has not been subject
to in-depth theoretical investigation. Most notably, several papers identified the
circuitbreakerpatternasanincreasinglyusefulforpatternfordealingwithfailures.
Thispatternexplicitlyinjectsfailuresintotheapplicationtoindicatethefailureofa
dependency that will no longer be called, further necessitating the need for fault
injectiontesting,ofwhichlittleresearchexists.
QualitativeMethods. Asaresultofthelackofaccesstoindustrialmicroservice
applications, researchers have resorted to various qualitative methods (e.g., case
studies,developerinterviews)tostudymicroserviceapplications.
Forexample,O’Connoretal. extendedapreviousresearch study thatidentified
the software development processes that the developers of microservice architec-
tures used to understand the situational contexts and factors that drive process
selection [OEC16]. Leite et al. performed a grounded theory study involving
interviewswith 46professionalstounderstand howorganizationsstructure them-
selveswhenbuildingmicroserviceapplications[Lei+20]. Ayasetal. performeda
groundedtheorystudytoinvestigatethehumanprocessesinvolvedinmigrating
monolithicapplicationdesigntomicroservices[MALH21]. Sorgallaetal. performed
acomparativemulti-casestudywhereinterviewswereanalyzedusingagrounded
theory approach to identify the process(es) that were used in small to medium-
sizeddevelopmentorganizationswhenbuildingmicroserviceapplications[SSZ20].
However,outsideofsomenotableexceptions,failuredoesnotappeartobeaconcern
identifiedbythesestudiesinanyaspect.

12 BackgroundandRelatedWork
Taibietal. usedsemi-structuredinterviewswith72microserviceapplicationde-
velopersovertwoyearstoidentifybadpracticesinthedevelopmentofmicroservice-
basedsystemsandunderstandhowtheyovercamethem. Usingopenandselective
coding,theyidentified11microservice-specificbadsmells[TLP18]. However,only
one of the identified smells is related to reliability: API versioning mismatches
betweendifferentserviceswhereaservicethatdependsonanothermightreceive
datathatitisnotexpecting.
de Toledo et al. used a case study approach to identify technical debt in mi-
croservicearchitectures,specificallyrelatedtothecommunicationslayer,through
documentexaminationandparticipantinterviewsatacompanythatoperated1,000
differentservicesintheirmicroservice architecture [Tol+19]. Theirstudyrevealed
severalissuesinthecommunicationslayerthattheybelievearosewithrapid,de-
centralized development. The authors proposed a solution to these issues and
identifiedtherisksinherenttoimplementingthosesolutions.
Wang et al. performed a mixed-methods study that involved 21 practitioner
interviews,withafollow-uponlinesurveyof37participantsthatcovered37differ-
ent companies to identify best practices, challenges, and existing solutions to the
maintenanceand operationof microservices[WKR21]. While thisstudy acknowl-
edgedthatfailurescomplicatethemaintenanceandoperationofmicroservices,the
authorsonlypresentrecommendationsondebuggingtechniques.
2.1.2 Fault, Failures, and Errors in Microservices
There is little academic research on microservice application faults, failures, and
errors[Avi+04]. Severalauthorsbelievethatthisisaresultofacademicresearcher’s
limitedaccess toindustrialmicroserviceapplications [Jam+18b;Was+21b]. This
is demonstrated by examining the qualitative methods used in recent literature:
forexample,analysisofbugsreportedonopen-sourcemicroserviceapplications,
interviews withindustrial microservice developers, and grey literaturestudieson
microservicetestingmethodology.
Waseem et al. performed a thematic analysis of 1,345 issues gathered from
5 open source microservice applications on GitHub to build a taxonomy of the
types of problems that occur in microservice applications [Was+21b]. The authors
acknowledgedthelimitedrepresentationofthedataset: specifically,itwasrestricted
to smaller applications that are open source, but the authors still identify that
communicationfailuresrepresent119outofthe1,345(8.84%)issuesfiled. However,
whenfirststartingtheapplication,alltheidentifiedissuesarearoundmissingor
incorrectconfiguration. Therefore,thereisnodiscussionoffailuresresultingfrom
softwaredefectswhilethesystemisrunning.

Background 13
Zhou et al., to design a combined trace visualizer and visual debugger for mi-
croserviceapplications,surveyed16differentdevelopersacross13othercompanies
usingsemi-structuredinterviewstoidentifythebugsthattheyobservedinmicroser-
vice applications [Zho+18a]. They identified 22 different bugs and categorized
themaccordingtoataxonomybasedonseveralcriteria: mostnotably,whetherthey
arespecifictothearchitectureofmicroserviceapplicationsthemselves(5of22)or
wouldbefoundinmoretraditional,monolithicapplicationdesigns. Theirtaxonomy
draws a strict dichotomy between internal faults, where software defects cause one
ormorecomponentsofthemicroserviceapplicationtoreturnerrors,andinteraction
faults, where the unavailability of a dependent service causes the application to
malfunction. Oneareawherethisdichotomyisdeficientisitsconsiderationofthe
intersectionofinternalandinteractionfaults,anareadiscussedinthisdissertation.
Inshort,thesepapersreflectthestate-of-the-artknowledgeofwhymicroservice
applicationsfailbutonlyidentifyfewerthantenapplicationbugs,manyofwhich
donotresultincustomer-affectingapplicationoutages. Finally,itisessentialtonote
that all authors have created open-source corpora for future researchers based on
theirfindings;thisisconsistentwithoneofthetworecommendationsforimproving
researchinthearea[Zho+18a;Jam+18b].
2.1.3 Fault Injection
Faultinjectionhasarichhistoryinacademicresearch. Here,workthatconnectsto
thetechniquesusedinthisdissertationishighlighted.
Orchestra, [Daw+96], a system for message-level fault injection in distributed
applications, lets the application developer intercept and arbitrarily delay, drop,
or transform messages. Genesis2, [JD10] a system for performing fault injection
inservice-orientedarchitectures,anearlypredecessorofmicroservices,similarly
supportsarbitrarymessagetransformationalongwithdelayingserviceresponses.
Ferrari[KKA95]simulateslow-levelhardwarefaultsbyinjectingfaultsinsoftware
andwasthefirstsystemtoidentifythebenefitsoffaultinjectionwithindifferent
iterationsofloops.
FIG,[BST02a]LFI,[MC09a]andAFEX [BC12a]allperformlibrary-levelfault
injection. FIGfocuseson glibc. LFI firstproposed usingstaticanalysis onlibrary
codetoidentifythepossiblefaultsanapplicationshouldbetestedfor. WhileLFI
implementsamoreadvancedanalysis(e.g.,pointeraliasing,binaryanalysis),the
authorsrelyonover-approximationtoavoidmissingpotentialfaults. AFEX further
extends LFI with a search prioritization strategy for large applications where an
exhaustivesearchisimpossible.
Both Enforcer [ABH06] and ChaosMachine [Zha+21c] perform fault injection
ontheJVM.Enforcer injectscheckedexceptionstoverifytheerrorhandlingcode

14 BackgroundandRelatedWork
associatedwithexceptionhandlers. Mostoftheinnovationinthistoolistosupport
JVM-specificexceptionmodels. ChaosMachineinjectsallthrowableexceptionsand
requiresthatdevelopersusetestannotationstospecifyhowfaultsshouldimpactthe
internalstate. Incontrast,Fate[Gun+11]isafaultinjectorthatabstractstheinjected
faults toaddress the state spaceexplosion problemwhen exploringcombinations
ofdifferent faults. Itscounterpart,Destini[Gun+11],is adeclarativespecification
language over abstracted systemevents forwriting the system’sbehavioral specifi-
cation. SimilartoDestini,LDFI[ARH15a]isanoptimizedsearchstrategythatuses
a similar declarative specification language. The challenges of applying LDFI at
Netflix(e.g.,specificationlanguage,behavioralspecification,deterministicreplay)
havealsobeendiscussed[Alv+16a].
PreFail [JGS11]letsdevelopersinjectarbitraryfaultsandwritecustompruning
strategiestoreducetestcaseexplosion. Setsudo[Jos+13]useshigh-level,declarative
testspecificationsoverthesystemstatetodrivefaultinjection. Gremlin[Heo+16a],
is a system for programmatic specification and execution of chaos engineering
experimentsinmicroservicearchitectures.
2.2 Related Work
Thissectionpresentsresearchandindustrialpracticesrelatedtobothfaultinjection
and fault tolerance. While fault injection is the direct focus of this dissertation, it
is essential to frame its discussion within the context of fault tolerance, as fault
tolerance often impacts the type of fault injection techniques chosen when testing
microserviceapplicationsforresilience.
This related work is also presented in contrast with research in the same topics
performedondistributeddata systems: distributedsystems underlying infrastruc-
tureproductsandnotconsumerservices. Thesesystemsaremoreeasilystudieddue
totheiropen-sourceavailability,publicbughistorywithfixes,andwhichtypically
implementeitheroneorseveralwell-studieddistributedprotocols(e.g.,Zookeeper
andZookeeperAtomicBroadcast)ordesigns(e.g.,ApacheCassandraandAmazon’s
Dynamo.)
2.2.1 Industrial Practices
Industrial fault injection and fault tolerance techniques used by the developers
of microservice applications today are first presented. The reason for this is that
practitioners face faults daily and are highly motivated to identify practices that
havearealimpactonimprovingtheirapplication’sresilience.

RelatedWork 15
Fault Injection. Industrial fault injection practices in microservice applications
have been chiefly performed in production on a running application to determine
a system’s tolerance to a given fault. The collection of tools, techniques, and pro-
cessesthatsupportthisiscolloquiallyknownundertheumbrellatermofresilience
engineering: atermthathasitsformalrootsinthesafetyscience[Res]community.
Itreferstotheprocessesorganizationsandcommunitiesusetoadaptandrespond
tounanticipatedfailures.
GameDays,oneoftheearliestresilienceengineeringtechniquesusedbypracti-
tionersandthespiritualsuccessorofmostoftheapproachestakenbypractitioners
today, have beenused by Amazon, Google, andStripe[Rob+12; McC15]to identify
resilienceissuesinboththeirapplicationsandinfrastructure. GameDaysacknowl-
edgesthatfailureisinevitableatthescalethesecompaniesoperate. Therefore,they
opttopreemptivelytriggerfailuresandexploretheorganizationalresponsetothose
failures. Forexample,GooglediscoveredthroughaGameDayexercisethattheir
monitoringand alertinginfrastructure existedonlyinthedata centerwherethey
simulatedapoweroutage.[Rob+12]
Chaos engineering is another resilience engineering technique, initially pio-
neered by Netflix when first moving to the cloud [Chab]. The first iteration of
chaosengineering,Netflix’sChaosMonkey[Netb],randomlyterminatedinstances
in the live production cloud to ensure that Netflix’s applications were resilient
to instance failure: common, in the early iterations of Amazon’s EC2 cloud en-
vironment. Next, Netflix’s Simian Army [Netc; Nete], a collection of tools for
performing different types of fault injection, allowed developers to simulate in-
creasedlatencyandfailuresofbothEC2availabilityzonesandEC2regions. Since
then, chaos engineering has evolved into a discipline [RJ20b] practiced by many
different companies, where its supported by a variety of other open source tools
(e.g., ChaosToolkit [Chad], ChaosMesh [Chac], ChaosBlade [Chaa], Litmus [Lit],
LinkedOut [Lin]),books[RJ20b],communitymeetups1,andcommercialsoftware-
as-a-service(SaaS)offerings(e.g.,Gremlin [Grea],Harness [Har].)
As a discipline, chaos engineering closely resembles the scientific method: a
hypothesisisformedaboutwhattheapplicationwilldowhenfaultsareinjected,
faultsareinjectedineithertheentiretyof,asubsetof,ormirrorofproductiontraffic
and the hypothesis is falsified, if possible. Therefore, the key behind the chaos
engineering approach is application observation. In the case of Netflix, the key
performancemetricobservedduringchaosengineeringexperimentsisametricthat
countsthenumberofmoviestreamsstartedpersecond,whichvariesalittleweek
overweek,makingiteasytodetectdeviationsfromthenormwhenrunningachaos
experiment. This directly contrasts traditional approaches where a test oracle – a
1https://chaos.community,nowdefunct.

16 BackgroundandRelatedWork
sourceoftruth inthetestsuitethatisused identifyingapplicationbugs–contains
assertionsabouttheapplication’sdesiredbehavior.
Netflixhascontinuedtoinnovateinchaosengineering. TheirFailureInjection
Testing(FIT) [Neta] framework, forexample, isintegrated intothe RPC framework
thatalloftheirservicesuseforintra-servicecommunication,allowingthemtoinject
faults atany RPCsite intheir microservice application. Their ChaosAutomation
Platform(CHaP)[Bas+19a]enablesautomatedfailuretestingwithaminimalblast
radiusbyautomaticallyspinningupreplicasofserviceswherefaultswillbeinjected
onasmallpercentageoftheirproductiontrafficintheeventofanoticeabledeviation
fromthenormin theirkeyperformanceindicator,theexperiment isautomatically
terminated. Monocle[Bas+19a]pushesthisevenfurtherbyexaminingtheRPC
configurationcodethatisassociatedwitheachoftheirservicesandautomatically
generates chaosexperimentsthatare then automatically run with CHaP.It isim-
portanttonotethat Monoclewasrecentlydisabled[Ret]duetothelargenumber
ofexperimentalconfigurationsgeneratedandtherequiredoverheadrunningthose
experimentsatscale. Finally,Gremlin,thechaosengineeringSaaScompanyformed
byformerNetflixchaosengineers[Grea],alsobrieflypromotedaproductcalled
“application-level fault injection” (ALFI), where a library-level fault injection ap-
proachwasusedtoprovidemoregranularfaultinjectionwithanevensmallerblast
radiusanderrorsspecifictothelibraryinuse. Asof2018,thisproductisnolonger
offered.
Regarding the industrial practices for fault injection in microservice applica-
tions, several interesting observations can be made. First, the adoption of chaos
engineering techniques in practice seems to be related to two critical aspects of
chaos engineering: low-level fault injectionand application observation. Low-level
faultinjection(e.g.,disruptingthenetwork,terminatinginstances)isextremelylow
overhead for developers. For example, Gremlin [Grea] uses a daemon installed
onthevirtualmachineinstancesofeachserviceandrequiresnomodificationsto
application code to perform fault injection. Application observation, using key
performanceindicators(KPI)ormetrics, alsohaslowoverheadwhencomparedto
either heavyweight specifications describing the application’s behavior – in enough
detailformechanicalverification–orcomprehensivetestsuites,underfault. These
twokeyaspectsindicatethatdeveloperscanquickly“tryout”chaosengineering
before moving to more advanced fault injectiontechniques, which has presumably
helpedincreasethebroadadoptionthatchaosengineeringhasseeninrecentyears.
Second, the evolution ofchaosengineeringtoolsseemsto indicateadesirefor
functionalitythatistraditionallyseeninacademicapproaches: automation,granu-
larfaultinjection,andlibrary-levelfaultinjection. Forexample,Monocle[Bas+19a]
automaticallygenerateschaosexperimentsfromsoftwareconfiguration: thisresem-
blesatraditionalexhaustiveorsystematicsearchcommonlyfoundinapproaches

RelatedWork 17
builtonsomeformofmodelchecking. ALFI,theabandonedapproachfrom Grem-
lin [Grea],soughttoprovidefaultinjectioninthelibrariesthatservicesusedfor
issuingRPCsandcommunicatingwithdistributeddatasystemstoallowgranular
faultinjectionwithaminimalblastradiusandlibrary-specificerrors: thisresembles
traditional academic library-level fault injection approachesthat aim to givedevel-
opers confidence in proper API use and error handling of those libraries. However,
bothofthesemore“academic”approacheshavefailedduetotheoverheadinvolved
inmorecomprehensive,targetedtesting.
Forexample,Monoclereliesonexperimentationinproductionusing CHaP to
automaticallycreateclusterswithasubsetofproductiontrafficforexperimentation.
Thisisanexpensivetaskthat couldbereducedbyeither(A)experimentationina
stagingordevelopmentenvironment;or(B)throughtheuseoftestcasereduction
techniques,commonlyseeninacademicapproachesthatemploymodelchecking.
ALFI [Grea], initially designed for returning library-specific errors using fault
injectionwithaminimalblastradiusrequiredthatdevelopersmanuallyinstrument
thelibrariesinusebythemicroserviceapplication. Thisisalsoanexpensivetask
thatcould bereducedbyeither(A) experimentationina stagingordevelopment
environment;or(B)throughtheuseofsomesortofautomaticinstrumentation.
Whenconsidering(A)specifically,runningchaosexperimentsinthestagingor
developmentenvironmentisnotasstraightforwardasit sounds. Whilethetools
workinthesamemannerregardlessofenvironment,therelianceonakeyperfor-
mancemetricasthetestoraclenolongerworks: thelocaldevelopmentenvironment
willnotseeanyrequestsoutsideofwhatisissuedbythedeveloper;similarly,the
stagingenvironmentmaynotaswell. Therefore,tobringthisexperimentationstyle
into the local development environment, one must first solve the problem of the
missingtestoracle: thespecificationoftheapplication’sbehaviorunderfault.
FaultTolerance. Whenitcomestofaulttolerance,developersrelyonasetoftech-
niquesdesignedformicroserviceapplications,inadditiontothestandardretries
andtimeoutsoftenusedbythedevelopersofdistributeddatasystems(e.g.,Cassan-
dra). Thesetechniquesare: fallbacks,circuitbreakers,andloadshedding. Rather
obviously,circuitbreakersandloadsheddingarenamedaftertheircounterparts
inthefieldofelectricalpowermanagementanddelivery: bothtechniquesusedto
preventoverloadofasystemintheeventofoneormorefaults.
Fallbacks are used when a remote service is malfunctioning or unavailable in
order to find alternative or replacement information from a different, properly
functioning service. The canonical example here is from the streaming service,
Netflix,where whenmovierecommendations tailoredtotheuser arenotable to be
retrieved,asetofmovierecommendationsbasedontheglobaluserbaseisreturned

18 BackgroundandRelatedWork
instead. Fallbacksallowthesystemtokeepfunctioningincaseofafault,potentially
withadegradeduserexperience.
Circuitbreakersarealsousedwhenaremoteserviceismalfunctioningorunavail-
abletorelievepressureontheremoteserviceandtoavoidwaitingforaresourcethat
willnotrespondpromptly. Toachievethis,circuitbreakersaccumulatecountersthat
reflectthenumberofsuccessfulandunsuccessfulresponseswithinagivenwindow.
Whenthecountersexceedaparticularthreshold,theRPCtothemalfunctioningor
unavailable service is “short circuited” by returning an error immediately to the
callertoindicatethecircuitisopen. Periodically,toclosethecircuitoncetheremote
service begins functioningcorrectly, an RPCis allowedto happen. Eventually, once
theremoteservicefullyrecovers,thecircuitmovesbackintotheclosedstate.
Loadsheddingisusedwhenaremoteserviceisoverloadedandcannotrespond
promptly to reduce pressure on that service. Where circuit breakers are located
at the invocation site of an RPC, load shedding is situated on the invokee side
of an RPC. Load shedding compliments circuit breaking, as circuit breakers may
fail to fire quickly enough — or the remote service may have multiple invokers
whosecombinedloadexceedstheservice’scapacity—tokeepservicesfunctioning
correctly. Toachievethis,loadsheddingtypicallytracksthenumberofoutstanding,
concurrent requests, and once a threshold is exceeded, requests are immediately
“short-circuited “ by returning an error to the invoker (or dropped silently.) If a
circuitbreakerisinplace,theserequestsmaycausetheinvokerscircuitbreaker’s
counterstoincrement.
Thesethreetechniquesarenotapanaceaoffaulttolerance,however. Forexample,
fallbacksmustbecarefullyconsidered,asintheeventofafault, the fallbackmay
also be unavailable or malfunctioning. With circuit breaking, thresholds may be
misconfiguredor,whenthecircuitbreakerisusedtoocoarsely,mightsimultaneously
turnoffcorrectlyfunctioningcomponentsoftheapplicationwhiletryingtocontaina
fault. Withloadshedding,thesametypeofbehaviorcanoccur. Therefore,anyfault
injection technique must also consider faults within the fault tolerance measures
employedbytheapplication.
For most microservice applications, a combination of these three techniques,
alongwithtimeoutsandretries,areusedtopreventthedreadedcascadingfailure,
whereafaultinoneserviceleftunhandledorimproperlyhandled,propagatesto
theservicesthatdependonitthroughtheapplication’sRPCgraph,inducingfurther
faultsuntiltheentireapplicationfails.
2.2.2 Academic Literature
This section presents both the fault injection and fault tolerance techniques for
microserviceapplicationsthathavebeenthesubjectofacademicstudy. Therelated

RelatedWork 19
workindistributeddatasystemsisalsopresentedforhistoricalcontext.
FaultInjection. Academicresearchonfaultinjectiontestingandfaulttolerance
in distributed data systems has historically built upon the rich history of model
checking,eitherrelyingonspecificationsofeithertheexternalbehaviorofthesys-
tem under test or the internal system state [ARH15b; Kil+07; Luk+19; Yab+10;
Yan+09;SBG10;Lee+14;GY11]. However,successfullyapplyingthesetechniques
tomicroservice applicationshasbeen limited[Alv+16b]. Outsideofmechanizing
an approach that supports deterministic fault injection across multiple services
implemented in various languages, one of the main challenges has been the lack
of a test oracle that specifies behavior under failure. In industrial microservice
applicationsspecifically,specificationsthatarerichenoughtosupportmodelcheck-
ing are rarely if ever, written; similarly, the decentralized nature of microservice
applicationdevelopmentpreventstheuseofglobalstateinvariantsplacedacross
all stateful services in an microservice application. However, the developers of
industrialmicroserviceapplicationsarewritingfunctionaltests. Therefore,itwould
seem that any successful approach should built on and extend to cover behavior
underfault,thetestoraclesalreadybeingwritten.
Onekeyobservationaboutmicroserviceapplicationsisthatintra-servicecom-
munication is typically performed using client libraries (e.g., AWS DynamoDB
client)orRPCframeworksthataredirectlybuiltonand/orextendedaslibraries
(e.g., HTTP via Java’s Netty library, gRPC via Google’s gRPC library.) Therefore,
theexistingresearchonlibrary-levelfaultinjection(e.g.,FIG,LFI,AFEX)[BST02b;
BC12b;MC09b],whichpurportsthatlow-levelfaultswillmanifestthemselvesas
library-levelerrorsinanapplication,maybeahelpfulstartingpointforautomated
faultpreventiontechniquesformicroserviceapplications. Thereisevidenceofthis:
ChaosMachine [Zha+19], for example, usesa library-level fault injection approach
toexerciseandtestanmicroserviceapplicationsexceptionhandlers. Library-level
fault injection strikes a good middle ground where library-specific errors can be
simulatedautomaticallyandexhaustivelywithoutrequiringlow-levelfaultinjection
totriggerthemorganically.
Incontrasttolibrary-levelfaultinjection,recentacademicapproacheshavepro-
posed targeting the network layer for fault injection. For example, the academic
systemsharingthesamenameasanindustryservice,Gremlin[Heo+16b]proposes
the use of sidecar proxies at each node, where all RPC communication is routed
throughthembeforereachingthedestination,forfaultinjection;thisremovesthe
requirement of local code modifications to support fault injection. Even further,
ucheck [PSS17] proposes the use of software-defined networking (SDN) infras-
tructure for fault injection, removing the requirement for any code modification or

20 BackgroundandRelatedWork
additionalinfrastructureoneachnode. However,thisstyleoflow-levelfaultinjec-
tioncanproveproblematicwheninjectingspecificfaults,forinstance,triggeringa
gRPC failed precondition error instead of a somewhat more straightforward gRPC
serviceunavailableerror. Effectively,themovementawayfromlibrary-levelfault
injection,presumablydonebecauseofthecostsofinstrumentingeachlibrarythe
applicationuses toissue RPCs, hasmade itmore challengingto injectcertain types
offaultsandmorecostlyincomputingresourcesandrequiredinfrastructure.
Despiteadvancesinthefaultinjectionmethodology,theproblemofthemissing
test oracle remains unsolved. ucheck [PSS17], which relies on fault injection in
theSDNlayer,stillrequiresthatapplicationdeveloperswritestateinvariantsthat
canbeusedforverification: not feasibleformicroserviceapplications. Incontrast,
Gremlin [Greb], whichalso operatesat thenetwork layerbut insteaduses sidecar
proxiesforfaultinjection,hasnovisibilityintothesystemstateandonlyprovides
assertion languages over the request patterns between different services: this re-
quiresdevelopers,inadditiontowritingend-to-endfunctionaltestsalsoencodehow
communicationoccurs. Finally,ChaosMachine[Zha+19]eliminatestheneedfor
stateinvariantsbyallowingdeveloperstospecify,usingannotationsinapplication
code, whether or not an injected fault will be resilient (i.e., no change on system
state),observable(i.e.,bytheuser),debuggable(i.e.,createslogmessages),orsilent
(i.e., no derivation instate nor additional logging.) In short, whileChaosMachine
advances the academic work toward commonly used industrial techniques (c.f.,
chaos engineering), it remains somewhatdisconnected from typical functional test-
ing. Apromisingnaturalprogressionofthisresearchistoexplorethespecification
ofthetestoracleasobservabledeviationsfromtheapplicationbehaviorwhenfaults
arenotpresent.
Theunfortunatecasualtyofthismigrationawayfromspecificationsistestcase
reduction. In distributed data systems specifically, test case reduction has typi-
cally reliedonproperties ofthesystem undertest: for example, symmetry reduc-
tion[Luk+19],wherecertain testcasescanbeavoidedundertheassumptionthat
differentreplicasofthesameservicewillbehaveidentically. However,thelackof
access to realistic microservice applications [Jam+18a; Was+21a; Mei+21a], and
thedeficienciesinexistingopen-sourcecorpora,whichhavenotbeenoperatedat
scale[Was+21a]norcontainrealisticbugsspecifictothechoiceofamicroservice
application [Zho+18b], have limited the ability of researchers to discover simi-
lar techniques for microservice applications. Therefore, with increased access to
descriptions orimplementations ofrealistic microservice applicationsandactual
bugs experienced in microservice applications, the discovery of test case reduction
techniqueswillbepossible.
Mostnotably,andmostrecently,Rainmaker [Che+23]proposesanapproach
closesttotheinnovationsthatarepresentedinthisdissertation. However,insteadof

RelatedWork 21
focusingonmicroserviceapplications,Rainmaker’sfocusisontestingapplications
that use cloud services using HTTP APIs, leveraging the application’s test suite
foratestoracle,andemployingatestcasereductionstrategy. Thismeetsboththe
goalsofacheaplibrary-levelfaultinjectiontechnique,whereallHTTPcallscanbe
uniformly instrumented using a network proxy with no application modification,
andavoidstheheavyrequirementoftestoraclecreation.
Towardsthesegoals,Rainmakermakesseveralsimplifyingassumptions,thereby
achievinganautomatedfaultinjectiontechniquethatcanbeusedtosurfacebugs
quickly in these applications. As these assumptions are relevant to this dissertation,
theyarebrieflydiscussed:
• ApplicationStructure.
Inordertoreducetestingcost,redundanttestcasesareidentifiedandelimi-
natedthroughananalysisphase. However,theseredundanttestcasesareiden-
tifiedbothusingtheapplication’scallsiteofanRPCandundertheassumption
thattheerrorhandlingcodeforthatRPCisco-locatedattheinvocation’scall
site. Inshort,itisonlynecessarytotesteachindividualRPCasingletimeto
determineiffailureofthatRPCishandledproperly. Aswillbedemonstrated
inthisdissertation,thissimplificationisnottrueforindustrialmicroservice
applications. In fact, two of the bugs identified during the development of
thisdissertationinvolvednon-localizederrorhandling.
• TestOracle.
To avoid the high cost in creating a failure-specific test oracle [AMS13] an
application-agnostictestoracleisusedasanalternative. Thisoracleassumes
that any exception generated by the application code itself is not indicative
of a bug; this is in direct comparison to an exception generated by a under-
lying framework code. This simplification is based on an assumption that
application-thrownexceptionsindicatethatanunderlyingexceptionwashan-
dledandaspecificapplicationerrorwasthrown.
Notonlyisthisnottrueforindustrialmicroserviceapplicationcode,where
thelinebetweenframeworkcodeandapplicationlibrariesdevelopedbylarge
organization(s) to support rapid development is blurred, it also fails to ac-
knowledge “silent failures”: where something does not happen that should
have, but did not trigger an exception. As will be demonstrated in this
dissertation,useofanapplication-agnostictestoracleisnotsufficientfor
resiliencebugidentification. Infact,these“silentfailures”maptoanentire
classofapplicationbehaviorknownasgracefuldegradation,wheresilentfail-
urescanadverselyaffectendusers, embodiedbythebugsdiscoveredduring
thedevelopmentofthisdissertation.

22 BackgroundandRelatedWork
Rainmaker’sevaluationofthesetechniquesisperformedonopen-sourcelibrary
code,foundonGitHubbyresearchers. Thisfurtheremphasizestheneedforopen-
sourcecorporatofurtherfaultinjectionresearch.
Fault Tolerance. Research onmicroservice applicationspecific fault tolerance is
quitelimited,againpresumablyduetothelackofaccessforacademicresearchers
torealisticapplications[Jam+18a]. Whileacademicshaveseeminglystudiedthe
use, and improvement of, circuit breaker technology, none have considered it in
thecontextoffaultinjectiontodeterminewhatbehavioranapplicationhaswhen
a circuit breaker is open. This is despite circuit breakers provoking failures in
microserviceapplicationsbydesign.
Several qualitative studies [AAE16b; Tig+20; Li+21b; JC19; Ner+20; Val+20;
PP21; SMAP19; BHJ16; Bal+18] have identified circuit breakers as a core pattern
used toimprovereliability or availability (i.e., resilience) inmicroservice applica-
tions. Mostnotably,SurendroandSunindyo’ssystematicmappingstudy[SS+21]
identifiedalackofexistingresearchoncircuitbreakerscomparedtoothermicroser-
viceapplicationtopics.
Outsideofqualitativestudies,previousworkhasexploredthetransparentap-
plicationofcircuitbreakersinanacademicprogramminglanguage[MW18]and
eitherthedynamictuningof[SKT21]oroptimalconfigurationviamodelchecking
of [Men+20], a circuit breaker’s configuration parameters. Palliwar et al. [PP22]
proposeddistributedcircuitbreaking,whereagossipprotocolisusedtodissem-
inate circuit breaker state across nodes in a cluster for faster detection of failures
inamicroserviceapplication. Heorhiadietal.[Heo+16b]whoproposedthefault
preventiontoolGremlin,alsoconsideredcircuitbreakertestingaspartofthedesign
of Gremlin andprovideda mechanismfor assertingthatthey operated correctly,
butfailedtoconsiderapplicationbehavioronceactivated.
Researchers have also motivated the design of data plane fault injection tools
usingcircuitbreakers;however,noneofthesedesignscontainedanythingspecific
fortestingwhatanapplicationdoeswhenacircuitbreakerisopen: aspecificcase
whereafaultisinjectedintoanapplication. Itisimportanttonotethatnorelevant
academic research could be found regarding load shedding as a fault tolerance
techniqueinmicroserviceapplications: anothercasewherefaultsareinjectedinto
anapplicationwhenrunningbydesign.
2.3 Takeaways
Regardingfaultpreventioninmicroserviceapplications,thereisanevidenttrend
whenyouexaminetheexistingacademicresearchandindustrialpractices: theyare

Takeaways 23
converging.
Industrial practices seem to be evolving in the direction of more traditional
academicresearchthroughtheuseofordesiretouselibrary-levelfaultinjection,
withautomationforthegenerationoftestsorchaosexperiments,usinggranular
faultinjectiontominimizetheblastradius.
• Library-levelFaultInjection.
Developersrealizethatto buildmoreresilient systems,they needtobe con-
cerned withlibrary-specific faults, in additionto low-levelfaults (e.g.,service
unavailability, network partitioning). However, this approach remains dif-
ficult in practice as it requires instrumentation of each library used by an
microserviceapplication.
• AutomatedTestGeneration.
Developers are beginning to use the application’s configuration to identify
remotecallsandautomaticallycreatetestscenarios. However,runningthese
experiments in production, combined with the lack of test case reduction,
makesrunningexhaustiveexplorationinfeasible.
• GranularFaultInjection.
Developersarelookingatwaysforblastradiusminimization,asmanychaos
experiments are still performed in the production environment. However,
with a proper test oracle, it would not be possible to run these experiments
inalocaldevelopmentenvironmentwhereblastradiusminimizationisnot
necessary.
Academic research alsoseems to beevolving inthe direction ofcontemporary
industrialpractices.
• Network-levelFaultInjection.
For example, academic research has sought to solve the problem of heteroge-
neousimplementationlanguageusageinmicroserviceapplicationsthrough
theuseoffaultinjectionatthenetworklevel. However,thisapproachfailsto
accountforfaultsthatcannotbegeneratedthroughlow-levelfaultinjection
(e.g.,PreconditionFailed,NotFound).
• TestOracleCreation.
Similarly,recentacademicresearchhasacknowledgedtheproblemofthemiss-
ingtestoracle,proposingsolutionsthatbuildonapplicationobservation,asis
familiarwithchaosengineering. Despitethis,theexistingproposalsstilluse
assertionsthatrelyonthetechnicalaspectsoftheimplementation: forexample,

24 BackgroundandRelatedWork
messagessentbetweenservices[Greb]orwhetherornotthestatewillchange
and be observable by the end-user when a fault occurs [Zha+19]. Instead,
unfortunately, manual experiment (i.e., test) specification is still required
withmanyofthesetechniques. Asaresult,littleresearchintomicroservice
applicationspecifictestcasereductionexists.
Industrialpracticesareinfluencingacademicresearch,asclearbytheinnovations
inmechanizingchaosengineeringandtoolslikeRainmaker. Still,withoutaccessto
implementationsofindustrialmicroserviceapplications,academicsareleftguessing
atpracticalsolutionstothemostpressingofindustryconcerns.
This also extends to fault tolerance techniques for microservice applications.
At the same time, qualitative research that relies on developer interviews, ques-
tionnaires,andsurveysidentifiedcircuitbreakersasaprimarytechniqueusedfor
increasingtheresilienceofmicroserviceapplications,studiesperformedonopen-
source microserviceapplications failed to identifycircuit breakers, load shedding,
orfallbacksasresiliencetechniquesusedinmicroserviceapplications.
Thisseemstoindicatethatwhileacademicresearchandindustrypracticesare
converging on a similar design based on observation of each other’s techniques,
academics,withoutaccesstoindustrialcodebases,arelefttoinferthemethodsand
solutionstheyfeelwillbehelpfultopractitioners.

Chapter 3
Microservices: Dependency Types
“We’rebuildingsomethinghere,detective. We’rebuildingitfromscratch.
Allthepiecesmatter.”
DetectiveLesterFreamoninTheWire“...andallthepiecesmatter.”
Microservicearchitecturesarecurrentlythedominantarchitecturalstyleformost
consumer products and services [HSS23; Hil23; RJ20a; Hig20]. This architectural
styleinvolves breakingdownapplicationsinto independentservices,addressing
theneedsoflarge-scaledevelopmentorganizations: specifically,towardsincreasing
developmentvelocitybyallowingtheseservicestoevolveasnecessary,developed
bysmaller,agileteams[Cel20].
Structurally,applicationsbuiltusingamicroservicearchitectureresemblemono-
lithic applications, where the application is divided along module boundaries,
termed services. These (often stateless) services then take dependencies on third-
partyapplications(e.g.,databases,messagequeues),whicharemanagedin-house
anddeployedasservices,aswellasthird-partyservices(e.g.,AmazonAWS,Google
GCP),whicharedeployedandmanagedbythethird-party,forstatemanagement.
Such an application, utilizing bespoke stateless services and stateful third-party
servicesispresentedinFigure3.1.
Services then interact using Remote Procedure Calls (RPC) across a network in-
steadofmethodinvocationswithinasinglecodebase,asinmonolithicarchitectures.
Ascommunicationperformedoveranunreliablenetworkwithanindependently-
deployed and managed service is ultimately prone to failures, developers must
decidebeforedeployingcodetoproductionwhetheranapplicationshouldwithstanda
failureofaremotedependency. Thisdecisionisreferredtoasthetype oftheservice
dependency.
25

26 Microservices: DependencyTypes
Thischapterpresentsthedesignsoftwomicroserviceapplicationstodescribe
thetypesofservicedependenciescommonlyoccurringinmicroserviceapplications:
hard and soft dependencies. Each example application is (re-)constructed from
publicdiscussionsofeachcompany’sindustrialmicroserviceapplication.
Audible [Tyl18] is an audiobook streaming service. Their microservice ap-
plication is used to demonstrate a microservice application that is composed of
predominantlyharddependencies: dependencieswhereuponfailureofanRPC,the
failure forces the application to abort a customer’s request with an error. While
theirapplicationdoes containasinglesoft dependency,itssuccessorfailurehas no
bearing on the customer experience of streaming an audiobook: it merely tracks
internalstatisticsonwhataudiobookscustomersarestreaming.
Definition 1(HardDependency). Aharddependencyisadependencywhereafailed
invocationforcestherequestthattriggeredthedependencytoreturnanerrortoitscaller.
HarddependenciesarespecifictoaninvokedRPCservice,method,arguments,
andspecificcallsitewithcallingcontext,asdifferentcallsitesmaytreatthesame
RPCinvocationaseitherhardorsoft.
Netflix [Nor17] is a video streaming service. Their microservice application
designpresentsanapplicationwherebothhard andsoftdependenciesareused. With
theirhard dependencies,thefailureofsomeRPCsforcestheapplicationtoreturn
anerrortothecustomer. Incontrast,inthecaseofsoft dependencies,thefailureof
theRPCisignoredor“compensated”byissuingalternativeRPCs.
Definition 2 (Soft Dependency). A soft dependency is a dependency where a failed
invocationishandledintheapplicationtoavoidtherequestthattriggeredthedependency
fromreturninganerror.
Softdependencies arespecificto aninvokedRPC service,method, arguments,
andspecificcallsitewithcallingcontext.
In both of these example applications, the effects of the type of dependency
choice are directly visible to the customer when trying to use the service. For
example, in the Audible example, almost all fault injections cause the customer
to experience a failure. In the case of Netflix, some fault injections will cause a
successful response to turn into an unsuccessful response; however, other fault
injectionswillcausethesuccessfulresponse’s contenttochange. Thisisaresultof
the application “compensating” for the failure by loading alternative content or
omittingcontentthatisnotavailable.
The developers of microserviceapplications often prefer softdependencies as
they enable the “graceful degradation” of microservice applications: the ability
forapplicationstoreducetheirfunctionalityintheeventoffailuretoprovidestill
(some)servicetothecustomer.

Audible: HardDependencies 27
3.1 Audible: Hard Dependencies
ThefirstmotivatingexampleistakenfromAudible[Aud],anaudiobookstreaming
serviceownedbyAmazon,wherethefailureof(almostevery)dependentservice
resultsinthecustomerreceivinganerror.
Figure3.1: Audibleapplicationwithadescriptionoftheaudiobookretrievalprocess.
3.1.1 Application Structure
The Audible microservice application, depicted in Figure 3.1, comprises several
stateful and stateless services, all of which are hard dependencies with one notable
exception.
• ContentDeliveryService(CDS):
Givenabookidentifierandauseridentifier,returntheactualaudiocontent
andaudiometadataafterauthorization;
• ContentDeliveryEngine(CDE):
ReturnstheURLofthecorrectContentDeliveryServicetocontacttoretrieve
theaudiobookusingAWSElastiCache;
• AudibleDownloadService(ADS):
Orchestratesloggingandauthorizationoftheaudiobookonceownershipis
verified;
• OwnershipService:
VerifiesownershipofthebookusingAWSRDS;
• ActivationService:
Activates a Digital Rights Management (DRM) license for the user for the
requestedaudiobookusingAWSRDS;

28 Microservices: DependencyTypes
• StatsService:
Maintains audiobook and DRM license activation statistics using AWS Dy-
namoDB. This service isthe single soft dependency, whichhas no bearing on
thesuccessoftheuser’srequest;
• AssetMetadataService:
Storage (AWS S3)forthe audiobookassetmetadata, whichcontainsinforma-
tiononchapterdescriptionsand
• AudioAssetsService:
Storage(AWSS3)fortheaudiofiles.
3.1.2 Application Behavior
WhenacustomerrequestsanaudiobookusingtheAudiblemobileapplication,it
firstrequeststheContentDeliveryEnginetofindtheURLoftheContentDelivery
Service(CDS)containing the audiobookassets. TheappthenrequeststhatCDS.
TheCDSfirstrequeststheAudibleDownloadService(ADS).TheADSisresponsible
for first verifying that the customer owns the audiobook. Next, the ADS verifies
thataDRMlicensecanbeacquiredforthataudiobook. Finally,itupdatesstatistics
attheStatsservicebeforereturningaresponsetotheCDS.Ifownershipofthebook
cannot be verified or a license cannot be activated, an error response is returned
to theADS, which propagates back to the customer through an errorin the client.
Once the ADS completes its work, the CDS contacts the Audio Assets service to
retrievetheaudiobookassets. Then,theCDScontactstheAssetMetadataService
toretrieveassociatedmetadata. Finally,theseassetsarereturnedtothecustomer’s
appforplayback.
ThedecompositionoftheAudibleapplicationintoservicesresembleshowone
mightwritethisapplicationusingamonolithicarchitecture. Forexample,theADS,
which is responsible for verifying, tracking, and maintaining access to the user’s
audiobooks,encapsulatesthislogicbyfirstverifyingownership,performinglicence
activation, and recording statistics onactivation. Similarly, theCDS encapsulates
this logic with the retrieval of the data files: when the ADS returns a successful
result,itprovidesthenecessaryaudiofilesandmetadatatotheuser. Thisnatural
style of decomposition, or microservice architecture, contains more depth, rather
thanbreadth.

Audible: HardDependencies 29
If any of the dependent downstream RPCs executed when processing a cus-
tomer’s request fails,modulo the Stats service, the entirerequestfrom the customer
isfailedandtheyareaskedtotrytheirrequestagain. Now,letusexaminehowthis
cangowrongbasedonareal-lifeincidentreportedbyAudible[Tyl18].
Outage. TheAudibleapplicationassumesthatifanaudiobookexistsinthesystem
andtheassetsareavailable,themetadatawillalsobeavailable. However,thismay
notalwaysbethecase. Thisprecisefaultcouldbedetectedthroughfaultinjection
testing;ifused,thedevelopersmaychoosetoeitherspecificallywriteerrorhandling
forthiscaseorignorethefaultundertheassumptionthatthisinvariantwillnever
beviolated.
However,theinvariantwasviolatedforreasonsthatarenotdisclosedbyAudible
and are presumably related to operator or database error: the asset may have
been deleted accidentally, the database lost the file, or the database could have
malfunctionedatthetimeoftherequest. Thisresultedina cascadingfailureand
subsequentoutageoftheAudibleapplication.
This outage results from several different faults, both latent and active, that
interactwithoneanotherinsomemanner. Startingwiththelackoferrorhandling,
agenericerrorispropagatedbacktothemobileapplicationthat,uponreceivingthe
genericerror,assumesthefailurewastransientandconsequentlyretriestherequest
afinitenumberoftimes. Whenalloftheretriesreturnafailure,agenericerroris
providedbacktothecustomerinthemobileapplicationthatcausesthecustomerto
issuearetry. Thiscombinationofcustomer-initiatedretriesforrequeststhatwill
ultimately fail,paired withthe combinationof apopularaudiobook,is enoughto
exhaustavailable“compute”capacityandcausetheapplicationtofail.
Inshort,alatentbug canbedefinedasfollows:
Definition 3(LatentBug). Alatentbugisabugthatexistsinapplicationcodebuthas
notyetcausedanyobservableerror.
This type of bug remains dormant due to specific conditions or scenarios not
being met: the application’s environment, which includes but is not limited to
externaldependencies(e.g.,otherservices),orinvaliddatabeingprovidedasan
input. Inmicroserviceapplicationsspecifically,latentbugsarehiddenerrorsthat
donotnecessarilycauseproblemsinitiallybutmayleadtoissueslater,oftenafter
the application is already being used. In many cases, they are activated by the
unavailability of downstream dependencies or infrastructure failures. These bugs
arehardtospotandfixbecausetheydon’tshowupuntilspecific,sometimesrare,
conditionsoccurintheapplication,oftenoncealreadydeployedtoproduction.
Latentbugsareindirectcontrasttoactivebugs,definedasfollows:

30 Microservices: DependencyTypes
Definition 4 (Active Bug). An active bug in a microservice application is a noticeable
softwaredefectthataffectstheapplication’sfunctionalityorperformanceatpresent.
Unlike latent bugs, active bugs are immediately apparent, often causing er-
rors, performance degradation, or other unexpected behavior in the system. In
microservice applications specifically, these bugs can impact individual services
orthecommunicationbetweenservicesinamicroservicearchitecture,leadingto
problems like service unavailability, incorrect data handling, or failuretoexecute
certainrequests.
3.2 Netflix: Hard and Soft Dependencies
The second motivating example is taken from Netflix [Netd], a video streaming
service, where its homepage requires the resources of several dependent down-
stream services to populate its content. However, when a service is unavailable,
they replace its content with content from another appropriate service to avoid
failingonasingleharddependency: theonlyharddependencyinthispartoftheir
application isthe customer profile service, which, when failed, prevents the page
fromloading. Thisisreferred to asafallback,and canbeprovidedwhen makingan
RPCrequestusingtheirfaulttolerancelibrary,Hystrix.
Figure3.2: Industryexamplesinthemicroserviceapplicationcorpus.

Netflix: HardandSoftDependencies 31
3.2.1 Application Structure
The Netflix example,presented inFigure 3.2, hasten servicescomprising hardand
softdependencies. SimilartotheAudibleexample,theNetflixmobileapplicationis
representedasaservice.
TheservicesintheNetflixexampleare:
• Client:
Simulatesthemobileclient;
• APIGateway:
Assemblesauser’shomepageusingcontent fromvarious downstreamdepen-
dencies,bothhardandsoft;
• UserProfile:
Returnsprofileinformation;
• Bookmarks:
Returnslastviewedlocationsofmovies;
• MyList:
Returnsthelistofmoviesintheuser’slist;
• UserRecommendations:
Returnsrecommendationsspecifictotheuser;
• Ratings:
Returnstheuser’smovierating;
• Telemetry:
Recordstelemetryinformation;
• Trending:
Returnstrendingmovies;and
• GlobalRecommendations:
Returnsrecommendationsforallusersoftheapplication.
3.2.2 Application Behavior
Inthisexample,loadingtheNetflixhomepagerequirestheresponsesseveralser-
vices: ahighfan-outthattouchesmultipleservicestoretrievetheircurrentlocations
intelevisionshowsormoviestheywerewatching,whattheywanttowatch,trending
content,userrecommendations,andtheirratings.

32 Microservices: DependencyTypes
This style of decomposition into services differs from the Audible example.
Instead of services that encapsulate other services in order to derive their own
responsefromtheresponsesofdependentservices(c.f.,inAudible,verifyownership
toallowdownloadsofaudiofiles)manyoftheservicesinNetflixexamplehaveno
dependenciesandhaveverylittleimplicitorderingbetweenthem. Infact,mostof
these requests can be performed in parallel. These types of high-fanout content-
drivenapplications, whereindependentdatacanbe retrievedinparallel,typically
resultingraphsthatcontainmorebreadth,ratherthandepth.
Indirect contrast to theAudibleexample,Netflixdoes not wanttofailtheentire
homepageloadifoneoftheseservicesisdown. Instead,theyprefertoomitorload
alternativecontenttoprovideahomepagethatmaynotbeasrichinthepresenceof
failure.
While the list of services presented comes from several Netflix presentations
on chaos engineering, the precise fallback behavior is only known to Netflix em-
ployees. However,itisknownfromthesepresentationsthatfallbackbehaviorfor
eachserviceexists,solibertiesweretakento“re-imagine”whatreasonablebehavior
might be in the presence of dependency failure. One such example of this is the
assumptionthatwhentheuserrecommendationserviceisunavailable,theglobal
recommendationserviceisusedinsteadbyshowingcustomerswhat’sbeingrecom-
mendedtoeveryoneifuser-specificrecommendationsareunavailable. Similarly,if
thecustomersrecentlywatched,butunfinished,movieswereunavailable,display
moviesortelevisionshowscurrentlytrendingworldwideinstead.
Inallthesecases,providingalternativecontentonthehomepageovershowing
thecustomeranerrorpageisalwayspreferable: gracefuldegradationinpractice.
Therefore,gracefuldegradationcanbedefinedasfollows:
Definition5(GracefulDegradation). Gracefuldegradationinamicroserviceapplication
occurswhen,onunavailabilityofaservicedependency,themicroserviceapplicationoptsto
swallowthe error and alter its behavior in response totheunavailability, in either a manner
thatisdirectlyvisibletothecallerimmediately,duringsomesubsequentrequest,ornotat
all.
3.3 Takeaways
Classifyingdependenciesaseitherhardorsoftiscriticaltohowmicroserviceappli-
cation developers deal with partial failure in microservice applications. In short,
developers prefer soft dependencies, where failures can be mitigated at runtime
byignoringorcompensatingforthefailurewithdatafromadifferent,responsive
service. However, soft dependencies can often not be used; for example, if the

Takeaways 33
customer’suserinformationcannotberetrieved,itmaybeimpossibletoproceed.
AnexampleofthiswaspresentedinboththeAudibleandNetflixexamples.
When soft dependencies can be used, this is typically called graceful degrada-
tion. In essence, it is always preferred to give the customer a slightly incorrect or
incomplete answer over giving them an error, where they may turn to different
vendors of the same consumer service (i.e., when Uber, a ride-sharing service, is
returningerrors,usingLyft,analternative,competingride-sharingserviceasthe
cost of switching services is relatively low.) Therefore, using soft dependencies
enablesapplicationstobehighlyresilienttofailuresthatmayaffectcustomers.

Chapter 4
Microservice Application Corpus
“Ireallyenjoylisteningtostories. Irememberthemandkeeptheminmymind.”
AbbasKiarostami
Thefirstchallengeinapproachingthedesignofanewfaultinjectiontechnique
formicroserviceapplicationsistounderstandthestructureofindustrialmicroser-
vice applications and the type of faults that affect them. In other fields, such as
software testing and distributed systems, this is typically performed using open-
sourceapplicationsandbugcorpora. Unfortunately,whileopensourcemicroservice
applicationsdesignedforinstructiononmicroserviceapplicationdesign[Soc;Hip],
and microservice application research corpora [Gan+19] do exist, a corpus of real-
isticmicroserviceapplicationscontainingfaults,oremployingresiliencetechniques,
remainsunavailableformicroserviceapplicationresearchers.
For example, much of the research into testing distributed data system for re-
siliencereliesonopen-sourceinfrastructuresoftware(e.g.,Zookeeper,Cassandra,
HDFS) where all of the development of this software is performed using both a
publicbugtrackerandpublicsoftwarerepositorythatcontainallhistoricalrevisions
ofthesoftwareandthereasonsforeachchange. Theseresourcesallowresearchers
toreproducepreviouslyencountered,oftenfullydocumented,bugs. However,most
ofthese projectsare monolithicindesign anddo notresemblemicroservice appli-
cations: in short, they aresingle applications, thatwhile distributed, are typically
constructedinamonolithicstylewheretheyaredeployedinreplicasets. Rather,
unfortunately, theydonotreflect thetypeofmicroservice applicationsbeingbuilt
today: whereeachserviceprovidesitsuniquebusinesslogic,andmodularization,
fordeveloperproductivity,isacoredesigntenet. Forexample,Uber,aride-sharing
service,2020had2,200microservices,eachprovidinguniquefunctionality.
35

36 MicroserviceApplicationCorpus
Asanotherexample,mostoftheresearchintothetestingofmonolithicsoftware
usesbugdatabasesassembledbytheresearchcommunity: collectionsofsoftware
projectswithdocumentedbugsharvestedfromopen-sourcecoderepositories. How-
ever, these projects suffer from two issues that make them unsuitable for use in
microservicetesting:
1. Theseapplicationsaremonolithicindesign,lackingcommunicationoverthe
networkbetweendifferentsystemcomponents.
2. Many, if not all, of the bugs in the significant bug repositories contain bugs
thatcouldbeidentifiedthroughtraditionalsoftwaretestingusingregularunit
orfunctionaltests. Simplyput,thesebugsarenotspecifictoresilienceissues
inmicroservicearchitectures.
Therefore, to perform this research, it was necessary to create an application
corpusthatcouldbeusedasthebasisforresearch.
To create this corpus, conference talks at industry events such as Chaos Conf
and AWS re:Invent were used, where it is common for industry practitioners to
discussandadvocatefortheuseofchaosengineering. Thefollowingsearchterms
wereusedtofindthesetalks: “chaosengineering”or“resilence”,“chaos”,or“fault
injection”. Buildinguponthis,companiesthatsoldchaosengineeringserviceswere
also identified, and their public client lists were then used to perform a reverse
searchforthesecompaniestofindapresentationorblogpostdiscussingtheiruse
ofchaosengineering.
Intotal,50presentationsweresystematicallyreviewed,whichrepresented32
differentcompanies1)onchaosengineering. Theseincludedtechnicaltalkshosted
onYouTubeandblogposts. Thisreviewdemonstratedthatchaosengineeringisused
bycompaniesofallsizes,inallsectors,includingbutnotlimitedto;largetechfirms
(e.g.,Microsoft,Amazon,Google),bigboxretailers(e.g.,Walmart,Target),financial
institutions (e.g., JPMC, HSBC), and media and telecommunications companies
(e.g.,CondeNast,mediadpg,Netflix.)
Inthemajorityofthesepresentations,companieshadatleastoneoftwomajor
concerns: concernsaroundthereliabilityofsoftwareunderdevelopmentandthe
reliabilityofthecloudinfrastructurethatthecompanywasrunningitssoftwareon.
Fromthere,thepresentationswerefilteredusingthefollowingcriteria:
1. Didthepresentationsdetailarealbugtheydiscoveredusingchaosengineer-
ing?
1Providedisthelisttoasinglerepresentativepresentation,eachofthe32. Chaosengineering
wasusedinonecase,butnotalkorblogpostdiscussingitsusewasavailable[Mei24c].

37
2. Didthepresentationrunachaosengineeringexperimentthatcouldhavebeen
performedlocally?
Finally, bugs where the bug did not occur in the application code but instead
were related to incorrect cloud configuration were filtered out. These examples
ranged from the incorrectconfiguration of authorization policies(c.f., AWSIAM)
tomissingauto-scalingrules(c.f.,AWSEC2.)
Intheend,fourpresentationswereselected,whichrepresentedthefollowing
companies: Audible, Expedia, Mailchimp, and Netflix. It is important to note
that these are not full microservice applications: but, rather only contain a small
subsetofservicesusefulfordemonstratingaresiliencetechniqueorbugrelatedto
microserviceapplicationresilience. Thesearetheindustryexamples.
• Audibleisacompanythatprovidesanaudiobookstreamingmobileapplica-
tion. In theirpresentation, theydescribe abug wherethe applicationserver
does not expect to receive a NotFound error when reading from Amazon S3.
Thiserrorisunhandledinthecodeandpropagatedtothemobileclientwith
agenericerrormessage. Theydiscoveredthisbugusingchaosengineering.
• Expedia is a company that provides travel booking. In their presentation,
theydiscussusingchaosengineeringtoverifythatiftheirapplicationserver
attempts to retrieve hotel reviews from a service that sorts them based on
relevanceand thatserviceisunavailable,theywill fallbacktoanotherservice
thatprovideschronologicallysortedreviews.
• Mailchimp is a product for e-mail communication management. In their
presentation,theydiscusstwobugs:
1. legacy code that does not handle the case where their database server
returnsanerrorcodetoindicatethatitisread-only;and
2. oneservicebecomesunavailableandreturnsanunhandlederrortothe
application.
Bothofthesebugswerediscoveredusingchaosengineering.
• Netflix isamediastreamingproduct. Intwooftheirreviewedpresentations,
NetflixdiscussestheservicesinvolvedinloadingaNetflixcustomer’shome-
page. Netflix doesn’t disclosethe actualfallback behavior foreach servicein
thesepresentationsbutinsteadalludestopossiblefallbackbehavior. During
corpusconstruction,libertiesweretakenastowhatthisbehaviorwas.
Inoneofthesepresentations, Netflixdiscussesseveralbugs theydiscovered
usingtheirchaosengineeringinfrastructure. Theseare:

38 MicroserviceApplicationCorpus
1. Misconfiguredtimeouts:
Nestedservicecallsaren’tconfiguredcorrectlytoallowrequeststhattake
longerthanexpected,butremainwithinthetimeoutinterval;
2. Fallbackstothesameserver:
Servicesareconfiguredwithfallbacksthatpointbacktothefailedservice;
and
3. Criticalserviceswithnofallbacks:
Criticalservicesdonothavefallbacksconfigured.
Allthreeofthesebugswerere-createdinthecorpus.
Inadditiontothesefourindustryexamplesinthecorpus,thecorpusalsocon-
tains8smallmicroserviceapplications,thecinemaexamples,eachdemonstratinga
particularpatternobservedinmicroserviceapplicationsduringthesurvey. Thecin-
emaexamplesdemonstratethevariousimplementationstrategiesforanapplication
thatbooksticketsformovieviewingsmayhave.
Eachexamplecontainsunittestsaswellasfunctionalteststhatverifythefunc-
tionalbehavioroftheapplication. Sincethefunctionaltestswerenotdiscussedin
mostofthetalks,afunctionaltestwaswrittenthatreflectstheapplication’s“happy
path”behavior. Forthecinemaexamples,the“happypath”testattemptstoretrieve
themoviebookingsforaparticularuser.
All examples in the corpus are implemented in Python using the Flask web
framework. Each example can be run locally in-process or in Docker containers.
UsingDockercontainers,eachexamplecanalsoberuninanyKubernetesenviron-
ment(e.g.,minikube,AWSElasticKubernetesService)asdeploymentandservice
configurationsareprovidedforeachservice.
4.1 Cinema Examples
An open-source tutorial microservice application [Bui] was used as the starting
pointfor eachoftheseexamples. This applicationmimics anonlinecinema service
whereuserscanlookupinformationonthemoviesthattheyhavebookingsfor.
It’scomposedof4services,whereafunctionaltestexercisescorebehavior:
• Showtimes:
whichreturnstheshowtimesformovies;
• Movies:
whichreturnsinformationforagivenmovie;

CinemaExamples 39
• Bookings:
which,givenausername,returnsinformationabouttheuser’smoviebookings;
and
• Users:
whichstoresuserinformationandorchestratestherequestfromtheenduser
by first requesting the users’s bookings, and for every booking performs a
subsequentrequesttothemoviesserviceforinformationaboutthemovie.
A diagram of the structure of this application and the request path for this
functionaltestinFigure4.1. Inthisdiagram,theShowtimesserviceisnotcontacted
butwasincludedbytheoriginaltutorial,becausethatserviceisnotinvolvedinthis
functionaltest.
Figure4.1: Cinemaexamplesinthemicroserviceapplicationcorpus.
Thereare8cinemaexamples. Eachdemonstratesadifferentpatternobservedin
microserviceapplications. Here,thedetailsofeachcinemaexampleareprovided,
allexamplesaremodificationstocinema-1,unlessotherwisespecified.
• cinema-2:
Modifications: TheBookingsservicetalksdirectlytotheMoviesservice.
• cinema-3,derivedfrom cinema-2:
Modifications: TheUsersservicehasaretrylooparounditscallstotheBookings
service.
• cinema-4,derivedfrom cinema-2:
Modifications: Each service talks to an external service before issuing any
requests: the Users service requests IMDB; the Bookings service requests
Fandango;theMoviesservicemakesarequesttoRottenTomatoes.

40 MicroserviceApplicationCorpus
• cinema-5,derivedfrom cinema-1:
Modifications: Allrequestshappenregardlessoffailure;intheeventoffailure,
ahard-coded,default,responseisused.
• cinema-6,derivedfrom cinema-1:
Modifications: AddsasecondreplicaoftheBookingsservice,thatiscontacted
intheeventoffailureoftheprimaryreplica.
• cinema-7,derivedfrom cinema-6:
Modifications: theUsersservicecallsahealthcheckendpointontheprimary
Bookingsservicereplicabeforeissuingtheactualrequest.
• cinema-8,derivedfrom cinema-1:
Modifications: The example is collapsed into monolith where an API server
makesrequeststoitwitharetryloop.
4.2 Industry Examples
This section provides a description of the four industrial examples contained in
the corpus: Audible, Expedia, Mailchimp, and Netflix. These examples are not
meanttoreproducetheentiremicroservicearchitectureofthesecompanies. Instead,
they focus only on the services involved in a particular chaos experiment that they
performed.
4.2.1 Audible
TheAudibleexamplewaspresentedinSection3.1. ComparedtoAudible’sactual
deployment,someofthecomponentsrepresentedhereasservicesarecloudservices:
1. theAssetMetadataandAudioAssetsservicesareAWSS3buckets;Tosimulate
this, HTTP services were created that either return a 200 OK containing the
assetifavailableora404 Not Foundiftheassetisn’tpresent.
2. The Ownership and Activation services are AWS RDS instances. To simu-
late this, HTTP services were created that implements a REST pattern: a
403 Forbiddenisreturnediftheuserdoesnotownthebook,a404 Not Found
ifthebookdoesn’texist,otherwise,a200 OK.
3. The Stats service is an AWS DynamoDB instance. To simulate this, a HTTP
servicewascreatedthatreturnsa200 OK. Itwasnotnecessarytoimplement
anegativeresponseasitwasnotrequiredforthereproductionofthebug.

IndustryExamples 41
Asimpletestwaswrittenforthefunctionaltestthatattemptstodownload(or
stream)auser’saudiobook. Forthebug,theAssetMetadataservicecanreturna
404 Not Foundresponseifthechapterinformationforabookismissing. Thisisthe
precise bugdiscussed inthe Audiblepresentation andcauses a genericerror tobe
presentedtotheuserinthemobileapplication.
4.2.2 Expedia
TheExpediaexample,presentedinFigure3.2,has3services:
• ReviewML:
Returnsreviewsinrelevanceorder;
• ReviewTime:
Returnsreviewsinchronologicalorder;and
• APIGateway:
ReturnsreviewstotheuserfromeitherReviewMLorReviewTimebasedon
serviceavailability.
TheExpediaexamplehasonefunctionaltestthatloadstheinformationforahotel
fromtheAPIgateway. Inthisexample, thereisn’taspecific bugbutareplication of
achaosexperimentthatExpediadidrun.
4.2.3 Mailchimp
TheMailchimpexample,presentedinFigure3.2,has5services:
• Requestmapper:
MapsprettyURLsine-mailcampaignstoactualresourceURLs;
• DBPrimary:
Theprimaryreplicaoftheirdatabase;
• DBSecondary:
Thesecondaryreplicaoftheirdatabase;
• AppServer:
Requests the Requestmapper service to resolve a URL and then perform a
read-then-writerequesttothedatabase,withfallbacktosecondarydatabase
replicaiftheprimaryreplicaisunavailable;and

42 MicroserviceApplicationCorpus
• LoadBalancer:
Loadbalancesrequests.
ComparedtoMailchimp’sactualdeployment,someofthecomponentsrepre-
sentedasservicesarenon-HTTPservices:
1. the DB Primary and Secondary services are MySQL instances. To simulate
this,anHTTPservicewascreatedthateitherreturnsa200 OKonasuccessful
readorwriteora403 Forbiddenifthedatabaseisread-only.
2. theLoadBalancerserviceisanHAProxyinstance. Tosimulatethis,anHTTP
proxyservicewascreatedinPython.
For the functional test, a URL is resolved using the service. For the bugs, the
Mailchimpexamplecontainstwo:
•
Bug#1: MySQLinstanceisread-only.
Whenthe MySQLinstanceis read-only, thedatabasereturns anerrorunhan-
dledinoneareaofthecode. SinceMailchimpusesPHP,thiserrorisrendered
directlyintothepageoutput,whichissimulatedbyturningthe403 Forbidden
responseintooutputdirectlyinsertedintothepage.
•
Bug#2: Requestmapperisunavailable.
When the Requestmapper service is unavailable, the App Server fails to
properly handle the error, returning a 500 Internal Server Error to the
Load Balancer. However, the Load Balancer is only configured to handle
a 503 Service Unavailable error by returning a formatted error page. This
isanexampleofmissingorincorrectfailurehandling.
4.2.4 Netflix
TheNetflixexamplewaspresentedinSection3.2. However,intheirpresentations,
their fallback behavior is just provided as an example. Therefore, in the corpus,
arbitrary but realistic choices are made on what the fallbacks should be seemed
to reflectpossible fallback behavior. In short, thespecific fallback doesnotmatter
when it comes to fault injection testing to identify bugs, but rather, a reasonable
fallresent.
Twoexamplesoffallbackbehaviorimplementedinthecorpus:
1. whenthe Bookmarksare unavailable,load Trendingcontent insteadand log
errortoTelemetry;and

Takeaways 43
2. whenUserRecommendationsareunavailable,loadGlobalRecommendations.
Forthefunctionaltest,thereisasinglefunctionaltestthatattemptstoloadthe
Netflix homepage for auser. For thebugs, the Netflix example contains three that
canbeactivatedwithanenvironmentvariable.
•
Bug#1: Misconfiguredtimeouts.
TheUser Profileservice callstheTelemetry servicewitha timeoutof 10sec-
onds;however,theAPIGatewaycallstheUserProfileservicewitha1-second
timeout.
•
Bug#2: Fallbackstothesameserver.
IftheMyListserviceisunavailable,thesystemwillretryagain.
•
Bug#3: Criticalserviceswithnofallbacks.
TheUserProfileservicedoesnothaveafallback.
4.3 Takeaways
The construction of a microservice application corpus is critical in the ability to
enablepracticalmicroserviceresearchintobuildingresilientapplicationsthrough
testing. AsdiscussedinChapter2,thelackofanindustrialcorpusformicroservice
resilience, containing both bugs and common resilience patterns is believed to
be a limiting factor in existing academic research on microservices. Towards this
goal, this newly createdcorpus[Mei24b] servesas anessential foundationin this
dissertation. Additionally, it has also already been applied by other researchers
towardsthisgoal[RPA22].

Chapter 5
Distributed Execution Indexing
“Sometimes,thesongsthatweheararejustsongsofourown.”
Garcia&Hunter,EyesoftheWorld
Atthecoreofanyautomatedexhaustivefaultinjectiontechniqueformicroservice
applicationsimaginableistheneedtouniquelyanddeterministicallyidentifyevery
RPCamicroserviceapplicationissues. Forexample,intheAudibleexamplethat
ispresentedinFigure3.1,onemustidentifytheRPCissuedbetweentheContent
DeliveryServiceandtheAudibleDownloadServicebothuniquelyanddeterminis-
ticallyacrossallexecutionswhereanaudiobookisretrieved. Thisisnecessarytoknow
whentheexhaustivesearchiscompleteandallpossiblefaultshavebeeninjected.
While this may seemrelativelytrivial, asit only requires the identificationof a
singleedgeinamicroservicegraph,itbecomesmorecomplexwhenmultipleRPCs
betweenthesamepairsofservicesmayexistinthesameexecution. Theprogram-
mingpatternsthatcausethisbehaviorarerelativelycommonplace: loops,branching,
functionindirection,andconcurrency. Inthissection,theseprogrammingpatterns
aredescribedandusedtomotivatethedesignofanewalgorithm.
Tosolvethisproblem,analgorithmcalledDistributedExecutionIndexing (DEI)
ispresented. DEIassignsidentifierstoRPCswhileguaranteeingthatidentifiersare
both unique within an execution and deterministic across multiple executions of
thesamecode.
DEIdiffersfromthestateoftheartinbothindustriallibraries(e.g.,Zipkin[Zip],
Dapper [Sig+10], Jaeger [Jae], OpenTelemetry [Ope]) and academic (e.g., Pivot
Tracing[MRF18],3MileBeach[Zha+21a])proposals,asitisdesignedspecifically
foruseduringtestingasitishighercost, butwhenused,providesguaranteesnot
available inprevioussystems. Thesedifferencesareusefulfortestingmicroservice
applicationsexhaustivelyusingfaultinjection.
45

46 DistributedExecutionIndexing
DEI both buildson and inherits its namesakefrom execution indexing[XSZ08],
atechniqueforidentificationoffunctioninvocationsinmonolithicprograms. How-
ever,DEIdiffersfromexecutionindexinginthatratherthanidentifyingtheseries
ofmethodinvocationsleadingtoaprogramexecutionpoint,itaimstoidentifythe
remotemethodinvocationsthatleadtoaparticularprogramexecutionpoint.
5.1 Algorithm Requirements
Aswithalldynamicprogramanalyses,ofwhichanexhaustivemicroservicefault
injectiontesting approachis,theymust ideallybeboth soundandcomplete. For
thefollowingdefinitions,afaultinjectionanalysisisassumedwhichsystematically
performsfaultinjectionforallidentifiedRPCsissuedbyamicroserviceapplication.
Therefore,wecandefinesoundnessandcompletenessasfollows:
Definition 6 (Soundness). RPCs selected for fault injection must have faults injected
ononlythoseRPCs. SoundnessisviolatedwhenafaultisinjectedonanRPCinvocation
whereitwasnotintended.
Ifnot,eitherbecausemultipleRPCssharethesameidentifierornondeterministic
assignmentonrepeatedexecutions,suchanapproachwillexhibitunsoundbehavior,
whichmaypreventbothdeterministicreplay(i.e.,debugging)andexhaustivesearch
asfaultsmaybeinjectedontheincorrectRPCs.
Definition 7 (Completeness). RPCidentifiersmustbeuniquewithinagivenexecution
anddeterministicallyassignedacrossallexecutions.
Ifnot,theanalysiswillexhibit incompletebehavior,whereexhaustivesearch
mayfailtoexploretheentirefaultspaceproperly.
Definition 8 (Correctness). An exhaustive fault injection analysis can only be correct if
theassignment ofidentifiersto eachRPC,used fortargetingtheinjection offaults,is both
soundandcomplete.
Ifnot,theanalysismayfailtoinjectfaultswherefaultsshouldbeinjected (i.e.,
falsenegative)andmayinjectfaultswherenotintended(i.e.,falsepositive.)
5.2 Synchronous
Distributed Execution Indexing
TomotivateDistributedExecutionIndexing (DEI),thesimplestpossibleRPCidentifi-
cationmethodisused. Fromthere,complexityisaddedtoaddressprogramming
patternscommoninindustrialmicroserviceapplications.

SynchronousDistributedExecutionIndexing 47
5.2.1 Signatures Are Too Coarse-Grained
ConsiderastraightforwardwayofidentifyingRPCs,usedbyotherfaultinjection
approaches,theRPC’ssignature. ARPCsignatureisdefinedasfollows:
Definition 9(Signature). Asignatureisatriple (𝑚,𝑓,𝑎) where
• 𝑚 isthemoduleorclassnameoftheRPCstub;
• 𝑓 isthemethodorfunctionname,and
• 𝑎 istheparameternamesandtypes.
This technique is agnostic to the RPC framework and can be easily used to
representbothofthemostcommon: HTTPandgRPC.WithgRPC,theclassname
andmethodmapdirectly;parametersaretheparametertypesandnamesforthe
gRPCendpoint. WithHTTP,theURIandHTTPmethodcanbecombinedtoform
thesignatureasitcontainsthetargetservice,methodname,andparameternames
and types, which are assumed to be String. Let us see how the RPC signature is
toocoarse-grainedtoidentifyanRPCuniquelyanddeterministically.
Considerthe exampleinFigure5.1. Inthis example, amicroservice application
comprised of two services is presented inpseudocode. ServiceA exposes a single
RPC endpoint, helloworld, which issues two RPCs to Service B’s RPC endpoint,
echo,beforecombiningtheresponsesandreturningaresponse. IfServiceBisdown,
adefaultresponseisreturnedbythefunctionwrappingtheRPConline8.
InthecaseoftheRPCinvocationatline10,thesignaturewouldbecomposed
of the target service name B, the method echo, and the parameter (s,String). In
thisapplication,thesignatureforbothoftheRPCsinvokedbyServiceA,onlines
3 and 4, would be identical: (B,echo,(s,String)). Therefore, an analysis using
signaturealonewouldnotbeabletodistinguishbetweenthefirstandsecondRPCs
forfaultinjection;thatis,theRPCsignaturealoneistoocoarse-grainedforidentifying
aparticularRPC.
5.2.2 Increasing Granularity: Invocation Count or Call Stack
Increasing the assigned identifiers’ granularity is one solution for resolving the
issuewhereidenticalidentifiersareassignedtodifferentRPCs. Here,thetwoways
this could be accomplished are examined to demonstrate that they must be used
together.
Inthefollowingdiscussion,sincethepresentationgoesbeyondjustsignature-
basedidentifiers, itisassumed(for easeofpresentationand withoutlossofgener-
ality)thataservice(say A))makesRPCinvocationstoonlyoneotherservice(say

48 DistributedExecutionIndexing
@service_a.method("helloworld")
1
def service_a_helloworld():
2
hello = echo("Hello")
3
world = echo("World")
4
s = hello + " " + world
5
return s
6
7
def echo(s : String):
8
try:
9
res = rpc(service_b, "echo", s)
10
log_success(res)
11
return res
12
except Exception as e:
13
log_error(e)
14
return s
15
16
@service_b.method("echo")
17
def service_b_echo(s : String):
18
return s
19
Figure5.1: RPCsignaturealonecannotdistinguishbetweentheRPCsissuedonlines3and
4;callstackorinvocationcountmustbecombinedwithsignature.
B)andonlyasingleRPCendpoint(e.g. echo)perservice. Thus,onlytheinvoking
servicename (e.g., A)is usedas ashorthandfor anoutgoingRPC from Athat stands
inforthefullsignature,whichwouldcontainthetargetservice,methodname,and
themethod’sformalparameters.
1. Invocationcount.
3MileBeachkeepstrackofthenumberofinvocationsforeachRPCcallsiteto
distinguish multiple calls to the same call site. In Figure 5.1, the same RPC
is invoked twice. The symbol “|” indicates the invocation count of an RPC
signature. Forexample,theidentifiers𝐴| and𝐴| distinguishthe1st and2nd
1 2
RPCinvocationsmadefromServiceAatline10.
2. Callstack.
Another approach is to increase the granularity of the identifier with some
representationofthecallstack. InFigure5.1,theRPCisinvokedtwiceatline
10,however,withdifferentcallingcontextsfortheechofunction(lines3and

SynchronousDistributedExecutionIndexing 49
4). Asuperscript indicatesthelinenumber(s)correspondingtothecallstack
atthetimeofinvocation. Forexample,thetwoRPCinvocationsinFigure5.1
|     | canbedistinguishedbyidentifiers𝐴3,10 |     |     |     |     | and𝐴4,10. |     |     |
| --- | ------------------------------------ | --- | --- | --- | --- | --------- | --- | --- |
FortheexampleinFigure5.1,eitherinvocationcountorcall-stack-basedidentifi-
cationworkstodisambiguatethetwoRPCs. However,neitherapproachissufficient
on itsownin general. Abetter approachis touse acombinationof invocationcount
and callingcontextsforidentifyingRPCs,e.g.,𝐴3,10| ,denotingthefirstinvocation
1
| ofRPCfromAwiththecallingcontext |     |     |     |     | (3,10). |     |     |     |
| ------------------------------- | --- | --- | --- | --- | ------- | --- | --- | --- |
Todemonstratetheneedforboththeseterms,thereaderisreferredtoFigure5.2.
In Figure 5.2, the reader is presented with a different implementation for A; it is
assumedtheexactimplementationofBfromFigure5.1. Inthisexample,A’sRPC
endpoint helloworld takes, as parameters, a list of String. For each String that
is provided, an RPC is invoked to B’s echo endpoint. If the RPC to B throws an
exception,theremainderofthelisttraversalisabortedandafinalRPCismadeto
B using a default value and that value is returned by A. When no exceptions are
thrown,theaggregatedresultsarejoinedandreturnedbyA.
Consider a functional test that invokes helloworld with a list containing two
Strings. Forsimplicity,itisassumedthateachRPCcanonlythrowasingleruntime
exception. Therefore,anexhaustiveanalysismustrunfivedifferentexecutions.
First, consider the execution where both loop iterations execute and all RPCs
are successful, denoted as a sequence of RPC invocations: 𝑒 : (𝐴8| ,𝐴8| ). Next,
|     |     |     |     |     |     |     | 1   | 1 2 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
considerthe executionswherethe RPCthrowsanexception,using the¬symbolto
injectedinthe2nd
| denotea | failedRPCinvocation. |     |     | Whenafaultis |     |     |     | iterationofthe |
| ------- | -------------------- | --- | --- | ------------ | --- | --- | --- | -------------- |
loop, there are two cases when the fallback RPC either completes successfully or
fails: 𝑒 (𝐴8| ,¬𝐴8| ,𝐴16| ), 𝑒 (𝐴8| ,¬𝐴8| ,¬𝐴16| ). Finally, considertheexecutions
|     | :   |     | :   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | 2 1 | 2 1 | 3   | 1   | 2   | 1   |     |     |
where the RPC throws in the 1st iteration and the fallback RPC either completes
| successfullyorfails: |     | 𝑒 (¬𝐴8| | ,𝐴16| | ),  | 𝑒 (¬𝐴8| | ,¬𝐴16| | ).  |     |
| -------------------- | --- | ------- | ----- | --- | ------- | ------ | --- | --- |
|                      |     | :       |       |     | :       |        |     |     |
|                      |     | 4       | 1     | 1   | 5       | 1      | 1   |     |
Usingthisexampleandthesetestexecutions,itisnowdemonstratedwhyinvo-
cationcountandcallstackare,bythemselvesandincombinationwiththesignature,
insufficientforensuringcorrectnessbasedonourcriteria. Therefore,theymustbe
combined.
• InvocationCountAloneisInsufficient.
Consider executions𝑒 and𝑒 . Using invocation count alone these executions
1 4
would instead be represented as𝑒 : (𝐴| ,𝐴| ) and𝑒 : (¬𝐴| ,𝐴| ). However,
|     |     |     |     |     | 1   | 1 2 | 4   | 1 2 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
in𝑒 referstotheinvocationatline8,and𝐴| in𝑒 referstotheinvocationat
𝐴|
|     | 2 1 |     |     |     |     |     | 2 4 |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
line16. Therefore,tocorrectlyassignidentifierstotheseRPCs,thegranularity
mustbeincreasedtoincludethecallstackthatresultedintheRPCinvocation.

50 DistributedExecutionIndexing
@service_a.method("helloworld")
1
def service_a_helloworld(ss : List[String]):
2
rs = []
3
failure = False
4
5
for s in ss:
6
try:
7
r = rpc(service_b, "echo", s)
8
rs.append(r)
9
except Exception as e:
10
failure = True
11
break
12
13
if failure:
14
s = "Hello World"
15
r = rpc(service_b, "echo", s)
16
return r
17
else:
18
return rs.join(" ")
19
Figure 5.2: Signature combined with invocation count insufficient in distinguishing 2nd
iterationofloopfrom1st invocationoffailurehandler;signaturecombinedwithcallstack
insufficientindistinguishingloopiterations.
•
CallStackAloneisInsufficient.
In𝑒 ,bothrequestswouldbeassignedthesameidentifier: 𝑒 : (𝐴8,𝐴8). There-
1 1
fore, to correctly assign identifiers to these RPCs, the granularity must be
increased to include the number of times each RPC invocation statement is
reached.
CombiningtheRPCsignatureandthecallingcontextcreatesadynamicinvocation
signature. Thisallowsforhandlingbothloopingconstructsandconditionalcontrol
flow,aspresentedinFigure5.2. Thisisdefinedasfollows:
Definition10(SynchronousInvocationSignature). Thesynchronousinvocationsigna-
tureforanRPCinvocationisatriple (𝑠,𝑡),usuallydenotedas𝑠𝑡,where:
• 𝑠 isthesignatureoftheRPC;
• 𝑡 representsthecallstackoftheRPC.

SynchronousDistributedExecutionIndexing 51
Thus, the notation𝑠𝑡| refersto the𝑘-th invocationof an RPC with invocationsigna-
𝑘
ture𝑠𝑡. Animportant pointtonoteis thatwhileRPC signatures(Definition9) can
bestatically determined, the invocationsignatures (Definition10) aredetermined
onlybasedonobservedexecutions.
5.2.3 Increasing Granularity: Path to Invoking RPC
Figure5.3isanothervariationofthehelloworldmicroserviceapplication. Similar
toFigure5.2,ServiceAreceivesalistof Strings,invokesanRPConServiceBfor
each memberin the list, andaccumulates the result. Inthe eventof an exception, a
placeholdervalueisaccumulated,andthefailureisrecorded. Therecordedfailures
aretheniteratedinaretryloop,andifsuccessful,thevaluereplacestheplaceholder.
Different from Figure 5.2, Service B invokes an RPC on a third service, Service C,
anddecoratestheresponsesomehowbeforereturningaresponsetoServiceA.
The same functional test is assumed. However, the parameter name s in the
invocationsignaturesisomittedforreadability.
Using the technique from the previous section, the execution where the list
iterationcompletesandnofaultsareinjectedis: 𝑒 : (𝐴9| ,𝐵29| ,𝐴9| ,𝐵29| ). Foreach
1 1 2 1 2
iteration, A issues an RPC from line 9 to B; when B receives the RPC from A, it
issues an RPC to C from line 29. Recall from the previous section that the entire
callstackoftheapplicationisencoded;inthisexample,eachserviceonlycontains
a single method, and therefore, the call stack only includes a single line number.
Whenloopingorotherconditionalcontrolflowisused,includingtheinvocation
countforeachcallsitecaptureseachloopiteration.
Now, consider the functional test execution where a fault is injected on the
RPC in the 2nd iteration of the loop. This execution looks like the following: 𝑒 :
2
(𝐴9| ,𝐵29| ,¬𝐴9| ,𝐴19| ,𝐵29| ). Asbefore,duringthe1st iterationoftheloop,Service
1 1 2 1 2
AissuesanRPCtoServiceBatline9;ServiceBthenissuesanRPCtoServiceCat
line29. Whenthe 2nd iterationof theloop isreached, afaultis injectedforthe RPC
from Service Ato Service B. Then, the failure condition is met, and a subsequent
RPCis issuedfrom ServiceAto ServiceB online 19;Service Bthenissues anRPC
toServiceConline29beforereturningaresponse.
TheissueexperiencedinthisexampleisthattheRPCidentifiedby𝐵29| intest
1
execution𝑒 is not the same as the RPC identified by 𝐵29| in test execution𝑒 . In
1 1 2
execution𝑒 , the RPC from Service B to Service C at line 29 is caused by the RPC
1
issuedbyServiceAonline9. Inexecution𝑒 ,theRPCfromServiceBtoServiceC
2
atline 29is causedby theRPC issuedby ServiceAon line19. These aredifferent,
eventhoughtheyissuethesameRPCwiththesameargumentsandpayload. They
representdistinctcallsitesindifferentpartsofthecode: oneispartofthenormal
operationoftheRPCendpointwherenofailureoccurs,andonerepresentserror

52 DistributedExecutionIndexing
@service_a.method("helloworld")
1
| def service_a_helloworld(ss |     | : List[String]): |
| --------------------------- | --- | ---------------- |
2
rs = []
3
failure = False
4
| failures | = [] |     |
| -------- | ---- | --- |
5
6
| 7 for | s in ss: |                           |
| ----- | -------- | ------------------------- |
| 8     | try:     |                           |
|       | r =      | rpc(service_b, "echo", s) |
9
rs.append(r)
10
|     | except Exception | as e: |
| --- | ---------------- | ----- |
11
|     | failure | = True |
| --- | ------- | ------ |
12
failures.append(len(rs) - 1, s)
13
rs.append("")
14
15
| 16 if | failure: |                 |
| ----- | -------- | --------------- |
| 17    | for (i,  | s) in failures: |
try:
18
r = rpc(service_b, "echo", s)
19
rs[i] = r
20
|     | except | Exception as e: |
| --- | ------ | --------------- |
21
pass
22
23
| return | rs.join(" | ")  |
| ------ | --------- | --- |
24
25
26 @service_b.method("echo")
| def service_b_decorate_echo(s |     | : String): |
| ----------------------------- | --- | ---------- |
27
try:
28
r = rpc(service_c, "echo", s)
29
|     | return r |     |
| --- | -------- | --- |
30
| except | Exception | as e: |
| ------ | --------- | ----- |
31
|     | return s |     |
| --- | -------- | --- |
32
33
34 @service_c.method("echo")
| 35 def service_c_echo(s |     | : String): |
| ----------------------- | --- | ---------- |
return s
36
Figure5.3: RPCsignature,whenextendedwithinvocationcountandcallstack,isinsufficient
whendifferentincomingRPCrequeststriggerRPCinvocation.

AsynchronousDistributedExecutionIndexing 53
handlingcodethatneedstobetestedtoensurecorrectoperationoftheapplication
under failure. Therefore, associating the same identifier to these RPCs results in
bothunsoundandincompletebehavior: eithertheinjectionoffaultsontheincorrect
RPCorthefailuretoexplorethefaultspaceduringanexhaustivesearch.
Toresolvethisissue,thepathofRPCinvocationsthatresultedinthecurrentRPC
mustbeincluded,asthecallstackdoesnotcapturethisinformation. Toachievethis,
alistofidentifiersisaccumulatedasRPCsareinvokedfromservicetoserviceas
partofhandlingareceivedRPCinvocation: forexample, [𝐴9| :: 𝐵29| ]) toindicate
1 1
1st 1st
that the invocation of invocation signature 𝐵29 occurred as a result of the
invocationofinvocationsignature𝐴9.
| Testexecutions𝑒 |        | and𝑒    | canbereformulatedasfollows: |        |         |     |     |
| --------------- | ------ | ------- | --------------------------- | ------ | ------- | --- | --- |
|                 |        | 1       | 2                           |        |         |     |     |
| • 𝑒 : ([𝐴9|     | ],[𝐴9| | :: 𝐵29| | ],[𝐴9|                      | ],[𝐴9| | :: 𝐵29| | ])  |     |
| 1               | 1      | 1       | 1                           | 2      | 2       | 2   |     |
TheRPCinvocationsfromAtoBonline9aredenotedwiththeprefixes𝐴9|
1
| and𝐴9| | toincludetheenclosingRPCfromA. |     |     |     |     |     |     |
| ------ | ------------------------------ | --- | --- | --- | --- | --- | --- |
2
| • 𝑒 ([𝐴9| | ],[𝐴9| | 𝐵29| | ],[¬𝐴9| | ],[𝐴19| | ],[𝐴19| | 𝐵29|  |     |
| --------- | ------ | ---- | ------- | ------- | ------- | ----- | --- |
| :         |        | ::   |         |         |         | :: ]) |     |
| 2         | 1      | 1    | 1       | 2       | 1       | 1 2   |     |
TheRPCinvocationfromBtoConline29isprefixedby𝐴19| ,whichdistin-
1
guishesitfromthe2nd RPCinexecution𝑒 fromAtoBonline9thattriggered
1
theRPCfromBtoConline29.
Definition 11 (Synchronous Distributed Execution Index). The synchronous dis-
tributed execution index for an RPC invocation is a sequence [𝑟 𝑟 𝑟
| 𝑐 :: | 𝑐 :: ··· :: 𝑛 | 𝑐 ]
1 1 2 2 𝑛
where:
• 𝑟 istheinvocationsignatureofthecurrentRPCinvocation;and,
𝑛
• the current RPC invocation is the𝑐 -th invocation of𝑟 with the path having DEI
|        |     |            |     |     | 𝑛   | 𝑛   |     |
| ------ | --- | ---------- | --- | --- | --- | --- | --- |
| [𝑟 ::𝑟 |     | ::𝑟        |     | ].  |     |     |     |
| | 𝑐    | | 𝑐 | :: ··· 𝑛−1 | | 𝑐 |     |     |     |     |
| 1 1    | 2 2 |            | 𝑛−1 |     |     |     |     |
Thedefinitionofasynchronousdistributedexecutionindexisthusrecursive,withthebase
casebeingthetop-levelentrypointtotheapplication,whosepathistheemptysequence [ ].
ThisvariantofDEIis sufficient forapplicationsthatissuesynchronousRPCs,but
whataboutapplicationsthatuseasynchronousRPCstoimproveperformance?
5.3 Asynchronous
|     |     |     | Distributed |     |     | Execution | Indexing |
| --- | --- | --- | ----------- | --- | --- | --------- | -------- |
Recallfromthepreviousdiscussionthedefinitionofinvocationsignatures(Defi-
nition 10). With that definition and the associated discussion, the call stack and
invocation count were enough to distinguish RPC invocations in the presence of

54 DistributedExecutionIndexing
loopsandfunctionindirection. Theseare,however,notenoughtodistinguishRPCs
inthepresenceof concurrencyand theresulting schedulingnondeterminism from
theuseofconcurrency.
Forexample,consider Figure5.4,amodified version ofFigure5.2,where line7
invokesanRPCusingtheasyncprimitiveandtheresultsareawaitedonline11. In
this example, the invoked RPCs execute concurrently, and their execution orders
aresusceptibletoschedulingnondeterminism.
Similartobefore,afunctionaltestisassumedthatinvokesthehelloworldRPC
endpoint with two Strings. For example, the first test execution should read as
follows: 𝑒 : (𝐴7| ,𝐴7| ): 𝐴7| is the RPC invoked in the 1st iteration of the loop,
1 1 2 1
where𝐴7| istheRPCinvokedinthe2nd iterationoftheloop. However,onrepeated
2
executionofthistestthroughdeterministicreplay,orwhenperforminganexhaustive
search,schedulingnondeterminismmayresultinthe2nd iterationoftheloopbeing
assigned𝐴7| ,ifthe2nd blockhappenstoexecutefirst.
1
@service_a.method("helloworld")
1
def service_a_helloworld(ss : List[String]):
2
rs = []
3
4
for s in ss:
5
r = async {
6
return rpc(service_b, "echo", s)
7
}
8
rs.append(r)
9
10
awaitAll rs
11
return rs.join(" ")
12
Figure5.4: Schedulingnondeterminismcanpermutetheassignmentofidentifiers. Inthis
case,𝐴7| ,canrefertotheRPCinvocationfromeitherthe1st or2nd loopiteration.
1
Model checkers for distributed systems also face the problem of scheduling
nondeterminism. However, these model checkers were primarily designed for
identifying concurrency bugs before later being extended for failure testing (e.g.,
message omission) and therefore rely on control of the thread scheduler. This
is unrealistic for large microservice applications where (A) they may not run all
servicesonasinglemachineduringtestingandwhere(B)servicesareimplemented
inseveral languages. Therefore, ideally,asolution tothisproblem willnotrequire
controlofthethreadscheduler.

AsynchronousDistributedExecutionIndexing 55
Therearethreewaysthiscouldbeaccomplished;unfortunately,nonearesuffi-
cient.
1. Cloningperblock.
Oneapproachistoclone thestateusedtogenerateidentifiersforeachasyn-
chronous block. This would ensure that each block would independently
count invocations for each RPCsignature and associated callstack. However,
this approach does not work. In Figure 5.4, this technique would result in
identicalidentifiersforeachoftheRPCsexecutedduringtheloop: (𝐴7| ,𝐴7| ).
1 1
2. Encodethreadcreation.
DeadlockFuzzer [Jos+09], a system for detecting deadlocks in concurrent
programsusingexecutionindexes,takesanalternativeapproachwherethread
creationisincludedintheidentifier. Thisapproachdoesnotworkforasyn-
chronousblocks,astheymayexecuteonanexistingthreadpoolprovidedby
thesystemorframeworkwherethethreadshavealreadybeencreated.
3. Cloningperthread.
If one follows this line of thinking, they could also clone the state used to
generate the identifiers for each thread. This does not work either. In Fig-
ure 5.4, scheduling nondeterminism may causetwoof the RPCs to execute on
asingle threadinone execution (𝐴7| ,𝐴7| ) andon twodifferent threadsina
1 2
subsequentexecution: (𝐴7| ,𝐴7| ).
1 1
Theapproachthatseemsmostpracticalstemsfromakeyobservationaboutmi-
croserviceapplications: whiletheseapplicationsmayissueconcurrentRPCswith
thesamesignature,theseconcurrentRPCsshould rarelycontainthesamepayload:
thepreciseargumentvaluessuppliedatinvocationtime. Therefore,thekeyinsight
isthat,throughtheinclusionofthepayloadineachRPC’sidentifier,identifierswill
be assigned deterministically without requiring control of thread creation or the
threadscheduler. Toachievethis,thestatethatisusedtoderiveidentifiersisshared
acrossallthreadsthatareusedtoexecuteconcurrentcodebyreference.
Thisisreferredtoastheinvocationpayload.
Definition 12 (Invocation Payload). The invocation payload𝑝 for an RPC with𝑛 pa-
rameters is a sequence (𝑘
1
,𝑣
1
)(𝑘
2
,𝑣
2
)...(𝑘
𝑛
,𝑣
𝑛
) such that for each𝑖 in [1,𝑛], the term𝑘
𝑖
is
the𝑖-thargument’snameand𝑣 isthe𝑖-thargument’svalue.
𝑖
ForgRPC,thesearethepreciseargumentvaluesatinvocationtime. ForHTTP,these
arethecombinationofquery-stringargumentsandrequestbody.
In Figure 5.4, and assuming the concrete argument provided to the function
is the list ["Hello", "World"], the execution can be represented as follows: 𝑒 :
1

56 DistributedExecutionIndexing
(𝐴((s,Hello))7| , 𝐴((s,World))7| ). Itisimportanttonotethattheinvocationcount
1 1
intheseidentifiersis1,asitconsidersboththecallstackandpayloadtogether. This
ensuresdeterministicassignmentregardlessofschedulingnondeterminism.
UsingcanusethecombinationoftheRPCsignature,thecallingcontext,andthe
invocationpayloadaasynchronousinvocationsignature foranRPCcanbedefinedas
follows:
Definition 13 (Asynchronous Invocation Signature). The asynchronous invocation
signatureforanRPCinvocationisatriple (𝑠,𝑝,𝑡),usuallydenotedas𝑠(𝑝)𝑡,where:
• 𝑠 isthesignatureoftheRPC;
• 𝑝 istheinvocationpayloadoftheRPC,and
• 𝑡 representsthecallstackoftheRPC.
Thus,thenotation𝑠(𝑝)𝑡| referstothe𝑘-thinvocationofanRPCwithasynchronous
𝑘
invocationsignature𝑠(𝑝)𝑡. Whilethispresentationhasbeenframedusingasync/await,
many other concurrency primitives (e.g., futures, coroutines) exist that have the
samechallenges: thistechniqueextendstoallofthem.
Fromhere,wecandefineaasynchronousdistributedexecutionindex,orwhatwe
willrefertofromhereonasadistributedexecutionindex (DEI).
Definition 14 (Distributed Execution Index). Thedistributed executionindex for an
RPCinvocationisasequence [𝑟 1 | 𝑐 1 ::𝑟 2 | 𝑐 2 :: ··· ::𝑟 𝑛 | 𝑐 𝑛 ] where:
• 𝑟 istheasynchronousinvocationsignatureofthecurrentRPCinvocation;and,
𝑛
• the current RPC invocation is the𝑐 -th invocation of𝑟 with the path having DEI
𝑛 𝑛
[𝑟 1 | 𝑐 1 ::𝑟 2 | 𝑐 2 :: ··· ::𝑟 𝑛−1 | 𝑐 𝑛−1 ].
Thedefinitionofadistributedexecutionindexisthusrecursive,withthebasecasebeingthe
top-levelentrypointtotheapplication,whosepathistheemptysequence [ ].
Thisdesignassumesthatakeyobservationholds: microserviceapplicationsdo
notissueconcurrentRPCsfromthesamecallsite,withthesamecallingcontext,to
thesameservice,containingthesamepayload: whatisbelievedtobevalidfrom
the survey ofmicroservice applications performedduring the constructionof the
microserviceapplicationcorpus.

Implementation 57
5.4 Implementation
DEI’scanberepresentedinseveralformatsinanimplementation,dependingon
therequireduse case. Inthecaseof theimplementationforthisdissertation,three
different formats were realized with an option to reconfigure theiruse at runtime.
However,otherrepresentationsmaybehelpfulwhenapplyingDEI’sinotherdy-
namicanalyses.
5.4.1 Debugging Representation
Forthedebuggingrepresentation,eachelementinaDEIsequenceiscomposedof
fivecomponents:
1. A metadata component, where application developers can add debugging
annotations into their code to populate the metadata section with additional
debuggingtags. This metadatasection defaultsto anempty value whenno
tagsorannotationsareused.
2. Theinvokingservicename,atextualstringoftheinvokingservice’sname. Thisis
notnecessaryforcorrectnessbutmaybehelpfultothedeveloperinidentifying
thecallerofaparticularRPC.
3. Asignature,containingonlytheDEI’ssignature: moduleorclass,methodor
functionname,andparameternamesandtypes.
4. Asynchronouscomponent,containingtherepresentationofthecallstack,as
used in both the asynchronous (i.e., Definition 13) and synchronous (i.e.,
Definition10)invocationsignatures.
5. Anasynchronouscomponent,containing therepresentationoftheinvocation
payload,asusedintheasynchronousinvocationsignature(i.e.,Definition13.)
6. Theinvocationcount fortheinvocationsignature.
Theinvokingservicename,signature,synchronous,andasynchronouscompo-
nentformafive-tupleidentifier. Identifiersandinvocationcountarecombinedinto
atupletorepresentanRPCexecutedbytheapplication. Therefore,asequenceof
tuples forms a DEI, encoded as an array in RPC invocation order, and captures the
RPCinvocationpath.

58 DistributedExecutionIndexing
5.4.1.1 ProjectionandPartialOrders
Thisrepresentationhelpsdebugandanalyzemicroserviceapplicationsbyproviding
several applicable partial orders using a DEI projection algorithm. For example,
severalprojectionshaveprovenusefulduringthisdissertation:
•
IdentifyingallRPCsexecutedinanapplicationtrace.
Byprojectingthesignatureandsynchronouscomponentsofthelastsequence
element ina DEI foreach element inan application tracecontaining several
DEIs,anapplicationdevelopercanidentifyalloftheRPCsexecuted,froma
particularcallsite,inthatspecifictrace.
•
IdentifyingpossiblyredundantRPCsfromthesameservice.
Byprojectingtheinvokingservice,signature,andasynchronouscomponents
inaDEI,developerscanidentifypossiblyredundantRPCs: whenaservice
executesthesameRPC,withthesamearguments,fromthesameservicetwice
aspartofthesametrace,regardlessofthecallsite. Forexample,whenaservice
retrieves the user information twice. Thisis only an over-approximation, as
theRPCmayperformaside-effecttwiceonpurposeinsteadofreadingvalues
usinganRPC.
•
IdentifyingpossiblyredundantRPCsfromdifferentservices.
Byprojectingthesignatureandasynchronouscomponentofthelastsequence
inaDEI,developerscanidentifypossiblyredundantRPCs: whenaservice
executesthesameRPC,withthesamearguments,fromthesameservicetwice
as part of the same trace, regardless of the call site. For example, a service
retrievestheuser,whilesomedependentserviceretrievestheuser. Thismay
indicate that retrieved data should be passed between services instead of
reinvokingthedependency. Asbefore,thisisonlyanover-approximation,as
theRPCmayperformaside-effecttwiceonpurposeinsteadofreadingvalues
usinganRPC.
Similarly,theseprojectionshavealsobeenusedtoidentifysituationswhereRPC
APIscouldbeconstructedtobemoreefficient: forexample,wheretwoRPCsare
issuedtothesamedownstreamservicefromthesameserviceindirectsequence,
where the data from the first RPC is fed into the arguments of the second RPC.
ThiscanindicatethatthedownstreamserviceisnotprovidingthecorrectAPIfor
its callers and may arise naturally from the decentralized nature of microservice
applicationdevelopment.
Thesemicroserviceapplication“smells”andtheirdetectionusingDEIwereused
toconstructacodelinterthatisavailableasopensourceaspartofthisdissertation.

Implementation 59
5.4.2 Verbose and Compact Representations
Theverboserepresentation isthesameasthedebuggingrepresentation. However,
each element in the five-tuple is run through a cryptographically insecure hash
function (e.g., SHA-1) This representationis more space efficient than thedebug
representationbutpreservestheabilitytoidentifysignaturesandcallsitesusing
hashcomparisonuniquely.
ThecompactrepresentationfurthercompactstheDEIrepresentation,necessary
fortracingsystemsthatplaceasizerestrictiononmetadataforwardedwithRPC
invocations,aseachaDEIgrowslinearlywiththedepthofthemicroservicegraph.
5.4.3 Assignment
DEI’sareassignedbyapplyingdecorators(or,inthecaseofanRPCframeworkthat
supports interception of RPC invocations such as Google’s gRPC, interceptors) to
theRPClibrariesinuse. Thesedecorators(orinterceptors)interposeoninvocations
toeachRPCandgenerateaDEIfortheinvocationbeforeforwardingthecalltothe
underlyingRPCframework. Oncegenerated,theymuststorethegeneratedDEIin
outgoing metadata (e.g., HTTP headers, gRPC metadata) to be forwarded to the
nextservice.
Request State. As DEI’s are compositional in their sequence construction, the
incoming DEI,theDEIassignedtotheRPCinvocationthatresultedinasubsequent
RPCexecution,mustbeparsedfromincomingmetadataandstoredinaninterim
location(e.g.,thread-localstate)suchthatitcanthenbeusedinthegenerationof
any subsequent outgoing DEI’s (associated with downstream RPCs) originating
fromthatserviceasaresultoftheincomingRPC.
ThislocationmustbeaccessibletoanydecoratorattachedtoanyRPCframework
used on further downstream executions. For example, when an incoming gRPC
invocationtriggersdownstreaminvocationsofHTTPRPCs,thegRPChandlermust
placethe incomingDEIinto alocationaccessibleby theHTTPlibrary,performing
thesubsequentdownstreamRPC.
ServiceRe-Entrancy. Asservicesmayalsobere-entrant,suchthatServiceAcalls
Service B that then re-calls Service A using possibly a different RPC method, the
state required for generating an outgoing DEI must also be discriminated by the
entry. Inshort,are-entrymustgenerateoutgoingDEI’susingthecorresponding
incomingDEI.
To achieve this, incoming RPCs are assigned a random UUID called a request
identifier associatedwiththeincomingDEI.Therefore,whenaserviceisre-entrant,

60 DistributedExecutionIndexing
a new request identifier is generated for the re-entry, and theassociated incoming
DEI is related to that request identifier. This ensures that any outgoing DEI’s are
generated using the proper incoming DEI. As expected, instead of the incoming
DEI,therequestidentifiermustbeplacedinthesameinterimstate.
Finally, servicesshould exposeamechanism forresettinganyaccumulatedDEI
state. This reset mechanism is responsible for clearing any state, including the
request identifier to DEI mapping and any other state accumulated to track DEI
duringexecution.
Concurrency. Whilestraightforwardintheory,mechanizingthisissignificantly
morecomplicatedin practice. InPython, aprogramming language that contains
concurrencywithnotrueparallelism,theglobalstatecantracktheactiverequest
identifier for the current thread and map request identifiers to DEI’s. However,
where concurrency and true parallelism are present in Java, DEI maintenance is
morechallenging.
For example, when receiving an incoming DEI, a request identifier must first
be assigned and stored in a global mapping of request identifiers to DEI. This
request identifier can then be assigned to thread local storage. Any subsequent
RPCsexecutedbytheinvokedservicecanusetheassociatedDEItoconstructDEI
foranydownstreamRPCinvocations. Butwhathappensiftheinvokedcodespawns
twothreadstoissuetwodownstreamRPCconcurrently?
One solution is to use an inherited thread-local state, such that any created
threadsinherittherequestidentifierandusetheincomingDEI:thisonlyworksif
accesstotherequestidentifiertoDEImappingissynchronized. However,ifthreads
fromapreexistingthreadpoolareusedinsteadofcreatingnewthreads,thestate
will not be present in the local state of the used thread. Therefore, these threads
mustbebootstrappedwithstate,includingthecorrectrequestidentifier(inaddition
tosynchronizingaccesstotherequestidentifiertoDEImappingintheglobalstate).
This state mustbe migratedbetweenthreads upon contextswitches. Thisis further
complicated by task parallel libraries that are built on top of threads in Java (i.e.,
Kotlin, Scala, Clojure) or asynchronous RPC libraries with thread migration (e.g.,
Armeria)whereexecutionofRPCscanoccuracrossmultiplethreads.
Tosolvethisproblem,itisnecessarytoimplementtheunderlyingconcurrency
mechanismsinJava(e.g.,Thread,ForkJoinPool,etc.) andanytaskparallellibraries
written for the JVM (e.g., Kotlin’s CoroutineContext) to migrate any thread local
stateuponcontextswitchestoensurethattherequestidentifierisalwayspresent
whenRPCinvocationsoccur. Thisisnotanewproblem;theauthorsofOpenTeleme-
tryhavealreadydedicatedsignificantefforttosolvingthisproblemfortheirtracing

Takeaways 61
library. Therefore, their existing solution1 is leveraged to ensure that DEI’s are
propagatedaccordinglyinthepresenceofconcurrency.
5.5 Takeaways
DEI’sformoneofthefoundationalcontributionsofthisdissertation: theabilityto
identifythelocationofRPCinvocationsinamicroserviceapplicationinamanner
where they are consistent across executions of the same code. This ensures that
anyfaultinjectionapproachthataimstobeexhaustivecanguaranteethatallRPC
invocations are susceptible to fault injection and that no necessary fault injections
aremissed.
Aspresented,DEI’scanalsohaveapplicabilityoutsideofjustfaultinjectionand
can be used in other types of dynamic analyses: for example, by understanding
application behavior, identifying where RPC APIs may be incorrectly designed,
orwhereredundantRPCinvocationsareperformedandshouldbeoptimizedfor
performance.
1This solution relies on using a special Java instrumentation API (e.g.,
-javaagent INSTRUMENTATION.jar) at runtime to be able to override the implementations of
standardlibraryclasses(e.g.,java.lang.Thread).

Chapter 6
Service-level Fault Injection Testing
“Astoryshouldhaveabeginning,amiddle,andanend,butnotnecessarilyin
thatorder.”
Jean-LucGodard
In this chapter, one of the core contributions of this dissertation is presented:
Service-level Fault Injection Testing (SFIT). SFIT is a technique for identifying a mi-
croservice application’s behavior under fault through the use of automated fault
injectiontesting.
In spirit,SFIT is notunlike the previouslymentioned experimental approaches
tofaultinjection(e.g.,chaosengineering) usedbyindustry: SFIT injectsfaultsatall
of the inter-service communication points (e.g., RPC) to see what the application’s
behavior is under that specific fault. However, SFIT improves on several of the
deficienciesintheexistingacademicresearchinthisareabytakingadeveloper-centric
approach:
•
Exhaustive.
SFITisexhaustiveinthatSFITwillautomaticallyexploretheimpactoffaults
(and combinations thereof) of every RPC executed by a microservice applica-
tion automatically, without requiring that developers specificallyderiveand
manuallyexecutefaultinjectionscenarios.
•
Specification-Free.
Instead of requiring that developers require specifications, in a specification
languagespecific for faultinjectiontesting, SFITuses thefunctionaltest suite
thatdevelopersofmicroserviceapplicationsarealreadywritingtoestablish
whatthe“correct”behavioroftheirapplicationiswhenfaultsarenotpresent.
63

64 Service-levelFaultInjectionTesting
•
Behavior-Focused.
When failures occur due to fault injection, application developers will then
be asked whether or not the failure is legitimate: did the application do the
“correct” thing under failure? If not, SFIT has discovered a bug. If so, the
developersareaskedtoupdatetheirtestsaccordinglywithderivationsfromthe
expectedbehaviorwhenafaultisinjected: forexample,bystatingsomething
shouldnotoccurwhenafaultisinjected.
6.1 Overview
Service-level Fault Injection Testing (SFIT) is a developer-first approach for finding re-
siliencebugsinmicroserviceapplicationsusingfaultinjection. SFITintegratesfault
injectiontestingasearlyaspossible,indevelopment,beforedeploymentofapplication
code and avoids the needforspecifications, written in aspecification language, by
leveraging a developer’s existing integration of functional tests of their application.
Thisdecisioniscritical,makingitsoSFITcanseamlesslyintegratewithdevelopers’
existingdevelopmentenvironmentsandtools.
SFITbuildsonthreekeyobservationsmadeabouthowmicroserviceapplications
arebeingdevelopedtoday:
•
Microservicesdevelopedinisolation.
Microservicearchitecturesaretypicallyadoptedwhenteamsneedtofacilitate
rapidgrowth,breakingtheteamintosmallergroupsthatdevelopindividual
services that adhere to a contract. This contract typically requires two or
moreteams to meetandagree toan APIbetweenthe services theymanage.
Therefore, individual team members typically do not understand the state
orinternalsofservicesoutsidetheircontrolwellenoughtowriteadetailed
applicationspecificationtoverifyitautomaticallywithamodelchecker.
•
Mockingcouldpreventfailures.
Manybugsinmicroserviceapplicationscouldhavebeendetectedearlierifthe
developershadwrittenmocksthatsimulatedthefailureoftheremoteservice
inatestingenvironment.
•
Functionaltestsarethegoldstandard.
Insteadofwritingspecifications,developerswritemultipleend-to-endfunc-
tionalteststhatverifyapplicationbehavior.
SFITstartsbyidentifyingthefaultsthatshouldbeinjectedateachRPCinvocation
siteinamicroserviceapplicationtoconstructthefaultspacethatwillbeexhaustively

Overview 65
searched. Todothis,SFIT usesinformationfromthe underlyingRPCframeworks
to issuethose RPCs: this accounts forboth return valuesthat indicate an errorand
thrownexceptionsattheinvocationsite. SFITalsoreliesoninstrumentedversions
of each RPC framework to identify RPC invocations and perform fault injection.
ThisinstrumentationcommunicateswithaSFITserverinstancethatisresponsible
fordrivingtheexhaustivesearch.
Tostart,SFITusestheexistingfunctionaltestsuiteofthemicroserviceapplication.
Thiscapturesthedesiredbehavioroftheapplicationwhenfaultsarenotpresent.
However,SFITplacesseveralrequirementsonthesefunctionaltests:
1. Alldownstreamdependenciesinvokedbyaservicereturnsuccessfulresponses
whenfaultsarenotinjected.
2. Eachfunctionaltestcontainsacomprehensivesetofassertionstodetectappli-
cation correctness bugs. For example, SFIT requires assertions that capture
anon-customer-visiblesideeffectthatlaterpreventsthecustomerfromper-
formingsomesubsequentactionintheapplication. FromSFIT’spointofview,
theonusofguaranteeingthisisplacedonthetest’sauthor.
With these requirements met, SFIT runs each test in sequence to perform the
fault injection analysis. For each test, SFIT first runs a reference execution where
nofaultsareinjected. ThisisthesameasrunningthetestwithoutSFIT.Then,SFIT
willrepeatedlyre-executeit,injectingdifferent(combinationsof)faultsuntilthe
faultspaceisexplored.
UsingtheAudibleapplicationinFigure3.1,todemonstrate,theRPCsbetween
theAudibleDownloadServiceandit’sdependencieswouldfirstbetestedforall
possible faults and combinations thereof. Then, the RPC between the Content
Delivery Service and its direct dependency, the Audible Download Service, and
so on. As faults are injected, tests will fail. However, this is expected, as most
existingtestsonlyencodetheapplicationbehaviorwhennofaultsexist. Therefore,
developers will be prompted to use fault injection predicates provided by SFIT to
assertthedesiredapplicationbehaviorunderfailure.
SFITsitsattheoppositesideofthedesignspaceoffaultinjectiontestingtech-
niquesformicroserviceapplicationslikechaosengineering[Bas+16;RJ20a;Tuc+18;
Bas+19b]byfocusingonexhaustivecorrectnesstesting,indevelopment,before
deploymentofapplicationcodetoproduction.
Incontrast,techniqueslikechaosengineeringtypicallyrelyoncoarse-grained1
faultinjectionexperimentsdesignedbyhumanswherehigh-levelKeyPerformance
Indicators(KPI)areusedtodetectresilienceissuesintheproductionenvironment:
1crashingorDNSblack-holinganEC2instance.

66 Service-levelFaultInjectionTesting
for example, Netflix’s stream-starts-per-second KPI that indicates only if customers
cannotwatchvideostreamsintheirapplication. Whilechaosengineeringisused
by companies of all sizes, in all sectors — large tech firms (e.g., Microsoft, Amazon,
Google),bigboxretailers(e.g.,Walmart,Target),travelcompanies(e.g.,Expedia),
financialinstitutions(e.g.,JPMC,HSBC),andmediaandtelecommunicationscom-
panies (e.g., Conde Nast, media dpg, Netflix) [Mei+21b] — the cost of running
experimentsin productionisnot thesamefor allthesecompanies. For example,a
chaos experiment that prevents a user from reading an article in the New Yorker
or streaming a movie with Netflix is not the same as preventing a user from pur-
chasingatravelpackagewithExpediaorperformingafinancialtransactionwith
HSBC.ThisindustrialpartnerFoodly,oneofthelargestfooddeliveryservicesin
theUnitedStates,choseSFITspecificallyforthisreason: toverifythecorrectness
oftheirapplicationunderfaultduringdevelopment,beforedeployment,without
impactingcustomers.
Academically,SFITbuildsontheDirectedAutomaticRandomTesting[GKS05]
technique, which combines symbolic execution with concrete execution to explore
allpossiblepathsofamonolithicapplicationbysynthesizinginputsthatprovoke
theapplicationintonewapplicationpaths. Incontrast,SFITprovokesanapplication
intoerror-handlingcodepathsbyidentifyingthelocationsofmethodcallsthatmay
failandinjectingfaults.
6.2 Algorithm
First, some definitions will be presented to start describing the Service-level Fault
InjectionTesting algorithm. Then,thealgorithmwillbepresented,whichassumesa
singlefunctionaltestthatresultsinthemicroserviceapplicationissuinganumber
ofRPCswhenexecuted.
First,thedefinitionofafaultconfiguration,providedtoSFITtoinformitonwhich
faultsshouldbeexplored,ispresented. Then,definitionsofhowtotestexecutions
arerepresentedinternallytoSFIT.
Definition 15(FaultConfiguration). Afaultconfigurationisapartialfunctionfroma
pair (𝑠,𝑝) toasetoffaultspecifications 𝑓𝑠 = {𝑓 1 ,...,𝑓 𝑛 },where:
• 𝑠 isthesignatureoftheRPC;
• 𝑝 istheinvocationpayloadoftheRPC,whichmaybeemptyand
• 𝑓 is a fault specification: a client-specific representation of the fault that should be
injectedintotheapplication.

Algorithm 67
Inreality, 𝑓 canbeanarbitraryobjectindicatinganexceptiontobeinjectedwith
𝑖
asetofpropertiessetontheexception(e.g.,Google’sgRPC)ormayalternatively
bethedescriptionofanHTTPerrorresponsecontainingthestatuscode,body,and
(optional)responseheaders. Itisuptotheinstrumentationtocorrectlyinterpret
and inject this fault, as the precise exception types that may be raised differ by
implementationlanguageoftheinvokingRPCclient(e.g.,Javavs. PythongRPC.)
Definition 16 (Concrete Test Execution). A concrete test execution is a four-tuple
(𝑡,𝑑,𝑓,𝑟) thatrepresentsaconcreteexecutionwhere:
• 𝑡 isthefunctionaltestthatleadstotheinvocationsofthoseRPCs;
• 𝑑 isaset,suchthat {𝑑 ,...,𝑑 } isthesetofdistributedexecutionindexesrepresenting
1 𝑛
alloftheRPCsexecutedbythatfunctionaltest,𝑡.
• 𝑓 isapartialfunctionfromadistributedexecutionindex𝑑 toafaultinjectionspecifi-
𝑖
cations 𝑓 ,forelementsin𝑑 thatindicatesafaultwasinjectedfortheRPCrepresented
𝑖
by𝑑 ;
𝑖
• 𝑟 is a partial function from a distributed execution index 𝑑 to an RPC result for
𝑖
elements in𝑑 that indicates theclient-encoded response ofan RPC invocation under
𝑑.
Concrete test executions are sufficient for a replay of a test execution, given a
deterministic functional test. In short, as long as the application issues the same
RPCs, identified bythe sameDEIs, thesame faultswillbe injectedon thoseRPCs,
resultingindeterministicreplay,giventhesamedeterministicfunctionaltest.
Definition 17 (AbstractTestExecution). Anabstracttestexecutionisatriple (𝑡,𝑑,𝑓)
thatrepresentsapartialconcreteexecution,where:
• 𝑡 isthefunctionaltestthatleadstotheinvocationofatleasttheRPCsin𝑑;
• 𝑑 isaset,suchthat {𝑑 ,...,𝑑 } isthesetofdistributedexecutionindexesrepresenting
1 𝑖
someoftheRPCsexecutedbythatfunctionaltest,𝑡. Thissetisalwaysaprefixofa
valid,well-formedexecutionof𝑡: forexample,thefirst5RPCsexecutedbyatestthat
executes10RPCs.
• 𝑓 is a partial function from a distributed execution index 𝑑 to an fault injection
𝑖
specification 𝑓 ,forelementsin𝑑 thatindicatesafaulthasorshouldbeinjectedforthe
𝑖
RPCrepresentedby𝑑 .
𝑖

68 Service-levelFaultInjectionTesting
Abstract test executions are partial test executions that may or may not result
in more RPCs: for example, by injecting a fault, the application may respond by
executingsubsequentRPCsonfailure. Whenthisdoesnotoccur,theabstracttest
executionanditsassociatedconcretetestexecutionareequivalent.
Next,thesearchalgorithmofSFITispresentedinAlgorithm1. Thisalgorithm
repeatedlyre-executesthetestofthemicroserviceapplication,recordingtheconcrete
testexecutionsassociatedwitheachabstracttestexecution. Duringthisexploration,
new abstract test executions are derived that represent new failure scenarios to
explore: this is called scheduling and presented in Algorithm 2. This combined
processofsearchandschedulingisperformeduntilthefailurespaceisexhausted,
basedontheprovidedfaultconfiguration.
Algorithm1:SFITAlgorithm: Search
ExecutedbySFITatstartofthesearch
1
Function Search(t: Test,c: FaultConfiguration):
2
Executestheinitial,fault-freereferenceexecution
3
4
CurrentFaultConfiguration=c
5
CurrentConcreteTestExecution=ConcreteTestExecution()
6
CurrentAbstractTestExecution=AbstractTestExecution()
ExecTest(t)
7
8
ExploredAbstractTestExecutions.add(CurrentAbstractTestExecution)
9
ExploredConcreteTestExecutions.add(CurrentConcreteTestExecution)
Explorethefaultspacewhileincreasingitasnewfailuredimensionsexist
10
11
whilete=ToExploreAbstractTestExecutions.pop():
12 CurrentAbstractTestExecution=te
13
CurrentConcreteTestExecution=ConcreteTestExecution()
ExecTest(t)
14
15
ExploredAbstractTestExecutions.add(CurrentAbstractTestExecution)
16
ExploredConcreteTestExecutions.add(CurrentConcreteTestExecution)
Search. First,areferenceexecution–afault-freeexecutionofthetest–isperformed,
wherethetestexecutesnormallyunaffectedbySFIT.Duringthisexecutionaconcrete
test execution is constructed that contains the DEI’s associated with every RPC
executedbythemicroserviceapplicationasaresultofthetest.
As a concrete test execution is constructed, a number of abstract test executions
arealsoconstructedthatarescheduledforexecution. Theseabstracttestexecutions

Algorithm 69
areonlypartialtestexecutions: validprefixesoftheconcretetestexecution,upto
theexecutionpointwheretheywerecreated,andcontainingthelocationsoffault
injections. Effectively,theseabstracttestexecutionscontainonlytheRPCsexecuted
bytheapplicationuptothatprogrampointinorderto“fix”theexecutiontosome
particularprogrampointandthenallowforderivationincontrolflowbasedona
listoffaultstobeinjected.
AtleastoneabstracttestexecutioniscreatedforeachRPCthatisexecutedand
eachfaultthatshouldbeinjected. Abstracttestexecutionsareexplorediteratively
untilexhausted,depictedformallyinAlgorithm1.
Scheduling. Abstract test executions contain both the RPCs executed up to a
particularprogrampointandthefaultsthatshouldbeinjectedforthoseRPCs.
Search is performed by executing each abstract test execution, which yield a
correspondingnumberof concretetestexecutions, ofwhich mayormay not extend
theabstracttestexecutionsthatrealizedthem. Forexample,anabstracttestexecution
may contain 4 RPCs, but by injecting a fault on the 4th RPC, the concrete test
execution contains a number of new, previously unobserved, RPCs, which were
invokedbyapplicationerrorhandlingcode.
WhenthesenewRPCsoccurasaresultoffaultinjections–whichdonotexistin
the abstracttest execution that is being executed – additional abstract test executions
arecreatedwhichcontain(A)afaultontheRPCsthatresultedintheadditional
RPCs and (B) a fault on each of the additional RPCs, for each fault in the fault
configuration. Effectively,thenewabstracttestexecutions all“fix”the execution to
the program point containing the injected fault, which resulted in the additional
RPCs, with each abstract test execution exploring a different fault on each of the
additionalRPCs. Thisprocessisiterative,schedulingallpossiblefaultconfigurations
forthesearch.
Asabstract testexecutions areonly generatedoncea programpoint isreached,
noabstracttestexecutionsareeverscheduledforunreachableprogrampoints,given
afaultconfigurationanddeterministictest.
ThecreationofnewabstracttestexecutionsisperformedwheneveranRPCis
executed. When executing a test with SFIT, each invocation of an RPC results in
twomessagesbeingsenttoSFIT.First,ainvocationmessagewhentheRPCclient
issuestheRPC;second,ainvocation_receivedwhentheserverreceivestheRPC.
This separation is necessary for protocol-specific reasons for both Google’s
gRPC and HTTP. First, when issuing calls with gRPC, multiple services may im-
plementthesamegRPCspecificationandrespondtothesamemethod;therefore,
to properly inject faults on the appropriate service it is necessary to determine
precisely the service that terminates the call. For example, even thought a gRPC

70 Service-levelFaultInjectionTesting
Algorithm2:SFITAlgorithm: SchedulingNewTests
ExecutedonSFITanytimethemicroserviceapplicationexecutesanRPC
1
Function OnRPCInvoked(d: DEI,s: Signature,p: InvocationPayload):
2
3 if𝑑 ∈ CurrentAbstractTestExecution.d:
Addtothecurrentconcreteexecution
4
5
CurrentConcreteTestExecution.d.add(𝑑)
ThisRPCappearsinabstractexecution
6
7
if 𝑓 =CurrentAbstractTestExecution.f(𝑑):
Addtothecurrentconcreteexecutionwithfault
8
9
CurrentConcreteTestExecution.f.add(𝑑, 𝑓)
return𝑑, 𝑓
10
else:
11
AllowtheRPCtoexecuteasnormal
12
return Noop()
13
else:
14
Ifweshouldinjectsomefaults...
15
16
if 𝑓𝑠 =CurrentFaultConfiguration(s,p):
Schedulefortestinginsubsequentexecutions...
17
18 for 𝑓 ∈ 𝑓𝑠:
19
NewATE=CurrentAbstractTestExecution
20
NewATE.d.add(𝑓)
21
NewATE.f.add(𝑓)
...onlyifwehavenotalreadyscheduledforexploration
22
23
if NewATE∉ToExploreAbstractTestExecutions:
24
ToExploreAbstractTestExecutions.push(NewATE)
Allowtoexecutenormally
25
return Noop()
26
ExecutedonSFITanytimethemicroserviceapplicationfinishesanRPC
27
Function OnRPCFinished(d: DEI,r: Response):
28
29
CurrentConcreteTestExecution.r.add(𝑑,𝑟)

FaultInjectionPredicates 71
var response = rpc(service\_a, method, args);
1
if wasFaultInjectedOn(service_b, method, args):
2
assertFalse(database.contains(record));
3
assertTrue(response.isFailure()));
4
else:
5
assertTrue(database.contains(record));
6
assertTrue(response.isSuccess()));
7
Figure6.1: SFIT’sfaultinjectionpredicatesareusedtoupdateatesttocaptureanapplica-
tion’sbehaviorunderfault. YellowindicatesaddedlinesduringSFITprocess.
servicemightindicatethatthemethodNotificationService.sendEmailisbeingin-
voked,thatmethodmightbeimplementedbybothaOldNotificationServiceand
aNewNotificationServicewhereonemightonlywanttoperformfaultinjectionon
asingleservice. Second,withHTTP,oftenrequestsaremadeusingahostnameorIP
only: therefore,toproperlydeterminetheserviceSFITmustdeferfaultscheduling
until it knows the actual reported service name of the invoked host. In this case,
SFITdefersfaultinjectionuntiltheactualservicenameisknown.
Inthispresentation,itisassumedthatthesameOnRPCInvokedmethodisused
in either case, as the logic remains the same and is tolerant to whenever clients
reportRPCs(i.e.,clientinvocationorserverinvocation)aslongasaservicename
ispresent. However,itisimportanttonotethatwhentestingthird-partyservices,
the server invocation is not controlled and fault injection must be performed and
configured based on client configuration alone. Whenever an RPC completes, it
invokesonRPCFinished. ThisalgorithmisdepictedformallyinAlgorithm2.
6.3 Fault Injection Predicates
AsapplicationdevelopersapplySFITtotheirfunctionaltests,writtentoassumea
happypathexecutionoftheirapplication,theirtestswillfailasfaultsareinjected.
Therefore, applicationdeveloperswillneedto adapt theseteststo accountforthe
behavioroftheirapplicationunderfault. TheSFITmechanismiscalledfaultinjection
predicates.
Faultinjectionpredicatescanbeusedinconditionalstatementsplacedinfunc-
tional test code tomake assertions on application behavior dependenton whether
faultswereinjected.
Forexample,bywrappingassertionsinstatementssuchasthefollowing:

72 Service-levelFaultInjectionTesting
• “Wasafaultinjectedduringthistestexecution?”
• “Wasafaultinjectedonaparticulardownstreamserviceduringthistestexecution?”
• “WasafaultinjectedonaparticularRPCmethodduringthistestexecution?”
• “WasafaultinjectedonaparticularRPCmethod,withcertainarguments,during
thistestexecution?”
InFigure6.1, exampleusageoffaultinjectionpredicatestomake atestcapture
both the application’s behavior in and without the presence of faults is shown.
Here it is indicated that under a fault injection to a downstream RPC, the response
returnedfromthetestedRPCshouldeithersucceedorfail,withwritesperformedto
the database accordingly. In yellow, the lines that wouldbe added during the SFIT
processarehighlighted. Thisprocessisnotunlikethemethodsusedbysoftware
modelchecking [JM09]or interactivetheorem proving[BC13], wheredevelopers
mustencodeallpossiblebehaviorsforcompletion.
Fault injection predicates use the current concrete execution to determine if
that RPC was subjected to a fault and returns a response to the test. SFIT can be
configured to generate all fault scenarios regardless of whether a previous fault
injectionscenariopassedorstoppedatthefirstfailure. Asalways,uponeachtest
executionwithSFIT,allfaultinjectionscenariosarere-executedandcheckedagainst
thetest’sassertions.
6.4 Testing Process
OutlinedbelowistheSFITtestingprocess:
1. Executethedeveloper’sfunctionaltestwithoutfaultinjection.
Oncethetestispassing,proceedtofaultinjection.
2. ExecutefaultinjectionscenariofromSFIT.
If the test fails, display failure to the developer with a log of failure and
faultinjectiondetails.
a) Ifabug,resolve.
b) Ifnotbug,encodeapplication’sbehaviorunderfaultusingrecommendations.
c) Goto1.
3. Ifmorefaultinjectionscenariosremain,goto2onlyifthecurrenttestexecu-
tion passed based onthe developer specifications of application behavior
underfault.

EncapsulatedServiceReduction 73
6.5
Encapsulated Service Reduction
To identify corner-case bugs, SFIT must ideally explore combinations of service
failures. Toachievemaximumcoverageofthefailurespaceforasinglefunctional
test,whereserviceresponsesare deterministic, andtherearenodatadependencies
onpreviousfailures,thenumberoftestexecutionsthatarerequiredisquitelarge.
Astraightforwardapproachofinjectingfailuresineachcombinationofservice
requestsrequiresexecutingtestsinamagnitudethatisexponentialinthenumberof
service requests. However, it is possible to leverage the decomposition of an appli-
cationinto independentmicroservicestoreducethesearch spacewithoutlossof
completenessdramatically.
6.5.1 Service Encapsulation
Let us revisit the Audible example that is presented in Figure 3.1. Excluding the
completefailurespaceforreadability,letusconsiderjustthefailuresofasubsetof
theservices: AudibleDownloadService(ADS)anditsdependenciesandContent
DeliveryService(CDS)anditsdependencies.
WhenexploringfailuresoftheADS,SFITmustconsiderthefailureofitsthree
dependencies: the Ownership, the Activation, and the Stats services. The entire
request is failed if either the Ownership or Activation service calls fail. However,
if the call to the Stats service fails, that failure has no impact on the result of the
request. Aftertesting,itisknownthatanyfailureoftheOwnershiporActivation
service will cause the ADS to return a 500; however, a failure of the Stats service
willnot impacttheresponse oftheADS- regardlessof itsfailure, the service will
return 200aslongasbothOwnershipandActivationprovideasuccessfulresponse.
With the CDS, at a minimum, SFIT has to consider the failure of the Asset
Metadataserviceindependently,thefailureoftheAudioAssetsindependently,and
thenthecombinationsofthewayseachservicecanfailtogether. However,tofully
explorethefailurespaceusingourapproach,SFITmustconsiderthefailureofthe
StatsservicecombinedwithallpossiblefailuresoftheAssetMetadataserviceand
theAudioAssetservice. ThesearefailuresthatSFITalreadyknowstheimpactof
andshouldnothavetobetestedincombination. Forexample:
• SFIT already knows that a failure of the Stats service has no impact on the
ADSand
• SFITalreadyknowstheimpactofanycombinationoftheAssetMetadataand
AudioAssetservicesfailures.

74 Service-levelFaultInjectionTesting
Itiscritical,then,toidentifyawaytoleverageourknowledgeofservicefailures
andtheirimpactontheservicesthattakethemasdependencies. Todothis,SFIT
cantakeadvantageofthefollowingthreekeyobservations:
• First, SFIT must fully explore how a service’s dependencies can fail. This
ensuresthatSFITunderstandsthebehaviorofasingleservicewhenoneor
moreofitsdependenciesfailandwhattheresultingfailuresreturnedbythat
serviceare. ReferringtotheAudibleexampleinFigure3.1,itisclearthatSFIT
must fully explore the combination ofthe waysthatADS’s dependencies can
fail(aswellasthewaytheCDS’sdependenciescanfail,etc.)
• Second,whenSFITisabouttoinjectfaultsonatleastone dependencyoftwo
or more different services, SFIT already know the impact that those failures
willhaveontheserviceswhichtakesthemasdependencies. Referringtothe
AudibleexampleinFigure3.1,SFITalreadyknowswhattheADSwillreturn
whenitsdependenciesfailinanypossiblecombination,asSFIThasalready
run that test. SFIT also already knows what the CDS will return when its
dependenciesfailinanypossiblecombinationforthesamereason. Therefore,
SFITdoesnothavetoinjectthefaultatthedependencies. SFITcaninjectthe
appropriateresponsedirectlyattheADSorCDS.
• Third, SFIT has already injected that fault at that service, then the test is
redundant,asithasalreadyobservedthatapplicationbehavior.
Referring to the Audible example in Figure 3.1, SFIT do not need to test the
StatsservicefailingincombinationwithfailuresoftheAudioAssetsorAudio
Metadata services, as SFIT already knows the outcome of those failures on
theservicesthattakethemasdependencies;SFIThasalsoalreadyobserved
thoseoutcomes.
Algorithm3presentstheencapsulatedservicereductionalgorithm(ESR).This
algorithmreducestheexponentinthesizeofthetestexecutionspacefromthetotal
numberofservicerequeststothemaximumnumberofoutgoingrequestsfromanygiven
service. InFigure3.1,thisreducestheexponentfrom8(thetotalnumberofedges)
to 3 (the maximum branching factor.) Since microservice applications typically
scaleindepthratherthanbreadth,dynamicreductionmakesSFITtractable.
Thepropertyofmicroserviceapplicationsthatenablesthisstyleofdynamictest
casereductionisreferredtoasserviceencapsulationandisenabledbyDEI’sindexing
algorithm.
Definition 18 (Service Encapsulation). Service encapsulation states that invoked down-
streamdependenciesofaservicecanonlyindicatefailureorsuccesstotheirdirectcaller,and

Takeaways 75
aslongastheydonotexposetheirinternalstatetotheinvoker,theinvokercanonlyassert
ontheresponsesthatarereturnedtothecallerbythosedependencies.
Therefore,aninvokingServiceAandaServiceBexhibitingthispropertyissaid
tobe encapsulatedby thisservice: in short, ServiceAis saidto encapsulate Service
B;conversely,ServiceBisencapsulatedbyServiceA.Whenthisistrue,anyservice
invoking an RPC to Service A can only infer the behavior of Service B through
ServiceA’sbehavior.
Encapsulated service reduction is automatic and requires no additional infor-
mation from the application developer. It is important to note that encapsulated
servicereductionisnotsoundingeneralandreferstoourassumptionsaboveonthe
behaviorofasinglefunctionaltest: serviceresponsesaredeterministicforasingle
functional test, and servicecode does not contain data dependencieson previous
failures.
ItisimportanttonotethatEncapsulatedServiceReductionisnotsoundingeneral
and refers to our assumptions above on the behavior of a single functional test:
service responses are deterministic for a single functional test, and service code
doesnotcontaindatadependenciesonpreviousfailures.
6.5.2 Algorithm
Thisalgorithmisexecutedeachtimeanabstracttestexecutionisabouttobeexecuted
bytheSFITsearch. First,everyconcretetestexecutionthathasalreadybeenexecuted
issearchedtodetermineif there isamatchingconcreteexecutionwhere, foreach
fault,thefollowingcriteriaaremet: eitherafaultwasinjectedonanencapsulated
servicethatresultedintheencapsulatingservicereturningafailureresponsethatwe
intendtoinjectthroughfaultinjection,orafaultis(orshouldbe)directlyinjectedon
that request. If that criterion is true, ESR determines that the test case is redundant
anddoesnotexecuteit.
Thisresultsinthefollowingaugmented searchalgorithmforSFIT,presentedin
Algorithm4: SFITwithESR.
6.6 Takeaways
Service-levelFaultInjectionTesting (SFIT)isoneofthecorecontributionsofthisdis-
sertation: afaultinjectiontechniqueforidentifyingresilienceissuesinmicroservice
applications.
SFITachievesthisbyleveragingDEI,atechniqueforuniquelyidentifyingthe
RPCsexecutedbyamicroserviceapplication,tosystematicallyinjectalistoffaults

76 Service-levelFaultInjectionTesting
Algorithm3:SFITAlgorithm: EncapsulatedServiceReduction
Function ShouldSkip(a: AbstractTestExecution):
1
Startbysearchingeveryconcreteexecutionwehavealreadyrun...
2
3 for ConcreteTestExecution ∈ ExploredConcreteTestExecutions:
4
found=True
ForeveryRPCexecutedintheabstracttestexecutionprovided...
5
6 for𝑑 ∈ a.d:
Ifwewanttoinjectafaultinourexecution...
7
if 𝑓 =a.f(𝑑):
8
...butthefaultwewanttoinjectalreadyhappenedorganically...
9
10 if 𝑓 ∈ ConcreteTestExecution.r:
...then,wemightbeabletoskipthisexecution
11
12
found=found&&True
else:
13
...butiftheinjectedfaultdoesn’tmatchourresponse...
14
...wehavetorunit.
15
16
found=found&&False
Ifeveryfaultwewanttoinjectoccurredorganically(orsynthetically)
17
inanothertestexecutionwealreadyran,wecandefinitelyskipit.
18
19
if found:
return True
20
Otherwise,wehavetorunitbecauseit’sdifferent...
21
return False
22
on each of (and all combinations thereof) those RPCs. This forces application
developerstothinkaboutfailurescenariostheymayormaynothavebeenawareof
andensuretheirapplicationdoeswhattheyexpectwhenthosefailuresinevitably
occur,indevelopment andbeforeapplicationcodeisdeployedtoproduction.
Toaccountforthesefailures,applicationdevelopersarepromptedtousefaultin-
jectionpredicates: amechanismforencodingthefailurebehavioroftheirmicroservice
applicationintheexistinghappypathtestsoftheirapplication.
Whenpossible,SFITcanavoidexecutingredundant testcaseswherefaultsare
injected, and the outcome of those faults is already known because of service en-
capsulation. Service encapsulation is a core property of microservice applications
andthewaytheyaredeveloped: failuresofdownstreamservicesareoftenhidden

Takeaways 77
Algorithm4:SFITAlgorithm: SearchwithESR
ExecutedbySFITatstartofthesearch
1
Function SearchESR(t: Test,c: FaultConfiguration):
2
Executestheinitial,fault-freereferenceexecution
3
4
CurrentFaultConfiguration=c
5
CurrentConcreteTestExecution=ConcreteTestExecution()
6
CurrentAbstractTestExecution=AbstractTestExecution()
ExecTest(t)
7
8
ExploredAbstractTestExecutions.add(CurrentAbstractTestExecution)
9
ExploredConcreteTestExecutions.add(CurrentConcreteTestExecution)
Explorethefaultspacewhileincreasingitasnewfailuredimensionsexist
10
11
whilete=ToExploreAbstractTestExecutions.pop():
12 CurrentAbstractTestExecution=te
13
CurrentConcreteTestExecution=ConcreteTestExecution()
14
if !ShouldSkip(CurrentAbstractTestExecution):
ExecTest(t)
15
16
ExploredAbstractTestExecutions.add(CurrentAbstractTestExecution)
17
ExploredConcreteTestExecutions.add(CurrentConcreteTestExecution)
behind,orwithin,theresponsesoftheirancestorsinthemicroservicegraph. This
optimization can reduce the number of test cases needed for full coverage of the
faults exhibited in application code upon dependency failure of a downstream
service.
Inthenextchapter,anevaluationofSFITispresented,usingtheotherfounda-
tionalcontributionofthisthesis: theconstructedmicroserviceapplicationcorpus
takenfromindustryexamples.

Chapter 7
Evaluating SFIT: Corpus
“Ifyoucantalkbrilliantlyaboutaproblem,itcancreatetheconsolingillusion
thatithasbeenmastered.”
StanleyKubrick
Inthischapter,asyntheticevaluationofbothDistributedExecutionIndexing(DEI)
Service-levelFaultInjectionTesting (SFIT)ispresented.
First, the experimental configuration is presented. This section describes the
prototype implementation of SFIT, calledFilibuster. This initialimplementation is
writteninthePythonprogramminglanguagetomatchtheimplementationlanguage
ofthesyntheticmicroservicecorpusandishereinreferredtoasPython Filibuster.
ThisisdonetodistinguishitfromthesecondprototypeimplementedinJava,which
willbediscussedinasubsequentchapter.
Next, an evaluation of DEI is presented using the microservice corpus. This
evaluationshowsthatDEIencodestheminimalamountofinformationrequiredto
correctlyidentifyRPCsinamicroserviceapplicationbothuniquelyanddeterministi-
cally. Specifically,thisisdemonstratedbythesystematicremovalofeachcomponent
intheDEIhighlightingtheviolationsineithersoundnessorcompleteness(inSFIT)
thatresultfromtheirremoval.
Next,SFITisevaluatedonthecorpususingtheDEI’sevaluatedintheprevious
section. First, it is shown that SFIT can increase code coverage by automatically
generatingthenecessaryteststoexercisethecodepathsassociatedwithRPCfailure.
Thisshowsthatinadditiontotheincreasedcoverage,theSFITcanidentifyallof
the synthetic, industry-inspired bugs seeded into the corpus applications. Then
ESR is evaluated, and it is shown that ESR can significantly reduce the testing
overhead byremovingredundant test caseswhen microserviceapplication graphs
arestructuredaccordingly: depthoverbreadth. Fromthere,itisshownthatSFIT
79

80 EvaluatingSFIT:Corpus
can avoid expensive mock creation that would typically be manually created by
automatically generating those test cases. Finally, it is shown that theexecutionof
SFITisreasonableenoughtobeintegrateddirectlyintoeitherthelocaldevelopment
or continuousintegration environments toidentify application resilience issuesin
development,andbeforedeployment ofapplicationcodetoproduction.
7.1 Experimental Configuration
Allexperimentsinthissectionwereperformedusingtheprototypeimplementation
of Filibuster in Python. This implementation is called Python Filibuster and is
availableasopensource[Mei24g].
As all the services in the constructed corpus communicate using HTTP, the
popularHTTPrequestslibrarywasused. Toenablefaultinjection,theopentelemetry
instrumentation library for Python was extended to support fault injection and
enablemetadataassignmenttorequests. Toidentifythetargetofrequestsmadeto
servicesviaURL,theopentelemetryinstrumentationlibrarywasusedforFlaskto
recordtheservicewhereinstrumentedrequestswereterminated.
Thisinstrumentationassignsdistributedexecutionindexesandvectorclocks[Fid91;
Mat88] to each request to uniquely identify each request. This information is also
forwardedtoeachservicethroughtheinstrumentation. Distributedexecutionin-
dexescorrelatecallsbetweendifferenttestexecutionsfordynamicreduction;vector
clocksareusedtoidentifythedependenciesofaparticularservice.
This instrumentation communicates with the Filibuster server, as shown in
Figure 7.1. The Filibuster is responsible for starting all the services associated
with anapplication ineither localprocesses, DockerCompose, orKubernetes. The
Filibuster serverthenrunsthefunctionaltest,recordsandmaintainsthestackof
test executionsto execute, performsfunctional testassertions, reportstest failures,
andaggregatestestcoverage. TheFilibuster clientlibrary,writteninPythonwhich
communicateswiththeFilibuster serverprovidesanAPIthatfunctionaltestscan
usetowriteconditionalassertionsandallowsfortestreplayusingacounterexample
file. Testcoverageisaggregatedfromeachservicebytheserver.
Filibusterrequiresastaticanalysistodeterminethetypesoffailureseachservice
can return. In this prototype implementation, a purely lexical static analysis that
over-approximates these errors by performing abstract syntax tree traversals on
the source code of each service is used. This analysis is highly tailored to how
Flaskapplicationsarewrittenbyidentifyingraisestatementsthatthrowexceptions
convertedtoHTTPresponsescontainingstatuscodesindicatingerrorbyFlask. (e.g.,
ServiceUnavailable,NotFound.) Ifthistypeofanalysisisimpossible,developer’s

ExperimentalConfiguration 81
Figure7.1: ArchitectureofPythonFilibuster
canopttotestallpotentialfailures,asafinitenumberofHTTPstatuscodesindicate
theerror.
Thisimplementationof Filibuster caninjectthefollowingfaults(orfailures):
• Callsiteexceptions.
Callsiteexceptionthrownbytherequestslibrarythatindicatesconditionslike
connectionerrorortimeout. Forallexceptiontypes,Filibuster cancondition-
ally contact the other service before throwing the exception. For timeouts,
Filibustercanconditionallywaitthetimeoutperiodbeforethrowingatimeout
exception.
• Errorresponses.
ErrorresponsesreturnedfromaremoteserviceusingstandardHTTPerror
codesthatindicateconditionslikeInternalServerErrororServiceUnavailable.
Foreacherrorcode,Filibuster canreturnanassociatedbodyconditionally.
Eachisconfigurablewhenrunning Filibuster. This enablesdevelopers torun
a subset of these errors during local development, a more significant subset on
pushto afeaturebranch,andthecompletesubsetasa nightlyjob. Theprototype
implementationof Filibuster wasconfiguredtoruninAWSCodeBuildfollowing
thisdesign,allowingforrapidfeedbacktodevelopersandcompletecoveragenightly.

82 EvaluatingSFIT:Corpus
AsFilibuster hasbeenwrittenusingaclient-serverarchitecture,cross-language
supportispossibleandcurrentlyexistsfortheJUnittestinglibraryinJavaforHTTP
andGoogle’sgRPC:thisimplementationisdiscussedinasubsequentchapter. All
communication between instrumentation and the Filibuster server is through a
language-independentprotocol;anythinglanguage-specificisdoneintheinstru-
mentationlibrary.
7.2
Distributed Execution Indexing
Inthissection,PythonFilibusterisusedasanevaluationofDEItodemonstratethat
the innovations in DEI are required for a microservice application fault injection
approach to be both sound and complete. In short, without the inclusion of the
invocationcount,callstack,andinvocationpath,afaultinjectionanalysissuchas
SFIT can violate either soundness (where faults are injected on the incorrect RPCs),
completeness(wherefaultsarenotinjectedonRPCstheyshouldbe),orboth.
Next, an example application in Java is written to demonstrate that nondeter-
minismisaproblemthatanymechanismthatidentifiesRPCsforthetargetoffault
injectionmustdealwith. ThisapplicationistestedusingFilibusterbyextendingthe
Filibuster prototype with support for Google’s gRPC in Java. Then, it is shown that
throughtheinclusionoftheinvocationpayload,DEIcandealwithnondetermin-
ismwhileavoidingtheexpensiveinstrumentationrequiredforcontroloftheJava
scheduler; however, only when applications do not issue concurrent RPCs to the
sameRPCservice,method,fromthesamecallsite,withthesameRPCarguments.
While these innovations are evaluated in the context of the prototype imple-
mentationofSFIT,Filibuster,anyrequest-levelfaultinjectiontechnique(e.g.,LDFI,
3MileBeach,etc.) aresusceptibletotheseissues. Therefore,DEIisageneralsolution
foranyrequest-levelfaultinjectiontechniqueforaddressingtheidentificationof
RPCsforfaultinjectioninamicroserviceapplication.
7.2.1 Required: Invocation Count, Stack, and Path
Theconstructedcorpusisusedtodemonstratetheneedforinvocationcount,call
stacks, and RPCpath. Asnone of the industrialexamples in thiscorpus contained
thecodingpatternsdiscussedinChapter5,thecinemaexamplesfromthecorpus
areusedforthisevaluationinstead.
Withregardtothecinemaexamples,onecinemaexampleinparticular,cinema-3,
exhibitsapatternthatrequirestheinclusionofthecallstackorinvocationcount. To
demonstratetheneedforboth,combiningthestructureofcinema-6withretrieson

DistributedExecutionIndexing 83
Cinema All NoIC NoStack NoIC NoPath,
Example &Stack IC&Stack
cinema-3 7 4 7 - -
cinema-9 5 5 5 3 -
cinema-10 6 6 6 6 5
Table7.1: Resultsdemonstratingalltechniquesmustbecombinedforcorrectidentification.
failurefrom cinema-1is necessary. Itis alsonecessaryto extractthe RPCinvocation
intoahelperfunction.
Todemonstratetheneedforinclusionoftheexecutionpath,itwasrequiredto
combinethestructureofcinema-2withtheuseofdefaultresponsesonfailurefrom
cinema-5. Thesenewexamplesareincludedinthecorpusandreferredtoascinema-9
and cinema-10, respectively. These are not unrealistic, as the changes were taken
fromotherexamplesinthecorpusandcombinedwithexistingexamples.
Todemonstrate,recallthatcinemaiscomprisedoffourservices,asdepictedin
Figure4.1. The usersserviceretrieves thebookingsforauser: thisinvolvesan RPC
totheBookingsserviceandthentoMoviesserviceforeachretrievedbooking. In
thetwovariations,either:
1. the Usersservice issues anRPC tothe moviesservice after theresponse from
theBookingsservice,or
2. theBookingsserviceissuesanRPCtotheMoviesservicedirectly.
For testing, a functional test that retrieves a user’s movie bookings is used. In
terms offault injection specifically, a singleconnection error exceptionis injected
foreachRPC.
Theevaluation resultsarepresented inTable7.1. For clarity,redundant results
areomitted: forexample,ifatestexecutionproduceseitherunsoundorincomplete
behaviorwithoutincludinganinvocationcount. Noresultsarepresentedwhere
invocationcountandstackareexcluded.
Forthisexperiment,cinema-3isused.
InvocationCount.
Incinema-3,theRPCfromtheUsersservicetotheBookingsserviceisperformed
inaloopandre-executedonceonfailure.
Exhaustivesearchrequiressevenexecutions. Withouttheinvocationcount,only
fourexecutionsareperformed.

84 EvaluatingSFIT:Corpus
✓SFITisincorrectwithout
invocationcounting:
• Unsound.
EachRPCintheloopwillbeassignedthesameidentifier,SFITwillinject
afaultonzerooralliterations.
• Incomplete.
Requests that occur due to any iteration, not the 1st, will not have faults
injected.
Forthisexperiment,cinema-9isused.
CallStack.
In the event of failure of the 1st RPC from the Users service to the Bookings
service,itwillmarktherequestasfailedandtrythatrequestlaterfromadifferent
callsite. Thisdiffersfromtheloopwherethesamecallsiteisused. Eachcallsite
usesahelperfunctiontoissuetheRPCtoensurethestacksdiffer.
Exhaustive search requires five executions. Without call stack, only three execu-
tionsareran.
✓SFITisincorrectwithout
callstackinclusion:
• Unsound.
As each call invocation of the helper’s RPC will be assigned the same
identifier,SFITwilleitherinjectafaultonbothorneither.
• Incomplete.
Requests that occur as a result of the 1st invocation will not have faults
injected.
Forthisexperiment,cinema-10 isused.
RPCPath.
In the event of a failure of the Bookings service, a default response is used in
placeofthefailureandtheMoviesserviceiscontacteddirectlybytheUsersservice.
Exhaustive search requires 6 test executions. Without the RPC path, only 5
executionsareperformed.

DistributedExecutionIndexing 85
✓SFITisincorrectwithout
RPCpathinclusion:
• Unsound.
SincethebookingsRPCtomoviesandtheusersRPCtomoviessharethe
sameidentifier,SFITwilleitherinjectafaultonbothorneither.
• Incomplete.
AsSFITwillalwaysfailthe2nd RPCtomovies,thesuccessfulcaseisnot
explored.
7.2.2 Nondeterminism is a Problem
In orderto understandthe impact ofscheduling nondeterminismwithin the JVM
oncorrectidentifierassignment,asmallexamplewasconstructedwiththeArmeria
libraryforJavathatcontainedtwoservices: HelloandWorld.
In this example, the World service exposed a single endpoint that returned a
Stringconstant whenitreceivedanRPC. TheHelloservice exposedanendpoint
that,whenitreceivedanRPCfromthetestharness,wouldlaunchaconfigurable
number of threads, each that issued an RPC to the World service, and then wait
forthemtocomplete. EachthreadwasdefinedasaclassinJava,wheretheHello
servicewouldcreateinstancesofthisclassofinaloop. Thisensuredthatthecallsite
oftheRPCwasthesameandthestacktraceofthecallsitewereidentical. AllRPCs
weremadethesameserviceanddifferedonlyinthepayload,whichcontainedthe
identifierofthethreaddeterminedbythreadcreationorder.
For this experiment, Python Filibuster was extended with support for Java,
Google’s gRPC library. Then, a server stub at the World service was installed to
recordtheexecutionindexesgeneratedbytheHelloservice. Then,theDEIalgorithm
wasreconfiguredtoincludethethreadcreationorder;therefore,thepayloaddiffered
onlybythisidentifier.
ThistestapplicationwasexecutedforvaryingnumbersofRPCs(2,4,8,16,32,
64)for100iterationseach. ThethreadpoolsizewasalsofixedattheHelloservice
at size 2. For each iteration, it was recorded whether or not the execution index
assignmentmatchedthethreadcreationorderbyexaminingtheexecutionindex
payloadvalues. TheresultsarepresentedinFigure7.2.
With only 2 RPCs, 44% of the tests exhibited an RPC execution order that did
notmatchthecreationorder;by64,100%oftheRPCsdidnotmatchthecreation
order. With16RPCs,thisroseto80%;by32RPCs,thiswasat96%,andby64,98%
oftheRPCsdidnotmatchthecreationorder.

86 EvaluatingSFIT:Corpus
Figure7.2: Percentageofexecutionswithdeterministicassignmentfortwothreads.
✓ Even in the presence of relatively low amounts of concurrency, scheduling
nondeterminismisaproblemforSFIT.
7.2.3 Payload Inclusion Distinguishes
Using the same example, the key insight of asynchronous DEI could be verified:
includingthe payload intotheidentifier foreachRPC invocation wassufficientfor
distinguishing these concurrent, inter-service RPCs. With asynchronous DEI, all
RPCidentifierswereuniqueanddeterministic,asshowninFigure7.2. Therefore,
schedulingnondeterminismwasnotanissue.
✓ Payload is sufficient for distinguishing concurrent, inter-service RPCs
in microservice applications, assuming that these RPCs will not share the
same payload when issued to the same service and method with the same
parameters.

Service-levelFaultInjectionTesting 87
7.3
Service-level Fault Injection Testing
Table7.2presentsresultsfromrunningPython Filibuster onthecorpus. Forthis
evaluation,itisassumedthatallRPCscanthrowaconnectionerrorexception. When
a timeoutis specified,timeout exceptionsare alsoconsidered. Anyservice-specific
failuresarealsoincluded,asdeterminedbythePython Filibuster staticanalysis.
AllexampleswererunonanAWSCodeBuildinstancewith15GBofmemory
and eight vCPUs. At the start of the Python Filibuster run, all of the services
werestartedforeachexample;Python Filibuster waitedforthoseservicestocome
online,e,and theservicesweremanuallyterminatedattheendoftherun. Asmost
of the applications in the corpus have no side effects, they seed the system with
values and verify they can be read so the services are not restarted between test
executions. However, this option is available. Given that the cost of the service
restart is fixed, that cost is excluded when comparing the system’s performance
withandwithoutencapsulatedservicereduction.
7.3.1 Tests Generated and Increased Coverage
Todeterminethebenefittodevelopersinidentifyingresilienceissues,itmakessense
toconsider thenumber oftestsgeneratedbyPython Filibuster andtheresulting
increaseincodecoverage.
The “Test Gen/ESR Gen” column presents the number of tests generated and
executedbyPython Filibuster. Sinceeachexampleonlyhasasinglefunctionaltest,
thesenumbersincludethattestinthetotal. ThisisbecausePython Filibuster must
executetheinitialpassingfunctionaltestfirsttoidentifywheretobegininjecting
faults. Inallofthecorpusexamplesthatcontainedbugs,thebugscouldbeidentified
usingPython Filibuster.
The “Coverage After” column shows the increase in statement coverage. By
generating the tests that exercise possible failures, Python Filibuster can increase
thecoverageof the application. These numbersonly accountfor coverage gained
using the functional tests. The generated tests increase coverage related to error-
handlingcodewhichisnotexercisedbytheunmodifiedfunctionaltest,whichdoes
notconsiderfailure.
✓SFITwasabletopreventdevelopersfromhavingtowritetime-consuming
mocksby automaticallygenerating teststhatintroducefailures atallof the
remotecallsites.
AsdemonstratedbytheNetflixexample,someoftheseapplicationsarelarge
enough torequire manytests toensure coverage of the failure spaceproperly. For

88 EvaluatingSFIT:Corpus
| Example   | Test/   | Coverage | Time     | ESR      | TG       |
| --------- | ------- | -------- | -------- | -------- | -------- |
|           | ESRGen  | After    | w/ESR    | Overhead | Overhead |
|           |         | (%)      | (s)      | (ms)     | (ms)     |
| cinema-1  | 9/9     | 90.72    | 8.83     | 0.46     | 0.60     |
|           | (-0)    | (+5.67)  | (+1.16)  | (0.02)   | (0.06)   |
| cinema-2  | 10/9    | 90.76    | 8.81     | 0.43     | 0.64     |
|           | (-1)    | (+5.64)  | (+1.15)  | (0.01)   | (0.06)   |
| cinema-3  | 91/37   | 91.08    | 13.21    | 34.10    | 4.09     |
|           | (-54)   | (+6.43)  | (+5.54)  | (0.02)   | (0.04)   |
| cinema-4  | 34/21   | 91.34    | 12.11    | 3.25     | 2.31     |
|           | (-13)   | (+8.17)  | (+4.23)  | (0.01)   | (0.06)   |
| cinema-5  | 25/25   | 90.72    | 11.17    | 2.23     | 1.57     |
|           | (-0)    | (+5.16)  | (+3.51)  | (0.01)   | (0.06)   |
| cinema-6  | 41/41   | 91.35    | 13.99    | 5.91     | 2.57     |
|           | (-0)    | (+9.05)  | (+6.28)  | (0.01)   | (0.06)   |
| cinema-7  | 45/45   | 91.28    | 14.41    | 6.37     | 2.71     |
|           | (0)     | (+6.64)  | (+6.71)  | (0.01)   | (0.06)   |
| cinema-8  | 21/21   | 92.70    | 10.47    | 1.66     | 1.37     |
|           | (-0)    | (+8.33)  | (+2.88)  | (0.01)   | (0.06)   |
| Audible   | 69/31   | 96.04    | 15.28    | 13.35    | 4.72     |
|           | (-38)   | (+12.75) | (+6.35)  | (0.01)   | (0.06)   |
| Expedia   | 17/17   | 98.54    | 9.87     | 1.15     | 1.06     |
|           | (-0)    | (+15.33) | (+6.35)  | (0.01)   | (0.06)   |
| Mailchimp | 135/134 | 98.96    | 59.83    | 473.48   | 44.07    |
|           | (-1)    | (+11.54) | (+52.01) | (0.02)   | (0.32)   |
Netflix
| –nobugs    | 1606/1603  | 96.31    | 513.83    | 94566  | 6748.93  |
| ---------- | ---------- | -------- | --------- | ------ | -------- |
|            | (-3)       | (+17.25) | (+504.85) | (0.09) | (4.20)   |
| –w/bugs    | 18653/4670 | 97.38    | 2303.84   | 748750 | 62100.34 |
| (#2,#3)    | (-13983)   | (+15.67) | (+2293.8) | (0.07) | (3.32)   |
| –w/bugs    | 18653/4670 | 97.38    | 2363.84   | 744052 | 60002.91 |
| (#1,#2,#3) | (-13983)   | (+15.67) | (+2353.8) | (0.07) | (3.31)   |
Table7.2: PythonFilibusterevaluatedonthecorpus. Includesthenumberofgenerated
tests with and without encapsulated service reduction; coverage before and after using
PythonFilibuster,overheadofencapsulatedservicereductionalgorithm,andoverheadof
testgeneration.

Service-levelFaultInjectionTesting 89
mostorganizations,manuallywritingthismanytestswithoutasystemtogenerate
thesetestsautomaticallywouldbeexpensiveintermsofdevelopmenttime. Similarly,
the cost of test adaptation is also low. In the Netflix example, Python Filibuster
executed1,606testsbutrequiredonlyninefaultinjectionpredicatestocaptureall
behavior. SFITalsofoundallofthebugsinadevelopmentsetting withoutrunning
chaosexperimentsinaliveproductionenvironment.
Asdiscussedinoursectiononcorpuscreation,allofthesebugswerediscovered
using chaos engineering. In fact, these use cases were used to advocate for the
adoptionofchaosengineering. UsingPython Filibuster,chaosengineeringcanbe
avoided.
7.3.2 Encapsulated Service Reduction
The “Test Gen/ESR Gen” column shows the benefits of encapsulated service re-
duction: yellow cells are used to identify impact; green cells are used to identify
significantimpact. Encapsulatedservicereductionexcelswhengraphshave more
depthandlessbreadth.
IntheAudibleexample,whichhasaservicedecompositionthatresemblesthe
manner in which the same application might be built a in monolithic style, there
aredeeppathscontainingnestedrequeststhatcanallowPython Filibuster toavoid
running redundant testexecutions. Effectively, ESR takes advantage of the natural
compositionalityintheapplication.
However,intheNetflixexample(withoutbugs),whereawidefanoutisused
andeachdatadependencyisrelativelyindependent,thegraphhasanenormous
breadthwithnodepth. Inthiscase,allcombinationsoffailuresmustbetested,as
thecontrolflowintheapplicationcouldbebasedonarequestfailure.
Furthermore,intheNetflixexample(withbugs),wheredeeperpathsareintro-
duced through additional fallback behavior, the benefits of encapsulated service
reductionbecomevaluable–only25%ofthetestshavetobeexecutedtoreachthe
samefailurecoverage.
✓ When applications are structured with depth over breadth to the service
graph,theycansignificantlybenefitfromencapsulatedservicereduction.
Thisoccursbecauseourdesigncanobservethebehaviorofserviceswhentheir
dependenciesfailearlierintheexplorationofthefailurespace—thisinformation
canbeusedtoavoidrunningsubsequenttestswherethatbehaviorisalreadyknown.
Thisinsightcanguidethedesignofmicroservicearchitecturestodecreasethecostof

90 EvaluatingSFIT:Corpus
testing—deeper servicegraphsallowforthereuseofresults acrosstestexecutions.
Thisreducestheoveralltesttimerequiredtoexhaustthespaceofpossiblefailures.
7.3.3 Mocks
Duringtheinitialcorpusimplementation,unittestswerewrittenforeachservicein
eachexampleusingmockstoaccountforpossibleremoteservicefailures. When
writing thesetests, only independent failures were considered. Referto Figure 3.1
andconsidertheAudibleDownloadService. Inthisexample,unittestswereonly
written,eachcontainingamockforthefailuresofthethreedependencies: Owner-
ship, Activation, andStats. Thelist ofservice-specific failuresis omittedhere, and
thereaderreferredtothediagramforthelist;forexceptions,amockwaswritten
foreachofthetwoexceptions: TimeoutandConnectionError.
Notonlywasthisprocesstime-consuming,fromlearningthemockingframe-
work to writing and verifying they worked correctly, but it was also a significant
amountofadditionalcode. Thesefailuresalsounder-approximatetheactualfailures
thatcouldoccurintheapplication: mocksthatverifiedallpossiblecombinations
of failures were not written. For example, the failure of the Stats service and the
AssetMetadataservicewouldrequireacombinationoftwomocksontwodifferent
services. Asanexampleofhowmuchcodeisrequiredtowritethesemocks,theim-
plementationofallNetflixserviceswas936LOC.Anadditional743LOC(+79.3%)
oftestcodewaswrittentoverifyfailurebehavior.
✓ SFIT can be used to verifyresilience without the time-consuming, ad-hoc,
and error-prone effort of writing mocks for what failures the developers
believearepossible.
PythonFilibustercanautomaticallygeneratethesetestswithminimaleffortand
accounts for more complicated mocking scenarios, where multiple mocks across
differentservicesarerequiredtoexecuteaparticularerror-handlingcodepath.
7.3.4 Execution Time
The“Timew/ESR”columnshowsthe execution timewithencapsulatedservicere-
ductionenabled. Thiscolumnshowsthetotalexecutiontimeforalltests,excluding
setupandtear-downtime. Thedifferencebetweenrunningtheinitialsinglefunc-
tional testand running all ofthe tests generatedby Python Filibuster is presented
inparentheses.

Service-levelFaultInjectionTesting 91
Comparingthisdifferencetothenumberoftestsgeneratedandexecutedwith
encapsulatedservicereduction,itisclear. Itisexpectedthattheexecutiontimescales
linearlywiththenumberofteststhatmustbeperformed. Thisper-testexecution
time accounts for starting a Python interpreter, performing whatever setup and
tear-downisrequired,andexecutingthetest.
In the “TG Overhead” column, the total overhead (in milliseconds) for test
generation is presented. This test generation process, running inside the Python
Filibuster server,schedulesnewtestexecutionseachtimeanewrequestisreached,
andthePython Filibuster serverlearnsaboutthiscallthroughtheinstrumentation
call from the service. As is apparent, this overhead is minimal. The overhead
foreachgeneratedtestispresentedinparentheses,whichintheworstcaseis3.2
milliseconds.
Inthe“ESROverhead”column,thetotaloverhead(inmilliseconds)introduced
bytheencapsulatedservicereductionalgorithmispresented. Thisalgorithmhas
to,foreachtestthatisgenerated,determineifthistestisredundantwithaprevious
testexecution. Asisapparent,thisoverheadisminimal. Theoverheadpertestis
presentedinparentheses: inthemostcomplicatedexamples,itis90microseconds.
✓SFIT’sexecutiontimescaleslinearlywiththenumberofgeneratedtests.
However,thetestgenerationoverheadissignificantlylessthanthecostofthe
developmenttimerequiredinmanuallywritingthesetestsusingmocks. Addition-
ally,Python Filibuster provideshighercoveragebyautomaticallywritingmocks
forcombinationsoffailuresacrossserviceboundaries.
7.3.5 Misconfigured Timeouts
To identify misconfigured timeouts, where Service A calls to Service B with a
timeoutthatislessthanServiceB’stimeouttoaServiceC,isperformedbysleeping
the timeout interval plus one additional millisecond before returning a Timeout
exception. ThisensuresthatPythonFilibusterwaitsatleastlongenoughtoaccount
forthetimeoutinterval.
In Figure 7.2, the difference in execution time when testing timeouts is high-
lighted in red. To identify Netflix bug #1, Python Filibuster must execute the
timeouts while sleeping the timeout interval. Compared to the execution where
timeoutsarenotconsidered,thedifferenceintimeofthecumulativetimeoutinterval
duringtestingcanbeobserved.

92 EvaluatingSFIT:Corpus
✓ SFIT can detect incorrectly configured timeouts at the cost of additional
executiontime,equivalenttotheinjectedtimeoutduration.
7.4 Takeaways
In this chapter, an evaluation ofService-level FaultInjection Testing (SFIT) was pre-
sentedusingtheinitialprototypeimplementationofSFITinPython,Filibuster.
UsingthesyntheticmicroserviceapplicationcorpusconstructedinChapter4,
it was first demonstrated that Distributed Execution Indexing (DEI) is a necessary
foundationaltechniquefortheidentificationofRPCsexecuted,forfaultinjection,
inamicroserviceapplication.
DEI’s provide both a sound and complete method for enabling request-level
(e.g., RPCs) fault injection techniques while ensuring that repeated execution of
the same application path yields the same identifiers enabling both exhaustive
searchanddeterministicreplay. DEIalsoaddressRPCexecutionnondeterminism
inmicroserviceapplications,undercertaindesignrestrictions,whileavoidingthe
necessity of scheduler control in managed VMs: common in distributed system
testing but impractical in microservice applications composed of many different
servicesthatareimplementedinotherimplementationlanguages.
SFITwasthenevaluatedagainstthesyntheticmicroserviceapplicationcorpus.
ItwasshownthatSFITcanidentifyallapplicationbugsseededintothesynthetic
microservice corpus at lower cost, and in development compared to existing fault
injection techniques typically performed in production. By leveraging an emer-
gentpropertyofmicroserviceapplicationsandthewaytheyaredeveloped,service
encapsulation, DEI’s can be used in SFIT to further reduce the overhead in testing
microservice applications for resilience by avoiding redundant test cases when
testingtheapplicationwholesale,end-to-end. Thistestcasereductiontechniqueis
referredtoasEncapsulatedServiceReduction.
In short, SFIT provides an efficient mechanism for detecting resilience bugs,
in the development environment and before deploying application code, when the
applicationcanbetestedend-to-endinthedevelopmentenvironment.

Chapter 8
Industrial Microservices: Foodly
“Ilearnedalongtimeagothatrealitywasmuchweirderthananyone’s
imagination.”
HunterS.Thompson
As discussed in the background and related work, designing a fault injection
technique for microservice applications is only half of the problem: many fault
injectiontechniques have beencreatedinacademia buthavefailedtofind adoption
withindustrypractitionersastheirdesignedwasmismatchedwithhowapplication
developersdesign,develop,deploy,andmaintaintheirmicroserviceapplications.
Toaddressthisdeficiency,itwasfirstnecessarytoidentifyanindustrypartner
interestedinusingfaultinjectiontestingtoimprovetheresilienceoftheirmicroser-
viceapplication. Then,itwasnecessarytodetermineifthedesignedapproachwas
compatible withhow they developand test their services. Finally, it was necessary
todetermineiftheapproachcouldidentifyapplicationbugsrelatedtoresiliencein
theirapplication. Therefore, andtowardsthat end,a partnershipwasestablished
withFoodly. FoodlyoperatesoneofthelargestfooddeliveryserviceintheUnited
Statesusingamicroserviceapplicationcomprisedofover500differentservices.
This chapter presents background material on Foodly: how they build their
microserviceapplication,howtheyremainresilienttofaults,andwhy, fromtheir
perspective,existingindustrialfaultinjectiontechniquesarenotsufficientorappro-
priatefortheirconsumerproduct.
93

94 IndustrialMicroservices: Foodly
8.1 Foodly
Foodly is a food ordering and delivery consumer product built using a microser-
vice architecture comprised of over 500 services, primarily written in the Kotlin
programming language. Foodly’s decision to migrate from a monolithic to a mi-
croservicearchitecturetoimprovedeveloperproductivityatscale. Eachservicein
Foodly’s microservice application platform provides a specific set of functionality
that is grouped by business logic (e.g., ordering, delivery), and an independent
teammanagesthesoftwarelifecycleforthoseservices. ServicesatFoodlyprimarily
communicateusingGoogle’sgRPC,withsomelegacycommunicationoccurring
overHTTP.Servicesaredeployed whennewcodeis readyforrelease,witharound
100uniquedeploymenteventsoccurringdaily.
Eachservice’sfunctionalityiscontrolledatruntimeusinganexperimentation
framework that allows features to be deployed and then gradually enabled for
customers. This is done to minimize the impact of application bugs and allow
for experiments that adversely impact the business to be disabled, all without
redeploying. These experiments are tested independently but run concurrently
in production. There can be hundreds of active experiments running across the
deployed applicationsimultaneously. The combinationoffrequent deployments
andactiveexperimentsmeansthatthesystemisconstantlyinfluxand,asaresult,
nospecificationoftheend-to-endsystembehaviorexists.
8.2 How Foodly is Resilient To Faults
Foodly’smicroserviceapplicationmustremainresilienttofaults. Forexample,in
thecaseofbaddeployments,whereapplicationcodethatcontainbugsorisprone
to crashing and spurious failures due to underlying infrastructure issues such as
containerfailuresandnetworkanomalies. AtFoodly,andmanyothercompanies
thatoperatemicroservice applications, this reliability isensured throughseveral
differenttechniques,workinginconcertandwiththeprimarygoalofminimizing
theimpactoffailuresinproduction.
Several techniques are employed to mitigate the impact of bad deployments:
container orchestration, canary deployments, load balancing, probes, and auto-
scaling rules. Container orchestration is used to support rolling deployments of
serviceswhere possible. Canary deployments andbulkheads detectbad releases
as early in the deployment process as possible while minimizing the impact of
thesebaddeployments. Servicesaredeployedintoreplicasets,andloadbalancing
distributestheloadacrossallserviceinstanceswithinareplicaset. Serviceswithin
areplicasetareautomaticallycheckedusingstartup,liveness,andreadinessprobes

WhyNotChaosEngineering? 95
to detectmalfunctioning servicesfor automaticremoval fromthe replica set. Auto-
scaling rules and restart policies ensure that a minimum set of nodes in a replica
setis operationalat agiventime. These techniquesensure thatservices areonline
andrespondingasmuchaspossiblebyminimizingtheimpactofbaddeployments
throughdetectionandautomaticrollback.
Retries,loadshedding,andcircuitbreakingareemployedforspuriousfailures.
Foodly’scustomRPCclientautomaticallyretriesRPCsintheeventoffailure,except
timeoutfailures,whichmayindicateafailureorslowdownofatransitivedepen-
dency. Load shedding is employed by each service to ensure that services refuse
(i.e.,short-circuitwithanerrorresponse)incomingRPCswhentheserviceiseither
alreadyoverloadedoratriskofbecomingoverloadedshouldtheyprocesstheincom-
ingRPC.Circuitbreakersareusedateachservicetopreventrepeatedinvocation
ofadownstreamdependencythatmaybemalfunctioningorotherwisefailingby
dynamicallyre-configuringtheapplicationtoshort-circuittheRPCwithanerror
untiltheremoteservicebeginsfunctioningcorrectlyagain. Thesetechniquesensure
that spurious failures are mitigated through retries until the application can be
reconfigured to avoid invocation to these failing or failed dependencies until the
failuresareresolved.
Whilethesetechniquesforminimizingtheimpactofspuriousfailuresprovide
reliabilityatscale,theyareprimarilyreactiveapproaches,specifically,responding
tofailures asquicklyas possibletoeither isolatethefailure’s effectordegrade the
applicationgracefully. However,theydonotaccountforfailuresobservedbythe
applicationuntiltheapplicationisreconfiguredorfailurespropagatedunderthat
configuration. Therefore,developersarelefttoanswerthefollowingquestions:
• Whatdoesa service return toitscallerswhen oneofitsdownstreamdepen-
denciesreturnsanerrorduetoactiveloadshedding?
• Whatdoesa service return toitscallerswhen oneofitsdownstreamdepen-
denciesisreturninganerrorbecausethecircuitbreakerisopen?
• Whatdoesa service return toitscallerswhen oneofitsdownstreamdepen-
denciesis slowor returningan errorbeforeload sheddingor circuitbreaking
hasbeenactivated?
8.3 Why Not Chaos Engineering?
Frequently, to answer questions of resilience, the operators of large, industrial
microserviceapplicationsturntochaosengineering. Chaosengineeringisacoarse-
grainedfaultinjectiontechniquetypicallyperformedinanenvironmentwherethe

96 IndustrialMicroservices: Foodly
entireend-to-endapplicationcanbetested—forexample,stagingorproduction
— pioneered by Netflix when moving to the cloud. While chaos engineering is
excellent at identifying infrastructure issues that can adversely affect microservice
applications,itissomewhatlackinginitsabilitytoidentifyapplicationbugsrelated
toresilience. Thisisduetotherisks,cost, andgranularityinvolvedinthisstyleof
large-scaleexperimentation.
First,concerningtherisks,whenanexperimentisnotwelldesignedorisscoped
too broadly, it might adversely affect the customer experience, for example, by
preventingaconsumerfrommakingapurchase. ForFoodly,thisisnotanoption.
Second,thecostofrunningandmonitoring chaosexperimentscanbe prohibitive.
Therefore, the numberofexperimentsthatcan berunandthefrequency ofthose
experimentsare prettylimited. Itis impossibleto runasetof experimentsofthis
style per-commit or even daily. Even after fully automating chaos experiments
and removing any manual overhead in monitoring and rollback, Netflix concluded
thattheycouldnotrunexperimentsfastenoughtocoveralltheexperimentsthey
wanted. Third,iftheanalysisoftheseexperimentsisperformedtoocoarsely—for
example,byexaminingthevolumeofpurchasesrelativetoacontrolgroup—minor
variations,suchasasingle smallgroupofcustomersbeingunable to purchasedue
toalatent applicationbugthatisactivatedbyfaultinjection, maygo unnoticed. As
activeexperimentationofthisstyleisprohibitiveforFoodlyfortheseveryreasons,
Foodly choseSFIT to identifyapplication bugs relatedto resilience,in development,
beforedeployment ofapplicationcodetoproduction.
8.4 How Changes at Foodly are Tested
To set the context of an evaluation of SFIT at Foodly, the testing and deployment
practicesofFoodlyaredescribed. Specifically,onemightaskhowisanapplication,
likeFoodly,comprisedofover500serviceswith100uniquedeploymenteventsper
daytestedbeforeachangeisdeployed?
First,anapplicationofthissizecannotberunonasingledeveloper’smachinefor
localtesting. Thisisduetothesheernumberofservicesanddatabasedependencies
requiredtosetupanend-to-endfunctioning versionoftheapplication. Evenusing
auniquecloud environmentfortestingiscost-prohibitiveinterms ofbothrequired
effortandtime: inherenttothedecentralizednatureofservicedevelopmentinami-
croservicearchitecture,eachservicemayendupwithslightlydifferentprocessesfor
deploymentandconfiguration. Combinedwithchurnfromfrequentdeployments,
keepingaseparatestagingenvironmentfunctioningandreflectiveoftheproduction
environmenttofacilitaterealistictestingiscomplexand,atFoodlyspecifically,is
not done. As a result, Foodly primarily tests changes to services in two ways: in

Takeaways 97
productionwithsandboxesorlocallyinisolation.
For production testing with sandboxes, the service code under test is first de-
ployedtoa“sandbox”instancerunninginproduction,whereadevelopercanattach
aremotedebuggertothesandbox’sJVMinstance. Atthispoint,thedevelopercan
thenissueend-to-endrequestsfromFoodly’smobileorwebapplicationwithatest
accounttotesttheservice’sfeaturesinteractively. WhenissuingRPCstotheservice
under test, these requests will traverse production dependencies and have those
RPCsroutedtothesandboxinstance. Fromthere,anyRPCsissuedtodownstream
dependencies by the service in the sandbox are then routed back to production
instances. Topreventdatacorruptionwhenwritingtodatastores,multi-tenancy
routeswritesforonly thoserequeststoseparatedatastoresornamespaces.
Withlocal,isolatedtestingofservices,automatedteststhatexercisetheservice’s
APIareused. Thesetestsusestubsfordownstreamservicedependencies,wherethe
hard-codedresponsesrequiredforeachtestareencodedineachstub. Itisimportant
to note thatthese stubs are in-processgRPC services that returnthese hard-coded
responses,notstubsthatshort-circuitthemethodinvocationwiththehard-coded
response. Therefore,thetestcodeexercisestheRPCframeworkcodethatwillbe
executedinproduction. Fordownstreamdatastoredependencies,Dockercontainers
areusedwheretheyareseededwiththerequireddataforeachtest: again,these
arethesamedatabasesthat areusedinproduction,justrunninglocally. Theonly
differencefromproductioncodepathsisthatdependencyinjectionchangestheIP
addresses/portnumbersusedtoconnecttodependencies,maximizingthecoverage
ofproductioncodepaths. Foodlyreferstothisstyleoftestingascomponenttesting,
which resembles functional testing of individual services as a single functional
component;theuseofadifferentnamewasneededtodistinguishthesetestsfromthe
functionalteststhatexerciseend-to-endapplicationbehavior,tominimizeconfusion
whendiscussingdifferenttestingapproaches.
8.5 Takeaways
Conceptually,FoodlyisaprimecandidateforevaluatingSFITforseveralreasons:
• MinimizedBlastRadius.
First, Foodly wants to ideally avoid any fault injection testing performed in
production, as anyinjected fault in the production environment may adversely
affectthecustomerexperiencewhenorderingfood. Uniquely,SFITisdesigned
to identify application resilience bugs by testing in development before the
applicationcodeisdeployedintoproduction.

98 IndustrialMicroservices: Foodly
• AutomatedTestGeneration.
Second,Foodlyhasalargemicroserviceapplicationgraph,whereindividual
services can issue upwards of a hundred RPCs to downstream services to
process a single customer request, prime for fault injection testing where a
single RPCfailure can alterapplication behavior. SFIT avoidsthe overhead of
application developers manually writing these fault scenarios using mocks
byautomaticallygeneratingthesescenariosbasedonfunctionaltestsofthe
microserviceapplication. Similarly,SFITalsoensuresthatnoimportantfault
injection scenarios are missed during testing, providing that each RPC is
testingforthesetoffaultsitissusceptibleto.
• Exhaustiveness.
Third, and finally, while Foodly has implemented a large number of appli-
cation resilience mechanisms (e.g., circuit breakers, load shedding, retries)
thatareallindependentlytestedandprovidedaslibraries,theirapplication
remainsvulnerabletofailuresbeforetheseresiliencemechanismsactivateand
afterfailuresstartoccurring. ThisspaceiswhereSFITshines: identifyingall
possiblefaultstheapplicationcanandwillobserve.
Inthefollowingchapter,SFITisevaluatedonFoodly’sapplication.

Chapter 9
Evaluating SFIT: In Practice
“TheywannaknowhowmanyrhymeshaveIrippedinrep,butresearchers
neverfoundallthepiecesyet,scientiststrytosolvethecontext,philosophersare
wonderingwhat’snext.”
EricBandRakim,Don’tSweatTheTechnique
As demonstratedin the previous chapter, Foodly provides anexciting and very
relevantindustrialmicroserviceapplicationforevaluatingService-levelFaultInjection
Testing(SFIT) in practice. In this chapter, the challenges with applying the SFIT
technique, using both the existing research prototype Python Filibuster and a
newopensourcere-implementationJavaFilibuster [Mei24e],arepresentedand
discussed.
Thechallengesfacedduringthisevaluationrangeallacrossthesoftwareengi-
neeringspectrum: technicaldifficultieswiththeprototypeimplementation,chal-
lenges faced with integration of the technique into existing processes within the
organization,andthehighcostinvolvedintestingservices.
Here,thesechallengesarepresentedinthecontextoftestingasingleserviceat
Foodly using Filibuster, a continuous process performed over two years (2) as an
independentcontractorofFoodly.
9.1 Philosophical Challenges
As discussed in Chapter 8, Foodly primarily tests their microservice application
in two ways: manual testing with their mobile application in production using
sandboxesandlocally,indevelopment,usingcomponenttests.
99

100 EvaluatingSFIT:InPractice
Manual testing does not suit SFIT, in that it is too difficult to orchestrate an
efficient,systematicexhaustivetestingapproachthatinvolvesmanual,interactive
developer actions: for example, by clicking in the UI of a mobile application to
perform operations that result in requests to the application. Therefore, it was
decidedbyFoodlytoexploretheuseofSFITonaservicethatusedcomponenttests,
testingservicesindependentlyandpair-wiseagainstanypossiblefailuresthatany
of their direct downstream dependencies might return. Rather obviously, pair-wise
testingofservicesin amicroserviceapplicationobviatestheneed foranytestcase
reductionstrategysuchasEncapsulatedServiceReduction(ESR)thatisbasedonhow
servicesencapsulatethethefailuresoftheirdownstreamserviceswhenresponding
totheircaller(s).
As the predominant communicationframework used by Foodly was Google’s
gRPCframework,whichcanonlyreturnaminimal(16)setofpossibleerrorcodes,
eachRPCissuedbyaservice couldbetestedusingSFITforallerrorcodesthatany
downstream dependenciesofthatservicemightreturn: thisincludeserrorcodes
that are overloaded for indicating active load shedding or open circuit breakers,
allowing SFITto coverthosefailure casesaswell. This contrasts with theregular
applicationofSFIT, whereanapplicationis tested entirely byusingareversetopo-
logical sort of the dependency graph to onlytest upstream services for the errors
thattheir directdownstreamdependencies canproduce: inessence, bypreferring
rawcomputepower duringtestingto address therestrictions of not beingable to
testthemicroserviceapplicationwholesale.
Instead,asingleserviceatFoodlywasselected,anditsexistingfunctionaltest
suitewastestedusingSFIT.Thisresultedinasignificant numberoftestfailures,as
expected,asnoneofthesetestscontainedassertionsregardingapplicationbehavior
underfault.
One test class was then selected that contained 39 functional tests, which rep-
resented the service’s core functionality and accounted for the majority of that
service’s test coverage. Using the SFIT technique, as faults were injected and the
testfailed,thedesiredapplicationbehaviorunderfaultwasthenencodedintothe
test using SFIT’s fault injection predicates. This process was completed when all
failure behavior in the application, for the functionality covered by the test suite,
wascapturedbythetest,andthetestsuitepassedultimatelyunderSFITexecution.
9.2 Results Overview
The results of applying SFIT to this service at Foodly were somewhat surprising.
First,fewertestfailuresoccurredthanexpected,duetotheuseofsoft dependencies.

ResultsOverview 101
It was only upon manual inspection of the individual tests that should have failed
withfaultinjection,thatthefollowingwasdiscovered:
1. First,manyfunctionaltestsinvokeddownstreamdependenciesthatwerenot
stubbed. This resultedin RPCs to these unstubbed dependencies returning
the error code indicating the RPC method was unimplemented. Not only
is fault injection redundant in these cases, but the functional test does not
captureapplicationbehaviorwhenalldownstreamdependenciesareworking
correctly.
2. Second, many tests did not assert that invoked downstream dependencies
were invoked(orstatedthatthedependenciescouldbeinvokedanynumber
oftimes.) Thiswasindependentofwhethertheywerestubbed.
This might indicate one of two things: developers only write tests for the pes-
simisticcase toensure thatapplications workcorrectlywhen allsoftdependencies
fail,orthelatter,wheredevelopersonlyiterateontestsuntiltheypass. Ifthelatter,
itissafetoassumethatifdevelopersdonotinvestigatetestssufficientlytostuball
dependencies when tests are passing, any tests that continue to pass under fault
injectionwillremainunquestioned,resultinginpossiblelatentbugsinproduction.
When it came to hard dependencies, it was a cumbersome task to encode the
samefailurebehaviorineveryfunctionaltestforallcombinationsoffailures. This
is because many of the tests shared a common code path responsible for loading
context information related to the customer with several RPCs, each throwing a
fatalerrorunderRPC failure. Thiswasthenexacerbatedbyteststhatperformed
setupforthetestinsideofthetestitself,whichresultedinfatalfaultsbeinginjected
duringtestsetupandnottestexecution,requiringthatboththetestandtestsetup
beupdatedwithfaultinjectionpredicates,asdescribedbySFIT.
Finally,theprocessofupdatingteststoencodethebehavioroftheapplication
underfaultwasgenerallydifficult:
1. It was challenging to understand where an injected fault occurred in a test
execution due to the large number of RPCs executed asynchronously by a
single test (with some identical RPCs being performed multiple times in a
singleexecutionatdifferentpointsinthatexecution.)
2. It was challenging to know which SFIT fault injection predicate to use to
encodefaultbehavior.
3. Theprocess ofupdatingtestswiththeappropriate SFITfault injection pred-
icate was cumbersome due to duplication of fault behavior across multiple
testsandwhenfaultswereinjectedintestsetupandteardown.

102 EvaluatingSFIT:InPractice
Inthefollowingsections,boththechallengesfacedwhenapplyingSFITatFoodly
and the preliminary results of using SFIT at Foodly are presented. These results
arethenusedtoderiveanewdesignofSFIT,PrincipledService-levelFaultInjection
Testing (p-SFIT)thatistheresultofaco-evolutionoftheService-levelFaultInjection
Testing designbytheauthorofthisdissertationincollaborationwithFoodly.
9.3 Experimental Configuration
ToevaluateSFIT,oneserviceatFoodlywasselectedtobetestedwith Filibuster. In
agraphofhundredsofdifferentservices,thisservicehastheprimaryresponsibility
of subscribing consumers to the premium plan offered by Foodly. This service
takesdependenciesonseveraldifferentdownstreamservicesovergRPCandseveral
directdependenciesondatabasesandqueues: CockroachDBandKafka.
Thisserviceisautomaticallytestedforeachnewcommitusing3,209tests,where
1,419ofthose3,209testsarecomponenttests. Thereare936authoredcomponent
tests,whichresultin1,419tests: 862arestandardtests,whereas74areparameterized
testswithasetofprovidedinputs. Thesetestshavebeenwrittenandmaintained
by30differentdevelopers.
Forourevaluation,onlythe862non-parameterizedtestswereusedtounderstand
thebroadtypesoffailuresexhibitedbythesystemunderfaultinjectionandthen
focus on one specific test file containing 39 specific tests that cover the essential
functionalityoftheservice: subscribingusers.
9.3.1 Component Tests
ComponenttestsareimplementedinJUnitasstandardtestswithsupportingcode
forstartingandstoppingtheserviceundertest,stubbingdependencies,andstarting
requireddatabasedependencies. StubbingofRPCsisperformedusinganin-process
gRPCserverwherefixturesareinstalledforanRPCmethod;therefore,RPCsare
fullyexecutedinsteadofdirectlystubbingthemethodinvocations. Stubusagein
componenttestsisaproxyfor(potential)sideeffectsperformedbyotherservices.
For example, instead of running a dependency and asserting that the state was
mutatedinthatservice’sdatabase,astubisusedtomimicthatservice’sbehavior.
Testauthorsmostlyusea“given,when,then”stylewhenwritingtests. However,
thisstyle is not enforced by any underlying framework code thatimplementsthe
separationofthesedifferentconcernsbutismerelyacodingstyleusedinsideofa
singletestmethodwiththedifferentsectionsdelineatedbycodecomments.
Inthe“given”section,developersinstallrequiredfixturesandstubdownstream
dependencies. These stubbed dependencies are then automatically checked for

ExperimentalConfiguration 103
the correct number of invocations by the stubbing framework only after the test
passes successfully. In the “when” section, developers issue an RPC to one of the
APIsexposedbytheservice. Inthe“then”section,developersasserttheexpected
response from the RPC and any side-effects that should have been performed.
Developers leave this section blank to indicate that an RPC invocation does not
throwanexceptionwithoutanyotherexplicitassertions.
Basedonthisstructure,componenttestsfailonlyinthreepossibleways:
1. ThrownExceptions:
whentheRPCinvocationthrowsaruntimeexception;
2. AssertionFailures:
whenthetestassertionsdonothold;and
3. StubInvocationFailures:
whenstubsarenotinvokedthenumberoftimesspecified. Whilestubinvoca-
tion failures do surface as assertion failures at the end of the test execution,
thesearedistinguishedfromassertionfailures. Thisisbecause,incontrastto
assertionfailures whichcan checkanyarbitrary expressionthatreduces toa
booleanvalue,stubinvocationfailurestakeaspecificformthatcorrespondto
aparticulartypeoftestfailure. Thesethenandcanbeautomaticallychecked
againsttheobservedbehaviorofthesystem,asinp-SFIT.
9.3.2 Re-implementing Filibuster
Theoriginalgoalofthisevaluationwastoadapttheprototypeimplementationof
SFIT,Python Filibuster,asnecessarytoperformtestingofservicesatFoodly.
ArchitectureandImplementation. Asdiscussed,theoriginalPython Filibuster
prototypeis implementedusing alanguage-agnostic designcomprised ofdifferent
componentsthatoperateinconcert:
• Several instrumented RPC clients, implemented in Python to support the
Filibuster application corpus but designed to be language-agnostic. These
instrumentedRPCclients,implementedinthelanguageofchoiceusedbythe
microservice, communicate with the Filibuster server to register RPCs and
injectfaultswhennecessaryinalanguage-agnosticJSONformat.
• A CLI for executing tests, implemented in Python. The CLI executes the
developer-authoredfunctionaltestinanylanguagethatexercisestheapplica-
tionbehavior.

104 EvaluatingSFIT:InPractice
• A server, implemented in Python. The Filibuster server tracks how many
test executions are necessary and what faults must be injected for each test
execution.
Initially, the thinking was to create instrumented RPC clients for Java the lan-
guage runtime used by Foodly, and reuse the existing components. However, in
the courseof iterating onthe integration of Filibuster with Foodly’s code over two
years,theentiretyof Filibuster wasrewritteninJava.
First,theinstrumentationneededforRPCclientswaswritteninJavaforGoogle’s
gRPClibrary. Next,anexternalCLItoolwasreplacedwithintegrationintotheJUnit
testframeworkusedbyFoodly’sfunctionaltestsusingacustomtestannotationand
factory. Thiswasdoneforseveralreasons.
1. AsFilibuster needsto runthe functionaltestmultiple times,it was necessary
to minimize the cost of starting a new JVM each execution and waiting for
Kotlintestcodegenerationtoexecute. Evenwithsharingagradledaemon,the
buildtoolusedbyFoodly,acrossexecutions,thisstartuptimewasprohibitive,
withasingletestexecutiontakingaslongas1minute.
2. NotrestartingtheJVMandintegratingit intoJUnitwouldavoidtheneed to
writeacustomtoolforaggregationofcoveragedataacrossdifferentexecutions,
asthiswouldhappenautomatically.
3. WithJUnitintegration,anexternalFilibustertestharnessthatlivedoutsidethe
application code was no longer required. Similarly, this integration avoided
the need to pause Filibuster execution to allow an external debugger to be
attachedwhendebuggingfailuresfromfaultinjectionwerenolongerrequired.
Finally,theFilibuster serverthatcommunicatedwiththeinstrumentedclients
using RPCs was replaced with an in-process Java implementation of that server.
ThisreducedseveralchallengeswefacedwithusinganexternalPythonprocessin
Foodly’scontinuousintegrationenvironment,reducedexecutiontimebyavoiding
expensiveRPCsbetweentheapplicationandFilibusterserverandallowedformore
detailedreportingbyremovinglanguage-agnosticerrorreportingwiththeserver
itself.
From there, it was determined that the style of reporting used by Filibuster’s
server,duplicatedintheJavare-implementationoftheserverandpresentedaslog
entries, made debugging and understanding of what went wrong during a fault
injectiontesttoodifficult. Therefore,anIntelliJpluginwasdesignedthatallowed
applicationdeveloperstovisualizetheresultsrecordedbytheFilibuster serverto
makedebuggingsignificantlymoreaccessible. Thisincluded,butwasnotlimitedto,

ExperimentalConfiguration 105
thetestexecutionsgeneratedby Filibuster,thefaultsthatwereinjected,therequest
andresponsesforallissuedRPCs,andthetestfailuresthatoccurredwhenfaults
wereinjected.
Nondeterminism: Data andScheduling. Most of the functionaltests that Foodly
writes are free from observable nondeterminism. However, these tests contain
significantnondeterminismintheirimplementationinbothdataandtheunderlying
scheduling of threads. This complicates the SFIT approach, as the systematic,
exhaustive exploration performed by SFIT assumes that RPC invocations can be
uniquelyand deterministicallyidentifiedusingtheirrequestandcallsite,aswell
asthattheresponsestothoseRPCinvocationsacrossdifferenttestexecutionsare
deterministic. Inpractice,alloftheseassumptionswereviolated.
As discussed, SFIT uses an algorithm called DEI to identify RPC invocations
uniquely and deterministically: this enables SFIT to know when the fault space has
beenfullyexplored. DEIusestheinvokedRPCservice,RPCmethod,callsite,and
invocationcounttodeterminethepreciselocationofanRPCintheapplicationcode
regardlessofconditionalcontrol flow, loopingconstructs,and functionabstraction.
ThisisencodedasauniqueanddeterministicidentifierforthatstableRPCacross
multipleexecutionsofthesametest. Whenconcurrencyprimitivesareused,like
threads, DEI also encodes the RPC’s arguments, called the invocation payload,
intothisidentifiertoavoidtheuseofaspecializedresearchversionoftheJVMin
testingthatcancontrolthreadscheduling. Thisisimpracticalforlargemicroservice
applications that use different language runtime versions and support libraries
acrossotherservices.
AtFoodly,componenttestsarenondeterministicinbothdataandscheduling.
Regarding data, tests generate random user identifiers often derived from auto-
incrementing fields in databases. These identifiers are included in many RPCs
executedbytheapplication,andtherefore,RPCargumentsandresponsesarenot
deterministic acrossexecutions. Regarding scheduling, every RPC executed uses a
Kotlincoroutine,whereasingleRPCcanbeginrunningononethreadandcomplete
executiononadifferentthread. Furtheringthecomplexity,Kotlin’scoroutinesare
limitedinthatstacktraces,usedtodeterminetheRPCscallsite,arenotavailable
undercoroutineresumptioninapplicationcodebutonlyavailableasynchronously
through a reassembly process performed by, and available onlyin, the debugger,
whenattached. ThesecomplicatethegenerationofstableidentifiersforeachRPC
necessaryforexhaustivesearchbySFIT.
To work around this deficiency, a modified version of DEI was created that is
“best-effort.” This modified version encodes as much information as is available
at the time of the RPC, omitting any information known to be nondeterministic

106 EvaluatingSFIT:InPractice
banannotationprovidedtothetestitself. Inpractice,almostalltestscontaindata
nondeterminism in RPCs. However, most of the code tested in this evaluation
executesdownstreamRPCsinsequence,regardlessofcoroutineusage. WhenRPCs
occurconcurrently,theyalmostalwaysdifferbyRPCserviceormethod.
9.3.3 Enabling Filibuster
ToenableFilibusterforthesubscriptionservice,Filibuster wasincludedasatest
dependencyoftheapplication. ThisensuredthatanycodeintroducedbyFilibuster
did not impactanyof the productioncode or alteranyproduction dependencies of
thesubscriptionservice.
Aminorrefactoringwasthenperformedofthesubscriptionservicetoallowthe
FilibusterGRPCinterceptortobeadded(usedfortrackingRPCduringthereference
executionandinjectingfaultduringthegeneratedfaultinjectionexecutions)only
atruntimewhenrunningasatestusingthedependencyinjectionlibraryusedby
Foodly: Google’sGuice.
Thisinterceptorwas specifically installedbetweentheapplication codeand the
underlying RPC framework used by Foodly: Foodly’s Hermes library. This was
donetoensurefaultscouldbeinjectedwithoutbeingadverselyaffectedbyHermes
built-in resilience mechanisms: specifically, circuit breaking and load shedding
under failure as well as automatic retry on certain RPC failures. Therefore, this
allowedFilibuster toinjectfaults withoutthoseRPCsbeingautomatically retried
underfailureorriskrepeatedfaultinjectioninterferingwith Filibuster’sexhaustive
exploration algorithm: the goal was to find application resilience issues and not
test the already well-tested built-in resilience mechanisms of the underlying RPC
framework.
9.3.4 Configuring Filibuster
Filibusterwasconfiguredusingthefollowingconfigurationoptions. First,toensure
terminationofthesearchalgorithmwithinareasonabletime:
• DataNondeterminism.
Filibuster was configured to adapt the exhaustive search algorithm to deal
withthedatanondeterminismthatispresentincomponenttests.
As presented, Filibuster uses analgorithm that encodesthe RPC’s arguments
into a unique RPC identifier used during an exhaustive search. This allows
Filibustertosearchthefaultspacewhenschedulingnondeterminismproperly
ispresentwithoutcontroloftheunderlyinglanguageVMscheduler.

ExperimentalConfiguration 107
Unfortunately,thisalgorithmisincompatiblewithtestscontainingdatanon-
determinism,astheseargumentswillvaryfrom executiontoexecutionasall
ofthetestswrittenbyFoodlyhavedatanondeterminism. Forexample,each
testgeneratesauniqueuseridentifierforeachre-executionofthesametest.
Therefore, each invocation of the same test will not execute the same RPCs,
andtheexhaustivesearchalgorithmhastobeadaptedaccordinglytocorrelate
RPCsbetweendifferentexecutionsasthesameRPCforexhaustivesearchto
terminate.
• MaximumFaultInjections(UpperBound.)
Filibuster was configuredto generate, atmaximum, 100faultinjectiontests
percomponenttest. BecauseofrestrictionsdeepinthedesignofJUnit,fault
injectionteststhatwerenotnecessarywerestillgeneratedbutwereeffectively
ano-op.
Specifically,ifareferenceexecutionofagiventestexecuted30RPCs,Filibuster
would generate30 additionaltests(i.e., 1referenceexecution+ 30faultexecu-
tions) to cover all single fault, no permutation scenarios required, with the
remaining70executionsresultinginno-ops. Ifareferenceexecutionofatest
executed101 RPCs,Filibuster would generate100additional tests,skipping
thefinalrequiredfaultinjection(i.e.,1reference+100faults,onenon-executed
scenario.)
No-opexecutionsincurredanexecutionpenaltyof0.15msperexecution. In
theworstcase,a15-secondpenaltypertestthatexecutednoRPCs. Thiswas
done to place an upper bound onexecution time underthe assumptionthat
notestwouldrunmorethan100RPCstodownstreamservices.
Second,toreducethenumberofFilibuster-generatedtestspercomponenttest,
twooptimizationsweredone:
• FaultPermutations.
Filibuster wasconfiguredto notinjectmultiple simultaneousfaultsand only
toinjectasinglefaultineachgeneratedtest.
This was done to keep the execution time reasonable, given that each test
issuesmanyRPCs.
This optimization was performed by examination of a subset of tests that
determinedthatRPCexecutionwasperformedinasequentialworkflowwith
minimalconcurrency.
• Exhaustiveness.
Foregoing static analysis, Filibuster was configured only to inject a single

108 EvaluatingSFIT:InPractice
fault: the gRPC StatusRuntimeException exception parameterized by code
UNAVAILABLE,whichismostoftenusedtoindicatethattheremoteserviceis
unreachableorreturningaconnectionerror.
Again, this was done to keep the execution time reasonable for this naive
evaluationgiventhatthere wasasignificantamount ofteststoexecuteusing
Filibuster andthateachtestissuesalargenumberofRPCs.
This optimization was performed by examining a subset of tests that deter-
minedthatRPCexecutionrarelycontainederrorhandlingcodeconditional
ontheerrorcodethatwasreturned.
Third,anapplication-specificoptimizationwasdone:
• CacheAssumption.
UsingacacheforRPCinvocationsandresponsesforagivenRPCwasassumed.
Atthetimeofwriting,theservicetestedwasconvertingfromaRedis-based
cacheto amulti-tier cachein theapplication. Both cacheswere turnedoff by
defaultwhenexecutingthetestsuite.
Therefore,toavoidencodingcachesemanticsintothetestharnessandtoavoid
havingtorestartbothRedisand theJVMin betweeneach testinvocation,the
FilibustersearchalgorithmwasconfiguredtopreventfaultinjectionsonRPCs
for the same service, method, and arguments if it has already succeeded in
thetestexecutionpreviously,simulatingthebehaviorofthiscache.
This under-approximation reduces the completeness of the Filibuster algo-
rithmbyskippingscenariosofcachefailuremid-request.
Itisnotedthatalloptimizationswerevalidatedagainstthesubscriptionprocess,
whichaccountsforthemajorityofcodecoverageofthisservice. Whilethisisnot
definitive,itaccountsfortheprogrammingstylewidelyusedinthisrepositoryand
acrosstheFoodlymicroserviceapplication.
9.4 Socio-Technical Challenges
Intermsofsocio-technicalchallenges,itwasfoundthatanymodificationsmadeto
applicationcode,buildprocesses,ortestcodetosupportSFITneededtobejustified
forthosechangestobeintegratedintothecodebase. Thisinvolvedwritingtechnical
documentation,minimizingtheimpactonexistingprocesses,andproducingvisual
resultsforunderstandingtheapproach’sbenefits.

Socio-TechnicalChallenges 109
9.4.1 Education and Documentation
When it came to integration into the service that was tested with SFIT at Foodly,
theauthorwasimmediatelyaskedseveralquestionsbydifferentdevelopersthat
all took the general form of “What is this, and how will it impact me?” In short,
developerswantedto knowwhatthistool wasdoing,howitwould impactthem,
andhowit would impact theirdailyworkflow. Thishad tobeaddressedin several
steps.
Asmodificationswerebeingmadedirectlytotestcodethatapplicationdevel-
opers of the service were working on as part of their daily work, documentation
had to be written on how actually to work with the SFIT tool, what errors they
mightsee,whatthoseerrorsmean,andwhattodoaboutdebuggingthoseerrors.
ThisinvolvedextensiveJavadocworkwithinthecodeoftheFilibuster Javaimple-
mentationitselfand usingFoodly’sexternaldocumentation toolforwritingseveral
interactivetutorialson adapting a tool for use with Filibuster and debugging the
resulting failures. In addition, how the Filibuster integration was performed for
thatservice,howitintegratedintotheIDE,andhowitintegratedintothebuildand
deploymentprocessesusedforfeaturedevelopmentallhadtobedocumented.
Duringthisprocess,severaliterationsoftheFilibuster APIweremadebasedon
feedbackfrom theteamthat workedon theservicewe weretesting. From there,a
“RequestforComments”(RFC)documentwasproducedthatwasdistributedtothe
broaderteamwithwhatweassumedwouldbethefinalizedAPI,whichresulted
inseveraladditionaliterationsoftheAPI.Aspartofthis,severaldetaileddiscus-
sions were had with team members to justify why this approach was better than
thealternativeapproachesforfaultinjectiontestingandwhyseemingly“cleaner”
approacheswouldnotscalewithinFoodly.
9.4.2 Development Processes
Regardingthelocaldevelopmentexperience,severaldifferentIDEintegrationswere
builtbasedondeveloperfeedback.
Itwasdiscoveredthatdeveloperswantedamostlyopt-inexperience,wherethey
didnotrunthesetestsautomaticallywhenrunningthetestsuiteoftheirapplication.
Inshort,theydidnotwantanyprocesschangesmadethatmayimpacttheirlocal
development experience. Whentheauthorinadvertentlymadethesechanges early
during our initial integration, they were immediately asked to revert them. A
designwasultimatelysettledwhereasingletestcouldberunwithfaultinjection
optionallyinIntelliJbutdefaultedtorunningthattestwithoutfaultinjection. Itis
believed that thisreflects the methodology ofthis style of test development: iterate
quicklytogetthetestpassingandthenrunwithSFITtoidentifyresiliencebugs. In

110 EvaluatingSFIT:InPractice
practice,thereisnoevidencetoindicateifthisintegrationstylewilleverresultina
developerrunningthetestswithSFIT,butinsteaddefertoresiliencebugsidentified
incontinuousintegration.
Asobservedwhen integratingSFIT withcontinuous integration, developersare
hesitanttoadoptanyprocessthatwillincreaseaperceived“slow”buildtimefor
theirapplicationincontinuousintegration. Therefore,anyproposalwhereanew
techniquewouldincreasecodecoverage, forexample, atthecostof16additional
tests for every single RPC executed by a given test of several thousands of tests,
was met with pushback. Therefore, it was necessary to develop a strategy where
SFIT could still be used but without impacting the daily workflow of developers.
ThestrategyultimatelyimplementedinvolvedperformingnightlySFITrunsonthe
most recent commit to the ‘main’ branch of the repository and reporting failures
using a Slack notification on failure. While this appeased the developers of the
servicewherethistestingwasbeingperformedbyavoidinganexpensiveSFITrun
foreachcommitduringfeaturedevelopment,itwasfoundthatbothcausederrors
to be ignored by most developers and made correlation between SFIT failures with
the change set that introduced the regression difficult. At this point, it remains
unclearwhatthecorrectbalanceishere,astraditionalapproachesforregression
identification(e.g., git bisect)canbeprohibitivelyexpensiveduetotheoverhead
involvedinSFIT-styletesting.
Itwasalsodiscoveredthatintegrationwithcodecoveragewashelpfulincon-
vincingdevelopersofthevalueofSFITtesting. Forexample,itispossibletovisually
show developers the increase in code coverage provided by SFIT through fault
injection. Todothis,statisticswerereportedusingJavaCodeCovusingaspecific
tagthatcouldbeusedtodifferentiatethenon-SFITtestsuiteexecutionagainstthe
SFITtestexecutionvisuallyandseetheincreaseincoverage.
9.5 Results
The applicationof JavaFilibuster resulted inmanyfailing tests. This wasexpected
asnoneoftheexistingtestswereadaptedtoencodetheapplication’sbehaviorunder
failure.
Ofthe862componenttests,JavaFilibusteridentified546faultinjectionscenarios
thatresultedintestfailures,withtwoofthosefailuresalsoappearinginthereference
execution butnotin any fault injectionexecution,indicating thatthese testswere
flaky. Thesefailureswereconsistentwithouranalysisofhowcomponenttestscan
fail: thrownexceptionsforthefailureofharddependenciesassertionfailures,andstub
invocationfailuresforthefailureofsoftdependencies.

Results 111
• 367 of 546 (67.22%) failures were because the test expected a response, but
agRPCexceptionwasthrown. Thisindicatesaharddependency failureasan
exceptionwasthrown,indicatingthattherequestcouldnotbeprocessed.
✓Therefore, -SFITshouldprovideamechanismfordirectlyidentify-
p
ing RPCs that are hard dependencies and the thrown exceptions that
theirfailureproduces.
• In85ofthe367(23.16%),thesameexceptionwasthrownonharddependency
failure. However, it was parameterized with four different status codes de-
pendingon thefailed dependency. Similarly,in304 ofthe367 (82.83%),the
same exception was thrown on hard dependency failure. However, it was
parameterizedwiththesamestatuscodewithdifferentexceptionmessages,
eachtoindicatewhichharddependencyfailed. Thisindicatesthatdifferent
hard dependency failuresmayarbitrarily return thesame or different status
codes.
✓Therefore, -SFITshould requirethatdevelopers indicatetheasser-
p
tionsthatshouldholdunderathrownexception toensure
bystatuscode
that statuscodeshaveconsistentmeaningand canbetreated uniformly
bytheupstream,callingservice.
In contrast, p-SFIT should not allowthe developer to encode behavior based
onthecontentsoftheexceptionmessage,asthatismeantonlyfordebugging.
• 110ofthe546(20.15%)failureswerebecausethetestfailedanassertionafter
returningasuccessfulresponsetothetestedRPCmethod. Thismay indicates
that a soft dependency failed and the service gracefully degraded. However,
as assertions may be written arbitrarily, it may also indicate the failure of a
harddependency. Arandom samplingof the110 failures revealed thatmany
of theseerrors were directlyrelated to gracefuldegradation: for example,by
assumingacustomer’slocationistheUSAwhenitcannotbedetermineddue
toRPCfailureorbynotdisplayingfiveadvertisementsonalandingpageif
only4oftheRPCsthatloadtheadvertisementssucceed. Thisindicatesthat
bothhardandsoftdependency failurescanbeidentifiedbyassertionfailures.

112 EvaluatingSFIT:InPractice
✓Therefore, -SFITshouldrequirethatonbothhardandsoftdepen-
p
dencyfailure,developersexplicitlyindicatetheassertionsthatshould
hold. This ensures that when soft dependencies fail and fallbacks are
used,theyarecapturedintests;whenharddependenciesfailandthrow
exceptions,thesystemremains consistent basedonthe thrown exception
type.
• 61ofthe546(11.17%)failureswerebecausethetestreceivedasuccessfulre-
sponsefromthetestedRPCmethod,thenpassedallassertions,butfailedwhen
RPCstubswereverifiedforthecorrectnumberofinvocations. Thisindicates
asoftdependency failureonlydetectablethroughmissingstubinvocations.
✓Therefore, -SFITshouldrequirethatdevelopersindicateprecisely
p
howmanytimeseverystubbedRPCshouldbeinvoked.
A single file that exercised the core functionality of the service (39 tests) was
thenselected,andthetests weresubsequentlyupdatedtocontaintheapplication’s
behaviorunderfaultusingSFIT’sfaultinjectionpredicates.
✓ -SFITshouldproviderecommendationstothedeveloperonhowtoupdate
p
theirteststocontaintheapplication’sbehaviorunderfault.
Ineverytest,itwasnecessarytoencodethefailureoftwoharddependenciesin
sharedcodepathsforthrownexceptions: iftheRPCfailedtolookupthecustomer
ortheir location. Then,forsoftdependencies, the invocation counthad tobe condi-
tionalizedbasedonthefaultinjectionsoneitherthestubbedRPCoranyRPCfailure
thatwould preventthestubbedRPCfrombeinginvokeddue tocontrolflow that
wasconditionalonpreviousRPCssucceeding.
Outofthe39teststhatwereencodedwiththeapplication’sbehaviorunderfault,
thefollowingwasidentified:
• 33ofthe39tests(84.62%)hadtobeadaptedfortheexceptionthrownwhen
thelocationlookup failed. 34of 39tests(87.18%) hadtobe adaptedforthe
exceptionthrownwhenthecustomerlookupfailed. Thisindicatesthathard
dependenciesareoftenusedinsharedcodepathsexecutedbymultipletests.

Results 113
✓ Therefore, -SFITshould provideamethodfor sharingtheencoded
p
failurebehavioroftheapplicationeasilyacrossdifferenttests.
• Asexpected,7of39tests(17.95%)hadtobemodifiedintheexecutionblock
to account for downstream dependencies where faults were injected. Still,
they had noimpact on test outcomesother than asserting they wereinvoked.
However, 9 of the 39 tests (23.08%) had to be adapted to verify that, on a
thrownexception,other downstreamdependencieswerenotinvokedbymodi-
ficationoftheirstubinvocationsusingconditionalcodeonfaultinjection. This
indicatesthatharddependency failuresthatresultinthrownexceptionsprevent
theinvocationofsubsequent,stubbedRPCs.
✓Therefore, -SFITshould requirethaton thrownexception,develop-
p
ersre-asserthowmanytimesstubsshouldbeinvoked.
Thisensuresthatside-effectsperformedbyRPCsarenot completedwhenan
exceptionisthrown,potentiallyleavingthesysteminaninconsistentstate.
Finally,outofthe39testsencodedwiththeapplication’sbehaviorunderfailure,
not a single test stubbed all of the soft dependencies it invoked. Instead, developers
duplicated the same test repeatedly only to, in each derivative test, only stub the
RPCandassertthatthestubwasinvoked.
✓Therefore, -SFITshouldrequire thathappypathfunctional testsstuball
p
invokedRPCsandrequirethosestubstoreturnsuccessfulresponses.
(Potential)Bugs. WithSFIT,itwasclearthatsoftdependencyfailurecanbethe
rootcauseoflatentapplicationbugs. Ofthe39tests,3ofthesetests(7.69%)revealed
thepresenceof3uniqueapplicationbugs. Twoofthesebugsinvolvedthefailure
ofasoftdependencyinfluencingwhetherornotasubsequentRPCwasexecuted.
Thethirdbuginitiallyappearedasaduplicateofthesecondbug. However,another
independent bug was then discovered in the existing test suite when fixing the
second bug, indicating that SFIT can help surface interesting, unexplored failure
scenarios.
With the first failing test case, a failure of RPC A inhibits the invocation of
someRPCB.Inthisspecificcase,RPCB’sfailureisloggedandreported. However,
control flow prohibits the invocation of RPC B when RPC A fails. When RPC A

114 EvaluatingSFIT:InPractice
fails, its failure is swallowed, and nothing is logged. In this application, RPC A
canfailbyreturningbotharesponseindicatingthatarecordisnotpresentanda
communication failure. When investigating the possible bug, it was determined
thatanofflineprocessisusedtocompensate forthefailureofbothRPCthrougha
manualreconciliationprocessusingFoodly’sdatawarehouse.
Withboththesecondandthethirdfailingtestcases,thesameshapeappearedin
thesamecodepath: someRPCXfailsandinhibitstheinvocationofsome(different)
RPCYonfailure. However,inthecaseofthethirdfailingtest,theservicedevelopers
hadwrittenatestexplicitlyforthespecificnegativecaseofRPCYfailing. Therefore,
duringtheinvestigation,itwasdeterminedthattheX-failure-inhibits-Ybugshould
be repaired like the strategy employed in the test case that specifically modeled
thefailureofY.Whatwasidentifiedwassurprising: notonlydidthetestcasethat
developershadwrittentotestthefailureofRPCYmishandlethefailureexplicitly,
but it was an active bug that had adversely affected customers as recently as five
daysbeforethebuginvestigation. SFIThadnotonlyidentifiedapotentialfailure
case,buthadalertedustohowtheexistingtestsuitewaswrittenincorrectly.
Inalloftheidentifiedcases,therootcausewasclear: developershadexplicitly
mapped the failed RPC into either a null or default response of the appropriate
type. Thisvariablewaspassedthroughouttheapplication,causingthefailureto
changethecontrolflowandbypasssubsequentRPCinvocations.
✓Therefore, -SFITshould requirethattest codeindicatehow manytimes
p
downstream dependencies, which do not affect the RPC’s response (as in
bothcasesa responsewasreturned)shouldbeinvoked.
successful
9.6 Takeaways
As demonstrated in this section, SFIT, as designed, suffers from several interest-
ingdeficienciesthatwouldhaveremainedundiscoveredwithoutevaluationinan
industrialcontextonareal-worldindustrialmicroserviceapplication.
First, and most notably, industrial microservice applicationsare much too large
and complicated to be tested wholesale. Therefore, any fault injection approach
must test services in isolation, exhaustively for the faults they are susceptible to
basedontheirdownstreamdependencies.
Second, without enforcing that application developers address each injected
fault,itismuchtooeasyfordeveloperstowritetestsofservicesthatignoreinjected
faultsthatdonotresultintestfailures. Forexample,whereanapplicationdeveloper
failstowriteanassertiononbehaviorconditionalonwhetherafaultisinjected.

Takeaways 115
Third, the overhead in determining how to encode failure behavior into ap-
plication test code is high. Therefore, it is necessary to provide a mechanism for
developerstounderstandwhereafaultisinjectedquickly,whattheimpactofthe
injectedfaultwas,andhowto,ifdesired,encodethatbehaviorintothetestsoftheir
microserviceapplication.

Chapter 10
Microservices: Dependency Type
Evolution
“Weallexistinourownpersonalrealityofcraziness.”
AlejandroJodorowsky
Armed with the results fromthe industrial evaluation at Foodly, presented in
Chapter9,thecontextcanbeswitchedbacktoresearchtoaddressthedeficiencies
intheexistingService-levelFaultInjectionTesting (SFIT)approach.
More specifically, with the knowledge of how microservices are tested in in-
dustrialsettings,thechallengeswithadaptingindustrialmicroserviceapplication
tests for resilience, and how both hard and soft dependencies are employed, and
testedinindustrialmicroserviceapplications,anewprocessfortestingmicroservice
applicationscanbedesigned.
However,first,itisnecessarytodesignanewapplicationforthemicroservice
applicationcorpusthatreflectsthegroundtruthofindustrialmicroserviceapplica-
tions. Inthischapter,applicationispresentedusingstrictlyharddependencies: this
applicationisinspiredbyapplicationdesignandbehaviorobservedatFoodly. Then
thisapplication isevolved, inthesame manneras doneat Foodly, to changehard
dependenciestosoftdependencieswiththegoalofimprovingapplicationresilience.
Thisevolutionintroduceslatentapplicationbugs,primefordetectionwithSFIT.
10.1 Application Structure
Considerthemicroserviceapplication,depictedinFigure10.1comprised6services,
eachwithitsownassociateddatastore:
117

| 118 Microservices: | DependencyTypeEvolution |     |     |             |     |
| ------------------ | ----------------------- | --- | --- | ----------- | --- |
|                    | Client                  |     |     | Client      |     |
|                    | API Gateway             |     |     | API Gateway |     |
Interceptor
Filibuster
Server
Order Service
Order Service
Interceptor
|              |              | Pricing     |              |              | Pricing     |
| ------------ | ------------ | ----------- | ------------ | ------------ | ----------- |
| User Service | Cart Service | Adjustment  |              |              |             |
|              |              | Service     | User Service | Cart Service | Adjustment  |
Service
Interceptor
Shipping
|     |     | Service |     |     | Shipping  |
| --- | --- | ------- | --- | --- | --------- |
Service
| (a)withoutFilibuster |     |     | (b)withFilibuster |     |     |
| -------------------- | --- | --- | ----------------- | --- | --- |
Figure10.1: PurchaseApplicationStructurewithFilibusterInstrumentation
• APIGateway:
Forhandlingconsumerrequests;
• Order:
Forhandlingpurchases;
• User:
Mappingactivesessionstousers;
• Cart:
Mappingsessionstoshoppingcarts;
• PricingAdjustment:
Determiningifacartiseligibleforapricingadjustment,intermsofadditional
feesordiscounts;and
• Shipping:
Forshipping.

ApplicationStructure 119
| Service | Database | Database | Database | Database |     |
| ------- | -------- | -------- | -------- | -------- | --- |
Process
Filibuster
| RPC Process |              |              | Pricing         |           |     |
| ----------- | ------------ | ------------ | --------------- | --------- | --- |
|             | User Service | Cart Service | Ad ju s tm ent  | Shipping  |     |
| Decision    |              |              |                 | Service   |     |
S e rv ice
Response
Instrumentation
RPC
|     | RPC     | RPC     | RPC           | Error | Error |
| --- | ------- | ------- | ------------- | ----- | ----- |
|     | getUser | getCart | getAdjustment |       |       |
|     |         |         |               | Yes   | Yes   |
|     |         | No      | No            |       |       |
|     | Fail?   | Fail?   | Soft Dep? No  | Fail? | Fail? |
API Gateway
|        |       |       | Yes No          |            | No       |
| ------ | ----- | ----- | --------------- | ---------- | -------- |
|        | Yes   | Yes   |                 |            |          |
|        |       |       |                 | RPC        | Complete |
| Client | Error | Error | Adjustment? Yes |            |          |
|        |       |       |                 | updateCart | Purchase |
No
Order Service
Figure10.2: PurchaseApplicationWorkflowwithGracefulDegradation
WhilethisexamplereflectsbehavioratFoodly,theexampleisfictional: itiscon-
siderably simplified in this paper for both presentation and confidentiality. Specifi-
cally,serviceshavebeenrenamed,andadditionalservices,RPCs,andbusinesslogic
thatisunnecessaryforexploringRPCfailure’simpactonmicroserviceresilience
havebeenremoved.
WhentheorderservicereceivesanRPCfromtheAPIgateway,itfirstissuesan
RPCtotheuserservicetoretrievetheuser’sinformation. Oncethatiscomplete,the
orderservicethenissuesanRPCtothecartservicetoretrievetheuser’sshopping
cart. Then,thecartanduserinformationissentinanRPCtothepricingadjustment
servicefromtheorderservice. Ifandonlyifanadjustmentisreturned,asubsequent
RPCisissuedtothecartservicetoadjustthepricingforthatshoppingcart. When
all of that is complete, the purchase is confirmed through additional RPCs and
databasewritesthathavebeenomitted. ThisworkflowisdepictedinFigure10.2.

120 Microservices: DependencyTypeEvolution
10.2 Hard Dependencies
In the first iteration of the purchase application, all of the services that RPCs are
madetoareharddependencies: inthatifanyoftheRPCs fail, anerrorisreturnedto
the API gateway which is propagated back to the customer and asks them to try
theirrequestagain.
Let us explore what happens in a bad deployment of the pricing adjustment
service. For example, consider the case where the pricing adjustment service is
deployedwithabugthatcausesnullpointerexceptionswheneveranRPCisreceived
to adjust the user’s cart. This bug may not be caught in testing because it is only
triggeredbyamismatcheddependencyinproduction.
When this code is deployed to production, it is incrementally rolled out: up-
grading a single service instance at a time, in bulkheads [Mic23b] that partition
traffic to isolate theeffects of a bad deployment to a singlepartition. As each par-
tition is upgraded, it passes standard health checks and probes (e.g., readiness,
liveness) [Kub23] indicating that the service can respond to requests. However,
these probes may only be shallow checks that verify the service is answering re-
questsbutdonotexerciseeachandeverycodepath. Assoonasthecodeisliveand
beginsreceivingusertraffic,developerswillbealertedtofailuresasService-Level
Indicators(SLIs)andService-LevelObjectives(SLOs)[JC18]willbegintodegrade,
indicating both increased error rates to the pricing adjustment service, the order
service,andtheAPIgateway.
Atthispoint,thedeploymentwillbeaborted,andthedeploymentversionwill
be rolled back. But, before this can occur, circuit breakers [aut22] on the order
servicewillfireandreconfiguretheservicetoavoidcallingthefailingdependency.
This allows developers toprovidespecial-case errormessagesto upstream callers
andremoves loadonthe failingservice, astherootcausemaybeunclear. Similarly,
had this been related to a feature rollout, this same process would occur when
enabling the feature using a feature flag. In this case, the resilience mechanisms
workasexpected: bugsaremitigatedquicklywithminimalimpactoncustomers.
Requestswereabortedwitherrors,andclean-upoftheincorrectstateisminimal.
10.3 Soft Dependencies
Withmanyindustrialmicroserviceapplicationsissuingover100RPCstohandlea
singlecustomerrequest,developersoftheseapplicationstendtoclassifyservices
intotiers[Atc19]:
• Tier1,
Representingthecriticalservices;

LatentResilienceBugs 121
• Tier2,
Representingessentialbusinessfunctions,and
• Tier3+,
Representingservicesthat,ifunavailable,haveahard-to-noticeimpact.
Forexample,inourpurchaseapplication,onemightclassifytheuserandcart
servicesasTier1: theapplicationcannotcompleteacustomer’spurchasewithout
theseservices. However,onemightclassifythepricingadjustmentserviceandits
dependencies as Tier 2: important, but its failure should not prevent a user from
makingapurchase,asthepurchase’spaymentamountcouldalwaysbeadjusted
later. Therefore,onecan thinkof thepricing adjustment serviceas asoft dependency
oftheorder service. Specifically, should itfail, therequest shouldproceed without
thefailureimpactingthepurchase.
Softdependenciesmaypreventthemitigationofbaddeploymentsbygracefully
degradingfeaturesorusingreasonabledefaultvaluesuponfailure. Todemonstrate,
considerthecasewherethepricingadjustmentserviceisdeployedwithabugthat
causesnullpointerexceptionswheneverthepricingadjustmentservicereceivesan
RPC,andonlywhentheuseriseligibleforapricingadjustment. Whenthenullpointer
exceptionsdooccur,thecustomercanstillmakeapurchase,howeverwillnotreceive
apricingadjustment.
As expected, soft dependency failures may be more difficult to identify after
deployment for several reasons. First, the failure does not cause the SLIs of the
orderserviceandAPIgatewaytochange,asfailuresareswallowed,andcustomer
requestsare processed successfully, albeit without anadjusted price. Second, while
theSLIsforthepricingadjustmentservicewillbeaffected,giventhatonlyasubset
of users will be eligible for a pricing adjustment, this failure may go unnoticed,
unlesssomeoneisactivelyobservingthesemetricsduringdeployment. Still,circuit
breakerswillactivatewith asufficienterrorrate, andoncethe SLIisinvestigated as
part of the deployment, the bad deployment will be rolled back. Cleanup is a bit
morecomplex,assomecustomerswillhaveplacedpurchasesandpaidtheincorrect
price. However,ifametricwasloggedforeacherror,manualremediationcanbe
performedforeach logged error. Every failedRPCreflecteda singlecustomerwho
shouldhavereceivedanadjustment.
10.4 Latent Resilience Bugs
Incontrasttoactiveapplicationbugs,latentresiliencebugs–bugsthatareintroduced
inabaddeploymentbutthatarelateractivatedbythefailureofadependency–can
bemorechallengingtomitigateastheywillnotbedetectedduringdeploymentbut

122 Microservices: DependencyTypeEvolution
atsomelatertime. Whencombinedwithsoftdependencies,theycanbeextremely
difficulttodetectinproductioniffailuresareeitherinfrequentorotherwisehidden
byaservice’serrorbudget.
Forexample,considerthecasewherethepricingadjustmentservicecontainsa
latent bug involvinga downstream dependency. With this latentbug, atimeout is
misconfiguredwithrespecttotheorderservice’stimeout,andthereforewhenthe
pricingadjustmentservice’sdependencyslowsdown,atimeouterrorispropagated
backtotheorderservice. Thiscouldhappenforanynumberofreasonsrelatedtothe
serviceorunderlyinginfrastructure. Giventhatthepricingadjustmentserviceisnot
aharddependency,thecustomer’spurchaseiscompletedwithouttheproperpricing
adjustmentandmustberemediated. However,identifyingwhichpurchasesrequire
remediation may be difficult, as the remediation process must now discriminate
betweenlegitimateandspuriousfailures.
10.5 Takeaways
As described in the background and related work material, one of the limiting
factorsinresearchonmicroserviceapplicationsisaccesstoindustrialapplications.
In fact, as demonstrated in our evaluation of SFIT in practice, this resulted in
several mismatches betweentheSFIT designand how industrial applications are
tested,resultingindifficultiesinapplyingtheapproach. Evenwhenthosedifficulties
were overcome, challenges were still faced related to gaps in the SFIT approach:
SFIT assumes that tests will fail when injecting faults and non-failing tests may
resultinalackofinvestigationoftheimpactoffaults.
To address this, the observations from this industrial evaluation are used in
the co-evolution of the SFIT approach, with Foodly, to derive a new synthetic
examplethatcanbeusedtofurthermicroserviceapplicationresiliencetesting. This
resultedinthedesignofanewapproach,PrincipledService-levelFaultInjectionTesting,
presentedinthenextchapter.

Chapter 11
Principled Service-level Fault Injection
Testing
“Everybody’samadscientist,andlifeistheirlab. We’realltryingtoexperiment
tofindawaytolive,tosolveproblems,tofendoffmadnessandchaos.”
DavidCronenberg
PrincipledService-levelFaultInjectionTesting (p-SFIT)isasoftwaredevelopment
process that extends the SFIT approach for microservice applications that are de-
signed to degrade gracefully under failure. It provides a structured method for
writingstructuredhappypathfunctionaltests–testcasesthatproperlycaptureappli-
cationbehaviorwhentheapplicationcontainsnofaults–and thenupdatingthose
teststoalsoaccountfortheapplication’sbehaviorunderfailure –oncefaultinjectionis
applied.
It does this with a development IDE plugin that visualizes fault injection scenar-
iosandprovidesrecommendationsonaccountingforfailuresintestcode. p-SFIT
forcesdeveloperstomakeexplicittheirapplication’sbehaviorunderfaultandallevi-
atestheburdenofhavingthemthinkabouthowtheirapplicationmaybeimpacted
byRPCfailurebyauto-generatingthefailurescenarios.
Thisinnovationwasnecessary,asSFITleavesseveralquestionsunansweredand
inthehandsofthedevelopertosolve. p-SFITanswersthesequestionsbyproposinga
testingprocessthatextendsSFIT.Thisprocesswasdesignedalongsideanindustrial
microserviceapplicationtoremaingroundedinhowtheseapplicationsbehaveand
aretested.
Regarding writing structured happy path functional tests, two questions remain
unansweredbySFIT.
123

124 PrincipledService-levelFaultInjectionTesting
1. Howcanonewritethesehappypathfunctionaltestsinawaywhere,when
applyingfaultinjection,theyavoidexecutinguninteresting faultscenarios: for
example,wheretheyinjectfailuresinsetup,assertion,orteardowncode?
2. Howdoesoneknowifthesehappypathfunctional tests, whichtheywilluse
asthebasisfortheSFITprocess,arewritteninenoughdetailtocapturelatent
bugsactivatedbythefailureofadownstreamdependency?
Similarly,whenitcomestoupdatingthoseteststoaccountfortheapplication’sbehavior
underfailure,threequestionsremainunansweredbySFIT.
3. With soft dependencies that may not provoke a failure with fault injection,
howdoesoneensurethatadeveloperhasspecifiedandconsidereditsfailure
behavior?
4. How does one make updating existing functional tests to capture failure
behavioreasier?
5. Howdoesoneavoidrequiring developers to encodeeverypossiblecombina-
tionoffailuresintheirtestcode?
To answer (1), the possibility of generating fault injection scenarios that are
notinterestingshouldbeminimizedwhentestingaserviceforitsbehaviorunder
fault. This avoids tests where faults are injected in downstream RPCs executed
aspartofthesetup,tear-down,orassertioncode. Forexample,thetestcodethat
makesapurchaseandtheassertioncodethatverifiesapurchaseinvokethesame
downstreamdependencytolookuptheuser. Inthiscase,onlyinjectingfaultson
thelookupforthepurchase.
To answer (2), tests should also start from a known good place. Tests should
notinvoke downstream dependenciesthat areeithernotstubbed ornotstarted and
return an error. Instead, tests should either start orstub all downstreamdependen-
cies reflecting the “happy path” case where all dependencies return non-failure
responses. Faultinjectionshouldthenbeusedtogeneratetherequiredvariations
ofthetestwherefaultsareinjectedforthoseRPCs.
Similarly,ifdownstreamdependenciesarestubbed,apreciseexpectedinvoca-
tioncountforthatstubshouldbesuppliedunlessthatdependencyisspecifically
indicatedasaread-onlydependencywithoutside-effects. Forexample,amethodto
retrievetheusermaybeinvokedanarbitrarynumberoftimesifitonlyreadsfroma
databaseandreturnstheresponse. Incontrast,adependencythatperformsawrite
operationonadatabaseshouldhaveitsnecessarynumberofinvocationsspecified
precisely. Thisisnecessarytopreventbothunder-invocationandover-invocationin
thecaseofnon-idempotentendpointsthatdonotde-duplicaterequests.

Overviewofp-SFITApproach 125
Toanswer(3),developersshouldbeforcedtoconsidereveryinjectedfaultand
encodethebehaviorofthesystemwhenthosefaultsareinjected. Thisshouldbe
done in a lightweight manner, indicating that the fault has no impact, results in
differentassertionsholding,orresultsintheupstreamcallerreceivinganexception.
This is necessary because existing assertions are often too weak or permissive of
faults. Inshort,withoutexplicitlyencodingthatafaulthasnoimpact,thelackofa
failuremayindicateafalsenegative.
Toanswer (4),thetestinterfaceshould allow for reuseacrossmultiple tests that
test either the same API with different arguments or system configurations (i.e.,
featureflags.) ThisisnecessarywhentheAPIssharecommoncodepaths,where
re-encoding of failure behavior would be redundant. Further, to ease the process of
encoding this failure behavior, developers should be provided with “hints” on how
toencodethefailure. Forexample,supposethefailureofaharddependencyreturns
anexception. Inthatcase,thedevelopershouldbeprovidedwitharecommendation
orcodesnippetthattheycaneasilyusetoconverttheirtesttoencodethatbehavior
underfault.
Toanswer(5),compositionalreasoningwithinaserviceshouldbeusedwherever
possible to avoid redundant encoding of failure behavior under combinations of
faultsinthesametestexecution. Forexample,supposethedeveloperindicates,in
isolation,thatafailureofRPC1hasnoimpactonthetestoutcomeandthatafailure
of RPC 2 causes the system to throw an exception. In that case, the tool should
attempt to check that the simultaneous failure of RPC 1 and 2 causes the system
tothrow anexception, withoutrequiring thatthedeveloperexplicitlyencode this.
Furthermore, the developer should only be required to encode behavior where the
application behavior is ambiguous. For example, when the failure of RPC 1 and
RPC2eachhavebeenindependentlyspecifiedwithtwodifferentsetsofassertions.
11.1 Overview of -SFIT Approach
p
To realize these requirements, a testing process that integrates with the existing
testing procedure of SFIT is presented. The testing process is composed of both
developer actions(in italics), actions performed by p-SFIT (in bold), and actions
performedbySFIT(innormal).
Whendevelopersare writingstructuredhappy paths functionaltests, theprocess is
asfollows:
1. Executethetestwithoutfaultinjection.
Oncethetestispassing:
a) Failthetestifanyinvokeddependenciesreturnanon-successresponse.

126 PrincipledService-levelFaultInjectionTesting
i. UpdatetesttostubRPCwithresponse.
ii. GotoStep1.
b) Failthe testif any stubbed dependenciesdo not explicitly indicate a
preciseinvocationcount.
i. Updatestubtoindicateexpectedinvocationcount. p-SFITwillnotaccept
useofimprecisecounts: “any#oftimes”or“atleastonce.”
ii. GotoStep1.
When developers are updating their happy path functional test to account for the
application’sbehaviorunderfault,theprocessisasfollows:
2. ExecutefaultinjectionscenariofromSFIT.
Didthedeveloperencodeapplicationbehaviorunderfaultfortheinjected
faults?
a) Ifnot, fail thetestfor unspecified behaviorandproviderecommenda-
tionsonupdating thetesttoencodethe application’s behaviorunder
faultbasedontheobservedbehavior.
i. Update test to encode the application’s behavior under fault. Figure 6.1
providesanexampleofthisinSFIT.
ii. GotoStep1.
b) Ifso,checkthatapplicationbehaviormatchesthedeveloper-specified
behavior.
If false, ask the developer to investigate a possible application bug
andproviderecommendationsonencodingtheobservedapplication
behaviorunderfaultintothetest.
i. Ifabug,resolve.
ii. Ifnotbug,encodeapplication’sbehaviorunderfaultusingrecommendations.
iii. Goto1.
3. Ifmorefaultinjectionscenariosremain,goto2onlyifthecurrenttestexecu-
tion passed based onthe developer specifications of application behavior
underfault.
p-SFITdiffersfromSFITinthat,ratherthanrunningallpossiblefaultinjection
scenarios immediately and showing all fault injection executions and how they
failed, p-SFIT only executes fault injection scenarios until it encounters the first
test failure. The developer is then prompted to update the test to account for the
application’sfailurebehaviorbeforeproceeding,refiningthatbehaviorovertime

Componentsofp-SFIT 127
as new fault injection scenarios are introduced and avoiding the scenario where
developers encodebehavior that may be derived throughcompositional reasoning
forexample,iftheyweretostartwiththelastfaultinjectionscenario,whichcontains
themostsignificantnumberofsimultaneousfaults.
Thep-SFITtestingprocess,justlikeSFIT,alwaysre-executesboththehappypath
executionandallfaultscenarioexecutionseachtimeitisrun. Thisisdonebecause
thedevelopermayhaveinadvertentlymadeachangetoeitherthecode(toresolve
an identified bug) or the test (during the process of updating the test to capture
theapplication’sbehaviorunderfault)thatcauseseitherapreviouslypassingfault
scenario(orthehappypathexecution)tofail.
11.2 Components of -SFIT
p
Our design comprises four major components to meet these requirements and
realizeourtestingprocedure.
1. a test interface that improves on both the writing of happy path functional tests
andupdatingthoseteststoaccountfortheapplication’sbehaviorunderfault:
a) avoiding thegenerationof “non-interesting”failure casesresulting from
RPCsexecutedintestsetup,assertion,andtear-downcode;
b) maximizingreuseoffailurespecifications;and
c) warnsontheunder-encodingofdependencyfailure.
2. anAPIforupdatinghappypathfunctionalteststoaccountforapplicationbehavior
under fault that supports precise failure specification for all possible failure
scenariosofbothhardandsoftdependencies. ThisAPIisthenmechanically
checkedbyp-SFITtoensurethatallinjected(single)faultshaveacorrespond-
ingcoveringspecification;
3. analgorithmforcompositionalreasoningwithinaservice. Thisalgorithmallows
fortheencodingoffailurespecificationundersinglefaultsandtheautomatic
checking of failure scenarios under simultaneous faults when the desired
behaviorisunambiguousand
4. anIntelliJIDEpluginthatvisuallydepicts:
a) testexecutionsandtheRPCsthattheyexecutetodownstreamdependen-
cies;

128 PrincipledService-levelFaultInjectionTesting
b) the specific RPCs where SFIT fault injections have been performed in
eachexecution;and
c) code snippets and recommendations with integrated JavaDoc on how to
encode failure behavior for a test failure, based on the precise injected
fault,forusewhenthatbehaviorisdesiredunderfault.
Thesefourcomponentsaredescribedinthefollowingsections.
However, before describing these four
Transitive Service Encapsulation Testing.
different components, it is important to note that a complimentary algorithm to
ESR was designed during the development of p-SFIT that is compatible with the
componenttestingstyle.
Inthisalgorithm,theresultsfromcomprehensivelytestingaserviceforfailures
toitsdownstreamserviceswouldproduceafaultinjectionconfigurationthatwas
basedontheobservedresponsesreturnedfromtheservice-under-test(sayService
𝐵). Thisconfigurationcouldthenbeusedfortestingadifferentservicethattookthe
testedserviceasadependency,inordertoavoidexhaustivetestingofthatservice
(sayService𝐴,whichcallsService𝐵)directly.
Thisobviatestheneedforastaticanalysis,howeveronlyundertheassumption
that testing all terminal nodes in a graph exhaustively yield all possible error re-
sponses that those services can return. Thus, any upstream service must only be
testedforthosefaults(plusastandardsetoftimeoutandnetworkingfailures)using
a depth-first searchof the microservice graph,recursivelyas the graphis traversed.
Inessence, thisleveragestheserviceencapsulationproperty, compositionally,by
only synthesizingnecessary tests; this isin directcontrastto ESR whichperforms
thereductionofredundanttestcasesbasedonobservationofservicebehavior.
As an example, consider the Audible example presented in Figure 3.1. By ex-
haustivelytestingAudibleDownloadServiceforfailuresofallofit’sdownstream
dependencies, andthen usingthe informationlearned fromtheAudible Download
Service’s responses to it’s upstream service when faults are injected, the Content
DeliveryServiceneedonlybetestedforthefailurescanbeactuallyreturned returned
by theAudibleDownloadService,it’sdownstream. Thiscorrespondstotheresults
presentedinChapter10.
WhileitcanbeshownthatthisnewalgorithmisequivalenttotheESRalgorithm
intermsofthenumberoftestsrequiredforexhaustivesearch1,itsdiscussionomit-
tedfromthisdissertation. Thisisbecausethedecentralizednatureofmicroservice
application development, the independent development cadences of individual
services,andrequiredinfrastructureforsharingthisinformationacrossdifferent
1ImplementedintheFilibusterprototypeintheopen-sourceimplementation.

Componentsofp-SFIT 129
repositoriesanddifferentteams,allmakeitmoreoperationallychallenging(inthe-
ory, but not evaluated) than just running the additional fault injection experiments
required for exhaustive search of all error code during testing. Similarly, it was
observedthattherewaslittleinterestinthisfeaturefromapplicationdevelopers,
oncebuilt,whileconsiderednovel.
11.2.1 Structured Test Interface
Toensurestructuredhappypathfunctionaltests,aninterfacewhereexplicitblocks
areusedtodelineatethestagesofthetestinglifecycleisproposed.
Toaddress1(a),explicitblocksareproposedforeachstageoftesting(e.g.,setup,
assertions, tear down) to know precisely when fault injection should be used to
avoidinjectingfaultswhensettingupthetestorperformingassertionsthathappen
tousetheAPIsthatareundertest.
Toaddress1(b),eachblockwillsupport abstractionviainheritance,allowing
developerstoquicklycreatetestvariantsthatchangetheRPCmethod’sarguments
andslightlyaugmenttheassertionsunderfault-freeorfaultyexecutions.
This is necessary for two reasons: shared code paths and feature flag-based
variations. WithsharedcodepathsmanyRPCmethodsshareacommoncodepath
whenhandlingrequeststhatperformrequestvalidationandretrieverequiredinfor-
mationfromdownstreamdependenciesusingRPCs,forexample,theuser’sdata.
Withvariationsbasedonfeatureflags, manytestsare variantsof thesametestwith
eitherthesameorslightlydifferentassertions. Forexample,testinganexperiment
(i.e., A/B test) that invokes the same RPC method with the same arguments and
performsthesameassertionsunderadifferentconfiguration.
Toaddress1(c),thedeveloperwillberequiredtostubanyinvokedRPCmethod
and indicate precisely the number of times that the RPC method will be invoked
ifthatdependencyisnoteithermarkedasread-onlyornotstartedasanexternal
service. Thispreventsthedeveloperfromwritingtestswheredependenciesfailin
the“happypath”without knowinghowmany timestheywillbe invoked. These
indications of desired invocations count will then automatically be adjusted (i.e.,
required invocation calculate one automatically is converted to 0 when a fault
is injected on that specific stubbed RPC.) when faults are injected to avoid the
developerhavingtoperformthatadjustmentmanuallyasrequiredinSFIT.
11.2.2 Behavior-Under-Fault Encoding API
p-SFITrequires thatdeveloperstatethe behavior oftheir applicationunder allRPC
failurestoavoidassumptionsaroundhowanapplication’sbehaviorchangesunder
failure. Therefore, when updating tests to account for the application’s behavior

130 PrincipledService-levelFaultInjectionTesting
under fault, p-SFIT should allow the developer to do this for both hard and soft
dependencies,andatincreasinglevelsofprecision(e.g.,fromanyfaultforaspecific
RPCtoaparticularfaultforaspecificRPCwithspecificarguments),asnecessary
bythep-SFITtestingprocess.
When it comes to hard dependencies, where a fault causes the API to return an
error, thedeveloper mustindicate so. This ensuresthat anyinstances oferror sup-
pression, whereerrors are re-writtenbefore beingreturned, are explicitlyencoded
inthetest. Thisforcesthedevelopertoenumeratetheexceptionsreturnedtothe
upstreamonfault. Similarly,forany faultpropagateddirectlybacktotheupstream
without any suppression (i.e., unhandled exception), the developer must indicate
thisbehaviorisdesired. Thisisthenverifiedbyp-SFITbyensuringthatwhenafault
isinjected,itsurfacesasanerrorinthetest,thusavoidingcaseswhererefactored
codeinadvertentlyintroducessuppression.
Inthesecases,thedeveloperalsowillbeforcedtoreasserthowmanytimesany
subsequent downstream dependencies will be invoked by indicating whether they are
read-only,where theymayormaynothappen when that errorisreturned,or side-
effecting, where they must(not) happen under any error returned to the upstream.
Thisexplicitdesignistoautomaticallyidentifytwodifferenttypesofbugs: partially
appliedsideeffectsoralackofrequiredsideeffects. Fortheformer,identifythecase
whereanerrorisreturnedtotheuser,butsomesideeffectshavebeenperformed.
Forthelatter,identifyingthecasewheresuccessisreturnedtotheuserbutsome
side-effectshavenotbeenperformedbecauseofafault.
Foreachreturnederror,developersmustthenencodetheassertionsthatshould
hold regardless of the fault that resulted in that error: for example, in the case
wheretwodifferenterrorsresultinaservicethrowingagRPCexceptionwithstatus
codeNOT_FOUND. Thisisdonebothtoensurethatthesystemstateisconsistentfor
anyfaultsthatcausethesameexceptiontobethrownandalsotoensurethatside-
effectsareexplicitlyindicatedforeachexception. Thisavoidssituationswherethe
sameexceptionisthrown,butthesystemisleftindifferentstates,withside-effects
partially applied (or worse, unapplied), making it easier for the upstream, who
receivedtheexception,toknowwhetheritshouldretrytherequest.
Regardingsoft dependencies— dependenciesthat, upon failure, donot causethe
upstreamtoreceiveanexception—thedevelopermustindicatewhetherthetest’s
existing assertions continue to hold or provide different assertions. This ensures
thatdevelopersthinkabouttheimpactoffailuresbyforcingatestfailure.
11.2.3 Compositional Reasoning
Whilethedevelopershouldindicatethebehavioroftheirapplicationunderfault,
requiring that they encode the precisebehavior under all possible combinations of

Componentsofp-SFIT 131
faultsisimpractical. Therefore,someabilityforcompositionalreasoningisrequired
tokeepthetestingprocesstractableandminimizethehumancost.
The key observationthat enablescompositional reasoningis the following. First,
asdescribed,RPCfailurescanhaveeithernoimpactifasoftdependency,resultin
differentsystemassertionsholdingif asoftdependency,or thrownexceptionsin
thecaseofharddependency. Thecombinatorialexplosioninherenttothisstyleof
testingoccurswhensoftdependenciesarefailedsimultaneouslytogether. Therefore,
ourkeyinsight inreducingoverheadinencodingfailurebehavioristhefollowing:
anySFIT-generatedfaultinjectionexecutionsthatcontainmultiplefaults,whereatleastone
ofthosefailures hasno impact, shouldbe observationallyequivalent to theSFIT-generated
faultinjectionexecutionthatdoesnotcontainthefaultsthathavenoimpact.
Inshort,iftwoRPCsfailinthesameexecution,thatwhentestedindividuallyin
separateexecutionsdidnotcauseassertionfailures,andtheirsimultaneousfailure
should also not cause assertion failures. However, this may not be generally true
for all microservice applications, as developers cite code conditional on whether
ornottwofail,ituresoccurredinthesameexecution,hencethattheyonlymaybe
observationallyequivalent. Therefore,ratherthanskippingthetestexecution,p-SFIT
executes the test assuming that the test outcome will be observationally equivalent;
if this isn’t true, the test will fail assertions normally and the developer will be
prompted to encode the behavior for this combination of faults. In practice, this
manifestsitselfinseveraldifferentways.
To demonstrate, consider the most straightforward case: RPCs that result in
thrownexceptionsoraparticularsetofassertionsholdingwhenafaultisinjected
combinedwithotherRPCsthathavenoeffectunderfailureinthesameexecution.
Inthiscase,p-SFITwillassumethatthesameexceptionswillbethrownorthesame
set of assertions will hold under any of these combinations and explicitly test them
forthisbehavior. Inthecasethatthetestfails,thedeveloperwillthenbeprompted
byp-SFITtoexplicitlyencodethefailurebehaviorforthiscombinationoffaults.
Inmorecomplicatedcases,RPCsthatresultinthrownexceptionsoraparticular
setofassertionsholdingwhenafaultisinjectedarecombinedwithotherRPCsthat
result in thrown exceptions or a particular set of assertions holding when a fault
is injected. In these cases, the system cannot determine which exception will be
thrown orwhat assertions willbe true atthe endof theexecution. Therefore, the
developerwill thenbepromptedby p-SFITtoexplicitlyencodethe failurebehavior
forthiscombinationoffaults.
Inallcases,p-SFITalwaysexecutesthetestandverifiestheoutcome: therefore,
notestcasereductionisperformed,butinsteaditispreferredtoavoidburdening
thedeveloperwithwritingtheadditional,redundantassertionsifpossible.

132 PrincipledService-levelFaultInjectionTesting
11.2.4 IDE Plugin
In order to assist application developers in debugging failed tests and encoding
failure behavior, an IntelliJ plugin was developed where the p-SFIT process is vi-
sualized: every test generated, each RPCinvoked by eachtest,and the locationof
everyinjectedfault. Thispluginalsoprovidesrecommendationsonhowtoresolve
failingtestsbasedonboththeinjectedfaultandthesurfacedfailure.
11.3 Implementation
p-SFIT is implemented directly into the Java Filibuster prototype [Mei24e] and
provided as an open source IntelliJ IDE plugin [Mei24d], both available as open
source.
The design of p-SFIT is realized as a Java interface that each JUnit component
test will implement: FilibusterGrpcTest. This interface requires that each test
implements several abstract methods, each corresponding to one of the blocks
representingastageinthetestingprocedurerunbyp-SFIT.
Executedinthisspecificorder,thereisablockforeachofthefollowingstagesof
thetestingprocedure.
1. setupBlock
Testsetup;
2. stubBlock
Stubbingofdownstreamdependencies;
3. executeTestBlock
ExecutionoftheserviceRPCmethodthatisundertest;
4. assertTestBlock
AssertionsontheresponseoftheRPCmethodthatisinvokedinthetestblock;
5. assertStubBlock
Assertionsontheinvocationcountofinstalledstubsand
6. teardownBlock
Testtear-down.
Finally,thereisafailureblock(failureBlock)thatcanbeusedforplacingthe
assertions on failure behavior, which is executed before the test. The placement
of assertions in this block is superficial: it is merely a location to encode failure
behaviorthatisseparatefromthemaintestcode.

Implementation 133
AsanalternativetousingtheFilibustersuppliedsetupandtear-downblocks,de-
velopersmayalsouseeithertheJUnitsupported@BeforeAll,@BeforeEach,@AfterEach,
and@AfterAllblocks: faultinjectionwillautomaticallybeinhibitedforanyRPCs
executedinsideoftheseblocks. p-SFITalsoprovidesaspecificblocktypethatcan
beusedinanytestthatinhibitsfaultinjectionforcodeplacedwithinitthatcanbe
placedinanyblock. Similarly,p-SFITalsoprovidesanexplicitblocktypethatcan
be used for bracketing different sets of RPCs together. This is done only for ease
of debugging tests using the associated IDE plugin, as it has no impact on fault
injection.
When any of these blocks are used, p-SFIT automatically brackets any RPCs
initsIDEplugintoindicatewhichblockanyRPCsexecutedinthoseblockswere
executedfrom.
11.3.1 Failure Specification API
In Table 11.1, the API that can be used in the failure block for encoding behavior
of the service under failure is presented. In the Java Filibuster implementation,
thisAPIisdesignedspecificallyforthetestingofgRPCendpoints. Thereforeitis
assumed that all thrown exceptions are of type StatusRuntimeException and are
instantiatedbybothgRPCcodeanddescription.
Fortheassertionsonaninjectedfault,suchasassertFaultThrows,assertOnFault
andassertFaultHasNoImpact,fourvariantsexist: bymethod,bymethodanderror
code;bymethodandrequest;andbymethod,requestanderrorcode. Forthestub
invocationmethods,readOnlyRPCandsideEffectingRPC,theyaresyntacticsugar
ontopoftheexistingatLeast(0)andtimes(N)APIs,respectively. Thisisdoneto
forcethedeveloperstothink abouttheimplicationsofstatingthatanRPCcanbe
invokedanarbitrarynumberoftimes.
Shouldmultiple faults beinjected simultaneouslyin atest iteration,Filibuster
provides the builder CompositeFaultSpecification, which test authors can use
to state the combination of the failing RPC requests. Test authors can use that
CompositeFaultSpecification object as a parameter in assertFaultThrows and
assertOnFaulttoasserttheirapplication’sbehaviorwhenmultipleRPCssimulta-
neouslyfail.
11.3.2 Fault Matching API
Developersshouldalsobeabletoencodefaultsatwhatevergranularitytheychoose.
Forexample,wheninjectingafaultonRPC1withstatuscodeUNAVAILABLE,thedevel-
opermightuseassertFaultThrowswitharguments(RPC1, UNAVAILABLE, NOT_FOUND)
toindicatethattheservicethrowsanexceptionwithstatuscodeNOT_FOUNDwhen

134 PrincipledService-levelFaultInjectionTesting
API Description
(UsageBlock)
stubFor Stubdownstreamdependencywithresponse
(stubBlock)
verityThat CheckthatstubbeddependencyisinvokedNtimes
(assertStubBlock)
assertOnException Assertionsforthrownexceptiononharddependency
(failureBlock)
assertOnFault AssertionsonRPCfailureforhard&softdependency
(failureBlock)
assertFaultThrows RPCfailureofharddependencyresultsinexception
(failureBlock)
assertFaultPropagates RPCfailureofharddependencyasunhandled
(failureBlock)
assertFaultHasNoImpact RPCfailureofsoftdependencyhasnoimpact
(failureBlock)
MarkRPCtosoftdependencyasread-only
readOnlyRPC
Maybecalled0ormoretimes
(assertOnException)
MarkRPCtosoftdependencyasside-effecting
sideEffectingRPC
Needsexplicitinvocationcounts
(assertOnException)
Table11.1: Tableofp-SFIT-enabledFilibusterassertionAPIandusageblocksforeachAPI
method.
RPC1throwsanexceptionwithstatuscodeUNAVAILABLE. Thedevelopercouldalter-
nativelyencodeassertFaultThrowswitharguments(RPC1, NOT_FOUND)toindicate
thattheservicethrowsanexceptionwithcodeNOT_FOUNDwhenRPC1throwsan
exceptionwithany statuscode. Eitheriscorrect,buttheirknowledgeoftheservice
mayinfluencethedeveloper’schoice.
When Filibuster generatesasubsequenttestthatinjectsafaultonRPC1with
status code DEADLINE_EXCEEDED, the service throws the same exception with the
samestatuscodeasaresultofthatfaultinjection. Atthispoint,thedeveloperinthe
former case may either write an additional assertion for the new failure or refine
theirtesttoindicatethatanystatuscodecausestheexceptiontobethrown,asfirst
doneinthelattercase.

Implementation 135
To facilitate this matching approach, a method was necessary to characterize
eachsystemfault. ThismethodwouldenableSFITtogeneratesortableprojections
ofeachfault, organizedindescending orderbasedonthespecificity oftheirfault
representation. ThisensuredthatSFITcouldmatchthefaultbehaviorspecifiedby
theuserbasedontheirintention.
Inspired by the distributed execution indexing algorithm, each fault is repre-
sented by the RPC’s signature where the fault was injected, the RPC’s request
arguments, and the description of the fault injected for that RPC. When match-
ing, SFIT first look for a matching use of one of the API functions by signature,
arguments, and injected fault. When no match is found, SFIT then decreases the
precision,firsttothesignatureandarguments,thentothesignatureandcode,and
thentothesignaturealone.
Thisseemstomatchthedeveloper’sintentwiththeAPI:
1. First,themostprecisematchshouldbesearched: thesignature,arguments,
andcode.
2. Next,anyencodingsthatuseanexplicitrequestshouldbematched,asthey
indicatemultipleRPCstothesamemethodexistinthesameexecution,and
failuresofeachmaybetreateddifferentlyatdifferentcallsites.
3. Third,thesignatureandstatuscode,asallfailuresofthesametypearemost
likelytreateduniformlyforasinglerequest.
4. Finally, the developer may have just treated all failures for an RPC method
uniformly.
11.3.3 IDE Plugin
Tofacilitateapplicationdevelopersinthediagnosticassessmentoffailedtestsand
encodingfailurebehavior,Filibuster isprovidedwithanIntelliJIDEplugin. This
plugin visualizes each test run generated and executed by p-SFIT, every RPC to
a downstream dependency within a specific test along with its arguments and
response,andeachinjectedfaultintheirrespectiveinvocationsequences.
Figure11.1showsascreenshotoftheplugin. Foreachofthe4RPCsissuedin
thereferenceexecution,Filibuster injectsStatusRuntimeExceptionwiththestatus
codeDEADLINE_EXCEEDEDandUNAVAILABLE. Thisresultsin8executionswithinjected
faults(4RPCs*2faults). InFigure11.2aniterationwhereStatusRuntimeException
withthecodeDEADLINE_EXCEEDEDwasinjectedintheRPCto(UpdateCart)isshown.
Thepluginprovidesrecommendationstothedeveloperbasedonthetestfailures
thatFilibusteridentifies. Theserecommendationsguidethedeveloper: forexample,

136 PrincipledService-levelFaultInjectionTesting
Figure11.1:
FilibusterIntelliJpluginvisualizestheinterceptedRPCinvocationsandtheirargumentsandresponses.

Implementation 137
.traCetadpUotnoitacovniCPRehtnidetcejnisinoitpecxEemitnuRsutatSaerehwnoitaretiretsubiliF
:2.11erugiF

138 PrincipledService-levelFaultInjectionTesting
ifatestfailsbecauseafaultwasinjectedandthedeveloperdidnotencodethebe-
haviorunderfault. ForeveryexceptionthatFilibusterGrpcTestthrows,Filibuster
hasa defineddiagnosticmessagethattheplugin shows. That message describes
whytheexceptionwasthrownandprovideslinkstothe preciseAPImethodsthat
developers need to use to resolve the issue. That includes errors for hard depen-
dencies, assertion failures for softdependencies, and missing stub invocations for
under-specified dependencies. The plugin also provides an overview of the API
coverageoftheserviceundertest,promptingdeveloperstoincreasecoveragewhere
necessary.
Anecdotally,theauthoridentifiedthatintheprocessofwritingtestsusingthis
design,havingavisualdepictionofthefailurewithrecommendationsonhowtofix
wasextremelyvaluable. AnerrorandrecommendationsgeneratedbytheFilibuster
pluginisshowninFigure11.3andFigure11.4.
Fortheimplementation,theIntelliJIDEpluginisawebviewthatrendersinfor-
mationthatiswrittentothefilesystem,bytheFilibusterimplementation. Therefore,
noactuallogiclivesintheplugincodeitself. Thiswasdonetoenablethedevelop-
mentofpluginsforotherIDE’s,suchasVisualStudioCode.
11.3.4 -SFIT Testing Procedure
p
Thep-SFITtestingprocedureisdepictedinFigure11.5.
1. setupBlock
Testauthorsshouldputcode for thesetupofthetestinthisblock. Theuseof
thisblockinhibitsfaultinjectionforanyRPCsissuedinit. Forexample,ifusing
theservice-under-test’sAPItostagestateforrunningatest,anydownstream
dependenciesthatareinvokedaspartoftheexecutionofthesetupblockwill
notbetestedforfaults. Thereby,thisensuresthatfaultsdonotpreventproper
stagingbeforetheexecutionoftheactualtest.
2. stubBlock
Thisblockcontainscodeforstubbinganydownstreamdependenciesthatneed
tobestubbedforthetesttopass. Stubbingofthesedependenciesshouldonly
be performed using the Filibuster-provided stubFor method as Filibuster
needstointerposeonthesemocksforfaultinjectiontesting.
3. executeTestBlock
The test execution code should be placed in this block. Any downstream
RPCsthatareinvokedasaresultofamethodinvocationinsideofthisblock
will be subject to fault injection. Test authors should store any responses
that are required for assertions, placed in the assertTestBlock, in instance

Implementation 139
tsetehT
.resUteGniELBALIAVANUedocehthtiwnoitpecxEemitnuRsutatSadetcejniretsubiliFerehw,noitaretI
:3.11erugiF
gnidragersnoitadnemmocerswohsnigulpretsubiliFehT
.tluafsihtrofdenfiedtonsiroivahebnoitacilppaehtecnissliaf
.roivahebnoitacilppaehtenfiedotdesuebnactahtsdohtemIPA

140 PrincipledService-levelFaultInjectionTesting
oftherespectivemethodinFilibuster’sAPI. Figure11.4:
Popupthatappearswhenoneoftherecommendationsisclicked.
Thepopupshowsthedocumentationpage

Implementation 141
ro noitucexe
.fer sI
?sworhT
etucexE
?tcapmIoNevaHstluaf
?sworhT
?noitucexe
.fer
sI
kcolBtseTtressa
seY
n w o o it r p h e te cx R e seY
seY
worhT
oN
deliaFkcolBtseTtressA
oN
lanoitisopmoC si noitacifirev ?denifed
oN
? 1 tl u > a s f t c C e P jn R IoN
seY
?tluaf
elgnis
s o t N cejnI
oN
? s h e d Y c n ta a m s e s d n o o c it p ro ir r c r s E ed
seY swo ? rh d T e t n lu if a e F d t r s e i ssa se oN taga ? p d o e r n P if t e lu d a F si tressa
?s s w eY orhT
seY
si tluaFnOtressa ?denifed
seY
oN
wo se rh Y T
si tlu ? a d F e n n O ife tr d essa
seY
seY
tlua
e F tu n c O e t x re E ssa
oN
wo o r N hT
-n o w - i s t o p a r e h H c T xE n -s - o r u i - o w t o w a r u o r g o E g r a r h d h i p b T T n o m A r A P swo ? rh d s T e eY t n lu if a e F d t r s e i ssa
sey
detcejnIstluaFelpitluM
oN
?sworhT
-erulia g F n w i s o ld u r n h o a T u H gibmA
CPRdeliaF
-d r e - o e if iv i r c u a e l h i p a e s F B nU
oN
oN
oN
-tressA r w o o F r s h n T oitressA
-saHt l w ua o F rh d T etcejnI
oN
seY
deliaFnoitpecxEnO
-eruliaFdeificepsnU roivaheB
?sworhT
seY
noitp
e e c t x u E ce n x O E tressa
tlua
F w n o O rh tr T essA
snoitressA
mrofreP
assertOnException
is defined?
puteS
sbutS
ddA
?sworhT
etucexE
worhT
kcolBbutStressa
-gnissiM oN -noitressA -sutatSroF
worhT
edoC
oN
snoitressAoNsaHCPRdebbutS ylno liaf sCPR fo esuaceb
oN
?stluaf detcejni
tahTyfirev
seY
dellac
si
lla no ?sbuts
seY
oN
seY
seY
worhT -CPRdekovnI detnemelpminU
seY
dna sedoc rorrE ?hctam snoitpircsed
oN
-dloHtoN
w d o iD rh s T noitressA
oN
edoCsut a w tS or d h e T sserppuS
esnopseRrorrErednU
snoitacovnI
buts yfireV
tseT
etucexE
nwodraeT
.TIFS-proferudecorpgnitseT
:5.11erugiF

142 PrincipledService-levelFaultInjectionTesting
variables. Filibuster executes the test code written in this block. If the test
is successful and no exceptions are thrown, Filibuster proceeds to the next
block. Otherwise,shouldthetestthrowanexceptionbecauseofafailingRPC
invocation(referredtohereas𝑅 ),Filibusterdistinguishesbetweentwocases:
𝑓
a) Ifthecurrentexecutionistheinitialreferenceexecutionwherenofaults
areinjected,Filibuster rethrowstheexceptionandfailthe testiteration.
Filibuster showstheexceptiondetailsintheIDEplugin.
b) Otherwiseifafaultwasinjectedinthecurrentiteration,Filibusterbegins
by verifyingthattheauthorshaveproperlyspecified thefailurebehavior
of the application under fault in the test for a hard dependency. This
processisdescribedbelowinSection11.3.4.1.
4. assertTestBlock
Testauthorsshouldplacetestassertionshere. Theuseofthisblockinhibits
fault injection, which is necessary when using the very API under test to
performassertions. For example,if atestinvolves querying auser database
to initiate a subscription and subsequently querying again to confirm the
subscription,itisessentialtointroduceafaultsolelyduringthesubscription
phase’suserqueryandnotduringtheverificationphase.
In this block, Filibuster checks whether the current execution is the initial
reference execution or whether the faults injected in the current execution
havenoimpact. Ifeitheristhecase,Filibuster executestheassertionsdefined
by the test author in the assertTestBlock. If they are successful, Filibuster
proceedstothenextblock. Otherwise,iftheyfail,Filibustercheckshowmany
faultswereinjected.
a) If more than 1 fault was injected, Filibuster throws FilibusterGrpc_
⌋
MultipleFaultsInjectedException.
b) Otherwise,Filibuster throwsFilibusterGrpcAssertTestBlockFailed_
⌋
Exception.
Otherwise, if the current execution is not the reference execution and the
injected faults have an impact, Filibuster executes the subprocedure associ-
ated with soft dependency failure. This process is described below in Sec-
tion11.3.4.2.
5. assertStubBlock
Usethisblockforperformingassertionsonstubinvocations. Thisshouldbe
done using the Filibuster-provided verifyThat method, as Filibuster must

Implementation 143
interpose on thesecalls to automatically adjust theexpected invocation count
whenfaultsareinjected.
a) First, the assertions in the stub block are executed. Should they fail,
FilibusterGrpcAssertionsDidNotHoldUnder_ErrorResponseExceptionis
thrown.
b) Second,FilibustercheckswhetherallRPCsthatfailedhadinjectedfaults.
If that is not the case, this indicates that some invoked RPCs were left
unimplemented. Thus,Filibuster throwsFilibusterGrpcInvokedRPC_
⌋
UnimplementedException.
c) Third,Filibuster checkswhetherverifyThatwascalledonallstubbed
methods. If that is not the case, Filibuster fails the test and throws
FilibusterGrpcStubbedRPCHasNoAssertions_Exception. Otherwiseifsuc-
cessful,Filibuster proceedstothenextblock.
6. teardownBlock
Testauthorsshouldusethisblockforperformingtesttear-down. Similarto
thesetupBlock,faultinjectionisinhibitedforanydownstreamdependencies
thatareinvokedaspartofanymethodinthisblock.
11.3.4.1 HardDependencySubprocedure
Thissubprocedureisexecuteduponharddependencyfailure, duetoafaultinjec-
tion,intheexecuteTestBlockblock,whenthetestthrowsanunhandledexception
receivedbytheapplication.
1. First,Filibusterstartsbycheckingwhetherthetestauthorshaveindicatedthat
thefailureof𝑅 shouldpropagateupstream(usingassertFaultPropagates).
𝑓
a) If that is the case, Filibuster perform a sanity check whether the test
authors have simultaneously defined an exception-throwing behavior
for 𝑅 (using assertFaultThrows). Defining both assertFaultThrows
𝑓
and assertFaultPropagates for 𝑅 indicates ambiguous failure behav-
𝑓
ior. Iftrue,FilibusterthrowsFilibusterGrpcAmbiguousThrowAndError_
⌋
PropagationException.
2. If the sanity check is successful and only assertFaultPropagates is defined
for𝑅 ,Filibuster proceedstocheckwhetherthestatuscodeanddescription
𝑓
ofthepropagatedfaultmatchthecodeanddescriptionoftheinjectedfault.

144 PrincipledService-levelFaultInjectionTesting
a) Iftheydonotmatch,FilibusterthrowsFilibusterGrpcSuppressedStatus_
⌋
CodeException.
b) If the status code and description match, Filibuster proceeds to check
whethertestauthorshavedefinedassertionsfortheexception-throwing
behaviourof𝑅 (usingassertOnException). Ifthatisthecase,Filibuster
𝑓
proceeds tothe nextblock. Otherwise,Filibuster throws Filibuster_
⌋
GrpcMissingAssertionForStatusCodeException.
3. If test authors have not indicated that failure of 𝑅 propagates upstream,
𝑓
Filibusterchecksiftheyinsteaddefinedthatfailureof𝑅 resultsintheservice
𝑓
returninganexception(usingassertFaultThrows).
a) In case assertFaultThrows was not defined, this indicates unspecified
failure behavior for 𝑅 and Filibuster throws FilibusterGrpcThrown_
𝑓 ⌋
ExceptionHasUnspecifiedFailureBehaviorException.
b) Ifthatisnotthecase,FilibusterthrowsFilibusterGrpcFailedRPCException.
4. Otherwise, Filibuster checks whether test authors have defined assertions for
theexception-throwingbehaviourof𝑅 (usingassertOnException).
𝑓
a) Ifthatisthecase,Filibuster proceedstothenextblock.
b) Otherwise,FilibusterthrowsFilibusterGrpcMissingAssertionForStatus_
⌋
CodeException.
11.3.4.2 SoftDependencySubprocedure
Thissubprocedureisexecuteduponsoftdependencyfailure,duetoafaultinjection,
intheassertTestBlockblock.
1. First,Filibuster proceedstocheckwhethertestauthorshavedefinedalterna-
tive assertions that apply when a fault is injected (using assertOnFault). If
thatisthecase,Filibuster executestheseassertions.
a) Shouldtheyfail,FilibusterthrowsFilibusterGrpcAssertOnFaultException.
b) Otherwise, if they aresuccessful, Filibuster executes the assertionsde-
fined in assertOnException. If the assertions fail, Filibuster throws
FilibusterGrpcAssertionsForAssertOn_ExceptionFailedException. Oth-
erwiseifsuccessful,Filibuster proceedstothenextblock.

Takeaways 145
2. IftestauthorshavenotdefinedalternativeassertionsinassertOnFault,Fili-
buster differentiatesbetweentwocases:
a) If Filibuster is injecting a single fault, the lack of assertOnFault indi-
catesthereisnospecificationoffailurebehavior. Thus,Filibuster throws
FilibusterGrpcInjectedFaultHasUnspecifiedFailureBehavior_Exception.
b) If more than one fault is being injected, Filibuster checks if composi-
tional reasoning potentially defines the fault behavior. If that is the
case, Filibuster proceeds to the next block. Otherwise, Filibuster throws
FilibusterGrpcAmbiguousFailureHandlingException.
11.4 Takeaways
PrincipledService-levelFaultInjectionTesting (p-SFIT)improvesonSFITbyproviding
astructured,developer-centricmethodologyforresiliencetesting.
Morespecifically,p-SFITisasoftwaredevelopmentprocessthatextendstheSFIT
approach for applications that are designed to gracefully degrade under failure,
as observed in our industrial evaluation with Foodly. It improves the process of
bothwritingstructuredhappypathfunctionaltestsandthenupdatingthoseteststoalso
accountfortheapplication’sbehaviorunderfailure. ThroughtheapplicationofSFITto
an industrial application, requirements were derived based on observations from
their testcode, which led to theredesign of SFIT asp-SFIT, whichhas led to latent
bugsfoundbyengineersatFoodly.
InAppendixA,atutorialonusingp-SFITispresented,demonstratinghowthe
p-SFITcanhelpdevelopersupdateteststoencodefailurebehaviorintheirfunctional
testsbasedonfaultinjection.

Chapter 12
Conclusions
“Theracedoesn’talwaysbelongtotheswiftnorthebattletothestrong. It
belongsrathertothosewhoruntherace,whostaythecourse,andwhofightthe
goodfight.”
CarlYastrzemski
Faultinjectiontestingisoneofthepredominanttechniquesusedbythedevel-
opers andoperatorsof industrial microserviceapplications today for testing their
applicationsforresiliencetobothinfrastructureanddownstreamservicefailures. It
ismainlyperformedonamicroserviceapplication,inproduction,wherecustomers
may be adversely affected when application resilience bugs are triggered by this
testing.
Moreoftenthannot,coarse-grainedapplicationmetricsareusedtodetectthe
presence of application resilience bugs during fault injection testing in lieu of a
specificationofapplicationbehavior. Thisoftencanresultineitheroftwopossible
outcomes,bothofwhicharenotusefulintheidentificationofapplicationresilience
bugs. Inthefirstcase,faultinjectiontestingisusedtotestadependencyofaservice,
whichisrequiredtocompletesuccessfullybyitscaller,andresultsinaelevatederror
rateoftheserviceundertest. Inthiscase,thefaultinjectiontestingonlyconfirms
thattheapplicationisworkingbydesign.
Inthesecondcase, however, theuse ofcoarse-grainedmetrics for bugdetection
mayhidecustomer-affectingissuesiftheyareeitherinfrequentordonoteffecta
largesegmentofthecustomersofanapplication. Forexample,considerthecaseof
aservicethat isallowedto exhibita 0.01%error rateunder theassumption thatall
possibleoperationsthatmayfaildonotresultinsideeffects. Whenanoperationis
introducedthatdoesresultinoneormoresideeffects–themselvesRPCstoother
services–anyfailuremayresultintheapplicationbeingleftinaninconsistentstate
147

148 Conclusions
byonlypartiallyapplyingsideeffects,withouttriggeringanymetrics-basedalerting,
norbeotherwisedetectableduringfaultinjectiontesting.
Aservice’serrorrate,andthecoarse-grainedmetricsthattrackit,onlytellpartof
thestory: whenaservicetakesaharddependencyonsecondservicethatreturnsan
errorwhencalled,resultinginthefirstservicereturninganerrortoitscaller. Often,
however,servicestakesoftdependenciesonotherservices,whereanyfailureofa
RPCiseitherignoredorotherwisecompensatedforbythecallingservice. These
softdependenciescantakeonseveralformsofincreasingcomplexity.
Considerthefollowingexamples,whicharenotcomprehensive:
• Service A takes a soft dependency on a read-only API of Service B, where
ServiceB’sresponsedoesnotinfluenceServiceA’sresponseatall.
• Service A takes a soft dependency on a side effect API of Service B, where
ServiceB’sresponsedoesnotinfluenceServiceA’sresponseatall.
• ServiceAtakesasoftdependencyonaread-onlyorsideeffectAPIofService
B, whereService A includesService B’s response inthe payload returned by
ServiceA.
• ServiceAtakesasoftdependencyonaread-onlyorside-effectAPIofService
B,whereServiceB’sresponseisusedinasubsequentread-onlyorsideeffect
APIofServiceC,whichmayormaynotbeasoftdependencyitselforappear
intheresponsepayloadreturnedbyServiceA.
Inalloftheseexamplesofsoftdependencyusage,noneoftheexamples,under
any fault injectiontestingappliedtothesoftdependenciesofacallingservice,alter
the error rate of the service that takes the soft dependency (i.e., Service A.) In
fact, only some of them altered the response payload of the calling service, also
undetectablethroughcoarse-grainedmetrics. Evenfurther,noneofthemdirectly
altertheerrorrateofthecalledserviceeither(i.e.,ServiceB,ServiceC.)
Inthisdissertation,all oftheresiliencebugsthat werediscoveredaspart of
theindustrialevaluationexhibitedthemostcomplexformofsoftdependencies
usage and were undetectable through coarse-grained metrics. Specifically, the
application resiliencebugs identified all took the generalform where some Service
Amakes aRPC toasoftdependency ServiceB, whoseresponse was thenused ina
RPCtoasoftdependencyServiceC.ServiceCthenperformedside-effects,where
neithertheresponsefromServiceBorServiceCareeitherincludedintheresponse
from Service A. As both Service B and Service C are soft dependencies, they do
notcauseService Atohaveanincreasederrorrate onfailureofeitherdependency.
Furthermore,engineeringworkperformedbytheauthorofthisdissertation,after

149
completion of the industrial evaluation, unrelated to fault injection testing, and
performedatthesameindustrialpartner,identifiedadditionalapplicationresilience
bugs of this same shape. In all cases, these application resilience bugs had gone
unnoticed by coarse-grained metrics and were only identified through violated
assertions on subsequent end-user requests in the application, a result of side
effectsthatwerenotperformedwhereoneormoresoftdependencyfailureswere
swallowedonapreviousend-userrequest.
When considering one who truly wanted to use a coarse-grained metrics ap-
proachalonefortheidentificationofapplicationresiliencebugswithfaultinjection
testing, they would have to use several of the following approaches in concert to
successfullyidentifyapplicationresiliencebugs:
First,theywouldhavetoexaminetheerrorrateofallotherservicesthatconsumes
the response from another service who has had fault injection testing performed
on any of its dependencies. For example, by examining the error rate of Service
Z, which consumes responses from Service A, whose response payloads may be
missinginformationasaresultofafaultinjectiontoitssoftdependencies,ServiceB
orServiceC.Thistypeofanalysisisimpracticalforapplicationswithhundredsof
servicesthateachcontainanon-trivialamountofdirectandtransitivedependencies.
Second,theywouldhavetoexaminetheerrorrateofallotherservicesthatsharea
dependency with the dependency chain where the fault was injected on a service’s
soft dependency. For example, by examining the error rate of a Service D, that
readsthesideeffectsperformedbyServiceC,whenServiceCwaspreviouslycalled
by Service B, as a result of a request to Service A. Again, this type of analysis is
impracticalforapplicationswithhundredsofservicesthateachcontainanon-trivial
amountofdirectandtransitivedependencies.
Third,theywouldhavetoexaminetheweek-over-weekmetricsofalldirectand
transitivedependenciesofaserviceinordertoidentifywherefaultinjectionprevented
asideeffect thatshouldhaveoccurred. Forexample,whereService AcallsService
B, which itself calls Service C to perform a side effect, where there is an absence
of that call due to a fault injection on the call to Service B that does not alter the
responsereturnedfromServiceA.Aswithprevioususesofcoarse-grainedmetrics,
thisabsencemaygounnoticedorbenotobservable,byanymetrics,atscale.
Fourth,andasalastresort,theywouldhavetouselogstoidentifyerrors,during
fault injection testing, across all direct upstream and direct and transitive down-
streamdependencies. Atscale,inproduction,wheredependenciesareconstantly
addedandevolved,andremoved,thisisnotfeasible.
In short, none of these approaches, even considered independently, are feasi-
ble for the identification of application resilience bugs in industrial microservice
applications: they are cumbersome, ad-hoc, and error prone. Therefore, in order
to successfully identify application resilience bugs in microservice applications

150 Conclusions
withfaultinjectiontesting,onemustspecificallyindicate,whentestingaservicein
isolationtofailuresofitsdirectdependencies,whatsideeffectsshouldbeperformed
inboththesuccessfulcase(wherenofaultsareinjected)andinallpossiblefault
injectionscenarios,wherefaultsmaybeinjectedononeormoredirectdependencies.
In this dissertation, it was shown that an exhaustive fault injection testing
technique combinedwith principled approach in test authorship can be used for
identificationofthesedeepapplicationresiliencebugsinvolvingsoftdependency
failures. First,anexhaustivefaultinjectiontechniqueisnecessaryforensuringthat
allfaults,andallcombinationsofpossiblefaults,areexploredduringfaultinjection
testing. Thisexhaustivenessensuresthatallcodepaths,specificallycodepathsthat
areconditionalonRPCsuccessorfailure,areexplored. Second,inorder todetect
theabsence of remote calls that result inside effects, developersmustspecifically
indicate which calls are allowed to occur when the calling service returns either
failure or success to its caller. This ensures that developers are aware of actions
that either do not occur or only partially occur, under failure: the cause of many
errorsproducedbysubsequentRPCsthatassumethatsideeffectsweresuccessfully
performed in total. However, writing these tests and understanding the possible
failurescenariosisacomplicatedtask,andthereforetoenableapplicationdeveloper
successthisapproachalsoprovidesavisualcomponentwithinteractivetestauthor-
ship coaching and visualization of RPC executions. Following this methodology
allowsdeveloperstoidentifyapplicationresiliencebugs,indevelopment,priortocode
shippingtoproductionandalleviatestheneedofmetricobservationatanygranularity.
Finally,whiletheproblemofmicroserviceapplicationresilienceisnotnewtoaca-
demicresearchers,accesstoindustrialapplicationshaslimitedtheexistingresearch.
First, existingacademic researchhas failedtocapture theinherent complexityintro-
ducedbythetwodifferenttypesofservicedependenciesthatexistinmicroservice
applications. Second, without industrial applications academic approaches are
often misaligned with the need of industrial practitioners when it comes to bug
identificationandtestingprocesses.
Inthisdissertation,anewfaultinjectiontechniqueandtestauthorshipap-
proachwasco-evolvedwithanindustrypartner,whichdevelopsandoperatesa
large-scalemicroserviceapplicationusedbymillionsofcustomerseverymonth,
inordertounderstandpreciselywhatdeveloperswerelookingfor(andneeded
tobesuccessful)inafaultinjectionapproach.
Summary. Insummary,thisdissertationmakessignificantadvancementsoverthe
existingworkinmicroserviceapplicationfaultinjectiontestinginseveralareas. First,
itisimprovesaccessibilitytorealisticmicroservicefaultsandresiliencetechniquesin
microserviceapplicationsbyconstructinganapplicationcorpuscontainingapplica-

Takeaways 151
tionsexhibitingthosecharacteristics. Then,itpresentsthedesignofanewtechnique
forRPCidentificationinamicroserviceapplicationandusesthattechniquetode-
signanoveltechniqueformicroserviceapplicationfaultinjection. Thistechniqueis
bothevaluatedbothontheestablishedcorpusandinanindustrialsetting. Using
the knowledge gained from that evaluation, the corpus is then extended with a
morerealistic industrialapplication,and the techniqueredesignedtoalignmore
closelywiththeindustrialpracticesofmicroserviceapplicationdevelopment.
12.1 Takeaways
Inthissection,asummaryofthetakeawaysforthecontributionsofthisdissertation
arepresented.
InChapter2,itwasshownthatacademicandindustrialpracticesareconverging
whenitcomestofaultinjectionandfaultpreventioninmicroserviceapplications.
Specifically, industrial practices seem to be evolving towards more principled ap-
proaches: detectionofbugs through fault injectionin development,prior todeploy-
menttoproduction,usinglibrary-levelapproachesandautomation. Thisseemsto
indicatethatthereisadesirefromindustrypractitionerstoidentifycriticalresilience
bugsbeforeapplicationcodeisinproduction,wherebugsmaybecomebothmore
costly in terms ofresponse and potentialfinancial impact. Incontrast withrecent
academic research that focuses on automating chaos experiments in production,
this dissertation specifically targets the direction industrial practices are moving:
thedetectionofresiliencebugspriortoapplicationcodeshippingtoproduction.
In Chapter 3, a new classification of microservice application dependency types
was established: hard vs. soft dependencies. Not only this dissertation is the first
academic literature to use two realistic industrial examples to demonstrate these
differenttypesofmicroservicedependenciesandtheirroleinmicroserviceresilience,
thisclassificationhassincereplacedtheirprevious(unclear)terminologyof“fail
open”and“failclosed”usedbyourindustrypartnerFoodlytodescribemicroservice
dependenciesandtheirfailurebehavior.
InChapter4,amicroservicecorpuswasestablishedthatcontainedacollection
ofsmalldemonstrativemicroserviceapplicationscontainingcommonmicroservice
resiliencepatternsandmicroserviceapplicationbugsrelatedtoresilience. Whilethis
corpusisnotthefirstcorpusofmicroserviceapplications,itfillsneedformicroservice
resilienceresearchbyprovidingapplicationscontainingbugsandresiliencepatterns,
similar to the bug corpora used in software engineering research on monolithic
programs. Sincethe open-sourcerelease of this corpus, ithas beenused byother
researchersinmicroserviceresilience.

152 Conclusions
InChapter5,anewtracingtechniquewaspresentedthatidentifiesRPCs,exe-
cutedbyamicroserviceapplication,inaconsistentmanneracrossdifferentexecu-
tionsofthesamecode. Thistracingtechniqueisunlikeanytracingtechniquethat
existscurrentlyformicroserviceapplications,asitisspecificallydesignedforusein
dynamicanalysisandnotforproductiontracing. Notonlycanthisbeusedtosup-
port exhaustive faultinjection, as is thefocus of this dissertation,it wasalso shown
that it could be used by several other types of dynamic analyses (e.g., microservice
smelldetection).
InChapter6,anexhaustivefaultinjectiontechnique waspresentedformicroser-
viceapplications. Thistechniquewasshowntobeintegratedwiththeexistingde-
velopmentandtestingprocessesofdevelopers,leveragingtheirexistingfunctional
tests,withoutrequiringaspecification. Thisiscriticalforindustrialadoption,where
theoverheadofrequiringaspecificationistoomuchtobear. Itwasalsoshownthat
undercertainapplicationdesigns,wheregraphsfavordepthoverbreadth–thenat-
uraldecompositionofmicroserviceapplicationsfromtheirmonolithiccounterparts
–thatoptimizationsarepossibletoreduceoverheadinfaultspaceexploration.
In Chapter 7, both the tracing technique and its use in the new fault injection
techniquewasevaluatedagainstthesyntheticapplicationcorpus. Itwasfirstdemon-
strated that this tracing technique can be used to identify individual RPCs in a
microserviceapplicationuniquelyanddeterministically,therebyfacilitatinganex-
haustive search. Whenevaluated incombinationwiththe faultinjectiontechnique,
it was shown that all bugs seeded into the synthetic application corpus could be
identified both quickly and ina development environment, prior to deployment to
production. Finally, it was shownthat when graphstake onthe naturaldecomposi-
tion,asinamodule-basedmonolith,possibleoptimizationscanyieldsignificant
benefitsintermsoftestingtime.
InChapter8,thedescriptionofalarge-scaleindustrialmicroserviceapplication
waspresented. Inthisdescription,itwasshownhowformanyuse-casesfaultinjec-
tioninproductionisnotpossibleduetopossibilityofcustomerimpact. Fromthere,
itwasshownthatanymicroserviceapplicationresiliencetestingtechniquemustbe
exhaustive,inordertofindcorner-casebugs,andthatautomationisnecessaryfor
applyingthistoservicesthatcontainalargenumberofdownstreamdependencies.
InChapter9,anindustrialevaluationofthefaultinjectiontestingtechniquewas
presented. Thisevaluationidentifiedanumberofnotabledrawbacksanddesign
limitationsthatwouldinhibitadoptioninindustrialsettings.
Thefirstdesignlimitationisthatindustrialmicroserviceapplicationsaresimply
toolargetobetestedasawholesaleapplication;instead,individualservicesneedto
betestedinisolationfortheirtolerancetofailuresoftheirdirectdependencies. The
second designlimitation is thatwithout aprincipled approach to testauthorship,
it is much too easy for application developers to write tests that do not contain

Discussion 153
strongenoughassertionsneededforbugidentification. Thethirdandfinaldesign
limitation is that the process of writing a single test that captures both the appli-
cation behavior when there are not faults present in the system and when there
arefaultspresentinthesystem,containsmuchtooverheadasitisanewmanner
of test authorship that developers will be unfamiliar with. Therefore, in order to
be successful with fault injection testing, any technique must be paired with an
mechanizedapproachthatguidesthedeveloperduringthisprocess.
Finally,asdemonstrated,thechallengeoffaultinjectiontestingisnotonlytech-
nical – as in, adaptation of the fault injection technique to work on much larger
applications – but, it is also socio-technical, in that the process taken on by appli-
cation developers of introducing fault injection testing into their daily workflows,
mustalsobeaddressed.
In Chapter 10, differences between the constructed synthetic corpus and the
evaluated industrial microservice application were presented. From there, it is
shownthatthecomplexityofindustrialmicroserviceapplications–containingamix
ofhardandsoftdependencies–isarrivedatbyattemptingtoimprovetheresilience
ofanindustrialapplicationtodependencyfaults. Thisisoftenhowresiliencebugs
isintroduced. Therefore, itbecame necessarytoconstruct anewsynthetic example
forthecorpusthatresemblesanindustrialmicroserviceapplicationmoreclosely.
InChapter11,anewfaultinjectiontestingprocesswaspresentedthatprovidesa
structured,developer-centricapproachformicroserviceresiliencetesting. Thispro-
cessextendstheexistingfaultinjectiontechniqueforapplicationsthataredesigned
to gracefullydegrade underfailure, asobservedinour industrialevaluation, and
inherent in the use of soft dependencies. It improves both the process of writing
therequiredstructured happypathfunctionaltestsrequired forcapturingthefull
behaviorofaservicewhennofaultsarepresent,andthenassiststhedeveloperin
updating those tests to account for the service’s behavior under fault. To ensure
thatthis processwas alignedwith themanner inwhich industrialapplication de-
velopersbuild,test,anddeploytheirservices,therequirementswerederivedbased
onobservationsoftheseprocessesandtestcodeofFoodly,theindustrialpartner.
Thisprocesshassinceresultedinthediscoveryoflatentapplicationbugsrelatedto
resilienceatFoodly.
12.2 Discussion
SFIT, p-SFIT, and the open source Filibuster prototype stand alone in the fault
injection space by providing a principled approach for fault injection testing of
microserviceapplications.

154 Conclusions
SFIT. Whenitcomestothetechnique,SFIT,itistheonlyfaultinjectiontechnique
thatisdesignedspecificallyformicroserviceapplicationsthatcanprovideexhaus-
tivesearchwithdeterministicreplay,inthepresenceofconcurrency,withoutthe
requirementofdeepinstrumentationorschedulercontrol.
Whencomparedtothemostrecentacademicapproachestargetedat(oradjacent
to) microservice applications, they often fail to consider programming patterns
and behaviors common to industrial microservice code: for example, either by
failing to consider concurrency and its effect on permutation of RPC execution
order[Zha+21b]orbyfailingtoconsiderthatthesameRPCmaybeexecutedfrom
multiplelocationsinthecodeforthesameapplicationexecution[Che+23].
Intermsofindustrialapproaches,mostfocusonlow-level,coarse-grainedinstru-
mentationinordertoavoidanyinstrumentationoftheapplicationatall. Incontrast,
SFITandit’sprototypeimplementationFilibuster,demonstratedhowapplicationin-
strumentationcanbeperformedinalightweightwayandautomaticallythroughthe
useof ajavaagent. Byperforminginstrumentationat theapplicationlevel,amore
comprehensivesetoffaultscanbedirectly tested;thisisincontrasttoapproaches
that must trigger high-level application failures through low-level fault injection.
As discussed, one such industrial solution attempted this style of application-level
instrumentation,butsinceabandoneditduetothelevelofcomplexityinvolved.
Mostindustrialapproachesstillrelyonfaultinjectionatthegranularityofan
individualservice: inthat,ifServiceAmakesmultipleRPCstoServiceB,theonly
failurethatcanbesimulatedisthewholesalefailureofServiceB.Thisisunrealistic
becausemultiplecalls,todifferentendpointwith differentarguments,caneither
besimultaneouslyoperationalornon-operational. Forexample,considerthecase
where only certain arguments to an RPC made to endpoint X of Service A are
failingwheremultiplecallsaremadetoServiceA’sendpointsXandYwithdifferent
arguments. SFITprovidesasolutiontothisproblembytargetingindividualRPCs
forfaultinjectionsduringfaultinjectiontestingenablingexhaustiveexploration
forallpossiblefaultsthatanapplicationmaybesusceptibleto.
-SFIT. Asdiscussedinthisdissertation,oneofthefundamentalproblemswith
p
thefaultinjectiontestingofmicroserviceapplicationsisknowingpreciselywhatthe
applicationshoulddowhenfaultsarepresent. p-SFITprovidesthefoundational
process that assists developers in answering this problem. It first requires that
developersspecify,intotal,thebehavioroftheirservicewhennofaultsarepresent.
Then, through an integrated IDE plugin, fault injection visualization, and code
snippetsandrecommendations,itassiststhedevelopersinadaptingthoseteststo
accountforallpossiblefailurebehaviors. Wherepossible,p-SFITtriestominimize
the requirement of manual specification of behavior by inferring what it already

Discussion 155
knowsfromwhatthedeveloperhasspecifiedsofar: thisinferredbehavioristhen
checked against the application and only when it does not hold, is the developer
promptedtoaddadditionalinformationintheformofassertions.
Whenitcomestoacademicapproaches,mosthavereliedondeveloperspecifi-
cationsofthebehaviorofthesystem(orapplication)undertest[ARH15b]. This
is somewhat straightforward when testing a database or distributed system that
employ replicas (e.g., serializability, linerizability, causal consistency) but much
morecomplexinamicroserviceapplicationthatisbuiltandadaptedtostayfunc-
tional and degrade gracefully under failure, as some failures are permitted. As
an alternative, one academic approach has tried to address the problem from an
alternative direction by simplifying their classification of a bug as any operation
thatthrowsanexceptioninapplicationcodethatissurfacedtotheuserunderfault
injection[Che+23]. Thisisproblematicforseveralreasons.
First, the boundary between application code and library code is blurry: for
example, at our industry partner RPCs traverse multiple “in-house” libraries in
applicationcodebeforereachingunderlyingthird-partyframeworkandstandard
librarycode,makingitdifficulttoknowwhatisandisnotabug. Second,asmany
RPClibrariesthrowexceptionsbydesign,thisboundaryisfurtherblurred. Infact,
using this criteria alone, this dissertation identified hundreds of false positives
wheretheapplicationthrewanexceptiontoanupstreamserviceindicatingthata
requestcouldnotbeprocessedbecauseaharddependencywasunavailable: desired
behavioroftheapplication. Third,andfinally,asdemonstratedinthisdissertation,
mostmicroserviceresiliencebugsthatremainundetectedarebugswheresomething
didn’thappen,whichshouldhave. Inthiscase,onlyafullspecificationofbehavior
whenfaultsarenotpresentcanbeusedtoidentifythesebugs.
Inshort,knowingwhatamicroserviceapplicationshoulddounderfailure
cannot be automatically determined and requires input from the application
developer. This is key because the behavior may be either be counter-intuitive,
otherwise not straightforward, or rely on actions for remediation that occur outside
oftheactualapplication,aswasthecaseofoneofthebugsdiscoveredduringthe
testingofanindustrialapplicationperformedinthisdissertation. Therefore,thekey
istoforegoanymechanizedapproachtobugclassificationandinsteadprovidea
mechanismforthedevelopertoeasilyconfirmordenyobservedbehaviorthrough
testingandeasilyencodethatbehaviorintofunctionaltestsoftheirapplication.
Filibuster. Whenit comestotheexperience ofusing Filibuster noneof theexist-
ingacademicorindustrialtoolscomeclosetotheverticallyintegratedexperience
providedby Filibuster.
In terms of academic approaches, GraphViz has been used to provide visual

156 Conclusions
depictionsmicroserviceRPC’sexecutedinanapplicationwiththelocationoffault
injections at high-granularity [ARH15b]. On the industry side, some software-
as-a-serviceofferingsprovideavisualcomponentforthedesignoffaultinjection
experimentsthroughaweb-baseduserinterface.
In contrast Filibuster provides an unparalleled vertically integrated fault
injectiontestingexperiencealongsidethetestsyouareauthoringinIntelliJ.This
includesvisualizationofRPC’s(withargumentsandinvocationorder)executedby
thecurrenttest,thelocationofprecisefaultinjections,alistofsynthesized testsby
the fault injection and code snippets with integrated JavaDoc. Even further, and
not discussed in this dissertation, the IntelliJ plugin also provides basic linting for
RPCstohelpidentifyredundantRPCs[Mei23f]andinefficientRPCchains,[Mei23e;
Mei23g]aswellasavisualizationofendpointRPCAPIcoveragebythecurrenttest
suiteforthecurrentservice[Mei23d;Mei23c;Abd+23].
CompetingApproaches. WhentheinitialdevelopmentofthePython Filibuster
prototype was complete, this prototype was used to pitch Foodly on the partner-
shipthatweultimatelyestablishedoverthefollowingtwoyears,where: theJava
Filibuster implementation was built, integrated into the OpenTelemetry Java in-
strumentation, and the p-SFIT technique was evolved over several months with
trial-and-errorusingoneserviceatFoodly.
Duringthistime,twoteamswithinFoodlywereworkingonfaultinjectiontesting
independently. ThefirstteamwasaSiteReliabilityEngineering(SRE)teamthat
wasworkingon deployingLitmus,an infrastructurecoarse-grainedfaultinjection
tool, across the Foodly’s infrastructure. The second team was a team who had
seentheoriginal Filibuster pitchatFoodlyandgiventhatJavaFilibuster wasnot
yet complete, decided to implement their own fault injection testing framework
inspired by this (at thetime, yetincomplete) dissertation. Their target wastotest
theirindividualservicetofailuresofdownstreamdependencies.
ThefirstteamwassuccessfulindeployingLitmusacrosstheinfrastructureof
Foodly and used it for several chaos engineering style experiments. As Litmus
requires that developers design their own experiments, these experiments often
took the form where a fault was injected on RPCs to a service that was a known
harddependency: merelyonlyconfirmingthattheapplicationbehaviorwasasthey
expectedittobe. Experimentsofthistype,whileusefulforvalidatingthatmetrics
andalertingworkproperly,(i.e.,validatingthesocio-technicalresponse)aremuch
toosimplistictodiscoverapplicationbugs. However,thisexperimentation,while
carefullydesignedandexecuted,wasnotwithoutadverseimpact: infact,several
of the chaos engineering style experiments that they ran resulted in production
incidentsthataffectedcustomer’sabilitytousetheservice. Thisisahighcosttopay

Discussion 157
toonlyconfirmthatapplicationbehaviorisasonewouldexpect. Incontrast,SFIT
providesamannertoperformthissametypeofexperimentation,indevelopment,
beforecodeshipstoproductionwherethereisnoriskofadversecustomerimpact.
Whenitcomestothesecondteam,theyalsohadagoalofexperimentationin
production,butwithaminimizedblastradiustoavoidadversecustomerimpact.
SimilartoFilibuster,theirtechniqueusesRPCmetadatatoincludeinformationthat
couldbe used to drivewhere faultswereinjected. However, instead ofembedding
identifiers into metadata, which would be used to determine precisely on which
RPCtoinjectafault,headerinformationwouldcontainanRPCbyname,wherea
fault wasinjected. For example,bystatingthatafaultshouldbe injectedonRPC
X that is issued between Service A and Service B. This is in direct contrast to the
granular fault injection provided by SFIT, and is closer to a coarse-grained fault
injectionapproachthatconsidersservicesastheunitoffailure: insufficientforthe
detectionofdeepapplicationresiliencebugs.
ThisfunctionalitywasbuiltandintegratedintothecoreRPCandserviceframe-
worksofFoodlyanddesignedtobeoperatedinanisolatedproductionenvironment
whereatestversionoftheapplicationcouldbeusedtoperformactionsusingthe
service. Sincethedevelopmentofthistechnique,ithasseenadoptionacrossFoodly
asaquickand easywaytogetstartedwithfaultinjectiontesting,asit isalreadyin-
tegratedintoalloftheexistingdevelopmenttoolingandcaneasilybeperformedin
anisolated,production-likeenvironment. Whilethisspeaksvolumesabouttheuser
experienceofafaultinjectiontoolanditsadoption,incontrasttothecontributions
ofthisdissertation,thismethodologyisalsoshallowforseveralreasons.
First, as discussed, targeting a particular RPC by name is not sufficient for the
identificationofbugs: severalRPCsmaybemadetothesameRPCendpointwhere
only failure of one (with the others succeeding) may trigger a bug if application
behaviorisconditionalonacertainoneofthoseRPCsfailing. Itisbelievedthatthis
design mayhave been derivedeither underthe assumptionthat servicestypically
fail “wholesale” – where they either respond to RPCs successfully or do not – or
that services do not make RPCs the same downstream dependency twice in the
sameexecution,bothofwhicharenottruegenerally. Second,andmoregenerally,
targeting onlyasingle RPCisnot sufficient forthe identificationof bugs: failuresmay
onlybetriggeredifmultipleRPCsfailinthesameexecution–forexample,byfailing
anRPCthatisonlytriggeredinafallbackpathonceaninitialRPCfails. Thisdesign
may have been derived under an assumption that default values are often used
instead of fallbacks for RPC failure, which also is not true generally. SFIT is the
only fault injection technique that provides the granularity necessary for the
identificationofapplicationresiliencebugsinthepresenceofmultipleRPCsto
thesameRPCmethodinthepresenceofconcurrency.
Third,itisoftenthattheabsence ofasideeffecttriggersanapplicationbug: for

158 Conclusions
example,bynotperforminganRPCwhichresultsinasideeffect,whenitotherwise
should have been performed. As demonstrated by the bugs that were identified
during the evaluation of Filibuster on Foodly’s microservice application, these
often happen when a fault is injected on an soft dependency that then causes a
subsequent RPC – hard or soft – to not be executed at all. Testing an application
throughitsuserinterface,withcoarse-grainedfaultinjection(i.e.,byRPCname)
withoutvisibilityintowhatRPCsarenotoccurringthereforeisnotsufficientforthe
identificationofthesebugswhensoftdependenciesareemployed–theapplication
will show no error as the dependency is soft and the absent side effect will only
affect future user operations. All bugs identified in this dissertation were of this
classification,andallwentundetectedthroughcoarse-grainedmetricsduetotheir
rare occurrence with respect to overall application load. Most likely, these types
of bugs were unknown to the developers of Foodly, as it was discovered during
thewritingofthisdissertationandhadnotbeenpreviouslydiscussedatallinany
academicliterature. -SFITprovidesthenecessaryapproachfortheidentification
p
ofdeepapplicationresiliencebugswhichinvolvesideeffectingsoftdependencies
whichdonotresultinerrorsunderfailure.
Bug Identification. Identifying these deep application resilience bugs using the
existingapplication’stestsuitewasalsodifficult. WhenapplyingSFITtoFoodly’s
existingfunctionaltestsuite,itwasidentifiedthatmanyoftheteststhatdevelopers
werewritingfortheirserviceswereunderspecified: theymerelyexecutedthecode
path and made assertions on the response returned by the service under test. In
fact, it was discovered that SFIT could inject faults on almost all of the RPCs that
wereexecutedbyatestwithouttriggeringanassertionfailureofthetest. Essentially,
almost all dependencieswere soft dependencies; in othercases, all dependencies
were hard any any fault injection triggered a (trivial) assertion failure. This lead
to the realization that SFIT would only be successful in identifying bugs when
tests were written with a high enough fidelity that they included whether or not
the dependencies that were invoked were soft or hard. This directly lead to the
design and development of -SFIT, which integrates with an application’s ex-
p
isting functional test suite and allows for precise specification of hard and soft
dependenciesin orderto determineallowedwhat RPCfailuresare “admitted”
underfaultinjectionandwhichresultinapplicationbugs.
Once functional tests were written to a fidelity enough to capture valid bugs
related to fault injections, explaining these bugs to application developers still
remained difficult a challenge because they often involved executions involving
multipleRPCswhereafaultwasinjectedononeparticularRPCinasequenceof
many successful RPCs. Not only did this require application of the terminology

Discussion 159
of “hard” and “soft” to dependencies to provide a uniform manner to talk about
RPCs that trigger error responses and RPCs that do not trigger error responses –
sinceadopted by Foodlyreplacingpreviousunclear terminology– italsorequired
amechanismforvisualizationoftheRPCsexecutedbyatestandwherefaultswere
injectedinanexecutionthatresultedinanassertionfailureofafunctionaltest.
Not unlike third-party services such as LightStep [Lig] and Grafana [Gra],
p-SFIT allows developers to visualize RPC executions as a trace with the casual
dependenciesbetweenhighlighted. However,whatdifferentiatesp-SFITfromthese
servicesisthatthese visualizationsofRPCexecutionsaredirectlyintegratedinto
thedeveloper’sIDEandtiedtoaspecifictestexecutionthattheyareinteractively
running. As an added benefit, as they are only designed for use in the testing
and debugging scenarios, they include the invoked RPC’s request and response
payloads: not availablein tools designed forproduction sampling where overhead
istoohigh.
Inshort, -SFITistheonlyexhaustivefaultinjectionapproachformicroservice
p
applicationswithanintegrateddevelopmentenvironmentforvisualizationof
RPCexecutionsandfaultinjections,necessaryforhelpingapplicationdevelopers
understandcomplexfailurescenariosandtheimpacttheyhaveontheirfunctional
test’sassertions.
Test Adaptation. As developers write functional tests with integrated fault in-
jection testing, they are bound to run into issues with incorrectly classifying de-
pendenciesashardorsoftandwritingincorrecttestassertions. Therefore,itwas
necessarytoprovideamechanismthat,ineasy-to-understandterminology,could
explain to developers whya test failed under faultinjection and identify what they
didincorrectlyintheircode.
To solve this problem, p-SFIT provides an “coaching” interface that instructs
developers on thecorrect process toupdate their tests– using integratedJavaDoc
and code snippets. This helps developers use the correct APIs to use to classify
dependenciesashardorsoftandhowtoindicateprecisely,whendealingwitheach
dependency,theassociatedassertions. Thisdesignwasbasedonfeedbackgathered
when writing tests without p-SFIT and the difficulties in properly specifying this
usingstandardJavacode.
Finally, in order to avoid the overhead in writing tests for all combinations of
possiblefaults,p-SFITtriestoautomaticallyinferapplicationbehaviorundercombi-
nationsoffaultsusingthedeveloperspecifiedapplicationbehaviorforindividual
faults, only prompting developers to encode the specific behavior under one or
more faults when ambiguous. This design was based on feedback received from
developerswheretheycommonlyonlyconsiderfaultsinisolation,asdemonstrated

160 Conclusions
previouslyinFoodly’sownfaultinjectionframework’sdesign.
-SFIT is the only exhaustive fault injection methodology for microservice
p
applications with integrated developer “coaching” on how to properly write
functional tests for bug discovery, necessary as the concept of encoding the
behaviorofanapplicationunderfailureisnewtoapplicationdevelopers.
Dissertation-AdjacentWork. Theresearchinthisdissertationhasdirectlyresulted
intwopiecesofdistinctrelatedworkinthemicroserviceapplicationresiliencearea.
First, andmostnotably,Filibuster hasbeenusedtounderstandtheimpactofre-
siliencemechanismssuchascircuitbreakersandloadshedding. Morespecifically,re-
searchintounderstandinghowresiliencemechanismscanintroduceadverseeffects
whenactivatedbydisablingcorrectlyfunctioningpartsoftheapplicationtocontain
afailurehasbeenperformedbytheauthorofthisdissertationatFoodly[Mei+22].
Sincethen,Foodlyhasdecidedthatcircuitbreakersarenolongeranapproachthat
should be universally appliedacross their services, as a number of recentincidents
havetakenthepreciseformasidentifiedbythisresearch.
Second, service failures are not the onlything that canaffect microservice appli-
cations,asmicroservicesalsotakedependenciesonqueues,databases,andcaches.
Tothatend,theauthorofthisdissertationalsosupervisedamaster’sthesis[Ass+24;
Ass23;Mei23b;Mei23a;Mei23h]exploringthiswork: howcanSFITbeextendedto
faultinjectiontestingofdatabases? Thisworkinvolvedexploringnotonlyfaultsre-
latedtoconnectionfailuresandserviceunavailabilitybutalsotheimpactofincorrect
(i.e.,byzantinefaults)answersfromservices,suchasemptystringornull.
This work resulted in not only extensions to the SFIT algorithm, through the
use of a new recursive byzantine fault injection algorithm, but also extensions of
theIDEpluginof Filibuster toimprovedeveloperfeedbackanddebuggingofthe
impactofinjectedfaults. Thismaster’sthesisnotonlyimprovedonSFITandp-SFIT
butalsoresultedintheextensionoftheapplicationcorpuswithseveralexamples
fromFoodlyofactualbugsthatresultedincustomer-affectingoutages.
Impact. SincethedevelopmentandevaluationofbothSFITandp-SFIT,Foodly
has asked application developers across all of their500+services to useFilibuster
fortestingtheirapplicationsforresilience.
While the ultimate approach p-SFIT has not been fully adopted at Foodly yet for
technicalreasons,atleastsix(6)differentteamswithinFoodlyhaveimplemented
Filibuster tests in 2023 for their application using components taken from both
SFITandp-SFIT:thetestingprocess(fromSFIT)andtheintegratedIDEpluginfor
debuggingfailures(fromp-SFIT.)Moreteamsareexpectedtoadopt Filibuster for

Conclusion 161
faultinjectiontestinginthecomingyear,andsincewritingthisdissertation,atleast
threeadditionalteamshavestartedwriting Filibuster tests.
ToquoteananonymousdeveloperatFoodlywhenfirstwritingaFilibuster test:
“My team really looks forward to the first filibuster test to work for this
servicesothatwecouldaddmore.”
Similarly, one developer stated this when examining one of the application
behaviors,provokedby Filibuster,whereanactualbugwasdiscovered:
“rightyeahithinkthisisasolidcalloutfromtheFilibustertest”
In fact, since the evaluations performed in this dissertation, additional bugs
thatmatchthedesignthefictionalapplicationspresentedinthisdissertationhave
beenidentified inservicesthathavenot yetemployed faultinjectiontesting. This
indicatesthepressingconcernsaddressedbythisdissertationandtheneedformore
widespreadadoptionoffaultinjectiontesting.
Finally,oneoftheengineersonthechaosengineeringprojectatNetflixreached
outtotheauthorofthisdissertationpersonally1 regardingtheworkinthisdisserta-
tionwiththefollowing:
“I applaud your view of getting developers to encode their expectations
iteratively–thatisabranchofthespacethatIhavenotexplored. [...] Thanks
foradvancingthespace,I’mexcitedtofollowyourworkhereinthefuture.”
12.3 Conclusion
For a proper conclusion to this dissertation, the reader is referred to the thesis
statementthatopenedthisdissertation.
Identification of latent application bugs related to resilience in microservice applica-
tions,in development,andbeforedeploymentof codetoproduction,ispossible using
a developer-centric approach and can surface critical application bugs in large-scale,
industrialmicroserviceapplications.
Asdemonstrated bythis dissertation,itispossible toidentify latentapplication
resiliencebugs,indevelopmentandbeforedeploymentofcodetoproduction,using
1Personalcommunication,2022.

162 Conclusions
a developer-centric approach that surfaces critical application bugs in industrial
microserviceapplications.
Thetechniquebywhichthisisperformed iscalledSFIT,anovelfaultinjection
techniquethatallowsforexhaustivefaultinjectiontestingofmicroserviceapplica-
tionsindevelopmentusinganapplicationsexistingfunctionaltestsuite. Inorderto
ensurethatthesefunctionaltestsarewrittenwithhighenoughfidelitytosurface
deepapplicationresiliencebugs, aprocessnamedp-SFITwasdesignedthat assists
developersinunderstandingcomplexfailurescenariosandadapttheirfunctional
testsaccordingly. SFITandp-SFITprovideapowerfulcombination,unprecedented
inexistingacademicresearchandindustrialtoolingandservices,thatcansurface
deep,applicationresiliencebugs.

Appendix A
Using -SFIT: A Tutorial
p
“Facedwithmysteriesdarkandvast,statementsjustseemvainatlast,some
rise,somefall,someclimb,togettoTerrapin.”
Garcia&Hunter,TerrapinStation
Inthisappendix,theopen-sourceprototypeimplementationofp-SFIT,Filibuster,
is used to demonstrate the use of p-SFIT on the example application presented
in Section 10 to capture its behavior under fault. For a review of this example
application,thereaderisreferredtobothChapter10andFigure(s)10.1and10.2.
First, a functional test of the application is written using the p-SFIT testing
interfaceprovidedby Filibuster. Thisdemonstrateshowp-SFITexplicitlyassists
thedeveloperinwritingawell-formedhappypathtestoftheapplicationbeforethe
startoffaultinjectiontesting. Next,theauthoredfunctionaltestisusedtoperform
faultinjectiontestingoftheapplication. Fromhere,adevelopermustspecifyusing
p-SFIThowtheapplication’sbehaviorchangesunderfault.
Finally, the application’s behavior is altered, and the p-SFIT testing process is
re-employedtodemonstratehowitforcesthattheoriginalassertionsbemodifiedto
accountforthenewbehavior;theexistingassertionsareadjusted,andaspecification
ofnewapplicationbehaviorunderfaultisaddedtothefunctionaltest.
A.1 Single Adjustment Example
Consider the case where only a single possible pricing adjustment might be per-
formedbytheexampleapplicationpresentedinChapter10.
163

164 Usingp-SFIT:ATutorial
A.1.1 setupBlock: Perform Test Setup
First, the setupBlock is used to set up the test state before each test execution. In
thisexample,thecacheanddatabasestatesareresetandthenprimedbygivingthe
customersomestartingfundstousefortheirpurchase.
Thisblockfunctionssimilarlytothe@BeforeAlland@BeforeEachblocksandcan
becombined. However,setupBlockallowssubclassestooverridetestsetupwhile
inheritinganyoftheotherblocks: notpossiblewith@BeforeAllor@BeforeEach.
@Override
1
public void setupBlock() {
2
// Reset cache state.
3
PurchaseWorkflow.resetCacheObjectForUser(consumerId);
4
5
// Reset database state.
6
PurchaseWorkflow.depositFundsToAccount(consumerId, 20000);
7
assertEquals(
8
20000,
9
PurchaseWorkflow.getAccountBalance(consumerId));
10
}
11
A.1.2 stubBlock: Stub Downstream Dependencies
InthestubBlock,theFilibuster-providedstubFormethodisused,whichwrapsthe
existingstubFormethodprovidedbyGrpcMocktobeabletoadjuststubsbasedon
faultinjections,tostubtheresponsesofdownstreamdependencies.
Here, every downstream dependency invoked by this test with responses is
stubbed. Ifoneofthesestubsismissed,Filibuster willprovideaspecificwarning
askingthestubtobewrittenbeforeproceeding.
Stubbingcanbeperformedatamethodlevel(asdonewiththegetUser,getCart,
andupdateCartRPCs)orforanindividualRPCwithspecificarguments,asdone
withthegetAdjustmentRPC.
@Override
1
public void stubBlock() {
2
stubFor(
3
UserServiceGrpc.getGetUserMethod(),
4
Hello.GetUserRequest.
5
newBuilder().
6
setSessionId(sessionId).build(),
7

SingleAdjustmentExample 165
Hello.GetUserResponse.
8
newBuilder().
9
setUserId(consumerId).build());
10
11
stubFor(
12
CartServiceGrpc.getGetCartMethod(),
13
Hello.GetCartRequest.newBuilder()
14
.setSessionId(sessionId).build(),
15
Hello.GetCartResponse.newBuilder()
16
.setCartId(cartId)
17
.setTotal("10000")
18
.setMerchantId(merchantId)
19
.build());
20
21
stubFor(
22
PricingAdjustmentServiceGrpc
23
.getGetAdjustmentMethod(),
24
Hello.GetDiscountRequest
25
.newBuilder()
26
.setCode("FIRST-TIME").build(),
27
Hello.GetDiscountResponse
28
.newBuilder()
29
.setPercent("10").build());
30
31
stubFor(
32
CartServiceGrpc.getUpdateCartMethod(),
33
Hello.UpdateCartRequest.newBuilder()
34
.setCartId(cartId.toString())
35
.setDiscountAmount("10")
36
.build(),
37
Hello.UpdateCartResponse.newBuilder()
38
.setCartId(cartId.toString())
39
.setTotal("9000")
40
.build());
41
}
42

| 166   | Usingp-SFIT:ATutorial |     |       |                |      |     |
| ----- | --------------------- | --- | ----- | -------------- | ---- | --- |
| A.1.3 | executeTestBlock:     |     | Write | the Functional | Test |     |
ThetestcodeisplacedintheexecuteTestBlock. Inthisapplication,thereisonlya
calltotheAPIgateway. Theresponseisthensettotheresponsevariable,whichis
providedby Filibuster andautomaticallyfedintotheassertionmethods.
@Override
1
| public | void | executeTestBlock() |     | {   |     |     |
| ------ | ---- | ------------------ | --- | --- | --- | --- |
2
|     | APIServiceGrpc.APIServiceBlockingStub |     |     |     | blockingStub | =   |
| --- | ------------------------------------- | --- | --- | --- | ------------ | --- |
3
APIServiceGrpc.newBlockingStub(API_CHANNEL);
4
|     | Hello.PurchaseRequest |     | request | =   |     |     |
| --- | --------------------- | --- | ------- | --- | --- | --- |
5
Hello.PurchaseRequest.newBuilder()
6
.setSessionId(sessionId)
7
| 8   |                                                   | .build(); |     |     |     |     |
| --- | ------------------------------------------------- | --------- | --- | --- | --- | --- |
| 9   | response.set(blockingStub.makePurchase(request)); |           |     |     |     |     |
}
10
| A.1.4 | assertTestBlock: |     | Perform | Test Assertions |     |     |
| ----- | ---------------- | --- | ------- | --------------- | --- | --- |
Inthisblock,assertionsontheresponseoftheRPCmethodinvokedinthetestblock
areperformed. Asshown,itisassertedthattheresponseissuccessfulandthatthe
databasewritesarecorrect.
In thisexample, a helper method isparameterized so thatthe correct total can
be asserted in our failure case when the discount is not applied. Most likely, this
refactoringwouldbeperformedwhenadjustingthefunctionaltesttoaccountfor
theapplication’sfailurebehavior;thispresentationisforbrevity.
1 @Override
| public | void | assertTestBlock() |     | {   |     |     |
| ------ | ---- | ----------------- | --- | --- | --- | --- |
2
assertTestBlock(10000);
3
}
4
5
| public | void | assertTestBlock(int |     | total) | {   |     |
| ------ | ---- | ------------------- | --- | ------ | --- | --- |
6
|     | Hello.PurchaseResponse |     |     | response = |     |     |
| --- | ---------------------- | --- | --- | ---------- | --- | --- |
7
|     | (Hello.PurchaseResponse) |     |     | getResponse(); |     |     |
| --- | ------------------------ | --- | --- | -------------- | --- | --- |
8
9
| 10  | // Verify | response. |     |     |     |     |
| --- | --------- | --------- | --- | --- | --- | --- |
assertNotNull(response);
11
assertTrue(response.getSuccess());
12
|     | assertEquals(total, |     | response.getTotal()); |     |     |     |
| --- | ------------------- | --- | --------------------- | --- | --- | --- |
13

SingleAdjustmentExample 167
14
// Verify cache writes.
15
JSONObject cacheObject = PurchaseWorkflow
16
.getCacheObjectForUser(consumerId);
17
assertTrue(
18
generateExpectedCacheObject(
19
consumerId, cartId, total).similar(cacheObject));
20
21
// Verify database writes.
22
assertEquals(20000 - total,
23
PurchaseWorkflow.getAccountBalance(consumerId));
24
assertEquals(total,
25
PurchaseWorkflow.getAccountBalance(merchantId));
26
}
27
A.1.5 assertStubBlock: Verify Stub Invocations
In this block, assertions on the invocation counts of the stubbed RPC methods
arewritten. Asshown,themethodverifyThatfrom Filibuster’s APIisused asa
wrapperaroundtheGrpcMockmethodofthesamenametoassertthatthemethods
getUser,getCart,getAdjustment,andupdateCartisinvokedpreciselyonce.
@Override
1
public void assertStubBlock() {
2
verifyThat(UserServiceGrpc.getGetUserMethod(), 1);
3
verifyThat(CartServiceGrpc.getGetCartMethod(), 1);
4
5
Hello.GetDiscountRequest request =
6
Hello.GetDiscountRequest.newBuilder()
7
.setCode("FIRST-TIME")
8
.build();
9
10
verifyThat(
11
PricingAdjustmentServiceGrpc.getGetAdjustmentMethod(),
12
request,
13
1);
14
15
verifyThat(CartServiceGrpc.getUpdateCartMethod(), 1);
16
}
17

168 Usingp-SFIT:ATutorial
A.1.6 teardownBlock: Perform Test Teardown
SimilartosetupBlock,theteardownBlockcanbeusedforperformingtestteardown.
Again,itdoesn’treplaceuse@AfterEachor@AfterAll,butoperatesinasimilarway:
theycanbecombinedoroverriddenexplicitlyinsub-classestochangeteardown
whileinheritingotherbehavior.
Here,thestateofthedatabaseisresetintheteardowntobeapropertestcitizen.
@Override
1
public void teardownBlock() {
2
// Reset cache state.
3
PurchaseWorkflow.resetCacheObjectForUser(consumerId);
4
5
// Reset database state.
6
PurchaseWorkflow.deleteAccount(consumerId);
7
PurchaseWorkflow.deleteAccount(merchantId);
8
}
9
A.1.7 failureBlock: Application Failure Behavior
The failureBlock is executed at the start of the test, after setup and stubbing,
andprovidesaconvenientlocationforplacingtheassertionsontheapplication’s
behaviorunderfault.
Here,the entiretyofthe compltedfailureBlockispresented. However, aspart
ofthep-SFITprocess,eachinjectedfaultwouldinduceatestfailure: fromthere,the
developerwouldwriteasingleassertioninthissectiontoadaptthetest’sassertions
totheapplication’sbehaviorunderfault. Thiswouldthentriggerre-executionof
thetestwhereallassertionswouldbere-checkedbeforeinjectionofthenextfault,
whichwouldrequire anotheradditionto thissectionif thatfailure provokeda test
failure. ThisprocesswasdescribedinSection11.1.
First,itisstatedthatboththegetUserandgetCartmethodsareharddependencies:
they will throw an exception with a particular message on failure and abort the
purchasing process. In both cases, they result in a thrown exception with GRPC
statuscodeUNAVAILABLE. Thisisaresultofthefirsttwofaultinjections: first,afault
injectedonthegetUsermethod;second,afaultinjectedonthegetCartmethod.
Next,toensurethestateofthesystemisconsistentwheneveraGRPCexception
withstatuscodeUNAVAILABLEisthrown,thestateofthesystemisdescribed. This
avoidssituationswhereharddependenciesfailandresultinthrownexceptions,but
thestateofthesystemisdifferentinbothcases. Here,itisstatedpreciselythatno
transfer of funds should have occurred, and that the updateCart method should

SingleAdjustmentExample 169
nothavebeeninvoked. ItisalsostatedthatinvocationofotherdownstreamRPCs
are OK because they are read-only: getCart and getAdjustment. This statement
is required for both the first and second fault injections, as it must be written to
proceedtothesecondfaultinjectionscenario.
Next, it is stated that if the RPC to getAdjustment fails, the RPC will not be
invoked, with side effects, udpateCart and that the customer will pay total price.
Finally,itisstatedthatiftheupdateCartRPCfails,thecustomerwillpaytotalprice.
Theseareexamplesofsoftdependencies.
1 @Override
| public | void | failureBlock() |     |     | {   |     |     |     |
| ------ | ---- | -------------- | --- | --- | --- | --- | --- | --- |
2
|     | // Any | failure | of  | the | getUser | call | results | in  |
| --- | ------ | ------- | --- | --- | ------- | ---- | ------- | --- |
3
|     | // upstream |     | receiving |     | UNAVAILABLE |     | exception. |     |
| --- | ----------- | --- | --------- | --- | ----------- | --- | ---------- | --- |
4
assertFaultThrows(
5
UserServiceGrpc.getGetUserMethod(),
6
Status.Code.UNAVAILABLE,
7
|     | "Purchase |     | could | not | be  | completed | at  | this time, |
| --- | --------- | --- | ----- | --- | --- | --------- | --- | ---------- |
8
|     |     | please | retry |     | the request: |     |     |     |
| --- | --- | ------ | ----- | --- | ------------ | --- | --- | --- |
9
| 10  |     | cart | could | not | be retrieved." |     |     |     |
| --- | --- | ---- | ----- | --- | -------------- | --- | --- | --- |
);
11
12
|     | // Any | failure | of  | the | getCart | call | results | in  |
| --- | ------ | ------- | --- | --- | ------- | ---- | ------- | --- |
13
|     | // upstream |     | receiving |     | UNAVAILABLE |     | exception. |     |
| --- | ----------- | --- | --------- | --- | ----------- | --- | ---------- | --- |
14
assertFaultThrows(
15
CartServiceGrpc.getGetCartMethod(),
16
Status.Code.UNAVAILABLE,
17
|     | "Purchase |     | could | not | be  | completed | at  | this time, |
| --- | --------- | --- | ----- | --- | --- | --------- | --- | ---------- |
18
| 19  |     | please | retry |     | the request:   |     |     |     |
| --- | --- | ------ | ----- | --- | -------------- | --- | --- | --- |
|     |     | cart   | could | not | be retrieved." |     |     |     |
20
);
21
22
|     | // State | what | the | state | of  | the system | on  | UNAVAILABLE. |
| --- | -------- | ---- | --- | ----- | --- | ---------- | --- | ------------ |
23
|     | assertOnException(Status.Code.UNAVAILABLE, |     |     |     |     |     |     | () -> { |
| --- | ------------------------------------------ | --- | --- | --- | --- | --- | --- | ------- |
24
|     | //  | Verify | transaction |     | did | not | occur. |     |
| --- | --- | ------ | ----------- | --- | --- | --- | ------ | --- |
25
assertEquals(
26
20000,
27
| 28  |     | PurchaseWorkflowWithPricingAdjustmentService |     |     |     |     |     |     |
| --- | --- | -------------------------------------------- | --- | --- | --- | --- | --- | --- |
.getAccountBalance(consumerId));
29
assertEquals(
30
0,
31

170 Usingp-SFIT:ATutorial
| 32  |     | PurchaseWorkflowWithPricingAdjustmentService |     |     |     |     |
| --- | --- | -------------------------------------------- | --- | --- | --- | --- |
.getAccountBalance(merchantId));
33
34
|     | //  | Notify | the system | some | endpoints | are read-only |
| --- | --- | ------ | ---------- | ---- | --------- | ------------- |
35
|     | //  | and | therefore OK | to skip |     |     |
| --- | --- | --- | ------------ | ------- | --- | --- |
36
|     | //  | when | one returns | a failure. |     |     |
| --- | --- | ---- | ----------- | ---------- | --- | --- |
37
readOnlyRpc(CartServiceGrpc.getGetCartMethod());
38
readOnlyRpc(
39
PricingAdjustmentServiceGrpc
40
| 41  |     |     | .getGetAdjustmentMethod()); |     |     |     |
| --- | --- | --- | --------------------------- | --- | --- | --- |
42
|     | //  | Ensure | one did | not update |     | the cart. |
| --- | --- | ------ | ------- | ---------- | --- | --------- |
43
sideEffectingRpc(
44
CartServiceGrpc.getUpdateCartMethod(), 0);
45
});
46
47
|     | // Failure |     | of the getAdjustment |     | call | results |
| --- | ---------- | --- | -------------------- | --- | ---- | ------- |
48
|     | // in | no discount | (and | no call | to  | updateCart.) |
| --- | ----- | ----------- | ---- | ------- | --- | ------------ |
49
| 50  | assertOnFault( |     |     |     |     |     |
| --- | -------------- | --- | --- | --- | --- | --- |
PricingAdjustmentServiceGrpc
51
.getGetAdjustmentMethod(),
52
Hello.GetDiscountRequest.newBuilder()
53
.setCode("FIRST-TIME")
54
.build(),
55
|     | ()  | -> { |     |     |     |     |
| --- | --- | ---- | --- | --- | --- | --- |
56
assertTestBlock(10000);
57
sideEffectingRpc(CartServiceGrpc
58
| 59  |     |     | .getUpdateCartMethod(), |     |     | 0); |
| --- | --- | --- | ----------------------- | --- | --- | --- |
}
60
);
61
62
|     | // Failure |     | of the updateCart |     | call | results |
| --- | ---------- | --- | ----------------- | --- | ---- | ------- |
63
|     | // in | no discount. |     |     |     |     |
| --- | ----- | ------------ | --- | --- | --- | --- |
64
assertOnFault(
65
CartServiceGrpc.getUpdateCartMethod(),
66
|     | ()  | -> { | assertTestBlock(10000); |     |     | }   |
| --- | --- | ---- | ----------------------- | --- | --- | --- |
67
| 68  | );  |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |
}
69

MultipleAdjustmentExample 171
A.2 Multiple Adjustment Example
TodemonstratehowFilibuster supportsencodingtheapplication’sbehaviorunder
faultwhenmultiplefaultsareinjectedatthesametime,afewsmallmodificationsto
ourapplication. Insteadofonlyseeingifthecustomeriseligibleforasinglepricing
adjustment, the application should attempt to look up discounts using multiple
discountcodes,anddependingonwhichRPCssucceed,applythegreatestdiscount
value. Therefore, the amountthe customer is charged is now dependenton which
RPCssucceed.
A.2.1 Updating the Happy Path Test
First,itisnecessarytoaddthenewstubsfortheadditionalcallstolookupdifferent
discountcodesinthestubBlock.
stubFor(PricingAdjustmentServiceGrpc
1
.getGetAdjustmentMethod(),
2
Hello.GetDiscountRequest.newBuilder()
3
.setCode("FIRST-TIME")
4
.build(),
5
Hello.GetDiscountResponse.newBuilder()
6
.setPercent("10")
7
.build());
8
9
stubFor(PricingAdjustmentServiceGrpc
10
.getGetAdjustmentMethod(),
11
Hello.GetDiscountRequest.newBuilder()
12
.setCode("RETURNING")
13
.build(),
14
Hello.GetDiscountResponse.newBuilder()
15
.setPercent("5")
16
.build());
17
18
stubFor(PricingAdjustmentServiceGrpc
19
.getGetAdjustmentMethod(),
20
Hello.GetDiscountRequest.newBuilder()
21
.setCode("DAILY")
22
.build(),
23
Hello.GetDiscountResponse.newBuilder()
24
.setPercent("1")
25

172 Usingp-SFIT:ATutorial
.build());
26
27
stubFor(CartServiceGrpc
28
.getUpdateCartMethod(),
29
Hello.UpdateCartRequest.newBuilder()
30
.setCartId(cartId.toString())
31
.setDiscountAmount("10").build(),
32
Hello.UpdateCartResponse.newBuilder()
33
.setCartId(cartId.toString())
34
.setTotal("9000").build());
35
36
stubFor(CartServiceGrpc.getUpdateCartMethod(),
37
Hello.UpdateCartRequest.newBuilder()
38
.setCartId(cartId.toString())
39
.setDiscountAmount("5").build(),
40
Hello.UpdateCartResponse.newBuilder()
41
.setCartId(cartId.toString())
42
.setTotal("9500").build());
43
44
stubFor(CartServiceGrpc.getUpdateCartMethod(),
45
Hello.UpdateCartRequest.newBuilder()
46
.setCartId(cartId.toString())
47
.setDiscountAmount("1").build(),
48
Hello.UpdateCartResponse.newBuilder()
49
.setCartId(cartId.toString())
50
.setTotal("9900").build());
51
Next,theexpectedinvocationcountsforeachstubintheassertStubBlockmust
beupdated,otherwiseFilibuster willnotproceedpasttheinitial,referenceexecu-
tion.
for (Map.Entry<String, String> discountCode :
1
PurchaseWorkflow.getDiscountCodes()) {
2
Hello.GetDiscountRequest request =
3
Hello.GetDiscountRequest.newBuilder()
4
.setCode(discountCode.getKey()).build();
5
6
verifyThat(
7
PricingAdjustmentServiceGrpc.getGetAdjustmentMethod(),
8

MultipleAdjustmentExample 173
| 9   | request, |     | 1); |     |     |     |     |     |
| --- | -------- | --- | --- | --- | --- | --- | --- | --- |
}
10
| A.2.2 Updating |     | the | Application’s |     | Failure |     | Behavior |     |
| -------------- | --- | --- | ------------- | --- | ------- | --- | -------- | --- |
InthefailureBlock,itisnecessarytostartconsideringhowthesefaultscanimpact
theapplicationinisolation. Here,itisnecessarytostatethatifthe10%discountis
notapplied,the5%willbe;ifeitherthe5%or1%discountfails,the10%discount
willbeapplied.
| // If they | don't | get | 10% | discount | they | will | get | 5%. |
| ---------- | ----- | --- | --- | -------- | ---- | ---- | --- | --- |
1
assertOnFault(
2
PricingAdjustmentServiceGrpc.getGetAdjustmentMethod(),
3
| 4   | Hello.GetDiscountRequest.newBuilder() |                        |     |     |     |     |     |     |
| --- | ------------------------------------- | ---------------------- | --- | --- | --- | --- | --- | --- |
| 5   |                                       | .setCode("FIRST-TIME") |     |     |     |     |     |     |
.build(),
6
|     | () -> | { assertTestBlock(9500); |     |     |     | }   |     |     |
| --- | ----- | ------------------------ | --- | --- | --- | --- | --- | --- |
7
);
8
9
| // If either |     | the 5% | or 1% | fail | or succeed, |     |     |     |
| ------------ | --- | ------ | ----- | ---- | ----------- | --- | --- | --- |
10
| // the 10% | will | be  | applied. |     |     |     |     |     |
| ---------- | ---- | --- | -------- | --- | --- | --- | --- | --- |
11
assertOnFault(
12
| 13  | PricingAdjustmentServiceGrpc.getGetAdjustmentMethod(), |     |     |     |     |     |     |     |
| --- | ------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- |
| 14  | this::assertTestBlock                                  |     |     |     |     |     |     |     |
);
15
Next,itisnecessarytostartthinkingaboutcompositionsoffaults. Forexample,
what happens if both the 10% and 5% requests fail? Then, the user will get a 1%
discount.
| // What | happens | if  | the 10% | and | 5% fail | together? |     | 1%. |
| ------- | ------- | --- | ------- | --- | ------- | --------- | --- | --- |
1
| CompositeFaultSpecification |     |     |     | firstTwoDiscounts |     |     |     | =   |
| --------------------------- | --- | --- | --- | ----------------- | --- | --- | --- | --- |
2
new CompositeFaultSpecification.Builder()
3
.faultOnRequest(
4
PricingAdjustmentServiceGrpc.getGetAdjustmentMethod(),
5
| 6   | Hello.GetDiscountRequest.newBuilder() |     |     |     |     |     |     |     |
| --- | ------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
.setCode("FIRST-TIME").build())
7
.faultOnRequest(
8
PricingAdjustmentServiceGrpc.getGetAdjustmentMethod(),
9

174 Usingp-SFIT:ATutorial
Hello.GetDiscountRequest.newBuilder()
10
.setCode("RETURNING").build())
11
.build();
12
assertOnFault(firstTwoDiscounts, () -> { assertTestBlock(9900); });
13
This must then be repeated for each composition of failures for all possible
discount codes. Even the combination where allthree fail. In each of these cases,
thetestcannotdeterminethecode’soutcomewhenthefailuresoccur.
// What happens if all three fail?
1
CompositeFaultSpecification allDiscounts =
2
new CompositeFaultSpecification.Builder()
3
.faultOnRequest(
4
PricingAdjustmentServiceGrpc.getGetAdjustmentMethod(),
5
Hello.GetDiscountRequest.newBuilder()
6
.setCode("FIRST-TIME").build())
7
.faultOnRequest(
8
PricingAdjustmentServiceGrpc.getGetAdjustmentMethod(),
9
Hello.GetDiscountRequest.newBuilder()
10
.setCode("RETURNING").build())
11
.faultOnRequest(
12
PricingAdjustmentServiceGrpc.getGetAdjustmentMethod(),
13
Hello.GetDiscountRequest.newBuilder()
14
.setCode("DAILY").build())
15
.build();
16
assertOnFault(allDiscounts, () -> { assertTestBlock(10000); });
17
From here, the developer will have to consider what happens when the first
twodiscountcodegetAdjustmentRPCsfailincombinationwiththeupdateCartcall,
whereno discountwillbeapplied becausethecartcannotbeupdated. Thisisnot
includedhereforbrevity.
✓Asdemonstrated, -SFITcansurfaceandprovokethedeveloperintothink-
p
ingaboutfailurescenariostheymaynothaveimagined: thefirsttwodiscount
lookupsfail,theuseronlygetsa1%discount,butbecausethecartcouldnot
beupdated,theyendupwithoutadiscount.

AddingAnotherSoftDependency 175
A.3 Adding Another Soft Dependency
Let’s assume that one may want to add one more piece of functionality to our
applicationwhereanemailissenttotheuserafterpurchase. Thiswillbedonewith
anewRPConthecartservice,notifyOrder.
As one does not want to abort the entire purchasing process if they cannot
send the email, this is another example of a soft dependency that the user will not
immediatelyseetheeffectof(ornotevenbeawarethatitshouldhavehappened.)
First,itisnecessarytoupdateboththestubBlockandassertStubBlockstostub
andverifytheinvocationofthestub. Next,itisnecessarytoupdatethefailureBlock
toindicate thatwhenthis RPCfails, itdid notaffectthe outcomeofthe test(other
thanthestubnotbeinginvoked.)
assertFaultHasNoImpact(CartServiceGrpc.getNotifyOrderMethod());
1
Finally,isitrequiredtowriteassertionstocapturethefailureofthenotifyOrder
RPCthatsendstheemailwithallpossiblecombinationsoffailuresofthegetAdjustment
RPCcalls?
✓No, compositionalreasoningwill inferautomatically, andcheck withtest
execution,thatexecutionswheresomecombinationofgetAdjustmentRPCs
failwithnotifyOrderRPCactthesamewayasinvocationswheretheemail
canbesent.
A.4 Takeaways
As demonstrated, p-SFIT’s structured test interface not only assists application
developers in writing better happy path functional tests for their microservice
applicationsbutalsoenforcesthattheyauthorthosetestsinsuchawaythatcanbe
usedtoidentifybugsrelatedtoamicroserviceapplication’sfailurehandlingcode.
Insteadof relyingonthe developer tounderstandwhat thepossibleimpacts of
afaultare,p-SFITpromptsthemwhenfaultsareinjectedtoensurethattheeffects
ofthatfaultareexplicitly encoded,therebyavoidingsituationswheredevelopers
ignoretheimpactoffailuresthatseeminglydonotaffecttheirapplication.
Whenever possible, this structured way of writing tests also enables compo-
sitional reasoning, preventing developers from writing individual test cases and
assertionsforeachfailurescenariothatcombinesalreadyobservedfailures. Only
whenthesystemcannotdeterminethesystem’sbehaviororwhenanexistingas-
sumptiondoesnotholdisthedeveloperrequiredtospecifythebehaviormanually.

| Appendix |     | B   |
| -------- | --- | --- |
Availability
All contributions of this dissertation are available as open source and licensed
under the Apache 2 license. These can be both found on GitHub as part of the
filibuster-testingorganization[Fila]andatthefollowingindividualDOIs,part
| ofthemain | Filibuster | reproductionpackage[Mei24a]: |
| --------- | ---------- | ---------------------------- |
• theFilibuster corpusreferenceset[Mei24c],usedtoconstructthecorpus;
| • theFilibuster |     | corpus[Mei24b];                         |
| --------------- | --- | --------------------------------------- |
| • theFilibuster |     | PythonImplementation[Mei24g];           |
| • theFilibuster |     | JavaImplementation[Mei24e];             |
| • theFilibuster |     | IntelliJIDEplugin[Mei24d];and           |
| • theFilibuster |     | implementationforOpenTelemetry[Mei24f]. |
Additionally, the Filibuster plugin for IntelliJ can be found on the JetBrains
marketplace[Filb].
177

List of Algorithms
1 SFITAlgorithm: Search . . . . . . . . . . . . . . . . . . . . . . . . . . . 68
2 SFITAlgorithm: SchedulingNewTests . . . . . . . . . . . . . . . . . . 70
3 SFITAlgorithm: EncapsulatedServiceReduction . . . . . . . . . . . . 76
4 SFITAlgorithm: SearchwithESR . . . . . . . . . . . . . . . . . . . . . 77
179

List of Figures
3.1 Audibleapplicationwithadescriptionoftheaudiobookretrievalprocess. 27
3.2 Industryexamplesinthemicroserviceapplicationcorpus. . . . . . . . . 30
4.1 Cinemaexamplesinthemicroserviceapplicationcorpus. . . . . . . . . . 39
5.1 RPCsignaturealonecannotdistinguishbetweentheRPCsissuedonlines
3and4;callstackorinvocationcountmustbecombinedwithsignature. 48
5.2 Signaturecombinedwithinvocationcountinsufficientindistinguishing
2nd iteration of loop from 1st invocation of failure handler; signature
combinedwithcallstackinsufficientindistinguishingloopiterations. . . 50
5.3 RPCsignature,whenextendedwithinvocationcountandcallstack,is
insufficientwhendifferentincomingRPCrequeststriggerRPCinvocation. 52
5.4 Scheduling nondeterminism can permute the assignment of identifiers.
In this case,𝐴7| , can refer to the RPC invocation from either the 1st or
1
2nd loopiteration. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 54
6.1 SFIT’sfaultinjectionpredicatesareusedtoupdateatesttocapturean
application’sbehaviorunderfault. Yellowindicatesaddedlinesduring
SFITprocess. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 71
7.1 ArchitectureofPython Filibuster . . . . . . . . . . . . . . . . . . . . . . . 81
7.2 Percentageofexecutionswithdeterministicassignmentfortwothreads. 86
10.1 PurchaseApplicationStructurewith Filibuster Instrumentation . . . . . 118
10.2 PurchaseApplicationWorkflowwithGracefulDegradation . . . . . . . 119
11.1 Filibuster IntelliJ plugin visualizes the intercepted RPC invocations and
theirargumentsandresponses. . . . . . . . . . . . . . . . . . . . . . . . . 136
11.2 Filibuster iteration where a StatusRuntimeException is injected in the
RPCinvocationtoUpdateCart. . . . . . . . . . . . . . . . . . . . . . . . . . 137
180

ListofFigures 181
11.3 Iteration,whereFilibuster injectedaStatusRuntimeExceptionwiththe
codeUNAVAILABLEinGetUser. Thetestfailssincetheapplicationbehavior
isnot definedforthisfault. The Filibuster pluginshowsrecommenda-
tions regarding API methods thatcan be used to define the application
behavior. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 139
11.4 Popupthatappearswhenoneoftherecommendationsisclicked. The
popupshowsthedocumentationpageoftherespectivemethodin Fili-
buster’sAPI. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 140
11.5 Testingprocedureforp-SFIT. . . . . . . . . . . . . . . . . . . . . . . . . . 141

List of Tables
7.1 Resultsdemonstrating alltechniquesmustbe combinedforcorrect iden-
tification. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 83
7.2 Python Filibuster evaluated on the corpus. Includes the number of
generatedtestswithandwithoutencapsulatedservicereduction;cover-
agebefore and afterusing Python Filibuster, overheadof encapsulated
servicereductionalgorithm,andoverheadoftestgeneration. . . . . . . . 88
11.1 Table of p-SFIT-enabled Filibuster assertion API and usage blocks for
eachAPImethod. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 134
182

List of Definitions
1 Definition(HardDependency) . . . . . . . . . . . . . . . . . . . . . . 26
2 Definition(SoftDependency) . . . . . . . . . . . . . . . . . . . . . . . 26
3 Definition(LatentBug) . . . . . . . . . . . . . . . . . . . . . . . . . . 29
4 Definition(ActiveBug) . . . . . . . . . . . . . . . . . . . . . . . . . . 30
5 Definition(GracefulDegradation) . . . . . . . . . . . . . . . . . . . . 32
6 Definition(Soundness) . . . . . . . . . . . . . . . . . . . . . . . . . . . 46
7 Definition(Completeness) . . . . . . . . . . . . . . . . . . . . . . . . . 46
8 Definition(Correctness) . . . . . . . . . . . . . . . . . . . . . . . . . . 46
9 Definition(Signature) . . . . . . . . . . . . . . . . . . . . . . . . . . . 47
10 Definition(SynchronousInvocationSignature) . . . . . . . . . . . . . 50
11 Definition(SynchronousDistributedExecutionIndex) . . . . . . . . 53
12 Definition(InvocationPayload) . . . . . . . . . . . . . . . . . . . . . . 55
13 Definition(AsynchronousInvocationSignature) . . . . . . . . . . . . 56
14 Definition(DistributedExecutionIndex) . . . . . . . . . . . . . . . . 56
15 Definition(FaultConfiguration) . . . . . . . . . . . . . . . . . . . . . 66
16 Definition(ConcreteTestExecution) . . . . . . . . . . . . . . . . . . . 67
17 Definition(AbstractTestExecution) . . . . . . . . . . . . . . . . . . . 67
18 Definition(ServiceEncapsulation) . . . . . . . . . . . . . . . . . . . . 74
183

Bibliography
[AAE16a] NuhaAlshuqayran,NourAli,andRogerEvans.“Asystematicmap-
ping study in microservice architecture”. In: 2016 IEEE 9th interna-
tionalconferenceonservice-orientedcomputingandapplications(SOCA).
IEEE.2016,pp.44–51.
[AAE16b] NuhaAlshuqayran,NourAli,andRogerEvans.“ASystematicMap-
pingStudyinMicroserviceArchitecture”.In:2016IEEE9thInterna-
tionalConferenceonService-OrientedComputingandApplications(SOCA).
2016,pp.44–51.doi:10.1109/SOCA.2016.15.
[Abd+23] AmrSAbdelfattah,TomasCerny,JorgeYeroSalazar,AustinLehman,
Joshua Hunter, Ashley Bickham, and Davide Taibi. “End-to-End
Test CoverageMetricsin Microservice Systems:AnAutomatedAp-
proach”.In:EuropeanConferenceonService-OrientedandCloudComput-
ing.Springer.2023,pp.35–51.
[ABH06] CyrilleArtho,ArminBiere,andShinichiHoniden.“ExhaustiveTest-
ing of Exception Handlers with Enforcer”. In: Proceedings of the 5th
International Conferenceon Formal Methodsfor Componentsand Objects.
FMCO’06.Amsterdam,TheNetherlands:Springer-Verlag,2006,26–46.
isbn:3540747915.
[Alv+16a] Peter Alvaro, Kolton Andrus, Chris Sanden, Casey Rosenthal, Ali
Basiri,andLorinHochstein.“AutomatingFailureTestingResearch
at Internet Scale”. In: Proceedings of the Seventh ACM Symposium on
Cloud Computing. SoCC ’16. Santa Clara, CA, USA: Association for
Computing Machinery, 2016, 17–28. isbn: 9781450345255. doi: 10.
1145/2987550.2987555. url: https://doi.org/10.1145/2987550.
2987555.
[Alv+16b] Peter Alvaro, Kolton Andrus, Chris Sanden, Casey Rosenthal, Ali
Basiri,andLorinHochstein.“AutomatingFailureTestingResearch
at Internet Scale”. In: Proceedings of the Seventh ACM Symposium on
Cloud Computing. SoCC ’16. Santa Clara, CA, USA: Association for
185

186 Bibliography
Computing Machinery, 2016, 17–28. isbn: 9781450345255. doi: 10.
1145/2987550.2987555. url: https://doi.org/10.1145/2987550.
2987555.
[AMS13] SheevaAfshan, Phil McMinn,and Mark Stevenson. “Evolving Read-
ableStringTestInputsUsingaNaturalLanguageModeltoReduce
HumanOracleCost”.In:2013IEEESixthInternationalConferenceon
Software Testing, Verification and Validation. 2013, pp. 352–361. doi:
10.1109/ICST.2013.11.
[ARH15a] Peter Alvaro, Joshua Rosen, and Joseph M. Hellerstein. “Lineage-
Driven Fault Injection”. In: Proceedings of the 2015 ACM SIGMOD
International Conference on Management of Data. SIGMOD ’15. Mel-
bourne, Victoria, Australia: Association for Computing Machinery,
2015, 331–346. isbn: 9781450327589. doi: 10.1145/2723372.2723711.
url:https://doi.org/10.1145/2723372.2723711.
[ARH15b] Peter Alvaro, Joshua Rosen, and Joseph M. Hellerstein. “Lineage-
Driven Fault Injection”. In: Proceedings of the 2015 ACM SIGMOD
International Conference on Management of Data. SIGMOD ’15. Mel-
bourne, Victoria, Australia: Association for Computing Machinery,
2015, 331–346. isbn: 9781450327589. doi: 10.1145/2723372.2723711.
url:https://doi.org/10.1145/2723372.2723711.
[Ass23] Michael Assad. Service-Level Byzantine and Exception Fault Injection in
DatabaseswithinMicroserviceApplications.2023.
[Ass+24] MichaelAssad,ChristopherMeiklejohn,HeatherMiller,andStephan
Krusche. “Can My Microservice Tolerate an Unreliable Database?
ResilienceTestingwithFaultInjectionandVisualization”.In:arXiv
preprintarXiv:2404.01886(2024).
[Atc19] Lee Atchison. How Service Tiers Can Help to Avoid Microservices Dis-
asters. https://thenewstack.io/how-service-tiers-can-help-to-
avoid-microservices-disasters/.Accessed:2023-07-21.2019.
[Aud] Audible.https://www.audible.com.Accessed:2021-05-21.2021.
[aut22] Anonymizedauthors.“Suppressedtitle”.In:ID:2.2022.
[Avi+04] A.Avizienis,J.-C.Laprie,B.Randell,andC.Landwehr.“Basiccon-
ceptsandtaxonomyofdependableandsecurecomputing”.In:IEEE
TransactionsonDependableandSecureComputing 1.1(2004),pp.11–33.
doi:10.1109/TDSC.2004.2.

Bibliography 187
[Bal+18] Armin Balalaie, Abbas Heydarnoori, Pooyan Jamshidi, Damian A
Tamburri, and Theo Lynn. “Microservices migration patterns”. In:
Software:PracticeandExperience 48.11(2018),pp.2019–2042.
[Bas+16] Ali Basiri, Niosha Behnam, Ruud de Rooij, Lorin Hochstein, Luke
Kosewski,Justin Reynolds, andCasey Rosenthal.“Chaos Engineer-
ing”.In:IEEESoftware 33.3(2016),pp.35–41.doi:10.1109/MS.2016.
60.
[Bas+19a] AliBasiri,LorinHochstein,NoraJones,andHaleyTucker.“Automat-
ingChaosExperimentsinProduction”.In:2019IEEE/ACM41stIn-
ternational Conference on Software Engineering: Software Engineering in
Practice(ICSE-SEIP).2019,pp. 31–40.doi:10.1109/ICSE-SEIP.2019.
00012.
[Bas+19b] AliBasiri,LorinHochstein,NoraJones,andHaleyTucker.“Automat-
ing chaos experiments in production”. In: 2019 IEEE/ACM 41st In-
ternational Conference on Software Engineering: Software Engineering in
Practice(ICSE-SEIP).IEEE.2019,pp.31–40.
[BC12a] RaduBanabicandGeorgeCandea.“FastBlack-BoxTestingofSystem
Recovery Code”. In: Proceedings of the 7th ACM European Conference
on Computer Systems. EuroSys ’12. Bern, Switzerland: Association
forComputingMachinery,2012,281–294.isbn:9781450312233.doi:
10.1145/2168836.2168865. url: https://doi.org/10.1145/2168836.
2168865.
[BC12b] RaduBanabicandGeorgeCandea.“FastBlack-BoxTestingofSystem
Recovery Code”. In: Proceedings of the 7th ACM European Conference
on Computer Systems. EuroSys ’12. Bern, Switzerland: Association
forComputingMachinery,2012,281–294.isbn:9781450312233.doi:
10.1145/2168836.2168865. url: https://doi.org/10.1145/2168836.
2168865.
[BC13] YvesBertotandPierreCastéran.Interactivetheoremprovingandprogram
development: Coq’Art: the calculus of inductive constructions. Springer
Science&BusinessMedia,2013.
[BHJ16] ArminBalalaie,AbbasHeydarnoori,andPooyanJamshidi.“Microser-
vicesArchitectureEnablesDevOps:MigrationtoaCloud-NativeAr-
chitecture”.In:IEEESoftware 33.3(2016),pp.42–52.doi:10.1109/MS.
2016.64.

188 Bibliography
[BST02a] Pete Broadwell, Naveen Sastry, and Jonathan Traupman. “FIG: A
prototype tool for online verification of recovery mechanisms”. In:
WorkshoponSelf-Healing,AdaptiveandSelf-ManagedSystems.Citeseer.
2002.
[BST02b] Pete Broadwell, Naveen Sastry, and Jonathan Traupman. “FIG: A
prototype tool for online verification of recovery mechanisms”. In:
WorkshoponSelf-Healing,AdaptiveandSelf-ManagedSystems.Citeseer.
2002.
[Bui] Building Microservices in Python and Flask. https://codeahoy.com/
2016/07/10/writing-microservices-in-python-using-flask.
Accessed:2021-05-21.2016.
[Cel20] CesareCelozzi.Future-proofing:HowDoorDashTransitionedfromaCode
MonolithtoaMicroserviceArchitecture.https://doordash.engineering/
2020/12/02/how-doordash-transitioned-from-a-monolith-to-
microservices/.Accessed:2023-07-21.2020.
[Chaa] ChaosBlade.https://chaosblade.io.Accessed:2022-06-05.2022.
[Chab] “Chaos Engineering Saved Your Netflix Extreme stress testing of
onlineplatformshasbecomeitsownscience”.In:IEEESpectrum58.3
(2021),pp.4–10.issn:1939-9340.doi:10.1109/MSPEC.2021.9370069.
[Chac] ChaosMesh.https://chaos-mesh.org.Accessed:2022-06-05.2022.
[Chad] ChaosToolkit.https://chaostoolkit.org.Accessed:2022-06-05.2022.
[Che+23] Yinfang Chen,XudongSun, SumanNath, ZeYang,and Tianyin Xu.
“{Push-Button} Reliability Testing for {Cloud-Backed} Applications
withRainmaker”.In:20thUSENIXSymposiumonNetworkedSystems
DesignandImplementation(NSDI23).2023,pp.1701–1716.
[Daw+96] S. Dawson, F. Jahanian, T. Mitton, and Teck-Lee Tung. “Testing of
Fault-TolerantandReal-TimeDistributedSystemsviaProtocolFault
Injection”. In: Proceedings of the The Twenty-Sixth Annual International
Symposium on Fault-Tolerant Computing (FTCS ’96). FTCS ’96. USA:
IEEEComputerSociety,1996,p.404.isbn:0818672617.
[Deu94] PeterDeutsch.“Theeightfallaciesofdistributedcomputing”.In:URL:
http://today.java.net/jag/Fallacies.html(1994).
[Fid91] C. Fidge.“Logical timein distributedcomputing systems”.In: Com-
puter 24.8(1991),pp.28–33.doi:10.1109/2.84874.
[Fila] Filibuster.http://filibuster.cloud.Accessed:2021-09-07.2021.

Bibliography 189
[Filb] Filibuster (for MacOS, Linux). https://plugins.jetbrains.com/
plugin/21057-filibuster-for-macos-linux-.Accessed:2024-04-27.
2024.
[Gan+19] Yu Gan, Yanqi Zhang, Dailun Cheng, Ankitha Shetty, Priyal Rathi,
Nayan Katarki, Ariana Bruno, Justin Hu, Brian Ritchken, Brendon
Jackson,etal.“Anopen-sourcebenchmarksuiteformicroservicesand
theirhardware-softwareimplicationsforcloud&edgesystems”.In:
ProceedingsoftheTwenty-FourthInternationalConferenceonArchitectural
SupportforProgrammingLanguagesandOperatingSystems.2019,pp.3–
18.
[GKS05] PatriceGodefroid,NilsKlarlund,andKoushikSen.“DART:Directed
automatedrandomtesting”.In:Proceedingsofthe2005ACMSIGPLAN
conference on Programming language design and implementation. 2005,
pp.213–223.
[Gra] Grafana.https://grafana.io.Accessed:2024-05-01.2024.
[Grea] Gremlin.http://www.gremlin.com.Accessed:2021-05-21.2021.
[Greb] Gremlin.http://www.gremlin.com.Accessed:2021-05-21.2021.
[Gun+11] Haryadi S. Gunawi, Thanh Do, Pallavi Joshi, Peter Alvaro, JosephM.
Hellerstein,AndreaC.Arpaci-Dusseau,RemziH.Arpaci-Dusseau,
KoushikSen,andDhrubaBorthakur.“FATEandDESTINI:AFrame-
workforCloudRecoveryTesting”.In:Proceedingsofthe8thUSENIX
ConferenceonNetworkedSystemsDesignandImplementation.NSDI’11.
Boston,MA:USENIXAssociation,2011,238–252.
[GY11] RachidGuerraouiandMaysamYabandeh.“ModelCheckingaNet-
worked System Without the Network”. In: 8th USENIX Symposium
on Networked Systems Design and Implementation (NSDI 11). Boston,
MA:USENIXAssociation,Mar.2011.url:https://www.usenix.org/
conference/nsdi11/model-checking-networked-system-without-
network.
[Har] Harness:The ModernSoftwareDelivery Platform.https://harness.io.
Accessed:2024-05-01.2024.
[Heo+16a] Victor Heorhiadi, Shriram Rajagopalan, Hani Jamjoom, Michael K.
Reiter,andVyasSekar.“Gremlin:SystematicResilienceTestingofMi-
croservices”.In:2016IEEE36thInternationalConferenceonDistributed
Computing Systems (ICDCS). 2016, pp. 57–66. doi: 10.1109/ICDCS.
2016.11.

190 Bibliography
[Heo+16b] Victor Heorhiadi, Shriram Rajagopalan, Hani Jamjoom, Michael K.
Reiter,andVyasSekar.“Gremlin:SystematicResilienceTestingofMi-
croservices”.In:2016IEEE36thInternationalConferenceonDistributed
Computing Systems (ICDCS) (2016), pp. 57–66. doi: 10.1109/ICDCS.
2016.11.
[Hig20] High Scalability Blog. http://highscalability.com/blog/2020/
4/8/one-team-at-uber-is-moving-from-microservices-to-
macroservic.html.Accessed:2023-07-21.2020.
[Hil23] Jeremy Hillpot. 4 Microservices Examples: Amazon, Netflix, Uber, and
Etsy. https://blog.dreamfactory.com/microservices-examples/.
Accessed:2023-07-21.2023.
[Hip] OnlineBoutique.https://github.com/GoogleCloudPlatform/microservices-
demo.Accessed:2021-05-21.2021.
[HSS23] DarbyHuye,YuriShkuro,andRajaR.Sambasivan.“Liftingtheveilon
Meta’s microservice architecture: Analyses of topology and request
workflows”.In:2023USENIXAnnualTechnicalConference(USENIX
ATC23).Boston,MA:USENIXAssociation,July2023,pp.419–432.
isbn: 978-1-939133-35-9. url: https://www.usenix.org/conference/
atc23/presentation/huye.
[Jae] Jaeger.https://jaegertracing.io.Accessed:2024-05-01.2024.
[Jam+18a] PooyanJamshidi,ClausPahl,NaborCMendonça,JamesLewis,and
Stefan Tilkov. “Microservices: The journey so far and challenges
ahead”.In:IEEESoftware 35.3(2018),pp.24–35.
[Jam+18b] PooyanJamshidi,ClausPahl,NaborCMendonça,JamesLewis,and
Stefan Tilkov. “Microservices: The journey so far and challenges
ahead”.In:IEEESoftware 35.3(2018),pp.24–35.
[JC18] Jay Judkowitz and Mark Carter. SRE fundamentals: SLIs, SLAs and
SLOs. https://cloud.google.com/blog/products/devops-sre/sre-
fundamentals-slis-slas-and-slos.Accessed:2023-07-21.2018.
[JC19] ChristinaTereseJosephandKChandrasekaran.“Straddlingthecrevasse:
Areviewofmicroservicesoftwarearchitecturefoundationsandre-
centadvancements”.In:Software: PracticeandExperience 49.10(2019),
pp.1448–1484.

Bibliography 191
[JD10] Lukasz Juszczykand SchahramDustdar.“Programmable FaultInjec-
tionTestbedsforComplexSOA”.In:Service-OrientedComputing.Ed.
byPaulP.Maglio,MathiasWeske, JianYang,andMarceloFantinato.
Berlin, Heidelberg: Springer Berlin Heidelberg, 2010, pp. 411–425.
isbn:978-3-642-17358-5.
[JGS11] Pallavi Joshi, Haryadi S. Gunawi, and Koushik Sen. “PREFAIL: A
ProgrammableToolforMultiple-FailureInjection”.In:Proceedingsof
the2011ACMInternationalConferenceonObjectOrientedProgramming
SystemsLanguagesandApplications.OOPSLA’11.Portland, Oregon,
USA: Association for Computing Machinery, 2011, 171–188. isbn:
9781450309400. doi: 10.1145/2048066.2048082. url: https://doi.
org/10.1145/2048066.2048082.
[JM09] Ranjit Jhala and Rupak Majumdar. “Software Model Checking”. In:
ACMComput.Surv.41.4(2009).issn:0360-0300.doi:10.1145/1592434.
1592438.url:https://doi.org/10.1145/1592434.1592438.
[Jos+09] Pallavi Joshi, Chang-Seo Park, Koushik Sen, and Mayur Naik. “A
Randomized Dynamic Program Analysis Technique for Detecting
RealDeadlocks”.In:SIGPLANNot.44.6(June2009),110–120.issn:
0362-1340.doi:10.1145/1543135.1542489.url:https://doi.org/10.
1145/1543135.1542489.
[Jos+13] Pallavi Joshi, Malay Ganai, Gogul Balakrishnan, Aarti Gupta, and
Nadia Papakonstantinou. “SETSUDO: Perturbation-Based Testing
Framework for Scalable Distributed Systems”. In: Proceedings of the
FirstACMSIGOPS Conference on Timely Resultsin Operating Systems.
TRIOS ’13. Farmington, Pennsylvania: Association for Computing
Machinery,2013.isbn:9781450324632.doi:10.1145/2524211.2524217.
url:https://doi.org/10.1145/2524211.2524217.
[Kil+07] Charles Killian, James W. Anderson, Ranjit Jhala, and Amin Vah-
dat.“Life,Death, andtheCriticalTransition: FindingLivenessBugs
in Systems Code”. In:4th USENIX Symposium on NetworkedSystems
Design&Implementation(NSDI07).Cambridge,MA:USENIXAsso-
ciation, Apr. 2007. url: https://www.usenix.org/conference/nsdi-
07/life-death-and-critical-transition-finding-liveness-
bugs-systems-code.
[KKA95] G.A.Kanawati,N.A.Kanawati,andJ.A.Abraham.“FERRARI:aflexi-
blesoftware-basedfaultanderrorinjectionsystem”.In:IEEETransac-
tionsonComputers44.2(1995),pp.248–260.doi:10.1109/12.364536.

192 Bibliography
[Kub23] Kubernetes.Configure Liveness, Readiness and Startup Probes.https://
kubernetes.io/docs/tasks/configure-pod-container/configure-
liveness-readiness-startup-probes/.Accessed:2023-07-21.2023.
[Lee+14] Tanakorn Leesatapornwongsa, Mingzhe Hao, Pallavi Joshi, Jeffrey F.
Lukman,andHaryadiS.Gunawi.“SAMC:Semantic-AwareModel
Checking for Fast Discovery of Deep Bugs in Cloud Systems”. In:
Proceedingsofthe11thUSENIXConferenceonOperatingSystemsDesign
andImplementation.OSDI’14.Broomfield,CO:USENIXAssociation,
2014,399–414.isbn:9781931971164.
[Lei+20] LeonardoLeite,FabioKon,GustavoPinto,andPauloMeirelles.“Build-
ingatheoryofsoftwareteamsorganizationinacontinuousdelivery
context”.In:2020IEEE/ACM42ndInternationalConferenceonSoftware
Engineering: Companion Proceedings (ICSE-Companion). IEEE. 2020,
pp.296–297.
[LF14] JamesLewisandMartinFowler.“Microservices:adefinitionofthis
newarchitecturalterm”.In:MartinFowler.com25(2014),pp.14–26.
[Li+21a] Shanshan Li, He Zhang, Zijia Jia, Chenxing Zhong, Cheng Zhang,
ZhihaoShan,JinfengShen,andMuhammadAliBabar.“Understand-
ingandaddressingqualityattributesofmicroservicesarchitecture:A
Systematicliteraturereview”.In:InformationandSoftwareTechnology
131(2021),p.106449.
[Li+21b] Shanshan Li, He Zhang, Zijia Jia, Chenxing Zhong, Cheng Zhang,
ZhihaoShan,JinfengShen,andMuhammadAliBabar.“Understand-
ingandaddressingqualityattributesofmicroservicesarchitecture:A
Systematicliteraturereview”.In:InformationandSoftwareTechnology
131 (2021), p. 106449. issn: 0950-5849. doi: https://doi.org/10.
1016/j.infsof.2020.106449.url:https://www.sciencedirect.com/
science/article/pii/S0950584920301993.
[Lig] LightStep.https://lightstep.com.Accessed:2023-09-30.2024.
[Lin] LinkedOut:ARequest-LevelFailureInjectionFramework.https://engineering.
linkedin.com/blog/2018/05/linkedout--a-request-level-
failure-injection-framework.Accessed:2021-05-21.2018.
[Lit] Litmus.https://litmuschaos.io.Accessed:2022-06-05.2022.

Bibliography 193
[Luk+19] Jeffrey F. Lukman, Huan Ke, Cesar A. Stuardo, Riza O. Suminto,
DaniarH.Kurniawan,DikaiminSimon,SatriaPriambada,ChenTian,
FengYe,TanakornLeesatapornwongsa,AartiGupta,ShanLu,and
Haryadi S. Gunawi. “FlyMC: Highly Scalable Testing of Complex
Interleavings in Distributed Systems”. In: Proceedings of the Fourteenth
EuroSysConference2019.EuroSys’19.Dresden,Germany:Association
for Computing Machinery, 2019. isbn: 9781450362818. doi: 10.1145/
3302424.3303986.url:https://doi.org/10.1145/3302424.3303986.
[MALH21] HamdyMichaelAyas,PhilippLeitner,andReginaHebig.“TheMigra-
tionJourneyTowardsMicroservices”.In:InternationalConferenceon
Product-FocusedSoftwareProcessImprovement.Springer.2021,pp.20–
35.
[Mat88] FriedemannMattern.“VirtualTimeandGlobalStatesofDistributed
Systems”.In:PARALLELANDDISTRIBUTEDALGORITHMS.North-
Holland,1988,pp.215–226.
[MC09a] PaulD.MarinescuandGeorgeCandea.“LFI:Apracticalandgeneral
library-levelfaultinjector”.In:2009IEEE/IFIPInternationalConference
onDependableSystemsNetworks.2009,pp.379–388.doi:10.1109/DSN.
2009.5270313.
[MC09b] PaulD.MarinescuandGeorgeCandea.“LFI:Apracticalandgeneral
library-levelfaultinjector”.In:2009IEEE/IFIPInternationalConference
onDependableSystemsNetworks.2009,pp.379–388.doi:10.1109/DSN.
2009.5270313.
[McC15] CaitieMcCaffrey.“TheVerificationofaDistributedSystem:APracti-
tioner’sGuidetoIncreasingConfidenceinSystemCorrectness”.In:
Queue 13.9 (2015), 150–160. issn: 1542-7730. doi: 10.1145/2857274.
2889274.url:https://doi.org/10.1145/2857274.2889274.
[Mei+21a] Christopher S Meiklejohn, Andrea Estrada, Yiwen Song, Heather
Miller, and Rohan Padhye. “Service-Level Fault Injection Testing”. In:
ProceedingsoftheACMSymposiumonCloudComputing.2021,pp.388–
402.
[Mei+21b] Christopher S Meiklejohn, Andrea Estrada, Yiwen Song, Heather
Miller,andRohanPadhye.“Service-levelfaultinjectiontesting”.In:
ProceedingsoftheACMSymposiumonCloudComputing.2021,pp.388–
402.

194 Bibliography
[Mei+22] ChristopherMeiklejohn,LydiaStark,CesareCelozzi,MattRanney,
andHeatherMiller.“MethodOverloadingtheCircuit”.In:Proceedings
of the 13th Symposium on Cloud Computing. SoCC ’22. San Francisco,
California: Association for Computing Machinery, 2022, 273–288.
isbn: 9781450394147. doi: 10.1145/3542929.3563466. url: https:
//doi.org/10.1145/3542929.3563466.
[Mei23a] Christopher Meiklejohn. Filibuster 2.0: Byzantine Fault Injection with
Arbitrary Faults. https://christophermeiklejohn.com/filibuster/
2023/09/07/filibuster-2.0-byzantine-arbitrary.html.Accessed:
2024-05-01.2023.
[Mei23b] Christopher Meiklejohn. Filibuster 2.0: Byzantine Fault Injection with
HardcodedFaultValues.https://christophermeiklejohn.com/filibuster/
2023/09/09/filibuster-2.0-byzantine-hardcoded.html.Accessed:
2024-05-01.2023.
[Mei23c] Christopher Meiklejohn. Filibuster 2.0: Computing API coverage of a Mi-
croserviceApplication.https://christophermeiklejohn.com/filibuster/
2023/09/06/filibuster-2.0-API-coverage.html. Accessed: 2024-
05-01.2023.
[Mei23d] Christopher Meiklejohn. Filibuster 2.0: Healthcheck your Functional
Test Suite with API Coverage. https://christophermeiklejohn.com/
filibuster/2023/09/02/filibuster-2.0-01-healthcheck.html.
Accessed:2024-05-01.2023.
[Mei23e] Christopher Meiklejohn. Filibuster 2.0: Microservice Linter, Multiple
InvocationstotheSameRPCMethod.https://christophermeiklejohn.
com/filibuster/2023/09/05/filibuster-2.0-multiple.html.
Accessed:2024-05-01.2023.
[Mei23f] ChristopherMeiklejohn.Filibuster2.0:MicroserviceLinter,Redundant
RPCs. https://christophermeiklejohn.com/filibuster/2023/09/
03/filibuster-2.0-redundant.html.Accessed:2024-05-01.2023.
[Mei23g] Christopher Meiklejohn. Filibuster 2.0: Microservice Linter, Requests
become part of a Response. https://christophermeiklejohn.com/
filibuster/2023/09/04/filibuster-2.0-request-response.html.
Accessed:2024-05-01.2023.
[Mei23h] ChristopherMeiklejohn.Filibuster2.0:RedisFaultInjection.https://
christophermeiklejohn.com/filibuster/2023/09/01/filibuster-
2.0-redis-fault-injection.html.Accessed:2024-05-01.2023.

Bibliography 195
[Mei24a] ChristopherMeiklejohn.Filibuster.2024.doi:10.17605/OSF.IO/G8T4P.
url:osf.io/g8t4p.
[Mei24b] ChristopherMeiklejohn.Filibuster:ApplicationCorpus.2024.doi:10.
17605/OSF.IO/ZVYJN.url:osf.io/zvyjn.
[Mei24c] Christopher Meiklejohn. Filibuster: Corpus References. 2024. doi: 10.
17605/OSF.IO/BJ52A.url:osf.io/bj52a.
[Mei24d] Christopher Meiklejohn. Filibuster: IntelliJ Plugin for Java. 2024. doi:
10.17605/OSF.IO/28B3K.url:osf.io/28b3k.
[Mei24e] Christopher Meiklejohn.Filibuster: JavaImplementation.2024. doi: 10.
17605/OSF.IO/7EWYZ.url:osf.io/7ewyz.
[Mei24f] ChristopherMeiklejohn.Filibuster:OpenTelemetryImplementationfor
Java.2024.doi:10.17605/OSF.IO/4F2AR.url:osf.io/4f2ar.
[Mei24g] ChristopherMeiklejohn.Filibuster:PythonImplementation.2024.doi:
10.17605/OSF.IO/EAH93.url:osf.io/eah93.
[Men+20] NaborC.Mendonca,CarlosM.Aderaldo,JavierCamara,andDavid
Garlan.“Model-BasedAnalysisofMicroserviceResiliencyPatterns”.
In: 2020 IEEEInternational Conference onSoftware Architecture(ICSA).
2020,pp.114–124.doi:10.1109/ICSA47634.2020.00019.
[Mic23a] MichalKaczmarski.Whichcompanyiswinningtherestaurantfooddeliv-
ery war? https://secondmeasure.com/datapoints/food-delivery-
services-grubhub-uber-eats-doordash-postmates/. Accessed:
2023-11-26.2023.
[Mic23b] Microsoft. Bulkhead pattern. https://learn.microsoft.com/en-
us/azure/architecture/patterns/bulkhead. Accessed: 2023-07-21.
2023.
[MRF18] JonathanMace,RyanRoelke,andRodrigoFonseca.“PivotTracing:
DynamicCausalMonitoringforDistributedSystems”.In:ACMTrans.
Comput.Syst.35.4(2018).issn:0734-2071.doi:10.1145/3208104.url:
https://doi.org/10.1145/3208104.
[MW18] FabrizioMontesiandJanineWeber.“From theDecoratorPatternto
CircuitBreakersinMicroservices”.In:Proceedingsofthe33rdAnnual
ACMSymposiumonAppliedComputing.SAC’18.Pau,France:Associa-
tionforComputingMachinery,2018,1733–1735.isbn:9781450351911.
doi: 10.1145/3167132.3167427. url: https://doi.org/10.1145/
3167132.3167427.

196 Bibliography
[Ner+20] Davide Neri, Jacopo Soldani, Olaf Zimmermann, and Antonio Brogi.
“Designprinciples,architecturalsmellsandrefactoringsformicroser-
vices: a multivocal review”. In: SICS Software-Intensive Cyber-Physical
Systems35.1(2020),pp.3–15.doi:10.1007/s00450-019-00407-8.url:
https://doi.org/10.1007/s00450-019-00407-8.
[Neta] FIT: Failure Injection Testing. https://netflixtechblog.com/fit-
failure-injection-testing-35d8e2a9bb2. Accessed: 2022-06-05.
2014.
[Netb] GitHub:Netflix/chaosmonkey.https://github.com/Netflix/chaosmonkey.
Accessed:2022-06-05.2022.
[Netc] GitHub:Netflix/SimianArmy.https://github.com/Netflix/SimianArmy.
Accessed:2022-06-05.2022.
[Netd] Netflix.https://www.netflix.com.Accessed:2021-05-21.2021.
[Nete] TheNetflixSimianArmy-TheNetflixTechnologyBlog.https://netflixtechblog.
com/the-netflix-simian-army-16e57fbab116.Accessed:2022-06-05.
2011.
[Nor17] NoraJones.AWSre:Invent2017:PerformingChaosatNetflixScale(DEV334).
https://www.youtube.com/watch?v=LaKGx0dAUlo. Accessed: 2022-
06-05.2017.
[OEC16] RoryO’Connor,PeterElger, andPaulM Clarke.“Exploringtheim-
pactofsituationalcontext—Acasestudyofasoftwaredevelopment
processforamicroservicesarchitecture”.In:2016IEEE/ACMInterna-
tional Conference on Software and System Processes (ICSSP). IEEE. 2016,
pp.6–10.
[Ope] OpenTelemetry. https://opentelemetry.io. Accessed: 2022-06-05.
2022.
[PJ16] Claus Pahland Pooyan Jamshidi. “Microservices:a systematicmap-
pingstudy.”In:CLOSER(1)(2016),pp.137–146.
[PP21] Dewmini Premarathna and Asanka Pathirana. “Theoretical frame-
work to address the challenges in Microservice Architecture”. In:
2021InternationalResearchConferenceonSmartComputingandSystems
Engineering(SCSE).Vol.4.IEEE.2021,pp.195–202.
[PP22] AashayPalliwarandSrinivasPinisetty.“UsingGossipEnabledDis-
tributed Circuit Breaking for Improving Resiliency of Distributed
Systems”.In:2022IEEE19thInternationalConferenceonSoftwareArchi-
tecture(ICSA).2022,pp.13–23.doi:10.1109/ICSA53651.2022.00010.

Bibliography 197
[PSS17] AurojitPanda,MoolySagiv,andScottShenker.“Verificationinthe
AgeofMicroservices”.In:Proceedingsofthe16thWorkshoponHotTopics
inOperatingSystems.HotOS’17.Whistler,BC,Canada:Association
for Computing Machinery, 2017, 30–36. isbn: 9781450350686. doi:
10.1145/3102980.3102986. url: https://doi.org/10.1145/3102980.
3102986.
[Res] Resiliency in Distributed Systems. https://blog.pragmaticengineer.
com/resiliency-in-distributed-systems/.Accessed:2023-07-21.
[Ret] Rethinking How the Industry Approaches Chaos Engineering. https://
www.infoq.com/presentations/rethinking-chaos-engineering.
Accessed:2021-05-21.2020.
[RJ20a] CaseyRosenthal andNoraJones. Chaosengineering:systemresiliency
inpractice.O’ReillyMedia,2020.
[RJ20b] CaseyRosenthal andNoraJones. Chaosengineering:systemresiliency
inpractice.O’ReillyMedia,2020.
[Rob+12] JesseRobbins,KripaKrishnan,JohnAllspaw,andThomasA.Limon-
celli. “Resilience Engineering: Learning to Embrace Failure: A Dis-
cussionwithJesseRobbins,KripaKrishnan,JohnAllspaw,andTom
Limoncelli”. In: Queue 10.9 (2012), 20–28. issn: 1542-7730. doi: 10.
1145/2367376.2371297. url: https://doi.org/10.1145/2367376.
2371297.
[RPA22] KamalaRamasubramanian,ElianaPhillips,andPeterAlvaro.“Min-
ingmicroservicedesignpatterns”.In:Proceedingsofthe13thSympo-
siumonCloudComputing.2022,pp.190–195.
[SBG10] JiriSimsa,RandyBryant,andGarthGibson.“dBug:SystematicEvalu-
ationofDistributedSystems”.In:5thInternationalWorkshoponSystems
SoftwareVerification(SSV10).Vancouver,BC:USENIXAssociation,
Oct. 2010. url: https://www.usenix.org/conference/ssv10/dbug-
systematic-evaluation-distributed-systems.
[Sig+10] BenjaminH.Sigelman,LuizAndréBarroso,MikeBurrows,PatStephen-
son,ManojPlakal,DonaldBeaver,SaulJaspan,andChandanShanbhag.
Dapper, a Large-Scale Distributed Systems Tracing Infrastructure. Tech.
rep.Google,Inc.,2010.url:https://research.google.com/archive/
papers/dapper-2010-1.pdf.

198 Bibliography
[SKT21] Mohammad Reza Saleh Sedghpour, Cristian Klein, and Johan Tords-
son.“ServiceMeshCircuitBreaker:FromPanicButtontoPerformance
ManagementTool”.In:Proceedingsofthe1stWorkshoponHighAvail-
abilityandObservabilityofCloudSystems.HAOC ’21.Online,United
Kingdom: Association for Computing Machinery, 2021, 4–10. isbn:
9781450383363. doi: 10.1145/3447851.3458740. url: https://doi.
org/10.1145/3447851.3458740.
[SMAP19] Cleber Jorge Lira de Santana, Brenno de Mello Alencar, and Cás-
sio V. Serafim Prazeres. “Reactive Microservices for the Internet of
Things:ACaseStudyinFogComputing”.In:Proceedingsofthe34th
ACM/SIGAPPSymposiumonAppliedComputing.SAC’19.Limassol,
Cyprus:AssociationforComputingMachinery,2019,1243–1251.isbn:
9781450359337. doi: 10.1145/3297280.3297402. url: https://doi.
org/10.1145/3297280.3297402.
[Soc] SockShop:AMicroservicesDemoApplication.https://microservices-
demo.github.io.Accessed:2021-05-21.2021.
[SS+21] KridantoSurendro,WikanDanarSunindyo,etal.“CircuitBreaker
in Microservices: State of the Art and Future Prospects”. In: IOP
Conference Series:Materials Science andEngineering. Vol. 1077. 1. IOP
Publishing.2021,p.012065.
[SSZ20] Jonas Sorgalla, Sabine Sachweh, and Albert Zündorf. “Exploring
the microservice development process in small and medium-sized
organizations”.In:InternationalConferenceonProduct-FocusedSoftware
ProcessImprovement.Springer.2020,pp.453–460.
[STVDH18] JacopoSoldani,DamianAndrewTamburri,andWillem-JanVanDen
Heuvel.“Thepainsandgainsofmicroservices:Asystematicgreylit-
eraturereview”.In:JournalofSystemsandSoftware146(2018),pp.215–
232.
[Tig+20] RafikTighilt,ManelAbdellatif,NaouelMoha,HafedhMili,Ghizlane
ElBoussaidi,JeanPrivat,andYann-GaëlGuéhéneuc.“OntheStudyof
MicroservicesAntipatterns:ACatalogProposal”.In:Proceedingsofthe
EuropeanConferenceonPatternLanguagesofPrograms2020.EuroPLoP
’20.VirtualEvent,Germany:AssociationforComputingMachinery,
2020.isbn:9781450377690.doi:10.1145/3424771.3424812.url:https:
//doi.org/10.1145/3424771.3424812.

Bibliography 199
[TLP18] DavideTaibi,ValentinaLenarduzzi,andClausPahl.“Architectural
patternsformicroservices:asystematicmappingstudy”.In:CLOSER
2018:Proceedingsofthe8thInternationalConferenceonCloudComputing
and Services Science; Funchal, Madeira, Portugal, 19-21 March 2018. -.
2018.
[Tol+19] SauloSoaresdeToledo,AntonioMartini,Agata Przybyszewska,and
DagIKSjøberg.“Architecturaltechnicaldebtinmicroservices:acase
studyinalargecompany”.In:2019IEEE/ACMInternationalConference
onTechnicalDebt(TechDebt).IEEE.2019,pp.78–87.
[Tuc+18] Haley Tucker, Lorin Hochstein, Nora Jones, Ali Basiri, and Casey
Rosenthal.“Thebusinesscaseforchaosengineering”.In:IEEECloud
Computing 5.3(2018),pp.45–54.
[Tyl18] TylerLund.AWSre:Invent2018:ChaosEngineeringandScalabilityatAu-
dible.com (ARC308). https://www.youtube.com/watch?v=7uJG3oPw_
AA.Accessed:2022-06-05.2018.
[Val+20] J.A.Valdivia,A.Lora-González,X.Limón,K.Cortes-Verdin,andJ.O.
Ocharán-Hernández.“PatternsRelatedtoMicroserviceArchitecture:
a Multivocal LiteratureReview”. In: Programming and ComputerSoft-
ware 46.8(2020),pp.594–608.doi:10.1134/S0361768820080253.url:
https://doi.org/10.1134/S0361768820080253.
[Wal+96] Jim Waldo, Geoff Wyant, Ann Wollrath, and Sam Kendall. “A note
ondistributedcomputing”.In:InternationalWorkshoponMobileObject
Systems.Springer.1996,pp.49–64.
[Was+21a] MuhammadWaseem,PengLiang,MojtabaShahin,AakashAhmad,
andAliRezaeiNassab.“Onthenatureofissuesinfiveopensource
microservicessystems:Anempiricalstudy”.In:EvaluationandAssess-
mentinSoftwareEngineering.2021,pp.201–210.
[Was+21b] MuhammadWaseem,PengLiang,MojtabaShahin,AakashAhmad,
andAliRezaeiNassab.“Onthenatureofissuesinfiveopensource
microservicessystems:Anempiricalstudy”.In:EvaluationandAssess-
mentinSoftwareEngineering.2021,pp.201–210.
[WKR21] YingyingWang,HarshavardhanKadiyala,andJuliaRubin.“Promises
and challenges of microservices: an exploratory study”. In: Empirical
SoftwareEngineering 26.4(2021),pp.1–44.
[WLS20] MuhammadWaseem,PengLiang,andMojtabaShahin.“Asystematic
mappingstudyonmicroservicesarchitectureindevops”.In:Journal
ofSystemsandSoftware 170(2020),p.110798.

200 Bibliography
[XSZ08] BinXin,WilliamN.Sumner,andXiangyuZhang.“EfficientProgram
Execution Indexing”. In: SIGPLAN Not. 43.6 (June 2008), 238–248.
issn: 0362-1340. doi: 10.1145/1379022.1375611. url: https://doi.
org/10.1145/1379022.1375611.
[Yab+10] MaysamYabandeh,NikolaKnežević,DejanKostić,andViktorKun-
cak. “Predicting and Preventing Inconsistencies in Deployed Dis-
tributed Systems”. In: ACM Trans. Comput. Syst. 28.1 (2010). issn:
0734-2071.doi:10.1145/1731060.1731062.url:https://doi.org/10.
1145/1731060.1731062.
[Yan+09] Junfeng Yang, Tisheng Chen, Ming Wu, Zhilei Xu, Xuezheng Liu,
HaoxiangLin,MaoYang,FanLong,LintaoZhang,andLidongZhou.
“MODIST:TransparentModelCheckingofUnmodifiedDistributed
Systems”.In:6thUSENIXSymposiumonNetworkedSystemsDesignand
Implementation (NSDI 09). Boston, MA: USENIX Association, Apr.
2009. url: https://www.usenix.org/conference/nsdi-09/modist-
transparent-model-checking-unmodified-distributed-systems.
[Zha+19] Long Zhang, BriceMorin, Philipp Haller, Benoit Baudry, andMartin
Monperrus. “A Chaos Engineering System for Live Analysis and
FalsificationofException-handlingintheJVM”.In:IEEETransactions
on Software Engineering (2019), pp. 1–1. doi: 10.1109/TSE.2019.
2954871.
[Zha+21a] JunZhang,RobertFerydouni,AldrinMontana,DanielBittman,and
Peter Alvaro. “3MileBeach: A Tracer with Teeth”. In: Proceedings
of the ACM Symposium on Cloud Computing. SoCC ’21. Seattle, WA,
USA: Association for Computing Machinery, 2021, 458–472. isbn:
9781450386388. doi: 10.1145/3472883.3486986. url: https://doi.
org/10.1145/3472883.3486986.
[Zha+21b] JunZhang,RobertFerydouni,AldrinMontana,DanielBittman,and
Peter Alvaro. “3MileBeach: A Tracer with Teeth”. In: Proceedings
of the ACM Symposium on Cloud Computing. SoCC ’21. Seattle, WA,
USA: Association for Computing Machinery, 2021, 458–472. isbn:
9781450386388. doi: 10.1145/3472883.3486986. url: https://doi.
org/10.1145/3472883.3486986.
[Zha+21c] Long Zhang, BriceMorin, Philipp Haller, Benoit Baudry, andMartin
Monperrus. “A Chaos Engineering System for Live Analysis and
FalsificationofException-HandlingintheJVM”.In:IEEETransactions
onSoftwareEngineering47.11(2021),pp.2534–2548.doi:10.1109/TSE.
2019.2954871.

Bibliography 201
[Zho+18a] Xiang Zhou, Xin Peng, Tao Xie, Jun Sun, Chao Ji, Wenhai Li, and
Dan Ding. “Fault analysis and debugging of microservice systems:
Industrialsurvey,benchmarksystem,andempiricalstudy”.In:IEEE
TransactionsonSoftwareEngineering 47.2(2018),pp.243–260.
[Zho+18b] Xiang Zhou, Xin Peng, Tao Xie, Jun Sun, Chao Ji, Wenhai Li, and
Dan Ding. “Fault analysis and debugging of microservice systems:
Industrialsurvey,benchmarksystem,andempiricalstudy”.In:IEEE
TransactionsonSoftwareEngineering 47.2(2018),pp.243–260.
[Zip] Zipkin.https://zipkin.io.Accessed:2024-05-01.2024.