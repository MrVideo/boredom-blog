---
title: "Statistiche congiunte"
draft: false
type: 'page'
toc: true
mathjax: true
---

---

## Legge della somma di variabili aleatorie

Supponiamo di avere due variabili aleatorie indipendenti $X,Y$.

Definiamo una variabile aleatoria $W$ come la somma delle due precedenti:

$$W = X + Y$$

Possiamo calcolare la legge di probabilità di $W$ in questo modo:

$$\begin{aligned}
p_W(w) &= P(W=w)\\\
&= P(X+Y = w)\\\
&= \sum_{(x,y):x+y=w} p_{X,Y}(x,y)\\\
&= \sum_{(x,y):x+y=w} p_X(x)p_Y(y) &(1)\\\
&= \sum_x p_X(x)p_Y(w-x) &(2)
\end{aligned}$$

Come si vede dal procedimento, grazie all'indipendenza delle due variabili aleatorie $(1)$ ed alla relazione tra le realizzazioni di $x$, $y$ e $z$ $(2)$, possiamo più semplicemente trovare la legge di probabilità cercata.

L'espressione in $(2)$ è detta **somma di convoluzione**.

> **Come effettuare una convoluzione**
>
> 1. Si sovrappongono graficamente le due leggi di probabilità
> 2. Si ribalta una delle due leggi di cui sopra
> 3. Si trasla di $w$ posizioni la legge ribaltata precedentemente
> 4. Si moltiplicano le leggi e si sommano i prodotti

Questa legge vale anche nel caso continuo: in tal caso, si applica il cosiddetto **integrale di convoluzione**:

$$f_W(w) = \int_{-\infty}^\infty f_X(x)\cdot f_Y(w-x)dx$$

---

## Legge congiunta di due variabili aleatorie Gaussiane indipendenti

Si supponga di avere due variabili aleatorie gaussiane indipendenti:

$$\begin{aligned}
X &\sim N(\mu_X, \sigma^2_X)\\\
Y &\sim N(\mu_Y, \sigma^2_Y)\\\
\end{aligned}$$

Possiamo calcolare la legge di probabilità congiunta delle due in questo modo:

$$\begin{aligned}
f_{X,Y}(x,y) &= f_X(x)f_Y(y)\\\
&= {1\over\sqrt{2\pi\sigma_X^2}} e^{-{(x-\mu_X)^2\over 2\sigma_X^2}} \cdot {1\over\sqrt{2\pi\sigma_Y^2}} e^{-{(y-\mu_Y)^2\over 2\sigma_Y^2}}\\\
&= {1\over 2\pi\sqrt{\sigma_X^2\sigma_Y^2}} \cdot e^{-{(x-\mu_X)^2\over 2\sigma_X^2}-{(y-\mu_Y)^2\over 2\sigma_Y^2}}
\end{aligned}$$

Possiamo definire le cosiddette *curve di livello* della legge congiunta trovando il luogo dei punti $(x,y)$ tale per cui $f_{X,Y}(x,y) = \text{cost}$.

Si può calcolare che questo luogo dei punti è un'ellisse di espressione:

$${(x-\mu_X)^2\over\sigma_X^2} + {(y-\mu_Y)^2\over\sigma_Y^2} = \text{cost}$$

> **Casi particolari**
>
> - Se $\sigma_X^2 = \sigma_Y^2$, allora le curve di livello sono circonferenze
> - Se $\sigma_X^2 > \sigma_Y^2$, allora l'ellisse avrà l'asse maggiore parallelo all'asse $x$
> - Se $\sigma_X^2 < \sigma_Y^2$, allora l'ellisse avrà l'asse maggiore parallelo all'asse $y$

> **Attenzione**
>
> Se le due variabili aleatorie non sono indipendenti, allora le curve di livello saranno orientate diagonalmente.

---

## Somma di due variabili aleatorie gaussiane indipendenti

È dimostrabile che *la somma di due variabili aleatorie Gaussiane è a sua volta una variabile aleatoria Gaussiana*.

In generale, date due variabili aleatorie indipendenti così definite:

$$\begin{aligned}
X &\sim N(\mu_X, \sigma^2_X)\\\
Y &\sim N(\mu_Y, \sigma^2_Y)
\end{aligned}$$

Considerata una variabile aleatoria $W = X + Y$, allora possiamo dire che:

$$W \sim N(\mu_X + \mu_Y, \sigma^2_X + \sigma---

## Covarianza

La covarianza di due variabili aleatorie è una misura di quanto le due variabili varino assieme ed è così definita:

$$\text{Cov}[X,Y] = E[XY] - E[X]E[Y]$$

> **Nota**
>
> $$\text{Cov}[X,X] = \text{Var}[X]$$

Se il valore atteso di una delle due variabili aleatorie è nullo, allora vale:

$$\text{Cov}[X,Y] = E[XY]$$

### Varianza della somma di variabili aleatorie

Supponiamo di avere $i$ variabili aleatorie $X_i$.

Vediamo qual è la varianza della somma di tutte queste variabili aleatorie:

$$\begin{aligned}
\text{Var}\bigg[\sum_{i=1}^n X_i\bigg] &= \text{Var}\bigg[\sum_{i=1}^n \big(X_i - E[X_i]\big) \bigg]
\end{aligned}$$

Per comodità, facciamo questa sostituzione:

$$\tilde{X_i} \triangleq X_i - E[X_i]$$

Possiamo dire allora:

$$E[\tilde{X_i}] = 0$$

Vediamo che queste sono tutte variabili aleatorie *a media nulla*. Continuiamo ora i calcoli applicando la sostituzione:

$$\begin{aligned}
\text{Var}\bigg[\sum_{i=1}^n X_i\bigg] &= \text{Var}\bigg[\sum_{i=1}^n \tilde{X_i} \bigg]\\\
&= E\bigg[\bigg(\sum_{i=1}^n \tilde{X_i}\bigg)^2 \bigg] - 0^2\\\
&= E\bigg[\sum_{i=1}^n \tilde{X_i}^2 \bigg] + E\bigg[\sum_{i\ne j} \tilde{X_i}\tilde{X_j} \bigg]\\\
&= \sum_{i=1}^n E[\tilde{X_i^2}] + \sum_{i\ne j} E[\tilde{X_i}\tilde{X_j}]
\end{aligned}$$

A questo punto, sapendo che $E[\tilde{X_i}] = 0$, posso *sottrarre uno zero* all'espressione a cui siamo giunti in questo modo:

$$\text{Var}\bigg[\sum_{i=1}^n X_i\bigg] = \sum_{i=1}^n \bigg(E[\tilde{X_i^2}] - E[\tilde{X_i}]^2\bigg) + \sum_{i\ne j} E[\tilde{X_i}\tilde{X_j}]$$

Troviamo così la varianza della variabile aleatoria $\tilde{X_i}$:

$$E[\tilde{X_i^2}] - E[\tilde{X_i}]^2 = \text{Var}[\tilde{X_i}]$$

È possibile eseguire la stessa operazione sul termine prodotto delle variabili aleatorie, ottenendo così la *covarianza* delle due:

$$E[\tilde{X_i}\tilde{X_j}] - E[\tilde{X_i}]E[\tilde{X_j}] = \text{Cov}[\tilde{X_i},\tilde{X_j}]$$

Giungiamo all'espressione finale:

$$\text{Var}\bigg[\sum_{i=1}^n \tilde{X_i}\bigg] = \sum_{i=1}^n \text{Var}[\tilde{X_i}] + \sum_{i\ne j}\text{Cov}[\tilde{X_i},\tilde{X_j}]$$

Da questa equazione comprendiamo che la varianza di una somma di variabili aleatorie è pari alla **somma delle varianze di ciascuna**, più la **somma delle covarianze di ogni coppia** di variabili aleatorie.

### Covarianza e indipendenza

[Considerando quanto visto per il valore atteso](../multiple-drv#indipendenza), se due variabili aleatorie sono indipendenti, possiamo dire che:

$$\begin{aligned}
\text{Cov}[X,Y] &= E[XY]-E[X]E[Y]\\\
&= E[X]E[Y] - E[X]E[Y]\\\
&= 0
\end{aligned}$$

Non è detto il contrario però:

$$\text{Cov}[X,Y] = 0 \nRightarrow X \perp Y$$

### Coefficiente di correlazione lineare

Il coefficiente di correlazione lineare è una versione *adimensionale* della covarianza calcolabile in questo modo:

$$\rho[X,Y] = {\text{Cov}[X,Y] \over \sigma_X\sigma_Y} = E\bigg[{\big(X-E[X]\big)\over\sigma_X} \cdot {\big(Y-E[Y]\big)\over\sigma_Y} \bigg]$$

Elenchiamo alcune proprietà di questo coefficiente:

- $-1 \le \rho[X,Y] \le 1$
- $X\perp Y \implies \rho[X,Y] = 0$
- $\rho[X,Y]=0\implies\text{Cov}[X,Y] = 0 \nRightarrow X\perp Y$

> **Nota**
>
> In particolare, se $\big|\rho[X,Y]\big| = 1$, allora $X$ e $Y$ sono **linearmente dipendenti** l'una dall'altra, quindi si può dire che $Y = aX+b$, con coefficienti $a,b$ opportuni.
