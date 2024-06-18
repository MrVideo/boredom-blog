---
title: "Stabilità"
draft: false
type: 'page'
toc: true
mathjax: true
---

---

Possiamo applicare il concetto di stabilità ad equilibri, movimenti e talvolta a sistemi.

## Stabilità di un equilibrio

Sia $\overline x$ uno stato di equilibrio per il SD $\dot x=f(x,u)$, con $u=\overline u$ costante. Si verifica sempre uno di questi tre casi:

1. **Equilibrio stabile**: l'equilibrio è stabile (*S*) se:$$\forall\epsilon>0,\exists\delta>0:||x(0)-\overline x||<\delta\implies||x(t)-\overline x||<\epsilon,\forall t\geq0$$
2. **Equilibrio asintoticamente stabile**: l'equilibrio è asintoticamente stabile (*AS*) se è stabile e:$$||x(t)-\overline x||\to0\text{ per } t\to+\infty$$
3. **Equilibrio instabile**: l'equilibrio è instabile (*I*) se non viene rispettata nessuna delle condizioni precedenti.

## Stabilità nei SD LTI a TC

Consideriamo il SD LTI $\dot x=Ax+bu$.

Sia $\overline x$ uno stato di equilibrio per $u=\overline u$ costante. Allora:

$$\begin{cases}x(0)=\overline x\\\\u(t)=\overline u,\ t\geq0\end{cases}\implies x(t)=\overline x,\ t\geq 0$$

quindi:

$$x(t)=e^{At}\overline x+\int_0^te^{A(t-\tau)}b\overline ud\tau=\overline x$$

Consideriamo ora il movimento perturbato $x_\Delta(t)$ prodotto da $x(0)=\overline x+\Delta\overline x$ e $u(t)=\overline u$:

$$x_\Delta(t)=e^{At}(\overline x+\Delta\overline x)+\int_0^te^{A(t-\tau)}b\overline ud\tau$$

Quindi:

$${x_\Delta(t)-\overline x}={e^{At}\Delta\overline x}$$

in cui la parte a sinistra dell'uguale rappresenta la traiettoria che $x_\Delta$ compie rispetto a $x$. Inoltre, la parte a destra dell'uguale non dipende dal particolare $\overline x$.

Come si vede da questo risultato, **tutti gli equilibri hanno le stesse caratteristiche di stabilità**.

Dunque, nei sistemi LTI, la stabilità è una proprietà del sistema e dipende soltanto dal comportamento di $e^{At}$, cioè dalla matrice $A$.

### Proprietà dei SD LTI AS

1. I ML di $x$ e $y$ tendono a 0 per $t\to+\infty$, quindi tali SD *dimenticano* lo stato iniziale
2. Se:$$u(t)=\begin{cases}\text{qualsiasi segnale},&t<\overline t\\\\0,&t\geq\overline t\end{cases}$$allora, a partire da $\overline t$, c'è soltanto il ML e quindi $x,y\to0$ per $t\to+\infty$.

## Stabilità di un SD LTI e matrice $A$

Riassumiamo i tre possibili casi di stabilità:
1. **AS**: il ML di $x$ tende a 0 per $t\to+\infty$
2. **I**: il ML di $x$ diverge per $t\to+\infty$, salvo eccezioni
3. **S**: il ML non tende a 0, né diverge
Che ruolo ha la matrice $A$ in questi casi?

### Matrice $A$ diagonalizzabile a TC

Consideriamo il ML di $x$:$$\begin{align}x_L(t)&=e^{At}x(0)\\\\&=T\begin{bmatrix}e^{\lambda_1t}&&\\\\&\ddots&\\\\&&e^{\lambda_nt}\end{bmatrix}T^{-1}\end{align}$$
Se la matrice $A$ è reale, allora gli autovalori $\lambda_i$ sono o reali o coppie di numeri complessi coniugati:
1. Se $\lambda_i$ è **reale** abbiamo tre casi:
	1. $\lambda_i>0$: il modo $e^{\lambda_it}$ diverge, quindi $x_L$ diverge
	2. $\lambda_i=0$: il modo $e^{\lambda_it}$ è costante
	3. $\lambda_i<0$: il modo $e^{\lambda_it}\to0$
