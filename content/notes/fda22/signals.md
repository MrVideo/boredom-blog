---
title: "Segnali e trasformate"
draft: false
type: 'page'
toc: true
mathjax: true
---

---
## Serie di Fourier

Dato un segnale $v(t)$ periodico di periodo $T$:$$v(t)=v_0+\sum_{k=1}^{+\infty}v_k\sin(k\omega_0y+\varphi_k),\ \omega_0={2\pi\over T}$$
La somma è formata da un'infinità *numerabile* di elementi.

## Trasformata di Fourier

Dato un segnale $v(t)$ definito per $t\in\mathbb R$, definiamo la sua trasformata di Fourier (*TDF*) come:$$V(j\omega)=\mathscr F[v(t)]=\int_{-\infty}^{+\infty}v(t)e^{-j\omega t}dt,\ e^{-j\omega t}\text{ nucleo della trasformata}$$
se esiste l'integrale.

## Antitrasformata di Fourier

$$v(t)=\mathscr F^{-1}[V(s)]={1\over2\pi j}\int_{-\infty}^{+\infty}V(j\omega)e^{j\omega t}d\omega$$
In questo caso, $v(t)$ è una somma di un'infinità *non numerabile* di sinusoidi.

## Trasformata di Laplace

Dato un segnale $v(t)$ definito per $t\geq0$ (o, equivalentemente, pensato nullo per $t<0$), definiamo la sua trasformata di Laplace come:$$V(s)=\mathscr L[v(t)]=\int_0^{+\infty}v(t)e^{-st}dt,\ s\in\mathbb C,\ \Re(s)\ne0$$
se l'integale esiste.

## Antitrasformata di Laplace

$$v(t)=\mathscr L^{-1}[V(s)]={1\over2\pi j}\int_{\alpha-j\infty}^{\alpha+j\infty}V(s)e^{st}ds$$
>**Nota**: va all'infinito solo sull'asse immaginario

---

## Proprietà della trasformata di Laplace

1. La trasformata di Laplace è un **operatore lineare**:$$\mathscr L[\alpha v_1(t)+\beta v_2(t)]=\alpha\mathscr L[v_1(t)]+\beta\mathscr L[v_2(t)]$$
2. **Trasformata di Laplace della derivata**:$$\mathscr L\bigg[{dv(t)\over dt}\bigg]=s\mathscr L[v(t)]-v(0)$$Nel caso in cui $v$ sia discontinuo, si sostituisce $v(0)$ con $v(0^-)$.
3. Conseguenza del punto `(2)`: **trasformata di Laplace dell'integrale**:$$\mathscr L\bigg[\int_0^tv(\tau)d\tau\bigg]={1\over s}\mathscr L[v(t)]$$
4. Trasformata di Laplace del **segnale ritardato**: vogliamo trovare $\mathscr L\big[v(t-\tau)\big]$. Possiamo procedere così:
    $$\begin{align}
\mathscr L\big[v(t-\tau)\big]&=\int_0^{+\infty}v(t-\tau)e^{-st}dt\end{align}$$sostituiamo ora $x=t-\tau\to t=x+\tau,\ dt=dx,\ t=0\implies x=-\tau,\ t\to\infty\implies x\to\infty$ e troviamo:$$\begin{align}\mathscr L\big[v(t-\tau)\big]&=\int_0^{+\infty}v(t-\tau)e^{-st}dt\\\
&=\int_{-\tau}^{+\infty}v(x)e^{-s(x+\tau)}dx&\text{ma }v(t)=0 \text{ per } t=-\tau<0\\\
&=\int_0^{+\infty}v(x)e^{-s(x+\tau)}dx\\\
&=e^{-s\tau}\int_0^{+\infty}v(x)e^{-sx}dx\\\
&=e^{-s\tau}\mathscr L[v(x)]\\\
&=e^{-s\tau}\mathscr L[v(t)]\end{align}$$

---

## Teorema del valore iniziale (*TVI*)

$$V(s)=\mathscr L[v(t)]\implies v(0)=\lim_{s\to\infty}sV(s)$$
>**Nota**: se $v$ è discontinua, allora vale la stessa equazione per $v(0^+)$.

## Teorema del valore finale (*TVF*)

$$V(s)=\mathscr L[v(t)]\implies\text{se }\exists\lim_{t\to\infty}v(t),\text{ allora }\lim_{t\to\infty}v(t)=\lim_{s\to0}sV(s)$$

---

## Trasformate di Laplace notevoli

| $v(t)$                   | $V(s)$                      |
| ------------------------ | --------------------------- |
| $\text{imp}(t)$          | $1$                         |
| $\text{sca}(t)$          | $\displaystyle{1\over s}$   |
| $\text{ram}(t)$          | $\displaystyle{1\over s^2}$ |
| $e^{at}\text{sca}(t)$    | $\displaystyle{1\over s-a}$ |
| $t^ne^{at}\text{sca}(t)$ | $\displaystyle{n!\over (s-a)^{n+1}}$                            |

---

## Antitrasformazione secondo Heaviside

Questo metodo di antitrasformazione vale per TDL razionali fratte, cioè:$$V(s)={N(s)\over D(s)}$$
dove $N,D$ sono polinomi in $s$ tali che $\deg(N)\leq\deg(D)$.
Le radici del polinomio $N(s)$ vengono detti **zeri** della TDL, mentre le radici del polinomio $D(s)$ vengono detti **poli** della TDL.
Il metodo generale segue tre passi:

1. Si fattorizza $D(s)$ che, così facendo, risulterà espresso come prodotto di termini del tipo:
	- $s-p$, dove $p$ è un polo reale semplice
	- $(s-p)^m$, dove $p$ è un polo reale multiplo
	- $p\in\mathbb C$, casi di poli complessi che non trattiamo
2. Si riscrive $V(s)$ usando la fattorizzazione di $D(s)$ trovata al passo precedente come segue:
	- Polo reale semplice: $${N(s)\over\ldots(s-p)\ldots}=\ldots+{\alpha\over s-p}+\ldots$$
	- Polo reale multiplo:$${N(s)\over\ldots(s-p)^m\ldots}=\ldots+{\alpha_1\over s-p}+{\alpha_2\over (s-p)^2}+ \ldots +{\alpha_m\over(s-p)^m}+\ldots$$
3. Si antitrasformano i fratti semplici trovati e si sommano
