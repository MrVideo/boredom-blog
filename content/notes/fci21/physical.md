---
title: 'Livello fisico'
draft: false
type: 'page'
toc: true
mathjax: true
---

---

## Segnali

I segnali possono essere divisi in due categorie:

1. Segnali **fisici** (**Sorgenti analogiche** o continue): associati a grandezze fisiche e tipicamente continue.
2. Segnali **logici** (**Sorgenti digitali-numeriche** o discrete): sequenze *nativamente* numeriche oppure segnali fisici digitalizzati.

L’informazione trasportata da Internet è **sempre in forma numerica**, anche se l’informazione originale è prodotta da una sorgente analogica.

![](../images/physical-Untitled.png)

Un segnale si può rappresentare con una **funzione del tempo**.

- **Segnali a tempo continuo**: $s(t), t \geq 0$, dove $s(t)$ rappresenta la variazione nel tempo di una grandezza fisica misurabile (tensione, corrente, intensità di campo elettrico, intensità luminosa…)

![Esempio di segnale a tempo continuo](../images/physical-Untitled%201.png)

Esempio di segnale a tempo continuo

- **Segnali a tempo discreto**: rappresenta una sequenza di impulsi ideali che si succedono a intervalli regolari $*T_c*$, per esempio:

$$s(t) = \sum_{k = 0}^\infty a_k \delta (t - kT_c), \space t \geq 0, \space \delta(x) = \begin{cases} 1 & \text{se } x = 0\\ 0 & \text{se } x \neq 0 \end{cases}$$

La sequenza dei numeri $\{a_k\}$, detta **sequenza dei campioni**, può rappresentare un segnale digitale.

![Esempio di segnale digitale a tempo discreto](../images/physical-Untitled%202.png)

Esempio di segnale digitale a tempo discreto

