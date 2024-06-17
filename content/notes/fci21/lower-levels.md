---
title: 'Livelli inferiori e LAN'
draft: false
type: 'page'
toc: true
mathjax: true
---

---

Abbiamo visto che i router possono scambiare pacchetti IP attraverso collegamenti e reti locali di tipo eterogeneo, ma non sappiamo come questi pacchetti vengano scambiati *all'interno* delle reti locali.

## Il livello di linea

| Funzionalità | Descrizione |
| --- | --- |
| Framing | Delimitazione delle trame, ossia le UI di livello 2. Identifica logicamente i bit trasportati dal livello fisico. |
| Gestione degli errori | Error detection e uso di ARQ oppure FEC. Può quindi implementare sia la correzione che la ritrasmissione. |
| Indirizzamento |  |
| Multiplazione |  |
| Accesso multiplo | Gestione di diversi host su un mezzo trasmissivo condiviso |

Il livello di linea è normalmente parte della **scheda di rete** (*Network Interface Card*, **NIC**). Insieme al livello fisico, è di solito implementato su un chipset dedicato (controller). Alcune funzionalità, quali la gestione degli indirizzi e la preparazione delle trame, sono svolte in software dall'host.

### Tipi di collegamenti al livello di linea

Esistono fondamentalmente tre tipi di collegamento a livello di linea:

- Point-to-Point connection
- Collegamenti Broadcast
- Collegamenti commutati (variante del Point-to-Point ma con altri elementi di rete locale)

## Collegamenti Point-to-Point

In ricezione, il livello di linea riceve una serie di bit provenienti dal livello fisico. La prima funzione è di individuare il significato logico dei bit scambiati con il livello fisico. Allo scopo, i bit sono raggruppati in una struttura dati di livello due chiamata **trama**.

![Rappresentazione di livello di linea e livello fisico](../images/lower-levels-Untitled.png)

Rappresentazione di livello di linea e livello fisico

Occorre identificare la posizione delle varie trame all'interno del flusso continuo di bit. Per questo si usano i **delimitatori di trama**, una particolare stringa di bit, detti **flag**. I flag sono particolari sequenze di bit che permettono di individuare l'allineamento di trama.

Nel protocollo di linea HDLC, il flag usato all'inizio ed alla fine di una trama è la sequenza `01111110`.

Come si può impedire una casuale presenza della sequenza flag nella trama? Si usa la tecnica di **bit stuffing** (in HDLC): prima di aggiungere i flag, si inserisce un bit 0 dopo aver osservato cinque bit 1 consecutivi. Alla decodifica della trama, si rimuovono i flag e si procede con il **bit destuffing**, che elimina gli 0 aggiunti precedentemente.

### Gestione degli errori

A livello due, si possono implementare due tecniche per la gestione degli errori:

- Rilevazione e correzione di errori con codici di tipo Forward Error Correction
- Rilevazione di errore e ritrasmissione con protocolli Automatic Repeat reQuest

L'ARQ a livello di linea è usato principalmente per il recupero degli errori di livello fisico. Per questo scopo si usa un campo della trama chiamato in genere **FCS** (*Frame Check Sequence*).

### Multiplazione

Nei collegamenti punto-punto, i protocolli di linea possono essere istanziati su più canali fisici. In questi casi, un canale viene diviso in più sotto-canali al livello fisico. Quest'operazione viene definita **multiplazione fisica** e serve a suddividere la capacità di un canale a velocità costante in sottocanali di velocità inferiore ma sempre costante.

Le modalità operative della multiplazione fisica sono:

- Multiplazione a divisione di spazio (**SDM**)
    
    L'esempio tipico è un cavo a coppie usato per concentrare i doppini utente in telefonia o in cavi che portano diverse fibre ottiche.
    
    ![Cavo telefonico che raggruppa doppini utente](../images/lower-levels-Untitled%201.png)
    
    Cavo telefonico che raggruppa doppini utente
    
    ![Cavo che trasporta molteplici connessioni a fibra ottica](../images/lower-levels-Untitled%202.png)
    
    Cavo che trasporta molteplici connessioni a fibra ottica
    
- Multiplazione a divisione di frequenza (**FDM**)
    
    Equivalente alla multiplazione di lunghezza d'onda.
    
    Il mezzo trasmissivo è caratterizzato da un insieme di frequenze utilizzabili. La banda complessiva può essere divisa in sotto-bande cui associare i vari canali. Spesso si usano bande di guardia per avere un margine di sicurezza nella separazione dei canali.
    
    ![Divisione in canali nella multiplazione a divisione di frequenza](../images/lower-levels-Untitled%203.png)
    
    Divisione in canali nella multiplazione a divisione di frequenza
    
    Alcuni esempi sono la radio FM, la TV Digitale, l'ADSL.
    
- Multiplazione a divisione di tempo (**TDM**)
    
    L'intera risorsa trasmissiva è messa a disposizione degli utenti, che la utilizzano alternandosi nel tempo con periodicità $T$. Ciascun canale è associato ad uno *slot* temporale in cui è il solo a trasmettere. Spesso si usano tempi di guardia per avere un margine di sicurezza nella separazione dei canali.
    
    ![Separazione in canali nella multiplazione a divisione di tempo](../images/lower-levels-Untitled%204.png)
    
    Separazione in canali nella multiplazione a divisione di tempo
    
    Alcuni esempi sono la rete telefonica digitale, il sistema GSM.
    
    Per la multiplazione TDM si definiscono le *trame* (non la UI di livello 2):
    
    - Slot organizzati in trame di uguale lunghezza (durata $T$)
    - Esecuzione di opportuna strategia di allineamento
    - *Parola* di allineamento in posizione prefissata
    
    La delimitazione delle UI è implicita, basata su istanti di inizio e fine slot. Con questa struttura, anche l'indirizzamento delle UI è implicito, perché si basa sulla posizione dello slot nella trama.
    
    ![Trame in TDM](../images/lower-levels-Untitled%205.png)
    
    Trame in TDM
    
    I bit di $N$  flussi vengono raccolti in code e trasmessi sul canale d'uscita a gruppi di $K$ (**interlacciamento** di $K$ bit). Ogni gruppo di $K$ bit è trasmesso in un dato *slot* temporale, che si ripetono ciclicamente nelle *trame*.
    
    ![Interlacciamento di 2 bit in TDM](../images/lower-levels-Untitled%206.png)
    
    Interlacciamento di 2 bit in TDM
    
    La durata della trama deve eguagliare l'intervallo di tempo in cui sul singolo canale (*tributario*) in entrata arrivano un numero di bit pari a quelli trasmessi nello slot della trama dedicato a quel flusso.
    
    ![../images/lower-levels-Untitled%207.png](../images/lower-levels-Untitled%207.png)
    
    I **tributari** sono gli utenti connessi che stanno sfruttando la rete.
    
    La **frequenza di cifra** del segnale multiplato è pari a:
    
    $$\begin{aligned}
    f_m &= {L_m \over T} =\\&= {N\cdot L_C + L_a \over T} =\\&=N\cdot f_C +f_a
    \end{aligned}$$
    
    L'assegnazione dei canali può essere:
    
    - A slot singolo: a ciascun utente viene assegnato uno slot: $f_C = {L_C \over T}$
    - A slot multiplo: **sovramultiplazione**: $f_C = n{L_C\over T}, 1\leq n\leq N$
    - A frazione di slot: **sottomultiplazione**: $f_C = {n\over T}$
