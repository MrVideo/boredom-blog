---
title: 'Serie di funzioni'
draft: false
type: 'page'
toc: true
mathjax: true
---

---

## Disclaimer

For some reason, MathJax is misbehaving on this page, so the last equation is not rendering correctly. Sorry for the inconvenience.

---

## Serie di funzioni e convergenza puntuale

 Siano dati un $J\subseteq \mathbb R$ e delle funzioni $f_n:J\to\mathbb R, n = 0,1,2,...$

La serie di funzioni di termine generale $f_n(x)$ è la successione delle somme parziali:

$$S_k(x) = \sum_{n=0}^kf_n(x)$$

Tale serie converge puntualmente (o semplicemente) in $\overline x\in J$ se la serie numerica di termine generale $f_n(\overline x)$ converge, cioè se esiste finito il limite:

$$\lim_{k\to+\infty}S_k(\overline x) = \lim_{k\to+\infty}\sum_{n=0}^kf_n(\overline x)$$




 Alcune osservazioni:

1. Fissato $\overline x\in J$, si tratta di una serie numerica.
2. Una serie di funzioni potrebbe essere convergente per alcuni $x\in J$ e divergente o indeterminata per altri $x$.



 Chiamiamo insieme di convergenza puntuale (o semplice) $E\subseteq J$ l'insieme dei punti in cui la serie converge puntualmente.

$\forall x\in E$ risulta definita una nuova funzione, detta somma della serie:

$$f(x) = \sum_{n=0}^{+\infty}f_n(x)$$

Essa è definita da:

$$f(x) = \lim_{k\to+\infty}S_k(x)$$




 Va notato che spesso si usa indicare con il simbolo $\sum_{n=0}^{+\infty}f_n(x)$ sia la serie che la sua somma.




 La somma di una serie di funzioni è a sua volta una funzione.



## Convergenza assoluta di una serie di funzioni


 Diciamo che la serie di termine generale $f_n(x),x\in J$ converge assolutamente in $\overline x\in J$ se converge la serie numerica di termine generale:

$$|f_n(\overline x)|$$




 È utile notare che la convergenza assoluta implica quella semplice, ma non è valido il viceversa.



## Serie armonica generalizzata o serie di Riemann


 Si definisce serie armonica generalizzata (o serie di Riemann) una serie di funzioni che ha forma:

$$\sum_{n=0}^{+\infty}{1\over n^x}$$

Dove $n = 1,2,3,...$ e $J=\mathbb R$.



L'insieme di convergenza puntuale di questa serie è $E=(1, +\infty) = \{x\in\mathbb R\mid x>1\}$.

Al di fuori dell'insieme di convergenza, la serie diverge.

È inoltre possibile dire che, all'interno di $E$, la convergenza della serie è anche assoluta, essendo essa a termini positivi.

## Convergenza totale di una serie di funzioni

Possiamo porci diverse domande sulla natura di $f_n$ e su cosa implichi per la natura di $f$, ad esempio:

1. Se $f_n$ sono funzioni continue, allora $f$ è una funzione continua?
2. Se $f_n$ sono funzioni derivabili, allora $f$ è una funzione derivabile?
3. Se $f$ è una funzione derivabile, allora la serie è derivabile termine a termine, ossia vale $\big(\sum f_n(x)\big)'=\sum f_n'(x)$?

La convergenza puntuale non è sufficiente ad assicurare queste proprietà, perciò introduciamo il concetto di **convergenza assoluta**.

Data una serie di termine generale $f_n(x)$, sia $E$ il suo insieme di convergenza puntuale. Si supponga che $E$ contenga almeno un intervallo.

Dato un qualunque intervallo $I\subseteq E$, possiamo chiederci se la convergenza della serie sia *in qualche senso uniforme rispetto alla $x$ in $I$*.


 La serie di termine generale $f_n(x),x\in J$ converge totalmente in $I\subseteq E\subseteq J$ se esiste una successione numerica $a_n$ non negativa tale che:

1. si ha $|f_n(x)|\leq a_n, \forall n = 0,1,2,...,\forall x\in I$
2. $\sum_{n=0}^{+\infty}a_n<+\infty$, cioè la serie numerica di termine $a_n$ è convergente.



 La convergenza totale in $I$ implica la convergenza assoluta e quindi anche puntuale $\forall\overline x\in I$.

Non vale necessariamente il viceversa: se una serie converge assolutamente $\forall\overline x\in I$, non è detto che converga totalmente in $I$.

Va notato però che, in generale, se una serie converge totalmente in un intervallo $I$, allora essa converge totalmente in ogni sottoinsieme di $I$.



- **Dimostrazione**
    
    Cerchiamo di dimostrare che se una serie converge totalmente in $I$, converge totalmente in ogni sottoinsieme di $I$.
    
    Prendiamo ad esempio la serie geometrica $\sum_{n=0}^{+\infty}x^n$.
    
    Dimostriamo che converge totalmente in $[-\delta,\delta]\subseteq I$, con $\delta <1$:
    
    1. $\forall n\in\mathbb N$, cerchiamo $a_n$ tale che valga $|x^n|=|x|^n\leq a_n \forall x\in [-\delta,\delta]$
        
        $|x^n|=|x|^n\leq a_n = \delta^n$
        
    2. $\sum_{n=0}^{+\infty}\delta^n$ converge poiché, per definizione, $\delta<1$.
    
    Allora la serie geometrica converge totalmente in ogni intervallo $[-\delta,\delta]$, con $0<\delta<1 \ _\blacksquare$
    

Quando una serie converge totalmente, alcune proprietà delle funzioni $f_n$ vengono ereditate dalla somma della serie.

### Continuità della somma

 Sia $I\subseteq\mathbb R$ un intervallo e $f_n:I\to\mathbb R, n\in\mathbb N$. Se:

1. le funzioni $f_n$ sono continue in $I \ \forall n\in \mathbb N$,
2. la serie di termine generale $f_n$ converge totalmente in $I$,

allora la funzione somma $f(x) = \sum_{n=0}^{+\infty}f_n(x)$ è continua in $I$.

 $I$ è il sottoinsieme dell'insieme di definizione delle $f_n$ sul quale:

1. tutte le $f_n$ sono continue,
2. la convergenza della serie è totale.

Nelle ipotesi del teorema, in particolare, $f$ è integrabile in ogni sottoinsieme chiuso e limitato $[a,b]\subset I$.



### Integrabilità termine a termine


 Nelle ipotesi del teorema precedente, comunque scelto un intervallo $[a,b]\subset I$ chiuso e limitato, si ha:

$$\underbrace{\int_a^bf(x)dx = \int_a^b\bigg(\sum_{n=0}^{+\infty}f_n(x)\bigg)}_{\text{integrale funzione somma}} = \underbrace{\sum_{n=0}^{+\infty}\bigg(\int_a^bf_n(x)dx\bigg)}_{\text{serie degli integrali}}$$



- **Dimostrazione 4**
    
    $f$ è continua grazie al teorema precedente, perciò è anche integrabile sull’intervallo $[a,b]$.
    
    Dobbiamo dimostrare la formula, cioè:
    
    $$\int_a^b\sum_{n=0}^{+\infty}f_n(x)dx - \lim_{k\to+\infty}\sum_{n=0}^{k}\bigg(\int_a^bf_n(x)dx\bigg)=0$$
    
    Riscrivo il lato sinistro:
    
    $$\lim_{k\to+\infty} \bigg\\{ \int_a^b \sum_{n=0}^{+\infty} f_n(x)dx -\sum_{n=0}^k \bigg[ \int_a^b f_n(x)dx \bigg] \bigg\\} = 0$$
    
    
    Va notato che vale:
    
    $$\int_a^b\sum_{n=0}^{+\infty}f_n(x)dx = 
    \lim_{k\to+\infty} \bigg(\int_a^b\sum_{n=0}^{k}f_n(x)dx \bigg)$$
    
    perché la quantità a sinistra non dipende da $k$.
    
    
    
    $$\lim_{k\to+\infty}\bigg\\{\int_a^b\bigg[\sum_{n=0}^{+\infty}f_n(x)-\sum_{n=0}^{k}f_n(x)\bigg]dx\bigg\\} = \lim_{k\to+\infty}\bigg[\int_a^b\sum_{n=k+1}^{+\infty}f_n(x)dx\bigg]$$
    
    Vogliamo dimostrare che quest’espressione è pari a 0.
    
    Si stima il valore assoluto dell’integrale usando l’ipotesi di convergenza totale:
    
    1. $|f_n(x)|\leq a_n,\forall x$
    2. $\sum^{+\infty}a_n<+\infty$
    
    $$\begin{aligned}
    \bigg|\int_a^b\sum_{n=k+1}^{+\infty}f_n(x)dx\bigg| &\leq \int_a^b\sum_{n=k+1}^{+\infty}|f_n(x)|dx\\\
    &\leq\int_a^b\bigg(\sum_{n=k+1}^{+\infty}a_n\bigg) dx = \sum_{n=k+1}^{+\infty}a_n\int_a^bdx = (b-a)\sum_{n=k+1}^{+\infty}a_n
    \end{aligned}$$
    
    Si afferma che:
    
    $$\lim_{k\to+\infty}\bigg[(b-a)\sum_{n=k+1}^{+\infty}a_n\bigg]=0$$
    
    
    Si osserva che:
    
    $$\sum_{n=0}^{+\infty}a_n<+\infty\implies \lim_{k\to+\infty}\sum_{n=k+1}^{+\infty}a_n=0$$
    
    
    
	Allora vale che:
    
    $$(b-a)
    \lim_{k\to+\infty}\sum_{n=k+1}^{+\infty}a_n=0\ _\blacksquare$$
    


 **Derivabilità termine a termine**

Sia $I\subseteq\mathbb R$ un intervallo e $f_n:I\to\mathbb R$. Se:

1. $f_n$ è derivabile in $I, \forall n\in\mathbb N$
2. La serie di termine generale $f_n$ converge totalmente in $I$
3. La serie di termine generale $f_n'$ converge totalmente in $I$

Allora la funzione somma:

$$f(x) = \sum^{+\infty} f_n(x)$$

è derivabile. Inoltre vale:

$$f'(x)=\bigg[\sum_{n=0}^{+\infty}f_n(x)\bigg]' = \sum_{n=0}^{ +\infty}f_n'(x)$$



## Serie di potenze


 Una **serie di potenze** è una serie di funzioni della forma:

$$\sum_{n=0}^{+\infty} a_n(x-x_0)^n = a_0 + a_1(x-x_0) + a_2(x-x_0)² + ... + a_n(x-x_0)^n + ...$$

con:

1. $a_n\in\mathbb R$ coefficienti della serie
2. $x_0\in\mathbb R$ centro della serie



 La serie geometrica $\sum_{n=0}^{+\infty}x^n$ è una serie di potenze avente $x_0=0, a_n=1, \forall n\in\mathbb N$.



Per convenzione, se $x=x_0$ e $n=0$, definiamo $(x_0-x_0)^0=1$, perciò:

$$\sum_{n=0}^{+\infty}a_n(x_0-x_0)^n=a_0\cdot 1 + \cancel{a_1\cdot0}+\cancel{a_2\cdot0}+...=a_0$$

Dunque, tutte le serie di potenze convergono almeno nel loro centro.

