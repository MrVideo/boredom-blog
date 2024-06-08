---
title: "Test d'integrazione"
draft: false
type: 'page'
toc: true
mathjax: true
---

---

Con i test di integrazione, si testano sistemi o sottosistemi composti.

È più conveniente che questo test sia di tipo black box.

Questo test è critico poiché la maggior parte degli errori sono di integrazione.

## Moduli stub e moduli driver

L'integrazione si riferisce generalmente ad una gerarchia di componenti, determinata dalle relazioni di utilizzo.

Si osservi l'immagine di seguito:

![](../../images/Pasted%20image%2020221219181443.png)

Per poter testare il modulo $C$, occorre che $E$ sia disponibile. Se non lo è, si ricorre ad uno *stub*.

Per poter testare il modulo $B$, invece, occorre che $A$ sia disponibile. Se non lo è, si ricorre ad un *driver*.

## Strategia di test *big bang*

Integrare tutti i componenti in una volta, ossia applicare la strategia *big bang*, rende il testing particolarmente difficoltoso. I problemi maggiori sono:

- Necessità di numerosi driver e stub
- Diverse anomalie vengono scoperte solo dopo che tutti i moduli vengono rilasciati
- È spesso difficile capire dove sono localizzati gli errori

## Strategia di test incrementale

Per ovviare ai problemi visti, si ricorre a tecniche di test incrementali: i moduli non sono integrati tutti insieme, ma si procede integrandone un numero progressivamente maggiore.

Ci sono due modi possibili di procedere:

- **Top-down**: si sviluppa e si testa il modulo di più alto livello e si testa con gli stub necessari; poi si procede verso il basso.
- **Bottom-up**: si sviluppano prima i moduli di più basso livello e si testano con i driver necessari; poi si procede verso l'alto.

L'approccio incrementale comporta numerosi vantaggi:

- Necessita di driver e stub in numero inferiore al *big bang*
- Le anomalie possono essere scoperte presto
- È spesso più facile capire dove sono localizzati gli errori
- I primi moduli sviluppati sono testati più a lungo

Ci sono differenze anche tra i metodi top-down e bottom-up:

- Bottom-up non richiede stub ma richiede driver, anche complessi; inoltre, testa prima e più a lungo i moduli base, che sono spesso i più critici
- Top-down fornisce subito un prototipo del sistema, utile per una sorta di validazione anticipata

Possono anche essere usate una combinazione dei due approcci.

## Test delle interfacce

Il test delle interfacce avviene quando si integrano più moduli per produrre sistemi più ampi.

In oggetto all'analisi sono:

- I parametri passati da un modulo all'altro
- La memoria condivisa
- Le procedure chiamate
- La richiesta di servizi tra moduli

## Tipi di errori di interfaccia

Gli errori di interfaccia più comuni sono:

- Cattivo uso dell'interfaccia: ad esempio, si passano parametri sbagliati
- Cattiva comprensione dell'interfaccia: quando si cerca di usare un'interfaccia per uno scopo diverso da quello per cui è progettata
- Errori di sincronizzazione o violazione dei vincoli real-time

## Come definire i test delle interfacce

Per definire un test per un'interfaccia, occorre:

- Testare i casi limite
- Cercare di causare malfunzionamenti nel componente utilizzato
- Cercare di essere il più esigenti possibile nei test di servizi
- Provare a variare l'ordine di accesso nei test di condivisione della memoria
