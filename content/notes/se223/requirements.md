---
title: 'Requirements engineering'
draft: false
type: 'page'
toc: true
mathjax: true
---

---

## Definition

The primary measure of success of a software system is the degree to which it meets the purpose for which it was intended.

> **Requirements engineering**
>
> Software systems requirements engineering (shortened: *RE*) is the process of discovering the purpose of the software system by identifying stakeholders and their needs and documenting these in a form that is amenable to analysis, communication and subsequent implementation.

A software engineer needs to:

- Identify stakeholders
- Identify their needs
- Produce some documentation
- Analyse, communicate and implement the requirements

> What is a requirement?

There are three main types of requirements:

| Requirement type                         | Description                                                                                            | Example                                                                  |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| **Functional**                           | They describe the interaction between the system and its environment                                   | "A word processor user should be able to search for strings in the text" |
| **Non-functional**                       | They describe user-visible aspects of the system that are not directly related to functional behaviour | "The response time must be less than one second"                         |
| **Constraints** or *pseudo-requirements* | They are imposed by the client or the environment in which the system operates                         | "The implementation language must be Java"                               | 

> **Characteristics of non-functional requirements**
>
> Non-functional requirements are constraints on how functionality has to be provided to the end user and are independent of the application domain. However, the application domain determines their relevance and prioritisation and have a strong impact on the structure of the system to be.

All of the qualities in the red box below are non-functional requirements:

![](../images/Pasted%20image%2020230914091945.png)

Let's see some examples of bad requirements now:

> "The system shall validate and accept credit cards and cashier's check with high priority"

The issues with this requirement are:

- It's actually two requirements in the form of one sentence
- It is ambiguous: what does "high priority" mean?

Let's look at another example:

> "The system shall process all mouse clicks very fast to ensure users do not have to wait"

This constraint cannot be verified: what does "fast" mean? Do you have a metric for it? Can you quantify it?

Last example:

> "The user must have Adobe Acrobat installed"

This constraint cannot be achieved because installing Adobe Acrobat is not something that should be done by the system.

## Cost of late correction

The cost of correcting an error depends on the number of subsequent decisions that are based on it. Errors in requirements have the potential for **greatest cost**, because many other decisions depend on them.

## What makes requirements engineering so complex?

Requirements engineering is a very complex topic because it covers composite systems with multiple abstraction levels.

Requirements engineering concerns multiple aspects of the system development and has to engage with multiple stakeholders with very different backgrounds.

![](../images/Pasted%20image%2020230914094627.png)

## Understanding phenomena and requirements

Let's start from an example: an ambulance dispatching system:

- For every urgent call reporting and incident, an ambulance should arrive at the incident scene within 14 minutes
- For every urgent call, details about the incident are correctly encoded
- When an ambulance is mobilised, it will reach the incident location in the shortest possible time
- Accurate ambulance locations are known by GPS
- Ambulance crews correctly signal ambulance availability through mobile data terminals on the ambulances

Here are some questions that may arise when thinking about the requirements of the system:

> **Questions**
>
> - Should the software system drive the ambulance?
> - Who or what is the one "correctly encoding" details about incidents?
> - Are mobile data terminals pre-existing or not?
> - Who is assigned to what?

To answer these questions, a useful paradigm is the one proposed by Michael Jackson (not that one) and Pamela Zave: **The World and The Machine**. In this paradigm, the *machine* is the portion of the system that needs to be developed, while the *world* is the portion of the real world affected by the machine.

Requirements engineering is concerned with phenomena occurring in the world. For the ambulance dispatching system, these are:

- The occurrences of incidents
- The report of incidents by public calls
- The encodings of incidents by public calls
- The encodings of calls' details into the dispatching software
- The allocation of an ambulance
- The arrival of an ambulance at the incident location

> Requirements models are models of the world

![](../images/Pasted%20image%2020230916155335.png)

### Goals, domain assumptions and requirements

Let's take a look at a variant of the Venn diagram from before:

![](../images/Pasted%20image%2020230916155427.png)

- **Goals** are prescriptive assertions formulated in terms of world phenomena
- **Domain properties** (or *assumptions*) are descriptive assertions assumed to hold in the world
- **Requirements** are prescriptive assertions formulated in terms of shared phenomena

In the ambulance dispatching system, these are:

> **Goal**
>
> "For every urgent call reporting an incident, an ambulance should arrive at the incident scene within 14 minutes"

