GPU Occupancy Prediction of Deep Learning
Models Using Graph Neural Network
Hengquan Mei1∗, Huaizhi Qu1∗, Jingwei Sun1†, Yanjie Gao2, Haoxiang Lin2, Guangzhong Sun1
1University of Science and Technology of China, China
2Microsoft Research, China
{hengquanmei, qhz991029}@mail.ustc.edu.cn, {sunjw, gzsun}@ustc.edu.cn, {yanjga, haoxlin}@microsoft.com
Abstract—Over the past few years, deep learning has been hardware instances [7], [10]. For users, since GPU rental can
rapidly adopted in many fields. Among the various hardware be costly, estimating the GPU utilization of their DL models
accelerators specifically for deep learning computation, graphics
canaidinselectingacost-efficientGPUresource.Whenusers
processing units (GPUs) are mainly used. GPU occupancy—the
employ automated machine learning (AutoML) tools, it is
average ratio of active warps to maximum supported warps
on all streaming multiprocessors—is an essential indicator of also beneficial to take GPU utilization into account for better
how well GPUs are utilized. Predicting the GPU occupancy of hyperparameter tuning and neural architecture search [11]–
deep learning models is critical for boosting both job runtime [14]. For developers, extracting the GPU utilization patterns
performance and platform resource efficiency. However, GPU
of different DL models can help design resource-efficient DL
occupancy prediction is challenging due to the complex factors
systems [15], [16].
hidden in framework runtimes and diverse architectures and
hyperparametersofmodels.Inthispaper,weproposeDNN-occu In order to portray the patterns of GPU utilization of
topredicttheGPUoccupancyofdeeplearningmodels.Ourkey DL models, employing a quantitative utilization model for
observationisthatmodelscanberepresentedasdirectedacyclic predictions proves to be a more time-efficient and resource-
computation graphs. DNN-occu extracts a set of occupancy-
saving approach compared to actual execution and profiling
related features from the computational semantics of the graph
[6], [7], especially when a variety of DL model architectures
nodes and edges. It also employs a novel graph neural net-
work for better feature encoding and prediction generalization. and GPU types need to be evaluated [17]. However, GPU
The experiments on various configurations of real-world deep utilization modeling faces two primary challenges. The first
learningmodelsshowthatDNN-occuachieveshighaccuracyfor challengeinvolvesthereadilyavailableGPUutilizationmetric,
occupancy prediction (with an overall error of 9.271%) and has
NVIDIA Management Library (NVML) utilization, typically
astronggeneralizationabilityforunseenmodels.Inaddition,we
acquired through the nvidia-smi command. This metric tends
apply DNN-occu in a trace-driven simulation of deep learning
workload scheduling and achieve up to a 31.45% increase in to overestimate actual GPU utilization and lacks generaliz-
overall GPU utilization and a 19.71% reduction in makespan. ability to unseen DL model architectures. NVML utilization
Index Terms—deep learning, GPU occupancy, graph neural is defined as the “percent of time over the past sample
network, performance prediction period during which one or more kernels was executing on
the GPU” [18] and does not accurately represent the finer-
I. INTRODUCTION grained runtime status within GPUs. For instance, a GPU
kernel (i.e., a compiled routine designed to execute on GPUs)
Overthepastfewyears,deeplearning(DL)hasbeenrapidly
withacontinuoussingle-threadrunwillresultin100%NVML
adopted in various fields, including computer vision, natural
utilization, although a large portion of hardware resources
language processing, recommender systems, gaming, etc. The
are actually idle. The second challenge is caused by the
growth of data volume and model complexity has led to
vast architecture and hyperparameter configuration space of
increasing demands for deep learning accelerators. Graphics
DL models, complicating the design of an accurate ML-
processing units (GPUs) have emerged as the most prevalent
based prediction model from limited samples. It is difficult
accelerators for deep learning computation. Prominent cloud
to generalize to unseen DL models, even if they use the same
platforms,suchasMicrosoftAzureMachineLearning[1]and
operatorsasseenmodels[13],[19],[20].Forexample,despite
AmazonSageMaker[2],provideGPUresourcesfordeploying
bothBERT[21]andGPT[22]beingtransformer-based,using
and executing DL workloads as a part of their Infrastructure
thetrainingdatafromaBERTmodeltoaccuratelypredictthe
as a Service (IaaS) [3]–[5].
performance of a GPT model is still challenging.
To understand resource efficiency, it is crucial to moni-
In this paper, we propose DNN-occu, a tool that predicts
tor and forecast the hardware utilization of GPUs [6]–[9].
the GPU occupancy of DL models before job execution using
For resource providers, understanding the variation trend in
Graph Neural Network (GNN). This tool provides insight-
GPU utilization allows them to make appropriate scheduling
ful guidance for subsequent scheduling or decision-making.
strategiestodeployco-locatedworkloadsefficientlyonproper
DNN-occu addresses the above-mentioned two challenges
∗HengquanMeiandHuaizhiQucontributedequallytothiswork. as follows. Firstly, instead of NVML utilization, DNN-occu
†Correspondingauthor. predicts the GPU occupancy of DL models, which is a fine-

| grained | GPU | utilization | metric. | The | definition | of  | streaming |     |     |     |     |     |     |     |
| ------- | --- | ----------- | ------- | --- | ---------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
Input
| multiprocessor |                | occupancy | is   | “the ratio | of          | active warps | on        | a   |     |     |     |     |     |     |
| -------------- | -------------- | --------- | ---- | ---------- | ----------- | ------------ | --------- | --- | --- | --- | --- | --- | --- | --- |
| streaming      | multiprocessor |           | (SM) | to         | the maximum |              | number of |     |     |     |     |     |     |     |
MaxPool
active warps supported by the SM.” [23] The average occu- Conv2D Conv2D Conv2D
2D
| pancy across | all | SMs | represents | the | overall | occupancy | of the |     |     |     |     |     |     |     |
| ------------ | --- | --- | ---------- | --- | ------- | --------- | ------ | --- | --- | --- | --- | --- | --- | --- |
entireGPU.Suchametricismuchmorepreciseinportraying
Concat
| the portion | of  | occupied | GPU | computation |     | units than | NVML |     |     |     |     |     |     |     |
| ----------- | --- | -------- | --- | ----------- | --- | ---------- | ---- | --- | --- | --- | --- | --- | --- | --- |
utilization. Because obtaining exact occupancy needs costly Average
runtime profiling, a quick prediction of GPU occupancy is Pool2D
| necessary | for | guiding | better | scheduling. | Secondly, |     | since the |     |     |     |     |     |     |     |
| --------- | --- | ------- | ------ | ----------- | --------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
architectures of DL models evolve quickly, it is impractical Flatten
| to collect | all DL | models’ | runtime | profiling |     | data exhaustively. |     |     |     |     |     |     |     |     |
| ---------- | ------ | ------- | ------- | --------- | --- | ------------------ | --- | --- | --- | --- | --- | --- | --- | --- |
Therefore, DNN-occu leverages a representative set of DL Dense
| models to | build | a prediction |     | model | and extrapolates |     | the GPU |     |     |     |     |     |     |     |
| --------- | ----- | ------------ | --- | ----- | ---------------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
occupancy of unseen DL model architectures. To achieve this Fig.1. ComputationgraphofanexampleDLmodel.
| goal, DNN-occu |               | adopts    | a unified  |         | representation  | for     | all DL    |        |          |                  |     |             |              |         |
| -------------- | ------------- | --------- | ---------- | ------- | --------------- | ------- | --------- | ------ | -------- | ---------------- | --- | ----------- | ------------ | ------- |
| models,        | regarding     | each      | of them    | as      | a directed      | acyclic | graph.    |        |          |                  |     |             |              |         |
|                |               |           |            |         |                 |         |           | engine | DNN-occu | reduces          | the | performance | interference |         |
| Each node      | in            | the graph | represents |         | a computational |         | operator  |        |          |                  |     |             |              |         |
|                |               |           |            |         |                 |         |           | caused | by GPU   | over-allocation. |     | This leads  | to           | up to a |
| (e.g., 2D      | convolution), |           | and        | an edge | denotes         | the     | data flow |        |          |                  |     |             |              |         |
31.45%increaseinoverallGPUutilizationanda19.71%
betweentwonodes.Buildinguponthisdatarepresentationand
|                      |      |               |        |         |                 |         |         | reduction | in makespan |     | compared | to existing | approaches. |     |
| -------------------- | ---- | ------------- | ------ | ------- | --------------- | ------- | ------- | --------- | ----------- | --- | -------- | ----------- | ----------- | --- |
| feature engineering, |      | we            | design | a novel | attention-based |         | GNN     |           |             |     |          |             |             |     |
| architecture         | with | a transformer |        | encoder | to              | fit the | mapping |           |             |     |          |             |             |     |
II. BACKGROUND
betweenDLmodelarchitectures,theorderofkernelexecution,
runtime factors, and the associated GPU occupancy. A. DL Models and Computation Graphs
In addition, we conduct a trace-driven simulation of co- Fig. 1 shows the computation graph of an example DL
location DL workload scheduling to demonstrate the appli- model in popular deep learning frameworks, such as PyTorch
| cation of | the | predicted | GPU | occupancy |     | from DNN-occu. |     |                     |     |       |      |                      |     |      |
| --------- | --- | --------- | --- | --------- | --- | -------------- | --- | ------------------- | --- | ----- | ---- | -------------------- | --- | ---- |
|           |     |           |     |           |     |                |     | [24] and TensorFlow |     | [25]. | A DL | model is represented |     | by a |
Although co-location could improve GPU utilization, it also directed acyclic graph, also known as a computation graph.
introduces performance interference. Based on the predicted A node in the graph represents a tensor computation operator
| GPU occupancy |     | of  | unseen | DL  | models | from DNN-occu, |     |                 |     |         |         |          |      |         |
| ------------- | --- | --- | ------ | --- | ------ | -------------- | --- | --------------- | --- | ------- | ------- | -------- | ---- | ------- |
|               |     |     |        |     |        |                |     | (e.g., Conv2d), | and | an edge | denotes | the data | flow | between |
our scheduler determines an appropriate combination of co- two nodes. Each operator invokes specific APIs from GPU-
location jobs to reduce interference. Our approach avoids accelerated libraries (e.g., NVIDIA cuDNN [26]), and the
profiling kernel patterns, modifying the underlying DL frame- library executes a sequence of kernels on GPUs to perform
| work, and | tracing | job       | execution | online | (which | requires | GPU       | the computation. |     |     |     |     |     |     |
| --------- | ------- | --------- | --------- | ------ | ------ | -------- | --------- | ---------------- | --- | --- | --- | --- | --- | --- |
| isolation | at the  | scheduler | runtime). |        | All    | of these | tasks are |                  |     |     |     |     |     |     |
|           |         |           |           |        |        |          |           | B. GPU Occupancy |     |     |     |     |     |     |
expensiveandtime-consuming.Experimentalfindingsdemon-
strate that GPU occupancy outperforms NVML utilization as The occupancy of a streaming multiprocessor is “the ratio
a more effective guiding metric for downstream co-location of active warps on a streaming multiprocessor (SM) to the
tasks [6], [7]. Furthermore, our approach facilitates hyperpa- maximum number of active warps supported by the SM.”
rameterselectionandimprovestheperformanceofDLmodels. [23] GPU occupancy is the average occupancy across all
We list the main contributions of this paper as follows: SMs. It gives a fine-grained and low-level measurement of
We propose DNN-occu, a tool designed to predict the GPU utilization. In practice, GPU occupancy is sampled by
•
GPU occupancy of DL models accurately during in- hardware performance counters on each warp scheduler of
ference. DNN-occu effectively learns the representation SMs. GPU occupancy is available in Nsight Compute [27]
of different DL model architectures and demonstrates a by the ncu command. However, collecting such a metric is
promising generalization ability to unseen models. both time-consuming and resource-consuming. Therefore, it
We design a set of node and edge features to represent motivates us to design a model for efficiently predicting the
•
GPUruntimefactors.WealsoproposeaneffectiveGNN- GPU occupancy of DL models rather than relying on costly
| based | model | to  | map these | factors | to  | the corresponding |     | profiling. |     |     |     |     |     |     |
| ----- | ----- | --- | --------- | ------- | --- | ----------------- | --- | ---------- | --- | --- | --- | --- | --- | --- |
GPU occupancy. The prediction targets cover a broad NVIDIA Management Library (NVML) utilization is an-
range of DL models, including CNN-based, RNN-based, other metric for GPU utilization, which is often easily ob-
andTransformer-basedmodels.DNN-occuprovidesfine- tained.Itisdefinedasthe“percentoftimeoverthepastsample
grained forecasts of hardware resource usage by DL period during which one or more kernels was executing on
models. the GPU.” [18] Users acquire this metric from the nvidia-smi
Weexperimentallydemonstratethat,whenintegratedinto (NVIDIA System Management Interface) command, which
•
a simulated DL job co-location scheduler, the prediction invokesthebackendNVMLAPI.Suchahigh-levelutilization

