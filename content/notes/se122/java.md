---
title: 'The Java Programming Language'
draft: false
type: 'page'
toc: true
mathjax: true
---

---

## Introduction

Java is an object-oriented programming language designed by Sun Microsystems (now Oracle) between 1995 and 1996.

The main features of the Java programming language are:

- Java is **object-oriented**
- Java is **platform-independent**
- Java is **safe**: it runs its programs in a sandbox
- Java has **great distribution support**

## Classes and abstractions

A Java program is organized as a set of **classes**. Each class corresponds to a type declaration.

A class contains declarations of variables (*attributes*) and functions (*methods*). The values of attributes characterize individual instances (*objects*) of a class. Methods are used to manipulate objects.

Let's look at an example of a class:

```java
public class Date {
	private int day;
	private int month;
	private int year;
	
	public int readDay() { }
	public int readMonth() { }
	public int readYear() { }
}
```

A class in Java is similar to a `struct` in C, but some *fields* can be functions.

A class can be viewed as a *user-defined type* that specifies the operations that can be used on the type itself. The type can then be used to declare other variables. A class defines an **abstract data type** (*ADT*).

### Attributes and methods

The data structure of a class is defined by its **attributes**. Taking a peek at the `Date` class from before, `day`, `month` and `year` are `Date`'s attributes. In Java, these are also called **instance variables**.

The operations defined in the class are called **methods**. Methods define the behavior of objects that belong to a class.

### Objects and state

All objects of the same class have the same structure: the number and type of their attributes is the same. When the program is executed, each object is characterized by a **state**, which depends on the value of the object's attributes.

The state of objects can change over time through the invocation of appropriate methods. There are, however, some objects which are **immutable**: they cannot change state once they have been instantiated. One example is the default class `String`.

### Dot notation

Attributes and methods can be accessed through **dot notation**. For example:

```java
Date d;
int x;

x = d.readDay();
```

In this code snippet, we instantiate a `Date` object and then call the method `readDay` on it through dot notation.

To change the state of an object, a method must be able to access the fields of the object on which it was called. When defining a method, the user can refer directly to attributes and methods of the object he's working on:

```java
public void dayAfter() {
	day++;
	if(day > 31) {
		day = 1;
		month++;
	}
	if(month > 12) {
		month = 1;
		year++;
	}
}
```

### Private and public

Through the public methods of a class, it is possible to check the state of an object, as is the case for `readDay` in the class `Date`. However, the private data inside a class cannot be accessed directly, so the following code results in a compilation error:

```java
Date d;

if(d.month == 12) {
	// Compilation error
}
```

### Abstract classes and methods

An *abstract class* is a class that cannot be instantiated into an object.

Abstract classes are very useful to create high level abstractions, since they can contain one or more *abstract methods*: methods that do not have an implementation.

### Enumerations

Enumerations are similar to normal classes and they are used to define a small group of constants. Enumeration constants are always `public`, `static` and `final`.

Enumerations can be declared to, for example, model sets with a small cardinality. For example:

```java
enum Size {SMALL, MEDIUM, LARGE, EXTRA_LARGE}

Size s = Size.MEDIUM;
```

In this example, `Size` is a class with exactly four instances. No more instances can be built for the class `Size`. Moreover, comparisons can be done through the primitive type comparison operator `==`.

An object instantiated from an enumeration class can only be either `null` or one of the values defined for that class.

An enumeration class can contain constructors, methods and attributes, like any other class in Java. They allow for more information to be stored alongside the enumeration value. There is one key difference from normal classes though: you cannot construct generic objects through enumeration constructors.

Here is an expansion of the example from earlier:

```java
public enum Size {
	SMALL("S"), MEDIUM("M"), LARGE("L"), EXTRA_LARGE("XL");
	private String abbreviation;
	
	private Size(String abbreviation) {
		this.abbreviation = abbreviation;
	}
	
	public String getAbbreviation() {
		return abbreviation;
	}
}
```

Every enumeration class offers the following methods:

- `ordinal()`: returns the position of an enumeration constant
- `compareTo()`: compares enumeration constants based on their ordinal values and returns their difference
- `valueOf(String name)`: returns the enumeration constant with name `name`
- `toString()`: returns the representation of the enumeration constant in `String` format
- `values()`: returns an array containing all the values defined in the class
- `name()`: returns the name of the enumeration constant in `String` format

