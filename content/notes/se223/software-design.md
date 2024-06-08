---
title: 'Software Design'
draft: false
type: 'page'
toc: true
mathjax: true
---

---

## Introduction

The design process behind software engineering is all about making structural decision and it's the step that defines the **software architecture**.

The main goals of this phase are:

- To support the trade-off analysis through reasoning-enabling structures
- To enable concurrent development
- To separate responsibilities
- To increase the understandability of the solution

This phase in the software development life cycle produces the so called **Design Document**.

### What is a software architecture?

The software architecture of a system is the set of structures needed to reason about the system. These structures include:

- Software elements
- Relations of software elements
- Properties of software elements and the relationships among them

The software architecture of a system is also a tool that engineers use to reason about the system itself.

The structures we can find in software architectures are:

- Component and connector structures
- Module structures
- Allocation structures

#### Component and connector structures

They describe how the system is structured as a set of elements that have runtime behaviour (*components*) and interactions (*connectors*).

Components are the principal units of computation; some examples are:

- Clients
- Servers
- Services

Connectors are the communication means of the components; some examples are:

- Request-response mechanisms
- Pipes
- Asynchronous messages

An example of component and connector structure comes from the Chromium documentation:

![](../images/Pasted%20image%2020231206170554.png)

Component and connector structures allow us to answer questions such as:

- What are the major executing components and how do they interact at runtime?
- What are the major shared data stores?
- Which parts of the system are replicated?
- How does data progress through the system?
- Which parts of the system can run in parallel?
- How does the structure of the system evolve during execution?

These structures also allow us to study runtime properties such as availability and performance.

We can use both component and sequence diagrams in UML to represent component and connector structures:

![](../images/Pasted%20image%2020231206170830.png)

![](../images/Pasted%20image%2020231206170840.png)

#### Module structures

Module structures show how a system is structured as a set of code or data units that have to be procured or constructed, together with their relations.

Some examples of modules are:

- Packages
- Classes
- Functions
- Libraries
- Layers
- Database tables

Modules constitute the implementation units that can be used as the basis for work splitting.

Typical relations among modules are:

- Uses
- Is-as (or generalisation)
- Is-part-of

An example of modular structure is given by the Reference IoT Layered Architecture (or RILA):

![](../images/Pasted%20image%2020231206171038.png)

![](../images/Pasted%20image%2020231206171133.png)

![](../images/Pasted%20image%2020231206171142.png)

In layered organisations, separation of concerns is easier to achieve, since:

- We can identify the main focuses of each layer at a glance
- Each layer can be implemented by a different team

The UML diagrams we use to represent modular structures are:

- The composite structure diagram:
  ![](../images/Pasted%20image%2020231206182048.png)
- The class diagram:
  ![](../images/Pasted%20image%2020231206182114.png)
- The package diagram:
  ![](../images/Pasted%20image%2020231206182204.png)

Modular structures allow us to answer questions such as:

- What is the primary functional responsibility assigned to each module?
- What other software elements is a module allowed to use?
- What other software does it actually use and depend on?
- What modules are related to other modules by generalisation or specialisation relationships?

#### Allocation structures

Allocation structures define how the elements in component and connector structures or module structures map onto things that are not software, like hardware, teams or file systems.

Typical allocation structures are:

- The deployment structure
- The implementation structure
- The work assignment structure

##### Deployment structures

Deployment structures capture the topology of a system's hardware and are built as part of the architectural specification.

They are needed to specify the distribution of components and to identify the performance bottlenecks.

They are usually developed by architects, networking engineers and system engineers.

![](../images/Pasted%20image%2020231206183331.png)

![](../images/Pasted%20image%2020231206183349.png)

## Software Design Description (SDD)

