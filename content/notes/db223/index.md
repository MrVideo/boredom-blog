---
title: 'Concurrency'
draft: false
type: 'page'
toc: true
mathjax: true
---

---

## Concurrency in the DBMS architecture

The Concurrency Control System in a DBMS does several things:

- It manages the simultaneous execution of transactions
- It avoids the insurgence of anomalies

Moreover, it ensures that everything is done while maintaining a good level of performance.

## Problems due to concurrency

In DBMSs, problems may be caused by concurrent SQL transactional statements addressing the same resource. For example, let's consider the two following transactions:

```text
T1: begin transaction
	D = D + 3
	commit work

T2: begin transaction
	D = D + 6
	commit work
```

The transactions both write a value to the datum `D`. If one of them writes **after** the other one has read the datum but **before** it has written it, then we encounter an anomaly.

## Concurrent executions and anomalies

There are many types of concurrent execution.

The main type of concurrent execution is the **serial** one, when two transaction execute one after the other:

![](images/Pasted%20image%2020230921163859.png)

This type of concurrent execution does not pose any problem in terms of anomalies. The other two concurrent execution types do, though: the **interleaved** execution:

![](images/Pasted%20image%2020230921163956.png)

and the **nested** execution:

![](images/Pasted%20image%2020230921164010.png)

Let's take a look at how executing transaction in some orders may bring the database to an anomaly.

### Lost update

Let's consider two interleaved transactions:

```text
D = 100

T1: r(D -> x)
T1:	x = x + 3
	T2: r(D -> y)
	T2:	y = y+ 6
T1:	w(x -> D)        D = 103
	T2:	w(y -> D)    D = 106
```

The execution of the operations in this order causes the database to "forget" the update brought by `T1`.

### Dirty read

Let's consider two interleaved transactions once again:

```text
D = 100

T1: r(D -> x)
T1: x = x + 3
T1: w(x -> D)        D = 103
	T2: r(D -> y)    The value read is uncommitted, so the read is dirty
T1: rollback
	T2: y = y + 6
	T2: w(y -> D)    D = 109
```

This order of execution made it possible for `T2` to read a value that was not committed and was then rolled back. This led to a wrong final value for the datum `D`.

### Non-repeatable read

Let's now consider two nested transactions:

```text
D =100

T1: r(D -> x)
	T2: r(D -> y)
	T2: y = y + 6
	T2: w(y -> D)    D = 106
T1: r(D -> z)        z <> x
```

In this case, the transaction `T2` writes a value to `D` after `T1` read it once and before it reads it again, so we end up with two variables, `x` and `z`, with two different values.

### Phantom update

Let's imagine that there is a constraint on values in a table that impose:

$$A + B + C = 100$$

Let's also hypothesise that currently:

- $A = 50$
- $B = 30$
- $C = 20$

Now, imagine that the following transactions occur:

```text
T1: r(A -> x), r(B -> y)
	T2: r(B -> s), r(C -> t)
	T2: s = s + 10, t = t - 10
	T2: w(s -> B), w(t -> C)
T1: r(C -> z)
```

When the block of transaction finishes its execution, $A+B+C=90$ and the constraint is no longer respected.

This happens because `T1` reads data $A$ and $B$ before it reads $C$ and `T2` changes the value of $B$ and $C$ before `T1` can read the updated data at once.

### Phantom insert

Let's take a look at the following transactions:

```text
T1: C = AVG(B: A = 1)
	T2: INSERT (A = 1, B = 2)
T1: C = AVG(B: A = 1)
```

So, `T1` finishes execution after new values are inserted. This causes the average to be wrong.

### Summary of anomalies

We can summarise anomalies with the table below:

| Anomaly             | Order of operations                               | Description                                                                      |
| ------------------- | ------------------------------------------------- | -------------------------------------------------------------------------------- |
| Lost update         | `r1 - r2 - w2 - w1`                               | An update is applied from a state that ignores a preceding update, which is lost |
| Dirty read          | `r1 - w1 - r2 - abort1 - w2`                      | An uncommitted value is used to update the data                                  |
| Non-repeatable read | `r1 - r2 - w2 - r1`                               | Someone else updates a previously read value                                     |
| Phantom update      | `r1 (partial) - r2 (partial) - w2 (partial) - r1` | Someone else updates data that contributes to a previously valid constraint      |
| Phantom insert      | `r1 - w2 (new data) - r1`                         | Someone else inserts data that contributes to a previously read datum            | 

