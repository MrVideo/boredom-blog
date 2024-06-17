---
title: 'Ottimizzazione'
draft: false
type: 'page'
toc: true
mathjax: true
---

---

## Derivate seconde per funzioni di due variabili


Siano $A\subseteq\mathbb R^2$ aperto, $f:A\to\mathbb R$ derivabile.

Supponiamo che le due derivate parziali

$${\partial f\over\partial x}(x,y),\ {\partial f\over\partial y}(x,y)$$

siano a loro volta derivabili in $A$.

Definiamo le derivate parziali seconde di $f$:

$$\begin{matrix}
{\partial^2f\over\partial x^2}={\partial\over\partial x}\big({\partial f\over\partial x}(x,y)\big) & {\partial^2f\over\partial y\partial x}={\partial\over\partial y}\big({\partial f\over\partial x}(x,y)\big)\\\
{\partial^2f\over\partial x\partial y}={\partial\over\partial x}\big({\partial f\over\partial y}(x,y)\big) & {\partial^2f\over\partial y^2}={\partial\over\partial y}\big({\partial f\over\partial y}(x,y)\big)
\end{matrix}$$

Diciamo che $f$ è derivabile due volte in $(x_0,y_0)\in A$ se esistono le quattro derivate parziali seconde in $(x_0, y_0)$.

In questo caso, le derivate seconde si organizzano in una matrice, detta **hessiana**:

$$H_f(x_0,y_0) = \begin{pmatrix}
{\partial^2f\over\partial x^2}={\partial\over\partial x}\big({\partial f\over\partial x}(x,y)\big) & {\partial^2f\over\partial y\partial x}={\partial\over\partial y}\big({\partial f\over\partial x}(x,y)\big)\\\
{\partial^2f\over\partial x\partial y}={\partial\over\partial x}\big({\partial f\over\partial y}(x,y)\big) & {\partial^2f\over\partial y^2}={\partial\over\partial y}\big({\partial f\over\partial y}(x,y)\big)
\end{pmatrix}$$




Se $(x_0,y_0)$ è fissato, allora $H_f(x_0,y_0)$  è una matrice numerica.

Se $(x,y)$ è variabile, allora $H_f(x,y)$  è una matrice di funzioni.




$f:A\subseteq\mathbb R^2\to\mathbb R$ è detta di classe $C^2$ su $A$, e si scrive $f\in C^2(A)$, se:

1. $f$ è derivabile due volte in tutti i punti di $A$
2. Tutte le derivate parziali seconde di $f$ sono continue in $A$


In pratica:

- $f\notin C^1(A)\implies f\notin C^2(A)$
- Se $f$ contiene termini quali $(x-x_0)^\alpha, (y-y_0)^\alpha, |x-x_0|^\alpha, |y-y_0|^\alpha$, con $0<\alpha<2$, potrebbe non essere di classe $C^2$


**Teorema di Schwartz**

Siano $A\subseteq\mathbb R^2$ aperto ed $f\in C^2(A)$. Allora:

$${\partial^2f\over\partial y\partial x}(x,y)= 
{\partial^2f\over\partial x\partial y}(x,y),\ \forall(x,y)\in A$$

cioè $H_f(x,y)$  è una matrice simmetrica $\forall(x,y)\in A$.




Se $f\in C^2(A)$, allora $\forall\underline{x_0}\in A$ si ha che $H_f(\underline{x_0})$  è una matrice $2\times2$ simmetrica e posso associarle la forma quadratica indotta da $H_f(\underline{x_0})$ :

$$\begin{align*}
&q:\mathbb R^2\to\mathbb R\\\
&q(h_1, h_2) = \begin{pmatrix}h_1& h_2\end{pmatrix}H_f(\underline{x_0})\begin{pmatrix}h_1\\\h_2\end{pmatrix}
\end{align*}$$

Con una notazione più compatta:

$$\begin{align*}
q(\underline h) &= \underline h^TH_f(\underline{x_0}) \underline h = \\\
&=\ <\underline h, H_f(\underline{x_0}) \underline h>,\ \underline h=\begin{pmatrix}h_1\\\h_2\end{pmatrix}
\end{align*}$$

Esplicitando $q$:

$$\begin{align*}
q(h_1,h_2)&=\begin{pmatrix}h_1&h_2\end{pmatrix}\begin{pmatrix}{\partial^2f\over\partial x^2}(\underline{x_0})& {\partial^2f\over\partial x\partial y}(\underline{x_0})\\\
{\partial^2f\over\partial x\partial y}(\underline{x_0})& {\partial^2f\over\partial y^2}(\underline{x_0})\end{pmatrix}\begin{pmatrix}h_1\\\h_2\end{pmatrix}=\\\
&=\begin{pmatrix}h_1&h_2\end{pmatrix}\begin{pmatrix}{\partial^2f\over\partial x^2}(\underline{x_0})h_1& {\partial^2f\over\partial x\partial y}(\underline{x_0})h_2\\\
{\partial^2f\over\partial x\partial y}(\underline{x_0})h_1& {\partial^2f\over\partial y^2}(\underline{x_0})h_2\end{pmatrix}=\\\
&= {\partial^2f\over\partial x^2}(\underline{x_0})h_1^2 + 2{\partial^2f\over\partial x\partial y}(\underline{x_0})h_1h_2 + {\partial^2f\over\partial y^2}(\underline{x_0})h_2^2
\end{align*}$$



## Sviluppo in serie di Taylor al secondo ordine per funzioni di due variabili

Ricordiamo lo sviluppo in serie di Taylor per una funzione di una variabile arrestato all’ordine due: se $f$ è derivabile due volte in $x_0$, allora:

$$f(x_0+h) = f(x_0)+f'(x_0)h+{f''(x_0)\over2}h^2+o(h^2), \text{con}\lim_{h\to0}{o(h^2)\over h^2}=0$$


**Formula di Taylor al secondo ordine**

Siano $A\subseteq\mathbb R^2$ aperto e $f\in C^2(A)$. Allora, $\forall\underline{x_0}\in A$ vale la formula:

$$f(\underline{x_0}+\underline h) = f(\underline{x_0})+<\nabla f(\underline{x_0}), \underline h>+{1\over2}<\underline h, H_f(\underline{x_0})\underline h>+\ o(||\underline h||^2)$$




Ponendo $\underline{x_0}+\underline h = \underline x$:

$$f(\underline x) = f(\underline{x_0})+<\nabla f(\underline{x_0}), \underline x-\underline{x_0}>+{1\over2}<\underline x-\underline{x_0}, H_f(\underline{x_0})(\underline x-\underline{x_0})>+\ o(||\underline x-\underline{x_0}||^2)$$



## Forme quadratiche in $\mathbb R^2$


Sia $A\in\mathbf M_{2,2}(\mathbb R)$ simmetrica.

La forma quadratica indotta da $A$ è la funzione $q:\mathbb R^2\to\mathbb R$:

$$q(\underline h)=\underline h^T\cdot A\cdot\underline h =\ <\underline h, A\underline h>,\ \underline h\in\mathbb R^2$$

Più esplicitamente, se $A = \begin{pmatrix}a&b\\\b&c\end{pmatrix}$:

$$\begin{align*}
q(h_1,h_2)&=\begin{pmatrix}h_1&h_2\end{pmatrix}\begin{pmatrix}a&b\\\b&c\end{pmatrix}\begin{pmatrix}h_1\\\h_2\end{pmatrix} = \\\
&= \begin{pmatrix}h_1&h_2\end{pmatrix}\begin{pmatrix}ah_1&bh_2\\\bh_1&ch_2\end{pmatrix} = \\\
&= ah_1^2+2bh_1h_2+ch_2^2
\end{align*}$$

Equivalentemente, una forma quadratica in $\mathbb R^2$ è un polinomio di due variabili $(h_1,h_2)$ formato solo da monomi di grado due.




Una forma quadratica in $\mathbb R^n$ è un polinomio di $n$ variabili $(h_1, ..., h_n)$ formato solo da monomi di grado due.




Tutte le forme quadratiche si annullano nell’origine:

$$q(\underline0)=q(0,0)=0$$




Il segno della forma quadratica $q:\mathbb R^2\to\mathbb R$ (o equivalentemente della matrice simmetrica $A$) è:

- **Definito**
    - **Positivo** se $q(\underline h)>0, \forall \underline h\ne\underline 0$
    - **Negativo** se $q(\underline h)<0, \forall \underline h\ne\underline 0$
