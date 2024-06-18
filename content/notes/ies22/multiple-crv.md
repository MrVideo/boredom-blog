---
title: "Variabili aleatorie continue multiple"
draft: false
type: 'page'
toc: true
mathjax: true
---

---

## Densità di probabilità congiunta

[Come già visto per le variabili aleatorie discrete](../multiple-drv#legge-di-probabilità-congiunta), anche le variabili aleatorie continue possono essere unite per dare luce alle densità di probabilità congiunte:

$$P\big((X,Y)\in S\big) = \iint_{(x,y)\in S} f_{X,Y}(x,y)dxdy$$

> **Osservazione**
>
> Geometricamente, la densità di probabilità congiunta è il volume sotteso alla superficie descritta da $f_{X,Y}$ nel dominio $S$.

## Valore atteso

[Analogamente al caso discreto](../multiple-drv#valore-atteso-per-variabili-aleatorie-multiple), è possibile calcolare un generico valore atteso per due variabili aleatorie continue in questo modo:

$$E\big[g(X,Y)\big] = \iint_{-\infty}^\infty g(x,y)\cdot f_{X,Y}(x,y)dxdy$$

## Legge di probabilità marginale

[Come nel caso discreto](../multiple-drv#leggi-di-probabilità-marginali), anche le variabili aleatorie continue multiple possono essere marginalizzate per trovare la densità di probabilità di una sola variabile casuale:

$$\begin{aligned}
f_X(x) &= \int_{-\infty}^\infty f_{X,Y}(x,y)dy\\\
f_Y(y) &= \int_{-\infty}^\infty f_{X,Y}(x,y)dx
\end{aligned}$$

## Indipendenza tra due variabili aleatorie continue

[Analogamente alle variabili aleatorie discrete](../multiple-drv#variabili-aleatorie-indipendenti), è possibile definire il concetto di indipendenza per le variabili casuali continue:

$$X\perp Y \iff f_{X,Y}(x,y) = f_X(x)\cdot f_Y(y), \> \forall (x,y)\in\mathbb R^2$$

## Densità di probabilità condizionata

[Sempre analogamente al caso discreto](../multiple-drv#leggi-di-probabilità-condizionale), possiamo calcolare la densità di probabilità condizionata continua così:

$$f_{X|Y}(x|y) = {f_{X,Y}(x,y)\over f_X(x)}$$