## Concurrency theory vs. system implementation

Concurrency theory builds upon a model of transactions and concurrency control principles that helps understanding real systems. Real systems exploit implementation level mechanisms, like locks and snapshots, which help achieve some of the desirable properties postulated by the theory.

In DBMSs, there are no view serialisability or conflict serialisability checks. Instead, there are lock tables, lock types, lock granting rules, snapshots and much more, which implement some of the functionality described by concurrency theory.

## Transactions, operations and schedules

> **Operation**
> 
> A read or write of a specific datum by a specific transaction

An operation is defined by the agent of the operation and the datum that is either written or read.

> **Schedule**
> 
> A sequence of operations performed by concurrent transactions that respects the order of operations of each transaction

A schedule is a sequence that mixes transaction in their proper order. For example, given the two transactions:

```text
T1: r1(x) w1(x)
T2: r2(z) w2(z)
```

A sequence combining the two would be:

```text
S1: r1(x) r2(z) w1(x) w2(z)
```

> How many distinct schedules exist for two transactions?

Considering the example above, we can easily say that there are **six** possible schedules for the two transactions:

- Two serial schedules
- Two interleaved schedules
- Two nested schedules

Let's now generalise this number: for $n$ transactions, there can be:

- $N_S = n!$ serial schedules
- $N_D = {(\sum_{i=1}^n k_i)!\over \prod_{i=1}^n (k_i!)}$ distinct schedules

It is obvious that $N_S \ll N_D$.

## Principles of concurrency control

The goal of concurrency control is to reject schedules that causes anomalies.

Let's give two important definitions:

> **Scheduler**
> 
> A component that accepts or rejects the operations requested by the transactions

> **Serial schedule**
> 
> A schedule in which the actions of each transaction occur in a contiguous sequence

We need to define some sort of *acceptability* metric for schedules. In order to do this, let's make some assumptions first:

> **Assumptions**
>
> - We assume that transactions are observed **a posteriori** and limited to those that have committed
> - We are ignoring the possibility of aborts

### View-serialisability

Our *correctness* metric will be the notion of **serialisable schedule**:

> **Serialisable schedule**
>
> A schedule that leaves the database in the same state as some serial schedule of the same transactions

![](images/Pasted%20image%2020230918105536.png)

We need to set up a notion of equivalence that lets us compare serialisable schedules to serial schedules. To do so, we can observe the following:

- Two schedules that read the same values could be equivalent
- Two schedules that both write the same final values could be equivalent

If both these conditions hold, then the state of the database before and after the schedules should be the same.

> **View-equivalence** and **view-serialisability**
>
> Two schedules that have these two properties are known as **view-equivalent**. If two schedules are view-equivalent to a serial schedule of the same transactions, then the schedule is **view-serialisable**.

The class of view-serialisable schedules is called **VSR**.

> **Example**
> 
> Let's look at an example of view-serialisability: given the following schedule:
>
> ```text
> S3: w0(x) r2(x) r1(x) w2(x) w2(z)
> ```
>
> We could *manually* rearrange the operations in it to obtain a **serial** schedule:
>
> ```text
> S4: w0(x) r1(x) r2(x) w2(x) w2(z)
> ```
>
> We can then conclude that `S3` is **view-equivalent** to the serial schedule `S4`, hence it is also **view-serialisable**.

Some schedules are **never** view-serialisable:

- The lost update pattern
- The non-repeatable read pattern
- The phantom update pattern

Unfortunately, deciding if a generic schedule is in VSR is an **NP-Complete problem**. We must then look for a stricter definition that is *easier* to check.

![](images/Pasted%20image%2020230918112441.png)

### Conflict-serialisability

In order to understand conflict-serialisability, we need to define what a conflict is:

> **Conflicts between operations**
>
> Two operations are in conflict if they address the same resource and at least one of them is a write. This brings forth two types of conflicts:
> - **Read-write** conflicts: only one of the operations is a write operation
> - **Write-write** conflicts: both the operations are write operations

Now we can define conflict-equivalence and conflict-serialisability:

> **Conflict-equivalence and conflict-serialisability**
>
> Two schedules are **conflict-equivalent** if both contain the same operations and, in all the conflicting pairs, the transactions occur in the same order.
> A schedule is **conflict-serialisable** if and only if it is conflict-equivalent to a serial schedule of the same transactions.

The class of conflict-serialisable schedules is named **CSR**.

We can prove that **all conflict-serialisable schedules are also view-serialisable**, but the inverse is not necessarily true. So we can say:

$$\begin{aligned}
\text{VSR}&\supset\text{CSR}\\
\text{CSR}&\implies\text{VSR}
\end{aligned}$$

![](images/Pasted%20image%2020230918113724.png)

Testing conflict-serialisability is done with a **conflict-graph** that has:

- One node for each transaction
- One arc between two transactions $T_i, T_j$ if there exists at least one conflict between an operation $o_i$ of $T_i$ and an operation $o_j$ of $T_j$ such that $o_i$ precedes $o_j$.

> **Theorem**
>
> A schedule is in CSR if an only if its conflict graph is **acyclic**.

## Concurrency control in practice

CSR checking would be efficient if we knew the graph from the beginning, but we don't.

A scheduler must rather work **online**, i.e. decide for each requested operation whether to execute it immediately or to reject or delay it. It is not feasible to maintain a conflict graph, update it and check its acyclicity at each operation request.

Furthermore, the assumption that concurrency control can work only with the commit-projection of the schedule is unrealistic: **aborts do occur**.

Some simple online *decision criterion* is required for the scheduler, which must:

- Avoid as many anomalies as possible
- Have negligible overhead

> How can concurrency control be implemented online, as described?

There are two main families of techniques:

- **Pessimistic**: it is based on locks (so resource access control); if a resource is taken, make the requester wait or pre-empt the holder
- **Optimistic**: it is based on timestamps and versions; the scheduler serves as many requests as possible, maybe even using out-of-date versions of the data

We will compare the two families after introducing their features.

> Commercial systems take the best of both worlds

### Locking and 2PL

Locking is the most common method in commercial systems.

A transaction is well-formed with respect to locking if:

- Read operations are preceded by `r_lock` (a shared lock) and followed by `unlock`
- Write operations are preceded by `w_lock` (an exclusive lock) and followed by `unlock`

> Unlocking can be delayed with respect to the end of the read/write operation

Transaction that first read and then write an object may:

- Acquire a `w_lock` **while reading**
- Acquire an `r_lock` first and then **upgrade it** to a `w_lock`: this process is called **lock escalation**

Given what we've said, an object can then be in three states:

- **Free**
- **Read-locked** by one or more readers
- **Write-locked** by a single writer

The **lock manager** receives the primitives from the transactions and grants resources according to the conflict table, which looks something like this:

![](images/Pasted%20image%2020230922105820.png)

Typically, locks are implemented through **lock tables**: hash tables indexing the lockable items via hashing. Each locked item has a linked list associated with it and every node in the linked list represents the transaction which requested for the lock. Every new lock request for the data item is **appended** as a new node to the list.

In order to make locks respect serialisability, we can apply a technique called **Two-Phase Locking**, or 2PL: a transaction **cannot acquire any other lock** after releasing one.

This is sufficient to prevent non repeatable reads but also ensures serialisability.

![](images/Pasted%20image%2020230922110157.png)

We can now state that schedules in 2PL are **both view and conflict-serialisable**:

$$\text{VSR} \supset \text{CSR} \supset 2\text{PL}$$

There is a problem though: 2PL is actually **smaller** than CSR. For example, let's look at this schedule:

```text
r1(x) w1(x) [T1 released] r2(x) w2(x) r3(y) [T1 acquired] w1(y)
```

![](images/Pasted%20image%2020230922110641.png)

Since we said that a lock cannot be acquired again by the same transaction in 2PL, the schedule above is not 2PL but is CSR. We are now **restricting too much**.

![](images/Pasted%20image%2020230922110607.png)

### Strict 2PL

If we remove the commit-projection hypothesis from our model, that is if we "let aborts happen", 2PL does not protect us from dirty reads.

To correct this, we must add a constraint to 2PL and so create **strict 2PL**: locks held by a transaction can be released **only after a commit or rollback**.

This version of 2PL is used in most commercial DBMSs when a high level of isolation is required.

