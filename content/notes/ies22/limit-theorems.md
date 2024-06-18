---
title: "Teoremi limite"
draft: false
type: 'page'
toc: true
mathjax: true
---

---

## Media campionaria

Supponiamo di avere $n$ variabili aleatorie indipendenti ed identicamente distribuite $X_1, X_2, \ldots, X_n$.

Possiamo definire una variabile aleatoria speciale chiamata **media campionaria** nel seguente modo:

$$M_n = {X_1+X_2+\ldots+X_n\over n}$$

La media campionaria viene usata quando non si riesce a calcolare il valore atteso di una data variabile aleatoria.

> Se $X$ è l'altezza di uno studente pescato a caso da una popolazione, ipotizzando che la popolazione sia di $n$ persone, $M_n$ approssima bene $E[X]$?

Ipotizziamo di avere $X_1,X_2,\ldots,X_n$ variabili aleatorie indipendenti ed identicamente distribuite, con $E[X_i]=\mu<\infty$ e $\text{Var}[X_i]=\sigma^2<\infty$.

Calcoliamo $E[M_n]$ e $\text{Var}[M_n]$:

$$\begin{aligned}
E[M_n] &= {E[X_1+X_2+\ldots+X_n]\over n}\\\
&= \sum_{i=1}^n {E[X_i]\over n}\\\
&= {n\mu\over n}\\\
&= \mu\\\\\\
\text{Var}[M_n] &= {\text{Var}[X_1+X_2+\ldots+X_n]\over n^2}\\\
&= \sum_{i=1}^n {\text{Var}[X_i]\over n^2}\\\
&= {n\sigma^2\over n^2}\\\
&= {\sigma^2\over n}
\end{aligned}$$

Vogliamo provare che $\{M_n\} \xrightarrow{P} \mu$:

$$\begin{aligned}
0 &\le \lim_{n\to\infty} P(|M_n - \mu|\ge\epsilon)\\\
\text{(Chebyshev)} &\le \lim_{n\to\infty} {\text{Var}[M_n]\over\epsilon^2}\\\
&= \lim_{n\to\infty} {\sigma^2\over n\epsilon^2}\\\
&= 0
\end{aligned}$$

Allora possiamo affermare che:

$$M_n \xrightarrow{P} \mu = E[M_n] = E[X]$$ Questa espressione è nota come **legge debole dei grandi numeri** (o *Weak Law of Large Numbers*).

---

## Il problema del sondaggista ed il Central Limit Theorem

Sia $f$ la frazione di persone che soddisfa un evento $A$, il problema del sondaggista consiste nello **stimare** $f$.

Selezioniamo la persona $i$-esima nella popolazione sottoposta al sondaggio e poniamo il quesito del sondaggio: il risultato dell'intervista è una variabile aleatoria $X_i$, che ha le seguenti proprietà:

- $X_i$ sono variabili aleatorie indipendenti ed identicamente distribuite
- $E[X_i] = \mu = f$
- $\text{Var}[X_i] < \sigma^2 < \infty$

Considerando che la legge di probabilità di $X_i$ è:

$$X_i = \begin{cases}
1, &\text{ se l'evento }A \text{ si verifica per la persona } i\text{-esima}\\\
0, &\text{altrimenti}
\end{cases}$$

Allora la variabile aleatoria $X_i$ è una variabile aleatoria di Bernoulli con probabilità $f$:

$$X_i \sim \text{Bern}(f)$$

Possiamo allora specificare ancora che:

- $E[X_i] = f = P(X_i=1)$
- $\text{Var}[X_i] = f\cdot(1-f)$

Utilizziamo ora la media campionaria per stimare il valore di $f$:

$$M_n = {X_1+X_2+\ldots+X_n\over n} = \hat{f}$$

Il nostro obiettivo è quello di avere una grande accuratezza della stima con alta probabilità. Prendendo dei valori come esempio, potremmo dire:

$$P(|M_n-f|\le \underbrace{0.01}_\text{accuratezza}) \ge \underbrace{0.95}_\text{fiducia}$$

Dato che aumentare $n$ aumenta il livello di fiducia, troviamo il valore di $n$ minimo per cui riusciamo a raggiungere il 95% di fiducia, come scritto sopra. Per farlo, utilizziamo la [diseguaglianza di Chebyshev](../successions#diseguaglianza-di-chebyshev):

$$\begin{aligned}
P(|M_n-f|\ge 0.01) &\le {\text{Var}[M_n]\over 0.01^2}\\\
&= {\text{Var}[X_i]\over n\cdot 0.01^2}\\\
&= {f\cdot(1-f)\over n\cdot 0.01^2}\\\
&\le {{1\over4}\over n\cdot 0.01^2}\\\
&\stackrel{!}{\le} 1-0.95\\\
&= 0.05
\end{aligned}$$

Dall'equazione troviamo che:

$$n_\text{min} = 50\ 000$$

Questo numero è molto alto ma possiamo fare diverse cose per abbassarlo:

- È possibile diminuire il livello di fiducia (ma non ne vale la pena)
- È possibile abbassare l'accuratezza: passare al 3% comporterebbe un abbassamento di $n$ di un fattore 9
- È possibile utilizzare un'approssimazione migliore della disuguaglianza di Chebyshev per ridurre $n$

Procediamo con l'ultima soluzione. Definiamo una nuova variabile aleatoria $S_n = X_1+X_2+\ldots+X_n$ tale che:

$$M_n = {S_n\over n}$$

> Esiste una normalizzazione di $S_n$ tale che la varianza di quest'ultima non dipenda da $n$?

Possiamo procedere in questo modo:

$$\begin{aligned}
\text{Var}\bigg[{S_n\over a}\bigg] &= {\text{Var}[S_n]\over a^2}\\\
&= {n\sigma^2\over a^2}\\\
&= \sigma^2
\end{aligned}$$

L'equazione sopra è valida se e solo se $a = \sqrt n$.

Volendo trovare una media che non dipenda da $n$ invece, definiamo un'ulteriore variabile aleatoria $Z_n$ in questo modo:

$$Z_n = {S_n - E[S_n]\over \sqrt{n\sigma^2}}$$

In questo modo, abbiamo:

$$\begin{aligned}
E[Z_n] &= {E[S_n]-E[S_n]\over \sqrt{n\sigma^2}}\\\
&= 0\\\\\\
\text{Var}[Z_n] &= \text{Var}\bigg[{S_n\over\sqrt{n\sigma^2}}\bigg]\\\
&= {\text{Var}[S_n]\over n\sigma^2}\\\
&= 1
\end{aligned}$$

Per capire cosa succede quando $n\to\infty$, possiamo enunciare il **teorema fondamentale del limite**:

> **Teorema fondamentale del limite (o *Central Limit Theorem*)**
>
> Siano $X_i$ variabili aleatorie indipendenti ed identicamente distribuite con varianza finita e sia $Z_n$ una variabile aleatoria così definita:
> $$Z_n = {\sum_i X_i - n\mu\over\sqrt n\sigma}$$
> Sia inoltre $Z\sim N(0,1)$. Vale:
> $$F_{Z_n}(c) = P(Z_n\le c) \xrightarrow{n\to\infty} P(Z\le c) = \Phi(c), \ \forall c\in\mathbb R$$

> **Alcuni commenti**
>
> - È universale, perciò vale per qualunque legge di probabilità
> - È una scorciatoia per un calcolo approssimato ma spesso accurato
> - Con questo teorema è possibile costruire modelli fisici che si comportano in maniera Gaussiana
> - Il teorema ci dà informazioni sulla convergenza della cumulata, ma non sulla convergenza della legge di probabilità

Ora che conosciamo il Central Limit Theorem, proviamo ad applicarlo al problema del sondaggista. Vogliamo arrivare a:

$$P(|M_n-f|\ge0.01)\le0.05$$

Standardizziamo l'evento:

$$\begin{aligned}
|M_n - f| &\ge 0.01\\\
\bigg|{S_n\over n} - f \bigg| &\ge 0.01\\\
\bigg|{S_n - nf \over n}\bigg| &\ge 0.01\\\
\bigg|{S_n - nf \over \sqrt n\sigma}\bigg| &\ge {0.01\over\sigma}\sqrt{n}\\\
|Z_n|&\ge {0.01\over\sigma}\sqrt{n}
\end{aligned}$$

Sapendo che $\sigma^2\le{1\over4}$, possiamo dire che $\sigma\le{1\over2}$, perciò:

$$\begin{aligned}
P(|Z_n| \ge {0.01\sqrt n\over \sigma}) &\le P(|Z_n|\ge 0.02\sqrt n)\\\
\text{CLT}&\approx P(|Z|\ge 0.02\sqrt n)\\\
&= 2P(Z\ge0.02\sqrt n)\\\
&= 2\big(1-P(Z\le0.02\sqrt n)\big)\\\
&= 2\big(1-\Phi(0.02\sqrt n)\big)\\\
&\stackrel{!}{\le} 0.05
\end{aligned}$$

Risolvendo l'equazione sopra, troviamo:

$$n \ge 9604$$

Che è molto meno del numero minimo di persone trovato precedentemente. Possiamo anche dire che:

$$n_\text{min} = 9604$$

### Applicazione alla variabile aleatoria binomiale: il Teorema di DeMoivre-Laplace

Secondo il Central Limit Theorem, possiamo approssimare una variabile aleatoria binomiale $S_n\sim\text{Bin}(n,p)$ con una Gaussiana:

$${S_n - np\over \sqrt{np(1-p)}} \xrightarrow{n\to\infty} Z\sim N(0,1)$$

Quindi possiamo dire che:

$$S_n \approx \sqrt{np(1-p)}Z + np \sim N(np, np(1-p))$$

Il fatto che ogni binomiale possa essere ben approssimata tramite una Gaussiana è descritto dal teorema di **DeMoivre-Laplace** per la binomiale.
