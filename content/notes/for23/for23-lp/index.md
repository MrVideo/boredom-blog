---
title: 'Linear Programming'
draft: false
type: 'page'
toc: true
mathjax: true
---

---

## Download as PDF

You can download this note as a PDF by clicking [here](lp.pdf).

---

## Equivalent forms

A problem is in **standard form** if it:

1. **Only has equality constraints**, no inequality constraints are allowed
2. **Only has non-negative variables**, nil and negative variables are not allowed

To transform constraints:

- If the constraint is in the form $\underline a^T\underline x \le \underline b$, I can add a **slack** variable $s\ge 0$ to let the left side of the equation reach the value of the right side, and obtain:
  $$\begin{cases} \underline a^T\underline x + s = \underline b\\\ s\ge 0 \end{cases}$$
- If the constraint is in the form $\underline a^T\underline x \ge \underline b$, I can subtract a **surplus** variable $s\ge 0$ to let the left side of the equation reach the value of the right side, and obtain:
  $$\begin{cases} \underline a^T\underline x - s = \underline b\\\ s\ge 0 \end{cases}$$

To transform variables:

- If a variable $x_j$ is **unrestricted in sign**, it can be expressed as the difference of its positive and negative parts:
  $$\begin{cases} x_j = x_j^+ - x_j^-\\\ x_j^+, x_j^- \ge 0 \end{cases}$$
  After the substitution, we can delete $x_j$ from the problem.

All other transformations are very straightforward and are related to changing the signs of constraint equations and inequalities.

## Geometry of linear programming

An **unbounded feasible direction** is a vector that, placed at any point within a polyhedron $P$, can continue forever.

That is, the direction in which the vector is pointing is **always contained within the polyhedron**, infinitely, **regardless of the vector's length or point of origin**.

This definition can help us define polyhedra in a new way:

> **Weyl-Minkowski Theorem**
>
> Every point $x$ of a polyhedron $P$ can be expressed as a **convex combination of its vertices** $\underline x_1, \ldots, \underline x_k$ and, if needed, an **unbounded feasible direction** $\underline d$ of $P$:
> $$\underline x = \alpha_1\underline x_1 + \ldots + \alpha_k\underline x_k + \underline d, \text{ with } \alpha_i \ge 0,\ \sum_{i=1}^k \alpha_i = 1$$

Unbounded feasible directions are not needed in **polytopes**, which are polyhedra in which the only unbounded feasible direction is $\underline d = \underline 0$. This means that polytopes can be described through just the convex combination of their vertices. For example:

$$\underline x = \alpha_1\underline x_1 + \alpha_2\underline x_2 + \alpha_3\underline x_3, \text{ with } \alpha_i \ge 0 \text{ and } \sum_{i=1}^3 \alpha_i = 1$$

Given the above information, we can enunciate the Fundamental Theorem of Linear Programming:

> **Fundamental Theorem of Linear Programming**
>
> Consider a Linear Programming problem such as:
> $$\min\  \{ \underline c^T\underline x : \underline x\in P \}$$
> Where $P\subseteq \mathbb R^n$ is a non-empty polyhedron in standard or canonical form.
> Then, either there exists at least one **optimal vertex**, or the value of the objective function is **unbounded below** on $P$.

There are four types of Linear Programming problems:

1. **Unique optimal solution**: only one vertex has no *improving directions*:
   ![](../images/Pasted%20image%2020231126152116.png)
2. **Multiple optimal solutions**: a whole segment has no *improving directions*:
   ![](../images/Pasted%20image%2020231126152209.png)
3. **Unbounded solution**: no optimal vertex can be found:
   ![](../images/Pasted%20image%2020231126152400.png)
4. **Infeasible solution**: the feasible region is an empty polyhedron:
   ![](../images/Pasted%20image%2020231126152436.png)

## Basic feasible solutions and vertices of polyhedra

Since we discovered that we can find optimal solutions by checking the vertices of feasible polyhedra, let's find a way to compute vertices algebraically.

We know that vertices correspond to the intersections of hyperplanes associated to the $n$ constraint inequalities in Linear Programming problems. However, in standard form, we have no inequalities.

In order to solve this problem, we can begin from the canonical form of a problem and transform it into standard form in the ways we've seen before.

If this is done, every constraint in $P$ now **corresponds to a slack variable** in the new polyhedron $P'$ and, when $s_i=0$, the **constraint is satisfied** through an equality.

It must be noted that, when computing intersections in $P'$, if any variable or slack variable is negative, the found solution is infeasible:

![](../images/Pasted%20image%2020231126153924.png)

We must now define which are the vertices of a polyhedron in standard form. It is quite simple:

> **Property of standard form polyhedra**
>
> For any polyhedron $P = \{ \underline x \in \mathbb R^n : A\underline x = \underline b, \ \underline x \ge \underline 0 \}$:
> 1. The **facets** are obtained by setting one variable to zero
> 2. The **vertices** are obtained by setting $n-m$ variables to zero, where:
> 	- $n$ is the number of variables in the problem
> 	- $m$ is the number of constraints in the problem

We can now formally characterise vertices.

Consider any polyhedron in standard form and assume that $A\in \mathbb R^{m\times n}$ is such that $A$ is of rank $m$. This is **equivalent to assume** that there are **no redundant constraints** (so all rows and columns in the matrix are linearly independent).

Now:

- If $m=n$, there is a unique solution to $A\underline x = \underline b$, which is:
  $$\underline x = A^{-1}\underline b$$
