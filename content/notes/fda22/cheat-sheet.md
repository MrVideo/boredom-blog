---
title: 'Cheat sheet'
draft: false
type: 'page'
toc: true
mathjax: true
---

---

## Download as PDF

You can download this note as a PDF by clicking [here](../cheat-sheet.pdf).

---

## Sistemi dinamici

- Forma a tempo continuo:$$\begin{cases}
\dot{x}(t)=f(x(t), u(t),t)\\\
y(t)=g(x(t),u(t),t)
\end{cases}$$
- Forma a tempo discreto:$$\begin{cases}x(k)=f(x(k-1), u(k-1), k)\\\y(k)=g(x(k), u(k), t)\end{cases}$$
- Proprietà:
	1. $f, g$ sono **lineari** in $x, u \iff$ sistema dinamico **lineare** (indicato con **L**)
	2. $f=f(x,u), g=g(x,u)\iff$ sistema dinamico **tempo-invariante** (indicato con **TI**, anche detto *stazionario*)
	3. $g=g(x,t)\iff$ sistema dinamico **strettamente proprio** (indicato con **SP**)

---

## Linearizzazione

Un sistema non lineare si linearizza nell'intorno di un equilibrio secondo questo schema:

$$\begin{align}
A&=\begin{bmatrix}
{\partial\over\partial x_1}f(x,u) & {\partial\over\partial x_2}f(x,u)\\\
{\partial\over\partial x_1}f(x,u) & {\partial\over\partial x_2}f(x,u)
\end{bmatrix},\\\
b&=\begin{bmatrix}
{\partial\over\partial u}f(x,u)\\\
{\partial\over\partial u}f(x,u)
\end{bmatrix},\\\
c&=\begin{bmatrix}
{\partial\over\partial x_1}g(x,u) & {\partial\over\partial x_2}g(x,u)
\end{bmatrix},\\\
d&={\partial\over\partial u}g(x,u)
\end{align}$$

---

## Movimenti

- Tempo continuo:
    $$\begin{align}
x(t) &= {e^{At} x(0)} + {\int_0^t e^{A(t-\tau)}bu(\tau)d\tau}\\\
y(t) &= {ce^{At}x(0)} + {\int_0^te^{A(t-\tau)}bu(\tau)d\tau+du(t)}
\end{align}$$
- Tempo discreto:
    $$\begin{align}
x(k)&={A^kx(0)}+{\sum_{l=0}^{k-1}A^{k-l-1}bu(l)}\\\
y(k)&={cA^kx(0)}+{c\sum_{l=0}^{k-1}A^{k-l-1}bu(l)+du(k)}
\end{align}$$

---

## Stabilità

- Negli equilibri:
	1. **Equilibrio stabile**: l'equilibrio è stabile (*S*) se:$$\forall\epsilon>0,\exists\delta>0:||x(0)-\overline x||<\delta\implies||x(t)-\overline x||<\epsilon,\forall t\geq0$$
	2. **Equilibrio asintoticamente stabile**: l'equilibrio è asintoticamente stabile (*AS*) se è stabile e:$$||x(t)-\overline x||\to0\text{ per } t\to+\infty$$
	3. **Equilibrio instabile**: l'equilibrio è instabile (*I*) se non viene rispettata nessuna delle condizioni precedenti.
- Nella matrice $A$:
	- Tutti gli autovalori di $A$ hanno $\Re<0$ $\iff$ il sistema è **AS**
	- Almeno un autovalore di $A$ ha $\Re>0$ $\implies$ il sistema è **I**
	- Tutti gli autovalori di $A$ hanno $\Re\leq0$ ed almeno uno ha $\Re=0$ $\implies$ il sistema è o **I** o **S**, ma non può essere **AS**
- Criteri di stabilità:
	1. $\det A=\pi(s_i)$. $\det A=0\implies\exists s_i=0\implies$ sistema **non AS**
	2. $\text{Tr } A=\sum s_i = \sum\Re(s_i)$. $\text{Tr }A>0\implies\exists s_i:\Re(s_i)>0\implies$ sistema **I**
	3. $\Re(s_i)<0,\forall i$ (sistema **AS**) $\implies$ i coefficienti di $\pi(s)$ sono tutti concordi e non nulli
	4. Criterio di Routh:
		1. Tabella di Routh:$$\begin{cases}\begin{matrix}a_0&a_2&\ldots&a_{n-1}&\text{oppure}&a_n\\\a_1&a_3&\ldots&a_n&&0\\\h_1&h_2&\ldots&\ldots&\ldots&\ldots\\\q_1&q_2&\ldots&\ldots&\ldots&\ldots\\\w_1&w_2&\ldots&\ldots&\ldots&\ldots\end{matrix}&&n+1\text{ righe}\end{cases}$$
		2. Calcolo elementi della tabella di Routh:$$w_i=-{1\over q_1}\det\begin{bmatrix}h_1&h_{i+1}\\\q_1&q_{i+1}\end{bmatrix}$$
		3. Criterio di Routh: un SD con PC $\pi(s)$ è **AS** $\iff$ **tutti gli elementi della prima colonna della tabella di Routh sono concordi**

