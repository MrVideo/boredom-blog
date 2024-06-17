---
title: 'Concetti base delle reti'
draft: false
type: 'page'
toc: true
mathjax: true
---

---

Principio fondamentale: *come viene organizzata e smistata l’informazione in una rete?*

1. Commutazione **di circuito**: le risorse trasmissive sono dedicate alla comunicazione; esiste un circuito soltanto con sorgente e destinazione; si definisce *connection-oriented*
2. Commutazione **di pacchetto**: dati inviati in rete con *messaggi* (pacchetti, UI, PDU); vengono condivisi con varie coppie sorgente-destinazione; **non vengono riservate risorse per coppie specifiche** e quindi si definisce generalmente *connectionless*.

La scelta del tipo di commutazione dipende dal **servizio da offrire** e quindi dal **tipo di informazione** da scambiare.

---

## Commutazione di circuito

Tempo fa, la commutazione di circuito veniva usata per le comunicazioni telefoniche. Ad ogni telefonata si dedicava un circuito completo che collegava direttamente sorgente (chiamante) e destinazione (chiamato). Le risorse di rete sono suddivise in *fette*, e ciascuna fetta viene allocata ad un *circuito*, ossia ad un flusso di informazione continuo. Le risorse rimangono **inattive se non utilizzate** e non possono in ogni caso essere condivise.

La suddivisione delle risorse nelle comunicazioni di circuito si fanno *a livello fisico* generalmente, con metodi quali:

- Divisione di frequenza
- Divisione di tempo
- Divisione di lunghezza d’onda

All’interno dei nodi, nella commutazione di circuito, viene conservata la **matrice input-output**, ossia come vengono collegati i circuiti in entrata con quelli in uscita. All’inizio della comunicazione viene fatta quest’associazione e **non è necessario memorizzare l’informazione lungo il circuito una volta instaurato**. Il **tempo di instaurazione** della connessione si aggiunge al **ritardo totale** di trasferimento, dove il ritardo di trasferimento è l’intervallo di tempo tra l’apertura della connessione e l’arrivo dell’ultimo bit a destinazione. L’elaborazione, la propagazione e la trasmissione del messaggio in uscita avvengono solo **dopo l’instaurazione del collegamento**.

![Diagramma di commutazione di circuito](../images/base-concepts-Untitled.png)

Diagramma di commutazione di circuito

---

## Commutazione di pacchetto

La **commutazione di pacchetto** invece *spezza l’informazione stessa in fette*, non i canali di trasmissione. Per fare ciò, è necessario aggiungere un *header* o *overhead* contenenti informazioni di servizio al *payload*, il contenuto stesso dell’oggetto.

I vantaggi che si hanno suddividendo il contenuto in pacchetti sono:

- Tutti i pacchetti **condividono le risorse di rete**
- Ciascun pacchetto **utilizza completamente il canale per un determinato intervallo di tempo**, non determinato a priori
- Le risorse vengono usate a **seconda delle necessità**

Un pacchetto è composto da:

- Header contenente l’indirizzo di destinazione
- Payload

Attraverso la *tabella di instradamento*, che associa ciascun indirizzo di destinazione ad un prossimo nodo, il router ridirige il pacchetto attraverso una delle sue porte verso la destinazione, selezionando effettivamente il percorso corretto.

### Modello di nodo (packet switch/router)

- Capacità dei collegamenti arbitraria
- Possono esserci conflitti temporali per la trasmissione
- È necessario **memorizzare temporaneamente** il pacchetto:
    - All’ingresso, per **analizzare la destinazione**.
    - All’uscita, per **gestire le contese** (generalmente segue la regola *First In First Out*).

Due caratteristiche sono importanti per capire la gestione delle contese all'interno dei router:

- *Store and forward*: il commutatore riceve l’intero pacchetto prima di poter cominciare a trasmettere sul collegamento in uscita.
- *Multiplazione statistica*: accomodamento dei pacchetti ed attesa per l’utilizzo del collegamento.

### Comunicazione in Internet ed efficienza

Per la comunicazione attraverso Internet si usa la **commutazione di pacchetto**. La maggiore efficienza però è anche causa di problemi, quali:

- **Perdita di pacchetti**: dovuta alla dimensione finita dei buffer. Sono necessari dei *protocolli* per il trasferimento affidabili e per il controllo della gestione.
- **Ritardo non determinabile a priori**: si può stimare tramite modelli probabilistici e statistici ma non deterministici.

Non c’è tempo di instaurazione della connessione nella commutazione di pacchetto. Il ritardo è dovuto ad ogni *hop* a:

- Propagazione
- Trasmissione o ritrasmissione (comportamento *Store & Forward*)
- Elaborazione
- Accodamento

Propagazione e trasmissione sono componenti **deterministiche**, mentre l’elaborazione e l’attesa sono contributi **casuali**, che non possono essere calcolati con certezza a priori.

