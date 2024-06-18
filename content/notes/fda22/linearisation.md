---
title: "Linearizzazione nell'intorno di un equilibrio"
draft: false
type: 'page'
toc: true
mathjax: true
---

---

Consideriamo un SD NL TI a TC:

$$S:\begin{cases}\dot x = f(x,u)\\\y=g(x,u)\end{cases}$$

ed un suo equilibrio $(\overline u, \overline x, \overline y)$.

Vogliamo determinare un SD LTI che approssima $S$ nell'intorno di un equilibrio.

Consideriamo l'equazione di stato e sviluppiamola in serie fermandoci al primo ordine:

$$f(\overline x +\delta x,\overline u + \delta u)=\cancelto{0}{f(\overline x, \overline u)}+f_x(\overline x, \overline u)\delta x+f_u(\overline x,\overline u)\delta u$$

dove $\delta x,\delta u$ sono gli spostamenti di $x,u$ dall'equilibrio.

Poniamo ora $\delta\dot x={d\over dt}\delta x$, cioè:

$${d\over dt}(\overline x+\delta x)=\delta\dot x\implies\dot x=\delta\dot x$$

poiché $\overline x$ è una costante, quindi la sua derivata è nulla. Otteniamo così:

$$\underbrace{\delta\dot x}_{n\times1}=\underbrace{f_x(\overline x, \overline u)}_{n\times n}\underbrace{\delta x}_{n\times 1}+\underbrace{f_u(\overline x, \overline u)}_{n\times1}\underbrace{\delta u}_{1\times1}$$

L'equazione di stato del sistema linearizzato allora diventa:

$$\delta\dot x=A\delta x+b\delta u$$

Consideriamo ora l'equazione di uscita ed operiamo analogamente:

$$\underbrace{g(x,u)}_y=g(\overline x+\delta x, \overline u+\delta u)=\underbrace{g(\overline x,\overline u)}_{\overline y}+g_x(\overline x,\overline u)\delta x+g_u(\overline x, \overline u)\delta u$$

L'equazione di uscita del sistema linearizzato è:

$$\delta y=c\delta x+d\delta u$$

---
## Esempio
Dato il sistema dinamico a tempo continuo, tempo invariante, non lineare:$$
\begin{cases}
\dot x_1=x_1^2-u\\\
\dot x_2=\sqrt{x_1}-x_2\\\
y = 4x^3_2+u^2
\end{cases}$$
Esso si linearizza così:$$
\begin{align}
A&=\begin{bmatrix}
{\partial\over\partial x_1}(x_1^2-u) & {\partial\over\partial x_2}(x_1^2-u)\\\
{\partial\over\partial x_1}(\sqrt{x_1}-x_2) & {\partial\over\partial x_2}(\sqrt{x_1}-x_2)
\end{bmatrix},\\\
b&=\begin{bmatrix}
{\partial\over\partial u}(x_1^2-u)\\\
{\partial\over\partial u}(\sqrt{x_1}-x_2)
\end{bmatrix},\\\
c&=\begin{bmatrix}
{\partial\over\partial x_1}(4x^3_2+u^2) & {\partial\over\partial x_2}(4x^3_2+u^2)
\end{bmatrix},\\\
d&={\partial\over\partial u}(4x^3_2+u^2)
\end{align}$$
Questi calcoli risultano in:$$\begin{align}
A&=\begin{bmatrix}
2x_1 & 0\\\
{1\over 2\sqrt{x_1}} & -1
\end{bmatrix},\\\
b&=\begin{bmatrix}
-1\\\
0
\end{bmatrix},\\\
c&=\begin{bmatrix}
0 & 12x_2^2
\end{bmatrix},\\\
d&=2u
\end{align}$$
Allora, il sistema linearizzato è:$$\begin{cases}
\delta\dot x_1=2\delta x_1\\\
\delta\dot x_2={1\over2\sqrt{\delta x_1}}-\delta u\\\
\delta y = 12\delta x_2^2 + 2\delta u
\end{cases}$$