- Multiplazione a divisione di lunghezza d'onda (**WDM**)
- Multiplazione a divisione di codice (**CDM**)

### Duplexing

Una canale di comunicazione unidirezionale ha un tipo di trasmissione **simplex**. Nel caso di un canale di comunicazione bidirezionale, la trasmissione può essere:

- **Half duplex**: la trasmissione avviene alternativamente in una direzione o nell'altra (in ogni istante è *simplex*)
- **Full Duplex**: la trasmissione avviene contemporaneamente nelle due direzioni

Il **duplexing** è la tecnica di multiplazione utilizzata per condividere il mezzo fisico nelle due direzioni. Per metterlo in atto si usano il *Frequency Division Duplexing* (**FDD**) o il *Time Division Duplexing* (**TDD**).

![Collegamento simplex](../images/lower-levels-Untitled%208.png)

Collegamento simplex

![Collegamento duplex](../images/lower-levels-Untitled%209.png)

Collegamento duplex

---

## Collegamenti broadcast

### Gli esordi delle reti locali (anni '70)

All'inizio della storia di Internet, quando i nodi della rete ARPANET gestivano collegamenti dell'ordine di poche decine di kbps, esistevano già reti locali con velocità dell'ordine dei Mbps.

La funzione di rete è un'operazione che richiede capacità computazionale:

- Analisi dell'header
- Lookup della tabella di instradamento
- Inoltro alla coda di uscita
- Gestione della coda

Il segreto che rendeva le LAN più veloci era il canale broadcast, che inviava i pacchetti a tutti gli host collegati.

Le prime reti locali furono **Ethernet** (1976) ed **AlohaNET** (1971). La prima utilizzava cavi coassiali, la seconda era una rete wireless.

Le reti broadcast oggi sono principalmente **Wi-Fi** e **Passive Optical Networks** (che utilizza fibra ottica e splitter o accoppiatore ottico, lo *star-coupler*).

### Topologie di rete broadcast

- **Bus**
    
    Mezzo fisico condiviso con trasmissione bidirezionale. Le stazioni sono solo sorgenti o destinazioni di UI.
    
- **Stella**
    
    Connessioni bidirezionali, stazioni solo sorgenti o destinazioni. Il centro stella agisce come snodo delle informazioni. I centri stella sono solitamente composti da hub (reti wired) o stazioni radio base (reti wireless)
    
- **Anello**
    
    Trasmissione unidirezionale in cui ogni nodo ritrasmette anche le UI di altri stazioni.
    

I problemi con il canale broadcast sono generalmente:

- La **ricezione**: tutti ricevono il segnale, solo il destinatario analizza il contenuto della trama. È necessario un opportuno indirizzamento anche a livello di linea
- La **trasmissione**: tutti trasmettono sullo stesso mezzo fisico condiviso. È necessario garantire l'accesso multiplo dei vari utenti allo stesso mezzo.

### Accesso multiplo

L'accesso multiplo è la funzione che consente di regolare l'accesso al canale ed evitare collisioni.

La funzione di accesso multiplo può essere implementata:

- **A livello fisico**, dividendo staticamente le risorse fra gli host.
    
    L'accesso multiplo fisico è equivalente alla multiplazione, ma è relativo al caso in cui i diversi sottocanali sono gestiti da trasmettitori diversi.
    
    | Sigla | Nome | Descrizione |
    | --- | --- | --- |
    | FDMA | Frequency Division Multiple Access | Equivalente alla multiplazione FDM. Usata da canali Wi-Fi, canali cellulari. |
    | TDMA | Time Division Multiple Access | Equivalente alla multiplazione TDM. Vengono definiti degli slot temporali dedicati alla trasmissione dei dati di un utente. Il flusso di bit fra i vari utenti generalmente non è sincrono. Il ricevitore deve sincronizzarsi su un particolare flusso e vanno adottati dei tempi di guardia fra gli slot. Il tempo di guardia va dimensionato al massimo ritardo di propagazione della rete |
    | CDMA | Code Division Multiple Access | Alcune stazioni possono condividere lo stesso slot temporale e la stessa banda trasmissiva. La distinzione avviene tramite opportuni codici ortogonali (chip). Il vantaggio è il maggiore utilizzo delle risorse, lo svantaggio è la maggiore complessità del sistema. Viene usato da UMTS. |
