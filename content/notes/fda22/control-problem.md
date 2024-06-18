---
title: 'Problema del controllo'
draft: false
type: 'page'
toc: true
mathjax: true
---

---
Dato un sistema $S$ con ingressi $u$, disturbi $d$ e uscita $y$, l'obiettivo del sistemista è quello di mantenere $y\approx w$ nonostante la presenza di $d$ e nonostante una conoscenza imperfetta di $S$.

---
## Strategie di controllo
Esistono quattro diverse strategie di controllo:
1. **Controllo in anello aperto** (o *AA*)
	+ In questo caso, il controllore $C$ non conosce né l'uscita $y$, né il disturbo $d$.
	+ Questo sistema di controllo funziona se il modo in cui l'ingresso $u$ influenza l'uscita $y$ è perfettamete noto ed invertibile e non ci sono disturbi.
2. **Controllo in anello aperto con compensazione del disturbo**
	+ Questo caso è simile a quello precedente, ma si aggiunge un *misuratore del disturbo* $M_d$.
	+ Questo sistema di controllo funziona se è noto il legame $(u, d)\to y$ e se $d_m$ è una buona misura di $d$.
3. **Controllo in anello chiuso** (o *AC*, *in retroazione*)
	+ In questo caso si aggiunge al controllore $C$ un *misuratore dell'uscita* $M_y$, che fornisce ad esso una misura di $y$: $y_m$.
	+ Si può dire che il controllore conosce il disturbo tramite il suo effetto sull'uscita, ma non conosce il disturbo direttamente.
	+ Questo tipo di controllo può contrastare disturbi non misurati ed errori di modello.
4. **Controllo in anello chiuso con compensazione del disturbo**
	+ Questo caso è simile al precedente, ma aggiungiamo un *misuratore del disturbo* $M_d$.
	+ Se il sistema di controllo è ben progettato, otteniamo una reazione al disturbo pronta ma imprecisa attraverso il misuratore del disturbo ed una reazione al disturbo lenta ma precisa attraverso il misuratore dell'uscita.