- **Semidefinito**
    - **Positivo** se:
        
        $$\begin{cases}
        q(\underline h)\ge 0, \forall\underline h\in\mathbb R^2\\\
        \exists\underline{h_0}\ne\underline 0:q(\underline{h_0})=0
        \end{cases}$$
        
    - **Negativo** se:
        
        $$\begin{cases}
        q(\underline h)\le 0, \forall\underline h\in\mathbb R^2\\\
        \exists\underline{h_0}\ne\underline 0:q(\underline{h_0})=0
        \end{cases}$$
        
- **Indefinita** se esistono $\underline{h_1}, \underline{h_2}\in\mathbb R^2:q(\underline{h_1})>0, q(\underline{h_2})<0$



**Segno di una forma quadratica ed autovalori**

Sia $A\in\mathbf M_{2,2}(\mathbb R)$ simmetrica e $q$ la forma quadratica indotta. Allora:

- $q$ è **definita** positiva (o negativa) se e solo se tutti gli autovalori di $A$ sono strettamente positivi (o negativi)
- $q$ è **semidefinita** positiva (o negativa) se e solo se un autovalore di $A$ è nullo e l’altro è strettamente positivo (o negativo)
- $q$ è **indefinita** se e solo se $A$ ha autovalori di segno opposto diversi da zero


### Criterio per determinare il segno di una forma quadratica in $\mathbb R^2$

Prendiamo la forma quadratica:

$$q(h_1, h_2)=ah_1^2+2bh_1h_2+ch_2^2,\ A = \begin{pmatrix}a&b\\\b&c\end{pmatrix},\ a\ne0$$

Possiamo dire che:

- $q$ è **definita** se e solo se $\det A> 0$. In particolare:
    - $q$ è definita positiva se e solo se $\det A>0 \land a>0$
    - $q$ è definita negativa se e solo se $\det A>0 \land a < 0$
- $q$ è **semidefinita** se e solo se $\det A=0$. In particolare:
    - $q$ è semidefinita positiva se e solo se $\det A = 0\land a > 0$
    - $q$ è semidefinita negativa se e solo se $\det A = 0\land a < 0$
- $q$ è **indefinita** se e solo se $\det A<0$.

Nel caso in cui $a=0$ ma $c\ne0$, valgono le stesse affermazioni considerando $c$ al posto di $a$.

## Richiami di ottimizzazione in una dimensione


**Teorema di Weierstrass**

Sia $f:[a,b]\to\mathbb R$ continua, allora esistono:

- $x_m\in[a,b]$ punto di minimo assoluto
- $x_M\in[a,b]$ punto di massimo assoluto

Cioè:

$$f(x_m)\le f(x)\le f(x_M), \forall x\in[a,b]$$




Se $f$ tende a $\pm\infty$, non ammette massimo o minimo.




**Teorema di Fermat**

Sia $f:(a,b)\to\mathbb R$ derivabile.

Se $x_0$ è punto di massimo o minimo (globale o locale), per $f$ in $(a,b)$:

$$f'(x_0)=0$$



## Introduzione all’ottimizzazione in due dimensioni


Sia $A\subseteq\mathbb R^2$ un sottoinsieme qualunque e sia $f:A\to\mathbb R$.

Un punto $(x_0,y_0)\in A$ si dice:

- Punto di massimo locale o relativo per $f$ in $A$ se esiste $\delta>0$ tale che:
    
    $$f(x_0,y_0)\ge f(x,y), \forall(x,y)\in B_\delta(x_0,y_0)\cap A$$
    
    Il valore $f(x_0,y_0)$ è detto valore di massimo locale o relativo.
    
- Punto di massimo globale o assoluto per $f$ in $A$ se:
    
    $$f(x_0,y_0)\ge f(x,y), \forall(x,y)\in A$$
    
    Il valore $f(x_0,y_0)$ è detto valore di massimo globale o assoluto.
    

Analogamente si definiscono i punti di minimo ed i valori di minimo, cambiando i versi delle disuguaglianze.




Alcune osservazioni:

- I punti di massimo appartengono al piano $(x,y)$, mentre i valori di massimo appartengono all’asse $z$
- I punti di massimo appartengono all’insieme $A$ e possono essere interni o di frontiera
- Il valore di massimo assoluto, se esiste, è unico, ma può essere assunto da più di un punto

