---
title: 'Architettura a livelli'
draft: false
type: 'page'
toc: true
mathjax: true
---

---

## Servizio di comunicazione

Si considerano due nodi (A e B), in due zone geografiche differenti, che vogliono *comunicare*. Il **servizio di comunicazione** è ciò che i due nodi utilizzano per trasportare l’informazione da A a B, ossia è il *fornitore del servizio di trasporto dell’informazione*.

Esempi:

- Il servizio postale
- Servizi di online gaming

Il servizio di trasferimento può trasportare diversi tipi di informazioni (flussi audio, video, messaggi applicativi, pacchetti, bit).

### Primitive di servizio

Il servizio di comunicazione può essere descritto mediante delle **chiamate di servizio**, dette *primitive di servizio*. In generale, servono a descrivere il servizio, a richiederlo ed a ricevere le informazioni sul servizio dal fornitore. Sono caratterizzate da *parametri* quali:

- Informazione da trasferire
- Indicazione del destinatario
- Caratteristiche del servizio richiesto

### Caratteristiche del servizio di comunicazione

**Modalità a connessione**:

1. Instaurazione della connessione
2. Trasferimento dell’informazione
3. Rilascio della connessione

**Modalità senza connessione**: una sola fase: trasferimento dell’informazione

### Protocollo di comunicazione

Insieme di regole che gestiscono il *colloquio* tra entità. Riguarda:

- Il formato dei messaggi
- Le informazioni di servizio
- Gli algoritmi di trasferimento

Quando due entità colloquiano tra loro, sono dette di *pari livello*.

### Packet Data Units (PDU)

Unità di trasferimento delle informazioni, tipicamente una sequenza di bit. Possono contenere sia dati dell’informazione da trasferire, sia informazioni di servizio. La PDU ha un formato specifico. È formata da due parti:

1. **Header**: contiene le informazioni di servizio
2. **Dati**: informazione da trasferire

### Livelli

Se le entità sono in grado di colloquiare tra loro, possono offrire loro stesse un servizio di comunicazione ad un *livello superiore*. Le entità di livello superiore possono *sfruttare* il servizio di comunicazione costruito sui nodi del livello inferiore per scambiarsi dati. Il livello più basso si definisce *livello fisico*.

Il servizio di comunicazione è più ricco grazie all’implementazione di *funzioni* sui vari livelli.

#### Architettura a livelli

I servizi più complessi possono essere articolati a livelli, da un livello che garantisce solo il trasporto dei bit ad un livello dove sono definiti complessi servizi caratterizzati da molti parametri e funzionalità. Nel caso di internet, i livelli sono **cinque**:

| Nome livello | Numero | Descrizione                                                                                                 | Tipo di PDU |
| ------------ | ------ | ----------------------------------------------------------------------------------------------------------- | ----------- |
| Applicativo  | 5      | È il livello usato dalle applicazioni e che contiene i protocolli applicativi.                              | Messaggi    |
| Trasporto    | 4      | Ha il compito di consegnare le informazioni tra nodi.                                                       | Segmenti    |
| Rete         | 3      | Questo livello è importante per la gestione della consegna delle informazioni attraverso le vie della rete. | Pacchetti   |
| Linea        | 2      | Trasporta le trame.                                                                                         | Trame       |
| Fisico       | 1      | Trasporta i bit a livello fisico nella rete.                                                                | Bit         |

Effettivamente si *aprono* le buste mano a mano che si sale nella *pila di protocolli*.

**TCP/IP**: indica due protocolli:

- *Transport Control Protocol* (Livello 4)
- *Internet Protocol* (Livello 3)

#### Perché un’architettura a livelli?

Serve a consentire di svolgere una serie di funzioni separandole a livelli diversi. La separazione è utile perché la complessità nell’implementazione delle diverse funzioni può essere *relegata* a livelli diversi. Separare i livelli consente una modularità di implementazione che possono essere affidati a parti hardware diversi o a sviluppatori software diversi.

#### Funzioni

Sono molteplici le funzioni che possono essere svolte da un livello, ma alcuni esempi base sono:

- **Multiplazione** e **de-multiplazione**: consente ad un livello di ricevere unità informative da più livelli superiori (come avere più utenti dello stesso servizio di comunicazione). La de-multiplazione è il processo opposto che avviene al nodo destinatario. Per funzionare, si basa su etichette oppure indirizzi che distinguono le utenze del servizio. L’etichetta usata è identificata dalla **porta logica**: ogni applicazione è distinta da un numero di porta specifico, che è aggiunto all’**indirizzo di rete** di ogni nodo.
- **Controllo d’errore**: verifica che le informazioni ricevute siano corrette e nella giusta sequenza di ricezione. Vengono inserite nel pacchetto informazioni aggiuntive per il controllo d’errore. Il destinatario controlla i dati del controllo d’errore per vedere se i dati sono corretti. Nel caso non ci siano errori, il destinatario invia un pacchetto chiamato **ACK**, che indica al mittente che lo scambio è avvenuto senza errori. Se l’ACK non viene inviato, dopo un *timeout* il client invia nuovamente lo stesso pacchetto. Viene usato ai livelli 2 e 4 della rete internet.
- **Instradamento** (*routing*): implementa il meccanismo che consente all’*entità instradante* di definire che strada far seguire all’informazione per raggiungere la sua destinazione. L’entità instradante può ricevere informazioni dal livello superiore, in modo da ricevere l’**indirizzo**, oltre che alle informazioni da spedire. Quando questo pacchetto viene passato al livello 2, nell’header viene inserito anche l’indirizzo a cui il pacchetto deve essere inviato. L’indirizzo consente alle entità intermedie di proseguire nel percorso verso la destinazione. Il pacchetto può arrivare da una porta d’ingresso, viene portato all’entità instradante, che ne analizzerà l’header che contiene l’indirizzo. Grazie al processo chiamato **table lookup**, l’entità controlla l’indirizzo del pacchetto con una lista di indirizzi per decidere dove mandare il pacchetto perché arrivi alla giusta destinazione. Se il pacchetto arriva da una porta d’ingresso, **non sale mai oltre l’entità instradante** se non all’arrivo a destinazione. Esistono molti modi per compiere l’instradamento. Nel caso dei **router**, viene usata una funzione di livello 3. Nel caso dei **network switch**, l’instradamento avviene al livello 2 con tabelle differenti. Esiste anche la possibilità di fare instradamento al livello 5 grazie ai **proxy**.

#### Chi scrive le tabelle di instradamento?

Le tabelle di instradamento possono essere **scritte a mano** (*Human Defined Networking*). Questo meccanismo manuale configura *rotte statiche* di Internet.

Oggi, il meccanismo più comunemente utilizzato è formato dai **protocolli di instradamento**, meccanismi che consentono ai nodi di comunicare tra loro e di scrivere *automaticamente* le tabelle. I router possono imparare autonomamente le righe della tabella da scrivere mediante meccanismi distribuiti.

Da alcuni anni sta emergendo un nuovo meccanismo di gestione di rete chiamato **Software Defined Networking** (*SDN*). In questo caso, è un software che, al posto dell’umano, scrive le righe delle tabelle di instradamento. In alcuni contesti, rappresenta un modo sofisticato di modificare il modo in cui funzionano le reti.