---

## Trasformate di Laplace

- Teorema del valore iniziale:$$V(s)=\mathscr L[v(t)]\implies v(0)=\lim_{s\to\infty}sV(s)$$
- Teorema del valore finale:$$V(s)=\mathscr L[v(t)]\implies\text{se }\exists\lim_{t\to\infty}v(t),\text{ allora }\lim_{t\to\infty}v(t)=\lim_{s\to0}sV(s)$$
- Trasformate di Laplace notevoli:

| $v(t)$                   | $V(s)$                      |
| ------------------------ | --------------------------- |
| $\text{imp}(t)$          | $1$                         |
| $\text{sca}(t)$          | $\displaystyle{1\over s}$   |
| $\text{ram}(t)$          | $\displaystyle{1\over s^2}$ |
| $e^{at}\text{sca}(t)$    | $\displaystyle{1\over s-a}$ |
| $t^ne^{at}\text{sca}(t)$ | $\displaystyle{n!\over (s-a)^{n+1}}$                            |

---

## Funzione di trasferimento

$$G(s)=c(s\mathbb I-A)^{-1}b+d$$

---

## Funzioni di trasferimento di interesse nel progetto di un regolatore in retroazione

$$
\begin{align}
L(s) &= R(s)P(s)&\text{Funzione di trasferimento d'anello aperto}\\\
T(s) &= {L(s)\over 1+L(s)}&\text{Funzione di sensitività complementare}\\\
S(s) &= {1\over1+L(s)}&\text{Funzione di sensitività}\\\
Q(s) &= {R(s)\over1+L(s)}&\text{Funzione di sensitività del controllo}
\end{align}
$$

---

## Raggiungibilità ed osservabilità

- Un sistema è raggiungibile se e solo se:$$det(\overbrace{\begin{bmatrix}b&Ab&A^2b&\ldots&A^{n-1}b\end{bmatrix}}^{M_R})\ne0$$
- Un sistema è osservabile se e solo se:$$det(\overbrace{\begin{bmatrix}c^T&A^Tc^T&(A^2)^Tc^T&\ldots&(A^{n-1})^Tc^T\end{bmatrix}}^{M_O})\ne0$$

### Forma canonica di raggiungibilità

$$A=\begin{bmatrix}
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

### Forma canonica di osservabilità

$$A=\begin{bmatrix}
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

---

## Compensazione

Il compensatore ideale ha funzione di trasferimento:$$C_{\text{id}}=-{H\over MP}$$
ma spesso può non essere realizzabile, o perché ha più zeri che poli, o perché ha poli con parte reale positiva. In tal caso, si parte dal compensatore ideale e si aggiungono poli o si tolgono zeri per creare il compensatore reale $C_\text{r}$.

---

## Gradi di libertà

- Un grado di libertà:
    $${u\over w}=-{u\over y}=R$$
- Due gradi di libertà:
    $$\begin{align}
{u\over w} &= R_{FF}R_{FB}\\\
{u\over y} &= -R_{FB}
\end{align}$$

---

## Regolatori PID

- Legge di controllo ideale:$$u(t)=k_Pe(t)+k_I\int_0^te(\tau)d\tau+k_D{de(t)\over dt}$$
- Forma ISA reale a un grado di libertà:$$R(s) = k\bigg(1+{1\over sT_I}+{sT_D\over1+{sT_D\over N}}\bigg)$$
- Forma ISA reale a due gradi di libertà:$$U(s)=k\bigg[bw-Y+{1\over sT_I}(w-Y)+{sT_D\over1+{sT_D\over N}}(cw-Y)\bigg]$$
- Ruoli di ciascuna azione:
	- Azione proporzionale: risposta pronta alla variazione dell'errore
	- Azione integrale: errore nullo a regime
	- Azione derivativa: anticipazione della variazione dell'errore
- PI e PID in pratica:
	- PI: uno zero e un polo nell'origine
	- PID: due zeri e due poli, di cui uno nell'origine
---

## Metodi di discretizzazione
- Eulero esplicito:$$s = {z-1\over T_S}$$
- Eulero implicito:$$s={z-1\over zT_S}$$
- Tustin:$$s={2\over T}{z-1\over z+1}$$

---

## Criteri per la scelta del tempo di campionamento

1. Pongo:$$\omega_S=k\omega_C,\ k\in[10,50]$$
2. Più $|L(j\omega_N)|$ è piccolo, meno c'è aliasing. Si può trovare perciò $\omega_N$ e, di conseguenza, $\omega_S$ dal diagramma di Bode del modulo della risposta in frequenza della funzione di trasferimento d'anello.
3. Nella discretizzazione, il margine di fase $\varphi_m$ si riduce di:
	- $\Delta\varphi_m = {1\over 2}\omega_CT_S$ se il ritardo di calcolo è trascurabile
	- $\Delta\varphi_m = {3\over 2}\omega_CT_S$ se il ritardo di calcolo non è trascurabile
4. Si pone:$$T_S\ll{1\over 5}T$$dove $T$ è la minima costante di tempo del regolatore.

---

## Tempo di assestamento

Il tempo di assestamento di un sistema dinamico è calcolato come:$$
T_{\text{assestamento}}\approx5T\approx5{1\over\omega_C}$$
dove $T$ è la costante di tempo dominante del sistema.

---

## Controllo di sistemi instabili

Se un processo $P(s)$ ha un polo con $\Re>0$, posso chiuderlo in un anello per renderlo asintoticamente stabile con un regolatore $R_1(s)$ per poi chiudere un altro anello intorno a questo sistema con un regolatore $R_2(s)$ al fine di rispettare le specifiche di progetto.

$R_1(s)$ è spesso nella forma puramente proporzionale:

$$R_1(s) = k$$

ma se ciò non bastasse si può usare uno sfasatore puro:

$$R_1(s) = k{1+\tau s\over 1+Ts}$$

dove lo zero del regolatore va a cancellare uno dei poli con $\Re<0$ dell'anello interno, mentre il polo del regolatore lo sostituisce con uno con costante di tempo minore di quella del polo con $\Re>0$.

---

## Criterio di Nyquist

>Sia $L(s)$ una funzione di trasferimento d'anello aperto relativa ad un sistema dinamico lineare tempo invariante.
>Sia $p$ il numero di poli di $L(s)$ con parte reale maggiore di zero ed $N$ il numero di giri compiuti dal diagramma di Nyquist della funzione d'anello $L(s)$ attorno al punto $-1$, conteggiati positivamente se compiuti in senso antiorario e negativamente in senso orario.
>Se il diagramma passa per il punto $-1$, il valore di $N$ non è ben definito.
>Allora, condizione necessaria e sufficiente perché il sistema retroazionato con funzione di trasferimento ${L(s)\over 1+L(s)}$ sia asintoticamente stabile è che $N$ sia ben definito e risulti $N=p$.

---

## Criterio di Bode

>Sia $L(s)$ una funzione di trasferimento d'anello aperto relativa ad un sistema dinamico lineare tempo invariante.
>Sia $p$ il numero di poli di $L(s)$ con parte reale maggiore di zero.
>Dato che $p=0$ ed il diagramma di Bode del modulo di $L(s)$ tagli l'asse $0\text{ dB}$ una volta soltanto, dall'alto verso il basso, condizione necessaria e sufficiente perché il sistema retroazionato con funzione di trasferimento ${L(s)\over 1+L(s)}$ sia asintoticamente stabile è che, detto $\mu_L$ il guadagno di $L$ e $\varphi_L$ il margine di fase di $L$, essi siano strettamente maggiori di zero.

---

## Risposta esponenziale

Dato un SD LTI SISO:

$$\begin{cases}
\dot x = Ax+bu\\\
y = cx+du
\end{cases}$$

posto in generale $u(t)=Ue^{\lambda t}, t\geq 0$, se $\lambda$ non è un autovalore di $A$, allora:

$$\exists!x(0)=(\lambda\mathbb I-A)^{-1}b:x(t)=(\lambda\mathbb I-A)^{-1}bUe^{\lambda t}$$

e quindi:

$$y(t)=\big[c(\lambda\mathbb I-A)^{-1}b+d\big]Ue^{\lambda t}=G(\lambda)Ue^{\lambda t}, t\geq 0$$

Se il sistema è anche asintoticamente stabile, allora:

$$\forall x(0), y(t)\to G(\lambda)Ue^{\lambda t}, t\to\infty$$

Se invece $G(\lambda)=0$ allora, con lo stesso $x(0)$, si ha $y(t)=0, t\geq0$. Questa proprietà è detta *proprietà bloccante degli zeri*.

---

## Teorema fondamentale della risposta in frequenza

Dato il sistema dinamico lineare tempo-invariante single-input single-output:

$$\begin{cases}
\dot x = Ax+bu\\\
y = cx+bu
\end{cases}$$

detta $G(s)$ la sua funzione di trasferimento ed applicatogli l'ingresso:

$$u(t)=U\sin(\omega t)$$

per $t\geq 0$:

1. Se $\mp j\omega$ non sono autovalori di $A$, allora esiste un unico stato iniziale $x(0)$ tale che:

$$y(t)=|G(j\omega)|U\sin\big[\omega t+\enclose{phasorangle}{G(j\omega)}\big], t\geq 0$$

2. Se, inoltre, il sistema dinamico è asintoticamente stabile, allora:

$$\forall x(0), y(t)\to|G(j\omega)U\sin\big[\omega t +\enclose{phasorangle}{G(j\omega)}\big], t\to+\infty$$