Facciamo un ragionamento formale: la serie geometrica $\sum_{n=0}^{+\infty}x^n$ è una particolare serie di potenze, avente $x_0=0, a_n=1, \forall n\in\mathbb N$ e converge nell’intervallo $(-1,1)$. Allora possiamo trarre due conclusioni:

- L’insieme di convergenza di $\sum_{n=0}^{+\infty}(x-x_0)^n$ è una traslazione di $(-1,1)$: $(-1 + x_0, 1 + x_0)$.
- Non si può determinare l’insieme di convergenza della generica serie di potenze $\sum_{n=0}^{+\infty}a_n(x-x_0)^n$ senza avere informazioni sui suoi coefficienti. Infatti l’insieme di convergenza di una serie è determinato dalla rapidità di convergenza della serie numerica dei coefficienti della serie stessa: $\sum_{n=0}^{+\infty}a_n$

Una particolarità delle serie di potenze è che il loro insieme di convergenza è sempre un intervallo centrato in $x_0$. Così sono possibili anche due casi limite:

1. L’intervallo di convergenza può essere costituito dal solo centro $x_0$
2. L’intervallo di convergenza è tutto $\mathbb R$


 **Raggio di convergenza di una serie di potenze reale**

Data una serie di potenze reale $\sum_{n=0}^{+\infty}a_n(x-x_0)^n$, si verifica sempre uno dei tre seguenti casi:

1. Il raggio di convergenza della serie è **nullo**: la serie converge solo per $x=x_0$
2. Il raggio di convergenza della serie è **infinito**: la serie converge assolutamente in tutto $\mathbb R$
3. Il raggio di convergenza è un numero **finito** **diverso da zero**:
    - La serie converge assolutamente $\forall x \in(x_0-R,x_0+R) \iff |x-x_0|<R$
    - La serie non converge per $|x-x_0|> R$


- **Dimostrazione 5**
    
    Vogliamo dimostrare che se la serie converge in un certo punto $x$, allora converge assolutamente per qualunque $y$ tale che $|y-x_0|<|x-x_0|$.
    
    Abbiamo due ipotesi:
    
    1. $\sum_{n=0}^{+\infty}
    a_n(x-x_0)^n<+\infty$
    2. $|y-x_0|<|x-x_0|$
    
    Dobbiamo dimostrare la tesi:
    
    $$\sum_{n=0}^{+\infty}
    \big|a_n(x-x_0)^n\big|<+\infty$$
    
    Dall’ipotesi i si deduce che:
    
    $$\lim_{n\to +\infty}\bigg[a_n(x-x_0)^n\bigg]=0$$
    
    perché termine generale di una serie convergente. Quindi, per $n$ sufficientemente grandi vale anche:
    
    $$\big|a_n(x-x_0)^n\big|\le1$$
    
    Stimiamo ora $\big|a_n(y-x_0)^n\big|$:
    
    $$\big|a_n(y-x_0)^n\big|=\bigg|a_n(x-x_0)^n\cdot{(y-x_0)^n\over (x-x_0)^n}\bigg|\leq\big|a_n(x-x_0)^n \big|\cdot\bigg|{y-x_0\over x-x_0}\bigg|^n$$
    
    Quindi vale:
    
    $$\big|a_n(y-x_0)^n\big|\leq\bigg|{y-x_0\over x-x_0}\bigg|^n$$
    
    E allora:
    
    $$\sum_{n=0}^{+\infty}\big|a_n(y-x_0)^n\big|\leq\sum_{n=0}^{+\infty}\bigg|{y-x_0\over x-x_0}\bigg|^n \implies q=\bigg|{y-x_0\over x-x_0}\bigg|\leq 1$$
    
    Che è una serie geometrica convergente. Allora, per il teorema del confronto, $\sum_{n=0}^{+\infty}\big|a_n(y-x_0)^n\big|$ è convergente$\ _\blacksquare$
    


 La convergenza sulla frontiera dell’insieme di convergenza va studiata caso per caso e non è predeterminabile a priori.




 **Calcolo del raggio di convergenza per una serie di potenze reale**

Data la serie di potenze $\sum_{n=0}^{+\infty}
a_n(x-x_0)^n$, abbiamo visto nel teorema precedente che esiste sempre $R\in [0,+\infty]$. Se i seguenti limiti esistono, lo si può calcolare così:

1. $\displaystyle R = \lim_{n\to+\infty}\bigg|{a_n\over a_{n+1}}\bigg|$
2. $\displaystyle R=\lim_{n\to+\infty}{1\over \sqrt[n]{|a_n|}}$


Si nota che il criterio della radice e del rapporto applicati alla serie numerica dei coefficienti forniscono $1/R$, cioè:

$$\begin{aligned}
\lim_{n\to+\infty}\sqrt[n]{|a_n|}&=l\\\
\lim_{n\to+\infty}\bigg|{a_{n+1}\over a_n}\bigg|&=l
\end{aligned}$$

dove $l=1/R$.

### Convergenza totale per una serie di potenze e conseguenze

Va notato che non si può affermare che la convergenza sia totale in $(x_0-R,x_0+R)$
. Anche nel caso in cui il raggio di convergenza sia infinito, non è detto che la serie converga in tutto $\mathbb R$.

Poiché $f(x)=a_n(x-x_0)^n$ sono continue $\forall n\in \mathbb N$ e la serie converge totalmente $\forall[a,b]\subset(x_0-R, x_0+R)$, allora la funzione somma è sicuramente continua ed integrabile termine a termine.

In aggiunta, la funzione somma è sempre derivabile ad ogni ordine e vale la formula di derivazione termine a termine.


 **Derivabilità ed integrabilità termine a termine per una serie di potenze reale**

Sia $\sum_{n=0}^{+\infty}a_n(x-x_0)^n$ una serie di potenze reale avente raggio di convergenza $0<R\le+\infty$ e somma $f(x)$, con $x\in(x_0-R, x_0+R)$. Allora:

1. La funzione somma $f(x)$ è continua in $x\in(x_0-R, x_0+R)$. In particolare, è integrabile in ogni $[a,b]\subset(x_0-R, x_0+R)$ ed inoltre vale la formula di integrabilità termine a termine:
    
    $$\int_a^bf(x)dx = \int_a^b\sum_{n=0}^{+\infty}a_n(x-x_0)^n dx=\sum_{n=0}^{+\infty}a_n\int_a^b(x-x_0)^n dx$$
    
    Similmente, $f$ ammette primitiva in $(x_0-R,x_0+R)$:
    
    $$\int_{x_0}^xf(s)ds = \sum_{n=0}^{+\infty}a_n\int_{x_0}^x(s-x_0)^n ds$$
    
    Inoltre, il raggio di convergenza della serie integrata è anch’esso $R$.
    
2. $f(x)$ è derivabile nell’intervallo di convergenza $(x_0-R, x_0+R)$ ed inoltre vale la formula di derivabilità termine a termine:
    
    $$f'(x)=\sum_{n=0}^{+\infty}\big[a_n(x-x_0)^n\big]'
     = \sum_{n=0}^{+\infty}na_n(x-x_0)^{n-1}$$
    
    Il raggio di convergenza della serie derivata è anch’esso $R$. Inoltre, $f(x)$ è derivabile infinite volte e ad ogni passaggio si può applicare la formula di derivazione termine a termine.
    


## Serie di Taylor

Sia data una funzione $f(x)$ e supponiamo di sapere che essa è la somma di una serie di potenze in un intervallo $(a,b)$ non vuoto, cioè:

$$f(x) = \sum_{n=0}^{+\infty}a_n(x-x_0)^n, \forall n\in(a,b), x_0\in(a,b)$$

Individuiamo i seguenti aspetti:

- Qual è la regolarità minima di $f$?
    
    $f$ è derivabile almeno infinite volte, ma non vale il vicevesa: non è detto che $f(x)$  sia sviluppabile in serie di Taylor intorno a $x_0$.
    
- Cosa sono i coefficienti $a_n$?
    
    Possiamo scoprirlo determinando $a_0$. Per farlo, calcoliamo $f(x_0)$:
    
    $$\begin{aligned}
    f(x_0) &= \sum_{n=0}^{+\infty}a_n(x_0-x_0)^n = a_0\\\
    f'(x_0) &= \sum_{n=0}^{+\infty}na_n(x_0-x_0)^{n-1} = a_1\\\
    f''(x_0)&= \sum_{n=0}^{+\infty}n(n-1)a_n(x_0-x_0)^{n-2} = 2a_2
    \end{aligned}$$
    
    Quindi sappiamo che:
    
    $$\begin{aligned}
    a_0 &= f(x_0)\\\
    a_1 &= f'(x_0)\\\
    a_2 &= {1\over 2}f''(x_0)\\\
    ...\\\
    a_n &= {1\over n!} f^{(n)}(x_0)
    \end{aligned}$$
    

In conclusione: se $f(x)$  è sviluppabile in serie di potenze in un intervallo non vuoto $(a,b)$, con $x_0\in(a,b)$, allora necessariamente $f$ è derivabile infinite volte in $(a,b)$ ed inoltre tale serie è necessariamente la serie di Taylor:

$$f(x) = \sum_{n=0}^{+\infty}{f^{(n)}(x_0)\over n!}(x-x_0)^n, x\in(a,b)$$

Inoltre, $(a,b)\subseteq (x_0-R, x_0+R)$, dove $R$ è il raggio di convergenza della serie.

- **Dimostrazione 6**
    
    Controlliamo la convergenza della serie esponenziale:
    
    $$\sum_{n=0}^{+\infty}{x^n\over n!} = 1+x+{x^2\over 2} + {x^3\over 6}+...$$
    
    Il raggio di convergenza della serie è:
    
    $$\begin{aligned}
    R &= \lim_{n\to+\infty}{a_n\over a_{n+1}} =\\\
    &= \lim_{n\to+\infty}{(n+1)!\over n!} = \\\
    &= \lim_{n\to+\infty}(n+1) = \\\
    &= +\infty
    \end{aligned}$$
    
    Perciò possiamo concludere che la convergenza è semplice ed assoluta su tutto l’insieme $\mathbb R$ e totale $\forall[a,b]\subset \mathbb R$. Quindi:
    
    $$e^x = \sum_{n=0}^{+\infty}{x^n\over n!}, \forall x\in \mathbb R$$
    
- **Dimostrazione 7**
    
    Controlliamo la convergenza della serie logaritmica, calcolata integrando ${1\over 1+x}$:
    
    $$\ln(1+x) = \sum_{n=0}^{+\infty}(-1)^{n+1}{x^n\over n!}, x\in(-1, 1)$$
    
    Calcoliamo il raggio di convergenza della serie:
    
    $$\begin{aligned}
    R &= \lim_{n\to+\infty}{1\over\sqrt[n]{|a_n|}} =\\\
    &= \lim_{n\to+\infty}\sqrt[n]{n} = \\\
    &=1
    \end{aligned}$$
    
    Perciò la convergenza è semplice ed assoluta in $(-1,1)$ e totale $\forall[a,b]\subset(-1,1)$.
    
    Controlliamo il comportamento della serie sulla frontiera:
    
    - $x = 1$
        
        $$\sum_{n=0}^{+\infty}{(-1)^{n+1}\over n}$$
        
        Questa serie converge per il criterio di Leibniz, quindi la serie logaritmica converge per $x=1$.
        
    - $x=-1$
        
        $$\sum_{n=0}^{+\infty}{1\over n}$$
        
        Questa è la serie armonica con $\alpha= 1$, perciò diverge, il che implica che la serie logaritmica diverga per $x= -1$.
        
    
    Da questi calcoli possiamo concludere che l’insieme di convergenza puntuale della serie logaritmica è $E=(-1,1]$.
    