- **A livello di linea**, gestendo l'accesso pacchetto per pacchetto.
    
    L'obiettivo di questi protocolli è regolare l'istante di inizio trasmissione delle singole trame.
    
    IL coordinamento può essere gestito da un'entità centrale, ma molto più spesso è gestito in modo distribuito dalle singole stazioni. Ciascuna stazione decide autonomamente quando iniziare la trasmissione.
    
    In questi casi, il livello di linea è diviso in due sotto livelli:
    
    - **MAC**: *Medium Access Control*
    - **LLC**: *Logical Link Control* (ora quasi in disuso)
    
    Una stazione che ha una trama da trasmettere decide autonomamente quando iniziare la trasmissione. Se avviene una **collisione**, la trasmissione non va a buon fine e così le stazioni coinvolte ritrasmettono **dopo un tempo casuale**. La casualità consente *con buona probabilità* che la collisione non si ripresenti.
    
    | Nome | Descrizione | Funzionamento |
    | --- | --- | --- |
    | ALOHA | Primo protocollo di accesso multiplo a contesa, studiato ed utilizzato in AlohaNET. | Una stazione che ha un pacchetto da trasmettere lo trasmette subito, senza osservare il canale. Se avviene una collisione, il pacchetto viene ritrasmesso dopo un tempo casuale. La collisione è identificata dalla mancanza di un ACK entro un tempo ⁍ (due volte il ritardo di propagazione tra sorgente e destinazione). Il ritardo per la ritrasmissione viene calcolato con un algoritmo di backoff, calcolato come multiplo ⁍ di un tempo di trasmissione base ⁍ di una trama, dove ⁍. |
    | Slotted ALOHA | Variante di ALOHA più raffinata. | Equivalente ad ALOHA, ma invece di trasmettere immediatamente il pacchetto, si attendono degli istanti discreti predefiniti (slot). Generalmente, la durata dello slot è pari al tempo di trasmissione di una trama. Tutte le stazioni sono sincronizzate, perciò, se due o più stazioni trasmettono contemporaneamente, le loro trasmissioni sono completamente sovrapposte. |
    | Carrier Sense Multiple Access (CSMA) | Controlla il canale per vedere se può trasmettere. | Una stazione che ha una trama da trasmettere verifica che il canale sia libero, rilevando la presenza di segnale a livello fisico. Se il canale è libero, la stazione trasmette la trama. Altrimenti la trasmissione è rimandata ripetendo lo stesso sensing dopo un tempo casuale. In altre implementazioni, la stazione resta in ascolto e trasmette appena il canale si è liberato (CSMA Persistent). La trasmissione viene riprogrammata (rescheduling) con l'algoritmo di backoff (come in ALOHA). |
    | Slotted Carrier Sense Multiple Access | Equivalente a CSMA, ma con slot temporali. | Il tempo di durata di uno slot è pari al ritardo di propagazione ⁍. Il rescheduling può avvenire in momenti diversi a seconda del tipo di CSMA: nel non-persistent, la trasmissione viene spostata a dopo; nel 1-persistent, il protocollo rimane in ascolto sul canale e cerca di trasmettere comunque finché non viene liberato il canale. |
    | Carrier Sense Multiple Access - Collision Detection | Equivalente a CSMA, ma anche le stazioni che trasmettono possono accorgersi della collisione. Si dice anche CSMA listen while talking. | Quando una stazione si accorge di una collisione, smette di trasmettere per risparmiare tempo e risorse. Rilevando la collisione, la trasmissione viene interrotta e si invia un segnale di jam di durata ⁍. Il ritardo di propagazione deve essere inferiore al tempo di trasmissione. Questa tecnica riduce l'intervallo di collisione ed elimina la necessità di avere ACK. L'unico modo per rilevare correttamente una collisione sui collegamento è avere una trama dimensionata in modo tale che ⁍, quindi ⁍. |
    
    ### Efficienza dei protocolli
    
    - **Slotted ALOHA**
        
        <aside>
        📌 **Periodo di vulnerabilità**: periodo in cui può avvenire una collisione sullo stesso slot.
        
        </aside>
        
        Se due o più stazioni decidono di trasmettere in questo periodo di tempo, avverrà una collisione. 
        
        La probabilità che la trasmissione abbia successo, date $N$ stazioni ed ogni stazione trasmette in uno slot con probabilità $p$, è:
        
        $$P_S = (1-p)^{N-1}$$
        
        Dunque, avendo $N$ stazioni, il numero medio di trasmissioni con successo, che chiamiamo **throughput** è:
        
        $$ ⁍$$
        
        Il numero medio di trasmissioni sul canale, che chiamiamo **traffico**, è dato da $G = Np$. Sostituendo nella formula del throughput, si ha:
        
        $$⁍$$
        
        Ma allora:
        
        $$\lim_{N\to \infty}S = Ge^{-G} \approx 0.37$$
        
        La massima efficienza di Slotted ALOHA è $37\%$.
        
    - **ALOHA**
        
        Senza slot, l'analisi è simile a quella per Slotted ALOHA, ma ora sono possibili anche collisioni con sovrapposizione parziale. Quindi abbiamo un periodo di vulnerabilità pari a $2T$. Ciò implica che, ragionando analogamente a prima:
        
        $$\lim_{N\to\infty}S = Ge^{-2G} \approx 0.18$$
        
        Quindi l'efficienza di ALOHA è del $18\%$.
        
    - **CSMA**
        
        Il periodo di vulnerabilità, nel caso di CSMA, dipende dal **ritardo di propagazione** delle connessioni.
        
        Analizzando questo protocollo, troviamo che il throughput è pari a:
        
        $$S = {Ge^{-aG}\over G(1+2a)+e^{-aG}}, \ a = {\tau \over T}$$
        
        Perciò notiamo come il throughput è tanto maggiore quanto è più grande il ritardo di propagazione tra le stazioni.
        
    - **CSMA-CD**
        
        Il throughput è:
        
        $$S = {Ge^{-aG} \over G(1+2a)+e^{-aG} - G(1-\gamma)(1-e^{-aG})}$$
        
    
    ### Problemi con il collision detection
    
    Il collision detection si basa sul fatto che, nelle reti locali cablate come Ethernet, l'attenuazione del segnale è piccola ed il livello di segnale ricevuto dalle altre stazioni è simile al proprio. Ci si può accorgere facilmente della presenza di altre trasmissioni.
    
    Nelle reti radio wireless, il mezzo attenua molto e quindi non è più possibile usare il collision detection. La soluzione è il CSMA con **Collision Avoidance**.
    

### Duplexing ed accesso multiplo

È analogo al duplexing della multiplazione.

Le tecniche di suddivisione della capacità trasmissiva nei due versi sono:

- Divisione di spazio
- FDD
- TDD

Un esempio sono downlink ed uplink di reti cellulari.

---

## LAN

IEEE è il principale organismo di standardizzazione delle tecnologie per reti locali con il progetto IEEE 802.

IEEE 802 ha standardizzato diverse tecnologie, tra cui:

- Il sottostrato LLC
- Il sottostrato MAC
- Il livello fisico per ogni tecnologia di rete

![Standard IEEE 802 divisi per strati di rete](../images/lower-levels-Schermata_2021-05-28_alle_08.50.11.png)

Standard IEEE 802 divisi per strati di rete

### IEEE 802.2: Sottostrato LLC

Il sottostrato LLC offre tre tipi di servizi:

![Funzioni di livello di linea e fisico](../images/lower-levels-Schermata_2021-05-28_alle_08.52.05.png)

Funzioni di livello di linea e fisico

- **Type 1** (default): puro incapsulamento, nessuna funzione aggiunta a MAC
- **Type 2**: controllo di connessione con ARQ (rende IEEE 802 uguale al vecchio HDLC)
- **Type 3**: equivalente al Type 1, ma con riscontro delle trame

LLC è poco usato nella pratica, la maggior parte delle funzioni è stata delegata al livello MAC.

### Sottostrato MAC

Il sottostrato MAC risolve problemi specifici di ciascuna tecnologia LAN legati all'utilizzo del sistema trasmissivo fisico per trasmettere le trame del livello di linea.

Si può considerare *a cavallo* tra livello fisico e di linea.

Esistono venti diverse tecnologie (da IEEE 802.3 a IEEE 802.22). Le più importanti sono:

- **IEEE 802.3**: CSMA-CD Access Method (Ethernet)
- **IEEE 802.11**: WLAN
- **IEEE 802.15**: WPAN (*Wireless Personal Area Network*)
    - **IEEE 802.15.1**: Bluetooth
    - **IEEE 802.15.4**: ZigBee

