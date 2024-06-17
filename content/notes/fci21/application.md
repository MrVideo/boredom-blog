---
title: 'Livello applicativo'
draft: false
type: 'page'
toc: true
mathjax: true
---

## Cosa significa creare un’applicazione di rete?

Significa scrivere un software che possa:

- Essere eseguito su diversi terminali
- Comunicare con altri software remoti tramite la rete

Il **browser web**, per esempio:

- È un software in esecuzione su un dispositivo
- Comunica con altri software tramite la rete

Le applicazioni sono solo **nei terminali** e possono essere facilmente sviluppate e diffuse. Inventare una nuova applicazione **non richiede di cambiare il software della rete**. I nodi **non contengono software applicativo**.

## Architetture

### Client-server

I dispositivi coinvolti nella comunicazione implementano o solo il processo *client* o solo il processo *server.*

I dispositivi *client* e *server* hanno caratteristiche diverse:

- Server:
    - Deve essere **sempre attivo** e raggiungibile
    - Possono **ricevere richieste** da molti client
    - Hanno indirizzo **IP fisso**
- Client:
    - **Comunicano solo con il server**, non con altri client
    - Possono essere connessi in modo **discontinuo**
    - Possono **cambiare indirizzo IP**
    - Possono inviare **più richieste allo stesso server**

### Peer-to-peer

- I dispositivi coinvolti implementano sia la porzione *client* sia quella *server*
- **Non ci sono server sempre connessi**
- I terminali comunicano **direttamente**
- I peer sono collegati in modo **intermittente** e **possono cambiare indirizzo IP**

Alcuni esempi possono essere **BitTorrent** e **Skype**.

## Elementi fondamentali per un applicazione di rete

- **Host**: dispositivo d’utente (laptop, smartphone, desktop…)
- **Processo**: programma software in esecuzione su un host
- **Comunicazione inter-processo** (*IPC*): tecnologie software il cui scopo è consentire a diversi processi di comunicare scambiandosi informazioni e dati
    - Processi **locali**: risiedono sullo stesso host
    - Processi **remoti**: risiedono sul host diversi
        - Perché funzionino c’è bisogno di **indirizzamento** dei processi (bisogna conoscere l’indirizzo del processo e dell’host su cui il processo è in esecuzione) e di **protocolli** di scambio di dati, che decide i tipi, la sintassi, la semantica e la tempistica dei messaggi.

### Indirizzamento

Lo scambio dei messaggi tra processi applicativi:

- È supportato dai servizi offerti dai livelli inferiori a quello applicativo
- Avviene attraverso i **SAP** (*Service Access Point*)

Ogni processo è associato ad un **SAP** del livello inferiore (trasporto), al quale è associata a sua volta l’**informazione di indirizzamento del processo nell’host** (*socket*).

![Struttura di un SAP](../images/Untitled.png)

Struttura di un SAP

**Esempio**: cosa identifica il browser Chrome in esecuzione sul nostro smartphone?

- Indirizzo dell’*host*: indirizzo IP univoco di 32 bit
- Indirizzo del **SAP**: associato al processo in esecuzione sull’host: **numero di porta**

<aside>
📓 **Indirizzo di un processo in esecuzione su un host**:
Indirizzo IP + numero di porta = **Socket**

</aside>

Le socket sono “*porte di comunicazione*“:

- Il processo trasmittente mette il messaggio “*fuori dalla porta*“.
- La rete raccoglie il messaggio e lo trasporta fino alla porta del destinatario

### Quale protocollo di trasporto usare?

**Requisiti**:

- **Affidabilità**: alcune applicazioni possono tollerare perdite parziali, altre richiedono totale affidabilità.
- **Ritardo**: alcune applicazioni richiedono un ritardo molto basso.
- **Banda**: alcune applicazioni richiedono un minimo di velocità di trasferimento, altre si adattano alla velocità disponibile (*applicazioni elastiche*).

## TCP e UDP

- **TCP**: *Transmission Control Protocol*
    - **Connection-oriented**: instaurazione della connessione prima dello scambio di dati
    - **Trasporto affidabile**: nessuna perdita
    - **Controllo di flusso**: il trasmettitore regola la velocità in base al ricevitore
    - **Controllo di congestione**: per impedire di sovraccaricare la rete
    - **Controllo di errore**: per garantire l’integrità dell’informazione