90
80
70
60
50
40
20 40 60 80 100
Batch size
)%(scirteM
noitazilitU
UPG
DL model Runtime Model
Architecture Configuration Configuration
GPU occupancy
NVML utilization
Computation Graph
Fig.2. ComparisonofGPUoccupancyandNVMLutilization.
metricisprettycoarseandcannotmeasurehowmanySMsare MLP
actually in use.
Fig. 2 shows the difference between the two metrics of
Occupancy
GPUoccupancyandNVMLutilizationwhentrainingResNet-
50 [28] on the CIFAR10 dataset [29] and an NVIDIA A100.
The y-axis value of each point in Fig. 2 is the average metric
value weighted by the kernels’ duration. With the increase in
the batch size, NVML utilization reaches around 90%, while
GPU occupancy is about 45%. In general, NVML utilization
provides a relaxed upper bound of GPU utilization; therefore,
GPUoccupancyismuchmorepreciseinmeasuringtheactual
usage of hardware resources, revealing more potential for
performance improvement.
C. Graph Neural Networks
The graph is a commonly used data structure for rep-
resenting elements and their dependencies. The family of
graphneuralnetworks(GNNs)hasdemonstratedeffectiveness
in various applications and domains [30]–[32], prompting
the emergence of numerous methods aimed at accelerating
GNN training [33]. The main objective of GNNs is to learn
to structure the information representation as a graph. The
learningprocessofGNNsconsistsofpropagatinginformation
between the nodes and edges of the graph through multiple
message-passing mechanisms, followed by aggregation. In
eachmessage-passingiteration,therepresentationofthenodes
andedgesareupdated.Thefinallearnedembeddingsareused
for downstream tasks such as regression, classification, and
link prediction.
III. DNN-OCCUDESIGN
A. Problem Formulation of GPU Occupancy Prediction
GivenaDLmodel,includingmodelarchitectureM,model
configuration C (e.g., the batch size, input channel size,
m
hidden size, etc.), and runtime configuration C (e.g., GPU
r
floating-point operations per second (FLOPS), memory band-
width of the device, etc.), DNN-occu is to find a function
f∗ :(M,(M|C )×C )|w∗ →occu
m r
kernel kernel kernel kernel kernel kernel kernel kernel kernel kernel kernel kernel
0
2 1
3
4
Node & Edge
Feature Engineering
ANEE
Graphormer
Set Transformer
Decoder
Fig.3. WorkflowofDNN-occu.
thatpredictstheGPUoccupancyoccuforMduringinference
iterations of the input DL model, achieving a minimum
empiricallossLbetweenthepredictedoccuandthemeasured
occupancy ocˆcu. The parameters of f∗ are solved by:
w∗ =argminL(ocˆcu,f((M,(M|C )×C )|w)).
m r
w
For a model M consisting of n kernels at runtime, DNN-
occu provides a general form of occupancy predictions:
occupancy=aggr{occu , occu , ..., occu }, 1 2 n
where occu denotes the GPU occupancy of the i-th kernel.
i
The aggregation function aggr(·) can be max, min, mean, etc.
In this paper, we choose mean as a representative aggre-
gationfunctionforstudying.AverageGPUoccupancyusually
revealstheresourceusageofDLworkloadsthroughoutthelife
cycleandisanessentialindicatortoprovidemoreinsightsfor
co-location DL workload scheduling [7], [34].
B. DNN-occu Overview
The overall workflow of DNN-occu is shown in Fig. 3. As
introduced in Section II-A, a DL model is represented by a
computation graph and is later transformed into a sequence
of kernels executed on GPUs. Based on this fact, we con-
sider the prediction of GPU occupancy as a mapping from
a computation graph to an occupancy value. The workflow
of DNN-occu mainly consists of four stages: (1) DNN-occu
takes the DL model architecture, runtime configuration, and
model configuration as input. We use Nsight Compute [27]
to analyze the kernel and corresponding GPU occupancy, and
we use ONNX [35] to obtain an intermediate representation
of the input model. (2) We calculate the arithmetic average
occupancy of the DL model according to the kernel. The

TABLEI Similarly,foroperatorsinRNN-basedmodels,wecalculate
NODEANDEDGEFEATURES. the FLOPs based on their input and output tensor sizes. For
Transformer-basedmodelssuchasBERT,sincetheycontaina
Name Description
Operator Typeoftheoperator large number of attention modules that are essentially gener-
Type (e.g.,Conv2d,MaxPool2d) alizedmatrixmultiplication(GEMM)operations,wecalculate
Typeandvalueofeachhyper-
Hyper- the FLOPs of GEMM as their features.
parameteroftheoperator
parameter
(e.g.,kernelsizeandchannelsize)
Temporary Sizesoftemporaryvariables D. GNN-based Encoder
TensorSize usedbytheoperator
Transformer-based models have demonstrated excellent
Node Input/Output Sizesofinputs,outputstensor
Features TensorSize shapeoftheoperator learning capabilities so far and are now widely adopted in
Operator Numberoffloating-point computer vision and natural language processing. Models
FLOPs operationsoftheoperator
with transformer architecture [31], [37], [38] have further
GPUpeakfloating-point
GPUFLOPS
operationspersecond exhibited exceptional performance in a wide range of tasks
GPUMemory MemorycapacityofGPU on the graph. Motivated by these advances, our study aims
Capacity
to leverage the strong learning abilities to develop a model
Numberofstreaming
SMs
multiprocessors with solid generalization capabilities, allowing it to perform
Edge Typeoftheedge well on unseen input models. Consequently, we propose our
Type (e.g.,ForwardorBackward)
model design, consisting of the ANEE (attention-based node-
Edge EdgeTensor
Sizeofthedeliveredtensor
Features Size edge encoder) layer [13], Graphormer layer [31], and Set
Edge Bandwidthforprocessing TransformerDecoderlayer[32],whichisshowninthemiddle
Bandwidth thedeliveredtensor
part of Fig. 3.
The ANEE layer utilizes attention to encode the feature of
inputgraphsefficiently.Supposeg isacomputationgraph,we
fused data contains complete dependency relations among oc-
denote a node as u and an edge as l = (u ,u ). We further
cupancydataandthecomputationgraphsothatthesubsequent s d
use hi and ei to represent the computed feature vectors of
supervised learning can be smoothly conducted. (3) DNN- u l
node u and edge l in the i-th round. First, the ANEE layer
occuadoptsaneffectiveGNN-basedencodertoaggregateand
comprising parameter matrices W , W , and W computes
update the features of the graph nodes over several rounds. u e m
the intermediate result of hi (denoted by h¯i) as follows [13]:
ThentheaggregatedresultsarefedtoanMLP[36].(4)DNN- u u
occu outputs the final prediction of GPU occupancy based on h¯i =LeakyReLU (cid:0) W ×hi−1(cid:1) .
u u u
the MLP predictor.
Next,theANEElayerupdatesei ofedgel=(s,d)asfollows:
l
C. Feature Engineering ei =σ (cid:0) aT × (cid:0) h¯i ∥h¯i(cid:1) ×W ×ei−1(cid:1) ,
l s d e l
Fordesigningfeatures,wecarefullyconsidertheunderlying
implementation of DL frameworks and ensure the features
where a∈R2×N1 is a weight vector and aT is its transpose,
and ∥ is the vector concatenation operation. Then, the layer
have precise computational semantics and a high correlation
gathers the information of node u from its neighboring nodes
to GPU occupancy. Table I lists the adopted features for
and associated edges as follows:
graphnodesandedges.Thesefeaturesareconcatenatedintoa
numerical feature vector for each node and edge. Categorical f(u′,l′)=Softmax (cid:0) W ×ei(cid:1) ×h¯i ,
m l′ u′
features, such as the operator type, are converted into numer-  
ical features by one-hot encoding. (cid:88)
The tensor size and number of floating-point operations
hi
u
=LeakyReLU f(u′,l′),
l′=(u′,u)
(FLOPs)arecalculatedfromthehyperparametervaluesofthe
DL model. We take the 2D convolution operator (denoted by where u′ is a neighbor node of u.
Conv2d) as an example to illustrate how to compute them The encoded features are then fed forward to Graphormer
underforwardpropagationforinference.Conv2dreceivesan layers. The Graphormer layer can be characterized by the
input feature mapping N ×C ×H ×W (i.e., a batch of N layer normalization (LN), multi-head self-attention (MHA),
input feature maps with the height and width H ×W and C and feedforward network (FFN) as follows:
channels)andasetofconvolutionalfiltersK×C×R×S (K h¯i =MHA (cid:0) LN (cid:0) hi−1(cid:1)(cid:1) +hi−1,
filters with the kernel size R×S and C channels). Conv2d u u u
generatesanoutputfeaturemapofsizeN×K×P×Q(with hi u =FFN (cid:0) LN (cid:0) h¯i u (cid:1)(cid:1) +h¯i u .
a batch of N output feature maps with the height and width
To introduce Set Transformer Decoder, we first define
P ×Q and K channels). P and Q can be inferred from the MultiheadAttentionBlock(MAB)ontheinputX,Y ∈Rn×d
input feature maps and filter shapes as well as from the addi-
with respect to the previous denotation as follows:
tionalstrideandpaddingparameters[26].Thus,theFLOPsof
theConv2discalculatedby2×K×C×R×S×N×P×Q. MAB(X,Y)=LN(H¯i+FFN(H¯i)),

|     |                                   |     | TABLEII |     |     |     |     |     |     |     | TABLEIII     |     |     |     |     |
| --- | --------------------------------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | --- | --- | --- |
|     | STATISTICSOFTHEDATASETSANDMODELS. |     |         |     |     |     |     |     |     |     | SYSTEMSETUP. |     |     |     |     |
◦CNN-based,△RNN-based,□Transformer-based Specification System-1 System-2 System-3
|           |     |     |             |     |     |     |     | GPUModel  |     |     | A100 | RTX2080Ti |     |     | P40 |
| --------- | --- | --- | ----------- | --- | --- | --- | --- | --------- | --- | --- | ---- | --------- | --- | --- | --- |
| ModelName |     |     | Variants    |     |     |     |     |           |     |     |      |           |     |     |     |
|           |     |     |             |     |     |     |     | GPUNumber |     |     | 2    |           | 8   |     | 4   |
| ◦ConvNext |     |     | ConvNext-B1 |     |     |     |     |           |     |     |      |           |     |     |     |
◦ResNet ResNet-18,ResNet-34,ResNet-50 GPUArch Ampere Turing Tesla
| ◦VGG             |     |     | VGG-11,VGG-13,VGG-16 |     |     |     |     | GPUMemory |     |           | 80GB   |           | 11GB   |           | 22.5GB |
| ---------------- | --- | --- | -------------------- | --- | --- | --- | --- | --------- | --- | --------- | ------ | --------- | ------ | --------- | ------ |
| ◦AlexNet         |     |     | Vanillamodel         |     |     |     |     | CPUCore   |     |           | 12     |           | 28     |           | 24     |
| ◦LeNet           |     |     | Vanillamodel         |     |     |     |     |           |     |           |        |           |        |           |        |
|                  |     |     |                      |     |     |     |     |           |     | IntelXeon |        | IntelXeon |        | IntelXeon |        |
| △LSTM            |     |     | Vanillamodel         |     |     |     |     | CPUModel  |     |           |        |           |        |           |        |
|                  |     |     |                      |     |     |     |     |           |     | w5-2455X  |        | E5-2680v4 |        | E5-2690v4 |        |
| △RNN             |     |     | Vanillamodel         |     |     |     |     |           |     |           |        |           |        |           |        |
|                  |     |     |                      |     |     |     |     | CUDA      |     |           | 11.7   |           | 10.2   |           | 11.0   |
| □ViT             |     |     | ViT-S,ViT-T          |     |     |     |     |           |     |           |        |           |        |           |        |
| □SwinTransformer |     |     |                      |     |     |     |     | PyTorch   |     |           | 1.13.1 |           | 1.12.0 |           | 1.12.0 |
Swin-S
| □MaxViT |     |     | MaxViT-T     |     |     |     |     |               |     |          |        |     |        |     |        |
| ------- | --- | --- | ------------ | --- | --- | --- | --- | ------------- | --- | -------- | ------ | --- | ------ | --- | ------ |
|         |     |     |              |     |     |     |     | TensorFlow    |     |          | 1.15.0 |     | 1.15.0 |     | 1.15.0 |
| □BERT   |     |     | DistilBERT   |     |     |     |     |               |     |          |        |     |        |     |        |
|         |     |     |              |     |     |     |     | NsightCompute |     | 2023.1.1 |        |     | 2019.5 |     | 2020.1 |
| □GPT-2  |     |     | Vanillamodel |     |     |     |     |               |     |          |        |     |        |     |        |
□CLIP
RN-50,ViT-B/32,ViT-B/16
Valuesoftypicalhyperparametersfortheabovemodels.
CNN-based:batchsize∈{4x|4≤x≤32,x∈N}, asthenumberoflayers,batchsize,andhiddensize.ForCNN-
inputchannel∈[1,10]. based models, we choose ConvNext [39], ResNet [28], VGG
RNN-based:batchsize∈{8x|16≤x≤64,x∈N},
|     |     |     |     |     |     |     |     | [40], AlexNet |     | [41], and | LeNet | [42]. | We  | consider | the batch |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | --------- | ----- | ----- | --- | -------- | --------- |
sequencelength∈{8x|2≤x≤16,x∈N}.
|     |     |     |     |     |     |     |     | size (from | 16 to | 128 with | step | 4), input | channel |     | size (from 1 |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ----- | -------- | ---- | --------- | ------- | --- | ------------ |
Transformer-based:batchsize∈{4x|4≤x≤32,x∈N},
inputchannel∈[1,10],sequencelength∈{20,512}. to10withstep1),inputheight(224),andinputwidth(224)as
1B:base,S:small,T:tiny,RN50:ResNet-50 the hyperparameters. For RNN-based models, we use LSTM
[43]andRNN[36].Weusedifferentdomainsofthebatchsize
|     |     |     |     |     |     |     |     | (from 128 | to 512 | with | step 8) | and | sequence | length | (from 16 |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------ | ---- | ------- | --- | -------- | ------ | -------- |
where
|     |     |     |     |     |     |     |     | to 128 with | step | 8) as | the hyperparameters. |     |     | For Transformer- |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ---- | ----- | -------------------- | --- | --- | ---------------- | --- |
H¯i =LN(X+MHA(X,Y,Y)).
|     |     |     |     |     |     |     |     | based models, |     | we select | ViT | [44], | Swin | Transformer | [45], |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | --------- | --- | ----- | ---- | ----------- | ----- |
Using MAB, we define Set Attention Block as MaxViT [46], BERT (distilbert-base-uncased-finetuned-sst-2-
|     |     |     |     |     |     |     |     | english) | [47], GPT-2 | [22], | and | multimodal |     | model | CLIP [48]. |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ----------- | ----- | --- | ---------- | --- | ----- | ---------- |
SAB(X)=MAB(X,X).
|     |     |     |     |     |     |     |     | The hyperparameters |     |     | include | the batch | size | (from | 16 to 128 |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------- | --- | --- | ------- | --------- | ---- | ----- | --------- |
Then, we define Pooling by Multihead Attention (PMA) with withstep4),inputchannelsize(from1to10withstep1),and
∈Rk×d sequence length (from 20 to 512). Other model configuration
| k learnable | seed | vectors | S   | on a | set of | feature | vectors |     |     |     |     |     |     |     |     |
| ----------- | ---- | ------- | --- | ---- | ------ | ------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
Hi ∈Rn×d as parameters are default. We run these models at maximum
|     |     |     |     |     |     |     |     | capacity | on the | machine | until | they | encounter | out-of-memory |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------ | ------- | ----- | ---- | --------- | ------------- | --- |
(Hi)=MAB(S,FFN(Hi)).
PMA (OOM) errors. These models basically include typical model
k
|          |           |     |             |         |     |           |     | configurations | in  | various | real-world |     | domains. |     |     |
| -------- | --------- | --- | ----------- | ------- | --- | --------- | --- | -------------- | --- | ------- | ---------- | --- | -------- | --- | --- |
| Finally, | we define | Set | Transformer | Decoder |     | operating | on  |                |     |         |            |     |          |     |     |
∈Rn×d In total, our dataset contains 20 models with various op-
| features        | Hi  | as  |         |         |                     |        |     |         |              |     |         |          |        |     |         |
| --------------- | --- | --- | ------- | ------- | ------------------- | ------ | --- | ------- | ------------ | --- | ------- | -------- | ------ | --- | ------- |
|                 |     |     |         |         |                     |        |     | erators | (>30 types), |     | from 13 | to 2,664 | nodes, | and | from 12 |
| Decoder(Hi)=FFN |     |     | (cid:0) | (cid:0) | (Hi) (cid:1)(cid:1) | ∈Rk×d. |     |         |              |     |         |          |        |     |         |
SAB PMA k to 2,722 edges per computation graph. We employ ONNX
|     |     |     |     |     |     |     |     | [35] to | generate | DL  | model | intermediate |     | representation, | so  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | -------- | --- | ----- | ------------ | --- | --------------- | --- |
E. Loss Function
|              |           |                  |      |          |           |         |        | theoretically,                                          | DNN-occu    |       | can        | support    | more      | than 140      | operators |
| ------------ | --------- | ---------------- | ---- | -------- | --------- | ------- | ------ | ------------------------------------------------------- | ----------- | ----- | ---------- | ---------- | --------- | ------------- | --------- |
| The          | GNN-based | prediction       |      | of GPU   | occupancy |         | can be |                                                         |             |       |            |            |           |               |           |
|              |           |                  |      |          |           |         |        | included                                                | in ONNX.    |       | Currently, | the        | model     | configuration | is        |
| formulated   | as a      | graph regression |      | problem. | We        | use the | mean   |                                                         |             |       |            |            |           |               |           |
|              |           |                  |      |          |           |         |        | deterministic,                                          | and         | there | are        | no control | flow      | operators     | (e.g.,    |
| square error | (MSE)     | as the           | loss | function | for this  | task:   |        |                                                         |             |       |            |            |           |               |           |
|              |           |                  |      |          |           |         |        | loops and                                               | conditional |       | branches), | so         | we assume | the           | same exe- |
|              |           |                  | N    |          |           |         |        | cutionflowandruntimeperformanceacrossdifferentinference |             |       |            |            |           |               |           |
1 (cid:88)
|     |     | L=  |     | (yˆ −y | )2, |     |     |             |     |     |     |     |     |     |     |
| --- | --- | --- | --- | ------ | --- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     | i i    |     |     |     | iterations. |     |     |     |     |     |     |     |
N
i=1
|           |               |        |           |        |           |          |     | B. Hardware     | and | Runtime | Environment |     |       |          |           |
| --------- | ------------- | ------ | --------- | ------ | --------- | -------- | --- | --------------- | --- | ------- | ----------- | --- | ----- | -------- | --------- |
| where N   | is the        | number | of models | in the | training  | dataset, | yˆ  | i               |     |         |             |     |       |          |           |
|           |               |        |           |        |           |          |     | Our experiments |     | are     | conducted   | on  | three | systems, | and their |
| and y are | the predicted |        | and real  | GPU    | occupancy | values   | of  |                 |     |         |             |     |       |          |           |
i
the i-th model configuration, respectively. setups are listed in Table III. Any other parameters keep the
|     |     |     |     |     |     |     |     | default | settings. |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | --------- | --- | --- | --- | --- | --- | --- |
IV. EXPERIMENTALSETUP
C. Metrics
| A. Datasets | and | Models    |           |         |                |     |     |                |     |     |            |     |          |     |            |
| ----------- | --- | --------- | --------- | ------- | -------------- | --- | --- | -------------- | --- | --- | ---------- | --- | -------- | --- | ---------- |
|             |     |           |           |         |                |     |     | For evaluating |     | GPU | occupancy, | we  | evaluate | the | prediction |
| As shown    | in  | Table II, | we select | various | representative |     | DL  |                |     |     |            |     |          |     |            |
performancebyMeanSquareError(MSE)andMeanRelative
| modelsanduseastochasticstrategytogeneratemodelconfig- |          |              |     |         |        |          |      | Error (MRE): |     |            |          |     |     |     |     |
| ----------------------------------------------------- | -------- | ------------ | --- | ------- | ------ | -------- | ---- | ------------ | --- | ---------- | -------- | --- | --- | --- | --- |
| urations                                              | based on | the provided |     | API. We | create | numerous | data |              |     |            |          |     |     |     |     |
|                                                       |          |              |     |         |        |          |      |              |     | N (cid:12) | (cid:12) |     |     | N   |     |
a n d m o d e l s b y re fi n i n g e ac h m o d e l a r c h it e c t u re i nt o s ev e r a l 1 (cid:88)(cid:12) yˆ −y i(cid:12) 1 (cid:88)
|     |     |     |     |     |     |     |     | MRE= |     | i        | ,        | MSE= |     | (yˆ | −y )2, |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | -------- | -------- | ---- | --- | --- | ------ |
|     |     |     |     |     |     |     |     |      |     | (cid:12) | (cid:12) |      |     |     | i i    |
c o nfi gu r a ti o n s by c h a n g in g th e va l u e s o f h y p e r p a ra m e ter s s u c h N (cid:12) y i (cid:12) N
|     |     |     |     |     |     |     |     |     | i=1 |     |     |     |     | i=1 |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

where N is the number of models in the test dataset, and yˆ, DNN-occu uses one ANEE layer, two Graphormer layers,
i
y are the predicted and real peak GPU occupancy of the i- and two Set Transformer Decoder layers. We set the hidden
i
th model, respectively. We chose these two metrics because dimensionofallthelayersto256;thelearningrateandweight
they are widely used as standard measures of the accuracy of decayarebothsetto0.0001.WeusetheAdam[53]optimizer
predictive models in classification. with default hyperparameters to train DNN-occu.
A. How Effective is DNN-occu?
D. Comparison Baselines
1) ResultsofpredictingGPUoccupancyforasinglemodel:
To compare with the GNN-based model of DNN-occu, we
In this section, we compare DNN-occu with five baselines on
consider the following models as the baselines:
thesametestdatasettoevaluatetheeffectivenessofpredicting
(1) MLP (multilayer perceptron) [36] is a foundational
GPUoccupancyforasingleDLmodelthatrunsexclusivelyon
model in machine learning and serves as the basis for many
a GPU. Fig. 4 shows the results of our experiments involving
complex neural network designs. It was employed to predict
all the compared baselines for predicting GPU occupancy.
theexecution timeof operators[49].Here, weadopt thesame
Fig. 4 (a) shows the prediction results of DNN-occu on
node features utilized by DNN-occu to calculate the MLP
NVIDIAA100forvariousmodels.WhileMLPperformswell
predictions.
on seen test models, its predictions on unseen test models
(2) LSTM (long short-term memory) [50] is widely used
are poor, with an MRE/MSE of 90.435%/0.721. Such poor
invariousapplications,includingnaturallanguageprocessing,
performance is attributed to the overfitting of MLP and its
timeseriesanalysis,andotherapplicationswheretheinputhas
lack of strong generalization ability. On the seen test models,
a sequential structure.
the difference between the predictions of DNN-occu and
(3) Transformer [51] is a well-known time series predic-
all the baselines is insignificant. In contrast, on unseen test
tion model whose attention module can efficiently utilize the
models, DNN-occu achieves the best MRE/MSE values of
information on different time steps between series data.
5.496%/0.003, demonstrating a notable generalization ability.
(4) DNNPerf [13] is a runtime performance prediction tool
Fig. 4 (b) and Fig. 4 (c) show the prediction results of
for deep learning models. It adopts a GNN-based ANEE
DNN-occu on different devices for the tested models. Once
layerandsystematicallyexploresperformance-relatedfeatures
again, DNN-occu achieves the optimal predictions on the
derived from the semantics of the computation graph and
unseen test models, surpassing all the baselines on NVIDIA
hidden factors within the framework.
RTX 2080Ti and P40. The experimental results confirm the
(5)BRP-NAS[20]adoptsagraphconvolutionalnetworkfor
effectivenessofDNN-occuacrossvariousmodelsanddevices,
predictingmodellatencyinneuralarchitecturesearchtasks.It
demonstratingsuperiorextensible-modelandextensible-device
focuses on modeling the impact from the computation graph
generalization. The advantage of DNN-occu is its ability to
structure while overlooking runtime factors associated with
learn the characteristics, trends, and development patterns of
nodes and edges.
GPU occupancy changes from the DL model computation
WehaveimplementedMLP,LSTM,Transformer,DNNPerf,
graph, model configuration, and runtime configuration. This
and BRP-NAS with PyTorch 1.12.0 [24] and DGL 1.0.1
ability enables flexible prediction of future changes in GPU
[52]. After tuning these models, we choose the following
occupancy.
hyperparameter values. For MLP, we use four layers whose
2) Results of predicting GPU occupancy for multimodal
widths are set to 80, 512, 512, and 256, respectively. For
models: Multimodal models usually consist of multiple input
LSTM, we use two layers, each having 256 channels. For
modalities (e.g., images, text, and speech), so their analysis
Transformer, we only use the encoder part. We use three
and prediction are much more complex than unimodal mod-
encoderlayers,andeachlayerconsistsoffourattentionheads
els. The GNN, a deep learning model for graph-structured
and a 512-channel FFN. For DNNPerf and BRP-NAS, the
data, can process multimodal data and discover underlying
learning rate and weight decay are 0.0001, the same as other
relationships and patterns. We model multimodal data sepa-
baselines.
rately as independent graph structures and utilize DNN-occu
for learning, fusion, and prediction. DNN-occu employs the
V. EVALUTION
neural architecture to model the consistency and correlation
ToassessthepredictionaccuracyofDNN-occu,weemploy between these modalities and obtain better multimodal data
it to predict GPU occupancy during inference for the DL representation and feature extraction.
models listed in Table II. We divide 80% of the total dataset WetakethemultimodalmodelCLIPasanexampleandrun
(ViT-T,LSTM,RNN,ResNet-34,ResNet-18,VGG-16,VGG- bothlanguageandimageencoderssimultaneously.DNN-occu
13, VGG-11, AlexNet, and LeNet) to the training dataset and constructs multimodal graphs for learning the relationships
allocatetheremaindertothetestdataset.Thesemodelsarere- betweennodesandedges.Thismethodcanefficientlyprocess
ferredtoasseentestmodels.Furthermore,wecreateaseparate multimodaldataandeffectivelydiscoverrelationshipsbetween
test dataset for ViT-S, BERT, ConvNext-B, and ResNet-50, different modalities. Predicting the multimodal models GPU
whose models are unseen by DNN-occu. That is, the training occupancy helps select optimal hyperparameters and their
dataset does not include any of their configurations. values (such as the batch size). As demonstrated in Table