- If $m<n$, there are $\infty^{n-m}$ solutions of $A\underline x = \underline b$. We can also say that the system has $n-m$ degrees of freedom or that $n-m$ variables can be fixed arbitrarily. If we do fix $m-n$ solutions arbitrarily, we **find a vertex**.

If we consider the $A$ matrix from before, we can define a **basis** of such matrix as a subset of $m$ columns of $A$ that are linearly independent and form an $m\times m$ **non-singular** matrix $B$. We can so redefine $A$ as:

$$A = [ \underbrace{B}_m | \underbrace{N}_{n-m} ]$$

Now, let $\underline x = [\underline x_B^T | \underline x_N^T]^T$.

Then, any system $A\underline x = \underline b$ can be written as:

$$B\underline x_B + N\underline x_N = \underline b$$

For any set of values for $\underline x_N$, if $B$ is non-singular, we have:

$$\underline x_B = B^{-1}b - B^{-1}N\underline x_N$$

Finally we can say that:

- A **basic solution** is a solution obtained by setting $\underline x_N = \underline 0$ and consequently letting $\underline x_B = B^{-1}\underline b$.
- A basic solution with $\underline x_B \ge 0$ is known as a **basic feasible solution**.
- We call the variables in $\underline x_B$ **basic variables** and the variables in $\underline x_N$ **non-basic variables**.

Now that we defined everything that we need, we can enunciate the following theorem:

> **Theorem**
>
> $\underline x \in \mathbb R^n$ is a **basic feasible solution** if and only if $\underline x$ is a **vertex** of $P = \{ \underline x \in \mathbb R^n : A\underline x = \underline b, \ \underline x \ge \underline 0 \}$.

The number of basic feasible solutions of any given Linear Programming problem is always smaller or equal to $\binom{n}{m}$.

## The Simplex method

### Optimality test

Given a Linear Programming problem like $\min \ \{ \underline c^T \underline x : A \underline x = \underline b, \ \underline x > \underline 0 \}$ and a feasible basis $B$ of $A$, $A\underline x = \underline b$ can be rewritten as:

$$B\underline x_B + N\underline x_N = \underline b$$

From this equation we can extract $\underline x_B$ as:

$$\underline x_B = B^{-1}\underline b - B^{-1}N\underline x_N, \text{ with } B^{-1}\underline b \ge 0$$

Then, a **basic feasible solution** is such that $\underline x_B = B^{-1}\underline b, \ \underline x_N = \underline 0$, as we said earlier.

By substitution, we can express the objective function in terms of the non-basic variables only:

$$\begin{aligned}
\underline c^T \underline x &= \big( \underline c_B^T\ |\ \underline c_N^T \big) \begin{bmatrix} \underline x_B \\\ \underline x_N \end{bmatrix}\\\
&= \big( \underline c_B^T\ |\ \underline c_N^T \big) \begin{bmatrix} B^{-1}\underline b - B^{-1}N\underline x_N \\\ \underline x_N \end{bmatrix}\\\
&= \underline c_B^T B^{-1} \underline b + \big( \underline c_N^T - \underline c_B^T B^{-1} N \big)\underline x_N\\\
&= z_0 + \underline{\overline{c}}_N^T\underline x_N
\end{aligned}$$

Now we can say:

- The parameter $z_0 = \underline c_B^T B^{-1}\underline b$ is the cost of $\underline x = \big(\underline x_B \ | \ \underline x_N\big)^T$, where $\underline x$ is a basic feasible solution
- The parameter $\underline{\overline{c}}_N^T = \underline c_N^T - \underline c_B^T B^{-1} N$ defines the **reduced costs** of the non-basic variables

We can use the parameters above to define the vector of reduced costs for a basis:

> **Vector of reduced costs with respect to a basis $B$**
>
> $$\begin{aligned}
> \underline{\overline{c}}^T &= \underline c^T - \underline c_B^TB^{-1}A\\\
> &= \big[ \underline c_B^T - \underline c_B^T B^{-1}B \ | \ \underline c_N^T - \underline c_B^T B^{-1}N \big]\\\
> &= \big[ \underline 0^T \ | \ \underline{\overline{c}}_N^T \big]
> \end{aligned}$$

If we consider the same Linear Programming problem as before, we can now say that:

> **Proposition 1**
>
> If $\underline{\overline{c}}_N \ge \underline 0$[^1], then the basic feasible solution $\big( \underline x_B^T \ | \ \underline x_N^T \big)$ of cost $\underline c_B^TB^{-1}\underline b$, where $\underline x_B = B^{-1}\underline b \ge 0$ and $\underline x_N = \underline 0$, is a **global optimum**.

