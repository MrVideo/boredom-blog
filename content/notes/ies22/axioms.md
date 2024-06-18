---
title: 'Teoria assiomatica della probabilità'
draft: false
type: 'page'
toc: true
mathjax: true
---

---

## Spazio campionario ed eventi

Introdotta da Andrej Nikolaevič Kolmogorov nel 1933, si basa sul concetto di **spazio campionario**:

> **Spazio campionario**
>
> L'insieme di tutti i possibili risultati dell'esperimento aleatorio

Le proprietà di uno spazio campionario sono:

- **Esaustività**: deve elencare tutti i possibili risultati dell'esperimento
- **Mutua esclusività**: si deve sempre verificare uno ed un solo evento elementare all'esecuzione dell'esperimento

Possono esistere sia spazi *discreti*, come quello di un lancio di una moneta:

$$\Omega = \{\text{Testa}, \text{Croce}\}$$

Sia spazi *continui*, ossia nel dominio dei numeri reali:

$$\Omega = \{x:0\le x \le1\}$$

Possiamo ora definire anche gli eventi:

> **Evento**
>
> Un sottoinsieme misurabile di uno spazio campionario $\Omega$. Generalmente indicato con una lettera latina maiuscola.

## Assiomi

La teoria assiomatica della probabilità si basa su tre assiomi:

1. Non-negatività: $P(A) \ge 0$
2. Normalizzazione: $P(\Omega) = 1$
3. Additività: se $A \cap B = \emptyset$, allora $P(A\cup B) = P(A) + P(B)$

Dal terzo assioma possiamo ricavare anche il teorema delle probabilità totali:

> **Teorema delle probabilità totali**
>
> Dati $n$ eventi disgiunti $A_1, A_2, \ldots, A_n$, vale:
> $$P\bigg(\bigcup_{i=1}^n A_i\bigg) = \sum_{i=1}^n P(A_i)$$

## Leggi di probabilità uniformi

A seconda che lo spazio campionario $\Omega$ sia discreto o continuo, possiamo formulare le leggi di probabilità uniformi discrete o continue:

> **Legge di probabilità uniforme discreta**
>
> Se $\omega$ è un evento elementare di $\Omega$, allora:
> $$P(\omega) = {1 \over |\Omega|}, \forall \omega \in \Omega$$
> Inoltre, dato un evento $A$:
> $$P(A) = {\text{casi favorevoli ad }A\over\text{casi totali}} = {|A|\over|\Omega|}$$

> **Legge di probabilità uniforme continua**
>
> La probabilità di un evento è proporzionale all'area della regione dello spazio campionario coperta dai casi favorevoli a tale evento:
> $$P(A) = {\text{area}(A)\over\text{area}(\Omega)}, \forall A\subseteq\Omega$$