## Cenni alle serie di potenze complesse


 Una **serie di potenze in $\mathbb C$** è una serie di funzioni della forma:

$$\sum_{n=0}^{+\infty}a_n(z-z_0)^n = a_0+a_1(z-z_0)+a_2(z-z_0)^2+...+a_n(z-z_0)^n +...$$

Con:

1. $a_n\in \mathbb C$ coefficienti della serie
2. $z_0\in\mathbb C$ centro della serie
3. $z\in\mathbb C$ variabile



 **Raggio di convergenza di una serie di potenze complessa**

Data una serie di potenze $\sum_{n=0}^{+\infty}a_n(z-z_0)^n$, con $a_n, z, z_0\in\mathbb C$, si verifica sempre uno dei tre casi seguenti:

1. Raggio di convergenza nullo: la serie converge solo per $z=z_0$
2. Raggio di convergenza infinito: la serie converge assolutamente $\forall z\in \mathbb C$
3. Raggio di convergenza finito non nullo:
    - La serie converge assolutamente $\forall z\in \mathbb C:|z-z_0|<R$
    - La serie diverge per $|z-z_0|>R$



 Per calcolare il raggio di convergenza di una serie di potenze complessa resta valido il teorema *calcolo del raggio di convergenza di una serie di potenze reale*.



### Serie esponenziale complessa

La serie esponenziale complessa ha la seguente forma:

$$e^z=\sum_{n=0}^{+\infty}{z^n\over n!}, \forall z\in\mathbb C$$

Ponendo $z=ix\in\mathbb I$, si ottiene la formula di Eulero:

$$e^{ix} = \cos x+i\sin x$$

- **Dimostrazione facoltativa della formula di Eulero**
    
    $$\begin{aligned}
    e^{ix} &= \sum_{n=0}^{+\infty}{(ix)^n\over n!} = \\\
    &= 1+ix-{x^2\over2}-i{x^3\over6}+... = \\\
    &=\bigg(1-{x^2\over 2} + {x^4\over 4!}+...\bigg) + i\bigg(x-{x^3\over6} + {x^5\over5!}+...\bigg)=\\\
    &= \cos x+i\sin x \ _\blacksquare
    \end{aligned}$$
    

Valgono anche le due seguenti formule:

$$\begin{aligned}
\cos x&={e^{ix}+e^{-ix}\over2}\\\
\sin x&={e^{ix}-e^{-ix}\over2i}
\end{aligned}$$

Queste formule sono ottenute ponendo a sistema le seguenti equazioni:

$$\begin{aligned}
e^{ix} &= \cos x + i \sin x\\\
e^{-ix} &= \cos(-x) + i\sin(-x) = \\\
&= \cos x - i\sin x
\end{aligned}$$

Possiamo dire che la serie $\sum_{n=0}^{+\infty}a_nx^{n-1}$ sia una serie di potenze? Sì, purché parta da $1$. Infatti, cambiando indice:

$$\begin{aligned}
n-1=k&\implies k=n+1\\\
\sum_{n=1}^{+\infty}a_nx^{n-1} &= \sum_{k=0}^{+\infty}a_{k+1}x^k
\end{aligned}$$

## Serie di Fourier

La teoria di Fourier permette di approssimare una qualsiasi funzione periodica tramite combinazioni lineari infinite di funzioni trigonometriche, quali seni e coseni.


 La funzione $f:\mathbb R\to\mathbb R$ è periodica di periodo $T$ se $f(x) = f(x+T), \forall x\in \mathbb R$.




 Se $f$ è periodica di periodo $T$, allora è anche periodica di periodo $kT, k=2, 3, 4, ...$




 Solitamente, per noi, $T=2\pi$. Il nostro intervallo di interesse sarà $[-\pi,\pi]$.




 Nella definizione di funzione periodica non ci sono ipotesi di regolarità: la funzione può essere non derivabile o anche non continua.




 Se $f$ è dispari (o pari) in $[-\pi,\pi]$ e poi prolungata in modo periodico su $\mathbb R$, allora la funzione prolungata è anch’essa dispari (o pari).




 Chiamiamo **armoniche $n$-esime** le funzioni:

$$\cos(nx), \sin(nx), x\in\mathbb R, n=1,2,3,...$$

Queste funzioni sono periodiche di periodo $2\pi/n$.

Il caso speciale $n=0$ dà vita alla funzione costante $1$.




 Tutte le armoniche $n$-esime sono anche periodiche di periodo $2\pi$.



### Formule di ortogonalità

Di seguito, le tre formule di ortogonalità che useremo negli esercizi:

$$\begin{aligned}
\int_{-\pi}^\pi\cos(nx)\cos(kx)dx&=\begin{cases}0, &n\ne k\\\
\pi, &n=k\ne 0\end{cases}\\\
\int_{-\pi}^\pi\sin(nx)\sin(kx)dx&=\begin{cases}0, &n\ne k\\\
\pi, &n=k\ne 0\end{cases}\\\
\int_{-\pi}^\pi\sin(nx)\cos(kx)dx&=0, \forall n,k
\end{aligned}$$


 Se $n=k=0$, allora:

$$\int_{-\pi}^\pi dx = 2\pi$$



### Combinazione di armoniche per trovare la funzione approssimante

Per costruire la funzione approssimante, devo fare combinazioni lineari di armoniche.


 Un **polinomio trigonometrico** di ordine $m\in\mathbb N$ è una combinazione lineare finita di armoniche $n$-esime:

$$a_0+\sum_{n=1}^m\big[a_n\cos(nx)+b_n\sin(nx)\big]$$

