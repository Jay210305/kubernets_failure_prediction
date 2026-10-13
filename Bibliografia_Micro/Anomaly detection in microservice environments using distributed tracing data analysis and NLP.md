Kohyarnejadfard et al. Journal of Cloud Computing:
Journal of Cloud Computing (2022) 11:25
Advances, Systems and Applications
https://doi.org/10.1186/s13677-022-00296-4
RESEARCH Open Access
Anomaly detection in microservice
environments using distributed tracing data
analysis and NLP
Iman Kohyarnejadfard1*, Daniel Aloise1*, Seyed Vahid Azhari1,2 and Michel R. Dagenais1
Abstract
In recent years DevOps and agile approaches like microservice architectures and Continuous Integration have
become extremely popular given the increasing need for flexible and scalable solutions. However, several factors
such as their distribution in the network, the use of different technologies, their short life, etc. make microservices
prone to the occurrence of anomalous system behaviours. In addition, due to the high degree of complexity of small
services, it is difficult to adequately monitor the security and behavior of microservice environments. In this work, we
propose an NLP (natural language processing) based approach to detect performance anomalies in spans during a
given trace, besides locating release-over-release regressions. Notably, the whole system needs no prior knowledge,
which facilitates the collection of training data. Our proposed approach benefits from distributed tracing data to
collect sequences of events that happened during spans. Extensive experiments on real datasets demonstrate that
the proposed method achieved an F_score of 0.9759. The results also reveal that in addition to the ability to detect
anomalies and release-over-release regressions, our proposed approach speeds up root cause analysis by means of
implemented visualization tools in Trace Compass.
Keywords: Performance monitoring, Anomaly detection, Tracing, Microservices, Machine learning, NLP, LSTM
Introduction the monolithic architecture, if one microservice fails the
Nowadays, computing infrastructures have evolved sig- others continue to work.
nificantly using complex systems that facilitate many These improvements have increased user expecta-
complicated and large-scale tasks in distributed and tions in a way that any performance anomaly may lead
cloud environments. The microservice architecture has to user dissatisfaction and loss of revenue. Even when
emerged as a result of this development. Microservices several services are brought down for maintenance, the
are small interconnected services that present a com- users usually do not notice it. Although significant efforts
plex service, such as a web application [1]. They provide have been made to ensure the quality of microservices,
greater scalability, making possible the distribution of an the complexity and large scale of these systems make
application over multiple physical or virtual systems. In them fragile and prone to performance anomalies and
addition, the microservice architecture improves produc- failures [2]. Further, performance monitoring and trac-
tivity by decomposing applications into smaller services ing of microservices become even more challenging as
that are easier to manage and faster to develop. Unlike the degree of automation and distribution is increased.
For example, each service can be developed using its own
language or technology while still communicating with
*Correspondence: iman.kohyarnejadfard@polymtl.ca; daniel.aloise@polymtl.ca
other services.
1 Department of Computer and Software Engineering, Polytechnique
Montreal, Montreal, Canada
Full list of author information is available at the end of the article
© The Author(s) 2022. Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which
permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the
original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or
other third party material in this article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line
to the material. If material is not included in the article’s Creative Commons licence and your intended use is not permitted by statutory
regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this
licence, visit http:// creat iveco mmons. org/ licen ses/ by/4. 0/.

Kohyarnejadfard et al. Journal of Cloud Computing (2022) 11:25 Page 2 of 16
Unlike monolithic applications in which dedicated based on detecting point anomalies and also metric-
teams work on discrete functions such as UI or database, based algorithms cannot always identify the root cause
microservices employ cross-functional teams to handle of anomalies. A single data point (event or metric) does
an application’s entire life cycle using a continuous deliv- not include enough information to determine whether an
ery model [1, 3]. Nonetheless, dynamic services make anomaly actually happened in complex systems such as
monitoring more difficult. Even if a tracer can record all microservices. Usually, an anomaly is declared when the
the execution details, it is still hard to detect the source of execution of the program has not been normal during a
the problem inside the trace files. time interval that includes many events. In real applica-
Different reasons may cause performance anomalies in tions, only a limited number of events can be the result
microservice environments [4]. Any problem in a service, of an action. Therefore, just a few of the possible events
such as a network disconnection or hard disk failure, can appear as the next events for a sequence of observed
may cause the microservice system to crash. Miscon- events [9]. In other words, similar to words in natural
figurations or extreme load by a service can also affect language processing, events as elements of a sequence
the whole system. Changes in one service may influence follow specific patterns and grammar rules. We used this
other dependent services workload, and may result in idea in our anomaly detection framework and applied a
response time degradation. Moreover, the agile nature general NLP-based strategy to distinguish normal and
of microservice environments yields multiple service abnormal patterns in a sequence of events. In addition to
updates per day, and several versions of the application locating anomalies, our proposed framework also allows
may be deployed in a short amount of time. As such, sev- analysts to zoom in the detected anomalous parts of the
eral methods may change in a new update, then affect- trace to discover the root cause of the problems.
ing the response time behavior of services and leading to The main contributions of our work can be summa-
many false alarms from monitoring tools [4, 5]. rized as follows:
The way we trace such environments and collect data is
of particular importance. A microservice-based applica- • Unlike many other methods that use OpenTracing,
tion consists of tens, hundreds, or thousands of services our anomaly detection framework employs LTTng
running across many hosts. Consequently, it is not possi- to perform distributed tracing. OpenTracing is a
ble to rely on an individual trace. In this case, distributed vendor-agnostic API to help developers easily instru-
tracing is required, thus providing a view of a request’s ment tracing into their code [10]. A trace in Open-
life as it travels across multiple nodes and services com- Tracing is a directed acyclic graph of spans, and it
municating over various protocols [6]. It also enables to provides only relationships across microservices.
follow the spans and events that occur in different nodes. In contrast, LTTng provides details of the programs
A span is the primary building block in distributed trac- execution with higher resolution by presenting ker-
ing and represents an individual unit of work done in a nel and userspace events.
distributed system. Besides, many sub-spans may be gen- • We developed a handcrafted data extraction module
erated during the spans lifetime, in which tens of user- in Trace Compass to construct the spans using the
space and kernel events occur in a particular order. The request/response events tag. Moreover, the hierar-
proposed diagnostic approach proposed here works by chical structure of these tags helps us to extract sub-
collecting sequences of events during spans using the spans. This module is also responsible for converting
Linux Trace Toolkit Next Generation (LTTng) [7], send- each span into a sequence of events.
ing them to the detection module, and eventually analyz- • Our LSTM-based model, designed for post-analysis
ing the outputs of the model in Trace Compass. LTTng of traces, learns the normal patterns of events along
provides a system software package for correlated tracing with their arguments (e.g., event type, tag, and pro-
of the Linux kernel, applications, and libraries [7]. cess name). Further, this model is trained to predict
In this paper, we propose a general framework to find the next event’s arguments in addition to the event’s
anomalies as well as release-over-release regressions in name. Learning and predicting at this granularity
microservice environments by taking advantage of NLP sets our model apart from the others found in the
and open-source tools (i.e., LTTng and Trace Compass). literature.
In general, anomaly detection and localization is the pro- • Our framework makes it possible to examine the
cess of finding patterns in data that deviate from normal system behavior from both the system and ser-
behavior [8], which is different from noise detection and vice perspectives, which gives the troubleshooter a
noise elimination that refer to unwanted noise in the data. deep understanding of what happened at the time
Anomalies in data may happen in various forms, such of an anomaly. The provided visualizations consid-
as point and collective anomalies. Methods that work erably reduce troubleshooting time by highlighting

