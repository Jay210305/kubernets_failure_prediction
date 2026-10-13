Applied Intelligence (2025) 55:784
https://doi.org/10.1007/s10489-025-06681-1
Multi-modal anomaly detection for microservice system through
nested graph diffusion reconstruction
Mengwei Fan1 · Xiuguo Zhang1 · Peipeng Wang1 · Zhiying Cao1
Accepted: 29 May 2025 / Published online: 19 June 2025
© The Author(s), under exclusive licence to Springer Science+Business Media, LLC, part of Springer Nature 2025
Abstract
Accurately detecting anomalies in microservice systems has become increasingly important for rapidly growing microser-
vice architectures. On the one hand, existing anomaly detection methods typically focus on a single type of data source
(i.e., logs or traces) or overlook the correlations between different types of data, which can lead to missed anomalies and
a high number of false positives. On the other hand, regarding the issue of imbalanced positive and negative samples in
anomaly detection, existing research has not proposed effective solutions. To address these issues, in this paper, we pro-
pose MSNGAD, a microservice anomaly detection method based on nested graph diffusion reconstruction. MSNGAD uses
nested graphs to uniformly describe the complex structure of traces and embedded log messages. It treats the log template
temporal relationships as the inner graph of the nested graph, and the service invocations relationships as the outer graph.
By capturing the correlations between different modalities of data, the system can detect anomalies comprehensively. Fur-
thermore, to address the problem of imbalanced positive and negative samples in anomaly detection, MSNGAD trains a
diffusion reconstruction model to augment the features of anomalous samples. This approach abandons traditional manual
data augmentation strategies, effectively mitigating the unnatural disturbances to the graph structure caused by human
intervention in data augmentation. Extensive evaluations were conducted on large-scale datasets, and the experimental
results show that MSNGAD outperforms existing baseline models, achieving an F1-score of 0.96.
Keywords Microservice · Anomaly detection · Nested graph · Feature augmentation · Deep learning
1 Introduction introduces new challenges, particularly in anomaly detec-
tion. Due to the intricate dependencies between microser-
With the widespread adoption of microservice architectures, vices, an anomaly in one service can trigger a cascade of
the functionality of a single application is decomposed into anomalies, leading to additional performance and reusability
multiple small services that operate independently, each issues. Therefore, to enable operations engineers to detect
operating in its own process and interacting through light- potential anomalies in microservice systems promptly and
weight communication mechanisms. While this architec- take effective measures, automated anomaly detection is
ture enhances the system’s flexibility and scalability, it also crucial.
In microservice systems, there are various types of
monitoring data, such as logs and traces. Logs have been
widely used in anomaly detection tasks and play a crucial
Xiuguo Zhang
role in software reliability engineering. With the widespread
zhangxg@dlmu.edu.cn
adoption of standards such as OpenTracing [1] and infra-
Mengwei Fan
structures such as SkyWalking [2], distributed traces have
fanmengwei@dlmu.edu.cn
also been applied in anomaly detection tasks. As shown in
Peipeng Wang
Fig. 1, logs are semi-structured textual data, predefined by
wpp7@dlmu.edu.cn
developers, used to record the various behaviors of different
Zhiying Cao
services in the system for debugging and root cause analy-
czysophy@dlmu.edu.cn
sis. Traces describe the execution process (i.e., invocation
1 Information Science and Technology College, Dalian chain) of a request through different service instances in a
Maritime University, Dalian, Liaoning, China
1 3

784 Page 2 of 15 M. Fan et al.
F ig. 1 A multi-modal data case
microservice, with each operation (i.e., service invocation) data, aiming to balance the ratio between positive and neg-
referred to as a span, and each span records various informa- ative samples. Even so, this issue of class imbalance has
tion related to the invocation. not been completely resolved. For example, in the publicly
Based on these monitoring data, most research uses deep available GAIA dataset in the field of Artificial Intelligence
learning methods to detect anomalies in microservice sys- for IT Operations (AIOps), the positive-to-negative sample
tems. For logs, existing log anomaly detection methods ratio after manually injecting anomalies is approximately
mainly rely on extracting semantic features from log texts 9: 1, meaning that only 1 out of 10 samples is abnormal,
[3–5] for anomaly detection. Many detection models have which still presents a class imbalance issue. To address this,
been developed by optimizing log parsing and feature pro- Ying et al. [10] proposed a clustering-based self-training
cessing methods. For traces, current mainstream anomaly method aimed at improving KNN’s performance on imbal-
detection methods [6–8] focus on detecting anomalies anced log data. However, this method is overly dependent
through the response time or invocation paths of microser- on data distribution and is sensitive to noise. TraceCRL [11]
vices. However, due to the complexity and diversity of increases the number of anomalous traces using six manu-
anomaly patterns in microservice systems, using a single ally designed anomaly simulation strategies (i.e., network
source of monitoring data often fails to capture all abnormal delay injection and response code tampering). However,
behaviors within the microservices. For example, when a this method relies heavily on expert knowledge and is prone
microservice is subjected to a malicious attack, the attacker to introducing noise, leading to unnatural disturbances in
may deliberately avoid detection, causing the correspond- the graph structure. Moreover, current data augmentation
ing node’s logs to show no errors. However, analyzing the methods are mainly designed for single-modality data, and
trace data can help identify such anomalies. Conversely, it is crucial to develop a more robust and generalizable aug-
when there is an internal logic error in the service, the ser- mentation method for multi-modal anomaly detection tasks.
vice may respond normally but return incorrect data. This To address the above problems, in this paper, we pro-
type of anomaly cannot be detected from the traces but can pose MSNGAD, a microservice anomaly detection method
be identified by inspecting the log information of the cor- based on nested graph diffusion reconstruction. First, it uses
responding node. In summary, only by incorporating the Drain3 [12] to parse semi-structured log messages into log
analysis of logs and traces, and deeply analyzing the com- templates. For a given trace data, it obtains the log mes-
plex invocation relationships in microservices, can we com- sage templates that belong to the span in the trace based
prehensively capture the abnormal behavior of the system. on service instance names and timestamps, aligning the two
Furthermore, in normal microservice systems, excep- modalities of data. For log templates within a span, in order
tions are usually rare. According to statistics, in a microser- to effectively represent the execution order (i.e., temporal
vice system with millions of invocation requests per day, the relationships) and dependency relationships (i.e., spatial
occurrence rate of abnormal events due to network failures, relationships) during its generation, it models the log tem-
server crashes, resource bottlenecks, etc., is typically less plates as a graph structure as the inner graph of the nested
than 0.1%. This leads to the issue of imbalanced positive graph, uses the Graph Attention Network (GAT) [13] to
and negative samples in anomaly detection. Existing studies learn the contextual relationships between the log templates
[8, 9] generally use fault injection tools to manually inject in the inner graph. To better describe the complex hierarchi-
anomalies into microservices to generate more abnormal cal structure and dependency relationships between services
1 3

