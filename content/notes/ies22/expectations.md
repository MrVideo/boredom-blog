---
title: 'Valori attesi condizionati'
draft: false
type: 'page'
toc: true
mathjax: true
---

---

## Valore atteso come variabile aleatoria

[Come per le probabilità](../conditional-prob) e [per le variabili aleatorie](../drv#leggi-condizionate-e-valore-atteso-condizionato), è possibile condizionare il valore atteso:

$$E[X|Y=y] = \sum_x x\cdot p_{X|Y}(x|y)$$

In questo caso, sappiamo che il risultato dell'espressione sopra è un numero puro.

Ipotizziamo ora di non aver mai osservato una realizzazione della variabile aleatoria $Y$. In generale allora possiamo dire:

$$E[X|Y] = {Y\over2}$$

Questa espressione non è più rappresentata da un numero, bensì da una **variabile aleatoria** con densità di probabilità $f_Y$.

Dato che $E[X|Y]$ è una variabile aleatoria, posso provare a calcolarne il valore atteso:

$$\begin{aligned}
E\big[E[X|Y]\big] &= E\big[g(Y) \big]\\\
&= \int_{-\infty}^\infty g(y)\cdot f_Y(y)dy\\\
&= \int_{-\infty}^\infty E[X|Y=y] \cdot f_Y(y)dy &(1)\\\
&= E[X]
\end{aligned}$$

Applicando in $(1)$ la [legge dell'aspettativa totale](../drv#legge-dellaspettativa-totale), otteniamo la **legge delle aspettazioni iterate**, che afferma:

$$E[X] = E\big[E[X|Y]\big]$$

---

## Varianza condizionata

Possiamo applicare un ragionamento analogo a quello usato precedentemente alla varianza ed ottenere così la **legge della variazione totale**:

$$\text{Var}[X] = E\big[{\text{Var}[X|Y]}\big] + \text{Var}\big[{E[X|Y]}\big]$$

---

## Somma di un numero casuale di variabili aleatorie

Per spiegare questo fenomeno, utilizziamo un esempio: ipotizziamo di visitare $N$ siti con $N>0$. $N$ è una variabile aleatoria discreta.

Aggiungiamo una nuova variabile aleatoria $X_i$, che rappresenta la spesa totale sul sito $i$-esimo.

Assumiamo che le spese siano tutte indipendenti ed identicamente distribuite:

$$X_i \text{ i.i.d.}$$

Possiamo allora definire una variabile aleatoria $X$ che rappresenta la spesa totale come:

$$X = \sum_{i=1}^n X_i$$

Calcoliamo il valore atteso di $X$:

$$\begin{aligned}
E[X] &= E\bigg[\sum_{i=1}^N X_i\bigg]\\\
\text{(Aspettazioni iterate)}&= E\bigg[E\bigg[ \sum_{i=1}^n X_i\bigg|N\bigg] \bigg]\\\
E\bigg[\sum_{i=1}^n X_i\bigg|N=n\bigg] &= \sum_{i=1}^n E[X_i|N=n]\\\
(X_i \perp N \ \forall i) &= \sum_{i=1}^n E[X_i]\\\
(X_i\text{ i.i.d.}) &= nE[X_1]
\end{aligned}$$

Arrivati a questo punto, è possibile costruire la variabile aleatoria:

$$E[X|N] = NE[X_1]$$

Possiamo ora calcolare $E[X]$:

$$\begin{aligned}
E[X] &= E\big[E[X|N]\big]\\\
&= E\big[N\cdot E[X_1]\big]\\\
&= E[N]\cdot E[X_1]
\end{aligned}$$

Applicando lo stesso ragionamento alla varianza di $X$, troviamo:

$$\text{Var}[X] = E[X_1]^2\cdot\text{Var}[N] + \text{Var}[X_1]\cdot E[N]$$

Dove:

- $E[X_1]^2\cdot\text{Var}[N]$ rappresenta la variabilità sul numero di siti visitati
- $\text{Var}[X_1]\cdot E[N]$ rappresenta la varianza delle spese sui diversi siti