| Name | Dimensione (bit) | Descrizione |
| --- | --- | --- |
| Destination Address | 48 | Indirizzo MAC di destinazione |
| Source Address | 48 | Indirizzo MAC della sorgente |
| Pacchetto LLC |  | Di lunghezza variabile, contiene anche un header LLC |
| Frame Check Sequence | 32 | Simile ad un checksum |

Nella struttura della UI ci sono anche altri campi che dipendono dal tipo di MAC utilizzato.

Gli indirizzi di destinazione possono essere di tre tipi:

- **Unicast**: individuano un singolo host
- **Multicast**: individuano più host
- **Broadcast**: individuano tutti gli host di una rete fisica

Quando una scheda MAC riceve una trama ne verifica l'integrità ed analizza l'indirizzo di destinazione. La trama verrà trasferita ai livelli superiori nei casi in cui l'indirizzo di destinazione è:

- Broadcast
- Unicast con indirizzo uguale a quello della scheda ricevente
- Multicast con indirizzo della scheda ricevente nel gruppo

#### Indirizzi MAC

Gli indirizzi di rete locale sono detti **indirizzi MAC** o **indirizzi fisici**. Servono per la funzione di filtraggio.

Sono lunghi 48 bit e sono solitamente indicati con la notazione esadecimale.

L'indirizzo di broadcast è l'indirizzo MAC con 48 bit a 1. In esadecimale: `FF:FF:FF:FF:FF:FF`.

Originariamente, l'indirizzo MAC era *cablato* ****nella ROM della NIC. Oggi può invece essere riconfigurato.

Un indirizzo MAC è formato da sei ottetti, ognuno rappresentante un Byte dell'indirizzo.

Solitamente, se il penultimo bit del primo ottetto è impostato a 1, i primi 3 Byte dell'indirizzo identificano il **costruttore** (**OUI**, *Organizationally Unique Identifier*), mentre gli ultimi tre identificano la **scheda** (**NIC**).

