---
title: "Liskov's Substitution Principle"
draft: false
type: 'page'
toc: true
mathjax: true
---

---

## Open-closed principle

In object-oriented languages, it is possible to define abstractions through classes to be used later in other modules.

Every module should be **closed** to modifications, since the definitions of the abstractions that it uses do not change, but should be also **open** to extensions, like subclasses through inheritance.

## Liskov's Substitution Principle

Extensibility through inheritance is only guaranteed when we can use objects of a subclass in place of the ones generated from the superclass.

[Barbara Liskov](https://it.wikipedia.org/wiki/Barbara_Liskov) and Jeannette Wing defined a principle that should be always followed in object-oriented programming when designing software *by contract*:

> Let $\phi(x)$ be a property provable about objects $x$ of type $T$. Then $\phi(y)$ should be true for objects $y$ of type $S$ where $S$ is a subtype of $T$.

This is similar to [Bertrand Mayer's *design by contract*](Metrics.md#Open-closed%20Principle) and a direct extension of [Hoare logic](https://en.wikipedia.org/wiki/Hoare_logic).

When *designing by contract*, this principle poses some constraints on how contracts interact with inheritance:

- Prerequisites required by a superclass must be as binding as the ones required by the subclasses
- Postconditions and invariants in a subclass must be at least as binding as the ones defined for its superclass

Moreover, Liskov's Substitution Principle does not allow for the presence of more exceptions in subclasses than in superclasses.

## Rules for specifying subclasses

How can we ensure that an extension contract is compatible with its superclass's contract?

There are *three main properties* that the specification must have in order to be compatible:

| Rule           | Description                                                                                                                                            | Explaination                                                                                                                                                    |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Signature rule | A subtype must have all the methods of the supertype and signatures of the methods of the subtype must be compatible with the ones from the supertype. | This rule guarantees that the base class's contract still applies. In other words, the syntax of the extension is compatible with the syntax of the base class. |
| Method rule    | Calls to methods of the subtype must behave like calls to the corresponding methods of the supertype.                                                  | This rule guarantees that the contract of every single inherited method is compatible with the contract of the original methods.                                |
| Property rule  | The subtype must preserve all properties (e.g. *public invariants*) of the objects in the supertype.                                                   | This rule verifies that the specification as a whole is compatible with the original specification.                                                             |

### Signature rule

>A subtype must have all the methods of the supertype and signatures of the methods of the subtype must be compatible with the ones from the supertype.

The signature rule guarantees **type safety**: each correct call for the supertype is also correct for the subtype.

The signature rule is *statically verifiable*.

In Java, specifically in versions older than 1.5, the signature rule is defined as follows:

>A subtype must have all the methods of the supertype and the signatures of the methods of the subtype must be identical to the corresponding signatures of the supertype. However, a subtype method may have fewer exceptions in the signatures.

### Method rule

>Calls to methods of the subtype must behave like calls to the corresponding methods of the supertype.

For a call method of the subtype to have the same effect as the corresponding method of the supertype, the two methods only need to have the same specification.

Unfortunately, it's often necessary to change the specification.

When applying this rule, the [*weakest precondition* rule](Strength%20of%20logical%20conditions.md#Weaker%20precondition%20rule) and the [*strongest postcondition* rule](Strength%20of%20logical%20conditions.md#Stronger%20postcondition%20rule) apply.

### Property rule

>The subtype must preserve all properties (e.g. *public invariants*) of the objects in the supertype.

This rule refers to the *general properties* included in the class contract and those that can be derived from the method contracts. These properties do not always appear explicitly in the methods and they are typically defined in the overview or as public invariants of the supertype.

It should be noted that all new or redefined methods of the subtype, including constructors, retain the [*evolutionary*](Abstract%20Data%20Types.md#Abstract%20properties) and [*invariant*](Abstract%20Data%20Types.md#Abstract%20invariants) properties of the supertype, which can be observed through the [*public observer methods*](Abstract%20Data%20Types.md#Categories%20of%20operations) of the superclass.

## JML Extensions

A JML contract can be extended to add more pre and postconditions in subclasses through the keyword `@also`:

```java
/*@ also
 *@ requires (* subclass precondition extension *);
 *@ ensures (* subclass postcondition extension *);
 */
public class SubClass extends Class {
	// Class implementation
}
```

When extending a JML contract:

- The `@requires` part of the extension is added via *disjunction* to the base class's precondition, making the resulting precondition [*weaker*](Strength%20of%20logical%20conditions.md#Logical%20operators%20and%20strength%20of%20conditions)
- The `@ensures` part of the extension is added via *conjunction* to the base class's postcondition, making the resulting postcondition [*stronger*](Strength%20of%20logical%20conditions.md#Logical%20operators%20and%20strength%20of%20conditions)
