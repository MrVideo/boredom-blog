---
title: 'Scheda riassuntiva di elettrochimica'
draft: false
type: 'page'
toc: true
mathjax: true
---

---

## Ossidazione e riduzione
Le reazioni di **ossidoriduzione** (anche detti *redox*) sono processi che coinvolgono il trasferimento di elettroni tra due specie chimiche.

La specie che si riduce acquista elettroni: $$\ce{Au^{3+} +2e^- -> Au^+}$$
mentre la specie che si ossida perde elettroni:$$\ce{Cu-> Cu^{2+} +2e^-}$$
In un'ossidoriduzione, esistono due agenti:
- **Agente riducente**: è la specie che si ossida e, di conseguenza, causa la riduzione dell'altra specie
- **Agente ossidante**: è la specie che si riduce e, di conseguenza, causa l'ossidazione dell'altra specie

Un esempio di ossidoriduzione è dato dalla reazione:$$\ce{MnO_2 + ClO^-_3 ->MnO_4^{2-} + Cl^-}$$
### Numeri di ossidazione
Per riconoscere quale specie si ossida e quale si riduce, si ricorre all'assegnazione del numero di ossidazione ($NO$):

| Elemento                 | Numero di ossidazione                                                                 |
| ------------------------ | ------------------------------------------------------------------------------------- |
| Elemento puro            | 0                                                                                     |
| Ione monoatomico         | Carica dello ione                                                                     |
| Ossigeno                 | -2 nei composti, -1 nei perossidi                                                     |
| Idrogeno                 | +1 nei composti, -1 negli idruri metallici                                            |
| Metalli alcalini         | +1                                                                                    |
| Metalli alcalino-terrosi | +2                                                                                    |
| Fluoro                   | -1                                                                                    |
| Composto neutro          | La somma dei numeri di ossidazione degli atomi dev'essere 0                           |
| Ione poliatomico         | La somma dei numeri di ossidazione degli atomi dev'essere pari alla carica dello ione | 

### Bilanciamento delle ossidoriduzioni

Il bilanciamento delle reazioni redox è diverso dal bilanciamento normale. Si segue questo procedimento:
1. Identificare le specie che si ossidano e le specie che si riducono
2. Scrivere le due semireazioni di ossidazione e riduzione, non bilanciate, includendo solo le specie che partecipano alla reazione, elettroni inclusi
3. Bilanciare tutti gli atomi tranne $\ce{H}$ e $\ce{O}$
4. Bilanciare le cariche introducendo ioni $\ce{H3O+}$ o $\ce{OH-}$ a seconda del $pH$ dell'ambiente di reazione
5. Bilanciare gli atomi di $\ce{H}$ e $\ce{O}$ introducendo $\ce{H2O}$
6. Moltiplicare le due equazioni per opportuni coefficienti, in modo che il numero di $\ce{e-}$ prodotti eguagli il numero di $\ce{e-}$ consumati
7. Sommare le due semireazioni e semplificare

## Potenziale di riduzione
Il potenziale di riduzione è una grandezza che misura la tendenza di una specie chimica ad essere ridotta, cioè ad acquisire $\ce{e-}$. Tanto più è positivo, quanto più la specie chimica tende facilmente a ridursi.

Possiamo definire il **potenziale standard di riduzione** $E° [V]$ come il potenziale di riduzione misurato in condizioni standard, ovvero:
- $T=25°C$
- $p_i = 1\text{ atm}$
- $[M^{x+}]=1\text{ M}$

Il potenziale standard di riduzione di una specie chimica è misurato rispetto ad un **elettrodo standard ad idrogeno** (**SHE**), al quale viene assegnato il valore di riferimento $0\ V$:$$\ce{2H+ + 2e- -> H2}$$

## Forza elettromotrice
Il potenziale di cella, anche detto **forza elettromotrice**, è definito come la differenza di potenziale quando non passa corrente nella cella:

$$f.e.m. = E^\circ_\text{catodo} - E^\circ_\text{anodo}=E^\circ_\text{cella}$$

## Cella galvanica
Una cella galvanica è una cella che sfrutta un'ossidoriduzione spontanea per generare una differenza di potenziale.

Una cella galvanica è composta da:
- Un **anodo** (o polo negativo), in cui avviene l'ossidazione
- Un **catodo** (o polo positivo), in cui avviene la riduzione
- Un **ponte salino**
- Un **conduttore metallico**

