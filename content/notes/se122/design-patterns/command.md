---
title: 'Command'
draft: false
type: 'page'
toc: true
mathjax: true
---

---

Command è un object design pattern comportamentale.

## Motivazioni

Consideriamo di voler creare una classe `Menu` per eseguire operazioni all'interno di un'applicazione.

Un'istanza di `Menu` contiene un insieme di `MenuItem`, uno per ciascuna azione da eseguire. Un'istanza di `Menu` non deve conoscere i dettagli dell'applicazione associata, né delle azioni associate ai `MenuItem`.

Problema: gestire un insieme di comandi non conosciuti a priori. Le istanze di `Menu`, infatti, non devono avere dipendenze con i comandi. Ipotizziamo inoltre che l'azione associata ad un `MenuItem` possa cambiare a runtime.

## Alcune soluzioni non ideali

### Soluzione 1

```java
class Menu {
	MyApplicationDocument document;

	public Menu(MyApplicationDocument document) {
		this.document = document;
	}

	public void copy() {
		// Code
	}

	public void paste() {
		// Code
	}

	public void new() {
		// Code
	}
}
```

### Soluzione 2

```java
class Menu {
	List<MenuItem> items = new ArrayList<>();
	public void addMenuItem(MenuItem a) {
		// Code
	}
}

class MenuItem {
	MyApplicationDocument document;

	public void clicked() {
		// Code
	}
}
```

## Obiettivi

Lo scopo da raggiungere è quello di definire un'interfaccia `Command` che contenga, nel modo più semplice possibile, un solo metodo `execute`.

`MenuItem` ha un riferimento ad un oggetto di tipo `Command`.

L'azione da compiere diventa in questo modo completamente slegata dagli oggetti che la usano.

## Struttura

![](../../images/Pasted%20image%2020221126153308.png)

## Esempio

![](../../images/Pasted%20image%2020221126153324.png)

![](../../images/Pasted%20image%2020221126153334.png)

![](../../images/Pasted%20image%2020221126153346.png)

```java
interface Command {
	void execute();
}

class PasteCommand implements Command {
	private Document doc;
	public PasteCommand(Document doc) { this.doc = doc; }
	public void execute() {
		// Code
	}
}

class Menu {
	List<MenuItem> items = new ArrayList<>();
	public void addMenuItem(MenuItem a) {
		// Code
	}
}

class MenuItem {
	Command command;
	
	public void setCommand(Command cmd) { this.command = cmd; }

	public void clicked() { command.execute(); }
}
```
