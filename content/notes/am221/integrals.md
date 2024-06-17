---
title: 'Calcolo integrale per funzioni di più variabili'
draft: false
type: 'page'
toc: true
mathjax: true
---

---

## Integrali doppi su regioni semplici


$D\subseteq\mathbb R^2$ è detta **regione $y$-semplice** se:

$$D=\{(x,y)\in\mathbb R^2:x\in[a,b], g_1(x)\le y\le g_2(x)\}$$

con $[a,b]$ limitato e $g_1\le g_2$ continue in $[a,b]$.




$D\subseteq\mathbb R^2$ è detta **regione $x$-semplice** se:

$$D=\{(x,y)\in\mathbb R^2:y\in[c,d], h_1(y)\le x\le h_2(y)\}$$

con $[c,d]$ limitato e $h_1\le h_2$ continue in $[c,d]$.




Una regione $y$-semplice è colorabile con segmenti verticali e potrebbe non essere colorabile con segmenti orizzontali.

Viceversa per le regioni $x$-semplici.

Le regioni semplici sono sempre chiuse e limitate.



### Interpretazione geometrica dell’integrale doppio

L’integrale doppio di una funzione $f$ su un intervallo $[a,b]$ rappresenta il volume sotteso al grafico di $f$ con segno.


Non riusciremo a visualizzare gli integrali tripli, perché sono oggetti che vivono in $\mathbb R^4$.




Come calcolo l’area di una regione $y$-semplice $D$?

$$\text{Area}(D)=\int_a^b\big[g_2(x)-g_1(x)\big]dx$$

Analogamente, per regioni $x$-semplici:

$$\text{Area}(D)=\int_c^d\big[h_2(y)-h_1(y)\big]dy$$




Sia $D$ una regione semplice. Come calcolo il volume del solido che ha $D$ come basi ed altezza $h$?

$$\text{Volume}=\text{Area}(D)\cdot h$$

Ricordando l’interpretazione dell’integrale doppio:

$$\begin{align*}
\text{Volume}&=\text{Area}(D)\cdot h=\\\
&=\iint_Dh\ dxdy
\end{align*}$$

dove $h$ è una funzione costante. Sappiamo già integrare le funzioni costanti su regioni semplici:

$$\begin{align*}
\iint_Dh\ dxdy &= h\cdot\text{Area}(D) = \\\
&= h\int_a^b\big[g_2(x)-g_1(x)\big]dx\ \text{Area }y\text{-semplice}
\end{align*}$$

Se $h=1$:

$$\iint_Ddxdy=\text{Area}(D)$$



Dobbiamo ora porci alcune domande:

### Quali altre funzioni sono integrabili su regioni semplici, oltre alle costanti?


**Integrabilità di funzioni continue**

Siano $D\subseteq\mathbb R^2$ una regione semplice e $f:D\to\mathbb R$ continua in $D$.

Allora, $f$ è integrabile su $D$, cioè:

$$\iint_Df(x,y)dxdy<+\infty$$




Se $D$ è un’unione di regione semplici, si può integrare sui vari pezzi separatamente.



### Come calcolare l’integrale nel caso un cui $f$ non sia costante?

Si usano le **formule di riduzione**:

- $D$ regione $y$-semplice
    
    Sia $D$ una regione $y$-semplice:
    
    $$D=\{(x,y)\in\mathbb R^2:x\in[a,b], g_1(x)\le y\le g_2(x)\}$$
    
    Sia $f:D\to\mathbb R$ continua in $D$, allora:
    
    $$\iint_Df(x,y)dxdy=\int_a^b\bigg[\int_{g_1(x)}^{g_2(x)}f(x,y)dy\bigg]dx$$
    
- $D$ regione $x$-semplice
    
    Sia $D$ una regione $x$-semplice:
    
    $$D=\{(x,y)\in\mathbb R^2:y\in[c,d],h_1(y)\le x\le h_2(y)\}$$
    
    Sia $f:D\to\mathbb R$ continua in $D$, allora:
    
    $$\iint_Df(x,y)dxdy=\int_c^d\bigg[\int_{h_1(y)}^{h_2(y)}f(x,y)dx\bigg]dy$$
    

In pratica (per regioni $y$-semplici, ma analogo per le $x$-semplici):

1. Si *affetta* $D$ in verticale
2. Per ogni $\overline x\in[a,b]$ si ha che $f(\overline x,y)$ è una funzione nella sola variabile $y$
3. Si integra questa funzione di una variabile sul segmento:
    
    $$\int_{g_1(x)}^{g_2(x)}f(\overline x,y)dy$$
    
    questa quantità dipende da $\overline x$.
    
4. Si ripetono i punti precedenti $\forall\overline x=x\in[a,b]$: si ottiene una funzione che dipende solo da $x$:
    
    $$J(x)=\int_{g_1(x)}^{g_2(x)}f(x,y)dy$$
    
5. Infine, si integra $J(x)$ su $[a,b]$:
    
    $$\iint_Df(x,y)dxdy=\int_a^bJ(x)=\int_a^b\bigg[\int_{g_1(x)}^{g_2(x)}f(x,y)dy\bigg]dx$$
    


Le formule di riduzione trasformano un integrale doppio in due integrali singoli monodimensionali annidati.

In generale, due integrali annidati non sono uguali al prodotto dei due integrali:

$$\iint_Dxydxdy=\int_a^b\bigg[\int_{g_1(x)}^{g_2(x)}xydy\bigg]dx\ne\bigg(\int_a^bxdx\bigg)\cdot\bigg(\int_{g_1(x)}^{g_2(x)}ydy\bigg)$$

Si ottiene il prodotto di due integrali se e solo se:

1. $f(x,y)=f_1(x)\cdot f(y)$
2. $g_1(x)=c, g_2(x)=d, \iint_Df(x,y)dxdy=\int_c^df_2(y)dy\cdot\int_a^bf_2(x)dx$


### Passaggio alle coordinate polari

Se $E\subseteq\mathbb R^2$ è a simmetria radiale, può essere comodo passare in coordinate polari prima di integrare.

Supponiamo che $E=B_R(0)$:

$$\begin{align*}
\phi(r,\theta)&=\begin{pmatrix}r\cos\theta\\\r\sin\theta\end{pmatrix}\\\
E&=\{(x,y)\in\mathbb R^2:\sqrt{x^2+y^2}\le R\}\\\
D&=\{(r,\theta)\in\mathbb R^2:\theta\in[0,2\pi), r\in[0,R]\}
\end{align*}$$

Sappiamo che $\iint_Ef(x,y)dxdy\ne\iint_Df(r\cos\theta,r\sin\theta)drd\theta$. Infatti già in dimensione uno:

$$\int f(x)dx=\int f\big(\phi(t)\big)\phi'(t),\ \phi(t) \text{ derivabile e monotona}$$

Per una mappa $\phi:\mathbb R^2\to\mathbb R^2$, la derivata è una matrice: la **matrice jacobiana**:

$$J_\phi(r,\theta)=\begin{pmatrix}
{\partial\phi_1\over\partial r} & {\partial\phi_1\over\partial\theta}\\\
{\partial\phi_2\over\partial r} & {\partial\phi_2\over\partial\theta}
\end{pmatrix}=\begin{pmatrix}
\cos\theta & -r\sin\theta\\\
\sin\theta & r\cos\theta
\end{pmatrix}$$

In pratica, si corregge l’integrale sostituendo:

$$dxdy=|\det J_\phi(r,\theta)|drd\theta = rdrd\theta$$

Quindi l’integrale risulta:

$$\iint_Ef(x,y)dxdy=\iint_Df(r\cos\theta,r\sin\theta)rdrd\theta,\ r=|\det J_\phi(r,\theta)|$$

## Integrali tripli

Vediamo come integrare una funzione di tre variabili in una regione dello spazio:

$$\iiint_Df(x,y,z)dxdydz,\ D\subseteq\mathbb R^3$$

- Interpretazione fisica dell’integrale triplo
    
    Se $D$ è un corpo rigido nello spazio, $f(x,y,z)$ rappresenta la sua densità di massa, perciò:
    
    $$\text{massa}(D)=\iiint_Df(x,y,z)dxdydz$$
    
    Il baricentro di $D$ è il punto di coordinate $(x_B,y_B,z_B)$, che si ottengono integrando:
    
    $$\begin{align*}
    x_B&={1\over\text{massa}(D)}\iiint_Dxf(x,y,z)dxdydz\\\
    y_B&={1\over\text{massa}(D)}\iiint_Dyf(x,y,z)dxdydz\\\
    z_B&={1\over\text{massa}(D)}\iiint_Dzf(x,y,z)dxdydz
    \end{align*}$$
    
    Un caso particolare può essere quello di una lamina piana $D\subseteq\mathbb R^2$, in cui $f$ non dipende da $z$.
    

In questa sezione vedremo:

### Integrazione per fili su regioni semplici dello spazio

Con questo metodo, si svolge prima un integrale singolo e poi un integrale doppio.


$E\subseteq\mathbb R^3$ è detta regione $z$-semplice se:

$$E=\{(x,y,z)\in\mathbb R^3:(x,y)\in D=\text{regione semplice del piano }xy, h_1(x,y)\le z\le h_2(x,y), h_1, h_2 \text{ continue}\}$$




**Integrazione per fili**

Se $E$ è una regione $z$-semplice ed $f:E\to\mathbb R$ è una funzione continua:

$$\iiint_Ef(x,y,z)dxdydz=\iint_D\bigg[\int_{h_1(x,y)}^{h_2(x,y)}f(x,y,z)dz\bigg]dxdy$$




Può essere richiesto di integrare in regioni $x$-semplici o $y$-semplici di $\mathbb R^3$. In tal caso, basta adattare la formula.



### Integrazione per strati su regioni generiche dello spazio

Con questo metodo, si svolge prima un integrale doppio e poi un integrale singolo.

Le regioni su cui si usa l’integrazione per strati non devono necessariamente essere regioni semplici, ma devono prestarsi ad essere *affettate*. Una regione di questo tipo è:

$$E=\{(x,y,z)\in\mathbb R^3:a\le z\le b, (x,y)\in E_z\text{ regioni semplici}\}$$

Alcuni esempi pratici di regioni di questo tipo sono cilindri e coni.

La formula di integrazione per strati è la seguente:

$$\iiint_Ef(x,y,z)dxdydz=\int_a^b\bigg[\iint_Ef(x,y,z)dxdy\bigg]dz$$

### Passaggio alle coordinate sferiche

Così come negli integrali doppi si può passare alle coordinate polari nel caso di una regione con simmetria radiale, possiamo fare lo stesso nello spazio nel caso di integrali tripli, aggiungendo una coordinata e un angolo e modificando la matrice jacobiana per renderla di ordine tre.

Il passaggio in coordinate sferiche avviene secondo questo sistema:

$$\begin{cases}
x=r\sin\varphi\cos\theta\\\
y=r\sin\varphi\sin\theta\\\
z=r\cos\theta
\end{cases}, \varphi\in(0,\pi), \theta\in[0,2\pi), |\det J_\phi(r,\theta,\varphi)|=r^2\sin\varphi>0, \forall r,\theta,\varphi$$