In order to iterate through enumeration values, it is possible to use a *for each* loop, like the one used for arrays:

```java
enum Color { RED, WHITE, BLUE }

for(Color c : Color.values()) { }
```

## Variables

### Primitive types and reference types

In Java there are many different primitive types for variables. You can see them below with their default values:

| Data Type | Size        | Default Value |
| --------- | ----------- | ------------- |
| `byte`    | 8 bit       | `0`           |
| `short`   | 16 bit      | `0`           |
| `int`     | 32 bit      | `0`           |
| `long`    | 64 bit      | `0L`          |
| `float`   | 32 bit      | `0.0f`        |
| `double`  | 64 bit      | `0.0d`        |
| `char`    | 8 bit       | `\u0000`      |
| `String`  | $n \cdot 8$ bit | `null`        |
| `boolean` | 1 bit            | `false`       |

Variables of primitive type directly contain their value while other types only **reference** the values. Every variable declared by a class contains a reference to an object, which is akin to a pointer to a memory address in C.

Sometimes, it is more useful to instantiate primitive types as reference types instead. Java provides some default classes in the package `java.lang` to do just that:

- `Integer`
- `Character`
- `Float`
- `Long`
- `Short`
- `Double`

These are immutable types.

Converting a primitive type into the corresponding reference type (for example, from `int` to `Integer`) is an operation called **boxing** (or *autoboxing*); the opposite is **unboxing** (for example, going from `Double` to `double`). These two operations are done automatically by Java when using the assignment operator:

```java
Character ch = 'a'; // Autoboxing
```

### Declaration and initialization

The declaration of a reference variable does **not** allocate space for an object, but only for its reference. A reference variable is always initially assigned the reference `null`, to indicate that the variable is not yet associated with any object.

A parameter or local variable cannot be used without being initialized first: the Java compiler statically detects lack of initialization and throws a compilation error when this happens.

### Constant attributes

An attribute of a class can be declared constant through the keyword `final`.

Conventionally, constant variables have capitalized names:

```java
final double PI = 3.14159265;
```

### `new` keyword and constructors

The construction of an object is a dynamic operation made possible by the `new` operator, which is used like so:

```java
Date d = new Date();
```

The code snipped above:

- Constructs a new object of type `Date`
- Returns the reference to the newly created object, which is stored in the variable `d`

`Date()` is a special method called **constructor**. A constructor has the same name as the class it creates objects of.

Let's take a look at a specific case:

```java
Date date;

date = new Date(); // Object 1
date = new Date(); // Object 2
```

When an object is created twice, as seen above, the initial object (*object 1*) **is not deleted immediately** once the second (*object 2*) is instantiated: only the reference to the object is lost. The first object, which cannot be accessed anymore, will eventually be destroyed by the **garbage collector**: a system routine that automatically frees memory when needed.

If a class does not contain a definition for a constructor, the compiler provides a **default constructor**, which has no parameters, that performs the following functions:

- It allocates memory for attributes of primitive type
- It allocates memory for attribute references of user-defined types
- It initializes all allocated variables to their default value

However, when the developer provides a custom constructor, the compiler does not add the default one.

It is also possible to invoke a constructor inside a constructor, but it must be the first instruction:

```java
public Date(int d, int m, int y) {
	if(validDate(d, m, y)) {
		day = d;
		month = m;
		year = y;
	}
}

public Date(int d, int m) { // This constructor provides a default year
	this(d, m, 1900);
}
```

### Assignment and sharing

The assignment operator `=` performs different operations depending on what type of variable it is used on: with primitive types, it copies the value from one variable to the other; with reference types, it only copies the **reference** of the object from one variable to the other.

If an object is accessed by two different variables, we say the variables **share** that object. The assignment of reference type variables generates sharing. To better understand this, let's take a look at the following snippet of code:

```java
Date d1, d2;

d1 = new Date(20, 3, 2007);

d2 = d1; // Sharing
d2.dayAfter();

System.out.println(d1.getDay()); // This prints the date 21/03/2007
```

