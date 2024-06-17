---
title: 'Equazioni differenziali ordinarie'
draft: false
type: 'page'
toc: true
mathjax: true
---

---

## Equazioni differenziali del primo ordine

Un'equazione differenziale del primo ordine è una relazione che coinvolge una funzione incognita $y(t)$ e la sua derivata prima:

$$y'(t) = f\big(t, y(t)\big)$$

- **Esempio**
    
	Una equazione differenziale del primo ordine può essere:

$$y'(t) = {1\over t}, \ f\big(t, y(t)\big) = {1\over t}$$

In questo caso specifico, $f$ non dipende esplicitamente da $y$.

Poiché $1/t$ non è definita per $t = 0$, dobbiamo risolvere l'equazione differenziale separatamente negli intervalli $(-\infty, 0)$ e $(0, +\infty)$:

$$\begin{aligned}
y'(t) = {1\over t},\ t>0 &\to y(t) = \ln(t)+c,\ c\in\mathbb R\\\
y'(t) = {1\over t},\ t<0 &\to y(t) = \ln(-t)+c,\ c\in\mathbb R\\\
\end{aligned}$$

In generale, un'equazione differenziale ordinaria ha infinite soluzioni.

Nello specifico, se è un'equazione differenziale del primo ordine, avrà $\infty^1$ soluzioni; se è del secondo ordine, ne avrà $\infty^2$, e così via per i successivi ordini.

Data un'equazione differenziale ordinaria, si chiama **integrale generale** l'insieme di tutte le soluzioni, mentre si chiama **integrale particolare** una specifica soluzione.



- **Esempio**

Riprendendo l'equazione differenziale $y'(t) = 1/t$, applichiamo il teorema fondamentale del calcolo integrale:

$$\begin{aligned}
\int_{t_0}^t y'(x)dx &= \int_{t_0}^t{1\over x}dx\\\
y(t) - y(t_0) &= \ln(t)-\ln(t_0)\\\
y(t) &= \ln(t) \underbrace{- \ln(t_0) + y(t_0)}_{c}\\\
y(t) &= \ln(t) + c
\end{aligned}$$

### Soluzioni costanti di equazioni differenziali del primo ordine

Data un'equazione differenziale ordinaria $y'(t) = f\big(t, y(t)\big)$, una **soluzione costante** è una funzione $y(t) = c,\ \forall t$ che sia soluzione dell'equazione differenziale. Ciò accade nel caso in cui:

$$y(t) = c \iff f(t, c) = 0, \ \forall t$$

- **Esempio**

Data l'equazione differenziale ordinaria $y'(t) = ky(t) - hy^2(t)$, cerco una costante $c\in \mathbb R | ky-hy^2 = 0$.

$$\begin{aligned}
ky-hy^2 &= y(k-hy) = 0 \implies y = 0, {k\over h}
\end{aligned}$$

L'equazione differenziale ha quindi due soluzioni costanti.

Data ora l'equazione differenziale ordinaria $y'(t) = te^{y(t)}$, troviamone le soluzioni costanti. Deve valere:

$$y(t) = c \iff f(t, c) = 0, \ \forall t$$

Ma una funzione esponenziale non si annulla mai, perciò questa equazione differenziale ordinaria non ha soluzioni costanti poiché $\nexists \ c \ |\  e^c=0$.

### Equazioni differenziali ordinarie a variabili separabili

Un'equazione differenziale ordinaria del primo ordine si dice a variabili separabili se è nella forma:

$$y'(t) = h(t)g\big(y(t)\big), h:J_1\subseteq \mathbb R\to\mathbb R, g: J_2\subseteq\mathbb R\to\mathbb R ,\text{ continue}$$

In altre parole: $f(t, y) = h(t)\cdot g(y)$ è il prodotto di una funzione che dipende solo da $t$ per una funzione che dipende solo da $y$.

- **Esempio**

Prendiamo per esempio $y'(t) = 1/t$. Identifichiamo le due funzioni $h$ e $g$:

$$\begin{cases}
h(t) = {1\over t}, &J_1 = \mathbb R\setminus\{0\}\\\
g(y) = 1, &J_2 = \mathbb R
\end{cases}$$