Multi-modal anomaly detection for microservice system through nested graph diffusion reconstruction Page 3 of 15 784
in the microservice system, it also models the trace based logs to detect anomalous logs that deviate from the normal
on the invocation relationship between service operations as pattern, but this method ignores the semantic information of
the outer graph of the nested graph, uses the Graph Convo- the logs. In order to solve the problem, LogAnomaly [22]
lutional Network (GCN) [14] to learn the dependency rela- adds the semantic information of logs to the anomaly detec-
tionships between service operations in the outer graph. In tion and uses the LSTM model to predict the next possible
addition, to alleviate the imbalance problem between posi- log result based on the historical log sequence, but if there
tive and negative samples, it uses a feature augmentation is a loss or duplication of log data in the actual log sys-
method based on diffusion reconstruction, which uses the tem, it is likely to disrupt the sequential pattern of the logs,
encoder module of the Variational Autoencoder (VAE) to which makes the detection accuracy lower. Considering this
sample the latent features of the original anomalous data, problem, LogRobust [23] applies a Bi-LSTM model and
and utilizes the trained diffusion model to augment the fea- an attention network to detect anomalies in log sequences,
tures, then uses the decoder module to reconstruct the aug- improving the robustness of anomaly detection. To capture
mented data to obtain the pseudo-anomaly samples. Finally, dependencies between long distance logs. ContexLog [24]
it relies contrastive learning to improve the quality and retains all log information and processes it using a classifi-
diversity of the generated pseudo-anomaly samples. cation model based on a Transformer encoder. Although the
In summary, this paper makes the following contributions. above methods analyze log sequences from both sequen-
tial and semantic perspectives, collaborative interactions
● We design microservice nested graphs to integrate and between microservices mean that adjacent log messages not
represent both traces and logs to dig deeper into the spa- only have temporal continuity but may also originate from
tiotemporal dependencies between log templates nested different service nodes. Therefore, ignoring spatial depen-
within spans. dencies between logs may lead to insufficient analysis of
● We propose a feature augmentation model based on dif- log correlations, which in turn reduces the effectiveness of
fusion reconstruction, which not only addresses the im- anomaly detection. To address this, LogGT [25] converts
balance issue in anomaly detection, but also alleviates log sequences into a graph structure, considering the com-
the unnatural disturbance to graph structure information plex spatiotemporal dependencies of logs, and combines
caused by traditional data augmentation methods. transfer learning methods for cross-system log analysis. But
● Extensive experiments on two real-world datasets show logs describe the behavior of service instances, they often
that the proposed MSNGAD model achieves com- fail to directly represent the invocation topology between
petitive performance against all compared approaches, services, leading to insufficient cross-service anomaly cor-
achieving 0.96 F1-score. Additionally, ablation studies relation analysis.
further validate the effectiveness of each design in our
model. Trace-based anomaly detection In traditional trace anomaly
detection methods, traces are typically treated as sequences.
For example, Multimodal Trace [6] processes textual labels
2 Related work and response times in a trace into a sequential form and uses
a multimodal LSTM to detect anomalies. TraceAnomaly [7]
Currently, technologies such as deep learning and rein- represents each trace using a service trace vector, consid-
forcement learning have been widely applied across vari- ering both response time and invocation path features, and
ous fields, with their application scenarios continually applies a Deep Bayesian Network to learn normal patterns
expanding, driving the intelligent transformation of indus- and distinguish anomalous data. However, due to the highly
tries [15–20]. This paper studies the methods of AIOps for dependent and complex nature of microservice systems, the
microservice systems using graph neural networks, compar- complex spatial relationships between services are lost by
ing the limitations of single-modal data in anomaly detec- considering traces as sequence information only, so existing
tion and combining multi-modal data from traces and logs research workers represent traces as graph structures and
for comprehensive system anomaly detection. use graph neural networks to detect anomalies. TraceVAE
[26] proposes a dual-variable graph VAE that uses struc-
2.1 Single-modal data anomaly detection tural VAE and temporal VAE to separately reconstruct the
structural and temporal features of traces. PUTraceAD [27]
Log-based anomaly detection Log-based anomaly detec- constructs a span causal graph with node features such as
tion has been widely used in security applications, DeepLog operation names, response codes, and durations, and learns
[21] takes log template index sequence as input and uses the network parameters using positive and unlabeled data.
the LSTM model to learn the sequential pattern of normal GRAND [28] detects anomalous behaviors in traces by
1 3

| 784  Page 4 of 15 |     |     |     |     |     |     | M. Fan et al. |
| ----------------- | --- | --- | --- | --- | --- | --- | ------------- |
combining VAE and GAN. Although traces capture the  Nested Graph Construction, Nested Graph Feature Extrac-
global topology of service interactions, they lack the fine- tion, Feature Augmentation, and Anomaly Detection.
| grained  semantic  | and  temporal  | information  | of  internal  |     |     |     |     |
| ------------------ | -------------- | ------------ | ------------- | --- | --- | --- | --- |
service logs, limiting the completeness of anomaly repre- 3.1  Data preprocessing
sentation and affecting detection performance.
Log The first step is to process the raw log messages. Logs,
2.2  Multi-modal data anomaly detection
as semi-structured text data, record the event records gener-
ated at different time points during system operation. Each
Compared to single-modal studies, multi-modal anomaly  log record usually contains information such as timestamp,
detection studies are relatively rare, but considering that  log level, message content and so on. To eliminate redun-
single-modal data is difficult to comprehensively capture  dant information in logs, we use the Drain3 log parsing
the anomalous behaviors of microservices, an appropriate  algorithm to extract structured log templates from raw log
combination of multi-modal data can effectively capture  messages in a streaming manner, where each template rep-
system anomalies. LogTraceAD [29] combines logs and  resents a specific log event l and is assigned a unique ID.
traces to construct graphs and uses the Sentence Variational
Autoencoder (S-VAE) to learn graph features. DeepTraLog  Trace Trace as the textual data of invocation relationship
[9] combines logs and each trace to construct a trace event  between microservices consists of multiple span events
graph, learns graph features using Gated Graph Neural Net- and  the  causal  relationship  between  them,  each  span
works (GGNN), learns regular feature representations of  event represents an operation of the service, and usually
the training data as well as minimized hyperspheres with  contains information such as trace ID, span ID, service
deep SVDD (Support Vector Data Description), treats fea- instance name, start time, end time, and so on. In this paper,
ture representations inside the hyperspheres as normal, and  we  define  Tr = tr ,tr ,...,tr .  For  a  certain  trace
|     |     |     |     |     | 1   | 2 n |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     | {   | }   |     |
feature  representations  falling  outside  the  hyperspheres  tr i = s 1 ,s 2 ,...,s p , where s i  is a span event belonging
|                 |                 |                |            | {              | }   |     |     |
| --------------- | --------------- | -------------- | ---------- | -------------- | --- | --- | --- |
| as  anomalies.  | However,  when  | the  abnormal  | behaviors  | to this trace. |     |     |     |
of microservice systems are diverse, it is difficult to find
suitable boundaries to identify abnormal samples in high- Data alignment To align the logs and traces, we extract
dimensional potential spaces. the log events belonging to the span during the execu-
|     |     |     |     | tion  of  | the  microservice  | based  on  | the  service  instance  |
| --- | --- | --- | --- | --------- | ------------------ | ---------- | ----------------------- |
name, start time and end time involved in each span event
| 3  Method |     |     |     | Lsi = | l ,l , ,l , and embed them within the corre- |     |     |
| --------- | --- | --- | --- | ----- | -------------------------------------------- | --- | --- |
|           |     |     |     |       | 1 2 q                                        |     |     |
|           |     |     |     | {     | ··· }                                        |     |     |
sponding span.
The objective of MSNGAD is to automatically and accu-
3.2  Nested graph construction
rately detect microservice system anomalies using the com-
bined data of logs and traces generated by microservices
during operation. The overview of MSNGAD is presented  Since there are obvious differences in the way logs and
in Fig. 2, which includes five steps. Data Preprocessing,  traces represent anomalies, with logs as text and traces as

Fig. 2 MSNGAD overview
1 3

Multi-modal anomaly detection for microservice system through nested graph diffusion reconstruction Page 5 of 15 784
chain structures, this discrepancy poses a huge challenge to across different time points, reflecting the system’s behavior
effectively combine the information for downstream anom- patterns at various time stages. Therefore, in order to effec-
aly detection, so how to effectively represent the correlation tively analyze the spatiotemporal dependencies between
between the two becomes the focus of this study. Inspired log templates, MSNGAD models the log events inside each
by the nested graph structure, a trace can be regarded as span as a graph structure, forming the inner graph layer of
graph structure information(outer graph), and the log events the nested graph gsi = vsi,esi , where s
i
denotes a cer-
{ }
contained inside each span can also form a subgraph (inner tain span in the trace. In this graph, each node vsi represents
graph), so we describe the complex dependencies between different log events that belong to the span s
i
, each edge esi
microservice invocations and the log events embedded in indicates the invocation order between different log events
them by constructing nested graphs, and build nested graph within the span s , the direction of the edge points from the
i
inner graphs by log template timing relationships and nested calling log to the called log, and the frequency of node pairs
graph outer graphs by service invocation relationships, appearing in the span is used as the weight on the edges.
effectively capturing the correlations between different Specifically, as shown in Fig. 3, each node represents a dif-
modal data. The specific approach is as follows. ferent log event, for a certain log event lsi Lsi, in order to
m ∈
better extract its semantic features, inspired by a large pre-
Inner graph The log template sequences within the trace trained language model, this paper uses a pre-trained BERT
span exhibit temporal dependencies due to the order of [30] language model to extract the features, log templates
occurrence, and the same log may appear multiple times are processed by preprocessing [31], embedding layer and
at different times. This suggests that certain operations or the transformer encoder, to generate template semantic fea-
events in the system repeat in similar patterns at different tures zsi, which are used as corresponding node features.
m
points in time, indicating spatial dependencies as well, these using the execution order between different events in the
dependencies reveal the distribution patterns of the same logs log sequence as edges, and counting the number of times
Fig. 3 Inner graph construction of the nested graph
1 3

