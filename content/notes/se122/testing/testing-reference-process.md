---
title: 'Testing: un processo di riferimento'
draft: false
type: 'page'
toc: true
mathjax: true
---

---

Finora abbiamo visto attività di verifica basate su ispezioni ed analisi statica automatizzata. Ora vedremo il *testing*, ossia il *collaudo* dei programmi.

Il testing si applica al risultato finale dello sviluppo, ossia agli eseguibili prodotti. Ha lo scopo di far emergere quanti più difetti possibile.

Va comunque notato che attraverso il solo testing non si potrà mai concludere che il software prodotto è corretto.

## Necessità di un processo

Le ispezioni possono essere fatte in qualunque momento su qualunque documento prodotto. L'analisi statica può essere fatta dopo la produzione di un documento formalmente ben definito. Il testing, invece, dev'essere fatto dopo che gli eseguibili sono già stati prodotti.

In un processo software articolato, però, esistono diversi tipi di programmi, diversi momenti di rilascio e diversi scopi, perciò esistono anche diversi tipi di test, fatti in momenti diversi, con obiettivi diversi.

## Un modello di processo di riferimento

Per comprendere quali sono i momenti in cui si fa il testing e quali sono gli obiettivi di ciascuna fase, è stato introdotto un modello di riferimento: il **modello a V**.

![](../../images/Pasted%20image%2020221219153738.png)

## Livelli di test

I livelli del testing si riferiscono alla fase del ciclo di vita che ha prodotto il programma che viene testato.

I possibili oggetti del testing sono:

- Un modulo
- Un sottosistema
- L'intero sistema (da parte degli sviluppatori)
- L'intero sistema (in laboratorio, con gli utenti finali)
- L'intero sistema (in campo, da parte degli utenti finali)

I protagonisti e gli obiettivi del testing cambiano a seconda del livello.