K ohyarnejadfard et al. Journal of Cloud Computing (2022) 11:25 Page 3 of 16
the anomalous parts of the trace and directing the The earliest efforts for anomaly detection had used
debugger to the most relevant problem sites of inter- statistical methods [21] where an anomaly score was
est. Without such visualizations, manually tracking calculated using a function of abnormality to show the
the performance of systems within low-level tracing behavior of the application. In [22], CPU performance
data, possibly including thousands of events from dif- and network performance metrics in master-slave and
ferent spans, is indeed a very exhausting task. nested-container models are compared to provide a
• In addition to anomaly detection, our framework can benchmark analysis guidance for system designers. How-
be applied to identify release-over-release regres- ever, a live threshold is required given the system’s cur-
sions. Finding potential regressions from one release rent state to determine whether the program behavior is
to another is extremely valuable, and conventional normal or abnormal, which is practically impossible to
performance tests cannot reveal sufficient regres- set in real-time. Furthermore, these tools do not provide
sions. Many subtle changes in spans or sequence of any details about the application’s execution flow. Several
events signify a regression that can be captured using machine learning-based schemes have also been applied
our framework. to detect anomalies in microservice systems in addition
to statistical and metric-based methods. Hierarchical
The rest of the paper is organized as follows. In Sec- Hidden Markov Models (HHMM) are adopted in [23]
tion Previous work, related studies are presented. In to learn a model based on different monitored metrics
“Anomaly detection framework” section, we introduce such as CPU, Memory, and Network to locate anoma-
our automatic integrated anomaly detection framework lous behaviors. Besides, many clustering algorithms,
for microservice environments. “Evaluation” section pro- such as k-means, k-medoids, EM clustering, and outlier
vides the experimental results followed by the conclu- detection algorithms, have been employed for anomaly
sions in “Conclusion” section. detection in microservice environments [24–26]. The
main issue with such methods is that they are usually
Previous work difficult to interpret. Supervised methods such as SVM,
In traditional approaches, application performance man- Fuzzy Logic, and Neural Networks, which use labeled
agement (APM) tools that support various measures are data, were proposed in [27–29]. In [28], the authors used
utilized to perform resource behavior analysis on micros- a SVM to detect DoS attacks in virtualized clouds under
ervices [11]. Tracing is another robust and efficient a changing environment. In [30], a fuzzy technique was
approach for reverse engineering and debugging of com- proposed to extract abnormal patterns based on various
plex systems [12]. Many tracers across all software stack statistical metrics in which fuzzy logic rules are applied
layers, and even at the hardware level, have emerged in to classify data. However, in practice, the labeling process
the last years. Distributed tracing, unlike the most tradi- is highly complicated, or even impossible. Recently, deep
tional methods that only monitor individual components learning techniques which do not need labeled data have
of the architecture, is applied to complex distributed sys- yielded promising results. The works of [31, 32] propose
tems at the workflow level [13]. Tools like OpenCensus anomaly detection methods for large cloud infrastruc-
and OpenTracing [10] help to record the execution path tures using long short-term memory (LSTM) neural
of each microservice request. Jaeger [14], a popular tool networks [33] with data from distributed tracing technol-
that supports OpenTracing and developed by Uber, has ogies. In that work, a stacked LSTM network model was
been widely used to automatically collect and store the presented for anomaly detection in time series where the
service call data [15, 16]. Its counterpart Zipkin [17] aids network was trained on non-anomalous data. The draw-
in gathering timing data needed to troubleshoot latency back of these methods is that many details, including
problems in microservice architectures [18, 19]. How- events arguments such as event type, tag, process name,
ever, the high-level information that these tools provide and return value are ignored.
is not always sufficient to characterize the execution sta- Furthermore, researchers have made much effort to
tus of the system since they do not offer kernel events. improve anomaly detection by using different data rep-
Thus, tracing with LTTng is a fundamental part of our resentations and information resources. Tracing data and
anomaly detection framework. This open-source tool is log, as the most popular information resources, can be
implemented for achieving high throughput and includes represented in the form of an enumerated collection of
multiple modules for Linux kernel and userspace tracing, events sorted by their timestamps [34]. Different works
thereby imposing low overhead to the operating system. make different uses of this structure. In DeepLog [35],
Besides, this tool can work with a variety of environ- a deep neural network model is proposed to model an
ments, such as monolithic applications, microservices, unstructured system log as a natural language sequence.
and IoT devices [20]. In [36], by performing time-series-based forecasting,

Kohyarnejadfard et al. Journal of Cloud Computing (2022) 11:25 Page 4 of 16
Fig. 1 The architecture of our proposed anomaly detection method for microservice environments
anomalies on cyclic resource usage patterns are detected. addition, to collect labeled data related to an application,
In the sequel, graph representations of the events are a very specialized professional is needed. Conversely,
obtained from this data and employed to detect critical clustering approaches are difficult to interpret. We pro-
nodes and design anti-patterns proactively. The authors pose in this work an unsupervised method to learn nor-
of [37] designed and developed a simplified MSA applica- mal execution patterns, since collecting normal data is
tion and applied different graph algorithms, then assess- straightforward and can be done automatically without
ing their benefits in MSA analysis. In another article, any supervision. Fourthly, other deep learning-based
Tao Wang et al. [38] organized the trace information and NLP-based approaches ignore events arguments in
collected by the OpenTracing tool to characterize pro- their modeling. Event arguments such as process name,
cessing requests workflow across multiple microservice message, and event type contain beneficial details that
instances as a calling tree. The proposed approach con- increase detection quality [39]. We use these arguments
verts the given trace into the spans and detects perfor- to train our model. Then, in the prediction phase, our
mance anomalies using the model of normal key patterns. model predicts the name of the next event as well as its
Some points distinguish our work from previous related arguments. Finally, previous works from the literature,
literature. Fistly, unlike traditional approaches, that use such as DeepLog, have not presented any solution to
application performance management tools that support analyze the model’s output. However, the use of Trace
various metrics (e.g., CPU and memory utilization) to Compass in our approach enables us to develop analysis
perform resource behavior analysis on microservices, our scripts and even use many preexisting scripts and visuali-
work’s main source of information is tracing data. Com- zations to examine the model’s output more deeply.
pared to these approaches, our proposed framework is
Anomaly detection framework
not dependent on the existence of any threshold. Moreo-
ver, the metrics used by these approaches do not help to In this section, we introduce an NLP-based anomaly
find the cause of the anomaly after detecting it. Tracing detection framework for post-analysis of LTTng traces.
provides considerable details about the application’s exe- It is designed to help developers to efficiently find the
cution flow and about what exactly happened at the time root causes of abnormal behaviors in microservice
an anomaly occurred. Secondly, most previous works environments. We aim to provide a general framework
that make use of tracing data employ OpenTracing-based applicable to microservice-based applications with dif-
tools such as Jaeger or Zipkin to perform distributed ferent settings.
tracing. Nonetheless, the high-level information that Figure 1 presents the architecture of our approach
these tools provide about microservices interaction is not along with its three main modules, i.e., the tracing mod-
always sufficient to characterize the execution status of ule, the data extraction module, and the analysis module.
the system. Our proposed framework employs the LTTng We discuss this architecture in detail in the following
open-source tool, which imposes low overhead on the subsections.
operating system and presents low-level kernel and user-
space tracing. Thirdly, the main drawback of supervised Tracing module
methods is that they require labeled data. The process Tracing is an efficient way of gaining information from
of labeling data points in terms of performance status is a system for further analysis and debugging, thus mini-
highly complicated and sometimes even impossible. In mizing the monitoring influence. Distributed tracing