| 784  Page 6 of 15  |                                     |     |     |     | M. Fan et al. |
| ------------------ | ----------------------------------- | --- | --- | --- | ------------- |
| the node pairs vsi | vsi appear in that span, which are  |     |     |     |               |
time of each span. Assuming Span A is the root span, the
m −→ n
used as weights w  on the edges in the graph. Through  duration time dA =t t , waiting time wA =t t , and
|     | mn  |                         | t 8 1 |     | t 7 2 |
| --- | --- | ----------------------- | ----- | --- | ----- |
|     |     | local execution time lA | −     |     | −     |
this approach, the raw log messages are transformed into a  =(t 2 t 1 )+(t 8 t 7 ), since Span
|     |     |     | t   | − − |     |
| --- | --- | --- | --- | --- | --- |
directed, weighted graph containing multiple types of infor- A is the root span, its relative start time rA =0. For Span C
t
mation, in which multiple implicit relationships of the sys- and Span D, since they have no child spans, the waiting time
tem operation can be expressed more intuitively. wC =0, wD =0, the duration time equals the local execu-
|     |     | t   | t   |     |     |
| --- | --- | --- | --- | --- | --- |
tion time, the relative start time of Span C is rC
=t 3 t 1 ,
t −
Outer graph To better describe the complex hierarchical  and the relative start time of Span D is rD =t t . Based
|     |     |                                 |     | t                      | 5 1 |
| --- | --- | ------------------------------- | --- | ---------------------- | --- |
|     |     | on this, the time features Ttri |     | =[dx,wx,lx,rx], where  | −   |
structure and dependencies between service invocations
|     |     |     |     | x t | t t t |
| --- | --- | --- | --- | --- | ----- |
in a microservice system, MSNGAD models span events  x A,B,C,D , each span in the trace tr  can be calcu-
i
|     |     | ∈{  | }   |     |     |
| --- | --- | --- | --- | --- | --- |
as graph structures based on the contextual information  lated and used as the initial feature vector of the nodes in
| recorded in the span and uses them as the outer graph layer  |           | the outer graph. |     |     |     |
| ------------------------------------------------------------ | --------- | ---------------- | --- | --- | --- |
| of the nested graph Gtri                                     | Vtri,Etri |                  |     |     |     |
= . where tr i  denotes
{ }
a certain trace. In the graph, each node Vtri represents dif- 3.3  Nested graph representation
ferent service operations within the trace tr i , and each edge
Etri represents the invocation relationship between the ser- Inner graph features Considering that different neighbor-
vice operations in the trace tr i , with the direction pointing  ing nodes in the inner graph have varying levels of impor-
from a caller to a callee. For each node in the graph, we  tance, as shown in Fig. 5, we use GAT to dynamically assign
first calculate its initial feature using the time-related infor- weights to the relative importance of each neighbor node.
mation recorded in the span, such as the start time and end  The GAT adaptively learns the importance of each neigh-
time. Specifically, as shown in Fig. 4, suppose trace tr i  con- boring node, capturing the complex relationships between
tains four spans, each recording the start and end times of  nodes. For the inner graph gsi = vsi,esi , zsi represents
m
|     |     | the feature vector of the current node vsi |     | {   | } vsi, and the out- |
| --- | --- | ------------------------------------------ | --- | --- | ------------------- |
the invocation. To better detect time-related anomalies in
m ∈
the system, we compute the following four time-related fea- put representation hsi of each node is obtained through the
m
tures as the initial node features. GAT network. The definition of the GAT is given by the (1).
●  Duration Time is the duration of the span.
|     |     | hs  | si  |     |     |
| --- | --- | --- | --- | --- | --- |
●  Waiting Time is the waiting time of the callee for the  i =σ α mn Wz   (1)
|                                 |     | m  | m        |    |     |
| ------------------------------- | --- | --- | -------- | --- | --- |
| response of the other services. |     |     | n ∈∑N(m) |     |     |
●  Local Execution Time is the local execution time of the   
callee for the current invocation, excluding the waiting  where N(m) represents the set of neighboring nodes of
| time. |     | node m, W | RF′× F is the weight matrix to be learned,  |     |     |
| ----- | --- | --------- | ------------------------------------------- | --- | --- |
∈
●  Relative Start Time is the difference between the start  and α mn  is the normalized attention weight between node
time of the current span and the start time of the root  m and node n, which is calculated by the (2).
span.
aT[Whsi Whsi]
exp LeakyReLU
|     |     | α mn= |                   | m || n   |   (2)     |
| --- | --- | ----- | ----------------- | -------- | --------- |
|     |     |       | exp(LeakyR eLU(aT | [W hs mi | W hs i])) |
Figure 4 illustrates an example of the calculation of the four  k N(m() ( || )) k
∈
| time-related features. In the example, Span A is the root span  |     | ∑   |     |     |     |
| --------------------------------------------------------------- | --- | --- | --- | --- | --- |
and is the parent of Span B. Span B is the parent of Span C  where  W  and  a  are  learnable  parameters,  and
and Span D. The timestamps represent the start time and end  LeakyReLU( )  represents  the  activation  function.  For
•
F ig. 4 Outer graph construction of
the nested graph
1 3

Multi-modal anomaly detection for microservice system through nested graph diffusion reconstruction Page 7 of 15  784

Fig. 5 Illustration of nested graph feature extraction
node m, the output feature hsi is obtained through GAT, and  updated graph features Rtri, which is calculated by the fol-
m
| then, by applying an average pooling operation, the global  |     |     | lowing (5). |     |     |     |     |
| ----------------------------------------------------------- | --- | --- | ----------- | --- | --- | --- | --- |
graph vector Isi is obtained, which is used as the log feature
tri of the corresponding node x in the outer graph. Rtri =Stack Z tri,Z tri,...,Z tri
| part I |     |     |     | 1   | 2 p |     | (5) |
| ------ | --- | --- | --- | --- | --- | --- | --- |
x
|     |     |     |     | (   | )   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
Outer graph features To more accurately capture the infor-
mation flow between nodes, we use GCN to normalize the  3.4  Feature augmentation
number of neighbors for each node in the outer graph, all
the model to focus more on nodes with higher neighbor den- Traditional  graph  data  augmentation  methods  [32,  33]
sity. This helps effectively capture the potential dependen- mostly rely on manual modifications of graph features and
cies between nodes. Taking the outer graph in Fig. 5 as an  structures,  requiring  deep  expertise  and  often  introduc-
example, for a given node x in the outer graph, the feature  ing noise [34]. Although Generative Adversarial Networks
representation Htri of each node is obtained after applying  (GANs) [35] have strong generative capabilities, they are
x
a single layer GCN as (3). prone to mode collapse when anomaly samples are scarce,
resulting in insufficient diversity in the generated samples.
|     | D˜ 1 2A˜t riD˜ 1 |     |     |     |     |     |     |
| --- | ---------------- | --- | --- | --- | --- | --- | --- |
H tri =ReLU x− x− 2T triW   (3) Mixup [36, 37] generates new samples through linear inter-
| x   | x x | x   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
polation, but due to the sparse and discrete nature of anom-
|     | (   | )   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
where A˜tri =Atri +I is the matrix obtained by adding the  aly samples, key anomaly features may be diluted during
| x   | x   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
identity matrix I to the adjacency matrix Atri and normal- mixing, weakening the anomaly characteristic. In contrast,
x
izing it, ensuring that the GCN can learn the node’s own  diffusion models learn the underlying distribution of the
features. D˜  is the degree matrix of A˜t ri. The graph con- data through gradual noise addition and removal, reduc-
| x   |     | x   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
volution operation achieves the aggregation of normalized  ing manual intervention while avoiding mode collapse.
1 1 A d d it io n a l l y ,  d i ff u s io n   m o d e l s   c a n   c o n tr o l   th e  e x te n t  o f
| neighbor information, and D˜ | x− 2A˜t | riD˜ x− 2 represents the  |     |     |     |     |     |
| ---------------------------- | ------- | ------------------------- | --- | --- | --- | --- | --- |
x
|     |     |     | au g m e n ta | t i o n   a t  d i ff e | re n t  n o i s e   l e v | el s ,  e n r i ch in g |   th e  d a ta   |
| --- | --- | --- | ------------- | ----------------------- | ------------------------- | ----------------------- | ---------------- |
normalized adjacency matrix. Ttri is the feature matrix of
|               | x                                            |     | distribution and improving anomaly detection performance.  |     |     |     |     |
| ------------- | -------------------------------------------- | --- | ---------------------------------------------------------- | --- | --- | --- | --- |
| node V tri, W |  is the trainable weight matrix in the GCN,  |     |                                                            |     |     |     |     |
| x             | x                                            |     |                                                            |     |     |     |     |
The specific approach is as follows.
| and ReLU( | ) is the activation function. |     |     |     |     |     |     |
| --------- | ----------------------------- | --- | --- | --- | --- | --- | --- |
•
|     |     |     | VAE encoder To  | ensure  | the  diversity  | of  the  | generated  |
| --- | --- | --- | --------------- | ------- | --------------- | -------- | ---------- |
Feature fusion The feature representation Htri of each  pseudo-anomaly samples, it is far from sufficient to only
x
node is concatenated with the log features Itri within the
augment the diffusion of the original input data. Consider-
x
span to obtain the updated node representation Ztri, which  ing the working principle of the VAE, the corresponding
x
is calculated by the (4). hidden variables are computed by sampling the distributions
in the latent space using the reparameterization technique,
| Z tri =Concat | H tri,I tri   |     | (4) |     |     |     |     |
| ------------- | ------------- | --- | --- | --- | --- | --- | --- |
x x x in this way, the model can introduce randomness into the
hidden variables, so that the samples fed into the diffusion
( )
where  Concat( )  denotes  the  concatenation  operation.  model have a certain degree of randomness. In MSNGAD,
•
Then,  aggregate  all  node  representations  to  obtain  the  the VAE encoder module maps the graph feature Rtri to the
1 3

