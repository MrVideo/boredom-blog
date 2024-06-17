---
title: 'Funzioni di $n$ variabili'
draft: false
type: 'page'
toc: true
mathjax: true
---

---

## Cenni di topologia in $\mathbb R^n$

### Palle


Si definisce una **palla in $\mathbb R^n$** come segue:

$$B_r(\underline{x_0}) = \{x\in\mathbb R^n:||\underline x-\underline{x_0}||<r\}$$



### Punti interni, esterni e di frontiera


Dato un insieme $E\subseteq\mathbb R^n$, classifichiamo i punti di $\mathbb R^n$ relativamente ad $E$ come segue:

- $\underline x$ è un **punto di frontiera** (o bordo) per $E$ se $\forall r>0, B_r(\underline x)\cap E\ne\varnothing$ e $B_r(\underline x)\cap E^\complement\ne\varnothing$, dove $E^\complement=\mathbb R^n\setminus E$.
- $\underline x$ è un **punto interno** ad $E$ se non solo $\underline x\in E$, ma anche $\exists r>0:B_r(\underline x)\subseteq E$.
- $\underline x$ è un **punto esterno** ad $E$ se non solo $\underline x \notin E$, ma anche $\exists r>0:B_r(\underline x)\subseteq E^\complement$.



I punti di frontiera possono appartenere ad $E$ o meno.



### Insiemi aperti e chiusi


Dato $E\subseteq\mathbb R^n$, $E$ si dice **aperto** se tutti i punti di $E$ sono interni ad $E$.




Dato $E\subseteq\mathbb R^n$, $E$ si dice **chiuso** se $E^\complement$ è aperto.



In particolare, $\mathbb R^n$ è **sia aperto che chiuso**.

### Insiemi limitati ed illimitati


Un sottoinsieme di $\mathbb R^n$ è detto **limitato** se esiste $R>0:E\subset B_R(0)$. Altrimenti, $E$ si dice **illimitato**.



---

## Curve

Pensiamo ad un punto che si sposta in modo continuo nel piano, lasciando una traccia. La traccia lasciata dal punto è il **sostegno di una curva piana**.

La posizione del punto al tempo $t$ può essere descritta da due funzioni:

- $r_1(t)$, che descrive come cambia $x_1$, la prima coordinata del punto
- $r_2(t)$, che descrive come cambia $x_2$, la seconda coordinata del punto

Le funzioni $r_1, r_2$ costituiscono la **parametrizzazione** della curva.

Similmente, la traccia lasciata da un punto che si sposta in modo continuo nello spazio $\mathbb R^3$ è il **sostegno di una curva nello spazio**. La posizione del punto, in questo caso, è descritta da tre funzioni:

- $r_1(t)$ per la coordinata $x_1$
- $r_2(t)$ per la coordinata $x_2$
- $r_3(t)$ per la coordinata $x_3$

Una curva piana è un caso particolare di curva nello spazio, avente $r_3(t) = 0, \forall t$.


Una curva nello spazio è definita da:

1. Tre funzioni continue:
    
    $$t\in I\subseteq\mathbb R\to\underline{r}(t)=\begin{pmatrix}
    r_1(t)\\\
    r_2(t)\\\
    r_3(t)
    \end{pmatrix}\in\mathbb R^3$$
    
    dove $\underline r(t)$ indica la **parametrizzazione** della curva.
    
2. L’immagine dell’intervallo $I$ tramite le tre funzioni $r_1,r_2,r_3$:
    
    $$\gamma=\{(x_1,x_2,x_3)\in\mathbb R^3:(x_1, x_2, x_3)=\big(r_1(t), r_2(t), r_3(t)\big) \text{ per qualche } t\in I\}$$
    
    $\gamma$ è detto **sostegno** della curva.
    



Come caso particolare, quando $r_3(t)=0 \ \forall t\in I$, otteniamo una curva nel piano $(x,y)$.




L’intervallo $I$ può essere aperto, chiuso, né aperto né chiuso, limitato o illimitato. Può anche essere tutto $\mathbb R$.



### Parametrizzazioni equivalenti


Sia data la curva con sostegno $\gamma$ e parametrizzazione $\underline r(t):I\subseteq\mathbb R\to\mathbb R^3$ e sia $f:J\to I$ una funzione continua e biunivoca.

Una parametrizzazione equivalente è $\underline v(s)=\underline r\big(f(s)\big) = \underline r\circ f(s):J\to\mathbb R^3$.



### Curve regolari


$f:I\to\mathbb R$ si dice di classe $C^1(I)$ se è derivabile con continuità in $I$ una volta.




Una curva piana si dice **regolare** se ammette una parametrizzazione $\underline r(t)=\big(r_1(t), r_2(t)\big)$, con $t\in I$, che verifica le seguenti proprietà:

