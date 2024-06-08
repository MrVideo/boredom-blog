---
title: 'Tecniche di definizione dei casi di test'
draft: false
type: 'page'
toc: true
mathjax: true
---

---

## Tecniche di black box testing

Esistono diversi modi per identificare i casi di test:

- Testing guidato dalla sintassi
- Testing guidato dagli scenari d'uso
- Testing guidato da boundary conditions
- Derivazione semiautomatica dei casi di test dalle specifiche

### Testing guidato dalla sintassi

Questa tecnica è utile per programmi che interpretano testi secondo una grammatica formale.

L'idea è che le stesse regole che il programma da testare deve osservare o riconoscere vengono usate per generare dati di ingresso per quel programma. La grammatica fa parte delle specifiche del programma.

### Testing guidato dagli scenari d'uso

Spesso, è possibile derivare i casi di test dalla specifica degli scenari d'uso.

Per ogni caso, si possono elencare tutti i possibili ingressi che lo caratterizzano e provare quindi il comportamento del programma a fronte di tali casi.

In effetti, gli scenari d'uso non sono altro che un modo per rappresentare i requisiti funzionali del sistema.

### Derivazione semiautomatica dei casi di test dalle specifiche

Esistono linguaggi di specifica da cui si riesce a generare in modo automatico o semiautomatico dei casi di test. Esempi di tali linguaggi sono quelli che sfruttano la logica temporale o gli automi a stati.

In generale, il testing basato sulle specifiche può essere tanto più automatizzato ed efficace quanto più la specifica è formale.

Le specifiche formali permettono lo sviluppo di tool per la generazione automatica di casi di test. Inoltre, possono indicare per tali input anche i corrispondenti risultati attesi.

## Non linearità del software

Prima di procedere a vedere altri criteri di definizione di casi di test, occorre evidenziare alcune caratteristiche del software.

Una caratteristica fondamentale che distingue il software da molti altri semilavorati è la non linearità del comportamento. Ad esempio, consideriamo il seguente ragionamento:

> Se voglio provare un programma che cerca un elemento in una lista, provo con una lista di 100 elementi. Se funziona correttamente, darà risultati corretti anche per liste più piccole.

Questo ragionamento è fallato poiché, per esempio, il programma potrebbe cercare in una lista vuota, che è una condizione eccezionale.

## Classi di equivalenza

Accade normalmente che un programma si comporti in modo simile per interi insiemi di dati di ingresso. Questi insiemi vengono chiamati *classi di equivalenza*. Spesso, sono le specifiche che suggeriscono la classificazione.

Ad esempio, è possibile specificare i mesi in base alla durata, creando così tre classi di equivalenza:

$$\begin{aligned}
M_{31} &= \{1, 3, 5, 7, 8, 10, 12\}\\
M_{28} &= \{2\}\\
M_{30} &= \{4, 6, 9, 11\}
\end{aligned}$$

Così facendo, per testare un possibile programma che si basa su queste informazioni, possiamo scegliere uno solo degli elementi di ciascun insieme.

## Testing guidato dai casi limite

Alcuni errori tipici si manifestano in prossimità dei confini delle classi di equivalenza. Tra i vari casi di test è dunque opportuno, soprattutto nel black box testing, introdurre dei dati di test che vadano a verificare una corretta implementazione per i casi limite (detti anche *boundary conditions*).

Alcuni esempi di questi possono essere:

- Il pop su uno stack vuoto
- La visita di alberi vuoti o con un solo nodo
- Il passaggio della data da 1999 a 2000

## I grafi causa-effetto

Un modo piuttosto comune di determinare un insieme minimo di casi di test si basa sull'utilizzo dei cosiddetti *grafi causa-effetto*.

Questi grafi servono per mettere in relazione dei fatti elementari, espressi come condizioni booleane, con i risultati attesi.

Un esempio di grafo si ha nell'immagine sotto:

![](../../images/Pasted%20image%2020221219172000.png)

È essenziale dare un significato preciso ai nodi che si trovano alle estremità sinistra (gli input) e destra (gli output). Questo significato dipende dalle specifiche.

Conoscendo la dipendenza di un risultato dalla combinazione degli ingressi, si può stimolare il sistema da testare esattamente con tale combinazione e verificare se il risultato reale coincide con quello atteso.

Talvolta, può risultare conveniente trasformare il grafo in una tabella come la seguente:

![](../../images/Pasted%20image%2020221219172417.png)

Il testing black box può essere sempre applicato, una volta note le specifiche. Tuttavia, è particolarmente utile in appoggio a:

- **Test di modulo**: integra le capacità del testing strutturale
- **Test di integrazione**: interessano le interfacce, mentre i moduli vengono trattati come scatole nere
- **Test di sistema**: si controlla la funzionalità del sistema intero
- **Test di accettazione**: al committente interessa che il sistema funzioni bene, non delle specifiche funzionali