| 784  | Page 8 of 15 |     |     |     |     |     |     |     |     |     |     |     | M. Fan et al. |
| ---- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- |
latent space, and by sampling from the distribution in this  VAE decoder After generating augmented features through
latent space, it generates latent variables xtri with inherent  the denoising process of the diffusion model, the decoder
randomness, which is calculated by the (6). part of the VAE is used to reconstruct and generate aug-
mented features Rˆtri that are similar to the original features.
| xtri | =µ+ε | σ   |     |     |     |     | (6) |     |     |     |     |     |     |
| ---- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
×
Contrastive learning To ensure the quality of the gener-
where µ and σ represent the mean and standard deviation  ated pseudo-anomaly samples, this paper introduces the
of the latent space, and ε N(0,I) is random noise, with  idea of contrastive learning. In the feature space, the dis-
∼ tance between the pseudo-anomaly sample Rˆtri and the real
N denoting the normal distribution and I being the identity
matrix. This noise, combined with the mean and standard  anomaly sample Rtri is minimized, while the distance from
the normal sample Rtrj is maximized. This ensures that
deviation using the reparameterization trick, is applied to
avoid the issue where the sampling operation cannot partici- the generated pseudo-anomaly samples retain the original
pate in the gradient descent. anomaly characteristics, as shown in the (10).
|          |              |     |      |                  |     |         | xtri  | L   | 1   | N   |     |     |     |
| -------- | ------------ | --- | ---- | ---------------- | --- | ------- | ----- | --- | --- | --- | --- | --- | --- |
| Forward  | process For  |     | the  | low-dimensional  |     | vector  |       | c   | =   | log |     |     |     |
|          |              |     |      |                  |     |         |       |     | −N  | i=1 |     |     |     |
obtained through sampling, Gaussian noise is progressively  exp sim Rtri,Rtri /τ   (10)
(cid:31)
|     |     |     |     |     |     |     |     |     | Rtri,Rtri |     |     | Rtri,Rtrj |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --------- | --- |
added through the forward diffusion process. In this process,  exp sim (cid:30) /τ + (cid:30) exp (cid:28) sim (cid:28) /τ
j=i ̸
at each time step, the information x  is only dependent on  (cid:29)
|     |     |     |     |     | t   |     |     |     | (cid:30) (cid:30) | (cid:28) (cid:28) | (cid:31) (cid:30) | (cid:30) | (cid:28) (cid:28) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | ----------------- | ----------------- | -------- | ----------------- |
(cid:29) is the contrastive loss, τ is(cid:29) the temperature coef-
| the previous step x |     |     | t 1 . The forward process is described by  |     |     |     |     | where L | c   |     |     |     |     |
| ------------------- | --- | --- | ------------------------------------------ | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- |
−
the (7). ficient, and sim( ) is the similarity function used to control
•
the similarity between pseudo-anomaly samples, normal
q xt ri xt ri =N xt ri; 1 β xt ri ,β I s a m p l e s ,  a n d   a n o m a l o u s s a m p l e s ,  e n s u r in g   t h e   q u a li ty   a n d
|     | t t | 1   | t   |     | t t 1 | t   | (7) |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | −   |     |     | −   | −     |     |     |     |     |     |     |     | t r |
(cid:30) e ff ec t i v e n e s s  o f   th e  a u g m e n te d   s a m p l e s .R j   r e p r e se n ts   t h e
| (cid:31) |          | (cid:29) | (cid:31) | (cid:28) |     | (cid:29) |     |                                   |     |     |     |     |     |
| -------- | -------- | -------- | -------- | -------- | --- | -------- | --- | --------------------------------- | --- | --- | --- | --- | --- |
|          | (cid:30) |          |          |          |     |          |     | normal samples in the same batch. |     |     |     |     |     |
(cid:30)
where β t (0,1) represents the intensity of the Gauss- However, since system anomalies are influenced by multiple
∈
ian noise added at step t, which increases as the time step  factors and exhibit randomness and complexity, attempting
increases. To control the noise intensity variation at each  to further reduce the spatial distance between the pseudo-
step, we refer to previous work [34], we use linear noise  anomaly and anomaly samples may lead the model to fit
control to regulate the noise intensity. This is calculated by  specific anomalies, ultimately reducing its generalization
the (8). ability. Therefore, to further ensure the diversity of pseudo-
anomaly samples, upper and lower threshold bounds are set
t 1 in the feature space. This ensures that the similarity between
| βt=k | α min+ | −   | (α max− | α min) | , t 1,2,...,T |     |   (8) |     |     |     |     |     |     |
| ---- | ------ | --- | ------- | ------ | ------------- | --- | ----- | --- | --- | --- | --- | --- | --- |
|      | ×      | T   | 1       |        | ∈{            | }   |       |     |     |     |     |     |     |
( − ) the generated pseudo-anomaly samples and the real anom-
aly samples remains high (i.e., above the lower bound) but
where α min <α max (0,1) are the minimum and maxi- not identical (i.e., not exceeding the upper bound). In this
∈
mum values of the noise, k [0,1] is a hyperparameter that  way, the pseudo-anomaly samples can accurately capture
∈
adjusts the noise intensity, and T is the total number of for- the  original  anomaly  features  while  remaining  distinct,
ward steps. thereby ensuring the diversity of the generated anomaly
samples. Based on this, we define the margin constraint loss,
Reverse process After the noise addition process ends and  as shown in the (11).
pure noise xtri is obtained, the diffusion model’s reverse
T
|     |     |     |     |     |     |     |     | L   | =λ  | max 0,sim |     | sim Rˆtri,Rtri |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | -------------- | --- |
process is used to remove the noise, gradually restoring the  margin 1 low
|     |     |     |     |     |     |     |     |     |     |     | −   |     |   (11) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |
original vector from xtri. The reverse process is described  ( ( ))
|                      |           |     | T    |          |     |        |       |         | +λ     | max 0,sim                                  | Rˆtri,Rtri |     | sim  |
| -------------------- | --------- | --- | ---- | -------- | --- | ------ | ----- | ------- | ------ | ------------------------------------------ | ---------- | --- | ---- |
|                      |           |     |      |          |     |        |       |         |        | 2                                          |            |     | high |
| by the equation (9). |           |     |      |          |     |        |       |         |        |                                            |            | −   |      |
|                      |           |     |      |          |     |        |       |         |        | (                                          | (          | )   | )    |
|                      |           |     |      |          |     |        |       | where λ |  and λ |  are the weight parameters for each term,  |            |     |      |
| P                    | xtri xtri | =N  | xtri | µ xtri,t | ,σ  | xtri,t |   (9) |         | 1      | 2                                          |            |     |      |
|                      | t 1       | t   | t    | 1 t      |     | t      |       |         |        |                                            |            |     |      |
− − sim low  and sim high  represent the lower and upper bounds
| (cid:31)                       | (cid:30)     | (cid:29) | (cid:31) | (cid:30)                       |                   | (cid:29) |            |                              |     |     |     |     |     |
| ------------------------------ | ------------ | -------- | -------- | ------------------------------ | ----------------- | -------- | ---------- | ---------------------------- | --- | --- | --- | --- | --- |
|                                | (cid:30)     |          |          | (cid:30) (cid:28)              | (cid:27) (cid:28) | (cid:27) |            | of similarity, respectively. |     |     |     |     |     |
| wh ere µ                       | (cid:30)xtri | ,t  and  |  σ xt    | (cid:30) ri, t  are            | the m             | ean an d |  variance  |                              |     |     |     |     |     |
|                                |              | t        |          | t                              |                   |          |            |                              |     |     |     |     |     |
| used to recover the state xtri |              |          |          |  from the previous state xtri. |                   |          |            |                              |     |     |     |     |     |
|                                | (            | )        | (        | t 1 )                          |                   |          | t          |                              |     |     |     |     |     |
−
1 3

