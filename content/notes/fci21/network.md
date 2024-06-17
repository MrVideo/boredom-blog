---
title: 'Livello di rete'
draft: false
type: 'page'
toc: true
mathjax: true
---

---

Lo strato di trasporto si occupa di realizzare la comunicazione tra due processi applicativi remoti. Nonostante ciò, i due nodi generalmente sono distanti tra loro e collegati per mezzo di altri nodi, perciò è grazie al **livello di rete** che si realizza l'instradamento della connessione.

Lo strato di trasporto si occupa di realizzare la comunicazione tra due processi applicativi remoti. Nonostante ciò, i due nodi generalmente sono distanti tra loro e collegati per mezzo di altri nodi, perciò è grazie al **livello di rete** che si realizza l'instradamento della connessione.

## Architettura dei protocolli di rete

Ci sono diversi protocolli che controllano vari aspetti della connessione nel livello di rete, suddivisi in piani.

| Name               | Descrizione                                                              | Protocolli                |
| ------------------ | ------------------------------------------------------------------------ | ------------------------- |
| Piano dati         | Protocolli per trasferire i dati utente                                  | IP                        |
| Piano di controllo | Protocolli di segnalazione per supportare il trasferimento dati          | ARP, RARP, OSPF, RIP, BGP |
| Piano di gestione  | Protocolli di segnalazione per configurare e gestire errori ed eccezioni | ICMP, SNMP                |

I protocolli dello strato di rete sono implementati sia in host, sia in router*.*

Lo strato di rete trasferisce i segmenti dello strato di trasporto dall'host sorgente all'host di destinazione. Al lato sorgente, i segmenti vengono incapsulati in datagrammi IP

| Name                                      | Descrizione                                                                                                                  |
| ----------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| Indirizzamento                            | Identificazione univoca dell'interfaccia di rete di un host o router                                                         |
| Inoltro                                   | Funzione locale con cui il router trasferisce i pacchetti dall'ingresso all'uscita                                           |
| Instradamento                             | Serve a determinare i percorsi dei pacchetti dalla sorgente alla destinazione. Viene svolto attraverso algoritmi di routing. |
| Diagnostica di rete                       | Segnalazione di errori di varia natura svolta attraverso il protocollo ICMP.                                                 |
| Assegnamento ed associazione di indirizzi | Assegnazione di indirizzi IP dinamici (ARP, DHCP)                                                                            |

Esistono diverse tipologie di algoritmi di routing: centralizzato o distribuito, statico o dinamico, manuale o automatico...

L'inoltro viene fatto attraverso le **tabelle di routing**, che vengono definite attraverso gli algoritmi di routing. Generalmente, nelle tabelle di routing si ritrovano informazioni su **gruppi di indirizzi IP**, che servono al nodo per inoltrare nella direzione giusta il proprio datagramma.

## Indirizzamento IPv4

Gli indirizzi IP sono assegnati su *base globale*. Internet fa uso anche di nomi simbolici, anch'essi assegnati su base globale, che vengono risolti tramite l'applicativo DNS. Ad assegnarli è la **IANA** (*Internet Assigned Numbers Authority*), su base continentale, agglomerando zone contigue.

Un indirizzo IP è una stringa di numeri a 32 bit nella forma `x.y.z.w`, dove $x, y, z, w \in [0,255]$. Se ne deduce che per ogni numero di un IP abbiamo 8 bit. Ciascun indirizzo IP è associato ad un'interfaccia di rete.

L'indirizzo IP è costituito da due livelli:

- `NET-ID`: **prefisso di rete** o ***network prefix***, comune a tutti gli indirizzi IP di una rete
- `HOST-ID`: distingue gli **host sulla stessa rete**

Esistono due valori di `HOST-ID` particolari, che non possono essere assegnati a nessun host:

- Tutti 0: utilizzato quanto si vuole individuare l'intera rete `NET-ID`
- Tutti 1: utilizzato come indirizzo di broadcast della rete `NET-ID`

La notazione *slash-n* indica che la lunghezza del prefisso è data dai primi $n$ bit dell'indirizzo. Un'altra notazione equivalente è l'utilizzo della **netmask**, che contiene 1 in tutti i bit relativi alla parte rete, e 0 per la parte host. Consente di individuare l'identificativo di rete di un qualunque indirizzo del blocco tramite una semplice operazione logica tra bit.

### Indirizzamento *Classful*

In origine, sono state definite 5 classi di indirizzi IP.