> **Domain assumptions**
>
> - "For every urgent call, details about the incident are correctly encoded"
> - "When an ambulance is mobilised, it will reach the incident location in the shortest possible time"
> - "Accurate ambulances' location are known by GPS"
> - "Ambulance crews correctly signal ambulance availability through mobile data terminals on the ambulances"

> **Requirement**
>
> "When a call reporting a new incident is encoded, the Automated Dispatching Software should mobilise the nearest available ambulance according to information available from the ambulances' GPS and mobile data terminals"

## Requirements completeness

The requirements $R$ are complete if:

1. $R$ ensure satisfaction of goals $G$ in the context of domain properties $D$:$$R\land D \vDash G$$
2. $G$ adequately captures all of the stakeholders' needs
3. $D$ represents valid properties or assumptions about the world

### The Airbus A320 example

> What can go wrong when defining $G$, $R$ and $D$?

We can look at an example provided by an Airbus A320 flight landing in Warsaw Airport in bad weather.

On landing, the aircraft's software-controlled braking system did not deploy when activated by the flight crew and it was about nine seconds before the braking system activated. There was insufficient runway remaining to stop the airplane and the aircraft ran into a grass embankment. Two people were killed and 54 were injured.

One of the reasons that caused this accident was because of an incorrect requirements engineering practice: originally, the world/machine graph would've probably been like this:

![](../images/Pasted%20image%2020230920084045.png)

Let's analyse goals, assumptions and requirements:

| Category           | Elements                                                                                                                     |
| ------------------ | ---------------------------------------------------------------------------------------------------------------------------- |
| Goals              | Reverse thrust enabled if and only if the aircraft is moving on the runway                                                   |
| Domain assumptions | <ul><li>Wheel pulses on if and only if wheels are turning</li><li>Wheels turning if and only if moving on a runway</li></ul> |
| Requirements       | Reverse thrust enabled if and only if wheel pulses on                                                                        | 

We can then verify that $R\land D \vDash G$ holds.

The problem lies in **invalid domain assumptions**: they did not include the phenomenon known as **aquaplaning**, which changes the behaviour of the wheels when standing water is on the runway:

![](../images/Pasted%20image%2020230920084600.png)

---

