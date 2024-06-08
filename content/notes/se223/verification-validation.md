---
title: 'Verification and validation'
draft: false
type: 'page'
toc: true
mathjax: true
---

---

## Introduction

Verification and validation are both important aspects of testing a software system, but they answer very different questions:

> **Verification is internal**
>
> Are we building the software correctly with regards to a specification?

> **Validation is external**
>
> Are we building a software that satisfies the stakeholders' needs?

Quality Assurance (*QA*) defines policies and processes to achieve quality and aims to find defects through verification and validation techniques.

According to IEEE:

| Term    | Definition                                                                                                                                                                                                                                          |
| ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Failure | Termination of the ability of a product to perform a required function or its inability to perform within previously specified limits; an event in which a system or system component does not perform a required function within specified limits. |
| Fault   | A manifestation of a defect                                                                                                                                                                                                                         |
| Defect  | An imperfection or deficiency in a program                                                                                                                                                                                                          |
| Error   | Human action that introduced an incorrect result                                                                                                                                                                                                    | 

![](../images/mermaid1.png)

Since zero-defect software is impossible to achieve, careful and continuous quality assessment is needed. Ideally, every artefact produced by development shall be subject to QA.

Verification and validation are usually applied according to the V model:

![](../images/Pasted%20image%2020231211104338.png)

The main verification approaches used are static and dynamic analysis:

- **Static analysis**: examines the source code without executing it
- **Dynamic analysis** (or *testing*): examines the runtime behaviour of the program

Here are the main differences between the two approaches:

| Static                                 | Dynamic                           |
| -------------------------------------- | --------------------------------- |
| Done at compile time, before execution | Done at runtime, during execution |
| Related to the source code             | Related to software behaviour     |
| Done on generic or symbolic inputs     | Done on specific inputs           | 

## Static analysis

The idea behind static analysis it to analyse the source code with automated analyser programs. Each analyser targets a fixed set of hard-coded properties.

Checked properties are often general safety properties, like:

- No overflow for integer variables
- No type errors
- No null-pointer dereferencing
- No out-of-bound array accesses
- No race conditions
- No useless assignments
- No usage of undefined variables

Static analysis uses techniques, methods and tools to **infer** properties of the dynamic behaviour **without explicitly running the software**.

The behaviour of a program is composed of all possible executions of that program as a sequence of states. Static analysis allows us to find erroneous states.

However, a program behaviour may never reach any erroneous state, so we can say that static analysis is pessimistic.

![](../images/Pasted%20image%2020231211112737.png)

Static analysis is based on over-approximations to be sound, so some degree of precision is often traded off against efficiency. Lower precision is cheaper, but can lead to false positives that must be verified manually. For this reason, designing a static analysis technique requires to balance precision and efficiency in a way that's practical.

### Data-flow analysis

In order to understand how data-flow analysis works, we must first learn what **Control-Flow Graphs** (or *CFG*s) are: directed graphs representing possible execution paths:

- A CFG node is a program statement
- A CFG edge connects two consecutive statements

In CFGs we ignore declarations, since they do not affect the program state.

If we take the following pseudocode:

```go
x := 1
y := x + 2

if (y > 3)
	z := y
else
	z := x

y := x
```

We can create its CFG like so:

![](../images/Pasted%20image%2020231211113303.png)

Data-flow analysis works on the CFG of a program and extracts information about the data flow, which defines what values are read and written when the program is executed.

One example of data-flow analysis is the so called *live variable analysis*, which tells the programmer if a variable assignment is useless in the current snippet of code.

#### Live variable analysis

Given a CFG, a variable `v` is **live** at the exit of a block `b` if there is some path from block `b` to a use of `v` that does not redefine `v`.

In the following graph:

![](../images/Pasted%20image%2020231211113553.png)

`y` is live at block 2, while it isn't at block 4.

Live variable analysis aims to determine which variables **may be live** at the exit of each CFG block.

Live variable analysis has several uses, among which is **dead assignment elimination**: if a variable is not live after it is defined by an assignment, the assignment is useless and can be removed without changing the program behaviour.

Live variable analysis reduces to an equation system, the solution of which identifies live variables. This equation can be solved by algorithms automatically, so it can be performed by an analyser in static analysis.

#### Reaching definition analysis

