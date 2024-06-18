---
title: 'Stima Bayesiana'
draft: false
type: 'page'
toc: true
mathjax: true
---

---

## Realtà e modelli

Per stimare un dato bisogna, per prima cosa, raccogliere dati dall'evento reale. I dati raccolti serviranno per costruire un modello dell'evento reale osservato. Tramite il modello trovato, è possibile costruire una stima e **fare delle previsioni**.

![](../images/mermaid1.png)

Le quantità da stimare possono essere discrete o continue.

Nel caso di quantità discrete, poiché queste possono assumere soltanto un numero limitato di valori, si applica il cosiddetto **test di ipotesi**, tramite il quale si cerca di capire quale dei valori che può assumere la variabile è quello effettivo.

> **Attenzione**
>
> Quando si applica il test di ipotesi, è necessario **avere poche ipotesi**, per riuscire a descrivere correttamente soltanto il fenomeno che si vuole modellare.

Generalmente, quando si applica il test di ipotesi, si hanno due sole ipotesi possibili: l'ipotesi **nulla** (anche detta ipotesi zero) e l'ipotesi uno. Ognuna delle due ipotesi deve essere mappata ad una probabilità concreta. Per farlo, si possono assegnare a ciascuna delle soglie e vedere in quale soglia ricade il dato osservato. Se per caso il dato ricadesse tra le due soglie, non si può concludere nulla ed è necessario continuare a raccogliere dati.

Nel caso di quantità continue, invece, si ricorre direttamente alla stima.

Esistono due tipi di stima: la stima **classica** e la stima **Bayesiana**.

## Tipi di stima: modelli di inferenza

Esistono generalmente due tipi di modelli di inferenza: l'approccio classico e l'approccio Bayesiano.

### Approccio classico

L'approccio classico misura, tramite una legge di probabilità che dipende dal numero da stimare $\theta$, la probabilità che un certo evento avvenga.

Un esempio di stima classica è la stima della massa dell'elettrone. Per stimare la massa dell'elettrone possiamo formulare un modello di questo tipo:

$$X=\theta + Z$$

Dove $\theta$ è la massa effettiva dell'elettrone, mentre $Z$ è il rumore termico che disturba la misura. Possiamo ipotizzare che $Z \sim N(0,1)$.

Lo strumento di misura non è altro che la variabile aleatoria $X$, che ha come densità di probabilità:

$$f_X(x;\theta) = {1\over\sqrt{2\pi}}e^{-{(x-\theta)^2\over2}}$$

Per stimare $\theta$ necessitiamo di uno strumento che elabori le misure che abbiamo raccolto tramite $X$: lo **stimatore** $\hat\Theta(X)$. Notare come il risultato che viene fornito dallo stimatore è a sua volta una variabile aleatoria funzione dello strumento di misura $X$.

### Approccio Bayesiano

L'approccio Bayesiano è fondamentalmente diverso da quello classico perché suppone che l'entità da misurare sia una variabile aleatoria.

Questo impone che lo strumento di misura non sia più una legge di probabilità incondizionata con un parametro numerico, bensì una legge di probabilità condizionata alla variabile aleatoria da stimare.

Riprendendo l'esempio della stima della massa dell'elettrone, possiamo modificare la legge dello strumento di misura in questo modo:

$$f_{X|\Theta}(x|\theta)$$

Da qui, si arriva di nuovo allo stimatore $\hat\Theta(X)$ e quindi alla stima della massa dell'elettrone.

#### Applicazione dell'inferenza Bayesiana

Guardiamo ora come applicare l'inferenza Bayesiana nei casi discreti e continui.

Supponiamo di avere una variabile aleatoria discreta $\Theta\in\{0,1\}$ dopo aver applicato il test di ipotesi.

In questo approccio, non abbiamo una conoscenza perfetta di $\Theta$, ma possiamo avere una conoscenza a priori di $\Theta$ da esperimenti precedenti, per esempio.

