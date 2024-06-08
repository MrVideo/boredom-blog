---
title: 'Procedural Abstraction'
draft: false
type: 'page'
toc: true
mathjax: true
---

---

## Abstraction

> Abstraction: Ignoring details that are not essential to the intended purpose

Computer science is entirely based on the concept of abstraction. In fact, the concepts of variables, types and control instructions are all abstractions.

We can define four types of abstractions for software design:

- Abstractions on operations: **procedural abstractions**
- Abstractions on data: **Abstract Data Types**
- Control Abstractions: like iterators
- Abstraction from individual types to *families* of types: inheritance

### Abstraction mechanisms in software design

#### Abstraction by parametrization

Parametrization is a way to generalize modules so that they can be used on different data.

Let's look at an example: here's some repeated code with the same function:

```java
if(a < 0) a = -a;

if(varB < 0) varB = -varB;

if(anotherVar < 0) anotherVar = -anotherVar;
```

We can define an abstraction and call it each time by applying it to parameters:

```java
public static int abs(int p) {
	if(p < 0) return -p;
	return p;
}
```

#### Abstraction by specification

*Specification* is a description of *what* the module does, regardless of *how*. It does not matter how the code implements a given function as long as it behaves as expected.

For example, we could've programmed the `abs` method from before in many different ways:

```java
public static int abs(int p) {
	return (p < 0) ? -p : p;
}

public static int abs(int p) {
	return p * sgn(p);
}

public static int abs(int p) {
	return sqrt(p * p);
}
```

These are all abstractions that perform the same function.

The advantages of abstraction by specification are:

- Locality: the specification can be read or written without the need to examine the implementation and it allows for programmer independence
- Modifiability: abstraction can be reimplemented without effect on customers and it enables simple and inexpensive maintenance when the specification does not change

## Procedural Abstraction

Procedural abstraction defines a complex operation on generic data by specification.

It can generally have several implementations that meet its specification.

A procedural abstraction can be said to represent the equivalence class of all static methods that implements the same specification.

### Specification of procedural abstractions

Procedural abstractions are specified using natural language in a systematic way or through simple mathematical notation. In Java, they are specified through the **Java Modeling Language** (*JML*).

A JML specification is composed of two main parts:

1. `requires` or *precondition* (`pre`): conditions on the parameters under which the specification is defined
2. `ensures` or *postcondition* (`post`): guaranteed effect at the end of the abstraction's execution

Let's look at an example:

```java
/* requires value >= 0 of parameter x
 * ensures returns the square root of x */
public static float sqrt(float x) {
	// Code for sqrt(x)
}
```

Since the precondition requires $x \geq 0$, what happens if the parameter passed to the method is less than zero? In that case, the method is not defined, so any behaviour is acceptable, since the precondition must be verified.

Let's define more thoroughly pre and post conditions:

- The *precondition* of a method tells us what must be true in order to call the method.
- The *normal postcondition* tells us what must be true when the method returns normally (that is without raising exceptions).
- The *exceptional postcondition* tells us what is true when the method returns raising an exception.

### Scheduling by contract

*Contract* is a term often used to describe the specification of procedural abstractions. A contract is composed of pre and post conditions.

A software contract usually looks like this:

```java
/*@ requires x >= 0.0
 *@ ensures JMLDouble.approximatelyEqualTo(x, \result * \result, eps);
 */
 public static double sqrt(double x) {/*Code for sqrt*/}
```

Let's break down the obligations and rights of consumer and implementation defined by this contract:

|                | Obligations                          | Rights                            |
| -------------- | ------------------------------------ | --------------------------------- |
| Customer       | Pass a non-negative value            | Obtain an approximate square root |
| Implementation | Calculate and return the square root | Receive a non-negative argument   |               |                                      |                                   |

A contract can be fulfilled in many ways. For example, in the case of a method to calculate the square root of a given number, the method can use:

- Linear search
- Binary search
- Newton's method