![](images/Pasted%20image%2020230922112039.png)

Strict 2PL locks are also called **long duration** locks, while normal 2PL locks are **short duration** locks.

> Real systems may apply 2PL policies differently to read and write locks. Typically, long duration locks are for write operations and read locks follow variable policies in real systems.

> **Warning**
>
> Long duration read locks are costly in terms of performances: real systems replace them with more complex mechanisms.

### Prevent phantom inserts: predicate locks

A phantom insertion occurs when a transaction adds items to a data set previously read by another transaction.

In order to prevent phantom inserts a lock should be place also on "future data", i.e. data inserted in the table that would **satisfy a previous query**.

**Predicate locks** extend the notion of **data locks** to "future data".

### Isolation levels in SQL:1999 and JDBC

SQL defines **transaction isolation levels**, which specify the anomalies that should be prevented by running at that level.

> The level does not affect write locks.

A transaction should always get exclusive lock on any data it modifies, and hold it until completion (according to strict 2PL), **regardless** of the isolation level.

For read operations, levels define the degree of protection from the effects of modifications made by other transactions.

The isolation levels in SQL:1999 are as follows:

| Isolation level  | Dirty read | Non-repeatable read | Phantoms     | Description                                       |
| ---------------- | ---------- | ------------------- | ------------ | ------------------------------------------------- |
| Read uncommitted | Yes        | Yes                 | Yes          | No read locks implemented                         |
| Read committed   | No         | Yes                 | Yes          | No 2PL on read locks                              |
| Repeatable read  | No         | No                  | Yes (insert) | Read locks follow strict 2PL                      |
| Serialisable     | No         | No                  | No           | Read locks follow strict 2PL with predicate locks | 

Serialisable transactions don't necessarily execute serially. The requirement is that transactions can only commit if the result would be as if they had executed serially in any order. The locking requirements to meet this guarantee can **frequently lead to a deadlock** where one of the transactions needs to be rolled back. Therefore, the serialisable isolation level is used **sparingly** and is **not the default** in most commercial systems.

Below is a table describing the type of locks found in the different SQL isolation levels:

| Isolation level  | Read locks                                                                            | Write locks                                   |
| ---------------- | ------------------------------------------------------------------------------------- | --------------------------------------------- |
| Read uncommitted | Not required                                                                          | Well formed writes, long duration write locks |
| Read committed   | Well formed reads, short duration read locks                                          | Well formed writes, long duration write locks |
| Repeatable read  | Well formed reads, long duration data read locks, short duration predicate read locks | Well formed writes, long duration write locks |
| Serialisable     | Well formed reads, long duration read locks                                           | Well formed writes, long duration write locks |

### The impact of locking: waiting is dangerous

Locks are tracked by lock tables: main memory data structures. Resources in this table can be either free, read-locked or write-locked. To keep track of readers, every resource also has a **read counter**.

Transactions requesting locks are either **granted the lock** or **suspended and queued**, according to a FIFO queue. Because of this, there are risks of:

- **Deadlock**: two or more transaction in endless mutual wait
- **Starvation**: a single transaction in endless wait

Deadlocks usually occur when each transaction waits for another to release a lock, while starvation typically occurs due to write transactions waiting for resources that are continuously read.

#### Deadlocks

A deadlock occurs because concurrent transactions hold and in turn request resources held by other transactions.

A schedule creating a possible deadlock is the following:

```text
T1: r1(x) w1(y)
T2: r2(y) w2(x)

S: r_lock1(x), r_lock2(y), r1(x), r2(y), w_lock1(y), w_lock2(x)
```

There are two ways to visualise deadlocks:

- **Lock graphs**: bipartite graphs in which nodes are resources or transactions and arcs are lock requests or lock assignments
- **Wait-for graphs**: graphs in which nodes are transactions and arcs are "waits for" relationships

In both types of graph, a deadlock is represented by a cycle in the wait-for graph of transactions:

![](images/Pasted%20image%2020230922115443.png)

Deadlocks can be resolved via:

- **Timeout**: transactions are killed after a long wait
- **Deadlock prevention**: transactions are killed when they *could* be in a deadlock (this is decided through heuristics)
- **Deadlock detection**: transactions are killed when they *are* in a deadlock (this is decided by wait-for graph inspection)