K ohyarnejadfard et al. Journal of Cloud Computing (2022) 11:25 Page 5 of 16
Fig. 2 The overview of our distributed tracing module
is derived from traditional tracing so as to be employed represented as an enumerated collection of events sorted
within distributed systems. Distributed tracing technolo- by their timestamps.
gies provide a view of the communication among micros- During the execution of a microservice application,
ervices [6]. Microservices mostly use Representational many tasks or spans, such as opening a web page, are per-
State Transfer (REST) as a usual way to communicate formed. In fact, a trace can be divided into a set of spans,
with other microservices. where each span consists of a sequence of events that are
We aim to provide a general anomaly detection frame- invoked in a specific order to perform the desired task. It
work that can be easily applicable for any microservice- should be noted that spans can not be directly retrieved
based application in practice and subsequently lead to using LTTng. In the sequel, we will discuss in detail how
the discovery of the cause of the identified anomalies. We to extract spans from tracing data.
have described how to analyze an application and pre-
pare its associated dataset, instead of using pre-existing Data extraction module
available datasets which do not inherently contain infor- We implemented the data extraction module within the
mation needed to extract spans and their associated Trace Compass open-source tool, which offers scripting
sequence of events. capability [40] and visualization mechanisms to pro-
As our case study, we created our dataset by tracing mote our analysis. LTTng generates a CTF (Common
a distributed software available in Ciena Corporation. Trace Format) file for every node in the microservice
Many new releases of this software are provided by the environment. The CTF format is a file format optimized
developers of this company every day. Thus, we collected for the production and analyses of big tracing data [7].
traces from different releases to compose the dataset. After generating the CTF files, Trace Compass is used
We denote the set of all traces collected from different to read these files and integrates them into trace T,
i
releases as Γ {T ,T ,...,T }, where n indicates the number where i indicates the index of this trace in Γ. The result
= 1 2 n
of collected traces. of this process is an enumerated collection of events
Figure 2 illustrates the structure of our tracing mod- sorted by their timestamps.
ule that make use of the LTTng open-source tool. As An event is composed of well-defined fields that are
presented in this figure, LTTng is deployed on each common to all events, such as name, timestamp, and
node to send the tracing data to the manager. The run- process ID. However, the delivered sequence of time-
ning LTTng-relayd daemon on the manager collects ordered events does not provide the spans that reflect
the tracing data received from the nodes. Later, Trace separate tasks. In order to extract spans and their sub-
Compass integrates the traces obtained from different spans, Γ is scanned with respect to the tag of request/
nodes to form a Trace T i ={e1 ,e2 ,...,e g(Ti) } , where g(T
i
) response events. Other events are then processed, so as
is the number of events associated to T. Actually, T is that each event is assigned to the span it belongs. In our
i i

Kohyarnejadfard et al. Journal of Cloud Computing (2022) 11:25 Page 6 of 16
Fig. 3 Illustration of the process for creating the training dataset from multiple traces
framework, events are stored by means of their asso- indicating the beginning or the end of a span, or any
ciated keys composed by the name of the event and its other operation.
arguments. Requests and responses are the two types of events we
In order to train a model which is able to detect per- consider for extracting spans. Each span starts with a
formance anomalies as well as release-over-release deg- request and ends with a response. In addition, the request
radations, a massive training dataset is required to cover and response associated with a span possess the same
as many normal patterns of keys as possible. Actually, the tag. For example, a request with tag 00 indicates the start
training data Γ correspond to entries of traces obtained of a span, whereas a response with the same tag marks
from the execution of previous stable releases of an appli- its end. Moreover, many sub-spans may be generated
cation. Figure 3 summarizes how to create such a dataset. during a span’s lifetime since a service may communicate
After collecting n different traces, each of them is pro- with other services to answer a demand. Similar to spans,
cessed, so as that all the spans associated with each trace sub-spans are created with a request and a response
are individually extracted from Γ. Next, for each span, its that share the same tag. Besides, the parent’s tag of each
sequence of events is collected and stored in S, for i 1,… sub-span is embedded into the children’s tag. For exam-
i =
,m. In our framework, each sequence S is represented by ple, 00/01 indicates a sub-span whose parent is repre-
κ1,...,κh(Si) i κk
its corresponding keys i i , where i represents sented by the 00 tag. As shown in Fig. 4, each span and
the k-th key in the sequence S, and h(S) indicates the its sub-spans form a tree. Yet, each span can be displayed
i i
length of sequence S. as a sequence of requests and responses sorted by their
i
timestamp. In the example of Fig. 4, this sequence would
be S {Req,Req,Resp,Req,Resp,Resp}.
=
Extracting spans
In the following, we describe how spans are extracted Construction of sequences of keys
from an LTTng trace. LTTng uses tracepoints designed In addition to requests and responses, many other
to hook mechanisms that can be activated at runtime userspace and kernel events happen during each span.
to record information about a program execution. Tra- After collecting all spans, all events in Γ are processed,
cepoints are placed inside the code by developers or and assigned to the span to which they belong. The
debuggers to extract useful information without the appropriate span for each event is found by compar-
need of knowing the code in-depth. Hence, one can ing the event’s arguments (e.g., TID and PID) with the
expect to encounter different event types in trace data, arguments of the events that have been assigned to the

