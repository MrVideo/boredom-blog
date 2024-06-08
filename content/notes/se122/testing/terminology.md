---
title: 'Terminologia'
draft: false
type: 'page'
toc: true
mathjax: true
---

---

Sia data la seguente situazione: un programma $P$ elabora dati di ingresso appartenenti ad un insieme $I$ e produce risultati appartenenti all'insieme $O$.

Effettuare un test vuol dire selezionare un sottoinsieme dei dati di $I$, che indicheremo $T$, ed eseguire $P,\ \forall t \in T$. In questo contesto, $t$ si chiama *dato di test*.

I casi di test (o *test case*) sono dati dalle coppie $(t, o_{\text{atteso}})$.

Ovviamente, dopo aver eseguito $P$ con ingresso $t$, occorre confrontare il risultato ottenuto con quello previsto associato a $t$.

![](../../images/Pasted%20image%2020221219160430.png)

## Il processo di test

Dato un programma $P$ con il suo insieme di possibili ingressi $I$, non basta eseguirlo per un certo numero di volte scegliendo gli ingressi appartenenti ad $I$ in modo casuale. In questo modo, le probabilità di trovare errori sono molto basse.

Occorre dunque un processo di test che inizi dal design dei casi di test in grado di sollecitare il sistema in una gamma di situazioni ampia. Bisogna quindi:

1. Progettare i casi di test
2. Definire i dati di test ed i risultati attesi
3. Eseguire il programma
4. Confrontare i risultati ottenuti con quelli attesi
5. Documentare le differenze
