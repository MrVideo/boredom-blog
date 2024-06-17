---
title: 'Livello di trasporto'
draft: false
type: 'page'
toc: true
mathjax: true
---

---

> [!info] Il livello di trasporto è il livello che **si interfaccia con il livello applicativo** e che **maschera i processi di trasporto** all’utente finale ed al livello applicativo stesso. Consente il **collegamento logico** tra i processi applicativi.

## Indirizzamento

Il livello di trasporto svolge funzioni di *multiplexing* e *demultiplexing* per le applicazioni, così che più applicazioni possano essere attive su un solo host.

Ciascun collegamento logico tra applicazioni necessita di un **indirizzo** fornito dal livello di trasporto: il **socket**, formato da indirizzo IP e numero di porta.

Le funzioni di multiplexing e demultiplexing vengono gestite mediante indirizzi trasportati dalle UI di livello di trasporto (*segmenti*). Tali indirizzi sono lunghi 16 bit e prendono il nome di **porte**. I numeri di porta possono assumere valori compresi tra 0 e 65535 e si dividono in 3 gruppi:

![Servizio di multiplexing del livello di trasporto](../images/transport-Untitled.png)

Servizio di multiplexing del livello di trasporto

- **Well-known ports**: assegnati a servizi applicativi comuni lato server (HTTP, FTP, SMTP, POP3, DNS…). Vanno da 0 a 1023.
- **Numeri registrati**: numeri di porta assegnati a specifiche applicazioni da chi lo richiede (in genere da protocolli proprietari). Vanno da 1024 a 49151.
- **Numeri dinamici**: assegnati dinamicamente ai processi applicativi lato client. Vanno da 49152 a 65535.

## Buffering

![Buffer del livello di trasporto](../images/transport-Untitled%201.png)

Buffer del livello di trasporto

I protocolli di trasporto sono implementati nei più diffusi sistemi operativi. Quando un processo viene associato ad una porta, viene associato dal sistema operativo a *due code* (**buffer**), una d’ingresso e una d’uscita. I buffer *assorbono* i rallentamenti del processing dei livelli adiacenti (rete ed applicazione).

## Modalità del servizio di trasporto

Il servizio di rete non è affidabile, ma fa del proprio meglio per consegnare i messaggi a destinazione (si parla di protocolli *best effort*). Serve infatti un servizio di trasporto che assorba questa negligenza.

Si possono fornire vari tipi di servizio di trasporto:

- **Affidabile**: garanzia di consegna dei messaggi nel corretto ordine
- **Non affidabile**: solo funzionalità di multiplexing
- **Connection-oriented**
- **Connectionless**

In Internet vengono usati due protocolli di trasporto:

- **TCP** (*Transmission Control Protocol*): connection-oriented ed affidabile
- **UDP** (*User Datagram Protocol*): connectionless e non affidabile

## Interazione tra entità di trasporto

Avviene sempre attraverso il paradigma Client-Server:

- Un client può essere eseguito in modalità parallela o seriale (si possono aprire più connessioni in parallelo per richiedere gli oggetti richiamati in un documento html)
- Anche un server può essere eseguito in modalità parallela o seriale

Per gli applicativi che usano **UDP**: i server sono gestiti in modo seriale:

- I pacchetti che arrivano con delle richieste vengono immagazzinati e attendono il loro turno
- Il server li esamina e genera le risposte sequenzialmente

Per gli applicativi che usano **TCP**: i server sono eseguiti tipicamente in modalità parallela. Una connessione aperta verso ciascun processo client è mantenuta per il tempo necessario a scambiare richieste e risposte.

### Interazione tramite UDP

![Esempio di comunicazione con UDP](../images/transport-Untitled%202.png)

Esempio di comunicazione con UDP

Nessuna connessione. Client e server si parlano perché conoscono le proprie socket. Attraverso ciascuna socket si comunica con un solo processo remoto per volta.

### Interazione tramite TCP

Ogni connessione è identificata da una **coppia** di socket: porta e IP della sorgente, porta e IP della destinazione. È possibile il multi-demultiplexing di più connessioni sulla stessa porta nello stesso host server.

![Esempio di comunicazione con TCP](../images/transport-Untitled%203.png)

Esempio di comunicazione con TCP

## User Datagram Protocol

Protocollo **connectionless**.

Fornisce funzioni di trasporto base quali:

- Multiplazione
- Rivelazione di errore (opzionale)

Non fornisce:

- Consegna in sequenza
- Rivelazione di perdita/duplicazione
- Controllo di flusso e di congestione

È un servizio di trasporto **inaffidabile**.

Non offre particolari servizi aggiuntivi rispetto al livello sottostante (IP).

**Vantaggi dell’UDP**:

- **Minore latenza**: non occorre stabilire una connessione
- **Maggiore semplicità**: non occorre tenere traccia dello stato della connessione e ci sono poche regole da implementare
- **Minore overhead**: l’header UDP è più piccolo dell’header TCP

## Incapsulamento

![Incapsulamento nel segmento UDP](../images/transport-Untitled%204.png)

Incapsulamento nel segmento UDP

Un messaggio applicativo viene incapsulato esattamente in un messaggio UDP e trasportato da un pacchetto IP. La frammentazione è eventualmente svolta dal livello di rete. 

Vedremo che TCP invece lavora su *stream di byte*.

### Formato del messaggio

Il valore offerto da UDP consiste in:

- Indirizzo con mutilazione/demultiplazione
- Rilevazione di errore (opzionale)

![Formato del segmento UDP](../images/transport-Untitled%205.png)

Formato del segmento UDP

## Checksum: controllo di integrità