> **Example**
>
> Let's take a look at the following example:
> $$\begin{matrix}
> &\min &z= &-x_1 &-x_2 &\\\
> &\text{s.t.} & &x_1 &-x_2 &+s_1 &= 1\\\
> & &x_1 &+x_2 & &+s_2 &=3\\\
> & &x_1, &x_2, &s_1, &s_2 &\ge 0
> \end{matrix}$$
> If we consider a BFS with $\underline x_B = \big( x_1 \ | \ s_2 \big)^T$, then we must put the other non-basic variables to zero, which means that $\underline x_N = \big( x_2 \ | \ s_1 \big)^T = \underline 0^T$. We obtain the following model:
> $$\begin{matrix}
> &\min &z= &-x_1 &-0 &\\\
> &\text{s.t.} & &x_1 &-0 &+0 &= 1\\\
> & &x_1 &+0 & &+s_2 &=3\\\
> & &x_1, &x_2, &s_1, &s_2 &\ge 0
> \end{matrix}$$
> From the above equations we can now extract the values of $x_1$, $s_2$ and $z$:
> $$\begin{matrix}
> &\min &z= &-x_1 & & &=-1\\\
> &\text{s.t.} & &x_1 & & &= 1\\\
> & & & & &s_2 &=2\\\
> & &x_1, &x_2, &s_1, &s_2 &\ge 0
> \end{matrix}$$
> We can also write the $B$ and $N$ matrices:
> $$B = \begin{bmatrix} 1 & 0 \\\ 1 & 1 \end{bmatrix}, N = \begin{bmatrix} -1 & 1 \\\ 1 & 0 \end{bmatrix}$$
> Returning to the beginning for a minute, we note that the cost vector $\underline c$ is:
> $$\underline c = \big[ -1\ -1\ 0\ 0 \big]^T$$
> So now we can extract $\underline c_B^T$ and $\underline c_N^T$:
> $$\underline c_B^T = \underline c_N^T = \big[ -1 \ 0 \big]^T$$
> Once this is done, we can calculate the reduced costs for $x_2$ and $s_1$:
> $$\underline{\overline{c}}_N^T = \underline c_N^T - \underline c_B^T B^{-1}N = \big[ -2 \ 0 \big]^T$$
> Since we know that we are in a global optimum if $\underline{\overline{c}}_N^T \ge 0$, we see that we can move to a better vertex thanks to the reduced cost vector.
> Specifically, if $x_2$ can be increased from 0 to 1 while keeping $s_1 = 0$, then $z$ can vary by -2.
> In practice, we now know that, in order to minimise $z$ more, we can move from the green vertex $(1,0)$ to the blue vertex $(2, 1)$, as shown below:
> ![](../images/Pasted%20image%2020231127105457.png)

### Move to an adjacent vertex

When moving from a vertex to another, we are simply substituting a column from $B$ with a column from $N$. To better understand this, take a look at the example below:

![](../images/Pasted%20image%2020231127105657.png)

In order to understand *where* to move, we can express the basic variables in terms of the non-basic ones and "choose" a direction to move in. Taking the same example as before, we can write:

$$\begin{aligned}
s_1 &= 6 - x_1 - x_2\\\
s_2 &= 8 - 2x_1 - x_2
\end{aligned}$$

If we decide to move on $x_1$, then we set $x_2 = 0$ and increase $x_1$. But how do we know how much we should increase it by?

Taking the previous equations, we can say that, since $x_1, x_2, s_1, s_2 \ge 0$:

$$\begin{aligned}
s_1 &= 6 - x_1 \ge 0\\\
s_2 &= 8 - 2x_1 \ge 0
\end{aligned}$$

Solving these inequalities gives us two upper bounds:

$$\begin{aligned}
x_1 &\le 6\\\
x_1 &\le 4
\end{aligned}$$

We can now check which solutions are feasible by substituting their value in the equations above:

- For $x_1 = 6$:
  $$\begin{aligned} s_1 &= 6 - 6 = 0\\\ s_2 &= 8 - 12 = -4 \end{aligned}$$
  Since $s_2 < 0$, the solution is infeasible.
- For $x_1 = 4$:
  $$\begin{aligned} s_1 &= 6 - 4 = 2\\\ s_2 &= 8 - 8 = 0 \end{aligned}$$
  Since both $s_1$ and $s_2$ are non-negative, the solution is feasible.

We can also see the result above through the graph (where vertex 5 is the feasible solution, while vertex 4 is the infeasible one):

![](../images/Pasted%20image%2020231127115704.png)

In general, we can apply the **change of basis** method to minimise a Linear Programming problem:

> **Change of basis for a minimisation Linear Programming problem**
>
> Let $B$ be a feasible basis and $x_s$ in $\underline x_N$ a non-basic variable with a reduced cost $\overline c_s < 0$. Now:
> 1. **Increase** $x_s$ **as much as possible** (we say that $x_s$ *enters the basis*) while keeping the other non-basic variables equal to zero
> 2. The basic variable $x_r$ in $\underline x_B$ such that $x_r\ge 0$ imposes the **tightest upper bound** $\theta^*$ on the increase of $x_s$ (we say that $x_r$ *leaves the basis*)
> 3. If $\theta^*>0$, the new basic feasible solution has a better objective function value. The new basis differs by a single column with respect to the previous one.

Since the basis $B$ changes when moving from a canonical form to the next, one may think that $B^{-1}$ should be computed all over again. However, we only need a **pivoting** operation in order to recompute it:

> **Pivoting operation**
>
> Given the system $A\underline x = \underline b$:
> 1. Select a coefficient $\overline a_{rs} \ne 0$: this will be our **pivot**
> 2. Divide the $r$-th row by $\overline a_{rs}$
> 3. For each row $i$ with $i \ne r$ and $\overline a_{is}\ne 0$, subtract the resulting $r$-th row multiplied by $\overline a_{is}$.
> 
> This is similar to the operations used in the Gaussian elimination method to solve systems of linear equations.

Let's look at an example starting from the following matrices:

$$A = \begin{bmatrix}
1 & 1 & 1 & 0\\\
2 & 1 & 0 & 1
\end{bmatrix}, \underline b = \begin{bmatrix}
6\\\
8
\end{bmatrix}$$

We will now write the two matrices next to each other, highlighting the chosen row and column for our example:

$$\begin{matrix}
& \textcolor{blue}{s} & & & &\\\
& 1 & 1 & 1 & 0 & 6\\\
\textcolor{blue}{r} & \textcolor{red}{2} & 1 & 0 & 1 & 8
\end{matrix}$$

Now, let's apply the algorithm as written above: we chose our 2 for a pivot, so now we divide the row containing 2, which is $r$, by 2:

$$\begin{matrix}
& \textcolor{blue}{s} & & & &\\\
& \textcolor{green}{1} & 1 & 1 & 0 & 6\\\
\textcolor{blue}{r} & \textcolor{red}{1} & {1\over2} & 0 & {1\over2} & 4
\end{matrix}$$

Finally, we subtract each row in the matrix that is not $r$ with the resulting $r$ row, multiplied by the coefficient in the same column as 2. In this case, we only have another row, in which $\overline a_{is} = 1$:

$$\begin{matrix}
& \textcolor{blue}{s} & & & &\\\
\textcolor{green}{i}& 0 & {1\over2} & 1 & -{1\over2} & 2\\\
\textcolor{blue}{r} & \textcolor{red}{1} & {1\over2} & 0 & {1\over2} & 4
\end{matrix}$$

Summing up, in order to move to a better vertex, we must answer the following two questions:

1. Which non-basic variable enters the basis?
	- Any variable with reduced cost $\overline c_j < 0$
	- A variable that yields the maximum $\Delta z$
2. Which basic variable leaves the basis?
	- This is decided via the **min ratio test**: the variable of index $i$ with smallest ${\overline b_i\over \overline a_{is}} = \theta^*$ among those with $\overline a_{is} > 0$ is the one that leaves the basis

Both variables can be decided by applying **Bland's rule**:

> **Bland's rule**
>
> The variable that enters the basis is the one with index $s$ such that:
> $$s = \min\ \{ j:\overline c_j<0 \}$$
> The variable that leaves the basis is the one with index $r$ such that:
> $$r = \min\ \bigg\{ i: {\overline b_i\over \overline a_{is}}=\theta^*, \ \overline a_{is}>0 \bigg\}$$

A Linear Programming problem is said to be **unbound** if there exists a variable with a reduced cost $\overline c_j<0$ with $\overline a_{ij}\le 0, \ \forall i$. In other words, a problem is unbounded if **no element** of the $j$-th column **can be a pivot**.

### Tableau representation

Linear Programming problems in standard form can easily be visualised in the so called **Tableau representation**.

Let's take the following problem as an example:

$$\begin{matrix}
\min & -x_1 & -x_2 & & &\\\
\text{s.t.} & 6x_1 &+4x_2 &+x_3 & &=24\\\
&3x_1 &-2x_2 & &+x_4 &=6\\\
&x_1, &x_2, &x_3, &x_4 &\ge 0
\end{matrix}$$

The Tableau representation of the above problem is:

$$\begin{matrix}
&&x_1 &x_2 &x_3 &x_4\\\
-z &0 &-1 &-1 &0 &0\\\
x_3 &24 &6 &4 &1 &0\\\
x_4 &6 &3 &-2 &0 &1
\end{matrix}$$

Applying Bland's rule, we find that the variable entering the basis is $x_1$, while the one exiting the basis is $x_4$. We find that the pivot is 3, as shown:

$$\begin{matrix}
&&\textcolor{blue}{x_1} &x_2 &x_3 &x_4\\\
-z &0 &-1 &-1 &0 &0\\\
x_3 &24 &6 &4 &1 &0\\\
\textcolor{blue}{x_4} &6 &\textcolor{red}{3} &-2 &0 &1
\end{matrix}$$

Now, we can divide the $x_4$ row by the pivot and subtract it from the $x_3$ and $-z$ rows:

$$\begin{matrix}
&&x_1 &x_2 &x_3 &x_4\\\
-z &2 &0 &-{5\over 3} &0 &{1\over 3}\\\
x_3 &12 &0 &8 &1 &-2\\\
\textcolor{red}{x_1} &2 &1 &-{2\over 3} &0 &{1\over 3}
\end{matrix}$$

We can continue by applying iteratively the above operations, until we only have non-negative reduced costs:

$$\begin{matrix}
&&x_1 &x_2 &x_3 &x_4\\\
-z &6 &\textcolor{red}{1\over2} &\textcolor{red}{0} &\textcolor{red}{1\over4} &\textcolor{red}{0}\\\
x_2 &6 &{3\over2} &1 &{1\over 4} &0\\\
x_4 &18 &6 &0 &{1\over2} &1
\end{matrix}$$

So we can conclude that the basic feasible solution (composed of nil non-basic variables and non-negative basic variables) is $\underline x^* =(0,6,0,18)^T$.

### Degenerate basic feasible solutions

In some cases, basic variables **can be nil**. If that happens, the basic feasible solution found is said to be **degenerate**.

A solution with more than $n-m$ zeroes (where $n$ is the number of variables and $m$ is the number of constraints, as mentioned before) corresponds to more than one basis, which also means that more than $n$ constraints are satisfied with equality.

In the presence of degenerate basic feasible solutions, a basis change **may not decrease the objective function value**, since $\theta^*$ could be zero and the new optimised solution remains the same as the previous one.

It should be noted that a degenerate BFS can arise from a non-degenerate one: even if $\theta^*>0$, several basic variables may become nil when $x_s$ is increased to $\theta^*$.

The main problem with degenerate bases is that one can **cycle through a sequence** of them when solving a problem. Several anti-cycling rules have been proposed for the choice of the variables that enter and exit the bases, like Bland's rule.

When applying Bland's rule, the Simplex algorithm is guaranteed to terminate after at most $\binom{n}{m}$ iterations, since the number of pivots is finite.

In some pathological cases, the number of iterations may grow exponentially with respect to $n$ or $m$. However, the Simplex algorithm is overall very efficient. Extensive experimental campaigns show that the number of iterations grows linearly with respect to $m$ and very slowly with respect to $n$.