A definition `(v, k)` is an assignment to variable `v` occurring at block `k`. A definition `(v, k)` reaches block `r` if there is a path from `k` to `r` that does not redefine `v`.

Let's look at this pseudocode:

```go
x := 5
y := 1
while (x > 1)
	y := x * y
	x := x - 1
```

We want to find which definitions reach the entry of block 5. We can say:

- At the first loop iteration, `(x, 1)` and `(y, 4)` reach block 5
- In the following iterations, `(y, 4)` and `(x, 5)` reach block 5

Reaching definition analysis aims to find which definitions may reach a block for every block in the CFG.

For the graph shown below:

![](../images/Pasted%20image%2020231211114537.png)

The reaching definition analysis output is:

$$\text{RD}_\text{IN}(5) = \text{RD}_\text{OUT}(4) = \{ (x, 1), (x, 5), (y, 4) \}$$

The algorithm to find this result first works forward in the CFG. An analyser records the reaching definitions at the entry end exit of every block:

![](../images/Pasted%20image%2020231211114912.png)

We can then define the following equations: for each block $k$:

$$\begin{aligned}
\text{RD}_\text{IN}(k) &= \bigcup_{h\to k} \big(\text{RD}_\text{OUT}(h)\big)\\
\text{RD}_\text{OUT}(k) &= \big(\text{RD}_\text{IN}(k) \setminus \text{kill}_\text{RD}(k)\big) \cup \text{gen}_\text{RD}(k)
\end{aligned}$$

Where:

- $h\to k$ indicates all blocks $h$ such that $h$ is a predecessor of $k$
- $\text{kill}_\text{RD}(k)$ indicates other definitions of the same variables redefined at block $k$
- $\text{gen}_\text{RD}(k)$ indicates all variables defined at block $k$

An application of reaching definition analysis is to inform the developer about which statements define values and which use them. This is useful for program optimisation and to avoid potential errors.

We can define two types of "chains":

- **Use-def** chains: they link the use to all the definitions that might reach it:
  $$\text{UD}(v,k) = \{ q | q:v\coloneqq E \text{ and } \text{def\_clear}(v, q, k) \} \cup \{ ? | \text{def\_clear}(v, ?, k) \}$$
- **Def-use** chains: they link from a definition to all uses that the definition may reach:
  $$\text{DU}(v,k) = \{ q | q \text{ uses } v \text{ and } (v,k) \text{ reaches } q \} = \{ q | k \in \text{UD}(v,q) \}$$

### Static analysis in practice

Various static analysis tools are available nowadays. Many static analysis tools are language-specific, but some support multiple programming languages too.

The first static analysis tool was a Unix utility, Lint, developed in 1978 for C programs. This is why simple static analysis is also called *linting*.

## Symbolic execution

Symbolic execution executes programs on symbolic values, so that the output is expressed as a function of symbolic input.

Symbolic execution is halfway between static and dynamic verification.

The idea behind symbolic execution is to analyse real code, its reachability and path feasibility properties in an automated way. Symbolic execution can be used to generate test cases, but may fail to analyse all possible paths.

The properties checked by symbolic execution are:

- **Reachability**: symbolic execution tries to verify either that a line $l$ cannot be reached or, alternatively, spots the condition under which $l$ can be reached
- **Path feasibility**: symbolic execution tries to verify either that the path $p$ cannot be executed or, alternatively, spots the condition under which $p$ can be executed.

Symbolic execution executes programs on symbolic values, as we said earlier, so **symbolic states** keep track of the symbolic value of variables. For example, given the following snippet of code:

```java
void foo(int x, int y) {
	z := x
}
```

The symbolic state for this would be:

| Variable       | `x` | `y` | `z` |
| -------------- | --- | --- | --- |
| Symbolic value | $X$ | $Y$ | $X$ | 

Executing a branch in symbolic execution splits the symbolic state. For example:

```java
void foo(int x, int y) {
	z := x
	if (z < y)
}
```

This would yield to two symbolic states: if the condition in the code is true, then:

| Variable       | `x` | `y` | `z` | $\pi$ |
| -------------- | --- | --- | --- | ----- |
| Symbolic value | $X$ | $Y$ | $X$ | $X<Y$ | 

Otherwise, we have:

| Variable       | `x` | `y` | `z` | $\pi$ |
| -------------- | --- | --- | --- | ----- |
| Symbolic value | $X$ | $Y$ | $X$ | $X\ge Y$ | 

The variable $\pi$ is called **path condition** and represents the constraint of a path taken when branching.

Symbolic execution has two possible outcomes:

- `SAT` exit: the path variable $\pi$ is satisfiable, so any satisfying assignment to variables in $\pi$ is an input that satisfies the given property in a concrete execution
- `UNSAT` exit: the path variable $\pi$ is not satisfiable, so the given property cannot be satisfied by any concrete execution

Execution paths can be collected in an **execution tree**, where final states are marked as either `SAT` or `UNSAT`:

![](../images/Pasted%20image%2020231211160652.png)

Below, a full example of symbolic execution: given this code:

```java
void swap(int x, int y) {
	int z := x + y
	int w := z - y
	z := z - w
	
	if (z != y || w != x)
		print("error")
}
```

The resulting paths are:

| Path               | Feasible? |
| ------------------ | --------- |
| $<0,1,2,3,4,5,6>$ | No        |
| $<0,1,2,3,4,6>$    | Yes          |

The execution tree relative to this snippet of code is:

![](../images/Pasted%20image%2020231211161025.png)

### Limitations

While symbolic execution is a very useful tool, it still has some limitations:

- Path conditions may be too complex for constraint solvers: solvers are very good at checking linear constraints, but reasoning on non-linear arithmetic, bit-wise operations or string manipulation is more difficult for them
- Symbolic execution cannot be used when the number of paths to be explored is either very large or infinite: unbounded loops give rise to infinite sets of paths and, even if the set of paths to explore is finite, checking all loops is very expensive computationally, hence it may be infeasible
- There might be external code used in a program: if the symbolic solver can't access the source, it can't analyse that code

### Evolution

Symbolic execution was first introduced in 1976, but became practical about thirty years later with progress in constraint solving and concolic techniques, which are a combination of concrete and symbolic execution. These can alleviate several weaknesses of classic symbolic execution and can be used to generate test cases covering alternative execution paths.

## Dynamic analysis

The idea behind dynamic analysis is to test the program behaviour.

In testing, properties are encoded as executable oracles that represent expected outputs or desired conditions (*assertions*).

Dynamic analysis can only run finite sets of test cases, so it is not exhaustive verification.

Dynamic analysis too can be automated.

The main goal of testing is to **make the programs fail**, while also:

- Exercising different parts of a program to increase coverage
- Making sure the interaction between components works (*integration testing*)
- Supporting fault localisation and error removal (*debugging*)
- Ensuring that bugs introduced in the past do not happen again (*regression testing*)

### Test cases

A test case is a set of inputs, execution conditions and a pass or fail criterion.

Running a test case typically involves:

- **Setup**: it brings the program to an initial state that fulfils the execution conditions
- **Execution**: it runs the program on the actual inputs
- **Teardown**: it records the output, the final state and any failure determined based on the pass or fail criterion

A test set or test suite can include multiple test cases.

A test case specification is a requirement to be satisfied by one or more actual test cases. An example of test case specification could be:

> The input must be a sentence composed of at least two words

### Unit testing

Unit testing is conducted by the developers and is aimed at testing small pieces of code in isolation.

Unit testing is useful to find problems early, guide the design and increase coverage.

The problem with testing in isolation is that units may depend on other units, so they must be simulated. Assume we want to test unit $B$, which depends on units $A$ and $C$, but those units aren't ready yet. In that case, we create a **driver** which simulates $A$ and a **test stub** which replaces $C$ and test $B$ accordingly:

![](../images/Pasted%20image%2020231211164305.png)

### Integration testing

Integration testing aims at exercising interfaces and component interactions.

The faults usually discovered by integration testing are:

- Inconsistent interpretation of parameters
- Violations of assumptions about domains
- Side effects on parameters or resources
- Non-functional properties

Typically, **build plans** and **test plans** are defined in the design document and define, respectively, the order of the component implementations and how integration testing should be carried out.

There are several strategies that can be applied to carry out integration testing:

- **Big bang**: test only after integrating all modules together
- **Top-down**: test starting with the top level in terms of the "use" relation
- **Bottom-up**: the opposite of top-down
- **Threads**: test functionalities that compose a user-visible program feature
- **Critical modules**: start testing from modules with the highest risk