##### Timeout method

A transaction is killed and restarted after a given amount of waiting, assumed as due to a deadlock.

This is the simplest deadlock resolution method.

The timeout value is system-determined and it can sometimes be altered by the database administrator.

The main problem with this approach is choosing a proper timeout value.

##### Deadlock prevention

The idea behind deadlock prevention is to kill transactions that **could** cause deadlocks. There are two types of deadlock prevention:

- **Resource-based prevention**: restrictions are imposed on lock requests
	- Transactions request all resources at once and only once
	- Resources are globally sorted and must be requested "in global order"
	- It is not easy for transactions to anticipate all requests though
- **Transaction-based prevention**: restrictions are based on transactions' IDs
	- Assigning IDs to transactions incrementally defines the transaction's age
	- The idea is to prevent older transactions from waiting for younger ones to end their work
	- There are options for choosing the transaction to kill:
		- **Preemptive**: kills the holding transaction
		- **Non-preemptive**: kills the requesting transaction
	- This method kills too many transactions, so it's slow

##### Deadlock detection

This method requires an algorithm to detect cycles in a wait-for graph and must work with distributed resources efficiently and reliably.

An elegant solution is **Obermarck's algorithm**, which makes the following assumptions:

- Transactions execute on a single main node
- Transactions may be decomposed in "sub-transactions" running on other nodes
- Synchronicity: when a transaction spawns a sub-transaction, it suspends work until the latter completes
- Two wait-for relationships: lock between two different transaction and lock between a transaction and one of its sub-transactions

##### Deadlocks in practice

The probability of a deadlock happening is much lower than the probability of a conflict occurring. Regardless, they still occur: once every minute in a mid-size bank.

The probability of a deadlock is **linear** in the number of transactions but **quadratic** in their length.

###### Update locks

There are some techniques to limit the frequency of deadlocks. One of these is the **update lock**: the most frequent deadlock occurs when two concurrent transactions start by reading the same resources and then decide to write and try to upgrade their lock to exclusive. To avoid this situation, systems offer the **update lock**, which is requested by transactions that will read and then write.

###### Hierarchical locking

Another technique to reduce deadlocks is **hierarchical locking**: update locks prudentially extend the interval during which a resource is locked.

Locks can be **specified with specific granularity**: you can lock not only a table, but a whole schema, a fragment, a page, a tuple or even just a field.

Hierarchical locking tries to lock the minimum amount of data and to recognise conflicts as soon as possible. Hierarchical locking is achieved by requesting resources top-down until the right level is obtained and releasing locks bottom-up.

The hierarchical locking scheme adds **three** new lock modes to the shared lock (SL) and exclusive lock (XL): the new modes express the **intention of locking at lower levels of granularity**:

- **ISL**: intention of locking a subelement of the current element in **shared** mode
- **IXL**: intention of locking a subelement of the current element in **exclusive** mode
- **SIXL**: lock of the element in shared mode with intention of locking a subelement in exclusive mode (so it is a sum of SL and IXL)

To request an SL or ISL lock on a non-root element, a transaction must hold an equally or more restrictive lock (ISL or IXL) on its parent.

To request an IXL, XL or SIXL lock on a non-root element, a transaction must hold an equally or more restrictive lock (SIXL or IXL) on its parent.

When a lock is requested on a resource, the lock manager decides based on the rules specified in the hierarchical lock granting table:

| Request \ Resource state | Free | ISL | IXL | SL  | SIXL | XL  |
| --------------------- | ---- | --- | --- | --- | ---- | --- |
| ISL                   | ✔️   | ✔️  | ✔️  | ✔️  | ✔️   | ⛌   |
| IXL                   | ✔️   | ✔️  | ✔️  | ⛌   | ⛌    | ⛌   |
| SL                    | ✔️   | ✔️  | ⛌   | ✔️  | ⛌    | ⛌   |
| SIXL                  | ✔️   | ✔️  | ⛌   | ⛌   | ⛌    | ⛌   |
| XL                    | ✔️   | ⛌   | ⛌   | ⛌   | ⛌    | ⛌   |

### Concurrency control based on timestamps

Locking is also named *pessimistic* concurrency control because it assumes that collisions will arise. In reality, collisions are rare.

