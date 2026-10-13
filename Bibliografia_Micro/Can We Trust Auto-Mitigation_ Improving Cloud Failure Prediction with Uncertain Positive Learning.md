Can We Trust Auto-Mitigation? Improving Cloud
Failure Prediction with Uncertain Positive Learning
Haozhe Li†, Minghua Ma‡∗, Yudong Liu†, Pu Zhao†, Shuo Li§, Ze Li‡, Murali Chintalapati‡,
Yingnong Dang‡, Chetan Bansal‡, Saravan Rajmohan‡, Qingwei Lin†, Dongmei Zhang†
†Microsoft, Beijing, China
‡Microsoft, Redmond, USA
Abstract—In the rapidly expanding domain of cloud comput- to predict failures and proactively mitigate them. This not
ing, a variety of software services have been deployed in the only boosts the availability and performance of cloud-based
cloud. To ensure the reliability of cloud services, prior studies
software systems but also reduces operational costs and risks.
focusonthepredictionoffailureinstances,suchasdisks,nodes,
At the forefront of cloud system reliability is the prediction
switches, etc. The mitigation actions are initiated to resolve the
underlyingissueoncethepredictionoutputispositive.However, of node failures, a critical step that enables us to anticipate
our real-world practice in Microsoft Azure revealed a decline problemsbeforetheyfullymanifest.Numerouspreviousstud-
in prediction accuracy, approximate 9%, subsequent to model ies aim to design better machine learning models to improve
retraining. The decrease is attributed to the mitigation actions,
the performance of cloud failure prediction tasks. Commonly
which can result in uncertain positive instances. Since these
employedmodelsareused,suchasRecurrentNeuralNetwork
instancescannotbeverifiedaftermitigation,theymayintroduce
additional noise into the model updating process. To the best (RNN) [32], Long Short-Term Memory (LSTM) [33], Trans-
of our knowledge, we are the first to identify this Uncertain former [26], and Temporal Convolutional Network (TCNN)
Positive Learning (UPLearning) issue in the real-world cloud [34]. Prediction is the first step to manage the cloud failures.
failure prediction scenario, and we design an Uncertain Positive
Onceapredictionindicatesapotentialfailure,swiftmitigation
Learning Risk Estimator (Uptake) approach to address this
actions are taken automatically to refresh and change the
problem. By utilizing two real-world datasets for disk failure
predictionandconductingnodepredictionexperimentsinAzure, node’sstatus.Failureauto-mitigationheremeanstoattemptto
which is a top-tier cloud provider serving millions of users, we makethefailurealertdisappearbytakingautomaticmitigation
demonstrate that our Uptake method can significantly enhance actions (e.g., refresh the node) after the failure prediction
failure prediction accuracy by an average of 5%.
is positive, without necessarily diagnosing and fixing the
IndexTerms—FailurePrediction,CloudSystems,PULearning
underlying bugs first. For example, if a computing node
is predicted to fail, we might reboot it automatically [35].
I. INTRODUCTION This auto-mitigation alters the node’s status, however, cannot
provide insights into the root cause of the potential failure.
Failure prediction and mitigation are vital across various
Consequently, we cannot be certain whether the predicted
domains, such as cloud computing [1]–[6], autonomous driv-
failurewilloccur,whichwecallanuncertainpositiveinstance.
ing [7] and automatic control [8], where swift and precise
The limitations of these auto-mitigation actions highlight
responses are critical for maintaining reliability and efficiency
the need for advanced prediction and mitigation techniques.
[9]–[14]. By employing real-time data analysis combined
Based on our experience with deploying prediction models
with predictive models, these fields can proactively manage
for cloud failures in Microsoft Azure, we have observed
potential disruptions, minimizing risks before they escalate
significant challenges in updating these models during real-
into significant issues and ensuring operational continuity and
world online usage. Model updating is the process of re-
safety against unforeseen incidents [15]–[19].
training the machine learning model over time (weekly or
In the context of cloud computing, similar predictive and
monthly) to adapt to the changing cloud environment (new
mitigation strategies are employed to manage substantial
hardware and software) [36]. An empirical study conducted
workloads on platforms, such as Microsoft Azure, Amazon
on both open datasets and Azure (see Section III), suggests
Web Services, and Google Cloud Platform. These providers
that the prediction accuracy of updated models may decrease
continuouslymonitorandanalyzethousandsofmetricsacross
byabout9%overtimebecausetheuncertainpositiveinstances
their cloud infrastructures to deliver high-quality service for
bring noise to the model updating. This effect is compounded
billions of users worldwide [20]–[24]. These metrics enable
when using a continuously updated model that accumulates
the detection and prevention of component failures within the
uncertain positive instances over time.
cloud system, such as memory [25], disk [26], [27], nodes
More specifically, Fig. 1 illustrates a toy example of the
[28]–[30], and switches [31]. By employing machine learning
model updating scenario in the cloud failure prediction. The
and deep learning techniques on these metrics, it is possible
figure has two parts, i.e., the offline updating and the online
updating. The offline updating is an ideal scenario in which
*Correspondingauthor.Email:minghuama@microsoft.com
§WorkwasperformedwhenhewasatCarnegieMellonUniversity we can access the oracle of cloud instance status (shown as

directlyapplytheriskestimatorapproachusedinPULearning.
In this paper, we propose an Uncertain Positive Learning
RiskEstimator(UPTAKE),anovelapproachforvariouscloud
failure prediction models to achieve high prediction accuracy
evenwithuncertainpositiveinstances.UPTAKEregardsuncer-
tain positive instances as both positive and negative through
a specially designed risk estimator during the model updating
procedure. Besides, UPTAKE only improves the loss function
whichmakesiteasytointegratewithvariousmachinelearning
models, such as RNN, LSTM, Transformer, and TCNN. To
evaluate the effectiveness of our proposed UPTAKE approach,
weconductextensiveexperimentstocompareUPTAKEagainst
three model updating approaches on two public disk datasets,
Alibaba and Backblaze, which both contain tens of thousands
of disks over months. In addition, we apply UPTAKE to the
scenario of node failure prediction in Azure, which is a top-
tier cloud provider and serves millions of customers around
the world. The experiment results on those three datasets
Fig.1. Toyexampleofcloudfailurepredictionmodelwithofflineupdating
and online updating. The prediction model (M) is updated by training with demonstrate that UPTAKE outperforms any other model up-
datainthedashedboxineachtimestage(T).Thenumberonthetopofeach datingapproachesoverdifferentpredictionmodels(i.e.,RNN,
sub-figureillustratestheinstanceID.
LSTM, Transformer and TCNN). The F1-scores of UPTAKE
are 45.26%, 70.16%, and 69.33% in scenarios of Alibaba,
the disk icons in black color). We may collect the monitoring
Backblaze and Azure, which are 4.85%, 4.17%, and 5.13%
metrics and status of the cloud instances in each period (T1,
better than those achieved by the best baseline approaches,
T2, T3, etc.). Then we train the model (M1, M2, M3, etc.)
respectively.
in each period without any concern. When it comes to the
To sum up, this work has the following contributions:
online scenario, however, we lack access to the oracle of
instancesstatusafterT1,mirroringtheconditionsoftheoffice • We introduce the UPLearning problem in the context of
scenario. In practice, we train a model in the T1 and make cloud failure prediction and auto-mitigation, marking a
online inferences in the T2 stage, some instances (#7, #8, and pioneering effort to tackle this substantial challenge in the
#9) are predicted as failure and highlighted in blue. These practical deployment of machine learning models in real-
instances are subsequently mitigated, and cannot access their world cloud scenarios.
actual status, which is noted as uncertain positive instances. • To solve the UPLearning, we propose an uncertain positive
Finally, together with the known failure instance (#10), we learningriskestimatorapproach,dubbed UPTAKE,whichis
may retrain the model M2. Clearly, the #7 instance is a False easy to integrate with various machine learning models.
PositiveonethatmayintroducenoisetomodelM2.Similarly, • To illustrate the generality and effectiveness of UPTAKE,
we may obtain a less accurate model (#11, #12 are uncertain weconductexperimentsondifferentcloudfailureprediction
positive instances, and #14, #15 are true positive instances) in scenarios, i.e., two public disk failure datasets and the node
the T3 stage since the model noise may be accumulated. failure from Azure. UPTAKE outperforms any other online
model updating approach over four widely used failure pre-
To the best of our knowledge, we are the first to identify
the Uncertain Positive Learning (UPLearning) challenge in
diction models. Moreover, UPTAKE has been successfully
applied to Azure and it is proven to improve the reliability
the real-world scenario of cloud failure prediction. The most
of cloud platforms.
closely related research topic to UPLearning is the Positive
Unlabeled Learning (PULearning) [37]–[45]. PULearning is a
machine learning scenario for binary classification where the
II. BACKGROUND
trainingsetconsistsofasetofpositivelylabeledinstancesand
Cloud failure prediction. Cloud failure refers to a state
an additional unlabeled set that contains positive and negative
where cloud instances become unavailable due to hardware
instancesinunknownproportions(sonotraininginstancesare
interruptions, code bugs, or high workload demands. Cloud
explicitly labeled as negative). The risk estimator-based ap-
failure can be categorized based on the affected instances,
proach, which estimates the distribution of negative instances
suchasnodefailure[28],networkissue[46],diskfailure[26],
in the unlabeled set, is widely used to solve the PULearning
service overloading [47], etc. In the following, we introduce
problem [38], [39], [45]. However, our UPLearning involves
two typical cloud failure prediction scenarios, i.e., disk failure
uncertainpositiveinstances,whicharesimilartotheunlabeled
prediction and node failure prediction.
setinthePULearningscenario,butalsoincludesbothpositive
and negative instances that system operators investigate after • Node failures may occur for a variety of reasons (e.g., OS
failures occur (see Section II). As a result, it is infeasible to crashes,applicationbugs,misconfigurations,memoryleaks,
2

TABLEI
EXAMPLESOFNODE&DISKMONITORINGMETRICS.
| Type |     | Description |     |     |     |     |     |     |     | Examples(FeaturebelongstoDisk/Node) |     |     |     |     |     |
| ---- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | ----------------------------------- | --- | --- | --- | --- | --- |
SpinUpTimeNorm(Disk)
Theimplementationofatimerforvariousoperationsofharddiskdrives,
SpinRetryCountRaw(Disk)
| OperationTimer |     | e.g.,magneticheadseekingandspindleactivation,playsacrucialrolein |     |     |     |     |     |     |     |            |       |             |     |     |     |
| -------------- | --- | ---------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ---------- | ----- | ----------- | --- | --- | --- |
|                |     |                                                                  |     |     |     |     |     |     |     | Spin Retry | Count | VALUE(Disk) |     |     |     |
optimizingtheperformanceofthesedevices. Spin Up Time VALUE(Disk)
PowerCycle(Node)
Countofcommonoperations,e.g.,CPUutilizationandpower
| OperationCounter |     |     |     |     |     |     |     |     |     | PowerOnHours(Node) |     |     |     |     |     |
| ---------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------ | --- | --- | --- | --- | --- |
consumption,etc.
PowerConsumption(Node)
AirflowTempRaw(Node)
|                         |     | Themeasurementofphysicalcharacteristics, |     |     |     |     | e.g.,temperatureand |     |     |                      |     |     |     |     |     |
| ----------------------- | --- | ---------------------------------------- | --- | --- | --- | --- | ------------------- | --- | --- | -------------------- | --- | --- | --- | --- | --- |
| PhysicalCharacteristics |     |                                          |     |     |     |     |                     |     |     | TemperatureRaw(Node) |     |     |     |     |     |
humidity,etc.
Temperature(Node)
|     |     |     |     |     |     |     |     |     |     | Program    | Fail Cnt | Total           | RAW VALUE(Disk) |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | -------- | --------------- | --------------- | --- | --- |
|     |     |     |     |     |     |     |     |     |     | Seek Error | Rate     | RAW VALUE(Disk) |                 |     |     |
Acountofspecific,identifiableerrorsismaintained.Thiscounttypically
TotalErrors(Node)
| ErrorCounter |     | remainsunchangedunlessanerroroccurs,atwhichpointthecountis |     |     |     |     |     |     |     |     |     |     |     |     |     |
| ------------ | --- | ---------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
IOEDCErrorCountRaw(Node)
updatedtoreflecttheoccurrenceoftheerror.
MediaErrors(Node)
ErrorInfoLogEntryCount(Node)
Windowseventaretypicallyusedforindicatingexceptionhandlingfor WindosStorportEvent 534(Node)
EVENT
|     |     | Windowsservers. |     |     |     |     |     |     |     | WindosStorportEvent |     | 554(Node) |     |     |     |
| --- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- | ------------------- | --- | --------- | --- | --- | --- |
software incompatibility, overheating, and service excep- chronological sequences and their long-range dependencies
tions). The node failure can be predicted by a wide range more precisely than conventional RNNs. With long-term
of monitoring metrics (signals indicating their temporal and features, LSTM can always perform better than RNN and
spatial information). MING [28] predicts node failure by can typically class difficult examples in RNN.
takingintoaccountbothspatialandtemporalsignals.TableI • Transformer [26]: The Transformer Model is a novel deep
presents several monitoring metrics of a node, which are learning-based approach to failure prediction tasks with the
classified into six distinct categories: operation timer, phys- attentionmechanism,whichcancapturethetemporalnature
ical characteristics, operation counter, error counter, logical from instance status data. Transformer utilizes not only a
input/output, and EVENT data. A detailed explanation of singleinstance’sstatusdatabutalsoconsidersitsneighbors’
thesecategories,includingexamples,isillustratedinTableI. status data to optimize its prediction performance.
The collection of these metrics is conducted at regular • TCNN [34]: TCNN is a variation of Convolutional Neural
intervals,exceptforEVENTdata.Toanalyzethesemetrics, Networks (CNN) for sequence modeling tasks, by combin-
a sliding window technique is employed in the prediction ing aspects of RNN and CNN architectures.
| model,         | transforming | of            | the metrics  | into   | feature     | vectors.       |              |           |              |              |               |                  |            |         |        |
| -------------- | ------------ | ------------- | ------------ | ------ | ----------- | -------------- | ------------ | --------- | ------------ | ------------ | ------------- | ---------------- | ---------- | ------- | ------ |
|                |              |               |              |        |             |                | Model        | updating. | The          | distribution |               | of online        | monitoring |         | met-   |
| • Disk failure | in           | cloud systems | is           | a type | of hardware | failure        |              |           |              |              |               |                  |            |         |        |
|                |              |               |              |        |             |                | rics changes |           | with dynamic |              | software      | and              | hardware   | updates |        |
| that can       | lead to      | service       | downtime.    |        | Disk        | failure can be |              |           |              |              |               |                  |            |         |        |
|                |              |               |              |        |             |                | in cloud     | systems,  | which        |              | causes        | the distribution |            | learned | by     |
| predicted      | based        | on its        | status data, | known  |             | as the SMART   |              |           |              |              |               |                  |            |         |        |
|                |              |               |              |        |             |                | the previous |           | model        | to deviate   | significantly |                  | from       | the     | online |
(Self-Monitoring,AnalysisandReportingTechnology)[48],
|           |            |         |     |        |     |              | distribution | [36]. | As  | a result, | the | prediction | performance |     | of  |
| --------- | ---------- | ------- | --- | ------ | --- | ------------ | ------------ | ----- | --- | --------- | --- | ---------- | ----------- | --- | --- |
| [49]. The | monitoring | metrics | of  | a disk | are | SMART (Self- |              |       |     |           |     |            |             |     |     |
Monitoring,Analysis,andReportingTechnology)[48],[49]. the model may degrade. To ensure prediction performance,
|     |     |     |     |     |     |     | machine | learning | models |     | deployed | online | need | to be | up- |
| --- | --- | --- | --- | --- | --- | --- | ------- | -------- | ------ | --- | -------- | ------ | ---- | ----- | --- |
Theseattributes,whichincludemetricssuchastemperature,
|           |                  |             |            |           |           |              | dated over     | time       | (weekly | or  | monthly). | Model        | updating |             | needs |
| --------- | ---------------- | ----------- | ---------- | --------- | --------- | ------------ | -------------- | ---------- | ------- | --- | --------- | ------------ | -------- | ----------- | ----- |
| spin-up   | time, and        | reallocated |            | sectors   | (examples | shown        | in             |            |         |     |           |              |          |             |       |
|           |                  |             |            |           |           |              | a considerable |            | number  | of  | failure   | instances.   | Updating |             | cloud |
| Table     | I), are employed |             | to predict |           | potential | failures. By |                |            |         |     |           |              |          |             |       |
|           |                  |             |            |           |           |              | failure        | prediction | models  |     | using     | pre-training | and      | fine-tuning |       |
| providing | early            | warning     | of such    | failures, | SMART     | technol-     |                |            |         |     |           |              |          |             |       |
ogy enables proactive maintenance and replacement to be [50] strategies is not feasible due to the imbalance between
|           |             |              |            |          |     |                 | positive | and         | negative  | instances, |               | as well | as the     | insufficient |     |
| --------- | ----------- | ------------ | ---------- | -------- | --- | --------------- | -------- | ----------- | --------- | ---------- | ------------- | ------- | ---------- | ------------ | --- |
| performed | prior       | to a failure | occurring. |          |     |                 |          |             |           |            |               |         |            |              |     |
|           |             |              |            |          |     |                 | number   | of positive | instances |            | in real-world |         | scenarios. |              |     |
| Based     | on insights | gained       | from       | previous |     | studies, we in- |          |             |           |            |               |         |            |              |     |
III. ANEMPIRICALSTUDYOFPREDICTIONACCURACY
| troduce    | and implement  | four                | widely       | used | machine     | learning       |            |        |           |          |            |             |        |       |        |
| ---------- | -------------- | ------------------- | ------------ | ---- | ----------- | -------------- | ---------- | ------ | --------- | -------- | ---------- | ----------- | ------ | ----- | ------ |
| models for | cloud          | failure prediction. |              |      |             |                |            |        |           | OVERTIME |            |             |        |       |        |
|            |                |                     |              |      |             |                | In this    | study, | we aim    | to       | uncover    | the problem |        | based | on our |
| • RNN      | [32]: RNN      | is a                | widely-used  |      | deep        | learning model |            |        |           |          |            |             |        |       |        |
|            |                |                     |              |      |             |                | experience | in     | deploying | failure  | prediction |             | models | in    | Azure. |
| designed   | for sequential |                     | data. During |      | prediction, | RNN uses       |            |        |           |          |            |             |        |       |        |
its recurrent unit to feature the difference between the We address the following research questions:
normalstateandfailurestatefromtheinputsequentialdata. • RQ1: How does the accuracy of failure prediction change
| LSTM | [33]: LSTM | is  | an advanced |     | version | of recurrent | over time? |     |     |     |     |     |     |     |     |
| ---- | ---------- | --- | ----------- | --- | ------- | ------------ | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
•
neural network architecture that was designed to model • RQ2:Whydoesthepredictionaccuracydecreaseovertime?
3

100
80
60
40
20
T2 T3 T4 T5
# Time
)%(
erocS
1F
TABLEII
Microsoft Azure Backblaze Alibaba
MITIGATIONACTIONSTOCLOUDFAILURES.
Action Description
78.12
75.36
67.33 LiveMigration MoverunningVMsfromtootherfailure-freenodes
63.25
71.59 68.17 66.56 VMPreserving RebootthehostOSkernelandpreservetheVMstates
50.44 57.46 SoftReboot
41.72 42.67 DisconnectcurrentVMandgeneratenewassignment
36.67 ServiceHealing oftheVMtohealthynodes
Mark
BlockallocationofnewVMstoanode
Unallocatable
Avoid ReducetheweighttoallocateanewVMtoanode
Fig.2. CloudfailurepredictionaverageF1-scoreovertime.
is divided into 5 equal-length time phases. At the start of
A. Subjects
each phase (except for the first training phase T1), model
We adopt two public datasets [26], [27] for disk-level updating is performed using monitoring data collected from
failure prediction, i.e., Alibaba Cloud and Backblaze datasets. the previous phase, then deployed for online prediction. The
Besides, Azure provides large-scale datasets for node-level average prediction performance of the model is calculated at
failure prediction. each time phase.
Alibaba is collected from large-scale data centers and The prediction F1-score (see Section V-A4) on 3 datasets
publishedbyAlibabaCloudforPAKDD2020AlibabaAIOps across 4-time phases is illustrated in Fig. 2. The time in the
Competition [51], which contains millions of disks with a figure starts from T2, which is because monitoring data in
period of more than 16 months. In our experiment, we adopt the T1 phase is used for the initial model training. Overall,
the dataset within 10 months and split it into five continuous there is a significant and consistent decrease in the accuracy
time phases of equal length. Each time phase contains more of the failure prediction model over time for all datasets. Per-
than 8,000 disk records with a period of two months and formance on Azure decreases from 78.22% on T2 to 57.46%
each record has 30 days long monitoring metrics. We use 17- on T5, a decrease of 20.66%. Backblaze and Alibaba also
dimension features for failure prediction. showdecreasesof8.34%and13.77%,respectively.Theresults
Backblaze is a public dataset published by Backblaze, on Alibaba do not show a decreasing trend in performance
based on the hard drives in Backblaze data center [52]. Each on T3 and T4 because the percentage and performance of
disk of the dataset has a label indicating its status. In our failures are not completely consistent across time, but the
experiment,weusefivemonthsfrom2021Q4to2022Q1,and performance of failure prediction on Alibaba also shows a
it contains over 90,000 disks in total. We split the dataset into significant decreasing trend of 13.77% when observed over
five continuous time phases of equal length. Each time phase the entire experimental time.
contains approximately 16,000 disk records and each record The decrease in prediction accuracy over time can be at-
contains 38 dimension features with a period of 30 days. tributedtochangesinthedistributionofonlinedata.However,
Azureisalarge-scalecloudsystemthatincludesnode-level it is important to note that this accuracy decrease is observed
monitoring metrics. Over 500,000 node recordings overall consistently across all three cloud systems and time phases.
from a period of 35 days are employed in our experiment. Furthermore, the retrained model is trained using the latest
We divide all records into five continuous time phases of collecteddata,whichhastheleastbiascomparedtotheonline
equal length. Each time phase comprises more than 100,000 data. We refer to this decrease in prediction accuracy after
noderecords.Thefeatureinputisthe23-dimensionmonitoring retraining as the UPLearning problem.
metrics of nodes in a 48-hour time window.
To demonstrate the generality and robustness of our inves-
C. RQ2: Explanation of Accuracy Decrease
tigation, we employed different periods for model updating:
Itismitigationactionsthatcontaminatethetrainingdataand
two months for Alibaba, one month for Backblaze, and one
lead to a decrease in prediction accuracy (i.e., UPLearning)
week for Azure. These periods were selected based on the
duringmodelretraining.Inthecontextoffailurepredictionin
number of positive instances available in each, as positive
cloud systems, when a cloud component is anticipated to fail,
instances are significantly less frequent than negative ones
mitigation actions [35] in Table II are promptly undertaken to
in real-world datasets, as noted by Ntam [26]. We aim to
either resolve the underlying failure or minimize the impact
ensure that each period contains a relatively sufficient number
on services. The effectiveness of these mitigation actions,
ofpositiveinstances,maintaininganimbalancerate(#Positive
however, makes it impractical to verify the accuracy of the
to #Negative ratio) of approximately 1%.
predictions.Forinstance,inthecaseofapplyinglivemigration
B. RQ1: Prediction Accuracy over Time
to a predicted failing node, all run-time state is migrated to a
We undertake a detailed investigation on prediction perfor- new node, resulting in the release of workload on the original
mance trends across a continuous long range of time, which node [53]. This operation alters the original state, rendering it
4

ThetrainingsetisacollectionoffeaturesX withtheircor-
respondinglabelY,denotedasN ={(X ,Y ),...,(X ,Y )},
1 1 n n
where n = |N|. Our target is to minimize prediction loss L,
(e.g., the binary cross-entropy loss), on the training set.
In the scenario of cloud failure prediction, some labels
Y (i∈{1,...,n})inthetrainingsetareuncertain,specifically,
i
we have to use the training set which contains uncertain label
Yˆ to train and update the online model. The training loss to
be minimized is represented as:
n
Fig.3. Exampleofpositive,negative,anduncertainpositiveinthescenario L=− n 1 (cid:88) l(f(X i ),Yˆ i ) (1)
ofonlinecloudfailureprediction. i=1
unverifiable whether the failure would have indeed occurred where l is the loss function, f is the binary classifier, and
in the original state.
(X
i
,Yˆ
i
), i∈{1,...n}isthesamplefromthetrainingset.Yˆ
is the uncertain label (i.e., the predicted label collected from
UPLearning problem. The UPLearning problem in cloud
the online model).
systems is mainly due to mitigation actions, which change
the state of the instances and make it impossible to verify the
B. UPTAKE
accuracy of the predictions. In the context of cloud failure
prediction, an online model (M) is initially trained using Typically, the model’s performance is assessed using the
historicaldatawithtruelabels(oraclelabels)duringperiodT1. risk function [54]. A precise risk function enhances the
Thismodelpredictsinstancesthatarelikelytofail,represented performance of the failure prediction model. The UPTAKE
by blue-filled instances in period T2, applying mitigation approach ensures high prediction accuracy, especially when
actions to address the potential failure. However, it remains handlinguncertainpositiveinstances,andeffectivelyaddresses
unknown whether these predicted instances will actually fail the UPLearning problem.
or not, as indicated by the black-bordered instances (#6-#10).
Risk estimator. In this section, we describe the binary
Uncertain positive instances are those predicted as failures by
classification representation of the risk function [54], [55].
the online model, such as instances #7, #8, and #9 in Fig. 3. Consider a feature set X ∈ Rd and its corresponding label
However,thetruelabels(oraclelabels)fortheseinstances(#7:
Y ∈ {0,1}. Let p(x,y) be the underlying joint density of
Negative,#8and#9:Positive)cannotbeverifiedafterapplying
(X,Y), p (x) = p(x|Y = 1), and p (x) = p(x|Y = 0)
p n
failure mitigation actions, because mitigation actions change
represent the positive and negative marginals, respectively.
the original state of the instances.
Additionally, define π = p(Y = 1) as the class-prior
p
IV. APPROACH probability and π n =p(Y =0)=1−π p .
Let f → Y be the decision function, and l : R ×
In this section, we introduce a model updating approach to X
{0,1}→R be the loss function, where l(f(X),Y) measures
solve the UPLearning problem, named UPTAKE, which still
the loss between the predicted output f(X) and the actual
consumes uncertain positive instances during model updating
label Y. Define R(f) as the risk function for the given
and significantly improves the online model updating perfor-
decision function f → Y, R+(f) = E [l(f(X),1)], and
mance for cloud failure prediction. X p p
R−(f) = E [l(f(X),0)], where E [·] = E [·] and
n n p X∼pp
A. Problem Settings E [·] = E [·], denoting the expectations of positive and
n X∼pn
Beforedivingintotheapproachdetails,wepresentaformal negativevariables.Instandardbinaryclassification,theriskof
definition of the cloud failure prediction task. We define the decision function f X →Y is denoted as:
the cloud failure prediction task as a binary classification
problem based on monitoring metrics. Essentially, we collect
feature vectors with d dimensions, which contain different R(f)=E (X,Y)∼p(x,y) [l(f(X),Y)]=π p R p +(f)+π n R n −(f)
types of monitoring metrics from cloud infrastructures, at (2)
regular intervals (e.g. hourly or daily). These feature vectors UPTAKE. In the context of cloud failure prediction, we en-
areusedtocreateacontinuoustimeseriesoffeatures,denoted counter instances not only labeled as positive or negative but
as X = [x 1 ,x 2 ,...,x l ] ∈ Rd, where l is the number of also instances with uncertain positive labels predicted by the
timestamps in the feature X. For each feature X, we assign a online model. UPTAKE treats uncertain positive instances as
labelY ∈0,1basedonwhetheritrepresentsafailureinstance havingbothpositiveandnegativelabelswithdifferentweights.
(Y = 1) or a normal instance (Y = 0) in the cloud system. The risk function for this scenario is represented as follows:
The goal of cloud failure prediction is to train a classifier
f → Y that can predict the class label Y when given a
X
feature X with uncertain positive labels. R(f)=π R+(f)+π R−(f)+(π R+(f)+π R−(f)) (3)
p p n n p u n u
5

| where | R+(f)=E |     | [l(f(X),1)] | and | R−(f)=E | [l(f(X),0)] |     | A. Settings |     |     |     |     |     |     |     |
| ----- | ------- | --- | ----------- | --- | ------- | ----------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
|       | u       | u   |             |     | u       | u           |     |             |     |     |     |     |     |     |     |
representtheexpectationsofthedecisionfunctionf(X)when 1) Datasets: To evaluate the reliability and applicability
| dealing | with    | uncertain | positive | instances. |       |                  |     |            |     |        |     |          |            |           |     |
| ------- | ------- | --------- | -------- | ---------- | ----- | ---------------- | --- | ---------- | --- | ------ | --- | -------- | ---------- | --------- | --- |
|         |         |           |          |            |       |                  |     | of UPTAKE, | we  | employ | two | publicly | accessible | datasets: | the |
| It is   | crucial | to note   | that     | π and      | π are | hyper-parameters |     |            |     |        |     |          |            |           |     |
p n Alibaba Cloud and Backblaze datasets [26], [27], for predict-
in this study. π estimates the proportion of real positive in- ing disk failures. Furthermore, we integrate a vast industrial
p
| stancesamonguncertainpositiveinstances,whileπ |     |     |     |     |     |     | =1−π |                |     |         |            |      |           |       |          |
| --------------------------------------------- | --- | --- | --- | --- | --- | --- | ---- | -------------- | --- | ------- | ---------- | ---- | --------- | ----- | -------- |
|                                               |     |     |     |     |     |     | n    | p cloud system |     | dataset | to predict | node | failures. | These | datasets |
estimatesthepercentageofnegativeinstances.Inthispaper,π p together form the foundation of our assessment and analysis.
| is set | to the             | Precision | value   | obtained | during | the T1       | validation |              |               |          |            |         |          |          |       |
| ------ | ------------------ | --------- | ------- | -------- | ------ | ------------ | ---------- | ------------ | ------------- | -------- | ---------- | ------- | -------- | -------- | ----- |
|        |                    |           |         |          |        |              |            | The specific | configuration |          | and        | details | of these | datasets | align |
| stage  | of hyper-parameter |           | tuning. | When     | π      | approximates | the        |              |               |          |            |         |          |          |       |
|        |                    |           |         |          | p      |              |            | with what    | we            | outlined | in Section | III-A.  |          |          |       |
proportionofuncertainpositiveinstanceswithtruepositivela- 2) Implementations and Environments: Four deep learning
bels,UPTAKEdemonstratesimprovedperformance.InSection
|     |     |     |     |     |     |     |     | models, | i.e., | RNN, | LSTM, | Transformer, |     | and | TCNN, are |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ----- | ---- | ----- | ------------ | --- | --- | --------- |
V-F, we discuss the parameter sensitivity of π p . implemented based on Python 3.8.13 and PyTorch 1.11.0
|                |     |     |         |         |        |     |           | [56]. Identical |     | parameter | values | are | used | as in the | previous |
| -------------- | --- | --- | ------- | ------- | ------ | --- | --------- | --------------- | --- | --------- | ------ | --- | ---- | --------- | -------- |
| Implementation |     | in  | various | models. | UPTAKE | is  | a generic |                 |     |           |        |     |      |           |          |
approach that can be integrated with any machine learning works for the compared approaches. The model was selected
model for cloud failure prediction. based on the epoch that achieved the highest F1-score on the
Algorithm1illustratesthecoreimplementationofUPTAKE. validation set. All the experiments are conducted on Linux
The input training data subscripted with p, n, and u are Dev Node with Ubuntu 20.04 LTS 64-bit operating system,
|               |     |         |      |           |           |     |           | 24 cores | AMD | Epyc | 7V13, | 220 GB | memory, | and | NVIDIA |
| ------------- | --- | ------- | ---- | --------- | --------- | --- | --------- | -------- | --- | ---- | ----- | ------ | ------- | --- | ------ |
| the instances |     | labeled | with | positive, | negative, | and | uncertain |          |     |      |       |        |         |     |        |
positive, respectively, and θ indicates the model parameter Tesla A100 with 80 GB GPU memory.
for decision function f(X;θ). To reduce the interference 3) Important Hyper-parameters: As explained in Section
|     |     |     |     |     |     |     |     | IV-B, the | parameter |     | π plays | a crucial | role | in this | study. Its |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | --------- | --- | ------- | --------- | ---- | ------- | ---------- |
of uncertain positive instances to the direction of gradient p
descent, UPTAKE improves the loss function in the model valueis derivedfrom thePrecision metricobtained duringthe
updating procedure by adjusting the direction of the gradient. T1 validation stage.
|       |        |      |          |     |          |      |          | 4) Evaluationmetrics: |     |     | Thecloudfailurepredictiontaskisa |     |     |     |     |
| ----- | ------ | ---- | -------- | --- | -------- | ---- | -------- | --------------------- | --- | --- | -------------------------------- | --- | --- | --- | --- |
| Since | UPTAKE | only | improves | the | original | loss | function |                       |     |     |                                  |     |     |     |     |
without changing its property, it is suitable for a wide range binary classification task, aligning with existing research. The
|            |          |     |        |                |     |               |     | performance   | of  | UPTAKE    | is       | assessed     | using | Precision, | Recall, |
| ---------- | -------- | --- | ------ | -------------- | --- | ------------- | --- | ------------- | --- | --------- | -------- | ------------ | ----- | ---------- | ------- |
| of machine | learning |     | models | across various |     | applications. |     |               |     |           |          |              |       |            |         |
|            |          |     |        |                |     |               |     | and F1-score, |     | following | standard | conventions. |       | Instances  | are     |
Algorithm 1 Introducing UPTAKE in the gradient descent labeled as either normal or failure based on their practical
|        |          |      |       |       |     |     |     | performance, |     | with failure |     | considered | positive | and | normal |
| ------ | -------- | ---- | ----- | ----- | --- | --- | --- | ------------ | --- | ------------ | --- | ---------- | -------- | --- | ------ |
| Input: | training | data | (X ,X | ,X ); |     |     |     |              |     |              |     |            |          |     |        |
|        |          |      | p     | n u   |     |     |     |              |     |              |     |            |          |     |        |
hyperparameter 0≤π ≤1, and π =1−π ; considerednegative.TruePositive(TP)representsthenumber
|          |     |          | p       |      | n        | p         |     |              |           |     |         |            |       |      |          |
| -------- | --- | -------- | ------- | ---- | -------- | --------- | --- | ------------ | --------- | --- | ------- | ---------- | ----- | ---- | -------- |
|          |     |          |         |      |          |           |     | of correctly | predicted |     | failure | instances, | while | True | Negative |
| decision |     | function | f(X;θ); | loss | function | l(f(X),Y) |     |              |           |     |         |            |       |      |          |
Output: gradient ∇ to update θ for f(X;θ) (TN) represents the accurately predicted normal instances.
θ
Improved loss Conversely, False Positive (FP) and False Negative (FN)
1:
|        |          |     |            |          |     |       |     | indicate     | instances     | that | were | incorrectly | predicted |     | as normal |
| ------ | -------- | --- | ---------- | -------- | --- | ----- | --- | ------------ | ------------- | ---- | ---- | ----------- | --------- | --- | --------- |
| L=π    | l(f([X   |     | ,X ]),1)+π | l(f([X   | ,X  | ]),0) |     |              |               |      |      |             |           |     |           |
|        | p        | p   | u          | n        | n   | u     |     |              |               |      |      |             |           |     |           |
| 2: Set | gradient | ∇   | L and      | update θ |     |       |     | and failure, | respectively. |      |      |             |           |     |           |
θ
|     |     |     |     |     |     |     |     | 5) Compared |     | Approaches: |     | In the | experiment |     | section, we |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ----------- | --- | ------ | ---------- | --- | ----------- |
compareUPTAKEwithtwomodelupdatingapproaches,which
V. EXPERIMENT are offline updating (offline), and online updating with certain
|     |     |     |     |     |     |     |     | positive | labels | (certain). | To  | the best | of our | knowledge, | UP- |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------ | ---------- | --- | -------- | ------ | ---------- | --- |
Inthissection,weconductextensiveexperimentstodemon-
|        |                   |     |     |            |          |     |          | Learning | has | not been | proposed | before. | Therefore, |     | there are |
| ------ | ----------------- | --- | --- | ---------- | -------- | --- | -------- | -------- | --- | -------- | -------- | ------- | ---------- | --- | --------- |
| strate | the effectiveness |     | of  | our UPTAKE | approach |     | when in- |          |     |          |          |         |            |     |           |
nostate-of-the-artsolutionsformodelupdating.Wedesignthe
| tegrated | with             | existing | failure   | prediction |     | models.   | First, we |           |          |            |     |     |          |      |         |
| -------- | ---------------- | -------- | --------- | ---------- | --- | --------- | --------- | --------- | -------- | ---------- | --- | --- | -------- | ---- | ------- |
|          |                  |          |           |            |     |           |           | two model | updating | approaches |     | as  | compared | with | UPTAKE. |
| present  | the experimental |          | settings, | including  |     | datasets, | the fail- |           |          |            |     |     |          |      |         |
ure prediction models, and three comparative approaches. • Offline updating employs ground truth labels for model
Following the setup, we conduct experiments to verify the training, which contain no uncertain labels. However, this
|             |          |             |     |                             |        |          |           | approach | is         | not feasible |               | in practice | because  |                    | part of the |
| ----------- | -------- | ----------- | --- | --------------------------- | ------ | -------- | --------- | -------- | ---------- | ------------ | ------------- | ----------- | -------- | ------------------ | ----------- |
| following   | research | questions:  |     |                             |        |          |           |          |            |              |               |             |          |                    |             |
|             |          |             |     |                             |        |          |           | ground   | truth      | labels       | are uncertain |             | positive | labels.            | It serves   |
| RQ3:Howdoes |          | UPTAKE      |     | performforUPLearningproblem |        |          |           |          |            |              |               |             |          |                    |             |
| •           |          |             |     |                             |        |          |           | as an    | upper      | bound        | of the        | performance |          | for UPTAKE         | and         |
| in cloud    | failure  | prediction? |     |                             |        |          |           |          |            |              |               |             |          |                    |             |
|             |          |             |     |                             |        |          |           | other    | subsequent | approaches.  |               |             |          |                    |             |
| • RQ4:      | How      | does UPTAKE |     | perform                     | in the | scenario | of online |          |            |              |               |             |          |                    |             |
|             |          |             |     |                             |        |          |           | • Online | updating   | with         | certain       | positive    |          | labels accumulates |             |
cloud systems?
|           |      |         |         |            |             |               |        | all records |          | with certain |          | labels      | for model      | updating.    | For        |
| --------- | ---- | ------- | ------- | ---------- | ----------- | ------------- | ------ | ----------- | -------- | ------------ | -------- | ----------- | -------------- | ------------ | ---------- |
| • RQ5:    | Does | UPTAKE  | exhibit | consistent | performance |               | across |             |          |              |          |             |                |              |            |
|           |      |         |         |            |             |               |        | instance,   | when     | updating     | the      | model       | for predicting |              | phase T4,  |
| different | base | models? |         |            |             |               |        |             |          |              |          |             |                |              |            |
|           |      |         |         |            |             |               |        | the certain | approach |              | collects | all records |                | with certain | labels     |
| • RQ6:    | What | is the  | impact  | of UPTAKE  |             | on predicting | effi-  |             |          |              |          |             |                |              |            |
|           |      |         |         |            |             |               |        | from        | phase    | T1 to        | phase    | T3. This    | includes       | all          | records in |
ciency?
|      |     |             |     |            |        |     |            | phase        | T1, as | well as   | true | negative | (TN) | and false | negative |
| ---- | --- | ----------- | --- | ---------- | ------ | --- | ---------- | ------------ | ------ | --------- | ---- | -------- | ---- | --------- | -------- |
| RQ7: | How | do UPTAKE’s |     | parameters | impact | its | prediction |              |        |           |      |          |      |           |          |
| •    |     |             |     |            |        |     |            | (FN) records |        | in phases | T2   | and T3.  |      |           |          |
performance?
6

TABLEIII
PERFORMANCECOMPARISONOFAPPROACHESONALIBABADATASET.P,R,ANDF1DENOTEPRECISION,RECALLANDF1-SCORE,RESPECTIVELY.
T2 T3 T4 T5 Avg.
Model Approach
P R F1 P R F1 P R F1 P R F1 F1
Offline 40.12 50.00 44.52 76.92 35.71 48.78 43.89 49.07 46.33 46.54
RNN Certain 57.84 33.33 42.29 35.95 42.31 38.87 79.59 23.21 35.94 49.12 17.39 25.69 33.50
UPTAKE 40.30 41.54 40.91 47.65 42.26 44.79 35.96 39.75 37.76 41.15
Offline 65.82 40.00 49.76 74.71 38.69 50.98 63.11 40.37 49.24 49.99
LSTM Certain 65.31 36.16 46.55 54.22 34.62 42.25 80.43 22.02 34.58 59.09 24.22 34.36 37.06
UPTAKE 56.18 38.46 45.66 64.76 40.48 49.82 58.72 39.75 47.41 47.63
Offline 61.80 42.31 50.23 68.47 45.24 54.48 61.42 48.45 54.17 52.96
Trans
Certain 62.41 46.89 53.55 53.92 42.31 47.41 79.66 27.98 41.41 61.76 26.09 36.68 41.83
-former
UPTAKE 53.04 46.92 49.80 46.70 50.60 48.57 41.24 49.69 45.07 47.81
Offline 43.59 52.31 47.55 60.38 38.10 46.72 58.88 39.13 47.01 47.09
TCNN Certain 57.72 40.11 47.33 46.25 28.46 35.24 72.41 25.00 37.17 42.86 22.36 29.39 33.93
UPTAKE 63.24 33.08 43.43 36.84 54.16 43.85 68.29 34.78 46.09 44.46
Offline 52.83 46.16 48.02 70.12 39.44 50.24 56.83 44.26 49.19 49.15
Avg. Certain 60.82 39.12 47.43 47.59 36.93 40.94 78.02 24.55 37.28 53.21 22.52 31.53 36.58
UPTAKE 53.19 40.00 44.95 48.99 46.88 46.76 51.05 40.99 44.08 45.26
TABLEIV
PERFORMANCECOMPARISONOFAPPROACHESONBACKBLAZEDATASET.P,R,ANDF1DENOTEPRECISION,RECALLANDF1-SCORE,RESPECTIVELY.
T2 T3 T4 T5 Avg.
Model Approach
P R F1 P R F1 P R F1 P R F1 F1
Offline 62.75 73.56 67.73 74.29 73.24 73.76 76.33 62.32 68.62 70.04
RNN Certain 50.88 84.67 63.56 57.89 50.57 53.99 80.91 41.78 55.11 83.67 39.61 53.77 54.29
UPTAKE 59.31 69.54 64.02 62.21 87.32 72.66 57.73 81.16 67.47 68.05
Offline 70.79 82.18 76.06 76.71 78.87 77.78 70.71 81.64 75.78 76.54
LSTM Certain 63.59 85.40 72.90 71.81 61.49 66.25 86.79 43.19 57.68 82.86 42.03 55.77 59.90
UPTAKE 63.32 83.33 71.96 61.72 74.18 67.38 54.79 80.19 65.10 68.15
Offline 74.87 85.63 79.89 76.23 79.81 77.98 72.44 78.74 75.46 77.78
Trans
Certain 71.60 84.67 77.59 69.54 69.54 69.54 83.48 45.07 58.54 82.41 43.00 56.51 61.53
-former
UPTAKE 71.36 87.36 78.55 71.31 81.69 76.15 64.77 82.61 72.61 75.77
Offline 67.35 75.86 71.35 74.24 79.81 76.92 79.63 62.32 69.92 72.73
TCNN Certain 63.54 83.94 72.33 77.45 45.40 57.25 79.07 47.89 59.65 80.92 51.21 62.72 59.87
UPTAKE 59.26 73.56 65.64 62.45 81.22 70.61 63.49 77.29 69.72 68.66
Offline 68.94 79.31 73.76 75.37 77.93 76.61 74.78 71.26 72.45 74.27
Avg. Certain 62.40 84.67 71.60 69.17 56.75 61.76 82.56 44.48 57.75 82.47 43.96 57.19 58.90
UPTAKE 63.31 78.45 70.04 64.42 81.10 71.70 60.20 80.31 68.73 70.16
B. RQ3: Performance of UPTAKE The performance of these models remains competitive with
previous work [27], despite the inherent challenges of cloud
Weassessourproposed UPTAKE,usingtwopublicdatasets
failurepredictiontasksinreal-worldscenarios.Notably,online
referredtoasAlibabaandBackblaze.Theresultsarepresented
disk failure prediction often faces limitations due to low F1-
in Table III and Table IV respectively. In these tables, the last
scores. This challenge largely stems from the prevalence of
column displays the average F1-score for each row. The final
missing data and significant imbalances in the data distribu-
three rows depict the average results of all four models across
tion, posing significant obstacles to improvement.
different time phases and using different approaches.
Intherestofthetable,everysetofthreecolumnsshowcases
the performance metrics (Precision, Recall, and F1-score) for Upon analyzing Table III and Table IV, we observe that
different time phases. Notably, the time phases in Table III UPTAKE performs admirably on these two public datasets.
andTableIVcommencefromT2,asthedatainT1isutilized The average F1-scores are 45.26% for Alibaba and 70.16%
for the initial model training. It is observed that the three forBackblaze.Accordingtotheresultssharedabove,wehave
approachesyieldidenticalresultsatT2sinceitmarksthefirst thefollowingfindings.Theresultsofvariousmethodsapplied
stage to obtain model inference results without encountering to Alibaba’s data demonstrate low performance due to the
any UPLearning problem (as illustrated in Fig. 1). complexity of the dataset. The highest F1-score achieved on
7

TABLEV
PERFORMANCECOMPARISONOFAPPROACHESONAZURE.P,R,ANDF1DENOTEPRECISION,RECALLANDF1-SCORE,RESPECTIVELY.
T2 T3 T4 T5 Avg.
Model Approach
P R F1 P R F1 P R F1 P R F1 F1
Offline 88.59 67.11 76.36 71.43 59.14 64.71 82.24 68.75 74.89 71.99
RNN Certain 88.31 86.96 75.16 93.94 46.62 62.31 83.16 43.82 57.39 93.50 48.70 64.04 61.25
UPTAKE 94.62 49.62 65.10 84.65 51.88 64.33 93.28 57.81 71.38 66.94
Offline 66.19 78.76 71.93 77.44 68.28 72.57 80.79 63.54 71.14 71.88
LSTM Certain 80.60 79.67 80.13 47.45 61.28 53.49 78.95 56.45 65.83 68.65 93.69 68.65 62.66
UPTAKE 59.58 79.51 68.12 65.05 75.54 69.90 84.00 60.16 70.11 69.38
Offline 75.27 78.95 77.06 76.45 67.20 71.53 71.03 73.44 72.22 73.60
Trans
Certain 65.60 96.55 78.12 80.54 56.02 66.08 82.63 52.42 64.14 91.28 51.82 66.11 65.44
-former
UPTAKE 72.38 77.82 75.54 65.37 72.04 68.54 71.74 68.75 70.21 71.43
Offline 67.89 79.89 73.40 84.69 66.94 74.77 64.25 76.30 69.76 72.64
TCNN Certain 80.87 75.70 78.20 45.24 57.14 50.50 86.51 50.00 63.37 91.08 50.52 64.99 59.62
UPTAKE 63.72 77.26 69.84 71.28 73.39 72.32 57.77 78.39 66.52 69.56
Offline 74.49 76.18 74.69 77.50 65.39 70.90 74.58 70.51 72.00 72.53
Avg. Certain 78.85 84.72 77.90 66.79 55.27 58.10 82.81 50.67 62.68 86.13 61.18 65.95 62.24
UPTAKE 72.58 71.05 69.65 71.59 68.21 68.77 76.70 66.28 69.56 69.33
the leader-board is only 49.07%. 1 shows the smallest improvement, with an average F1-score
increase of 1.64%. However, when compared with offline
Comparison with different updating approaches. When
updating, we do not observe a consistent pattern in model
examining the last column of Table III and Table IV, it
performance across all datasets. This discrepancy can be
becomesevidentthatofflineupdatingconsistentlyoutperforms
attributed to biases introduced in the data distribution among
other approaches. It achieves an average F1-score of 49.15%
differentstages,whichaffecttheperformanceofvariousmod-
in Alibaba and 74.27% in Backblaze. However, it is impor-
tant to note that offline updating, while showing the best
els in distinct ways. In summary, UPTAKE consistently out-
performs Certain model updating approaches and approaches
performance, is not practically applicable as it requires the
the performance of the Offline (i.e., the upper bound) across
access to all certain labels, which is often unavailable in
different prediction models. This consistency underscores its
real-world scenarios. Therefore, we present this approach as
generality and robustness in enhancing model performance.
the ”upper bound” of the prediction model, representing the
best possible performance using all certain labels. Among the C. RQ4: Online Performance
practical and feasible approaches, UPTAKE demonstrates the
Wehavedeployed UPTAKE tooneofthetop-tiercloudsys-
best performance. It achieves an average F1-score of 45.26%
tems in the world, Azure, which suffer from the UPLearning
in Alibaba and 70.16% in Backblaze. In contrast, Certain
problem before using our approach. We have conducted an
performs the worst, with an average F1-score of 36.58% in
online experiment (in the A/B testing environment to obtain
Alibaba and 58.90% in Backblaze. We attribute the lower
ground truth) for a period of time over five weeks from July
accuracy of Certain to the accumulation of phases, which
2022 to August 2022.
causes the proportion of positive and negative instances to
Table V presents a comparison of model performance for
deviate from the actual distribution. Specifically, the Certain
the model updating approaches mentioned before, following
method disregards all uncertain positive samples, even though
the same format as the tables in Section V-B. UPTAKE out-
only an average of 60.84% in Alibaba and 19.27% in Back-
performs Certain, achieving an average F1-score of 69.33%.
blaze of positive labels are certain positive. This discrepancy
This performance surpasses Certain by an average of 7.09%
in handling uncertain positive samples results in a distribution
and falls slightly below the Offline performance by 3.2% in
drift, leading to less accurate performance.
terms of F1-score.
Model comparison. Analyzing the UPTAKE results for each The accumulation of uncertain positive labels impacts the
model displayed in Table III and Table IV, we observe that performance of node failure prediction. Unlike failure predic-
UPTAKE consistently demonstrates different performance im- tion on public disk datasets, the node failure prediction model
provements compared to the Certain approach across various is more concerned with the quality of labels rather than the
models.Ingeneral,eachmodelinourexperimentexperiences proportion of positive samples to negative samples. In this
enhancements when using UPTAKE. Specifically, RNN ex- context, the accuracy and reliability of labels are important in
hibitsthemostsubstantialimprovement,achievinganaverage determining the effectiveness of the prediction model.
F1-score increase of 7.02% across all datasets, while LSTM In summary, UPTAKE excels in handling the UPLearning
problem compared to previous online updating approaches.
1https://tianchi.aliyun.com/competition/entrance/231775/rankingList Additionally, it proves effective in mitigating performance
8

|              |     | Offline |     | Certain      |     | Uptake |     |     |     |     | Transformer |     | TCNN |     |     |
| ------------ | --- | ------- | --- | ------------ | --- | ------ | --- | --- | --- | --- | ----------- | --- | ---- | --- | --- |
|              |     |         |     |              |     |        |     |     |     |     | LSTM        |     | RNN  |     |     |
|              | 100 |         |     |              | 100 |        |     |     |     |     |             |     |      |     |     |
| )%( erocs-1F |     |         |     | )%( erocs-1F |     |        |     |     |     | 60  |             |     |      |     |     |
50
|     | 50  |     |     |     | 50  |     |     |     | )%( erocs-1F |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- |
40
30
|     | 0       |           |       |     | 0       |           |       |     |     |     |     |     |     |     |     |
| --- | ------- | --------- | ----- | --- | ------- | --------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | Alibaba | Backblaze | Azure |     | Alibaba | Backblaze | Azure |     |     |     |     |     |     |     |     |
20
|     |     | Dataset |     |     |     | Dataset  |     |     |     |     |     |     |     |     |     |
| --- | --- | ------- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     | (a) RNN |     |     |     | (b) LSTM |     |     |     |     |     |     |     |     |     |
10
|              |         |           |       |              |         |           |       |     |     | 0.0 0.2 | 0.4         | 0.6 | 0.8 1.0 |     |     |
| ------------ | ------- | --------- | ----- | ------------ | ------- | --------- | ----- | --- | --- | ------- | ----------- | --- | ------- | --- | --- |
|              | 100     |           |       |              | 100     |           |       |     |     |         |             | p   |         |     |     |
| )%( erocs-1F |         |           |       | )%( erocs-1F |         |           |       |     |     |         |             |     |         |     |     |
|              |         |           |       |              |         |           |       |     |     |         | (a) Alibaba |     |         |     |     |
|              | 50      |           |       |              | 50      |           |       |     |     |         |             |     |         |     |     |
|              |         |           |       |              |         |           |       |     |     |         | Transformer |     | TCNN    |     |     |
|              |         |           |       |              |         |           |       |     |     |         | LSTM        |     | RNN     |     |     |
|              | 0       |           |       |              | 0       |           |       |     |     | 80      |             |     |         |     |     |
|              | Alibaba | Backblaze | Azure |              | Alibaba | Backblaze | Azure |     |     |         |             |     |         |     |     |
|              |         | Dataset   |       |              |         | Dataset   |       |     |     |         |             |     |         |     |     |
70
|     |     | (c) Transformer |     |     |     | (d) TCNN |     |     | )%( erocs-1F |     |     |     |     |     |     |
| --- | --- | --------------- | --- | --- | --- | -------- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- |
60
Fig.4. TheaverageF1-scorecomparisonofUPTAKEanditstwocompared
| approachesonthreedatasets:Alibaba,Backblaze,andAzure.Eachsub-figure |     |               |      |                |     |           |               |     |     | 50  |     |     |     |     |     |
| ------------------------------------------------------------------- | --- | ------------- | ---- | -------------- | --- | --------- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
| corresponds                                                         |     | to a specific | type | of base model. | The | error bar | in the figure |     |     |     |     |     |     |     |     |
40
representstheupperandlowerboundsoftheresults,indicatingtherobustness
| ofUPTAKEacrossdifferentbasemodels. |     |     |     |     |     |     |     |     |     | 30      |     |     |         |     |     |
| ---------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | ------- | --- | --- |
|                                    |     |     |     |     |     |     |     |     |     | 0.0 0.2 | 0.4 | 0.6 | 0.8 1.0 |     |     |
p
TABLEVI
(b) Backblaze
EFFICIENCYCOMPARISONOFUPTAKEANDITSTWOCOMPARED
APPROACHESONALIBABA,BACKBLAZEANDAZUREDATASET.EACH
|     |     |     |     |     |     |     |     | Fig.5. F1-scoreofUPTAKEunderdifferentπp |     |     |     |     | ontwopublicdatasets.The |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------------------------------- | --- | --- | --- | --- | ----------------------- | --- | --- |
VALUEINDICATESTHEAVERAGETIME(S)TAKENOFTHETRAINING
dotsaretheparameterschosenbyoursolution.
EPOCHINTHEMODELUPDATINGPROCESS.
|     |     |     | Offline | Certain |     | UPTAKE |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | ------- | ------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
E. RQ6: Efficiency
|     |     | Alibaba   |       | 5.38 | 12.58 | 4.31  |     |             |            |              |                |               |            |                 |     |
| --- | --- | --------- | ----- | ---- | ----- | ----- | --- | ----------- | ---------- | ------------ | -------------- | ------------- | ---------- | --------------- | --- |
|     |     |           |       |      |       |       |     | Besides     | prediction | performance, |                | efficiency    | is         | also a critical |     |
|     |     | Backblaze |       | 4.38 | 12.75 | 4.12  |     |             |            |              |                |               |            |                 |     |
|     |     | Azure     | 11.54 |      | 27.90 | 10.95 |     |             |            |              |                |               |            |                 |     |
|     |     |           |       |      |       |       |     | metric      | for online | model        | updating.      | Consequently, |            | we compare      |     |
|     |     |           |       |      |       |       |     | the running | time       | of UPTAKE    | with           | other         | approaches | proposed        |     |
|     |     |           |       |      |       |       |     | in Section  | V-A5.      | Since        | the difference |               | between    | different       | ap- |
degradation over time, showcasing its robustness and relia- proaches only exists in the training step, we compared the
averagetimecostofanepochwiththesamehyper-parameters
| bility | in  | real-world | applications. |     |     |     |     |         |             |        |       |           |            |         |     |
| ------ | --- | ---------- | ------------- | --- | --- | --- | --- | ------- | ----------- | ------ | ----- | --------- | ---------- | ------- | --- |
|        |     |            |               |     |     |     |     | on each | time        | phase. |       |           |            |         |     |
|        |     |            |               |     |     |     |     | From    | the results | in     | Table | VI, these | approaches | perform |     |
D. RQ5: Robustness
|     |     |     |     |     |     |     |     | almost   | similarly | in efficiency |              | except | Certain,   | and UPTAKE |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | --------- | ------------- | ------------ | ------ | ---------- | ---------- | --- |
|     |     |     |     |     |     |     |     | take the | least     | time to       | train during | an     | epoch with | 4.31s      | in  |
TofurtherempiricallyevaluatetheperformanceofUPTAKE,
Alibaba,4.12sinBackblaze,and10.95sinAzure.TheCertain
| we     | counted | the results | of      | UPTAKE | for          | different | base models |          |            |         |     |         |             |           |     |
| ------ | ------- | ----------- | ------- | ------ | ------------ | --------- | ----------- | -------- | ---------- | ------- | --- | ------- | ----------- | --------- | --- |
|        |         |             |         |        |              |           |             | approach | is slowest | because |     | Certain | accumulates | instances |     |
| (i.e., | the     | model in    | Section | V-A2)  | on different | cloud     | systems     |          |            |         |     |         |             |           |     |
withcertainlabelsinallformerphases,whichleadstoalarger
| (i.e., | Alibaba, | Backblaze | and | Azure). |     |     |     |          |          |        |             |          |     |             |     |
| ------ | -------- | --------- | --- | ------- | --- | --- | --- | -------- | -------- | ------ | ----------- | -------- | --- | ----------- | --- |
|        |          |           |     |         |     |     |     | training | set. The | larger | the dataset | it uses, | the | longer time | it  |
TheprovidedFig.4displaystheaverageF1-scoreacrossall
takes to train.
| time | phases | for different |     | model | update | strategies | on diverse |     |     |     |     |     |     |     |     |
| ---- | ------ | ------------- | --- | ----- | ------ | ---------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
basemodelsanddatasets.Itisessentialtoclarifythat“Offline” F. RQ7: Parameter Sensitivity
| denotes |     | the theoretical | optimal |     | performance | of  | the current |                |     |            |     |             |           |     |      |
| ------- | --- | --------------- | ------- | --- | ----------- | --- | ----------- | -------------- | --- | ---------- | --- | ----------- | --------- | --- | ---- |
|         |     |                 |         |     |             |     |             | We investigate |     | the impact |     | of the only | parameter | π   | used |
p
system at a given time, assuming ideal conditions. However, in UPTAKE. It reflects the ratio of positive instances in all
| achieving |     | this theoretical |     | best performance |     | in practical | appli- |           |          |            |     |               |          |     |       |
| --------- | --- | ---------------- | --- | ---------------- | --- | ------------ | ------ | --------- | -------- | ---------- | --- | ------------- | -------- | --- | ----- |
|           |     |                  |     |                  |     |              |        | uncertain | positive | instances. |     | Our algorithm | suggests |     | using |
cations is hindered by the UPLearning problem. the Precision value on the T1 stage to set π , which is an
p
Fig.4clearlydemonstratesUPTAKE’ssuperiorperformance estimation using historical information.
over other model update strategies across all scenarios and Inthisexperiment,wegridsearchthevalueofπ from0to
p
models. Notably, it closely approaches the theoretical best 1ona0.1basestep.Fig.5showstheeffectivenessofdifferent
performance (Offline). UPTAKE exhibits greater stability over π p intermsofF1-score.Inthisfigure,eachlineistheaverage
time, as indicated by the smaller fluctuations in performance F1-score of the prediction model (RNN, LSTM, Transformer,
metrics,highlightingitsrobustnessandreliabilitycomparedto and TCNN) on the Alibaba and Backblaze datasets, respec-
other model updating strategies. tively. The dots represent the π p chosen by our solution.
9

Despite minor perturbations under different π , the overall theonlineretrainingstrategydiscussedinSectionIII,UPTAKE
p
performance is stable, and our selected π p consistently yield significantlyreducedrequiredmitigationactionsandenhanced
near-optimal performance, which indicates UPTAKE is robust service availability. These results demonstrate UPTAKE’s sub-
in practice without the need to tune parameters extensively. stantialbenefitsforonlinefailurepredictionmodels,highlight-
|                 |          |            |                 |         |         |             |                 | ing its effectiveness |            | and          | positive   | business         |            | impact.    |              |
| --------------- | -------- | ---------- | --------------- | ------- | ------- | ----------- | --------------- | --------------------- | ---------- | ------------ | ---------- | ---------------- | ---------- | ---------- | ------------ |
|                 |          |            | VI. DISCUSSIONS |         |         |             |                 |                       |            |              |            |                  |            |            |              |
|                 |          |            |                 |         |         |             |                 | C. Future             | Directions | for          | Model      | Evaluation       |            |            |              |
| A. Threats      | to       | Validity   |                 |         |         |             |                 |                       |            |              |            |                  |            |            |              |
|                 |          |            |                 |         |         |             |                 | Evaluation            | over       | long running |            | periods.         |            |            |              |
|                 |          |            |                 |         |         |             |                 |                       |            |              |            |                  | The        | current    | scope of     |
| Internal        | threats. | Our        | implementation  |         | choices |             | are a potential |                       |            |              |            |                  |            |            |              |
|                 |          |            |                 |         |         |             |                 | our research          | primarily  |              | focuses    | on demonstrating |            |            | the efficacy |
| internal        | threat.  | To address | this,           | we      | utilize | established |                 | imple-                |            |              |            |                  |            |            |              |
|                 |          |            |                 |         |         |             |                 | of our predictive     |            | model        | through    | short-term,      |            | controlled | experi-      |
| mentations      | for      | our deep   | learning        | models, |         | detailed    | in              | Section               |            |              |            |                  |            |            |              |
|                 |          |            |                 |         |         |             |                 | ments designed        |            | to mirror    | real-world |                  | scenarios. | This       | approach     |
| V-A2. Moreover, |          | our        | implementation  |         | is      | openly      | accessible,     |                       |            |              |            |                  |            |            |              |
waschosentoprovideaclear,immediatecomparisonbetween
ensuringtransparencyandenablingfutureresearchreplication.
traditionalmodelsandourproposedmethod.Weacknowledge
| External | threats. | External |     | threats | stem | from model | and | data |     |     |     |     |     |     |     |
| -------- | -------- | -------- | --- | ------- | ---- | ---------- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
theimportanceofevaluationonlongtimeperiodsandconsider
| selection, | as  | well as | comparisons |     | with | other | methods. | We  |     |     |     |     |     |     |     |
| ---------- | --- | ------- | ----------- | --- | ---- | ----- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
itanessentialdirectionforfutureresearch,intendingtoextend
| mitigate | selection | bias | by incorporating |     | diverse |     | datasets | from |     |     |     |     |     |     |     |
| -------- | --------- | ---- | ---------------- | --- | ------- | --- | -------- | ---- | --- | --- | --- | --- | --- | --- | --- |
ouranalysistocovermoreperiodsandassessthesustainability
threedistinctcloudsystems,coveringbothnodeanddisk-level
|                        |          |       |        |          |               |            |           | and adaptability |             | of our       | model       | over time. |       |           |          |
| ---------------------- | -------- | ----- | ------ | -------- | ------------- | ---------- | --------- | ---------------- | ----------- | ------------ | ----------- | ---------- | ----- | --------- | -------- |
| data. These            | datasets | align | with   | industry |               | standards, | enhancing |                  |             |              |             |            |       |           |          |
|                        |          |       |        |          |               |            |           | Changing         | proportions |              | of failures |            | over  | time. Our | research |
| the representativeness |          |       | of our | results. | Additionally, |            | this      | study            |             |              |             |            |       |           |          |
|                        |          |       |        |          |               |            |           | acknowledges     |             | that failure | rates       | and        | their | patterns  | are not  |
pioneersinvestigationsintotheUPLearningproblem,selecting
|           |              |          |            |     |       |               |          | static, but | vary       | across    | different     | time | windows,  | reflecting | the      |
| --------- | ------------ | -------- | ---------- | --- | ----- | ------------- | -------- | ----------- | ---------- | --------- | ------------- | ---- | --------- | ---------- | -------- |
| standard  | model        | updating | strategies |     | and   | a theoretical |          | optimal     |            |           |               |      |           |            |          |
|           |              |          |            |     |       |               |          | dynamic     | nature     | of cloud  | environments. |      | The       | initial    | focus on |
| strategy, | as explained |          | in Section |     | V-A5. | We remain     |          | open to     |            |           |               |      |           |            |          |
|           |              |          |            |     |       |               |          | specific    | real-world | ternaries | was           | to   | establish | a baseline | for      |
| exploring | new          | cloud    | component  |     | data  | and model     | updating |             |            |           |               |      |           |            |          |
immediateimpactandmeasurement.Movingforward,weplan
| techniques | in  | future research |     | to enhance |     | our study’s | depth. |                   |     |             |     |         |          |     |            |
| ---------- | --- | --------------- | --- | ---------- | --- | ----------- | ------ | ----------------- | --- | ----------- | --- | ------- | -------- | --- | ---------- |
|            |     |                 |     |            |     |             |        | to systematically |     | investigate | the | model’s | response |     | to varying |
Constructthreats.Constructthreatsconcernourchosenmet-
|               |             |     |            |                 |               |     |             | failure proportions |            | over       | extended               | periods, |     | aiming      | to develop |
| ------------- | ----------- | --- | ---------- | --------------- | ------------- | --- | ----------- | ------------------- | ---------- | ---------- | ---------------------- | -------- | --- | ----------- | ---------- |
| rics and      | parameters. | We  | utilize    | widely-accepted |               |     | metrics     | such                |            |            |                        |          |     |             |            |
|               |             |     |            |                 |               |     |             | more adaptive       |            | predictive | strategies             | that     | can | accommodate | the        |
| as precision, | recall,     | and | F1-score   | for             | effectiveness |     | evaluation, |                     |            |            |                        |          |     |             |            |
|               |             |     |            |                 |               |     |             | evolving            | conditions | of         | cloud infrastructures. |          |     |             |            |
| and training  | time        | for | efficiency | measurement.    |               |     | Future      | evalua-             |            |            |                        |          |     |             |            |
tions will incorporate additional metrics for a more compre- VII. RELATEDWORK
| hensive        | assessment. | Parameters     |            | in     | UPTAKE     | are      | defined     | based        |             |              |            |           |           |            |             |
| -------------- | ----------- | -------------- | ---------- | ------ | ---------- | -------- | ----------- | ------------ | ----------- | ------------ | ---------- | --------- | --------- | ---------- | ----------- |
|                |             |                |            |        |            |          |             | Failure      | prediction. | In           | recent     | years,    | various   | approaches | for         |
| on established |             | rules (Section |            | V-A3), | with       | detailed | discussions |              |             |              |            |           |           |            |             |
|                |             |                |            |        |            |          |             | predicting   | cloud       | failure      | have       | appeared, | including |            | hard drive  |
| about the      | primary     | parameter,     |            | π p ,  | in Section | V-F,     | ensuring    | a            |             |              |            |           |           |            |             |
|                |             |                |            |        |            |          |             | disk failure | and         | node failure | prediction |           | [25],     | [29],      | [30], [57]. |
| well-informed  |             | evaluation     | framework. |        |            |          |             |              |             |              |            |           |           |            |             |
Asabinaryclassificationproblem,machinelearninganddeep
B. Deployment learning mechanisms are widely used for failure prediction.
Machinelearningapproachesforcloudfailureprediction,such
| Our UPTAKE    |          | framework |             | is deployed | on   | Azure,       | a platform |               |            |           |            |           |           |        |            |
| ------------- | -------- | --------- | ----------- | ----------- | ---- | ------------ | ---------- | ------------- | ---------- | --------- | ---------- | --------- | --------- | ------ | ---------- |
|               |          |           |             |             |      |              |            | as support    | vector     | machine   | [33]       | and       | tree      | models | [58]–[61], |
| with millions |          | of nodes  | serving     | a           | wide | customer     | base.      | The           |            |           |            |           |           |        |            |
|               |          |           |             |             |      |              |            | use several   | monitoring |           | metrics    | collected | in        | a time | window to  |
| process       | consists | of three  | core        | phases:     | data | preparation, |            | model         |            |           |            |           |           |        |            |
|               |          |           |             |             |      |              |            | predict       | whether    | the cloud | component  |           | will fail | soon.  | However,   |
| retraining,   | and      | model     | deployment. |             |      |              |            |               |            |           |            |           |           |        |            |
|               |          |           |             |             |      |              |            | these machine |            | learning  | approaches |           | struggle  | to     | handle the |
Datapreparation.Duringthisphase,collecteddataiscleaned complex temporal information of cloud systems [34]. Deep
| and engineered |           | to ensure |           | completeness |             | and | quality.       | These    |            |                |     |              |       |             |          |
| -------------- | --------- | --------- | --------- | ------------ | ----------- | --- | -------------- | -------- | ---------- | -------------- | --- | ------------ | ----- | ----------- | -------- |
|                |           |           |           |              |             |     |                | learning | approaches | such           | as  | RNN          | [32], | LSTM        | [28] and |
| steps are      | essential | for       | enhancing | the          | reliability |     | and effective- |          |            |                |     |              |       |             |          |
|                |           |           |           |              |             |     |                | TCNN     | [34] can   | better capture |     | the temporal |       | correlation | of the   |
ness of subsequent model retraining. complex monitoring metrics than classical machine learning
Model retraining. In this stage, the failure prediction model approaches. In recent years, Transformers have outperformed
undergoes retraining. To address challenges related to the conventional deep-learning approaches. The state-of-the-art
UPLearningproblem,UPTAKEisintegratedintotheretraining performance is achieved by NTAM [26], which incorporates
process, effectively mitigating associated issues. both temporal and spatial information into failure prediction.
|       |             |     |     |           |       |     |          | Our research |     | is orthogonal |     | to previous |     | failure | prediction |
| ----- | ----------- | --- | --- | --------- | ----- | --- | -------- | ------------ | --- | ------------- | --- | ----------- | --- | ------- | ---------- |
| Model | deployment. |     | The | retrained | model | is  | deployed | on           |     |               |     |             |     |         |            |
AzureML, a platform designed for seamless management and approaches since we aim to solve the model updating issue
|            |     |        |         |      |           |     |     | and boost | the | overall performance |     | of  | failure | prediction. |     |
| ---------- | --- | ------ | ------- | ---- | --------- | --- | --- | --------- | --- | ------------------- | --- | --- | ------- | ----------- | --- |
| deployment | of  | online | models. | Once | deployed, |     | the | model     |     |                     |     |     |         |             |     |
actively performs online cloud failure prediction, providing Uncertain Labels. UPLearning solves uncertain/unlabeled
insights into potential failure events within the cloud system. problems for classification tasks [37]–[43]. It defines positive
To gauge UPTAKE’s effectiveness in terms of business samples and unlabeled ones for the training phase. For ex-
impact,weconductA/Btesting,measuringreducedmitigation ample, an unbiased risk estimator [44] is proposed to solve
action times and improved service availability. Compared to this problem. Different from PULearning, the UPLearning is
10

| identified | in the   | model | updating | phase,    | where    | the samples   | for    |               |           |         |               |             |            |            |              |
| ---------- | -------- | ----- | -------- | --------- | -------- | ------------- | ------ | ------------- | --------- | ------- | ------------- | ----------- | ---------- | ---------- | ------------ |
|            |          |       |          |           |          |               |        | [9] Z. Xie,   | S. Zhang, | Y.      | Geng, Y.      | Zhang,      | M. Ma, X.  | Nie, Z.    | Yao, L. Xu,  |
|            |          |       |          |           |          |               |        | Y. Sun,       | W. Li     | et al., | “Microservice |             | root cause | analysis   | with limited |
| retraining | have     | three | classes: | positive, | negative | and uncertain |        |               |           |         |               |             |            |            |              |
|            |          |       |          |           |          |               |        | observability |           | through | intervention  | recognition | in         | the latent | space,” in   |
| positive   | samples. | This  | approach | allows    | the      | model to      | refine |               |           |         |               |             |            |            |              |
Proceedingsofthe30thACMConferenceonKnowledgeDiscoveryand
| its predictions |     | by incorporating |     | the | uncertainty | of samples, |     |     |     |     |     |     |     |     |     |
| --------------- | --- | ---------------- | --- | --- | ----------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
DataMining,2024.
|         |           |     |         |            |     |           |     | [10] Y. Chen, | H.  | Xie, M. | Ma, Y. | Kang, X. | Gao, L. | Shi, Y. | Cao, X. Gao, |
| ------- | --------- | --- | ------- | ---------- | --- | --------- | --- | ------------- | --- | ------- | ------ | -------- | ------- | ------- | ------------ |
| thereby | enhancing | its | overall | robustness | and | accuracy. |     |               |     |         |        |          |         |         |              |
H.Fan,M.Wenetal.,“Automaticrootcauseanalysisvialargelanguage
VIII. CONCLUSION modelsforcloudincidents,”inProceedingsoftheNineteenthEuropean
ConferenceonComputerSystems,2024,pp.674–688.
| Cloud | failure | prediction |     | and auto-mitigation |     | are | crucial |                                                            |     |     |     |     |     |     |     |
| ----- | ------- | ---------- | --- | ------------------- | --- | --- | ------- | ---------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
|       |         |            |     |                     |     |     |         | [11] Z.Zeng,Y.Zhang,Y.Xu,M.Ma,B.Qiao,W.Zou,Q.Chen,M.Zhang, |     |     |     |     |     |     |     |
to maintain the reliability of cloud systems. Through our X. Zhang et al., “Traceark: Towards actionable performance anomaly
|           |            |     |                |               |       |                    |     | alerting             | for online | service | systems,”             | in           | 2023 IEEE/ACM |             | 45th Interna- |
| --------- | ---------- | --- | -------------- | ------------- | ----- | ------------------ | --- | -------------------- | ---------- | ------- | --------------------- | ------------ | ------------- | ----------- | ------------- |
| practical | experience |     | from deploying |               | cloud | failure prediction |     |                      |            |         |                       |              |               |             |               |
|           |            |     |                |               |       |                    |     | tional               | Conference | on      | Software              | Engineering: | Software      | Engineering | in            |
| models    | on Azure,  | we  | identify       | a significant |       | issue known        | as  |                      |            |         |                       |              |               |             |               |
|           |            |     |                |               |       |                    |     | Practice(ICSE-SEIP). |            |         | IEEE,2023,pp.258–269. |              |               |             |               |
UPLearning, which arises during the model updating process. [12] H. Li, M. Ma, Y. Liu, S. Qin, B. Qiao, R. Yao, H. Chaturvedi,
|     |     |     |     |     |     |     |     | T. Tran, | M.  | Chintalapati, | S.  | Rajmohan | et al., “Codec: |     | Cost-effective |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | ------------- | --- | -------- | --------------- | --- | -------------- |
Thisissuecriticallyimpairsthepredictionperformanceinreal-
durationpredictionsystemfordeadlineschedulinginthecloud,”in2023
| world scenarios. |     | To address |     | this, we | introduce | a novel | model |     |     |     |     |     |     |     |     |
| ---------------- | --- | ---------- | --- | -------- | --------- | ------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
IEEE34thInternationalSymposiumonSoftwareReliabilityEngineering
updating approach, referred to as UPTAKE, which enhances (ISSRE). IEEE,2023,pp.298–308.
the performance of various predictive models including RNN, [13] R. Ding, C. Zhang, L. Wang, Y. Xu, M. Ma, X. Wu, M. Zhang,
|     |     |     |     |     |     |     |     | Q. Chen, | X.  | Gao, X. | Gao et | al., “Tracediag: | Adaptive, |     | interpretable, |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | ------- | ------ | ---------------- | --------- | --- | -------------- |
LSTM, Transformer, and TCNN. Our experiments on both and efficient root cause analysis on large-scale microservice systems,”
public and private cloud datasets have shown that UPTAKE in Proceedings of the 31st ACMJoint European Software Engineering
substantially outperforms baseline methods, achieving signif- ConferenceandSymposiumontheFoundationsofSoftwareEngineering,
2023,pp.1762–1773.
icantly improved performance. Furthermore, by integrating [14] M.Ma,Z.Yin,S.Zhang,S.Wang,C.Zheng,X.Jiang,H.Hu,C.Luo,
UPTAKE into our cloud platforms, we have proven tangible Y.Li,N.Qiuetal.,“Diagnosingrootcausesofintermittentslowqueries
inclouddatabases,”ProceedingsoftheVLDBEndowment,vol.13,no.8,
| benefits | in practical | applications |     | and | demonstrated | the | robust- |     |     |     |     |     |     |     |     |
| -------- | ------------ | ------------ | --- | --- | ------------ | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
pp.1176–1189,2020.
| ness of | UPTAKE | in enhancing |     | the failure | prediction | and | auto- |             |         |          |     |        |         |              |         |
| ------- | ------ | ------------ | --- | ----------- | ---------- | --- | ----- | ----------- | ------- | -------- | --- | ------ | ------- | ------------ | ------- |
|         |        |              |     |             |            |     |       | [15] Z. Yu, | C. Pei, | X. Wang, | M.  | Ma, C. | Bansal, | S. Rajmohan, | Q. Lin, |
mitigation in the real-world cloud environments. D. Zhang, X. Wen, J. Li et al., “Pre-trained kpi anomaly detection
|     |     |     |     |     |     |     |     | model | through | disentangled |     | transformer,” | in Proceedings |     | of the 30th |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | ------- | ------------ | --- | ------------- | -------------- | --- | ----------- |
ACKNOWLEDGMENT ACMConferenceonKnowledgeDiscoveryandDataMining,2024.
|          |           |     |             |     |       |              |     | [16] N. Zhao, | J. Zhu, | Y.  | Wang, M. | Ma, W. | Zhang, D. | Liu, M. | Zhang, and |
| -------- | --------- | --- | ----------- | --- | ----- | ------------ | --- | ------------- | ------- | --- | -------- | ------ | --------- | ------- | ---------- |
| We thank | Microsoft |     | engineering |     | teams | engaged with | us, |               |         |     |          |        |           |         |            |
D.Pei,“Automaticandgenericperiodicityadaptationforkpianomaly
contributing their expertise and efforts to this research. We detection,” IEEE Transactions on Network and Service Management,
also thank the reviewers, whose insightful feedback improve vol.16,no.3,pp.1170–1183,2019.
|             |     |            |     |     |     |     |     | [17] Z.Wang,C.Pei,M.Ma,X.Wang,Z.Li,D.Pei,S.Rajmohan,D.Zhang, |          |     |                  |     |                      |     |             |
| ----------- | --- | ---------- | --- | --- | --- | --- | --- | ------------------------------------------------------------ | -------- | --- | ---------------- | --- | -------------------- | --- | ----------- |
| the quality | of  | this work. |     |     |     |     |     |                                                              |          |     |                  |     |                      |     |             |
|             |     |            |     |     |     |     |     | Q. Lin,                                                      | H. Zhang | et  | al., “Revisiting |     | vae for unsupervised |     | time series |
anomalydetection:Afrequencyperspective,”inProceedingsoftheACM
REFERENCES
onWebConference2024,2024,pp.3096–3105.
[1] C.Colman-Meixner,C.Develder,M.Tornatore,andB.Mukherjee,“A [18] Y. Chen, C. Zhang, M. Ma, Y. Liu, R. Ding, B. Li, S. He et al.,
surveyonresiliencytechniquesincloudcomputinginfrastructuresand “Imdiffusion: Imputed diffusion models for multivariate time series
applications,”IEEECommunicationsSurveys&Tutorials,vol.18,no.3, anomalydetection,”VLDBEndowment,vol.17,no.3,p.359–372,2023.
|     |     |     |     |     |     |     |     | [19] M. | Ma, S. Zhang, | J.  | Chen, | J. Xu, | H. Li, Y. Lin, | X. Nie, | B. Zhou, |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ------------- | --- | ----- | ------ | -------------- | ------- | -------- |
pp.2244–2281,2016.
[2] B.Alouffi,M.Hasnain,A.Alharbietal.,“Asystematicliteraturereview Y. Wang, and D. Pei, “Jump-starting multivariate time series anomaly
on cloud computing security: threats and mitigation strategies,” IEEE detection for online service systems,” in Proceedings of the Annul
Access,vol.9,pp.57792–57807,2021. TechnicalConference(ATC). USENIX,2021,pp.413–426.
[3] Z. Yu, M. Ma, C. Zhang, S. Qin, Y. Kang, C. Bansal, S. Rajmohan, [20] M. Babaioff, R. Lempel, B. Lucier, I. Menache, A. Slivkins, and
|          |     |         |        |                         |     |             |       | S. C.-w. | Wong, | “Truthful | online | scheduling | of cloud | workloads | under |
| -------- | --- | ------- | ------ | ----------------------- | --- | ----------- | ----- | -------- | ----- | --------- | ------ | ---------- | -------- | --------- | ----- |
| Y. Dang, | C.  | Pei, D. | Pei et | al., “Monitorassistant: |     | Simplifying | cloud |          |       |           |        |            |          |           |       |
servicemonitoringvialargelanguagemodels,”inCompanionProceed- uncertainty,” in Proceedings of the international conference on World
ingsofthe32ndACMInternationalConferenceontheFoundationsof WideWeb,2022,pp.151–161.
SoftwareEngineering,2024,pp.38–49. [21] L. Zeng, P. Huang, K. Luo, X. Zhang et al., “Fograph: Enabling real-
[4] V.Ganatra,A.Parayil,S.Ghosh,Y.Kang,M.Ma,C.Bansal,S.Nath, time deep graph inference with fog computing,” in Proceedings of the
internationalconferenceonWorldWideWeb,2022,pp.1774–1784.
| and | J. Mace, | “Detection | is  | better than | cure: | A cloud incidents | per- |     |     |     |     |     |     |     |     |
| --- | -------- | ---------- | --- | ----------- | ----- | ----------------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
spective,” in Proceedings of the 31st ACM Joint European Software [22] A.Alhilal,T.Braud,B.Han,andP.Hui,“Nebula:Reliablelow-latency
EngineeringConferenceandSymposiumontheFoundationsofSoftware video transmission for mobile cloud gaming,” in Proceedings of the
Engineering,2023,pp.1891–1902. internationalconferenceonWorldWideWeb,2022,pp.3407–3417.
[5] P. Jin, S. Zhang, M. Ma, H. Li, Y. Kang, L. Li, Y. Liu, B. Qiao, [23] Y.Jiang,C.Zhang,S.He,Z.Yang,M.Ma,S.Qin,Y.Kang,Y.Dang,
et al., S.Rajmohan,Q.Linetal.,“Xpert:Empoweringincidentmanagement
| C. Zhang, | P.  | Zhao |     | “Assess and | summarize: | Improve | outage |     |     |     |     |     |     |     |     |
| --------- | --- | ---- | --- | ----------- | ---------- | ------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
understandingwithlargelanguagemodels,”inProceedingsofthe31st withqueryrecommendationsvialargelanguagemodels,”inProceedings
ACMJointEuropeanSoftwareEngineeringConferenceandSymposium oftheIEEE/ACM46thInternationalConferenceonSoftwareEngineer-
| ontheFoundationsofSoftwareEngineering,2023,pp.1657–1668. |     |     |     |     |     |     |     | ing,2024,pp.1–13. |     |     |     |     |     |     |     |
| -------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | --- | --- | --- | --- | --- | --- |
[6] Q.Lin,T.Li,P.Zhao,Y.Liu,M.Ma,L.Zheng,M.Chintalapati,B.Liu, [24] X.Qin,M.Ma,Y.Zhao,J.Zhang,C.Du,Y.Liu,A.Parayil,C.Bansal,
P. Wang, H. Zhang et al., “Edits: An easy-to-difficult training strategy S. Rajmohan, ´I. Goiri et al., “How different are the cloud workloads?
for cloud failure prediction,” in Companion Proceedings of the ACM characterizinglarge-scaleprivateandpubliccloudworkloads,”in2023
WebConference2023,2023,pp.371–375. 53rd Annual IEEE/IFIP International Conference on Dependable Sys-
[7] A. Stocco, P. J. Nunes, M. d’Amorim, and P. Tonella, “Thirdeye: temsandNetworks(DSN). IEEE,2023,pp.522–530.
|           |      |          |            |         |           |                |     | [25] S. Zhang, | P.  | Jin, Z. | Lin, Y. | Sun, B. | Zhang, S. | Xia, Z. | Li, Z. Zhong, |
| --------- | ---- | -------- | ---------- | ------- | --------- | -------------- | --- | -------------- | --- | ------- | ------- | ------- | --------- | ------- | ------------- |
| Attention | maps | for safe | autonomous | driving | systems,” | in Proceedings |     |                |     |         |         |         |           |         |               |
ofthe37thIEEE/ACMInternationalConferenceonAutomatedSoftware M.Ma,W.Jinetal.,“Robustfailurediagnosisofmicroservicesystem
Engineering,2022,pp.1–12. through multimodal data,” IEEE Transactions on Services Computing,
[8] H. Lu, H. Wang, Q. Wu, H. Luo, Q. Zhao, B. Liu, Q. Si, S. Zheng, vol.16,no.6,pp.3851–3864,2023.
| W. Guo, | and | N. Ren, | “Automatic | control | and | optimal operation | for |     |     |     |     |     |     |     |     |
| ------- | --- | ------- | ---------- | ------- | --- | ----------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
greenhousegasmitigationinsustainablewastewatertreatmentplants:A
review,”ScienceoftheTotalEnvironment,vol.855,p.158849,2023.
11

[26] C.Luo,P.Zhao,B.Qiao,Y.Wu,H.Zhang,W.Wu,W.Lu,Y.Dang, [43] B. Liu, Y. Dai, X. Li, W. S. Lee, and P. S. Yu, “Building text
S. Rajmohan, Q. Lin, and D. Zhang, “NTAM: neighborhood-temporal classifiers using positive and unlabeled examples,” in Proceedings of
attention model for disk failure prediction in cloud platforms,” in the International Conference on Data Mining (ICDM). IEEE, 2003,
| ProceedingsoftheInternationalWorldWideWebConferences. |     |     |     |     |     |     | ACM, | pp.179–186.                                                    |     |     |     |     |     |
| ----------------------------------------------------- | --- | --- | --- | --- | --- | --- | ---- | -------------------------------------------------------------- | --- | --- | --- | --- | --- |
|                                                       |     |     |     |     |     |     |      | [44] M.C.DuPlessis,G.Niu,andM.Sugiyama,“Analysisoflearningfrom |     |     |     |     |     |
2021,pp.1181–1191.
[27] Y.Liu,H.Yang,P.Zhao,M.Ma,C.Wen,H.Zhang,C.Luo,Q.Lin, positive and unlabeled data,” Proceedings of the Advances in Neural
C. Yi et al., “Multi-task hierarchical classification for disk failure InformationProcessingSystems,vol.27,2014.
predictioninonlineservicesystems,”inProceedingsoftheConference [45] R. Kiryo, G. Niu, M. C. Du Plessis, and M. Sugiyama, “Positive-
unlabeledlearningwithnon-negativeriskestimator,”Proceedingsofthe
onKnowledgeDiscoveryandDataMining,2022,pp.3438–3446.
AdvancesinNeuralInformationProcessingSystems,vol.30,2017.
[28] Q.Lin,K.Hsieh,Y.Dang,H.Zhang,K.Sui,Y.Xu,J.-G.Lou,C.Li,
Y.Wu,R.Yaoetal.,“Predictingnodefailureincloudservicesystems,” [46] Y.Chen,X.Yang,Q.Lin,H.Zhang,F.Gao,Z.Xu,Y.Dang,D.Zhang,
inProceedingsoftheJointMeetingonEuropeanSoftwareEngineering H.Dong,Y.Xu,H.Li,andY.Kang,“Outagepredictionanddiagnosis
ConferenceandSymposiumontheFoundationsofSoftwareEngineering for cloud service systems,” in Proceedings of the International World
|             |        |                      |     |              |        |           |        | WideWebConferences.                                       |     | ACM,2019,pp.2659–2665. |     |     |     |
| ----------- | ------ | -------------------- | --- | ------------ | ------ | --------- | ------ | --------------------------------------------------------- | --- | ---------------------- | --- | --- | --- |
| (ESEC/FSE). |        | ACM,2018,pp.480–490. |     |              |        |           |        |                                                           |     |                        |     |     |     |
|             |        |                      |     |              |        |           |        | [47] H.Zhou,M.Chen,Q.Lin,Y.Wang,X.She,S.Liu,R.Gu,B.C.Ooi, |     |                        |     |     |     |
| [29] M.     | Ma, Y. | Liu, Y. Tong,        | H.  | Li, P. Zhao, | Y. Xu, | H. Zhang, | S. He, |                                                           |     |                        |     |     |     |
L. Wang, Y. Dang et al., “An empirical investigation of missing data and J. Yang, “Overload control for scaling wechat microservices,” in
handling in cloud node failure prediction,” in Proceedings of the 30th ProceedingsoftheSymposiumonCloudComputing(SoCC),ser.SoCC
ACMJointEuropeanSoftwareEngineeringConferenceandSymposium ’18. NewYork,NY,USA:ACM,2018,p.149–161.
|     |     |     |     |     |     |     |     | [48] Wikipediacontributors,“S.m.a.r.t.—Wikipedia,thefreeencyclopedia,” |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------------------------------------------------------------- | --- | --- | --- | --- | --- |
ontheFoundationsofSoftwareEngineering,2022,pp.1453–1464.
2022,[Online;accessed28-September-2022].[Online].Available:https:
| [30] L. Li, | X. Zhang, | S. He, | Y. Kang, | H. Zhang, | M. Ma, | Y. Dang, | Z. Xu, |     |     |     |     |     |     |
| ----------- | --------- | ------ | -------- | --------- | ------ | -------- | ------ | --- | --- | --- | --- | --- | --- |
S.Rajmohan,Q.Linetal.,“Conan:Diagnosingbatchfailuresforcloud //en.wikipedia.org/w/index.php?title=S.M.A.R.T.&oldid=1109378579
systems,”in2023IEEE/ACM45thInternationalConferenceonSoftware [49] S. Lu, B. Luo, T. Patel, Y. Yao, D. Tiwari, and W. Shi, “Making disk
Engineering: Software Engineering in Practice (ICSE-SEIP). IEEE, failure predictions smarter!” in Proceedings of the Conference on File
|     |     |     |     |     |     |     |     | andStorageTechnologies(FAST). |     | USENIX,2020,pp.151–167. |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------------------- | --- | ----------------------- | --- | --- | --- |
2023,pp.138–149.
|                |     |         |          |         |              |           |         | [50] H. Xu, | N. Kang, G. | Zhang, C. Xie, | X. Liang, | and Z. Li, | “Nasoa: |
| -------------- | --- | ------- | -------- | ------- | ------------ | --------- | ------- | ----------- | ----------- | -------------- | --------- | ---------- | ------- |
| [31] S. Zhang, | Y.  | Liu, W. | Meng, Z. | Luo, J. | Bu, S. Yang, | P. Liang, | D. Pei, |             |             |                |           |            |         |
J. Xu, Y. Zhang et al., “Prefix: Switch failure prediction in datacenter Towards faster task-oriented online fine-tuning with a zoo of models,”
networks,” Proceedings of the ACM on Measurement and Analysis of inProceedingsoftheIEEE/CVFInternationalConferenceonComputer
ComputingSystems(SIGMETRICS),vol.2,no.1,pp.1–29,2018. Vision(ICCV),October2021,pp.5097–5106.
|             |     |          |         |      |           |              |        | [51] T. D. | Sets, “Large-scale | disk failure | prediciton | dataset,” | https:// |
| ----------- | --- | -------- | ------- | ---- | --------- | ------------ | ------ | ---------- | ------------------ | ------------ | ---------- | --------- | -------- |
| [32] C. Xu, | G.  | Wang, X. | Liu, D. | Guo, | and T.-Y. | Liu, “Health | status |            |                    |              |            |           |          |
tianchi.aliyun.com/dataset/dataDetail?dataId=70251,2022.
| assessment | and | failure | prediction | for hard | drives with | recurrent | neural |     |     |     |     |     |     |
| ---------- | --- | ------- | ---------- | -------- | ----------- | --------- | ------ | --- | --- | --- | --- | --- | --- |
networks,”TransactionsonComputers,vol.65,no.11,pp.3502–3508, [52] Backblaze, “The backblzae hard drive data and stats,” https://
| 2016. |     |     |     |     |     |     |     | www.backblaze.com/b2/hard-drive-test-data.html,2022. |     |     |     |     |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | ---------------------------------------------------- | --- | --- | --- | --- | --- |
[33] J.Zhang,J.Wang,L.He,Z.Li,andP.S.Yu,“Layerwiseperturbation- [53] C.Clark,K.Fraser,S.Hand,J.G.Hansen,E.Jul,C.Limpach,I.Pratt,
|       |             |          |     |            |               |              |     | and A. | Warfield, “Live | migration of virtual | machines,” | in Proceedings |     |
| ----- | ----------- | -------- | --- | ---------- | ------------- | ------------ | --- | ------ | --------------- | -------------------- | ---------- | -------------- | --- |
| based | adversarial | training | for | hard drive | health degree | prediction,” |     | in     |                 |                      |            |                |     |
Proceedings of the International Conference on Data Mining (ICDM). ofthe2ndconferenceonSymposiumonNetworkedSystemsDesign&
IEEE,2018,pp.1428–1433. Implementation-Volume2,2005,pp.273–286.
[34] X.Sun,K.Chakrabarty,R.Huang,Y.Chen,B.Zhao,H.Cao,Y.Han, [54] M.C.duPlessis,G.Niu,andM.Sugiyama,“Analysisoflearningfrom
X.Liang,andL.Jiang,“System-levelhardwarefailurepredictionusing positiveandunlabeleddata,”inProceedingsoftheAdvancesinNeural
InformationProcessingSystems,Z.Ghahramani,M.Welling,C.Cortes,
| deep | learning,” | in Proceedings |     | of the | Design Automation |     | Conference |     |     |     |     |     |     |
| ---- | ---------- | -------------- | --- | ------ | ----------------- | --- | ---------- | --- | --- | --- | --- | --- | --- |
(DAC). ACM,2019,p.20. N.Lawrence,andK.Weinberger,Eds.,vol.27. MITPress,2014.
[35] S.Levy,R.Yao,Y.Wu,Y.Dang,P.Huang,Z.Mu,P.Zhao,T.Ramani, [55] M. D. Plessis, G. Niu, and M. Sugiyama, “Convex formulation for
N.Govindaraju,X.Lietal.,“Predictiveandadaptivefailuremitigation learningfrompositiveandunlabeleddata,”inProceedingsofthe32nd
InternationalConferenceonMachineLearning(ICML),ser.Proceedings
| to avert           | production | cloud  | {VM} | interruptions,” | in      | Proceedings | of the  |                                                        |     |     |     |     |        |
| ------------------ | ---------- | ------ | ---- | --------------- | ------- | ----------- | ------- | ------------------------------------------------------ | --- | --- | --- | --- | ------ |
|                    |            |        |      |                 |         |             |         | ofMachineLearningResearch,F.BachandD.Blei,Eds.,vol.37. |     |     |     |     | Lille, |
| Operating          | Systems    | Design | and  | Implementation  | (OSDI). |             | USENIX, |                                                        |     |     |     |     |        |
| 2020,pp.1155–1170. |            |        |      |                 |         |             |         | France:PMLR,07–09Jul2015,pp.1386–1394.                 |     |     |     |     |        |
[36] M. Ma, S. Zhang, D. Pei, X. Huang, and H. Dai, “Robust and rapid [56] A. Paszke, S. Gross, F. Massa, A. Lerer, J. Bradbury, G. Chanan,
adaption for concept drift in software system anomaly detection,” in T.Killeenetal.,“Pytorch:Animperativestyle,high-performancedeep
learninglibrary,”inProceedingsoftheAdvancesinNeuralInformation
| Proceedings         |     | of the International |                     | Symposium | on  | Software | Reliability |                    |                                    |     |     |     |     |
| ------------------- | --- | -------------------- | ------------------- | --------- | --- | -------- | ----------- | ------------------ | ---------------------------------- | --- | --- | --- | --- |
|                     |     |                      |                     |           |     |          |             | ProcessingSystems. | MITPress,2019,vol.32,pp.8024–8035. |     |     |     |     |
| Engineering(ISSRE). |     |                      | IEEE,2018,pp.13–24. |           |     |          |             |                    |                                    |     |     |     |     |
[37] C. Elkan and K. Noto, “Learning classifiers from only positive and [57] C.Zhao,M.Ma,Z.Zhong,S.Zhang,Z.Tan,X.Xiong,L.Yu,J.Feng,
unlabeled data,” in Proceedings of the international conference on Y. Sun et al., “Robust multimodal failure detection for microservice
Knowledgediscoveryanddatamining. ACM,2008,pp.213–220. systems,” in Proceedings of the 29th ACM SIGKDD Conference on
KnowledgeDiscoveryandDataMining,2023,pp.5639–5649.
| [38] M. N. | Nguyen,     | X.-L.            | Li, and | S.-K. Ng,      | “Positive | unlabeled         | learning |                                                                   |     |     |     |     |     |
| ---------- | ----------- | ---------------- | ------- | -------------- | --------- | ----------------- | -------- | ----------------------------------------------------------------- | --- | --- | --- | --- | --- |
|            |             |                  |         |                |           |                   |          | [58] J.Li,X.Ji,Y.Jia,B.Zhu,G.Wang,Z.Li,andX.Liu,“Harddrivefailure |     |     |     |     |     |
| for        | time series | classification,” |         | in Proceedings | of        | the Twenty-Second |          |                                                                   |     |     |     |     |     |
InternationalJointConferenceonArtificialIntelligence,ser.IJCAI’11. prediction using classification and regression trees,” in Proceedings of
AAAIPress,2011,p.1421–1426. the International Conference on Dependable Systems and Networks
[39] X.-L. Li, P. S. Yu, B. Liu, and S.-K. Ng, “Positive unlabeled learning (DSN). IEEE/IFIP,2014,pp.383–394.
|     |     |     |     |     |     |     |     | [59] M.M.Botezatu,I.Giurgiu,J.Bogojeska,andD.Wiesmann,“Predicting |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------------------------------------------------------- | --- | --- | --- | --- | --- |
fordatastreamclassification,”inProceedingsoftheSIAMinternational
|                              |     |     |     |                       |     |     |     | disk replacement | towards | reliable data | centers,” | in Proceedings | of the |
| ---------------------------- | --- | --- | --- | --------------------- | --- | --- | --- | ---------------- | ------- | ------------- | --------- | -------------- | ------ |
| conferenceondatamining(SDM). |     |     |     | SIAM,2009,pp.259–270. |     |     |     |                  |         |               |           |                |        |
[40] B.Liu,W.S.Lee,P.S.Yu,andX.Li,“Partiallysupervisedclassification KnowledgeDiscoveryandDataMining. ACM,2016,pp.39–48.
oftextdocuments,”inProceedingsoftheInternationalConferenceon [60] X.Huang,“Harddrivefailurepredictionforlargescalestoragesystem,”
MachineLearning(ICML),vol.2,no.485,2002,pp.387–394. Ph.D.dissertation,UCLA,2017.
|            |     |                   |     |             |       |       |              | [61] Y. Xu, | K. Sui, R. Yao, | H. Zhang, Q. | Lin, Y. | Dang, P. Li, K. | Jiang, |
| ---------- | --- | ----------------- | --- | ----------- | ----- | ----- | ------------ | ----------- | --------------- | ------------ | ------- | --------------- | ------ |
| [41] X. Li | and | B. Liu, “Learning |     | to classify | texts | using | positive and |             |                 |              |         |                 |        |
unlabeleddata,”inProceedingsoftheTwenty-SecondInternationalJoint W. Zhang, J. Lou, M. Chintalapati, and D. Zhang, “Improving service
ConferenceonArtificialIntelligence,vol.3,2003,pp.587–592. availability of cloud systems by predicting disk error,” in Proceedings
[42] W.S.LeeandB.Liu,“Learningwithpositiveandunlabeledexamples of the USENIX Annul Technical Conference (ATC). USENIX, 2018,
| usingweightedlogisticregression,”inProceedingsoftheInternational |     |     |     |     |     |     |     | pp.481–494. |     |     |     |     |     |
| ---------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- |
ConferenceonMachineLearning(ICML),vol.3,2003,pp.448–455.
12