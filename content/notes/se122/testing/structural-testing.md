---
title: 'Testing strutturale: principi, processo e criteri di copertura'
draft: false
type: 'page'
toc: true
mathjax: true
---

---

## Testing strutturale o white box

Il testing strutturale, come dice il nome, tiene conto della struttura interna del programma.

I casi di test sono derivati da un'analisi diretta dell'implementazione, ossia del codice del programma da testare).

L'obiettivo del testing, anche qui, è quello di sollecitare tutte le parti del programma.

Applicare questo criterio in modo esaustivo è generalmente molto costoso o infattibile, perciò si applica solo su porzioni particolarmente critiche del codice, come ad esempio quella da cui può dipendere la sicurezza di un sistema.

Nell'immagine, si può vedere in sintesi il processo di testing white box.

![](../../images/Pasted%20image%2020221219174534.png)

Mentre per il testing black box è necessario testare tutte le funzioni che si mettono a disposizione dell'utente, per il testing strutturale il criterio più ovvio è quello di testare tutte le istruzioni di cui è composto il codice.

L'insieme dei casi di test deve essere selezionato in modo che ogni istruzione del codice venga eseguita almeno una volta.

Nonostante si riesca a testare un programma con un insieme di casi di test che assicuri la copertura delle istruzioni, non è assicurata l'assenza di errori.

Si introduce anche un criterio detto *edge coverage*, che serve a testare le istruzioni che verrebbero altresì nascoste da condizioni di input specifiche. Ad esempio, considerando il seguente snippet di codice:

```c
if(x > 0)
	x += 4;
z = 365 / x;
```

L'insieme minimo di casi di test che realizzano la copertura delle istruzioni è costituito da un unico caso che abbia `x > 0`. Attraverso questo caso, però, non è possibile controllare cosa succede nel programma quando il ramo `if` non è eseguito.

![](../../images/Pasted%20image%2020221219175423.png)

## Criteri di copertura delle decisioni e delle condizioni

L'insieme dei casi di test per l'edge coverage deve essere definito in modo che ogni ramo del *Control Flow Graph* del programma venga attraversato almeno una volta. Per applicare il criterio, quindi, è necessario costruire il control flow graph: un grafo che rappresenta il flusso di controllo del programma da testare con una certa approssimazione.

### Control Flow Graph (CFG)

- Una sequenza di istruzioni semplici diventa un arco del CFG:

![](../../images/Pasted%20image%2020221219175727.png)

- Una sequenza di blocchi semplici diventa un arco che collega i CFG corrispondenti ai blocchi:

![](../../images/Pasted%20image%2020221219175800.png)

- Istruzioni condizionali `if ... then ... else ...`:

![](../../images/Pasted%20image%2020221219175924.png)

- Istruzioni condizionali `if ... then`:

![](../../images/Pasted%20image%2020221219180008.png)

- Ciclo `while`:

![](../../images/Pasted%20image%2020221219180028.png)

- Esempio di CFG:

![](../../images/Pasted%20image%2020221219180054.png)

### Limiti del criterio di edge coverage

Anche con il criterio di edge coverage rispettato, non si può essere sicuri che il programma non contenga errori.

Prendiamo per esempio questo snippet di codice:

```c
void p(int x, int y) {
	if(x == 0 || y > 0)
		y = y / x;
	else
		y = (-y) / x;
}
```

Consideriamo i dati di test:

- $(x = 1; y = 1)$
- $(x = 1; y = -1)$

Il problema è dovuto al fatto che la condizione che regola l'istruzione `if` è composta, ma è stata sollecitata solo la condizione relativa a `y`, mantenendo falsa la condizione relativa ad `x`. Per risolvere il problema, è necessario introdurre un criterio più stringente.

### Criterio di copertura delle decisioni e delle condizioni

L'insieme dei casi di test deve essere definito in modo che ogni ramo del CFG venga attraversato almeno una volta e con tutti i possibili valori che compaiono nelle condizioni composte.

Nell'esempio precedente, scegliendo le seguenti tre coppie, si soddisfa il criterio:

- $(x = 0;y = -1)$
- $(x = 1; y = 1)$
- $(x = 1; y = -1)$

Anche con questo criterio, non possiamo dire con certezza se il programma contiene degli errori o no.

## Criteri di copertura dei cammini

### Limiti del criterio di copertura delle decisioni e delle condizioni

L'insieme minimo di casi di test permette di attraversare tutti gli archi del CFG, ma l'errore si ha quando si esegue una combinazione di archi non coperta dai casi di test.

Si introduce allora il *criterio di copertura dei cammini* (o *path coverage*): l'insieme dei casi di test deve garantire che ogni possibile cammino che porti dal nodo iniziale al nodo finale del CFG sia percorso. L'idea alla base di questo criterio è quella di stimolare tutti i possibili funzionamenti del programma.

### Problemi con la copertura dei cammini

Con questo criterio, si superano le limitazioni dei criteri precedenti, ma in generale il numero di casi di test richiesti per seguirlo è troppo elevato per poter essere applicato in pratica.

In generale, occorre individuare accuratamente le porzioni di codice critiche per la correttezza del sistema. Queste saranno soggette a test strutturale. Occorre inoltre determinare il livello di copertura desiderato. Questo è un compito non banale che necessita di metriche adeguate.