Alternative and complementary methods to 2PL (and to locking in general) are **optimistic** concurrency control methods. One of these methods is based on **timestamps**, identifiers that define a total ordering of the events in a system.

Each transaction has a timestamp representing the time at which the transaction begins so that transactions can be ordered by "birth date". A schedule is accepted if and only if it reflects the serial ordering of the transactions induced by their timestamps.

#### Assigning timestamps in distributed systems

A timestamp is an indicator of the current time. If no "global time" is available, then a system needs to give out timestamps on requests.

A timestamp computed like this usually has a syntax that follows this paradigm:

```text
timestamp = event-id.node-id
```

In this case, we can say that timestamp 5.1 "occurs before" timestamp 5.2.

If some systems sends a transaction with a timestamp that exceeds the greatest timestamp computed by the database system, then the **Lamport method** is applied: the database system uses a "bumping rule" that updates the local timestamp to exceed the timestamp of the received transaction.

![](images/Pasted%20image%2020230925113152.png)

In this example:

- Events Y and F represent messages received from the "present" or "past", which "agree" with the local timestamp and are not bumped
- Events T, G and V represent messages received from the "future", so the local timestamp is incremented (bumped) accordingly, leaving a **hole** in the local event sequence

> Note that the timestamp of the received events T, G and V is generated so as to exceed that of the send event

#### Timestamp concurrency control principles

In a timestamp concurrency control system, the scheduler has two counters: $RTM(x)$, the index of the last reader, and $WTM(x)$, the index of the last writer.

The scheduler received read or write requests tagged with the timestamp of the requesting transaction:

- **Read transaction** $r_{ts}(x)$: if the timestamp of the read request is **lower** than the timestamp in $WTM(x)$, the request is **rejected** and the transaction is **killed**; otherwise, the access is **granted** and $RTM(x)$ is set to $\max(RTM(x), \text{ts})$
- **Write transaction** $w_{ts}(x)$: if the timestamp of the write request is **lower** than $RTM(x)$ or $WTM(x)$, the request is **rejected** and the transaction is **killed**; otherwise, access is **granted** and $WTM(x)$ is set to the received timestamp

With this policy, **many transactions are killed**.

#### 2PL vs. timestamps (TS)

2PL and TS are **incomparable**: there are some schedules that are in 2PL and are not in TS and viceversa. For example:

- In TS but not 2PL: `r1(x) w1(x) r2(x) w2(x) r0(y) w1(y)`
- In 2PL but not TS: `r2(x) w2(x) r1(x) w1(x)`
- Both 2PL and TS: `r1(x) r2(y) w2(y) w1(x) r2(x) w2(x)`

Even a serial schedule like `r2(x) w2(x) r1(x) w1(x)` is **not** in TS.

#### TS and CSR

If we consider CSR, we can say that:

$$\text{TS}\implies\text{CSR}$$

This is demonstrable through *reductio ad absurdum*.

#### TS and dirty reads

Basic TS-based control considers only committed transactions in the schedule: aborted transactions **are not considered**. This means that if aborts occur, dirty reads may happen.

To cope with dirty reads, a variant of basic TS must be used.

#### CSR, VSR, 2PL and TS

There's a summary of what we've found out until now:

![](images/Pasted%20image%2020230925115005.png)

#### Reducing the kill rate: Thomas Rule

In order to reduce the number of transactions that get killed in TS-based systems, the **Thomas Rule** can be implemented:

> When a write transaction is received:
> 
> - If $\text{ts}<RTM(x)$, the request is **rejected** and the transaction is killed
> - If $\text{ts}<WTM(x)$, then our write is obsolete and it can be **skipped**
> - Otherwise, access is **granted** and $WTM(x)$ is set to $\text{ts}$

The rationale behind this rule is that writing on an object that has already been written on by a younger transaction is **useless**, but it does not require the system to kill the transaction as a whole, so **only the write is skipped**.

With this modification, we obtain the following set:

![](images/Pasted%20image%2020230925115949.png)

We are **breaking the boundary** set by CSR, proving that it is a little restrictive, but we are also going outside of VSR: Thomas Rule makes it possible to "correct" schedules that are normally outside of the acceptable range put by VSR, but it also removes operations from transactions, which is not fair.

#### Multiversion concurrency control

> To be continued...