Multi-modal anomaly detection for microservice system through nested graph diffusion reconstruction Page 9 of 15  784
Loss We use three loss functions to jointly optimize the dif- anomalies, Algorithm 1 outlines the complete learning
fusion reconstruction model: the VAE model loss, the diffu- process of MSNGAD.
Algorithm 1 The learning process of MSNGAD
sion model loss, and the contrastive learning loss. The loss
is defined by the (12).
| L i=(MSE | Rtri,Rˆtri       | +D q                   | xtri Rtri | p xtri )                           |        |     |     |     |     |
| -------- | ---------------- | ---------------------- | --------- | ---------------------------------- | ------ | --- | --- | --- | --- |
|          |                  | KL                     | |         | ∥                                  |        |     |     |     |     |
|          |                  |                        |           |                                    |   (12) |     |     |     |     |
|          | (cid:31) xt ri,t | 2 (cid:30) c+(cid:29)L | (cid:29)  | (cid:28) (cid:29) (cid:28)(cid:28) |        |     |     |     |     |
| +        | ε i− εˆ i t      | +(L m                  | argin )   |                                    |        |     |     |     |     |
2
| (cid:27) | (cid:29) | (cid:28)(cid:27) |     |     |     |     |     |     |     |
| -------- | -------- | ---------------- | --- | --- | --- | --- | --- | --- | --- |
| (cid:27) |          | (cid:27)         |     |     |     |     |     |     |     |
where L  is the total loss of sample i in the diffusion recon-
i
| struction module, MSE(                                       |     | ) and D | KL                     | ( ) together form    |     |     |     |     |     |
| ------------------------------------------------------------ | --- | ------- | ---------------------- | -------------------- | --- | --- | --- | --- | --- |
|                                                              |     | •       |                        | •                    |     |     |     |     |     |
| the loss of the VAE model, MSE(                              |     |         | ) represents the mean  |                      |     |     |     |     |     |
| squared error between Rtri and Rˆtri, used to calculate the  |     |         | •                      |                      |     |     |     |     |     |
| reconstruction error of the VAE. D                           |     |         | (                      | ) represents the KL  |     |     |     |     |     |
KL
| divergence, where q(xtri |     | Rtri) is the approximate poste- |     | •   |     |     |     |     |     |
| ------------------------ | --- | ------------------------------- | --- | --- | --- | --- | --- | --- | --- |
|
rior distribution used to learn the distribution of latent vari-
ables from input data Rtri, p(xtri) is the prior distribution,
which is the assumed distribution of latent variable xtri,
and in this paper, the standard normal distribution N(0,I)
| is chosen. ε                                            |  and εˆ(xtri,t) refer to the true noise and pre- |     |     |     |     |     |     |     |     |
| ------------------------------------------------------- | ------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- |
|                                                         | i                                                | i t |     |     |     |     |     |     |     |
| dicted noise of sample i at time step t, respectively.  |                                                  |     |     |     |     |     |     |     |     |
∥•∥2
| represents the L2 norm, used to calculate the loss between  |     |     |     |             |          | 4  Evaluation |     |     |     |
| ----------------------------------------------------------- | --- | --- | --- | ----------- | -------- | ------------- | --- | --- | --- |
| the true noise and the predicted noise. (L                  |     |     |     | c +L margin | ) repre- |               |     |     |     |
sents the contrastive loss with the added margin constraint. In our study, we evaluate the MSNGAD method and discuss
the following questions:
3.5  Anomaly detection
|     |     |     |     |     |     | ●  RQ1:  How  | effective  | is  MSNGAD  | in  microservice  |
| --- | --- | --- | --- | --- | --- | ------------- | ---------- | ----------- | ----------------- |
In the anomaly detection phase, we train an MLP classifica- anomaly detection compared to existing baseline meth-
tion network with a softmax output layer to predict the  ods, including single-modal and multi-modal methods?
probabilities yˆ of normal and anomalous states. The prob- ●  RQ2: How do different experimental parameters in
abilities yˆ are calculated by the (13). MSNGAD affect anomaly detection results?
|            |       |      |     |     |      | ●  RQ3:  How  | effective  | are  the  different  | modules  in  |
| ---------- | ----- | ---- | --- | --- | ---- | ------------- | ---------- | -------------------- | ------------ |
| yˆ=softmax | WRtri | +b   |     |     | (13) |               |            |                      |              |
MSNGAD?
|     | (   | )   |     |     |     |                          |     |     |     |
| --- | --- | --- | --- | --- | --- | ------------------------ | --- | --- | --- |
|     |     |     |     |     |     | 4.1  Experimental design |     |     |     |
where W and b are the weight matrix and the bias term
of the output layer. During training, the model’s predic-
| tions are compared with the true labels to compute the  |     |     |     |     |     | 4.1.1  Dataset |     |     |     |
| ------------------------------------------------------- | --- | --- | --- | --- | --- | -------------- | --- | --- | --- |
cross-entropy loss, which is used to optimize the model’s
prediction performance. For a given new trace and its  Our experimental studies are conducted based on two data-
corresponding logs, MSNGAD follows the same process  sets: TrainTicket (TT) and Generic AIOps Atlas (GAIA)1.
as in the training phase to generate the nested graph. It  TT is a dataset collected from deploying TrainTicket
uses GAT and GCN to extract features from the inner  on a Kubernetes cluster. It is a medium-sized open-source
and outer graphs, respectively. The fused features are  microservice  system  for  booking  train  tickets,  which
then passed to the trained classification network to detect  has  been  widely  applied  in  microservice  architecture,
1  h t t p s :   /  / g i t h u   b . c  o  m /  C l o  u d W  i  s  e - O p  e n S  o u r   c e / G  A I A - D a t a S e t
1 3

784 Page 10 of 15 M. Fan et al.
infrastructure, and AIOps related research [38, 39]. The ● LogRobust [23] is a log anomaly detection method that
dataset includes 41 microservices written in 45 different employs the FastText algorithm to model the semantic
languages, including Java, JavaScript, and Python, which representation of log templates. It combines the TF-
communicate via synchronous REST calls and asynchro- IDF algorithm to generate semantic vectors for logs and
nous messaging. We deployed TT on a Kubernetes cluster uses an attention-based Bi-LSTM model for anomaly
with 4 virtual machines, each configured with 8 CPU cores detection.
and 32GB of memory. The cluster also hosts the TT appli- ● TraceAnomaly [7] is a trace anomaly detection method
cation, ElasticSearch [40], and Apache SkyWalking [2]. that represents traces as service trace vectors and trains
We used Python scripts to automatically send requests to a VAE model to detect anomalous traces.
the deployed microservice system, simulating user requests ● TraceVAE [26] is a trace anomaly detection method
in various scenarios. Apache SkyWalking was used as the that uses a dual-variable graph VAE to separately en-
distributed tracing framework to collect trace and log infor- code and reconstruct temporal and structural features of
mation, while ElasticSearch was used to store the collected traces. Anomalies are detected by calculating the recon-
data. During data collection, we used fault injection meth- struction score.
ods to collect abnormal data. Following previous works ● DeepTraLog [9] is a multi-modal anomaly detection
[41–43], this experiment used the widely used chaos engi- method for microservices that combines logs and each
neering tool, chaos-mesh [44], to inject network failures trace data to construct trace event graph. It uses deep
(i.e., network loss, network delay) and pod failures (i.e., support vector data description to train a one-class clas-
CPU pressure, memory pressure, request loss) into different sification model for anomaly detection.
services separately.
GAIA is an open dataset in the field of AIOps, provided 4.1.3 Evaluation metrics
by CloudWise. It is collected from a simulated microservice
system environment consisting of 5 hosts and 10 microser- This paper uses Precision, Recall and F1-score
vices, including redisservice1, webservice1, loginservice1, as evaluation metrics to measure the perfor-
etc. This dataset contains over 2 million trace records and mance of anomaly detection, defined as fol-
87 million log records. Additionally, this dataset simulates lows: Precision= TP , Recall= TP ,
TP+FP TP+FN
r ( e i. a e l . - , w sy o s r t l e d m f a fr il e u e r z e e , s p c r e o n c a e r s io s s c r b as y h ) i n a j n e d c t s in er g v i s c y e s f te a m ilu r f e a s i l ( u i. r e e . s , F1 − score= 2 ×P P re r c e i c s i i s o i n o + n ×R R ec e a c l a l ll, where TP represents the
number of instances correctly classified as anomalies by the
login failure, file loss, access denied).
model, FP represents the number of instances incorrectly
More detailed information is shown in Table 1, where
classified as anomalies, and FN represents the number of
templates represent the number of log templates obtained by
undetected anomalies.
parsing logs with Drain3.
4.1.2 Baseline approaches 4.1.4 Experimental settings
In our study, we compare the MSNGAD method with the We implement MSNGAD using PyTorch 2.5.3, Python
following baseline approaches, which include both single- 3.9.19, and PyTorch Geometric 2.5.3. During the experi-
modal log and trace anomaly detection methods, as well as ments, 70% of the total data is used for training, and 30% is
multi-modal anomaly detection methods. reserved for testing. In the data collection process, the data
generated by the system during the time period when faults
● DeepLog [21] is a log anomaly detection method that are injected is considered anomaly data, while other data is
takes log template index sequences as input. It uses an considered normal data generated during system operation.
LSTM model to learn the sequential patterns of normal The settings of MSNGAD are the following: use the GAT
logs and detects anomalous logs by identifying devia- to extract the nested inner graph features, set the number of
tions from the normal pattern. layers of the GAT to 2, set the dimensionality of the out-
put features to 16, and use the GCN to extract the nested
outer graph features, set the number of layers of the GCN to
Table 1 The details of two datasets 2, and the output feature dimension set to 4, and the batch
Dataset Services Templates Records %Failures size is set to 64, feature augmentation ratio factor in each
TT 41 294 Trace: 121,280 2.3% batch is set to 3, and the noise scale of the diffusion model is
Log: 1,359,061 set to 1e − 4. MSNGAD uses Adam as the optimizer, epoch
GAIA 10 43 Trace: 2,321,280 8.9%
is set to 20, and the learning rate is set to 0.001. For the
Log: 87,974,577
1 3

