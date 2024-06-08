---
title: 'Strategy'
draft: false
type: 'page'
toc: true
mathjax: true
---

---

Strategy è un object design pattern comportamentale.

## Motivazioni

Si assuma di voler creare una classe `Composition` che gestisca elementi organizzati in righe. A seconda del contesto, si possono usare diversi algoritmi per organizzare gli elementi, che hanno efficienza diversa a seconda del caso d'uso.

Problema: gestire un insieme di strategie o algoritmi per compiere una determinata azione. La strategia può essere cambiata a runtime.

## Una soluzione non ideale

```java
class Composition {
	private Data data;
	public void traverse() {
		// Code
	}
	public void repair() {
		if(case1) simpleCompose();
		else if(case2) texCompose();
		else arrayCompose();
	}
	public void simpleCompose() {
		// Code
	}
	public void texCompose() {
		// Code
	}
	public void arrayCompose() {
		// Code
	}
}
```

## Obiettivi

Per risolvere questo problema si può definire un'interfaccia `Strategy`: ciascuna sua implementazione usa un algoritmo differente.

La classe `Composition` avrà un riferimento a `Strategy` e la strategia potrà essere modificata a runtime.

## Struttura

![](../../images/Pasted%20image%2020221126170631.png)

## Esempio

![](../../images/Pasted%20image%2020221126170647.png)

```java
interface Compositor {
	void compose(Data data);
}

class SimpleCompositor implements Compositor {
	public void compose(Data data) {
		// Code
	}
}

class Composition {
	private Data data;
	private Compositor compositor;
	public void setCompositor(Compositor cmp) {
		compositor = cmp;
	}
	public void traverse() {
		// Code
	}
	public void repair() {
		compositor.compose(data);
	}
}
```
