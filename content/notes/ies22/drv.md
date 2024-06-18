---
title: 'Variabili aleatorie discrete'
draft: false
type: 'page'
toc: true
mathjax: true
---

---

## Definizione

> **Variabile aleatoria**
>
> Una variabile aleatoria è una funzione definita come:
> $$H:\Omega\to\mathbb R$$

> **Nota**
>
> Una funzione deterministica di una variabile aleatoria è a sua volta una variabile aleatoria.

Per indicare una variabile aleatoria si usano generalmente le lettere maiuscole, mentre per indicare il *valore* assunto da una variabile aleatoria, detto **realizzazione**, si usano lettere minuscole.

## Legge di probabilità

Una legge di probabilità serve per passare da una notazione *a eventi* come quelle utilizzate finora ad una notazione con variabili aleatorie e rispettive realizzazioni.

In generale, dato un evento $\{X=x\}$, abbiamo che:

$$\begin{aligned}
P(X=x) &= P\big(\{\omega\in\Omega:X(\omega)=x\}\big)\\\
&= p_X(x), \forall x\in\mathbb R
\end{aligned}$$

dove $p_X$ è la **legge di probabilità** di $X$, detta anche *probability law* o *probability mass function*.

Valgono ancora gli [assiomi](../axioms) elencati precedentemente. Infatti:

1. $p_X(x)\ge0, \forall x\in\mathbb R$
2. $\sum_{x\in\mathbb R}p_X(x) = 1$

### Legge di probabilità geometrica

> **Esperimento**
>
> Lancio di una moneta fino all'ottenimento della prima testa

Creiamo una variabile aleatoria $X$ pari al numero di lanci necessari ad ottenere la prima testa. Possiamo allora formulare una legge di probabilità di questo tipo:

$$\begin{aligned}
P(X=k) &= p_X(k)\\\
&= P(\underbrace{CC\ldots C}_{k-1}T)\\\
&= \begin{cases}
(1-p)^{k-1}p, &k=1, 2, 3, \ldots\\\
0, &\text{altrimenti}
\end{cases}\\\
&=(1-p)^{k-1}p\cdot\mathbb 1\{k\in\mathbb N\}
\end{aligned}$$

Questa legge di probabilità è detta **geometrica** e risponde a domande del tipo:

> Facendo diversi esperimenti indipendenti, qual è la probabilità di ottenere il primo successo al $k$-esimo tentativo?

### Legge di probabilità binomiale

Esiste anche una legge di probabilità *binomiale*, che può rispondere ad una domanda del tipo:

> Quante volte uscirà testa su quattro lanci indipendenti di una moneta?

Ipotizzando che la probabilità di avere una testa come risultato sia $p$, troviamo:

$$p_X(k) = \begin{cases}
\binom{n}{k}p^k(1-p)^{n-k}, &k=0,1,2,\ldots,n\\\
0, &\text{altrimenti}
\end{cases}$$

---

## Valore atteso

> **Valore atteso**
>
> Il valore atteso di una variabile aleatoria è una media pesata delle sue realizzazioni, dove i pesi sono le probabilità di tali realizzazioni:
> $$E[X] = \sum_{x\in\mathbb R}x\cdot p_X(x)$$

> **Nota**
>
> Può anche essere interpretato come il baricentro della legge di probabilità.

### Proprietà del valore atteso

1. Se $X$ è una variabile aleatoria, allora $Y=g(X)$ è a sua volta una variabile aleatoria

> **Legge dello statistico inconsapevole**
>
> $$E[Y]=E[g(X)]$$

> **Attenzione**
>
> In generale, vale che:
> $$E[g(X)] \ne g(E[X])$$

2. $E[\beta] = \beta, \beta\in\mathbb R$
3. $E[\alpha Y] = \alpha E[Y], \alpha\in\mathbb R$
4. L'operatore valore atteso è lineare, perciò se abbiamo $E[g(X)]$ e $g$ è una funzione lineare, è possibile scambiare le posizioni delle due. ---

## Varianza

La varianza è utile per calcolare l'informazione della dispersione della legge di probabilità attorno al suo baricentro. Si può calcolare come:

$$\text{Var}[X] = E\big[(X-E[X])^2\big] = E[X^2]-E[X]^2$$

### Proprietà della varianza

1. $\text{Var}[X]\ge0$ per tutte le variabili aleatorie
2. $\text{Var}[\alpha] = 0, \alpha\in\mathbb R$
3. $\text{Var}[\alpha X] = \alpha^2\text{Var}[X], \alpha\in\mathbb R$

### Scarto quadratico medio (o deviazione standard)

È definito come la radice quadrata della varianza di una variabile aleatoria:

$$\sigma_X = \sqrt{\text{Var}[X]}$$

---

## Leggi condizionate e valore atteso condizionato

Anche nel caso delle variabili aleatorie è possibile avere [probabilità condizionate](../conditional-prob):

$$P\big(\{X = x\}|\{Y = y\}\big) = p_{X|Y}(x|y)$$

È anche possibile calcolare il valore atteso di una variabile aleatoria condizionata ad un'altra in questo modo:

$$E[X|Y] = \sum_{x\in\mathbb R}xp_{X|Y}(x)$$

> **Proprietà di perdita di memoria**
>
> Tramite il calcolo del valore atteso di una variabile aleatoria geometrica condizionata ad un altra, possiamo notare che:
> $$p_{X-t|X>t}(k) = p_X(k), \forall k,t\in\mathbb N$$

---

## Legge dell'aspettativa totale

Ipotizziamo di avere tre partizioni $A_1, A_2, A_3$ di uno spazio campionario $\Omega$. Supponiamo inoltre di avere un insieme $B$ che include una parte di ciascuna delle partizioni.

Per la legge delle probabilità totali:

$$P(B) = P(A_1)P(B|A_1) + P(A_2)P(B|A_2) + P(A_3)P(B|A_3)$$

Se consideriamo l'evento $B$ pari ad una variabile aleatoria $X$ in questo modo:

$$B = \{X=x\}$$

Allora possiamo dire che:

$$p_X(x) = P(A_1)p_{X|A_1}(x) + P(A_2)p_{X|A_2}(x) + P(A_3)p_{X|A_3}(x)$$

Moltiplicando ogni termine per la realizzazione $x$ della variabile aleatoria $X$ e sommando:

$$\underbrace{\sum_{x\in\mathbb R}xp_X(x)}_{E[X]} = \sum_{x\in\mathbb R}P(A_1)xp_{X|A_1}(x) + \sum_{x\in\mathbb R}P(A_2)xp_{X|A_2}(x) + \sum_{x\in\mathbb R}P(A_3)xp_{X|A_3}(x)$$

Generalizzando:

$$E[X] = \sum_{i=1}^n P(A_i)E[X|A_i], A_i \text{ partizioni di } \Omega$$
