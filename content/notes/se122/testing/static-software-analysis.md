---
title: 'Analisi statica del software'
draft: false
type: 'page'
toc: true
mathjax: true
---

---

## Analisi statica automatica

L'analisi statica è una tecnica che consente di analizzare semilavorati software senza eseguirli.

L'analisi statica è possibile grazie all'esistenza di strumenti automatici. Ciò implica che l'oggetto in analisi dev'essere ben definito, cioè deve avere una semantica formale.

Laddove applicabile, l'analisi statica è un ottimo ausilio alle ispezioni (condotte invece da operatori umani), poiché è più efficiente ed affidabile.

L'analisi automatica ha però diverse limitazioni dovute alla non decidibilità di molte caratteristiche interessanti.

## Limiti dell'analisi automatica

Molti programmi che sarebbero convenienti a scopo di testing non sono realizzabili. Ad esempio, non esiste un programma che dica se due generici programmi $P_1$ e $P_2$ siano equivalenti (è dimostrabile formalmente).

Dobbiamo accontentarci perciò di analizzare solo alcune proprietà o solo alcuni casi particolari.

## Analisi statica: esempi

Facendo riferimento all'analisi del codice, ci sono alcuni tipi di difetti che si possono facilmente individuare. Per esempio, è semplice vedere quando viene utilizzata una variabile non inizializzata:

```c
int n;
if(n > 0) {
	//...
}
```

Purtroppo però, anche in questo caso, non sempre riusciamo ad avere la certezza che l'errore sussista:

```c
int n;
while(/*...*/) {
	//...
}
if(n > 0) {
	//...
}
```

In questo ultimo caso infatti, può darsi che nel ciclo `while`, la variabile `n` venga inizializzata, ma non possiamo prevedere il flusso di controllo run-time.

## Conseguenze dei limiti dell'analisi statica

Esistono due approcci fondamentali usati dagli strumenti di analisi:

1. **Rigoroso**: si segnalano soltanto gli errori certi, tralasciando quelli possibili. L'utente deve sapere che se l'analisi si conclude senza errori non è detto che non ce ne siano.
2. **Pessimistico**: si segnalano sia gli errori certi, sia quelli possibili. Se non vengono segnalati errori, significa che non ce ne sono. L'utente deve sapere che, a fronte di una segnalazione, deve verificare se si tratti di un difetto reale o no.

## Altri tipi di analisi sul codice

Alcuni controlli fatti spesso sono:

- Variabili definite ma non usate (difficile da applicare in linguaggi con puntatori)
- Accesso ad array fuori dai limiti
- Codice irraggiungibile
- Sottoprogrammi dichiarati ma non usati

È da notare che tutti questi casi cercano di verificare staticamente proprietà run-time del programma.

I compilatori fanno anche altre verifiche, che non fanno riferimento alla situazione run-time e sono quindi totalmente affidabili.

## Aspetti dell'analisi statica

L'analisi statica si concentra su diversi tipi di problemi:

- Flusso di controllo: si analizzano le possibili sequenze di esecuzione; rivela ad esempio blocchi di codice irraggiungibili
- Uso dei dati: si analizza l'uso (lettura o assegnamento) delle variabili o delle costanti dichiarate; rivela errori come l'uso di variabili non inizializzate, la dichiarazione di variabili non utilizzate e altro
- Interfacce: si analizza la coerenza delle dichiarazioni di funzioni o metodi e dell'uso di queste da parte dei sottoprogrammi

Altri tipi di analisi non servono a scoprire errori ma generano informazioni utili per review ed ispezioni. Ad esempio, si può derivare l'elenco di istruzioni eseguite in corrispondenza di certi dati in ingresso insieme all'output fornito dal programma in esame.

## Strumenti per l'analisi statica

Esistono molti strumenti per l'analisi statica, che differiscono sia per il linguaggio a cui si applicano, sia per il tipo di analisi compiuta. Ad esempio, per linguaggi object-oriented con tipi dinamici, esistono strumenti che fanno *type inference*: cercano di stabilire quali tipi saranno associati a quali variabili runtime.

Uno dei primi e più noti strumenti di analisi statica è il *lint* per il linguaggio C.

## Oggetto dell'analisi statica

È possible applicare l'analisi statica del codice anche ad altri sottoprodotti del processo di sviluppo, purché il documento da analizzare abbia una semantica formale e ben definita.

Esistono infatti diversi linguaggi di specifica formali che possono essere analizzati dai cosiddetti *model checkers*: programmi che verificano alcune proprietà dei modelli dati.
