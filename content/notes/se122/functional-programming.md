---
title: 'Functional programming'
draft: false
type: 'page'
toc: true
mathjax: true
---

---

Functional programming is a programming paradigm that promotes the expression of computation as the applications of one or more functions on data.

In this context, functions are meant in their *mathematical* sense, which means:
- There are no side effects
- The value of the output depends entirely on the input of the function
- Verification is simplified
- Parallelization is simplified

## Functional languages

Just like different languages support the object-oriented paradigm to different degrees, different languages favor or disfavor the functional style of programming.

There are some exclusively functional languages, the likes of Erlang, Lisp and Haskell, and some languages that support functional features, such as PHP, Perl and Python.

Java started supporting functional programming from version 8.0.

## Functional programming in Java

Let's start with an example:

```java
class Person {
	private String name;
	private int age;

	// Code

	int getAge() {
		return age;
	}
}

List<Person> list = /*...*/;
list.add(/*...*/);
list.add(/*...*/);
```

How do we sort a list so that people in it appear in ascending order of age?

We can use the `Collections.sort()` method:

```java
public static <T> void sort(List<T> list, Comparator<? super T> c);

// Sorts the specified list according to the order induced by the
// specific comparator.
```

Let's implement the comparator:

```java
MyComparator c = new MyComparator();
Collections.sort(list, c);

class MyComparator implements Comparator<Person> {
	@Override
	public int compare(Person p1, Person p2) {
		if(p1.getAge() < p2.getAge()) return -1;
		else if (p1.getAge() > p2.getAge()) return 1;
		else return 0;
	}
}
```

The `MyComparator` class implements a single function that encodes the meaning of comparing two elements. We could say that `sort` is parametric in respect to the comparison function and `MyComparator` represents that function.

If we don't want to reuse the `MyComparator` class, we can build an *anonymous class*:

```java
Collections.sort(list, new Comparator<Person>() {
	@Override
	public int compare(Person p1, Person p2) {
		if(p1.getAge() < p2.getAge()) return -1;
		else if (p1.getAge() > p2.getAge()) return 1;
		else return 0;
	}
});
```

Java 8 offers some *syntactic sugar* to support this programming pattern. Interfaces with only one method, such as `Comparator`, are called *functional interfaces*. The new syntax introduced with Java 8 to define the method of a functional interface is called **lambda expression** and looks like this:

```java
Comparator<Person> c = (Person p1, Person p2) -> {
	if(p1.getAge() < p2.getAge()) return -1;
	else if (p1.getAge() > p2.getAge()) return 1;
	else return 0;
};
```

We can also use type inference to get an even shorter snippet of code:

```java
Comparator<Person> c = (p1, p2) -> {
	if(p1.getAge() < p2.getAge()) return -1;
	else if (p1.getAge() > p2.getAge()) return 1;
	else return 0;
};
```

Taking a look again at the example from earlier, we can directly pass a lambda function to `Collections.sort()`:

```java
Collections.sort(list, (p1, p2) -> {
	if(p1.getAge() < p2.getAge()) return -1;
	else if (p1.getAge() > p2.getAge()) return 1;
	else return 0;
});
```

### Lambda functions syntax

A general expression for lambda functions with just one input is the following:

```java
// With a mutable object:
obj.method(String name -> name.doSomething());

// With an immutable object:
obj.method(final String name -> name.doSomething());
```

If the object passed as input is immutable, the lack of side effects is ensured.

The compiler can also always infer the type of the input data, so the example above can also be rewritten as:

```java
obj.method(name -> name.doSomething());
```

You cannot, however, let the compiler infer the type and set the input variable as `final` like so:

```java
obj.method(final name -> name.doSomething());
```

In case of multiple parameters, a lambda function can be written like this:

```java
obj.method((par1, par2) -> par1.foo(par2));
```

The latter `par2` in the lambda function signals an *implicit return*.

In the case of more than one statement in the lambda function, this is the syntax to use:

```java
obj.doSomething(final String name -> {
	if(name.equals("Boo")) return "Foo";
	else return name;
});
```

### Another example with `Runnable`

The thread class has a parameter of type `Runnable`, and `Runnable` is an interface with just one method, which means that `Runnable` is a functional interface.