Dato che $\Theta$ è una variabile aleatoria binaria, possiamo sapere con che probabilità è zero o uno, perciò conosciamo $p_\Theta(0)=p$ e $p_\Theta(1)=1-p$. Possiamo dire allora:

$$\Theta\sim\text{Bern}(1-p)$$

Per costruire la conoscenza a posteriori di $\Theta$, è necessario costruire la legge a posteriori di questa variabile aleatoria dopo aver osservato $X$. Possiamo farlo applicando la [regola di Bayes](../bayes#regola-di-bayes-per-le-variabili-aleatorie). Se ipotizziamo che $X$ sia una variabile aleatoria continua:

$$p_{\Theta|X}(\theta|x) = {f_{X|\Theta}(x|\theta)\cdot p_\Theta(\theta)\over f_X(x)}$$

La funzione $f_{X|\Theta}(x|\theta)$ prende il nome di **funzione di verosimiglianza** (o *likelihood function*), poiché indica quanto sia verosimile ottenere $x$ allo strumento di misura in base al valore misurato di $\theta$.

Vediamo ora come applicare lo stesso metodo nel caso in cui $\Theta$ sia una variabile aleatoria continua.

È comunque possibile applicare la [regola di Bayes](../bayes#regola-di-bayes-per-le-variabili-aleatorie):

$$f_{\Theta|X}(\theta|x) = {f_{X|\Theta}(x|\theta)\cdot f_\Theta(\theta)\over f_X(x)}$$

Anche in questo caso, i fattori di questa equazione hanno nomi particolari:

- $f_{\Theta|X}(\theta|x)$ viene detta **densità a posteriori**
- $f_\Theta(\theta)$ viene detta **densità a priori**
- $f_{X|\Theta}(x|\theta)$ è la funzione di verosimiglianza, come nel caso discreto

Per calcolare il denominatore, possiamo applicare la [legge delle probabilità totali](../conditional-prob#teorema-delle-probabilità-totali):

$$f_X(x) = \int_{\mathbb R}f_{X|\Theta}(x|\theta')\cdot f_\Theta(\theta')d\theta'$$

#### Risultati dell'inferenza Bayesiana: stimatore MAP (*Maximum A Posteriori*)

Vediamo ora a che risultati ci porta la stima Bayesiana.

Nel caso di una variabile aleatoria $\Theta$ discreta, il risultato dell'inferenza è la legge a posteriori $p_{\Theta|X}$.

Per arrivare ad un solo numero che stimi il valore di $\Theta$ è possibile seguire diversi approcci. Una possibile stima può essere decidere l'**ipotesi con la massima probabilità a posteriori**.

Definiamo allora uno stimatore $\hat\Theta_\text{MAP}$, dove MAP sta per *Maximum A Posteriori*, in questo modo:

$$\hat\Theta_\text{MAP}(X) = \arg \max \big[p_{\Theta|X}(\theta|X)\big]$$

> In pratica, lo stimatore MAP è definito come il valore di $\Theta$ associato alla probabilità massima della legge a posteriori $p_{\Theta|X}$.

La stima MAP **minimizza la probabilità di errore a posteriori**.

Vediamo ora il caso in cui $\Theta$ sia una variabile aleatoria continua.

Lo stimatore MAP nel caso continuo è definito analogamente a quello discreto:

$$\hat\Theta_\text{MAP}(X) = \arg \max \big[f_{\Theta|X}(\theta|X)\big]$$

#### Stima ai minimi errori quadratici medi (*Least Mean Square*)

Un'altra buona stima di $\Theta$ può essere il valore atteso a posteriori $E[\Theta|X=x]$:

$$E[\Theta|X=x] = \int_{\mathbb R}\theta\cdot f_{\Theta|X}(\theta|x)d\theta$$

Questo ci porta a discutere della stima *Least Mean Square*.

La stima ai minimi errori quadratici medi risponde alla domanda:

> Qual è il valore di $\Theta$ che minimizza l'errore quadratico medio di stima?

L'errore di stima non è altro che la differenza tra il valore reale di $\theta$ ed il suo valore stimato $\hat\theta$. La stima LMS non fa altro che minimizzare il valore medio del quadrato di questo errore, cioè calcola $E\big[(\theta-\hat\theta)^2\big]$. Chiamiamo $\hat\theta = c$ ed il valore atteso descritto precedentemente $h(c)$. Per trovare il minimo di questa funzione, deriviamola:

$$\begin{aligned}
{d\over dc}h(c) &= {d\over dc}E\big[(\theta-c)^2\big]\\\
&= {d\over dc}E\big[\theta^2 -2c\theta +c^2\big]\\\
&= {d\over dc}\big(E[\theta^2] - 2cE[\theta] + c^2\big)\\\
&= -2E[\theta] + 2c
\end{aligned}$$

Per trovare il minimo della funzione, eguagliamola a zero. Troviamo:

$$c = E[\theta]$$

Ecco spiegato come mai una buona stima di $\Theta$ è il suo valore atteso.

Possiamo allora definire lo stimatore LMS come il valore atteso della variabile aleatoria che cerchiamo:

$$\hat\Theta_\text{LMS} = E[\theta]$$

Notiamo che l'errore quadratico medio minimo utilizzando lo stimatore LMS è pari alla varianza di $\theta$:

$$E\big[(\theta-\hat\Theta_\text{LMS})^2 \big] = E\big[(\theta - E[\theta])^2 \big] = \text{Var}[\theta]$$

##### Stima LMS basata sull'osservazione di $X$

Supponiamo di avere due variabili aleatorie $\Theta$ ed $X$ e di osservare $X=x$. Proviamo a trovare una costante $c$ tale che $E\big[(\Theta-c)^2|X=x\big]$ sia minimo.

È facile concludere che $c = E[\Theta|X=x] = \hat\Theta_\text{LMS}(X=x)$.

Così facendo, abbiamo dimostrato che:

$$E\big[(\Theta -\hat\Theta_\text{LMS})^2|X=x \big] \le E\big[(\Theta-g(x))^2|X=x \big], \ \forall x $$

Applicando la [legge dell'aspettativa totale](../drv#legge-dellaspettativa-totale), possiamo calcolare il valore del minimo errore quadratico medio:

$$\begin{aligned}
E\big[(\Theta - E[\Theta|X])^2 \big] &= E\big[E[(\Theta-E[\Theta|X])^2|X] \big]\\\
&= E\big[\text{Var}[\Theta|X] \big]\\\
&\le \text{Var}[\Theta]
\end{aligned}$$

##### Stima LMS con $n$ osservazioni di $X$

Possiamo estendere la stima LMS al caso in cui si abbiano più osservazioni di $X$ in questo modo:

$$\begin{aligned}
\hat\Theta_\text{LMS}(X_1,X_2,\ldots,X_n) &= E[\Theta|X_1,X_2,\ldots,X_n]\\\
&= \int_{-\infty}^\infty \theta\cdot f_{\Theta|X_1,X_2,\ldots,X_n}(\theta|X_1,X_2,\ldots,X_n)d\theta
\end{aligned}$$

Troviamo la legge a posteriori tramite la [regola di Bayes](../bayes#regola-di-bayes-e-funzioni-di-variabili-aleatorie):

$$f_{\Theta|X_1,X_2,\ldots,X_n}(\theta|X_1,X_2,\ldots,X_n) = {f_\Theta(\theta)\cdot f_{X_1,X_2,\ldots,X_n|\Theta}(x_1,x_2,\ldots,x_n|\theta)\over f_{X_1,X_2,\ldots,X_n}(x_1,x_2,\ldots,x_n)}$$

##### Stimatore lineare a minimo errore quadratico medio

Supponiamo di avere una variabile aleatoria continua $\Theta$. Vogliamo costruirne una **stima lineare**:

$$\hat\Theta_\text{LIN}(X) = aX + b$$

Per fare ciò, è necessario calcolare i due coefficienti $a$ e $b$ in modo da **minimizzare l'errore quadratico medio**:

$$\begin{aligned}
\{\}[a^\*, b^\*] &= \arg\min E\big[(\Theta-\hat\Theta_\text{LIN})^2 \big]\\\
&= \arg\min E\big[(\Theta-aX-b)^2 \big]
\end{aligned}$$

Dato che $E\big[(\Theta-aX-b)^2 \big]$ è una funzione quadratica in $a$ e $b$, per trovare i due fattori possiamo procedere derivando:

$$\begin{cases}
{∂\over∂a}E\big[(\Theta-aX-b)^2 \big] = 0\\\
{∂\over∂b}E\big[(\Theta-aX-b)^2 \big] = 0
\end{cases}$$

Risolvendo, troviamo:

$$\begin{cases}
a^* = {\text{Cov}[X,\Theta]\over\text{Var}[X]}\\\
b^* = E[\Theta] - a^*E[X]
\end{cases}$$

Possiamo allora definire lo stimatore lineare LMS come segue:

$$\hat\Theta_\text{LIN}(X) = E[\Theta] + {\text{Cov}[X,\Theta]\over\text{Var}[X]}\big(X-E[X]\big)$$

È anche possibile riscrivere lo stesso stimatore in questa forma:

$${\hat\Theta_\text{LIN}(X)-E[\Theta]\over\sigma_\Theta} = {\text{Cov}[X,\Theta]\over\sigma_\Theta\sigma_X}\cdot{X-E[X]\over\sigma_X} = \rho[\Theta,X]\cdot{X-E[X]\over\sigma_X}$$

In questo modo, possiamo valutare soltanto statistiche del primo e del secondo ordine di $X$ e $\Theta$.

Nel caso di più osservazioni di $X$, imponiamo di trovare una stima lineare nella forma:

$$\hat\Theta_\text{LIN} = a_1X_1+a_2X_2+\ldots+a_nX_n+b$$

Sempre con lo scopo di minimizzare l'errore quadratico medio.

Analogamente al caso di una singola osservazione, si può dimostrare che $a_1^\*,a_2^\*,\ldots,a_n^\*$ si possono calcolare da statistiche del secondo ordine di $\Theta$ e $(X_1,X_2,\ldots,X_n)$.

Facciamo un esempio: supponiamo di avere $n$ variabili aleatorie $X_i$ così definite:

$$X_i = \Theta + W_i, \ i=1,\ldots,n$$

Diciamo anche che $\Theta, W_1,W_2,\ldots,W_n$ sono tutte indipendenti e che conosciamo alcuni dati:

$$\begin{aligned}
E[\Theta] &= \mu & \text{Var}[\Theta] &= \sigma_0^2\\\
E[W_i] &= 0 & \text{Var}[W_i] &= \sigma_i^2
\end{aligned}$$

Si può dimostrare che:

$$\hat\Theta_\text{LIN} = {{\mu\over\sigma_0^2} + \sum_{i=1}^n {X_i\over\sigma_i^2}\over\sum_{i=0}^n{1\over\sigma_i^2}}$$

> **Nota**
>
> Se le variabili aleatorie $X_i$ fossero Gaussiane, allora $\hat\Theta_\text{LIN}$ sarebbe a sua volta Gaussiana:
> $$\hat\Theta_\text{LIN} = \hat\Theta_\text{LMS} = E[\Theta|X_1,\ldots,X_n]$$
> Nel "mondo" Gaussiano, gli stimatori lineari sono ottimi per quanto riguarda l'errore quadratico medio.

> **Attenzione**
>
> Va notato che vale:
> $$\hat\Theta_\text{LMS} = E[\Theta|X] = E[\Theta|X^3]$$
> Mentre invece non vale:
> $$\hat\Theta_\text{LIN}(X) = a_1X+b_1 \ne \hat\Theta_\text{LIN}(X^3) = a_2X^3+b_2$$