Below, a detailed explanation of all these strategies.

#### Big bang strategy

The big bang strategy aims to test modules only after integrating them all together.

This strategy requires no stubs and less drivers; however, it yields minimum observability and fault localisation is very difficult. Furthermore, the repair cost is very high, since every module is already implemented and integrated.

#### Top-down strategy

The top-down strategy starts from the top level and works its way to the bottom of the "use" (or "include") relation chain.

When using the top-down strategy, drivers use top level interfaces (like CLIs or REST APIs), but a lot of stubs of lower-level modules are needed.

#### Bottom-up strategy

This strategy is similar to the top-down one, but needs no stubs, since it starts from the bottom of the "use" relation chain. This means, however, that drivers must be implemented to test functionality.

The bottom-up strategy may create several working subsystems which are eventually integrated into the final one.

#### Thread strategy

A thread is a portion of several modules that, together, provide a user-visible program feature.

Integrating by thread maximises visible progress for users and stakeholders.

The thread strategy reduces the need for drivers and stubs, but its integration plan is typically more complex.

#### Critical modules strategy

When applying the critical module strategy, integration starts with modules having the highest risk. This means that risk assessment is a necessary first step.

The key point of the critical modules strategy is that it is a risk-oriented process: integration and testing are designed to deliver any bad news as soon as possible in the development process.

#### Choosing a strategy

Structural strategies, like the bottom-up and top-down strategies, are simpler to apply, while thread and critical modules strategies provide better external visibility on progress, particularly in complex systems.

It is also possible to combine different strategies: the top-down and bottom-up strategies are reasonable for relatively small components and subsystems, while a combination of thread and critical modules strategies are often preferred for larger subsystems.

### System testing

System testing, also known as end-to-end (*E2E*) testing, is conducted on a complete, integrated systems by independent teams and it can be both functional and non-functional.

The testing environment for E2E testing should be as close as possible to the production environment.

Common types of E2E testing are:

- **Functional testing**: it checks whether the software meets the functional requirements
- **Performance testing**: it aims to detect bottlenecks affecting response time, utilisation or throughput, to detect inefficient algorithms, hardware or network issues and to identify optimisation possibilities
- **Load testing**: it aims to expose bugs such as memory leaks, mismanagement of memory or buffer overflows, to identify upper limits of components and to compare alternative architectural options
- **Stress testing**: it aims to make sure that the system recovers gracefully after a failure

### Automated testing

Test cases can be either defined manually or automatically generated. 

A good test case is a test case that:

- Has a high probability of finding errors
- Is able to cover an acceptable amount of cases
- Is sustainable (since testing cannot continue indefinitely)

Test cases can be automatically generated through many techniques:

- **Combinatorial testing**: enumerate all possible inputs following some policy[^1]
- **Concolic execution**: pseudo-random generation of inputs guided by symbolic path properties
- **Fuzz testing** (or *fuzzing*): pseudo-random generation of inputs, including invalid or unexpected inputs
- **Search-based testing**: explores the space of valid inputs looking for those that improve some metrics, like coverage, diversity, failure inducing capacity...

#### Concolic Execution

Symbolic execution can be used to test specific execution paths automatically. However, we have already discussed about the weaknesses of symbolic execution.

This is where concolic execution comes into play: the idea is to perform symbolic execution alongside concrete execution (*concolic* is a crasis between concrete and symbolic).

The state of concolic execution combines a symbolic and a concrete part, which are used as needed to make progress in the exploration.

Concolic execution has two steps:

1. **Concrete to symbolic**: used to derive conditions to explore new paths
2. **Symbolic to concrete**: used to simplify conditions in order to generate concrete inputs

Let's look at the first step: if we take for example the following code:

```java
void m(int x, int y) {
	int z := 2 * y
	if (z == x) {
		z := y + 10
		if (x <= z)
			print("Log message.")
	}
}
```

We start from a random, concrete input and, at the same time, we build the symbolic condition of the explored path:

![](../images/Pasted%20image%2020231212154820.png)

If our input is $(x = 22, y = 7)$, we take the path $<0,1,2,6,7>$, which has the condition $2Y\ne X$. In order to explore another path, we simply have to negate that condition: $\lnot(2Y\ne X)$.