Possiamo trovare il dominio di $f$ come il **prodotto cartesiano** dei domini di $h$ e $g$:

$$\text{dom}(f): \big[(-\infty, 0) \cup(0, +\infty)\big]\times\mathbb R$$

Analizziamo ora l'**equazione logistica**: $y'(t) = ky(t)-hy^2(t)$. Questa si divide:

$$\begin{cases}
h(t) = 1, &J_1 = \mathbb R\\\
g(y) = ky-hy^2, &J_2 = \mathbb R
\end{cases}$$

Quest'equazione differenziale è definita in $\mathbb R\times\mathbb R = \mathbb R^2$.

Per trovare le **soluzioni costanti** di un'equazione differenziale ordinaria a variabili separabili, è necessario trovare una costante $c\in\mathbb R|h(t)g(c)=0, \ \forall t \iff g(c)=0$.

### Problema di Cauchy per un'equazione differenziale ordinaria del primo ordine

Data, in generale, un'equazione differenziale ordinaria del primo ordine $y'(t) = f\big(t, y(t)\big)$, sia $(t_0, y_0)$ un punto in cui l'equazione è definita. Si chiama **problema di Cauchy** il problema di determinare $y:I\subseteq\mathbb R\to\mathbb R$ che soddisfa:

$$\begin{cases}
y'(t) = f\big(t,y(t)\big)\\\
y(t_0)=y_0
\end{cases}$$

per qualche intervallo $I$ con $t_0\in I$.

Nella pratica, si possono seguire tre step per determinare la soluzione al problema di Cauchy:

1. Determinare l'integrale generale dell'equazione differenziale
2. Imporre $y(t_0) = y_0$ e determinare la costante arbitraria $c\in\mathbb R$
3. Sostituire il valor della costante $c$ nell'integrale generale
- **Esempio**

Partiamo dal problema di Cauchy seguente:

$$\begin{cases}
y'(t)=ty^3(t)\\\
y(0)=1
\end{cases}$$

Seguiamo i passi descritti sopra:

1. Trovo l'integrale generale dell'equazione differenziale:
    
    $$y(t) = 0, y(t) = \pm\sqrt{{1\over-t^2+c}}, c\in\mathbb R$$
    
2. Impongo la condizione $y(0) = 1$:
    
    $$y(0) = \sqrt{{1\over 0 + c}} \implies c = 1$$
    
3. Sostituisco $c = 1$ nell'integrale generale:
    
    $$y(t) = \sqrt{1\over-t^2+1}$$
    
### Equazioni differenziali ordinarie del primo ordine lineari

Un'equazione differenziale ordinaria del primo ordine lineare ha forma:

$$y'(t)+a(t)y(t)=b(t)$$

con $a, b:J\subseteq\mathbb R\to\mathbb R$ continue su $J$.

Chiamiamo equazione differenziale ordinaria **omogenea associata** l'equazione di forma:

$$y'(t) + a(t)y(t) = 0$$

- **Esempi**

Alcune equazioni differenziali ordinarie del primo ordine lineari sono:

- $y'(t)-\sqrt{t}y(t) = 0,\ a(t) = -\sqrt{t}$ (equazione omogenea, poiché $b(t) = 0$)
- $y'(t) + e^ty(t) = \cos t, \ a(t) = e^t,\ b(t) = \cos t$

L'insieme $J\subseteq\mathbb R$ è **il più grande intervallo** su cui sono definite $a$ e $b$.

#### Formula risolutiva

Date $a, b: J\subseteq\mathbb R\to\mathbb R$ continue, consideriamo $y'(t)+a(t)y(t) = b(t)$.

L'integrale generale dell'equazione differenziale lineare è dato dalla formula:

$$y(t) = e^{-\mathscr{A}(t)}\big[\mathscr{B}(t)+c\big], \ \forall t\in J$$

dove:

$$\begin{cases}
\mathscr{A}(t) = \int{a(t)dt}\\\
\mathscr{B}(t) = \int{e^{\mathscr{A}(t)}\cdot b(t)dt}
\end{cases}$$

- **Dimostrazione 1**

Partendo dall'equazione differenziale lineare $y'+ay=b$, moltiplico ambo i membri per $e^\mathscr A$:

$$\underbrace{y'e^\mathscr A+aye^\mathscr A}_{(ye^\mathscr A)'} = be^\mathscr A$$

Vale l'equivalenza scritta sopra poiché:

$$\begin{aligned}
\big(ye^\mathscr A\big)' &= y'e^\mathscr A + y\big(e^\mathscr A\big)' = \\\
&=y'e^\mathscr A+y\mathscr A'e^\mathscr A = \\\
&= y'e^\mathscr A+yae^\mathscr A
\end{aligned}$$

Si ottiene quindi l'equazione $\big(ye^\mathscr A\big)' = be^\mathscr A$. Ora, integrando a destra ed a sinistra tra $t_0$ e $t$, posto $t_0<t, t, t_0\in J$:

$$\begin{aligned}
\int_{t_0}^t\big[y(x)e^{\mathscr{A}(x)}\big]'dx &= \underbrace{\int_{t_0}^tb(x)e^{\mathscr A(x)}dx}_{\mathscr B(t)}\\\
y(t)e^{\mathscr A(t)}\underbrace{-y(t_0)e^{\mathscr A(t_0)}}_c &= \mathscr B(t)\\\
y(t)e^{\mathscr A(t)} &= \mathscr B(t)+c\\\
y(t) &= e^{-\mathscr A(t)}\big[\mathscr B(t)+c\big]\ _\blacksquare
\end{aligned}$$

Le soluzioni risultano definite su tutto $J$, cosa che non accade nelle equazioni differenziali non lineari.

### Equazioni di Bernoulli

Si chiamano **equazioni di Bernoulli** le equazioni differenziali ordinarie del primo ordine non lineari del tipo:

$$y'(t) = f(t)y(t)+g(t)y^\alpha(t), \alpha\in\mathbb R, \alpha\ne0,1$$

con $f,g:J\to\mathbb R$ continue.

Per risolvere questo tipo di equazioni, si procede in quattro step:

1. Ricerca delle soluzioni costanti:
    
    $$fy+gy^\alpha=0, \ \forall t\in J$$
    