When two reference variables share an object, they share the **reference** to the same object. This means that, if the object is mutable, changes applied to that object through one of the two variables are reflected on the other variable as well.

### Static attributes

Attributes in a class can be declared as `static`. This means that they belong to the class of the object, not to the particular object that has been instantiated.

Static attributes can be accessed by any [method](#Static%20methods).

### Comparisons between references

The comparison operator `==` compares reference values, it does not compare the objects themselves. Let's take a look at some code:

```java
Date d1 = new Date(1, 12, 2001);
Date d2 = new Date(1, 12, 2001);

if(d1 == d2) { // This returns false
	// Code
}
```

The `if` clause returns `false` because `d1` and `d2` are two different objects: even though the values of their attributes are the same, they are instantiated in two different moments, which means that the constructor for `Date` allocated two different memory spaces for the objects. Since the comparison operator compares references and not objects, the two memory addresses contained in the variables are different, which means that `d1 == d2` returns `false`.

The only way to compare two objects on their attribute values is using the `equals()` method. Let's look at an example below:

```java
String a = new String("Alberto");
String b = new String("Hello");
String c = new String("Hello");

System.out.println(a.equals(b)); // Prints "false"
System.out.println(b.equals(c)); // Prints "true"
System.out.printls(b == c);      // Prints "false"
```

### Strings

In Java, strings are objects of the class `String`, which is immutable and has two constructors:

- `String()`
- `String(String s)`

Strings can be chained through the `+` operator.

The `String` class also contains some useful methods to interact with strings:

- `int length()` returns the length of a string
- `char charAt(int index)` returns the character at the specified index position
- `String substring(int startIndex)` returns the substring starting from `startIndex` (a version of the method that contains `endIndex` is also defined)

### Stack allocation and heap allocation

When a method ends its execution, all variables in the corresponding activation record on the stack are destroyed. However, objects that are created on the heap can still be available after a method terminates. For example:

```java
public Date foo() {
	Date d = new Date(1, 1, 2001); // Deallocated when foo() terminates
	return d;
}

public static void main(String[] args) {
	Date x = foo(); // The object created in foo() keeps existing on the heap
}
```

In general, when a method is called:

- Primitive types are directly allocated in the stack
- Reference types are allocated in the heap but referenced in the stack

### Parameter passing in methods

Suppose we have to create a method to copy a `Date` object into another `Date` object. To do so, we must **disambiguate** between the attributes of one object and the other. We use **dot notation** in order to do that:

```java
public class Date {
	private int day;
	private int month;
	private int year;
	
	public void copyIn(Date d) {
		d.day = day; // left: parameter; right: object that performs the call
		d.month = month;
		d.year = year;
	}
}
```

There is also a pseudo-variable, `this`, which is used to reference the object the call is performed in. The code above would be equivalent (although redundant) to this:

```java
public void copyIn(Date d) {
	d.day = this.day;
	d.month = this.month;
	d.year = this.year;
}
```

The `this` pseudo-variable can also be used to return a reference to the current object in a method.

### Array types

Arrays in Java are declared as follows:

```java
int[] i1, i2;
float[] f;
double[] d;
Object[][] objectArray; // Bidimensional array
```

As you can imagine, these arrays are not initialized. That can be done like this:

```java
int[] a = {1, 2, 3};
double[][] m = {{1.3, 2.7}, {1.22, 9.0}};
```

If an array is not initialized, its declaration alone does not allocate space for its future elements. Allocation is done dynamically through the `new` operator:

```java
int[] i = new int[10];
float[][] f = new float[20][10];
Object[] o = new Object[45];
```

If the elements of an array are a reference type, however, the `new` operator will only allocate space for the references to the objects, not for the objects themselves. In order to allocate space for an object as well, the user should allocate the specific element as well:

```java
Person[] personArray; // Declaration (no space allocated)
personArray = new Person[20]; // Initialization (space for references alloc'd)
person[0] = new Person(); // Space for Person object allocated for index 0
```

A user can iterate through the elements of an array in many ways. While iteration via the usual loops is the same as in C, there is one more way to iterate through an array which does not need an index variable:

```java
int sum(int[] a) {
	int result = 0;
	for(int n : a)  // This is read as: "for each n in a"
		result += n;
	return result;
}
```

### Type conversion

In Java, type conversions can happen manually or automatically.

Manual conversions are called *castings* and are written as:

```java
int myVar = (int) otherVar;
```

Casting is always allowed when converting a type to one of its subtypes.

During runtime, it is possible to determine what the dynamic type of an object is through the `instanceof` operator, which is used as follows:

```java
if(myVar instanceof String)
	System.out.println(myVar);
```

Automatic conversions happen when it is possible to *promote* a type to another without loss of information, for example when promoting an integer to a long integer.

## Methods

Methods are functions that can be embedded into classes. Their syntax is similar to the C declaration of a function:

```java
public class Date() {
	private int day;
	private int month;
	private int year;
	
	public void getDay() { // Method
		return day;
	}
}
```

Methods can be called through **dot notation**:

```java
Date d = new Date(1, 1, 2001);

System.out.println(d.getDay()); // Prints "1"
```

### Static methods

Some methods can be declared as `static`, much like the `main` method in a Java program. This means that a method does not belong to an instance of a type, but to the type itself.

A static method can only access [static attributes](#Static%20attributes) and methods, while any method can access static attributes and methods.

### Overloading

One class can have **multiple method with the same name**, as long as they differ in the number or type of parameters. Note that the return type is not enough to distinguish two methods. We can see one example of this below:

```java
public class Max {
	// These are all valid declarations
	public int max(int a, int b) { /*Code*/ }
	public int max(int a, int b, int c) { /*Code*/ }
	public double max(double a, double b) { /*Code*/ }
}
```

## Inheritance

In Java, the programmer can establish an **inheritance relationship** between classes with the keyword `extends`:

```java
public class B extends A {
	// Code
}
```

In this case, class `A` is called *base class* (or *ancestor*, *parent*, *superclass*), while class `B` is called *derived class* (or *descendant*, *child*, *heir*, *subclass*).

When a class extends another, the subclass inherits everything that is in the superclass, like attributes and methods, but it can also add new methods and attributes and change the implementation of the superclass's methods: this operation is called **overriding**.

You can take a look at a simple example of inheritance below:

```java
public class Car {
	private String model;
	private boolean on;
	public Car(String model) {
		this.model = model;
		this.on = false;
	}
	public void turnOn() {
		on = true;
	}
	public boolean canStart() {
		return on;
	}
}

public class ElectricCar extends Car {
	private boolean isCharged;
	public ElectricCar(String model) {
		super(model); // This executes the code in the superclass's constructor
		isCharged = true;
	}
	public void recharge() {
		isCharged = true;
	}
	@Override
	public void turnOn() {
		if(isCharged)
			super.turnOn(); // Executes the turnOn method as implemented in Car
		else System.out.println("Low batteries. Recharge.");
	}
}
```

One key factor to note in the example is the usage of the pseudo-variable `super`: it is used to access methods and attributes of the superclass directly, but also to call the superclass's constructor. Note that `super()` must be called as the first operation in any constructor of any subclass if you intend to use it.

Every class in Java inherits from the `Object` class, which means that `Object` is the **topmost** class in Java. This inheritance is useful because it provides some useful methods to all classes:

| Method                                                                        | Description                                                                      |
| ----------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `public final Class getClass()`                                               | Returns the class object of this object                                          |
| `public int hashCode()`                                                       | Returns the hash number for this object                                          |
| `public boolean equals(Object obj)`                                           | Compares the given object to this object                                         |
| `protected Object clone() throws CloneNotSupportedException`                  | Creates and returns the exact copy of this object                                |
| `public String toString()`                                                    | Returns the string representation of this object                                 |
| `public final void notify()`                                                  | Wakes up a single thread that was waiting                                        |
| `public final void notifyAll()`                                               | Wakes up all the threads that were waiting                                       |
| `public final void wait(long timeout) throws InterruptedException`            | Causes the current thread to wait for the specified milliseconds                 |
| `public final void wait(long timeout, int nanos) throws InterruptedException` | Causes the current thread to wait for the specified milliseconds and nanoseconds |
| `public final void wait() throws InterruptedException`                        | Causes the current thread to wait until another thread notifies                  |
| `protected void finalize() throws Throwable`                                  | This method is invoked by the garbage collector before the object is collected   |

### Final classes and methods

If the programmer wants to avoid the creation of subclasses from a specific class, this can be declared as `final`.

Similarly, if a method cannot be overridden by another in a subclass, it can be declared as `final`.

### Simple inheritance and interfaces

Simple inheritance does not allow the user to describe many real world situations, since subclasses can only inherit from one superclass.

Java tries to solve this problem by distinguishing between *inheritance hierarchy* and *implementation hierarchy*, introducing the **interface** construct.

An interface is similar to a class, with some constraints:

- An interface can only have *public, static and final attributes*
- An interface can only have *public and abstract methods*

An interface is declared as shown below:

```java
interface Interface {
	// Public, static and final attributes

	// Public and abstract methods
}
```

The simple inheritance problem can be solved through interfaces because these can inherit from more than one interface:

```java
interface Interface extends Int1, Int2, Int3 {
	// Code
}
```

Furthermore, a class can inherit from one class only, but can *implement* as many interfaces as needed:

```java
public class Class extends SuperClass implements Interface1, Interface2 {
	// Code
}
```

Unless the class that implements one or more interfaces is abstract, then it *must* implement all methods defined in the interfaces.

Starting from Java 8, interfaces can also define and implement static methods.

## Information hiding

### Packages and compilation units

In Java, classes are collected into **packages**, which group classes by defining **visibility rules**.

To understand packages, we must first talk about **compilation units**.

The compilation unit is a file that contains the declaration of one or more classes or interfaces. One of these classes must have the same name as the file itself. Moreover, the file can contain at most one `main` method.

A package can be thought of as a directory containing one or more compilation units. This introduces new aspects to the visibility of names in a Java program. For example, units with the same name can coexist if they are in different packages.

### Class visibility

A class can be either `public` or *friendly*.

A public class is visible to all packages that import the package the class is in. A file can only have one public class and there can be at most one public class for each file.

A friendly class is declared without modifiers before its name and is visible to other classes within the same package. There can be multiple friendly classes in a package.

### Visibility of attributes and methods

What follows is a table showing what a method or attribute is visible to depending on what modifier is on it.

| Modifier    | Class | Package | Subclass | World |
| ----------- | ----- | ------- | -------- | ----- |
| `public`    | Yes   | Yes     | Yes      | Yes   |
| `protected` | Yes   | Yes     | Yes      | No    |
| No modifier | Yes   | Yes     | No       | No    |
| `private`   | Yes   | No      | No       | No    | 

### Good practice in information hiding

Creating a public class, method or attribute is like making a promise to whoever will use that class: that element of the program will always be available and will not change. This promise is very binding, so all properties that should not be modified or deleted should be declared as private or, when needed, friendly.

It is also strongly recommended that the attributes of public classes are declared as private or friendly, so that accidental manipulation is avoided.

## Polymorphism

### Dynamic binding

The ability of syntactic elements to refer to elements of different types is known as **polymorphism**.

Java supports **dynamic binding**, which means that the type of an object is not determined at compile time, but at run time. This is what makes polymorphism possible.

In Java, a class defines an **Abstract Data Type**. If a class defines a type, then its subclasses define subtypes, and an object of the subtype can be substituted for an object of the type. For this reason, Java distinguishes between **static** type and **dynamic** type:

- The static type is the type chosen when declaring a variable
- The dynamic type is the type defined by the constructor used to create the object

Java ensures that this type of substitution does not compromise type safety: the compiler checks whether each object is manipulated correctly according to the static type and the language guarantees that, at run time, no errors will arise when manipulating objects that have a dynamic type that is a subtype of their own static type.

### Overloading and overriding

Knowing the difference between overloading and overriding is important to understand polymorphism better. Let's look at an example below:

```java
public class Point2D {
	public float distance(Point2D p) { }
}

public class Point3D extends Point2D {
	public float distance(Point3D p) { } // This is overloading
}
```

As you can see from the example, `distance` has a different header in the two classes, so declaring `distance(Point3D p)` is not overriding, which requires the same header with a different implementation. It is, in fact, overloading.

## Exception handling

A method should be able to report any problem it encounters while running in order to give meaningful information to the program and the programmer about possible coding errors. This has been done in many ways in different programming languages and some solutions are:

- Terminating the program
- Returning a conventional error code that identifies a problem
- Changing the state of the entire program to an error state
- Using a default method for error handling

These methods are all outdated because they add a great deal of overhead during development.

In object-oriented languages like Java, the normal procedure to notify an error to the user or the programmer is to **raise an exception**. An exception is a special object that is returned by the method once its execution comes to a halt due to an error.

Exceptions are reported to the caller of the method and they might contain some data that can let the caller examine what went wrong in more detail.

Exceptions have a specific type, such as `NullPointerException` and can also be user defined.

### Try/catch constructs

An exception can be *caught* through the **try/catch** construct:

```java
try {
	x = x / y;
} catch (DivisionByZeroException e) {
	// Code used to handle the exception
}

// Instructions to execute after handling the exception
```

Multiple catch blocks can be added to the same try block, to check for more than one exception.

A try/catch block can also include a *finally* branch, which will be executed regardless of how the execution of a catch block goes.

### Propagation of exceptions

When an error occurs and an exception is raised, the block that raised it stops running.

If the block that is halted is a try/catch block and the exception that is raised is included in one of the catch blocks, then the program continues execution in that block to handle the exception. If the catch block terminates its execution and there are more instructions after it, then the program continues from there.

If the block that is halted is not a try/catch block, then the program returns to the previous call in the call stack and tries to find a block that can handle the exception recursively, until it either finds one or not.

If there are no blocks that can handle and exception, then the program is terminated.

### Methods with exceptions

A method can throw any exception that is specified in its signature through the keyword `throws`:

```java
public void myMethod() throws Exception {
	// Implementation
}
```

Methods can raise exception explicitly through the keyword `throw`:

```java
public int factorial(int n) throws NegativeException {
	if(n < 0) throw new NegativeException;
	else if(n == 0 || n == 1) return 1;
	else return (n * factorial(n - 1));
}
```

### Types of exceptions

Exceptions are defined via classes. Specifically, the class `Exception` is a subclass of `Throwable`.

There are two types of exceptions:

| Type of exception | Supertype          | Description                                                                                                |
| ----------------- | ------------------ | ---------------------------------------------------------------------------------------------------------- |
| Checked           | `Exception`        | They must be declared by the methods that can raise them.                                                  |
| Unchecked         | `RuntimeException` | They can propagate without being declared in method headers and without being handled by try/catch blocks. | 

Unchecked exception should only be used in limited cases. These exceptions are usually arithmetic or logic exceptions and can be avoided easily by performing manual checks on objects before calling a method on them.

It is good practice to include unchecked exceptions in method headers to let other users know that it is used.

New exceptions can be defined by extending `Exception` or `RuntimeException`:

```java
public class MyException extends Exception {
	public MyException() {
		super();
	}

	public MyException(String s) {
		super(s);
	}
}
```

The new exception can also have specific methods or attributes that give more information about the error encountered by the method that raised it.

In the case above, the new exception simply calls the default constructors of `Exception`.

### Masking

Exceptions can also be used to check for specific conditions. This is called *masking*. In this case, the exception is not propagated outside of the method it is raised in.

Here is an example:

```java
public static boolean sorted(int[] a) {
	int prev;
	try {
		prev = a[0];
	} catch (IndexOutOfBoundsException e) {
		return true; // If the array is empty, it is sorted.
	}
	for(int i = 0; i < a.length; i++) {
		if(prev <= a[i]) prev = a[i];
		else return false;
	}
	return true;
}
```

## Collections

Collections are default data structures contained in Java.

### Lists

The class `List` represents dynamic lists and offers various implementations of them, such as `ArrayList` and `LinkedList`.

Since Java 5, lists are parametric to a type, which means that the same class can organize lists of any type of object. Given any type `T`, a list of objects of type `T` is declared as:

```java
List<T> intList = new List<>();
```

The methods used to access and modify list elements are as follows:

| Method                      | Description                                           |
| --------------------------- | ----------------------------------------------------- |
| `add(int index, E element)` | Inserts `element` at position `index` of the list.    |
| `remove(int index)`         | Removes the element the position `index` of the list. |
| `get(int index)`            | Returns the element at position `index`.              |
| `set(int index, E element)` | Changes the element at position `index` to `element`  |

### Collections and subtypes

Let's take a look at the code below:

```java
List<String> ls = new ArrayList<>();
List<Object> lo = ls; // Compilation error

lo.add(new Object());
String s = ls.get(0); // Compilation error: cannot assign type Object
                      // to type String.
```

This looks conflicting with what was said earlier, but it must be noted that, in general, if `ClassB` is a subclass of `ClassA`, then `Gen<ClassB>` **is not** a subclass of `Gen<ClassA>`.

### Iterators

A generalized for loop is not enough to iterate through all types of collections, so Java introduced a new object, called **iterator**, that can move through any collection.

An iterator is an abstraction of the concept of pointer: an iterator points to an object in a collection and moves through it by changing its reference.

The interface that defines an iterator is the following:

```java
public interface Iterator<E> {
	public boolean hasNext();
	public E next() throws NoSuchElementException;
	public void remove(); // Optional
}
```

In order to standardize the use of iterators, Java also introduced the `Iterable` interface. Classes that implement it are collections that provide a method, called `iterator()`, to create an iterator object to scan its own elements.

Here's an example of an iterator implemented through an internal class:

```java
public class Poly implements Iterable {
	private int[] trms;
	private int deg;

	public Iterator<Integer> terms() {
		return new PolyGen(this);
	}

	private class PolyGen implements Iterator<Integer> {
		private Poly p;
		private int n;

		PolyGen(Poly p) {
			this.p = p;
			n = 0;
		}

		public boolean hasNext() {
			while(n <= p.deg) {
				if(p.trms[n] != 0) return true;
				else n++;
			}
			return false;
		}

		public Integer next() throws NoSuchElementException {
			if(hasNext()) return p.trms[n++];
			else throw new NoSuchElementException();
		}
	}
}
```

An iterator might also not be part of a class, but be defined as a standalone procedure. One example could be an iterator that generates the number in the Fibonacci sequence. For this reason, the inner class should be defined as static.

Let's look at an example:

```java
public class Nums {
	public static Iterator<Integer> fibonacci() {
		return new FibonacciGen();
	}

	private static class FibonacciGen implements Iterator<Integer> {
		private int prev1, prev2;
		private int next;

		FibonacciGen() {
			prev1 = 0;
			prev2 = 1;
		}

		public boolean hasNext() { return true; }

		public Integer next() {
			next = prev1 + prev2;
			prev2 = prev1;
			prev1 = next;
			return next;
		}
	}
}
```

#### The `remove()` method

The `remove()` method declared in the `Iterator<E>` class is an optional operation: if it is not implemented, when called it raises the `UnsupportedOperationException`.

It is rarely useful to modify a collection while iterating through it, which is why this method is optional.

According to the contract of the interface, `remove()` deletes the last element returned by `next()` from the collection, provided that `remove()` is only called once per each call of `next()` and the collection is not modified in any other way during the iteration.

If the contract is not fulfilled, an `IllegalStateException` is thrown.

## I/O operations

### Get input from the terminal

In order to get input from the terminal, the programmer needs to build a **scanner** connected to the *standard input stream* `System.in` and then use the methods provided by the scanner:

| Method         | Description                                                    |
| -------------- | -------------------------------------------------------------- |
| `nextLine()`   | Returns the next line.                                         |
| `next()`       | Returns the next `String` object up to a whitespace character. |
| `nextInt()`    | Returns the next `int`.                                        |
| `nextDouble()` | Returns the next `double`.                                     |
| `hasNext()`    | Returns whether there are new objects in the input stream.     | 

This is not an extensive list of methods: only the most commonly used are represented for brevity.

### Printing text on the terminal

`System.out` provides methods to print to the screen. Some of these are:

| Method                                    | Description                                                     |
| ----------------------------------------- | --------------------------------------------------------------- |
| `println(String s)`                       | Prints the passed string followed by a newline character.       |
| `print(String s)`                         | Prints the passed string without appending a newline character. |
| `printf(String format, String arguments)` | Similar to the C function `printf()`.                           |
