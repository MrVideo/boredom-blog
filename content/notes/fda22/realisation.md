---
title: "Realizzazione"
draft: false
type: 'page'
toc: true
mathjax: true
---

---

Il problema della realizzazione consiste nel ricavare un modello in variabili di stato equivalente al modello assegnato tramite la funzione di trasferimento $G(s)$:$$G(s)\to(A,b,c,d)$$
Limitandosi alla realizzazione minima, in cui $\dim(A)=\deg(\text{denominatore di }G)$, esistono alcuni modi *comodi*, detti **canonici** per risolvere il problema della realizzazione.

---
## Premessa
Se in $G(s)=G_N(s)/G_D(s)$ vale $\deg(G_N(s))=\deg(G_D(s))$, si può scrivere:$$G(s)=d+{N(s)\over D(s)},\ d\text{ costante}$$dove $\deg(N(s)) < \deg(D(s))$, quindi basta trattare il caso $\deg(N(s)) < \deg(D(s))$.

---

## Forma canonica di raggiungibilità (FCR)
Data la funzione di trasferimento:$$G(s) = {b_1s^{n-1}+b_2s^{n-2}+\ldots+b_n\over s^n+a_1s^{n-1}+\ldots+a_{n-1}s+a_n}$$
la **forma canonica di raggiungibilità** o di controllo è data dalle matrici:$$A=\begin{bmatrix}
0&1&0&\cdots&0\\\
0&0&1&\cdots&0\\\
\vdots&\vdots&\vdots&\ddots&\vdots\\\
0&0&0&\cdots&1\\\
-a_n&-a_{n-1}&-a_{n-2}&\cdots&-a_1
\end{bmatrix},\ \ b=\begin{bmatrix}
0\\\
0\\\
0\\\
\vdots\\\
1
\end{bmatrix},\ \ c=\begin{bmatrix}
b_n&b_{n-1}&b_{n-2}&\cdots&b_1
\end{bmatrix}$$

---

## Forma canonica di osservabilità (FCO)
Data la funzione di trasferimento:$$G(s) = {b_1s^{n-1}+b_2s^{n-2}+\ldots+b_n\over s^n+a_1s^{n-1}+\ldots+a_{n-1}s+a_n}$$
la **forma canonica di osservabilità** o di ricostruzione è data dalle matrici:$$A=\begin{bmatrix}
0&0&0&\cdots&0&-a_0\\\
1&0&0&\cdots&0&-a_1\\\
0&1&0&\cdots&0&-a_2\\\
\vdots&\vdots&\vdots&\ddots&\vdots&\vdots\\\
0&0&0&\cdots&1&-a_{n-1}
\end{bmatrix},\ \ b=\begin{bmatrix}
b_n\\\
b_{n-1}\\\
b_{n-2}\\\
\vdots\\\
b_1
\end{bmatrix},\ \ c=\begin{bmatrix}
0&0&0&\cdots&1
\end{bmatrix}$$