And many more. What changes essentially are *nonfunctional properties*, such as:

- Efficiency
- Memory consumption
- Network load

A contract, therefore, abstracts from all implementations, which we can change at a later point of development.

#### More on contracts

For each method, a contract should define what the method requires and what the method ensures.

The contracts are more abstract than the code and often mechanically verifiable, so as to facilitate debugging (in this case, contracts must always be updated).

Code is a bad language for making contracts, as it fails to distinguish between intention and reification. Instead, contracts allow the provider to describe the intention of the method, the seller to freely change the details of the supply and they communicate what customers should expect.

Generally, natural language can be abiguous, so it's better to use a specific language to write contracts.

### Contract languages

Writing specifications is done through mathematical notation. This brings some advantages:

- Specifications are not ambiguous
- Code and specifications can be verified if the notation is executable

Specifications can be verified through **assertions**, checks that can be inserted into compiled Java code that verify the validity of a specification. This is very useful especially in the testing and debugging phases.

Assertions are boolean expressions that are verified at runtime. If the expression returns true, the execution goes on; if the expression returns false, the system generates an unrecoverable error: `AssertionError`, and the program terminates.

Assertions can be enabled or disabled at compile time.

An assertion has a very simple syntax:

```java
assert /*boolean expression*/;
```

Assertions can be used to verify postconditions. For example:

```java
//@ ensures (*if x in a, returns the index at which x is located,
//@         else returns -1*)
public static int search(int a[], int x) {
	// Search code
	assert (i == -1 || a[i] == x); // Partial check during the execution
	return i;
}
```

If the implementation returns a value that does not match the index at which `x` is located, then `AssertionError` is thrown.

## JML: Java Modeling Language

**JML** (*Java Modeling Language*) is a language for formal specification description, specialized for Java.

JML specifications are contained in *annotations*, represented by this comment syntax:

```java
//@ this is an annotation

/*@ this is a
  @ multiline
  @ annotation */
```

### Assertions in JML

JML assertions are like Java boolean expressions, but:

- They cannot have side effects
	- No unary operators can be used
	- Only *pure* methods can be called (that is, that have no side effects)
- They are preceded by appropriate keywords
- They can use some extensions to Java

Here is some special syntax for JML assertions:

| Syntax        | Semantics                   |
| ------------- | --------------------------- |
| `a ==> b`     | a implies b                 |
| `a <== b`     | b implies a                 |
| `a <==> b`    | a iff b                     |
| `a <== ! ==>` | !(a <==> b)                 |
| `\old(E)`     | value of E in the pre-state |

#### `requires` and `ensures`

In JML:

- `requires` establishes the precondition
- `ensures` establishes the postcondition
- `\result` indicates the value returned at the end of the execution of the method

Let's see an example below:

```java
//@ requires in >= 0:
//@ ensures Math.abs(\result * \result - in) < 0.0001;
public static float sqrt(float in);
```

If the `requires` clause is omitted, the method has no precondition, which means it does not impose any condition on the input parameters (it is essentially the same as writing `requires true`).

If the `ensures` clause is omitted, the method has no postcondition, which means it does not promise anything about its results (it is essentially the same thing as writing `ensures true`).

#### Managing informality

In JML assertions, comments can be entered inside `(**)` structures, which mean that whatever is written between the asterisks is always true. For example:

```java
//@ ensures (* a is a permutation of the original value *)
//@         && (* a is sorted by increasing values *);
public static void sort (int[] a) { /* Code */ }
```

This makes writing complex contracts in JML much easier, at the cost of losing executability.

It is also possible to write a JML postcondition that is weaker than the exact one but still meaningful, rather than just writing a comment. This is done through *mixed* descriptions:

```java
/*@ requires x >= 0:
  @ ensures \result >= 0 &&
  @         (* \result is an int approximation of square root of x *);
  @*/
public static int isqrt(int x) { /* Code */ }
```

#### Managing mutable objects