### Two-phase Simplex method

Let's take the following problem as an example:

$$\begin{matrix}
\min &x_1 & &+x_3 &\\\
\text{s.t.} &x_1 &+2x_2 & &\le 5\\\
& &x_2 &+2x_3 &=6\\\
&x_1, &x_2, &x_3 &\ge 0
\end{matrix}$$

Let's transform it into standard form:

$$\begin{matrix}
\min &x_1 & &+x_3 & &\\\
\text{s.t.} &x_1 &+2x_2 & &+x_4 &= 5\\\
& &x_2 &+2x_3 & &=6\\\
&x_1, &x_2, &x_3, &x_4 &\ge 0
\end{matrix}$$

We notice that the problem is not in canonical form: that is, the $A$ matrix does not contain a $2\times 2$ submatrix which is the identity matrix.

In order to be able to solve this problem, we can use an **auxiliary, artificial problem** which has this form:

$$\begin{matrix}
\min &v = \sum_{i=1}^m y_i\\\
\text{s.t.} &A\underline x  +I\underline y = \underline b\\\
&\underline x, \underline y \ge 0
\end{matrix}$$

Basically, we are adding some **artificial variables** that can help us find an identity matrix in the original problem (which we'll identify as $P$) by **minimising the sum of the artificial variables** in the auxiliary problem (which we'll identify as $P_A$).

One obvious initial basic solution for $P_A$ is:

$$\begin{cases}
\underline y = \underline b \ge 0\\\
\underline x = \underline 0
\end{cases}$$

Now, we have two options:

1. If $v^*>0$, then $P$ is **infeasible**
2. If $v^*=0$, then clearly $\underline y^* = 0$ and $\underline x^*$ is a basic feasible solution of $P$

Depending on whether or not the auxiliary variables $y_i$ are basic, $P_A$ is solved differently:

- If $y_i$ are non-basic $\forall i$, then the corresponding columns are deleted and a Tableau representation is obtained with respect to some basis. The objective function row (the $z$ row) must be determined by substitution.
- If at least one $y_i$ variable is basic (which also means the basic feasible solution is degenerate), a pivot operation is performed with respect to a non-zero coefficient of the row of $y_i$ so as to exchange $y_i$ with any other non-basic variable $x_j$.

Let's look at an example: our main problem $P$ is:

$$\begin{matrix}
\min &x_1 &+x_2 &+10x_3\\\
\text{s.t.} & &x_2 &+4x_3 &=2\\\
&-2x_1 &+x_2 &-6x_3 &=2\\\
&x_1, &x_2, &x_3 &\ge 0
\end{matrix}$$

We define our auxiliary problem $P_A$ as:

$$\begin{matrix}
\min &v & & &=y_1 &+y_2 &\\\
\text{s.t.} & &x_2 &+4x_3 &+y_1 & &=2\\\
&-2x_1 &+x_2 &-6x_3 & &+y_2 &=2\\\
&x_1, &x_2, &x_3, &y_1, &y_2 &\ge 0
\end{matrix}$$

We can write $v=y_1+y_2$ in canonical form by expressing $y_1$ and $y_2$ in terms of $x_1, x_2$ and $x_3$. Now we obtain the Tableau form like so:

$$\begin{matrix}
& &x_1 &x_2 &x_3 &y_1 &y_2\\\
-v &-4 &2 &-2 &2 &0 &0\\\
y_1 &2 &0 &1 &4 &1 &0\\\
y_2 &2 &-2 &1 &-6 &0 &1
\end{matrix}$$

From here on, we can apply the Simplex method as we've seen earlier, and we reach the end of the first phase of the two-phase Simplex method by obtaining the optimal solution for $P_A$:

$$\begin{cases}
\underline x^* = (0,2,0)^T\\\
\underline y^* = (0,0)^T
\end{cases}$$

Now, we need to express the auxiliary problem in a basis consisting of the $x_i$ variables only, to return to the original problem. We obtain:

$$\begin{matrix}
& &x_1 &x_2 &x_3 &y_1 &y_2\\\
-v &0 &0 &0 &0 &1 &1\\\
x_2 &2 &0 &1 &4 &1 &0\\\
x_1 &0 &1 &0 &5 &{1\over2} &-{1\over2}
\end{matrix}$$

We note that the optimal solution $\underline x^*$ found earlier is also a basic feasible solution of $P$.

The only thing we're missing now is an expression of the original objective function in only non-basic variables. The objective function of $P$ was:

$$z = x_1 + x_2 + 10x_3$$

Looking at the Tableau representation, we obtain the following equations:

$$\begin{cases}
2 = x_2+4x_3\\\
0 = x_1 + 5x_3
\end{cases}$$

By substituting in the objective function, we obtain:

$$z = 2 + x_3$$

We can now write the Tableau representation for $P$ and enter phase two of the two-phase Simplex method, which consists in optimising the original problem:

$$\begin{matrix}
& &x_1 &x_2 &x_3\\\
-z &2 &0 &0 &1\\\
x_2 &2 &0 &1 &4\\\
x_1 &0 &1 &0 &5
\end{matrix}$$

Fortunately, we can see that the solution we found earlier is already optimal (there are no negative costs), so there is no need to complete phase two.

---

> **Note for the reader**
>
> The following paragraphs are more detailed than the ones above.

---

## Linear Programming duality

Given any minimisation problem, we can associate a related maximisation problem to it. This, of course, works the other way around too.

The two problems will likely have different spaces and objective functions. However, generally, their optimal value will coincide.

The fact that we can formulate a dual problem to the one we currently have is useful, especially when we have to estimate the optimal value of our main problem.

