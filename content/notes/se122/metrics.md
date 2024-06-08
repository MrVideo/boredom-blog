---
title: 'Metrics'
draft: false
type: 'page'
toc: true
mathjax: true
---

---

## Some design principles

### Open-Closed Principle

A module should be [**open to extensions but closed to modifications**](Liskov's%20Substitution%20Principle.md#Open-closed%20principle).

This principle comes from the work of [Bertrand Meyer](https://it.wikipedia.org/wiki/Bertrand_Meyer):

> We should always write our classes in such a way that they are extensible without having to be modified.

According to this principle, we would like to be able to change the behaviour of a class without changing the source code. This brings a maintenance advantage: if the source is the same, there can be no new mistakes.

The core concepts behind this principle are:

- Inheritance
- Overriding
- Polymorphism
- Dynamic binding

Let's look at an example. We would like to make a program that draws geometric figures on the screen. In C, that could look like this:

```c
void drawAll(figure figure[]) {
	for(i = 0; i < 100; i++) {
		if(figure[i] /*is "rectangle"*/)
			// Draw "rectangle"
		if(figure[i] /*is "triangle"*/)
			// Draw "triangle"
		if(figure[i] /*is "circle"*/)
			// Draw "circle"
	}
}
```

If we want to add a way to draw a trapezoid, for example, we must change the code in the `drawAll` function.

In Java, we could avoid that by doing this:

```java
public static void drawAll(Figure[] figure) {
	for(i = 0; i < 100; i++)
		figure[i].draw();
}
```

This lets us create classes for every figure without ever changing the method that draws them.

### Liskov Substitution Principle

The object of the subclass must respect the contract of the superclass. This means that the behaviour of the subclass must be compatible with the specification of the superclass.

Modules that use objects of one type must be able to use objects of a subtype without "*noticing*" the difference.

Let's look at an example: an `Imperial` class has a constructor and a `calculation` method that accept values in feet and return values in inches. How can we reuse this class with parameters and results expressed in the metric system?

It can be done like this, but it is not ideal:

```java
public class Metric extends Imperial {
	public Metric(double x) {
		super(x / 0.3048);
	}

	public double calculation(double x) {
		return super.calculation(x / 0.3048) * 0.0254;
	}
}
```

In this case, the `Metric` class violates the substitution principle. The correct way to solve this problem is by *composition*:

```java
public class Metric {
	protected Imperial i;
	
	public Metric(double x) {
		i = new Imperial(x / 0.3048);
	}

	public double calculation(double x) {
		return i.calculation(x / 0.3048) * 0.0254;
	}
}
```

You should always favour composition over inheritance.

### Dependency Inversion Principle

The depencency inversion principle says you should depend on abstractions and not on concrete elements.

With the word *inversion*, this principle means that the top classes in the inheritance hierarchy should not depend on the bottom classes: it should work the other way around.

Following this principle means that any class that you think might be extended in the future should be defined as a subtype of an interface or abstract class.

Whenever it's not strictly necessary to refer to objects of the class, it's better to refer to objects that have an abstract static type. This way, it will be easier to modify the code for extensions.

### Other principles

- *Interface Segregation Principle*: many client specific interfaces are better than one general purpose interface.
- *Reuse/Release Equivalency Principle*: the granularity of reuse is the same as the granularity of release. Only components that are released through a tracking system can be effectively reused.
- *Acyclic Dependencies Principle*: the dependency structure for released components must be a directed acyclic graph.
- *Stable Dependencies Principle*: dependencies between released categories must run in the direction of stability. The dependee must be more stable than the depender.
- *Stable Abstractions Principle*: the more stable a class category is, the more it must include abstract classes. A completely stable category should consist of nothing but abstract classes.

## Evaluating software quality

The *functional correctness* of a project is fundamental, but the quality of a piece of software is also assessed through non-functional requirements, such as efficiency, or structural requirements, such as modifiability and stability.

The structural aspects of a project are evaluated using coupling, cohesion and the open-closed principle.

### Coupling

Coupling is a metric that captures the degree of interconnectedness between classes.

A high degree of coupling means that there is a high interdependence between classes and a single class is difficult to modify by itself.

A low degree of coupling is necessary to create a comprehensible and modifiable system.

In the object-oriented world, there are three types of coupling:

- Interaction coupling
- Component coupling
- Inheritance coupling

#### Interaction coupling

Interaction coupling happens when methods of one class call methods of other classes.

Interaction coupling should be avoided particularly when a metod manipulates state variables of other classes directly or exchanges information through temporary variables.

Interaction coupling is acceptable in some forms, like when methods communicate directly via parameters.

To reduce interaction coupling, methods should pass as little information as possible through as few parameters as possible.

#### Component coupling

A class `A` is paired with another class `C` if it has:

- Attributes of type `C`
- Parameters of type `C`
- Methods with local variables of type `C`

When `A` is paired with `C`, it is also paired with all its subclasses.

Component coupling usually also implies the presence of interaction coupling.

#### Inheritance coupling

Inheritance coupling happens when one class is a subclass of another.

Inheritance coupling should be avoided when a subclass changes the signature of an inherited method. Ideally, the subclass should only add methods and attributes and avoid ovverriding any other method.

### Cohesion

Cohesion is an *intra-module concept*. It focuses on why some elements are in the same module.

Only strongly related elements should be in the same module. This would make the code more comprehensible and create a higher abstraction level. High cohesion also usually leads to low coupling.

There are three types of cohesion:

- Method cohesion
- Class cohesion
- Inheritance cohesion

#### Method cohesion

Method cohesion describes how related the functions of a specific method are.

The best form of cohesion is when a method implements a single, clearly defined function, similarly to a C function. The programmer should be able to describe a method with one simple sentence.

#### Class cohesion

Class cohesion describes how elements of a class are related to one another.

A class should represent only one concept and all properties should contribute to its representation. If the user encapsulates different concepts in the same class, cohesion decreases.

Different method groups accessing disjoint attribute groups is a clear symptom of low cohesion.

#### Inheritance cohesion

Inheritance could be induced by the need to add a layer of generalisation or by the need to reuse some portion of code many times.

Cohesion is greater if hierarchy is used to manage generalisation.

### Software metrics

To evaluate the quality of a software project in an objective manner, a software engineer can apply some predefined metrics such as:

- *Weighted Methods per Class* (WMC): number of methods weighted for their complexity
- *Depth of Inheritance Tree* (DIT)
- *Number of Children* (NoC)
- *Coupling Between Classes* (CBC)
- *Response for a Class* (RfC): total number of methods that can be invoked by an object of a class
- *Lack of Cohesion in Methods* (LCoM): captures the "closeness" between methods of a class by measuring how often they access common variables and attributes

Given a program, these metrics can be calculated via different tools, usually based on Java bytecode analysis.

#### Weighted Methods per Class

The complexity of a class depends on the number of classes and their complexity.

Suppose that class `C` has methods `m1`, `m2`, to `mn` with respective complexities of `c1`, `c2`, to `cn`. In this case, $\text{WMC} = \sum c_i$.

A high WMC metric could mean a stronger lean towards code defects.

#### Depth of Inheritance Tree

A deep class hierarchy means more potentially reusable methods and a high cohesion, which consequently makes code more difficult to change.

The Depth of Inheritance Tree of a class is the shortest path of the class from the root node. The value of DIT helps predicting the defect susceptibility of a class.

#### Number of Children

The Number of Children is the number of immediate subclasses of a given class. This metric assesses the degree of reuse of code.

A high NoC indicates reuse of definitons by a large number of subclasses and also indicates the influence of a class on other elements. High influence requires careful design and implementation.

Classes with a high NoC should not be a cause of errors.

#### Coupling Between Classes

CBC reduces modularity and makes changes in the codebase more complex.

CBC is defined as the number of classes with which a given class is paired. Two classes are coupled if the methods of one use methods or attributes of the other.

This metric can be calculated on the code, but there are some direct forms of coupling that cannot be calculated statically.

This metric can provide some insight on possible class defects.

#### Response for a Class

The RfC is defined as the total number of methods that can be invoked by an object of a class.

RfC is the cardinality of the response set of the class, which is the set of all methods that can be invoked when sending a message to an object of a class.

Even if the CBC of a class is $1$, its RfC could be much higher.

The RfC metric captures the "weight" of connections between classes. As a result, testing high-RfC classes is more complex.

#### Lack of Cohesion Methods

As said earlier, cohesion captures the "closeness" between methods of a class. Two methods form a cohesive pair if they access common variables or attributes. On the contrary, they form a *non-cohesive pair* if they have no variables in common.

High cohesion in a codebase is desirable, since it makes the code more comprehensible and easier to maintain.

This metric, however, is non-significant for predicting the possible defectiveness of a class.

### Studies

Some studies conducted on professional software say that:

- Most classes have a limited number of methods, so a high WMC has significant correlation with error propensity.
- Classes are usually very close to the root, with a maximum DIT nearing $10$, while most classes have a null DIT. Designers tendo to keep the number of abstraction levels low, sacrificing reusability for comprehensibility.
- Classes often have a limited number of children and, in many cases, they have none. Inheritance is therefore not fully taken advantage of.
- Most classes are completely self-contained, sporting a CBC of $0$, but interface objects tend to have a non-zero CBC.
- Most classes invoke few methods of other classes, thus having a low RfC, but interface objects tend to increase that metric.
- Lack of Cohesion Methods have been proven to be futile in the prediction of defect propensity.

### Symptoms of a "poorly made" project

A badly managed project is usually identifiable through some properties, such as:

- **Rigidity**: the software is difficult to change, even when the changes are minor
- **Fragility**: the software "breaks" in different places when changes are made
- **Immobility**: the inability to reuse software from other projects or other parts of the same project
- **Viscosity**: the use of shortcuts is easier than the use of methods that respect the project's design

The four symptoms listed above are caused, directly or indirectly, by improper dependencies between software modules. Dependencies between modules must be managed through special firewalls, like ad-hoc classes.

## Practical suggestions

### Interface minimisation

If there is no strong reason to declare a method as `public`, it must be declared as `private`.

It is preferable to only define getter methods for class fields where possible, avoiding setter methods. Avoid replicating the data structure contained in a class in its interface. It usually is absurd to provide a getter for every attribute of a class.

### Methods with few parameters

If a method has more than three or four parameters, programmers might not remember them. Methods with too many parameters are very difficult to grasp, especially when parameters are all of the same type.

A method that requires many parameters can generally be broken down into methods that require less parameters. It's also possible to create auxiliary classes that contain the aggregate parameters.

For example, let's try and break down the two following methods:

```java
class Circle {
	public void Circle(double x, double y, double z, double radius) {
		// Code
	}
}

class Square {
	public void Square(double x, double y, double z, double side) {
		// Code
	}
}
```

A good solution could be this:

```java
class Point {
	private double x;
	private double y;
	private double z;
}

class Circle {
	public void Circle(Point center, double radius) {
		// Code
	}
}

class Square {
	public void Square(Point vertex, double side) {
		// Code
	}
}
```

### Anti-pattern

An anti-pattern is a frequently used solution, but it should be avoided. It is a common mistake that should provide suggestions on how to improve the code or avoid known errors.

Note that anti-patterns don't just apply to object-oriented design.

For example, let's take a look at a *blob class*: it's a big class that contains most of the application logic. The class operates on class objects that only contain data and it often comes from the application of procedural, C-style design in an object-oriented language.

The issues brought along by a blob class are usually the presence of duplicate code and very long methods. Both of these issues can be solved by analysing and extracting excess code from large methods to pack them in service methods.

Here is a list of more common issues:

- If a method mainly uses data from another class, you need to move the method to the class where that data is defined.
- Using a switch construct is not advisable: the switch often indicates a type of objects, so the introduction of new types requires the modification of the relative switches. It's best practice to use inheritance and enumeration where possible.
- The presence of data blocks (that is, pieces of data often used together) can lead to a long list of parameters, so a class should be introudced to aggregate that data.
- The presence of extensive comments is a sign of difficult to read code. Methods should be self-explanatory and very clear with their naming and structure.
- Classes should know as little as possible about other classes, so to make data access less complex.
- Error handling that is not implemented through exception throwing should be avoided at all costs: it makes maintenance and extensibility much more complex.

### Refactoring

Coding a software project correctly on the first try is impossible. Found solutions usually require refactoring, which is improving the design of existing code without changing its fundamental behaviour. This brings code and architecture improvements that make execution faster and maintenance easier.

There is no precise rule on when to refactor. The thumb rule is: when the code becomes too difficult to read, it's refactoring time. It's also better to refactor the codebase *before* implementing new features.

## Programming style and comments

We will now discuss some good practice when actually *writing* code, not desigining it. These rules are usually supported by the IDE of choice and verifiable.

### Comments

Comments can be used to clarify the meaning of the code or to make it even more obscure. Discretion is advised.

Some good rules:

- Comments that repeat code are useless
- Comments that contradict the code indicate that both the code *and* the comment are probably incorrect
- Comments can indicate the meaning of the code in a way that is partially independent of changes
- Comments should indicate what the code is *intended* to do

Some examples:

```java
// Useless comment
i++; // Increment i

// Useful comment
i++; // Increment the card counter

// No comment needed
cardCounter++;
```

A good choice of variable and method names makes the code largely "self-commented".

What to comment on depends on multiple factors, particularly the expressiveness of the language. In Java, it's generally useless to have a comment for every line of code.

In object-oriented languages in general, however, it's generally a good idea to provide a comment at the beginning of each method, detailing what the method does, constraints and requirements.

It may also be useful to include references to external documentation.

You should comment only when you have to say something more than the code is already saying. If you can make the code clear enough, you might not need any comment at all.

### Names and capitalisation

The name of an element might well be used to indicate the nature of the element itself. This effect is usually achieved through *scheduling conventions*, established at the company level.

The usual Java naming conventions are the following:

- Names of classes and interfaces are capitalised
- Variable and method names always start with a lowercase letter
- The names of constants are all caps
- Package names are all lower case
- When names consist of several words, camel case is used
- Class names should be singular
- Void methods should be named after a verb that describe what they do
- Methods and boolean variables should have names that start with a tense of the verb "be"
- Other non-void methods should have names that suggest what they return
- Non-boolean variables should have nouns as names, possibly with some adjectives
