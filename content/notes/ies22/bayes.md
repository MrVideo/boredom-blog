---
title: 'Regola di Bayes e funzioni di variabili aleatorie'
draft: false
type: 'page'
toc: true
mathjax: true
---

---

## Regola di Bayes per le variabili aleatorie

Finora, abbiamo visto la [regola di Bayes](../conditional-prob#regola-di-bayes-e-inferenza) soltanto nel caso in cui consideriamo insiemi ed eventi. Possiamo però applicarla anche alle variabili aleatorie:

> **Regola di Bayes per variabili aleatorie discrete**
>
> $$p_{X|Y}(x|y) = {p_{Y|X}(y|x)\cdot p_X(x)\over p_Y(y)}$$

> **Regola di Bayes per variabili aleatorie continue**
>
> $$f_{X|Y}(x|y) = {f_{Y|X}(y|x)\cdot f_X(x)\over f_Y(y)}$$

Un fatto interessante della regola di Bayes è che si può applicare anche a variabili aleatorie **eterogenee**, ossia mescolando variabili casuali discrete e continue.

Ipotizziamo di avere due variabili aleatorie, $X$ discreta ed $Y$ continua. Possiamo calcolare la legge di probabilità condizionata $p_{X|Y}$ in questo modo:

$$p_{X|Y}(x|y) = {f_{Y|X}(y|x)\cdot p_X(x)\over f_Y(y)}$$

Chiaramente questo vale anche invertendo le due variabili, ossia rendendo $X$ continua ed $Y$ discreta:

$$f_{X|Y}(x|y) = {p_{Y|X}(y|x)\cdot f_X(x)\over p_Y(y)}$$

---

## Calcolo di una funzione di variabile aleatoria

> È possibile ricavare la legge di probabilità, continua o discreta, di una funzione di una o più variabili aleatorie con legge di probabilità nota?

Vediamo un esempio: prendiamo uno spazio di probabilità uniforme continuo:

$$f_{X,Y}(x,y) = \begin{cases}
1, &(x,y)\in\Omega\\\
0, &\text{altrimenti}
\end{cases}, \> \Omega=\{0\le x\le 1, 0\le y\le 1\}$$

Prendiamo poi una funzione $g$ definita in questo modo:

$$g(x,y) = {y\over x}$$

Sostituiamo le realizzazioni nella funzione con le rispettive variabili aleatorie:

$$g(X,Y) = {Y\over X}$$

Possiamo allora definire una nuova variabile aleatoria $Z$ a partire da questa funzione:

$$Z = g(X,Y) = {Y\over X}$$

Cerchiamo ora di determinare $f_Z(z)$. Per farlo, utilizziamo il valore atteso:

$$\begin{aligned}
E[Z] &= E\bigg[{Y\over X}\bigg]\\\
&= \iint_{-\infty}^\infty {y\over x}\cdot f_{X,Y}(x,y)dxdy
\end{aligned}$$

Grazie alla [legge dello statistico inconsapevole](../drv#proprietà-del-valore-atteso), possiamo evitare di calcolare esplicitamente $f_Z(z)$.

### Variabile aleatoria discreta

Ipotizziamo di avere una variabile casuale discreta $X$ ed un'altra variabile aleatoria $Y=g(X)$, dove $g$ è una funzione deterministica nota. Possiamo risalire alla legge di probabilità di $X$ in questo modo:

$$\begin{aligned}
p_Y(y) &= P(Y=y)\\\
&= P(g(X) = y)\\\
&= \sum_{x:g(x)=y}p_X(x)
\end{aligned}$$

### Variabile aleatoria continua

Supponiamo di avere una variabile aleatoria continua $X$ con legge di probabilità $f_X(x)$.

Supponiamo inoltre di avere un'altra variabile aleatoria $Y = g(X)$, dove $g$ è una funzione deterministica nota.

Per determinare la legge di probabilità di $Y$ è possibile procedere in questo modo:

1. Calcolare la legge cumulata di $Y$:$$F_Y(y) = P(Y \le y)$$
2. Calcolare la derivata della cumulata:$$f_Y(y) = {d\over dy}F_Y(y)$$

> **Esempio**
>
> Supponiamo di avere una variabile aleatoria uniforme continua $X\sim U[0,2]$, la cui legge di probabilità è quindi:
> $$f_X(x) = \begin{cases}
> {1\over2}, &0<x<2\\\
> 0, &\text{altrimenti}
> \end{cases}$$
> Ipotizziamo ora di avere una variabile aleatoria così definita:
> $$Y = g(X) = X^3$$
> Proviamo a seguire i passaggi elencati sopra per ottenere $f_Y(y)$:
> 1. Calcoliamo la legge cumulata di $Y$:$$\begin{aligned}
> F_Y(y) &= P(Y\le y)\\\
> &= P(X^3\le y)\\\
> &= P(X \le y^{1/3})\\\
> &= F_X(y^{1/3}) = \begin{cases}
> {1\over2}y^{1/3}, &0<y<8\\\
> 0, &y<0\\\
> 1, &y>8
> \end{cases}
> \end{aligned}$$
> 2. Deriviamo il risultato:$$f_Y(y) = {d\over dy}F_Y(y) = \begin{cases}
> {1\over 6y^{2/3}}, &0<y<8\\\
> 0, &\text{altrimenti} 
> \end{cases}$$

### Trasformazioni lineari di variabili aleatorie

Supponiamo di avere una variabile aleatoria $X$ con legge di probabilità nota $f_X$ ed un'altra variabile casuale $Y=aX+b$ con $a,b$ costanti note.

È dimostrabile che vale:

$$f_Y(y) = f_X\bigg({y-b\over a}\bigg)\cdot{1\over|a|}, \> \forall a \ne 0$$

> **Osservazione**
>
> Se $a=0$, allora $Y=b$ è una variabile aleatoria *degenere*.

### Trasformazioni monotone di variabili aleatorie

Vediamo ora un caso particolare di trasformazione: prendiamo una variabile aleatoria $Y=g(X)$, con $g$ funzione deterministica nota e *strettamente monotona*.

Nel caso in cui $g$ abbia le caratteristiche specificate, è possibile determinare $f_Y$ in modo **diretto**, *senza calcolare la sua legge cumulata*.

Possiamo infatti calcolare che:

$$f_Y(y) = f_X\big(g^{-1}(y)\big)\cdot {1\over\bigg|{dg\over dx}\big(g^{-1}(y)\big)\bigg|}$$

> **Esempio**
>
> Riprendiamo l'esempio fatto [precedentemente](#variabile-aleatoria-continua) ed applichiamovi quello che abbiamo scoperto ora.
> Possiamo certamente dire che $y=g(x)=x^3$ è strettamente monotona, perciò calcoliamo la funzione inversa $g^{-1}$:
> $$x = g^{-1}(y) = y^{1/3}$$
> Calcoliamo poi la derivata rispetto ad $x$ di $g$:
> $${dg\over dx}(x) = 3x^2$$
> Possiamo allora dire:
> $$\begin{aligned}
> f_Y(y) &= f_X(y^{1/3})\cdot{1\over\big|3y^{2/3}\big|}\\\
> &= f_X(y^{1/3})\cdot{1\over 3y^{2/3}}
> \end{aligned}$$