K ohyarnejadfard et al. Journal of Cloud Computing (2022) 11:25 Page 7 of 16
Fig. 4 The structure of a span and its sub-spans in a distributed trace
spans. Once the appropriated span is identified, the name, message, and event type contain important
event is placed in the sequence according to its times- information to increase detection quality.
tamp. In the example of Fig. 4, if an event happens The scope of this work is limited to the arguments that
right after the first request, the resulting sequence are common to all events. In our experimental traces,
becomes S {Req,Event,Req,Resp,Req,Resp,Resp}. This event name, process name (Procname), Thread ID (TID),
=
process is repeated for all events so that a set contain- Process ID (PID), timestamp, message, and event type
ing all sequences is obtained, where each sequence are present in most of the events. We divided the events
refers to a span. into two categories: 1) requests/responses, and 2) other
The previous paragraph explained how sequences are events. Table 1 lists the arguments we selected for each
extracted from a trace. Now, we explain how the argu- category of events. The key for requests and responses is
ments of events are used. Whenever a specific trace- created using the name, type, tag, and procname argu-
point is encountered at runtime, an event is produced ments. Event type specifies whether the event is a request
with its arguments such as a name, timestamp, and or a response, and tag specifies the span or sub-span to
possibly many others. Event arguments such as process which the event belongs. The second category of general

Kohyarnejadfard et al. Journal of Cloud Computing           (2022) 11:25  Page 8 of 16
Table 1 The categories of events and the arguments used by  probable keys at the moment t according to the previ-
our framework ously observed sequences of keys. Later in the detection
Event category Argument Type phase, the model determines which events in a sequence
do not conform to normal patterns.
| Request/Response |     | Event name |     | string |              |     |               |            |     |          |          |
| ---------------- | --- | ---------- | --- | ------ | ------------ | --- | ------------- | ---------- | --- | -------- | -------- |
|                  |     |            |     |        | We  modeled  |     | the  anomaly  | detection  |     | problem  | on  our  |
|                  |     | Event type |     | string |              |     |               |            |     |          |          |
sequences of keys as a multi-class classification problem for
Tag string which the input length α is fixed. Remark that the sequences
|     |     | Procname |     | string |     |     |     |     |     |     |     |
| --- | --- | -------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
obtained by the data extraction module are of different
Others Event name string lengths.  Multiple  sub-sequences  of  fixed  size  are  hence
|     |     | Procname |     | string |     |     |     |     |     |     |     |
| --- | --- | -------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
obtained by considering a window of size α over the larger
|     |     | Message |     | string |     |     |     |     |     |     |     |
| --- | --- | ------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
sequences. It should be noted that sequences smaller than α
are very rare in our dataset. These small sequences are
related to light operations that are often not prone to perfor-
mance anomalies. Consequently, they are simply ignored by
| events  uses                                             | the  event  | name,  procname,  | and  | message  |                            |     |     |                  |                              |     |     |
| -------------------------------------------------------- | ----------- | ----------------- | ---- | -------- | -------------------------- | --- | --- | ---------------- | ---------------------------- | --- | --- |
|                                                          |             |                   |      |          | the analysis module. Let V |     |     | {v 1 ,v 2 ,...,v | d } be the set of all possi- |     |     |
| arguments to compose the keys. Thus, the resulting keys  |             |                   |      |          |                            |     |     | =                |                              |     |     |
ble unique keys, where each key v defines a class. From a
are all textual strings, and V {v ,v ,...,v } denotes the set  i
= 1 2 d sequence of size h(S), h(S) α subsequences are analyzed.
|     |     |     |     |     |     |     | i   | i−  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
of all possible unique keys.
Thus, for each sequence S, the input of the model is denoted
Although simple, extending our framework to a new  j j,κ (j+1) (j+iα−1)
|               |                   |                       |                      |                  | by X =κ   |              | ,...,κ |  and the output is expressed            |     |     |     |
| ------------- | ----------------- | --------------------- | -------------------- | ---------------- | --------- | ------------ | ------ | --------------------------------------- | --- | --- | --- |
|               |                   |                       |                      |                  | j i       | (j+α) i i    | i      |                                         |     |     |     |
| a r g u m e n | t  m a y  r e q u | i r e   a   m u c h   | la r g e r  d a t as | e t  d e p e n d | - by Y =κ |              |        |                                         |     |     |     |
|               |                   |                       |                      |                  | i         | i  , where j |        | 1,...,h(S i ) α. Sequences represent a  |     |     |     |
i n g   o n   th e  n u m b e r   o f   v a l ue s   th a t  a r g u m e n t  m a y   h a v e .  ∈ −
part of a task’s execution path in which keys happen in a par-
To illustrate, let us suppose we use only one argument to  j j
|     |     |     |     |     | ticular order. Hence, for each X |     |     |  , Y  can only take a few of the  |     |     |     |
| --- | --- | --- | --- | --- | -------------------------------- | --- | --- | --------------------------------- | --- | --- | --- |
|     |     |     |     |     |                                  |     |     | i i                               |     |     |     |
create keys, and that this argument has β  different val- d possible keys from V and is dependent on the sequence X j
|     |     |     | 1   |     |     |     |     |     |     |     | i   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ues. In this case, only β  unique keys are created (d β ).  j
1 = 1 that appeared before Y  . In other words, the input of the
i
| If another argument with β |     | 2  different values is then used,  |     |     |     |     |     |     |     |     |     |
| -------------------------- | --- | ---------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
model is a sequence of α recent keys, and the output is a
| β β  unique keys are obtained (d |     |     | β β ). Thus, each  |     |     |     |     |     |     |     |     |
| -------------------------------- | --- | --- | ------------------ | --- | --- | --- | --- | --- | --- | --- | --- |
1× 2 = 1× 2 probability distribution over the d keys from V, expressing
time a new argument with β different values is consid-
i the probability that the following key in the sequence is v V.
r∈
ered, the number of unique keys increases β times.
|     |     |     | i   |     | Eventually, a model of the conditional probability distribu- |     |      |           |         |     |       |
| --- | --- | --- | --- | --- | ------------------------------------------------------------ | --- | ---- | --------- | ------- | --- | ----- |
|     |     |     |     |     |                                                              | j+α |      | j,κ (j+1) | (j+α−1) |     |       |
|     |     |     |     |     | Prob(κ                                                       |     | =v | | κ ,...,κ  |         | ),v | ∈V    |
|     |     |     |     |     | tion                                                         | i   | r    | i i       | i       |     | r is  |
Analysis module
made after the training. Figure 5 shows an overview of the
In microservice environments such as our experimental
described anomaly detection model.
application, events are expected to occur in a particular  An LSTM network is employed to learn the probabil-
order. Actually, the keys in the sequences obtained by  ity distribution Prob(κ j+α =v | κ j,κ (j+1) ,...,κ (j+α−1) )
|     |     |     |     |     |     |     |     | i r (cid:31) | i i | i   | (cid:30)   |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | --- | ---------- |
the data extraction module must follow specific patterns
|     |     |     |     |     | that  maximizes  |     | the  | probability  | of  | the  | training  |
| --- | --- | --- | --- | --- | ---------------- | --- | ---- | ------------ | --- | ---- | --------- |
and grammar rules similar to the ones found in natural
sequences. The architecture of this LSTM network is
languages. Hence, only a few possible keys can appear as
shown in Fig. 6. Each layer contains α LSTM blocks,
the next key in a sequence following a specific set of keys.
where each block processes a key of the input sequence.
The training dataset in our experiments includes normal
sequences of keys obtained from previous stable releases  LSTM blocks have a cell state vector C and a hidden
vector H. Both values are moved to the next block to
o f  t h e  a p p li c at i o n.  I n   t h is  s e c ti o n ,  w e   r e v i e w  t h e  m a c h in e   q q−1
|     |     |     |     |     | initialize its state. The values of input  |     |     |     | κ   |  and H |  , for  |
| --- | --- | --- | --- | --- | ------------------------------------------ | --- | --- | --- | --- | ------ | ------- |
le a r n in g   m o d e l  w e   h a v e  p r o p o s e d  t o   d i s t in g u is h  n o r m a l  i i
|                                                      |     |     |     |     | q {j,j 1,...,j | α   | 1}, determine how the current input  |     |     |     |     |
| ---------------------------------------------------- | --- | --- | --- | --- | -------------- | --- | ------------------------------------ | --- | --- | --- | --- |
| patterns from abnormal ones. We adopted an LSTM net- |     |     |     |     | ∈ +            | +   | −                                    |     |     |     |     |
and the previous output affect that state. They indicate
| work to model this sequence to word problem given its  |     |     |     |     |     |     | q−1 |     |     |     |     |
| ------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ch of C
success for modeling text prediction and other similar  how mu i  (the previous cell state) holds in the
state C q
i . They also influence the construction of the
natural language processing tasks. This model learns the
Fig. 5 The overview of our anomaly detection model