Now, the second step: if we can solve the negated constraint, we restart the process with another concrete input which satisfies that constraint (in this case, $\lnot(2Y\ne X)$). Then we explore the new path and reapply the concrete to symbolic step again:

![](../images/Pasted%20image%2020231212155123.png)

If we choose $(x=2, y=1)$ as our input, we follow the path $<0,1,2,3,4,5,6,7>$, which has the path condition $2Y=X \land X\le Y+10$.

The process continues iteratively like so until all paths are covered. In this example, the algorithm iterates for three times, giving us the three paths below:

| Path                | Input          |
| ------------------- | -------------- |
| $<0,1,2,6,7>$       | $(x=22, y=7)$  |
| $<0,1,2,3,4,5,6,7>$ | $(x=2, y=1)$   |
| $<0,1,2,3,4,6,7>$   | $(x=30, y=15)$ | 

Sometimes, however, the algorithm won't be able to solve the symbolic condition, like in this case:

```java
void m2(int x, int y) {
	int z := bb(y) // Black-box function
	if (z == x) {
		z := y + 10
		if (x <= z)
			print("Log message.")
	}
}
```

Here, we don't know the source of the black-box function `bb`, so we are unable to solve the negated condition $\lnot(\text{bb}(Y)\ne X)$.

If this happens, we go directly to the symbolic to concrete step, we execute the function with the selected input (in this case, `bb(7)`) and use the return value to solve the condition. If, for example, `bb(7)` returns 14, the condition becomes $\lnot (14 \ne X) \equiv (14=X)$, which is trivial. Now execution can continue.

Concolic execution has its own set of pros and cons:

| Pros                                                                                      | Cons                                                                                                            |
| ----------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| Can deal with black-box functions in path conditions                                      | Finds just one input example per path, so fault detection caused by input is more difficult to identify and fix |
| Can generate concrete test cases automatically, according to some code coverage criterion | The number of paths explodes due to complex, nested conditions                                                  |
|                                                                                           | It does not guide the exploration, but just explores possible paths one by one                                  | 

In the testing workflow, concolic execution finds its place at the beginning of the process:

![](../images/Pasted%20image%2020231212160234.png)

#### Fuzz testing

Fuzz testing complements functional testing and works at a component or system level. It deals with external qualities other than correctness, like reliability and security, by providing randomly generated data as inputs.

Fuzzing can uncover defects that might not be caught by other methods, since randomness typically leads to unexpected or invalid inputs.

The essence of fuzzing is to create random inputs to see if they break things.

In order to apply fuzzing to a piece of software, we must first build a fuzzer, a program that will output a random character stream. After that's done, we can attack the piece of software to test with the fuzzer, trying to break it.

Common bugs that can be found through fuzzing are:

- Buffer overflows
- Missing error checks
- Rogue numbers

> **Missing error checks**
>
> Many languages, like C, do not have exceptions; instead, they have functions that return special error codes in exceptional circumstances.
> 
> For example, the C function `getchar()` returns a character from `stdin`; however, if no input is available, it returns `EOF`.
> 
> Take a look at the following code:
> ```c
> while (getchar() != ' ');
> ```
> 
> If the program reads `EOF` before it encounters a space character, then the code enters an infine loop and hangs.

> **Rogue numbers**
>
> Fuzzing easily generates uncommon values in the input, causing interesting behaviour.
> 
> Take a look at this code:
> ```c
> char* read_input() {
> 	size_t size = read_size();
> 	char *buffer = (char *) malloc(size);
> 	// fill buffer
> 	return buffer;
> }
> ```
> 
> By providing a random number for `size`, fuzzing can create all kinds of damages to the program.

Fuzzing usually comes in the first phases of testing:

![](../images/Pasted%20image%2020231212164234.png)

##### Runtime memory checking

Fuzzing is very useful when paired with runtime memory-checks, since they can help catch problematic memory accesses during testing.

Runtime memory check tools analyse every memory operation at runtime in order to detect violations such as:

- Out-of-bounds accesses to the heap and stack
- Use-after-free
- Double-free

Unfortunately, using such tools increases execution time.

##### Fuzzing with mutations

Many programs expect inputs in very specific formats before they would process them. In this case, completely random inputs have a low chance to execute deep paths.

