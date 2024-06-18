---
title: 'Sistemi dinamici'
draft: false
type: 'page'
toc: true
mathjax: true
---

---
Dato un sistema di cui si conoscono i parametri fisici e gli ingressi $u(t)$ sull'intervallo temporale $[t_0, t]$, se queste informazioni non sono sufficienti a determinare l'uscita $y(t)$ sullo stesso intervallo di tempo, il sistema si definisce **dinamico**.
## Sistemi dinamici a tempo continuo
Con espressione vettoriale, un sistema dinamico a tempo continuo *single input, single output* è descrivibile con il sistema di equazioni:
$$\begin{cases}
\dot{x}(t)=f(x(t), u(t),t)\\\
y(t)=g(x(t),u(t),t)
\end{cases}$$
dove:
+ $x(t)$ è detta **variabile di stato** del sistema, $x(t)\in\mathbb R^n$
+ $\dot{x}(t)$ è definita come la **derivata temporale** di $x(t)$
+ $y(t)$ è detta **equazione di uscita** del sistema, $y(t)\in\mathbb R$
+ $u(t)$ rappresenta l'**ingresso** del sistema, $u(t)\in\mathbb R$
### Proprietà dei sistemi dinamici a tempo continuo
Possiamo individuare tre proprietà importanti dalla forma delle due funzioni $f,g$ contenute nel sistema rappresentato sopra:
1. $f, g$ sono **lineari** in $x, u \iff$ sistema dinamico **lineare** (indicato con **L**)
2. $f=f(x,u), g=g(x,u)\iff$ sistema dinamico **tempo-invariante** (indicato con **TI**, anche detto *stazionario*)
3. $g=g(x,t)\iff$ sistema dinamico **strettamente proprio** (indicato con **SP**)
## Sistemi dinamici a tempo discreto
Nei sistemi dinamici a tempo discreto, l'indice *temporale* è un intero $k\in\mathbb Z$.
Considerando la forma vettoriale, possiamo esprimere un sistema dinamico a tempo discreto con il sistema di equazioni:$$\begin{cases}x(k)=f(x(k-1), u(k-1), k)\\\y(k)=g(x(k), u(k), t)\end{cases}$$
Alcune osservazioni:
+ Il caso a tempo discreto gode di diverse similarità al caso a tempo continuo
+ Le equazioni, invece di essere *differenziali*, sono *alle differenze*, la loro controparte per domini discreti
+ L'equazione di stato di un sistema a tempo discreto prevede gli stati e gli ingressi precedenti, mentre l'equazione di uscita è completamente sincrona
+ Le stesse proprietà valide per i sistemi a tempo continuo sono valide, con opportune trasformazioni, a tempo discreto

## Sistemi dinamici lineari tempo-invarianti (SISO)
### Caso a tempo continuo
Possiamo riscrivere in forma compatta il sistema di equazioni rappresentante un sistema dinamico a tempo continuo lineare tempo-invariante in questo modo:$$\begin{cases}\dot{x}=Ax+bu\\\y=cx+du\end{cases}$$
La quadrupla $(A,b,c,d)$ si dice **descrizione di stato** del sistema dinamico.
### Caso a tempo discreto
Come abbiamo fatto per il caso a tempo continuo, riscriviamo le equazioni di un sistema dinamico a tempo discreto:$$\begin{cases}x(k)=Ax(k-1)+bu(k-1)\\\y(k)=cx(k)+du(k)\end{cases}$$
Anche in questo caso, la quadrupla $(A,b,c,d)$ si dice **descrizione di stato** del sistema dinamico.