- **UDP**: *User Datagram Protocol*
    - **Connectionless**: nessuna connessione prima dello scambio di dati
    - **Trasporto non affidabile**: possibili perdite
    - **Nessun controllo di flusso**
    - **Nessun controllo di congestione**
    - **Controllo di errore**: opzionale

| Servizio | Protocollo applicativo | Protocollo di trasporto | Standard |
| --- | --- | --- | --- |
| Posta elettronica | SMTP | RFC 5321 | TCP |
| Web | HTTP | RFC 2616 | TCP |
| Trasferimento file | FTP | RFC 959 | TCP |
| Traduzione nomi di dominio | DNS | RFC 1034-1035 | UDP |
| Assegnazione indirizzi IP | DHCP | RFC 2131 | UDP |
| Protocollo di instradamento inter-dominio | BGP | RFC 4271 | TCP |
| Protocollo di instradamento intra-dominio | RIP | RFC 2453 | UDP |
| Telefonia audio/video | SIP
RTP
Skype | RFC 3261
RFC 3550
Proprietario | Tipicamente UDP
Tipicamente UDP
TCP e UDP |
| Streaming on-demand |  | Proprietario | Tipicamente TCP |
| Streaming live |  | Proprietario | Tipicamente UDP |

## Primitive socket

Per richiedere e fornire un servizio, il processo applicativo scambia informazioni al livello di trasporto tramite delle **primitive di servizio** attraverso le socket. Possono essere inviate da client, server o entrambi.

### Caso TCP

Operazioni iniziali:

- Server: *passive open*
- Client: *active open*

