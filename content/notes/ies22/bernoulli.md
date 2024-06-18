---
title: 'Processi di Bernoulli'
draft: false
type: 'page'
toc: true
mathjax: true
---

---

## Definizione

Si dice processo aleatorio un insieme di variabili aleatorie.

Ad esempio, un insieme di lanci di moneta è un processo aleatorio.

Si dice **processo di Bernoulli** una sequenza di prove di Bernoulli indipendenti $X_i$ identicamente distribuite.

Un processo di Bernoulli viene indicato con la dicitura $BP$ ed è caratterizzato dal solo parametro $p$, che è la probabilità di un successo:

$$BP(p)$$

## Numero di successi $S$ in $n$ istanti temporali

Il numero di successi di un processo di Bernoulli è rappresentabile come una variabile aleatoria binomiale:

$$S_n \sim \text{Bin}(n,p)$$

La probabilità di avere $k$ successi in un processo di Bernoulli è quindi:

$$P(S_n=k) = \binom{n}{k} p^k(1-p)^{n-k}, \ 0 \le k \le n$$

## Tempi di interarrivo

Se consideriamo un processo di Bernoulli, possiamo definire una variabile aleatoria $T_1$ come il numero di prove fino al primo successo riscontrato. Questa variabile aleatoria è perciò geometrica:

$$T_1 \sim \text{Geom}(p)$$

La probabilità che il tempo al primo successo sia pari a $t$ allora è pari a:

$$P(T_1=t) = \begin{cases}
(1-p)^{t-1}\cdot p, &t\ge1\\\
0, &\text{altrimenti}
\end{cases}$$

Inoltre, essendo $T_1$ geometrica, gode della proprietà di perdita di memoria.

## Tempo al $k$-esimo arrivo

Ipotizziamo di voler trovare il numero di prove per arrivare al $k$-esimo successo. Possiamo applicare i tempi di interarrivo sommandoli:

$$Y_k = T_1+T_2+\ldots+T_k$$

Le variabili aleatorie $T_i$ in questo caso sono tutte indipendenti ed identicamente distribuite.

Possiamo calcolare la probabilità che il tempo al $k$-esimo arrivo sia pari a $t$ in questo modo:

$$P(Y_k=t) = \begin{cases}
\binom{t-1}{k-1}p^{k}(1-p)^{t-k}, &t\ge k\\\
0, &\text{altrimenti}
\end{cases}$$

Questa variabile aleatoria è una **variabile aleatoria di Pascal** e si scrive:

$$Y_k\sim\text{Pascal}(t,p)$$

Vediamo anche il valore atteso e la varianza di questa variabile aleatoria:

$$\begin{aligned}
E[Y_k] &= {k\over p}\\\
\text{Var}[Y_k] &= k{1-p\over p^2}
\end{aligned}$$

## Splitting di un processo di Bernoulli

Possiamo eseguire un'operazione di *splitting* su un processo di Bernoulli, che consiste nel dividere quest'ultimo in altri processi che, insieme, sono equivalenti a quello di partenza.

È dimostrabile che lo splitting di un processo di Bernoulli porta ad avere altri processi di Bernoulli.

## Merging di un processo di Bernoulli

Il contrario dell'operazione di splitting è l'operazione di *merging*, in cui più processi di Bernoulli vengono uniti insieme per formarne un altro.

Anche in questo caso, è dimostrabile che i processi ottenuti tramite merging di processi di Bernoulli sono a loro volta processi di Bernoulli.
