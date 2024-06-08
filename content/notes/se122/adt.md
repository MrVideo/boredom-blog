---
title: 'Abstract Data Types'
draft: false
type: 'page'
toc: true
mathjax: true
---

---

## Data abstraction by specification

A new data type for which possible values and operations have been specified (known as *Abstract Data Type*, or **ADT**) is a *data abstraction*.

Abstracting from the details of value representation and operation implementation, the rest of the program depends only on the type specification, not its implementation. It therefore allows *locality* and *modifiability*.

### Locality and Modifiability

Using a specification instead of an implementation:

- Promotes independent development of different parts of the program
- Limits the impact of any of the changes (which remain localized to the type implementation, as long as the specification does not change)
- Allows implementation and representation details to be deferred to more advanced stages of the project

### Interface specification of an ADT

A specification is composed of *syntax* and *semantics*. The method signature (or interface construct) defines only the syntax, while for semantics it is not enough to specify methods as if they were procedural abstractions, since these act on state variables.

### JML for specifying classes

Abstract Data Types divide specification from implementation.

Classes are the equivalent of ADTs in object-oriented languages. However, the separation between specification and implementation introduced by Java classes is not always sufficient.

However, when JML is added to the mix, Java is able to conveniently define abstractions about data.

#### Visibility and pure methods

Only the public elements of a method and class can appear in the JML specification of a public, non-static method.

A *pure method* is a non-static method that does not have side effects; it's declared in JML through the keyword `pure`.

When a pure method is declared, `assignable \nothing` applies, but the state does not change either. Furthermore, the keyword `pure` allows you to call the method in JML.

A pure method can only call other pure methods and constructors can also be declared pure: they can initialize attributes declared in the class, but they cannot modify anything else.

Let's see an example of the method `size()`, which returns the number of elements in a container (which means it is a pure method):

```java
//@ ensures (* \result is cardinality of this *)
public int /*@ pure @*/ size() { /* Code */ }
```

Pure methods allow the user to *observe* the state of an object.

## Specification of data abstractions

### Example of a data type specification: `IntSet`

Let's see an example of data type specification.

We want to create a container which represents a *set of integers* (`IntSet`).

The possible values that this container can hold are all finite sets of integers of any cardinality, so for example $\{1, 10, 35\}$ or $\{7\}$.

We want to define the following operations on a given set `I`:

- Construction: creates `I` and initializes it as an empty set
- `void insert(int x)`: adds `x` to the elements of `I`
- `void remove(int x)`: removes `x` from `I`
- `boolean isIn(int x)`: returns whether `x` is in the set or not
- `int size()`: returns the cardinality of `I`
- `int choose()`: returns any element of `I`

First of all, let's specify the *observers*, pure methods that return state information:

```java
public class IntSet {
	// OVERVIEW: unlimited and modifiable sets of integers;
	// i.e.: {1, 2, 10, -55}
	
	// observers:

	//@ ensures \result == (* x is among the elements of this *);
	public /*@ pure @*/ boolean isIn(int x) { }

	//@ ensures (* \result is cardinality of this *)
	public /*@ pure @*/ int size() { }

	//@ ensures this.isIn(\result) && this.size() > 0;
	//@ signals (EmptyException e) this.size() == 0;
	public /*@ pure @*/ int choose() throws EmptyException { }
```

> Note that observers are often defined with a comment because they are very difficult to define with other operators.

Now, let's look at *builders* (constructors) and *mutators* (methods that modify an object):

```java
	// constructors:
	
	//@ ensures this.size() == 0;
	public IntSet() { }
	
	// mutators:
	
	//@ ensures this.isIn(x)
	//@ && size() == \old(size()) + \old(isIn(x) ? 0 : 1)
	//@ && (\forall int y; x != y; \old(isIn(y)) <==> isIn(y));
	public void insert(int x) { }

	//@ ensures !this.isIn(x)
	//@ && size() == \old(size()) - \old(isIn(x) ? 1 : 0)
	//@ && (\forall int y; x != y; \old(isIn(y)) <==> isIn(y));
	public void remove(int x) { }
}
```

#### Remarks