Con:

1. $a_0, a_n, b_n$ coefficienti
2. $x\in\mathbb R$ variabile



 Ogni polinomio trigonometrico è periodico di periodo $2\pi$.




 La somma, la differenza ed il prodotto di due polinomi trigonometrici è ancora un polinomio trigonometrico.




 **Calcolo dei coefficienti di Fourier**

Se $f(x) = a_0+\sum_{n=1}^m\big[a_n\cos(nx)+b_n\sin(nx)\big]$, allora:

1. $\displaystyle a_0 = {1\over 2\pi}\int_{-\pi}^\pi f(x)dx$
2. $\displaystyle a_n = {1\over \pi}\int_{-\pi}^\pi f(x)\cos(nx)dx, \forall n = 1, ..., m$
3. $\displaystyle b_n = {1\over \pi}\int_{-\pi}^\pi f(x)\sin(nx)dx, \forall n = 1, ..., m$


- **Dimostrazione 8**
    
    Sfruttiamo le formule di ortogonalità per dimostrare questo teorema.
    
    Sappiamo che $f(x) = a_0+\sum_{n=1}^m\big[a_n\cos(nx)+b_n\sin(nx)\big]$.
    
    - Per calcolare $a_0$, si integra tra $-\pi$ e $\pi$:
        
        $$\begin{aligned}
        \int_{-\pi}^{\pi}f(x)dx &= \int_{-\pi}^\pi \bigg\\{a_0+\sum_{n=1}^m\big[a_n\cos(nx)+b_n\sin(nx)\big]\bigg\\}dx=\\\
        &=\int_{-\pi}^\pi a_0dx + \sum_{n =1}^ma_n\cancel{\int_{-\pi}^\pi \cos(nx)dx} + \sum_{n =1}^ma_n\cancel{\int_{-\pi}^\pi \sin(nx)dx} = \\\
        &= \int_{-\pi}^\pi a_0dx = \\\
        &= a_o\int_{-\pi}^\pi dx = \\\
        &= 2\pi a_0
        \end{aligned}$$
        
        Questo significa che:
        
        $$a_0 = {1\over 2\pi}\int_{-\pi}^\pi f(x)dx$$
        
    - Per calcolare $a_n$, si moltiplica l’identità per $\cos(nx)$ e si integra tra $-\pi$ e $\pi$:
        
        $$\begin{aligned}
        \int_{-\pi}^\pi f(x)\cos(nx)dx &= \int_{-\pi}^\pi \bigg\\{a_0+\sum_{k=1}^m\big[a_k\cos(kx)+b_k\sin(kx)\big]\bigg\\}\cos(nx)dx=\\\
        &= \cancel{a_0\int_{-\pi}^\pi\cos(nx)dx} + \sum_{k=1}^ma_k\int_{-\pi}^\pi\cos(kx)\cos(nx)dx + \sum_{k=1}^mb_k\cancel{\int_{-\pi}^\pi\sin(kx)\sin(nx)dx} = \\\
        &= a_n\int_{-\pi}^\pi\cos^2(nx)dx  =\\\
        &= a_n\pi
        \end{aligned}$$
        
        Questo significa che:
        
        $$a_n={1\over\pi}\int_{-\pi}^\pi f(x)\cos(nx)dx$$
        
    - Per calcolare $b_n$ si procede analogamente al passo precedente, moltiplicando per $\sin(nx)$ invece che per $\cos(nx)\ _\blacksquare$


 Il calcolo dei coefficienti segue le stesse formule anche nel caso di somma infinita.




 I coefficienti $1/\pi$ e $1/2\pi$ sono dovuti al fatto che:

- $\int_{-\pi}^\pi dx = 2\pi$
- $\int_{-\pi}^\pi \cos^2(nx)dx = \int_{-\pi}^\pi \sin^2(nx)dx = \pi$



 Alcuni libri scrivono anche:

$${a_0\over 2}+\sum_{n=1}^m\big[a_n\cos(nx)+b_n\sin(nx)\big], a_0 = {1\over\pi}\int_{-\pi}^\pi f(x)dx$$




 Un’osservazione importante per gli esercizi:

- Se $f$ è una funzione pari, si sviluppa in soli coseni, ossia $b_n=0\ \forall n$
- Se $f$ è una funzione dispari, si sviluppa in soli seni, ossia $a_n = 0\ \forall n$


### Serie trigonometrica

Poiché la somma di polinomi trigonometrici è ancora un polinomio trigonometrico, per avere speranze di approssimare una generica funzione periodica è necessario passare al limite $n\to+\infty$.


 Una **serie trigonometrica** è una serie nella forma:

$$a_0+\sum_{n=1}^{+\infty}\big[a_n\cos(nx)+b_n\sin(nx)\big]$$

Con $a_0, a_n,b_n\in\mathbb R$.




 **Convergenza di una serie trigonometrica a partire dai suoi coefficienti**

1. Se la serie numerica di termine generale $|a_n|+|b_n|$ è convergente, allora la serie trigonometrica converge totalmente in $\mathbb R$. Inoltre, la funzione somma è continua in $\mathbb R$ ed è possibile integrare termine a termine in ogni sottoinsieme limitato di $\mathbb R$:
    
    $$\int_{x_0}^x\bigg\\{a_0+\sum_{n=1}^{+\infty}\big[a_n\cos(nt)+b_n\sin(nt)\big]\bigg\\}dt = a_0(x-x_0)+\sum_{n=1}^{+\infty}\bigg[a_n\int_{x_0}^x\cos(nt)dt + b_n\int_{x_0}^x\sin(nt)dt\bigg]$$
    