Informazione *ridondante* inserita per il servizio di **controllo d’errore**. Viene calcolato dal trasmettitore ed inserito nell’header. Il calcolo è svolto anche al ricevitore sull’intero segmento, includendo il checksum. Se il risultato è corretto, si accetta il segmento, altrimenti si scarta.

Il checksum viene calcolando considerando:

- **Header UDP**
- **Pseudo-header IP**: definito solo ai fini del calcolo del checksum per evitare recapiti di UDP a host sbagliati. Non viene trasmesso realmente in rete.
- **Dati** del messaggio di livello applicativo

Il calcolo avviene così: $\text{Sum} = \text{Segmento UDP}\space + \space \text{Pseudo-header}$

- **Somma in complemento a 1**: l’eventuale bit di carry viene aggiunto come bit meno significativo a destra
- Il checksum è il **`NOT`** della somma: $\text{Checksum} = \overline{\text{Sum}}$

In un collegamento ideale, tutto ciò che viene trasmesso arriva nello stesso ordine e senza errori viene correttamente interpretato a destinazione.

![Esempio di calcolo al trasmettitore del Checksum](../images/transport-Untitled%206.png)

Esempio di calcolo al trasmettitore del Checksum

![Esempio di calcolo al ricevitore del Checksum. In questo caso, non ci sono errori e il pacchetto viene accettato.](../images/transport-Untitled%207.png)

Esempio di calcolo al ricevitore del Checksum. In questo caso, non ci sono errori e il pacchetto viene accettato.

## Metodi di ritrasmissione

In un collegamento reale invece possono esserci errori o perdite sul canale dovute a:

- Errori sui bit causati da interferenze
- Perdita di pacchetti a causa di overflow

Si possono usare tecniche di **correzione d’errore**, come i **FEC**, *Forward Error Correction*, ma introducono un’elevata ridondanza nei pacchetti.

Si possono anche utilizzare **protocolli di ritrasmissione**: ciascuna UI ricevuta correttamente viene riscontrata positivamente con un messaggio di *Acknowledgement* (**ACK**). La mancata ricezione di un ACK entro un certo periodo (*timeout*) indica la necessità di ritrasmissione. A volte l’errore può essere esplicitamente segnalato da un **NACK** (*Negative ACK*). La procedura continua fino a quando la UI non viene ricevuta correttamente. È necessario però avere un canale di ritorno per il trasporto di ACK e NACK e anche quelli possono essere affetti da errori.

Il recupero d’errore con ritrasmissione può essere implementato a qualunque livello, ma storicamente sono sempre presenti a livello 2 (*Data link*). Ma c’è anche la necessita del recupero d’errore al livello di trasporto, per il recupero end-to-end. Proteggere i collegamenti fisici non basta, i pacchetti possono essere persi nei buffer dei router lungo la rete. Nei sistemi moderni, il recupero d’errore a livello di linea può anche non esserci.

## Metodo “Stop and wait”

![Funzionamento del metodo *Stop & Wait*](../images/transport-Untitled%208.png)

Funzionamento del metodo *Stop & Wait*

Si utilizzano solo **ACK** e **timeout**. Ogni messaggio ricevuto correttamente è riscontrato dal ricevitore. Il trasmettitore trasmette un pacchetto e avvia il timeout. Il trasmettitore si mette in attesa e, se il primo evento è un ACK, trasmette il prossimo pacchetto, mentre se scade il timeout ritrasmette il pacchetto precedente.

Il tempo di trasferimento totale è pari a:

$$T_{tot} = N_fT_1 = N_f(T_f + T_a + 2T_p + 2\tau)=N_f\bigg (\frac{L_f}{C} + \frac{L_a}{C} + 2T_p + 2\tau \bigg)$$

Si definisce **efficienza del protocollo** la frazione di tempo in cui il canale è usato per trasmettere informazione utile in assenza di errore. Vale la relazione:

$$\eta = \frac{T_f}{T_{tot}} = \frac{T_f}{T_f + T_a + 2T_p + 2\tau}$$

Un protocollo ha efficienza bassa se $T_f \ll \tau$.

Si definisce **Throughput** il grado di utilizzazione del collegamento. Vale la relazione:

$$\text{THR} = \eta \cdot C$$

Se un pacchetto ACK viene perso e il timeout scade, uno dei pacchetti viene duplicato. È pertanto necessario numerare i pacchetti ed i riscontri.

![Esempio di errore su una UI e su un ACK](../images/transport-Untitled%209.png)

Esempio di errore su una UI e su un ACK

### Dimensionamento del Timeout

Il timeout non dev’essere troppo grande per evitare inefficienze. Spesso viene dimensionato al valore minimo di $T_O = T_a + 2\tau$. Tuttavia, il tempo di elaborazione di un pacchetto non è controllabile e la stima del RTT in una rete non è sempre veritiera.

Per evitare ambiguità è anche necessario **numerare i riscontri**. Nel metodo *Stop & Wait* basta un bit per la numerazione.

![Esempio nel caso di pacchetti non numerati](../images/transport-Untitled%2010.png)

Esempio nel caso di pacchetti non numerati

![Esempio nel caso di pacchetti numerati](../images/transport-Untitled%2011.png)

Esempio nel caso di pacchetti numerati

## Continuous ARQ

![Esempio di finestra di dimensione $W_s$](../images/transport-Untitled%2012.png)

Esempio di finestra di dimensione $W_s$

Con questo metodo si possono trasmettere più UI senza aspettare ogni volta il rispettivo riscontro. Infatti, si possono inviare tante UI quante quelle con numerazione inclusa entro una **finestra** di dimensione $W_s$.

In questo metodo, la numerazione è detta *ciclica modulo $N$*, con $N = 2^b$. Per esempio, usando tre bit, otterrei UI numerate ciclicamente da 0 a 7. In quest’ottica, il metodo *Stop & Wait* è un caso particolare di *Continuous ARQ* con $N = 2, \space b = 1$. Il protocollo TCP, per esempio, utilizza 32 bit per la numerazione.

