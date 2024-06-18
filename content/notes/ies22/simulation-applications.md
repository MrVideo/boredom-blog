---
title: "Applicazioni della simulazione di esperimenti aleatori"
draft: false
type: 'page'
toc: true
mathjax: true
---

---

## Simulazione Monte Carlo

Si supponga di avere un esperimento aleatorio, che può essere ripetuto molte volte, ed un evento di interesse $A$.

[Abbiamo visto che](../limit-theorems#media-campionaria), per $n$ prove indipendenti, la media campionaria dei singoli esperimenti aleatori tende in probabilità al valore atteso degli stessi.

Supponiamo che $g(X)$ sia una qualsiasi statistica di una variabile aleatoria $X$. Vogliamo stimare il suo valore atteso:

$$E[g(X)] = \int_{-\infty}^\infty g(X)\cdot f_X(x)dx$$

Oltre alla stima tramite la media campionaria, possiamo anche applicare un algoritmo detto **Monte Carlo**:

1. Generare $X_i\sim f_X, \ i=1,\ldots,n$ in maniera indipendente
2. Calcolare $\hat{G_n} = {1\over n} \sum_{i=1}^n g(X_i)$

Si dice allora che $\hat{G_n}$ è la stima Monte Carlo di $E[g(X)]$.

L'errore relativo di stima dell'algoritmo Monte Carlo è pari a:

$${1\over\sqrt{n}}\sqrt{1-P(A)\over P(A)}$$

Un difetto di questo algoritmo sta nella difficoltà che ha nello stimare eventi rari, dato che per $n\to\infty$, $P(A)\to0$.

---

## Importance Sampling

L'idea dietro all'Importance Sampling è che si vuole far accadere l'evento di interesse $A$ con una probabilità maggiore rispetto a quella originale. Per fare ciò, è necessario modificare l'esperimento aleatorio in modo che $A$ si verifichi più spesso.

Ipotizziamo di avere il seguente spazio campionario:

![](../images/Pasted%20image%2020230806174901.png)

Se nell'esperimento originale $X$ c'è una probabilità che $A$ accada pari a:

$$p_X(A) = p_X(\omega_1) + p_X(\omega_2) + p_X(\omega_3)$$

Possiamo eseguire un nuovo esperimento $Y$:

$$p_Y(A) = p_Y(\omega_1) + p_Y(\omega_2) + p_Y(\omega_3)$$

Di cui possiamo costruire la legge di probabilità in modo tale che $p_Y(A) > p_X(A)$. Introduciamo una funzione indicatrice $\mathbb 1(Y\in A)$ definita così:

$$\mathbb 1(Y\in A) = \begin{cases}
1, &Y\in A\\\
0, &Y\not\in A
\end{cases}$$

Allora possiamo concludere che $\mathbb 1(Y\in A)\sim\text{Bern}(p_Y(A))$. Allora:

$$\begin{aligned}
p_Y(A) &= p_Y(\omega_1) + p_Y(\omega_2) + p_Y(\omega_3)\\\
&= P(Y\in A)\\\
&= E \big[\mathbb 1(Y\in A) \big]
\end{aligned}$$

Calcoliamo ora:

$$\begin{aligned}
p_X(A) &= E \big[\mathbb 1(X\in A) \big]\\\
&= \int_{\mathbb R}\mathbb 1(x\in A)\cdot f_X(x)dx\\\
&= \int_{\mathbb R}{\mathbb 1(x\in A)\cdot {f_X(x)\over f_Y(y)}}\cdot f_Y(y)dx, &\text{se }f_Y(y)>0 \ \forall x\in \text{supp}(f_X)\\\
&= E\bigg[{\mathbb 1(Y\in A)\cdot {f_X(x)\over f_Y(y)}} \bigg]
\end{aligned}$$

Riassumiamo ora i passaggi dell'algoritmo di Importance Sampling:

1. Generare $Y_i \text{ i.i.d. }\sim f_Y$
2. Calcolo $\hat p_X(A) = 1/n \sum_{i=1}^n \mathbb 1(Y_1\in A)\cdot {f_X(Y_i)\over f_Y(Y_i)}$

Il fattore ${f_X(Y_i)\over f_Y(Y_i)}$ è detto **Importance Weight**. È necessario scegliere $f_Y$ in modo tale che $p_Y(A) \gg p_X(A)$.

Per abbassare la varianza della stima, inoltre, è necessario scegliere $Y$ in modo tale che:

$$f_Y(y) \approx \mathbb 1(x\in A)\cdot f_X(x)$$

> **Esempio di applicazione dell'Importance Sampling**
>
> Ipotizziamo di avere una variabile aleatoria gaussiana $X\sim N(0,1)$ e di voler stimare $P(X>5)$.
> Tramite MATLAB, possiamo calcolare che $P(X>5) \approx 2.86\cdot 10^{-7}$, constatando così che stiamo analizzando la probabilità di un evento molto raro.
> Volendo avere un errore relativo di stima target pari a $10^{-2}$, avremmo bisogno di $n \ge 3.48\cdot10^{10}$ campioni.
> Proviamo, tramite l'Importance Sampling, a modificare l'esperimento aleatorio: passiamo da $X$ a $Y$ in modo che $f_Y(x)\approx\mathbb 1(x>5)\cdot f_X(x)$.
> Ad esempio, possiamo scegliere:
> $$f_Y(x) = \begin{cases}
> e^{-(x-5)}, &x>5\\\
> 0, &\text{altrimenti}
> \end{cases}$$
> Calcoliamo allora l'Importance Weight:
> $${f_X(x)\over f_Y(x)} = {1\over\sqrt{2\pi}}e^{-x^2/2+x-5}$$
> Possiamo ora scrivere l'algoritmo di Importance Sampling per calcolare $P(X>5)$:
> 1. Genero $Y_i=T_i+5$, dove $T_i \text{ i.i.d. } \sim\text{Exp}(1)$
> 2. Calcolo:
    $$\hat p_X(A) = {1\over n}\sum_{i=1}^n \mathbb 1(Y_i>5)\cdot {1\over\sqrt{2\pi}}e^{-x^2/2+x-5}$$
> Vediamo ora se abbiamo effettivamente ridotto la varianza della stima:
> $$\begin{aligned}
> \text{Var}[\hat{p}_X(A)] &= {1\over n}\bigg\\{E\bigg[\mathbb 1(X\in A)\cdot{f_X(X)\over f_Y(X)} -\big(p_X(A)\big)^2 \bigg]\bigg\\}\\\
> &\le {1\over n}\bigg\\{ {E \bigg[\mathbb 1(X\in A)\bigg]}{1\over\sqrt{2\pi}} e^{-25/2} - \big(p_X(A)\big)^2 \bigg\\} \\\
> &= {1\over n}p_X(A)\bigg({1\over\sqrt{2\pi}}e^{-25/2}-p_X(A) \bigg)
> \end{aligned}$$
> Calcoliamo infine l'errore relativo di stima:
> $$\begin{aligned}
> \sqrt{\text{Var}[\hat p_X(A)]\over p_X^2(A)} &\le \sqrt{{1\over n}\bigg({e^{-25/2}\over \sqrt{2\pi}p_X(A)}-1 \bigg)}\\\
> &\approx \sqrt{{1\over n}\cdot 1.915}\\\
> &\stackrel{!}{\le}0.01\\\
> &\implies n \approx 1.9\cdot 10^5
> \end{aligned}$$
> Utilizzando quindi il valore trovato con MATLAB, vediamo che abbiamo abbassato il numero di campioni necessari di cinque ordini di grandezza con l'Importance Sampling.

L'algoritmo di Importance Sampling ha diversi vantaggi:

- È un metodo di facile applicazione
- Abbassa sensibilmente il valore di $n$ (o migliora semplicemente l'errore di stima)

Ha anche uno svantaggio: bisogna trovare un esperimento aleatorio ausiliario da cui sia semplice campionare e per cui $P(Y\in A)$ sia grande.

---

## Calcolo di integrali

È possibile applicare la stima di Monte Carlo per calcolare degli integrali particolarmente complessi.

Prendiamo ad esempio l'integrale:

$$I={1\over\pi}\int_0^\pi e^{\cos x}dx$$

Proviamo a risolverlo stimandolo: scegliamo $X\sim U[0,\pi]$, che ha legge di probabilità:

$$f_X(x) = \begin{cases}
{1\over\pi}, &0<x<\pi\\\
0,&\text{altrimenti}
\end{cases}$$

Troviamo in questo caso:

$$\begin{aligned}
I &= \cancel{1\over\pi}\int_0^\pi {e^{\cos x}\over \cancel{1/\pi}}\cdot {1\over\pi}dx\\\
&= E\big[e^{\cos X}\big]
\end{aligned}$$

Trovato il valore atteso, possiamo procedere con la stima Monte Carlo.

L'algoritmo per risolvere un integrale tramite la stima Monte Carlo è riassumibile in due passi:

1. Genero $X_1,X_2,\ldots,X_n \text{ i.i.d. }$ in modo da facilitare il calcolo dell'integrale
2. Calcolo la stima dell'integrale $\hat I$ come media campionaria