2. Divisione dell'equazione differenziale per $y^\alpha$:
    
    $${y'(t)\over y^\alpha(t)} = {f(t)\over y^{\alpha-1}(t)} + g(t)$$
    
    Si può ricondurre il primo membro dell'equazione all'espressione $y^{-\alpha}(t)y'(t)$, che è pari a:
    
    $$\bigg({y^{-\alpha + 1}(t)\over-\alpha +1}\bigg)'$$
    
    Perciò si può scrivere:
    
    $${1\over 1-\alpha}\bigg[{1\over y^{\alpha - 1}(t)}\bigg]'=f(t){1\over y^{\alpha-1}(t)}+g(t)$$
    
    Facendo un cambio di variabile tale che $z(t) = 1/y^{\alpha-1}(t)$:
    
    $$z'(t) = (1-\alpha)f(t)z(t)+(1-\alpha)g(t)$$
    
    Si vede facilmente che l'equazione differenziale in $z$ è lineare.
    
3. Risoluzione dell'equazione differenziale in $z$
4. Ritorno alla variabile $y(t) = 1/z^{1/\alpha - 1}(t)$

---

## Equazioni differenziali del secondo ordine lineari

Un'**equazione differenziale del secondo ordine lineare** è un'equazione differenziale ordinaria nella forma:

$$a(t)y''(t)+b(t)y'(t)+c(t)y(t)=f(t)$$

Dove $a, b, c, f$ sono continue in $J$ e la funzione $a$ non è nulla.

Le soluzioni delle equazioni differenziali di secondo grado sono $\infty^2$.

### Problema di Cauchy

Il **problema di Cauchy** per un'equazione differenziale del secondo ordine lineare è così definito:

$$\begin{cases}
a(t)y''(t)+b(t)y'(t)+c(t)y(t)=f(t)\\\
y(t_0)=y_0\\\
y'(t_0) = v_0
\end{cases}$$

Dove $y(t_0)=y_0$ rappresenta la condizione iniziale rispetto alla funzione non derivata, mentre $y'(t_0)=v_0$ rappresenta la condizione iniziale rispetto alla funzione derivata al grado 1.

L'esistenza di una ed una sola soluzione è confermata dal **teorema di Cauchy per le equazioni differenziali ordinare del secondo ordine**:

Se $a,b,c,f$ sono funzioni continue in $J$, allora $\forall t_0\in J$ e $\forall(y_0,v_0)\in \mathbb{R}^2$, il sistema:

$$\begin{cases}
a(t)y''(t)+b(t)y'(t)+c(t)y(t)=f(t)\\\
y(t_0)=y_0\\\
y'(t_0) = v_0
\end{cases}$$

ha **una ed una sola soluzione** definita su tutto l'intervallo $J$.

Le conseguenze del teorema di Cauchy sono:

1. La soluzione dell'equazione differenziale **esiste sempre**, poiché $a,b,c,f$ sono continue
2. La soluzione dell'equazione differenziale **è unica**, poiché $g(t,y,v)=f(t)-b(t)y-c(t)v$ è lineare in $y,v$ e quindi derivabile
3. La soluzione dell'equazione differenziale **è definita su tutto $J$**, poiché l'equazione è lineare

### Principio di sovrapposizione degli effetti

Se $y_1$ è una soluzione dell'equazione differenziale $ay''+by'+cy=f_1$ e $y_2$ è una soluzione dell'equazione differenziale $ay''+by'+cy=f_2$, allora la funzione:

$$y(t) = c_1y_1(t)+c_2y_2(t)$$

è soluzione dell'equazione differenziale:

$$ay''+by'+cy=c_1f_1+c_2f_2$$

- **Dimostrazione 2**

Dal principio di sovrapposizione degli effetti, le soluzioni formano uno spazio vettoriale.

Per dimostrare che è di dimensione 2, devo:

1. Determinare due soluzioni linearmente indipendenti: $y_{01}(t), y_{02}(t)$
2. Dimostrare che ogni soluzione si scrive come combinazione lineare di $y_{01}(t), y_{02}(t)$

Scelgo $y_{01}$ come soluzione del problema di Cauchy:

$$\begin{cases}
ay''+by'+cy=0\\\
y(0)=1\\\
y'(0)=0
\end{cases}$$

$y_{02}$ risolve invece:

$$\begin{cases}
ay''+by'+cy=0\\\
y(0)=0\\\
y'(0)=1
\end{cases}$$

Per dimostrare che queste due soluzioni sono linearmente indipendenti, suppongo per assurdo che non lo siano:

$$y_{01}=cy_{02}, \forall t\in \mathbb R$$

Ponendo $t=0$, ottengo:

$$\begin{aligned}
y_{01}(0)&= cy_{02}(0)\\\
1 &= 0 \text{ Assurdo}
\end{aligned}$$

Sia ora $y_0$ una soluzione dell'equazione differenziale. Cerco $c_1,c_2\in\mathbb R:y_0(t) = c_1y_1(t) + c_2y_2(t)$:

$$\begin{cases}
y_0(0) = c_1\overbrace{y_{01}(0)}^{1} + c_2\overbrace{y_{02}(0)}^{0} = c_1\\\
y_o'(0) = c_1\underbrace{y_{01}'(0)}_{0} + c_2\underbrace{y_{02}(0)}_{1} = c_2
\end{cases}$$

cioè $y_0(0) = c_1$ e $y_0'(0) = c_2 \ _\blacksquare$

L'integrale generale di un'equazione differenziale ordinaria lineare omogenea del primo ordine è uno spazio vettoriale di dimensione 1.

### Integrale generale di un'equazione differenziale ordinaria del secondo grado omogenea

#### Teorema di struttura per equazioni differenziali di secondo grado omogenee

L'integrale generale dell'equazione differenziale di secondo grado omogenea:

$$ay''+by'+cy=0$$

dove $a,b,c$ sono funzioni continue in $J$, è dato da **tutte le combinazioni lineari**:

$$y(t)=c_1y_1(t)+c_2y_2(t), \forall c_1,c_2\in\mathbb R$$

dove $y_1,y_2$ sono **due soluzioni linearmente indipendenti** dell'equazione stessa.

### Integrale generale di un'equazione differenziale ordinaria del secondo grado completa

#### Teorema di struttura per equazioni differenziali di secondo grado complete

L'integrale generale dell'equazione differenziale di secondo grado completa:

$$ay''+by'+cy=f$$

con $a,b,c,f$ funzioni continue in $J$, è dato da **tutte e sole le funzioni**:

$$y(t) = c_1y_1(t) + c_2y_2(t) + y_P(t), \forall c_1,c_2\in\mathbb R$$

dove:

1. $y_1,y_2$ sono soluzioni dell'equazione omogenea associata
2. $y_P$ è una soluzione particolare dell'equazione completa

Le funzioni $y,y'\in \mathbb R$ poiché, posta $a(t)y''(t) = g\big(t, y(t),y'(t)\big)$, elimino la dipendenza da $t$ in $y(t), y'(t)$:

$$g(t,y,z) = f(t)-c(t)y-b(t)z$$

dove $g$ è una funzione di tre variabili definita in un sottoinsieme di $\mathbb R^3$.

Dato che $t\in J, y\in\mathbb R, z\in\mathbb R$, allora $(t,y,z)\in J\times\mathbb R\times\mathbb R$, perciò l'equazione differenziale è definita in $(t,y,z)\in J\times\mathbb R\times\mathbb R \subseteq \mathbb R^3$.

### Equazione omogenea a coefficienti costanti

Consideriamo l'equazione differenziale ordinaria di secondo ordine $ay'' + by' + cy = 0$, con $a, b, c\in\mathbb R$ e $a\ne 0$.

Vogliamo determinare l'integrale generale di questa equazione differenziale omogenea.

Dal teorema di struttura, sappiamo che basta trovare due soluzioni linearmente indipendenti.

Il procedimento generale per trovare la soluzione di questa equazione è il seguente:

1. Si pone $y(t) =e^{\lambda t}$
2. Si sostituisce nel testo dell'equazione: $a\lambda^2e^{\lambda t} + b\lambda e^{\lambda t} + ce^{\lambda t} = 0$
3. Si raccoglie $e^{\lambda t}$ e si semplifica, dato che $e^{\lambda t} \neq 0\  \forall t \in \mathbb R$: $a\lambda^2 + b\lambda + c = 0$
4. $y(t)$ è soluzione dell'equazione differenziale se e solo se $P(\lambda) = a\lambda^2 +b\lambda +c = 0$

La natura delle radici di $P(\lambda)$ e, di conseguenza, delle soluzioni dell'equazione differenziale, dipende dal suo $\Delta$:

- Se $\Delta > 0$
    
    $P(\lambda)$ ha due radici reali distinte, perciò esistono due soluzioni linearmente indipendenti dell'equazione differenziale.
    
    Per il teorema di struttura:
    
    $$y(t) = c_1e^{\lambda_1 t}+c_2e^{\lambda_2 t}, c_1,c_2\in\mathbb R$$
    
- Se $\Delta = 0$
    
    $P(\lambda)$ ha due radici reali coincidenti, perciò l'equazione differenziale ha una soluzione che si trova attraverso $P(\lambda)$ e un'altra pari a $te^{\lambda t}$.
    
    Per il teorema di struttura:
    
    $$y(t) = e^{\lambda t}(c_1+tc_2), c_1,c_2\in\mathbb R$$
    
- Se $\Delta < 0$
    
    $P(\lambda)$ ha due soluzioni complesse coniugate, perciò esistono due soluzioni linearmente indipendenti dell'equazione differenziale, che si ricavano applicando la formula di Eulero alle radici di $P(\lambda)$.
    
    Poste le due radici di $P(\lambda)$:
    
    1. $\lambda_1 = \alpha + i\beta$
    2. $\lambda_2 = \alpha - i\beta$
    
    Trovo le due soluzioni:
    
    1. $y_1(t) = e^{(\alpha + i\beta)t}$
    2. $y_1(t) = e^{(\alpha - i\beta)t}$
    Trasformiamo le precedenti espressioni tramite la formula di Eulero:
    
    1. $y_1(t) = e^{\alpha t}\cos(\beta t)$
    2. $y_2(t) = e^{\alpha t}\sin(\beta t)$
    
    Per il teorema di struttura:
    
    $$y(t) = e^{\alpha t}\big[c_1\cos(\beta t) + c_2\sin(\beta t)\big], c_1,c_2\in\mathbb R$$