K ohyarnejadfard et al. Journal of Cloud Computing (2022) 11:25 Page 9 of 16
Fig. 6 The architecture of the LSTM network we used in our anomaly detection framework
q
output H i . Our deep LSTM neural network architec- analyzes some practical use-cases and examines the
ture includes two hidden layers in which the hidden success of our framework in locating the anomalies we
state of the previous layer is used as the input of each injected into the system through various simulated sce-
corresponding LSTM block in the next layer. narios. Finally, in “Root cause analysis” subsection, we
During training, appropriate weights are assigned to input explain how the scripting feature of Trace Compass as
so that the final output of the LSTM provides the desired key. well as different views can assist experts to find the root
The categorical cross-entropy loss function [41] is used as the cause of anomalies.
loss function for the designed multi-classification task. Then,
Experimental setup and dataset generation
a standard multinomial logistic function is applied to trans-
late the last hidden state into the probability distribution We deployed the target microservice environment
Prob(κ
i
j+α =v
r
|
(cid:31)
κ
i
j,κ
i
(j+1) ,...,κ
i
(j+α−1)
(cid:30)
,v
r
∈V)
.
(developed by Ciena Co.) on a virtualized platform
with two nodes, each equipped with two cores Intel
In the detection phase, the trained model is used to ana-
Core Processor (Broadwell, IBRS), and 4 Gb of RAM.
lyze unseen tracing data. This trace can be obtained from
An Oracle Linux server was installed on both nodes.
an old or a new release of the software. Like what was done
Moreover, LTTng was employed on each of them to
to collect the training data, spans are extracted and then
send the tracing data to the manager. The manager
converted into sequences of different lengths. Therefore,
VM benefits from the LTTng-relayd daemon, which
from a sequence of size h(S), h(S) α subsequences are
i i − is responsible for receiving trace data from remote
obtained, and h(S) α probability distributions are pre-
i − LTTng daemons.
dicted. The model predicts the probablity distribution
Prob(𝜅 i j+𝛼 { 𝜅 i j,𝜅 i (j+1),...,𝜅 i (j+𝛼−1) } )= { v 1 ∶p 1 ,v 2 ∶p 2 ,...,v d ∶p d} , tio I n n o o r f d 5 e r t o t o 1 c 0 r e m a i t n e u t t h e e s t w ra e i r n e i n o g b d ta a i t n a e , d 1 2 f r t o r m ac e t s h w e i p th re d v u io r u a s -
where p| j describes the j + p α robability of v j to appear as the stable releases of the studied software. After removing
κ
next key value. Then, i is marked as an u j n + e α xpected key incomplete spans, a total of 61709 spans were extracted.
κ
if the probability of the real seen value of i is less than The dictionary of unique keys collected from the training
the confidence threshold of 0.5. data contains 4028 unique keys.
Our data collection module has been implemented
Evaluation
using python and the Trace Compass Scripting feature
In the following, we evaluate the proposed technique by [40]. Furthermore, we employed PyTorch to implement
analyzing a microservice-based application. First, the the LSTM network1. Finally, the model was trained on a
experimental setup and dataset generation are explained server with two Intel(R) Xeon(R) Bronze 3104 1.70GHz
in “Experimental setup and dataset generation” sub- CPUs and NVIDIA TITAN V graphic cards.
section. Then, in “Evaluation of the anomaly detection
framework” subsection, we evaluate the performance of
1 The implementations of the data collection module and the detection mod-
our model. “Analysis of practical use-cases” subsection
ule are available in https:// github. com/ kohyar/ LTTng_ LSTM_ Anoma ly_ Detec
tion.