[Primitive di servizio TCP](https://www.notion.so/7804f1ea48dc4b37ae8005b8e0c3c423)

![Colloquio TCP tra un client ed un server](../images/Untitled%201.png)

Colloquio TCP tra un client ed un server

### Caso UDP

Non ci sono primitive per l’instaurazione di una connessione e generalmente le operazioni sono simili. Le differenze principali sono in `Send()` e `Receive()`, poiché non essendo instaurata una connessione preliminare è necessario specificare a chi mandare e da chi ricevere informazioni.

[Primitive di servizio UDP](https://www.notion.so/5fb56ef9ecdf486fbda2aa96cda5fc92)

---

## Il servizio di Web Browsing

Le pagine web sono fatte di *oggetti*. Gli oggetti possono essere file HTML, immagini, applet [Java](Università/Anno%203/Semestre%201/Ingegneria%20del%20Software/Java.md), file audio e video, collegamenti ad altre pagine web…

Generalmente le pagine sono costituite da un file HTML o php base che **chiama** gli altri oggetti. 

<aside>
📓 Ogni oggetto è **indirizzato** da una *Uniform Resource Locator* (**URL**), per esempio: `http://www.polimi.it:80/index.html`.

</aside>

### Protocollo HTTP

L’architettura per l’HTTP si basa sul client-server. Il client è il **browser** che effettua **richieste di pagine web**, le riceve e le mostra all’utente; il server **invia gli oggetti richiesti** tramite **risposte HTTP**.

L’HTTP è un protocollo **stateless**, ossia il server non mantiene uno stato della connessione, un registro dell’interazione client-server.

L’HTTP si appoggia su **TCP** a livello di trasporto:

1. Il client HTTP inizia una connessione TCP attraverso il server (porta 80)
2. Il server HTTP accetta connessioni TCP da client HTTP
3. Client e server HTTP si scambiano informazioni
4. La connessione TCP tra client e server HTTP viene chiusa

#### Modalità di connessione

Le modalità di connessione sono **persistente** e **non persistente**:

- **Non persistente** (HTTP v1.0 default mode)
    - **Una connessione** TCP **per una sola sessione** richiesta-risposta; inviato l’oggetto, il server chiude la connessione TCP
    - La procedura viene **ripetuta per tutti i file** collegati al documento base
    - Le connessioni TCP per più oggetti **possono esser aperte in parallelo** per minimizzare il ritardo
- **Persistente**
    - La connessione TCP **rimane aperta** e può essere usata per trasferire più oggetti della stessa pagina web o più pagine web.
        - *Without pipelining*: richieste HTTP inviate in serie, si aspetta la risposta prima di fare una nuova richiesta (HTTP v1.1 default mode)
        - *With pipelining*: le richieste HTTP vengono accodate ed inviate insieme, senza attendere la risposta (HTTP v1.1 supported mode)

#### Round Trip Time (RTT)

Tempo necessario per trasferire un messaggio dal client al server e ritorno e per ricevere il relativo ACK.

Tempo di trasferimento in HTTP:

- un RTT per **iniziare** la connessione TCP
- un RTT per **inviare i primi byte** della richiesta HTTP e ricevere i primi byte di risposta
- tempo di **trasmissione dell’oggetto**

Il tempo è **soltanto una stima**, non è un calcolo preciso.

Supponendo che la pagina web contenga 10 oggetti oltre al file HTML base, il tempo di download dell’intera pagina è:

- Non persistente:
    
    $$T_{\text{non persistente}} = \sum_{i=0}^{10} (2\text{RTT} + T_i)$$
    
- Persistente:
    
    $$T_{\text{persistente}} = \text{RTT} \space + \sum_{i = 0}^{10}(\text{RTT} + T_i)$$
    

#### Tempistiche di comunicazione persistente e non persistente

![HTTP 1.0 non persistente](../images/Untitled%202.png)

HTTP 1.0 non persistente

![HTTP 1.1 persistente, senza pipelining](../images/Untitled%203.png)

HTTP 1.1 persistente, senza pipelining

![HTTP 1.1 persistente, con pipelining](../images/Untitled%204.png)

HTTP 1.1 persistente, con pipelining

#### HTTP 1.1 e 2

L'**HTTP 1.1** permette il pipelining, ma **a condizione che gli oggetti richiesti vengano generati nello stesso ordine delle richieste**. Questo impone **Head Of Line** (**HOL**) **blocking** se c’è un oggetto particolarmente grande.

L'**HTTP 2** permette invece che un oggetto grande venga trasmesso **inframezzandolo con oggetti brevi**, grazie alla **gestione a stream**: si può formare rapidamente un’anteprima della pagina, anche se con qualche dettaglio in meno.

![Esempio di frammentazione nell'HTTP 2](../images/Untitled%205.png)

Esempio di frammentazione nell'HTTP 2

#### Messaggi HTTP

- Richieste
    
    I messaggi sono codificati in **ASCII** (*human-readable*)
    
    ![Struttura di una richiesta HTTP](../images/Untitled%206.png)
    
    Struttura di una richiesta HTTP
    
    - **Request line**: *Method*, *URL*, *Version*
        - **Method**: tipo di operazione che il client richiede al server
        - **URL**: identifica la risorsa locale rispetto al server
        - **Version**: indica la versione del protocollo HTTP
    - **Header lines**
    - **Entity body** (generalmente vuoto, pieno nel caso di alcuni metodi come `POST`)
    
    **Esempi di metodi**:
    
    - `GET`: È usato quando il client vuole **scaricare un documento dal server** (specificato nell’URL). Il server normalmente risponde con il documento richiesto nel corpo del messaggio di risposta.
    - `HEAD`: È usato quando il client non vuole **scaricare** il documento ma **solo alcune informazioni sul documento** (come ad esempio la data di ultima modifica). Nella risposta il server non inserisce l’intero documento ma solo degli header informativi.
    - `POST`: È usato per fornire al server degli **input da utilizzare per un particolare oggetto** identificato nell’URL.
    - `PUT`: È utilizzato per **memorizzare un documento nel server**. Il documento viene fornito nel corpo del messaggio e la posizione di memorizzazione nell’URL.
    
    Altri metodi: `PATCH`, `COPY`, `MOVE`, `DELETE`, `LINK`, `UNLINK`, `OPTIONS`
    
    Header HTTP: servono per scambiare informazione di servizio aggiuntiva. È possibile inserire più linee di header per messaggio. Alcuni header sono:
    
    - `Cache-control`: informazioni sulla cache
    - `Accept`: formati accettati
    - `Accept-language`: linguaggio accettato
    - `Authorization`: mostra i permessi del client
    - `If-modified-since`: invia il documento richiesto solo se modificato
    - `User-agent`: tipo di *user agent*
    
    ```
    GET /index.html HTTP/1.1\r\n
    Host: www-net.cs.umass.edu\r\n
    User-Agent: Firefox/3.6.10\r\n
    Accept: text/html,application/xhtml+xml\r\n
    Accept-Language: en-us,en;q=0.5\r\n
    Accept-Encoding: gzip,deflate\r\n
    If-modified-since: <date>
    Accept-Charset: ISO-8859-1,utf-8;q=0.7\r\n
    Keep-Alive: 115\r\n
    Connection: keep-alive\r\n
    \r\n
    ```
    
- Risposte
    
    ![Struttura di una risposta HTTP](../images/Untitled%207.png)
    
    Struttura di una risposta HTTP
    
    - **Status line**: *Version*, *Status code*, *Phrase*
        - **Status code**: codice che informa il client di alcuni eventi
        - **Phrase**: messaggio di stato, correlato al codice di stato (*OK*, *Bad Request*…)
            
            
            | Significato | Numero | Esempi |
            | --- | --- | --- |
            | Informational | 1 | 100 Continue |
            | Success | 2 | 200 OK |
            | Redirection | 3 | 301 Moved Permanently
            302 Moved Temporarily
            304 Not Modified |
            | Client error | 4 | 400 Bad Request
            401 Unauthorized
            404 Not Found |
            | Server error | 5 | 500 Internal Server Error
            501 Not Implemented
            503 Service Unavailable |
    - **Header lines**
    - **Entity body** (generalmente pieno, contiene l’elemento richiesto dal client)
    
    ```
    HTTP/1.1 200 OK\r\n
    Date: Sun, 26 Sep 2010 20:09:20 GMT\r\n
    Server: Apache/2.0.52 (CentOS)\r\n
    Last-Modified: Tue, 30 Oct 2007 17:00:02 GMT\r\n
    ETag: "17dc6-a5c-bf716880"\r\n
    Accept-Ranges: bytes\r\n
    Content-Length: 2652\r\n
    Keep-Alive: timeout=10, max=100\r\n
    Connection: Keep-Alive\r\n
    Content-Type: text/html; charset=ISO-8859-1\r\n
    \r\n
    <dati dell'Entity Body>
    ```
    

#### Conditional GET

Ha l’obiettivo di **non inviare un oggetto** richiesto **se è già presente presso il client**. Si inserisce nella richiesta HTTP **la data dell’oggetto** presente in *cache* locale **tramite l’header**: `If-modified-since: <date>`. La risposta HTTP **non contiene l’oggetto** richiesto **se la copia** presente al client **è aggiornata**.

**Risposta**: `HTTP/1.0 304 Not Modified`

#### Mantenere uno “stato” in HTTP

Poiché l’HTTP è *stateless*, i fornitori di contenuti possono usare i **cookies** per tracciare le attività dell’utente.

![Esempio di impostazione di cookie](../images/Untitled%208.png)

Esempio di impostazione di cookie

- **Elementi dei cookie**
    1. Un header `set-cookie` nelle risposte HTTP
    2. Un header `cookie` nella prossima richiesta HTTP
    3. Una lista di cookie mantenuta sull’host (nella cache del browser)
    4. Un database di cookie mantenuto dal sito web

#### Proxy HTTP

Hanno l’obiettivo di fare un *caching* di più alto livello. Devono rispondere alle richieste HTTP **senza coinvolgere il server** HTTP, in modo da memorizzare quella pagina web e far sì che altri utenti connessi al Proxy ricevano la stessa pagina richiesta **più velocemente**. Il client invia tutte le richieste HTTP al Proxy. Se il Proxy ha già la risorsa richiesta, sarà lui a rispondere. Altrimenti sarà il Proxy a interrogare il server d’origine per ricevere la risorsa.

![Struttura di una rete con proxy](../images/Untitled%209.png)

Struttura di una rete con proxy

I Proxy sono definiti *application gateway*, ovvero instradatori di messaggi di livello applicativo (sono host *fittizzi*). Devono essere sia client, nei confronti del server d’origine, sia server, nei confronti degli utenti ad esso connessi, contemporaneamente. L’utilizzo di un Proxy fa sì che un server veda tutte le connessioni ad esso fatte arrivare dal Proxy, come se le avesse fatte **un singolo utente**.

#### Condivisione equa di risorse

La velocità di trasferimento di una rete dipende da molti fattori:

- Trasmissione
- Propagazione
- Accomodamento nei nodi
- Connectionless e Connection-oriented

Si può mostrare che in condizioni ideali il meccanismo di controllo del **TCP** (Connection-oriented) è in grado di:

- Consentire una **suddivisione equa della capacità di ciascun link** tra i diversi flussi che lo attraversano
- Limitare la **congestione di rete**

Nella realtà, i valori dei rate indicati sono solo valori medi e valgono solo in condizioni ideali e a regime (flussi di lunga durata). Il ritmo di trasmissione cambia sempre e in condizioni reali la condivisione può non essere equa.

![../images/Untitled%2010.png](../images/Untitled%2010.png)

![../images/Untitled%2011.png](../images/Untitled%2011.png)

![../images/Untitled%2012.png](../images/Untitled%2012.png)

---

## Posta elettronica

### Elementi

- **User Agent** (UA): client d’utente
- **Mail Server**: ogni client è associato ad un Mail Server. Include il **Mail Transfer Agent**, processo applicativo necessario per il trasferimento dei messaggi sia da client a server, sia tra server.
- **Protocolli**
    - **SMTP**: *Simple Mail Transfer Protocol*, si occupa della trasmissione della mail in uscita
    - **POP3/IMAP**: *Post Office Protocol V.3* e *Internet Message Access Protocol*, si occupano del ricevimento delle email in entrata

Per ogni client, i mail server contengono:

- Una coda di email in ingresso (*Mailbox*)
- Una coda di email in uscita (condivisa tra tutti gli utenti)

### Esempio di trasferimento email

1. Il mittente **compone** una mail per un destinatario
2. Il client d’utente **invia la mail al proprio mail server**
3. Il mail server si comporta come **client SMTP** e apre una **connessione TCP** sulla porta **25 con il mail server del destinatario**
4. **Il client** SMTP **invia la mail** sulla connessione TCP
5. Il mail server del destinatario **memorizza la mail** nella *mailbox* del destinatario
6. Il destinatario usa il proprio **client** per **leggere la mail** usando un **protocollo differente** (POP3, IMAP…)

Si parla di protocollo di tipo **push** dalla parte dell’invio della mail (la mail viene *spinta* verso il destinatario), mentre si parla di tipo **pull** dalla parte del destinatario della mail (la mail viene *tirata* dal mail server al client).

### SMTP

È un protocollo applicativo di tipo *push* ed utilizza la porta 25 del server.

Quando un mail server riceve un messaggio da un utente:

- Il server lo mette in coda
- Apre una connessione TCP sulla porta 25 del mail server del destinatario
- Trasferisce il messaggio
- Chiude la connessione TCP

L’interazione tra client SMTP e server SMTP è di tipo *comando-risposta*, ossia il client fa richieste e il server dà risposte. Sia comandi che risposte sono testuali e ciò richiede che anche il corpo dei messaggi sia ASCII.

| Header | Significato |
| --- | --- |
| From: | Indirizzo email dell'autore del messaggio |
| To: | Indirizzo email del destinatario del messaggio |
| Cc: | Indirizzi email di altri destinatari in copia |
| Bcc: | Indirizzi email di altri destinatari in copia nascosta ai precedenti destinatari |
| Date: | Data e ora di generazione del messaggio pronto per l'invio |
| Sender: | Indirizzo email di origine del messaggio |
| Subject: | Argomento del messaggio |
| Message-Id: | Identificatore univoco del messaggio |
| Reply-To: | Identificatore del messaggio originario cui si risponde |
| Received: | Identificatore del MTA lungo il percorso e data/ora di attraversamento |
| Return-Path: | Indicatore di un percorso di ritorno verso il mittente |

#### Fasi del colloquio

1. **Apertura connessione** TCP tra client (sia User Agent che Mail Transfer Agent) e server (sempre Mail Transfer Agent)
2. Il client avvia una *fase di presentazione* verso il server
3. Si **trasferisce il messaggio** (prima header, poi messaggio)
4. **Richiesta chiusura** connessione TCP
5. **Chiusura connessione TCP**

| Comando | Parametro | Funzione |
| --- | --- | --- |
| HELO | Dominio client | Richiesta di apertura della connessione con identificazione del client SMTP verso il server SMTP |
| MAIL FROM | Indirizzo mittente | Identificazione del mittente |
| RCPT TO | Indirizzo destinatario | Identificazione del destinatario |
| DATA |  | Richiesta di autorizzazione ad inviare il messaggio |
| QUIT |  | Richiesta di chiusura della connessione |
| RSET |  | Segnalazione di interruzione della transazione in atto |
| VRFY | Stringa | Richiesta di verifica identificazione di utente o di mailbox |

| Significato | Parametro | Codice |
| --- | --- | --- |
| Servizio pronto | Dominio server | 220 |
| Servizio in fase di chiusura | Dominio server | 221 |
| Comando richiesto completato |  | 250 |
| Utente non locale, messaggio da inoltrare |  | 251 |
| Autorizzazione a invio email |  | 354 |
| Server non disponibile, canale in chiusura | Dominio server | 421 |
| Comando richiesto ignorato: mailbox non disponibile |  | 450 |
| Comando interrotto: errore locale |  | 451 |
| Comando richiesto ignorato: memoria insufficiente |  | 452 |
| Server non disponibile ad accettare i parametri |  | 455 |
| Errore di sintassi |  | 500 |
| Errore di sintassi nei parametri o negli argomenti |  | 501 |
| Comando non implementato |  | 502 |
| Sequenza di comandi errata |  | 503 |
| Parametro del comando non implementato |  | 504 |
| Comando richiesto ignorato: mailbox insidponibile |  | 550 |
| Utente non locale |  | 551 |
| Comando ignorato: memoria allocata insufficiente |  | 552 |
| Comando ignorato: nome della mailbox non corretto |  | 553 |
| Transazione fallita |  | 554 |
| Parametri dei comandi MAIL FROM/RCPT TO non riconosciuti o non implementati |  | 555 |

![Esempio di colloquio SMTP](../images/Untitled%2013.png)

Esempio di colloquio SMTP

### Protocolli di accesso alla mailbox

I tre protocolli usati solitamente sono:

- **POP3**, *Post Office Protocol V.3*: download “semplice” dei messaggi
- **IMAP**, *Internet Mail Access Protocol*: download dei messaggi e gestione della mailbox sul server
- **HTTP**

Sono tutti protocolli di tipo *pull*, che servono a scaricare *on-demand* la posta dalla propria mailbox. L’interazione tra client e server è sempre comando-risposta.

### POP3

Utilizza la **porta 110** del server. Le fasi della comunicazione sono:

- Instaurazione connessione TCP
- Autenticazione da parte del client
- Richiesta lista messaggi (vengono chieste solo le informazioni di base)
- Eventuale richiesta di download e/o cancellazione dei messaggi
- Chiusura comunicazione con il server
- Chiusura connessione TCP

| Comando | Parametro | Funzione |
| --- | --- | --- |
| USER | Nome | Richiesta di accesso alla mailbox |
| PASS | Stringa | Invio della password associata a USER |
| STAT |  | Interrogazione sul numero di messaggi ed occupazione nella mailbox |
| LIST | Numero messaggio (opzionale) | Interrogazione sui messaggi presenti nella mailbox |
| RETR | Numero messaggio | Richiesta di recupero di un messaggio dalla mailbox |
| DELE |  | Richiesta di cancellazione di un messaggio dalla mailbox |
| RSET |  | Richiesta di annullamento di precedenti ordini di cancellazione nella mailbox |
| NOOP |  | Nessuna operazione |
| QUIT |  | Richiesta di chiusura della comunicazione |

Le risposte del server sono solitamente di tre tipi:

1. `+OK`
2. `ERR`
3. Consegna dei messaggi

![Esempio di colloquio client-server con POP3](../images/Untitled%2014.png)

Esempio di colloquio client-server con POP3

## Risoluzione di nomi simbolici

Gli indirizzi IP (32 bit) si adattano bene ad essere letti e processati da macchine ma sono poco adatti ad essere usati dai software applicativi e dagli utenti. È molto più conveniente utilizzare indirizzi simbolici. Occorre quindi fare una **mappatura** fra indirizzi IP e nomi simbolici. Si definisce **risoluzione di un nome** la mappatura tra un nome simbolico ed un indirizzo IP.

### Domain Name System (DNS)

È un’applicazione client-server che utilizza il protocollo di trasporto **UDP** su porta **53**. Viene usato l’UDP perché la risoluzione dei nomi dev’essere veloce.

Ha una struttura basata su un database **distribuito**: esistono tanti **name server** (*NS*) con un’organizzazione *gerarchica*.

Esistono alcuni servizi aggiuntivi quali:

- *Host aliasing*: associazione tra vero nome host e suoi alias
- *Load distribution*: consente di distribuire il carico delle richieste di mapping tra molti NS distribuiti geograficamente ma che hanno le stesse informazioni di mapping

L’alta disponibilità del servizio è garantita dalla replicazione delle mappature tra nomi simbolici e indirizzi IP.

#### Struttura gerarchica

![Struttura gerarchica dei Name Server](../images/Untitled%2015.png)

Struttura gerarchica dei Name Server

Ha dei nodi *etichettati*, in cui il nodo root non ha etichetta, seguiti da **domini di primo livello**, di secondo, di terzo…

Il nome di dominio è la *sequenza di etichette* fino alla radice. La struttura del nome dipende dal suo albero.

![Divisione delle etichette tra Name Server](../images/Untitled%2016.png)

Divisione delle etichette tra Name Server

Ad ogni dominio corrispondono uno o più server (*Name Server*). Ogni livello nella gerarchia ha diversa *profondità* di informazione: per esempio, se voglio raggiungere `www.google.com`, i Root NS sanno come trovare i name server che gestiscono i domini `.com`, I TLD NS possono trovare chi gestisce `google.com` e i NS di livello inferiore possono risolvere l’ultima parte `www.`.

Altri tipi di NS comprendono:

- **Local Name Server**: Ogni ISP ha un NS locale, direttamente collegato all’host. Tutte le volte che un host deve risolvere un indirizzo simbolico, esso contatta il Local NS ed esso, eventualmente, contatta gli altri Name Server.
- **Authoritative Name Server**: NS *responsabile* di un particolare nome simbolico.

#### Esempio di ottenimento associazione nome simbolico-indirizzo IP

Ogni host ha configurato l’indirizzo del Local Name Server. Le applicazioni che richiedono l’associazione usano le funzioni del DNS. Il Local NS reperisce l’informazione e restituisce la risposta:

- Immediatamente, se l’informazione è disponibile nel suo database
- Cercando con due modalità in altri NS:
    - Iterativa
        
        Un host presso `cis.poly.edu` vuole risolvere l’indirizzo simbolico `gaia.cs.umass.edu`.
        
        1. Il client DNS dell’host contatta il Local Name Server
        2. Il LSN contatta il Root Name Server e il server segnala il responsabile del dominio `.edu`
        3. Il LSN contatta il Top Level Domain Server responsabile di `.edu` e riceve l’indirizzo del server autorevole per il nome simbolico `gaia.cs.umass.edu`
        4. Il LSN contatta il server autorevole ed esso risponde con l’IP del dominio `gaia.cs.umass.edu`
        
        Ora il client ha l’IP cercato e può connettersi alla pagina richiesta.
        
    - Ricorsiva
        
        Riprendendo le premesse dell’esempio precedente, invece di rispondere con l’indirizzo di un altro NS tutte le volte, l’informazione viene passata da server a server, percorrendo prima la catena di server verso l’autorevole corretto e poi al contrario, per tornare al client e restituire l’indirizzo IP richiesto.
        

#### DNS Caching

Un server, dopo aver reperito un’informazione su cui non è autorevole, può memorizzarla temporaneamente nella cache. All’arrivo di una nuova richiesta può fornire l’informazione senza risalire di nuovo fino al server autorevole. Il **Time-To-Live**, ossia letteralmente *tempo di vita*, è una quantità di tempo decisa dal server autorevole per decidere quanto tempo può sopravvivere l’informazione richiesta dall’host nella sua stessa cache.

Un record della cache DNS è costituito da *Name*, *Value*, *Type* e *TLL*. A seconda di *Type*, gli altri campi hanno significato diverso:

- `Type = A`: *Name* è il nome di un host autorevole e *Value* è il suo indirizzo IP
- `Type = NS`: *Name* è un dominio e *Value* è il nome di un server che può ottenere le informazioni relative
- `Type = CNAME`: *Name* è un nome alternativo per un host, il cui nome canonico è in *Value*
- `Type = MX`: *Name* è un dominio di mail e *Value* è il nome del mail server

#### Formato dei messaggi DNS

![Struttura messaggi DNS](../images/Untitled%2017.png)

Struttura messaggi DNS

- `Identification`: identificativo coppia richiesta-risposta
- `Flag`: richiesta-risposta, authoritative-non authoritative, iterative-recursive
- `Number of`: relativo al numero di campi nelle sezioni successive
- `Questions`: nome richiesto e tipo (solitamente A o MX)
- `Answers`: resource records completi forniti in risposta
- `Authority`: contiene altri record forniti da altri server autorevoli
- `Additional info`: informazione aggiuntiva come per esempio il record con l’indirizzo IP per il MX fornito in `Answers`
