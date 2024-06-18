---
title: "Osservazioni su IeS"
draft: false
type: 'page'
toc: true
mathjax: true
---

---

## Probabilità ipergeometriche

Le probabilità ipergeometriche vengono utilizzate quando si ha un problema del tipo:

> Ho un’urna con $n$ biglie, di cui $m$ rosse, $l$ blu, $k$ verdi. Voglio estrarre 2 biglie rosse, 3 verdi e 4 blu. Qual è la probabilità che questo accada, senza che reinserisca le biglie nell’urna?

Un esempio di questo problema è dato dal tema d’esame del 1° settembre 2022, nell’esercizio 1:

> Un allenatore di calcio ha a disposizione 3 portieri, 8 difensori, 7 centrocampisti e 4 attaccanti. Per la prossima partita, l’allenatore ha intenzione di schierare 1 portiere, 4 difensori, 4 centrocampisti e 2 attaccanti. Supponendo che l’allenatore scelga 11 giocatori a caso tra i 22 disponibili, calcolare la probabilità che riesca ad ottenere il suo modulo ideale.

---

## Teorema di Bayes

Grazie al teorema di Bayes, è possibile risalire a probabilità condizionate “inverse” rispetto a quelle trovate nel problema.

La formula rappresentante il teorema di Bayes è la seguente:

$$P(A_i|B) = {P(A_i)\cdot P(B|A_i)\over\sum_{j=1}^n P(A_j)\cdot P(B|A_j)}$$

È anche possibile considerare il denominatore come "*l'unica altra probabilità base*", tramite la regola moltiplicativa:

$$P(A_i|B) = {P(A_i)\cdot P(B|A_i)\over P(B)}$$

Un esempio pratico dove è possibile comprendere meglio questa eguaglianza si ha nel tema d'esame del 1° settembre 2022, esercizio 2:

> Ci sono 4 scatole contenenti alcune banconote:
>
> - la scatola rossa contiene una banconota da €100 e 9 da €5;
> - la scatola verde contiene 2 banconote da €100 e 8 da €5;  
> - la scatola blu contiene 3 banconote da €100 e 7 da €5;
> - la scatola gialla contiene 5 banconote da €100 e 5 da €5.
>
> Pescate una scatola a caso e una banconota a caso dalla scatola. Se la banconota pescata è di €100, qual è la probabilità che la scatola scelta sia quella gialla?

In questo caso, la probabilità richiesta è:

$$P(G|\text{pesco €100}) = {P(G)P(\text{pesco €100}|G)\over P(\text{pesco €100})}$$

È chiaro che la probabilità di pescare €100 è pari alla somma delle probabilità di pescare €100 da ciascuna delle quattro scatole:

$$\begin{aligned}
\text{pesco €100} &= \sum_{i=1}^4P(S_i)P(\text{pesco €100}|S_i)\\\
&= 0.25\cdot0.1+0.25\cdot0.2+0.25\cdot0.3+0.25\cdot0.5\\\
&= {11\over40}
\end{aligned}$$

Ecco spiegata l'uguaglianza delle due forme del teorema di Bayes specificate sopra.

---

## Somma di variabili aleatorie indipendenti