2. Se la serie numerica di termine generale $n(|a_n|+|b_n|)$ è convergente, allora la funzione somma è derivabile su $\mathbb R$ ed è possibile derivare termine a termine su $\mathbb R$:
    
    $$\bigg\\{a_0+\sum_{n=1}^{+\infty}\big[a_n\cos(nx)+b_n\sin(nx)\big]\bigg\\}' = \sum_{n=1}^{+\infty}n\big[-a_n\sin(nx)+b_n\cos(nx)\big], \forall x\in\mathbb R$$
    


- **Dimostrazione 9**
    1. $|f_n(x)| = \big|a_0+\sum_{n=1}^{+\infty}\big[a_n\cos(nx)+b_n\sin(nx)\big]\big|\leq|a_0| + \sum_{n=1}^{+\infty}\big[|a_n|\underbrace{|\cos(nx)|}_{\leq1}+|b_n|\underbrace{|\sin(nx)|}_{\leq1}\big]\leq|a_0|+\sum_{n=1}^{+\infty}\big(|a_n|+|b_n|\big)$
        
        Quindi se la serie $\sum_{n=1}^{+\infty}\big(|a_n|+|b_n|\big)$ converge allora, per definizione di convergenza totale, la serie trigonometrica converge totalmente in $\mathbb R$. Grazie al teorema *conseguenze della convergenza totale*, la funzione somma è continua su $\mathbb R$ ed integrabile termine a termine sugli intervalli limitati.
        
    2. Sappiamo che $f_0(x) = a_0$ e che $f_n(x) = a_n\cos(nx)+b_n\sin(nx)$. Notiamo che sono tutte funzioni derivabili.
        
        Troviamo la derivata $f'_n(x) = -na_n\sin(nx)+nb_n\cos(nx)$.
        
        Confrontiamola con il termine generale: $|f'_n(x)|\leq n(|a_n|+|b_n|)$.
        
        Se la serie $\sum_{n=1}^{+\infty}n(|a_n|+|b_n|)$ converge allora, a maggior ragione, $\sum_{n=1}^{+\infty}(|a_n|+|b_n|)$ converge, quindi la funzione somma è derivabile termine a termine.
        
        Iterando: se $\sum_{n=1}^{+\infty}n^2(|a_n|+|b_n|)$ converge, allora la funzione somma può essere derivata due volte e vale la formula di derivazione termine a termine$\ _\blacksquare$
        


 Notare la differenza rispetto alle serie di potenze, che sono tutte derivabili infinite volte all’interno del raggio di convergenza.



### Serie di Fourier

Data una funzione $f:\mathbb R\to\mathbb R$ periodica, vogliamo approssimarla con una serie trigonometrica. I coefficienti $a_0, a_n, b_n$ vanno calcolati come nel teorema visto per somme finite, perciò serve qualche ipotesi di integrabilità su $f$.


 Sia $f:[-\pi,\pi]\to\mathbb R$.

Diciamo che $f$ è **regolare a tratti** nell’intervallo $[-\pi,\pi]$ se esistono un numero finito di punti $x_1 = -\pi, x_2, ...,x_{n-1}, x_n=\pi$ tali che:

1. $f$ è continua in $(x_i, x_{i+1}), \forall i=1, 2, ..., n-1$ ed esistono finiti i limiti $\lim_{x\to x_i^+}f(x), \forall i = 1, ..., n$ e $\lim_{x\to x_i^-}f(x)\forall i =2, ..., n$
2. $f$ è derivabile in $(x_i, x_{i+1}), \forall i=1, 2, ..., n-1$ ed esistono finiti i limiti $\lim_{x\to x_i^+}f'(x), \forall i = 1, ..., n$ e $\lim_{x\to x_i^-}f(x)\forall i =2, ..., n$



 Se $f$ è periodica di periodo $2\pi$ e regolare a tratti in $[-\pi,\pi]$, allora $f$è regolare a tratti in qualunque intervallo $[a,b]\subseteq\mathbb R$ limitato.




 Data $f:\mathbb R\to\mathbb R$ periodica di periodo $2\pi$ e regolare a tratti in $[-\pi,\pi]$, definiamo i **coefficienti di Fourier** di $f$ come:

1. $\displaystyle a_0 = {1\over 2\pi}\int_{-\pi}^\pi f(x)dx$
2. $\displaystyle a_n = {1\over \pi}\int_{-\pi}^\pi f(x)\cos(nx)dx, n = 1,2,3, ...$
3. $\displaystyle b_n = {1\over \pi}\int_{-\pi}^\pi f(x)\sin(nx)dx, n = 1,2,3, ...$

Chiamiamo **polinomio di Fourier** di ordine $m$ associato ad $f$ il polinomio:

$$F_m(x) =a_0+\sum_{n=1}^m\big[a_n\cos(nx)+b_n\sin(nx)\big]$$

Chiamiamo, invece, **serie di Fourier** associata ad $f$ il limite:

$$\lim_{m\to+\infty}F_m(x) =a_0+\sum_{n=1}^m\big[a_n\cos(nx)+b_n\sin(nx)\big]$$




 Non è detto che la funzione somma della serie di Fourier associata ad $f$ sia proprio $f$.



### Convergenza della serie di Fourier

Data $f$ periodica e regolare a tratti, vediamo dei risultati teorici che ci permettono di stabilire, senza bisogno di calcolare i coefficienti di Fourier:

- Per quali $x$ la sua serie di Fourier converge
- Per quali $x$ converge proprio a $f(x)$
- Se la convergenza è puntuale, totale...


 **Convergenza puntuale di una serie di Fourier**

Sia $f:\mathbb R\to\mathbb R$ periodica di periodo $2\pi$ e regolare a tratti in $[-\pi,\pi]$.

Allora, la serie di Fourier di $f$ converge puntualmente in tutto $\mathbb R$ ed inoltre:

$$\lim_{m\to+\infty}F_m(x) = {1\over2}\bigg[\lim_{s\to x^+}f(s) + \lim_{s\to x^-}f(s)\bigg]$$

cioè la serie di Fourier nel punto $x$ converge alla media tra $f(x^-)$ ed $f(x^+)$.




 Se $f$ è continua nel punto $x$, questo teorema ci dice in particolare che:

$$\lim_{m\to+\infty} F_m(x) = f(x)$$

cioè la serie di Fourier ha come somma nel punto $x$ proprio $f(x)$. Infatti, se $f$ è continua:

$${f(x^+) + f(x^-)\over 2} = {f(x)+f(x)\over 2} = f(x)$$

In particolare, se $f$ è continua su tutto $\mathbb R$, allora la serie di Fourier associata ad $f(x)$ converge proprio a $f(x), \forall x\in\mathbb R$.




 Ci servirà più avanti osservare che la convergenza puntuale in $x$ a $f(x)$ si scrive:

$$\lim_{m\to+\infty}|F_m(x)-f(x)|=0$$




 **Convergenza totale ed integrabilità termine a termine della serie di Fourier**

Sia $f:\mathbb R\to\mathbb R$ periodica di periodo $2\pi$ e regolare a tratti in $[-\pi, \pi]$.

Se inoltre $f$ è anche continua in $\mathbb R$, allora la serie di Fourier di $f$ converge totalmente ad $f$ in tutto $\mathbb R$.

In particolare, vale la formula di integrabilità termine a termine sui limitati.




 **Derivabilità termine a termine della serie di Fourier**

Sia $f:\mathbb R\to\mathbb R$ periodica di periodo $2\pi$ e derivabile su $\mathbb R$.

Sia $f'$ regolare a tratti in $[-\pi,\pi]$ e continua su $\mathbb R$.

Allora la serie di Fourier di $f$ è derivabile in $\mathbb R$ e vale la formula di derivazione termine a termine.



### Convergenza in norma (o media) quadratica

Si parte sempre da una funzione $f:\mathbb R\to\mathbb R$ periodica di periodo $2\pi$ e regolare a tratti in $[-\pi,\pi]$.

Abbiamo visto che non sempre si ha convergenza puntuale proprio a $f(x)$, cioè può accadere:

$$\lim_{m\to+\infty}F_m(x)\ne f(x) \iff \lim_{m\to+\infty}|F_m(x)-f(x)|\ne0$$

nel caso in cui $f$ sia discontinua in $x$.


 **Convergenza in norma quadratica della serie di Fourier**

Sia $f:\mathbb R\to\mathbb R$ periodica di periodo $2\pi$ e regolare a tratti in $[-\pi, \pi]$. Allora:

$$\lim_{m\to+\infty}\int_{-\pi}^\pi|F_m(x)-f(x)|^2dx = 0$$




 Si tratta di un nuovo tipo di convergenza che introduciamo solo per le serie di Fourier. È la convergenza più *naturale* per queste serie, infatti vale sempre, senza ipotesi aggiuntive.




 Sapendo che $\lim_{m\to+\infty}\int_{-\pi}^\pi|F_m(x)-f(x)|^2dx = 0$, concludo anche:

$$\int_a^b|F_m(x)-f(x)|^2dx = 0, \forall[a,b]\subseteq[-\pi, \pi]$$

perché:

$$\int_a^b|F_m(x)-f(x)|^2dx\leq\int_{-\pi}^\pi|F_m(x)-f(x)|^2dx$$

in quanto la funzione integranda è positiva. A posteriori, per periodicità:

$$\lim_{m\to+\infty}\int_a^b|F_m(x)-f(x)|^2dx = 0, \forall[a,b]$$




 **Identità di Parseval**

Sia $f:\mathbb R\to\mathbb R$ periodica di periodo $2\pi$ e regolare a tratti in $[-\pi, \pi]$.

Indicando con $a_0, a_n, b_n$ per $n\ge1$ i suoi coefficienti di Fourier, si ha:

$${1\over\pi}\int_{-\pi}^\pi|f(x)|^2dx = 2a_0^2+\sum_{n=1}^{+\infty}(a_n^2+b_n^2)$$



### Cenni: forma esponenziale della serie di Fourier

Dalla formula di Eulero abbiamo ricavato che:

$$\begin{aligned}
\cos x&={e^{ix}+e^{-ix}\over2}\\\
\sin x&={e^{ix}-e^{-ix}\over2i}
\end{aligned}$$

Trasformando $x$ in $nx$:

$$\begin{aligned}
\cos (nx)&={e^{inx}+e^{-inx}\over2}\\\
\sin (nx)&={e^{inx}-e^{-inx}\over2i}
\end{aligned}$$

Allora vale:

$$
\begin{align}
a_0 + \sum_{n=1}^{+\infty} \big[a_n\cos(nx) + b_n\sin(nx)\big] &= a_0 + \sum_{n=1}^{+\infty}\bigg(a_n{e^{inx}+e^{-inx}\over2}+ b_n{e^{inx}-e^{-inx}\over2i}\bigg) = \\\
&= a_0 + \sum_{n=1}^{+\infty}e^{inx}\bigg({a_n\over2}+{b_n\over2i}\bigg) +\underbrace{\sum_{n=1}^{+\infty}e^{-inx}\bigg({a_n\over2}-{b_n\over2i}\bigg)}_{\text{cambio indice: }n=-k} = \\\
&= a_0 + \sum_{n=1}^{+\infty}c_ne^{inx} + \sum_{k=-1}^{-\infty}c_ke^{-inx} = \\\
&= \sum_{n=-\infty}^{+\infty}c_ne^{inx}
\end{align}
$$

Non approfondiamo $c_n={1\over2\pi}\int_{-\pi}^\pi f(x)e^{-inx}dx$.