Il metodo *Continuous ARQ* è molto efficiente a meno di errori.

Il tempo di trasferimento di $N_f$ UI è:

$$T_{tot} = N_fT_f + T_a + 2\tau$$

Ma quante e quali UI posso trasmettere senza avere riscontro? Tutte quelle che rientrano nella finestra di trasmissione (*sliding window*).

![Esempio di *sliding window*](../images/transport-Untitled%2013.png)

Esempio di *sliding window*

Nel caso di errori, occorre ritrasmettere, e si può fare in seguito a due eventi:

- Se scade un timeout
- Se il ricevitore invia un esplicito riscontro **negativo** (**NACK**)

Al livello di trasporto, nel caso TCP, viene usato il timeout come *trigger* principale per la ritrasmissione, ma alcune versioni avanzate di TCP utilizzano anche un *NACK implicito* (*fast retransmit*).

**Esistono diversi protocolli e versioni di ARQ**:

- **Go-Back-N** (GBN)
- **Selective repeat** (SR)

### Go-Back-N

![Esempio di ritrasmissione Go-Back-N](../images/transport-Untitled%2014.png)

Esempio di ritrasmissione Go-Back-N

Quando si verifica un errore, si comincia a **ritrasmettere la finestra a partire dal primo pacchetto non riscontrato**. La ritrasmissione avviene per scadenza di timeout.

Ad ogni pacchetto viene fatto partire un timeout che viene cancellato alla corretta ricezione dell’ACK. La ritrasmissione del primo pacchetto non riscontrato (e dei successivi) inizia allo scadere del timeout. Raggiunto l’ultimo pacchetto della finestra, la trasmissione si blocca in attesa di un nuovo ACK o della scadenza del timeout

Con GBN si può avere la ritrasmissione di pacchetti ricevuti correttamente, ma **semplifica il funzionamento**, perché:

- I pacchetti fuori sequenza vengono **ignorati e scartati**, in modo da mantenere automaticamente l’ordine
- Per i pacchetti ignorati **non viene trasmesso alcun ACK**

![Pacchetti ignorati perché già fuori sequenza](../images/transport-Untitled%2015.png)

Pacchetti ignorati perché già fuori sequenza

![ACK cumulativo che include i pacchetti da 1 a 3](../images/transport-Untitled%2016.png)

ACK cumulativo che include i pacchetti da 1 a 3

Se non ci sono fuori sequenza, il riscontro ACK può anche essere inviato **cumulativamente**, ossia vengono riscontrati più pacchetti alla volta con un singolo ACK. Se non scade alcun timeout, in questo modo si rimedia alla perdita di ACK.

La finestra ottimale della finestra coincide con il **RTT della connessione**:

$$\text{RTT} = T + \tau + T_{\text{ACK}} +\tau$$

Se viene rispettato questo vincolo, **la finestra scorre prima che abbia esaurito di trasmettere tutti i pacchetti** al suo interno e **la trasmissione non si interrompe mai** a meno di errori.

Dimensione ottimale finestra:

$$W_s = \bigg\lceil\frac{T+T_{\text{ACK}}+2\tau}{T}\bigg\rceil$$

La finestra può anche essere espressa in tempo, byte e altre unità di misura.

Il dimensionamento si complica se i tempi di trasmissione e propagazione non sono noti. Alcuni rimedi a questo problema sono:

- Fare una finestra grande a prescindere
    - Non pregiudica il funzionamento in assenza di errore
    - Può aumentare il numero di ritrasmissioni inutili in caso di errore
- Stimare il tempo di RTT ed adattare la finestra e/o il timeout

## Protocolli bidirezionali

![Connessione bidirezionale *full-duplex*](../images/transport-Untitled%2017.png)

Connessione bidirezionale *full-duplex*

In una comunicazione TCP, il trasferimento di dati e riscontri avviene in modo *bidirezionale* (**full-duplex**). Viene usato il **piggybacking**: il trasporto di informazioni viene unito anche agli ACK, se necessario.

![Numerazione di Sequenza e di ACK in TCP](../images/transport-Untitled%2018.png)

Numerazione di Sequenza e di ACK in TCP

