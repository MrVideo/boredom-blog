---
title: 'Sistemi differenziali lineari'
draft: false
type: 'page'
toc: true
mathjax: true
---

---


Un **sistema differenziale lineare** di ordine $n$ è un sistema di $n$ equazioni differenziali ordinarie lineari del primo ordine:

$$\begin{cases}
y_1'(t) = a_{11}(t)y_1(t) + ... + a_{1n}(t)y_n(t)+b_1(t)\\\
...\\\
y_n'(t) = a_{n1}(t)y_1(t) + ... + a_{nn}(t)y_n(t) + b_n(t)
\end{cases}$$

dove:

1. $y_i:I\subseteq\mathbb R\to\mathbb R$ sono funzioni incognite
2. $\begin{aligned}
\underline{y}:I\subseteq \mathbb R&\to\mathbb R^n\\\
t &\mapsto 
\begin{bmatrix}
y_1(t)\\\
...\\\
y_n(t)
\end{bmatrix}
\end{aligned}$ è un vettore di funzioni
3. $a_{ij}:J\subseteq\mathbb R\to\mathbb R$ sono funzioni continue assegnate
4. $b_i:J\subseteq\mathbb R\to\mathbb R$ sono funzioni continue assegnate

Possiamo scrivere l'equivalente del sistema in forma matriciale come segue:

