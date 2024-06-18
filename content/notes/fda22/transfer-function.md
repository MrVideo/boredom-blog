---
title: "Funzione di trasferimento"
draft: false
type: 'page'
toc: true
mathjax: true
---

---
# Funzione di trasferimento

Prendiamo un SD LTI a TC SISO:

$$\begin{cases}\dot x=Ax+bu\\\y=cx+du\end{cases}$$

Trasformiamo ora secondo Laplace l'equazione di stato:

$$\begin{align}
\mathscr L[\dot x(t)]&=\mathscr L[Ax(t)+bu(t)]\\\
&\downarrow\text{proprietà della derivata}\\\
sX(s)-x(0)&=AX(s)+bU(s)\\\
(s\mathbb I-A)X(s)&=x(0)+bU(s)
\end{align}$$

Allora, $\forall s\notin\{\text{autovalori di }A\}$:

$$X(s)={(s\mathbb I-A)^{-1}x(0)}+{(s\mathbb I-A)^{-1}bU(s)}$$

In cui il primo addendo è la trasformata di Laplace del movimento libero, mentre il secondo quella del movimento forzato.

Ora trasformiamo l'equazione di uscita secondo Laplace e vi sostituiamo $X(s)$:

$$\begin{align}
Y(s)&=cX(s)+dU(s)\\\
&\downarrow\text{linearità TDL}\\\
&={c(s\mathbb I-A)^{-1}x(0)}+{\overbrace{\big[c(s\mathbb I-A)^{-1}b+d\big]}^{G(s)}U(s)}
\end{align}$$

Anche in questo caso, il primo addendo non è altro che la trasformata di Laplace del movimento libero dell'uscita, mentre il secondo quella del movimento forzato.

Chiamiamo **funzione di trasferimento** (*FdT*), e la indichiamo con $G(s)$, la funzione:

$$G(s)=c(s\mathbb I-A)^{-1}b+d$$

---

## Calcolo ed aspetto di una FdT

Studiamo la forma della funzione di trasferimento: $G(t)=c(s\mathbb I-A)^{-1}b+d$:

- Calcoliamo $(s\mathbb I-A)^{-1}$:
    $$(s\mathbb I-A)^{-1}={1\over\det(s\mathbb I-A)}\begin{bmatrix}A_{11}(s)&\ldots&A_{1n}(s)\\\\vdots&\ddots&\vdots\\\A_{n1}(s)&\ldots&A_{nn}(s)\end{bmatrix}$$
- Calcoliamo $c(s\mathbb I-A)^{-1}b$:
    $$c(s\mathbb I-A)^{-1}b={1\over\det(s\mathbb I-A)}\underbrace{\overbrace{\begin{bmatrix}c_1&\ldots&c_n\end{bmatrix}}^{1\times n}\overbrace{\begin{bmatrix}A_{11}(s)&\ldots&A_{1n}(s)\\\\vdots&\ddots&\vdots\\\A_{n1}(s)&\ldots&A_{nn}(s)\end{bmatrix}}^{n\times n}\overbrace{\begin{bmatrix}b_1\\\\vdots\\\b_n\end{bmatrix}}^{n\times 1}}_{\text{polinomio di grado al più }n-1}$$
- Studiamo ora $G(s)$:
    $$\begin{align}
G(s)&=\overbrace{c(s\mathbb I-A)^{-1}b}^{\tilde N(s)/D(s)}+d\\\
&={\tilde N(s)\over D(s)}+d&\text{dove: }&D(s)\text{ PC di A, grado }n\\\
&&&\tilde N(s)\text{ polinomio di grado al più }n-1
\end{align}$$

Ora, se $d=0$, ossia se il sistema è strettamente proprio:

$$G(s)={\tilde N(s)\over D(s)},\ \deg(\text{Num})<\deg(\text{Den})$$

Altrimenti, se $d\ne0$:

$$G(s)={\tilde N(s)+dD(s)\over D(s)}={N(s)\over D(s)},\ \deg(\text{Num})=\deg(\text{Den})$$

Quindi:

1. $G(s)$ è **razionale fratta**
2. I poli di $G(s)$ sono **autovalori di A** (ma non necessariamente tutti)
3. $\deg(\text{Num})=\deg(\text{Den})\iff d\ne0$, altrimenti $\deg(\text{Num})<\deg(\text{Den})$
