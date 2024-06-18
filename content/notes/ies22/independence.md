---
title: 'Indipendenza'
draft: false
type: 'page'
toc: true
mathjax: true
---

---

Ipotizziamo di lanciare tre monete non bilanciate.

In ogni stadio dell'esperimento (ossia tra ogni lancio di una moneta diversa) le probabilità che il risultato sia testa o croce non cambia, ma rimangono costanti *indipendentemente* dal punto dell'esperimento in cui ci si trova.

Le probabilità condizionate sono quindi uguali a quelle incondizionate e conoscere i risultati dei lanci precedenti non aiuta a predire i lanci futuri.

Definiamo ora formalmente l'indipendenza:

> **Indipendenza**
>
> Una definizione intuitiva di indipendenza potrebbe essere:
> > Dati due eventi $A$ e $B$, questi si dicono *indipendenti* se $P(B|A) = P(B)$.
> 
> Una definizione più formale invece è:
> > $A$ e $B$ sono indipendenti se e solo se $P(A\cap B) = P(A)\cdot P(B)$
> 
> La definizione formale si basa sulla [regola moltiplicativa](../conditional-prob#regola-moltiplicativa).

Per scrivere che due eventi sono indipendenti, si usa il simbolo di perpendicolarità: $\perp$.

## Indipendenza condizionata

Consideriamo tre eventi non disgiunti $A$, $B$, $C$. Assumiamo che i due eventi $A$ e $B$ siano indipendenti.

> Sapendo che $C$ è accaduto, è comunque vero che $A\perp B$?

Con questo esempio, notiamo che l'indipendenza condizionata **non è equivalente** a quella incondizionata:

$$P(A\cap B|C) = P(A|C)P(B|C) \nLeftrightarrow P(A\cap B) = P(A)P(B)$$
