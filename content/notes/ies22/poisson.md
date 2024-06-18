---
title: "Processi di Poisson"
draft: false
type: 'page'
toc: true
mathjax: true
---

---

## Definizione

Un processo di Poisson è un processo analogo a quello di [Bernoulli](../bernoulli) ma a tempo continuo.

In un processo di Poisson si mantengono tutte le proprietà di un processo di Bernoulli:

- Vale la proprietà di perdita di memoria ^6697af
- L'intensità media degli arrivi per unità di tempo è costante:$$P(k\text{ arrivi in un intervallo di tempo }\tau) = P(k,\tau) = \text{cost}$$
- Proprietà di *omogeneità temporale*: date due variabili aleatorie $N_{t_1}$ ed $N_{t_2}$ che rappresentano il numero di successi nel rispettivo intervallo di tempo $t_i$, se $t_1\cap t_2=\emptyset$, allora $N_{t_1}\perp N_{t_2}$
- Il numero di successi medio per intervallo di tempo (o anche il ritmo di successi per intervallo di tempo) è pari a $\lambda$

## Distribuzione del numero di arrivi in un intervallo di tempo

Definiamo una variabile aleatoria $N_{[0,\tau]}$ come il numero di successi nell'intervallo di tempo $[0,\tau]$.

Se dividessimo la linea temporale in $n$ intervalli di tempo piccoli a piacere, avremmo un modello di processo di Bernoulli e potremmo calcolare la probabilità che nell'intervallo $[0,\tau]$ avvengano $k$ successi come:

$$P_{N_{[0,\tau]}}(k) = \lim_{n\to\infty} \binom{n}{k}\cdot \bigg({\lambda\tau\over n}\bigg)^k\cdot \bigg(1-{\lambda\tau\over n}\bigg)^{n-k}$$

Allora possiamo dire che la legge di probabilità descritta sopra è pari a:

$$P_{N_{[0,\tau]}}(k) = \lim_{n\to\infty} \text{Bin}\bigg(n,{\lambda\tau\over n}\bigg) = \begin{cases}
{(\lambda\tau)^k\over k!}e^{-\lambda\tau}, &k=0,1,2,\ldots\\\
0,&\text{altrimenti}
\end{cases}$$

Questa espressione è enunciata dalla **legge di Poisson**.

Possiamo allora classificare la variabile aleatoria $N_{[0,\tau]}$ come una variabile aleatoria di Poisson in questo modo:

$$N_{[0,\tau]} \sim \text{Poisson}(\lambda\tau)$$

Una variabile aleatoria di Poisson ha le seguenti proprietà:

- Converge a 1 per $k\to\infty$
- Valore atteso e varianza hanno entrambi valore $\lambda\tau$

## Tempo al $k$-esimo arrivo: legge di Erlang

[Come per i processi di Bernoulli](../bernoulli#tempo-al-k-esimo-arrivo), possiamo calcolare il tempo al $k$-esimo successo in un processo di Poisson tramite la **legge di Erlang**.

Se prendiamo $Y_k$, variabile aleatoria continua, come tempo al $k$-esimo arrivo, la sua densità di probabilità sarà:

$$f_{Y_k}(t) = \begin{cases}
{(\lambda t)^{k-1}\over (k-1)!}\lambda e^{-\lambda t}, &t>0,k\ge1\\\
0, &\text{altrimenti}
\end{cases}$$

Possiamo anche dire che $Y_k$ è una variabile aleatoria distribuita come una variabile di Erlang:

$$Y_k \sim \text{Erlang-}k(\lambda)$$

### Variabili aleatorie esponenziali

Il tempo al primo arrivo calcolato tramite la legge di Erlang è pari a:

$$f_{T_1}(t) = \begin{cases}
\lambda e^{-\lambda t},&t\ge0\\\
0,&\text{altrimenti}
\end{cases}$$

Una variabile aleatoria così distribuita è detta *esponenziale*:

$$T_1 \sim\text{Exp}(\lambda)$$

Dato che il processo di Poisson gode della [proprietà di perdita di memoria](../poisson#definizione), sappiamo che anche il tempo al secondo successo e tutti i successivi saranno a loro volta distribuiti come esponenziali. Per questo, in generale, si può dire: $$Y_k = T_1+T_2+\ldots+T_k \sim \text{Erlang-}k(\lambda), \text{ con } T_i \sim \text{Exp} (\lambda)\text{ i.i.d.}$$

Possiamo anche calcolare il valore atteso di $Y_k$:

$$E[Y_k] = \sum_{i=1}^k E[T_i] = {k\over\lambda}$$

> **Nota**
>
> È possibile generare un processo di Poisson generando soltanto i suoi tempi di interarrivo.

## Relazione tra processi di Bernoulli e di Poisson

Mettiamo a confronto i processi di Bernoulli e quelli di Poisson tramite la seguente tabella:

|                                                 | Poisson                      | Bernoulli     |
| ----------------------------------------------- | ---------------------------- | ------------- |
| Tempo di arrivo                                 | Continuo                     | Discreto      |
| *Rate* degli arrivi                             | $\lambda$ per unità di tempo | $p$ per prova |
| Densità di probabilità del numero di arrivi     | Poisson                      | Binomiale     |
| Densità di probabilità del tempo di interarrivo | Esponenziale                 | Geometrica    |
| Tempo al $k$-esimo arrivo                       | Erlang                       | Pascal        | 

## Splitting e merging dei processi di Poisson

[Come visto per i processi di Bernoulli](../bernoulli#splitting-di-un-processo-di-bernoulli), anche i processi di Poisson possono essere divisi o uniti tramite splitting e merging, ottenendo sempre un processo di Poisson come risultato.

## Incidenza casuale per processi di Poisson

> Consideriamo un processo di Poisson iniziato da moltissimo tempo ed osserviamolo a partire da un tempo casuale. Qual è la distribuzione della lunghezza del tempo che trascorre tra due arrivi adiacenti a cavallo dell'istante di tempo scelto?

Chiamiamo $W$ la variabile aleatoria che rappresenta il tempo tra un arrivo e l'altro.

Considerando che i processi di Poisson [godono della proprietà di perdita di memoria](../poisson#definizione), sappiamo che i due intervalli tra il tempo scelto e l'arrivo $T_1, T_1'$ sono **indipendenti tra loro**. Per questo motivo, possiamo considerarli come il tempo al primo arrivo a partire dall'istante selezionato $t$ e dire:

$$T_1,T_1' \sim \text{Exp}(\lambda)$$

Di conseguenza, [come visto precedentemente](../poisson#variabili-aleatorie-esponenziali), possiamo dire che:

$$W = T_1+T_1' \sim \text{Erlang-}2(\lambda)$$