[Classi di indirizzi IP](https://www.notion.so/e5fd9e97d44d4a59bb440c9d340d4b28)

| Name | Struttura | Descrizione |
| --- | --- | --- |
| Indirizzo di rete | NET-ID specifico, HOST-ID tutto 0 | Utilizzato nelle tabelle di routing |
| Broadcast diretto | NET-ID specifico, HOST-ID tutto 1 | Usato per inviare un pacchetto a tutti gli host di una stessa rete |
| Limited broadcast | 255.255.255.255 | Funziona come il broadcast diretto, ma non può uscire dalla rete in cui viene inviato, infatti viene bloccato dai router. |
| Host concorrente sulla rete corrente | 0.0.0.0 | Un host che non conosce il proprio indirizzo IP (perché non gli è stato assegnato) utilizza questo |
| Specifico host della rete corrente | NET-ID tutto 0, HOST-ID specifico | È usato come indirizzo di destinazione nella comunicazione tra due host nella stessa rete IP |
| Indirizzo di loopback | 127.y.z.w | Serve a far comunicare dei processi localmente |

### Indirizzi privati

Utilizzabili da chiunque, ma solo in **ambito privato**. In internet possono essere riutilizzati più volte. Ne sono definiti tre blocchi:

| Name | IP iniziale | IP finale | Descrizione |
| --- | --- | --- | --- |
| Blocco 1 | 10.0.0.0 | 10.255.255.255 | Un'intera rete di classe A |
| Blocco 2 | 172.16.0.0 | 172.31.255.255 | 16 reti adiacenti di classe B |
| Blocco 3 | 192.168.0.0 | 192.168.255.255 | 256 reti adiacenti di classe C |

Un router non deve mai inoltrare un pacchetto con destinazione un indirizzo IP privato verso una propria interfaccia di uscita che abbia un indirizzo IP pubblico. Nei casi in cui ciò è necessario, si usa il **NAT** (*Network Address Translation*).

---

## Subnetting

![Esempio di subnet](../images/network-Untitled.png)

Esempio di subnet

Per reti di dimensioni molto grandi, può convenire creare varie **sottoreti** per rendere più efficienti le connessioni. Ogni sottorete, o *subnet*, è una rete fisica diversa.

Si può usare il terzo byte dell'IP per individuare la sottorete interessata.

Il valore di $n$, ossia il numero di bit per il subnet ID, si sceglie in funzione di:

- Quante sottoreti si vogliono creare
- Quanto devono essere estese le sottoreti

![Esempio di subnetting con indirizzi di classe B](../images/network-Untitled%201.png)

Esempio di subnetting con indirizzi di classe B

Per creare una subnet sarà necessaria una **subnet mask**, ossia una maschera più lunga di una di default, di lunghezza decisa dall'amministratore di sistema. La subnet mask indica dove si trova il confine tra subnet e host.

![IP Addressing nel caso di una subnet](../images/network-Untitled%202.png)

IP Addressing nel caso di una subnet

Nel caso di indirizzi di classe B con un subnet ID da 5 bit, avremmo una subnet mask con un prefisso lungo 21 bit: `11111111.11111111.11111000.00000000`, quindi la subnet mask sarebbe: `255.255.248.0`. Il NET_ID in tal caso sarebbe: `159.100.0.0`, l'extended network address, ossia il NET_ID con aggiunta di SUBNET_ID, diventerebbe: `159.100.8.0`.

### Netmask variabile

Esistono casi in cui il subnetting non basta. Per esempio, un'organizzazione che possiede un indirizzo di classe C ha bisogno di creare 3 sottoreti con 60 host ed altre 2 con 30 host, per un totale di 240 host. In questo caso:

- Subnet con 2 bit: 4 sottoreti con 62 host ciascuna
- Subnet con 3 bit: 8 sottoreti con 30 host ciascuna

In questi casi, si può usare la ***Variable Length Subnet Mask*** (**VLSM**). Funziona come applicare due netmask a cascata. La prima, `255.255.255.192/26`, definisce quattro subnet con 62 indirizzi per gli host. A una delle quattro subnet poi viene applicata la netmask `255.255.255.224/27`, che divide la sottorete in due ulteriori subnet, con 30 indirizzi per host.

![](../images/network-Untitled%203.png)

---

## Indirizzamento Classless

Il *Classless Inter-Domain Routing* (**CIDR**) è stato sviluppato nel settembre del 1993 (RFC 1517, 1518, 1519, 1520) ed è noto anche come *supernetting*.

L'indirizzamento classless è una soluzione fondamentale per contenere la crescita delle tabelle di routing, ma una soluzione temporanea per tamponare l'esaurimento degli indirizzi IP. La soluzione definitiva per l'esaurimento degli indirizzi IP è l'IPv6, che ha la possibilità di fornire $2^{128}$ indirizzi differenti.

### Regole del CIDR

Non essendo più ristretto a classi, il CIDR è più flessibile nell'allocazione di indirizzi IP. La notazione `x.y.z.w/n` indica un insieme di indirizzi contigui in cui il primo indirizzo è `x.y.z.w` e `/n` indica che ci sono $2^{32-n}$ indirizzi in totale, ossia che la maschera di rete è di $n$ bit.

Gli indirizzi privati espressi in notazione CIDR sono:

1. `10.0.0.0/8`
2. `172.16.0.0/12`
3. `192.168.0.0/16`

Il subnetting può essere utilizzato anche con indirizzamento CIDR.

### Classful vs. CIDR

Nel sistema classful, i router deducono la lunghezza del prefisso a seconda del valore assunto dai primi bit del primo byte: non occorre la netmask per ciascuna entry della tabella di routing. Nel CIDR invece è fondamentale.

I problemi principali delle classi sono:

- Le reti di classe A e B sono troppo grandi
- Le reti di classe B sono troppe poche
- Le reti di classe C sono tante ma spesso troppo piccole

Eliminando completamente la distinzione tra reti di classe A, B e C, CIDR risolve il problema.

![Organizzazione di una rete con CIDR](../images/network-Untitled%204.png)

Organizzazione di una rete con CIDR

![Organizzazione di una rete con Subnet in CIDR](../images/network-Untitled%205.png)

Organizzazione di una rete con Subnet in CIDR

![Organizzazione di una rete con CIDR e VLSM](../images/network-Untitled%206.png)

Organizzazione di una rete con CIDR e VLSM

### Gestione degli indirizzi

Gli indirizzi del CDIR vengono destiti dalla *Internet Assigned Numbers Authority* (**IANA**), un dipartimento dell'*Internet Corporation for Assigned Names and Numbers* (**ICANN**), che coordina e pianifica l'assegnamento di indirizzi IP a livello mondiale, sia per IPv4 che per IPv6.

IANA assegna blocchi di indirizzi a cinque *Regional Internet Registries* (**RIRs**), tipicamente nello spazio di indirizzi con prefisso di dimensione `/8`.

| Nome                                                   | Acronimo | Regioni coperte                                |
| ------------------------------------------------------ | -------- | ---------------------------------------------- |
| African Network Information Centre                     | AfriNIC  | Africa                                         |
| American Registry for Internet Numbers                 | ARIN     | Stati Uniti, Canada, Caraibi e Antartide       |
| Asia-Pacific Network Information Centre                | APNIC    | Asia, Australia, Nuova Zelanda e dintorni      |
| Latin America and Caribbean Network Information Centre | LACNIC   | America Latina e Caraibi                       |
| Réseaux IP Européens Network Coordination Centre       | RIPE NCC | Europa, Russia, Medio Oriente ed Asia Centrale |

In questo momento, tutti gli indirizzi IP sono esauriti, infatti IANA ha assegnato tutti gli indirizzi ai RIR nel 2011 e quasi tutti i RIR hanno terminato gli indirizzi disponibili. L'unico modo di assegnare nuovi indirizzi è usare IPv6.

---

## Inoltro IP

### IP Network

Una rete IP, identificata da un NET_ID, è un **insieme di host direttamente interconnessi**.

Nella maggior parte dei casi, la IP NET coincide con una rete di livello due, ad esempio con una **LAN Ethernet**. Le schede Ethernet degli host sono stazioni della LAN e sono identificate dall'**indirizzo MAC**.

Esiste almeno un router con un'interfaccia sulla IP NET per interconnettere gli host della rete ad host appartenenti ad altre IP NET.

### Inoltro dei pacchetti

L'IP è una tecnica di internetworking, perciò nell'inoltro dei pacchetti tra router e host, IP si serve della capacità di inoltro delle varie reti locali tra loro interconnesse.

La trasmissione di pacchetti nelle reti locali attraversate avviene tramite un incapsulamento in *trame* di livello 2 e si basa apunto sugli indirizzi di livello 2, ossia gli **Indirizzi MAC**, dei dispositivi.

Si hanno due tipi di inoltro:

- **Inoltro diretto**: quando la destinazione è nella stessa rete IP
    
    Ipotizziamo di avere due entità, A e B.
    
    1. L'entità IP di B deve spedire un pacchetto all'indirizzo IP di A.
    2. B conosce l'indirizzo IP di B della propria interfaccia e dal confronto con l'IP di A capisce che si trova nella stessa rete.
    3. B consulta una tabella di corrispondenza tra indirizzi IP e MAC **per reperire l'indirizzo MAC di A
    4. L'entità IP di B passa il pacchetto al livello inferiore, che crea una *trama* con destinazione indirizzo MAC di A
    
    ![Inoltro diretto di un pacchetto](../images/network-Untitled%207.png)
    
    Inoltro diretto di un pacchetto
    
- **Inoltro indiretto**: quando la destinazione non è nella stessa rete IP
    
    Ipotizziamo di avere due entità, A e B.
    
    1. L'entità IP di B deve spedire un pacchetto all'indirizzo IP di D `131.17.23.4`, al di fuori della propria rete
    2. B conosce l'indirizzo IP della propria interfaccia e dal confronto con l'IP di D capisce che D non si trova nella stessa rete
    3. B deve quindi inoltrare il pacchetto ad un router designato
    4. B recupera l'indirizzo MAC del router nella tabella di corrispondenza e passa il pacchetto al livello inferiore
    5. Il pacchetto viene costriuto e spedito sull'interfaccia
    
    ![Inoltro indiretto di un pacchetto](../images/network-Untitled2.png)
    
    Inoltro indiretto di un pacchetto
    

### Dual Homing

Anche un host può avere più interfacce di rete, ed ogni interfaccia deve appartenere ad IP NET diverse. Non è possibile assegnare due interfacce dello stesso apparato alla stessa rete IP.

### Inoltro nei router

I router sono dispositivi di internetworking con diverse interfacce di uscita.

Anche i router seguono le tecniche di inoltro diretto ed indiretto, ma:

- **Inoltro diretto**: hanno tipicamente più di un'interfaccia dove poter effettuare l'inoltro diretto, poiché sono connessi a più reti
- **Inoltro indiretto**: su basa sulle tabelle di routing, dov'è definita l'informazione di inoltro

L'inoltro fino alla destinazione fra router e router posti tra reti IP (*next-hop routing*).

I router inoltrano pacchetti solo sulla base della porzione NET_ID dell'indirizzo IP di destinazione (*destination based*).

Tutti gli host connessi alla rete sono espressi nella tabella di inoltro del router come un'unica entry, che esprime l'intera rete.

### Tabelle di routing con le Netmask

![Esempio di tabella di routing](../images/network-Untitled%208.png)

Esempio di tabella di routing

Nelle tabelle di routing è necessario specificare il prefisso di rete per esteso, tramite le netmask, per ciascuna riga della tabella.

I protocolli di routing devono trasportare l'informazione sul prefisso di rete completo in ciascun *annuncio di rete* (*route advertisement*). In passato, non tutti i protocolli di routing supportavano lo scambio di netmask.

Per inoltrare un pacchetto, anche nei router occorre prima capire se il destinatario appartiene alla rete (o sottorete) di una delle sue interfacce. Per effettuare questa verifica, si confrontano due risultati:

1. Indirizzo dell'interfaccia `AND` netmask dell'interfaccia
2. Indirizzo di destinazione `AND` netmask dell'interfaccia

Se i due risultati coincidono, allora la sottorete è la stessa e si procede all'inoltro diretto.

Se i confronti con tutte le interface sono negativi, occorre procedere con un inoltro indiretto, perciò occorre analizzare la tabella di routing. Il confronto riga per riga si effettua allo stesso modo usando la netmask relativa:

1. Indirizzo di rete della riga `AND` netmask della riga
2. Indirizzo di destinazione `AND` netmask della riga

Se il confronto dà esito positivo per più righe della tabella, viene selezionata la rabella con la netmask che ha il maggior numero di bit 1 (*longest prefix match*), perché indica la rete più piccola e perciò l'informazione di routing è la più precisa.

![Matching su una tabella di routing](../images/network-Untitled3.png)

Matching su una tabella di routing

Esiste poi un **default gateway**, che è un indirizzo IP `0.0.0.0` con netmask di lunghezza 0, che conferma sempre il riscontro durante il confronto tra indirizzi IP per l'inoltro. Nel caso non ci siano riscontri nel processo di consultazione della routing table, il pacchetto viene inviato di default a questo indirizzo.

Esistono però router che non hanno un default gateway: quelli della backbone. Essi non hanno un indirizzo di default e quindi se incontrano un pacchetto che non ha indirizzo di destinazione nella routing table, lo scartano direttamente.

### IP Addressing con Supernetting

Con la crescita di Internet, anche il numero di reti è aumentato, e con esso anche la dimensione delle tabelle di routing.

Per diminuire il tempo di riscontro nelle routing table, è stato introdotto il **supernetting**, una tecnica di riduzione dei record nella tabella, che funziona creando un unico record per reti che hanno la prima parte dell'indirizzo uguale. In questo caso, una supernet ha la forma `213.2.96.0/22`, dove `/22` indica la lunghezza della supernet mask, che è quella che agglomera le reti simili.

Non sempre è semplice creare supernet però. In alcuni casi, può succedere che ci siano molti meno bit in comune tra gli indirizzi, perciò la supernet spazia per un numero molto alto di indirizzi.

Il principio per cui si aggregano varie reti simili si chiama *route aggregation*.

### Exception Routing

L'*exception routing* si usa per distinguere pacchetti che passano sulla stessa subnet (o supernet) ma che vogliono essere indirizzati verso un router specifico o attraverso una porta del router particolare.

Per fare ciò, è indispensabile il *longest prefix match*.

---

## Network Address Translation

Le reti private (*Intranet*) si sono evolute grazie alla tecnologia IP e sono passate da grandi reti collegate a livello due (*bridge*) a reti collegate con router IP.

Una *intranet* non è altro che una rete privata che utilizza tecnologia di interconnessione IP, dotata degli stessi servizi di Internet, quali server HTTP, SMTP, eccetera.

L'evoluzione dei servizi e dei protocolli ha però reso le intranet strutturalmente differenti dalle reti pubbliche:

- Problemi di sicurezza
- Problemi di gestione indirizzi
- Problemi di distinzione tra servizi offerti ai soli utenti della intranet e servizi offerti anche dagli utenti di internet

Una rete privata ha normalmente una serie di servizi che sono accessibili dalla rete pubblica. I server per questi servizi devono avere un indirizzo pubblico, mentre gli host interni alla rete possono avere un indirizzo privato. I metodi più comunemente utilizzati per consentire il colloquio tra indirizzi pubblici e privati sono il Proxy ed il **NAT** (*Network Address Translation*).

I Proxy sono *application gateway*: qualunque richiesta viene inviata al proxy, che la inoltra con il proprio IP address pubblico. Occorre però avere un proxy per ogni applicazione.

Il NAT invece funziona a livello di rete, quindi basta averne uno. In linea di principio, un'organizzazione a cui sono assegnati $N$ indirizi IP, non necessita di $N$ indirizzi pubblici per accedere contemporaneamente alla rete. La maggior parte del traffico, infatti, viene scambiato internamente. Possono essere sufficienti quindi $k$ indirizzi pubblici tali che $k \ll N$.

Con la **NAT Table**, ogni indirizzo privato viene mappato 1:1 con un indirizzo pubblico. Non è una soluzione scalabile, poiché più dispositivi vogliono connettersi, più IP pubblici servono.

Una soluzione più efficiente è il **NAPT** (*Network Access Port Translation*), che traduce soltanto le porte, potendo così utilizzare anche solo un indirizzo IP pubblico.

Si può ulteriormente aumentare la flessibilità del NAPT associando alla coppia IP-Porta anche la destinazione a cui devono essere consegnati i pacchetti.

Una limitazione del NAPT è che non posso avere più server con le stesse porte, poiché andrebbero in conflitto nella traduzione. Esistono anche dei problemi per le applicazioni peer-to-peer, ma anche modi per aggirarli, quali lo *Universal Plug and Play*.

---

## IP Dataplane

### Servizio di comunicazione offerto da IP

Le UI del protocollo IP sono chiamate **datagrammi IP** o **pacchetti IP**.

Il protocollo IP è *Connectionless* ed utilizza la commutazione di pacchetto datagram. Due pacchetti destinati allo stesso host sono trattati in maniera indipendente.

Il protocollo IP non è affidabile. Usa una consegna *best-effort* dei datagrammi e lascia ai livelli superiori il controllo d'errore.

Altre funzioni svolte da IP sono:

- Indirizzamento: uso di indirizzi IP universalmente riconosciuti
- Rivelazione di errori svolta sull'header del datagram IP
    - Segnalazione di errori offerta tramite altri protocolli appositi, come l'ICMP
- Garanzia sul *max lifetime*: il datagram IP viene elminiato se non consegnato entro un certo *time-to-live*
- Frammentazione e riassemblaggio: frammenta e riassembla i pacchetti se la tecnologia di rete locale a livello 2 lo richiede. IP è pensato per interconnettere reti eterogenee, quindi deve adattarsi a molteplici tecnologie di livello inferiore.

### Formato del datagramma IP

![](../images/network-Untitled%209.png)

| Campo                         | Dimensione (bit) | Descrizione                                                                                                                          |
| ----------------------------- | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| IP Source/Destination Address | 32               | Indirizzi IP di sorgente e destinazione                                                                                              |
| Ver                           | 4                | Indica la versione del protocollo. Se non è compatibile con il router a cui viene recapitato, il datagramma potrebbe essere scartato | 
| HLEN                          | 4                | Indica la lunghezza dell'header del pacchettto in parole da 32 bit.                                                                  |
⁍ |
| Total length | 16 | Lunghezza totale del pacchetto in byte |
| TOS (Type of Service) | 8 | Ha subito vari cambiamenti. Vi sono definiti dei codici che indicano delle classifiche di priorità ai router. È ora diviso in DSCP e ECN (Differentiated Services Code Point e Explicit Congestion Notification) |
| TTL (Time To Live) | 8 | Contatore che indica la massima vita del programma. Viene decrementato di 1 ad ogni hop, solo in uscita, quando si effettua un inoltro. Il massimo TTL è ⁍. |
| Protocol | 8 | È un codice che indica il protocollo di livello superiore. Più protocolli di livello superiore possono usare IP.
Valori comuni:
1 - ICMP
2 - IGMP
6 - TCP
17 - UDP
89 - OSPF |
| Header Checksum | 16 | Protezione sull'header |
| Options |  | I campi opzionali possono allungare l'header fino ad un massimo di 60 byte. In origine erano pensate per testing e debugging, ora sono raramente usate |
| Padding |  | Usato per ottenere un header con lunghezza multiplo di 32 bit |

### Frammentazione e riassemblaggio

I pacchetti IP possono dover essere frammentati a causa della dimensione della MTU (*Maximum Transmission Unit*) del livello 2. Poiché reti diverse possono avere MTU diversi, IP può frammentare il suo datagramma in più datagrammi di minor dimensione.

Il riassemblaggio del pacchetto sarà effettuato dal livello di rete, ma solo arrivato a destinazione.

| Rete | MTU (Byte) |
| --- | --- |
| Massima dimensione | 65535 |
| Default | 576 |
| FDDI | 4352 |
| Ethernet | 1500 |
| PPPoE | 1492 |
| PPP (low delay) | 296 |

| Campo | Dimensione (bit) | Descrizione |
| --- | --- | --- |
| Identification | 16 | È un campo che identifica tutti i frammenti di uno stesso pacchetto in modo univoco, ma è usato anche in pacchetti non frammentati |
| Fragment Offset | 13 | I byte del payload del pacchetto originale sono numerati da 0 al valore complessivo. Questo campo riporta l'offset del primo byte trasportato nel frammento rispetto al riferimento 0 in parole da 8 byte |
| Flags | 3 | M: More fragments, indica se il pacchetto corrente è seguito da altri frammenti. 0 indica che è l'ultimo frammento, 1 indica che devono arrivare altri frammenti.
D: Do not fragment, viene impostato a 1 quando non si vuole che il pacchetto sia frammentato. I router che pensano sia necessario frammentare il pacchetto lo scarteranno, inviando un messaggio di errore. |

---

## Protocolli di controllo

### Address Resolution Protocol

Illustrando le tecniche di inoltro, abbiamo ipotizzato la presenza di una tabella di corrispondenza tra indirizzi IP ed indirizzi fisici. Queste tabelle vengono create dinamicamente da ciascun host mediante il **protocollo ARP**.

Per recuperare l'indirizzo MAC di un destinatario, il mittente invia un messaggio broadcast chiedendo a quale dispositivo sia associato l'indirizzo IP del destinatario.

L'ARP-reply, contenente l'indirizzo MAC del destinatario, viene inviata soltanto al dispositivo mittente.

Nonostante ARP sia un protocollo di livello 3, viene incapsulato direttamente in una trama di livello 2.

ARP può essere utilizzato da:

- Host che fanno inoltro diretto
- Host che fanno inoltro indiretto, quando inviano il pacchetto ad un router
- Router che fanno inoltro diretto verso altri router
- Router che fanno inoltro diretto verso altri host

### Reverse Address Resolution Protocol

Protocollo ormai poco utilizzato. Viene utilizzato da host che non conoscono il proprio indirizzo IP.

Come per ARP, il client invia una richiesta RARP in broadcast chiedendo del proprio indirizzo IP. Il server RARP risponde all'host fornendogli un indirizzo IP.

RARP è incapsulato in trame di livello 2 come ARP.

È sostituito dal maggiormente utilizzato DHCP.

### Internet Control Message Protocol

È un protocollo per lo scambio di messaggi di servizio tra host e router, usato per le informazioni sugli errori e fasi di attreaversamento della rete. È un protocollo che si affianca all'IP.

I messaggi vengono incapsulati e trasportati da IP, nel payload del pacchetto di livello 3.

| Nome              | Dimensione (bit) | Descrizione                                                         |
| ----------------- | ---------------- | ------------------------------------------------------------------- |
| Type              | 8                | Include un numero che specifica il tipo di messaggio ICMP trasmesso |
| Code              | 8                | Esprime un sottotipo che dipende dal campo type                     |
| Checksum          | 16               | Analogo agli altri campi checksum già visti                         |
| Resto dell'header | 32               | Usato in maniera differente a seconda del tipo di messaggio         |
| Sezione dati      |                  | Di lunghezza variabile (può anche rimanere inutilizzato)            |

Esistono generalmente due tipi di messaggi:

1. Error reporting: riportano gli errori di trasmissione
2. Diagnostica: controllo di raggiungibilità, richiesta netmask…

#### Messaggi di *error reporting*

Il protocollo ICMP non corregge errori, si limita soltanto a segnalarli. L'evento di errore è notificato alla sorgente del pacchetto IP che ha generato l'errore.

I messaggi ICMP di errore contengono nel payload l'header del pacchetto IP che li ha generati ed i suoi primi 8 Byte di dati, per aiutare la sorgente ad identificare il punto in cui è avvenuto l'errore.

[Eventi di errore](https://www.notion.so/777f015e8e0448d9aee4760258ef33e0)

| Nome                 | Type | Descrizione                                                                                                                                                                                                                                                                                                                                        |
| -------------------- | ---- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Echo-request         | 8    | Usato per verificare la raggiungibilità e lo stato di un host o router. Generalmente chiamato ping. Il campo identifier viene scelto dal mittente e nella risposta viene ripetuto lo stesso valore. Più richieste consecutive aumentano il campo sequence number. Una sequenza arbitraria può essere posta nel payload del messaggio dal mittente. |
| Echo-reply           | 0    | Risposta ad un messaggio Echo-request.                                                                                                                                                                                                                                                                                                             |
| Address mask request | 17   | Usato per conoscere la netmask di un host o router. Il campo address mask viene riempito dal destinatario.                                                                                                                                                                                                                                         |
| Address mask reply   | 18   | Risposta ad un messaggio Address mask request.                                                                                                                                                                                                                                                                                                     |
| Timestamp Request    | 13   |                                                                                                                                                                                                                                                                                                                                                    |
| Timestamp Reply      | 14   |                                                                                                                                                                                                                                                                                                                                                    |
| Router Solicitation  | 10   |                                                                                                                                                                                                                                                                                                                                                    |
| Router Advertisement | 9    |                                                                                                                                                                                                                                                                                                                                                    |

#### Traceroute

Il traceroute usa messaggi di echo-request verso la destinazione in modo ricorsivo.

Il primo messaggio di ping avrà un TTL pari a 1. Alla scadenza del TTL viene inviato dal primo router un messaggio ICMP di tipo `time-exceeded`. In questo modo, il mittente riceve l'indirizzo IP del primo router nella rotta verso la destinazione.

Man mano, il mittente aggiunge un'unità al TTL di nuovi pacchetti, per trovare tutti i router della rotta verso la destinazione, fino a quando non viene ricevuta una risposta al pacchetto di echo-reply, ossia quando si arriva alla destinazione.

A volte, il traceroute si implementa anche attraverso UDP, inviando segmenti UDP allo stesso modo su una porta mai utilizzata del protocollo. Si capisce l'IP di destinazione quando viene ricevuto l'errore di tipo `port-unreachable`.

### Dynamic Host Configuration Protocol

Le procedure statiche di assegnamento degli indirizzi IP sono poco flessibili. Può essere comodo non configurare i singoli host con indirizzo IP, ma usare un server per memorizzare tutte le configurazioni correnti.

In molti casi, non è necessario avere un'associazoine stabile tra i due indirizzi, ma si può usare un'**associazione dinamica**. L'associazione dinamica è temporanea e dipende da un timeout. Nel caso non ci fossero più indirizzi IP disponibili, la richiesta viene rifiutata dal server DHCP.

Quando un client non sa ancora il proprio indirizzo IP, invia con un broadcast limitato un messaggio `DHCPDISCOVER` contenente il proprio indirizzo fisico. Il server poi risponde con un messaggio `DHCPOFFER`, contenente l'IP disponibile che il server potrebbe assegnare all'host, insieme ad alcuni parametri della connessione. Il client può accettare l'offerta del server inviando un pacchetto `DHCPREQUEST`, contenente l'identificativo del server. Il server, allora, crea l'associazione con l'indirizzo IP e invia un pacchetto `DHCPACK` al client.

Se il client invia un pacchetto di tipo `DHCPRELEASE` o se scade il timeout, il server fa tornare disponibile per nuove associazioni l'IP precedentemente assegnato al client.

I messaggi DHCP sono incapsulati in un segmento UDP. DHCP è assimilabile ad un protocollo applicativo. Le porte di default per client e server DHCP sono 68 (Client) e 67 (Server).

È anche possibile avere più di un server DHCP **in una rete sola. Si avrà allora un server principale ed uno o più server *di riserva*.

Visto che il DHCP è un protocollo assimilabile ad uno di livello 5, non è necessario avere un server per ogni rete fisica. È comunque possibile creare server DHCP *relay*, che fungono da ripetitori.

---

## Algoritmi di routing

Gi algoritmi di routing (o di instradamento) definiscono i criteri di scelta del cammino nella rete per i pacchetti che viaggiano da sorgente a destinazione. Servono a costruire le tabelle di routing, consultate dai router per effettuare l'inoltro dei pacchetti. In alcuni casi, l'instradamento può essere svolto anche senza ricorrere a tabelle di routing.

Il tipo di rete (datagram o circuito virtuale) determina il criterio da adottare nella scelta dei cammini e quindi l'algoritmo di routing opportuno.

Esiste una differenza fondamentale tra protocollo ed algoritmo:

- **Protocollo**: scambio fra i router delle informazioni di raggiungibilità quali topologia della rete, informazioni sul traffico...
- **Algoritmo**: costruzione delle tabelle di routing e scelta del percorso migliore sulla base delle informazioni scambiate

Formalmente, il protocollo è solo la parte che descrive lo scambio di messaggi tra i router, ma in realtà questo scambio è strettamente legato al modo in cui sono calcolate le tabelle di routing.

Negli algoritmi di routing vengono usati i **grafi**, in cui sono rappresentati solo router e link, nessuna rete.

I principali requisiti per un algoritmo di instradamento sono:

- Semplicità
- Robustezza
- Stabilità
- Ottimalità

Esistono tre tipi di algoritmi, a seconda dell'origine del calcolo:

- Algoritmi **centralizzati**: un unico centro di controllo prende tutte le decisioni
- Algoritmi **distribuiti**: tutti i nodi cooperano per determinare il migliore instradamento in ogni nodo
- Algoritmi **isolati**: ciascun nodo prende le proprie decisioni in modo autonomo, eventualmente anche in base ad informazioni richieste ad altri nodi

![Tassonomia degli algoritmi di instradamento](../images/network-Untitled%2010.png)

Tassonomia degli algoritmi di instradamento

### Algoritmi di instradamento con tabella

Questi algoritmi sono basati su instradamento a distanza minima (o costo minimo).

Richiede la definizione di una **metrica di costo**, quale:

- Numero di *hop*
- Capacità dei link
- Ritardo dei link
- Numero medio di pacchetti in coda sul percorso

Le tabelle di instradamento indicano per ogni destinazione di rete il nodo successivo verso cui instradare il pacchetto.

| Nome            | Descrizione                                                                                                                                                 |
| --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Routing statico | È la forma più semplice di routing IP. Non richiede segnalazione tra router e le tabelle di routing sono compilate manualmente dall'amministratore di rete. | 
Nella fase di design, per ciascun router viene selezionata una rotta per ogni possibile sottorete. Nella fase di configurazione, le tabelle di routing sono configurate tramite opportune istruzioni.
È opportuno utilizzare questo algoritmo quando si è nella periferia della rete, quando si usano sistemi con bassa connettività o quando è necessario imporre delle rotte. |
| Routing dinamico (adattivo) | I protocolli e gli algoritmi di routing usati in Internet sono dinamici. Le entry delle tabelle di routing, in questo caso, cambiano nel tempo in base a guasti nei link, cambiamenti nella tipologia della rete, carico di rete e congestione. |

### Routing a cammini minimi

![Esempio di grafo con pesi per ogni arco](../images/network-Untitled%2011.png)

Esempio di grafo con pesi per ogni arco

La politica di routing utilizzata sin dall'introduzione delle reti TCP/IP è basata sul calcolo dei cammini minimi.

Il calcolo viene effettuato sul **grafo** che rappresenta la rete. Ad ogni arco del grafo è associato un peso opportunamente scelto, la **metrica di costo**.

Esistono degli algoritmi di calcolo dei MST (*Minimum Spanning Tree*) che possono essere eseguiti in modo distribuito dai router.

### Cenni sui grafi

Un **digrafo** (o **grafo diretto**) $G(N, A)$ ha le seguenti proprietà:

- $N$ insieme dei nodi
- $A = \{(i,j), i,j \in \mathbb{N}\}$ insieme degli archi, che sono coppie ordinati di nodi

Se i link sono bidirezionali, si parla di **grafo non diretto**.

<aside>
📌 Un **percorso** è un insieme di nodi $\{n_1, ...n_i\}$ con $(n_i, n_{i+1})\in A$.

</aside>

<aside>
📌 Si definisce **cammino** un percorso senza nodi ripetuti.

</aside>

<aside>
📌 Un **ciclo** è un percorso tale che $n_1 = n_i$.

</aside>

<aside>
📌 Si definisce **digrafo connesso** un grafo in cui per ogni coppia $(i, j)$ esiste almeno un cammino da $i$ a $j$.

</aside>

<aside>
📌 Se ad ogni arco $(i, j)$ è associato un **peso $d_{ij}$**, il grafo si dice **pesato**.

</aside>

<aside>
📌 Si definisce **costo** associato ad un cammino la somma di tutti i pesi dei lati associati a quel cammino.

</aside>

### Internet Routing Policy

L'obiettivo degli algoritmi e protocolli di routing è quello di compilare le tabelle di routing che consentono di svolgere inoltro indiretto.

L'inoltro indiretto nei router avviene sulla base dell'indirizzo di destinazione, *hop-by-hop*. Quindi:

1. I pacchetti diretti alla stessa destinazione $D$ in arrivo su un router $R$ seguono lo stesso percorso da $R$ a $D$, indipendentemente dal collegamento di ingresso ad $R$.
2. L'algoritmo di routing deve permettere al router di ottenere il next-hop verso la destinazione $D$.

Ciò porta a degli algoritmi di routing con cui si ottiene, per ogni possibile destinazione $D$, l'insieme dei percorsi da ogni sorgente a $D$, ovvero l'**albero dei cammini minimi** (MST, *Minimum Spanning Tree*).

Lo stesso algoritmo si può applicare considerando come radice dell'albero il nodo sorgente $S$, ed in questo caso si calcolano i cammini minimi verso tutte le possibili destinazioni.

### Problema del cammino minimo

Il problema del cammino minimo è di complessità polinomiale. Al crescere del numero di nodi $N$, il numero di operazioni necessarie per ottenere i cammini minimi cresce cone un polinomio in $N$.

<aside>
❇️ Se il nodo $k$ è attraversato dal cammino a costo minimo $(i, j)$, il sottocammino fino a $k$ è anch'esso a costo minimo.

</aside>

### Algoritmo Distance Vector

Questo algoritmo sfrutta l'instradamento a distanza minima: in ogni nodo, la tabella di routing specifica la minima distanza da ogni altro nodo e quale nodo deve essere utilizzato come next-hop. Ha sia una forma distribuita che una centralizzata:

- Forma **distribuita**: ciascun nodo riceve solo dai suoi vicini la stima delle distanze (vettore delle distanze), somma la sua distanza dal vicino e scopre la distanza minima verso ogni altro nodo.
- Forma **centralizzata**: si applica l'algoritmo di Bellman-Ford al grafo della rete per calcolare in modo centralizzato l'albero dei cammini minimi.

Applicare l'algoritmo Distance Vector in forma distribuita equivale ad applicare in ogni nodo l'algoritmo di Bellman-Ford.

#### Forma centralizzata: algoritmo di Bellman-Ford

Data la topologia della rete, costruisce l'albero dei cammini minimi dal nodo sorgente $S$. È un algoritmo iterativo che considera un numero di salti $h$ crescente.

Posti $d_{ij}$ il costo del link da $i$ a $j$ (con $d_{ij} = \infty$ se manca il link diretto) e $D_j^h$ il costo della via a minimo costo da $s$ a $j$ con un massimo di $h$ salti, gli *step* dell'algoritmo sono:

$$\begin{align}
\tag{1} h &= 1\\
D_j^h &= d_{sj}, \forall j \ne s
\end{align}$$

$$\begin{align}
\tag{2} h &= h + 1\\
D_j^h &= \min\big(D_i^{h-1}+d_{ij}, D_j^{h-1}\big), \forall j \ne s
\end{align}$$

$$\begin{align}
\tag{3}
&\text{If } D_j^h = D_j^{h-1}, \forall j \ne s\\
&\text{then } h_{\max} = h-1\\
&\text{else go to 2}
\end{align}$$

![Esempio di algoritmo di Bellman-Ford in azione](../images/network-Untitled%2012.png)

Esempio di algoritmo di Bellman-Ford in azione

#### Forma distribuita

In questo caso, il distance vector è inviato soltanto ai nodi adiacenti. Il distance vector è inviato periodicamente oppure in seguito ad un cambiamento nella topologia di rete. Ogni nodo esegue il calcolo del proprio distance vector se cade o nasce una linea attiva a cui è connesso.

Appena un nodo riceve un distance vector da un vicino:

1. Aggiunge a ciascuna destinazione inclusa nel distance vector il costo del link verso il vicino
2. Per ognuna di queste destinazioni:
    - Se la destinazione non era già inclusa nella tabella di routing, aggiunge la destinazione e la distanza
    - Se il next hop nella tabella di routing corrisponde al mittente del distance vector, sostituisce l'informazione della tabella di routing con quella nuova, anche se peggiorativa. In caso contrario, se la nuova distanza verso la destinazione è minore di quella attualmente scritta nella tabella di routing, aggiorna l'informazione della tabella di routing con i nuovi dati.

![Esempio di aggiornamento della tabella di routing in distance vector](../images/network-Schermata_2021-05-06_alle_09.46.57.png)

Esempio di aggiornamento della tabella di routing in distance vector

![Esempio di distance vector in una rete, parte 1](../images/network-Untitled%2013.png)

Esempio di distance vector in una rete, parte 1

![Esempio di distance vector in una rete, parte 2](../images/network-Untitled%2014.png)

Esempio di distance vector in una rete, parte 2

Nell'algoritmo distance vector, il cambiamento di topologia può portare sia buone che cattive notizie:

- Nel caso di un aggiunta di un nodo si ha una notizia positiva, che porta ad una propagazione veloce dell'aggiornamento
- Nel caso della rimozione di un nodo si ha una notizia negativa, che potrebbe dare luogo a problemi, quali il *count to infinity*

![Nuovo nodo raggiungibile](../images/network-Schermata_2021-05-06_alle_09.54.21.png)

Nuovo nodo raggiungibile

![Nodo che diventa irraggiungibile e fenomeno del *count to infinity*](../images/network-Schermata_2021-05-06_alle_09.55.58.png)

Nodo che diventa irraggiungibile e fenomeno del *count to infinity*

Si può rimediare al problema di *count to infinity* evitando che il nodo $A$ annunci a $D$ la raggiungibilità di $X$ nel suo distance vector, visto che $A$ manda i suoi pacchetti attraverso $D$ per raggiungere $X$.

<aside>
📌 Metodo **Split-Horizon**: il nodo $A$ non annuncia a $D$ con quale costo raggiunge $X$.

</aside>

Un altro tipo di Split Horizon è quello detto *with poisonous reverse* (o anche *poisoned reverse*): la stima della distanza viene inviata a tutti i vicini, ma viene posta a infinito se il collegamento è utilizzato per raggiungere la destinazione.

Nonostante sia un metodo molto utile, lo Split Horizon pone comunque dei problemi in alcuni casi. Infatti, potrebbe non funzionare con certe topologie di rete, poiché dipende dalla successione dei DV inviati e ricevuti.

---

### Link state

L'algoritmo di link state misura il costo dei collegamenti verso tutti i suoi vicini, secondo metriche di distanza o ritardo.

Link state funziona soltanto con costi di segno positivo.

La distanza è comunicata a tutti gli altri nodi con tecnica **flooding**.

Ogni nodo ha visibilità completa della rete (*topology discovery*) e può così costruire i percorsi a minima distanza verso ciascun altro nodo. Spesso, l'algoritmo usato per i cammini minimi è l'algoritmo di **Dijkstra**.

I costi dei link possono variare, perciò è necessario inviare nuovi link state all'occorrenza. Gli aggiornamenti vengono inviati in maniera periodica, anche senza cambiamenti, oppure a seguito di una modifica.

#### Algoritmo di Dijkstra

L'algoritmo di Dijkstra si applica al generico nodo sorgente.

Si definiscono:

- $s$ nodo sorgente
- $N$ nodi della rete
- $M$ insieme dei nodi del MST corrente
- $V(M)$ nodi *vicini* all'insieme $M$
- $d_{ij}$ costo della via diretta tra $i$ e $j$ ($d_{ij} = \infty$ in assenza di link)
- $D_j$ costo del cammino minimo tra $s$ e $j$
- $P_i$ nodo predecessore del nodo $j$
1. Inizializzazione dell'algoritmo:
    - $M = \{s\}$
    - $D_j = d_{sj}, \forall j \in N-\{s\}, D_s = 0$
    - $P_j = s, \forall j \in N-\{s\}$
2. $\text{Select } k \in V\{M\}\mid D_k = \min D_i,\  {i \in V\{M\}}$
    - $M = M\cup \{k\}, \text{connect } k \text{ to } P_k \text{ in MST}$
    - $\text{if } D_j > D_k + d_{kj} \text{ then } P_j = k, \forall j\in V(M),\\
    D_j = \min\{D_j, D_k + d_{kj}\}, \forall j \in V(M)$

I due algoritmi di Dijkstra e Bellman-Ford convergono alla stessa soluzione in condizioni statiche.

Il distance vector, con Bellman-Ford, ha una convergenza più lenta in condizioni dinamiche ed è un protocollo semplice da implementare, mentre link state, con Dijkstra, ha una velocità di convergenza molto più alta ma è più difficile da implementare.

---

## Instradamento in IP

Non possiamo pensare di applicare Distance Vector o Link State a tutta internet, perché non sono protocolli scalabili: Link State genera troppa informazione, mentre Distance Vector converge troppo lentamente.

Internet viene suddivisa in **Autonomous Systems** (**AS**), che sono porzioni di rete gestite da una stessa autorità.

Un router interno ad un AS si chiama **Interior Gateway**, mentre un router al bordo di un AS si chiama **Exterior Gateway**.

All'interno di ciascun AS il routing è indipendente dagli altri AS. Gli Interior Gateway si scambiano informazioni di routing *Intra-AS* usando un **Interior Gateway Protocol** (**IGP**), con cui si condividono le informazioni topologiche.

Il routing tra AS è gestito in modo differente: gli Exterior Gateway si scambiano informazioni di routing usando un **Exterior Gateway Protocol** (**EGP**), con cui si scambiano informazioni di raggiungibilità sintetiche.

Esistono fondamentalmente tre tipi di inoltro tra AS:

- **Diretto**: il NET ID degli host sorgente e destinazione coincidono, l’inoltro è effettuato mediante la rete di livello 2
- **Indiretto**: il NET ID degli host sorgente e destinazione sono diversi ma appartengono allo stesso Autonomous System, quindi il forwarding avviene mediante gli Interior Gateway attraverso IGP
- **Indiretto gerarchico**: sorgente e destinazione sono in due Autonomous System diversi, quindi il pacchetto viene instradato con IGP fino all’Exterior Gateway con IGP, poi viene inviato all’AS corretto mediante EGP ed infine consegnato all’host destinazione con IGP

## Protocolli di Routing

### Interior Gateway Protocols

In un AS possono essere configurati più IGP, che devono essere gestiti in modo da garantire la consistenza del routing. Generalmente però gli AS sono configurati con un singolo IGP.

Il **dominio di routing** (*Routing Domain*, **RD**) è una porzione di AS in cui è implementato un unico protocollo IGP.

Alcuni router appartengono a più RD ed implementano più protocolli IGP.

I router su più domini possono *ridistribuire* le informazioni di un dominio nell'altro e viceversa. La traduzione delle informazioni tra protocolli dipende dall'implementazione e dalle caratteristiche dei due protocolli A e B. I due protocolli possono anche essere un IGP ed un EGP.

[Protocolli di routing più usati](https://www.notion.so/fdcfec8c2133433daefdc5f735531b41)

#### Routing Information Protocol

Primo protocollo creato per il routing in Internet. Si basa su piccoli messaggi inviati tramite **segmenti UDP**, utilizzando la porta **520**.

Si basa sull’algoritmo di **Distance Vector**, in cui la metrica di costo è soltanto l’*hop count*, ossia il numero di salti tra sorgente e destinazione. Il massimo costo raggiungibile da un percorso in RIP è 15 hop, mentre per convenzione, **16 hop è il costo infinito**, che rappresenta una rete irraggiungibile. Le informazioni di aggiornamento DV vengono inviate circa ogni **30 secondi**.

I vantaggi del protocollo RIP sono la sua facile implementazione e la semplicità dei messaggi. Il contro di questo protocollo è il fatto che sia basato su Distance Vector, algoritmo con convergenza lenta e piuttosto complesso, in cui si possono verificare loop e count to infinity.

| Nome | Descrizione |
| --- | --- |
| Request | Inviate da un router appena connesso o con entry in scadenza nella tabella di routing. Con questo tipo di messaggio, si possono richiedere ai propri vicini entry specifiche o tutte le entry in loro possesso. |
| Response | Possono essere di due tipi:
1. Solicited: inviate in risposta ad una request (regular update)
2. Unsolicited: inviate periodicamente (triggered update) |

**Triggered Update**: ****Appena cambia il costo di una rotta, la nuova tabella di routing è inviata immediatamente, senza aspettare lo scadere del periodo di aggiornamento base di 30 secondi.

RIP è un protocollo limitato, a causa di diverse motivazioni:

- *Hop count* è una metrica di costo troppo semplice
- Converge lentamente
- Diffonde le informazioni lentamente a meno di richieste specifiche
- È limitato a reti di piccole dimensioni, dato che il massimo *hop count* è 15

La **versione 2** di RIP **supporta il CIDR**. Mentre RIPv1 usava le maschere di default a partire dalla classe IP, RIPv2 ha bisogno di specifiche netmask per annunciare i blocchi.

#### Open Shortest Path First

Algoritmo di routing basato sul **Link State**, che adotta il routing *shortest path* con l’algoritmo di **Dijkstra** e che consente ad ogni nodo di conoscere l’intera topologia del routing domain.

I router inviano **Link State Packet ****(**LSP**) a tutti gli altri nodi nel routing domain attraverso il *flooding* (inviati in broadcast a tutti i nodi della rete), periodicamente oppure a seguito di eventi di modifica dei costi dei link (*event update*). I pacchetti Link State contengono poche informazioni sui link adiacenti, non su tutte le destinazioni note, a differenza del RIP.

OSPF supporta qualsiasi metrica di costo, che viene decisa dall’amministratore di rete. Il costo di attraversamento di ciascun link o rete è visto indipendentemente da ciascuno dei router adiacenti al link o alla rete. Possono esserci quindi anche costi diversi ed asimmetrici sui link. Questo è utile soprattutto per funzioni di *load balancing*.

Il *load balancing* su OSPF è dinamico ed è ottenuto specificando rotte multiple, da utilizzare quando più rotte hanno lo stesso costo. L’aspetto negativo è che possono nascere fuori sequenza a causa di invii di pacchetti su rotte equivalenti ma diverse.

OSPF supporta il routing gerarchico, tramite suddivisione in aree e ridistribuzione dell’informazione di routing. L’*autonomous system* viene diviso in:

- **Internal routers**: tutte le interfacce che appartengono alla stessa area
- **Area border routers**: hanno interfacce su aree diverse
- **Autonomous system boundary routers**: connessi ad almeno un router all’esterno dell’autonomous system

La suddivisione in aree consente di semplificare le istruzioni di routing. Si crea un’ulteriore gerarchia all’interno degli autonomouos system, in cui gli area border routers inviano all’interno delle proprie aree un’informazione di routing dettagliata, mentre inviano all’esterno dell’area un’informazione sintetica.

### Exterior Gateway Protocols

#### Border Gateway Protocol

Consente di effettuare routing tra Autonomous System differenti. È un protocollo EGP. La versione più usata è la versione 4.

L’algoritmo usato da BGP è il **Path Vector**: le informazioni propagate contengono rotte costituite da catene di Autonomous Systems.

I gestori di autonomous system decidono, grazie a BGP, il routing in base alle proprie **politiche**, conoscendo i percorsi usati per raggiungere altri autonomous system.

BGP è indipendente dai protocolli di tipo IGP adottati all’interno degli autonomous systems.

Esistono due tipologie di protocolli BGP:

- **eBGP** (*external* BGP): usato da diversi autonomous system border router per scambiare tra loro informazioni di routing.
- **iBGP** (*internal* BGP): usato da un autonomous system border router per propagare l’informazione di routing all’interno dell’autonomous system stesso.

L’algoritmo Path Vector è simile a Distance Vector, ma nelle informazioni scambiate tra i nodi non è indicata una *distanza dalla destinazione*, bensì l’intero percorso verso la destinazione, ossia la sequenza degli autonomous system da attraversare. Agli autonomous system è assegnato un **Autonomous System Number** (**ASN**) globale da IANA, come per gli indirizzi IP.

I messaggi di Path Vector che si scambiano due router vicini non contengono solo il percorso, ma anche una sequenza di attributi. Tra gli attributi obbligatori, troviamo:

- `ORIGIN`: protocollo IGP da cui proviene l’informazione
- `AS_PATH`: sequenza di autonomous system attraversati
- `NEXT_HOP`: prossimo router

Ogni router BGP invia il proprio Path Vector ai router BGP vicini (*peers*) attraverso **connessioni TCP**, sulla porta **179**.

| Nome | Descrizione |
| --- | --- |
| Open | Apre la connessione TCP e gestisce l’autenticazione reciproca del router. |
| Update | Annuncia una nuova rotta o ne annulla una vecchia. |
| Keep Alive | Mantiene attiva la connessione in caso di assenza di UPDATE (usato anche come ACK ai messaggi OPEN). |
| Notification | Notifica errori in messaggi precedenti (usato anche per chiudere la connessione). |

#### Policy Based Routing

Un router BGP che riceve un *path vector* da un *peer* può decidere di effettuare o meno quanto segue:

- Aggiungere alla propria tabella di routing la destinazione specificata dal path vector
- Inoltrare il path vector ai suoi vicini

La scelta viene fatta a seconda della politica di routing implementata localmente.

---

## Software Defined Networking

Il paradigma tradizionale del networking prevede hardware che si specializza nell'inoltro di pacchetti e protocolli e software di controllo, per organizzare le trasmissioni. La logica di controllo è integrata nei dispositivi di networking, quali le *Line Card*. Ogni protocollo implica l'installazione di un nuovo apparato hardware che lo supporti e tutta la manutenzione che ne deriva.

Il **Software Defined Networking** (**SDN**) vuole separare la parte hardware dalla parte software, per realizzare infrastrutture più flessibili che, invece di essere integrate *verticalmente*, lo sono *orizzontalmente*, lasciando anche più scelta agli amministratori di rete su quali software e protocolli usare.

Quando il software di controllo viene separato dall'hardware per l'inoltro, possono nascere vari tipi di network:

- **Distribuito**: quando la parte di controllo e la parte di hardware per l'inoltro sono in rapporto $1:1$
- **Centralizzato**: parte di controllo e parte hardware sono in rapporto $1:n$
- **In-Between**: parte di controllo e parte hardware sono in rapporto $m:n$

Il sistema operativo degli apparati è stato migrato ed unificato in un *NetOS* **Centralizzato**, così come le *NetApp*, ossia le implementazioni delle varie funzioni dei protocolli a livello software. L'hardware che viene ora usato è *commodity hardware*, che non è più venduto dalle compagnie che integravano l'intera stack IP (da hardware a software) in hardware *proprietario*. Ora l'hardware può essere comprato anche da aziende che si specializzano soltanto in quel settore.

Nasce un nuovo apparato di rete: il **controller**, attraverso cui si possono controllare tutte le interfacce hardware: gli **Switch SDN**. Il piano di controllo della rete viene quindi lasciato separato e centralizzato. La comunicazione tra Controller e Switch avviene grazie alle **Southbound Interface**, mentre la comunicazione tra Controller e NetApp avviene con la **Northbound Interface**.

Tutta la rete, alla fine di questo processo, assomiglia ad un grande computer, dove le NetApp possono essere assimilate a software applicativi, il Controller ad un sistema operativo e le interfacce di controllo a driver.

### Interfacce del controller

- **Northbound Interface**: basato su **Application Programming Interface** (**API**). L'astrazione della rete permette la semplice creazione ed il lancio di nuovi protocolli ed applicazioni, insieme ad una visualizzazione ed un controllo della rete più intuitivi.
- **Southbound Interface**: i controller e gli elementi del dataplane controllati da esso sono in luoghi differenti. Sono necessari dei **protocolli di comunicazione** per scambiare messaggi tra controller ed elementi del dataplane.

### Piano di controllo distribuito e centralizzato

Il vantaggio di aver messo in atto una centralizzazione della rete è che gli amministratori di rete hanno maggiore controllo su infrastrutture sempre più grandi. Possono infatti cambiare le policy di tutta la loro infrastruttura in modo centrale, senza agire su ogni singolo punto di scambio.

Il modello principale a cui si fa riferimento per il SDN è il **Modello IETF SDN**, trasformato nella raccomandazione **RFC 7426**.

| Termine | Descrizione |
| --- | --- |
| Application | Software che usa i servizi sottostanti per svolgere una funzione. È standalone, ossia non offre altre interfaccie ad altre applicazioni o servizi. |
| Service | Software che svolge una o più funzioni e fornisce una o più API ad applicazioni o ad altri servizi. Può essere combinato con altri servizi o chiamato per creare un nuovo servizio. |
| Network Services Abstraction Layer | L'intero network è rappresentato da un modello di rete unificato che include ed unisce tutte le viste astratte dei dispositivi di rete individuali. Fornisce queste astrazioni ad applicazioni e servizi. |
| Control Abstraction Layer | Fornisce l'accesso alla Southbound Interface dal lato di controllo (Control Plane). Possono esserci diversi layer di questo tipo. |
| Management Abstraction Layer | Fornisce l'accesso alla Southbound Interface dal lato di gestione (Management Plane). Possono esserci diversi layer di questo tipo. |
| Device and resource Abstraction Layer | Interfaccia attraverso cui l'apparato mostra al Controller uno o più data model, ossia la rappresentazione delle proprie funzionalità ed i parametri che descrivono lo stato dell'apparato in quel momento. Attraverso quest'interfaccia vengono anche rivecuti i messaggi di controllo dal Controller. Questa interfaccia comunica con il controller attraverso la Southbound Interface, divisa in Control Plane e Management Plane. |
| Forwarding Plane | Insieme di risorse che svolge operazioni sui dispositivi di rete sul dataplane. |
| Operational Plane | Insieme di risorse che controlla e gestisce l'operazione generale dei dispositivi di rete. È essenzialmente il sistema operativo del dispositivo. |

![Gerarchia nel modello IETF del Software Defined Networking](../images/network-Untitled%2015.png)

Gerarchia nel modello IETF del Software Defined Networking

Il Device and Resource Abstraction Layer è implementato in ogni dispositivo di rete da un **agente**, un software e spesso un sottosistema hardware che è necessario per eseguire il software sull'equipaggiamento controllato. È capace di recuperare il data model e tutti i parametri che devono essere esposti per il controller e può anche cambiare la configurazione del dispositivo di rete sulla base di comandi inviatigli dal Controller attraverso il **model builder**. Mantiene un canale di comunicazione con il Controller, controllando il trasporto dei messaggi su protocolli adatti della Southbound Interface. Gli agent possono essere proprietari o avere interfacce aperte. Si può dire che l'agente stesso espone un insieme di API, quindi lo switch stesso si dice *programmabile*.

Il Control Abstraction Layer (o Management Abstraction Layer) all'interno del controller si basa su un data model di ogni dispositivo (o tipo di dispositivo) capace di rappresentare:

- L'**identità** del dispositivo
- Le **funzionalità** disponibili nel dispositivo
- Tutti i **parametri** che rappresentano lo stato del dispositivo

I CAL ed i MAL possono essere integrati anche in un singolo data model.

Per ogni dispositivo, agent e protocollo dovrebbero essere scelti per supportare il data model del dispositivo sulla SBI.

La combinazione di CAL/MAL e manager di protocollo SB sulla parte Controller è anche nota come ***plug-in*** o ***device driver***.

Un controller può anche avere diversi CAL/MAL per supportare diverse interfacce verso diversi elementi del dataplane, a volte anche usando diversi protocolli SB.

### Network Abstraction

All'interno del controller, i data model dei diversi elementi di dataplane sono:

- Sfruttati dalle app interne per svolgere alcune funzioni di rete, tra cui *topology discovery*, *routing*...
- Combinate dal NSAL per generare un'unica **Network Abstraction** o **Network Abstracted Data-Model**.

Il Network Abstracted Data-Model è inviato alla NBI per le app esterne, al fine che queste possano svolgere altre funzioni di rete, quali connessione o lancio di servizi.

I data model dei diversi dispositivi di rete dovrebbero essere scelti appropriatamente al fine di connettersi tra loro e permettere l'integrazione all'interno del network data model.

Per scegliere il device data model corretto, bisogna pensare a cosa si sta cercando:

- **Specializzazione**: possibilità di controlare un grande numero di funzionalità del dispositivo
- **Generalizzazione**: semplicità di integrazione in un modello di rete comune

Un grande impegno nella ricerca e nello sviluppo industriale è al momento dedicato alla definizione di data model che assicurino l'interoperabilità di diversi dispositivi sotto lo stesso SDN Controller, dove *diversi* sta a significare:

- Multi-Vendor
- Multi-Layer
- Multi-Technology

### Northbound Interface

L'insieme di API esportate dipende dallo specifico controller, il che è un problema per gli sviluppatori. Lo stesso vale per il tipo di network astratto fornito dal Controller.

Il principio generale vuole che:

- Le NetApp non debbano gestire dettagli di distribuzione di stato della rete
- La raccolta dello stato, della disseminazione e della sincronizzazione dovrebbe essere una responsabilità del Controller

Esistono due casi generali:

1. Se le NetApp sono eseguite sulla stessa macchina su cui è eseguito il controller, la NBI è definita interamente su software
    - A differenza della SBI, questo non è uno standard accettato.
    - È più probabile che sia implementato su una base *ad-hoc* per app particolari
2. Se le NetApp sono eseguite su una macchina (o in un luogo) differente, è necessario un protocollo per lo scambio di messaggi
    - La soluzione più comune è la comunicazione basata su HTTP (**REST-based APIs**)

### Southbound Interface

Sulla SBI possono essere usati moltissimi protocolli.

#### OpenFlow e switch OpenFlow

L'hardware per l'inoltro consiste di:

- Una **Flow Table** che contiene entry di flusso, consistenti di regole ed azioni che fanno partire flussi attivi
- Un **OpenFlow channel** aperto su un Transport Layer Protocol (TLS) che comunica in modo sicuro con un controller nuove entry non ancora aggiunte alla Flow Table

Uno switch OpenFlow svolge classificazione, processing ed inoltro dei pacchetti. Ogni Flow Table dello switch ha un insieme di Flow Entry:

- Campi header e porte d'ingresso per classificare i pacchetti in entrata
- Contatori per raccogliere statistiche
- Un insieme di istruzioni o azioni da applicare ai pacchetti

L'insieme di campi che possono essere usati per la classificazione dei pacchetti spazia su diversi livelli di rete.

Ogni entry nella Flow Table definisce un flusso. I pacchetti sono classificati in base ad un valore di priorità. Non si può applicare la regola del *longest prefix match*.

L'entry `table-miss` gestisce pacchetti che non rientrano in nessun'altra entry della Flow Table.

Le **azioni** istruiscono lo switch OpenFlow su come gestire un pacchetto che rientra in un flow. Se non ci sono azioni nella entry, il pacchetto viene scartato. Altrimenti, le azioni presenti devono essere svolte nell'ordine in cui vengono specificate.

| Azione | Descrizione |
| --- | --- |
| Drop | Scarta il pacchetto |
| All | Invia il pacchetto a tutte le interfacce, tranne quella da cui arriva il pacchetto stesso |
| Controller | Incapsula il pacchetto e lo inoltra al controller |
| IN_PORT | Invia il pacchetto sulla porta di input |
| Flood | Invia il pacchetto con flooding sull'intero Minimum Spanning Tree, escludendo però l'interfaccia d'arrivo |
| Modify Field | Alcune azioni servono a modificare i campi dell'header |

![](../images/network-Untitled%2016.png)

![](../images/network-Untitled%2017.png)

![](../images/network-Untitled%2018.png)

![](../images/network-Untitled%2019.png)

![](../images/network-Untitled%2020.png)

![](../images/network-Untitled%2021.png)

## IETF NETCONF

Il **Network Configuration Protocol** (**NETCONF**), sviluppato nell'ultimo decennio, prenderà il posto di SNMP, un protocollo di Management Plane, ora usato primariamente per il monitoraggio della rete.

NETCONF usa un formato eXtensible Markup Language (**XML**) per passare dati e comandi verso e da dispositivi di rete.

Questo protocollo è particolarmente popolare tra i più grandi provider di servizi, poiché semplifica il controllo remoto di dispositivi eterogenei. Tutti i venditori sono stati spinti ad implementare NETCONF.

| Funzione | Descrizione |
| --- | --- |
| Sicurezza | NETCONF opera su un canale sicuro |
| Organizzazione | NETCONF separa dati di configurazione e dati operazionali |
| Annuncio delle capacità | Il primo scambio tra un server NETCONF sul dispositivo ed il client della management station è l'annuncio di tutti i modelli YANG (Yet Another Next Generation) che supporta. YANG fornisce un linguaggio formale per esprimere le capacità del dispositivo. |
| Operations | Le operazioni NETCONF sono Remote Procedure Calls (RPC): permettono al Controller SDN di istruire il dispositivo a compiere una specifica azione, passando un insieme di parametri alla RCP. Ciò permette al Controller di manipolare più facilmente il comportamento di inoltro del dispositivo. Inoltre, i cambiamenti di configurazione possono essere convalidati e riportati a stati precedenti. |

### IETF YANG Data Modeling Language

YANG è un acronimo che significa *Yet Another Next Generation*, ideato nel 2007 e realizzato nel 2010 (RFC 6020). Rimpiazza il precedente linguaggio di data modeling usato con SNMP (*Structure of Management Information*, SMI).

È progettato per scrivere data model per il protocollo NETCONF. Fornisce le seguenti funzionalità:

- È *human readable*, facile da imparare
- I data model hanno una configurazione gerarchica
- Grazie a meccanismi di aumento, è estensibile
- Supporta le definizioni di operazioni (RPC)
- Supporta la validazione della configurazione

YANG è soltanto un linguaggio. La vera definizione dei modelli YANG per i dispositivi viene attuata da:

- Venditori
- Organizzazioni per gli standard
- Trust di venditori

### REST

REST fu introdotta anni fa per l'accesso all'informazione attraverso un servizio web, ora adottato da Controller SDN per sfruttare HTTP ed HTTPS.

Le API basate su questa tecnologia si chiamano **interfacce RESTful** ed hanno le seguenti caratteristiche:

- **Semplicità**: usa i comandi HTTP `GET`, `PUT`, `POST`, e `DELETE` ed usa l'encoding URL per i riferimenti alle risorse sui dispositivi target
- **Flessibilità**: può accedere a configurazioni di componenti su un dispositivo usando risorse REST, rappresentate da URL separati
- **Sicurezza**: è molto semplice rendere sicure le comunicazioni grazie al protocollo HTTPS, che ha anche il vantaggio di penetrare firewall facilmente.

Uno dei problemi di REST è che manca di formalismo e di type-checking, a differenza di altri metodi.

### RESTCONF

Un correlato uso di REST si vede nel protocollo **RESTCONF**, implementazione di NETCONF/YANG che usa JSON o XML su HTTP invece di XML e RPC su SSH.

Solitamente, un'interfaccia RESTCONF è più semplice e può supportare un sottoinsieme di funzioni a seconda della versione NETCONF.

REST e RESTCONF sono usate più spesso con la NBI, ma possono anche essere usate come API per i dispositivi.

### gRPC

gRPC è un sistema RPC open source inizialmente sviluppato da Google nel 2015. Usa il protocollo HTTP/2 per il trasporto, quindi è più semplice e leggero dell'XML.

Fornisce funzionalità quali l'autenticazione, lo streaming bidirezionale, il controllo di flusso, la cancellazione ed i timeout.

È semplice implementare client e server gRPC con molti linguaggi (Java, C++, Python, Java Lite, Ruby, JavaScript...).

Sta avendo un enorme successo nell'implementare funzioni di monitoraggio in SDN.

### Controller OpenFlow

Basato su framework di sviluppo. L'architettura può essere semplice o complessa: i controller più semplici inviano comandi OpenFlow sulla NBI, quelli più complicati forniscono molte funzioni per supportare l'astrazione e SBI multiple.

### RYU

Presenta poche opzioni ed è una buona scelta per le piccole aziende e per la ricerca.

Poiché è programmato in Python, questo controller rende semplice lo sviluppo di applicazioni e moduli, ma la sua mancanza di grande modularità e la sua inabilità di eseguire applicazioni cross-platform limita l'ampio uso nelle applicazioni di mercato.

### Architettura OpenDaylight

![Struttura generale dell'architettura Open Daylight](../images/network-Untitled%2022.png)

Struttura generale dell'architettura Open Daylight

È il primo controller ad entrare nel dominio dell'Internet of Things e supporta un'ampia gamma di SBI ed il paradigma di controllo distribuito.

Viene a volte definito il controller dell'Internet del futuro.

L'architettura OpenDaylight è composta principalmente da tre strati:

- Plugin e protocolli southbound che formano il **Network Device Layer**
- La piattaforma del controller per l'adattamento dei servizi e per le funzioni di rete, che formano il **Coordination and Control Layer**
- Un'interfaccia northbound per applicazioni e servizi che forma l'**Application Layer**

![Struttura dell'architettura Open Daylight Helium](../images/network-Untitled%2023.png)

Struttura dell'architettura Open Daylight Helium

### Architettura ONOS

L'architettura ONOS è stata creata da ONF (in precedenza ONLAB, ora fusa con ONF).

![](../images/network-Untitled%2024.png)

---

## Virtual Private Networks

Una volta create delle Intranet, può sorgere la necessità di collegarle tra loro.

Uno dei metodi che sarebbe possibile applicare è l'uso di canali dedicati, ma questa tecnica ha solitamente un costo molto elevato.

Si può altrimenti affidarsi ad Internet per svolgere l'indirizzamento corretto, creando una **VPN** (*Virtual Private Network*). Questo metodo ha alcuni problemi, quali l'uso degli indirizzi IP privati, la sicurezza e le prestazioni della rete, ma possono essere risolti attraverso l'uso di **tunnel di collegamento**.

### IP Tunneling

![Funzionamento dell'IP Tunneling](../images/network-Untitled%2025.png)

Funzionamento dell'IP Tunneling

Il tunnel si costruisce *incapsulando* pacchetti IP in altri pacchetti IP. Il payload che viaggia nel segmento pubblico viene generalmente cifrato.

Gli indirizzi del pacchetto IP incapsulato possono anche essere IP privati, mentre gli indirizzi dell pacchetto trasportatore sono normalmente pubblici.

- Esempio
    
    ![Incapsulamento nell'IP Tunneling](../images/network-Untitled%2026.png)
    
    Incapsulamento nell'IP Tunneling
    
    ![Routing del pacchetto incapsulato tra intranet connesse da VPN](../images/network-Untitled%2027.png)
    
    Routing del pacchetto incapsulato tra intranet connesse da VPN
    

In realtà, i tunnel sono uno strumento più generale del caso di IP Tunneling appena descritto. Generalmente, un tunnel è costituito da:

- **Protocollo passeggero**: è il protocollo che viene trasportato all'interno del tunnel da un estremo all'altro
- **Protocollo trasportatore**: è il protocollo che trasporta il passeggero
- **Protocollo di incapsulamento**: è un protocollo supplementare che sta tra passeggero e trasportatore

Il protocollo di incapsulamento svolge principalmente funzioni di sicurezza, quali autenticazione, cifratura ed integrità dei dati, ma può anche svolgere funzioni di gestione del tunnel, come setup e teardown.

#### Protocolli passeggeri

I protocolli più usati come passeggeri in internet sono **IP** ed **Ethernet**:

- Nel caso di tunnel IP, il tunnel si comporta come un collegamento punto-punto tra router.

![Esempio di tunneling di livello 2](../images/network-Untitled%2028.png)

Esempio di tunneling di livello 2

- Nel caso di tunnel Ethernet, il tunnel si comporta come un collegamento tra due switch Ethernet e la rete viene unita sotto un unico dominio di broadcast.

#### Protocolli trasportatori

![Protocolli di trasporto usati come protocolli trasportatori](../images/network-Untitled%2029.png)

Protocolli di trasporto usati come protocolli trasportatori

Il protocollo trasportatore può essere IP, ma in alcuni casi anche un protocollo di trasporto, quali TCP o UDP.

#### Protocolli di incapsulamento

Il protocollo di incapsulamento fornisce principalmente servizi di sicurezza e gestione del tunnel. Alcuni dei principali sono:

- **IPSec**: IP Security Protocol
- **L2TP**: Layer 2 Tunneling Protocol
- **PPTP**: Point-to-Point Tunneling Protocol
- **GTP**: GPRS Tunneling Protocol

![Incapsulamento di un pacchetto in una VPN](../images/network-Untitled%2030.png)

Incapsulamento di un pacchetto in una VPN

### Tipi di VPN

- Site-to-Site
    
    ![](../images/network-Untitled%2031.png)
    
- Remote Access
    
    ![](../images/network-Untitled%2032.png)
    
- Tunneling GTP
    
    ![](../images/network-Untitled%2033.png)
    

### User-space VPN: OpenVPN

![Tunnel OpenVPN](../images/network-Untitled%2034.png)

Tunnel OpenVPN

OpenVPN è la soluzione più usata per le VPN Remote Access.

Usa TCP o UDP come protocollo di trasporto ed incapsula con SSL o TLS.

È nota come User-space VPN perché crea un'interfaccia virtuale collegando l'utente allo user-space delle applicazioni dove un'interfaccia di socket sicura trasporta le trame.

OpenVPN è anche la soluzione più utilizzata dai servizi VPN offerti da una serie di provider.

L'utilizzo di una VPN ha vari obiettivi: evitare il blocco di alcuni servizi in alcune aree geografiche, nascondere il proprio indirizzo IP...

### TOR

![](../images/network-Untitled%2035.png)

**TOR** (*The Onion Router*) è la soluzione più nota per la gestione distribuita ed anonima dell'accesso a servizi su internet ed al deep web.

Utilizza **Onion Routing** con tunnel innestati, cifrati ed anonimizzati.

---

## IPv6

**IPv6** è la nuova versione dell'Internet Protocol il cui processo di standardizzazione è iniziato negli anni '90.

Mantiene l'impostazione fondamentale di IPv4 ma cambia molti aspetti. La caratteristica principale è che **aumenta la lunghezza degli indirizzi** da 32 bit a 128 bit.

La maggiore lunghezza degli indirizzi IPv6 permette di passare dall'esaurimento degli indirizzi IPv4 ad avere $6.67\cdot 10^{23} \text{ indirizzi} /\text{m}^2$.

Le novità principali di IPv6 sono:

- IPv6
    - Indirizzi
    - Gestione delle opzioni
    - Gestione della frammentazione
    - Identificazione flussi
    - Classi di traffico
    - Nessun header checksum
- ICMPv6
    - Espande le funzionalità di ICMP
- ARP
    - Eliminato e sostituito da ICMPv6
- DHCPv6
    - Modificato per il nuovo protocollo (alcune funzioni sono svolte da ICMPv6)
- Protocolli di routing
    - RIPng e OSPFv6

### Header IPv6

![Basic Header in IPv6](../images/network-Untitled%2036.png)

Basic Header in IPv6

![Next Header in IPv6](../images/network-Untitled%2037.png)

Next Header in IPv6

L'header base può essere accompagnato da **Extension Header**, che aggiungono funzionalità quali:

- **Hop-by-hop option**: deve essere interpretato dai router ed ha varie opzioni per pacchetti lunghi e gestione di allineamenti a 32 bit
- **Source Routing**: serve ad obbligare i router a seguire un particolare percorso per il pacchetto
- **Fragmentation**: implementa la frammentazione, ma questa può essere eseguita solo dal mittente, che deve conoscere la massima MTU del path, ottenuta tramite i messaggi MTU Path Discovery forniti da ICMPv6
- **Authentication**: serve per l'autenticazione del mittente
- **Encrypted security payload**: serve a cifrare il payload

### Indirizzi IPv6

Gli indirizzi IP sono composti da 128 bit raggruppati a gruppi di 2 Byte. Spesso sono scritti in notazione esadecimale: `8000:0000:0000:0000:8965:0678:A45C:87D3`.

Gli zeri dell'indirizzo IP possono essere omessi per avere una notazione più compatta: `8000::8965:678:A45C:87D3`.

Esiste inoltre una notazione speciale per gli indirizzi IPv4: `::131.175.21.173`.

IPv6 prevede una ricca varietà di indirizzi ed assume che normalmente un'interfaccia abbia più di un indirizzo associato ad essa. Gli IPv6 si distinguono per:

- **Destinatario**
    - Unicast
    - Anycast (almeno uno di un gruppo)
    - Multicast
- **Uso**
    - Globale
    - Locale (stesso link o stesso site)

#### Prefissi IPv6

Così come IPv4, anche IPv6 assume i prefissi per un'individuazione del campo che identifica l'interfaccia. La notazione rimane uguale alla notazione *slash* usata per IPv4.

![Struttura di un indirizzo IPv6](../images/network-Untitled%2038.png)

Struttura di un indirizzo IPv6

I tipi diversi di indirizzi sono individuati dalla prima parte del prefisso, il **Format Prefix** (**FP**).

| Prefisso | Uso | Frazione |
| --- | --- | --- |
| 0000 0000 | Riservato per gli indirizzi IPv4 | ⁍ |
| 0000 0001 | Non assegnato | ⁍ |
| 0000 001 | Indirizzi OSI NSAP | ⁍ |
| 0000 010 | Indirizzi Novell Netware IPX | ⁍ |
| 0000 011 | Non assegnato | ⁍ |
| 0000 1 | Non assegnato | ⁍ |
| 0001 | Non assegnato | ⁍ |
| 001 | Indirizzi Aggregatable Global Unicast | ⁍ |
| 010 | Non assegnato | ⁍ |
| 011 | Non assegnato | ⁍ |
| 100 | Non assegnato | ⁍ |
| 101 | Non assegnato | ⁍ |
| 110 | Non assegnato | ⁍ |
| 1110 | Non assegnato | ⁍ |
| 1111 0 | Non assegnato | ⁍ |
| 1111 10 | Non assegnato | ⁍ |
| 1111 110 | Non assegnato | ⁍ |
| 1111 1110 0 | Non assegnato | ⁍ |
| 1111 1110 10 | Indirizzi ad uso Local Link | ⁍ |
| 1111 1110 11 | Indirizzi ad uso Local Site | ⁍ |
| 1111 1111 | Multicast | ⁍ |

| Tipo | Indirizzo | Descrizione |
| --- | --- | --- |
| Non specificato | 0:0:0:0:0:0:0:0 | Usato come indirizzo sorgente quando il nodo non conosce altri suoi indirizzi. Non può essere usato come indirizzo di destinazione |
| Indirizzo di loopback | 0:0:0:0:0:0:0:1 | Analogo a 127.0.0.0 in IPv4 |
| Indirizzo IPv6 compatibile con IPv4 | ::IPv4_Address | Utilizzato per far comunicare host IPv6 quando occorre attraversare una rete IPv4. Equivale a scrivere 96 bit 0 seguiti da un indirizzo a 32 bit |
| Indirizzo IPv4-Mapper | ::FFFF:IPv4_Address | Utilizzati per far comunicare host IPv6 con host IPv4. Equivale a scrivere 80 bit 0, 16 bit 1 ed un indirizzo a 32 bit |

#### Aggregatable Global Unicast Address

È un formato unicast globale. Ha una struttura gerarchica per ridurre i problemi di scalabilità delle tabelle di routing.

I tre macrolivelli sono:

- Public Topology
- Site Topology
- Interface ID

![Struttura di un Aggregatable Global Unicast Address](../images/network-Untitled%2039.png)

Struttura di un Aggregatable Global Unicast Address

| Campo | Acronimo | Descrizione |
| --- | --- | --- |
| Top Level Aggregation | TLA | Livello gerarchico più elevato, normalmente assegnato su base geografica o agli ISP di backbone |
| Reserved | Res | Riservato per future espansioni |
| Next Level Aggregation | NLA | Ogni ISP con un TLA può strutturare gerarchicamente le sue reti con diversi NLA |
| Site Level Aggregation | SLA | Livello legato al singolo site (sottorete) |
| Interface ID |  | 64 bit con formato derivato da IEEE EUI-64 |

Va notato che i livelli NLA e SLA possono essere ulteriormente divisi gerarchicamente.

#### Link-Local Unicast Address

![Struttura di un indirizzo Link-Local Unicast](../images/network-Untitled%2040.png)

Struttura di un indirizzo Link-Local Unicast

Sono tutti quegli indirizzi che hanno Format Prefix `1111 1110 10`.

Sono indirizzi utilizzabili solo per l'indirizzamento su un singolo *link* (sottorete).

IPv6 prevede che ogni interfaccia disponga di almeno un indirizzo link-local unicast, che viene normalmente assegnato per autoconfigurazione a partire dall'indirizzo fisico dell'interfaccia (IEEE EUI-64).

Questi indirizzi sono fondamentali nel processo di **Neighbor Discovery**.

#### Site-Local Unicast Address

![Struttura di un indirizzo Site-Local Unicast](../images/network-Untitled%2041.png)

Struttura di un indirizzo Site-Local Unicast

Sono tutti quegli indirizzi che hanno Format Prefix `1111 1110 11`.

Anche questi indirizzi sono destinati ad uso locale: definiscono uno spazio di indirizzamento privato.

### ICMPv6

ICMP acquista un'importanza molto maggiore con IPv6. Da questo protocollo infatti vengono svolte moltissime funzioni, quali:

- Error reporting e diagnostica di rete
- Risoluzione degli indirizzi di livello link
- Individuazione del router corretto
- Controllo degli indirizzi IPv6 assegnati
- Autoconfigurazione degli indirizzi IPv6
- Calcolo del PATH-MTU per la frammentazione

#### Struttura dei messaggi

![Struttura di un messaggio ICMPv6](../images/network-Untitled%2042.png)

Struttura di un messaggio ICMPv6

| Type | Nome |
| --- | --- |
| 1 | Destination unreachable |
| 2 | Packet too big |
| 3 | Time exceeded |
| 4 | Parameter problem |
| 128 | Echo request |
| 129 | Echo reply |

#### ICMPv6 Neighbors Discovery

Sono previste diverse procedure di **ND**:

- **Address Resolution**: funzione analoga a quella di ARP per IPv4
    
    Il messaggio di **Neighbor Solicitation** viene inviato all'indirizzo node-solicited multicast address, che può essere ricavato anche dal richiedente.
    
    Il messaggio di **Neighbor Advertisement** viene inviato all'indirizzo IPv6 sorgente del pacchetto di richiesta.
    
    ![Funzionamento dei messaggi di Neighbor Discovery](../images/network-Untitled%2043.png)
    
    Funzionamento dei messaggi di Neighbor Discovery
    
- **Router Discovery**: segnala e scopre la presenza di router sul link
    
    ![](../images/network-Untitled%2044.png)
    
- **Redirection**: simile all'operazione di redirect di IPv4
- **Neighbor Unreachability Detection**: scopre l'irraggiungibilità di host noti

#### Autoconfigurazione indirizzi

Oltre agli indirizzi Link-Local, si possono autoconfigurare anche indirizzi globali:

- **Stateful configuration** (tramite DHCPv6)
- **Stateless configuration** (tramite ICMP): in questo caso è noto il prefisso annunciato dai router e si può ricavare l'indirizzo a partire dall'indirizzo fisico a 64 bit

#### MTU Path Discovery

Il mittente deve conoscere la MTU più piccola sul percorso da seguire fino alla destinazione.

Per farlo, invia un pacchetto con una dimensione pari all'MTU del primo link da attraversare. Se viene ricevuto un messaggio ICMP `Packet too big`, viene ridotta la MTU fino a quando non arrivano più messaggi di errore.

### Migrazione IPv4 - IPv6

La migrazione, che sta avvenendo tuttora, si basa sull'uso di queste componenti:

- **Dual stack**: sistemi con doppio stack IPv4 ed IPv6
- **Tunneling**: attraversamento di porzioni di rete IPv4 mediante tunneling
- **Header translation**: traduzione degli header dei due formati