![Organizzazione in ottetti dell'indirizzo MAC](../images/lower-levels-Untitled%2010.png)

Organizzazione in ottetti dell'indirizzo MAC

### IEEE 802.3: Ethernet

Nasce come un progetto di tre aziende negli anni '70: Digital, Intel e Xerox (**DIX**). Successivamente, nel 1985, viene standardizzata come IEEE 802.3

Le caratteristiche di questa tecnologia sono:

- Topologia a bus
- Capacità della rete: $10\  \text{Mbps}$
- Metodo di accesso: CSMA-CD

| Campo | Dimensione (byte) | Descrizione |
| --- | --- | --- |
| Preambolo | 7 | Consente la sincronizzazione in ricezione |
| Start Frame Delimiter | 1 | Individua l'inizio della trama |
| Destination Address | 6 | Indirizzo MAC di destinazione |
| Source Address | 6 | Indirizzo MAC sorgente |
| Length/Type | 2 | Lunghezza del campo payload o Ether Type |
| Data |  | Lunghezza variabile |
| Pad |  | Grantisce la lunghezza minima della trama (64 Byte) per il CSMA-CD |
| Frame Check Sequence | 4 | Usato per il controllo d'errore |

#### Funzioni dello strato MAC

- **Trasmissione e ricezione trame**
    
    In trasmissione, il MAC riceve l'unità informativa dal livello superiore e genera una stringa seriale da trasmettere sul mezzo fisico.
    
    In ricezione, il MAC riceve una stringa seriale di bit sul mezzo fisico e fornisce l'unità informativa al livello superiore.
    
    Esiste una spaziatura minima tra trame trasmesse, chiamata inter-frame gap. Le trame più corte della lunghezza minima vengono automaticamente scartate.
    
- **Gestione del Frame Check Sequence**
    
    Il MAC genera il campo FCS per le trame da trasmettere e controlla la correttezza del FCS nelle trame ricevute.
    
- **Gestione del preambolo e del Start Frame Delimiter**
    
    Il MAC genera il preambolo e lo SFD per le trame da trasmettere e li rimuove nelle trame ricevute.
    

#### Accesso multiplo

Il metodo di accesso scelto per Ethernet è il CSMA-CD.

Quando avviene una collisione, il MAC interrompe la trasmissione e genera un segnale di jamming di 32 bit per segnalarla. Poi riprogramma la trasmissione con l'algoritmo di backoff, al massimo per 16 volte.

Il ritardo scelto è un multiplo intero $iT$ dello slot di tempo $T$, il quale dipende dalla capacità della rete. $i$ è un numero casuale tale che $i \in\big[0, K-1\big]$. $K = 2^k,\  k=\min(n,10)$ dopo $n$ collisioni.

#### Topologie di rete e mezzi fisici

Le topologie fisiche delle reti Ethernet erano in origine soltanto a bus, ma sono stati introdotti dei dispositivi che hanno permesso di creare reti a stella.

Dal punto di vista logico, Ethernet usa topologie sempre a bus.

I mezzi fisici usati da Ethernet sono:

- **Rame**
    - 10Base5: coassiale thick (RG-213)
    - 10Base2: coassiale thin (RG-58)
    - 10Base-T: doppino (RJ-45)
- **Fibra**
    - 10Base-FB: standard con caratteristiche di fault tolerance
    - 10Base-FL: fibra ottica
    - 10Base-FP: utilizzo dei dispositivi ottici passivi

Il primo numero indica il bit rate, la parola *Base *****indica che la trasmissione dei dati a livello fisico è fatta in banda base, mentre il secondo numero indica la massima distanza tra due stazioni:

- 2 indica massimo $200\text m$
- 5 indica massimo $500\text m$

In alcuni casi, quali 10BaseT, l'ultima lettera indica il tipo di mezzo trasmissivo. Nello specifico, T indica *twisted pair*, ed identifica i doppini in rame usati ancora oggi.

Il mezzo fisico adottato inizialmente negli anni '70 era un cavo coassiale passivo (BUS) a cui si connettevano le stazioni tramite un *transceiver* (trasmettitore e ricevitore).

![Struttura di rete fisica a bus con cavi coassiali, anni '70](../images/lower-levels-Untitled%2011.png)

Struttura di rete fisica a bus con cavi coassiali, anni '70

![HUB e cavi *twisted pairs*](../images/lower-levels-Schermata_2021-05-28_alle_09.38.38.png)

HUB e cavi *twisted pairs*

A partire da metà anni '90, i BUS con cavo coassiale sono stati sostituiti da topologie a stella, basate su *ripetitori di segnale a livello fisico multi-porta*, denominati **HUB**. Il mezzo trasmissivo è rimpiazzato dai doppini in rame (*twisted pairs*).

[Tipi di doppini in rame](https://www.notion.so/4b5edc70740b4967826805b92e41a4f2)

#### IEEE 802.3u: Fast Ethernet

A fine anni '90, il rate di trasmissione viene aumentato da $10 \ \text{Mbps}$ a $100 \ \text{Mbps}$ con **Fast Ethernet**.

Indica le reti con standard 100BaseT: la velocità aumenta di 10 volte, raggiungendo i $100 \ \text{Mbps}$.

Oltre ai doppini in rame, si usano anche i cavi in fibra ottica (100BaseFX).

#### Gigabit Ethernet

Nei primi anni 2000 il rate di trasmissione viene aumentato fino a $1 \ \text{Gbps}$ e poi a $10 \ \text{Gbps}$ a metà anni 2000 con 10-Gigabit Ethernet.

I mezzi trasmissivi sono utilizzati sono vari: doppini di diversi tipi, fibre ottiche monomodali e multimodali ($40 \ \text{Gbps}$ e $100 \ \text{Gbps}$ sono già standard). Si usano principalmente le fibre ottiche, il doppino di rame viene mantenuto ma solo per distanze molto ravvicinate.

Oggi si va verso la standardizzazione del $\text{Tbps}$. I collegamenti $400 \ \text{Gbps}$ sono già commerciali.

### IEEE 802.11: Wireless LAN

La tecnologia Wi-Fi è standardizzata dal gruppo di lavoro IEEE 802.11. Rappresenta la versione Wireless di Ethernet usata per reti locali ed è largamente usata.

Esistono molte versioni di livello fisico che operano a velocità e bande di frequenze diverse.

[Versioni di Wireless Ethernet](https://www.notion.so/213764984c7d4184bbce9fbaf32d2a5c)

#### Struttura di rete

Esistono fondamentalmente due strutture di rete per le WLAN:

- **Basic Service Set** (**BSS**)
    - Stazioni mobili in mutua comunicazione
    - Modalità
        - Access Point (**AP**)
        - Rete ad-hoc
- **Extended Service Set** (**ESS**): diversi BSS messi in comunicazione tramite un **Distribution System** (**DS**), che può essere sia wired che wireless

#### Accesso al mezzo condiviso

Anche se il mezzo è condiviso, l'elevata attenuazione dei segnali tipica del canale wireless determina un raggio di copertura di ciascuna stazione. Per questo, il protocollo di accesso CSMA-CD non può essere utilizzato per il problema della *stazione nascosta*.

Poiché manca la certezza di poter rilevare le collisioni, è necessario l'uso di ACK. Per le connessioni wireless è stato studiato un nuovo protocollo di accesso: **CSMA-CA** (*Carrier Sense Multiple Access, Collision Avoidance*).

#### CSMA Collision Avoidance

Il funzionamento di questo nuovo protocollo segue principalmente tre passaggi:

1. Il mittente invia un'esplicita richiesta di autorizzazione a trasmettere (**RTS**, *Request To Send*)
2. Il destinatario risponde con un'esplicita autorizzazione (**CTS**, Clear To Send)
3. Viene richiesto un ACK per ogni trama ricevuta correttamente

![Esempio di comunicazione con CSMA-CA](../images/lower-levels-Untitled%2012.png)

Esempio di comunicazione con CSMA-CA

Per far sì che le collisioni possano avvenire soltanto fra RTS, sono stati creati dei time frame specifici tra invio e ricezione dei pacchetti:

- **DIFS**: Distributed Coordination Function Interframe Space
- **SIFS**: Short Interframe Space

Vale la relazione $\text{SIFS} < \text{DIFS}$.

Se la sorgente riceve il CTS, prosegue con la trama dati.

#### Collision Avoidance con Backoff

Se il canale è occupato al momento della trasmissione, si resta in ascolto fino a canale libero e poi si aspetta un intervallo di tempo pari a $\text{DIFS } + \text{ Backoff}$ , dove il backoff è un numero di slot scelto casualmente.

Se il canale si occupa durante il backoff, il conteggio del backoff si ferma e riprende quando il canale diventa libero.

Quando devono essere trasmesse delle trame consecutive, il DIFS e l'eventuale backoff viene comunque applicato, anche se il canale è libero.

In caso di collisioni, l'intervallo di backoff è scelto in un intervallo più ampio, per ridurre la probabilità di ulteriori collisioni, come in CSMA-CD.

![Esempio di messa in atto di backoff in CSMA-CA](../images/lower-levels-Untitled%2013.png)

Esempio di messa in atto di backoff in CSMA-CA

#### Accesso in modalità Point Coordination Function

Oltre che in modo distribuito (**DCF**), l'accesso al mezzo può essere gestito in modo centralizzato (**PCF**).

In questo caso, una stazione agisce da **Point Coordinator** (**PC**):

- Controlla centralmente l'accesso al mezzo trasmissivo dando alle varie stazioni l'autorizzazione esplicita a trasmettere.
- Attiva la modalità PCF con invio di trama speciale dopo un tempo **PIFS** (*PCF Interframe Space*) tale che $\text{SIFS} < \text{PIFS} < \text{DIFS}$. Ciò garantisce che non possa iniziare la finestra di contesa per trame *normali* (per queste è richiesta l'attesa di un intervallo di tempo DIFS) ma possono essere inviati prima CTS o ACK (dopo un tempo SIFS) perché hanno priorità più alta.
- Interroga (*poll*) le singole stazioni che rispondono (dopo un intervallo SIFS)

![Tempistiche della modalità PCF](../images/lower-levels-Untitled%2014.png)

Tempistiche della modalità PCF

### IEEE 802.15: Wireless Personal Area Networks (WPAN)

Le WPAN sono reti che connettono dispositivi di comunicazione a corto raggio. Non necessitano di un grande dispendio di energia per funzionare e sono relativamente economiche da implementare. Creano uno *spazio operativo personale*.

Alcuni tipi di aree personali potrebbero essere:

- Access Point per scambio dati o linea telefonica digitale
- Connettività ad-hoc personale
- Rimpiazzo per i cavi (mouse e tastiere wireless, per esempio)

Le WPAN sono state definite dal gruppo di lavoro 802.15, per agevolare la standardizzazione del Bluetooth nel periodo in cui veniva sviluppato. Il LLC usato da tutte le WPAN è lo stesso definito nel gruppo 802.2.

Alcuni gruppi di lavoro specifici sono:

- **802.15.1**: Bluetooth™, usa una banda da 2.4 GHz ed ha un rate di trasmissione di $1 \text{ Mbps}$
- **802.15.3**: riunisce tecnologie di WPAN-HR (*High Rate*), che trasmettono dati ad un rate molto maggiore di $1 \text{ Mbps}$
- **802.15.4**: riunisce tecnologie di WPAN-LR (*Low Rate*), che trasmettono dati ad un rate molto minore di $1 \text{ Mbps}$

#### IEEE 802.15.1: Bluetooth

Bluetooth è una specifica industriale per le WPAN. Il gruppo di lavoro 802.15.1 ha adattato le specifiche industriali del Bluetooth per i livelli 1 e 2.

| Anno | Evento |
| --- | --- |
| 1996/1997 | Il Bluetooth viene sviluppato come un progetto interno alla Ericsson |
| 1998 | Nasce il Bluetooth SIG (Special Interest Group), formato da Ericsson, IBM, Intel, Toshiba e Nokia |
| 1999 | Nuovi membri del SIG: 3Com, Lucent Tecnologies, Microsoft, Motorola |

Il nome ed il logo di Bluetooth derivano dal re danese Harald Blaatand II, conosciuto come *Dente blu* (*blue tooth*), vissuto tra il 940 ed il 981. Ha unificato la Danimarca e la Svezia.

Il Bluetooth ha le seguenti caratteristiche:

- Usa tecnologia radio con bande ISM da 2.4 GHz
- È a basso costo
- È una tecnologia a corto raggio
- È piuttosto semplice da implementare
- I moduli Bluetooth sono di dimensione contenuta

Il Bluetooth ha vari scenari d'applicazione, quali:

- Headset wireless
- Sincronizzazione dati tra dispositivi vicini
- Può connettere dispositivi utente ad Access Point

L'architettura di rete più semplice definita dallo standard del Bluetooth è la **Piconet**: un network ad-hoc composto da due o più dispositivi.

Uno dei dispositivi è il **master**, mentre gli altri vengono definiti **slave**. La comunicazione può avvenire soltanto tra master e slave, mai tra slave.

In una Piconet possono esserci fino a 7 slave attivi contemporaneamente. Gli altri possono essere in due stati:

- **Stand-by**: non fanno parte della Piconet.
- **Parked**: fanno parte della Piconet, ma non sono attivi. Possono coesistere in questo stato fino a 256 dispositivi.

I dispositivi facenti parte della Piconet hanno tutti indirizzi MAC da 48 bit, oltre a:

- Un **Active Member Address** (**AMA**) di 3 bit se sono dispositivi attivi nella Piconet
- Un **Parked Member Address** (**PMA**) di 8 bit se sono dispositivi *parcheggiati *****nella Piconet

A livello fisico, Bluetooth fa uso di bande ISM a 2.4 GHz, con 79 canali a distanza ciascuno di 1 MHz (da 2402 a 2480 MHz) ed una modulazione di tipo G-FSK, che raggiunge bitrate di 1 Mbps.

A seconda della potenza del modulo Bluetooth, si distinguono tre classi di dispositivi:

| Classe | Potenza (mW) | Raggio (m) |
| --- | --- | --- |
| Class 1 | 100 | 100 |
| Class 2 | 2.5 | 10 |
| Class 3 | 1 | 1 |

La tecnologia Bluetooth permette l'uso del **Frequency Hopping** (**FH**), con un rate di 1600 hop al secondo. La frequenza FH è pseudo-casuale e viene determinata dal master, che regola l'accesso al canale. Gli altri dispositivi seguono la sequenza $f_k$ definita dal master.

![Frequency Hopping in Bluetooth](../images/lower-levels-Untitled%2015.png)

Frequency Hopping in Bluetooth

![Tempistiche di trasmissione tra master e slave in Bluetooth](../images/lower-levels-Untitled%2016.png)

Tempistiche di trasmissione tra master e slave in Bluetooth

La trasmissione si alterna tra master e slave. Soltanto uno può trasmettere in ogni periodo.

È anche possibile trasmettere pacchetti con durata di 1, 3 o 5 intervalli temporali.

![Trasmissione di un pacchetto di durata pari a 3 intervalli](../images/lower-levels-Untitled%2017.png)

Trasmissione di un pacchetto di durata pari a 3 intervalli

![Trasmissione di un pacchetto di durata pari a 5 intervalli](../images/lower-levels-Untitled%2018.png)

Trasmissione di un pacchetto di durata pari a 5 intervalli

| Campo | Dimensione (Byte) | Descrizione |
| --- | --- | --- |
| Access code | 72 | Usato per la sincronizzazione e per l'identificazione della Piconet |
| Header | 54 | Usato per il Link Control (LC), che include anche lo schema di ritrasmissione |
| Payload | 2745 | Ha una dimensione variabile (a fianco è indicata la massima) ed il suo formato dipende dal tipo di connessione e dal tipo di pacchetto (numero di slot, PHY protection...) |

#### IEEE 802.15.4: ZigBee

ZigBee è un altro standard per WPAN con un costo di hardware e software molto basso (circa 2$), bassa latenza, raggio limitato, alta efficienza energetica. La differenza con il Bluetooth è che la stack di protocolli implementata non è IP-compliant.

![Stack protocolli ZigBee](../images/lower-levels-Untitled%2019.png)

Stack protocolli ZigBee

La tecnologia ZigBee nasce a metà anni '90 a causa delle troppe soluzioni proprietarie per il campo dell'Internet of Things. All'epoca, i problemi di compatibilità ed interoperabilità erano dilaganti e le tecnologie erano ad alto costo.

Per risolvere questo problema, l'IEEE ha creato il gruppo di lavoro 4 nel 2001 per raggiungere una tecnologia di riferimento. Lo standard IEEE 802.15.4 è stato pubblicato nel Marzo 2003 e la tecnologia è spesso erroneamente identificata con il nome ZigBee.

I tipi di dispositivi previsti dallo standard sono:

- **PAN Coordinator**
    - È responsabile di una Personal Area Network
    - Controlla l'associazione e la dissociazione nelle PAN
- **Full Function Device** (**FFD**)
    - Può inviare beacon
    - Può comunicare con altri FFD
    - Può instradare trame
    - Può fungere da coordinatore PAN
    - Generalmente ha una fonte di energia propria
- **Reduced Function Device** (**RFD**)
    - Non può instradare trame
    - Non può comunicare con altri RFD
    - Può comunicare solo con FFD
    - Viene generalmente alimentato da batterie

Le topologie supportate da ZigBee sono:

- A stella
- A maglia
- Cluster-Tree (non ufficialmente inclusa nello standard 802.15.4)

![Esempio di topologia a stella](../images/lower-levels-Untitled%2020.png)

Esempio di topologia a stella

![Esempio di topologia a maglia](../images/lower-levels-Untitled%2021.png)

Esempio di topologia a maglia

![Esempio di topologia Cluster-Tree](../images/lower-levels-Untitled%2022.png)

Esempio di topologia Cluster-Tree

![Caratteristiche del livello fisico di ZigBee](../images/lower-levels-Untitled%2023.png)

Caratteristiche del livello fisico di ZigBee

A livello fisico, ZigBee implementa:

- 3 canali disponibili in bande da 868 MHz
- 30 canali disponibili in bande da 915 MHz
- 16 canali disponibili nelle bande da 2.4 GHz

Sono definite, a livello fisico, due modalità:

1. **Beacon Enabled**
    - Il PAN Coordinator trasmette periodicamente dei beacon
    - Generalmente adottato nelle topologie di rete a stella
    - Il protocollo di accesso usato è lo Slotted CSMA-CA con trasmissioni programmate
2. **Non Beacon Enabled**
    - Accesso non coordinato con Unslotted CSMA-CA

---

## Collegamenti commutati

### Apparati di interconnessione di LAN

Finora abbiamo visto LAN con livello di linea broadcast. 

Le LAN odierne sono più complesse in quanto possono essere costituite da molteplicità di apparati. In tal caso si parla di **LAN Commutate** (o anche **Switched**).

L'interconnessione di apparati può avvenire a diversi livelli:

- **Repeater** o **Hub**: operano a livello 1 e sono semplici ripetitori di segnali. Non leggono indirizzi e non interpretano il significato dei bit.
- **Bridge** o **Switch**: operano a livello 2. Hanno algoritmi di instradamento semplici e si usano normalmente per interconnesioni locali.
- **Router**: operano a livello 3. Hanno algoritmi di instradamento sofisticati e si usano normalmente per interconnessioni geografiche.
- **Gateway**: operano a livello 5. Sono usati per interconnettere architetture di rete diverse a livello applicativo.

#### Hub e Repeater

Implementano soltanto il livello fisico.

Mentre i repeater hanno soltanto due porte, gli hub ne hanno molteplici.

Il loro funzionamento è analogo: si limitano ad inviare su tutte le porte (tranne quella di ricezione) gli stessi dati ricevuti, semplicemente ripetendo il segnale ed amplificandolo.

![Stack dei protocolli implementata in un hub](../images/lower-levels-Untitled%2024.png)

Stack dei protocolli implementata in un hub

<aside>
📌 **Dominio di collisione**: porzione di LAN in cui, se due stazioni trasmettessero contemporaneamente, le due trame trasmesse colliderebbero.

</aside>

<aside>
📌 **Dominio di broadcast**: porzione di rete in cui tutte le stazioni ricevono una trama con indirizzo MAC broadcast emessa da una stazione arbitraria.

</aside>

I repeater e gli hub non separano i domini di collisione e non hanno alcuna influenza sui domini di broadcast, servono soltanto a superare le limitazioni fisiche ed elettriche per ciò che riguarda l'estensione delle reti locali.

Porzioni di rete connessi da repeater o hub sono nello stesso dominio di collisione e perciò anche nello stesso dominio di broadcast. Parti di rete connesse da apparati di interconnessione di livello superiore al primo sono in domini di collisione diversi.

#### Bridge

Implementano livello fisico e di linea.

Implementano due funzioni:

- **Filtering**: se una trama ricevuta da LAN 1 è indirizzata ad una stazione di LAN 1, viene scartata
- **Relay**: se una trama ricevuta da LAN 1 è indirizzata ad una stazione di LAN 2, viene trasmessa su LAN 2

![Stack dei protocolli implementata in un bridge](../images/lower-levels-Untitled%2025.png)

Stack dei protocolli implementata in un bridge

![Tabella di switching in un bridge](../images/lower-levels-Untitled%2026.png)

Tabella di switching in un bridge

Per stabilire se filtrare o instradare una trama, si consulta una tabella di switching locale chiamata **Forwarding Database** (**FDB**).

A ciascuna porta di uno switch è collegato un unico dominio di collisione, che può contenere una rete broadcast tradizionale o anche solo una stazione. In questo caso si hanno le seguenti funzionalità:

![Differenza tra hub e bridge](../images/lower-levels-Untitled%2027.png)

Differenza tra hub e bridge

- **Inoltro**: lo switch assicura che le trame provenienti da ciascun dominio siano inoltrate al dominio di destinazione
- **Funzione broadcast**: le trame con destinazione indirizzo di broadcast sono inoltrate su tutti i domini tranne quello di origine

In ogni caso, gli apparati collegati ad uno switch sono nello stesso dominio di broadcast.

I bridge possono anche operare con tecnologie LAN differenti. Ad esempio, gli Access Point Wi-Fi sono collegati anche ad un Distribution System basato su Ethernet.

![Bridge connessi ad apparati eterogenei](../images/lower-levels-Untitled%2028.png)

Bridge connessi ad apparati eterogenei

#### Router

Implementano tutti i livelli fino a quello di rete.

Hanno una serie di funzioni:

- Rimuovono l'header di livello 2 (se il MAC di destinazione è broadcast o corrispondente a quello dell'interfaccia del router)

![Stack dei protocolli implementata in un router](../images/lower-levels-Untitled%2029.png)

Stack dei protocolli implementata in un router

![Apparati connessi ad un router appartengono a domini di broadcast differenti](../images/lower-levels-Untitled%2030.png)

Apparati connessi ad un router appartengono a domini di broadcast differenti

- Esaminano e modificano l'header di livello 3 per eseguire l'instradamento
- Inseriscono un nuovo header di livello 2
- Operano implicitamente con domini di broadcast separati, quindi le interfacce di un router appartengono a domini di collisione diversi

#### Gateway

Implementa l'intera stack dei protocolli.

![Stack dei protocolli implementata in un gateway](../images/lower-levels-Untitled%2031.png)

Stack dei protocolli implementata in un gateway

### Learning and Forwarding

Abbiamo detto che uno dei compiti di uno switch è di inviare verso una LAN solo le trame che sono destinate a una LAN (o che devono attraversarla per giungere a destinazione). Questo avviene attraverso la **tabella di switching** (**FDB**).

Ma come fa lo switch ad apprendere attraverso quale interfaccia si può raggiungere una certa destinazione? Come si compila la FDB?

Se la rete è ad albero, il processo è semplice, perché esiste un solo collegamento tra ogni coppia di nodi.

![Struttura di rete ad albero](../images/lower-levels-Schermata_2021-05-29_alle_10.38.23.png)

Struttura di rete ad albero

#### Tabella di switching (FDB)

Nella tabella di switching di un bridge coesistono diversi tipi di informazione:

- **Entry statiche**
- **Entry dinamiche** con ageing time, ricavate ed aggiornate automaticamente tramite l'approccio di **backward learning**

Il backward learning si basa fondamentalmente su due step:

1. **Learning**: basato sull'indirizzo MAC sorgente di un pacchetto. Ogni volta che un pacchetto arriva allo switch, esso associa il suo indirizzo sorgente alla porta da cui arriva.
2. **Forwarding**: basato sull'indirizzo MAC di destinazione. Ogni volta che un pacchetto va inoltrato dallo switch verso altre destinazioni, se lo switch conosce già la porta su cui effettuare l'inoltro, procede con esso. Altrimenti, invia un messaggio di broadcast contenente il pacchetto.

<aside>
❗ Va notato che lo switch non ha indirizzo MAC, o meglio, non è usato nelle trame che elabora. Per questo motivo si parla di **transparent bridging**: lo switch è *trasparente* alle stazioni che interconnette.

</aside>

Questo approccio funziona soltanto su reti con topologia ad albero. Le topologie magliate sono trasformate in topologie ad albero tramite lo *Spanning Tree Protocol*.

A meno che lo switch non abbia già un'entry statica che identifichi la destinazione di un pacchetto che riceve, quando un pacchetto arriva allo switch, esso crea un'entry dinamica, con un *ageing time*. Se esiste già un'entry dinamica per quell'indirizzo MAC, il suo ageing time viene azzerato. Questa tecnica fa sì che, quando la switching table raggiunge la dimensione massima, le nuove entry possano essere aggiunte eliminando quelle più vecchie, ossia quelle con ageing time maggiore.

- Esempio
    
    ![La stazione 1 deve inoltrare un pacchetto alla stazione 5. Lo switch non conosce la destinazione corretta e allora manda la trama in broadcast su tutte le sue porte.](../images/lower-levels-Untitled%2032.png)
    
    La stazione 1 deve inoltrare un pacchetto alla stazione 5. Lo switch non conosce la destinazione corretta e allora manda la trama in broadcast su tutte le sue porte.
    
    ![La stazione 5 deve inoltrare un pacchetto alla stazione 1. Lo switch contiene un'entry dinamica che identifica la stazione 1 grazie all'inoltro precedente, quindi il pacchetto viene mandato solo sulla porta 1 dello switch.](../images/lower-levels-Untitled%2033.png)
    
    La stazione 5 deve inoltrare un pacchetto alla stazione 1. Lo switch contiene un'entry dinamica che identifica la stazione 1 grazie all'inoltro precedente, quindi il pacchetto viene mandato solo sulla porta 1 dello switch.
    
    ![La stazione 2 vuole inviare un pacchetto alla stazione 1, ma sono sulla stessa LAN. Se lo switch riceve questa trama, la scarta.](../images/lower-levels-Untitled%2034.png)
    
    La stazione 2 vuole inviare un pacchetto alla stazione 1, ma sono sulla stessa LAN. Se lo switch riceve questa trama, la scarta.
    
    ![La stazione 5 cambia posizione: ora si trova sulla LAN A. Manda un pacchetto alla stazione 2 in broadcast, che viene ricevuto anche dallo switch, che quindi può aggiornare la sua switching table: cambia la porta verso la stazione 5.](../images/lower-levels-Untitled%2035.png)
    
    La stazione 5 cambia posizione: ora si trova sulla LAN A. Manda un pacchetto alla stazione 2 in broadcast, che viene ricevuto anche dallo switch, che quindi può aggiornare la sua switching table: cambia la porta verso la stazione 5.
    
    ![Se la stazione 2 si sposta ma non manda nessun pacchetto allo switch o attraverso lo switch, la switching table non può essere aggiornata, perciò i pacchetti vengono inoltrati verso la destinazione sbagliata. Si vede proprio in questi casi l'importanza dell'ageing time.](../images/lower-levels-Untitled%2036.png)
    
    Se la stazione 2 si sposta ma non manda nessun pacchetto allo switch o attraverso lo switch, la switching table non può essere aggiornata, perciò i pacchetti vengono inoltrati verso la destinazione sbagliata. Si vede proprio in questi casi l'importanza dell'ageing time.
    

### Spanning Tree Protocol

Cosa succede se la rete non è in una topologia ad albero?

#### Broadcast storm

In una topologia di rete magliata, se un host vuole comunicare con un altro host ed entrambi sono connessi a due switch, inizialmente le switching table dei due switch creeranno un'entry dinamica per il MAC sorgente con la rispettiva porta da cui ricevono la trama.

Successivamente però, non conoscendo la destinazione, invieranno la trama in broadcast, che giungerà anche ai due switch e cambierà le rispettive porte di entrata dello stesso MAC. Avviene così il fenomeno di **Broadcast Storm**, che si ripete all'infinito in queste topologie di rete

![Primo invio verso gli switch](../images/lower-levels-Untitled%2037.png)

Primo invio verso gli switch

![Modifica delle porte in modo errato nelle switching table](../images/lower-levels-Untitled%2038.png)

Modifica delle porte in modo errato nelle switching table

Nella pratica, la topologia di una rete è solitamente *magliata*, ossia contiene loop per garantire tolleranza ai guasti. Per evitare il problema del Broadcast Storm, i bridge devono trasformare la topologia di rete in un albero che include tutti i nodi.

Per fare ciò, si usa il protocollo **STP** (*Spanning Tree Protocol*), che calcola lo Spanning Tree corrispondente alla rete magliata e lo modifica in caso di guasti.

STP è un protocollo distribuito che permette di ricavare la topologia ad albero attraverso il blocco delle porte degli switch. Una porta bloccata lascia passare i messaggi STP ma non le trame dati.

### Virtual LAN (VLAN)

Le Virtual LAN consentono di creare LAN logicamente separate **su un'unica LAN fisica. Sono usate per distinguere il traffico di diversi host di una stessa LAN.

- Soluzione con **bridge e hub**
    
    L'inoltro selettivo viene applicato soltanto nei bridge.
    
    La presenza di hub può consentire a host di altre VLAN di ricevere comunque delle trame.
    
    È necessario separare i domini di broadcast a livello della trama con il **VLAN Tagging**.
    
    ![VLAN con bridge e hub](../images/lower-levels-Untitled%2039.png)
    
    VLAN con bridge e hub
    
- Soluzione con **Switch**
    
    Garantisce una migliore separazione tra VLAN, basata sulle porte degli switch.
    
    Rimane necessario il VLAN Tagging sulle **trunk port**, che collegano gli switch tra loro.
    
    ![VLAN con switch](../images/lower-levels-Untitled%2040.png)
    
    VLAN con switch
    

L'associazione di una stazione ad una VLAN può essere fatta:

- Per porta di bridge o switch
- Per indirizzo MAC di stazione
- Per tipo di protocollo di livello 3 utilizzato

Il formato della trama comprendente VLAN ID, specificato nello standard IEEE 802.1Q, ha alcuni campi aggiuntivi:

| Campo | Dimensione (bit) | Descrizione |
| --- | --- | --- |
| VLAN Prot | 16 | Contiene il valore: 0x8100 |
| Priority | 3 |  |
| Canonical Format Identifier | 1 | Identifica il tipo di formato del campo indirizzo |
| VLAN ID | 12 |  |

![Struttura di una trama con VLAN Tagging](../images/lower-levels-Untitled%2041.png)

Struttura di una trama con VLAN Tagging