> **Video**
>
> The following notes were taken watching the video available [here](https://polimi365-my.sharepoint.com/:v:/g/personal/10143828_polimi_it/EQzGESnSzdBMnTIQvI9XG6QBV0zp715j6HqGqhHJ2Vx7qQ?e=Rx4Cab).

## Requirement elicitation

> **Requirement elicitation**
>
> Activity that allows a requirements engineer to define the requirements for a software to be.

Requirements engineers will have to collaborate with many different stakeholders, analyse existing systems and documentation in order to gather enough information to specify requirements for a given system.

The requirements engineer creates **models** in order to formalise the requirements of a system to be. These models are used for analysis and validation with the stakeholders and the other engineers.

Once everything has been formalised and validated, the models created before are used to create the **requirements documents**, which are the ones that get delivered to the stakeholders.

### Difficulties in the elicitation

When eliciting requirements, we must come face to face with some difficulties:

- **Implicit knowledge**: often times, stakeholders will apply some knowledge to their job which is not formally written and/or open to interpretation
- **Conflicting information**: different stakeholders may have different information or opinions about a specific rule
- **Bias**: some stakeholders may not agree with the creation of a given software system and could try to emphasise some very specific cases in order to make requirement elicitation more difficult on purpose
- **Probe effect**: the observing presence of a requirements engineer might change the behaviour of some of the stakeholders, effectively modifying the requirements, since the observed conditions are not the standard ones

> How do we cope with these complexities?

The requirements engineer can:

- Adopt different approaches and strategies, like listening, observing, and studying, and combine the results achieved with all of them
- Get as near as possible to the stakeholders
- Let each stakeholder describe their viewpoint

### Scenarios

In this context, **scenarios** are a useful tool:

> **Scenario**
>
> A narrative description of what people do and experience as they try to make use of computer systems and applications

Let's look at an example of scenario: a warehouse is on fire:

> Bob, driving down main street in his patrol car, notices smoke coming out of a warehouse. His partner, Alice, reports the emergency from her car.
> Alice enters the address of the building, a brief description of its location and an emergency level. In addition to a fire unit, she requests several paramedic units on the scene, given that the area appears to be relatively busy. She confirms her input and waits for an acknowledgement.
> John, the dispatcher, is alerted to the emergency by a beep of his workstation. He reviews the information submitted by Alice and acknowledges the report. He allocates a fire unit and two paramedic units to the incident site and sends their ETA to Alice.
> Alice then receives the acknowledgement and the ETA.

A couple of observations about the former example:

- This example is very **concrete** and does not describe all possible situations in which a fire can be reported.
- The participating actors in this scenario are Bob, Alice and John.

> How can I create scenarios?

An important step in order to find scenarios is to ask the client (or yourself) the following questions:

- Which user groups are supported by the system to perform their work?
- What are the primary tasks that the system needs to perform?
- What data will the actor create, store, change, remove or add in the system?
- What external changes does the system need to know about?
- What changes or events will the actor of the system need to be informed about?

However, a good requirements engineer should not rely on questions alone; if a system is already in place, **insist on task observation**.

You should also try to speak to the end user and not just the software contractor.

> Remember: you will probably encounter resistance, so you should try to overcome it.

### Use cases

Scenarios can be too specific sometimes. In order to gather more *abstract* information, a requirements engineer can take advantage of **use cases**.

> **Use case**
>
> A use case is a generalisation of a scenario

If we look back at the "Warehouse on fire" example, we could generalise it to a "Report emergency" use case.

Furthermore, use cases have a more formal structure than scenarios. A use case needs to be structured in terms of:

- Participating actors
- Description of the *Entry condition*
- Description of the *Flow of events*
- Description of the *Exit condition*
- Description of the *Exceptions*
- Description of the *Special requirements*, such as constraints or non-functional requirements

Returning to the example of the fire, we could formulate the "Report emergency" use case like so:

| Structural element   | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Notes                                                        |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------ |
| Participating actors | Field officer and Dispatcher                                                                                                                                                                                                                                                                                                                                                                                                                                     | Bob and Alice are field officers, while John is a dispatcher |
| Entry condition      | `True`                                                                                                                                                                                                                                                                                                                                                                                                                                                           | An emergency can be reported at all times                    |
| Flow of events       | <ol><li>The field officer activates the "Report emergency" function of her terminal</li><li>FRIEND, the system to be developed, responds by presenting a form to the officer</li><li>The field officer fills the form and submits it</li><li>The dispatcher is notified</li><li>The dispatcher reviews the submitted information and allocates resources by invoking the `AllocateResources` use case; he then sends an acknowledgement to the officer</li></ol> |                                                              |
| Exit condition       | The field officer has received the acknowledgement and the response sent by the dispatcher                                                                                                                                                                                                                                                                                                                                                                       |                                                              |
| Exceptions           | <ul><li>The field officer is notified immediately if the connection between her terminal and the control room is lost</li><li>The dispatcher is notified immediately if the connection between any logged in officer and the control room is lost</li></ul>                                                                                                                                                                                                      |                                                              |
| Special requirements | <ul><li>The field officer's report is acknowledged within 30 seconds</li><li>The selected response arrives no later than 30 seconds after it is sent by the dispatcher</li></ul>                                                                                                                                                                                                                                                                                 |                                                              |

By comparison, let's look at a bad example of a use case:

> Use case: Accident
> 
> | Structural element   | Value                                                                                                                                                             |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Participating actors | Field officer                                                                                                                                                     |
| Flow of events       | <ol><li>The field officer reports the accident</li><li>An ambulance is dispatched</li><li>The dispatcher is notified when the ambulance arrives on site</li></ol> |

The issues with this use case are:

- The name of the use case is not the action that is performed. The name of a use case should always be a **verb**
- The dispatcher is not included in the participating actors element
- Some actions in the flow of events do not have agents associated to them: that is, it is not specified by whom they are carried through
- The flow of events is very inconclusive

Here are some tips to define good use cases:

- Use cases should be named with verbs that indicate what the user is trying to accomplish
- Actors are always named with nouns
- The steps in the flow of events should be in the active voice
- The causal relationship between steps should be clear
- There should be a use case for each user transaction
- The description of exceptions should always be separate from the normal flow of events
- Use cases should be short in length (at most two to three pages)
- The steps accomplished by actors and those accomplished by the system should be clearly distinguished

---

> **Video**
>
> The following notes were taken watching the video available [here](https://polimi365-my.sharepoint.com/personal/10143828_polimi_it/_layouts/15/stream.aspx?id=/personal/10143828_polimi_it/Documents/Didattica/SE2/SoftwareEngineering2/LecturesFlippedClasses/ModelingReqs.mp4&ga=1)

## Modelling requirements

### What is a model

> **Model**
>
> A model is a representation in a certain medium of something in the same or another medium. The model captures the important aspects of the thing being modelled and simplifies or omits the rest.

Modelling is an abstraction of something that exists in **reality**.

If we assign to reality the letter $R$ and the letter $M$ to the model, we can map reality to a model through **interpretation** $I$:

$$I: R \to M$$

Objects in reality are related to one another and so are objects in the model. In a **good** model, real world relationships **correspond to relationships in the model**:

![](../images/Pasted%20image%2020230918154227.png)

In software development, models can be used for many activities:

- They are used to describe requirements and domain knowledge
- They are used to think about the design of a software system
- They are used to generate usable work products (or *artifacts*)
- They can give a simplified view of a complex system
- They can be used to evaluate and simulate a complex system
- They can be used to generate potential configurations of a system

Several issues arise when modelling reality:

- **Coherence**: different views of the system must be coherent
- **Variation in interpretation and ambiguity**: define where different interpretations of the model are acceptable

### Modelling in requirements engineering

The concepts that are typically modelled in requirements engineering are:

- The objects and people that are of interest for the given problem
- The relevant phenomena
- The goals, requirements and domain assumptions

### Tools for modelling

There are different tools that can be used to create models:

| Tool                 | Pros                                                                                                                            | Cons                                                                  |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------- |
| Natural language     | Simplicity of use                                                                                                               | High level of ambiguity                                               |
| Formal language      | It is possible to use tools to support analysis and validation and the approach forces the user to specify all relevant details | The user must be an expert in the use of the selected formal language |
| Semi-formal language | It's simpler than a formal language and imposes some kind of structure to the models                                            | It is not amenable for automated analysis and there is some ambiguity | 

An accepted practice is to use a **mixed approach**, where semi-formal languages are used for the basic requirements of the system. Some informative text can be added to the semi-formal model to clarify some parts. Formal languages are only used for the most critical parts of the system.

#### UML

UML is a semi-formal language that can be used for both **static** modelling and **dynamic** modelling:

![](../images/Pasted%20image%2020230921092953.png)

UML is very useful specifically to create **use case models**:

![](../images/Pasted%20image%2020230921093318.png)

In use case models, **associations** define relationships between use cases. There are three main associations:

- **Include**: a use case uses another use case
- **Extend**: a use case extends another use case
- **Generalisation**: an abstract use case has several different specialisations

The table below compares the three associations among one another:

| Generalisation                                                      | Extend                                                            | Include                                                         |
| ------------------------------------------------------------------- | ----------------------------------------------------------------- | --------------------------------------------------------------- |
| The base use case could be an abstract use case or a concrete one   | The base use case is complete by itself and defined independently | The base use case is incomplete                                 |
| A specialised use case is required if the base use case is abstract | Extending a use case is optional                                  | The included use case is required                               |
| No explicit location to use the specialisation                      | It has at least one explicit extension localisation               | No explicit inclusion location but is included at some location |
| No explicit condition to use specialisation                         | Could have optional extension condition                           | No explicit inclusion condition                                 | 

We can look at a refined incident management system model below:

![](../images/Pasted%20image%2020230921094343.png)

---

## Example of goals, assumptions and requirements

Let's now look at an example of goals, assumptions and requirements in a non-mission critical system: a turnstile control system.

The main purpose of the systems is to let people in only if they paid a coin.

Let's start with the domain analysis: we should identify the relevant phenomena with respect to the purposes of the system:

| Phenomenon | Description                 | Environment controlled | Machine controlled | Shared phenomenon |
| ---------- | --------------------------- | ---------------------- | ------------------ | ----------------- |
| Enter      | Person enters the room      | ✔                      |                    |                   |
| Push       | Person pushes the turnstile | ✔                      |                    |                   |
| Coin       | Coin inserted               | ✔                      |                    | ✔                 |
| Turn       | Turnstile turns             | ✔                      |                    | ✔                 |
| Lock       | Electrical signal           |                        | ✔                  | ✔                 |
| Unlock     | Electrical signal           |                        | ✔                  | ✔                  |

The events "Enter", "Push" and "Turn" are clearly linked, but they are outside of the control of the machine. Their dependencies are captured by **domain assumptions**:

- $D_a$: "Turn" occurs only after a "Push" occurs
- $D_b$: "Turn" leads to "Enter"
- $D_c$: "Enter" occurs only after "Turn" occurs

Essentially, each "Enter" corresponds to a "Turn", while on the other hand there can be "Push" events that do not lead to "Turn" events.

For our application, we are not interested in deeply studying the cases in which a person pushes the turnstile but it does not turn, so we conflate the "Push" and "Turn" events in a single "Push&Turn" **shared, world-controlled** event. We have a new assumption then:

- $D_d$: "Push" leads to "Turn"

Let's analyse what the goals of our application are now:

- $G_1$: at any time entries should never exceed the number of accumulated payments
- $G_2$: those who pay are not prevented from entering

These goals are described through **optative** descriptions (they describe things that we *want* to happen) and both are said to be **safety properties**: they state that nothing bad will ever occur.

We can now revisit our domain assumptions:

- $D_{1a}$: "Enter" cannot occur without "Push&Turn"
- $D_{1b}$: a new "Push&Turn" cannot occur until the previous visitor entered

Assumptions $D_{1a}, D_{1b}$ can be summed up in the following assumption:

- $D_1$: "Push&Turn" and "Enter" alternate, starting with "Push&Turn"

Let's take a look at some more assumptions:

- $D_2$: "Push&Turn" always leads to "Enter"
- $D_3$: "Push&Turn" cannot occur if and only if the turnstile is Locked
- $D_4$: after "Push&Turn", there is a minimum delay before the next "Push&Turn" can occur

We can now revisit goal $G_1$ and set the requirements for it:

- $G_1$: at any time, entries $e$ should never exceed accumulated payments $c$, so $e\le c$ must hold

$G_1$ can be enforced by controlling either entries or coins. The machine cannot, however, compel coin events, but it can prevent "Enter" events. So, the requirements for this goal are:

- $R_1$: initially, the turnstile is locked
- $R_2$: the command "Unlock" is given only if the number of pushes is less than the number of payments ($p<c$)
- $R_3$: if "Push&Turn" occurs and $p=c$ holds, command "Lock" is given before the next "Push&Turn" can occur

We must now show that $R_1, R_2, R_3, D_1, D_3, D_4$ guarantee $G_1$:

$$R_1, R_2, R_3, D_1, D_3, D_4 \vDash G_1$$

We can model this through a **finite automaton**:

![](../images/Pasted%20image%2020230920093556.png)

We need to show that $e\le c$ holds, so if we can show that $p\le c$ holds, we have that $e\le p\le c$, which is the desired property:

> **Demonstration for $G_1$**
>
> Initially, $p=c=0$ and the turnstile is locked ($R_1$), so "Push&Turn" cannot occur ($D_3$).
> The turnstile is unlocked only if $p<c$ holds ($R_2$), so the first coin must occur *before* the first "Push&Turn" can occur.
> Consider now a time in which $p<c$ holds and "Push&Turn" occurs; we indicate with $p'$ the new number of pushes, so $p' = p+1$. If $p'=c$, then some time must pass before a new "Push&Turn" can occur ($D_4$) and the "Lock" command is given before a new "Push&Turn" can occur ($R_3$). Hence, a new "Push&Turn" cannot occur ($D_3$) unless a new coin is inserted.

Let's now consider goal $G_2$:

- $G_2$: those who pay are not prevented from entering

This means that we need to show that if $p<c$ holds, then "Enter" can occur.

Intuitively, we should not lock the turnstile if there is an excess of payments, as captured by the following new requirements:

- $R_4$: command "Lock" is given only if $p=c$ holds
- $R_5$: if $p<c$ holds and the turnstile is locked, command "Unlock" is given

We must now show that $R_4, R_5, D_1, D_2, D_3 \vDash G_2$:

> **Demonstration for $G_2$**
>
> From $D_{1a}$ and $D_2$ we have that "Enter" occurs if and only if "Push&Turn" occurs; then, from $D_3$, we have that "Enter" can occur if and only if the turnstile is unlocked. So, to prove $G_2$, we need to show that if $p<c$ holds, then the turnstile is unlocked.
> Consider now a time in which $p<c$ holds; we have two cases:
> - If the turnstile is unlocked, then from $R_4$ we have that the machine does not lock it, so it stays unlocked
> - If the turnstile is locked, then from $R_5$ we have that the machine unlocks it

## Conclusion

The boundary between the world and the machine is generally not given at the start of a development project. The purpose of a requirements engineering activity is to identify the **real goals** of the project, **explore alternative ways** to satisfy the goals and to **evaluate strengths and risks** of each alternative, in order to select the most appropriate one.
