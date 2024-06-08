---
title: 'Introduction'
draft: false
type: 'page'
toc: true
mathjax: true
---

---

## Why Software Engineering is important

Software is everywhere. Every aspect of our society is influenced by software.

It is fundamental for a Software Engineer to be able to develop good, working software. Software failures cannot be tolerated.

> **Software Engineering**
>
> Field of computer science dealing with software systems that are:
> - Large and complex
> - Built by teams
> - Exist in many version
> - Last many years
> - Undergo changes

A Software Engineer can't have programming skills only. A Software Engineer must be able to:

- Identify requirements and develop specifications
- Design a component to be combined with other components, developed, maintained and used by others
- Work in a team

## Process and product

The goal of Software Engineering is to produce *software products* through a *process*.

Both the process and the product are extremely important, due to the nature of the software product.

A software product is very different from traditional products:

- It is *intangible*
- It is *malleable*
- It is *human intensive*

The quality of software products is influenced by many factors:

- The quality of the development process
- The quality of the people working on it
- The quality of the timeline used to develop it
- The quality of the technology used in the process

Software product qualities are also described in the ISO standard [ISO/IEC 25010:2011](https://iso25000.com/index.php/en/iso-25000-standards/iso-25010).

### Process qualities

We can measure different qualities about the process of software development. One of these is the **productivity**: the ability to produce a *good* amount of product. It can be measured in delivered items (generally quantified in lines of code or function points) by unit of effort (generally quantified as person month).

Another important quality of the development process is the **timeliness**: the ability to respond to change requests in a timely fashion.

## Software lifecycles: waterfall model

Initially, there was no reference model on how to create a complex software system: you just coded what you needed to and then fixed it if needed.

In response to the countless errors and mistakes in programming, the **waterfall** model was introduced: some phases and activities in software development are identified and once one phase is completed, there is no turning back, since *climbing* the waterfall up is harmful time-wise.

![](../images/Pasted%20image%2020230916151750.png)

Later, other *flexible* models were introduced:

- Iterative models
- Agile methods
- DevOps

### Feasibility study and project estimation

This phase of the waterfall lifecycle includes a cost/benefit analysis and determines whether the project should be started.

The output produced by this phase is the **feasibility study document**, which contains:

- A preliminary problem description
- Scenarios describing possible solutions
- Costs and schedules for the different alternatives

### Requirement analysis and specification

In this phase, the software engineer analyses the domain in which the application takes place in order to identify the requirements of the system. From this, the software specifications are derived.

This phase requires continuous interaction with the user and an understanding of the properties of the domain in which the application will be deployed.

The outcome for this phase is the **Requirements Analysis and Specification Document** (or *RASD*).

### Design

In the design phase, the software architecture is defined:

- Components (or modules)
- Relations among components
- Interactions among components

The goal of this phase is to support concurrent development and separate responsibilities.

The output of this phase is the **design document**.

### Coding and unit level quality assurance

In this phase, each module is implemented using the chosen programming language and tested in isolation by the module developer.

Every module needs its own documentation.

### Integration and system test

In this phase, modules are integrated into subsystems and the integrated systems are tested.

This procedure follows an incremental implementation scheme.

### Maintenance

The maintenance phase is where problems found in the release version get corrected or new functionality is added to the software.

There are several types of maintenance:

| Type of maintenance | Description                                                          | % of total |
| ------------------- | -------------------------------------------------------------------- | ---------- |
| Corrective          | Deals with the repair of faults or defects found                     | 20%        |
| Adaptive            | Consists in adapting software to changes in the environment          | 20%        |
| Perfective          | Mainly deals with accommodating to new or changed user requirements  | 50%        |
| Preventive          | Concerns activities aimed at increasing the system's maintainability | 10%        | 

#### Correction vs. evolution

The distinction between correction and evolution may be unclear, since specifications are often incomplete and ambiguous.

This causes problems because specifications are often part of a contract between the developer and customer.

Specifications that are frozen early in the process can be problematic because they are more likely to be wrong by the end of development.

#### Problems of software evolution

Software evolution is almost never anticipated or planned and this causes disasters in the development process.

A good engineering practice to face evolution is to first modify the design and only then change the implementation. The applied changes must be consistent in all documents. This is one of the main goals of software engineering.

### Effort distribution in the software development lifecycle

This image shows the distribution of the developers' effort in the waterfall lifecycle:

![](../images/Pasted%20image%2020230916153102.png)

### Waterfall as a black box and transparency

The waterfall model is akin to a black box: the process is opaque to outside sources:

![](../images/Pasted%20image%2020230916153823.png)

More transparency in the process allows for early checks and changes through stakeholder feedback and it supports flexibility.

Transparency allows **validation** and **verification**, which answer the following questions:

> **Validation**
>
> "Are we making the right product?"

> **Verification**
>
> "Are we making the product correctly?"

## Flexible processes

The main goal of flexible processes is to *adapt to changes*, especially in requirements and specifications.

In flexible processes, stages are not sequential and processes become iterative and incremental:

![](../images/Pasted%20image%2020230916154159.png)

Flexible processes exist in many forms, like:

- eXtreme Programming (*XP*)
- SCRUM
- DevOps

Flexible processes are effective in dynamic contexts, like when there must be many changes per week. Some examples of this are web-based applications or mobile applications.
