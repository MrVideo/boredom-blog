---
title: 'Equilibrio'
draft: false
type: 'page'
toc: true
mathjax: true
---

---
Dato un SD TI ed applicatogli un ingresso costante $u(t)=\overline u$, esiste qualche valore costante $\overline x$ dello stato $x$ tale per cui $x(t)=\overline x, t\geq 0$?
Se ne esistono, questi si dicono **stati di equilibrio** per il SD con $u(t)=\overline u$.

## Calcolo degli stati di equilibrio
### Caso a tempo continuo
Se $x$ deve rimanere costante, allora deve valere $\dot{x}=0$, cioè $f(\overline x, \overline u)=0$.
Nel caso generale $\dot x = f(\overline x, \overline u)$, gli equilibri saranno le soluzioni dell'equazione $f(\overline x, \overline u)=0$.
Se il sistema è anche **LTI**, la sua equazione di stato sarà:$$\dot x = Ax+bu$$
Nel caso di uno stato di equilibrio, questa equazione diventa:$$o=A\overline x+b\overline u$$
Se la matrice $A$ non è singolare (cioè $\det A \ne 0$), esiste un unico stato $\overline x$ tale che:$$\overline x = -A^{-1}b\overline u$$
Altrimenti, o non esistono stati di equilibrio, o ne esistono infiniti.
### Caso a tempo discreto
Dovrà essere che $x(k+1)=x(k)=\overline x$, quindi per il SD con equazione di stato $x(k+1)=f(x(k), u(k))$, gli equilibri saranno le soluzioni dell'equazione $\overline x = f(\overline x, \overline u)$.
Se il sistema è anche **LTI**, la sua equazione di stato sarà:$$x(k+1) = Ax(k)+bu(k)$$
Nel caso di uno stato di equilibrio, questa equazione diventa:$$\begin{align}\overline x &= A\overline x+b\overline u\\\
(\mathbb I-A)\overline x&=b\overline u\end{align}$$
Se la matrice $A$ non ha autovalori in $1$, esiste un unico stato $\overline x$ tale che:$$\overline x=(\mathbb I-A)^{-1}b\overline u$$
## Uscita di equilibrio
### Caso generale
L'uscita prodotta dallo stato all'equilibrio, se esiste, è:$$\overline y = g(\overline x, \overline u)$$
### Caso LTI
L'uscita prodotta dallo stato all'equilibrio, se esiste, è sempre:$$\overline y = c\overline x+d\overline u$$
