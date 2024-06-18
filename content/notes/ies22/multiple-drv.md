---
title: "Variabili aleatorie discrete multiple"
draft: false
type: 'page'
toc: true
mathjax: true
---

---

## Legge di probabilità congiunta

Una legge di probabilità congiunta è simile ad una probabilità che due eventi si verifichino contemporaneamente.

Ipotizziamo di avere due variabili aleatorie $X$ e $Y$ e due eventi $\{X=x\}$ e $\{Y=y\}$. La legge di probabilità congiunta di questi due eventi è:

$$P(\{X=x\}\cap\{Y=y\}) = p_{X,Y}(x,y)$$

Valgono sempre le stesse [proprietà](../axioms) elencate precedentemente.

### Leggi di probabilità marginali

È possibile, tramite l'operazione di **marginalizzazione**, trovare la legge di probabilità di una sola delle due variabili aleatorie a partire dalla legge di probabilità congiunta:

$$p_X(x) = \sum_{y\in\mathbb R} p_{X,Y}(x,y), \forall x\in\mathbb R$$

Chiaramente vale anche al contrario:

$$p_Y(y) = \sum_{x\in\mathbb R} p_{X,Y}(x,y), \forall y\in\mathbb R$$

> **Nota**
>
> In pratica, per marginalizzare, *fisso* una delle due realizzazioni delle variabili aleatorie e sommo per tutte le realizzazioni dell'altra.

---

## Leggi di probabilità condizionale

Anche per le variabili aleatorie valgono le regole viste per le [probabilità condizionate](../conditional-prob):

$$p_{X|Y}(x|y) = {p_{X,Y}(x,y)\over p_Y(y)}$$