Kohyarnejadfard et al. Journal of Cloud Computing (2022) 11:25 Page 10 of 16
Evaluation of the anomaly detection framework
α {8,9,..,30}. The smallest possible α value is 8 since that
∈
As mentioned earlier, the analysis module models the corresponds to the minimum sequence length in the
anomaly detection problem on the sequences of keys as training data. Figure 7(A) shows that for α values greater
a multi-class classification problem. Our training dataset than 19, the F_score of the model begins to decrease.
is composed of the sequences obtained from 12 previous We omitted the results for 23 α 30 to make the figure
≤ ≤
stable releases of the studied software. A total of 61709 clearer. Figure 7(B) presents the F_score/training time for
spans were extracted from these 12 traces and approxi- the best found α values. According to the results, α 17
=
mately 5 million training sequences were obtained from achieves the best classification results in terms of training
the spans. In addition, the dictionary of unique keys col- time and F_score. This value is therefore selected for the
lected from the training sequences contains 4028 unique remaining of our experiments.
keys. Thus, there exist 4028 different classes in the train- After selecting the hyperparameter α, we evaluated the
ing dataset, each one associated to a key. quality of our model through 10-fold cross-validation.
We employed multi-class evaluation metrics to evalu- In 10-fold cross-validation, the dataset is divided into
ate the quality of our model. Accuracy is usually the first ten subsets of approximately equal size. One of the sub-
option to evaluate multi-class classification models on sets is reserved for testing, while the remaining subsets
a biased dataset. However, the dataset obtained in this are used for training. This process is repeated 10 times,
work is not balanced. Hence, we used precision, recall, and the results are averaged over each one of 10 differ-
and F_score instead, which are better suited for unbal- ent tested subsets. Results of evaluating our model with
anced datasets. Precision quantifies the number of posi- 10-fold cross-validation are listed in Table 2. Our pro-
tive class predictions that actually belong to the positive posed method demonstrates excellent performance with
class. Recall measures the number of positive class pre- a F_score of 0.9759. It should be noted that our dataset
dictions that have been made out of all positive examples contains approximately 5 million sequences and 4 thou-
in the dataset. Finally, the F_score can be interpreted as a sand unique keys.
harmonic mean of the precision and recall metrics. How-
ever, the computation of these metrics for a multi-class Analysis of practical use‑cases
problem is different from a binary one. In multi-class In this subsection, a newer release of the application was
classification, these metrics are obtained for each class investigated to evaluate the model on detecting possible
separately. The overall precision, recall and F_score for all performance degradations and anomalies. For this pur-
classes are then computed by averaging precision i , recall i , pose, we examined three different scenarios. In the first
and F_score i for the set of classes C i , where i = 1,…,4028. scenario, the regular execution of the application, i.e.,
For an individual class C i , the values of precision i , recall i , without any anomaly injection, was analyzed to deter-
and F_score i are computed as follows [21]: mine where and why the new release did not follow the
precision = TPi normal patterns learned by the model. In the other two
i TPi+FPi (1) scenarios, we investigated the performance vulnerability
of the new release when an external factor disrupts fair
access to system resources. To simulate such attacks, a
recall = TPi significant CPU load on the multi-core nodes was gener-
i TPi+FNi (2)
ated as the second scenario by continuously compressing
and decompressing a stream of random data (zip bombs).
Finally, in the third scenario, disk stress was injected into
F_score i = 2× pr p e r c e i c s i i s o i n o i n + i× re r c e a c l a li lli (3) the nodes by creating a file and then using a loop to copy
it repeatedly.
In order to create the final model, the hyperparameters After collecting the tracing data for each of the men-
must be tuned. As previously explained, the sequences tioned scenarios, the data collection module extracted the
obtained from the spans have different lengths, but the spans from these tracing files and created the sequences
input length of the model is fixed as α. Therefore h(S) α of keys. For all input subsequences, the model determines
i −
sub-sequences can be obtained by taking a window of size whether the key that appeared in the sequence right after
α over a sequence of size h(S). The value of this hyper- the input subsequence is probable to happen or not. The
i
parameter affects both the training time and the perfor- model marks that key as an unexpected key if it predicts
mance of the model. So, we tried to choose a value for α that the probability of that key in the sequence is lower
that would lead to a highly effective model in a reasonable than the confidence threshold of 0.5.
training time. For this purpose, we measured the f_score Table 3 reports the number of detected unexpected
and training time of the obtained models by selecting keys along with the total number of predictions made by

K ohyarnejadfard et al. Journal of Cloud Computing           (2022) 11:25  Page 11 of 16
Fig. 7 A F_score of the model by varying α. The dotted line indicates that the F_score of the model for α values between 11 and 19 is greater than
0.97. B F_score/Training time for different values of α. Only the values for which the F_score is greater than 0.97 are shown in this figure
Table 2 Results of evaluating our model with 10-fold cross-  Table 3 The number of detected unexpected keys along with
validation the total number of predictions made by our model for the three
scenarios
Precision 0.9774
|     | Number of detected  |     | Number of  |
| --- | ------------------- | --- | ---------- |
Recall 0.9760
|     | unexpected keys |     | predictions |
| --- | --------------- | --- | ----------- |
F_score 0.9759
| Test data (Scenario 1) | 32043 |     | 518503 |
| ---------------------- | ----- | --- | ------ |
| Test data (Scenario 2) | 65507 |     | 489593 |
our model for three scenarios. As expected, the number  Test data (Scenario 3) 66978 453781
of detected unexpected keys in the first scenario is less
than in the other two other scenarios, where CPU and
disk stress were injected into the system. The injected
| Our  proposed  | framework,  | however,  | does  not  sig- |
| -------------- | ----------- | --------- | --------------- |
load in the second and third scenarios has made the  nal keys as anomalous as soon as an unexpected key is
application behave much differently. The first scenario  detected. It also takes into consideration the frequency
reveals how the changes applied to the application by  of unexpected keys over the monitored period of time.
developers in a newer release may affect the execution’s  Once a high frequency of unexpected keys is identi-
path of the application.
| fied,  that  sequence  | of  keys  | is  highlighted  | for  further  |
| ---------------------- | --------- | ---------------- | ------------- |

Kohyarnejadfard et al. Journal of Cloud Computing (2022) 11:25 Page 12 of 16
Fig. 8 This Figure depicts the Likelihood of detecting unexpected keys over the traces obtained from the three mentioned scenarios. A In this
scenario, CPU-related anomalies were injected into the system. B In this scenario, disk-related anomalies were injected into the system. C In this
scenario, a new release of the application without injecting anomaly was investigated

K ohyarnejadfard et al. Journal of Cloud Computing (2022) 11:25 Page 13 of 16
investigation by developers or system experts. This is being correctly discovered by our framework. Figure 8(c)
intended to reduce troubleshooting time, as the develop- includes a smaller number of peaks with lower heights.
ers can examine few specific intervals instead of looking The observed peaks indicate the moments in which the
at large amounts of tracing data, which might include new release did not follow the normal behavior of the
thousands of system events. As we show next, the out- previous ones.
put of the model can be examined from two different
perspectives. Service‑based anomaly detection
In service-based anomaly detection, we detect anoma-
System‑based anomaly detection lous spans. Unlike system-based anomaly detection, in
In system-based anomaly detection, the entire execution which we examine the entire execution, service-based
is examined regardless of the span to which each unex- anomaly detection identifies spans with a high rate of
pected key belongs. To illustrate, let us consider traces of unexpected keys. The rate of unexpected keys for each
5 minutes divided into small time intervals of 1 second. span correspond to the rate of unexpected keys in the
The chart displayed in Fig. 8 shows the rate of detecting sequence associated with that span.
unexpected keys, i.e., number of detected unexpected A span for which the rate of unexpected keys is
keys divided by the total amount of predictions, com- greater than 0.5 is marked as an anomalous span. The
puted in each of the monitored intervals for the three chart of Fig. 9 depicts the anomalous spans detected
tested scenarios. They reveal the intervals in which more by our framework during the test trace obtained from
unexpected keys have detected, and are hence, more the second scenario. Spans are numbered according to
likely to represent anomalies. This view helps develop- their start time and are shown with a red bar. In Fig. 9,
ers to focus only on the areas prone to anomalies. The the x-axis shows the spans index and the y-axis indi-
peaks in Figs. 8(a) and 8(b) correspond exactly to the cates the rate of unexpected keys. From this figure, we
moments the anomalies were injected into the system, observe that many anomalous spans have been detected
Fig. 9 The anomalous spans that appeared during the trace of the second scenario where each span has been drawn with a bar

