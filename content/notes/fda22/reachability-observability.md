---
title: "Raggiungibilità e osservabilità"
draft: false
type: 'page'
toc: true
mathjax: true
---

---

## Raggiungibilità
Dato un SD LTI a TC SISO, uno stato $\tilde x$ si dice **raggiungibile** (da zero) se $\exists\tilde t<+\infty$ e $\tilde u(t)$ definito su $[0,\tilde t]$ tali che:$$\begin{cases}x(0)=0\\\u(t)=\tilde u(t),&0\leq t\leq\tilde t\end{cases}\implies x(\tilde t)=\tilde x$$
Un sistema si dice **completamente raggiungibile** se e solo se **ogni stato è raggiungibile**.
### Determinare la raggiungibilità di un sistema
Premessa: **teorema di Caylay-Hamilton**:
>Ogni matrice annulla il suo polinomio caratteristico.
>Se $\pi(s)$ è il PC di $A$, allora $\pi(A)=\underline 0$.

Quindi, detti $\beta_i$ i coefficienti del PC:

$$A^n+\beta_1A^{n-1}+\ldots+\beta_n\mathbb I=\underline 0\implies A^n=-\beta_1A^{n-1}-\ldots-\beta_n\mathbb I$$

e così ogni potenza di $A$ da $n$ in poi è combinazione lineare di $\mathbb I, A, \ldots, A^{n-1}$.

Di conseguenza, partendo da $x(0)=0$, si avrà:

$$\begin{align}
x(t)&=\int_0^te^{A(t-\tau)}bu(\tau)d\tau&e^{A(t-\tau)}=\mathbb I+A(t-\tau)+{A^2\over2}(t-\tau)^2+\ldots\\\
&=\int_0^t\sum_{l=0}^{n-1}\gamma_e(t-\tau)A^lbu(\tau)d\tau\\\
&=\sum_{l=0}^{n-1}A^lb\overbrace{\int_0^t\gamma_e(t-\tau)u(\tau)d\tau}^{z_e(t)}&z_e(t) \text{ contiene i coefficienti di }\pi(s)\text{ e l'ingresso}\\\
&=\sum_{l=0}^{n-1}A^lbz_e(t)
\end{align}$$

Ovvero:

$$x(t)=\overbrace{\begin{bmatrix}b&Ab&A^2b&\ldots&A^{n-1}b\end{bmatrix}}^{M_R}\overbrace{\begin{bmatrix}z_1(t)\\\z_2(t)\\\\vdots\\\z_{n-1}(t)\end{bmatrix}}^{Z(t)}$$

dove $M_R$ è la **matrice di raggiungibilità**. Allora:

$$x(t)=M_RZ(t)$$

Supponiamo ora di voler portare lo stato da $x(0)=0$ a $\tilde x$ arbitrario. Perché questo sia possibile, per ogni $\tilde x$, dev'essere $M_R\tilde Z(t)=\tilde x(t)$ e quindi occorre e basta che $M_R$ non sia singolare.

#### Criterio di raggiungibilità
Nel caso SISO:
>Sistema raggiungibile (*R*) $\iff M_R$ non singolare

Nel caso MIMO:
>Sistema raggiungibile $\iff \text{rank}(M_R)=n$.

---
## Osservabilità
Uno stato $\tilde x$ si dice ***non* osservabile** se:$$\begin{cases}x(0)=\tilde x\\\u(t)=0,\ t\geq0\end{cases}\implies y(t)=0,\ t\geq0$$
Un sistema è **osservabile** (*O*) $\iff$ **tutti gli stati sono osservabili**.
### Criterio di osservabilità
Data la **matrice di osservabilità** $M_O$:$$M_O=\begin{bmatrix}c^T&A^Tc^T&(A^2)^Tc^T&\ldots&(A^{n-1})^Tc^T\end{bmatrix}$$
un sistema è **osservabile** $\iff M_O$ è non singolare.

---
## Osservazioni generali
1. Un sistema può avere parti non raggiungibili (*NR*) e/o non osservabili (*NO*)
2. Queste parti NR e/o NO del sistema non si trovano nella FdT, che rappresenta solo la parte R e O
3. Di conseguenza, gli autovalori di parti NR e/o NO di un sistema dinamico **si cancellano** nel calcolo della sua FdT
### Cancellazione critica
>Una cancellazione si dice **critica** se avviene al di fuori della regione di stabilità asintotica, cioè se l'autovalore cancellato ha $\Re\geq0$.

### Conseguenze
1. $(A,b,c,d)$ e $G(s)$ sono rappresentazioni equivalenti di un sistema dinamico, a meno di una trasformazione si similarità, se e solo se nel calcolo di $G(s)$ **non vi sono cancellazioni** o, equivalentemente, se il sistema è **raggiungibile ed osservabile**.
2. Poiché i poli di $G(s)$ sono gli autovalori della sola parte R e O del sistema dinamico, perché si possa studiare la stabilità asintotica del SD usando i poli di $G(s)$, **non devono esserci cancellazioni critiche**.
