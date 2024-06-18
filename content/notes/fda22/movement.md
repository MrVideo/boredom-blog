---
title: "Movimento"
draft: false
type: 'page'
toc: true
mathjax: true
---
## Caso generale (TI per comodità)
Dato uno stato iniziale $x(0)$ e un ingresso generico $u(t)$ (o $u(k)$ per il caso a TD), vengono detti, per $t\geq0$ (o $k\geq0$):
- $x(t)$ (o $x(k)$) il **movimento dello stato**
- $y(t)$ (o $y(k)$) il **movimento dell'uscita**
---
## Caso LTI a TD

Dato il SD LTI a TD:

$$\begin{cases}x(k)=Ax(k-1)+bu(k-1)\\\y(k)=cx(k)+du(k)\end{cases}$$

dati $x(0)$ e $u(k)$ per $k\geq0$, calcoliamo il movimento dello stato:

$$\begin{align}
x(0) &\text{ dato}\\\
x(1) &= Ax(0)+bu(0)\\\
x(2) &= A^2x(0)+Abu(0)+bu(1)\\\
x(3) &= A^3x(0)+A^2bu(0)+Abu(1)+bu(2)\\\
\vdots\\\
x(k) &= {A^kx(0)} + {\sum_{l=0}^{k-1}A^{k-l-1}bu(l)}
\end{align}$$

in cui la prima parte dell'equazione rappresenta il **movimento libero**, mentre la seconda il **movimento forzato**. Questa equazione è nota come **formula di Lagrange a tempo discreto per lo stato**.

Alcune osservazioni:
- Il movimento libero (o *ML*) dipende linearmente da $x(0)$ e non dipende da $u(k)$
- Il movimento forzato (o *MF*) dipende linearmente da $u(k)$ e non dipende da $x(0)$
- Il movimento complessivo è dato dalla somma di ML ed MF
- Vale il **principio di sovrapposizione degli effetti** (o *PSE*)

Calcoliamo ora il movimento dell'uscita con la **formula di Lagrange a TD** per l'uscita:

$$\begin{align}
y(k)&=cx(k)+du(k)=\\\
&={cA^kx(0)} + {c\sum_{l=0}^{k-1}A^{k-l-1}bu(l)+du(k)}
\end{align}$$

Come visto sopra, la prima parte della formula riguarda il movimento libero dell'uscita $y$, mentre la seconda il movimento forzato.

---

## Caso LTI a TC

Dato il SD LTI a TC:

$$\begin{cases}\dot x=Ax+bu\\\y=cx+du\end{cases}$$

usiamo le **formule di Lagrange** per calcolare i movimenti di stato ed uscita:

$$\begin{align}
x(t) &= {e^{At}x(0)} + {\int_0^te^{A(t-\tau)}bu(\tau)d\tau}\\\
y(t) &= {ce^{At}x(0)} + {c\int_0^te^{A(t-\tau)}bu(\tau)d\tau+du(t)}
\end{align}$$

Il primo addendo di entrambe le formule, come nel caso a tempo discreto, riguarda il movimento libero del sistema, mentre il secondo riguarda il movimento forzato.

> **Nota**: vedere [*Calcolare l'esponenziale di matrice*](../matrix-exp).