2. Se $\lambda_{h,k}$ sono due numeri **complessi coniugati**:$$\lambda_{h,k}=\alpha\mp j\beta, \alpha,\beta\in\mathbb{R}\implies e^{(\alpha+j\beta)t}=e^{\alpha t}\underbrace{\big(\cos(\beta t)+j\sin(\beta t)\big)}_{\text{limitato}}$$e allora:$$\begin{cases}\Re(\lambda)<0\implies\text{il modo converge}\\\\\\Re(\lambda)=0\implies\text{il modo è limitato ma non tende a 0}\\\\\\Re(\lambda)>0\implies\text{il modo diverge}\end{cases}$$
Quindi, in conclusione:
- Tutti gli autovalori di $A$ hanno $\Re<0$ $\iff$ il sistema è **AS**
- Almeno un autovalore di $A$ ha $\Re>0$ $\implies$ il sistema è **I**
- Tutti gli autovalori di $A$ hanno $\Re\leq0$ ed almeno uno ha $\Re=0$ $\implies$ il sistema è o **I** o **S**, ma non può essere **AS**

### Matrice $A$ diagonalizzabile a TD

Il ML di un SD a TD è:$$x_L(k)=A^kx(0)$$
Consideriamo $A^k$:$$\begin{align}A^k&=\bigg(T\begin{bmatrix}\lambda_1&&\\\\&\ddots&\\\\&&\lambda_n\end{bmatrix}T^{-1}\bigg)^k\\\\&=T\underbrace{\begin{bmatrix}\lambda_1^k&&\\\\&\ddots&\\\\&&\lambda_n^k\end{bmatrix}}_{\text{modi del sistema}}T^{-1}\end{align}$$
Allora:
- $|\lambda_i|<1,\forall i\iff$ sistema **AS**
- $\exists i:|\lambda_i|>1\implies$ sistema **I**
- $\begin{cases}|\lambda_i|\leq1,\forall i\\\\\\exists i:|\lambda_i|=1\end{cases}\implies$ sistema **I** o **S**, non **AS**

## Criteri di stabilità asintotica per SD LTI a TC

Data la matrice A, posso sapere se tutti i suoi autovalori hanno $\Re<0$ senza calcolarli?
Esistono dei criteri per affermarlo, basati sull'ispezione di $A$ o del suo polinomio caratteristico (*PC*) $\pi(s)=\det(S\mathbb I-A)$.
1. $\det A=\pi(s_i)$. $\det A=0\implies\exists s_i=0\implies$ sistema **non AS**
2. $\text{Tr } A=\sum s_i = \sum\Re(s_i)$. $\text{Tr }A>0\implies\exists s_i:\Re(s_i)>0\implies$ sistema **I**
3. $\Re(s_i)<0,\forall i$ (sistema **AS**) $\implies$ i coefficienti di $\pi(s)$ sono tutti concordi e non nulli

### Criterio di Routh

Il criterio di Routh dà una condizione **necessaria e sufficiente** (*CNS*) per la stabilità asintotica di un SD LTI a TC (l'analogo a TD è il *criterio di Jury*).
Si basa sulla tabella di Routh, che si costruisce dal PC $\pi(s)$:$$\begin{cases}\begin{matrix}a_0&a_2&\ldots&a_{n-1}&\text{oppure}&a_n\\\\a_1&a_3&\ldots&a_n&&0\\\\h_1&h_2&\ldots&\ldots&\ldots&\ldots\\\\q_1&q_2&\ldots&\ldots&\ldots&\ldots\\\\w_1&w_2&\ldots&\ldots&\ldots&\ldots\end{matrix}&&n+1\text{ righe}\end{cases}$$
Le prime due righe contengono i coefficienti del PC, mentre ogni riga dalla terza in poi dipende dalle due precedenti, secondo la seguente regola:$$w_i=-{1\over q_1}\det\begin{bmatrix}h_1&h_{i+1}\\\\q_1&q_{i+1}\end{bmatrix}$$
Gli elementi eventualmente mancanti alla fine delle righe si assumono nulli.

#### Enunciato del criterio di Routh

Un SD con PC $\pi(s)$ è **AS** $\iff$ **tutti gli elementi della prima colonna della tabella di Routh sono concordi**

##### Corollario

Se non vi sono elementi nulli sulla prima colonna, il numero di inversioni di segno è uguale al numero di radici di $\pi(s)$ con $\Re>0$.