Kohyarnejadfard et al. Journal of Cloud Computing (2022) 11:25 Page 14 of 16
Fig. 10 This figure presents the time chart generated by our script in Trace Compass, which helped to find the cause of anomalies in our test traces
(due to Ciena’s security rules, we have changed the original names of the processes in these screenshots). A A sample of a normal span. B A sample
of an anomalous span where the PROC-X is the caused of the problem
when anomalies were injected in the system. This view particular areas. Furthermore, the time axis in this time
enables developers to filter a trace based on the anoma- chart is aligned with other views and tables that sup-
lous spans tag, that merits further investigation. port automatic time axis alignment, such as the editor
view that presents the events in a tabular format, or the
statistics view that displays the various event counters.
Root cause analysis More detailed data can be computed from the trace as
Using Trace Compass in our framework provides the the user zooms in the time chart or filters events in the
developers an in-depth perception of what happens editor table.
during a trace, especially in the presence of anomalies. Figure 10(a) shows the structure of a sample normal
Trace Compass is already used by many companies in span. In Fig. 10(b), the trace was filtered based on the
the field of performance analysis. We have converted tag of one of the anomalous spans. Interestingly, the
the output of our anomaly detection model to Goog- provided Trace Compass script could successfully find
le’s Trace Event format to be able to investigate the the cause of a latency issue in the target application that
root causes of the identified anomalies. Our output has been detected by our anomaly detection model,
in this format contains a set of events, each of which then pointing out to the process that caused this prob-
equivalent to an event in the original trace. However, lem. This process was present in many other abnormal
three new fields have been added to each event. Field spans as well. These results demonstrate the effective-
category determines whether the event is identified as ness of our proposed framework in locating anomalies
unexpected. In addition, each event keeps the tag of and finding their root causes.
the span in which it is located, and finally, another field
Conclusion
shows if the related span is abnormal or not.
To understand the cause of the anomalies in the intro- In recent years, advances in technology and comput-
duced test traces, we provided a script that separates ing power have led to the emergence of complex and
all the processes in the trace thereby displaying them large-scale software architectures like microservices and
with different colors in a time chart like illustrated in IoT devices that speed up different tasks. Despite all the
Fig. 10. This time chart can be zoomed in and out in advantages of these systems, several factors, such as their

K ohyarnejadfard et al. Journal of Cloud Computing (2022) 11:25 Page 15 of 16
distribution in the network, the use of different technolo- Declarations
gies, their short life, software bugs, hardware failures,
Ethics approval and consent to participate
and resource contentions, make them prone to the rise Not applicable.
of anomalous system behaviors. Besides, available per-
Consent for publication
formance monitoring and analysis tools have many short-
Not applicable.
comings. In this research, a general-purpose NLP-based
anomaly detection framework was presented for detect- Competing interests
The authors declare that they have no competing interests.
ing abnormal behaviors and release-over-release regres-
sions in microservice environments. Author details
The proposed framework is based on recording 1 Department of Computer and Software Engineering, Polytechnique Mon-
treal, Montreal, Canada. 2 Ciena Inc., Ottawa, Canada.
streams of events in the tracing module, sending them
to the data extraction module so as to create sequences Received: 17 March 2022 Accepted: 13 July 2022
of keys, which are finally analysed using a deep LSTM
model. This framework is general enough to work with
any application since it benefits from an all-purpose
open-source distributed tracing tool to collect event References
1 Thönes J (2015) Microservices. IEEE Softw 32(1):116–116.
sequences. Notably, our framework learns a represen-
2 Gan Y, Zhang Y, Hu K, Cheng D, He Y, Pancholi M, Delimitrou C (2019) Seer:
tation of the event names along with other arguments Leveraging big data to navigate the complexity of performance debug-
to remedy the limitations of other methods. In addi- ging in cloud microservices. In: Proceedings of the Twenty-fourth Interna-
tional Conference on Architectural Support for Programming Languages
tion, the whole system needs no prior knowledge which
and Operating Systems. Association for Computing Machinery, New York,
facilitates the collection of training data. pp 19–33. https:// doi. org/ 10. 1145/ 32978 58. 33040 04
Extensive experiments on real datasets confirm the 3 Jamshidi P, Pahl C, Mendonça NC, Lewis J, Tilkov S (2018) Microservices:
The journey so far and challenges ahead. IEEE Softw 35(3):24–35.
effectiveness of our framework in detecting abnormal
4 Wu L, Tordsson J, Elmroth E, Kao O (2020) Microrca: Root cause localiza-
behaviours in microservice environments. Our frame- tion of performance issues in microservices. In: NOMS 2020-2020 IEEE/
work is also projected to help in the root cause analy- IFIP Network Operations and Management Symposium. IEEE, pp 1–9.
https:// doi. org/ 10. 1109/ NOMS4 7738. 2020. 91103 53
sis of system issues, which can be performed through
5 Solé M, Muntés-Mulero V, Rana AI, Estrada G (2017) Survey on models
various plots and scripts that we have provided in and techniques for root-cause analysis. arXiv preprint arXiv:1701.08546.
Trace Compass. In addition, the proposed framework 6 Erlingsson Ú., Peinado M, Peter S, Budiu M, Mainar-Ruiz G (2012) Fay:
Extensible distributed tracing from kernels to clusters. ACM Trans Comput
is easy to deploy and use in practice since no particu-
Syst (TOCS) 30(4):1–35.
lar assumptions and settings are considered in the data 7 Desnoyers M, Dagenais MR (2006) The lttng tracer: A low impact
collection. Taken together, these findings suggest that performance and behavior monitor for gnu/linux. OLS (Ottawa Linux
Symposium), vol 2006. Linux Symposium, Citeseer, pp 209–224
our framework is an effective tool to reduce trouble-
8 Chandola V, Banerjee A, Kumar V (2009) Anomaly detection: A survey.
shooting time by directing the developer to the most ACM Comput Surv (CSUR) 41(3):1–58.
relevant problem sites of interest. 9 Ohlsson J (2018) Anomaly detection in microservice infrastructures.
10 OpenTracingVendor-neutral APIs and instrumentation for distributed
In the future, we will examine the impact of employ-
tracing. https:// opent racing. io/. Accessed 09 Apr 2021.
ing kernel tracing on the proposed approach. We will 11 Ravichandiran R, Bannazadeh H, Leon-Garcia A (2018) Anomaly detection
also extend this work to use other events arguments. using resource behaviour analysis for autoscaling systems. In: 2018 4th
IEEE Conference on Network Softwarization and Workshops (NetSoft).
Finally, it would be interesting to investigate other NLP
IEEE, pp 192–196. https:// doi. org/ 10. 1109/ NETSO FT. 2018. 84600 25
techniques to improve detection performance. 12 Ibidunmoye O, Hernández-Rodriguez F, Elmroth E (2015) Performance anomaly
detection and bottleneck identification. ACM Comput Surv (CSUR) 48(1):1–35.
Acknowledgements
13 Shkuro Y (2019) Mastering Distributed Tracing: Analyzing Performance in
We would like to gratefully acknowledge the Natural Sciences and Engineer-
Microservices and Complex Systems. Packt Publishing Ltd.
ing Research Council of Canada (NSERC), Ciena, Ericsson, and EffciOS for
14 JaegerOpen source, end-to-end distributed tracing. Uber Technologies.
funding this project.
https:// www. jaege rtrac ing. io/. Accessed 10 Apr 2021.
15 Meng L, Ji F, Sun Y, Wang T (2021) Detecting anomalies in microservices
Authors’ contributions
with execution trace comparison. Futur Gener Comput Syst 116:291–301.
Iman Kohyarnejadfard put forward the main ideas and drafted the manuscript.
16 Gan Y, Liang M, Dev S, Lo D, Delimitrou C (2021) Sage: Using unsuper-
Daniel Aloise guided the research and reviewed and edited the manuscript.
vised learning for scalable performance debugging in microservices.
Other authors participated in the discussion and provided suggestions for the
arXiv preprint arXiv:2101.00267.
article. The authors read and approved the final manuscript.
17 ZipkinA distributed tracing system. https:// zipkin. io/. Accessed 10 Apr 2021.
18 Nedelkoski S, Cardoso J, Kao O (2019) Anomaly detection from system
Funding
tracing data using multimodal deep learning. 2019 IEEE 12th Interna-
This work is funded by Natural Sciences and Engineering Research Council of
tional Conference on Cloud Computing (CLOUD). IEEE., pp 179–186.
Canada (NSERC), Ciena, Ericsson, and EfficiOS.
https:// doi. org/ 10. 1109/ CLOUD. 2019. 00038
19 Wang T, Zhang W, Xu J, Gu Z (2020) Workflow-aware automatic fault
Availability of data and materials
diagnosis for microservice-based applications with statistics. IEEE Trans
The data and materials are available from the corresponding author on
Netw Serv Manag 17(4):2350–2363.
reasonable request.