Multi-modal anomaly detection for microservice system through nested graph diffusion reconstruction Page 11 of 15 784
baseline approaches, this paper uses their publicly available complex relationships in the trace. Secondly, TraceAnomaly
implementation, preprocesses the experimental data, and focuses primarily on the response time of trace and therefore
configures the model based on the parameters in the original can only detect anomalies that significantly impact the ser-
paper, the final experimental results are obtained by averag- vice response time distribution. But TraceVAE reconstructs
ing over several experiments. both time and spatial features using the dual-variable graph,
considering multiple aspects of the trace data and thus
4.2 RQ1: effectiveness of MSNGAD detecting more anomalies. Despite this, its performance still
lags behind MSNGAD, mainly because it lacks log data and
Table 2 shows the effectiveness evaluation results of cannot detect abnormal behaviors within log events.
MSNGAD and various baseline approaches on two different Among all baseline approaches, DeepTraLog achieved the
datasets. The results indicate that MSNGAD outperforms best anomaly detection results. This is because DeepTraLog
all baseline approaches. On both datasets, its Precision, combines log and trace data, using a unified graph represen-
Recall and F1-score achieved values of 0.939, 0.978, 0.958 tation to describe the complex trace structure and embedded
and 0.941, 0.982, 0.961, respectively. With a high Recall, log events. Through feature interactions between different
MSNGAD demonstrates its ability to accurately detect most modalities, DeepTraLog can fully exploit the connections
anomalies in microservices, with very few false positives. between anomalous behaviors across modalities. However,
Among the two log-based anomaly detection methods, MSNGAD outperforms DeepTraLog by 1.8% and 2.0% in
DeepLog shows poorer performance. The reason lies in the F1-score on the two datasets, respectively. The reason for
fact that DeepLog only uses LSTM to learn the sequence this is that, in anomaly detection, DeepTraLog uses Deep
patterns of normal logs. However, the relationships between SVDD to learn the conventional feature representations
logs in a microservices system are complex, and relying of the training data and minimize the hypersphere. How-
solely on a single data feature for accurate prediction is chal- ever, when anomalies in a microservices system are highly
lenging, which results in a noticeable decline in DeepLog’s diverse, it is challenging to find an appropriate boundary to
detection performance. In contrast, LogRobust improves the identify anomalous samples in the high-dimensional latent
detection results as it not only considers the sequence pat- space. In contrast, MSNGAD uses feature augmentation to
terns of normal logs but also utilizes semantic vectors of increase the diversity of anomalous behaviors, enabling the
logs as features for detection. This enables it to effectively model to see more anomalous samples during the training
learn the distinguishing semantic features between normal phase and thus detect more diverse anomalies.
and abnormal data in the log sequence. However, logs gen-
erated during the operation of a microservices system have 4.3 RQ2: impact of hyperparameters
complex dependencies. Treating them only as simple time-
series data may overlook the spatial dependencies between To further explore the impact of different hyperparameter
logs. Moreover, both methods do not consider system trace settings on anomaly detection performance, this paper con-
information, limiting the reflection of the anomaly detection ducts a hyperparameter sensitivity experiment. Specifically,
results. we focus on the sensitivity of two important hyperparam-
Among the trace-based anomaly detection methods, eters in the feature augmentation module: the noise scale k
TraceVAE outperforms TraceAnomaly by 15.6% and 22% and the feature augmentation ratio factor n. When analyzing
in Recall, respectively, for the following reasons: First, each specific parameter, we keep all other parameters con-
TraceAnomaly constructs service trace vector that only stant. We use Precision, Recall and F1-score as evaluation
reflects the sequential relationship between services in metrics to assess the experimental performance under dif-
the trace, failing to fully capture the causal relationships ferent hyperparameter settings and perform experiments on
between spans. In contrast, TraceVAE uses a dual-variable both the TT and GAIA datasets to comprehensively evaluate
graph approach, leveraging graph structures to represent the
Table 2 Experimental results: best results are in bold font
Approach TT GAIA
Precision Recall F1-score Precision Recall F1-score
DeepLog 0.426 0.719 0.535 0.411 0.682 0.512
LogRobust 0.766 0.817 0.789 0.707 0.811 0.755
TraceAnomaly 0.502 0.673 0.575 0.539 0.637 0.584
TraceVAE 0.619 0.892 0.731 0.756 0.859 0.804
DeepTraLog 0.933 0.948 0.940 0.947 0.935 0.941
MSNGAD 0.939 0.978 0.958 0.941 0.982 0.961
1 3

784 Page 12 of 15 M. Fan et al.
Fig. 6 Sensitivity experiment of noise scale k
Fig. 7 Sensitivity experiment of feature augmentation ratio factor n
the changes in model performance under different hyperpa- Therefore, we choose a relatively small noise scale of 1e − 4
rameter configurations. as the optimal setting for feature augmentation.
Noise scale k In the experiment on the sensitivity of the Feature augmentation ratio factor n In the experiment
noise scale hyperparameter k, we evaluate k values of 0, on the impact of the feature augmentation ratio factor
1e − 5, 1e − 4, 1e − 3 and 1e − 2. The experimental results are n, as shown in Fig. 7, we observe the effect on anomaly
shown in Fig. 6. As can be seen, with the increase in noise detection when n takes values of 1, 2, 3, 4, and 5. When
scale, the performance shows a trend of first increasing n<3, the anomaly detection performance improves as n
and then decreasing. Compared to the baseline case with increases, indicating that moderately increasing the diver-
no noise (k =0), a moderate amount of noise (such as sity of pseudo-anomaly samples helps the model learn more
k =1e − 4) can improve the model’s generalization ability generalized anomaly patterns. However, when n>3, the
and enhance its learning of anomaly patterns, further vali- anomaly detection performance starts to decline. This is
dating the effectiveness of noise perturbation and denois- because excessive augmentation data might lead the model
ing training. However, when k increases further, the model to overly rely on these pseudo-anomaly samples. If these
performance drops significantly because excessive noise samples do not reflect actual anomaly patterns, they nega-
may disrupt the original graph structure, making it difficult tively affect the model’s learning process, thereby reduc-
for the model to extract valid features during training, thus ing the model’s ability to identify real anomalies. Based on
leading to a decline in the quality of generated samples. this, we select n=3 as the optimal setting for the feature
1 3