1. $r_1, r_2$ sono funzioni di classe $C^1(I)$
2. Il vettore derivato non è mai il vettore nullo:
    
    $$\underline{r'}\big(r_1'(t), r_2'(t)\big) \ne (0,0), \forall t\in I$$
    



Una curva nello spazio si dice **regolare** se ammette una parametrizzazione $\underline r(t)=\big(r_1(t), r_2(t),r_3(t)\big)$, con $t\in I$, che verifica le seguenti proprietà:

1. $r_1, r_2, r_3$ sono funzioni di classe $C^1(I)$
2. Il vettore derivato non è mai il vettore nullo:
    
    $$\underline{r'}\big(r_1'(t), r_2'(t), r_3'(t)\big) \ne (0,0,0), \forall t\in I$$
    



Alcune componenti di $\underline{r'}$ possono annullarsi, ma non tutte e tre contemporaneamente. In particolare:

$$||\underline{r'}(t)|| = \sqrt{\big[r_1'(t)\big]^2 + \big[r_2'(t)\big]^2 + \big[r_3'(t)\big]^2} \ne 0, \forall t$$

Va notato che il problema si ha soltanto in $t=0$. Se si considera un tratto di curva che non include $t=0$, allora quel tratto è regolare.



### Classe di curve regolari

Sia $f:I\to\mathbb R$ una funzione e sia $f\in C^1(I)$. Allora il suo grafico è il sostegno di una curva piana regolare:

$$\begin{aligned}
\underline r(t) &= \big(t, f(t)\big), t\in I\\\
\underline{r'}(t) &= \big(1, f'(t)\big)
\end{aligned}$$


Sia $\underline r:I\to\mathbb R^3$ una curva regolare.

Per ogni $t\in I$ è definito il versore tangente:

$$\underline T(t) = {\underline{r'}(t)\over||\underline{r'}(t)||}$$

Più esplicitamente:

$$\underline T(t) = \begin{pmatrix}
{r'_1(t)\over\sqrt{\big[r_1'(t)\big]^2 + \big[r_2'(t)\big]^2 + \big[r_3'(t)\big]^2}}\\\
{r'_2(t)\over\sqrt{\big[r_1'(t)\big]^2 + \big[r_2'(t)\big]^2 + \big[r_3'(t)\big]^2}}\\\
{r'_3(t)\over\sqrt{\big[r_1'(t)\big]^2 + \big[r_2'(t)\big]^2 + \big[r_3'(t)\big]^2}}
\end{pmatrix}$$



### Lunghezza di una curva


**Lunghezza di una curva regolare**

Sia $[a,b]\subseteq\mathbb R$ un intervallo limitato.

Sia $\underline r:[a,b]\to\mathbb R^n$ la parametrizzazione di una curva regolare $\gamma$. Allora:

$$\text{lunghezza}(\gamma) = \int_a^b||\underline{r'}(t)||dt$$




**Invarianza della lunghezza di una curva per riparametrizzazione**

Sia $\underline r:[a,b]\to\mathbb R^3$ la parametrizzazione regolare di una curva di sostegno $\gamma$.

Sia $f:[c,d]\to[a,b]$ una funzione derivabile e biunivoca.

Formuliamo la parametrizzazione equivalente $\underline v(s)$:

$$\underline v(s)=\underline r\big(f(s)\big) =\underline r \circ f(s):[c,d]\to\mathbb R^3$$

Sia $\delta$ il sostegno della nuova curva di parametrizzazione $\underline v$. Allora:

$$\text{lunghezza}(\gamma)=\text{lunghezza}(\delta)$$



- **Dimostrazione 10**
    
    Sappiamo che:
    
    $$\begin{aligned}
    \text{lunghezza}(\gamma)&=\int_a^b||\underline{r'}(t)||dt\\\
    \text{lunghezza}(\delta)&=\int_c^d||\underline{v'}(t)||dt\\\
    \end{aligned}$$
    
    Troviamo la norma del vettore derivato $\underline{v'}(t)$:
    
    $$\underline{v'} = \begin{pmatrix}r_1'\big(f(s)\big)f'(s)\\\r_2'\big(f(s)\big)f'(s)\end{pmatrix}$$
    
    $$\begin{aligned}
    ||\underline{v'}(s)|| &= \sqrt{\big[r_1'\big(f(s)\big)f'(s)\big]^2 + \big[r_2'\big(f(s)\big)f'(s)\big]^2} = \\\
    &= |f'(s)|\sqrt{\big[r_1'\big(f(s)\big)\big]^2 + \big[r_2'\big(f(s)\big)\big]^2} = \\\
    &= |f'(s)|\cdot||\underline{r'}\big(f(s)\big)||
    \end{aligned} $$
    
    Allora possiamo riscrivere:
    
    $$\text{lunghezza}(\delta) = \int_c^d|f'(s)|\cdot||\underline{r'}\big(f(s)\big)||ds$$
    
    Effettuiamo un cambio di variabile:
    
    $$\begin{cases}
    t = f(s)\\\ dt = f'(s)ds
    \end{cases}$$
    
    Dato che $f$ è biunivoca, essa è sempre crescente o decrescente. Supponiamo che $f'(s)\ge0, \forall s\in [c,d]$. Allora:
    
    $$\begin{aligned}
    \text{lunghezza}(\delta) &= \int_c^df'(s)\cdot||\underline{r'}\big(f(s)\big)||ds = \\\
    &= \int_a^b||\underline{r'}(t)||dt = \\\&=\text{lunghezza}(\gamma)\ _\blacksquare
    \end{aligned}$$
    

### Curve regolari a tratti


Si dice **regolare a tratti** una curva $\underline r:I\subseteq \mathbb R\to\mathbb R^3$ tale che:

1. $\underline r$ è continua in $I$
2. Ad eccezione di un numero finito di valori $t_1, ..., t_k$, la curva è regolare


La lunghezza di può calcolare anche per curve regolari a tratti.

### Integrale curvilineo


Sia $\underline r:[a,b]\to\mathbb R^3$ la parametrizzazione regolare di una curva di sostegno $\gamma$.

Sia $f:A\subseteq\mathbb R^3\to\mathbb R$ una funzione continua.

Si supponga $\gamma\subseteq A$.

L’integrale curvilineo di $f$ lungo $\gamma$ è:

$$\int_\gamma fds=\int_a^bf\big(\underline r(t)\big)||\underline{r'}(t)||dt$$



---

## Funzioni di due variabili


Sia $A\subseteq\mathbb R^2$.

Una funzione di due variabili a valori reali $f:A\to\mathbb R$ è una relazione che associa ad ogni $(x,y)\in A$ un unico valore reale:

$$\begin{aligned}
A\subseteq\mathbb R^2&\to\mathbb R\\\
(x,y)&\mapsto f(x,y)
\end{aligned}$$

$A$ è detto **insieme di definizione** o **dominio** della funzione.

Il grafico di $f$ è definito come segue:

$$\text{grafico}(f)=\{(x,y,z)\in\mathbb R^3:(x,y)\in A, z=f(x,y)\}\subseteq\mathbb R^3$$

Per ogni $k\in\mathbb R$, l’**insieme di livello** di $f$ al livello $k$ è:

$$I_k=\{(x,y)\in A\subseteq\mathbb R^2:z=f(x,y)=k\}\subseteq\mathbb R^2$$



### Limiti bidimensionali


Siano $A\subseteq\mathbb R^2$ aperto, $\underline{x_0}\in A$ e $f:A\to\mathbb R$.

Diciamo che $f$ tende al limite $l\in\mathbb R$ per $\underline x$ che tende a $\underline{x_0}$ e scriviamo:

$$\lim_{\underline x\to\underline{x_0}}f(x) = l$$

se $\forall\epsilon>0, \exists\delta>0:x\in B_\delta(\underline{x_0})\setminus\{\underline{x_0}\}\implies|f(x)-l|<\epsilon$.



Parafrasando, per ogni $\epsilon>0$ esiste una palla $B_\delta(\underline{x_0})$ contenuta nel piano $(x,y)$ tale che l’immagine tramite $f$ di $B_\delta(\underline{x_0})\setminus\{\underline{x_0}\}$ sia tutta contenuta nell’intervallo $(l-\epsilon,l+\epsilon)$ sull’asse $z$.


Si noti che:

$$\begin{aligned}
\underline x\in B_\delta(\underline{x_0})\setminus\{\underline{x_0}\}\iff&0<\text{distanza}(\underline x, \underline{x_0})<\delta\\\
&0<||\underline x-\underline{x_0}||<\delta\\\
&0<\sqrt{(x-x_0)^2+(y-y_0)^2}<\delta
\end{aligned}$$

Si esclude $\underline{x_0}$ perché modificando $f(\underline{x_0})=f(0)$, per esempio, il limite rimane comunque $l$. Il centro della palla è quindi ininfluente nel calcolo del limite.



La differenza dei limiti in $\mathbb R^2$ da quelli in $\mathbb R$ è che nel piano ci si può avvicinare ad un punto in infinite direzioni.

#### Esempi

- Esempio 1
    
    Calcoliamo il limite:
    
    $$\lim_{(x,y)\to(0,0)}{x^2-y^2\over x^2+y^2}$$
    
    Proviamo ad avvicinarci all’origine del piano lungo l’asse $x$, di equazione $y=0$:
    
    $$\lim_{x\to0}f(x,0) = \lim_{x\to0}{x^2\over x^2} =1$$
    
    Ora avviciniamoci all’origine lungo l’asse $y$, di equazione $x=0$:
    
    $$\lim_{y\to0}f(0,y) = \lim_{y\to0}{-y^2\over y^2} = -1$$
    
    Poiché i limiti monodimensionali sono diversi, **il limite bidimensionale richiesto non esiste**.
    
- Esempio 2
    
    Calcoliamo il limite:
    
    $$\lim_{(x,y)\to(0,0)}{x\sqrt{|y|}\over x^2+3y}$$
    
    1. $f$ ristretta all’asse $y$: $f(0,y) = 0\implies\lim_{y\to0}f(0,y)=0$
    2. $f$ ristretta all’asse $x$: $f(x,0) = 0\implies \lim_{x\to0}f(x,0)=0$
    3. È possibile verificare che, posta $y=mx$ ogni retta del piano: $\lim_{x\to0}f(x, mx)=0$
    4. $f$ ristretta alla parabola $y=x^2$:
        
        $$\begin{aligned}
        \lim_{x\to0}f(x, x^2) &= \lim_{x\to0}{x\sqrt{|x^2|}\over x^2+3x^2} =\\\
        &=\lim_{x\to0}{|x|\over4x} = \\\
        &= \pm{1\over4} \implies \text{non esiste}
        \end{aligned}$$
        
    
    Quindi il limite bidimensionale richiesto non esiste.
    

#### Calcolo dei limiti con coordinate polari

Per stabilire che un limite bidimensionale non esiste, è sufficiente esibire due cammini che si avvicinano a $\underline{x_0}$ tali che i limiti monodimensionali di $f$ ristretta ai due cammini siano diversi o non esistano. Tali cammini possono essere rette o altre curve.

Se invece il limite esiste, come dimostrarlo? Non si possono testare manualmente tutti i cammini.

Un modo può essere quello di passare alle coordinate polari.

- Esempio
    
    Calcoliamo il limite:
    
    $$\lim_{(x,y)\to(0,0)}{2x^2y\over x^2+y^2}$$
    
    Per calcolare questo limite tramite le coordinate polari, si seguono questi passi:
    
    1. Si calcolano i limiti monodimensionali lungo gli assi.
        
        Dato che la funzione è nulla lungo entrambi gli assi, il candidato limite è proprio $l=0$, cioè se il limite esiste, esso è necessariamente $0$.
        
    2. Si scrive $f$ in coordinate polari.
        
        La trasformazione avviene ponendo:
        
        $$\begin{cases}
        x = r\cos\theta\\\
        y = r\sin\theta
        \end{cases}$$
        
        Perciò trovo la funzione $g$ in coordinate polari:
        
        $$g(r,\theta) = 2r\cos^2\theta\sin\theta$$
        
    3. Si cerca una funzione $h(r)$ che dipenda solo dalla coordinata radiale $r$ tale che:
        1. $|g(r,\theta)-l|\le h(r)$
        2. $\lim_{r\to0^+}h(r) = 0$
        
        Se si trova una funzione $h$ con queste proprietà, allora il limite richiesto vale $l$.
        
        In questo caso:
        
        $$\tag{i}
        |g(r,\theta)-l| = |2r\cos^2\theta\sin\theta-0|
        = 2r|\cos^2\theta\sin\theta|\le2r=h(r)$$
        
        $$\tag{ii}\lim_{r\to0^+}h(r) = \lim_{r\to0^+} 2r = 0$$
        
        Verificate le due condizioni, possiamo concludere:
        
        $$\lim_{(x,y)\to(0,0)}f(x,y) = 0$$
        

### Continuità per funzioni di due variabili


Siano $A\subseteq\mathbb R^2$ aperto, $\underline{x_0}\in A$ e $f:A\to\mathbb R$.

Diciamo che $f$ è continua in $\underline{x_0}$ se:

$$\lim_{\underline x\to\underline{x_0}}f(\underline x)=f(\underline{x_0})$$

Diciamo che $f$ è continua in $A$ se è continua $\forall x\in A$.



#### Proprietà


Se due funzioni di due variabili $f, g$ sono continue, allora:

- $f+g,f-g,f\cdot g$ sono funzioni continue
- Se $g\ne0$, allora $f/g$ è una funzione continua
- Se $f>0$, allora $f^g$ è una funzione continua
- La funzione composta $f\circ g$ è continua


In pratica, dovremo definire la continuità solo per le funzioni definite per casi.

### Derivate parziali


Siano $A\subseteq\mathbb R^2$ aperto, $f:A\to\mathbb R$ e $(x_0,y_0)\in A$.

Le derivate parziali di $f$ in $(x_0, y_0)$ sono:

$$\begin{align*}
{\partial f\over \partial x}(x_0,y_0) &= \lim_{h\to0}{f(x_0+h,y_0)-f(x_0,y_0)\over h}\\\
{\partial f\over \partial y}(x_0,y_0) &= \lim_{h\to0}{f(x_0,y_0+h)-f(x_0,y_0)\over h}
\end{align*}$$

se i limiti esistono finiti.

Se uno dei due limiti non esiste, diciamo che $f$ non ha tale derivata parziale in $(x_0,y_0)$.

Se esistono entrambe le derivate parziali in $(x_0,y_0)$, diciamo che $f$ è derivabile in $(x_0,y_0)$. In questo caso, le due derivate parziali si organizzano in un vettore, detto **gradiente**:

$$\nabla f(x_0,y_0) = \begin{pmatrix}{\partial f\over \partial x}(x_0,y_0)\\\
{\partial f\over \partial y}(x_0,y_0)\end{pmatrix}\in\mathbb R^2$$

Se $f$ è derivabile in tutti i punti $(x,y)\in A$, diciamo che $f$ è derivabile in $A$.




Se $(x_0, y_0)$ è fissato, $\nabla f (x_0, y_0)$ è un vettore di $\mathbb R^2$.

Se $(x,y)$ è variabile, $\nabla f (x, y)$ è un vettore di funzioni.




Se $A$ è un insieme aperto, allora tutti i punti sono punti interni.



#### Calcolo delle derivate parziali

Esistono fondamentalmente tre casi per il calcolo delle derivate parziali:

1. $f$ è *costruita* a partire da funzioni monodimensionali derivabili, ossia non compaiono potenze $|x|^\alpha, 0<\alpha\le1$.
    
    In questo caso, si possono usare le regole di derivazione usuali sulle variabili $x$ e $y$.
    
2. $f$ è definita per casi
    
    In questo caso, è necessario usare la definizione di derivata parziale ai bordi degli insiemi di definizione dei casi.
    
3. $f$ non è definita per casi, ma compaiono delle funzioni monodimensionali non derivabili ovunque, come valori assoluti o $|x|^\alpha, 0<\alpha\le1$.
    
    In questo caso, potrebbe essere necessario usare la definizione di derivata parziale soltanto per una delle due derivate, a seconda di come è costruita la funzione $f$.
    

#### Significato della derivata parziale di una funzione

Cosa rappresenta, o cosa misura, la derivata parziale $\nabla f(x_0,y_0)$?

A partire dalla funzione di due variabili $f(x,y)$, costruisco una funzione di una variabile:

$$g(x) = f(x,y_0), y_0\text{ fissato}$$

Possiamo dire che $g$ è la restrizione di $f(x,y)$ alla retta $y=y_0$. Dato che $y$ è fissato, $g$ è una funzione della sola variabile $x$. Allora:

$${\partial f\over\partial x}(x_0,y_0)=g'(x_0)$$

Verifico:

$$\begin{align*}
g'(x_0) &= \lim_{h\to0}{g(x_0+h)-g(x_0)\over h} = \\\
&= \lim_{h\to0}{f(x_0+h,y_0)-f(x_0,y_0)\over h} \triangleq\\\
&\triangleq {\partial f\over\partial x}(x_0,y_0)
\end{align*}$$

#### Derivata direzionale


Siano $A\subseteq\mathbb R^2$ aperto, $f:A\to\mathbb R$ e $(x_0,y_0)\in A$.

Sia poi $\underline v\in\mathbb R^2$ un vettore di norma unitaria, cioè:

$$\begin{cases}
\underline v = \begin{pmatrix}v_1\\\v_2\end{pmatrix}\\\
||\underline v|| = \sqrt{v_1^2+v_2^2} = 1
\end{cases}$$

La **derivata direzionale** di $f$ in $(x_0,y_0)$ nella direzione individuata da $\underline v$ è:

$${\partial f\over\partial\underline v}(x_0,y_0) = \lim_{t\to0}{f(x_0+tv_1, y_0+tv_2)-f(x_0,y_0)\over t}$$

purché tale limite esista finito.




Alcune osservazioni:

- La definizione di derivata direzionale è un limite monodimensionale, non bidimensionale
- $\displaystyle \underline v=\begin{pmatrix}1\\\0\end{pmatrix}\implies{\partial f\over\partial\underline v}(x_0,y_0) = {\partial f\over\partial x}(x_0,y_0)$
- $\displaystyle \underline v=\begin{pmatrix}0\\\1\end{pmatrix}\implies{\partial f\over\partial\underline v}(x_0,y_0) = {\partial f\over\partial y}(x_0,y_0)$
- Non vediamo esempi di calcolo della derivata direzionale tramite la definizione perché per calcolarla si userà la *formula del gradiente*, che vedremo più avanti.


### Differenziabilità

Per capire il concetto di differenziabilità, dobbiamo richiamare un concetto di Analisi I: lo sviluppo di Taylor all’ordine 1 con resto secondo Peano: se $f$ è derivabile in $x_0$, allora:

$$f(x_0+h) = f(x_0) + f'(x_0)h +R(h), R(h) = o(|h|), \text{cioè} \lim_{h\to0}{R(h)\over|h|}=0$$

Ponendo $x=x_0+h$, riscriviamo in modo equivalente:

$$f(x) = f(x_0) + f'(x_0)(x-x_0) + o(|x-x_0|)$$

Per le funzioni di due variabili, la derivabilità non è sufficiente ad assicurare lo sviluppo di Taylor. Introduciamo quindi la differenziabilità:


Siano $A\subseteq\mathbb R^2$ aperto e $f:A\to\mathbb R$.

Diciamo che $f$ è **differenziabile** in $\underline{x_0}=(x_0,y_0)\in A$ se:

1. $f$ è derivabile in $\underline {x_0}$
2. $\displaystyle f(\underline{x_0}+\underline{h})=f(\underline{x_0})+<\nabla f(\underline{x_0}),\underline h>+R(\underline h), \ R(h) = o(||\underline h||), \text{cioè}\lim_{\underline h\to\underline0}{R(\underline h)\over ||\underline h||}= 0$



Riscriviamo esplicitando le componenti:

$$\underline{x_0}+\underline h = \begin{pmatrix}
x_0\\\
y_0
\end{pmatrix}+\begin{pmatrix}
h_1\\\
h_2
\end{pmatrix} = \begin{pmatrix}
x_0+h_1\\\
y_0+h_2
\end{pmatrix}\to f(\underline{x_0}+\underline h)=f(x_0+h_1, y_0+h_2)$$

$$\begin{align*}
\langle\nabla f(\underline{x_0}), \underline h\rangle &= \langle\begin{pmatrix}{\partial f \over \partial x}(\underline{x_0})\\\
{\partial f \over \partial y}(\underline{x_0})\end{pmatrix}, \begin{pmatrix}h_1\\\
h_2\end{pmatrix}\rangle = \\\
&= {\partial f\over\partial x}(\underline{x_0})h_1 + {\partial f\over\partial y}(\underline{x_0})h_2 = \\\
&= {\partial f\over\partial x}(x_0, y_0)h_1+{\partial f\over\partial y}(x_0,y_0)h_2
\end{align*}$$

$$f(x_0+h_1, y_0+h_2)=f(x_0, y_0)+ {\partial f\over\partial x} (x_0, y_0) h_1 + {\partial f\over\partial y} (x_0,y_0) h_2 + R (\underline h)\\\
\text{con } \lim_{\underline h\to0}{R(\underline h)\over||\underline h||} = \lim_{(h_1,h_2)\to(0,0)}{R(h_1,h_2)\over\sqrt{h_1^2+h_2^2}}=0$$

Ponendo $\underline{x_0}+\underline h=\underline x$:

$$f(\underline x) = f(\underline{x_0})+<\nabla f(\underline{x_0}), \underline x-\underline{x_0}> +\  o(||\underline x-\underline{x_0}||)$$



Dobbiamo ora rispondere alle tre seguenti domande:

#### Qual è l’analogo della retta tangente per le funzioni di due variabili?


Se $f$ è differenziabile in $\underline{x_0}=(x_0,y_0)$, allora il piano tangente al grafico di $f$ nel punto $\big(x_0,y_0,f(x_0,y_0)\big)$ è:

$$\begin{align*}
z &= f(\underline{x_0}) + < \nabla f(\underline{x_0}), \underline x-\underline{x_0}> =\\\
&= f(x_0,y_0)+{\partial f\over\partial x}(x_0,y_0)(x-x_0)+{\partial f\over\partial y}(x_0,y_0)(y-y_0)
\end{align*}$$



#### Come si può stabilire se una funzione è differenziabile senza usare la definizione?


Siano $A\subseteq\mathbb R^2$ aperto e $f:A\to\mathbb R$ derivabile.

Diciamo che $f$ è di classe $C^1$ in $A$, e scriviamo $f\in C^1(A)$, se:

1. $f$ è derivabile in $A$
2. Le derivate parziali ${\partial f\over\partial x}, {\partial f\over\partial y}$ sono funzioni continue in $A$



**Teorema del differenziale totale**

Sia $A\subseteq\mathbb R^2$ aperto.

Se $f\in C^1(A)$, allora $f$ è **differenziabile in ogni punto** di $A$.




Il teorema del differenziale totale non è un *se e solo se*: esistono funzioni differenziabili che non sono $C^1$.



In pratica, se $f$ contiene valori assoluti $|x-x_0|$ o $|y-y_0|$, radici $(x-x_0)^\alpha$ o $(y-y_0)^\alpha$ con $0<\alpha<1$ o se $f$ è definita per casi, bisogna verificare la differenziabilità in $(x_0,y_0)$ tramite la definizione. In tutti gli altri casi, $f\in C^1$ e quindi, per il teorema del differenziale totale, $f$ è differenziabile.

#### Quali sono le proprietà delle funzioni differenziabili?


**La differenziabilità implica la continuità**

Siano $A\subseteq\mathbb R^2$ aperto e $f:A\to\mathbb R$ differenziabile nel punto $\underline{x_0}\in A$. Allora $f$ è continua in $\underline{x_0}$.



- Dimostrazione
    
    Bisogna dimostrare che:
    
    $$\lim_{\underline x\to\underline{x_0}}f(\underline x) = f(\underline{x_0})$$
    
    Essendo $f$ differenziabile in $\underline{x_0}$:
    
    $$f(\underline x) -f(\underline{x_0}) =\ <\nabla f(\underline{x_0}), \underline x-\underline{x_0}>+\ o(||\underline x-\underline{x_0}||)$$
    
    Quindi:
    
    $$\begin{align*}
    |f(\underline x)-f(\underline{x_0})| &= |<\nabla f(\underline{x_0}), \underline x-\underline{x_0}>+\ o(||\underline x-\underline{x_0}||)|\\\
    &\le |<\nabla f(\underline{x_0}), \underline x-\underline{x_0}>|+\ o(||\underline x-\underline{x_0}||)\\\
    &\le ||\nabla f (\underline{x_0})||\cdot||\underline x-\underline{x_0}|| + o(||\underline x-\underline{x_0}||)
    \end{align*}$$
    
    $$\lim_{\underline x\to\underline{x_0}}|f(\underline x)-f(\underline{x_0})|\le \lim_{\underline x\to\underline{x_0}}||\nabla f (\underline{x_0})||\cdot||\underline x-\underline{x_0}|| + o(||\underline x-\underline{x_0}||)=0\implies \lim_{\underline x\to\underline{x_0}}|f(\underline x)-f(\underline{x_0})|=0\ _\blacksquare$$
    


**Formula del gradiente**

Siano $A\subseteq\mathbb R^2$ aperto e $f:A\to\mathbb R$.

Supponiamo che $f$ sia differenziabile in $\underline{x_0}\in A$. Allora:

1. $f$ ammette derivata direzionale in $\underline{x_0}$ lungo qualunque direzione $\underline v\in\mathbb R^2, ||\underline v ||=1$
2. $\displaystyle {\partial f\over\partial\underline v}(\underline{x_0}) = \ <\nabla f(\underline{x_0}), \underline v>$



**Direzioni di massima e minima crescita**

Siano $A\subseteq\mathbb R^2$ aperto e $f:A\to\mathbb R$. Supponiamo:

1. $f$ differenziabile in $\underline{x_0}\in A$
2. $\nabla f(\underline{x_0})\ne(0,0)$

Allora $\forall\underline v\in\mathbb R^2, ||\underline v||=1$ si ha:

$$\bigg|{\partial f\over\partial\underline v}(\underline{x_0})\bigg|\le||\nabla f(\underline{x_0})||$$

e inoltre, detti $\underline{v_\text{max}}={\nabla f(\underline{x_0})\over||\nabla f(\underline{x_0})||}$ e $\underline{v_\text{min}}=-{\nabla f(\underline{x_0})\over||\nabla f(\underline{x_0})||}$, si ha:

$$\begin{align*}
{\partial f\over\partial\underline{v_\text{max}}}(\underline{x_0})&=||\nabla f(\underline{x_0})||,\\\
{\partial f\over\partial\underline{v_\text{min}}}(\underline{x_0})&=-||\nabla f(\underline{x_0})||
\end{align*}$$



- **Dimostrazione 12**
    
    Sia $\underline v\in\mathbb R^2$ un vettore di norma unitaria.
    
    Poiché $f$ è differenziabile in $\underline{x_0}$, vale la formula del gradiente:
    
    $$\begin{align*}
    {\partial f\over\partial\underline v}(\underline{x_0}) &= \ <\nabla f(\underline{x_0}), \underline v>\\\
    \bigg|{\partial f\over\partial\underline v}(\underline{x_0})\bigg| &= |<\nabla f(\underline{x_0}), \underline v>|\\\
    &\le||\nabla f(\underline{x_0})||\cdot\underbrace{\cancel{||\underline v||}}_1 = ||\nabla f(\underline{x_0})||
    \end{align*}$$
    
    Adesso si verificano le identità per $\underline{v_\text{max}}, \underline{v_\text{min}}$:
    
    $$\begin{align*}
    {\partial f\over\partial\underline{v_\text{max}}}(\underline{x_0}) &=\ <\nabla f(\underline{x_0}),\underline{v_\text{max}}>\ =\\\
    &=\ <\nabla f(\underline{x_0}),{\nabla f(\underline{x_0})\over||\nabla f(\underline{x_0})||}>\ =\\\
    &={1\over||\nabla f(\underline{x_0})||}\cdot<\nabla f(\underline{x_0}),\nabla f(\underline{x_0})>\ =\\\
    &={||\nabla f(\underline{x_0})||^2\over||\nabla f(\underline{x_0})||}=\\\
    &= ||\nabla f(\underline{x_0})||
    \end{align*}$$
    
    Analogamente con $\underline{v_\text{min}}$, con segno negativo$_\blacksquare$
    
- Spiegazione euristica
    
    ${\partial f\over\partial\underline v}(\underline{x_0})$ è:
    
    - massima nella direzione $\underline{v_\text{max}}={\nabla f(\underline{x_0})\over||\nabla f(\underline{x_0})||}$
    - minima nella direzione $\underline{v_\text{min}}=-{\nabla f(\underline{x_0})\over||\nabla f(\underline{x_0})||}$
    - nulla lungo la direzione della curva di livello
    
    Inoltre, $\nabla f(\underline{x_0})$ è perpendicolare alla curva di livello.
    


**Derivazione di funzioni composte**

Sia $\underline r:I\subseteq\mathbb R\to A\subseteq\mathbb R^2$ la parametrizzazione regolare di una curva piana.

Sia $f:A\subseteq\mathbb R^2\to\mathbb R$ differenziabile.

Detta $F:I\to\mathbb R$ la funzione composta:

$$F(t)=(f\circ\underline r)(t) = f\big(\underline r(t)\big) = f\big(r_1(t), r_2(t)\big)$$

Allora vale:

$$F'(t) =\ <\nabla f\big(\underline r(t)\big), \underline r'(t)>$$




**Derivata direzionale come derivata della funzione composta**

Siano $A\subseteq\mathbb R^2$ aperto, $f:A\to\mathbb R$ differenziabile in $A$, $\underline{x_0}\in A$ e $\underline v\in\mathbb R^2$ con $||\underline v||=1$. Posto:

$$F(t)=f(\underline{x_0}+t\underline v),\ t\to 0$$

si ha:

$$F'(0) = {\partial f\over\partial\underline v}(\underline{x_0})$$



- **Dimostrazione 13**
    
    Si applica il teorema di derivazione della funzione composta con $\underline r(t)=\underline{x_0}+t\underline v$, per $t\to0$.
    
    $$\begin{align*}
    F(t)&=f(\underline{x_0}+t\underline v) = (f\circ\underline r)(t) = f\big(\underline r(t)\big)\\\
    F'(t) &=\ <\nabla f\big(\underline r(t)\big), \underline r'(t)>\\\
    F'(0)&=\ <\nabla f\big(\overbrace{\underline r(0)}^{\underline{x_0}}\big), \underline r'(0)>\\\
    \underline r(t)&= \begin{pmatrix}r_1(t)\\\r_2(t)\end{pmatrix} = \begin{pmatrix}x_0+tv_1\\\y_0+tv_2\end{pmatrix}\\\
    \underline r'(t)&= \begin{pmatrix}r_1'(t)\\\r_2'(t)\end{pmatrix} = \begin{pmatrix}v_1\\\v_2\end{pmatrix} = \underline v \implies \underline r'(t) = \underline r'(0) = \underline v
    \end{align*}$$
    
    Quindi, applicando la formula del gradiente:
    
    $$\begin{align*}
    F'(0) &=\ <\nabla f(\underline{x_0}), \underline v> =\\\&={\partial f\over\partial\underline v}(\underline{x_0})\ _\blacksquare
    \end{align*}$$
    


**Ortogonalità del gradiente agli insiemi di livello**

Sia $A\subseteq\mathbb R^2$ aperto e sia $f:A\to\mathbb R$ differenziabile in $A$.

Supponiamo che l’insieme di livello $I_k=\{(x,y)\in A:f(x,y)=k\}$ sia il sostegno di una curva regolare $\underline r:I\subseteq\mathbb R\to A$. Allora:

$$<\nabla f\big(\underline r(t)\big), \underline r'(t)>=0, \ \forall t\in I$$



- **Dimostrazione 14**
    
    Per ipotesi, $I_k$ coincide con il sostegno della curva $\underline r(t)$, cioè:
    
    $$I_k = \{\underline r(t):t\in I\}$$
    
    Quindi, in particolare:
    
    $$f\big(\underline r(t)\big)=k, \forall t\in I$$
    
    Chiamiamo $F:I\to\mathbb R,\ F(t)=f\big(\underline r(t)\big)$.
    
    Da un lato, $F(t)=k\ \forall t\implies F'(t)=0\ \forall t$.
    
    Dall’altro, si usa il teorema di derivazione della funzione composta:
    
    $$F'(t) =\ <\nabla f\big(\underline r(t)\big), \underline r'(t)>$$
    
    Quindi:
    
    $$<\nabla f\big(\underline r(t)\big), \underline r'(t)> = 0, \ \forall t\in I_\blacksquare$$
    


$\nabla f\big(\underline r(t)\big)$ è ortogonale solo alla specifica curva che è l’insieme di livello di $f$ passante per il punto $\underline{x_0}=\underline r(t)$.




Chiamando $\underline v = \underline r'(t)$, la formula del gradiente fornisce:

$${\partial f\over\partial\underline v}\big(\underline r(t)\big) =\ <\nabla f\big(\underline r(t)\big), \underline r'(t)>\ = 0$$

