---
title: 'Introduzione al corso'
draft: false
type: 'page'
toc: true
mathjax: true
---

---
## Panoramica sul corso

[Informazioni docenti](https://www.notion.so/911cbaa61e4b40a6a227d43eff9e0f5a)

### Materiale didattico

- Testo di riferimento: *Achille Pattavina*, **Internet e Reti - Fondamenti**, *Seconda edizione*, [internetereti.it](http://internetereti.it/)
- Slide e lezioni
- Video di approfondimenti, esercizi e strumenti
- Esercizi svolti e temi d’esame precedenti
- Materiale a supporto del laboratorio

**Tutto il materiale è disponibile su Beep**

### Programma del corso

Esercitazioni in presenza e online.

*Flipped classroom*: brevi video sugli argomenti con discussione in classe.

#### **Laboratorio**

- Sniffer di rete (Wireshark)
- Ping, Traceroute, Strumenti del browser, Dig, DNSLookup
- Protocolli applicativi

**Hands-on**

- Python e scripting per analisi di rete
- Programmazione socket in Python
- Configurazioni e simulazione di rete (Packet Tracker)
- Attività sperimentali

**Tre fasi per ogni laboratorio**

1. A casa: studio di materiale di base
2. In aula: esercizi hands-on con tutor
3. In aula o a casa: autovalutazione del lavoro confrontandolo con la soluzione proposta

#### Organizzazione del corso

- 50 ore di lezione circa
- 30 ore di esercitazione circa
- 18 ore di laboratorio

**Il laboratorio è online** ed è necessario **il proprio PC**.

Il venerdì ci sarà lezione **solo se necessario**.

#### Esame

**Quattro** mini prove in itinere:

1. 19 Marzo
2. 23 Aprile (include la prima parte di laboratorio)
3. 21 Maggio
4. 11 Giugno (da confermare; include la seconda parte di laboratorio)

**Esame scritto**:

- Esercizi simili a quelli visti a lezione ed esercitazione
- Domande (teoriche o in forma di esercizio breve)
- Massimo 26/27 punti

**Valutazione del laboratorio**: esercizi di laboratorio in forma scritta, massimo 6 punti.

**Possibilità bonus con Quiz** (circa sei durante l’anno).

**Non è possibile congelare il voto o porzioni di voto**, iscrivendosi ad un appello si rifiutano automaticamente le valutazioni precedenti.

Orale **solo a discrezione del docente**.

---

## Introduzione al corso

Scopo del corso: fornire le conoscenze fondamentali sul funzionamento della rete tra calcolatori.

### Cenni storici

#### Prima di internet

Applicazioni isolate:

- Elaborazioni isolate
- Scambio di dati *a mano* (schede perforate, nastri, floppy…)

Reti di TLC isolate:

- Reti dedicate ai servizi
- Nessuna elaborazione

#### La nascita di Internet

La nascita di Internet si fa risalire agli anni ’60 per vari eventi:

- **1961**: Kleinrock, dimostra l’efficacia della *commutazione di pacchetto* grazie alla *teoria delle code*
- **1967**: Lawrence Roberts progetta ARPAnet (*Advanced Research Projects Agency*), prima rete di computer interconnessi per i militari americani
- **1969**: primo nodo di IMP (*Interface Message Processor*) di ARPAnet all’UCLA

Negli **anni ’70** si sviluppa ancora di più il concetto di Internet:

- **1970**: ALOHAnet, rete radio a pacchetti dell’università delle Hawaii
- **1972**: Nasce **NCP** (*Network Control Protocol*), il primo vero *protocollo* di internet. Nasce anche il primo programma di posta elettronica e ARPAnet si espande a 15 nodi
- **1974**: Cerf e Kahn definiscono i principi dell’*internetworking*
- **1976**: Nasce **Ethernet** nei laboratori di Xerox
- **1979**: ARPAnet si espande a 200 nodi

**Anni ’80**:

- **1982**: definizione protocollo **SMTP**
- **1983**: rilascio dello stack di protocolli **TCP/IP** (sostituisce NCP). Viene anche definito il **DNS**.
- **1985**: definizione protocollo **FTP**
- **1988**: controllo della congestione TCP

Nascono nuove reti nazionali come Csnet, BITnet, NSFnet…

Ci sono ora più di 100000 host collegati.

**Anni ’90**:

- **1990**: ARPAnet viene dismessa
- **1991**: NSF lascia decadere le restrizioni sull’uso commerciale di NSFnet
- **Primi anni ’90**: Tim Berners-Lee inventa il **World Wide Web** al CERN di Ginevra
- **1994**: Browser internet: Mosaic e **Netscape**
- **Fine anni ’90**: commercializzazione del web

Anni **2000-2009**:

- Arrivano le *killer app*: instant messaging, file sharing P2P, IP telephony, social network
- **La sicurezza di rete diventa un problema**
- Centinaia di milioni di host, **un miliardo di utenti**
- Velocità nelle dorsali dell’ordine dei **Gbps**

Anni 2010 - **giorno d’oggi**:

- Esplosione della *Mobile Internet*
- Arrivano gli **smartphone**
- La **telefonia** si trasferisce **definitivamente su Internet**
- I **contenuti video** diventano il traffico predominante sulla rete
- Esplosione delle **app**

#### Cosa significa oggi sviluppare un'applicazione

Oggi, scrivere un’applicazione di rete comporta una serie di passi complessi:

- Scrivere le componenti server
- Inserirle in macchine virtuali
- Istanziarle su un servizio cloud
- Scrivere le componenti client per le diverse piattaforme
- Inserirle nei relativi store online
- Aspettare che gli utenti scarichino le applicazioni

**Controllare la relazione con la rete è fondamentale**. È ormai fondamentale saper gestire sia la parte di sviluppo software che di sviluppo rete per gestire correttamente un nuovo software.

---

## Elementi di Internet

### Cos’è Internet?

#### Un insieme di **componenti fisiche**

- Milioni di *computer* connessi alla rete chiamati **host** (**terminali**)
    - Tutti gli host sono sistemi in grado di inviare e ricevere informazioni per le loro applicazioni finali. Hanno caratteristiche molto diverse
- Nodi di rete chiamati **router** (**nodi**). Altri nodi di rete sono *switch*, *access point*, *modem*…
    - I principali sono i router, che operano su unità informatiche di dimensioni finite dette **pacchetti**. Esistono altri nodi di rete che a livello locale svolgono altre funzioni di collegamento
- Canali di comunicazione di diversi tipi (fibra, cavo, radio, satellite…) chiamati **link** (**collegamenti**)
    - I collegamenti possono essere di natura fisica molto diversa. Differiscono anche per tecnologia di trasmissione dell’informazione. La velocità di trasmissione è misurata in **bit/s** e suoi multipli
- Interconnesse gerarchicamente

#### Un’**architettura di rete**

Rete di accesso: tecnologie che permettono agli utenti finali di connettersi all’ISP (*Internet Service Provider*). Tipicamente si tratta di un router.

**Storia dei mezzi di accesso ad Internet**

| Name | Velocità di trasmissione | Descrizione |
| --- | --- | --- |
| Dial-Up Modem | 56 kbps | Accesso diretto al router dell'ISP mediante circuito telefonico.
Trasmissione del segnale in banda telefonica, fino a 4 kHz |
| ADSL | 20 Mbps down
1 Mbps up | Condivisione del doppino con la rete telefonica fino alla centrale (divisione di frequenza).
Accesso al router dell'ISP mediante rete dati ad alta velocità. |
| Fibra ottica | Fino a 10 Gbps | Diversi tipi:
FTTH (Fiber to the Home)
FTTB (Fiber to the Basement)
FTTC (Fiber to the Curb)
FTTN (Fiber to the Neighborhood) |
| Rete cellulare | 200 kbps
14,5 Mbps down / 5,7 Mbps up
300 Mbps down / 85 Mbps up | GPRS/EDGE
HSPA
LTE |
| Wireless LAN | 11 / 54 / 300 / 1000 Mbps | Standard 802.11 b/g/n/Y/ac
Accesso condiviso radio (wireless) attraverso stazione base o punto d’accesso. |

Internet è un puzzle di tante reti interconnesse. Questo ha due risvolti importanti:

1. La tecnologia di Internet (**IP** - Internetworking Protocol) può essere usata per interconnettere **sotto-reti di tipo eterogeneo**
2. L’intera rete Internet mondiale è composta da **tante reti** gestite da **operatori diversi** (**ISP**) che si accordano per collegarle

Le diverse porzioni di rete sono composte da tecnologie diverse ed esistono anche sotto-reti che gestiscono internamente propri nodi e link.

| Nome | Significato | Descrizione |
| --- | --- | --- |
| LAN | Local Area Network | impiegate in aree limitate (casa, campus, azienda) |
| MAN | Metropolitan Area Network | coprono estensioni di alcune decine di chilometri |
| WAN | Wide Area Network | coprono estensioni di alcune decine di chilometri |

Ci sono ISP specializzati per specifici segmenti di rete.

| Tier | Descrizione |
| --- | --- |
| Tier 1 | hanno clienti solo altri ISP e operano WAN intercontinentali |
| Tier 2 | ISP di estensione nazionale o regionale |
| Tier 3 | ISP locali che hanno come clienti gli utenti finali |

I collegamenti tra ISP dello stesso tipo vengono chiamati *Peering Link*. Servono a scambiare traffico tra ISP.

![Architettura di interconnessione](../images/Schermata_2021-02-23_alle_16.33.37.png)

Architettura di interconnessione

![Architettura dei Neutral Access Point](../images/82099958-9781-4F17-A0A4-A5954D95B00F.png)

Architettura dei Neutral Access Point

#### Un **servizio di comunicazione** ed i **protocolli di comunicazione**

Le componenti fisiche e l’architettura supportano diversi **servizi di comunicazione.**

<aside>
📓 **Protocolli di comunicazione**: insieme delle *regole* per *formattare*, inviare e ricevere messaggi

</aside>

Il servizio di trasporto offerto dalla rete alle applicazioni può essere di vari tipi, in funzione della qualità del servizio (QoS) richiesta:

- possono essere trasportati brevi messaggi in modo *non affidabile*
- possono essere trasportate sequenze anche lunghe di byte in modo *affidabile*

Le applicazioni richiedono alla rete di fornire il servizio più appropriato mediante apposite interfacce di programmazione: le **API** (*Application Programming Interface*).

**Tipici parametri di QoS**:

- Ritardo
- Traffico trasportato (*throughput*)
- Probabilità di perdita
- Tempo reale

[Tipici parametri di QoS di servizi comuni](https://www.notion.so/9024ba26bd34491aa6021d526b8e855c)

Tramite i protocolli, la rete può fornire un servizio di comunicazione alle applicazioni, ovvero il servizio di trasferimento delle informazioni tra i processi remoti.

L’architettura dei protocolli in Internet è organizzata in una struttura a **livelli**, ognuno dei quali può aggiungere un valore al servizio.

Esistono due modelli per i protocolli di comunicazione:

1. Modello **client/server**
2. Modello **peer-to-peer**

La rete che trasporta i dati **non fa distinzione tra i modelli.**
