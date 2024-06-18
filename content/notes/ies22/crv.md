---
title: 'Variabili aleatorie continue'
draft: false
type: 'page'
toc: true
mathjax: true
---

---

## Definizione

Una variabile aleatoria continua si ottiene se si mappa il contenuto di un insieme su un intervallo di valori reali:

![](../images/Pasted%20image%2020230801162108.png)

Possiamo scrivere:

$$P(a\le X\le b) = P(A) = \int_a^b f_X(x)dx$$

Vediamo ora una definizione formale di variabile aleatoria continua:

> **Variabile aleatoria continua**
>
> $X$ è una variabile aleatoria continua, $X:\Omega\to\mathbb R$, se le probabilità possono essere calcolate come integrali definiti di una funzione $f_X$ detta *densità di probabilità* (o *Probability Density Function*).

## Proprietà

Similmente a quanto visto negli [assiomi della probabilità](../axioms), per le variabili aleatorie continue valgono le seguenti proprietà:

1. $f_X(x) \ge 0, \forall x\in\mathbb R$
2. $P(\Omega) = \int_{-\infty}^\infty f_X(x)dx = 1$
3. $P(X\in A\cup B) = P(X\in A)+P(X\in B) = \int_A f_X(x)dx + \int_B f_X(x)dx, \text{ se } A\cap B=\emptyset$

## Valore atteso e varianza

Anche nel caso delle variabili aleatorie continue, il valore atteso può essere interpretato come il *baricentro* della densità di probabilità e quindi calcolato così:

$$E[X] = \int_{-\infty}^{\infty} x\cdot f_X(x)dx$$

Anche nel caso continuo, vale la [legge dello statistico inconsapevole](../drv#proprietà-del-valore-atteso):

$$E\big[g(X)\big] = \int_{-\infty}^\infty g(x)f_X(x)dx$$

La varianza è identica al caso discreto:

$$\begin{aligned}
\text{Var}[X] &= E\big[g(X)\big]\\\
&= E\big[(X-E[X])^2\big]\\\
&= \int_{-\infty}^\infty \big(x-E[X]\big)^2 f_X(x)dx\\\
&= E[X^2]-E[X]^2
\end{aligned}$$

## Variabile aleatoria uniforme continua

Consideriamo una variabile aleatoria uniforme in uno spazio campionario continuo:

$$X\sim U[a,b]$$

La sua legge di probabilità sarà:

$$f_X(x) = \begin{cases}
{1\over b-a}, &a<x<b\\\
0, &\text{altrimenti}
\end{cases}$$

Calcoliamo il suo valore atteso:

$$\begin{aligned}
E[X] &= \int_{-\infty}^\infty xf_X(x)dx\\\
&= \int_a^b x \cdot {1 \over b-a} dx\\\
&= {a+b\over2}
\end{aligned}$$

Vediamo anche la sua varianza e la sua deviazione standard:

$$\begin{aligned}
\text{Var}[X] &= \int_{-\infty}^\infty \bigg(x - {a+b\over2}\bigg)^2 f_X(x)dx \\\
&= \int_a^b \bigg(x-{a+b\over2}\bigg)^2{1\over b-a}dx \\\
&= {(b-a)^2\over12}\\\
\\\
\sigma_X &= \sqrt{\text{Var}[X]}\\\
&= {b-a\over\sqrt{12}}
\end{aligned}$$

---

## Funzione cumulativa di probabilità

Una funzione cumulativa di probabilità, o *Cumulative Distribution Function*, è una **funzione integrale** che specifica la *distribuzione di una variabile aleatoria prima o dopo un certo punto*:

$$\begin{aligned}
P(X\le x) &= F_X(x)\\\
&= \int_{-\infty}^x f_X(t)dt
\end{aligned}$$

### Proprietà

Vediamo alcune proprietà della funzione cumulativa di probabilità:

- $0\le F_X(x)\le 1, \forall x\in\mathbb R$
- $F_X(x)$ è **non decrescente** $\forall x\in\mathbb R$
- $F_X$ è la **funzione integrale** di $f_X$, cioè vale:$${d\over dx}F_X(x) = f_X(x)$$

---

## Variabile aleatoria Gaussiana

Una variabile aleatoria Gaussiana è rappresentata in questo modo:

$$X\sim N\big(E[X], \text{Var}[X]\big)$$

La legge di probabilità di una variabile aleatoria Gaussiana ha forma:

$$f_X(x) = {1\over\sqrt{2\pi\sigma^2}}e^{-{(x-\mu)^2\over 2\sigma^2}}, x\in\mathbb R$$

Chiamiamo *Gaussiana standard* la variabile aleatoria $X\sim N(0,1)$, rappresentata su un grafico così:

![](../images/desmos-graph.png)