Valgono le stesse considerazioni per i punti ed i valori di minimo.




**Teorema di Weierstrass**

Sia $f:A\subseteq\mathbb R^2\to\mathbb R$ continua, con $A$ chiuso e limitato.

Allora $f$ assume i valori di massimo e minimo assoluto in $A$, cioè esistono:

- $(x_m, y_m)\in A$ punto di minimo assoluto
- $(x_M, y_M)\in A$ punto di massimo assoluto

Cioè:

$$f(x_m,y_m)\le f(x,y)\le f(x_M,y_M), \forall(x,y)\in A$$




I valori di massimo e minimo assoluto di $f$ in $A$ dipendono da $A$. Nel caso in cui $A=\mathbb R$, allora $f$ non ammette massimo o minimo assoluto.



## Ottimizzazione libera

In questa sezione, considereremo insiemi $A$ aperti. Per questo, sicuramente il teorema di Weierstrass non è valido, ma vale invece il teorema di Fermat:


**Teorema di Fermat**

Siano $A\subseteq\mathbb R^2$ aperto ed $f:A\to\mathbb R$.

Sia $(x_0,y_0)$ punto di estremo per $f$ e supponiamo che $f$ sia derivabile in $(x_0,y_0)$. Allora:

$$\nabla f(x_0, y_0) = \begin{pmatrix}0\\\0\end{pmatrix}$$



- **Dimostrazione 15**
    
    Vogliamo dimostrare che:
    
    $${∂f\over∂x}(x_0,y_0) = {∂f\over∂y}(x_0,y_0)=0$$
    
    utilizzando il teorema di Fermat per funzioni di una variabile.
    
    Poiché $A$ è aperto, $(x_0 ,y_0 )$ è interno ad $A$, quindi esiste $\delta > 0$ tale che $B_\delta(x_0,y_0)\subseteq A$.
    
    Pongo $g_1(x)=f(x,y_0)$.
    
    $g_1$ è anch’essa definita in un aperto: $(x_0-\delta,x_0+\delta)$.
    
    $x_0$ è un punto estremale anche per $g_1$.
    
    $g_1$ è derivabile poiché:
    
    $$g_1'(x_0) = {∂f\over∂x}(x_0,y_0)=0$$
    
    Analogamente, $g_2(y)=f(x_0,y)$ e $g_2'(y_0)={∂f\over∂y}(x_0,y_0)=0_\blacksquare$
    


Siano $A\subseteq \mathbb R^2$ aperto e $f:A\to\mathbb R$ derivabile in almeno $(x_0,y_0)\in A$.

Chiamiamo $(x_0,y_0)$ **punto critico** (o punto stazionario) se:

$$\nabla f(x_0,y_0)=\begin{pmatrix}0\\\0\end{pmatrix}$$




Nelle ipotesi del teorema di Fermat: punto estremale $\implies$ punto critico.




Di solito, per noi, $f$ sarà differenziabile in tutto $A$.

Se, in aggiunta alle ipotesi del teorema di Fermat, $f$ è differenziabile in $(x_0,y_0)$, allora:

1. Il piano tangente al grafico in $\big(x_0,y_0,f(x_0,y_0)\big)$ è orizzontale:
    
    $$z = f(x_0,y_0)+\cancel{<\nabla f(x_0,y_0),\begin{pmatrix}x-x_0\\\y-y_0\end{pmatrix}>} = f(x_0,y_0)$$
    
2. $\displaystyle\forall\underline v\in\mathbb R^2:||\underline v||=1, {∂f\over∂\underline v}(x_0,y_0)=<{∂f\over∂\underline v}(x_0,y_0), \underline v>=0$



Un punto critico di $f$ che non è estremale è detto **punto di sella**.



In pratica, se si cercano i punti estremanti di $f$ in un insieme aperto $A$:

- Se $f$ è derivabile in tutto $A$, si determinano i punti critici di $f$ in $A$ e si stabilisce quali sono di massimo, di minimo o di sella
- Se $f$ ha punti di non derivabililtà, essi vanno studiati separatamente

### Classificazione dei punti critici

