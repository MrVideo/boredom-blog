---
title: "Successioni di variabili aleatorie"
draft: false
type: 'page'
toc: true
mathjax: true
---

---

## Diseguaglianza di Markov

Supponiamo di avere una variabile aleatoria $X\ge0$. Proviamo a calcolarne il valore atteso:

$$\begin{aligned}
E[X] &= \sum_{x\ge0}x\cdot p_X(x)\\\
&\ge \sum_{x\ge a}x\cdot p_X(x)\\\
&\ge \sum_{x\ge a}a\cdot p_X(x)\\\
&= a\sum_{x\ge a}p_X(x)\\\
&= a\cdot P(X\ge a),\ \forall a\ge0
\end{aligned}$$

Otteniamo così la diseguaglianza di Markov, che afferma che per ogni variabile aleatoria non nulla:

$$E[X] \ge a P(X\ge a)$$

In pratica, questa disuguaglianza afferma che se il valore atteso di una variabile aleatoria è piccolo, allora la probabilità che quella variabile aleatoria sia maggiore di un certo valore $a$ è a sua volta piccola.

## Diseguaglianza di Chebyshev

A partire dalla diseguaglianza di Markov si può formulare la diseguaglianza di Chebyshev, che afferma che:

$$\text{Var}[X] \ge a^2P\big(|X-E[X]| \ge a\big)$$

In pratica, questa disuguaglianza afferma che se la varianza di una variabile aleatoria è piccola, allora essa non si discosta molto dal suo baricentro, che è il suo valore atteso.

Esiste anche una formulazione alternativa della disuguaglianza di Chebyshev: scegliendo $a=k\cdot\sigma_X$, possiamo scrivere:

$$P\big(|X-E[X]|\ge k\sigma_X \big) \le {1\over k^2}$$

Questa espressione afferma che non si può essere troppo lontani dal baricentro $E[X]$ in termini di multipli della deviazione standard $\sigma_X$.

---

## Convergenza in probabilità

Ipotizziamo di avere una successione di variabili aleatorie $\{A_n\}$ ed un numero puro $a$.

Possiamo dire che $\{A_n\}$ converge in probabilità ad $a$ se:

$$\lim_{n\to\infty} P(|A_n - a|\ge\epsilon)=0, \ \forall\epsilon >0$$

È possibile scrivere in modo più compatto l'espressione sopra così:

$$A_n \xrightarrow{P} a$$

Facciamo un esempio per chiarire meglio questo concetto: prendiamo una variabile aleatoria $Y_n$ tale che:

$$Y_n = \begin{cases}
0, &\text{con probabilità } 1-{1\over n}\\\
n, &\text{con probabilità } {1\over n}
\end{cases}$$

Cerchiamo di determinare se $Y_n$ converge in probabilità.

Ipotizziamo che converga al valore $a=0$ e verifichiamolo:

$$\begin{aligned}
\lim_{n\to\infty} P(|Y_n-0|\ge\epsilon) &= \lim_{n\to\infty} P(Y_n\ge\epsilon)\\\
&= \lim_{n\to\infty}{1\over n}\\\
&= 0
\end{aligned}$$

Allora possiamo dire che $Y_n \xrightarrow{P} 0$.

La convergenza in probabilità viene anche detta *convergenza debole*, poiché non dice nulla sulla convergenza delle statistiche di una variabile aleatoria. Prendendo in considerazione la variabile aleatoria precedente infatti, calcolandone il valore atteso, troviamo:

$$E[Y_n] = 1, \ \forall n$$

Come si vede, nonostante la variabile aleatoria $Y_n$ converga in probabilità a zero, il suo valore atteso non fa lo stesso.
