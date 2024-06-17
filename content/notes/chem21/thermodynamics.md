---
title: 'Formulario di termochimica'
draft: false
type: 'page'
toc: true
mathjax: true
---

---
## Lavoro
- $w=-\Delta n\cdot R\cdot T$ se la trasformazione dipende dal variare del numero di moli di una specie chimica
- $w=-n\cdot R\cdot\Delta T$ se la trasformazione dipende da una variazione di temperatura del sistema

Per convenzione, si pone:
- $w>0$ se il lavoro è compiuto sul sistema
- $w<0$ se il lavoro è compiuto sull'ambiente circostante

## Variazione di energia interna
L'energia interna di un sistema è la somma delle energie cinetiche e potenziali di tutti i componenti del sistema. È una funzione di stato e solitamente è nota la sua variazione in seguito ad una trasformazione:
$$\Delta E = E_f-E_i=Q+w$$
Va ricordato che $Q$ e $w$ non sono funzioni di stato.

## Principi della termodinamica
0. Se due corpi $A$ e $B$ sono entrambi in equilibrio termico con un terzo corpo $C$, allora lo sono anche fra loro.
1. L'energia interna di un sistema termodinamico isolato è costante.
2. In un sistema termodinamico isolato, l'entropia è una funzione non decrescente nel tempo.
3. L'entropia di un cristallo perfetto allo zero assoluto ($T=0K=-273.15°C$) è esattamente uguale a zero.

## Entalpia
L'entalpia è una funzione di stato associata alla quantità di energia che un sistema termodinamico può scambiare con l'ambiente a pressione costante.
$$H=E+pV$$
La sua variazione si calcola come:
$$\Delta H=\Delta E+p\Delta V$$
Inoltre, $\Delta H=Q$, cioè la variazione di entalpia di un sistema rappresenta anche il calore scambiato dal sistema con l'ambiente. Per questo possiamo dire che:
- Se $\Delta H>0$, il calore viene assorbito dal sistema e perciò il processo che avviene è endotermico.
- Se $\Delta H< 0$, il calore viene ceduto dal sistema e perciò il processo che avviene è esotermico.

Possiamo definire alcune quantità:
- **Entalpia standard di formazione** $\Delta H_F° [{J\over\text{mol}}]$: è la variazione di entalpia associata alla reazione che produce una mole del composto a partire dagli elementi costituenti nei loro stati stabili, in condizioni standard, pari a $T=25°C, p=1\text{ atm}$. Gli elementi nei loro stati più stabili hanno, per definizione $\Delta H_F°=0$.
- **Entalpia standard di reazione** $\Delta H_R° [{J\over\text{mol}}]$: è la variazione di entalpia di una reazione quando tutti i reagenti ed i prodotti si trovano in condizioni standard. Si può calcolare come:

    $$\Delta H_R^\circ = \sum_{i=1}^{n_\text{prod}} \nu_i \Delta H^\circ_{F, i_\text{prod}} - \sum_{i=1}^{n_\text{reag}} \nu_i\Delta H^\circ_{F, i_\text{reag}}, \nu \text{ coefficiente stechiometrico}$$

- **Legge di Hess**: se una reazione è data dalla somma di due o più reazioni, la variazione di Entalpia della reazione è data dalla somma delle variazioni di entalpia delle reazioni sommate.
- **Entalpia molare di fusione** $\Delta H_\text{fus}$: calore da trasferire a temperatura e pressione costanti per far fondere una mole di sostanza.
- **Entalpia molare di solidificazione** $\Delta H_\text{sol}$: è l'opposto dell'entalpia molare di fusione. Vale: $\Delta H_\text{fus}=-\Delta H_\text{sol}$.
- **Entalpia molare di evaporazione** $\Delta H_\text{ev}$: calore da trasferire a temperatura e pressione costanti per far evaporare una mole di sostanza.
- **Entalpia molare di condensazione** $\Delta H_\text{cond}$: è l'opposto dell'entalpia molare di evaporazione. Vale: $\Delta H_\text{ev}=-\Delta H_\text{cond}$.

## Calorimetria
Il calore assorbito o ceduto da un sistema è dato da:
$$Q=mc\Delta T$$
dove:
* $m$ è la massa del composto
* $c$ è il calore specifico
* $\Delta T$ è la variazione di temperatura

Il **calore specifico** è il calore necessario da fornire per far aumentare di $1°C$ la temperatura di $1 g$ di sostanza.

Il calore scambiato si può anche calcolare come:
$$Q=nc_V\Delta T \text{ oppure } Q=nc_p\Delta T$$
nel caso in cui, rispettivamente, il trasferimento di calore avvenga a volume o pressione costante. In questo caso:
* $n$ è il numero di moli del composto
* $c_V$ è il calore specifico a volume costante, mentre $c_p$ è il calore specifico a pressione costante
* $\Delta T$ è la variazione di temperatura