> **Video**
>
> The following notes come from the slides used in [this video](https://polimi365-my.sharepoint.com/personal/10143828_polimi_it/_layouts/15/stream.aspx?id=%2Fpersonal%2F10143828%5Fpolimi%5Fit%2FDocuments%2FDidattica%2FSE2%2FSoftwareEngineering2%2FLecturesFlippedClasses%2FDesignDescriptionsAndPrinciples3%2Emp4&ga=1&referrer=StreamWebApp%2EWeb&referrerScenario=AddressBarCopied%2Eview). 

In order to define what a Software Design Description is, we can use IEEE's standards for:

- Systems Design - Software Design Descriptions
- Systems and software engineering - Architecture descripsion

According to the aforementioned standards, a Software Design Description must contain:

- The identification of the SSD, with dates, authors, organisations...
- The description of the design stakeholders
- The description of the design concerns
- The selected design viewpoints
- The design views
- The design overlays
- The design rationale

## Design principles

We will now look at some design principles that are useful in designing large software systems:

1. [Divide and conquer](#divide-and-conquer)
2. [Keep the level of abstraction as high as possible](#keep-the-level-of-abstraction-as-high-as-possible)
3. [Increase cohesion where possible](#increase-cohesion-where-possible)
4. [Reduce coupling where possible](#reduce-coupling-where-possible)
5. [Design for reusability](#design-for-reusability)
6. [Reuse existing designs and code](#reuse-existing-designs-and-code)
7. [Design for flexibility](#design-for-flexibility)
8. [Anticipate obsolescence](#anticipate-obsolescence)
9. [Design for portability](#design-for-portability)
10. [Design for testability](#design-for-testability)
11. [Design defensively](#design-defensively)

### Divide and conquer

This design principle is best understood through an example like binary search:

![](../images/Pasted%20image%2020231207104416.png)

### Keep the level of abstraction as high as possible

A good software engineer should always make sure that their designs allow them to hide or defer consideration of details, thus reducing complexity.

A good abstraction is said to provide *information hiding*.

Abstractions also allow someone to understand the essence of a subsystem without the need for implementation details.

### Increase cohesion where possible

This design principle can be easily understood via the following example class:

```java
Class Utility {
	ComputeAverageScore(Student s[])
	ReduceImage(Image i)
}
```

The two methods inside the `Utility` class are very different in use and scope, so the class is not cohesive.

### Reduce coupling where possible

There are different types of coupling, so let's look at some examples:

1. **Content** coupling: in the image below, `A` is accessing the data structure in `B`, thus breaking encapsulation:
   ![](../images/Pasted%20image%2020231207104941.png)
2. **Control** coupling: in the image, `A` is controlling `B` by passing one of its own parameters to a function in `B`:
   ![](../images/Pasted%20image%2020231207105133.png)
3. **Communication** coupling: in the image, `A` is sending a great deal of messages to `B`, rendering communication very busy and signifying that `A` cannot work without `B` to some extent:
   ![](../images/Pasted%20image%2020231207105642.png)

### Design for reusability

An engineer should always design the aspects of a system so that they can be reused in other contexts. This requires:

- Generalisation of designs
- Simplification of designs
- Following common design principles
- Making the system as extensible as possible

### Reuse existing designs and code

This principle complements the [Design for reusability](#design-for-reusability) one: an engineer should always take advantage of the investment they or other engineers made by making reusable components.

Note that cloning is not a form of reuse.

### Design for flexibility

A system should always be designed anticipating possible changes that the design may have to undergo in the future. This can be achieved by:

- Reducing coupling and increasing cohesion
- Create abstractions
- Using reusable code and making code reusable
- Avoiding hard-coding

### Anticipate obsolescence

A system should always be designed while planning for changes in the technology or the environment, so that it will be able to run continuously with minor changes.

In order to enable this, an engineer should:

- Avoid using software libraries that are specific to particular environments
- Avoid using undocumented features or little-used features of software libraries
- Avoid using software or special hardware from companies that are less likely to provide long-term support
- Use standard languages and technologies that are supported by multiple vendors

### Design for portability

The designed system should be able to run on as many platforms as possible, so the engineers developing it should avoid using facilities specific to one environment.

### Design for testability

Engineers should always take some steps to make testing easier. One could also design a program to automatically test the software.

In Java, for example, Junit automates unit testing.

### Design defensively

Engineers should be careful in trusting in how other will try to use a component they are designing.

One should always handle cases where some other code might attempt to use their component inappropriately.

This can be mitigated by checking preconditions every time, but overzealous defensive design may result in unnecessary repetitive checking.

> **Video**
>
> The notes from the video end here.

## Architectural styles

> An architectural style determines the vocabulary of components and connectors that can be used in instances of that style, together with a set of constraints on how they can be combined. These can include topological constraints on architectural descriptions (e.g., no cycles). Other constraints--say, having to do with execution semantics--might also be part of the style definition.
> - Garland & Shaw, ["An Introduction to Software Architecture"](http://www.cs.cmu.edu/afs/cs/project/able/ftp/intro_softarch/intro_softarch.pdf)

### Client-server architecture

In client-server architectures, there are two main components:

- A **client** that issues requests
- A **server** that provides responses

![](../images/Pasted%20image%2020231207112853.png)

Client-server architectures are used when:

- Multiple users need to access a single resource (e.g. a database)
- There's a preexisting software that must be accessed remotely (e.g. a mail server)
- It is convenient to organise the system around a shared piece of functionality used by multiple components (e.g. an authentication server)

Client-server software can be organised in different ways:

![](../images/Pasted%20image%2020231207113432.png)

In order to design a client-server architecture correctly, engineers should:

- Design and document proper interfaces for our server
- Ensure the server is able to handle multiple simultaneous requests

#### Interface design

An interface is a boundary across which components can interact.

The proper definition of interfaces is an architectural concern, which impacts maintainability, usability, testability, performance and integrability.

Interface design is based on two guiding principles:

- Information hiding
- Low coupling

An interface shall encapsulate a component's implementation so that it can be changed without affecting other components.

Some aspects to consider during interface design:

- **Contract principle**: any resource added to an interface implies a commitment to maintaining it
- **Least surprise principle**: interfaces should behave consistently with expectations
- **Small interfaces principle**: interface should limit the exposed resources to the minimum

Important elements that must be defined when designing interfaces are:

- The **interaction style** (e.g. sockets, RPC, REST)
- The **representation** and structure of exchanged data
- The **error handling** functions

##### Sockets

When using sockets, both parties must agree on the same protocol. After the connection is established, communication is bidirectional.

![](../images/Pasted%20image%2020231207114711.png)

##### RPC and RMI

RPC resembles procedure calls in local settings (that is, within the same node). Stubs and skeletons need to transform procedure and method calls into messages and viceversa.

![](../images/Pasted%20image%2020231207114830.png)

##### REST: REpresentational State Transfer

REST is a specific and standardised architectural style for Application Programming Interfaces (APIs). It realises a clear separation between distributed, heterogeneous systems and components.

![](../images/Pasted%20image%2020231207114955.png)

The main characteristics of REST are:

- Communication is simple and standardised:
	- HTTP is used as the communication protocol
	- Data is formatted in JSON
	- REST follows the request/response paradigm
- REST interactions are stateless, which means they don't keep track of states across servers and clients
	- This makes REST scalable and lightweight
	- If caching is used, this leads to very high performance

In REST, there are four types of requests, which follow the CRUD acronym:

| Action                          | Request (HTTP methods) |
| ------------------------------- | ---------------------- |
| **C**reate a new resource       | `POST`                 |
| **R**ead an existing resource   | `GET`                  |
| **U**pdate an existing resource | `PUT`                  |
| **D**elete a resource           | `DELETE`               |

![](../images/Pasted%20image%2020231207115605.png)

Following are two graphs explaining the components of REST requests and responses:

![](../images/Pasted%20image%2020231207153749.png)

![](../images/Pasted%20image%2020231207153812.png)

##### Representation and structure of exchanged data

The representation of data impacts on the expressiveness, interoperability, performance and transparency of the interface design.

Below, a table comparing the main three data representation techniques used today: JSON, XML and protocol buffers:

| Category         | XML                                       | JSON                                       | Protocol buffers |
| ---------------- | ----------------------------------------- | ------------------------------------------ | ---------------- |
| Expressiveness   | Good                                      | Good                                       | Good             |
| Interoperability | Good                                      | Good                                       | Good             |
| Performance      | Verbose, requires multiple parsing passes | More compact than XML, single pass parsing | The most compact |
| Transparency     | Good, data passed as text                 | Good, data passed as text                  | Binary format    | 

##### Error handling

Some issues we can encounter when designing interfaces may be:

- An operation is called with invalid parameters
- A call to a method does not return anything

The possible reactions to errors when working with interfaces are:

- Raising an exception
- Returning an error code
- Log the problem

##### Multiple interfaces and separation of concerns

A server can offer multiple interfaces at the same time. This enables:

- A good separation of concerns
- Different levels of access rights
- Support to interface evolution

##### Interface evolution

Interfaces constitute the contract between servers and clients and sometimes, they need to evolve in order to support new requirements.

Some strategies to support continuity between versions of the same interface are:

- **Deprecation**: declare in advance that an interface will be unavailable starting from a given date
- **Versioning**: maintain multiple active versions of the interface
- **Extension**: a new version of the interface simply extends the previous one

#### Interface documentation

The documentation of an interface should only explain how to use it, and not include any information about the internal specifications of it.

An interface documentation is useful to:

- Developers and maintainers who are offering the interface
- Developers and maintainers who are using the interface
- Quality assurance teams for system integration and testing
- Software architects

##### OpenAPI specification

The OpenAPI specification defines how to describe a REST API interface through an OpenAPI definition, which is a JSON or YAML file that describes what a service can do using its interface.

The benefits of using the OpenAPI specification are:

- It provides a standardised format that is public and well-known
- It is human readable
- It uses the REST API
- Machines can use it to automate tasks, like testing or code generation

The OpenAPI definition describes:

- Endpoints
- Resources
- Operations
- Parameters, including data types
- Authentication and authorisation mechanisms

There are several tools that support the OpenAPI definition as well, like:

- An **API validator**, which is used to check conformance to the standard
- **Documentation generators**, which provide human-readable documentation
- **SDK generators**, which allow for the automated creation of client libraries in a programming language of choice

#### Handling multiple requests

The server must be able to receive and handle requests from multiple clients and there are several approaches to make this happen.

##### Forking

Forking is a very simple approach used by, for example, the Apache Web Server. It is based on using one process per request (or per client).

The list of pros and cons of forking is provided below:

| Pros                                                                     | Cons                                                                                                            |
| ------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------- |
| Architectural simplicity                                                 | Too many active users nowadays                                                                                  |
| Isolation and protection given by the "One connection per process" model | The number of active processes at time $t$ is difficult to predict and may saturate the resources of the server |
| Effective solution until the 2000s                                       | Each connection means performing expensive `fork` and `kill` operations                                         | 

##### Worker pooling

An alternative, more scalable approach is worker pooling, used for example by the NGINX Web Server. This approach is designed for high concurrency.

| Pros                                                                                                     | Cons                                                                                              |
| -------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| Fixed number of workers, which cannot saturate available resources                                       | Optimises scalability and performance by sacrificing availability when all worker queues are full |
| Each worker has a queue. Once it's full, the dispatcher drops incoming requests to keep high performance |                                                                                                   |
| The dispatcher balances the workload among available workers according to given policies                 |                                                                                                   |

### Three-tier and $n$-tier architectures

An example of a different style of architecture is the three-tier architecture you can see below:

![](../images/Pasted%20image%2020231207161551.png)

Three-tier architectures can be extended to $n$-tier architectures easily:

![](../images/Pasted%20image%2020231207161631.png)

### Event-driven architecture

In event-driven architectures, components can register to and send events through an event dispatcher:

![](../images/Pasted%20image%2020231207161722.png)

This style is also often called a publish-subscribe architecture.

Many different kinds of event languages can be used to create event-driven architectures.

Some pros and cons of this architecture style are:

| Pros                                        | Cons                                     |
| ------------------------------------------- | ---------------------------------------- |
| Very common in modern development practices | Potential scalability problems           |
| Easy addition and deletion of components    | The ordering of events is not guaranteed | 

Other characteristics of event-driven architectures are:

- Messages and events are asynchronous
- Computation is reactive (that is, computation is started when a message is received)
- The destination of the messages is determined by receiver, not by sender
- It has very loose coupling, since senders and receivers can be added without having to reconfigure the whole system
- It is very flexible with regards to communication means

Some technologies that use event-driven architectures are [Apache Kafka](https://kafka.apache.org/) and [RabbitMQ](https://www.rabbitmq.com/).

#### Apache Kafka

Apache Kafka is a framework for the event-driven paradigm which includes primitives to create event producers and consumers and a runtime infrastructure to handle event transfer from producers to consumers.

Kafka stores events durably and reliably and allows consumers to process events as they occur or also retrospectively.

Kafka and its services are offered in a distributed, highly scalable, elastic, fault-tolerant and secure manner.

The architecture of Kafka is shown in this diagram:

![](../images/Pasted%20image%2020231207162528.png)

Let's now list the main characteristics of Kafka:

- Each broker handles a set of topics and topic partitions, parts including sets of messages on the topic
- Partitions are independent from each other and can be replicated on multiple brokers for fault tolerance
- There is one leading broker per partition. The other brokers containing the same partition are followers
- Producers know the available leading brokers and send messages to them
- Messages in the same topic are organised in batches at the producers' side and then sent to the broker when the batch size overcomes a certain threshold
- Consumers adopt a pull approach. They receive all messages belonging to a certain partition in a single batch, starting from a specified offset
- Messages remain available at the brokers' side for a specified period and can be read multiple times in this time frame
- The leader keeps track of the in-sync followers
- ZooKeeper is used to oversee the correct operation of the cluster. All brokers send a heartbeat to ZooKeeper, which will replace a failing broker by electing a new leader for all the partitions the failing broker was leading. It may also start or restart brokers

Kafka is a very scalable platform, since producers and consumers can be distributed on different partition handled by different brokers. Furthermore, Kafka supports the creation of clusters of brokers, with up to a thousand brokers per cluster.

Kafka is also very fault-tolerant, since partitions are stored persistently and replication reduces the chance of data loss.

### Microservices

The microservice architectural style has become very popular in recent years as an alternative to monolithic systems, in which applications are delivered as single, deployable software artifacts.

![](../images/Pasted%20image%2020231209111626.png)

The idea behind microservices is that monolithic systems are decomposed into small specialised services and deal with a single bounded context in the target domain:

![](../images/Pasted%20image%2020231209111855.png)

A lot of successful companies use microservices, such as Netflix, Amazon, eBay and Spotify.

The change in general infrastructure architecture can be seen in the image below:

![](../images/Pasted%20image%2020231209112017.png)

Microservice architectures bring a lot of advantages over their predecessor:

- Microservices enable **fine-grained scaling strategies**: in monolithic systems, selective replication is not possible, while microservices enable flexible deployment and selective replication
- Microservices **reduce the scale of localised issues**, like availability issues
- Microservices **improve system resilience**: if one microservice fails, the others can still work (alas with degraded functionality, sometimes)
- Microservices **provide better reuse and composability**: the functionality of a single microservice can be reused in multiple contexts and it is possible to compose multiple microservices in different ways to realise different workflows

The use of a microservice-based architecture also brings some process advantages: since microservices are self-contained, every team has well-defined areas of responsibility and synchronisation between teams has less overhead:

![](../images/Pasted%20image%2020231209112635.png)

Furthermore, the technical implementation of a microservice becomes irrelevant during integration, since applications communicate with technology-neutral protocols, like [REST APIs](#rest-representational-state-transfer).

Finally, having a smaller codebase for each microservice enables easier debugging and, consequently, cheaper maintenance.

#### Anatomy of a microservice

A microservice is composed of three main elements:

- A data store, which contains the microservice's local data
- Application logic, which is the implementation of the core operations of the microservice
- A REST API, which exposes core operations of the service to the outside world

The usual workflow of a microservice is the following:

![](../images/Pasted%20image%2020231209114223.png)

#### Microservices: besides business logic

There are several more aspects to consider when building a microservice:

- **Routing patterns**: how can you ensure that your applications can scale quickly with minimal dependencies between services?
- **Resiliency patterns**: how do you make sure that when a problem occurs in a service, the service client fails quickly?
- **Security patterns**: how do you determine whether the service client calling a microservice is allowed to undertake certain actions?
- **Communication patterns**: how do you choose between synchronous and asynchronous modes of communication?

##### Routing patterns

When using microservices, the execution environment has shared resources that are not preallocated: the physical location of running services is potentially unknown, so the services need to be discovered.

Service discovery must be:

- **Highly available**: replication should be applied to avoid a single point of failure
- **Load balanced**: service invocations are spread across all the service instances
- **Resilient**: if service discovery becomes unavailable, applications should still function and locate the services
- **Fault-tolerant**: service discovery should monitor the health status of services and take action if needed, without human intervention

![](../images/Pasted%20image%2020231209115126.png)

![](../images/Pasted%20image%2020231209115142.png)

Service discovery can be cached, but some issues may arise in that case, since nothing ensures the consistency of the cached data.

##### Resiliency patterns

> How can we make sure that, when there is a problem with a service, clients avoid it before recovery?

Service discovery provides some degree of resilience when a service instance dies (it no longer sends its heartbeat). There are, however, other subtle issues. For instance, remote resources could throw errors or perform poorly.

The goal of resiliency in microservices is to allow clients to fail fast, in order to avoid useless resource consumption and ripple effects.

A client-side resiliency pattern is the **Circuit Breaker** (or *CB*) pattern.

The CB acts as a proxy for a remote service. When a remote service is called, the CB monitors the call and if it errors out or takes too long to perform, the CB kills that call:

![](../images/Pasted%20image%2020231209115744.png)

##### Security patterns

When a service client invokes a service directly, there is no way one can easily implement cross-cutting concerns, such as security or logging, without having each service implement this logic directly in the service.

This is where Service Gateways come into play. Service Gateways act as mediators which sit between a service client and the service it's invoking. The service client only talks to the gateway, which gatekeeps traffic and hence can easily implement authentication or authorisation mechanisms.

![](../images/Pasted%20image%2020231209120141.png)

The problem with Service Gateways is that they are a single point of failure. However, this is solvable using a gateway which has multiple instances and a server-side load balancer.

##### Communication patterns

The choice between synchronous and asynchronous communication is important, since using synchronous communication requires that the two communicating components are ready to communicate at the same time, which implies a tight runtime coupling.

A good approach is to use an event-driven framework to decouple the two parts.

Event-driven frameworks can support multiple communication styles:

- Notification: one way communication
  ![](../images/Pasted%20image%2020231209120540.png)
- Request/response: two way communication
  ![](../images/Pasted%20image%2020231209120603.png)
- Publish/subscribe: multicast communication
  ![](../images/Pasted%20image%2020231209120627.png)

The advantages of an event-driven communication framework are loose coupling, higher flexibility, scalability and availability. However, using an event-driven framework also makes the whole system more complex to develop.

#### Microservice technologies

Some microservice technologies in use today are:

- [**Spring Boot**](https://spring.io/guides/gs/spring-boot/): the de-facto standard framework for developing microservices in Java
- [**Spring Cloud Netflix**](https://cloud.spring.io/spring-cloud-netflix/reference/html/): integrates Service Discovery with Eureka, Circuit Breaker with Hystrix, Intelligent Routing with Zuul and Client Side Load Balancing with Ribbon
- [**Spring Cloud Stream**](https://spring.io/projects/spring-cloud-stream): a framework for building event-driven microservices connected with shared messaging system; it makes used of a variety of binder implementation (the frameworks used to send messages) like Apache Kafka

## Structure of a Design Document

The purpose of a design document is to provide a baseline for implementation activity, mappings between requirements and components and a baseline for integration and quality assurance. Furthermore, it refines the plan and previous estimations of cost, size and schedule.

The reference structure for a design document is as follows:

1. Introduction
	1. Scope
	2. Definitions, acronyms, abbreviations
	3. Reference documents
	4. Overview
2. Architectural design
	1. Overview: high-level components and interactions
	2. Component view
	3. Deployment view
	4. Component interfaces
	5. Runtime view
	6. Selected architectural styles and patterns
	7. Other design decisions
3. User Interface Design
4. Requirements traceability
5. Implementation, integration and test plan
6. Effort spent
7. References

## Software qualities and architectures

Several software qualities are directly influenced by architectural choices:

- Scalability
- Reliability
- Availability
- Usability

We need metrics to quantify qualities and specific methodologies to analyse the quantitative impact of architectural choices on these qualities and tactics to address possible issues.

### Availability

A service shall be continuously available to the user: it must have little downtime and rapid recovery.

The availability of a service depends on:

- The complexity of the IT infrastructure architecture
- The reliability of the individual components
- The ability to respond quickly and effectively to faults
- The quality of the maintenance by support organisations and suppliers
- The quality and scope of the operational management processes

We can define some metrics to quantify availability. Let's start by defining some terms:

- **Time of occurrence**: time at which the user becomes aware of the failure
- **Detection time**: time at which operators become aware of the failure
- **Response time**: time required by operators to diagnose the issue and respond to users
- **Repair time**: time required to fix the service or components that caused the failure
- **Recovery time**: time required to restore the system

On a timeline, these terms look like so:

![](../images/Pasted%20image%2020231210163537.png)

We can now define:

- The **Mean Time to Repair** (*MTTR*): average time between the occurrence of a failure and service recovery. This is also known as *downtime*
- The **Mean Time to Failures** (*MTTF*): mean time between the recovery from one failure and the occurrence of the next failure. This is also known as *uptime*
- The **Mean Time Between Failures** (*MTBF*): mean time between the occurrences of two consecutive failures

Now, we can calculate the probability that a component is working properly at time $t$ as the **availability metric** $A$:

$$A = {\text{MTTF}\over \text{MTTF} + \text{MTTR}}$$

If the MTTR is small, then $\text{MTBF} \approxeq \text{MTTF}$.

Availability is typically specified in the "**nines notation**":

| Availability (percentage) | Availability (nines) | Downtime        |
| ------------------------- | -------------------- | --------------- |
| 90%                       | 1 nine               | 36.5 days/year  |
| 99%                       | 2 nines              | 3.65 days/year  |
| 99.9%                     | 3 nines              | 8.76 hours/year |
| 99.99%                    | 4 nines              | 52 minutes/year |
| 99.999%                   | 5 nines              | 5 minutes/year  | 

Availability is calculated by modelling the system as an interconnection of elements in series and parallel. If some elements operate in series, the failure of one element leads to a failure of every component in the series; if some elements operate in parallel, the failure of an element leads to the other elements taking over the operations of the failed element.

The combined availability for components working in series is the product of the availability of the component parts:

$$A = \prod_{i=1}^n A_i$$

The combined availability for components working in parallel instead is:

$$A = 1-\prod_{i=1}^n (1-A_i)$$

Some tactics used to improve availability are:

- Replication
  ![](../images/Pasted%20image%2020231210173005.png)
- Forward error recovery
  ![](../images/Pasted%20image%2020231210173121.png)
- [Circuit breaker](#resiliency-patterns)
