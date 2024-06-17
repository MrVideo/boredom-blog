---
title: 'Teoremi di Analisi Matematica II'
draft: false
type: 'page'
toc: true
mathjax: true
---

---

## Formula risolutiva EDO lineari I

Date $a, b: J\subseteq \mathbb R\to\mathbb R$ continue, consideriamo $y'(t)+a(t)y(t) = b(t)$.
L'integrale generale dell'equazione differenziale lineare è dato dalla formula:

$$ y(t) = e^{-\mathscr{A}(t)}\big[\mathscr{B}(t)+c\big], \ \forall t\in J $$

dove:

$$ \begin{cases} \mathscr{A}(t) = \int{a(t)dt}\\\ \mathscr{B}(t) = \int{e^{\mathscr{A}(t)}\cdot b(t)dt} \end{cases} $$

### Dimostrazione 1
    
Partendo dall'equazione differenziale lineare $y'+ay=b$, moltiplico ambo i membri per $e^\mathscr A$:
    
$$ \underbrace{y'e^\mathscr A+aye^\mathscr A}_{(ye^\mathscr A)'} = be^\mathscr A $$
    
Vale l'equivalenza scritta sopra poiché:
    
$$ \begin{aligned} \big(ye^\mathscr A\big)' &= y'e^\mathscr A + y\big(e^\mathscr A\big)' = \\\ &=y'e^\mathscr A+y\mathscr A'e^\mathscr A = \\\ &= y'e^\mathscr A+yae^\mathscr A \end{aligned} $$
    
Si ottiene quindi l'equazione $\big(ye^\mathscr A\big)' = be^\mathscr A$. Ora, integrando a destra ed a sinistra tra $t_0$ e $t$, posto $t_0<t, t, t_0\in J$:
$$ \begin{aligned} \int_{t_0}^t\big[y(x)e^{\mathscr{A}(x)}\big]'dx &= \underbrace{\int_{t_0}^tb(x)e^{\mathscr A(x)}dx}_{\mathscr B(t)}\\\ y(t)e^{\mathscr A(t)}\underbrace{-y(t_0)e^{\mathscr A(t_0)}}_c &= \mathscr B(t)\\\ y(t)e^{\mathscr A(t)} &= \mathscr B(t)+c\\\ y(t) &= e^{-\mathscr A(t)}\big[\mathscr B(t)+c\big]\ _\blacksquare \end{aligned} $$

---
## Problema di Cauchy EDO II
Se $a,b,c,f$ sono funzioni continue in $J$, allora $\forall t_0\in J$ e $\forall(y_0,v_0)\in \mathbb{R}^2$, il sistema:

$$ \begin{cases} a(t)y''(t)+b(t)y'(t)+c(t)y(t)=f(t)\\\ y(t_0)=y_0\\\ y'(t_0) = v_0 \end{cases} $$
ha **una ed una sola soluzione** definita su tutto l'intervallo $J$.

---
## Principio di sovrapposizione degli effetti
Se $y_1$ è una soluzione dell'equazione differenziale $ay''+by'+cy=f_1$ e $y_2$ è una soluzione dell'equazione differenziale $ay''+by'+cy=f_2$, allora la funzione:

$$ y(t) = c_1y_1(t)+c_2y_2(t) $$

è soluzione dell'equazione differenziale:

$$ ay''+by'+cy=c_1f_1+c_2f_2 $$

### Dimostrazione 2
    
Dal principio di sovrapposizione degli effetti, le soluzioni formano uno spazio vettoriale.
    
Per dimostrare che è di dimensione 2, devo:
    
1.  Determinare due soluzioni linearmente indipendenti: $y_{01}(t), y_{02}(t)$
2.  Dimostrare che ogni soluzione si scrive come combinazione lineare di $y_{01}(t), y_{02}(t)$
    
Scelgo $y_{01}$ come soluzione del problema di Cauchy:
    
$$ \begin{cases} ay''+by'+cy=0\\\ y(0)=1\\\ y'(0)=0 \end{cases} $$
    
$y_{02}$ risolve invece:
    
$$ \begin{cases} ay''+by'+cy=0\\\ y(0)=0\\\ y'(0)=1 \end{cases} $$
    
Per dimostrare che queste due soluzioni sono linearmente indipendenti, suppongo per assurdo che non lo siano:
    
$$ y_{01}=cy_{02}, \forall t\in \mathbb R $$
    
Ponendo $t=0$, ottengo:
    
$$ \begin{aligned} y_{01}(0)&= cy_{02}(0)\\\ 1 &= 0 \text{ Assurdo} \end{aligned} $$
    
Sia ora $y_0$ una soluzione dell'equazione differenziale. Cerco $c_1,c_2\in\mathbb R:y_0(t) = c_1y_1(t) + c_2y_2(t)$:
    
$$ \begin{cases} y_0(0) = c_1\overbrace{y_{01}(0)}^{1} + c_2\overbrace{y_{02}(0)}^{0} = c_1\\\ y_o'(0) = c_1\underbrace{y_{01}'(0)}_{0} + c_2\underbrace{y_{02}(0)}_{1} = c_2 \end{cases} $$
    
cioè $y_0(0) = c_1$ e $y_0'(0) = c_2 \ _\blacksquare$

---
## Teorema di struttura per EDO II omogenee
L'integrale generale dell'equazione differenziale di secondo grado omogenea:

$$ ay''+by'+cy=0 $$

dove $a,b,c$ sono funzioni continue in $J$, è dato da **tutte le combinazioni lineari**:

$$ y(t)=c_1y_1(t)+c_2y_2(t), \forall c_1,c_2\in\mathbb R $$

dove $y_1,y_2$ sono **due soluzioni linearmente indipendenti** dell'equazione stessa.

---
## Teorema di struttura per EDO II complete
L'integrale generale dell'equazione differenziale di secondo grado completa:

$$ ay''+by'+cy=f $$

con $a,b,c,f$ funzioni continue in $J$, è dato da **tutte e sole le funzioni**:

$$ y(t) = c_1y_1(t) + c_2y_2(t) + y_P(t), \forall c_1,c_2\in\mathbb R $$

dove:

1.  $y_1,y_2$ sono soluzioni dell'equazione omogenea associata
2.  $y_P$ è una soluzione particolare dell'equazione completa

---
## Teorema di esistenza e unicità globale per i problemi di Cauchy per sistemi differenziali lineari
Dato il sistema differenziale lineare $\underline y'(t)=A(t)\underline y(t)+\underline b(t)$, con $A,\underline b$ continue in $J\subseteq\mathbb R$ ed assegnati $t_0\in J$ e $\underline{y_0}\in\mathbb R^n$, il problema di Cauchy:

$$ \begin{cases} \underline y'(t)=A(t)\underline y(t) + \underline b(t)\\\ \underline y(t_0) = \underline{y_0} \end{cases} $$

ha un'unica soluzione $y(t)$ definita $\forall t\in J$.

---
## Principio di sovrapposizione per sistemi differenziali lineari
Sia $A(t)\in\mathbf M_{n\times n}$ una matrice di funzioni continue.

L'operatore $\mathbf L$ tale che:

$$ \underline y \to \mathbf L\underline y = \underline y' - A(t)\cdot\underline y $$

è **lineare**, cioè se:

$$ \begin{cases} \underline y_1'=A(t)\cdot\underline y_1+\underline b_1(t)\\\ \underline y_2'=A(t)\cdot\underline y_2+\underline b_2(t) \end{cases} $$

allora vale:

$$ (c_1\underline y_1 + c_2\underline y_2)' = A(t)\cdot(c_1\underline y_1 + c_2\underline y_2)+c_1\underline b_1(t)+c_2\underline b_2(t), \forall c_1,c_2\in\mathbb R $$

Equivalentemente:

$$ \begin{cases} \mathbf L_1\underline y_1=\underline b_1(t)\\\ \mathbf L_2\underline y_2=\underline b_2(t) \end{cases} \implies\mathbf L(c_1\underline y_1+c_2\underline y_2) = c_1\underline b_1(t) + c_2\underline b_2(t), \forall c_1,c_2\in\mathbb R $$

---
## Struttura dell'integrale generale per sistemi differenziali lineari omogenei
Sia $A(t)\in\mathbf M_{n\times n}$ una matrice di funzioni continue.

L'integrale generale del sistema differenziale lineare omogeneo $\underline y'(t) = A(t)\cdot\underline y(t)$ è uno **spazio vettoriale di dimensione $n$**, cioè generato da $n$ soluzioni **linearmente indipendenti**.

---
## Determinante della matrice Wronskiana
Sia $A(t)\in\mathbf M_{n\times n}$ una matrice di funzioni continue su $J\subseteq\mathbb R$.

Dato il sistema differenziale omogeneo:

$$ \underline y'(t) = A(t)\cdot\underline y(t) $$

siano $\underline y_{01}(t), \underline y_{02}(t),...,\underline y_{0n}(t)$ $n$ soluzioni.

Le $n$ soluzioni costituiscono un **sistema fondamentale di soluzioni** se e solo se $\exists t_0\in J$ tale che:

$$ \det W(t) = \det\begin{bmatrix}\underline y_{01}(t) & \underline y_{02}(t) & ... & \underline y_{0n}(t)\end{bmatrix} \ne 0 $$

---
## Struttura dell'integrale generale per sistemi differenziali lineari non omogenei
Sia $A(t)\in\mathbf M_{n\times n}$ una matrice di funzioni continue e $\underline b(t) \in \mathbb R^n$ un vettore di funzioni continue.

L'integrale generale del sistema differenziale lineare $\underline y'(t) = A(t)\cdot\underline y(t)+\underline b(t)$ è:

$$ \underline y(t) = \underline y_0(t) + \underline y_P(t) $$

dove:

1.  $\underline y_0(t)$ è l'integrale generale del sistema omogeneo associato
2.  $\underline y_P(t)$ è una soluzione particolare del sistema completo

---
## Integrale generale di un sistema con matrice diagonalizzabile
Data $A\in\mathbf M_{n\times n}(\mathbb R)$ diagonalizzabile, con autovalori $\lambda_1, ...,\lambda_n$ e relativi autovettori $\underline v_1,...,\underline v_n$ linearmente indipendenti, un sistema fondamentale di soluzioni del sistema omogeneo $\underline y'(t) = A\underline y(t)$ è:

$$ \underline y_{01}(t) = e^{\lambda_1 t}\underline v_1,\underline y_{02}(t) = e^{\lambda_2 t}\underline v_2,...,\underline y_{0n}(t) = e^{\lambda_n t}\underline v_n $$

Equivalentemente, l'integrale generale del sistema sarà:

$$ \underline y_0(t) = c_1e^{\lambda_1t}\underline v_1 + c_2e^{\lambda_2t}\underline v_2 + ... + c_ne^{\lambda_nt}\underline v_n, \forall c_1,c_2,...,c_n\in\mathbb R $$

### Dimostrazione 3
    
Dobbiamo dimostrare che:
    
1.  Ciascuna $\underline y_{0i}(t) = c_ie^{\lambda_it}\underline v_i$ è soluzione del sistema
2.  $\underline y_{01}(t), \underline y_{02}(t),...,\underline y_{0n}(t)$ sono linearmente indipendenti
    
Grazie al teorema di struttura, $n$ soluzioni linearmente indipendenti determinano univocamente l'integrale generale.
    
1.  Fissiamo un indice $i=1,...,n$. Devo verificare che:
        
$$ \underline y_{0i}' = A\underline y_{0i} $$
    Allora:
        
$$ \begin{aligned} \underline y_{0i}' &= (e^{\lambda_it}\underline v_i)' =\\\ &= \lambda_ie^{\lambda_it}\underline v_i \end{aligned} $$
    Quindi:
        
$$ \begin{aligned} e^{\lambda_it}\lambda_i\underline v_i &= e^{\lambda_it}A\underline v_i =\\\ &= Ae^{\lambda_it}\underline v_i=\\\ &= A\underline y_{0i}(t) \end{aligned} $$
        
2.  Consideriamo ora la matrice ottenuta affiancando le soluzioni:
        
$$ M(t) = \begin{bmatrix}\underline y_{01}(t) & ... & \underline y_{0n}(t)\end{bmatrix} $$
    Scegliamo $t = t_0 = 0$ e sostituiamo:
        
$$ \begin{aligned} M(t) &= \begin{bmatrix}e^{\lambda_1 0}\underline v_1 & ... & e^{\lambda_n 0}\underline v_n\end{bmatrix} =\\\ &=\begin{bmatrix} \underline v_1 & ... & \underline v_n\end{bmatrix} \end{aligned} $$
        
Possiamo dire che $\det M(0) \ne 0$ poiché $\underline v_1,...,\underline v_n$ formano una base di $\mathbb R^n$ quindi, grazie al teorema del determinante Wronskiano, $\underline y_{01}(t),...,\underline y_{0n}(t)$ sono soluzioni linearmente indipendenti$\ _\blacksquare$

---
## Integrale generale di un sistema con matrice quadrata di ordine 2 con autovalori complessi coniugati
Sia $A\in\mathbf M_{2\times 2}(\mathbb R)$ avente autovalori:

$$ \lambda, \overline\lambda\in\mathbb C, \Im(\lambda)\ne0 $$

Chiamiamo $\underline v\in\mathbb C^2$ l'autovettore associato a $\lambda$.

Un sistema fondamentale di soluzioni del sistema omogeneo $\underline y'(t)=A\underline y(t)$ è:

$$ \begin{cases} \underline y_{01}(t)=\Re(e^{\lambda t}\underline v)\\\ \underline y_{02}(t) = \Im(e^{\lambda t}\underline v) \end{cases} $$

Equivalentemente, l'integrale generale del sistema è:

$$ \underline y_0(t) = c_1\Re(e^{\lambda t}\underline v)+c_2\Im(e^{\lambda t}\underline v), \forall c_1,c_2\in\mathbb R $$

---
## Continuità della somma
Sia $I\subseteq\mathbb R$ un intervallo e $f_n:I\to\mathbb R, n\in\mathbb N$. Se:

1.  le funzioni $f_n$ sono continue in $I \ \forall n\in \mathbb N$,
2.  la serie di termine generale $f_n$ converge totalmente in $I$,

allora la funzione somma $f(x) = \sum_{n=0}^{+\infty}f_n(x)$ è continua in $I$.

---
## Integrabilità termine a termine
Nelle ipotesi del teorema precedente, comunque scelto un intervallo $[a,b]\subset I$ chiuso e limitato, si ha:

$$ \underbrace{\int_a^bf(x)dx = \int_a^b\bigg(\sum_{n=0}^{+\infty}f_n(x)\bigg)}_{\text{integrale funzione somma}} = \underbrace{\sum_{n=0}^{+\infty}\bigg(\int_a^bf_n(x)dx\bigg)}_{\text{serie degli integrali}} $$

### Dimostrazione 4
    
$f$ è continua grazie al teorema precedente, perciò è anche integrabile sull’intervallo $[a,b]$.
    
Dobbiamo dimostrare la formula, cioè:
    
$$ \int_a^b\sum_{n=0}^{+\infty}f_n(x)dx - \lim_{k\to+\infty}\sum_{n=0}^{k}\bigg(\int_a^bf_n(x)dx\bigg)=0 $$
    
Riscrivo il lato sinistro:
    
$$ \lim_{k\to+\infty}\bigg\\{\int_a^b \sum_{n=0}^{+\infty}f_n(x)dx-\sum_{n=0}^k\bigg[\int_a^bf_n(x)dx\bigg]\bigg\\}=0 $$
    
Va notato che vale:
    
$$ \int_a^b\sum_{n=0}^{+\infty}f_n(x)dx = \lim_{k\to+\infty} \bigg(\int_a^b\sum_{n=0}^{k}f_n(x)dx \bigg) $$
    
perché la quantità a sinistra non dipende da $k$.
    
$$ \lim_{k\to+\infty}\bigg\\{\int_a^b\bigg[\sum_{n=0}^{+\infty}f_n(x)-\sum_{n=0}^{k}f_n(x)\bigg]dx\bigg\\} = \lim_{k\to+\infty}\bigg[\int_a^b\sum_{n=k+1}^{+\infty}f_n(x)dx\bigg] $$
    
Vogliamo dimostrare che quest’espressione è pari a 0.
    
Si stima il valore assoluto dell’integrale usando l’ipotesi di convergenza totale:
    
1.  $|f_n(x)|\leq a_n,\forall x$
2.  $\sum^{+\infty}a_n<+\infty$
    
$$ \begin{aligned} \bigg|\int_a^b\sum_{n=k+1}^{+\infty}f_n(x)dx\bigg| &\leq \int_a^b\sum_{n=k+1}^{+\infty}|f_n(x)|dx\\\ &\leq\int_a^b\bigg(\sum_{n=k+1}^{+\infty}a_n\bigg) dx = \sum_{n=k+1}^{+\infty}a_n\int_a^bdx = (b-a)\sum_{n=k+1}^{+\infty}a_n \end{aligned} $$
    
Si afferma che:
    
$$ \lim_{k\to+\infty}\bigg[(b-a)\sum_{n=k+1}^{+\infty}a_n\bigg]=0 $$
    
Si osserva che:
    
$$ \sum_{n=0}^{+\infty}a_n<+\infty\implies \lim_{k\to+\infty}\sum_{n=k+1}^{+\infty}a_n=0 $$
Allora vale che:
    
$$ (b-a) \lim_{k\to+\infty}\sum_{n=k+1}^{+\infty}a_n=0\ _\blacksquare $$

---
## Derivabilità termine a termine
Sia $I\subseteq\mathbb R$ un intervallo e $f_n:I\to\mathbb R$. Se:

1.  $f_n$ è derivabile in $I, \forall n\in\mathbb N$
2.  La serie di termine generale $f_n$ converge totalmente in $I$
3.  La serie di termine generale $f_n'$ converge totalmente in $I$

Allora la funzione somma:

$$ f(x) = \sum^{+\infty} f_n(x) $$

è derivabile. Inoltre vale:

$$ f'(x)=\bigg[\sum_{n=0}^{+\infty}f_n(x)\bigg]' = \sum_{n=0}^{ +\infty}f_n'(x) $$

---
## Raggio di convergenza di una serie di potenze reale
Data una serie di potenze reale $\sum_{n=0}^{+\infty}a_n(x-x_0)^n$, si verifica sempre uno dei tre seguenti casi:

1.  Il raggio di convergenza della serie è **nullo**: la serie converge solo per $x=x_0$
2.  Il raggio di convergenza della serie è **infinito**: la serie converge assolutamente in tutto $\mathbb R$
3.  Il raggio di convergenza è un numero **finito** **diverso da zero**:
    -   La serie converge assolutamente $\forall x \in(x_0-R,x_0+R) \iff |x-x_0|<R$
    -   La serie non converge per $|x-x_0|> R$

### Dimostrazione 5
    
Vogliamo dimostrare che se la serie converge in un certo punto $x$, allora converge assolutamente per qualunque $y$ tale che $|y-x_0|<|x-x_0|$.
    
Abbiamo due ipotesi:
    
1.  $\sum_{n=0}^{+\infty} a_n(x-x_0)^n<+\infty$
2.  $|y-x_0|<|x-x_0|$
    
Dobbiamo dimostrare la tesi:
    
$$ \sum_{n=0}^{+\infty} \big|a_n(x-x_0)^n\big|<+\infty $$
    
Dall’ipotesi i si deduce che:
    
$$ \lim_{n\to +\infty}\bigg[a_n(x-x_0)^n\bigg]=0 $$
    