$$\underline{y'}(t)=A(t)\underline{y}(t)+\underline{b}(t)$$

dove:

1. $\underline{y}(t) = \begin{bmatrix} y_1(t) \\\ ... \\\ y_n(t)\end{bmatrix}$
2. $\underline b(t) = \begin{bmatrix}b_1(t)\\\ ...\\\b_n(t)\end{bmatrix}$
3. $A(t) = \begin{bmatrix}a_{11}(t) & ... & a_{1n}(t)\\\
... & ... & ...\\\
a_{n1}(t) & ... & a_{nn}(t)\end{bmatrix}$

con $t\in\mathbb R,\  \underline y(t),\underline b(t)\in\mathbb R^n,\  A(t)\in\mathbf M_{n\times n}(\mathbb R)$.



Va notato che:


 Un sistema che deriva da un'equazione differenziale del secondo ordine ha come prima riga di $A\in\mathbf M_{m\times n}(\mathbb R)$ sempre $\begin{bmatrix} 0 & 1 \end{bmatrix}$.



## Problema di Cauchy per un sistema differenziale lineare


 Dato il sistema differenziale lineare $\underline y'(t)=A(t)\underline y(t)+\underline b(t)$, con $a_{ij},b_i$ continue in $J\subseteq\mathbb R$, un **problema di Cauchy** è:

$$\begin{cases}
\underline y'(t) = A(t)\underline y(t)+\underline b(t)\\\
\underline y(t_0)=\underline {y_0}
\end{cases}$$

con $t_0\in J, \underline{y_0}\in\mathbb R^n$.



## Teorema di esistenza e unicità globale per il problema di Cauchy per sistemi differenziali lineari


 Dato il sistema differenziale lineare $\underline y'(t)=A(t)\underline y(t)+\underline b(t)$, con $A,\underline b$ continue in $J\subseteq\mathbb R$ ed assegnati $t_0\in J$ e $\underline{y_0}\in\mathbb R^n$, il problema di Cauchy:

$$\begin{cases}
\underline y'(t)=A(t)\underline y(t) + \underline b(t)\\\
\underline y(t_0) = \underline{y_0}
\end{cases}$$

ha un'unica soluzione $y(t)$ definita $\forall t\in J$.



Questo teorema ha alcune importanti conseguenze:

1. Se il sistema differenziale è omogeneo, ossia se $\underline b(t)=\underline 0 \ \forall t\in J$, il problema di Cauchy:
    
    $$\begin{cases}
    \underline y' = A\underline y\\\
    \underline y(t_0)=\underline 0
    \end{cases}$$
    
    ammette sempre almeno la soluzione nulla $\underline y(t)=\underline 0 \ \forall t \in J$. Inoltre, per il teorema precedente, è l'unica soluzione.
    
2. Se $A\in \mathbf M_{n\times n}(\mathbb R)$ e $\underline b \in \mathbb R^n$, posto il problema di Cauchy:
    
    $$\begin{cases}
    \underline y'=A\underline y+\underline b\\\
    \underline y(t_0) =\underline{y_0}
    \end{cases}$$
    
    $J=\mathbb R$ e la soluzione $\underline y(t)$ è definita su tutto $\mathbb R$.
    

## Principio di sovrapposizione per sistemi differenziali lineari


 Sia $A(t)\in\mathbf M_{n\times n}$ una matrice di funzioni continue.

L'operatore $\mathbf L$ tale che:

$$\underline y \to \mathbf L\underline y = \underline y' - A(t)\cdot\underline y$$

è **lineare**, cioè se:

$$\begin{cases}
\underline y_1'=A(t)\cdot\underline y_1+\underline b_1(t)\\\
\underline y_2'=A(t)\cdot\underline y_2+\underline b_2(t)
\end{cases}$$

allora vale:

$$(c_1\underline y_1 + c_2\underline y_2)' = A(t)\cdot(c_1\underline y_1 + c_2\underline y_2)+c_1\underline b_1(t)+c_2\underline b_2(t), \forall c_1,c_2\in\mathbb R$$

Equivalentemente:

$$\begin{cases}
\mathbf L_1\underline y_1=\underline b_1(t)\\\
\mathbf L_2\underline y_2=\underline b_2(t)
\end{cases}
\implies\mathbf L(c_1\underline y_1+c_2\underline y_2) = c_1\underline b_1(t) + c_2\underline b_2(t), \forall c_1,c_2\in\mathbb R$$



## Struttura dell'integrale per sistemi differenziali lineari omogenei


 Sia $A(t)\in\mathbf M_{n\times n}$ una matrice di funzioni continue.

L'integrale generale del sistema differenziale lineare omogeneo $\underline y'(t) = A(t)\cdot\underline y(t)$ è uno **spazio vettoriale di dimensione $n$**, cioè generato da $n$ soluzioni **linearmente indipendenti**.



## Matrice Wronskiana


 Dato un sistema differenziale lineare $n\times n$ omogeneo, chiamiamo **sistema fondamentale di soluzioni** $n$ soluzioni linearmente indipendenti:

$$\underline y_{01}(t), \underline y_{02}(t),...,\underline y_{0n}(t)$$

Queste soluzioni costituiscono una **base** dello spazio vettoriale delle soluzioni.



Detto questo, possiamo ora definire un utile strumento per la risoluzione dei sistemi differenziali lineari: la **matrice Wronskiana**:


 Chiamiamo **matrice Wronskiana** la matrice ottenuta affiancando tutte le soluzioni che costituiscono un sistema fondamentale di soluzioni per un sistema differenziale lineare:

$$W(t) = \begin{bmatrix}\underline y_{01}(t) & \underline y_{02}(t) & ... & \underline y_{0n}(t)\end{bmatrix}$$

La matrice Wronskiana è una **matrice di funzioni**.

Direttamente dall'algebra lineare, se $\det W\ne 0\ \forall t\in J$, le $n$ soluzioni del sistema sono **linearmente indipendenti**.



Leghiamo queste due definizioni attraverso un teorema:

### Determinante Wronskiana


 Sia $A(t)\in\mathbf M_{n\times n}$ una matrice di funzioni continue su $J\subseteq\mathbb R$.

Dato il sistema differenziale omogeneo:

$$\underline y'(t) = A(t)\cdot\underline y(t)$$

siano $\underline y_{01}(t), \underline y_{02}(t),...,\underline y_{0n}(t)$ $n$ soluzioni.

Le $n$ soluzioni costituiscono un **sistema fondamentale di soluzioni** se e solo se $\exists t_0\in J$ tale che:

$$\det W(t) = \det\begin{bmatrix}\underline y_{01}(t) & \underline y_{02}(t) & ... & \underline y_{0n}(t)\end{bmatrix} \ne 0$$



---

## Sistemi differenziali lineari non omogenei

### Struttura dell'integrale generale per sistemi differenziali lineari non omogenei


 Sia $A(t)\in\mathbf M_{n\times n}$ una matrice di funzioni continue e $\underline b(t) \in \mathbb R^n$ un vettore di funzioni continue.

L'integrale generale del sistema differenziale lineare $\underline y'(t) = A(t)\cdot\underline y(t)+\underline b(t)$ è:

$$\underline y(t) = \underline y_0(t) + \underline y_P(t)$$

dove:

1. $\underline y_0(t)$ è l'integrale generale del sistema omogeneo associato
2. $\underline y_P(t)$ è una soluzione particolare del sistema completo


---

## Sistemi a coefficienti costanti

In questa sezione, vedremo come determinare l'integrale generale di un sistema differenziale omogeneo in due casi:

- $A\in\mathbf M_{n\times n}(\mathbb R)$ diagonalizzabile
    
    
     Ricordiamo che una matrice $A\in\mathbf M_{n\times n}(\mathbb R)$  è diagonalizzabile in $\mathbb R$ se e solo se:
    
    1. Esiste un insieme di $n$ autovettori di $A$ che forma una base di $\mathbb R^n$
    2. Tutti i suoi autovalori sono regolari
    
    Un autovalore è regolare se e solo se la sua *molteplicità algebrica*, ossia quante volte appare come radice del polinomio caratteristico, coincide con la sua *molteplicità geometrica*, la dimensione dell'autospazio associato.
    
    Può essere utile ricordare le seguenti condizioni sufficienti:
    
    1. Se $A\in\mathbf M_{n\times n}(\mathbb R)$  ha **$n$ autovalori reali distinti**, allora $A$ è diagonalizzabile
    2. Se $A\in\mathbf M_{n\times n}(\mathbb R)$  è **simmetrica**, allora $A$ è diagonalizzabile
    
    
    ### Integrale generale di un sistema con matrice diagonalizzabile
    
    
     Data $A\in\mathbf M_{n\times n}(\mathbb R)$  diagonalizzabile, con autovalori $\lambda_1, ...,\lambda_n$ e relativi autovettori $\underline v_1,...,\underline v_n$ linearmente indipendenti, un sistema fondamentale di soluzioni del sistema omogeneo $\underline y'(t) = A\underline y(t)$ è:
    
    $$\underline y_{01}(t) = e^{\lambda_1 t}\underline v_1,\underline y_{02}(t) = e^{\lambda_2 t}\underline v_2,...,\underline y_{0n}(t) = e^{\lambda_n t}\underline v_n$$
    
    Equivalentemente, l'integrale generale del sistema sarà:
    
    $$\underline y_0(t) = c_1e^{\lambda_1t}\underline v_1 + c_2e^{\lambda_2t}\underline v_2 +  ... + c_ne^{\lambda_nt}\underline v_n, \forall c_1,c_2,...,c_n\in\mathbb R$$
    
    
    
    - **Dimostrazione 3**
        
        Dobbiamo dimostrare che:
        
        1. Ciascuna $\underline y_{0i}(t) = c_ie^{\lambda_it}\underline v_i$ è soluzione del sistema
        2. $\underline y_{01}(t), \underline y_{02}(t),...,\underline y_{0n}(t)$ sono linearmente indipendenti
        
        Grazie al teorema di struttura, $n$ soluzioni linearmente indipendenti determinano univocamente l'integrale generale.
        
        1. Fissiamo un indice $i=1,...,n$. Devo verificare che:
            
            $$\underline y_{0i}' = A\underline y_{0i}$$
            
            Allora:
            
            $$\begin{aligned}
            \underline y_{0i}' &= (e^{\lambda_it}\underline v_i)' =\\\
            &= \lambda_ie^{\lambda_it}\underline v_i
            \end{aligned}$$
            
            Quindi:
            
            $$\begin{aligned}
            e^{\lambda_it}\lambda_i\underline v_i &= e^{\lambda_it}A\underline v_i =\\\
            &= Ae^{\lambda_it}\underline v_i=\\\
            &= A\underline y_{0i}(t)
            \end{aligned}$$
            
        2. Consideriamo ora la matrice ottenuta affiancando le soluzioni:
            
            $$M(t) = \begin{bmatrix}\underline y_{01}(t) & ... & \underline y_{0n}(t)\end{bmatrix}$$
            
            Scegliamo $t = t_0 = 0$ e sostituiamo:
            
            $$\begin{aligned}
            M(t) &= \begin{bmatrix}e^{\lambda_1 0}\underline v_1 & ... & e^{\lambda_n 0}\underline v_n\end{bmatrix} =\\\
            &=\begin{bmatrix} \underline v_1 & ... & \underline v_n\end{bmatrix}
            \end{aligned}$$
            
            Possiamo dire che $\det M(0) \ne 0$ poiché $\underline v_1,...,\underline v_n$ formano una base di $\mathbb R^n$ quindi, grazie al teorema del determinante Wronskiano, $\underline y_{01}(t),...,\underline y_{0n}(t)$ sono soluzioni linearmente indipendenti$\ _\blacksquare$
            
    
    
     Se $n=2$ ed il sistema deriva da un'equazione differenziale ordinaria di secondo ordine, allora è il caso $\Delta > 0$ descritto nel *MOOC*.
    
    
    
- $A\in\mathbf M_{2\times 2}(\mathbb R)$ con autovalori complessi coniugati
    
    ### Integrale generale di un sistema con matrice quadrata di ordine 2 con autovalori complessi coniugati
    
    
     Sia $A\in\mathbf M_{2\times 2}(\mathbb R)$ avente autovalori:
    
    $$\lambda, \overline\lambda\in\mathbb C, \Im(\lambda)\ne0$$
    
    Chiamiamo $\underline v\in\mathbb C^2$ l'autovettore associato a $\lambda$.
    
    Un sistema fondamentale di soluzioni del sistema omogeneo $\underline y'(t)=A\underline y(t)$ è:
    
    $$\begin{cases}
    \underline y_{01}(t)=\Re(e^{\lambda t}\underline v)\\\
    \underline y_{02}(t) = \Im(e^{\lambda t}\underline v)
    \end{cases}$$
    
    Equivalentemente, l'integrale generale del sistema è:
    
    $$\underline y_0(t) = c_1\Re(e^{\lambda t}\underline v)+c_2\Im(e^{\lambda t}\underline v), \forall c_1,c_2\in\mathbb R$$
    
    
    
    
     Se il sistema deriva da un'equazione differenziale ordinaria del secondo ordine, è il caso $\Delta <0$ descritto nel *MOOC*.
    
    Le funzioni trigonometriche $\sin,\cos$ corrispondono ad espoenziali complesse grazie alla **formula di Eulero**:
    
    $$e^{ix} = \cos x + i\sin x$$
    
    
    

### Nota: matrici quadrate di ordine 2

Esistono quattro casi possibili quando si incontra una matrice $2\times2$:

1. Matrice con due autovalori reali distinti: è diagonalizzabile
2. Matrice con due autovalori reali coincidenti in forma diagonale: è diagonalizzabile
3. Matrice con autovalori complessi coniugati: non è diagonalizzabile
4. Matrice non multipla dell'identità con due autovalori coincidenti: non è diagonalizzabile

Considerando i casi (i) e (ii), troveremo delle soluzioni esponenziali.

Considerando il caso (iii), troveremo soluzioni in forma:

$$e^{\alpha t}\cos(\beta t), e^{\alpha t}\sin(\beta t)$$