## Entropia
Il disordine della materia in un campione di sostanza può essere misurato tramite l'entropia:
$$S=K_B\ln(\Omega)$$
dove:
* $K_B = 1.38\cdot10^{-23} {J\over K}$ costante di Boltzmann
* $\Omega$ numero di microstati, cioè posizioni accessibili alle particelle che costituiscono il sistema

L'entropia è una funzione di stato. La sua variazione si può calcolare come:
$$\Delta S={q_\text{rev}\over T}$$
dove $q_\text{rev}$ è il valore scambiato in una trasformazione reversibile.

Possiamo definire alcune quantità:
* **Entropia molare standard** $S° [{J\over \text{mol}\cdot K}]$: entropia molare associata ai composti nei loro stati standard a $T=25°C$ e $p=1\text{ atm}$. Questa quantità aumenta secondo l'ordine ($\text{solidi}<\text{liquidi}<\text{gas}$) e con la temperatura.
* **Entropia molare standard di reazione** $\Delta S_R° [{J\over\text{mol}\cdot K}]$: variazione di entropia di una reazione quando tutti i reagenti ed i prodotti si trovano in condizioni standard. Si può calcolare analogamente all'entropia molare standard di reazione:
    $$\Delta S_R^\circ=\sum_{i=1}^{n_\text{prod}}\nu_i S^\circ_{F, i_\text{prod}}-\sum_{i=1}^{n_\text{reag}}\nu_iS^\circ_{F, i_\text{reag}}, \nu \text{ coefficiente stechiometrico}$$

Nelle transizioni di fase:
- L'entropia aumenta nei processi di fusione ed evaporazione
- L'entropia diminuisce nei processi di condensazione e solidificazione

## Energia libera di Gibbs
Dal secondo principio della termodinamica, la condizione di spontaneità risulta: $$\Delta S_\text{U} = \Delta S_\text{sistema} + \Delta S_\text{ambiente} > 0$$
L'energia libera di Gibbs è una grandezza che misura la capacità del sistema di produrre lavoro utile. Viene calcolata come:$$\Delta G=\Delta H-T\Delta S$$
Esistono tre casi quindi:
- Se $\Delta G < 0$, allora la reazione è spontanea
- Se $\Delta G = 0$, allora la reazione è all'equilibrio
- Se $\Delta G>0$, allora la reazione non è spontanea

In condizioni standard, possiamo definire alcune grandezze:
- **Energia libera standard di formazione** $\Delta G_F° [{J\over\text{mol}}]$: variazione di energia libera per la reazione di formazione di un determinato composto a partire dagli elementi, a $T=25°C$ e $p=1\text{ atm}$.
- **Energia libera standard di reazione** $\Delta G_R° [{J\over\text{mol}}]$: variazione di energia libera di una reazione quando tutti i reagenti ed i prodotti si trovano in condizioni standard. Si può calcolare analogamente all'entropia molare standard di reazione:
    $$\Delta G_R^\circ=\sum_{i=1}^{n_\text{prod}}\nu_i\Delta G^\circ_{F, i_\text{prod}}-\sum_{i=1}^{n_\text{reag}}\nu_i\Delta G^\circ_{F, i_\text{reag}}, \nu \text{ coefficiente stechiometrico}$$
- **Temperatura di equilibrio** $T_\text{eq}\ [K]$: si può trovare la temperatura di equilibrio nel caso in cui $\Delta G_R°=0$ come: $$T_\text{eq} = {\Delta H_R°\over\Delta S_R°}$$

In condizioni non standard, la variazione di energia libera si esprime come: $$\Delta G_R = \Delta G_R°+RT\ln(Q)$$
dove:
- $\Delta G_R°$ è la variazione di energia libera dello stesso processo in condizioni standard
- $R = 8.31 [{J\over\text{mol}\cdot K}]$ è la costante universale dei gas perfetti
- $T$ è la temperatura a cui avviene il processo
- $Q$ è il quoziente di reazione del processo

Possiamo trovare analogamente un'espressione generica per la variazione di energia libera standard di reazione:$$\Delta G_R°=-RT\ln(K_\text{eq})$$
dove $K_\text{eq}$ indica la costante di equilibrio della reazione stessa.

Si può inoltre calcolare $K_\text{eq}$ come:$$\ln(K_\text{eq}) = -{\Delta G_R°\over RT}$$
Infine, si può calcolare il valore di $K_\text{eq}$ ad una temperatura $T_1$ conoscendone il valore ad una temperatura diversa $T_2$:$$\ln\bigg({{K_{\text{eq},T_1}}\over {K_{\text{eq},T_2}}}\bigg)=-{\Delta H_R°\over R}\bigg({1\over T_1}-{1\over T_2}\bigg)$$