- The specification is based on common knowledge of sets.
- The specification can be compiled if appropriate returns are added, but does not execute anything since the bodies of the methods are empty. This is useful for type checking; the bodies will be filled only at the time of implementation.
- The specification describes when to throw exceptions.

### Use of ADTs

The specification must be sufficient to be able to use the abstraction without knowing the implementation. For example:

```java
//@ ensures (* returns IntSet with all and only the elements of array a *)
public static IntSet getArray (int[] a) throws NullPointerException { }
```

This function can be easily implemented just using the public methods of `IntSet`:

```java
IntSet s = new IntSet(); // By specification, s is empty
for(int i = 0; i < a.length; i++) {
	s.insert(a[i]);      // By specification, a[i] is inserted in s
}
return s;
```

### Another example: `Poly`

Let's look at the specification to represent a polynomial with integer coefficients.

Polynomials are a combination of monomials obtained through sum, subtraction and multiplication.

The methods we want to implement are:

- Construction: creates a polynomial of a given degree and coefficient. As a special case, the zero polynomial is instantiated.
- `public int degree()`: returns the degree of the polynomial
- `public int coeff(int d)`: returns coefficient of the term of degree `d`
- `public Poly add(Poly q)`: restores sum of this and `q`
- `public Poly sub(Poly q)`: restores subtraction of this and `q`
- `public Poly mul(Poly q)`: restores product of this and `q`

Let's create this ADT:

```java
/*@ pure @*/ public class Poly {
	// OVERVIEW: immutable polynomials with integer coefficients

	// observers:

	//@ ensures (* \result is the degree of the polynomial *);
	public int degree() { }

	//@ requires d >= 0;
	//@ ensures (d > degree()
	//@ ? \result == 0
	//@ : (* \result is the coefficient of the term of degree d *));
	public int coeff(int d) { }

	// constructors:

	//@ ensures this.degree() == 0 && this.coeff == 0;
	public Poly() { }

	// monomial of degree n and coefficient c:
	//@ ensures n >= 0 && this.coeff(n) == c && this.degree() == n &&
	//@ (\forall int i; 0 <= i && i < this.degree(); this.coeff(i) == 0);
	//@ signals (NegativeExponentException e) n < 0;
	public Poly(int c, int n) throws NegativeExponentException { }

	// producers:

	//@ ensures q != null && (* \result == this + q *);
	//@ signals (NullPointerException e) q == null;
	public Poly add(Poly q) throws NullPointerException { }

	//@ ensures q != null && (* \result == this - q *);
	//@ signals (NullPointerException e) q == null;
	public Poly sub(Poly q) throws NullPointerException { }

	//@ ensures q != null && (* \result == this * q *);
	//@ signals (NullPointerException e) q == null;
	public Poly mul(Poly q) throws NullPointerException { }

	//@ensures (* \result == -this *);
	public Poly minus() { }
}
```

The `Poly` class, if implemented, can be used without knowing its implementation, but only its specification.

For example, let's write a program that reads a polynomial from the input:

```java
public static void main(String[] args) throws java.io.IOException, NegativeExponentException {
	BufferedReader in = newBufferedReader(new InputStreamReader(System.in));
	System.out.println("Enter degree: ");
	
	Poly p = new Poly();
	int g = Integer.parseInt(in.readLine());
	
	for(int i = 0; i <= g; i++) {
		System.out.println("Enter coefficient for " + i + " degree term: ");
		int c = Integer.parseInt(in.readLine());
		p = p.add(new Poly(c, i));
	}
}
```

### Abstract Objects and Concrete Objects

The specification of an abstraction describes an *abstract* object. The implementation of an abstraction describes a *concrete* object.

For example, in the case of `IntSet`, the abstract object is a set of integers, while the concrete object could be an ArrayList, a binary tree or any other data structure.

These two concepts should not be confused with each other.

## Formal specification of collections

### Observers are not enough

In general, the concrete state of class objects is not visible, so it should not be used in the specification. The abstract state, on the other hand, is observable through observer methods and thus usable in a specification.

However, observer methods are often not sufficient to describe pre and post states, because they don't fully capture the abstract state. This often happens with collections.

For example, let's look at the specification of the push and pop operations for a stack:

