---
title: 'Testing Black Box: principi e processo'
draft: false
type: 'page'
toc: true
mathjax: true
---

---

Esistono diverse modalità di testing possibili: ad esempio, si può decidere di collaudare un oggetto ignorando la sua organizzazione ed il suo funzionamento interno, oppure cercare di sfruttare queste conoscenze.

Nel primo caso, si svolge un *black box testing*; nel secondo, si svolge un *testing strutturale*.

## Black Box Testing

Il programma è considerato una scatola nera: non siamo interessati dal funzionamento interno, bensì solo da input e output.

I casi di test sono scelti a partire da un'analisi delle specifiche dei requisiti. Si scelgono i dati di test in modo da sollecitare tutte le funzioni previste, in tutte le condizioni di applicazione previste. Questo testing è di tipo funzionale.

Il black box testing può essere pianificato presto poiché dipende solo dalle specifiche. Non è detto che sia conveniente: infatti, se le specifiche cambiano presto nel ciclo di vita del software, anche i test già sviluppati andranno cambiati.

![](../../images/Pasted%20image%2020221219165558.png)

Attenzione: le specifiche del programma da testare devono essere precise.