103
102
101
100
ViT-T LSTM RNN ResNet-34ResNet-18 VGG-16 VGG-13 VGG-11 AlexNet LeNet ViT-S BERT ConvNextResNet-50
unseen unseen unseen unseen
)%(
ERM
DNN-occu Transformer
MLP DNNPerf
LSTM BRP-NAS
(a)EvaluationresultsonNVIDIAA100.
104
103
102
101
100
ViT-T LSTM RNN ResNet-34ResNet-18 VGG-16 VGG-13 VGG-11 AlexNet LeNet ViT-S BERT ConvNextResNet-50
unseen unseen unseen unseen
)%(
ERM
DNN-occu Transformer
MLP DNNPerf
LSTM BRP-NAS
(b)EvaluationresultsonNVIDIARTX2080Ti.
104
103
102
101
100
ViT-T LSTM RNN ResNet-34ResNet-18 VGG-16 VGG-13 VGG-11 AlexNet LeNet ViT-S BERT ConvNextResNet-50
unseen unseen unseen unseen
)%(
ERM
DNN-occu Transformer
MLP DNNPerf
LSTM BRP-NAS
(c)EvaluationresultsonNVIDIAP40.
Fig.4. EvaluationresultsofGPUoccupancyprediction.
IV, when compared to other baseline methods, DNN-occu of the numbers, perform experiments on each subset, and
can effectively learn performance patterns, fuse computation present the prediction results in Fig. 5. Moving from left to
graphs, and make predictions on multimodal models. The rightinthefigure,theexperimentaldevicesareNVIDIAA100,
experimental results illustrate the advantages of GNN-based RTX 2080Ti, and P40, respectively. DNN-occu achieves a
DNN-occu prediction and the key importance of GNNs in satisfactory level of accuracy and outperforms all the baseline
predicting the runtime performance of DL models. methods.TheMREvaluesofDNN-occufordifferentnumbers
of nodes range from 2.940% to 5.014% for A100 predictions,
B. How Robust is DNN-occu? from 0.233% to 2.095% for RTX 2080Ti predictions, and
from 1.046% to 21.382% for P40 predictions, respectively.
Ourdatasetcontainsavarietyofneuralarchitectureswhose
The MRE values of DNN-occu for different numbers of
numbers of the nodes and edges are widely distributed. We
edges range from 2.197% to 41.298% for A100 predictions,
splitthedatasetintoseveralsubsetsbasedonthevalueranges

TABLEIV
PREDICTIONOFGPUOCCUPANCYONTHEMULTIMODALMODELCLIP.
PredictionofGPUoccupancy
Model
onmultimodalmodelonNVIDIAA100
Name
Metric DNN-occu DNNPerf BRP-NAS
RN50(seen) MRE(%) 3.686 637.369 108.611
ViT-B/16(seen) MRE(%) 1.829 924.529 144.702
ViT-B/32(unseen) MRE(%) 3.614 937.356 134.573
PredictionofGPUoccupancy
Model
onmultimodalmodelonNVIDIAP40
Name
Metric DNN-occu DNNPerf BRP-NAS
RN50(seen) MRE(%) 11.724 112.863 173.318
ViT-B/16(seen) MRE(%) 3.395 115.226 175.242
ViT-B/32(unseen) MRE(%) 2.73 115.108 175.333
104
103
102
101
100
500 1000
#nodes
)%(ERM
104 104
103
103
102
102 101
101 100
250 500 750 200 400 600 800
#nodes #nodes
104
103
102
101
100
500 1000 1500
#edges
)%(ERM
TABLEV
GENERALIZATIONONTRANSFORMER-BASEDMODELS.
Model GeneralizationonNVIDIAA100
Name Metric DNN-occu DNNPerf BRP-NAS
SwinTransformer MRE(%) 9.829 735.787 235.174
MaxViT MRE(%) 8.075 175636.913 68579.639
ViT-S MRE(%) 5.239 163.795 118.171
BERT MRE(%) 8.470 1025.604 581.469
GPT-2 MRE(%) 185.817 901.541 421.053
Model GeneralizationonNVIDIARTX2080Ti
Name Metric DNN-occu DNNPerf BRP-NAS
SwinTransformer MRE(%) 8.032 115.171 129.084
MaxViT MRE(%) 10.445 742606.716 19475.475
ViT-S MRE(%) 7.459 104.621 107.621
BERT MRE(%) 9.071 760.725 470.512
GPT-2 MRE(%) 36.220 103.071 216.373
DNN-occu MLP RNN Transformer DNNPerf BRP-NAS Model GeneralizationonNVIDIAP40
Name Metric DNN-occu DNNPerf BRP-NAS
SwinTransformer MRE(%) 8.883 363.801 142.618
MaxViT MRE(%) 9.750 49309.784 37711.313
ViT-S MRE(%) 0.624 126.345 108.217
BERT MRE(%) 7.126 764.709 531.211
GPT-2 MRE(%) 69.318 473.288 246.846
VI. APPLICATIONCASESOFDNN-OCCU
104 104
In this section, we investigate the benefits of DNN-occu
103
103 in supporting downstream DL workload scheduling. As case
102 studies, we use two representative tasks: hyperparameter op-
102 101 timization and schedule guidance. In addition, DNN-occu can
101 100 be adopted in other applications, such as power management
250 500 750 250 500 750 andGPUkernelscheduling,whichareofinteresttoourfuture
#edges #edges
work.
A. Hyperparameter Optimization
Fig.5. Robustnessevaluation across variousnumbersof nodesandedges.
Movingfromlefttoright,theexperimentaldevicesareNVIDIAA100,RTX The general utilization of GPUs in deep learning systems
2080Ti,andP40,respectively.
tendstoberelativelymodest.Accordingtoarecentproduction
study [54], the target system’s average GPU utilization was
from 9.090% to 58.080% for RTX 2080Ti predictions, and about 52%, implying that nearly half of the GPUs remained
from 0.567% to 26.652% for P40 predictions, respectively. idle. By analyzing and forecasting the GPU occupancy in
The experimental results demonstrate that DNN-occu exhibits deep learning models, DNN-occu helps tune critical param-
satisfactory robustness across various neural architectures. eters capable of affecting GPU occupancy and enhancing the
program’s overall GPU utilization.
C. How Generalizable is DNN-occu?
Fig.6illustratestheGPUoccupancyandNVMLutilization
Generalization is a significant concern in the field of deep under different batch sizes on NVIDIA A100. By utilizing
learning. For a DL model, we expect it to perform well not DNN-occu,GPUoccupancycanbeaccuratelypredictedacross
only on known (seen) datasets but also on unknown (unseen) varioushyperparametersandtheirvaluesbeforejobexecution.
datasets,i.e.,withremarkablegeneralizationability.Therefore, Therefore,DNN-occuhelpsidentifythevaluesofhyperparam-
we evaluate the generalization ability of DNN-occu through eters that achieve maximum GPU occupancy without time-
extensive experiments. consuming runtime profiling, thereby accelerating hyperpa-
We utilize ViT-T with the attention operator as a training rameter optimization and boosting developer productivity. We
dataset to assess the generalization of DNN-occu for Swin notice that GPU occupancy is always lower than NVML
Transformer, MaxViT, ViT-S, BERT, and GPT-2. As shown utilization,confirmingthatGPUoccupancyservesasatighter
in Table V, DNN-occu achieves an MRE of 9.829% for upper bound for GPU utilization. This also indicates that, as
Swin Transformer, 8.075% for MaxViT, 5.239% for ViT-S, the batch size increases, other bottlenecks emerge that hinder
8.470% for BERT, and 185.817% for GPT-2 on NVIDIA further improvement of GPU occupancy.
A100, surpassing the optimal MRE values of the baselines.
B. Schedule Guidance
Furthermore, on NVIDIA RTX 2080Ti and P40, the predic-
tions of DNN-occu also outperform all the baselines. The Co-location execution means that applications with com-
experimental results demonstrate that DNN-occu exhibits a plementary resource requirements can be placed on the same
strong generalization ability to unseen models. GPUs, resulting in improved aggregated throughput. Due to

|     |     | ViT-S |     | VGG-11 | VGG-13 |     |     |     |     | TABLEVI |     |     |     |     |
| --- | --- | ----- | --- | ------ | ------ | --- | --- | --- | --- | ------- | --- | --- | --- | --- |
)%( egatnecreP 100 ANALYSISOFTHEPACKAGINGSTRATEGYOFDLSCHEDULER
90
|     |     |     |     |     |     |     | Pack              |     |     | Makespan(s) |        | NVMLutilization(%) |     |        |
| --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | --- | ----------- | ------ | ------------------ | --- | ------ |
|     | 80  |     |     |     |     |     | Strategy          |     |     | Avg         | Gain   | Avg                |     | Gain   |
|     |     |     |     |     |     |     | occu-packing      |     |     | 106.87      | 19.71% | 61.23              |     | 31.45% |
|     | 70  |     |     |     |     |     | nvml-util-packing |     |     | 126.58      | 4.90%  | 46.48              |     | -0.21% |
|     | 60  |     |     |     |     |     | slot-packing      |     |     |             |        |                    |     |        |
|     |     |     |     |     |     |     |                   |     |     | 133.10      | N/A1   | 46.58              |     | N/A    |
(disablingco-location)
|     |     | VGG-16 |     | ViT-T | ConvNext |     |     |     |     |     |     |     |     |     |
| --- | --- | ------ | --- | ----- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
1Asthebaseline,ithasnogainandisrepresentedasN/A.
)%( egatnecreP 100
90
80
70
|     |     |     |     |     |     | actual | SM  | usage | at a | fine-grained |     | level | and is | an essential |
| --- | --- | --- | --- | --- | --- | ------ | --- | ----- | ---- | ------------ | --- | ----- | ------ | ------------ |
60 performance indicator for a secure co-location policy. Fig. 7
|     |     |           |     |           |           | indicates |     | that the | JCT | slowdown |     | starts to | rise | dramatically, |
| --- | --- | --------- | --- | --------- | --------- | --------- | --- | -------- | --- | -------- | --- | --------- | ---- | ------------- |
|     |     | ResNet-18 |     | ResNet-34 | ResNet-50 |           |     |          |     |          |     |           |      |               |
)%( egatnecreP 100
|     |     |     |     |     |     | especially |     | when | the | cumulative |     | occupancy | exceeds | 100%. |
| --- | --- | --- | --- | --- | --- | ---------- | --- | ---- | --- | ---------- | --- | --------- | ------- | ----- |
90 Therefore, an appropriate packing policy for multiple jobs
80 should ensure the cumulative occupancy is at most 100% [7].
70
|     |     |     |     |     |     |     | We integrate |     | DNN-occu |     | into a | DL scheduler |     | deployed on |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --- | -------- | --- | ------ | ------------ | --- | ----------- |
60
|     |     |              |     |              |                 | a machine |     | with | four NVIDIA |     | P40 | GPUs | and one | Intel Xeon |
| --- | --- | ------------ | --- | ------------ | --------------- | --------- | --- | ---- | ----------- | --- | --- | ---- | ------- | ---------- |
|     | 50  | 100150200250 | 50  | 100150200250 | 50 100150200250 |           |     |      |             |     |     |      |         |            |
Batch Size Batch Size Batch Size E5-2690 v4 processor. The scheduler uses a GPU-occupancy-
|     |     |               |     |     |                  | based     | bin-packing |      | algorithm  |     | (with | co-location | ensuring         | GPU |
| --- | --- | ------------- | --- | --- | ---------------- | --------- | ----------- | ---- | ---------- | --- | ----- | ----------- | ---------------- | --- |
|     |     | GPU occupancy |     |     | NVML utilization |           |             |      |            |     |       |             |                  |     |
|     |     |               |     |     |                  | occupancy |             | does | not exceed |     | 100%; | denoted     | by occu-packing) |     |
Fig.6. ImpactofthebatchsizeonGPUoccupancyandNVMLutilization. to maximize GPU utilization, while minimizing GPU over-
|     |     |     |     |     |     | allocation |     | and the   | need   | for    | job resubmission |            | caused | by out-    |
| --- | --- | --- | --- | --- | --- | ---------- | --- | --------- | ------ | ------ | ---------------- | ---------- | ------ | ---------- |
|     |     |     |     |     |     | of-memory  |     | failures. | First, | before |                  | submitting | DL     | workloads, |
80
theresourcemanagerderivesthecorrespondingcomputational
70
|     |     |     |     |     |     | graph | from | the | DL model | and | adapts | the input | of  | DNN-occu. |
| --- | --- | --- | --- | --- | --- | ----- | ---- | --- | -------- | --- | ------ | --------- | --- | --------- |
)%( nwodwols TCJ DNN-occu predicts the GPU occupancy of the unexecuted
60
|     |     |     |     |     |     | DL  | workloads. |     | Then, | the system |     | uses the | predicted | value as |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --- | ----- | ---------- | --- | -------- | --------- | -------- |
50
|     |     |     |     |     |     | a          | metric   | for co-location |     | scheduling. |        | The         | system | combines   |
| --- | --- | --- | --- | --- | --- | ---------- | -------- | --------------- | --- | ----------- | ------ | ----------- | ------ | ---------- |
|     | 40  |     |     |     |     | the        | resource | requirements    |     |             | of the | DL workload |        | (i.e., GPU |
|     |     |     |     |     |     | occupancy) |          | and             | the | current     | GPU    | usage       | on the | nodes, and |
30
|     |     |     |     |     |     | schedules  |     | DL models |           | to the   | appropriate |              | node based | on the     |
| --- | --- | --- | --- | --- | --- | ---------- | --- | --------- | --------- | -------- | ----------- | ------------ | ---------- | ---------- |
|     | 20  |     |     |     |     | cumulative |     | GPU       | occupancy |          | of the      | DL           | load not   | exceeding  |
|     |     |     |     |     |     | 100%.      | We  | compare   | our       | approach | with        | slot-packing |            | (disabling |
10
|     |     |     |     |     |     | co-location) |     | and | NVML-utilization-based |     |     |     | bin-packing | [6], [7] |
| --- | --- | --- | --- | --- | --- | ------------ | --- | --- | ---------------------- | --- | --- | --- | ----------- | -------- |
0
50 100 150 200 250 (denoted by nvml-util-packing). The experiments are con-
Cumulative GPU Occupancy (%) ducted on a mix of DL workload samples from Table II. Each
experimentsimulatestheschedulingofdifferentDLworkloads
|     | Fig.7.     | CorrelationofJCTslowdownandGPUoccupancy |           |        |                    |        |          |       |        |           |            |          |              |            |
| --- | ---------- | --------------------------------------- | --------- | ------ | ------------------ | ------ | -------- | ----- | ------ | --------- | ---------- | -------- | ------------ | ---------- |
|     |            |                                         |           |        |                    | into   | GPUs     | using | the    | three     | scheduling | approach |              | above, and |
|     |            |                                         |           |        |                    | each   | approach |       | is run | 100 times | with       | workload | combinations |            |
|     |            |                                         |           |        |                    | scaled | from     | prior | work   | [11],     | [12].      |          |              |            |
| the | contention | of shared                               | resources | (e.g., | cache capacity and |        |          |       |        |           |            |          |              |            |
global memory bandwidth), co-location may impact the job Table VI summarizes that our occu-packing approach
completion time (JCT) of applications when compared to ap- achieves an average NVML utilization of 61.23% compared
plications running separately [7], [34]. To improve the results to slot-packing (46.58%) and nvml-util-packing (46.48%).
of these interference studies, we conducted a preliminary JCT This is because GPU occupancy is a much more precise
| interference |     | analysis. | This | analysis involved | 200 randomly |             |     |     |        |     |       |          |     |             |
| ------------ | --- | --------- | ---- | ----------------- | ------------ | ----------- | --- | --- | ------ | --- | ----- | -------- | --- | ----------- |
|              |     |           |      |                   |              | measurement |     | of  | actual | GPU | usage | compared | to  | the coarse- |
selected combinations of co-location DL model executions grainedNVMLutilization.Itprovidesatighterresourceupper
from Table II, each of which was run 100 times. Fig. 7 bound for packing jobs, therefore the occu-packing strategy
| illustrates |     | that the rise | in JCT | is positively | correlated with |     |      |      |            |     |         |      |        |               |
| ----------- | --- | ------------- | ------ | ------------- | --------------- | --- | ---- | ---- | ---------- | --- | ------- | ---- | ------ | ------------- |
|             |     |               |        |               |                 | can | make | more | aggressive |     | packing | with | little | interference. |
cumulativeGPUoccupancy,leadingtoaJCTriserangingfrom In all experimental runs, our approach achieves the lowest
| 10% | to  | 60% for each | DL model. |     |     |           |     |      |          |             |     |      |     |              |
| --- | --- | ------------ | --------- | --- | --- | --------- | --- | ---- | -------- | ----------- | --- | ---- | --- | ------------ |
|     |     |              |           |     |     | makespan, |     | with | a 19.71% | improvement |     | over | the | slot-packing |
Therefore, a safe co-location policy is necessary to achieve approach. It also shows that the overhead of DNN-occu is
better SM allocation and avoid overprovision while still en- tiny, and the inference time does not affect the model’s ready
suring QoS and fair sharing. GPU occupancy reflects the scheduling wait at all.

VII. RELATEDWORK demonstratethatDNN-occuaccuratelypredictstheGPUoccu-
pancy of deep learning models during inference. DNN-occu
GPU profiling. Regarding GPU utilization analysis, Gan-
is practical, robust, and generalized across various hyperpa-
diva [11] focuses on time-sharing and utilizes online profiling
rameter values and neural architectures. We apply DNN-occu
on isolated machines to determine proper co-location and
to hyperparameter optimization and employ it to guide co-
migration strategies. Antman [15] leverages GPU SM utiliza-
location packing, effectively reducing the makespan of deep
tion to identify jobs that might be suitable for co-location.
learning workloads and improving the overall GPU utilization
The work of Yeung et al. [6] predicts coarse-grained GPU
of systems.
utilization based on FLOPs, input data size, and the number
of convolutional layers. Moneo [8] intelligently collects SM
utilization in real time at a finer granularity without detecting IX. ACKNOWLEDGMENT
or tracking workloads. Prior work deals with coarse-grained
This work is funded by Youth Innovation Promotion Asso-
GPU utilization, while we concentrate on GPU occupancy,
ciation of Chinese Academy of Sciences (CAS).
which better reflects the actual usage of GPU resources.
Performance prediction for DL models. Performance
modelingandpredictionforDLmodelshaverecentlyattracted REFERENCES
researchers’ interest. Paleo [19] predicts the execution time of
[1] Microsoft, “Microsoft azure machine learning,” https://azure.microsoft.
DL models based on FLOPs. Habitat [55] uses wave scaling
com/en-us/services/machine-learning-service,2023.
(a technique for executing models on GPUs) and pre-trained
[2] Amazon, “Amazon sagemaker,” https://aws.amazon.com/sagemaker,
multilayer perceptrons to make predictions by scaling the ex- 2023.
ecution time of each operation during training iterations from [3] Microsoft,“Azurevmsizes-gpu-azurevirtualmachines,”https://learn.
microsoft.com/en-us/azure/virtual-machines/sizes-gpu,2023.
one GPU to another. However, these analytical techniques
[4] Google, “Cloud gpus — google cloud,” https://cloud.google.com/gpu,
requireextensivehandcraftedeffortsandarespecifictocertain 2023.
tasks. Some research work [13], [20], [56] proposes GNN- [5] Amazon, “Amazon ec2 p3 ideal for machine learning and hpc - aws,”
https://aws.amazon.com/ec2/instance-types/p3/,2023.
based timing predictors, which mainly focus on the perfor-
[6] G. Yeung, D. Borowiec, A. Friday, R. Harper, and P. Garraghan,
mance impacts from operator type and computation graph “Towards GPU utilization prediction for cloud deep learning,” in 12th
structure. Compared with prior works, DNN-occu captures USENIXWorkshoponHotTopicsinCloudComputing,HotCloud2020,
July 13-14, 2020, A. Phanishayee and R. Stutsman, Eds. USENIX
not only features at the operator level but also computation
Association,2020.
graph information and hidden factors within the framework. [7] G.Yeung,D.Borowiec,R.Yang,A.Friday,R.Harper,andP.Garraghan,
Our prediction-based learning method reduces handcrafted “Horus: Interference-aware and prediction-based scheduling in deep
learningsystems,”IEEETrans.ParallelDistributedSyst.,vol.33,no.1,
operations and achieves better prediction on unseen models.
pp.88–100,2022.
WeapplyDNN-occutodownstreamschedulingtasks,demon-
[8] Y. Jiang, Y. Xiong, L. Qu, C. Luo, C. Tian, P. Cheng, and Y. Xiong,
strating a practical application of performance prediction. “Moneo: Monitoring fine-grained metrics nonintrusively in AI infras-
Workload scheduling. There are some work considering tructure,” ACM SIGOPS Oper. Syst. Rev., vol. 56, no. 1, pp. 18–25,
2022.
DLworkloadschedulingonGPUclusters.Horus[7]proposes
[9] W.Chen,C.Lu,K.Ye,Y.Wang,andC.Xu,“RPTCN:resourcepredic-
aprediction-basedinterference-awaremechanismtodetermine tionforhigh-dynamicworkloadsincloudsbasedondeeplearning,”in
good decisions for DL job placement. Instead of predicting IEEEInternationalConferenceonClusterComputing,CLUSTER2021,
Portland,OR,USA,September7-10,2021. IEEE,2021,pp.59–69.
GPU utilization directly, Themis [34] predicts the slowdown
[10] S. Kim and Y. Kim, “Co-scheml: Interference-aware container co-
of each job, given k jobs sharing the GPU execution. The schedulingschemeusingmachinelearningapplicationprofilesforGPU
prediction model is a simple MLP, but the experiments are clusters,” in IEEE International Conference on Cluster Computing,
CLUSTER 2020, Kobe, Japan, September 14-17, 2020. IEEE, 2020,
all based on GPGPU-Sim [57], which also requires a minor
pp.104–108.
modification of the GPU structure to obtain feature counts. [11] W. Xiao, R. Bhardwaj, R. Ramjee, M. Sivathanu, N. Kwatra, Z. Han,
This means that the work cannot be implemented on a real P.Patel,X.Peng,H.Zhao,Q.Zhang,F.Yang,andL.Zhou,“Gandiva:
Introspective cluster scheduling for deep learning,” in 13th USENIX
GPU. Abacus [58] considers a more fine-grained scheduling
Symposium on Operating Systems Design and Implementation, OSDI
approach, treating DL jobs as a series of operators and 2018, Carlsbad, CA, USA, October 8-10, 2018, A. C. Arpaci-Dusseau
predicting the latency of a group of operators while running andG.Voelker,Eds. USENIXAssociation,2018,pp.595–610.
[12] J. Gu, M. Chowdhury, K. G. Shin, Y. Zhu, M. Jeon, J. Qian, H. H.
DLjobssimultaneously.Thepredictionmodelisalsoasimple
Liu,andC.Guo,“Tiresias:AGPUclustermanagerfordistributeddeep
MLP. This approach lacks extrapolation capability for unseen learning,” in 16th USENIX Symposium on Networked Systems Design
models and handles only a limited number of models. and Implementation, NSDI 2019, Boston, MA, February 26-28, 2019,
J. R. Lorch and M. Yu, Eds. USENIX Association, 2019, pp. 485–
500.
VIII. CONCLUSION
[13] Y.Gao,X.Gu,H.Zhang,H.Lin,andM.Yang,“Runtimeperformance
predictionfordeeplearningmodelswithgraphneuralnetwork,”in2023
In this paper, we propose DNN-occu, a tool for predicting
IEEE/ACM 45th International Conference on Software Engineering:
runtime GPU occupancy of deep learning models. We design SoftwareEngineeringinPractice(ICSE-SEIP),2023,pp.368–380.
a GNN-based prediction model that utilizes elaborate features [14] Y.Gao,Y.Zhu,H.Zhang,H.Lin,andM.Yang,“Resource-guidedcon-
figurationspacereductionfordeeplearningmodels,”in2021IEEE/ACM
derivedfromthecomputationgraphsemanticswithinprofiling
43rd International Conference on Software Engineering (ICSE), 2021,
statistics and runtime libraries. Our extensive experiments pp.175–187.

[15] W. Xiao, S. Ren, Y. Li, Y. Zhang, P. Hou, Z. Li, Y. Feng, W. Lin, [32] J. Lee, Y. Lee, J. Kim, A. Kosiorek, S. Choi, and Y. W. Teh, “Set
and Y. Jia, “Antman: Dynamic scaling on GPU clusters for deep transformer:Aframeworkforattention-basedpermutation-invariantneu-
learning,” in 14th USENIX Symposium on Operating Systems Design ral networks,” in Proceedings of the 36th International Conference on
and Implementation, OSDI 2020, Virtual Event, November 4-6, 2020. MachineLearning,2019,pp.3744–3753.
USENIXAssociation,2020,pp.533–548. [33] Q.Sun,Y. Liu,H.Yang,R.Zhang, M.Dun,M.Li,X. Liu,W.Xiao,
[16] Y.Wang,G.Wei,andD.Brooks,“Asystematicmethodologyforanal- Y. Li, Z. Luan et al., “Cognn: efficient scheduling for concurrent
ysisofdeeplearninghardwareandsoftwareplatforms,”inProceedings gnn training on gpus,” in SC22: International Conference for High
ofMachineLearningandSystems2020,MLSys2020,Austin,TX,USA, Performance Computing, Networking, Storage and Analysis, 2022, pp.
| March2-4,2020,I.S.Dhillon,D.S.Papailiopoulos,andV.Sze,Eds. |     |     |     |     |     |     |     |     | 1–15. |     |     |     |     |     |     |
| ---------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- |
mlsys.org,2020. [34] W.Zhao,Q.Chen,H.Lin,J.Zhang,J.Leng,C.Li,W.Zheng,L.Li,and
[17] Q. Yao, M. Wang, H. J. Escalante, I. Guyon, Y. Hu, Y. Li, W. Tu, M.Guo,“Themis:Predictingandreininginapplication-levelslowdown
| Q. Yang, | and | Y. Yu, | “Taking | human | out of learning |     | applications: | A   |     |     |     |     |     |     |     |
| -------- | --- | ------ | ------- | ----- | --------------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
onspatialmultitaskinggpus,”in2019IEEEInternationalParalleland
survey on automated machine learning,” CoRR, vol. abs/1810.13306, DistributedProcessingSymposium,IPDPS2019,RiodeJaneiro,Brazil,
| 2018. |     |     |     |     |     |     |     |     | May20-24,2019. |     | IEEE,2019,pp.653–663. |     |     |     |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | --------------------- | --- | --- | --- | --- |
[18] NVIDIA, “nvmlutilization,” https://docs.nvidia.com/deploy/nvml-api/ [35] O.R.developers,“Onnx,”https://github.com/onnx/onnx,2022.
structnvmlUtilization t.html#structnvmlUtilization t,2022. [36] I.Goodfellow,Y.Bengio,andA.Courville,Deeplearning. MITpress,
| [19] H. Qi, | E. R. | Sparks, | and A. | Talwalkar, | “Paleo: | A performance |     | model |     |     |     |     |     |     |     |
| ----------- | ----- | ------- | ------ | ---------- | ------- | ------------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
2016.
fordeepneuralnetworks,”in5thInternationalConferenceonLearning
[37] D.Q.Nguyen,T.D.Nguyen,andD.Phung,“UniversalSelf-Attention
Representations, ICLR 2017, Toulon, France, April 24-26, 2017, Con- arXiv preprint arXiv:1909.11855,
|                          |     |     |     |                      |     |     |     |     | Network for | Graph | Classification,” |     |     |     |     |
| ------------------------ | --- | --- | --- | -------------------- | --- | --- | --- | --- | ----------- | ----- | ---------------- | --- | --- | --- | --- |
| ferenceTrackProceedings. |     |     |     | OpenReview.net,2017. |     |     |     |     | 2019.       |       |                  |     |     |     |     |
[20] L. Dudziak, T. Chau, M. S. Abdelfattah, R. Lee, H. Kim, and N. D. [38] J. Zhang, H. Zhang, C. Xia, and L. Sun, “Graph-bert: Only at-
| Lane,     | “BRP-NAS:   |     | prediction-based |         | NAS using | gcns,” | in Advances |     |            |        |              |       |                   |     |                |
| --------- | ----------- | --- | ---------------- | ------- | --------- | ------ | ----------- | --- | ---------- | ------ | ------------ | ----- | ----------------- | --- | -------------- |
|           |             |     |                  |         |           |        |             |     | tention is | needed | for learning | graph | representations,” |     | arXiv preprint |
| in Neural | Information |     | Processing       | Systems | 33:       | Annual | Conference  | on  |            |        |              |       |                   |     |                |
arXiv:2001.05140,2020.
NeuralInformationProcessingSystems2020,NeurIPS2020,December
[39] Z.Liu,H.Mao,C.-Y.Wu,C.Feichtenhofer,T.Darrell,andS.Xie,“A
6-12,2020,virtual,H.Larochelle,M.Ranzato,R.Hadsell,M.Balcan,
|     |     |     |     |     |     |     |     |     | convnet for | the 2020s,” | Proceedings |     | of the IEEE/CVF |     | Conference on |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ----------- | ----------- | --- | --------------- | --- | ------------- |
andH.Lin,Eds.,2020. ComputerVisionandPatternRecognition(CVPR),2022.
| [21] J. Devlin, | M.  | Chang, | K. Lee, | and K. | Toutanova, | “BERT: | pre-training |     |     |     |     |     |     |     |     |
| --------------- | --- | ------ | ------- | ------ | ---------- | ------ | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
[40] K.SimonyanandA.Zisserman,“Verydeepconvolutionalnetworksfor
| of deep | bidirectional |     | transformers | for | language | understanding,” |     | in  |     |     |     |     |     |     |     |
| ------- | ------------- | --- | ------------ | --- | -------- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
large-scaleimagerecognition,”arXivpreprintarXiv:1409.1556,2014.
| Proceedings |     | of the | 2019 Conference |     | of the North | American |     | Chapter |     |     |     |     |     |     |     |
| ----------- | --- | ------ | --------------- | --- | ------------ | -------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
[41] A.Krizhevsky,I.Sutskever,andG.E.Hinton,“Imagenetclassification
| of the        | Association | for       | Computational |                    | Linguistics: | Human    | Language |      |           |               |        |            |             |     |               |
| ------------- | ----------- | --------- | ------------- | ------------------ | ------------ | -------- | -------- | ---- | --------- | ------------- | ------ | ---------- | ----------- | --- | ------------- |
|               |             |           |               |                    |              |          |          |      | with deep | convolutional | neural | networks,” | in Advances |     | in Neural In- |
| Technologies, |             | NAACL-HLT |               | 2019, Minneapolis, |              | MN, USA, | June     | 2-7, |           |               |        |            |             |     |               |
2019, Volume 1 (Long and Short Papers), J. Burstein, C. Doran, and formation Processing Systems 25: 26th Annual Conference on Neural
|                |     |                                                 |     |     |     |     |     |     | Information | Processing | Systems | 2012. | Proceedings | of  | a meeting held |
| -------------- | --- | ----------------------------------------------- | --- | --- | --- | --- | --- | --- | ----------- | ---------- | ------- | ----- | ----------- | --- | -------------- |
| T.Solorio,Eds. |     | AssociationforComputationalLinguistics,2019,pp. |     |     |     |     |     |     |             |            |         |       |             |     |                |
December3-6,2012,LakeTahoe,Nevada,UnitedStates,P.L.Bartlett,
4171–4186.
F.C.N.Pereira,C.J.C.Burges,L.Bottou,andK.Q.Weinberger,Eds.,
| [22] A. Radford, |     | J. Wu, | R. Child, | D. Luan, | D. Amodei, | and | I. Sutskever, |     |     |     |     |     |     |     |     |
| ---------------- | --- | ------ | --------- | -------- | ---------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
2012,pp.1106–1114.
“Languagemodelsareunsupervisedmultitasklearners,”2019.
[23] NVIDIA, “Achieved occupancy,” https://docs.nvidia.com/gameworks/ [42] Y.LeCun,L.Bottou,Y.Bengio,andP.Haffner,“Gradient-basedlearning
appliedtodocumentrecognition,”Proc.IEEE,vol.86,no.11,pp.2278–
content/developertools/desktop/analysis/report/cudaexperiments/
2324,1998.
kernellevel/achievedoccupancy.htm,2015.
[43] X.Shi,Z.Chen,H.Wang,D.Yeung,W.Wong,andW.Woo,“Convo-
| [24] A. Paszke, |     | S. Gross, | F. Massa, | A.  | Lerer, J. | Bradbury, | G. Chanan, |     |     |     |     |     |     |     |     |
| --------------- | --- | --------- | --------- | --- | --------- | --------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
lutionalLSTMnetwork:Amachinelearningapproachforprecipitation
T.Killeen,Z.Lin,N.Gimelshein,L.Antiga,A.Desmaison,A.Ko¨pf,
E.Z.Yang,Z.DeVito,M.Raison,A.Tejani,S.Chilamkurthy,B.Steiner, nowcasting,”inAdvancesinNeuralInformationProcessingSystems28:
L. Fang, J. Bai, and S. Chintala, “Pytorch: An imperative style, high- Annual Conference on Neural Information Processing Systems 2015,
|     |     |     |     |     |     |     |     |     | December | 7-12, 2015, | Montreal, | Quebec, | Canada, | C.  | Cortes, N. D. |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | ----------- | --------- | ------- | ------- | --- | ------------- |
performancedeeplearninglibrary,”inAdvancesinNeuralInformation
|     |     |     |     |     |     |     |     |     | Lawrence, | D. D. Lee, | M. Sugiyama, |     | and R. Garnett, |     | Eds., 2015, pp. |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | ---------- | ------------ | --- | --------------- | --- | --------------- |
ProcessingSystems32:AnnualConferenceonNeuralInformationPro-
802–810.
cessingSystems2019,NeurIPS2019,December8-14,2019,Vancouver,
BC,Canada,H.M.Wallach,H.Larochelle,A.Beygelzimer,F.d’Alche´- [44] A. Dosovitskiy, L. Beyer, A. Kolesnikov, D. Weissenborn, X. Zhai,
Buc,E.B.Fox,andR.Garnett,Eds.,2019,pp.8024–8035. T. Unterthiner, M. Dehghani, M. Minderer, G. Heigold, S. Gelly,
[25] M.Abadi,P.Barham,J.Chen,Z.Chen,A.Davis,J.Dean,M.Devin, J.Uszkoreit,andN.Houlsby,“Animageisworth16x16words:Trans-
formersforimagerecognitionatscale,”in9thInternationalConference
S.Ghemawat,G.Irving,M.Isard,M.Kudlur,J.Levenberg,R.Monga,
|           |     |            |     |             |       |         |               |     | on Learning | Representations, |     | ICLR 2021, | Virtual | Event, | Austria, May |
| --------- | --- | ---------- | --- | ----------- | ----- | ------- | ------------- | --- | ----------- | ---------------- | --- | ---------- | ------- | ------ | ------------ |
| S. Moore, | D.  | G. Murray, |     | B. Steiner, | P. A. | Tucker, | V. Vasudevan, |     |             |                  |     |            |         |        |              |
P.Warden,M.Wicke,Y.Yu,andX.Zheng,“Tensorflow:Asystemfor 3-7,2021. OpenReview.net,2021.
large-scalemachinelearning,”in12thUSENIXSymposiumonOperating [45] Z. Liu, Y. Lin, Y. Cao, H. Hu, Y. Wei, Z. Zhang, S. Lin, and
SystemsDesignandImplementation,OSDI2016,Savannah,GA,USA, B.Guo,“Swintransformer:Hierarchicalvisiontransformerusingshifted
|          |      |       |           |     |            |      |        |     | windows,”    | in 2021 | IEEE/CVF  | International | Conference |         | on Computer  |
| -------- | ---- | ----- | --------- | --- | ---------- | ---- | ------ | --- | ------------ | ------- | --------- | ------------- | ---------- | ------- | ------------ |
| November | 2-4, | 2016, | K. Keeton | and | T. Roscoe, | Eds. | USENIX |     |              |         |           |               |            |         |              |
|          |      |       |           |     |            |      |        |     | Vision, ICCV | 2021,   | Montreal, | QC,           | Canada,    | October | 10-17, 2021. |
Association,2016,pp.265–283.
[26] NVIDIA,“Nvidiacuda®deepneuralnetworklibrary,”https://developer. IEEE,2021,pp.9992–10002.
nvidia.com/rdp/cudnn-archive,2023. [46] Z. Tu, H. Talebi, H. Zhang, F. Yang, P. Milanfar, A. C. Bovik, and
[27] NVIDIA, “Nvdia nsight compute,” https://docs.nvidia.com/ Y. Li, “Maxvit: Multi-axis vision transformer,” in Computer Vision -
ECCV2022:17thEuropeanConference,TelAviv,Israel,October23-27,
nsight-compute/NsightCompute/index.html,2023.
2022,Proceedings,PartXXIV,ser.LectureNotesinComputerScience,
[28] K.He,X.Zhang,S.Ren,andJ.Sun,“Deepresiduallearningforimage
recognition,”in2016IEEEConferenceonComputerVisionandPattern S. Avidan, G. J. Brostow, M. Cisse´, G. M. Farinella, and T. Hassner,
Recognition,CVPR2016,LasVegas,NV,USA,June27-30,2016. IEEE Eds.,vol.13684. Springer,2022,pp.459–479.
ComputerSociety,2016,pp.770–778. [47] V. Sanh, L. Debut, J. Chaumond, and T. Wolf, “Distilbert, a distilled
[29] A.Krizhevsky,“Learningmultiplelayersoffeaturesfromtinyimages,” version of BERT: smaller, faster, cheaper and lighter,” CoRR, vol.
abs/1910.01108,2019.
UniversityofToronto,Tech.Rep.,2009.
[30] T.N.KipfandM.Welling,“Semi-supervisedclassificationwithgraph [48] A. Radford, J. W. Kim, C. Hallacy, A. Ramesh, G. Goh, S. Agarwal,
convolutional networks,” in 5th International Conference on Learning G.Sastry,A.Askell,P.Mishkin,J.Clarketal.,“Learningtransferable
Representations, ICLR 2017, Toulon, France, April 24-26, 2017, Con- visual models from natural language supervision,” in International
ferenceTrackProceedings. OpenReview.net,2017. conferenceonmachinelearning. PMLR,2021,pp.8748–8763.
[31] C. Ying, T. Cai, S. Luo, S. Zheng, G. Ke, D. He, Y. Shen, and T.-Y. [49] D.Justus,J.Brennan,S.Bonner,andA.S.McGough,“Predictingthe
Liu, “Do transformers really perform badly for graph representation?” computational cost of deep learning models,” in IEEE International
in Thirty-Fifth Conference on Neural Information Processing Systems, Conference on Big Data (IEEE BigData 2018), Seattle, WA, USA,
2021. December 10-13, 2018, N. Abe, H. Liu, C. Pu, X. Hu, N. K. Ahmed,

M. Qiao, Y. Song, D. Kossmann, B. Liu, K. Lee, J. Tang, J. He, and
J.S.Saltz,Eds. IEEE,2018,pp.3873–3882.
[50] S.HochreiterandJ.Schmidhuber,“LongShort-TermMemory,”Neural
Computation, vol. 9, no. 8, pp. 1735–1780, 11 1997. [Online].
Available:https://doi.org/10.1162/neco.1997.9.8.1735
[51] A.Vaswani,N.Shazeer,N.Parmar,J.Uszkoreit,L.Jones,A.N.Gomez,
L. Kaiser, and I. Polosukhin, “Attention is all you need,” in Advances
in Neural Information Processing Systems 30: Annual Conference on
NeuralInformationProcessingSystems2017,December4-9,2017,Long
Beach,CA,USA,I.Guyon,U.vonLuxburg,S.Bengio,H.M.Wallach,
R.Fergus,S.V.N.Vishwanathan,andR.Garnett,Eds.,2017,pp.5998–
6008.
[52] M. Wang, L. Yu, D. Zheng, Q. Gan, Y. Gai, Z. Ye, M. Li, J. Zhou,
Q.Huang,C.Ma,Z.Huang,Q.Guo,H.Zhang,H.Lin,J.Zhao,J.Li,
A.J.Smola,andZ.Zhang,“Deepgraphlibrary:Towardsefficientand
scalabledeeplearningongraphs,”CoRR,vol.abs/1909.01315,2019.
[53] D. P. Kingma and J. Ba, “Adam: A method for stochastic optimiza-
tion,” in 3rd International Conference on Learning Representations,
ICLR 2015, San Diego, CA, USA, May 7-9, 2015, Conference Track
Proceedings,Y.BengioandY.LeCun,Eds.,2015.
[54] M. Jeon, S. Venkataraman, A. Phanishayee, J. Qian, W. Xiao, and
F. Yang, “Analysis of large-scale multi-tenant GPU clusters for DNN
training workloads,” in 2019 USENIX Annual Technical Conference,
USENIX ATC 2019, Renton, WA, USA, July 10-12, 2019, D. Malkhi
andD.Tsafrir,Eds. USENIXAssociation,2019,pp.947–960.
[55] G.X.Yu,Y.Gao,P.Golikov,andG.Pekhimenko,“Habitat:Aruntime-
based computational performance predictor for deep neural network
training,”in2021USENIXAnnualTechnicalConference,USENIXATC
2021, July 14-16, 2021, I. Calciu and G. Kuenning, Eds. USENIX
Association,2021,pp.503–521.
[56] K. P. Selvam and M. Brorsson, “DIPPM: a deep learning inference
performancepredictivemodelusinggraphneuralnetworks,”CoRR,vol.
abs/2303.11733,2023.
[57] A.Bakhoda,G.L.Yuan,W.W.L.Fung,H.Wong,andT.M.Aamodt,
“Analyzing CUDA workloads using a detailed GPU simulator,” in
IEEEInternationalSymposiumonPerformanceAnalysisofSystemsand
Software,ISPASS2009,April26-28,2009,Boston,Massachusetts,USA,
Proceedings. IEEEComputerSociety,2009,pp.163–174.
[58] W.Cui,H.Zhao,Q.Chen,N.Zheng,J.Leng,J.Zhao,Z.Song,T.Ma,
Y.Yang,C.Li,andM.Guo,“Enablesimultaneousdnnservicesbasedon
deterministicoperatoroverlapandpreciselatencyprediction,”inSC21:
InternationalConferenceforHighPerformanceComputing,Networking,
StorageandAnalysis,2021,pp.1–15.