### Frammentazione e ritardo end-to-end

Grazie alla commutazione di pacchetto, posso parallelizzare la trasmissione di pacchetti e inviare due pacchetti, elaborandoli contemporaneamente. Questo processo è chiamato **frammentazione**. Frammentando un pacchetto in più parti, nonostante debba aggiungere un *overhead* per ogni frammento del pacchetto, posso parallelizzare la trasmissione dei frammenti ed avere un **ritardo complessivo minore**. Il numero di frammenti in cui va spezzato un pacchetto va **scelto con ragionevolezza**, poiché **frammentare troppo può portare a ritardi maggiori**.

### Datagram e circuito virtuale

Nella commutazione **datagram**, la scelta della porta d’uscita viene fatta sulla base del solo indirizzo IP di destinazione. I pacchetti dello stesso flusso sono inoltrati indipendentemente. Si usa per questo metodo la **tabella di instradamento** dei router.

Nel caso del **circuito virtuale**, i nodi identificano i pacchetti di un flusso informativo sulla base di un **identificativo di circuito virtuale** (*VCI* o *Label*). Il circuito virtuale viene instaurato in una fase di setup prima della fase di dati, che rende questo metodo *connection-oriented*. Dopo la fase di setup, i pacchetti **seguono tutti lo stesso percorso di rete** e sono instradati sulla base dell’identificativo di circuito virtuale.

### Parametri di prestazione

I parametri di prestazione di una rete sono:

- **Ritardo**
- **Perdita**
- **Throughput**

### Rete end-to-end

![Semplificazione di rete end-to-end](../images/base-concepts-Untitled%201.png)

Semplificazione di rete end-to-end

Contributi di ritardo in una connessione:

- Trasmissione
- Propagazione
- Ricezione

### Velocità e tempo di trasmissione

La **velocità di trasmissione** è la velocità (*rate*) $*c*$ con la quale l’informazione digitale viene trasmessa su una linea (*canale*). È misurata in **bit/s** (o **bps**) o suoi multipli.

Il **tempo** *T* necessario per trasmettere *L* bit dipende dalla velocità di trasmissione. Si ha la relazione:

$$T = \frac{L}{C}$$

Il **ritardo di propagazione** è il tempo $\tau$ affinché un **impulso generato dal trasmettitore** TX **raggiunga il ricevitore** RX. Dipende dalla distanza $*d*$ e dalla velocità di propagazione della luce nel mezzo fisico *v* in metri al secondo. Si ha la relazione:

$$\tau = \frac{d}{v}$$

Per le onde radio, $v = 300000 \frac{km}{s}$ **mentre per la propagazione guidata, $v = 200000 \frac{km}{s}$.

Il **tempo di attraversamento del canale** è quindi:

$$T_{tot} = T + \tau$$

### Modello di un nodo

![Modello di un nodo di rete](../images/base-concepts-Untitled%202.png)

Modello di un nodo di rete

Dato che i nodi in una rete a commutazione di pacchetto devono memorizzare ed elaborare i pacchetti per riuscire a ritrasmetterli verso la loro destinazione, nasce un **ritardo di elaborazione** da aggiungere al ritardo totale.

![Ritardo totale del trasporto di un pacchetto in una rete](../images/base-concepts-Untitled%203.png)

Ritardo totale del trasporto di un pacchetto in una rete

![Ritardo di accomodamento di un pacchetto in una rete](../images/base-concepts-Untitled%204.png)

Ritardo di accomodamento di un pacchetto in una rete

Nel caso la linea d’uscita sia occupata nella trasmissione di un altro pacchetto, il ritardo aumenta, poiché nella commutazione di pacchetto, ogni pacchetto **utilizza completamente le risorse** durante la sua trasmissione per un dato tempo.

### Throughput

È la **quantità di informazione trasportata** (con successo) da una rete o porzione di rete nell’unità di tempo. Si abbrevia con $**THR**$ e si misura in **bit/s**.

Su un collegamento di capacità *C*, si definisce una quantità simile al THR, detta **traffico**, che si calcola come:

$$A = \frac{THR}{C}$$

e si misura in **Erlang**. Assume valori tra 0 e 1 compresi ed è, di fatto, una **misura di efficienza**.

### Perdita

È un indice della **quantità di informazione persa** nell’attraversamento della rete. Può essere riferita ai pacchetti o ai bit (si parla di *tasso di errore sul bit*, o *Bit Error Rate*).

La perdita è determinata da:

- **Ricezione di UI corrotte** (errori di trasmissione)
- **Saturazione dei buffer** lungo il percorso end-to-end

È espressa attraverso una **probabilità** $\pi$:

$$\pi = \frac{\text{UI corrotte}}{\text{UI trasmesse}}$$