Data $f\in C^2(A)$ con $A$ aperto e $(x_0,y_0)\in A$ punto critico per $f$, come si distingue tra massimo locale, minimo locale o sella?


**Criterio della matrice hessiana**

Siano $A\subseteq\mathbb R^2$ aperto e $f\in C^2(A)$.

Sia $(x_0,y_0)\in A$ punto critico per $f$.

Denotiamo con $q$ la forma quadratica indotta da $H_f(x_0,y_0)$:

$$q(h_1,h_2)=<\begin{pmatrix}h_1&h_2\end{pmatrix}, H_f(x_0,y_0)\begin{pmatrix}h_1\\\h_2\end{pmatrix}>$$

1. Se $q$ è definita positiva, allora $(x_0,y_0)$ è punto di minimo locale
2. Se $q$ è definita negativa, allora $(x_0,y_0)$ è punto di massimo locale
3. Se $q$ è indefinita, allora $(x_0,y_0)$  è un punto di sella



Se $q$ è semidefinita, il criterio della matrice hessiana non dà informazioni.



Cosa fare se $\det H_f(x_0,y_0)=0$ ed il criterio della matrice hessiana non si applica?

- **Indagine diretta**
    
    Prendiamo la funzione $f(x,y)=x^4-6x^2y^2+y^4$. Si verifica che l’unico punto critico è $(0,0)$ e che $\det H_f(0,0)=0$.
    
    Restringiamo la funzione:
    
    - Restrizione a $y=0\implies f(x,0)=x^4 \implies$ positiva
    - Restrizione a $x=0\implies f(0,y)=y^4\implies$ positiva
    - Restrizione a $y=x\implies f(x,x)=-4x^4\implies$ negativa
    
    Poiché esiste una direzione lungo la quale $(0,0)$ è punto di minimo locale per la restrizione di $f$ in tale direzione ed un’altra direzione per cui lo stesso punto è di massimo locale per la restrizione di $f$, allora concludo che $(0,0)$ è punto di sella.
    

## Ottimizzazione vincolata

Nell’ottimizzazione vincolata si cercano i punti estremanti di una funzione in un insieme non aperto. Non è quindi sufficiente applicare Fermat, perché potrebbero esserci punti stazionari sulla frontiera dell’insieme di definizione.

La difficoltà sta nel fatto che in $\mathbb R^2$ il bordo di un insieme potrebbe essere complicato.

Se $A$ è chiuso e limitato, allora vale il teorema di Weierstrass, quindi:

1. Si applica il teorema di Fermat nell’insieme aperto $A\setminus(\text{bordo di }A)$
2. Si cercano eventuali punti estremanti sul bordo di $A$, detto **vincolo di uguaglianza**

### Vincoli di uguaglianza

In questa sezione, ci poniamo il problema di determinare i massimi ed i minimi di una funzione $f(x,y)$ quando il punto di $(x,y)$ verifica una condizione aggiuntiva, della forma $F(x,y)=0$. Il vincolo è l’insieme di livello della funzione $F(x,y)$.


Siano $A\subseteq\mathbb R^2$ aperto ed $f,F\in C^1(A)$. Poniamo:

$$z=\{(x,y)\in A:F(x,y)=0\}$$

Un punto $(x_0, y_0)\in z$ si dice:

- **Punto di massimo relativo** per $f$ vincolato a $z$ se esiste $\delta >0$ tale che:
    
    $$f(x_0,y_0)\ge f(x,y), \forall(x,y)\in B_\delta(x_0,y_0)\cap z$$
    
- **Punto di massimo assoluto** per $f$ vincolato a $z$ se:
    
    $$f(x_0,y_0)\ge f(x,y), \forall(x,y)\in z$$
    

Analogamente per le definizioni di punto di minimo relativo ed assoluto.

Un punto di massimo o minimo vincolato è detto **punto di estremo vincolato**.



