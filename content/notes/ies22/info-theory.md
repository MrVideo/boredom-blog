---
title: "Teoria dell'informazione"
draft: false
type: 'page'
toc: true
mathjax: true
---

---
# Teoria dell'informazione

---

## Definizione di informazione

Prima di effettuare un esperimento aleatorio, c'è indecisione sul risultato dell'esperimento stesso. Questa indecisione viene descritta dalle probabilità.

Dopo l'esperimento, sappiamo se un evento è accaduto. Se $A$ è un evento molto probabile, non ne rimaniamo sorpresi; se $A$ è invece un evento raro, ne rimaniamo sorpresi.

Vogliamo misurare il livello di sorpresa portato dall'accadere dell'evento $A$:

$$i(A) \triangleq \log\bigg({1\over P(A)}\bigg)$$

Definendo così l'**informazione** portata dall'evento, possiamo dire che:

- Se $P(A)\to1$, allora $i(A)\to0$
- Se $P(A)\to0$, allora $i(A)\to\infty$

Se la base del logaritmo con cui viene misurata l'informazione è naturale, allora l'unità di misura dell'informazione è $[\text{nat}]$. Se invece la base del logaritmo è 2, allora si misura in bit. Se, ancora, la base è 10, si misura in Hantley.

> **Informazione come logaritmo**
>
> L'informazione è definita come logaritmo perché ciò ci permette di misurare con facilità l'informazione portata da due eventi indipendenti:
> $$\begin{aligned}
> i(A\cap B) &= \log{1\over P(A\cap B)}\\\
> &= \log{1\over P(A)\cdot P(B)}\\\
> &= \log{1\over P(A)} + \log{1\over P(B)}\\\
> &= i(A) + i(B)
> \end{aligned}$$

## Contenuto informativo di una variabile aleatoria discreta

Un esperimento aleatorio discreto il cui risultato è descritto da una variabile aleatoria discreta associa ad ogni evento elementare una probabilità e, di conseguenza, un'auto-informazione.

L'informazione media (o *entropia*) della variabile aleatoria $X$ è definita come:

$$H(X) \triangleq E[i(X)] = \sum_{j=1}^n p_X(x_j)\log{1\over p_X(x_j)}$$

> **Interpretazione**
>
> $H(X)$ è il numero medio di bit di informazione che mi aspetto di ottenere dopo aver effettuato un esperimento aleatorio.

> **Alcune proprietà**
>
> - Le variabili aleatorie costanti non portano informazione, quindi $H(a) = 0,\ a=\text{cost}$
> - Non esistono variabili aleatorie discrete con entropia negativa

> Esiste un valore massimo di entropia a parità di numero di eventi elementari?

La variabile aleatoria uniforme $U\{x_1,x_2,\ldots,x_m\}$ è quella con il massimo valore di entropia:

$$H(U\{x_1,x_2,\ldots,x_m\}) = \log m$$

Quindi l'entropia di una qualunque variabile aleatoria $X$ è pari a:

$$0 \le H(X) \le \log m$$

## Disuguaglianza di Jensen

Questo è dimostrabile tramite la **disuguaglianza di Jensen**:

> **Disuguaglianza di Jensen**
>
> Siano $\lambda_1,\ldots,\lambda_m$ dei coefficienti tali che $\lambda_i\ge 0,\ \forall i$ e:
> $$\sum_{i=0}^m \lambda_i = 1$$
> Allora vale che:
> $$\sum_{j=1}^m \lambda_j\log x_j \le \log\bigg(\sum_{i=1}^m \lambda_ix_i\bigg)$$

> In pratica, facendo una media pesata dei logaritmi degli $x_i$, questa media viene maggiorata dal logaritmo della media pesata degli $x_i$.

In generale, la disuguaglianza di Jensen vale per qualunque funzione $f$ concava:

$$\begin{aligned}
E[f(Y)] &\le f(E[Y]), \forall f \text{ concava}\\\
E[f(Y)] &\ge f(E[Y]), \forall f \text{ convessa}\\\
\end{aligned}$$

## Binary Entropy Function

Prendendo l'esempio del lancio di una moneta in cui $P(T) = p$, definiamo l'informazione fornitaci dal verificarsi di una testa e di una croce:

$$\begin{aligned}
i(T) &= \log{1\over p}\\\
i(C) &= \log{1\over 1-p}
\end{aligned}$$

Possiamo allora calcolarne l'entropia come visto precedentemente:

$$\begin{aligned}
H(X) &= E[i(X)]\\\
&= p\cdot\log{1\over p} + (1-p)\cdot\log{1\over 1-p}
\end{aligned}$$

Volendo ottenere un risultato in bit, riscriviamo utilizzando il logaritmo in base due:

$$H(X) = p\cdot\log_2{1\over p} + (1-p)\cdot\log_2{1\over 1-p}$$

Possiamo denominare questa funzione **Binary Entropy Function** e riscriverla così:

$$H_2(p) = p\cdot\log_2{1\over p} + (1-p)\cdot\log_2{1\over 1-p}$$

Questa funzione ha il seguente aspetto:

![](../images/Pasted%20image%2020230831175145.png)