Multi-modal anomaly detection for microservice system through nested graph diffusion reconstruction Page 13 of 15 784
Fig. 8 Ablation experiment
augmentation ratio factor, ensuring the validity of the aug- log templates within spans. Due to the temporal and spatial
mented data while avoiding the negative effects of excessive dependencies between the generated log messages in the
augmentation. operation of the system, and the use of log template seman-
tics only as a part of the fusion features cannot fully utilize
4.4 RQ3: effectiveness of different modules the log features, thus ignoring some of the anomalies and
leading to degraded detection results.
To further verify the effectiveness of each module, we con- When comparing No-Aug and No-Cro, it was found that
ducted several ablation experiments on MSNGAD. Specifi- the F1-score remained stable across different datasets. This
cally, the following modifications were made to the original is because although No-Cro used the feature augmentation
model: technique, it did not control the diversity of the generated
pseudo-anomaly samples. In the diffusion reconstruction
(1) Only-Trace: The log data is removed, and only the trace phase, the optimization goal of the diffusion reconstruction
data is retained. stage degrades to minimize the error between the generated
(2) Only-Log: The trace data is removed, and only the log sample features and the original input sample features. As
data is retained. training progressed, the generated samples and the origi-
(3) No-NG: The nested graph structure is removed, and nal samples became very similar in feature space, which is
only the BERT-extracted log features are used as the equivalent to only increasing the number of anomaly sam-
update features for the external graph nodes. ples without increasing the diversity of anomaly samples,
(4) No-Aug: The feature augmentation module is removed. and when the model encounter types of anomalies it has
(5) No-Cro: The feature augmentation module is retained, never seen before, false positives may still occur. In con-
but the contrastive learning is removed. trast, MSNGAD shows significant improvement in Recall
compared to No-Cro, which further confirms the effective-
The above five variant models were experimented on the ness of introducing contrastive learning to increase the
datasets TT and GAIA respectively, and the experimen- diversity of anomalous samples. This enables the detection
tal results are shown in Fig. 8, which shows that, in the of more types of anomalies in the system, effectively reduc-
single-modal approaches (Only-Log and Only-Trace), the ing false positives.
experimental results on the two datasets have a significant
decrease compared to the three multi-modal approaches.
This effectively illustrates the superiority of multi-modal 5 Conclusion
data in detecting anomalies in microservice systems.
In the comparison experiment in which the nested graph In this paper, we propose MSNGAD, a microservice
structure was removed (No-NG), the F1-score decreased anomaly detection method based on nested graph diffusion
by 1.6% and 2.5% on the TT and GAIA datasets, respec- reconstruction. It combines two types of monitoring data,
tively. This proves that using nested graphs in MSNGAD traces and logs, and uses a unified nested graph representa-
effectively captures the dependency relationships between tion to describe the complex structure of traces and the log
1 3

784 Page 14 of 15 M. Fan et al.
2019 IEEE 12th International Conference on Cloud Computing
events embedded in them. MSNGAD uses GAT and GCN
(CLOUD). pp 179–186. h t t p s : / / d oi . o r g / 1 0 . 1 1 0 9 / C L O U D . 2 0 1 9 . 0
to extract features capturing the inner and outer graphs of 0 0 3 8
nested graphs, respectively, and solves the problem of posi- 7. Liu P, Xu H, Ouyang Q, et al. (2020) Unsupervised detection of
microservice trace anomalies through service-level deep bayes-
tive and negative sample imbalance in anomaly detection by
ian networks. In: 2020 IEEE 31st International Symposium on
feature augmentation using diffusion reconstruction method.
Software Reliability Engineering (ISSRE). pp 48–58. h t t p s : / / d o i .
We evaluated MSNGAD on two datasets and conducted o r g / 1 0 . 1 1 0 9 / I S S R E 5 0 0 3 . 2 0 2 0 . 0 0 0 1 4
experimental comparisons with single-modal and multi- 8. He Y, Zhang X, Wang P et al (2024) Microservice traces anom-
aly detection based on structural clustering and graph attention
modal methods, respectively, and the experimental results
autoencoder. In: 2024 7th International Conference on Advanced
show that MSNGAD outperforms other anomaly detection
Algorithms and Control Engineering (ICAACE). pp 977–981. h t t
methods and can effectively model the correlation between p s : / / d o i . o r g / 1 0 . 1 1 0 9 / I C A A C E 6 1 2 0 6 . 2 0 2 4 . 1 0 5 4 9 2 4 2
different data modalities as well as the temporal and spa- 9. Zhang C, Peng X, Sha C et al (2022) Deeptralog: Trace-log com-
bined microservice anomaly detection through graph-based deep
tial dependencies within each modality. In future work, we
learning. In: 2022 IEEE/ACM 44th International Conference on
will continue to evaluate MSNGAD using different types
Software Engineering (ICSE). pp 623–634. h t t p s : / / d o i . o r g / 1 0 . 1 1 4
of microservice systems to further explore the effectiveness 5 / 3 5 1 0 0 0 3 . 3 5 1 0 1 8 0
and advantages of the methods in this paper. 10. Ying S, Wang B, Wang L, Li Q, Zhao Y, Shang J, Huang H, Cheng
G, Yang Z, Geng J (2021) An improved knn-based efficient log
anomaly detection method with automatically labeled samples.
Acknowledgements This work is supported by Liaoning Prov-
ACM Trans Knowl Discov Data 15(3):1–22
ince Applied Basic Research Program Project (Grant No. 2023
11. Zhang C, Peng X, Zhou T et al (2022) Tracecrl: contrastive repre-
JH2/101300195).
sentation learning for microservice trace analysis. In: Proceedings
of the 30th ACM Joint European Software Engineering Confer-
Author contributions All authors contributed to the study conception
ence and Symposium on the Foundations of Software Engineer-
and design. Data collection, data processing, and analysis were per-
ing. ESEC/FSE 2022. Association for Computing Machinery,
formed by Xiuguo Zhang, Zhiying Cao, and Peipeng Wang. The first
New York. pp 1221–1232. h t t p s : / / d oi . o r g / 1 0 . 1 1 4 5 / 3 5 4 0 2 5 0 . 3 5 4
draft of the manuscript was written by Mengwei Fan and all authors
9 1 4 6
commented on previous versions of the manuscript. All authors read
12. He P, Zhu J, Zheng Z et al (2017) Drain: an online log parsing
and approved the final manuscript.
approach with fixed depth tree. In: 2017 IEEE International Con-
ference on Web Services (ICWS). pp 33–40. h t t p s : / / d o i . o r g / 1 0 . 1 1
Data availability The data that support the findings of this study are 0 9 / I C W S . 2 0 1 7 . 1 3
available on request from the corresponding author. 13. Brody S, Alon U, Yahav E (2021) How attentive are graph atten-
tion networks? arXiv:2105.14491
Declarations 14. Kipf TN, Welling M (2016) Semi-supervised classification with
graph convolutional networks. arXiv:1609.02907
15. Wang C, Zhang X, Gao H et al (2024) Colergs-constrained safe
Ethical and informed consent for data used This study does not con-
reinforcement learning for realising mass’s risk-informed colli-
tain any studies with human participants or animals performed by any
sion avoidance decision making. Knowl-Based Syst 300:112205.
of the authors.
h t t p s : / / d oi . o r g / 1 0 . 1 0 1 6 / j . k n o s y s . 2 0 2 4 . 1 1 2 2 0 5
16. Kazemi MH, Alvanchi A (2025) Application of nlp-based mod-
Conflict of interest The authors declare that they have no known com-
els in automated detection of risky contract statements written in
peting financial interests or personal relationships that could have ap-
complex script system. Expert Syst Appl 259:125296
peared to influence the work reported in this paper.
17. Liu Y, Wang H, Zhou H, Li M, Hou Y, Zhou S, Wang F, Hoetzlein
R, Zhang R (2024) A review of reinforcement learning for natural
language processing and applications in healthcare. J Am Med
References Inform Assoc 31(10):2379–2393
18. Santos CFGD, Arrais RR, Silva JVSd, Silva MHMd, Neto
WBGdA, Lopes LT, Bileki GA, Lima IO, Rondon LB, Souza
1. Opentracing.io: OpenTracing. (2021) https://opentracing.io/.
BMd et al (2025) Isp meets deep learning: a survey on deep learn-
Retrieved August 15, 2021
ing methods for image signal processing. ACM Comput Survey
2. skywalking.apache.org: Apache SkyWalking. (2022) h t t p : / / s k y w
57(5):1–44
a l k i n g . a p a c h e . o r g / . Retrieved March 11, 2022
19. Xu C, Zhang T, Zhang D, Zhang D, Han J (2024) Deep generative
3. Zhang C, Wang X, Zhang H et al (2023) Layerlog: Log sequence
adversarial reinforcement learning for semi-supervised segmen-
anomaly detection based on hierarchical semantics. Appl Soft
tation of low-contrast and small objects in medical images. IEEE
Comput 132:109860. h t t p s : / / d o i . o r g / 1 0 . 1 0 1 6 / j . a s o c . 2 0 2 2 . 1 0 9 8 6 0
Trans Med Imaging 43(9):3072–3084. h t t p s : / / d o i . o r g / 1 0 . 1 1 0 9 / T
4. Farzad A, Gulliver TA (2020) Unsupervised log message anom-
M I . 2 0 2 4 . 3 3 8 3 7 1 6
aly detection. ICT Express 6(3):229–237. h t t p s : / / d o i . o r g / 1 0 . 1 0 1 6
20. Wang C, Zhang X, Gao H et al (2024) Optimizing anti-collision
/ j . i c t e . 2 0 2 0 . 0 6 . 0 0 3
strategy for mass: a safe reinforcement learning approach to
5. Zhang C, Wang X, Zhang H et al (2021) Log sequence anom-
improve maritime traffic safety. Ocean Coast Manag 253:107161.
aly detection based on local information extraction and glob-
h t t p s : / / d oi . o r g / 1 0 . 1 0 1 6 / j . o c e c o a m a n . 2 0 2 4 . 1 0 7 1 6 1
ally sparse transformer model. IEEE Trans Netw Serv Manage
21. Du M, Li F, Zheng G et al (2017) Deeplog: anomaly detection
18(4):4119–4133. h t t p s : / / d o i . o r g / 1 0 . 1 1 0 9 / T N S M . 2 0 2 1 . 3 1 2 5 9 6 7
and diagnosis from system logs through deep learning. In: Pro-
6. Nedelkoski S, Cardoso J, Kao O (2019) Anomaly detection
ceedings of the 2017 ACM SIGSAC conference on computer and
from system tracing data using multimodal deep learning. In:
communications security. pp 1285–1298
1 3

