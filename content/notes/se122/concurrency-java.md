---
title: 'Synchronisation'
draft: false
type: 'page'
toc: true
mathjax: true
---
# Concurrent programming

In Java, we can write a program in which several activities are run in parallel. This may also indicate some form of hardware parallelism, but not necessarily.

At the process level, multitasking is achieved with this set of operations:
- The executable is loaded into the machine's memory and it has its own address space
- Each process runs a different program
- Processes communicate via the operating system, files or the network
- Processes can contain multiple *threads*

A *thread* is a sequential logical activity. It shares its address space with other threads in the same process and communicates to external components via shared variables.
A thread has its own execution process.

Many times, a thread is also reffered to as *light-weight process*.

---

## Language-level concurrency constructs

C and C++ are *single threaded* languages. Multitasking in these languages requires relying on the operating system, with appropriate calls to the OS's multithreaded primitives.

Higher-level languages such as Java contain multitasking primitives. In Java, for example, the class `Thread` is a multithreaded primitive. This allows multithreaded software to be written without having to deal with the operating system directly. This has enabled the development of high-level libraries that simplify the making of multithreaded software.

---

## Threads in Java - Method 1: `Thread`

To create a thread in Java, you can do the following:

1. Define a class that inherits from the `Thread` class and contains the `run()` method
   
   ```Java
class ListSorter extends Thread {
	// Code
	public void run() {
		// Thread code
	}
}
	```

2. Create an instance of the class

	```Java
	ListSorter concSorter = new ListSorter(list1);
	```

3. Invoke the `start()` method, which calls the `run()` method

	```Java
	concSorter.start();
	```

### Interleaving semantics

When multiple threads are running, any interleaving is valid (that is, any thread can be run as the first thread and any thread can stop the execution of the currently executed one).

Take a look at this piece of code:

```Java
public class A extends Thread {
   public void run() {
		for (int i=0; i<=5; i++)
			System. out.println("From Thread A: i="+i);
		System. out.println("Exit from A");
	}
}

public class B extends Thread {
	public void run() {
		for (int j=0; j<=5; j++)
			System. out.println("From Thread B: j="+j);
		System. out.println("Exit from B");
	}
}

public class C extends Thread {
	public void run() {
		for (int k=0; k<=5; k++)
			System. out.println("From Thread C: k="+k);
		System. out.println("Exit from C");
	}
}

public class ThreadTest {  
	public static void main(String[] args) {
      new A().start();
      new B().start();
      new C().start();
	}
}
```

Executing this source code can lead to both the following outputs:

```text
From Thread A: i= 0
From Thread A: i= 1
From Thread A: i= 2
From Thread A: i= 3
From Thread A: i= 4
From Thread A: i= 5
Exit from A
From Thread B: j= 0
From Thread B: j= 1
From Thread B: j= 2
From Thread B: j= 3
From Thread B: j= 4
From Thread B: j= 5
Exit from B
From Thread C: k= 0
From Thread C: k= 1
From Thread C: k= 2
From Thread C: k= 3
From Thread C: k= 4
From Thread C: k= 5
Exit from C
```

```text
From Thread A: i= 0
From Thread A: i= 1
From Thread A: i= 2
From Thread A: i= 3
From Thread A: i= 4
From Thread A: i= 5
Exit from A
From Thread C: k= 0
From Thread C: k= 1
From Thread C: k= 2
From Thread C: k= 3
From Thread C: k= 4
From Thread C: k= 5
From Thread B: j= 0
From Thread B: j= 1
From Thread B: j= 2
From Thread B: j= 3
From Thread B: j= 4
From Thread B: j= 5
Exit from B
Exit from C
```

Note that these aren't the only two possible outputs, but only two are shown for brevity.

## Threads in Java - Method 2: `Runnable`

The `Thread` class implements an interface called `Runnable`. The interface defines a single `run()` method that contains the thread code. This gives an alternative way to define a thread.

To define a thread with the interface `Runnable`, you can do the following:

1. Define a class that implements the `Runnable` interface

	```Java
	class ListSorter implements Runnable {
		// Code
		public void run() {
			// Thread statements
		}
	}
	```

2. Create an instance of that class

	```Java
	ListSorter concSorter = new ListSorter(list1);
	```

