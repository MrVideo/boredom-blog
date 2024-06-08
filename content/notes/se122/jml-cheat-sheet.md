---
title: 'Java Modelling Language'
draft: false
type: 'page'
toc: true
mathjax: true
---

---

## `@invariant`

La keyword `@invariant` indica una condizione che deve sempre essere verificata per un oggetto o una classe durante la sua intera esistenza nel programma.

```java
//@invariant (* espressione logica *)
```

## `@assignable`

La keyword `@assignable` indica che uno o più dei parametri passati al metodo specificato è modificabile dal metodo stesso. Nel caso nessuno di questi lo sia, si può indicare all'inizio della specifica JML:

```java
//@assignable \nothing;
```

## `@requires`

La keyword `@requires` indica la precondizione (o l'insieme di precondizioni) che servono al metodo per eseguire correttamente.

```java
//@requires (* espressioni logiche o commenti *);
```

## `@ensures`

La keyword `@ensures` indica la postcondizione (o l'insieme di postcondizioni) che devono verificarsi al termine dell'esecuzione del metodo specificato.

```java
//@ensures (* espressioni logiche o commenti *);
```

## `@signals`

La keyword `@signals` indica quale eccezione viene lanciata sotto quale condizione nel caso in cui il metodo termini in casi eccezionali.

```java
//@signals (Exception e) (* espressioni logiche o commenti *)
```

## Metodi puri

Un metodo puro è un metodo non statico che non ha effetti collaterali. Un metodo puro viene dichiarato tale in JML tramite la keyword `pure`.

Per un metodo puro vale sempre `@assignable \nothing`. Inoltre, lo stato dell'oggetto non cambia mai.

La keyword `pure` permette anche di chiamare il metodo in JML: un metodo puro può chiamare soltanto altri metodi puri.

Anche i costruttori possono essere definiti come puri: un costruttore puro inizializza gli attributi dichiarati in una classe ma non può modificare nient'altro.

## Sintassi per le asserzioni

La sintassi JML è simile a quella della logica:

| Syntax                               | Semantics                                                                                                                                   |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------- |
| `a ==> b`                            | `a` implica `b`                                                                                                                             |
| `a <==> b`                           | `a` se e solo se `b`                                                                                                                        |
| `a <==!==>`                          | non `a` se e solo se `b`                                                                                                                    |
| `\old(E)`                            | Valore di `E` nello stato precedente                                                                                                        |
| `\result`                            | Indica il valore di ritorno del metodo specificato                                                                                          |
| `contains(param)`                    | Ritorna `true` se la collezione a cui è applicato contiene il valore passatogli come parametro e `false` altrimenti.                        |
| `containsAll()`                      | Ritorna `true` se la collezione a cui è applicato contiene tutti gli elementi della collezione passata come parametro e `false` altrimenti. | 
| `(\forall var; range; condition)`    | $$\forall\text{var}\in\text{range}\ (\text{condition})$$                                                                                    |
| `(\exists var; range; condition)`    | $$\exists\text{var}\in\text{range}\ (\text{condition})$$                                                                                    |
| `(\sum int i; range; condition)`     | Ritorna la somma dell'espressione specificata.                                                                                              |
| `(\product int i; range; condition)` | Ritorna il prodotto dell'espressione specificata.                                                                                           |
| `(\min int i; range; condition)`     | Ritorna l'elemento con valore minimo dell'espressione specificata.                                                                          |
| `(\max int i; range; condition)`     | Ritorna l'elemento con valore massimo dell'espressione specificata.                                                                         |
| `(\num_of int i; P(i); Q(i))`        | Ritorna il numero totale `i` di elementi per cui è vera la condizione $P(\text{i}) \land Q(\text{i})$.                                      |
