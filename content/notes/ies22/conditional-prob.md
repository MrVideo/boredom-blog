---
title: 'Probabilità condizionate'
draft: false
type: 'page'
toc: true
mathjax: true
---

---

Ipotizziamo di avere due eventi in uno spazio campionario, $A$ e $B$, che si sovrappongono e supponiamo che i due eventi abbiano le seguenti probabilità di accadere:

- $P(A) = 3/6$
- $P(B) = 1/6$
- $P(A\cap B) = 2/6$

Se un osservatore affidabile ci comunica che B è accaduto, come dobbiamo modificare le probabilità degli eventi?

Possiamo dire che:

$$P(A|B) = {2/6\over2/6 + 1/6} = {2\over3} = {P(A\cap B)\over P(B)}$$

Possiamo allora definire il concetto di **probabilità condizionata**:

> **Probabilità condizionata**
>
> Dati due eventi $A$ e $B$, la probabilità condizionata di $A$ dato $B$ è:
> $$P(A|B) = {P(A\cap B)\over P(B)}, P(B) > 0$$

> **Nota**
>
> Quando viene fornita l'informazione che un evento è accaduto, è come se lo spazio campionario si restringesse all'evento stesso, dato che è certamente avvenuto.

Le probabilità condizionate hanno lo stesso comportamento delle probabilità non condizionate, quindi valgono anche per loro gli [assiomi](../axioms) elencati precedentemente.

Introduciamo ora alcune regole formali che aiutano nella comprensione delle probabilità condizionate:

## Regola moltiplicativa

> **Regola moltiplicativa**
>
> Dati tre eventi $A$, $B$ e $C$:
> $$P(A\cap B\cap C) = P(A) \cdot P(B|A) \cdot P(C|A\cap B)$$

## Teorema delle probabilità totali

> **Teorema delle probabilità totali**
>
> Dati $n$ eventi che formano una partizione del proprio spazio campionario $\Omega$, posso dire che:
> $$P(B) = \sum_{i = 1}^n P(A_i)\cdot P(B|A_i)$$

## Regola di Bayes e inferenza

> **Domanda**
>
> Sapendo che l'evento $B$ è accaduto, qual è la probabilità che *sia stato causato* dallo scenario $i$-esimo?

Per rispondere a questa domanda, possiamo introdurre la **Regola di Bayes**:

> **Regola di Bayes**
>
> $$P(A_i|B) = {P(A_i)\cdot P(B|A_i)\over\sum_{j=1}^n P(A_j)\cdot P(B|A_j)}$$

La Regola di Bayes è importante per risolvere i problemi di **inferenza**: partendo da un modello causa-effetto, vogliamo calcolare la probabilità che sia stato lo scenario $i$-esimo a generare l'effetto $B$.

## Paradosso di Monty Hall

Si ipotizzi di avere tre scatole, una sola delle quali contiene un premio. Ipotizziamo, in questo caso, che la scatola numero due sia quella vincente.

> il giocatore sceglie una scatola ed il presentatore ne apre una per mostrare che è vuota, conviene cambiare scatola o tenere quella scelta precedentemente per vincere?

Analizziamo lo spazio di probabilità (che è uniforme) tramite la seguente tabella:

| Pacco 1 | Pacco 2 | Pacco 3 | Cambio la scatola | Tengo la scatola |
| ------- | ------- | ------- | ----------------- | ---------------- |
| Premio  | Vuoto   | Vuoto   | Sconfitta         | Vittoria         |
| Vuoto   | Premio  | Vuoto   | Vittoria          | Sconfitta        |
| Vuoto   | Vuoto   | Premio  | Vittoria          | Sconfitta        | 

> **Nota**
>
> Ipotizziamo in questa tabella che la scatola scelta dal giocatore sia la numero uno, ma non lede la generalità del problema.

Possiamo dire allora che:

$$P(\text{Vincere cambiando il pacco }|\text{ Uno degli altri pacchi è vuoto}) = {2\over3}$$

Quindi conviene sempre cambiare il pacco, poiché la probabilità di vittoria dato il cambio del pacco è maggiore di quella che si avrebbe mantenendo la stessa scatola.