Grazie alla [marginalizzazione](#leggi-di-probabilità-marginali), è possibile trasformare l'equazione sopra in:

$$p_{X|Y}(x|y) = {p_{X,Y}(x,y)\over \sum_{\overline x \in \mathbb R}p_{X,Y}(\overline x, y)}$$

### Regola moltiplicativa

Come già menzionato prima, anche per le variabili aleatorie valgono le regole delle [probabilità condizionate](../conditional-prob).

Vediamo ora nello specifico la [regola moltiplicativa](../conditional-prob#regola-moltiplicativa):

$$\begin{aligned}
p_{X,Y}(x,y) &= p_Y(y)\cdot p_{X|Y}(x|y)\\\
&= p_X(x)\cdot p_{Y|X}(y|x)
\end{aligned}$$

### Variabili aleatorie indipendenti

Anche l'[indipendenza](../independence) vale per le variabili aleatorie.

Possiamo dire che due variabili aleatorie $X,Y$ sono indipendenti se e solo se:

$$p_{X,Y}(x,y) = p_X(x)\cdot p_Y(y), \forall (x,y)\in\mathbb R^2$$

Come nel caso degli eventi, se due variabili aleatorie sono indipendenti, è possibile scrivere $X\perp Y$.

> **Nota**
>
> Questo vale anche oltre le due dimensioni:
> $$p_{X,Y,Z}(x,y,z) = p_X(x)\cdot p_Y(y)\cdot p_Z(z), \forall (x,y,z)\in\mathbb R^3$$

Vale esattamente allo stesso modo descritto per gli eventi l'[indipendenza condizionata](../independence#indipendenza-condizionata).

---

## Valore atteso per variabili aleatorie multiple

In generale, possiamo dire che:

$$E\big[g(X,Y)\big] = \sum_x\sum_y g(x,y)\cdot p_{X,Y}(x,y)$$

[Come già detto](../drv#proprietà-del-valore-atteso), non è possibile ragionare *in media*.

### Proprietà del valore atteso

#### Linearità

[Come già visto](../drv#proprietà-del-valore-atteso), l'operatore valore atteso è lineare. Questa proprietà ci permette di affermare che:

$$E\big[\alpha X + \beta Y + \gamma\big] = \alpha E[X] + \beta E[Y] + \gamma$$

Come si evince dall'equazione sopra, è **sufficiente** avere conoscenza delle leggi marginali di due variabili aleatorie $X$ e $Y$ per calcolarne il valore atteso congiunto.

#### Indipendenza

Possiamo dimostrare che se due variabili aleatorie sono indipendenti, allora il valore atteso del loro prodotto è pari al prodotto dei loro valori attesi:

$$X\perp Y \implies E[XY] = E[X]\cdot E[Y]$$ Possiamo dimostrare inoltre che **non vale** il contrario:

$$E[XY] = E[X]\cdot E[Y] \nRightarrow X\perp Y$$

Questa proprietà vale non solo per le variabili aleatorie in sé, ma anche per funzioni di variabili aleatorie:

$$g(X) \perp h(Y) \implies E\big[g(X)h(Y)\big] = E\big[g(X)\big]\cdot E\big[h(Y)\big]$$

---

## Varianza per variabili aleatorie multiple

Si può calcolare che, in generale:

$$\text{Var}[X+Y] = \text{Var}[X]+\text{Var}[Y]+2\big(E[XY] - E[X]E[Y]\big)$$

Inoltre, [per la proprietà del valore atteso trovata precedentemente](#indipendenza), se le due variabili aleatorie sono indipendenti, vale che:

$$\text{Var}[X+Y] = \text{Var}[X]+\text{Var}[Y]$$

---

## Valore atteso e varianza della variabile aleatoria binomiale: variabili aleatorie di Bernoulli

Ipotizziamo di avere una variabile aleatoria $X\sim\text{Bin}(n,p)$, che ha la seguente legge di probabilità:

$$p_X(k) = \begin{cases}
\binom{n}{k}p^k(1-p)^{n-k}, &k=0,1,2,\ldots,n\\\
0, &\text{altrimenti}
\end{cases}$$

Possiamo calcolarne il valore atteso in questo modo:

$$\begin{aligned}
E[X] &= \sum_{k=0}^n k\cdot p_X(x)\\\
&= \sum_{k=0}^n k\cdot\binom{n}{k}\cdot p^k\cdot(1-p)^{n-k}
\end{aligned}$$

Consideriamo ora la variabile aleatoria $X_i$ definita in questo modo:

$$X_i = \begin{cases}
0, &\text{insuccesso nella prova }i\text{-esima}\\\
1, &\text{successo nella prova }i\text{-esima}
\end{cases},\ \ \  i = 1,2,\ldots,n$$

> **Nota**
>
> Tutte le variabili aleatorie $X_i$ sono indipendenti.

Possiamo calcolare allora la variabile aleatoria $X$ come **somma** di tutte le variabili aleatorie $X_i$:

$$X = \sum_{i=1}^n X_i$$

Conoscendo questa informazione, proviamo a calcolare il valore atteso della variabile aleatoria $X$:

$$\begin{aligned}
E[X] &= E\bigg[\sum_{i=1}^n X_i \bigg]\\\
&= \sum_{i=1}^n E[X_i]\\\
&= \sum_{i=1}^n \big(0\cdot (1-p)+1\cdot p\big)\\\
&= n\cdot p
\end{aligned}$$

Incidentalmente, ora conosciamo il valore a cui converge una probabilità binomiale:

$$\sum_{k=0}^n k\cdot\binom{n}{k}p^k(1-p^k) = np, \ \  n\in\mathbb N,\  0\le p\le 1$$

Calcoliamo allo stesso modo la varianza di $X$:

$$\begin{aligned}
\text{Var}[X] &= \text{Var}\bigg[\sum_{i=1}^n X_i\bigg]\\\
&= \sum_{i=1}^n \text{Var}[X_i]\\\
&= \sum_{i=1}^n E[X_i^2] - \big(E[X_i]\big)^2\\\
&= \sum_{i=1}^n p-p^2\\\
&= np(1-p)
\end{aligned}$$

> **Nota**
>
> Dato che $X_i$ può avere solo valore 0 o 1, possiamo dire:
> $$E[X_i^2]=E[X_i]=p$$

Anche in questo caso, abbiamo scoperto il valore di convergenza di una sommatoria:

$$\sum_{k=0}^n (k-np)^2\cdot\binom{n}{k}\cdot p^k \cdot (1-p)^{n-k} = np(1-p), \ \  \forall n\in\mathbb N, \  0\le p \le 1$$

Possiamo definire la variabile aleatoria $X_i$ **variabile aleatoria di Bernoulli**:

$$X_i\sim\text{Bern}(p)$$

Una variabile aleatoria di Bernoulli ha, come abbiamo visto, valore atteso pari a:

$$E[X_i] = p = p_X(1)$$

E varianza pari a:

$$\text{Var}[X_i] = p(1-p)$$

Si dice che le variabili aleatorie $X_i, i = 1,2,\ldots,n$ sono **indipendenti ed identicamente distribuite**, o *i.i.d.*, cioè:

$$p_{X_i}(x) = p_{X_{i+1}}(x), \forall x\in\mathbb R, \forall i = 1,2,\ldots,n-1$$

Inoltre, da questo deriva che $E[X_i]$ e $\text{Var}[X_i]$ sono uguali per ogni $i$.
