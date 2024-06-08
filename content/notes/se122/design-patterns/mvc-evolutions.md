---
title: "Evoluzioni dell'MVC"
draft: false
type: 'page'
toc: true
mathjax: true
---

---

## Motivazioni

Il paradigma Model-View-Controller tradizionale può presentare alcuni problemi. Ad esempio, la View può essere dipendente dal Modello o il Controller dalla View. In questi casi, il testing diventa assai complesso e il Controller spesso finisce per contenere troppa logica.

Vengono così introdotte delle alternative al classico MVC che elencheremo di seguito.

### Model-View-Presenter (MVP)

Il pattern MVP è simile a quello MVC, ma la View non ha dipendenze dal Modello. La comunicazione Controller-View avviene attraverso delle interfacce.

In questo caso, i componenti si dividono così:

- **Model**: contiene lo stato e la logica applicativa e non ha dipendenze con altri componenti
- **View**: contiene la logica di visualizzazione e propaga eventi al Presenter
- **Presenter**: riceve gli input degli utenti inoltrati dalla View e modifica Modello e View

![](../../images/Pasted%20image%2020221127102337.png)

### Model-View-ViewModel (MVVM)

Questo paradigma riduce ulteriormente le dipendenze tra livelli ed è strutturato come segue:

- **Model**: contiene lo stato e la logica applicativa, non ha dipendenze da altri componenti
- **View**: non contiene logica e di solito è creata con linguaggi dichiarativi
- **ViewModel**:
	- Non ha riferimenti né alla View né ad interfacce relative
	- Prepara un insieme di dati (solitamente primitivi) pensati per la visualizzazione (`Observable`)
	- Espone metodi per reagire agli input degli utenti

Un insieme di componenti dedicati hanno la funzione di collegare View e ViewModel nel processo di *Data Binding*. Solitamente, questo livello è fornito da un framework, come ad esempio Android. L'utente, nella definizione della View, può iscriversi ad uno specifico ViewModel ed ai relativi dati.

![](../../images/Pasted%20image%2020221127102720.png)