- **Metodo di sostituzione**
    
    Nel modello di Cobb-Douglas, si vuole massimizzare la funzione profitto:
    
    $$p(x,y)=\sqrt{xy}$$
    
    dove $x$ è il lavoro ed $y$ è il capitale, con il vincolo di budget:
    
    $$F(x,y)={x\over2}+{y\over2}-1$$
    
    Dato il modello:
    
    $$\begin{cases}
    x,y\ge0\\\
    p(x,y)=\sqrt{xy}\\\
    z=\{(x,y)\in\mathbb R^2:x+y=2, x\ge0,y\ge0\}
    \end{cases}$$
    
    si usa la tecnica di sostituzione: si sostituisce il vincolo $y=2-x$ nell’espressione della funzione $p$:
    
    $$g(x)=\sqrt{x(2-x)}\\\
    \begin{cases}
    x=2-y\\\
    x\ge0\\\
    y\ge0
    \end{cases}\implies0\le x\le2\implies x\in[0,2]$$
    
    Cerchiamo ora il massimo globale della funzione monodimensionale $g(x)$ in $[0,2]$:
    
    $$\begin{align*}
    g(0)&=g(2)=0\\\
    g'(x)&=0\iff x=1
    \end{align*}$$
    
    La funzione $g$ ha un unico punto di massimo globale in $x=1$.
    
    La funzione $p$ vincolata a $z$ ha punto di massimo globale in $(x_0,2-x_0)=(1,1)$.
    
    Il valore massimo assoluto di $p$ vincolata a $z$ è $1$.
    


Il metodo di sostituzione non è sempre applicabile. Ad esempio, quando il vincolo non è esplicitabile. In altri casi è possibile applicarlo, ma si rischia di sbagliare.



Un consiglio:

- Se il vincolo è lineare, si può usare la sostituzione
- Se il vincolo non è lineare, si usi il metodo dei moltiplicatori di Lagrange


**Metodo dei moltiplicatori di Lagrange**

Siano $A\subseteq\mathbb R^2$ aperto e $f,F\in C^1(A)$.

Sia $(x_0,y_0)$ un punto di estremo vincolato per $f$ con vincolo:

$$z=\{(x,y)\in\mathbb R^2:F(x,y)=0\}$$

Supponiamo inoltre che:

$$\nabla F(x_0,y_0)\ne0$$

Allora esiste $\lambda_0$, detto moltiplicatore di Lagrange, tale che:

$$\nabla f(x_0,y_0)=\lambda_0\nabla F(x_0, y_0)$$




Scriviamo in modo più esplicito:

$$\begin{cases}
{∂f\over∂x}(x_0,y_0)=\lambda_0{∂F\over∂x}(x_0,y_0)\\\
{∂f\over∂y}(x_0,y_0)=\lambda_0{∂F\over∂y}(x_0,y_0)
\end{cases}$$

Di fatto, negli esercizi va risolto un sistema di tre equazioni:

$$\begin{cases}
{∂f\over∂x}(x_0,y_0)=\lambda{∂F\over∂x}(x_0,y_0)\\\
{∂f\over∂y}(x_0,y_0)=\lambda{∂F\over∂y}(x_0,y_0)\\\
F(x,y)=0
\end{cases}$$

Le incognite di questo sistema sono $x,y,\lambda$. In generale, è un sistema non lineare.

Il caso $\lambda = 0$ è ammissibile.

Se $\nabla f(\underline{x_0})=\lambda_0\nabla F(\underline{x_0}), \lambda_0\ne0$, allora i due vettori sono paralleli, mentre se $\lambda_0=0$, $\underline{x_0}$ è un punto critico libero di $f$, con $\underline{x_0}\in z$.



#### Confronto tra teorema di Fermat e moltiplicatori di Lagrange

|  | Fermat | Lagrange |
| --- | --- | --- |
| Ambito di utilizzo | Ottimizzazione libera | Ottimizzazione vincolata con vincolo di uguaglianza |
| Afferma che, sotto opportune ipotesi | $$\underline{x_0} \text{ punto di estremo} \implies \nabla f(\underline{x_0})=\underline 0$$ | $$\underline{x_0} \text{ punto di estremo vincolato} \implies\nabla f(\underline{x_0})\parallel\nabla F(\underline{x_0}), \lambda_0\ne0$$ |
| Non è un se e solo se | $$\exists\underline{x_0} \text{ non di estremo con } \nabla f(\underline{x_0})=\underline 0\text{: i punti di sella}$$ | $$\exists\underline{x_0} \text{ non estremo vincolato tali che }\nabla f(\underline{x_0})\parallel\nabla F(\underline{x_0}) \text{: i flessi sulla curva}$$ |
