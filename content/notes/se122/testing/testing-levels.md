---
title: 'Livelli di testing'
draft: false
type: 'page'
toc: true
mathjax: true
---

---

## Test di modulo

Il test di modulo è il test del più piccolo elemento costitutivo di un sistema.

Un modulo è generalmente prodotto da un solo programmatore o da un piccolo team di programmatori ed il test è tipicamente eseguito dal programmatore stesso prima del rilascio. In alcuni casi, può anche essere fatto da persone diverse dai programmatori che l'hanno prodotto.

## Test di integrazione

Il test di integrazione si riferisce ad un insieme di componenti che devono essere integrati per formare un sistema. Nei sistemi più complessi, è possibile che il risultato dell'integrazione sia un sottosistema che deve, a sua volta, integrarsi con altri sottosistemi.

Il test di integrazione viene di solito effettuato da un gruppo di testing apposito di cui, tipicamente, non fanno parte i programmatori.

Le interfacce da verificare sono indicate dai documenti di progetto del sistema.

## Test delle interfacce

Verificare un'interfaccia per volta rende più facile progettare test soddisfacenti; inoltre, gli errori sono così individuati in modo più chiaro.

Si sviluppano dei programmi che servono solo a sollecitare le interfacce per verificare tutti i possibili interscambi tra moduli. In questo contesto:

- I **driver** sono i simulatori dei moduli che iniziano le interazioni
- Gli **stub** sono i simulatori dei moduli eventualmente utilizzati

![](../../images/Pasted%20image%2020221219154704.png)

## Test di sistema

In questo caso, l'oggetto del test è l'intero sistema. Lo scopo del test è di verificare:

- Che il sistema funzioni come specificato (processo di *verifica*)
- Che il sistema funzioni come richiesto dall'utente (processo di *validazione*)

A seconda dello scopo, si distingue tra:

- **Test di sistema** propriamente detto: condotto dal produttore per verificare la qualità del prodotto
- **Test di accettazione**: condotto con il committente per verificare che il prodotto corrisponda a quanto stipulato dal contratto di sviluppo

## Beta testing

A volte, nello sviluppo di un progetto software, non esiste un committente, quindi non esiste nemmeno un test di accettazione. Questo succede quando il software non è prodotto per un cliente, ma invece è immesso sul mercato.

In questo caso, si ricorre al cosiddetto *beta-test*: il sistema viene rilasciato in prova ad un certo numero di utenti selezionati, che usano il nuovo sistema in condizioni realistiche e segnalano eventuali errori. Questo non è un vero e proprio test poiché non si usano tecniche formali di verifica.

Per contrasto, si chiama *alfa-test* il testing effettuato dal produttore, spesso in un ambiente *artificiale*.

## Test di (non) regressione

Succede raramente che il software sia prodotto in un'unica soluzione. Generalmente, vengono rilasciate diverse versioni dello stesso programma. Nasce quindi il problema di verificare non solo che ogni versione raggiunga gli obiettivi per i quali è stata creata, ma accertarsi anche che le caratteristiche che erano già pienamente soddisfacenti nelle versioni precedenti non siano state compromesse.

## Obiettivi del testing

Poiché il testing può mostrare la presenza di difetti e non dimostrare la loro assenza, lo scopo del testing è trovare quanti più difetti possibile.

Va ricordato che qui, con *difetto*, si intende uno scostamento dalle qualità funzionali e non funzionali del software.

Trovare il vero e proprio difetto che sta all'origine di questi malfunzionamenti non è necessariamente un compito del testing.

Il testing, inoltre, deve essere ripetibile, che è una condizione necessaria ad effettuare il debugging.