La schematizzazione di una cella galvanica è data dalla seguente formula:$$\ce{(-)\ Zn|Zn^{2+}||Cu^{2+}|Cu\ (+)}$$
in cui la parte sinistra rappresenta l'anodo, mentre la parte destra rappresenta il catodo.

Il potenziale di cella di una cella galvanica in condizioni non standard può essere ricavato mediante l'**equazione di Nernst**:$$E_\text{cella} = E°_\text{cella} - {RT\over nF}\ln(Q)$$
dove:
- $Q$ è il quoziente di reazione
- $R=8.31 [{J\over\text{mol}\cdot K}]$ è la costante universale dei gas
- $T$ è la temperatura assoluta a cui avviene la reazione
- $n$ è il numero di moli di $\ce{e-}$ scambiate
- $F=96485 [{C\over\text{mol}}]$ è la costante di Faraday

Nel caso in cui la temperatura sia pari a $25°C$, la precedente formula si può semplificare in:$$E_\text{cella}=E°_\text{cella}-{0.059\over n}\log_{10}(Q)$$

Esiste una relazione tra l'energia libera di Gibbs ed il potenziale di cella di una cella galvanica, descritto dalle seguente equazioni:$$\begin{align}\Delta G&=-nF\cdot E_\text{cella}\\\Delta G°&=-nF\cdot E°_\text{cella}\end{align}$$
La prima equazione descrive l'energia libera di una cella in condizioni non standard, mentre la seconda la descrive solo in condizioni standard.

Da queste equazioni troviamo tre casi possibili:
- $\Delta G>0\implies E_\text{cella}<0$: la reazione non è spontanea
- $\Delta G=0\implies E_\text{cella}=0$: la reazione è all'equilibrio
- $\Delta G<0\implies E_\text{cella}>0$: la reazione è spontanea

## Cella elettrolitica
Fornendo energia elettrica, e quindi elettroni, è possibile invertire il funzionamento di una cella galvanica e far avvenire reazioni redox normalmente non spontanee. Una cella di questo tipo è detta **cella elettrolitica**.

Una cella elettrolitica è schematicamente simile ad una cella galvanica, ma con i poli invertiti:$$\ce{(+)\ Cu|Cu^{2+}||Zn^{2+}|Zn\ (-)}$$
Come si può notare, una cella elettrolitica è composta da:
- Un **anodo** (o polo positivo), in cui avviene l'ossidazione
- Un **catodo** (o polo negativo), in cui avviene la riduzione
- Un **ponte salino**
- Un **conduttore metallico**
- Un **generatore esterno**, per fornire energia elettrica alla cella

Una cella può avere due tipi di elettrodi:
- Elettrodi **inerti**: sono fatti di materiali che non vengono né ossidati né ridotti, quali la grafite, il platino, il mercurio...
- Elettrodi **attivi**: partecipano attivamente nel processo di ossidoriduzione

Le celle elettrolitiche sono spesso usate per operazioni di placcatura, in cui si dissolve un metallo e lo si fa depositare su un elettrodo di un altro metallo.

## Leggi di Faraday
Le due leggi di Faraday enunciano:

Legge | Enunciato
- | -
Prima | La massa di sostanza che si libera vicino ad un elettrodo è direttamente proporzionale alla carica che vi arriva
Seconda | Le masse di sostanze depositate agli elettrodi contenenti soluzioni diverse ed attraversate dalla stessa quantità di carica sono proporzionali ai rispettivi equivalenti elettrochimici

La seconda legge di Faraday si può enunciare in formula con questa equazione:$$nF=Q=it$$

## Lavoro elettrico
Il movimento di una carica $Q$ all'interno di un campo elettrico è un processo che richiede lavoro. Tale lavoro è detto **lavoro elettrico**.

In una cella galvanica, il movimento di elettroni nel filo conduttore produce lavoro elettrico pari a:$$w_\text{el}=-Q\cdot\Delta E$$
Applicando la legge di Faraday, si ottiene:$$w_\text{el}=-(nF)\cdot\Delta E$$
Infine, sfruttando la relazione tra l'energia libera ed il potenziale di cella:$$w_\text{el}=-(nF)\cdot\Delta E=\Delta G$$
