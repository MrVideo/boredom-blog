---
title: 'Calcolo combinatorio'
draft: false
type: 'page'
toc: true
mathjax: true
---

---

## Principi di calcolo combinatorio

Generalmente, per semplificare i problemi di calcolo combinatorio, è utile spezzare un dato problema in *stadi* di scelta.

Supponiamo di avere $r$ stadi ed $n_i$ scelte nello stadio $i$-esimo; in questo caso, avremmo in totale $n_1\cdot n_2\cdot \ldots\cdot n_r$ scelte.

> **Esempio: targhe automobilistiche**
>
> Un numero di targa è composto da 7 caratteri, perciò per calcolare il numero totale di targhe si può scomporre il problema di scelta in $r=7$ stadi.
> Considerando che esistono 26 lettere dell'alfabeto e 10 cifre nel sistema decimale, abbiamo che il numero totale di targhe è $26^4\cdot10^3$.
> Se volessimo invece calcolare quante targhe fosse possibile realizzare impedendo la ripetizione dei simboli, avremmo $26\cdot25\cdot24\cdot23\cdot10\cdot9\cdot8$.

## Permutazioni

> **In quanti modi è possibile ordinare $n$ elementi distinti?**
>
Se ipotizziamo di avere un insieme di 4 elementi distinti (e di conseguenza $r=4$ stadi) possiamo calcolare il numero di scelte totali come $4\cdot3\cdot2\cdot1$.

Generalizzando, perciò, con $n$ elementi distinti, è possibile trovare $n!$ permutazioni di quegli elementi.

Se avessimo un insieme di elementi non completamente distinti (ad esempio $\{A, A, B, C\}$) sarebbe possibile considerare gli elementi indistinguibili tra loro come un unico elemento se fissassimo le loro posizioni. In questo caso, dati $n$ elementi totali nell'insieme ed $m$ elementi indistinguibili, è possibile trovare $(n-m+1)!$ permutazioni di questi elementi.

In generale, invece, se non fissassimo le posizioni degli elementi indistinguibili, otterremmo $n!/m!$ permutazioni.

## Conteggio dei sottoinsiemi

> Quanti sottoinsiemi si possono formare dagli elementi di un insieme di cardinalità $n$?

Per ogni elemento dell'insieme, è possibile scegliere se metterlo in un sottoinsieme o meno. Procedendo in questo modo, si esauriscono tutte le scelte possibili, perciò si riesce a costruire tutti i sottoinsiemi possibili, che è $2^n$.

## Combinazioni

> Calcolare il numero di sottoinsiemi con $k$ elementi partendo da un insieme di $n$ elementi distinti.

![](../images/Pasted%20image%2020230728170724.png)

Il numero di sottoinsiemi di $k$ elementi che è possibile creare a partire da un insieme di cardinalità $n$ è pari a:

$$\frac{n!}{k!(n-k)!} = \binom{n}{k}$$

## Probabilità binomiali

Ipotizziamo di avere un esperimento composto da $N$ lanci di moneta indipendenti, in cui la probabilità che esca testa sia pari a $P(T) = p$.

La probabilità che esca esattamente la sequenza di risultati `TCCTTT` è allora pari a:

$$\begin{aligned}
P(TCCTTT) &= P(T)P(C)P(C)P(T)P(T)P(T)\\\\
&= p^4\cdot(1-p)^2\\\\
&= P(\text{Qualunque sequenza di quattro Teste e due Croci})
\end{aligned}$$

Possiamo generalizzare e dire che, per ogni sequenza specifica di teste e croci:

$$P(\text{Sequenza}) = p^\text{Numero teste}\cdot(1-p)^\text{Numero croci}$$

Confermato questo, possiamo provare a calcolare la probabilità di ottenere esattamente $k$ teste in $n$ lanci totali:

$$\begin{aligned}
P(k \text{ teste in } n \text{ lanci}) &= P\bigg(\bigcup \text{ sequenze con } k \text{ teste in } n \text{ lanci}\bigg)\\\\
&= \sum_{\text{sequenze con } k \text{ teste}} P(\text{sequenza particolare})\\\\
&=p^k\cdot(1-p)^{n-k}\cdot\sum_{\text{sequenze con } k \text{ teste}}1\\\\
&=\binom{n}{k}\cdot p^k\cdot(1-p)^{n-k}
\end{aligned}$$

L'espressione trovata rappresenta il caso generale di una cosiddetta **probabilità binomiale**:

> **Schema generale di una probabilità binomiale**
>
> > Date $n$ prove indipendenti ed una probabilità di successo di una singola prova pari a $p$, qual è la probabilità di avere $k$ successi su $n$ prove?

## Partizioni

### Estrazioni con reinserimento

Ipotizziamo di avere un sacchetto con 4 tipi di biglie.

La probabilità di avere $k_i$ estrazioni di tipo $i$, per $i=1,2,3,4$ su $n$ biglie totali è pari a:

$$\binom{n}{k_1, k_2, k_3, k_4}$$

Questo fattore si chiama **coefficiente multinomiale** ed è una generalizzazione del coefficiente binomiale.

### Probabilità ipergeometriche

Consideriamo il gioco del Superenalotto.

La probabilità di ottenere $k$ numeri vincenti sui sei totali è pari a:

$${\binom{6}{k}\binom{84}{6-k}\over\binom{90}{6}}$$

Questo tipo di probabilità è detta **ipergeometrica**.