perché termine generale di una serie convergente. Quindi, per $n$ sufficientemente grandi vale anche:
    
$$ \big|a_n(x-x_0)^n\big|\le1 $$
    
Stimiamo ora $\big|a_n(y-x_0)^n\big|$:
    
$$ \big|a_n(y-x_0)^n\big|=\bigg|a_n(x-x_0)^n\cdot{(y-x_0)^n\over (x-x_0)^n}\bigg|\leq\big|a_n(x-x_0)^n \big|\cdot\bigg|{y-x_0\over x-x_0}\bigg|^n $$
    
Quindi vale:
    
$$ \big|a_n(y-x_0)^n\big|\leq\bigg|{y-x_0\over x-x_0}\bigg|^n $$
    
E allora:
    
$$ \sum_{n=0}^{+\infty}\big|a_n(y-x_0)^n\big|\leq\sum_{n=0}^{+\infty}\bigg|{y-x_0\over x-x_0}\bigg|^n \implies q=\bigg|{y-x_0\over x-x_0}\bigg|\leq 1 $$
    
Che è una serie geometrica convergente. Allora, per il teorema del confronto, $\sum_{n=0}^{+\infty}\big|a_n(y-x_0)^n\big|$ è convergente$\ _\blacksquare$

---
## Calcolo del raggio di convergenza per una serie di potenze reale
Data la serie di potenze $\sum_{n=0}^{+\infty} a_n(x-x_0)^n$, abbiamo visto nel teorema precedente che esiste sempre $R\in [0,+\infty]$. Se i seguenti limiti esistono, lo si può calcolare così:

1.  $\displaystyle R = \lim_{n\to+\infty}\bigg|{a_n\over a_{n+1}}\bigg|$
2.  $\displaystyle R=\lim_{n\to+\infty}{1\over \sqrt[n]{|a_n|}}$

---
## Derivabilità ed integrabilità termine a termine per una serie di potenze reale
Sia $\sum_{n=0}^{+\infty}a_n(x-x_0)^n$ una serie di potenze reale avente raggio di convergenza $0<R\le+\infty$ e somma $f(x)$, con $x\in(x_0-R, x_0+R)$. Allora:

1.  La funzione somma $f(x)$ è continua in $x\in(x_0-R, x_0+R)$. In particolare, è integrabile in ogni $[a,b]\subset(x_0-R, x_0+R)$ ed inoltre vale la formula di integrabilità termine a termine:
    
$$ \int_a^bf(x)dx = \int_a^b\sum_{n=0}^{+\infty}a_n(x-x_0)^n dx=\sum_{n=0}^{+\infty}a_n\int_a^b(x-x_0)^n dx $$
Similmente, $f$ ammette primitiva in $(x_0-R,x_0+R)$:
    
$$ \int_{x_0}^xf(s)ds = \sum_{n=0}^{+\infty}a_n\int_{x_0}^x(s-x_0)^n ds $$
Inoltre, il raggio di convergenza della serie integrata è anch’esso $R$.
    
2.  $f(x)$ è derivabile nell’intervallo di convergenza $(x_0-R, x_0+R)$ ed inoltre vale la formula di derivabilità termine a termine:
    
$$ f'(x)=\sum_{n=0}^{+\infty}\big[a_n(x-x_0)^n\big]' = \sum_{n=0}^{+\infty}na_n(x-x_0)^{n-1} $$
Il raggio di convergenza della serie derivata è anch’esso $R$. Inoltre, $f(x)$ è derivabile infinite volte e ad ogni passaggio si può applicare la formula di derivazione termine a termine.

---
### Dimostrazione 6
Controlliamo la convergenza della serie esponenziale:

$$ \sum_{n=0}^{+\infty}{x^n\over n!} = 1+x+{x^2\over 2} + {x^3\over 6}+... $$

Il raggio di convergenza della serie è:

$$ \begin{aligned} R &= \lim_{n\to+\infty}{a_n\over a_{n+1}} =\\\ &= \lim_{n\to+\infty}{(n+1)!\over n!} = \\\ &= \lim_{n\to+\infty}(n+1) = \\\ &= +\infty \end{aligned} $$

Perciò possiamo concludere che la convergenza è semplice ed assoluta su tutto l’insieme $\mathbb R$ e totale $\forall[a,b]\subset \mathbb R$. Quindi:

$$ e^x = \sum_{n=0}^{+\infty}{x^n\over n!}, \forall x\in \mathbb R $$

---
### Dimostrazione 7
Controlliamo la convergenza della serie logaritmica, calcolata integrando ${1\over 1+x}$:

$$ \ln(1+x) = \sum_{n=0}^{+\infty}(-1)^{n+1}{x^n\over n}, x\in(-1, 1) $$

Calcoliamo il raggio di convergenza della serie:

$$ \begin{aligned} R &= \lim_{n\to+\infty}{1\over\sqrt[n]{|a_n|}} =\\\ &= \lim_{n\to+\infty}\sqrt[n]{n} = \\\ &=1 \end{aligned} $$

Perciò la convergenza è semplice ed assoluta in $(-1,1)$ e totale $\forall[a,b]\subset(-1,1)$.

Controlliamo il comportamento della serie sulla frontiera:

-   $x = 1$
    
$$ \sum_{n=0}^{+\infty}{(-1)^{n+1}\over n} $$
Questa serie converge per il criterio di Leibniz, quindi la serie logaritmica converge per $x=1$.
    
-   $x=-1$
    
$$ \sum_{n=0}^{+\infty}{1\over n} $$
Questa è la serie armonica con $\alpha= 1$, perciò diverge, il che implica che la serie logaritmica diverga per $x= -1$.
    

Da questi calcoli possiamo concludere che l’insieme di convergenza puntuale della serie logaritmica è $E=(-1,1]$.

---
## Raggio di convergenza di una serie di potenze complessa
Data una serie di potenze $\sum_{n=0}^{+\infty}a_n(z-z_0)^n$, con $a_n, z, z_0\in\mathbb C$, si verifica sempre uno dei tre casi seguenti:

1.  Raggio di convergenza nullo: la serie converge solo per $z=z_0$
2.  Raggio di convergenza infinito: la serie converge assolutamente $\forall z\in \mathbb C$
3.  Raggio di convergenza finito non nullo:
    -   La serie converge assolutamente $\forall z\in \mathbb C:|z-z_0|<R$
    -   La serie diverge per $|z-z_0|>R$

---
## Calcolo dei coefficienti di Fourier
Se $f(x) = a_0+\sum_{n=1}^m\big[a_n\cos(nx)+b_n\sin(nx)\big]$, allora:

1.  $\displaystyle a_0 = {1\over 2\pi}\int_{-\pi}^\pi f(x)dx$
2.  $\displaystyle a_n = {1\over \pi}\int_{-\pi}^\pi f(x)\cos(nx)dx, \forall n = 1, ..., m$
3.  $\displaystyle b_n = {1\over \pi}\int_{-\pi}^\pi f(x)\sin(nx)dx, \forall n = 1, ..., m$

### Dimostrazione 8
    
Sfruttiamo le formule di ortogonalità per dimostrare questo teorema.
    
Sappiamo che $f(x) = a_0+\sum_{n=1}^m\big[a_n\cos(nx)+b_n\sin(nx)\big]$.
    
-   Per calcolare $a_0$, si integra tra $-\pi$ e $\pi$:
$$ \begin{aligned} \int_{-\pi}^{\pi}f(x)dx &= \int_{-\pi}^\pi \bigg\\{a_0+\sum_{n=1}^m\big[a_n\cos(nx)+b_n\sin(nx)\big]\bigg\\}dx=\\\ &=\int_{-\pi}^\pi a_0dx + \sum_{n =1}^ma_n\cancel{\int_{-\pi}^\pi \cos(nx)dx} + \sum_{n =1}^ma_n\cancel{\int_{-\pi}^\pi \sin(nx)dx} = \\\ &= \int_{-\pi}^\pi a_0dx = \\\ &= a_o\int_{-\pi}^\pi dx = \\\ &= 2\pi a_0 \end{aligned} $$
    Questo significa che:
        
$$ a_0 = {1\over 2\pi}\int_{-\pi}^\pi f(x)dx $$
        
-   Per calcolare $a_n$, si moltiplica l’identità per $\cos(nx)$ e si integra tra $-\pi$ e $\pi$:
        
$$ \begin{aligned} \int_{-\pi}^\pi f(x)\cos(nx)dx &= \int_{-\pi}^\pi \bigg\\{a_0+\sum_{k=1}^m\big[a_k\cos(kx)+b_k\sin(kx)\big]\bigg\\}\cos(nx)dx=\\\ &= \cancel{a_0\int_{-\pi}^\pi\cos(nx)dx} + \sum_{k=1}^ma_k\int_{-\pi}^\pi\cos(kx)\cos(nx)dx + \sum_{k=1}^mb_k\cancel{\int_{-\pi}^\pi\sin(kx)\sin(nx)dx} = \\\ &= a_n\int_{-\pi}^\pi\cos^2(nx)dx =\\\ &= a_n\pi \end{aligned} $$
    Questo significa che:
        
$$ a_n={1\over\pi}\int_{-\pi}^\pi f(x)\cos(nx)dx $$
        
-   Per calcolare $b_n$ si procede analogamente al passo precedente, moltiplicando per $\sin(nx)$ invece che per $\cos(nx)\ _\blacksquare$

---
## Convergenza di una serie trigonometrica a partire dai suoi coefficienti
1.  Se la serie numerica di termine generale $|a_n|+|b_n|$ è convergente, allora la serie trigonometrica converge totalmente in $\mathbb R$. Inoltre, la funzione somma è continua in $\mathbb R$ ed è possibile integrare termine a termine in ogni sottoinsieme limitato di $\mathbb R$:
    
$$ \int_{x_0}^x\bigg\\{a_0+\sum_{n=1}^{+\infty}\big[a_n\cos(nt)+b_n\sin(nt)\big]\bigg\\}dt = a_0(x-x_0)+\sum_{n=1}^{+\infty}\bigg[a_n\int_{x_0}^x\cos(nt)dt + b_n\int_{x_0}^x\sin(nt)dt\bigg] $$
    
2.  Se la serie numerica di termine generale $n(|a_n|+|b_n|)$ è convergente, allora la funzione somma è derivabile su $\mathbb R$ ed è possibile derivare termine a termine su $\mathbb R$:
    
$$ \bigg\\{a_0+\sum_{n=1}^{+\infty}\big[a_n\cos(nx)+b_n\sin(nx)\big]\bigg\\}' = \sum_{n=1}^{+\infty}n\big[-a_n\sin(nx)+b_n\cos(nx)\big], \forall x\in\mathbb R $$

### Dimostrazione 9
1. $|f_n(x)| = \big|a_0+\sum_{n=1}^{+\infty}\big[a_n\cos(nx)+b_n\sin(nx)\big]\big|\leq|a_0| + \sum_{n=1}^{+\infty}\big[|a_n|\underbrace{|\cos(nx)|}_{\leq1}+|b_n|\underbrace{|\sin(nx)|}_{\leq1}\big]\leq|a_0|+\sum_{n=1}^{+\infty}\big(|a_n|+|b_n|\big)$
        
    Quindi se la serie $\sum_{n=1}^{+\infty}\big(|a_n|+|b_n|\big)$ converge allora, per definizione di convergenza totale, la serie trigonometrica converge totalmente in $\mathbb R$. Grazie al teorema _conseguenze della convergenza totale_, la funzione somma è continua su $\mathbb R$ ed integrabile termine a termine sugli intervalli limitati.
        
2.  Sappiamo che $f_0(x) = a_0$ e che $f_n(x) = a_n\cos(nx)+b_n\sin(nx)$. Notiamo che sono tutte funzioni derivabili.
        
    Troviamo la derivata $f'_n(x) = -na_n\sin(nx)+nb_n\cos(nx)$.
        
    Confrontiamola con il termine generale: $|f'_n(x)|\leq n(|a_n|+|b_n|)$.
        
    Se la serie $\sum_{n=1}^{+\infty}n(|a_n|+|b_n|)$ converge allora, a maggior ragione, $\sum_{n=1}^{+\infty}(|a_n|+|b_n|)$ converge, quindi la funzione somma è derivabile termine a termine.
        
    Iterando: se $\sum_{n=1}^{+\infty}n^2(|a_n|+|b_n|)$ converge, allora la funzione somma può essere derivata due volte e vale la formula di derivazione termine a termine$\ _\blacksquare$

---
## Convergenza puntuale di una serie di Fourier
Sia $f:\mathbb R\to\mathbb R$ periodica di periodo $2\pi$ e regolare a tratti in $[-\pi,\pi]$.

Allora, la serie di Fourier di $f$ converge puntualmente in tutto $\mathbb R$ ed inoltre:

$$ \lim_{m\to+\infty}F_m(x) = {1\over2}\bigg[\lim_{s\to x^+}f(s) + \lim_{s\to x^-}f(s)\bigg] $$

cioè la serie di Fourier nel punto $x$ converge alla media tra $f(x^-)$ ed $f(x^+)$.