- **SN**: Sequence Number: numero di sequenza del pacchetto trasmesso
- **AN**: ACK Number: numero di sequenza del pacchetto riscontrato ($\text{AN} =x$ significa che sono stati riscontrati tutti i pacchetti fino all'$x\text{-esimo}$)

In questo metodo, possono anche esserci UI di solo riscontro, ma in ogni caso le UI dati trasportano anche l’ACK.

![GBN bidirezionale senza errori](../images/transport-Untitled%2019.png)

GBN bidirezionale senza errori

![GBN bidirezionale con errori di trasmissione di ACK](../images/transport-Untitled%2020.png)

GBN bidirezionale con errori di trasmissione di ACK

![GBN bidirezionale con un errore di trasmissione di una sequenza](../images/transport-Untitled%2021.png)

GBN bidirezionale con un errore di trasmissione di una sequenza

![GBN bidirezionali con ACK ritardati](../images/transport-Untitled%2022.png)

GBN bidirezionali con ACK ritardati

È necessario, nel caso del GBN bidirezionale, **inizializzare** il protocollo:

- I numeri SN ed AN devono essere inizializzati in entrambe le direzioni
- Deve esistere un momento di **inizio inequivocabile** in cui scambiare l’informazione per l’inizializzazione: occorre un meccanismo **a connessione** che stabilisca l’istante $t = 0$.

## Controllo di flusso

Il buffer di ricezione ha sempre un limite a $W_{\text{RX}}$ posizioni. Il processo applicativo ricevente ha una velocità di *assorbimento* delle UI variabile, quindi all’arrivo di una UI il buffer in ricezione può essere pieno. Il nostro obiettivo è evitare che i pacchetti vadano persi **regolando il ritmo di invio**.

È possibile usare un meccanismo a finestra, come in Go-Back-N, per effettuare il controllo di flusso, ma ciò causa due problemi:

- Con un GBN, se la finestra è di dimensione $W_s$, il trasmettitore può inviare fino a $W_s$ UI senza aver ricevuto riscontri
- Se l’applicazione al ricevitore legge le UI lentamente, il buffer in ingresso al T-SAP si svuota lentamente

Quali sono le soluzioni?

1. Il ricevitore invia subito i riscontri, cioè non appena riceve le UI correttamente. Si provocherebbe lo scorrimento della finestra in trasmissione, che porterebbe ad un buffer pieno e quindi a delle perdite in ricezione.
2. Il ricevitore invia riscontri solo quando le UI sono passate al livello superiore e quindi eliminate dal buffer. Se il ricevitore è lento però, ci saranno molte ritrasmissioni per effetto dei timeout che scadono, quindi bisognerebbe aumentare il timeout, rallentando l’intero processo.

La soluzione adottata dal TCP è **eliminare la correlazione tra l’invio dei riscontri ed il controllo di flusso**: si ha un controllo di flusso *a credito esplicito* con finestra mobile. Si inserisce nei riscontri stessi un campo `window` che indica quante UI o quanti byte si possono ancora ricevere. Di fatto questo campo indica lo spazio rimanente nel buffer in ricezione.

## Transmission Control Protocol

![Schema di una connessione TCP](../images/transport-Untitled%2023.png)

Schema di una connessione TCP

Il TCP è un protocollo **connection-oriented** e fornisce un servizio di trasporto **affidabile**:

- Multiplazione per mezzo dei socket
- Consegna in sequenza
- Controllo di flusso e perdita
- Controllo di congestione

## Flusso di dati

Anche se il TCP riceve dal livello applicativo dei messaggi *preconfezionati*, considera la sequenza di messaggi come un **flusso continuo di dati** (*stream*). Il TCP converte il flusso di dati in **segmenti** che possono essere trasmessi in rete. Le dimensioni dei segmenti sono variabili.

L’applicazione trasmittente passa i dati a TCP ed il protocollo li accumula in un buffer. Periodicamente o in condizioni particolari, il TCP prende una parte dei dati nel buffer e forma un segmento. La dimensione del segmento è critica per le prestazioni, per cui il TCP cerca di attendere fino a che un ammontare ragionevole di dati sia presente nel buffer di trasmissione.

## Numerazione byte e riscontri

Il TCP adotta un meccanismo per il controllo delle perdite di pacchetti di tipo Go-Back-N:

- Il TCP numera ogni byte trasmesso, per cui ogni byte ha un numero di sequenza
- I segmenti sono gruppi di byte e le dimensioni delle finestre sono espresse in byte
- Nell’header del segmento TCP è trasportato il numero di sequenza del primo byte trasmesso nel segmento stesso
- Il ricevitore deve riscontrare i dati ricevuti inviando il numero di sequenza del prossimo byte che ci si aspetta di ricevere
- Se un riscontro non arriva entro il timeout, i dati sono ritrasmessi

![Struttura di un segmento TCP](../images/transport-8E756735-0185-4806-BF04-FAFBAD611CA4.jpeg)

Struttura di un segmento TCP

| Nome campo       | Dimensione (bit) | Descrizione                                                                                                                                                                          |
| ---------------- | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Source Port      | 16               | Indirizzo di porta sorgente                                                                                                                                                          |
| Destination Port | 16               | Indirizzo di porta destinazione                                                                                                                                                      |
| Sequence Number  | 32               | Numero di sequenza del primo byte nel payload                                                                                                                                        |
| ACK Number       | 32               | Numero di sequenza del prossimo byte che si intende ricevere                                                                                                                         |
| HLEN             | 4                | Contiene la lunghezza complessiva dell’header TCP, espressa come numero di parole da 32 bit                                                                                          |
| Window           | 16               | Contiene il valore della finestra di ricezione                                                                                                                                       |
| Checksum         | 16               | Calcolato come in UDP                                                                                                                                                                |
| CWR              | 1                | Congestion Window Reduced: settato quando si notifica al TCP remoto che si è ridotta la finestra di congestione                                                                      |
| ECE              | 1                | Explicit Consegtion notification Echo: serve a segnalare che si è rilevata una congestione e quindi serve a chiedere al TCP remoto di rallentare la trasmissione                     |
| URG              | 1                | Vale 1 se vi sono dati urgenti e quindi il TCP deve passare in modalità urgente. In questo caso, urgent pointer dà indicazione sulla posizione dei dati urgenti presenti nel payload | 
| ACK              | 1                | Vale 1 se il pacchetto è un ACK valido                                                                                                                                               |
| PSH              | 1                | Vale 1 quando il trasmettitore intende usare il comando di PUSH, ma il ricevitore può anche ignorare il comando                                                                      |
| RST              | 1                | Resetta la connessione                                                                                                                                                               |
| SYN e FIN        | 1                | Usati durante setup e teardown della connessione TCP                                                                                                                                 |
| Options          |                  | Dimensione variabile                                                                                                                                                                 |
Usato durante il setup per comunicare la massima dimensione dei segmenti |
| Padding |  | Riempimento fino a multipli di 32 bit con uso di no-operation e end-of-option |

### Funzione Push

TCP originariamente prevedeva una gestione speciale per i dati che richiedono di essere *immediatamente consegnati* all’applicazione ricevente. Per ottenere un inoltro immediato dei dati da parte del TCP ricevente all’applicazione ricevente, l’applicazione trasmittente può inviare un comando PUSH (è questo il caso di applicazioni come Telnet).

In verità, l’uso di PUSH **non è generalmente implementato** nella primitiva `SEND()` delle interfacce TCP, ma viene automaticamente rettato dal sistema operativo nell’ultimo segmento che svuota il buffer.

### Dati `URGENT`

![Campo Urgent Pointer e dati a cui punta](../images/transport-Untitled%2024.png)

Campo Urgent Pointer e dati a cui punta

La modalità di funzionamento TCP può essere cambiata in Urgent, ma c’è un’ambiguità negli standard RFC del TCP per questa funzione:

- RFC 793: puntatore all’inizio del primo byte dopo i dati urgenti
- RFC 1122: puntatore all’inizio dell’ultimo byte dei dati urgenti

Nonostante RFC successivi ribadiscano il contenuto di RFC 1122, molte implementazioni di TCP seguono ancora l’RFC 793. Inoltre, sistemi operativi differenti implementano Urgent in maniera differente. Per questi motivi, viene generalmente ignorata questa funzionalità.

### Opzioni

Le opzioni sono aggiunte all’header TCP e ne esistono di diversi tipi:

- Opzioni di 1 byte: servono come riempimento per avere un header multiplo di 32 bit:
    - **No Operation**: `00000001`, è puramente riempitivo
    - **End Of Option**: `00000000`, byte di riempimento finale, usato alla fine dell’header TCP
- Opzioni lunghe:
    - Per ciascuna di queste opzioni esiste un campo *length* che ne indica la dimensione in byte
    - *Maximum Segment Size* (MSS): 32 bit, definisce la dimensione massima del segmento che verrà usata durante la connessione TCP. Non viene modificata durante la connessione. La dimensione è decisa da ciascuna delle due parti durante la fase di setup (ciascuna delle parti decide il MSS dei segmenti che potrà ricevere). Il valore di default è 536 byte, ma il valore massimo teorico è 65535 byte.
    - Fattore di scala della finestra: 24 bit
    - Molti altri reperibili a [questa pagina](http://www.iana.org/assignments/tcp-parameters/tcp-parameters.xhtml).

### Incapsulamento e frammentazione

![Esempio di incapsulamento e frammentazione in TCP](../images/transport-Untitled%2025.png)

Esempio di incapsulamento e frammentazione in TCP

Il messaggio dell’applicazione può essere frammentato da TCP in più segmenti. IP può operare ulteriore frammentazione all’occorrenza.

L’MSS deve essere scelto in modo da far corrispondere un segmento ad un datagramma, considerando la massima dimensione del datagramma, impostata dal valore della MTU (*Maximum Transmission Unit*, payload di livello 2):

$$\text{MSS} = \text{MTU} - \text{size}(\text{IP Header}) - \text{size}(\text{TCP Header})$$

Gli header hanno dimensione variabile.

### Fattore di scala della finestra

Definisce il fattore di scala $f_s$ della finestra di ricezione. Settato in fase di apertura, non viene mai cambiato dopo. L’opzione fa sì che il valore del campo `window` venga scalato, per ottenere come segue il valore reale della finestra di ricezione:

$$R_{wnd}=W \cdot 2^{f_s}$$

Vale la seguente relazione:

$$\text{max}(f_s) = 14 \implies \text{max}(R_{wnd}) = 2^{16} \cdot 2^{14} = 2^{30} < \text{max}(\text{SN}) = 2^{32}$$

## Setup delle connessioni

Prima di iniziare la connessione (*call setup*), le applicazioni dal lato client e dal lato server devono comunicare con il software TCP locale:

1. Il server effettua una *Passive Open*, con cui comunica al TCP locale che è pronto ad accettare nuove connessioni
2. Il client che desidera comunicare effettua una *Active Open*, che comunica al TCP locale che l'applicativo intende effettuare una connessione verso un dato socket remoto
3. Il client TCP estrae a caso un numero di sequenza iniziale SN e manda un segmento TCP di tipo **SYN** (*Synchronize*) contenente questo numero di sequenza. Indica qui anche altri parametri della connesione quali **MSS** e $f_s$.
4. Quando riceve il **SYN**, il TCP server estrae a caso un numero di sequenza iniziale e manda un segmento **SYN/ACK** contenente anche un ACK number per riscontrare il numero di sequenza iniziale precedentemente inviato dal TCP client. L'ACK number indica **il numero del prossimo byte che il server aspetta**.
5. Il TCP client riceve il messaggio **SYN/ACK** del server ed invia un ACK. Nel payload inserisce i primi dati della connessione, con il numero di sequenza del primo byte. Inserisce anche la dimensione della finestra da imporre al server nel campo `window`.
6. Il TCP client notifica all'applicazione che la connessione è aperta
7. Quando il TCP server riceve l'ACK del TCP client, notifica al suo applicativo che la connessione è aperta

Questo processo viene definito **three-way handshaking**.

![Esempio di *three-way handshaking*](../images/transport-Untitled%2026.png)

Esempio di *three-way handshaking*

L'estrazione casuale del numero iniziale evita problemi nel caso di connessioni ravvicinate aperte tra due stesse socket. Se rimangono in circolo in rete pacchetti della prima connessione, questi potrebbero arrivare durante la seconda connessione e causare ambiguità.

## Teardown della connessione

1. Il TCP che chiude la connessione invia un segmento di tipo **FIN** con gli ultimi dati
2. Il TCP dall'altra parte invia un **ACK** per confermare la chiusura
3. Appena completa la trasmissione, il TCP chiude la connessione anche nell'altra direzione, inviando un messaggio di **FIN**
4. Il TCP che aveva già chiuso la connessione in direzione opposta invia un ACK finale per confermare

![Esempio di chiusura di connessione TCP](../images/transport-Untitled%2027.png)

Esempio di chiusura di connessione TCP

La connessione può anche rimanere aperta nell'altra direzione nel caso il TCP dalla parte opposta voglia continuare ad inviare dati.

### Collisione di richieste

![Esempio di collisione di richieste](../images/transport-Untitled%2028.png)

Esempio di collisione di richieste

Se due richieste di instaurazione di connessione hanno stessi socket sorgente e destinazione, si instaura **una sola connessione**.

### Reset della connessione

La connessione può anche essere chiusa senza scambio di messaggi nei due versi. È possibile infatti settare il flag di **Reset** nel segmento ed interrompere la connessione in entrambe le connessioni. Il TCP che riceve un Reset chiude la connessione interrompendo la comunicazione.

## Implementazione del controllo di flusso

![Finestra di trasmissione e buffer di ricostruzione](../images/transport-Untitled%2029.png)

Finestra di trasmissione e buffer di ricostruzione

Il TCP ricevente **controlla il flusso** di quello trasmittente. Dal lato del ricevitore abbiamo un buffer che accumula i byte ricevuti e non ancora assorbiti dall'applicazione. Dal lato del trasmettitore abbiamo un buffer che accumula i byte in attesa di essere trasmessi.

La finestra di trasmissione in A si sposta in sincronia con la finestra di ricezione in B, $R_{wnd}$: B determina $R_{wnd}$ in base alle dimensioni del proprio buffer di ricostruzione, mentre A adatta l'ampiezza della finestra di trasmissione in base al valore $R_{wnd}$ ricevuto da B.

![Finestra di ricezione](../images/transport-Untitled%2030.png)

Finestra di ricezione

![Finestra di trasmissione](../images/transport-Untitled%2031.png)

Finestra di trasmissione

### Lato ricevitore

![Riempimento e svuotamento del buffer del ricevitore](../images/transport-Untitled%2032.png)

Riempimento e svuotamento del buffer del ricevitore

Dal lato del ricevitore, abbiamo una finestra di ricezione di dimensione $R_{wnd}$, che indica lo spazio disponibile per ricevere dati nel buffer di ricezione. $R_{wnd}$ si estende dall'ultimo byte ricevuto e riscontrato fino alla fine del buffer. La dimensione della finestra è segnalata **in ogni segmento** inviato al trasmettitore.

Il buffer di ricezione può riempirsi a causa, per esempio, di congestione nel sistema operativo del ricevitore.

### Lato trasmettitore

Il trasmettitore mantiene un buffer di trasmissione che tiene traccia di:

- Dati che sono stati trasmessi ma non ancora riscontrati
- Dimensione della finestra di ricezione del partner

Se la dimensione della *Send Window* $S_{wnd} = R_{wnd}$, allora il buffer di trasmissione si estende dal primo byte non riscontrato all'estremo della finestra di ricezione del ricevitore. La parte inutilizzata del buffer rappresenta i byte che possono essere trasmessi senza attendere ulteriori riscontri.

Può verificarsi però il caso in cui $S_{wnd} \neq R_{wnd}$, in particolare $S_{wnd} < R_{wnd}$. Ciò avviene quando si ha un vincolo più stringente per effetto del **controllo di congestione**.

![Riempimento e svuotamento del buffer del trasmettitore](../images/transport-Immagine_2021-04-01_115048.png)

Riempimento e svuotamento del buffer del trasmettitore

### Problemi con la finestra

- Lato ricevitore
    
    **Silly window syndrome**: l'applicazione ricevente svuota lentamente il buffer di ricezione e comunica al trasmettitore una finestra molto piccola, perciò il trasmettitore invia **segmenti molto corti con molto overhead**.
    
    La soluzione di questo problema è l'**algoritmo di Clark**: il ricevitore *mente* al trasmettitore indicando una finestra di dimensione **nulla** sino a che il buffer di ricezione non si è svuotato per metà o per una porzione almeno pari al MSS:
    
    ```python
    if Window.free <= max(0.5 * Receive_Buffer_Size, Maximum_Segment_Size):
    	Window.size = 0
    else:
    	Window.size = Window.free
    ```
    
- Lato trasmettitore
    
    L'applicazione trasmittente genera dati lentamente, perciò il TCP invia segmenti molto corti e con molto overhead.
    
    La soluzione di questo problema è l'**algoritmo di Nagle**: il TCP sorgente invia la prima porzione di dati anche se corta. Gli altri segmenti vengono generati ed inviati solo se si verifica una delle seguenti condizioni:
    
    - Il buffer d'uscita contiene dati sufficienti a riempire un MSS
    - Si riceve un ACK per un segmento precedente

## Persistenza

Se il destinatario fissa a zero la finestra di ricezione, la sorgente TCP **interrompe la trasmissione**. Essa riprende quando il destinatario invia un segmento con un nuovo valore di dimensione della finestra, non nullo. Ma se un ACK andasse perso, la connessione rimarrebbe bloccata, perciò, per ovviare a questo problema, si introduce un **timer di persistenza** che viene attivato quando arriva un segmento con dimensione della finestra nulla.
Il valore del timer di persistenza coincide con il timeout di ritrasmissione. Quando il timer di persistenza scade, viene inviato un **segmento sonda** (*probe*) con pochi byte di payload.
Se viene ricevuto un ACK per questo segmento si esce dallo stato critico, altrimenti si riavvia il timer di persistenza e si ricomincia il processo di probing.

## Ritrasmissione

Il protocollo TCP usa un sistema **Go-Back-N senza NACK**.
Le ritrasmissioni avvengono **solo per scadenza di timeout**. I byte accettati da TCP possono anche essere fuori sequenza, purché con numerazione all'interno dell'attuale finestra di ricezione. Quando arrivano i segmenti mancanti, nella ritrasmissione, la finestra scorre in avanti fino al prossimo byte atteso di nuovo in sequenza e viene mandato un ACK che **riscontra collettivamente tutti i segmenti precedenti**.

Poiché i segmenti TCP attraversano una rete, essi subiscono ritardi variabili, poiché l'RTT varia nel tempo.
Una delle problematiche, perciò, è **stabilire il valore ottimale del timeout**. Se il timeout è troppo breve si rischiano ritrasmissioni inutili, mentre se è troppo lungo impedisce il recupero veloce di errori.
Il valore ottimale del timeout dipende fortemente dal ritardo in rete e dalle sue variazioni, perciò il TCP misura continuamente l'RTT per effettuare delle stime utili ad impostare un valore appropriato di timeout.

Per calcolare la stima dell'RTT, il TCP usa un **filtro a media mobile**: l'RTT viene misurato per ogni segmento al ricevimento del rispettivo riscontro. Va notato che *non viene misurato l'RTT per i segmenti che vengono ritrasmessi*.

La stima corrente, detta **Smoothed RTT**, è data da:

$$\text{RTT}_{\text{avg}} = (1 - \alpha) \cdot  \text{RTT}_{\text{avg}} + \alpha \cdot \text{RTT}_{\text{last}}, \space 0 < \alpha \leq 1$$

Tipicamente, $\alpha = 0.125$.

La stima della variabilità del RTT è data da:

$$\text{RTT}_{\text{dev}} = (1 - \beta) \cdot  \text{RTT}_{\text{dev}} + \beta \cdot \big|\text{RTT}_{\text{last}} - \text{RTT}_{\text{avg}} \big |, \space 0 < \beta \leq 1$$

Tipicamente, $\beta = 0.25$.

![Esempio di stima RTT in TCP](../images/transport-Untitled%2033.png)

Esempio di stima RTT in TCP

### Algoritmo di Karn

Normalmente, il timeout viene determinato sulla base del RTT stimato, secondo l'**algoritmo di Jacobson**:

$$T_O = \text{RTT}_{\text{avg}} + n \cdot \text{RTT}_{\text{dev}}, \space n \in \{2, 3, 4\}$$

Ma con una rete improvvisamente congestionata, quasi tutti i segmenti verrebbero ritrasmessi. Il timeout non verrebbe più aggiornato, dato che non si stima l'RTT sui pacchetti ritrasmessi, perciò si entra in un circolo vizioso che aumenta le ritrasmissioni.

La soluzione a questo problema è data dall'**algoritmo di Karn** (*timer backoff*): ad ogni ritrasmissione dovuta a scadenza di timeout, **il timeout viene aumentato**. Generalmente, il timeout viene aumentato con una tecnica moltiplicativa, quale raddoppiarlo ogni volta che scade, fino ad una soglia preimpostata, come ad esempio $T_O \leq 60 \text{s}$. Quando viene ricevuto il primo ACK di un segmento non ritrasmesso si ritorna alla procedura standard.

### Fast retransmit

![Esempio di ritrasmissione con e senza *Fast retransmit*](../images/transport-Untitled%2034.png)

Esempio di ritrasmissione con e senza *Fast retransmit*

Normalmente, la ritrasmissione di un segmento avviene inviando nuovamente il pacchetto perso dal buffer del trasmettitore, ma in ogni caso il ricevitore invia immediatamente l'ACK che indica come AN il segmento mancante. Il nuovo ACK cumulativo viene trasmesso dal ricevitore solo dopo aver ricevuto il segmento mancante ed il trasmettitore ritrasmette il segmento solo dopo la scadenza del timeout. Un metodo più efficiente sarebbe che il trasmettitore inviasse più velocemente il pacchetto perso.

Questo metodo è stato implementato con il ***Fast retransmit*** (RFC 2001): alla ricezione di tre ACK consecutivi *ripetuti* si procede alla ritrasmissione anche prima che scatti il timeout. Fondamentalmente, questi tre ACK equivalgono ad un NACK implicito. Per funzionare, il Fast retransmit richiede che il *Delayed ACK* venga disabilitato.

## Controllo di congestione

Il controllo di flusso dipende solo dalla capacità del ricevitore e non è sufficiente ad evitare la congestione nella rete. Nella rete Internet attuale non ci sono meccanismi sofisticati di controllo di congestione a livello rete. Il controllo di congestione è perciò **delegato interamente al TCP**. Poiché TCP è implementato solo negli host, il controllo di congestione è di tipo *end-to-end*.

Un evento di congestione si verifica quando il rate di trasmissione porta in congestione un link sul percorso in rete verso la destinazione.

<aside>
📓 Un link è **congestionato** quando la **somma dei rate** di trasmissione dei flussi che lo attraversano è **maggiore** della sua **capacità**.

</aside>

$$\sum_i R_i > C$$

Il modo più naturale per controllare il ritmo di immissione in rete dei dati per il TCP è quello di **regolare la finestra di trasmissione**.
Il trasmettitore mantiene una **Congestion Window** $C_{wnd}$ che varia in base agli eventi che osserva, quali ricezioni di ACK e timeout.
In ogni istante, la finestra del trasmettitore è **dimensionata al minimo** tra $R_{wnd}$ e $C_{wnd}$:

$$S_{wnd} = \text{min}(R_{wnd}, C_{wnd})$$

> [!important] L'idea di base del controllo di congestione del TCP è quella di **interpretare la perdita di un segmento**, segnalata dallo scadere di un timeout di ritrasmissione, **come un evento di congestione**.

La reazione ad un evento di congestione è quella di **ridurre l'ampiezza della finestra di congestione** $C_{wnd}$.

### Slow start e Congestion avoidance

Il valore $C_{wnd}$ viene aggiornato dal trasmettitore in base ad un algoritmo. Il modo in cui avviene l'aggiornamento dipende dalla **fase** o **stato** in cui si trova il trasmettitore, che in generale può essere:

- Slow start
    
    All'inizio di una connessione, il trasmettitore pone $C_{wnd} = 1 \text{MSS}$ e la $\text{Ssthresh}$ ad un valore molto elevato. Essendo vera la relazione $C_{wnd} < \text{Ssthresh}$, si inizia in Slow start.
    
    > [!note] In Slow start, la $C_{wnd}$ viene incrementata di **1 MSS per ogni ACK** ricevuto.
    
    ![Schematizzazione dell'incremento di $C_{wnd}$ in *Slow start*](../images/transport-Untitled%2035.png)
    
    Schematizzazione dell'incremento di $C_{wnd}$ in *Slow start*
    
    Al contrario di quanto faccia credere il nome, l'incremento della finestra avviene in esponenzialmente.
    
    L'incremento del numero di segmenti inviati può continuare fino al verificarsi di almeno uno dei seguenti eventi:
    
    - $C_{wnd} \geq \text{Ssthresh}$, ossia entro in Congestion avoidance
    - Si verifica il primo **evento di congestione** e scade un timeout
    - $C_{wnd} \geq R_{wnd}$, ossia la finestra di congestione continua ad aumentare, ma la finestra di trasmissione è comunque vincolata dalla finestra di ricezione
- Congestion avoidance
    
    Slow start continua fino a quando $C_{wnd} = \text{Ssthresh}$, quando inizia la fase di **Congestion avoidance**.
    
    > [!note] In Congestion avoidance, la $C_{wnd}$ viene incrementata di $\frac{1}{C_{wnd}}$ **per ogni ACK** ricevuto.
    
    Se la $C_{wnd}$ consente di trasmettere $W$ segmenti, la ricezione degli ACK relativi a tutti i $W$ segmenti porta la $C_{wnd}$ ad aumentare di un segmento. Congestion avoidance usa quindi un incremento lineare.
    
    ![Schematizzazione dell'incremento di $C_{wnd}$ in *Congestion avoidance (approssimato, poiché l'incremento avviene ad ogni ACK)*](../images/transport-Untitled%2036.png)
    
    Schematizzazione dell'incremento di $C_{wnd}$ in *Congestion avoidance (approssimato, poiché l'incremento avviene ad ogni ACK)*
    

Per distinguere fra le due fasi si usa una soglia, $\text{Ssthresh}$, gestita dall'entità TCP al trasmettitore:

- $C_{wnd} < \text{Ssthresh} \implies \text{Slow start}$
- $C_{wnd} \geq \text{Ssthresh} \implies \text{Congestion avoidance}$

Insieme alla finestra, aumenta anche il **rate di trasmissione**, stimato come:

$$R = \frac{C_{wnd}}{\text{RTT}}$$

Ad un certo punto, la trasmissione può diventare continua.

Se avviene congestione, ovvero se scade un timeout, sia in caso di Slow start che in caso di Congestion avoidance, **la finestra non cresce più** ed il TCP interviene per **modificare il valore di $\text{Ssthresh}$ e $C_{wnd}$** in questo modo:

$$\text{Ssthresh} = \text{max}\bigg (2\text{MSS}, \frac{\text{FlightSize}}{2} \bigg ), \space C_{wnd} = 1$$

dove $\text{FlightSize}$ indica i byte trasmessi ma mai riscontrati. Si noti che alcune versioni di TCP possono impostare la dimensione di finestra di congestione ad un altro valore e che generalmente vale $\text{FlightSize} = S_{wnd}$.

Perciò abbiamo che $C_{wnd} < \text{Ssthresh}$, e quindi si torna alla fase di Slow start, ed il segmento che viene inviato per primo è quello per cui era scaduto il timeout, dato che le ritrasmissioni hanno sempre la precedenza sulle nuove trasmissioni.

In seguito, a seconda della versione di TCP, possono succedere due cose:

- **Versioni odierne** (*TCP Reno*): il ricevitore accetta anche i fuori sequenza ed invia un ACK cumulativo appena riceve i segmenti mancanti
- **Versioni base** (*TCP Tahoe*): il trasmettitore ritrasmette tutti i segmenti successivi già trasmessi poiché il ricevitore li ha eliminati, essendo fuori sequenza

Il valore a cui è posta $\text{Ssthresh}$ corrisponde ad una stima conservativa della finestra ottimale, che eviterebbe futuri eventi di congestione.

![Esempio di funzionamento di controllo congestione in TCP](../images/transport-Schermata_2021-04-01_alle_14.19.01.png)

Esempio di funzionamento di controllo congestione in TCP

- Altre versioni di TCP
    - **Tahoe**: non implementa il Fast retransmit e non accetta fuori sequenza
    - **Reno**: implementa sia Fast retransmit che Fast recovery, in cui, dopo la fase di Congestion avoidance, si salta la fase di Slow start ponendo $C_{wnd} = \text{Ssthresh}$. Inoltre Reno accetta i fuori sequenza ed implementa il NACK implicito. Infatti, dopo aver ricevuto 3 ACK ripetuti, imposta $\text{Ssthresh} = \text{max} \bigg (2\text{MSS}, \frac{\text{FlightSize}}{2} \bigg )$.
    - **Vegas**: tenta di evitare la congestione, invece di reagire ad essa
    - **Westwood**, **Tibet**: versioni TCP ottimizzate per scenari wireless
