---
title: "Calcolare l'esponenziale di matrice"
draft: false
type: 'page'
toc: true
mathjax: true
---


Vediamo come calcolare $e^{At}$ con $A$ matrice diagonalizzabile.

Definiamo l'esponenziale di matrice come segue:

$$e^M := \mathbb I+ M+{M^2\over2!}+{M^3\over3!}+\ldots=\sum_{k= 0}^{+\infty}{M^k\over k!}$$

Nel caso in cui $M$ sia diagonalizzabile, detti $\lambda_i$ i suoi autovalori e posto $D=\text{diag}\{\lambda_i\}$, $\exists T^{-1}:T^{-1}MT = D \implies M=TDT^{-1}$.

Quindi:

$$\begin{align}
e^M&=TT^{-1}+TDT^{-1}+{TDT^{-1}TDT^{-1}\over2!} + {TDT^{-1}TDT^{-1}TDT^{-1}\over3!}+\ldots\\\
&=T\bigg(\mathbb I+D+{D^2\over2!}+ {D^3\over3!}+\ldots\bigg)T^{-1}\\\
&=Te^DT^{-1}
\end{align}$$

Ma sappiamo che:

$$D=\begin{bmatrix}\lambda_1&&\\\&\ddots&\\\&&\lambda_n\end{bmatrix}\implies D^k = \begin{bmatrix}\lambda_1^k&&\\\&\ddots&\\\&&\lambda_n^k\end{bmatrix}$$

Allora:

$$e^D=\begin{bmatrix}e^{\lambda_1}&&\\\&\ddots&\\\&&e^{\lambda_n}\end{bmatrix}$$

Dunque:

$$e^{At}=e^{TDT^{-1}t} = T\begin{bmatrix}e^{\lambda_1t}&&\\\&\ddots&\\\&&e^{\lambda_nt}\end{bmatrix}T^{-1}$$

I termini $e^{\lambda_it}$ si chiamano **modi del sistema**.