For example, if we need to test a piece of software that only accepts URLs as inputs, using exclusively random inputs won't serve the purpose we're looking for.

That's where **mutational fuzzing** comes in: rather than using random inputs from scratch, we *randomly mutate a valid input*.

##### Fuzzing: guiding by coverage

The higher the variety of the generation, the higher the risk of an invalid input. This means that we should keep and mutate inputs that are especially valuable for testing. This is called **guiding by coverage** and is a very popular approach.

The idea behind guiding by coverage is that the fuzzer should evolve only the test cases that find a new execution path. To do so, the fuzzer keeps and maintains a population of successful inputs. If a new input finds a new path, it will be added to the population.

This method is very practical with large programs, since it explores different paths in a more efficient manner. All that's needed to implement it is a way to capture the coverage.

#### Search-Based Software Testing

**Search-Based Software Testing** (SBST) complements test case generation techniques we've seen so far. It works at a component or system level and guides the generation toward a **specific testing objective**.

Compared to fuzzing, it typically incorporates domain-specific knowledge in order to generate more meaningful test cases.

It can also deal with both functional and non-functional aspects.

The idea behind SBST is to generate specific test cases that achieve some test objective, like:

- Observing wrong or undesired outputs
- Breaking requirements
- Reaching specific source code locations
- Executing some given paths

In SBST, search space and fitness guide the exploration of paths, making this type of testing essentially an optimisation problem.

The steps to apply SBST are:

1. Identify the objective
2. Define how to measure the distance, known as **fitness**, of the current execution from the objective
3. Instrument the code to compute the fitness of the current execution to the objective
4. Pick some inputs to run the program
5. Execute the test case and compute its fitness with respect to the objective
6. If fitness is not sufficient, return to step 4
7. Otherwise, we are satisfied

Some key points of SBST are:

- How do we identify and define objectives?
- How can we measure the distance of the current test case to the objective?
- How do we instrument the code to retrieve the necessary information to compute the fitness?
- How do we pick the next test case, if the current one is not good enough?

##### Test generation as a search problem

We define **search space** as the space of all possible test cases. Search space depends on the testing problem: it could be made of single integer values, tuples, objects, XML documents and more.

Each point in the search space has its own **neighbours**, which are defined as all the points in the search space that are somewhat near the current test case (the closeness depends on the application and the testing needs).

Given a search space and a neighbourhood relation, we can define:

- A **fitness function**, which defines the goodness of a given test case
- An **algorithm** that explores the neighbourhood using heuristics to steer the search

The fitness function depends on the objective of testing, of course; the search algorithm, however, has some standard models it can follow, which are described below.

###### Hillclimbing search

Hillclimbing is a simple meta-heuristic algorithm which works like this:

1. Take a random starting point
2. Determine the fitness value of all its neighbours
3. Move to the neighbour with the best fitness value
4. If the solution hasn't been found, return to step 2

Sometimes, the algorithm may remain stuck in a local optimum. In that case, the best thing to get out of it is to "give up" and start over from a new random point.

###### Evolutionary search

The hillclimbing algorithm works well if the search space and the neighbourhood are reasonably small.

Assume that we have a program that receives UTF-16 strings as an input. Since each character is encoded with 16 bits, there are 65536 possible encodings for each character, which makes the search space far too large for hillclimbing.

In order to make the search more "global", we can use the notion of mutation once more to change valid inputs. The inputs that discover new paths will be maintained and, from those, new ones will be generated changing some aspects, like changing a character or flipping a bit.

This is known as evolutionary search, since the inputs maintain "traits" of their predecessors in a sort of hereditary way.

##### SBST in the testing workflow

SBST finds its place at the beginning of the testing workflow:

![](../images/Pasted%20image%2020231212170701.png)

##### Pros and cons

SBST has its own pros and cons:

| Pros                                                                                       | Cons                                                                           |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| Compared to concolic testing, it guides the generation toward a specific testing objective | Requires domain-knowledge to define fitness, which is not a trivial definition |
| Compared to fuzzing, it typically generates more meaningful test cases                     | Heavily relies on the quality of the heuristics to explore the neighbourhood   |
| It reaches the objective with enough budget                                                | Computationally expensive and time-consuming                                   | 

[^1]: This will not be covered in this course
