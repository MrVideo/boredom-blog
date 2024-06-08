---
title: 'Adapter'
draft: false
type: 'page'
toc: true
mathjax: true
---

---

L'adapter è un class design pattern strutturale.

## Motivazioni

Consideriamo di progettare un editor grafico.

La principale astrazione definita è un'interfaccia `Shape` che rappresenta una generica forma disegnabile.

Classi concrete come `LineShape` e `SquareShape` implementano la logica per disegnare specifiche forme come linee e quadrati.

Un'ulteriore possibile concretizzazione di `Shape` è `TextShape`, per disegnare caselle di testo. La logica di `TextShape` è significativamente più complessa di quelle per semplici forme geometriche. Si decide quindi di appoggiarsi ad una libreria grafica esterna che definisce una classe `TextView` ed implementa la logica desiderata.

Problema: `TextView` non implementa l'interfaccia `Shape` ed è difficilmente integrabile all'interno del sistema esistente.

## Possibile soluzione errata

Una soluzione potrebbe essere quella di modificare il codice di `TextView` affinché questa implementi `Shape`, ma non ha senso aggiungere codice specifico di un particolare dominio applicativo ad una classe già esistente. Inoltre, il codice di `TextView` potrebbe non essere accessibile.

## Obiettivi

L'obiettivo dell'adapter è quello di definire una strategia di *adattamento* per la classe non compatibile.

Esistono due modi per farlo:

1. Attraverso l'ereditarietà
2. Attraverso la composizione

### Struttura con ereditarietà

![](../../images/Pasted%20image%2020221126150545.png)

### Struttura con composizione

![](../../images/Pasted%20image%2020221126150601.png)

## Esempio

![](../../images/Pasted%20image%2020221126150616.png)

```java
interface Shape {
	public Size boundingBox();
}

class SquareShape implements Shape {
	public Size boundingBox() {
		return new Size(edge * edge);
	}
}

class TextView extends ExternalLibraryView {
	public Size getExtent() {
		return new Size();
	}
}

// Esempio con ereditarietà
class TextShape extends TextView implements Shape {
	public Size boundingBox() {
		return this.getExtent();
	}
}

// Esempio con composizione
class TextShape implements Shape {
	private TextView adaptee = new TextView();

	public Size boundingBox() {
		return adaptee.getExtent();
	}
}
```