- **Segnale periodico**: si ripete nel tempo dopo ciascun periodo $*T*$: $s(t+T) = s(t=, t \geq 0$. Nella realtà, i segnali di interesse **non sono mai perfettamente periodici** (altrimenti non porterebbero informazione), ma variazioni di essi. L’analisi dei segnali periodici è più semplice di quella dei segnali non periodici, quindi essi sono un **modello analitico utile**.

### Analisi di Fourier

![Processo dell'Analisi di Fourier](../images/physical-Untitled%203.png)

Processo dell'Analisi di Fourier

<aside>
📓 L’analisi di Fourier serve a trasformare matematicamente un segnale dal dominio del **tempo** al dominio della **frequenza**.

</aside>

L’analisi di Fourier consente di studiare qualsiasi segnale **scomponendolo in sinusoidi**. I segnali periodici di periodo $*T*$ possono essere scomposti in un numero *discreto* di sinusoidi (**serie di Fourier**) di frequenza multipla della **frequenza fondamentale** (o *armonica fondamentale*) $f_0 = T^{-1}$:

$$s(t) = a_0+2\sum_{n=1}^\infty[a_n\cos(2\pi n f_0 t) + b_n\sin(2\pi n f_0 t)]$$

Le sinusoidi costituenti sono dette **armoniche** o **componenti spettrali**. Ciascuna di esse ha una sua ampiezza $S_n = \sqrt{a^2 + b^2}$ ed in generale è presente anche una componente **continua** $a_0$, che è un valore costante.

#### Esempio di spettro di un segnale

![Segnale periodico a media nulla con $T = 0.5\space \text{ms}$ ed $f_0 = 2 \space \text{kHz}$](../images/physical-Untitled%204.png)

Segnale periodico a media nulla con $T = 0.5\space \text{ms}$ ed $f_0 = 2 \space \text{kHz}$

Una sinusoide di periodo $*T*$ e frequenza $f_0$ nel dominio del tempo può essere rappresentata nel dominio delle frequenze dalla sola componente alla frequenza $f_0$.

In questo caso, il segnale è più complesso rispetto ad una sinusoide e quindi viene approssimato con più sinusoidi, perciò il dominio delle frequenze è maggiormente popolato.

![Segnale periodico a media nulla (onda quadra) con $T = 0.5 \space \text{ms}$ ed $f_0 = 2 \space \text{kHz}$](../images/physical-Untitled%205.png)

Segnale periodico a media nulla (onda quadra) con $T = 0.5 \space \text{ms}$ ed $f_0 = 2 \space \text{kHz}$

![Segnale periodico a media non nulla (onda quadra) con $T = 400 \space \text{ns}$ ed $f_0 = 2.5 \space \text{MHz}$](../images/physical-Untitled%206.png)

Segnale periodico a media non nulla (onda quadra) con $T = 400 \space \text{ns}$ ed $f_0 = 2.5 \space \text{MHz}$

In questo caso invece, troviamo anche una componente continua, che non varia nel tempo.

![Onda a dente di sega (spettro con armoniche sia pari sia dispari) con $T = 4.545 \space \text{ms}$ ed $f_0 = 220 \space \text{Hz}$](../images/physical-Untitled%207.png)

Onda a dente di sega (spettro con armoniche sia pari sia dispari) con $T = 4.545 \space \text{ms}$ ed $f_0 = 220 \space \text{Hz}$

#### Caratterizzazione spettrale dei segnali analogici

La **trasformata di Fourier** generalizza la serie di Fourier al caso di segnali **non periodici**. La trasformata scompone i segnali non periodici in un **insieme continuo di armoniche**. Ogni componente è in generale moltiplicata per un **coefficiente complesso**, che determina **un’ampiezza ed una fase** della sinusoide.

<aside>
📓 La funzione $*X(f)*$ che descrive le ampiezze e le fasi delle sinusoidi componenti è lo **spettro** del segnale $*x(t)*$.

</aside>

#### Banda di un segnale

<aside>
📓 La **banda di un segnale** $B$ è l’**intervallo di frequenze in cui il segnale non è nullo**.

</aside>

Esistono due tipi di segnali:

- A **banda stretta**: variano lentamente nel tempo
- A **banda larga**: variano velocemente nel tempo

| Segnale | Banda segnale |
| --- | --- |
| Segnale telefonico | 300 - 4000 Hz |
| Voce | 300 - 8000 Hz |
| Musica | 100 - 20000 Hz |
| TV analogica PAL (Phase Alternating Line) | 0 - 5 MHz |
| Cinema | 0 - 500 MHz |

### Trasformazione AD (Analog to Digital)

Per poter trasmettere un segnale analogico, è necessario trasformarlo in un segnale digitale. Si fa attraverso tre fasi.

#### Campionamento

![Trasformazione di un segnale tempo continuo ad un segnale tempo discreto](../images/physical-Untitled%208.png)

Trasformazione di un segnale tempo continuo ad un segnale tempo discreto

Il **Teorema di Nyquist** (o *Teorema del campionamento*) dice che un segnale tempo-variante è **completamente determinato dai suoi campioni** presi a intervalli di durata $*T_c*$ tale che $T_c < \frac{1}{2f_{\text{max}}}$, dove $*f_{\text{max}}*$ è la frequenza massima nello spettro del segnale.

<aside>
📓 La **frequenza di Nyquist** è la **frequenza minima da usare** per il campionamento:$f_c > f_N = 2f_{\text{max}}$.

</aside>

Se non si rispetta il teorema di Nyquist, si rischia di **non poter ricostruire il segnale originale fedelmente** (*aliasing*). Se invece la frequenza di campionamento è **esattamente il doppio** della frequenza massima del segnale, campionando negli istanti di attraversamento degli zeri **si possono confondere sinusoide e componente continua**.

| Segnale | Banda | Frequenza di Nyquist |
| --- | --- | --- |
| Segnale telefonico | 300 - 4000 Hz | 8000 Hz |
| Voce | 300 - 8000 Hz | 16000 Hz |
| Musica | 100 - 20000 Hz | 40 kHz |
| TV (PAL) | 0 - 5 MHz | 10 MHz |
| Cinema | 0 - 500 MHz | 1 GHz |

#### Quantizzazione

![Esempio di errore di quantizzazione](../images/physical-Untitled%209.png)

Esempio di errore di quantizzazione

È l’operazione con cui una grandezza che assume valori in un intervallo continuo è **trasformata in un valore all’interno di un set discreto di valori**.

Nella trasformazione si commette un **errore di quantizzazione**, dovuto all’approssimazione. Più livelli ci sono, minore sarà l’errore di quantizzazione. Aumentare livelli di quantizzazione però **aumenta il numero di bit da utilizzare**.

#### Codifica

Ciascun campione quantizzato è **codificato**, ossia **trasformato in bit**, in funzione del **numero di livelli** *l* secondo questa espressione: $l = 2^m$.

| Segnale | Livelli di quantizzazione | Bit di codifica |
| --- | --- | --- |
| Segnale telefonico | 256 | 8 |
| CD | 65536 | 16 |
| Livelli di grigio | 256 o 65536 | 8 o 16 |
| Livelli di colore | 16777216 | 24 |

#### Flussi binari equivalenti

Il **bitrate ottimale** per trasmettere un segnale **dipende dalla sua banda**. La formula generale per calcolare il bitrate ottimale è $R_b = 2B\cdot b$, dove $*B*$ è la banda e $*b*$ sono i bit usati per la quantizzazione.

| Segnale | Bitrate ottimale |
| --- | --- |
| Segnale telefonico | 64 kb/s |
| Voce | 256 kb/s |
| Musica | 704 kb/s |
| TV (PAL) | 240 Mb/s |
| Cinema | 24 Gb/s |

#### Modulazione

La sequenza digitale viene usata per **modificare**, ossia *modulare*, **uno dei parametri** (ampiezza, frequenza, fase…) **di un segnale fisico** inviato nel mezzo trasmissivo.

La modulazione può avvenire in *banda base* o in *banda passante*:

- **Banda base**: i segnali hanno uno spettro contiguo rispetto all’origine. Un esempio è la **PAM** (*Pulse Amplitude Modulation*), in cui il bit corrisponde ad un impulso di ampiezza positiva (1) o negativa (0).
- **Banda passante** o **traslata**: i segnali da modulare hanno uno spettro traslato su intervalli di frequenze non contigue all’origine. Si usa un’onda elettromagnetica detta **portante** (*carrier*) ad una determinata frequenza *fp* per traslare lo spettro del segnale intorno alla frequenza della portante.

![Modulazione d'ampiezza analogica: **PAM** (*Pulse Amplitude Modulation*)](../images/physical-Untitled%2010.png)

Modulazione d'ampiezza analogica: **PAM** (*Pulse Amplitude Modulation*)

![Modulazione in **banda traslata**: moltiplico l’onda del segnale da modulare con la sinusoide portante per ottenere il segnale modulato da inviare nel canale](../images/physical-557828D2-CB4E-4FE3-B2FC-F5DD74E2ECEC.png)

Modulazione in **banda traslata**: moltiplico l’onda del segnale da modulare con la sinusoide portante per ottenere il segnale modulato da inviare nel canale

![Spettro del segnale modulato](../images/physical-Untitled%2011.png)

Spettro del segnale modulato

La modulazione numerica in banda traslata viene applicata modulando uno dei parametri della sinusoide portante:

- Modulazione d’ampiezza (**ASK**, *Amplitude Shift Keying*)
- Modulazione di frequenza (**FSK**, *Frequency Shift Keying*)
- Modulazione di fase (**PSK**, *Phase Shift Keying*)
- Modulazione **QAM** (*Quadrature-Amplitude Modulation*): cambiamento misto di ampiezza e fase

![Vari tipi di modulazione](../images/physical-Untitled%2012.png)

Vari tipi di modulazione

Per aumentare la capacità di canale è possibile incrementare l’**ordine** della modulazione: m**odulazione multilivello**.

Servono:

- Un bitrate in ingresso diviso in gruppi di $log_2(n)$
- $N$ livelli di ampiezza diversi
- Ad ogni simbolo/impulso corrispondono $n = log_2(N) \space \text{bit}$

![PAM con 4 livelli di ampiezza](../images/physical-Untitled%2013.png)

PAM con 4 livelli di ampiezza

<aside>
📓 Si definisce in questo contesto una velocità *diversa* dal bitrate, chiamata **baud rate**, che misura il numero di simboli al secondo. Vale la relazione $R_b = R_s * log_2(N)$.

</aside>

![Modulazioni multilivello di fase dove $l$ rappresenta la portante *in fase* (cosinusoide) e $Q$ la portante *in quadratura* (sinusoide). I valori differenti di seno e coseno distinguono i baud da trasmettere](../images/physical-Untitled%2014.png)

Modulazioni multilivello di fase dove $l$ rappresenta la portante *in fase* (cosinusoide) e $Q$ la portante *in quadratura* (sinusoide). I valori differenti di seno e coseno distinguono i baud da trasmettere

![Modulazione multilivello di ampiezza e fase (QAM). 16 livelli (*16QAM*) di fase e ampiezza. Si parla anche di *costellazione*.](../images/physical-Untitled%2015.png)

Modulazione multilivello di ampiezza e fase (QAM). 16 livelli (*16QAM*) di fase e ampiezza. Si parla anche di *costellazione*.

Usando la trasmissione multilivello, posso **incrementare la capacità trasmissiva** di *n* volte. Tuttavia, **la velocità massima non può essere aumentata** arbitrariamente aumentando i livelli, per due ragioni:

1. Se mantengo inalterata la distanza tra i vari simboli, devo **aumentare l’energia dell’impulso**, necessaria per trasmettere i simboli *più esterni* della costellazione.
2. Se mantengo inalterata l’energia massima, la trasmissione è **più sensibile al rumore introdotto dal canale**, che può far equivocare il livello in ricezione (errore di ricezione)

#### Canale trasmissivo

Un impulso che attraversa un canale trasmissivo è soggetto ad alterazioni di vario tipo:

- **Attenuazione**: la potenza del segnale si riduce in funzione della distanza percorsa e della frequenza del segnale.
- **Dispersione**: introduzione di un ritardo differente per ciascuna componente spettrale del segnale.

Tali distorsioni possono essere sintetizzate tramite una funzione $H(f)$ nel dominio delle frequenze, detta **risposta in frequenza** del canale trasmissivo. Inoltre il canale trasmissivo può introdurre **rumore** (segnale di disturbo) che influisce generalmente su tutte le componenti dello spettro elettromagnetico (cioè su tutte le armoniche che costituiscono l’impulso). Il rumore è generalmente descritto con modelli probabilistici, poiché è casuale e non deterministico. Il rumore bianco è chiamato così perché si presume sia presente in *tutte le frequenze*.

Ogni mezzo trasmissivo è caratterizzato da un intervallo di frequenze in cui l’alterazione del segnale è minima. Quella banda è detta **banda passante del canale**. È opportuno che il segnale introdotto nel canale sia alla frequenza che il canale non distorce. La banda passante del canale dev’essere non solo ben centrata sullo spettro del segnale, ma deve anche essere più larga dello spettro del segnale, per evitare che vengano tagliate parti di esso.

Una proprietà che nasce dalla trasformata di Fourier fa sì che lo spettro del segnale immesso nel canale trasmissivo $*S(f)*$ sia ricevuto con uno spettro $S'(f) = S(f) \cdot H(f)$, dove $*H(f)*$ è la funzione di trasferimento del canale.

#### Canale passa-basso e passa-banda

Se il mezzo presenta una banda passante intorno alla frequenza 0, viene detto canale **passa-basso** o in **banda base**. Ha un’attenuazione costante sulla sua banda e fa passare soltanto le frequenze più basse dello spettro.

Un canale **passa-banda** (o in **banda passante**) invece fa passare solo una certa banda di frequenze e taglia ciò che sta intorno. Anche questo ha un’attenuazione costante sulla sua banda. Deve sempre essere usata un’onda portante (*modulazione in banda passante*) per trasmettere il segnale.

Al giorno d’oggi, quasi tutti i canali trasmissivi sono passa-banda.

![**Esempio 1**: canale passa basso di larghezza $*W*$. Segnale periodico nel tempo a media nulla. $T = 500 \space \mu \text{s}, \space F = 2 \space \text{kHz}$](../images/physical-Untitled%2016.png)

**Esempio 1**: canale passa basso di larghezza $*W*$. Segnale periodico nel tempo a media nulla. $T = 500 \space \mu \text{s}, \space F = 2 \space \text{kHz}$

![Con frequenza di taglio a $W = 32 \space \text{kHz}$ è approssimato con sufficiente dettaglio.](../images/physical-Untitled%2017.png)

Con frequenza di taglio a $W = 32 \space \text{kHz}$ è approssimato con sufficiente dettaglio.

![**Esempio 2**: canale passa-basso di larghezza *W*. Segnale periodico nel tempo a media *non nulla*. $T = 400 \space \text{ns}, \space F = 2.5 \space \text{MHz}$](../images/physical-Untitled%2018.png)

**Esempio 2**: canale passa-basso di larghezza *W*. Segnale periodico nel tempo a media *non nulla*. $T = 400 \space \text{ns}, \space F = 2.5 \space \text{MHz}$

![Con frequenza di taglio a $W = 80 \space \text{MHz}$ è approssimato con sufficiente dettaglio.](../images/physical-Untitled%2019.png)

Con frequenza di taglio a $W = 80 \space \text{MHz}$ è approssimato con sufficiente dettaglio.

#### Canali e mezzi trasmissivi

- Mezzi trasmissivi **guidati**
    - **Mezzi elettrici**: si modula un segnale che è associato ad una variazione di tensione o corrente
    - **Fibre ottiche**: si modula un segnale sotto forma di impulsi luminosi
- Mezzi trasmissivi **non guidati**
    - **Onde radio**: il segnale è associato ad un’onda elettromagnetica che si propaga nello spazio che ha la proprietà di riprodotte a distanza una corrente elettrica in un dispositivo ricevente (antenna)

Ciascun mezzo ha le proprie peculiarità riguardo a:

- Banda passante
- Attenuazione
- Sensibilità al rumore

![Bande tipiche di mezzi trasmissivi](../images/physical-Untitled%2020.png)

Bande tipiche di mezzi trasmissivi

#### Velocità di trasmissione e banda passante del canale

Canale con banda passante pari a  $B \space [\text{Hz}]$.

Baud rate:$R_s = \eta _s \cdot B \space \frac{\text{simboli}}{\text{s}}$, dove $*\eta_s*$ è l’**efficienza spettrale$[\frac{\text{simboli}/\text{s}}{\text{Hz}}]$.**

Si può dimostrare che usando impulsi **ideali**, $\eta_s = 2$, quindi $R_s \approx 2B \text{ simboli}/\text{s}$, mentre usando forme di impulsi **reali** che resistono al rumore del canale: $\eta_s = 1$, quindi $R_s \approx B$.

- **Trasmissione binaria**: Bit rate massimo: $R_{b, \text{ max}} = R_s \approx B \text{ bit} / \text{s}$.
- **Trasmissione multilivello** con *n* bit per simbolo: Bit rate massimo: $R_{b, \text{ max}} = nR_s \approx nB \text{ bit} / \text{s}$.

#### Attenuazione

Se il segnale in ingresso ha una potenza *Pin* e il segnale di uscita ha una potenza *Pout*, si definisce **attenuazione** del collegamento il rapporto $A = P_{\text{out}}/P_{\text{in}}$. Viene generalmente indicato in decibel: $A = 10 \cdot log_{10}(P_{\text{out}}/P_{\text{in}})$.

Il contrario dell’attenuazione è il **guadagno**.

#### Rumore

![Probability Density Function d'esempio. Asse x: *ampiezza* del segnale ricevuto, asse y: *probabilità di ricezione* di una data ampiezza.](../images/physical-Untitled%2021.png)

Probability Density Function d'esempio. Asse x: *ampiezza* del segnale ricevuto, asse y: *probabilità di ricezione* di una data ampiezza.

In un canale di comunicazione, tra trasmettitore e ricevitore, è sempre inserito un **rumore casuale**, a componenti **non predicibili**, con frequenze anche del nostro segnale. Questo può determinare **errori di ricezione** con una **probabilità di errore** $*P*$ (qualità del sistema).

La probabilità di errore **quantifica quanti bit in una data sequenza vengono modificati** a causa del rumore o di altri segnali o apparati che creano interferenza.

Questo tipo di grafico prende il nome di *Probability Density Function* (**PDF**).

Nel mondo ideale, senza avere rumore, posso ricevere soltanto due valori. Ma per effetto del rumore, la probabilità che ciò avvenga è *distribuita* su un set di intervalli. Più alto è il picco nel grafico PDF, migliore è il canale. Nel ricevitore si imposta una **soglia di decisione**, che serve al ricevitore ad avere un intervallo in cui il segnale verrà decodificato in un modo e un altro in cui verrà decodificato in un altro.

![Esempio di decisore](../images/physical-Untitled%2022.png)

Esempio di decisore

Con la modulazione multilivello, il ricevitore è provvisto di un **decisore**, che elabora il campione del segnale ricevuto. Si misura l’**energia** del simbolo ricevuto e la si confronta con dei possibili risultati attesi. La misura sarà un numero casuale per effetto del rumore del canale.

#### Errori in ricezione

![Le code delle PDF si accavallano, causando errori in ricezione](../images/physical-Untitled%2023.png)

Le code delle PDF si accavallano, causando errori in ricezione

Nel mondo ideale, la PDF di un dato simbolo ricade interamente nella sua soglia di decisione. Ma nel mondo reale, le PDF dei simboli possono **accavallarsi**. In questo caso, il decisore tradurrà un simbolo errato e si avrà un **errore in ricezione**.

#### Codici correttori

Si può abbassare la probabilità d’errore in un blocco adottando codici correttori d’errore (**FEC**, *Forward Error Correction*). Questi consistono nell’aggiungere dei bit di ridondanza (*parità*) in modo che gli errori che occorrono, se limitati in numero, possono essere corretti. Sono progettati in modo da correggere fino a *c* errori (potere correttore del codice).

Esempio: codice a ripetizione $(n, 1)$; consiste nel ripetere tre volte il bit da trasmettere, quindi abbiamo $(n - 1)$ cifre di parità. Con $n$ dispari è in grado di correggere $c = (n-1)/2$ errori.

#### Ritrasmissione

Se un codice non riesce a correggere un errore può spesso riuscire a rilevarlo (il controllo di parità dà risultato negativo). Nella trasmissione a commutazione di pacchetto è possibile rilevare gli errori in ricezione e richiedere la **ritrasmissione** del pacchetto errato (**ARQ**, *Automatic Repeat reQuest*).