Kohyarnejadfard et al. Journal of Cloud Computing (2022) 11:25 Page 16 of 16
20 Gassais R, Ezzati-Jivan N, Fernandez JM, Aloise D, Dagenais MR (2020) 40 tracecompass-ease-scripting. https:// archi ve. eclip se. org/ trace compa ss.
Multi-level host-based intrusion detection system for internet of things. J incub ator/ doc/. Accessed 10 May 2021.
Cloud Comput 9(1):1–16. 41 Zhang Z, Sabuncu MR (2018) Generalized cross entropy loss for training
21 Patcha A, Park J-M (2007) An overview of anomaly detection tech- deep neural networks with noisy labels. In: Bengio S, Wallach H, Laro-
niques: Existing solutions and latest technological trends. Comput Netw chelle H, Grauman K, Cesa-Bianchi N, Garnett R (eds) 32nd Conference on
51(12):3448–3470. Neural Information Processing Systems (NeurIPS). Curran Associates, Inc.
22 Amaral M, Polo J, Carrera D, Mohomed I, Unuvar M, Steinder M (2015) https:// proce edings. neuri ps. cc/ paper/ 2018/ file/ f2925 f97bc 13ad2 852a7
Performance evaluation of microservices architectures using containers a5518 02fee a0- Paper. pdf
In: 2015 IEEE 14th International Symposium on Network Computing and
Applications, 27–34. IEEE.
Publisher’s Note
23 Samir A, Pahl C (2019) Dla: Detecting and localizing anomalies in
containerized microservice architectures using markov models In: 2019 Springer Nature remains neutral with regard to jurisdictional claims in pub-
7th International Conference on Future Internet of Things and Cloud lished maps and institutional affiliations.
(FiCloud), 205–213. IEEE. https:// doi. org/ 10. 1109/ FiClo ud. 2019. 00036
24 Syarif I, Prugel-Bennett A, Wills G (2012) Data mining approaches for
network intrusion detection: from dimensionality reduction to misuse
and anomaly detection. J Inf Technol Rev 3(2):70–83.
25 Ranjan R, Sahoo G (2014) A new clustering approach for anomaly intru-
sion detection. arXiv preprint arXiv:1404.2772.
26 Animesh P, Jung M (2007) Network anomaly detection with incomplete
audit data. Computer Networks 51(13):3935–55.
27 Kaur N, et al (2013) Survey paper on data mining techniques of intrusion
detection. Int J Sci Eng Technol Res 2(4):799–804.
28 Abusitta A, Bellaiche M, Dagenais M (2018) An svm-based framework for
detecting dos attacks in virtualized clouds under changing environment.
J Cloud Comput 7(1):1–18.
29 Elrawy MF, Awad AI, Hamed HF (2018) Intrusion detection systems for
iot-based smart environments: a survey. J Cloud Comput 7(1):1–20.
30 Agrawal S, Agrawal J (2015) Survey on anomaly detection using data
mining techniques. Procedia Comput Sci 60:708–713.
31 Nedelkoski S, Cardoso J, Kao O (2019) Anomaly detection from system
tracing data using multimodal deep learning In: 2019 IEEE 12th Interna-
tional Conference on Cloud Computing (CLOUD), 179–186. IEEE. https://
doi. org/ 10. 1109/ CLOUD. 2019. 00038
32 Ji S, Wu W, Pu Y (2020) Multi-indicators prediction in microservice using
granger causality test and attention lstm In: 2020 IEEE World Congress on
Services (SERVICES), 77–82. IEEE. https:// doi. org/ 10. 1109/ SERVI CES48 979.
2020. 00030
33 Malhotra P, Vig L, Shroff G, Agarwal P (2015) Long short term memory
networks for anomaly detection in time series In: Proceedings, vol. 89,
89–94. Presses universitaires de Louvain.
34 Laptev N, Amizadeh S, Flint I (2015) Generic and scalable framework
for automated time-series anomaly detection. In: Proceedings of the
21th ACM SIGKDD International Conference on Knowledge Discovery
and Data Mining. Association for Computing Machinery, New York, pp
1939–1947. https:// doi. org/ 10. 1145/ 27832 58. 27886 11
35 Du M, Li F, Zheng G, Srikumar V (2017) Deeplog: Anomaly detection and
diagnosis from system logs through deep learning. In: Proceedings of
the 2017 ACM SIGSAC Conference on Computer and Communications
Security. Association for Computing Machinery, New York, pp 1285–1298.
https:// doi. org/ 10. 1145/ 31339 56. 31340 15
36 Ravichandiran R, Bannazadeh H, Leon-Garcia A (2018) Anomaly detection
using resource behaviour analysis for autoscaling systems In: 2018 4th
IEEE Conference on Network Softwarization and Workshops (NetSoft),
192–196. IEEE. https:// doi. org/ 10. 1109/ NETSO FT. 2018. 84600 25
37 Gaidels E, Kirikova M (2020) Service dependency graph analysis in micros-
ervice architecture In: International Conference on Business Informatics
Research, 128–139. Springer.
38 Wang T, Zhang W, Xu J, Gu Z (2020) Workflow-aware automatic fault
diagnosis for microservice-based applications with statistics. IEEE Trans
Netw Serv Manag 17(4):2350–2363.
39 Fournier Q, Aloise D, Azhari SV, Tetreault F (2021) On improving deep
learning trace analysis with system call arguments In: 2021 IEEE/ACM
18th International Conference on Mining Software Repositories (MSR),
120–130. https:// doi. org/ 10. 1109/ MSR52 588. 2021. 00025.