Multi-modal anomaly detection for microservice system through nested graph diffusion reconstruction Page 15 of 15 784
22. Meng W, Liu Y, Zhu Y et al (2019) Loganomaly: unsupervised 35. Schlegl T, Seeböck P, Waldstein SM, Schmidt-Erfurth U, Langs G
detection of sequential and quantitative anomalies in unstructured (2017) Unsupervised anomaly detection with generative adversar-
logs. IJCAI 19:4739–4745 ial networks to guide marker discovery. CoRR. arXiv:1703.05921
23. Zhang X, Xu Y, Lin Q et al (2019) Robust log-based anomaly 36. Zhang H, Cisse M, Dauphin YN, Lopez-Paz D (2017) mixup:
detection on unstable log data. In: Proceedings of the 2019 27th beyond empirical risk minimization. arXiv:1710.09412
ACM Joint Meeting on European Software Engineering Confer- 37. Wang P, Zhang X, Cao Z (2025) Anomaly detection for microser-
ence and Symposium on the Foundations of Software Engineer- vice system via augmented multimodal data and hybrid graph
ing. ESEC/FSE 2019. Association for Computing Machinery, representations. Inf Fusion 103017
New York, pp 807–817. h t t p s : / / d o i . o r g / 1 0 . 1 1 4 5 / 3 3 3 8 9 0 6 . 3 3 3 8 9 38. Zhao N, Chen J, Yu Z et al (2021) Identifying bad software
3 1 changes via multimodal anomaly detection for online service sys-
24. Xiao R, Li W, Lu J, Jin S (2024) Contexlog: Non-parsing log tems. In: Proceedings of the 29th ACM joint meeting on Euro-
anomaly detection with all information preservation and enhanced pean Software Engineering Conference and Symposium on the
contextual representation. IEEE Trans Netw Service Manag Foundations of Software Engineering. ESEC/FSE 2021. Associa-
25. Wang P, Zhang X, Cao Z, Xu W, Li W (2024) Loggt: cross-system tion for Computing Machinery, New York, pp 527–539. h t t p s : / / d
log anomaly detection via heterogeneous graph feature and trans- o i . o r g / 1 0 . 1 1 4 5 / 3 4 6 8 2 6 4 . 3 4 6 8 5 4 3
fer learning. Expert Syst Appl 251:124082 39. Zhou X, Peng X, Xie T et al (2019) Latent error prediction and
26. Xie Z, Xu H, Chen W et al (2023) Unsupervised anomaly detec- fault localization for microservice applications by learning from
tion on microservice traces through graph vae. In: Proceedings system trace logs. In: Proceedings of the 2019 27th ACM joint
of the ACM Web Conference 2023. WWW ’23. Association for meeting on European Software Engineering Conference and
Computing Machinery, New York, pp 2874–2884. h t t p s : / / d oi . o r g Symposium on the Foundations of Software Engineering. ESEC/
/ 1 0 . 1 1 4 5 / 3 5 4 3 5 0 7 . 3 5 8 3 2 1 5 FSE 2019. Association for Computing Machinery, New York, pp
27. Zhang K, Zhang C, Peng X et al (2022) Putracead: Trace anomaly 683–694. h t t p s : / / d oi . o r g / 1 0 . 1 1 4 5 / 3 3 3 8 9 0 6 . 3 3 3 8 9 6 1
detection with partial labels based on gnn and pu learning. In: 40. Elastic (2022) Elasticsearch. Retrieved March 11, 2022 from h t t p
2022 IEEE 33rd International Symposium on Software Reliabil- s : / / w w w . e l a s t i c . c o / e l a s t i c s e a r c h /
ity Engineering (ISSRE). pp 239–250. h t t p s : / / d o i . o r g / 1 0 . 1 1 0 9 / I S 41. Yu G, Chen P, Chen H et al (2021) Microrank: end-to-end latency
S R E 5 5 9 6 9 . 2 0 2 2 . 0 0 0 3 2 issue localization with extended spectrum analysis in microser-
28. Kong S, Ai J, Lu M, Gong Y (2024) Grand: Gan-based software vice environments. In: Proceedings of the Web Conference. pp
runtime anomaly detection method using trace information. Neu- 3087–3098
ral Netw 169:365–377 42. Meng Y, Zhang S, Sun Y et al (2020) Localizing failure root
29. Xie X, Jian S, Huang C (2023) Logtracead: anomaly detection causes in a microservice through causality inference. In: 2020
from both logs and traces with graph representation learning. In: IEEE/ACM 28th International Symposium on Quality of Service
Proceedings of the 2023 2nd International Conference on Net- (IWQoS). pp 1–10. h t t p s : / / d oi . o r g / 1 0 . 1 1 0 9 / I W Q o S 4 9 3 6 5 . 2 0 2 0 . 9
works, Communications and Information Technology. CNCIT 2 1 3 0 5 8
’23. Association for Computing Machinery, New York. h t t p s : / / d o 43. Ma M, Xu J, Wang Y et al (2020) Automap: diagnose your
i . o r g / 1 0 . 1 1 4 5 / 3 6 0 5 8 0 1 . 3 6 0 5 8 2 4 microservice-based web applications automatically. In: Proceed-
30. Devlin J (2018) Bert: Pre-training of deep bidirectional trans- ings of The Web Conference 2020. WWW ’20. Association for
formers for language understanding. arXiv:1810.04805 Computing Machinery, New York, pp 246–258. h t t p s : / / d o i . o r g / 1 0
31. Song X, Salcianu A, Song Y et al (2020) Fast wordpiece tokeniza- . 1 1 4 5 / 3 3 6 6 4 2 3 . 3 3 8 0 1 1 1
tion. Conference on empirical methods in natural language pro- 44. Mesh C (2022) Chaos Mesh. Retrieved March 11, 2022 from
cessing. Punta Cana, DOMINICAN REP, pp 07–11 https://chaos-mesh.org/
32. Chen N, Liu Z, Hooi B, et al. (2024) Consistency training with
learnable data augmentation for graph anomaly detection with Publisher's Note Springer Nature remains neutral with regard to juris-
limited supervision. In: The twelfth international conference on dictional claims in published maps and institutional affiliations.
learning representations
33. You Y, Chen T, Sui Y et al (2020) Graph contrastive learning with
Springer Nature or its licensor (e.g. a society or other partner) holds
augmentations. Adv Neural Inf Process Syst 33:5812–5823
exclusive rights to this article under a publishing agreement with the
34. Tian Y, Jiang A, Huang Q et al (2024) Latent diffusion-based data
author(s) or other rightsholder(s); author self-archiving of the accepted
augmentation for continuous-time dynamic graph model. In: Pro-
manuscript version of this article is solely governed by the terms of
ceedings of the 30th ACM SIGKDD conference on Knowledge
such publishing agreement and applicable law.
Discovery and Data Mining. KDD ’24, pp. 2900–2911. Associa-
tion for Computing Machinery, New York. h t t p s : / / d o i . o r g / 1 0 . 1 1 4
5 / 3 6 3 7 5 2 8 . 3 6 7 1 8 6 3
1 3