```java
public class Stack<T> {
	//@ ensures (* \result is number of elements in this *)
	public int size() {/*code*/}

	//@ requires size() > 0;
	//@ ensures (* \result is top of the stack *)
	public /*@ pure @*/ T top() {/*code*/}

	//@ ensures size() == 0;
	public Stack() {/*code*/}

	//@ ensures size() == \old(size() + 1)
	//@ && top() == x
	//@ && (* elements below top unchanged *);
	public void push (T x) {/*code*/}

	//@ requires 0 < size();
	//@ ensures size() == \old(size()) - 1
	//@ && (* deletes element from the top of the stack *);
	public void pop() {/*code*/}
}
```

The specification of the stack is understandable but not fully formalized. Observers are not enough to define the rest of the specification.

To formalize the specification, it's possible to define a *typical abstract object* (**OAT**) only in the specification, which more precisely defines the abstract object defined by the class specification. Operations can then be described as effects on an OAT.

Let's look at the stack example again:

```java
public class Stack<T> {
	//@ public List<T> oat;
	//@ Typical object oat is [x_0, x_1, ..., x_n], n >= 0, x_i in T, x_n is the top.

	//@ ensures \result == oat.size();
	public int size() {/*code*/}

	//@ requires size() > 0;
	//@ ensures \result == oat.get(size() - 1);
	public /*@ pure @*/ T top() {/*code*/}

	//@ ensures size() == 0;
	public Stack() {/*code*/}

	//@ ensures size() == \old(size() + 1)
	//@ && top() == x
	//@ && \old(oat.sublist(0, size())).equals(oat.sublist(0, size() - 1));
	public void push (T x) {/*code*/}

	//@ requires 0 < size();
	//@ ensures size() == \old(size()) - 1
	//@ && oat.equals(\old(oat.sublist(0, size() - 1)));
	public void pop() {/*code*/}
}
```

## Properties of data abstraction

### Categories of operations

- **Creators**: they produce new objects from scratch
	- They are builders
	- Not all constructors are creators: when they have objects of their own type as arguments, they are producers
	- Usually pure methods
- **Producers**: they create objects of their own type when given other objects of the same type as arguments
	- They are usually pure as well
- **Modifiers** or **Mutators**: they modify objects of their own type
	- They don't have `assignable` statements in JML
	- They are never pure
- **Observers**: they return results of other types when given objects of their own type as arguments
	- They are typically declared as pure
	- Sometimes they are combined with producers or mutators

### Adequacy of a type

A type is *adequate* if it provides sufficient operations for the type to be used efficiently.

A simple adequacy check could be the following:

- If the type is at least mutable, it needs creators, observers and mutators
- If the type is at least immutable, it needs creators, observers and producers
- If the type must be fully populated, using creators, producers and mutators must make it possible to get every possible abstract state

Even if totally populated, check whether efficiency can be improved by adding some additional operations.

Adequacy is an informal concept and it depends on context. If context is limited, only a few operations are needed.

### Abstract properties

Abstract properties are observable in public methods. There are two main categories of properties:

- **Evolutionary** property: there is a relationship between an abstract observable state and the next
- **Invariant** property

#### Abstract invariants

We ignore implementation and only use specification to demonstrate abstract invariants, which are a formalization of an abstract property.

An abstract invariant is a condition that must always be verified for the abstract object.

Abstract invariants must be derivable from the class method specification.

In JML, they are called *public invariants*. They can only use public attributes and methods of a class:

```java
//@ public invariant this.size() >= 0;
//@ public invariant this.degree() >= 0;
```

A useful abstract invariant can be used to verify if a triangle is degenerate:

```java
//@ public invariant longest() < shortest() + middle()
//@ && shortest() * middle() * longest() > 0;

//@ ensures (*returns the length of the shortest side *)
public float shortest() { }
//@ ensures (*returns the length of the middle side *)
public float middle() { }
//@ ensures (*returns the length of the longest side *)
public float longest() { }
```

Abstract properties are useful because users of the class can use properties as assumptions on its behaviour. For example:

- A stack has the LIFO evolutionary property
- A triangle is not degenerate
- A polynomial has a degree greater or equal to zero
- An integer set has a positive cardinality