---
## Convergenza totale ed integrabilità termine a termine della serie di Fourier
Sia $f:\mathbb R\to\mathbb R$ periodica di periodo $2\pi$ e regolare a tratti in $[-\pi, \pi]$.

Se inoltre $f$ è anche continua in $\mathbb R$, allora la serie di Fourier di $f$ converge totalmente ad $f$ in tutto $\mathbb R$.

In particolare, vale la formula di integrabilità termine a termine sui limitati.

---
## Derivabilità termine a termine della serie di Fourier
Sia $f:\mathbb R\to\mathbb R$ periodica di periodo $2\pi$ e derivabile su $\mathbb R$.

Sia $f'$ regolare a tratti in $[-\pi,\pi]$ e continua su $\mathbb R$.

Allora la serie di Fourier di $f$ è derivabile in $\mathbb R$ e vale la formula di derivazione termine a termine.

---
## Convergenza in norma (o media) quadratica della serie di Fourier
Sia $f:\mathbb R\to\mathbb R$ periodica di periodo $2\pi$ e regolare a tratti in $[-\pi, \pi]$. Allora:

$$ \lim_{m\to+\infty}\int_{-\pi}^\pi|F_m(x)-f(x)|^2dx = 0 $$

---
## Identità di Parseval
Sia $f:\mathbb R\to\mathbb R$ periodica di periodo $2\pi$ e regolare a tratti in $[-\pi, \pi]$.

Indicando con $a_0, a_n, b_n$ per $n\ge1$ i suoi coefficienti di Fourier, si ha:

$$ {1\over\pi}\int_{-\pi}^\pi|f(x)|^2dx = 2a_0^2+\sum_{n=1}^{+\infty}(a_n^2+b_n^2) $$

---
## Lunghezza di una curva
Sia $[a,b]\subseteq\mathbb R$ un intervallo limitato.

Sia $\underline r:[a,b]\to\mathbb R^n$ la parametrizzazione di una curva regolare $\gamma$. Allora:

$$ \text{lunghezza}(\gamma) = \int_a^b||\underline{r'}(t)||dt $$

---
## Invarianza della lunghezza di una curva per riparametrizzazione
Sia $\underline r:[a,b]\to\mathbb R^3$ la parametrizzazione regolare di una curva di sostegno $\gamma$.

Sia $f:[c,d]\to[a,b]$ una funzione derivabile e biunivoca.

Formuliamo la parametrizzazione equivalente $\underline v(s)$:

$$ \underline v(s)=\underline r\big(f(s)\big) =\underline r \circ f(s):[c,d]\to\mathbb R^3 $$

Sia $\delta$ il sostegno della nuova curva di parametrizzazione $\underline v$. Allora:

$$ \text{lunghezza}(\gamma)=\text{lunghezza}(\delta) $$

### Dimostrazione 10
    
Sappiamo che:
    
$$ \begin{aligned} \text{lunghezza}(\gamma)&=\int_a^b||\underline{r'}(t)||dt\\\ \text{lunghezza}(\delta)&=\int_c^d||\underline{v'}(t)||dt\\\ \end{aligned} $$
    
Troviamo la norma del vettore derivato $\underline{v'}(t)$:
    
$$ \underline{v'} = \begin{pmatrix}r_1'\big(f(s)\big)f'(s)\\\r_2'\big(f(s)\big)f'(s)\end{pmatrix} $$
    
$$ \begin{aligned} ||\underline{v'}(s)|| &= \sqrt{\big[r_1'\big(f(s)\big)f'(s)\big]^2 + \big[r_2'\big(f(s)\big)f'(s)\big]^2} = \\\ &= |f'(s)|\sqrt{\big[r_1'\big(f(s)\big)\big]^2 + \big[r_2'\big(f(s)\big)\big]^2} = \\\ &= |f'(s)|\cdot||\underline{r'}\big(f(s)\big)|| \end{aligned} $$
    
Allora possiamo riscrivere:
    
$$ \text{lunghezza}(\delta) = \int_c^d|f'(s)|\cdot||\underline{r'}\big(f(s)\big)||ds $$
    
Effettuiamo un cambio di variabile:
    
$$ \begin{cases} t = f(s)\\\ dt = f'(s)ds \end{cases} $$
    
Dato che $f$ è biunivoca, essa è sempre crescente o decrescente. Supponiamo che $f'(s)\ge0, \forall s\in [c,d]$. Allora:
    
$$ \begin{aligned} \text{lunghezza}(\delta) &= \int_c^df'(s)\cdot||\underline{r'}\big(f(s)\big)||ds = \\\ &= \int_a^b||\underline{r'}(t)||dt = \\\&=\text{lunghezza}(\gamma)\ _\blacksquare \end{aligned} $$

---
## Teorema del differenziale totale
Sia $A\subseteq\mathbb R^2$ aperto.

Se $f\in C^1(A)$, allora $f$ è **differenziabile in ogni punto** di $A$.

---
## Differenziabilità implica continuità
Siano $A\subseteq\mathbb R^2$ aperto e $f:A\to\mathbb R$ differenziabile nel punto $\underline{x_0}\in A$. Allora $f$ è continua in $\underline{x_0}$.

### Dimostrazione 11
Bisogna dimostrare che:

$$ \lim_{\underline x\to\underline{x_0}}f(\underline x) = f(\underline{x_0}) $$

Essendo $f$ differenziabile in $\underline{x_0}$:

$$ f(\underline x) -f(\underline{x_0}) =\ <\nabla f(\underline{x_0}), \underline x-\underline{x_0}>+\ o(||\underline x-\underline{x_0}||) $$

Quindi:

$$ \begin{align*} |f(\underline x)-f(\underline{x_0})| &= |<\nabla f(\underline{x_0}), \underline x-\underline{x_0}>+\ o(||\underline x-\underline{x_0}||)|\\\ &\le |<\nabla f(\underline{x_0}), \underline x-\underline{x_0}>|+\ o(||\underline x-\underline{x_0}||)\\\ &\le ||\nabla f (\underline{x_0})||\cdot||\underline x-\underline{x_0}|| + o(||\underline x-\underline{x_0}||) \end{align*} $$

$$ \lim_{\underline x\to\underline{x_0}}|f(\underline x)-f(\underline{x_0})|\le \lim_{\underline x\to\underline{x_0}}||\nabla f (\underline{x_0})||\cdot||\underline x-\underline{x_0}|| + o(||\underline x-\underline{x_0}||)=0\implies \lim_{\underline x\to\underline{x_0}}|f(\underline x)-f(\underline{x_0})|=0\ _\blacksquare $$

---
## Formula del gradiente
Siano $A\subseteq\mathbb R^2$ aperto e $f:A\to\mathbb R$.

Supponiamo che $f$ sia differenziabile in $\underline{x_0}\in A$. Allora:

1.  $f$ ammette derivata direzionale in $\underline{x_0}$ lungo qualunque direzione $\underline v\in\mathbb R^2, ||\underline v ||=1$
2.  $\displaystyle {\partial f\over\partial\underline v}(\underline{x_0}) = \ <\nabla f(\underline{x_0}), \underline v>$

---
## Direzioni di massima e minima crescita
Siano $A\subseteq\mathbb R^2$ aperto e $f:A\to\mathbb R$. Supponiamo:

1.  $f$ differenziabile in $\underline{x_0}\in A$
2.  $\nabla f(\underline{x_0})\ne(0,0)$

Allora $\forall\underline v\in\mathbb R^2, ||\underline v||=1$ si ha:

$$ \bigg|{\partial f\over\partial\underline v}(\underline{x_0})\bigg|\le||\nabla f(\underline{x_0})|| $$

e inoltre, detti $\underline{v_\text{max}}={\nabla f(\underline{x_0})\over||\nabla f(\underline{x_0})||}$ e $\underline{v_\text{min}}=-{\nabla f(\underline{x_0})\over||\nabla f(\underline{x_0})||}$, si ha:

$$ \begin{align*} {\partial f\over\partial\underline{v_\text{max}}}(\underline{x_0})&=||\nabla f(\underline{x_0})||,\\\ {\partial f\over\partial\underline{v_\text{min}}}(\underline{x_0})&=-||\nabla f(\underline{x_0})|| \end{align*} $$

### Dimostrazione 12
    
Sia $\underline v\in\mathbb R^2$ un vettore di norma unitaria.
    
Poiché $f$ è differenziabile in $\underline{x_0}$, vale la formula del gradiente:
    
$$ \begin{align*} {\partial f\over\partial\underline v}(\underline{x_0}) &= \ <\nabla f(\underline{x_0}), \underline v>\\\ \bigg|{\partial f\over\partial\underline v}(\underline{x_0})\bigg| &= |<\nabla f(\underline{x_0}), \underline v>|\\\ &\le||\nabla f(\underline{x_0})||\cdot\underbrace{\cancel{||\underline v||}}_1 = ||\nabla f(\underline{x_0})|| \end{align*} $$
    
Adesso si verificano le identità per $\underline{v_\text{max}}, \underline{v_\text{min}}$:
    
$$ \begin{align*} {\partial f\over\partial\underline{v_\text{max}}}(\underline{x_0}) &=\ <\nabla f(\underline{x_0}),\underline{v_\text{max}}>\ =\\\ &=\ <\nabla f(\underline{x_0}),{\nabla f(\underline{x_0})\over||\nabla f(\underline{x_0})||}>\ =\\\ &={1\over||\nabla f(\underline{x_0})||}\cdot<\nabla f(\underline{x_0}),\nabla f(\underline{x_0})>\ =\\\ &={||\nabla f(\underline{x_0})||^2\over||\nabla f(\underline{x_0})||}=\\\ &= ||\nabla f(\underline{x_0})|| \end{align*} $$
    
Analogamente con $\underline{v_\text{min}}$, con segno negativo$_\blacksquare$

---
## Derivazione di funzioni composte
Sia $\underline r:I\subseteq\mathbb R\to A\subseteq\mathbb R^2$ la parametrizzazione regolare di una curva piana.

Sia $f:A\subseteq\mathbb R^2\to\mathbb R$ differenziabile.

Detta $F:I\to\mathbb R$ la funzione composta:

$$ F(t)=(f\circ\underline r)(t) = f\big(\underline r(t)\big) = f\big(r_1(t), r_2(t)\big) $$

Allora vale:

$$ F'(t) =\ <\nabla f\big(\underline r(t)\big), \underline r'(t)> $$

---
## Derivata direzionale come derivata della funzione composta
Siano $A\subseteq\mathbb R^2$ aperto, $f:A\to\mathbb R$ differenziabile in $A$, $\underline{x_0}\in A$ e $\underline v\in\mathbb R^2$ con $||\underline v||=1$. Posto:

$$ F(t)=f(\underline{x_0}+t\underline v),\ t\to 0 $$

si ha:

$$ F'(0) = {\partial f\over\partial\underline v}(\underline{x_0}) $$

### Dimostrazione 13
    
Si applica il teorema di derivazione della funzione composta con $\underline r(t)=\underline{x_0}+t\underline v$, per $t\to0$.
    
$$ \begin{align*} F(t)&=f(\underline{x_0}+t\underline v) = (f\circ\underline r)(t) = f\big(\underline r(t)\big)\\\ F'(t) &=\ <\nabla f\big(\underline r(t)\big), \underline r'(t)>\\\ F'(0)&=\ <\nabla f\big(\overbrace{\underline r(0)}^{\underline{x_0}}\big), \underline r'(0)>\\\ \underline r(t)&= \begin{pmatrix}r_1(t)\\\r_2(t)\end{pmatrix} = \begin{pmatrix}x_0+tv_1\\\y_0+tv_2\end{pmatrix}\\\ \underline r'(t)&= \begin{pmatrix}r_1'(t)\\\r_2'(t)\end{pmatrix} = \begin{pmatrix}v_1\\\v_2\end{pmatrix} = \underline v \implies \underline r'(t) = \underline r'(0) = \underline v \end{align*} $$
    
Quindi, applicando la formula del gradiente:
    
$$ \begin{align*} F'(0) &=\ <\nabla f(\underline{x_0}), \underline v> =\\\&={\partial f\over\partial\underline v}(\underline{x_0})\ _\blacksquare \end{align*} $$

---
## Ortogonalità del gradiente agli insiemi di livello
Sia $A\subseteq\mathbb R^2$ aperto e sia $f:A\to\mathbb R$ differenziabile in $A$.

Supponiamo che l’insieme di livello $I_k=\{(x,y)\in A:f(x,y)=k\}$ sia il sostegno di una curva regolare $\underline r:I\subseteq\mathbb R\to A$. Allora:

$$ <\nabla f\big(\underline r(t)\big), \underline r'(t)>=0, \ \forall t\in I $$

### Dimostrazione 14
    
Per ipotesi, $I_k$ coincide con il sostegno della curva $\underline r(t)$, cioè:
    
$$ I_k = \{\underline r(t):t\in I\} $$
    
Quindi, in particolare:
    
$$ f\big(\underline r(t)\big)=k, \forall t\in I $$
    
Chiamiamo $F:I\to\mathbb R,\ F(t)=f\big(\underline r(t)\big)$.
    
Da un lato, $F(t)=k\ \forall t\implies F'(t)=0\ \forall t$.
    
Dall’altro, si usa il teorema di derivazione della funzione composta:
    
$$ F'(t) =\ <\nabla f\big(\underline r(t)\big), \underline r'(t)> $$
    
Quindi:
    
$$ <\nabla f\big(\underline r(t)\big), \underline r'(t)> = 0, \ \forall t\in I_\blacksquare $$

---
## Teorema di Schwartz
Siano $A\subseteq\mathbb R^2$ aperto ed $f\in C^2(A)$. Allora:

$$ {\partial^2f\over\partial y\partial x}(x,y)= {\partial^2f\over\partial x\partial y}(x,y),\ \forall(x,y)\in A $$

cioè $H_f(x,y)$ è una matrice simmetrica $\forall(x,y)\in A$.

---
## Formula di Taylor al secondo ordine
Siano $A\subseteq\mathbb R^2$ aperto e $f\in C^2(A)$. Allora, $\forall\underline{x_0}\in A$ vale la formula:

$$ f(\underline{x_0}+\underline h) = f(\underline{x_0})+<\nabla f(\underline{x_0}), \underline h>+{1\over2}<\underline h, H_f(\underline{x_0})\underline h>+\ o(||\underline h||^2) $$

---
## Segno di una forma quadratica ed autovalori
Sia $A\in\mathbf M_{2,2}(\mathbb R)$ simmetrica e $q$ la forma quadratica indotta. Allora:

-   $q$ è **definita** positiva (o negativa) se e solo se tutti gli autovalori di $A$ sono strettamente positivi (o negativi)
-   $q$ è **semidefinita** positiva (o negativa) se e solo se un autovalore di $A$ è nullo e l’altro è strettamente positivo (o negativo)
-   $q$ è **indefinita** se e solo se $A$ ha autovalori di segno opposto diversi da zero

---
## Teorema di Weierstrass (una dimensione)
Sia $f:[a,b]\to\mathbb R$ continua, allora esistono:

-   $x_m\in[a,b]$ punto di minimo assoluto
-   $x_M\in[a,b]$ punto di massimo assoluto

Cioè:

$$ f(x_m)\le f(x)\le f(x_M), \forall x\in[a,b] $$

---
## Teorema di Fermat (una dimensione)
Sia $f:(a,b)\to\mathbb R$ derivabile.

Se $x_0$ è punto di massimo o minimo (globale o locale), per $f$ in $(a,b)$:

$$ f'(x_0)=0 $$

---
## Teorema di Weierstrass (due dimensioni)
Sia $f:A\subseteq\mathbb R^2\to\mathbb R$ continua, con $A$ chiuso e limitato.

Allora $f$ assume i valori di massimo e minimo assoluto in $A$, cioè esistono:

-   $(x_m, y_m)\in A$ punto di minimo assoluto
-   $(x_M, y_M)\in A$ punto di massimo assoluto

Cioè:

$$ f(x_m,y_m)\le f(x,y)\le f(x_M,y_M), \forall(x,y)\in A $$

---
## Teorema di Fermat (due dimensioni)
Siano $A\subseteq\mathbb R^2$ aperto ed $f:A\to\mathbb R$.

Sia $(x_0,y_0)$ punto di estremo per $f$ e supponiamo che $f$ sia derivabile in $(x_0,y_0)$. Allora:

$$ \nabla f(x_0, y_0) = \begin{pmatrix}0\\\0\end{pmatrix} $$

### Dimostrazione 15
    
Vogliamo dimostrare che:
    
$$ {∂f\over∂x}(x_0,y_0) = {∂f\over∂y}(x_0,y_0)=0 $$
    
utilizzando il teorema di Fermat per funzioni di una variabile.
    
Poiché $A$ è aperto, $(x_0 ,y_0 )$ è interno ad $A$, quindi esiste $\delta > 0$ tale che $B_\delta(x_0,y_0)\subseteq A$.
    
Pongo $g_1(x)=f(x,y_0)$.
    
$g_1$ è anch’essa definita in un aperto: $(x_0-\delta,x_0+\delta)$.
    
$x_0$ è un punto estremale anche per $g_1$.
    
$g_1$ è derivabile poiché:
    
$$ g_1'(x_0) = {∂f\over∂x}(x_0,y_0)=0 $$
    
Analogamente, $g_2(y)=f(x_0,y)$ e $g_2'(y_0)={∂f\over∂y}(x_0,y_0)=0_\blacksquare$

---
## Criterio della matrice hessiana
Siano $A\subseteq\mathbb R^2$ aperto e $f\in C^2(A)$.

Sia $(x_0,y_0)\in A$ punto critico per $f$.

Denotiamo con $q$ la forma quadratica indotta da $H_f(x_0,y_0)$:

$$ q(h_1,h_2)=<\begin{pmatrix}h_1&h_2\end{pmatrix}, H_f(x_0,y_0)\begin{pmatrix}h_1\\\h_2\end{pmatrix}> $$

1.  Se $q$ è definita positiva, allora $(x_0,y_0)$ è punto di minimo locale
2.  Se $q$ è definita negativa, allora $(x_0,y_0)$ è punto di massimo locale
3.  Se $q$ è indefinita, allora $(x_0,y_0)$ è un punto di sella

---
## Metodo dei moltiplicatori di Lagrange
Siano $A\subseteq\mathbb R^2$ aperto e $f,F\in C^1(A)$.

Sia $(x_0,y_0)$ un punto di estremo vincolato per $f$ con vincolo:

$$ z=\{(x,y)\in\mathbb R^2:F(x,y)=0\} $$

Supponiamo inoltre che:

$$ \nabla F(x_0,y_0)\ne0 $$

Allora esiste $\lambda_0$, detto moltiplicatore di Lagrange, tale che:

$$ \nabla f(x_0,y_0)=\lambda_0\nabla F(x_0, y_0) $$

---
## Integrabilità di funzioni continue
Siano $D\subseteq\mathbb R^2$ una regione semplice e $f:D\to\mathbb R$ continua in $D$.

Allora, $f$ è integrabile su $D$, cioè:

$$ \iint_Df(x,y)dxdy<+\infty $$

---
## Integrazione per fili
Se $E$ è una regione $z$-semplice ed $f:E\to\mathbb R$ è una funzione continua:

$$ \iiint_Ef(x,y,z)dxdydz=\iint_D\bigg[\int_{h_1(x,y)}^{h_2(x,y)}f(x,y,z)dz\bigg]dxdy $$