Let's take a look at this example:

$$\begin{matrix}
\max &z &=4x_1 &+x_2 &+5x_3 &+3x_4 & & \\\
\text{s.t.} & &x_1 &-x_2 &-x_3 &+3x_4 &\le 1 &(1)\\\
& &5x_1 &+x_2 &+3x_3 &+8x_4 &\le 55 &(2)\\\
& &-x_1 &+2x_2 &+3x_3 &-5x_4 &\le 3 &(3)\\\
& &x_1, &x_2, &x_3, &x_4 &\ge 0
\end{matrix}$$

The feasible solutions of this problem provide us with lower bounds for $z^*$:

- $(0,0,1,0) \implies z^* \ge 5$
- $(2, 1, 1, 1/3)\implies z^* \ge 15$
- $(3, 0, 2, 0) \implies z^*\ge 22$

Unfortunately, we can't be sure about which one is the best lower bound. However, by multiplying constraint 2 by $5/3$, we obtain an inequality that dominates the objective function:

$$\begin{aligned}
{25\over3}x_1 + {5\over3}x_2 + 5x_3 +{40\over3}x_4 &\le {275\over3}\\\
4x_1 + x_2 + 5x_3 + 3x_4 &\le {25\over3}x_1 + {5\over3}x_2 + 5x_3 + {40\over3}x_4\\\
z^* &\le {275\over 3}
\end{aligned}$$

Furthermore, by adding constraints 2 and 3, we obtain:

$$\begin{aligned}
4x_1 +x_2 +5x_3 +3x_4 &\le 4x_1 + 3x_2 + 6x_3 + 3x_4 \le 58\\\
z^* &\le 58
\end{aligned}$$

We can see that linear combinations of inequality constraints with non-negative multiplier yield valid upper bounds.

We have found a general strategy to calculate an upper bound on the optimal solution of a linear programming problem: linearly combine the constraints with non-negative multiplicative factors. In the example above, we have used the factors:

1. $y_1=0, y_2 = 5/3, y_3=0$
2. $y_1=0, y_2 = 1, y_3=1$

In general, any linear combination of the constraints 1, 2 and 3 reads:

$$\begin{aligned}
y_1(x_1-x_2-x_3+3x_4)&+\\\
y_2(5x_1+x_2+3x_3+8x_4)&+\\\
y_3(-x_1+2x_2+3x_3-5x_4)&\le y_1 +55y_2 +3y_3
\end{aligned}$$

Which is equivalent to:

$$\begin{aligned}
(y_1+5y_2-y_3)x_1 &+\\\
(-y_1+y_2+2y_3)x_2 &+\\\
(-y_1+3y_2+3y_3)x_3 &+\\\
(3y_1+8y_2-5y_3)x_4 &\le y_1+55y_2+3y_3
\end{aligned}$$

In order to use the left side of the inequality as an upper bound on our objective function $z = 4x_1 + x_2 + 5x_3 + 3x_4$, we must have:

$$\begin{cases}
\begin{matrix}
y_1 &+5y_2 &-y_3 &\ge 4\\\
-y_1 &+y_2 &+2y_3 &\ge 1\\\
-y_1 &+3y_2 &+3y_3 &\ge 5\\\
3y_1 &+8y_2 &-5y_3 &\ge 3\\\
y_1, &y_2, &y_3 &\ge 0
\end{matrix}
\end{cases}$$

In such a case, any feasible solution satisfies the inequality:

$$4x_1 + x_2 + 5x_3 + 3x_4 \le y_1+55y_2+3y_3$$

In particular, we can say:

$$z^* \le y_1+55y_2+3y_3$$

So we have formulated the so called **dual problem**. Our primal problem was:

$$\begin{matrix}
\max &z &=4x_1 &+x_2 &+5x_3 &+3x_4 & & \\\
\text{s.t.} & &x_1 &-x_2 &-x_3 &+3x_4 &\le 1 &(1)\\\
& &5x_1 &+x_2 &+3x_3 &+8x_4 &\le 55 &(2)\\\
& &-x_1 &+2x_2 &+3x_3 &-5x_4 &\le 3 &(3)\\\
& &x_1, &x_2, &x_3, &x_4 &\ge 0
\end{matrix}$$

And now we try to find an upper bound to its solution by solving our dual problem:

$$\begin{matrix}
\min &y_1 &+55y_2 &+3y_3 &\\\
\text{s.t.} &y_1 &+5y_2 &-y_3 &\ge 4\\\
&-y_1 &+y_2 &+2y_3 &\ge 1\\\
&-y_1 &+3y_2 &+3y_3 &\ge 5\\\
&3y_1 &+8y_2 &-5y_3 &\ge 3\\\
&y_1, &y_2, &y_3 &\ge 0
\end{matrix}$$


> **Dual problems**
>
> The general form for primal and dual problems of this kind is:
> $$\begin{matrix}
> &(P)
> &\begin{matrix}
> \max &z=\underline c^T\underline x\\\
> \text{s.t.} &A\underline x \le \underline b\\\
> &\underline x \ge \underline 0
> \end{matrix}
> &
> &(D)
> &\begin{matrix}
> \min &w=\underline b^T\underline y\\\
> \text{s.t.} &A^T\underline y \ge \underline c\\\
> &\underline y \ge \underline 0
> \end{matrix}
> \end{matrix}$$
> For standard form, we have:
> $$\begin{matrix}
> &(P)
> &\begin{matrix}
> \min &z=\underline c^T\underline x\\\
> \text{s.t.} &A\underline x=\underline b\\\
> &\underline x\ge0
> \end{matrix}
> &
> &(D)
> &\begin{matrix}
> \max &w=\underline b^T\underline y\\\
> \text{s.t.} &A^T\underline y\le \underline c\\\
> &\underline y\in\mathbb R
> \end{matrix}
> \end{matrix}$$

