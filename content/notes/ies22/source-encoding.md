---
title: "Codifica di sorgente"
draft: false
type: 'page'
toc: true
mathjax: true
---

---

## Rappresentazione in bit dei risultati di un esperimento

Ipotizziamo di voler rappresentare il risultato di un esperimento aleatorio con una stringa di bit. Quanti bit è necessario usare per rappresentarlo e come vanno scelti?

Prendiamo per esempio l'esperimento aleatorio del lancio di una moneta. Potremmo rappresentare ogni testa come uno 0 ed ogni croce come un 1. È efficiente come rappresentazione?

Se la moneta fosse bilanciata, allora avrebbe senso rappresentare ogni lancio con un solo bit ma, nel momento in cui la moneta è fortemente sbilanciata, ogni lancio genera mediamente meno di un bit di informazione, perciò è inefficiente rappresentare ogni lancio con un bit.

Il problema però è che non è possibile rappresentare meno di un bit, dato che il bit è l'unità base di rappresentazione che abbiamo scelto.

Prendiamo ora per esempio il lancio di due monete consecutive. Ipotizziamo che la probabilità di testa sia $P(T)=3/4$. Possiamo rappresentare le sequenze di lanci in questo modo (eseguiamo l'operazione di *encoding*):

$$\begin{aligned}
TT &\to 0\\\
TC &\to 10\\\
CT &\to 01\\\
CC &\to 111
\end{aligned}$$

Chiamiamo l'insieme di sequenze di bit che rappresentano gli eventi **codice** o **codebook**, mentre una singola sequenza di bit viene detta **parola di codice** o **codeword**.

Con la codifica fornita sopra, la lunghezza media dei messaggi sarebbe:

$$E[L] = 1\cdot \bigg({3\over4}\bigg)^2 + 2\cdot2\cdot{3\over4}\cdot{1\over4}+3\cdot\bigg({1\over4}\bigg)^2 = 1.125 \text{ bit}$$

In questo modo, i bit per lancio di moneta sono scesi drasticamente a 0.5625. Nonostante questo, la decodifica a partire da questo codice potrebbe risultare ambigua. Infatti, dato che l'evento $TT$ è codificato con un solo zero, potrebbe portare confusione nella distinzione tra gli eventi $TT$, $TC$ e $CT$.

Volendo codificare i lanci in modo disambiguo, si potrebbe procedere così:

$$\begin{aligned}
TT &\to 0\\\
TC &\to 10\\\
CT &\to 110\\\
CC &\to 111
\end{aligned}$$

In questo caso, abbiamo 0.84 bit per lancio.

## Disuguaglianza di Kraft-McMillan

Per migliorare ancora l'efficienza del nostro codice, entra in gioco la **disuguaglianza di Kraft-McMillan**.

Perché la disuguaglianza si possa applicare, è necessario che le codeword non creino ambiguità. Per questo, nessuna parola può essere prefisso di qualunque altra parola nel codice.

Date queste precondizioni, possiamo enunciare il teorema di Kraft-McMillan:

> **Teorema di Kraft-McMillan**
>
> È possibile trovare un codice *prefix-free* composto da $m$ codewords con lunghezze $l_1,l_2,\ldots,l_m$ se e solo se:
> $$\sum_{j=1}^m 2^{-l_j} \le 1$$

> In pratica, fissato il numero di parole nel codice $m$, non è possibile scegliere le lunghezze delle codeword troppo piccole: infatti, qualche codeword dovrà essere più lunga per soddisfare la diseguaglianza.

La conseguenza di questo teorema è che **non è possibile** abbassare troppo la lunghezza del codice $E[L]$, altrimenti diventerebbe **ambiguo**.

Rimane allora la domanda:

> Qual è il meglio che si può fare in termini di lunghezza media del codice $E[L]$?

A questa domanda si può rispondere con il seguente teorema:

> **Teorema della codifica di sorgente**
>
> Data una variabile aleatoria discreta $X$ con $m$ risultati possibili, per ogni codice prefix-free che assegna una codeword di $l_j$ bit al risultato $X=x_j$ si ha:
> $$E[L] = \sum_{j=1}^m l_j \cdot p_X(x_j) \ge H(X)$$

Il teorema della codifica di sorgente ci dà un **limite inferiore** alla lunghezza di un codice.