What happens if the objects referred to by the variables are mutable?

To denote the state of the variables before and after a given operation, we can use the `\old` clause. This returns the value assumed by the expression passed to it at the time of the call.

Let's look at an example: this is a method that reverses the state of ignition of a car:

```java
//@ ensures p.turnOn() <==> !\old(p.turnOn());
public static int invertStatus(Car p) { /* Code */ }
```

#### `assignable`

The keyword `assignable` is used to signal that a parameter can be changed:

```java
//@ assignable a[*];
//@ ensures (* a is a permutation of the original value of a *)
//@         && (* a is sorted by increasing values *);
public static void sort(int[] a) { /* Code */ }
```

If a method has no side effects, it's possible to write `\nothing` after `assignable` like so:

```java
//@ assignable \nothing;
//@ ensures (* x is in a *) && x == a[\result]
//@         || (* x is not in a *) && \result == -1;
public static int search(int[] a, int x) { /* Code */ }
```

If the `assignable` clause is omitted, there is no promise about non-modification, as if all parameters are assignable.

### Exceptions

As we've said before, there are two types of postcondition:

- **Normal** postcondition: it tells us what must be true when the method returns *normally*
- **Exceptional** postcondition: it tells us what must be true when the method returns *raising an exception*

Let's look at how this is rendered in JML:

```java
//@ assignable \nothing;
//@ ensures x == a[\result];
//@ signals (NotFoundException e) (* x is not present in a *);
public static int search(int x, int[] a) throws NotFoundException {/*Code*/}
```

Given the example above, we can see that there are two possible *states* when the execution of the method terminates:

1. The normal postcondition is true and no exception is thrown
2. The normal postcondition is false and the method throws an exception, making the exceptional postcondition true

A `signals` clause must be provided **for each exception that a method can throw**.

Having the following clauses:

```java
//@ ensures A;
//@ signals (Exception e) B;
```

is like having the postcondition:

```java
// A && (* no exceptions *)
// || B && (* exception e is thrown *)
```

Note that the exception can be thrown if, in addition to condition B, condition A is also true.

### Complete Scheme

The JML scheme that we are going to use answers these four questions:

- What is required? (i.e. inputs that are not `null`)
- What is modified? (Do inputs change during runtime?)
- What is the normal behaviour and what does it return?
- What exceptions are thrown and in what conditions?

The schema will look like this:

```java
visibility class myClass {
	// OVERVIEW: general comments on the class
	//@ assignable <editable parameters>
	//@ requires   <precondition>
	//@ ensures    <postcondition>
	//@ signals    <exceptions>
	visibility static returnType p1(/*parameters*/) {
		// Code
	}
}
```

### Partial procedures

A procedure is *partial* if it has a non-empty precondition, which means that it has a specified behaviour only for a subset of the argument's domain.

For example:

```java
//@ requires n >= 0;
//@ ensures (* \result is the factorial of n *);
public static int fact(int n)
```

This makes the operation unsafe, since the method could run without meeting the precondition and give out a result that is incorrect to other parts of the program.

Partial procedures compromise the *robustness* of programs. A program is robus if it has a reasonable or well-defined behaviour even when errors occur.

For partial procedures, behaviour outside the preconditions is simply not defined by the specification. If a procedure is not defined for some values, its execution with those values could lead to unpredictable behaviour.

To achieve robust programs, procedures must be total.

For public methods of public classes, it's good practice to drop the `requires` clause and throw exceptions when `requires` is violated. Exceptions are included in the `throws` Java clause:

```java
public static int fact(int n) throws NegativeException {
	if(n < 0) throw new NegativeException();
	// Code
}
```

Let's look at another example:

```java
// Worse version:

//@ requires x != null;
//@ ensures a[\result].equals(x);
//@ signals (NotFoundException e) (* x is not in a *);
public static int search(String x, String[] a) throws NotFoundException {/*...*/}

// Better version:

//@ ensures x != null && a[\result].equals(x);
//@ signals (NotFoundException e) (* x is not in a *)
//@ signals (NullPointerException e) x == null;
public static int search(String x, String[] a) throws NullPointerException, NotFoundException {/*...*/}
```

