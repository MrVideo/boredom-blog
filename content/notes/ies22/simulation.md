---
title: "Simulazione di esperimenti aleatori"
draft: false
type: 'page'
toc: true
mathjax: true
---

---

## Cosa significa simulare

> Dato un evento $A$ ed un esperimento aleatorio, qual è la probabilità dell'evento $A$?

Per rispondere a questa domanda, si potrebbe ripetere tante volte l'esperimento aleatorio e registrare tutte le volte che si verifica l'evento $A$.

Ipotizziamo di effettuare $n$ prove indipendenti e di registrare per ognuna una variabile aleatoria $X_i$. $X_i$ sono variabili aleatorie indipendenti ed identicamente distribuite definite come:

$$X_i = \begin{cases}
1, &\text{se }A\text{ si verifica}\\\
0, &\text{altrimenti}
\end{cases}$$

Possiamo dire allora che $X_i\sim\text{Bern}\big(P(A)\big)$.

Utilizziamo la media campionaria per stimare la probabilità che l'evento $A$ si verifichi:

$$M_n = {1\over n}\sum_{i=1}^n X_i$$

Avevamo dimostrato che:

$$M_n \xrightarrow{P} E[M_n] = P(A)$$

Perciò, per la [legge debole dei grandi numeri](../limit-theorems#media-campionaria), la media campionaria è una buona stima di $P(A)$ per $n$ grande.

## Come controllare l'errore di stima

Esistono diversi modi di controllare l'errore di stima.

Un metodo può essere quello di costruire un intervallo fiduciario, in modo analogo al [problema del sondaggista](../limit-theorems#il-problema-del-sondaggista-ed-il-central-limit-theorem):

$$P\big(|M_n-P(A)|>\epsilon\big)<0.05$$

Un altro metodo può essere quello di calcolare l'errore quadratico medio di stima:

$$\begin{aligned}
\text{MSE}\_{n} &= E\big[\big(M_n - P(A) \big)^2 \big]\\\
&= E\bigg[\bigg({1\over n} \sum_{i=1}^n X_i - E\bigg[{1\over n}\sum_{i=1}^n X_i \bigg] \bigg)^2 \bigg]\\\
&=\text{Var}\bigg[{1\over n}\sum_{i=1}^n X_i \bigg]\\\
&= {1\over n^2}\sum_{i=1}^n \text{Var}[X_i]\\\
&= {P(A)(1-P(A))\over n}
\end{aligned}$$

In questo caso, la varianza di stima dipende dalla quantità da stimare, come nel [problema del sondaggista](../limit-theorems#il-problema-del-sondaggista-ed-il-central-limit-theorem).

Possiamo calcolare l'errore relativo di stima come:

$${\sqrt{\text{Var}[M_n]}\over P(A)} = {1\over\sqrt{n}} \sqrt{1-P(A)\over P(A)}$$

Fissando un errore relativo di stima target $\epsilon$, imponiamo:

$$\epsilon \stackrel{!}{>} {1\over\sqrt{n}} \sqrt{1-P(A)\over P(A)}$$

Da questa espressione, possiamo trarre due conclusioni:

- Se $P(A)\to1$, $n$ è piccolo
- Se $P(A)\to0$, $n$ è molto grande e stiamo stimando un evento raro

> **Perché è utile simulare?**
>
> Grazie ai calcolatori, è più veloce simulare molti esperimenti aleatori che farli direttamente nel mondo reale. A volte può succedere invece il contrario: è più veloce effettuare l'esperimento nel mondo reale, ma è troppo costoso, quindi si sceglie la simulazione come misura di riduzione costi.
> Le simulazioni possono inoltre essere utilizzate per la ricerca scientifica o anche per validare un calcolo teorico.

## Generatore di variabili aleatorie uniformi

Simulare non significa che generare numeri casuali.

Per esempio, avere a disposizione una sequenza pseudo-casuale di bit 0 ed 1 ci permette di generare numeri $X\sim U[0,1]$ interpretando i bit nel seguente modo:

$$x = b_1\cdot 2^{-1} + b_2\cdot 2^{-2} + b_3\cdot 2^{-3} + b_4\cdot 2^{-4} + b_5\cdot 2$$

---

## Campionamento

Campionare significa generare realizzazioni a partire da una variabile aleatoria $X \sim f_X$ con legge nota a priori.

### Campionare da distribuzioni continue: metodo della cumulata inversa

Supponiamo di avere a disposizione un generatore uniforme che come output fornisce $U\sim U[0,1]$. Noi vogliamo trasformare questa variabile aleatoria tramite una funzione deterministica $g$ in modo tale da ottenere la variabile aleatoria $X$ descritta in precedenza. In pratica vogliamo:

$$g(U) = X \sim f_X$$

Supponiamo di voler campionare la variabile aleatoria $X \sim U[a,b]$. Per farlo, possiamo definire $X$ come segue:

$$X = g(U) = a + (b-a)U$$

Possiamo generalizzare questo procedimento partendo dalla cumulata della variabile aleatoria $X$:

$$\begin{aligned}
F_X(x) &= P(X\le x)\\\
&= P(g(U) \le x) &g\text{ invertibile e monotona crescente}\\\
&= P(g^{-1}(g(U)) \le g^{-1}(x))\\\
&= P(U \le g^{-1}(x))\\\
&= F_U(g^{-1}(x))\\\
&= g^{-1}(x) &\text{per } g^{-1}(x)\in[0,1]
\end{aligned}$$

Noi sappiamo che $F_X$ è non decrescente e perciò invertibile. Per questo, possiamo concludere che:

$$g(u) = F_X^{-1}(u),\ \forall u\in[0,1]$$

Detto questo, possiamo dire anche che $g(U) = F_X^{-1}(U)$, ma noi sappiamo che $X=g(U)$, quindi $X = F_X^{-1}(U)$. Otteniamo così che $X$ segue la legge $f_X$, come ci eravamo prefissati.

Questo metodo viene chiamato **metodo della cumulata inversa**.

Questo metodo ha diversi vantaggi:

- Se la cumulata $F_X$ è nota ed è semplice da invertire, l'applicazione del metodo è immediata
- Per ogni campione $U$ generato indipendentemente dagli altri, otteniamo un campione $X$ indipendente, quindi l'efficienza dell'algoritmo è del 100%

Ha anche degli svantaggi però:

- Talvolta, $F_X$ non è nota direttamente
- Talvolta, $F_X$ è nota ma non è semplice da invertire
- È difficile trattare casi con variabili aleatorie congiunte tramite questo metodo

#### Campionamento da una distribuzione discreta

È possibile riadattare il metodo della cumulata inversa per le distribuzioni discrete:

1. Generare $U\sim U[0,1]$
2. Assegnare:$$X = \begin{cases}x_1, & 0\le U\le P_X(x_1)\\\ x_2, & P_X(x_1) \le U \le P_X(x_2)\\\ \vdots &\vdots\\\ x_n,&P_X(x_{n-1})\le U \le P_X(x_n) = 1\end{cases}$$

### Metodo di *acceptance-rejection*

Vediamo ora un altro metodo di campionamento.

Supponiamo di avere una variabile aleatoria $X\sim f_X$ la cui legge di probabilità $f_X$ è nota. Diciamo per esempio che la legge di probabilità di $X$ sia quella disegnata qui sotto:

![](../images/Pasted%20image%2020230806174634.png)

Scegliamo un valore $m$ tale che $m \ge \max f_X(x), \ x\in\mathbb R$. Adesso "lanciamo" dei punti distribuiti uniformemente nella regione rettangolare $[0,10] \times [0,m]$. Finito questo processo, teniamo soltanto i punti caduti sotto la curva $f_X$. Questa viene chiamata **condizione di acceptance**.

Possiamo dimostrare che **le ascisse dei punti accettati sono distribuiti come** $f_X$.

Riassumiamo l'algoritmo di acceptance-rejection:

1. Generare $U\sim U[0,10]$
2. Generare $U'\sim U[0,1]$ tale che $U\perp U'$
3. Accettare e porre $X=U$ se $mU'\le f_X(U)$; altrimenti tornare al punto 1

Generalizziamo ora questo metodo: per "coprire" tutta la legge $f_X$ è necessario trovare un valore $m\in\mathbb R^+$ tale che:

$$mf_Y(x)\ge f_X(x), \ \forall x\in\mathbb R$$

L'algoritmo generalizzato del metodo di acceptance-rejection è:

1. Generare $Y\sim f_Y$ e $U'\sim U[0,1]$, con $Y\perp U'$
2. Accettare e porre $X=Y$ se $mf_Y(Y)\cdot U' \le f_X(Y)$; altrimenti torno al punto 1

Possiamo considerare questo algoritmo come un [processo di Bernoulli](14.%20Processi%20di%20Bernoulli.md), dato che ogni punto può essere accettato o rifiutato.

In questo caso, qual è il tempo medio al primo successo?

Introduciamo la variabile aleatoria $N$ come il numero di prove fino alla generazione di un $X$ valido (ossia fino ad un'accettazione). Essendo questo il tempo al primo successo in un processo di Bernoulli, possiamo dire che $N\sim\text{Geom}(t)$, con $t$ probabilità di acceptance:

$$\begin{aligned}
t &= P\big(mf_Y(Y)\cdot U' \le f_X(Y) \big)\\\
&= P\bigg(U'\le {f_X(Y)\over mf_Y(Y)} \bigg)
\end{aligned}$$

Applicando la [legge delle probabilità totali](../axioms#assiomi), troviamo:

$$\begin{aligned}
P\bigg(U'\le {f_X(Y)\over mf_Y(Y)} \bigg) &= \int_{\mathbb R} P\bigg(U'\le {f_X(Y)\over mf_Y(Y)}\bigg|Y=y \bigg)f_Y(y)dy\\\
&= \int_{\mathbb R} P\bigg(U'\le {f_X(y)\over mf_Y(y)}\bigg|Y=y \bigg)f_Y(y)dy\\\
U' \perp Y &= \int_{\mathbb R} P\bigg(U'\le {f_X(y)\over mf_Y(y)} \bigg)f_Y(y)dy\\\
&= \int_{\mathbb R} {f_X(y)\over m\cancel{f_Y(y)}} \cancel{f_Y(y)}dy\\\
&= {1\over m}\int_{\mathbb R} f_X(y)dy\\\
&= {1\over m}
\end{aligned}$$

A questo punto, possiamo dire che $E[N] = m$, perciò generiamo, mediamente, un campione valido di $X$ ogni $m$ cicli dell'algoritmo. Per questo, l'efficienza dell'algoritmo è $1/m$.

Per aumentare l'efficienza dell'algoritmo, quindi, è necessario **diminuire $m$ il più possibile**. Inoltre possiamo dire che, in generale, l'efficienza dell'algoritmo sarà sempre strettamente minore del 100%.

#### Campionamento di una variabile aleatoria Gaussiana

Prendiamo ora una variabile aleatoria Gaussiana $Z\sim N(0,1)$.

Dato che la legge della Gaussiana tende all'infinito ai suoi bordi, sarà necessario avere una funzione ausiliaria anch'essa infinita, in modo da coprire tutta la legge $f_Z$.

Per semplificare il lavoro però, possiamo notare che $f_Z$ è simmetrica rispetto all'asse $y$, perciò potremmo, ad esempio, considerare soltanto il ramo positivo della campana della Gaussiana:

$$Z = \text{sgn}(Z)\cdot |Z| = S\cdot|Z|$$

Così facendo, interpretiamo la variabile aleatoria $Z$ come il prodotto del suo segno e del suo modulo.

Possiamo dire:

$$P(S=+1) = P(S=-1) = {1\over2}$$

Cerchiamo ora un algoritmo per generare il segno $S$:

1. Generare $U\sim U[0,1]$
2. Scegliere $S=1$ se $U<1/2$, altrimenti scegliere $S=-1$
3. Tornare al punto 1

Noi sappiamo che:

$$f_{|Z|}(\rho) = f_Z(\rho) + f_Z(-\rho) = \begin{cases}
{1\over\sqrt{2\pi}}e^{-{\rho^2\over2}} + {1\over\sqrt{2\pi}}e^{-{(-\rho^2)\over2}} = {2\over\sqrt{2\pi}}e^{-{\rho^2\over2}}, &\rho>0\\\
0,&\text{altrimenti}
\end{cases}$$

Per campionare questa legge di probabilità, potremmo usare una variabile aleatoria [esponenziale](../poisson#variabili-aleatorie-esponenziali) $Y\sim\text{Exp}(1)$, che ha legge di probabilità:

$$f_Y(y) = \begin{cases}
e^{-y}, &y>0\\\
0, &\text{altrimenti}
\end{cases}$$

Ora, come abbiamo già fatto prima, è necessario trovare una costante $m$ tale che $mf_Y(\rho) \ge f_{|Z|}(\rho),\ \forall\rho>0$:

$${f_{|Z|}(\rho)\over mf_Y(\rho)} \stackrel{!}{\le} 1$$

Sostituendo con i valori delle leggi di probabilità, otteniamo:

$$m \ge 2\sqrt{e\over2\pi}$$

Il valore che conviene utilizzare è perciò:

$$m = 2\sqrt{e\over2\pi}$$

Riassumiamo quindi l'algoritmo di acceptance-rejection per una Gaussiana $Z$:

1. Generare $Y\sim\text{Exp}(1)$ e $U\sim U[0,1]$ indipendentemente
2. Accettare e porre $|Z|=Y$ se $U' \le {f_{|Z|}(Y)\over mf_Y(Y)} = e^{-{(Y-1)^2\over2}}$; altrimenti tornare al punto 1

> **Nota**
>
> La condizione di accettazione può anche essere riscritta come:
> $$-\ln(U')\ge{(Y-1)^2\over2}$$

Un algoritmo equivalente a questo potrebbe essere:

1. Generare $Y\sim\text{Exp}(1)$ e $T\sim\text{Exp}(1)$ indipendentemente
2. Se $T\ge{(Y-1)^2\over2}$, allora porre $|Z|=Y$ (o salvare $V = T - {(Y-1)^2\over 2}$); altrimenti tornare al punto 1

> **Alcune proprietà**
>
> 1. Tempo medio alla generazione di $|Z|$:$$E[N] = m = \sqrt{2e\over\pi}\approx 1.3155$$
> 2. Efficienza dell'algoritmo: circa il 76%
> 3. Distribuzione di $V$ sapendo che $V>0$:$$V = T - {(Y-1)^2\over 2}\sim\text{Exp}(1)\perp Y$$

Ora che abbiamo generato $S$ e $|Z|$, possiamo dire che $Z = S\cdot|Z|\sim N(0,1)$?

Vediamolo con le densità di probabilità di queste variabili aleatorie:

$$\begin{aligned}
f_Z(z) &= f_{S,|Z|}(s,\rho)\\\
&= p_S(s) \cdot f_{|Z|}(\rho)
\end{aligned}$$

Dato che $f_Z$ ha simmetria pari, possiamo dire che $S\perp|Z|$, perciò vale l'espressione scritta sopra. Allora è anche vero che $Z = S\cdot|Z|\sim N(0,1)$ e quindi si possono generare $S$ e $|Z|$ con algoritmi indipendenti e calcolare $Z$ come prodotto delle due variabili aleatorie generate.

> **Algoritmo migliore**
>
> Esiste un algoritmo con efficienza 100% per campionare delle variabili aleatorie Gaussiane, detto [Box-Muller](https://it.wikipedia.org/wiki/Trasformazione_di_Box-Muller).

Generalizziamo ora il metodo per le Gaussiane $X\sim N(\mu,\sigma^2)$. Per fare questo, normalizziamo la Gaussiana non-standard:

$$Z = {X-\mu\over\sigma}\sim N(0,1)$$

Dopodiché, basta campionare $Z$ e poi calcolare $X = \sigma Z + \mu$.

Come possiamo invece campionare un vettore di variabili aleatorie Gaussiane standard indipendenti?

Prendiamo un vettore di variabili aleatorie gaussiane standard:

$$\underline X = (X_1, X_2, \ldots, X_n)^T$$

Possiamo anche calcolare un vettore $\underline\mu$ che rappresenta il valore atteso di tutte le variabili aleatorie in $\underline X$:

$$\underline\mu = E[\underline x] = (E[X_1],E[X_2],\ldots,E[X_n])^T = 0$$

Questo vettore è nullo perché tutte le Gaussiane standard sono a media nulla.

Definiamo ora una matrice di covarianza:

$$\Sigma = \big[\text{Cov}[X_i,X_j] \big]_{i,j} = E\big[(\underline X-\underline\mu)(\underline X-\underline\mu)^T\big] = \mathbb I$$

Dato che le variabili aleatorie nei vettori sono tutte indipendenti ed a varianza unitaria, possiamo concludere che la matrice di covarianza sia pari, in questo caso, ad una matrice identica.

Volendo generalizzare, cerchiamo di generare un campione da un vettore di variabili aleatorie Gaussiane con vettore valore atteso generico e matrice di covarianza generica. Cerchiamo di seguire lo stesso procedimento di prima: normalizziamo tutte le variabili aleatorie del vettore e trasformiamo linearmente le variabili normalizzate per tornare a quelle generiche.

Riassumendo:

1. Generare $Z_i\sim N(0,1), \ i=1,\ldots,n$ indipendentemente
2. Porre $\underline X = A\underline Z + \underline b$

$A, \underline b$ devono essere tali da soddisfare $E[\underline X]=\underline\mu$ e $\Sigma_{\underline X} = \Sigma$. Vediamo come fare:

$$\begin{aligned}
\mu &= E[\underline X]\\\
&= E[A\underline Z + \underline b]\\\
&= AE[\underline Z] + \underline b\\\
&= \underline b
\end{aligned}$$

Vediamo che, dato che le variabili aleatorie normalizzate sono a media nulla, il vettore dei valori attesi non è altro che il vettore $\underline b$. Vediamo ora per la matrice di covarianza:

$$\begin{aligned}
\Sigma_{\underline X} &= E\big[(\underline X - \underline\mu)(\underline X - \underline\mu)^T \big]\\\
&= E\big[(\underline X - \underline b)(\underline X - \underline b)^T \big]\\\
&= E\big[A\underline Z(A\underline Z)^T \big]\\\
&= E\big[A\cdot\underline Z\cdot \underline Z^T\cdot A^T \big]\\\
&= A\cdot E[\underline Z\cdot\underline Z^T]\cdot A^T\\\
&= A\cdot A^T
\end{aligned}$$

Vediamo che, poiché $E[\underline Z\cdot\underline Z^T]$ non è altro che la matrice di covarianza delle variabili aleatorie normalizzate ed è perciò la matrice identità, troviamo semplicemente che $\Sigma_{\underline X} = AA^T$.

Per risolvere più semplicemente questa equazione quadratica, possiamo applicare la **fattorizzazione di Cholesky**:

> **Fattorizzazione di Cholesky**
>
> Quando si vuole trasformare una generica matrice $M$ in un prodotto di due generici vettori $V\cdot V^T$, si applica la fattorizzazione di Cholesky e si scrive:
> $$V = \text{Cholesky}(M)$$

Possiamo perciò concludere che, per campionare un vettore di variabili aleatorie Gaussiane non-standard, è sufficiente applicare una fattorizzazione di Cholesky in questo modo:

$$\underline X = \text{Cholesky}(\Sigma_{\underline X})\underline Z + \underline\mu$$