This means that can we launch a new thread to perform a function through a lambda expression:

```java
Runnable r = () -> doSomething();
Thread t = new Thread(r);
t.start();

// This is also valid
Thread t = new Thread(() -> doSomething());
t.start();
```

## `java.utils.function`

Here are some functions contained in the package `java.utils.function`:

- `Function<T, R>`: function with argument type `T` and return type `R`
- `BiFunction<T, U, R>`: function with two arguments of type `T` and `U` and return type `R`
- `Consumer<T>`: function with argument type `T` and no return
- `Predicate<T>`: function with argument type `T` that returns a boolean

All these have corresponding functions for primitive types, such as:

- `IntFunction<R>`
- `DoubleFunction<R>`
- `IntPredicate`
- `IntSupplier`
- `IntConsumer`

Another type of functional programming style is offered by the `Optional<T>` type. This type allows the user to operate on data ignoring the fact that some data might be `null`.

## Function composition

The idea behind function composition is to embed a value in a structure that allows concatenating functions.

![](../images/Pasted%20image%2020221121114508.png)

### `Stream<T>`

`Stream` allows concatenating functions that act on collections.

Starting from a `Collection<T>`, the `stream()` method returns a `Stream<T>`, which contains many interesting methods to transform one stream into another.

#### `forEach()`

The `forEach()` method takes a consumer input that does something with each element in the stream.

`forEach()` has a limited application in functional programming because it allows some side effects, limiting optimizations, parallelism and concurrency.

```java
List<String> list = /* some kind of list */;
list.stream().forEach(x -> System.out.println(x));
```

#### References to methods

Lambda expressions are *anonymous functions*. Functional style also applies when functions are named and preexisting though, so another syntax to achieve a lambda expression with a preexisting function is the following:

```java
list.stream().forEach(System.out::println);
```

#### `filter`

The `filter()` method takes a predicate as input and returns a stream that contains only the elements for which the predicate is `true`.

For example, if we want to print even numbers only from a list:

```java
List<Integer> list = /*...*/;

list.stream()
	.filter(x -> x % 2 == 0)
	.forEach(System.out::println);
```

![](../images/Pasted%20image%2020221122160952.png)

#### `map`

The `map` method takes a function $f:T\to U$ as input and applies it to each element of the stream, returning a `Stream<U>`. There are no restrictions to the types of $T$ and $U$.

For example, if we want to print the length of each string in a list:

```java
List<String> list = /*...*/;

list.stream()
	.map(x -> x.length())
	.forEach(System.out::println);
```

![](../images/Pasted%20image%2020221122161347.png)

#### More methods

- `distinct()`: this method deletes duplicates (a duplicate of element `a` is an element `b` that returns true when `a.equals(b)` is checked)
- `sort()`: this method sorts the elements of a stream (it sorts naturally for `Strings` and `int`, but needs a comparator otherwise)

Let's look at a more complex example:

```java
List<String> list = /*...*/;

list.stream()
	.map(x -> x.length())
	.distinct()
	.sort()
	.forEach(System.out::println);
```

#### `flatMap`

The `flatMap()` method takes a function $f:T \to \text{Stream<U>}$ as input and applies it to each stream element. Then, it merges all streams into one.

For example, given a set of multi-line strings, print the length of the ten longest lines in ascending order:

```java
list.stream()
	.flatMap(str -> str.lines())
	.mapToInt(line -> line.length())
	.sorted()
	.limit(10)
	.forEach(System.out::println);
```

![](../images/Pasted%20image%2020221122162721.png)

#### `reduce`

Reduction is an operation that collects a single value from a stream.

One example of reduction is: return the sum or average of word lengths in a sentence:

```java
List<String> phrase = Arrays.asList("pippo", "pluto", "minnie");

int sum = phrase.stream()
				.mapToInt(word -> word.length())    // returns Stream<int>
				.sum();                             // returns int

double average = phrase.stream()
					   .mapToInt(word -> word.length())
					   .average()                   // returns OptionalDouble
					   .getAsDouble();              // converts to double
```

Reduction can also be implemented manually by providing:

- An initial value (or *identity value*)
- A function that takes a partial result and an element and shows how the element is added to the partial result

For example, manually defining a reduction could translate to the following code:

```java
Integer sum = sentence.mapToInt(word -> word.length())
                      .reduce(0, (a, b) -> a + b);
```

Let's look at another example of reduction:

```java
final Optional<String> aLongName = friends
	.stream()
    .reduce((name1, name2) -> name1.length() >= name2.length() ? name1 : name2);
```

#### `collect`

While the `reduce()` method creates a new value for each element in the stream, `collect()` always changes the same value.

The `collect()` method takes three functions as input:

- A supplier creates the new return value
- An accumulator incorporates an additional element in the return value
- A combiner combines two partial results into one

In case of *standard* data structures, there are predefined collectors:

```java
List<String> sentence = /*...*/;

List<String> wordsWithA = sentence.stream()
								  .filter(word -> word.startsWith("a"))
								  .collect(Collectors.toList());
```

The code above translates into this:

```java
List<String> sentence = /*...*/;

List<String> wordsWithA = sentence.stream()
								  .filter(word -> word.startsWith("a"))
								  .collect(ArrayList::new,     // Supplier
										   ArrayList::add,     // Accumulator
										   ArrayList::addAll); // Combiner
```

#### Notes

A stream does **not** store its elements. They can be stored in a collection or generated on demand.

Let's look at some properties of stream operations:

- They are *stateless*: they cannot change the stream to which they are applied
- They can return new streams that contain the results
- They are *lazy* when possible: they are only executed when their result is needed

## Function references

Suppose we have a lambda function we want to use many times. How can we make that possible, since lambda functions are anonymous?

Assigning a lambda function to a variable of type `Predicate<T>` makes it *reusable*:

```java
final Predicate<String> startsWithL = s -> s.startsWith("L");

// Code

list.stream().filter(startsWithL);
```

### Functions as return values

If we want to generalise the behaviour of a lambda function, we can create a method that returns a *parametrised* lambda function, like so:

```java
public static Predicate<String> pred(String prefix) {
	return s -> s.startsWith(prefix); // returns a predicate
}

// Code

list.stream().filter(pred("X"));
```

## Closures

Let's take a look at this snippet of code from earlier:

```java
public static Predicate<String> pred(String prefix) {
	return s -> s.startsWith(prefix);
}
```

When executing this, Java looks for a variable called `prefix` in the definition context of the lambda function and it finds it as a parameter of the predicate `pred` itself.

In this case, the lambda function is said to *close over* the scope of its definition, hence it is called **closure**.

Let's take a look at another example:

```java
final String prefix = "Z";
Predicate<String> pred = s -> s.startsWith(prefix);
```

In this case, the predicate `pred` *closes* on the `prefix` variable defined outside the lambda function.

To avoid side effects, referenced variable within a lambda function must be either `final` or effectively final, which means they never change after their initialisation but are not declared as `final`.

## Parallel streams

Many times, the elements of a stream are independent of each other and could therefore be analyzed in parallel.

Java allows the user to parse the elements of a stream in parallel simply by invoking the `parallel()` method.

Let's take a look at an example:

```java
List<String> list = /*...*/;

list.stream()
	.parallel()
	.map(x -> x.length())
	.forEach(System.out::println);
```

All `stream()` calls for collections can be converted to `parallelStream()`. The JVM will then parallelise all operations whenever possible.

There may be some side effects associated with parallelisation of streams, so be careful when modifying a value like in the following example:

```java
List<String> list = /*...*/;
final List<Integer> result = new ArrayList<>();

list.stream().parallel()
	.map(x -> x.length())
	.forEach(x -> result.add(x));    // This does not work as intended
```

## Final remarks

### When to use functional programming

A functional programming style is applicable wherever functional interfaces are part of method prototypes, but it's particularly effective in specific areas, such as:

- Manipulation of collections
- Processing of strings
- Multi-threading
- Resource management

### Streams and iterators

Iterators provide a specific strategy for visiting the collection, preventing efficient concurrent execution.

Streams, on the other hand, allow for parallelisation. They can be defined for collections, arrays and iterators and give the programmer the very powerful methods that we have seen earlier.