3. Create an instance of the `Thread` class

	```Java
	Thread myThread = new Thread(concSorter);
	```

4. Call the `run()` method through the `start()` method

	```Java
	myThread.start();
	```

### Miscellaneous details

The `Thread` class also provides methods and features that allow for very fine control of concurrency, often OS-dependent and which we will ignore in this course.

For example, the Thread class contains methods like:
- `sleep(x)`: suspends the thread for $x$ milliseconds
- `interrupt()`: sends an interrupt to the thread (`run()` usually throws an `InterruptedException` in this case)

Each thread has a *priority*, used by the scheduler to decide which threads are going to run first. This number is defined as `Thread.Norm_Priority` by default, but can be any value between `Thread.Min_Priority` and `Thread.Max_Priority`.

---

## Shared data and mutual exclusion

It is critical that sequences of operation accessing shared data are executed by different threads in *mutual exclusion*. Let's look at an example to understand this concept better.

```Java
class BankAccount {
	private float balance;

	public BankAccount(float startBalance) {
		balance = startBalance;
	}

	public void deposit(float money) {
		balance += money;
	}

	public void withdrawal(float money) {
		balance -= money;
	}
}
```

Suppose `startBalance = 100` at the first execution of the constructor for the `BankAccount` class.

Now, `Thread1` calls `deposit(50)` and calculates the final balance on the account, which is $150$, but does not write the new value in `balance` because `Thread2` interrupts `Thread1`'s execution.

`Thread2` fully executes `withdrawal(50)`, so `balance = 50` at the end of the operation.

`Thread1` is free to conclude its operations now, so it writes `balance = 150`.

In conclusion, we deposited and withdrew the same amount of money from the bank account, but our balance increased by $50$.

This is where mutual exclusion comes into play. We need to block other threads from accessing a sensitive value when this needs to be updated without *interference*.

### *Atomic* sequences

When certain instruction sequences must be executed in an isolated manner, they are defined as *atomic sequences*. In Java, almost no instruction is atomic, but the software programmer can make a statement atomic by using the keyword `synchronized`.

```Java
class BankAccount {
	private float balance;

	public BankAccount(float startBalance) {
		balance = startBalance;
	}

	public synchronized void deposit(float money) {
		balance += money;
	}

	public synchronized void withdrawal(float money) {
		balance -= money;
	}
}
```

Java associates an intrinsic *lock* with each object, so when a `synchronized` method is invoked, if no other `synchronized` method is running, the object is locked and the method is executed, otherwise the calling task is suspended until the lock on the object is released.

#### Comments on `syncrhonized` and locks

- Multiple invocations of `synchronized` methods on the same objects are not subject to interleaving: while a thread executes a `synchronized` method of an object, threads trying to invoke `synchronized` methods on the same object are suspended until the first thread terminates execution.
- Constructors **cannot be** `synchronized`. Only the thread that creates the object should have access to it while it's being created.
- Any `final` data, which cannot be changed after its creation, can be read by non-`synchronized` methods.
- The intrinsic lock is automatically acquired when the `synchronized` method is invoked and released on its return
- Access to `static` fields is controlled by a *special lock*, different from those associated with instances of the class

#### Synchronization and inheritance

The `synchronized` keyword is not considered part of the interface of a method, but it's considered an *implementation detail*, so **it's not inherited**.

In the subclass, we are free to choose whether to implement the method as `synchronized` or not.

#### `volatile`

The keyword `volatile` is useful to delcare variables that are often used in read-only threads.

To declare a `volatile` variable, you can type:

```Java
private volatile int x;
```

The JVM requires a lock for read-only variables as well, which grants optimisation and caching.

In most cases, the JVM can reorder the execution of some instructions (this depends mostly on the hardware architecture). When reading from or writing to a variable, the JVM *cannot reorder the read or write operations*, so the reading or writing of the variable `x` is an atomic operation.

### `synchronized` statements

Synchronized statements need to specify the object to apply the lock to, like so:

```Java
public void addName(String name) {
	synchronized(this) {
		lastName = name;
		nameCount++;
	}
	nameList.add(name);
}
```

This releases the lock to the object before invoking a method that may in turn require you to wait for a lock to be released.

The advantage of using the `synchronized` statement is that a smaller portion of the code is locked, so that the non-sensitive parts of it can run without interruptions.

