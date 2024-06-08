---
title: 'Strength of logical conditions'
draft: false
type: 'page'
toc: true
mathjax: true
---

---

A logical expression is considered **stronger** when it is more restrictive, hence it is true in *fewer cases*; a logical expression is instead considered **weaker** when it's less restrictive and so true in *more cases*.

## Formal definition in mathematical logic

The strength of a condition is formalized in mathematical logic through the implication operator:

>Given two logical expressions $\alpha$ and $\beta$, it is said that $\alpha$ is stronger than $\beta$ if $\alpha\implies\beta$.

## Logical operators and strength of conditions

Forming more complex logical expressions by joining two or more simpler ones either strengthens or weakens the final expression, depending on what logical operator was used to unite the expressions:

- The disjunction $\lor$ weakens the final expression
- The conjunction $\land$ strengthens the final expression
- The implication $\implies$ weakens the final expression
- The expression $\alpha\implies\beta$ is weakened when $\alpha$ is strengthened

## In JML

This principle can be applied in JML through the following rules.

### Weaker precondition rule

If the precondition of a redefined method is weaker than the one of the original method, then the redefined method can be used in *more cases*.

This is always verified in JML.

If the precondition were to be stronger, then the *more specific* method in the subclass would apply to *less cases* than the general method defined in the superclass.

### Stronger postcondition rule

If the postcondition of a redefined method is stronger than the postcondition of the original method, then the postcondition of the superclass's method will always be verified. This can be summed up like so:

$$\text{post}_\text{sub} \implies \text{post}_\text{super}$$

This is always verified in JML.

If the opposite were to happen, then once the subclass's method returned, there would be no telling whether the superclass's method postcondition would also be fulfilled.