La legge di probabilità di due variabili aleatorie indipendenti è la **convoluzione** delle due leggi di probabilità. Nel caso di due variabili aleatorie discrete, si parla di [somma di convoluzione](../joint-stats#leggi-della-somma-di-variabili-aleatorie); nel caso di due continue, si parla di [integrale di convoluzione](../joint-stats#leggi-della-somma-di-variabili-aleatorie).

È possibile risolvere entrambi i tipi di convoluzione tramite un metodo grafico che somma le due leggi di probabilità dopo averne traslata una.

Possiamo però notare che, nel caso di due leggi di probabilità uniformi identiche, il risultato dell'integrale di convoluzione di queste due sarà un triangolo isoscele con base larga il doppio delle due leggi di partenza ed altezza uguale.

---

## Applicazione del teorema dell'aspettativa totale

Questo esempio è tratto dal tema d'esame del 31 agosto 2018. Il testo del problema è come segue:

> Vi viene proposto il seguente gioco: si compie una successione di lanci di una moneta bilanciata, dove effettuare ogni lancio vi costa 1 €. Se si ottengono 3 teste di fila allora si vincono 10 € e il gioco termina. Mediamente vi aspettate di guadagnare o perdere da questo gioco?

Per risolvere questo problema, è utile disegnare un albero delle probabilità ed applicare il [teorema dell'aspettativa totale](../drv#legge-dellaspettativa-totale):

![](../images/Pasted%20image%2020230830105135.png)

Come possiamo vedere dall'immagine, se in un qualunque caso otteniamo una croce, interrompiamo la catena di teste necessaria a vincere, quindi ci rimettiamo nel caso iniziale.

Sapendo questo, possiamo applicare l'aspettativa totale con le seguenti equazioni:

$$\begin{aligned}
E[N] &= 1 + E[N|T]P(T) + E[N|C]P(C)\\\
&= 1 + {1\over2}E[N|T]+ {1\over2}E[N]\\\
\\\
E[N|T] &= 1 + E[N|TT]P(T) + E[N|TC]P(C)\\\
&= 1 + {1\over2}E[N|TT] + {1\over2}E[N]\\\
\\\
E[N|TT] &= 1 + E[N|TTT]P(T) + E[N|TTC]P(C)\\\
&= 1 + {1\over2}E[N|TTT] + {1\over2}E[N]
\end{aligned}$$

Poiché il numero di lanci per arrivare ad avere tre teste quando si ha già ottenuto tre teste di fila è zero, possiamo riscrivere l'ultimo valore atteso così:

$$E[N|TT] = 1 + {1\over2}E[N]$$

A questo punto, basta sostituire ritornando fino alla prima equazione, che diventa:

$$E[N] = {7\over4}+{7\over8}E[N]$$

Risolvendo, otteniamo $E[N] = 14$. Questo significa che, per vincere i €10 promessi, in media, ne spendiamo €14, rendendo il gioco sconveniente.

---

## Campionare da una variabile aleatoria esponenziale

Prendiamo una variabile aleatoria esponenziale $X\sim\text{Exp}(\lambda)$, che ha cumulata:

$$F_X(x) = \begin{cases}
1-e^{-\lambda x}, &x\ge0\\\
0,&\text{altrimenti}
\end{cases}$$

Per campionare questa variabile aleatoria, possiamo utilizzare un'uniforme $U\sim U[0,1]$. Usando il metodo della cumulata inversa troviamo:

$$F_X^{-1}(u) = -{1\over\lambda}\ln(1-u)$$

Vediamo però che $U\sim 1-U\sim U[0,1]$, quindi possiamo semplificare la generazione dei campioni come:

$$x = -{1\over\lambda}\ln(u)$$

Su MATLAB, è possibile eseguire questa operazione così:

```matlab
u = rand;
x = -1 / lambda * log(u);
```

---

## Metodo acceptance-rejection

Ipotizziamo di avere una variabile aleatoria $X$ con legge di probabilità $f_X$ nota definita nell'intervallo $[0,10]$. Vogliamo campionarla.

Per farlo, possiamo prendere un valore $m$ tale che:

$$m \ge \max f_X(x)$$

Così facendo, abbiamo praticamente costruito un tabellone di dimensioni $[0,10]\times[0, m]$. Ora "lanciamoci" delle "freccette", cioè scegliamo dei valori a caso entro questa regione rettangolare. Una volta lanciate tutte queste metaforiche freccette, decidiamo di mantenere **soltanto quelle che cadono sotto la legge di probabilità** $f_X$. Questa è detta **condizione di *acceptance***.

Fatto questo, possiamo dire che **le ascisse dei punti accettati sono distribuite come** $f_X$.

Scriviamo quindi l'algoritmo di acceptance-rejection:

1. Genero il supporto della variabile aleatoria $X$ come una uniforme $U\sim U[0,10]$
2. Genero un altro campione uniforme $U'\sim U[0,1]$ in modo che $U\perp U'$
3. Accetto e pongo $X=U$ se l'ordinata del punto lanciato $mU'\le f_X(u)$, altrimenti torno al punto 1.

> In pratica, si può dire che $u$ equivale all'ascissa del campione, mentre $mu'$ equivale alla sua ordinata.

Come si può intuire, questo metodo non consente di avere un'efficienza molto alta nella maggior parte dei casi. Possiamo però aumentarla creando un tabellone che "segua" il profilo della funzione da campionare, cioè usando una variabile aleatoria $Y$ diversa da un'uniforme. Ci basta allora trovare un valore $m$ tale che:

$$mf_Y(x)\ge f_X(x), \ \forall x\in\mathbb R$$

Possiamo quindi riscrivere l'algoritmo generalizzato:

1. Genero l'ascissa $Y\sim f_Y$ e l'ordinata $U'\sim U[0,1]$ con $Y\perp U'$
2. Accetto e pongo $X=Y$ se $\underbrace{mf_Y(y)\cdot U'}_\text{ordinata}\le f_X(y)$, altrimenti torno al punto 1

> In pratica, sto prendendo un valore a caso tra 0 ed il massimo della funzione con cui campiono (cioè $Y$) e testo se questo valore sta sopra o sotto la variabile aleatoria da campionare (cioè $X$).

Possiamo interpretare questo algoritmo anche graficamente:

![](../images/Pasted%20image%2020230830183116.png)

Dato che sappiamo generare una densità di probabilità $f_Y$ che racchiude $f_X$ quando moltiplicata per un certo valore $m$, possiamo campionare $X$ prendendo dei valori a caso da $f_Y$ (che come si vede è l'ascissa) ed un valore a caso scelto uniformemente tra 0 ed il massimo di $mf_Y$.

Nell'immagine vediamo come il campione generato da $y$ sia stato accettato poiché cade sulla funzione da campionare $f_X$, mentre il campione generato da $y'$ è stato rifiutato perché va sopra ad $f_X$, fino a raggiungere $mf_Y$. Possiamo anche dire che si accetta l'ascissa $y$ con probabilità:

$${f_X(y) \over mf_Y(y)}$$

---

## Disuguaglianza di Chebyshev

La [disuguaglianza di Chebyshev](../successions#diseguaglianza-di-chebyshev) ci fornisce una stima della probabilità che una variabile aleatoria si discosti dal suo valore atteso.

---

## Stimatori di distribuzioni gaussiane

Si ipotizzi di avere due variabili aleatorie $X, \Theta$ entrambe distribuite come una gaussiana. In questo caso, vale:

$$\hat\Theta_\text{MAP}(x) = \hat\Theta_\text{LMS}(x) =\hat\Theta_\text{LIN}(x) = E[\Theta|X]$$

---

## Stimatore LMS e LMS lineare

Se l'espressione dello stimatore Least Mean Square di una variabile aleatoria è già lineare, allora vale:

$$\hat\Theta_\text{LMS}(x) =\hat\Theta_\text{LIN}(x)$$

Questo non vale però se lo stimatore LMS è solo lineare a tratti.

---

## Variabile aleatoria informazione ed entropia

Se consideriamo una variabile aleatoria discreta $X$, possiamo calcolare l'informazione di una delle sue realizzazioni così:

$$i\big(\{X=x\}\big) = i(x) = \log{1\over p_X(x)}, \ \forall x$$

Sostituendo alla realizzazione di $x$ la rispettiva variabile aleatoria, troviamo una funzione di variabile aleatoria, che a sua volta è una variabile aleatoria, così definita:

$$i(X) = \begin{cases}
\log{1\over p_X(x_1)},\text{ con probabilità } p_X(x_1)\\\
\log{1\over p_X(x_2)},\text{ con probabilità } p_X(x_2)\\\
\vdots\\\
\log{1\over p_X(x_n)},\text{ con probabilità } p_X(x_n)\\\
\end{cases}$$

Da questa variabile aleatoria possiamo calcolare delle statistiche quali il valore atteso, che ci indica l'**informazione media**, o **entropia**, fornitaci dalla variabile aleatoria:

$$\begin{aligned}
H(X) &= E\big[i(X)\big]\\\
&= E\bigg[\log{1\over p_X(X)} \bigg]\\\
&= \sum_{j=1}^n p_X(x_j)\cdot\log{1\over p_X(x_j)}
\end{aligned}$$

> La definizione di entropia ci permette di ignorare il valore delle realizzazioni della variabile aleatoria $X$, poiché basta avere le probabilità della stessa per calcolarla.