---

## *Liveness*

The *liveness* of a program is a very important property. It means that a concurrent application is executed withing acceptable time limits.

There are some main situations that must be avoided to increase the liveness of a program:
- Deadlock
- Starvation
- Livelock

### Deadlock

A *deadlock* is when two or more threads are locked forever, waiting for one another to release the lock.

Here is an example of deadlock:

```Java
private final String name;

public Friend(String name) {
	this.name = name;
}

public synchronized void bow(Friend bower) {
	System.out.format("%s: %s" + " has bowed to me!%n", this.name, bower.getName());
	bower.bowBack(this);
}

public synchronized void bowBack(Friend bower) {
	System.out.format("%s: %s" + " has bowed back to me!%n", this.name, bower.getName());
}

final Friend anna = new Friend("Anna");
final Friend bob = new Friend("Bob");

new Thread(new Runnable() {
	public void run() {
		anna.bow(bob);
	}
}).start();

new Thread(new Runnable() {
	public void run() {
		bob.bow(anna);
	}
}).start();
```

In this example, the first thread takes the object lock by invoking the `synchronized` method `anna.bow(bob)`. If the second thread takes the lock with `bob.bow(anna)` before the first thread executes `bob.bowBack(anna)`, the threads will start waiting for each other to release the lock, blocking the execution of the program.

### Starvation

In this situation, a thread has difficulty gaining access to a shared resource and therefore cannot proceed with its execution.

Greedy tasks that frequently invoke long methods and delay the thread or a scheduler that uses priority and gives precedence to greedy tasks are two common examples of starvation.

### Livelock

Livelock is caused by a design error that generates a sequence of unnecessary operations for the purpose of actual computation progress.

One example could be the endless sequence of "*You go first*" created when two people hold the door open for each other.

---

## Preconditions for synchronized methods: guarded blocks

Let's return to the `BankAccount` example: how do we stop a withdrawal operation when the account is overdrawn?

```Java
class BankAccount() {
	private float balance;

	// Constructor is omitted

	synchronized public void withdraw(float money) {
		while(balance - money < 0) wait();
		balance -= money;
	}
}
```

The `wait()` operation releases the lock on the object and suspends the task.

How do we wake up a task that has been put to sleep with `wait()`?

```Java
class BankAccount() {
	private float balance;

	// Constructor is omitted

	synchronized public void withdraw(float money) {
		while(balance - money < 0) wait();
		balance -= money;
	}

	synchronized public void deposit(float money) {
		balance += money;
		notify();
	}
}
```

The `notify()` operation awakens a task suspended through `wait()`.

In this case, it is necessary to add the `wait()` statement inside a `while` loop, because a simple `if` statement would withdraw money from the account even if after the first `notify()` the number `balance - money` is still less than zero.

---

## Life cycle of a thread

![The life cycle of a thread](Images/LifeCycleThread.png)

### Difference between `notify()` and `notifyAll()`

A thread that is in a waiting state can only be revived by `notify()` and `notifyAll()`. `notify()` only awakens one thread, but it is not known which one, while `notifyAll()` awakens all threads; which one is executed next is up to the scheduler to decide.

Notably, `notifyAll()` is a less efficient way to awaken threads, since it wakes up every waiting thread, but it's safer to use, since `notify()` introduces non-determinism in the program's execution. `notify()` can certainly be used when only one thread at a time is in a waiting state during the execution of the program.

### About calling `wait()`

Calling `wait()` needs to catch the checked `InterruptedException`. The simplest way to do this (alas not the best) is to add `throws InterruptedException` to the method that calls `wait()`. For example:

```Java
synchronized public void withdraw(float money) throws InterruptedException {
	while(balance - money < 0) wait();
	balance -= money;
}
```

---

## Problems with mutable objects

A mutable object can lead to consistency problems even when provided with correctly synchronized methods. Let's look at an example:

```Java
public class SynchronizedRGB {
    // Values must be between 0 and 255.
    private int red;
    private int green;
    private int blue;

    private String name;

    private void check(int red, int green, int blue) {
        if (red < 0 || red > 255 || green < 0 ||
        green > 255 || blue < 0 || blue > 255) {
            throw new IllegalArgumentException();
	}

	public SynchronizedRGB(int red, int green, int blue, String name) {
	    check(red, green, blue);
	    this.red = red;
	    this.green = green;
	    this.blue = blue;
	    this.name = name;
	}

	public void set(int red, int green, int blue, String name) {
	     check(red, green, blue);
	     synchronized (this) {
	         this.red = red;
	         this.green = green;
	         this.blue = blue;
	         this.name = name;
		}
	}

	public synchronized int getRGB() {
	     return ((red << 16) | (green << 8) | blue);
	}
	
	public synchronized String getName() {
	     return name;
	}
	
	public synchronized void invert() {
		red = 255 - red;
	    green = 255 - green;
		blue = 255 - blue;
		name = "Inverse of " + name;
	}
}
```

Now, let's add some executable code to see where the problem lies:

```Java
SynchronizedRGB color = new SynchronizedRGB(0, 0, 0, "Pitch Black");

// Code

int myColorInt = color.getRGB();        // Statement 1
String myColorName = color.getName();   // Statement 2
```

If another thread invokes `set()` after statement 1 but before statement 2, the value of `myColorInt` may not match the value of `myColorName`. This is because the object is **mutable**.

**Immutable** objects can be created through the following steps:

- Do not provide setter methods
- Define all final and private instance attributes
- Do not allow subclasses to override methods (by declaring the class final or declaring the constructor as private)
- If instance attributes have references to mutable objects, do not make them modifiable
	- Do not provide methods that modify mutable objects
	- Do not do reference sharing to mutable objects
		- Do not save references to mutable external objects passed to the constructor. If necessary, make copies and save the references to the copies
		- Do not return internal mutable objects. If necessary, create copies of internal mutable objects and return those

So, to make `SynchronizedRGB` an immutable object, we can do the following:

- There are two setter methods. The first arbitrarily transforms the object and will have no counterpart in the immutable version. The second, `invert`, is adapted by creating a new object instead of modifying the current one.
- All attributes are *already* private, so we only need to qualify them as `final`
- The class must be qualified as `final`
- A single attribute refers to an object and the object is immutable. Therefore, no more operations are necessary to safeguard the state of any mutable objects.

Here is the code for the immutable version of `SynchronizedRGB`:

```Java
final public class ImmutableRGB {
    // Values must be between 0 and 255.
    final private int red;
    final private int green;
    final private int blue;

    final private String name;

    private void check(int red, int green, int blue) {
        if (red < 0 || red > 255 || green < 0 ||
        green > 255 || blue < 0 || blue > 255) {
            throw new IllegalArgumentException();
	}

	public ImmutableRGB(int red, int green, int blue, String name) {
	    check(red, green, blue);
	    this.red = red;
	    this.green = green;
	    this.blue = blue;
	    this.name = name;
	}

	public synchronized int getRGB() {
	     return ((red << 16) | (green << 8) | blue);
	}
	
	public synchronized String getName() {
	     return name;
	}
	
	public synchronized void invert() {
		return new ImmutableRGB(255 - red,
								255 - green,
								255 - blue,
								"Inverse of " + name);
	}
}
```

---

## Advanced concepts

This section will take a look at concepts introduced with Java 5.0, specifically in the `java.util.concurrent` packages:

- "Lock" objects
- Executors
- Concurrent collections

It's suggested to use these tools instead of `wait()` and `notify()` as soon as possible, although they bring up some overhead at runtime and memory usage that may not be acceptable in some use cases.

### Lock objects

The `synchronized` code defines an elementary case of lock (an implicit lock), but more sophisticated mechanisms are provided by the `java.util.concurrent.locks` package.

A lock, defined by the lock interface, can be acquired by only one thread, as in the case of *implicit locks* associated with synchronized code.

It is possible, however, to withdraw from the lock request: the `tryLock()` method exits the lock if it is not available (either immediatly or after a specified timeout), while the `lockInterruptibly()` method allows withdrawal if another thread sends an interrupt before the lock is acquired.

Let's look at an example of a lock object by rewriting the bowing code from before:

```Java
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;
import java.util.Random;

public class Safelock {
	static class Friend {
		private final String name;
		private final Lock lock = new ReentrantLock();

		public Friend(String name) {
			this.name = name;
		}

		public String getName() {
			return this.name;
		}

		public boolean ImpendingBow(Friend bower) {
			Boolean myLock = false;
			Boolean yourLock = false;
			try {
				myLock = lock.tryLock();    // Try to lock this.lock
				yourLock = lock.tryLock();  // Try to lock bower.lock
			} finally {
				if(!(myLock && yourLock)) { // If no both locks: release
					if(myLock) lock.unlock();
					if(yourLock) bower.lock.unlock();
				}
			}
			return myLock && yourLock;
		}

		public void bow(Friend bower) {
			if(impendingBow(bower)) {
				try {
					System.out.format("%s: %s has bowed to me!%n",
										this.name,
										bower.getName());
					bower.bowBack(this);
				} finally {
					lock.unlock();
					bower.lock.unlock();
				}
			} else {
				System.out.format("%s: %s started bowing to me, but saw" + 
									" that I was already bowing to him.%n",
									this.name,
									bower.getName());
			}
		}

		public void bowBack(Friend bower) {
			System.out.format("%s: %s has bowed back to me!%n",
								this.name,
								bower.getName());
		}
	}
}

static class BowLoop implements Runnable {
	private Friend bower;
	private Friend bowee;

	public BowLoop(Friend bower, Friend bowee) {
		this.bower = bower;
		this.bowee = bowee;
	}

	public void run() {
		Random random = new Random();
		for(;;) {
			try {
				Thread.sleep(random.nextInt(10));
			} catch (InterruptedException e) {}
			bowee.bow(bower);
		}
	}
}

public static void main(String[] args) {
	final Friend bob = new Friend("Bob");
	final Friend anna = new Friend("Anna");
	new Thread(new BowLoop(bob, anna)).start();
	new Thread(new BowLoop(anna, bob)).start();
}
```

### Executors, thread pools and the fork/join framework

The tools available so far impose a close relationship between the task to be performed by a thread and the thread itself, but the two concepts can be kept apart in complex applications through *executor interfaces*, *thread pools* and *forks and joins*.

#### Executors

Executors are predefined and allow efficient management that reduces overhead due to thread management.

The `java.util.concurrent` package defines three interfaces:
- `Executor`
- `ExecutorService` (extends `Executor`)
- `ScheduledExecutorService` (extends `ExecutorService`)

If `r` is a `Runnable` thread and `e` is an `Executor`, instead of starting a thread through:

```Java
(new Thread(r)).start();
```

We can use an `Executor`:

```Java
e.execute(r);
```

This lets us avoid overhead caused by the creation of Thread objects.

#### Thread pools

Implementations of the `Executors` interface uses *thread pools*, which consist of threads that exist outside of `Runnable`. A common example is an executor using a *fixed thread pool*, which is created by calling the factory method `newFixedThreadPool` from the class `java.util.concurrent.Executors`. The tasks are sent to the pool through a queue.

#### Fork/join framework

The fork/join framework is yet another implementation of `ExecutorService`, useful in the case of multiple processors. It allows tasks to be distributed to elements of a thread pool in a recursive pattern.

### Concurrent collections

The `java.util.concurrent` package includes extensions to Java collections such as:

- `BlockingQueue`: FIFO data structure that blocks or returns a timeout when trying to insert an object into a full queue or trying to remove an object from an empty queue
- `ConcurrentMap`: allows to delete or edit a key-value pair atomically only if the key is present and to add a key-value pair only if the key doesn't already exist.

### Atomic variables

The `java.util.atomic` package defines classes that support atomic operations on single variables.

Let's see an example below:

```Java
import java.util.concurrent.atomic.AtomicInteger;

public class AtomicCounter {  
	private AtomicInteger c = new AtomicInteger(0);
	
	public void increment() {
		c.incrementAndGet();
	}

	public void decrement() {
		c.decrementAndGet();
	}  

	public int value() {
		return c.get();
	}
```

Atomic objects allow the programmer to avoid the liveness problems that can be caused by using synchronized methods, without the complications of synchronized statements.

Java 5 also provides atomic array implementations:

- `AtomicIntegerArray`
- `AtomicLongArray`
- `AtomicReferenceArray`

The methods used to access these atomic arrays are:

- `compareAndSet(int index)`
- `incrementAndGet(int index)`