We can now enunciate the **weak duality theorem**:

> **Weak duality theorem**
>
> Given the primal and dual problems:
> $$\begin{matrix}
> &(P)
> &\begin{matrix}
> \min &z=\underline c^T\underline x\\\
> \text{s.t.} &A\underline x \ge \underline b\\\
> &\underline x \ge \underline 0
> \end{matrix}
> &
> &(D)
> &\begin{matrix}
> \max &w=\underline b^T\underline y\\\
> \text{s.t.} &A^T\underline y \le \underline c\\\
> &\underline y \ge \underline 0
> \end{matrix}
> \end{matrix}$$
> With $X = \{ \underline x \in \mathbb R^n : A\underline x \ge \underline b, \underline x \ge \underline 0 \} \ne \emptyset$ and $Y = \{ \underline y \in \mathbb R^m : A^T\underline y \le \underline c, \underline y \ge \underline 0 \}\ne\emptyset$.
> For every feasible solution $\underline x \in X$ of $(P)$ and every feasible solution $\underline y\in Y$ of $(D)$ we have:
> $$\underline b^T\underline y \le \underline c^T\underline x$$

As a consequence of this theorem, if $\underline x$ is a feasible solution of $(P)$, $\underline y$ is a feasible solution of $(D)$ and $\underline c^T\underline x =\underline b^T\underline y$, then $\underline x$ **is optimal for** $(P)$ **and** $\underline y$ **is optimal for** $(D)$.

So we can enunciate the **strong duality theorem**:

> **Strong duality theorem**
>
> If $X = \{ \underline x \in \mathbb R^n : A\underline x \ge \underline b, \underline x \ge \underline 0 \} \ne \emptyset$ and $\min\ \{ \underline c^T\underline x : \underline x \in X \}$ is finite, there exist $\underline x^* \in X$ and $\underline y^* \in Y$ such that:
> $$\underline c^T\underline x^* = \underline b^T\underline y^*$$

For any pair of primal-dual problems, only four cases can arise among the following:

| $(P)$ \ $(D)$               | Finite optimal solution                 | Unbounded problem                     | Infeasible problem                    |
| --------------------------- | --------------------------------------- | ------------------------------------- | ------------------------------------- |
| **Finite optimal solution** | **Yes**, for [strong duality](#linear-programming-duality) | No                                    | No                                    |
| **Unbounded problem**       | No                                      | No                                    | **Yes**, for [weak duality](#linear-programming-duality) |
| **Infeasible problem**      | No                                      | **Yes**, for [weak duality](#linear-programming-duality) | **Yes**                               |

### Optimality conditions

Given the pair of problems:

$$\begin{matrix}
&(P)
&\begin{matrix}
\min &z=\underline c^T\underline x\\\
\text{s.t.} &A\underline x \ge \underline b\\\
&\underline x \ge \underline 0
\end{matrix}
&
&(D)
&\begin{matrix}
\max &w=\underline b^T\underline y\\\
\text{s.t.} &\underline y^TA \le \underline c^T\\\
&\underline y \ge \underline 0
\end{matrix}
\end{matrix}$$

Two feasible solutions $\underline x^*\in X$ and $\underline y^*\in Y$, with $X = \{ \underline x \in \mathbb R^n : A\underline x \ge \underline b, \underline x \ge \underline 0 \}$ and $Y = \{ \underline y \in \mathbb R^m : \underline y^TA\le\underline c^T, \underline y \ge \underline 0 \}$ are optimal if and only if $\underline{y^*}^T\underline b = \underline c^T\underline x^*$.

If $x_j$ and $y_i$ are unknown, this is a single equation in $n+m$ unknowns.

However, since $\underline{y^*}^T\underline b\le \underline{y^*}^TA\underline x^* \le \underline c^T\underline x^*$, we have:

$$\begin{aligned}
\underline{y^*}^T\underline b &= \underline{y^*}^TA\underline x^*\\\
\underline{y^*}^TA\underline x^* &= \underline c^T\underline x^*
\end{aligned}$$

Therefore:

$$\begin{aligned}
\underline{y^*}^T(A\underline x^* - \underline b) &= \underline 0\\\
(\underline c^T - \underline{y^*}^TA)\underline x^* &= \underline 0
\end{aligned}$$

These are $n+m$ equations in $n+m$ unknowns, and so **necessary and sufficient optimality conditions**.

> **Complementary slackness conditions**
>
> $\underline x^*\in X$ and $\underline y^*\in Y$ are optimal solutions of, respectively, $(P)$ and $(D)$, if and only if:
> $$\begin{aligned}
> y_i^*\overbrace{(\underline{a}_i^T\underline x^* - b_i)}^{s_i} &= 0, &i = 1, \ldots, m\\\
> \underbrace{(c_j^T-\underline{y^*}^TA_j)}_{s'_j}x_j^* &= 0, &j = 1, \ldots, n
> \end{aligned}$$
> Where:
> - $\underline a_i$ denotes the $i$-th row of $A$
> - $A_j$ denotes the $j$-th column of $A$
> - $s_i$ is the slack of the $i$-th constraint of $(P)$
> - $s'_j$ is the slack of the $j$-th constraint of $(D)$
> At optimality, the product of each variable with the corresponding slack variable of the constraint of the relative dual is zero.

## Sensitivity Analysis

Sensitivity analysis is the process used to evaluate the sensitivity of an optimal solution with regards to variations in the model parameters.

Let's start with an example about production planning:

$$\begin{matrix}
\max &\sum_{j=1}^n p_jx_j & \\\
\text{s.t.} &\sum_{j=1}^n a_{ij}x_j\le b_i &i = 1, \ldots, m\\\
&x_j\ge 0 &j = 1, \ldots, n
\end{matrix}$$

In the above problem:

- $p_j$ is the profit of one unit of the $j$-th product
- $b_i$ is the availability of the $i$-th resource

### Geometric interpretation

Let's try to understand the geometric interpretation of sensitivity analysis taking the following problem into account:

$$\begin{matrix}
\max &x_1 &+x_2 &\\\
\text{s.t.} &{x_1\over2} &+x_2 &\le 2\\\
&2x_1 &+x_2 &\le 4\\\
&x_1, &x_2, &\ge 0
\end{matrix}$$

We can graph this problem like so:

![](../images/Pasted%20image%2020231129143928.png)

We find that the optimal basic feasible solution is $\underline x^* = \big({4\over3}, {4\over3}\big)^T$, which corresponds to $z^* = {8\over3}$.

Now, if we multiply the variable $x_1$ by a coefficient $c_1$, we can see how the graph shifts with regards to the value of $c_1$:

$$\begin{matrix}
\max &\textcolor{red}{c_1}x_1 &+x_2 &\\\
\text{s.t.} &{x_1\over2} &+x_2 &\le 2\\\
&2x_1 &+x_2 &\le 4\\\
&x_1, &x_2, &\ge 0
\end{matrix}$$

When ${1\over2}\le c_1\le 2$, the graph looks like this:

![](../images/Pasted%20image%2020231129144256.png)

We can also try modifying the right side of the inequalities:

$$\begin{matrix}
\max &x_1 &+x_2 &&\\\
\text{s.t.} &{x_1\over2} &+x_2 &\le 2 &\textcolor{red}{+1}\\\
&2x_1 &+x_2 &\le 4&\\\
&x_1, &x_2, &\ge 0&
\end{matrix}$$

We obtain a different optimal solution and graph:

![](../images/Pasted%20image%2020231129144414.png)

We can define the **shadow price** of the $i$-th resource as the **maximum price** a company is willing to pay to buy **an additional unit** of the $i$-th resource.

In the example above, the shadow price of the first resource is:

$$z^* - x_2^* = {10\over3} - {8\over3} = {2\over3}$$

### Algebraic form

Sensitivity analysis can be performed algebraically as well.

Given the Linear Programming problem:

$$\begin{matrix}
\min &\underline c^T\underline x\\\
\text{s.t.} &A\underline x = \underline b\\\
&\underline x > \underline 0
\end{matrix}$$

and an optimal basic feasible solution $\underline x^*$ composed of:

$$\begin{aligned}
\underline x_B^* &= B^{-1}\underline b \ge \underline 0\\\
\underline x_N^* &= \underline 0
\end{aligned}$$

we want to understand which limits allow the basis $B$ to remain optimal.

We need to respect two conditions:

1. **Feasibility**:
   $$B^{-1}\underline b\ge \underline 0$$
2. **Optimality**:
   $$\underline{\overline{c}}_N^T = \underline c_N^T - \underline c_B^T B^{-1}N \ge \underline 0^T$$

Let's consider the variation of the right-hand side terms first. Let's suppose we have:

$$\underline b' \coloneqq \underline b + \delta_k\underline e_k, \ 1 \le k \le n$$

where $\underline e_k$ is the vector which has a single one in the $k$-th position.

In this case, the basis $B$ with the basic feasible solution:

$$\underline x^* = \begin{bmatrix}
B^{-1}(\underline b+\delta_k\underline e_k)\\\
\underline 0
\end{bmatrix}$$

remains optimal as long as:

$$B^{-1}(\underline b+\delta_k\underline e_k) \ge \underline0$$

which can be also written as:

$$B^{-1}\underline b \ge -\delta_k B^{-1} \underline e_k$$

These $m$ inequalities define an interval of variation for $\delta_k$.

Under these conditions, $B$ remains optimal, but the optimal basic feasible solution changes: the objective function value goes from $\underline c_B^T B^{-1}\underline b$ to $\underline c_B^T B^{-1}(\underline b + \delta_k\underline e_k)$, thus:

$$\Delta z^* = c_B^T B^{-1}(\delta_k\underline e_k)$$

Renaming $c_B^T B^{-1}$ to $\underline{y^*}^T$ (the optimal solution of the dual problem), we obtain the **shadow price** expression:

$$\Delta z^* = \delta_ky_k^*$$

Let's now see what happens if we change the cost coefficients.

Given $\underline c' \coloneqq \underline c + \delta_k\underline e_k$, a basis $B$ remains optimal as long as:

$${\underline{\overline{c}}'}_N^T = \underline{c'}_N^T - \underline{c'}_B^TB^{-1}N \ge \underline 0$$

In that case, the optimal basic feasible solution does not change:

$$\begin{aligned}
\underline x_B^* &= B^{-1}\underline b\\\
\underline x_N^* &= \underline 0
\end{aligned}$$

If $x_k$ is a non-basic variable, then the reduced cost of such variable is the maximum decrease of $c_k$ for which $B$ remains optimal. In that case, we don't see a variation in the optimal objective function value $z^*$.

If $x_k$ is a basic variable instead, we do see a difference in the optimal objective function value, equal to:

$$\Delta z^* = \delta_k x_k^*$$

[^1]: For maximisation problems, we check for $\underline{\overline{c}}_N \le \underline 0$.