There are some cases in which `requires` is left in the JML annotation, like so:

```java
//@ requires (* a sorted ascending *);
//@ ensures a[\result] == x;
//@ signals (NotFoundException e) (* x is not in a *);
public static int binarySearch(int a[], int x) throws NotFoundException {
	// Code
}
```

In this case, checking for the array to be ordered is a long task and it's not very efficient to reimplement it here. Generally, no exception is thrown when the caller can check whether the precondition is met better than the callee or when the callee would perform much worse checking the same condition.

### Collection methods and quantifiers in JML

When talking about the elements in a collection from the Java Collections Framework, JML offers some methods that have no side effects to check their properties, like:

- `equals`
- `contains`
- `containsAll`
- `get`
- `sublist`

This is often a simple procedure, but not in every case:

```java
//@ ensures a.containsAll(\old(a.sublist(0, a.size()))) &&
//@         \old(a.sublist(0, a.size())).containsAll(a) &&
//@         (* sorted by increasing values *);
public static void sort(ArrayList<Integer> a) { /*...*/ }
```

Here, `a.sublist(0, a.size())` returns a new list that contains all the elements of `a`. Thus, `a.containsAll(\old(a.sublist(0, a.size())))` is true if `a` eventually includes all the elements that were in `a` at the time of the call. `\old(a.sublist(0, a.size())).containsAll(a)` is true if, at the time of the call, `a` included all elements that were in `a` when the method ended.

JML extends Java by also including some quantifiers, like:

- The universal quantifier `\forall`
- The existential quantifier `\exists`
- Quantifying functions:
	- `\sum`
	- `\product`
	- `\min`
	- `\max`
- Numerical quantifier `\num_of`

#### `\forall`

The syntax used with quantifier is similar with all of them, so we will be writing it here just once:

```java
(\forall variable; range; condition)
```

This means:

> For all possible values of the variable in range, condition must be true.

For example, to say that an array is sorted by increasing values, we can write:

```java
(\forall int i; 0 <= i && i < a.length - 1; a[i] <= a[i + 1])
```

Let's look at an example with collections: to say that all freshmen have a referent, we can write:

```java
(\forall Student s; juniors.contains(s); s.getAdvisor() != null)
```

#### `\exists`

Let's look at a couple of examples:

```java
// An array includes a negative element:
(\exists int i; 0 <= i && i < a.length; a[i] < 0)

// Some freshmen don't have an advisor:
(\exists Student s; juniors.contains(s); s.getAdvisor() == null)
```

One complete schema would look like this:

```java
//@ ensures (\exists int i; 0 <= i && i < a.length; a[i] == x) ? x == a[\result]
//@                                                            : \result == -1;
//@ assignable \nothing;
public static int search(int x, int[] a)
```

#### `\num_of`

This quantifier has a slightly different syntax from the others:

```java
(\num_of int i; P(i); Q(i))
```

This means:

> The total number of `i` for which `P(i) && Q(i)` is worth.

Let's look at some examples:

```java
// Number of positive elements in array a:
(\num_of int i; 0 <= i && i < a.length; a[i] > 0)

// No element of a appears more than twice in a:
(\forall int i; 0 <= i && i < a.length; 
	(\num_of in j; i < j && j < a.length; a[i] == a[j]) <= 1);
```

#### Other quantifiers

We will define the last four quantifiers through examples:

```java
(\sum int i; 0 <= i && i < 5; i + 1)    <==> 1 + 2 + 3 + 4 + 5
(\product int i; 0 < i && i < 5; i * i) <==> 1 * 4 * 9 * 16
(\max int i; 0 <= i && i < 5; i * i)    <==> 16
(\min int i; 0 <= i && i < 5; i - 1)    <==> -1
```
