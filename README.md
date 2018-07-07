# brandberg-ki-10
DL network for classifying gender in Brandberg rock art


## Zwischenstand 11.06.2018

### Zwischenstand
* DNN verbessert:
	* Entfernen von zwei Convolution-Layern, um das Netzwerk auf die einfacheren Formen der Bandberg-Malereien (im Vergleich zu der MINST-Datenbasis aus dem Beispiel-Netzwerk, dass wir als Basis genutzt haben) anzupassen
	* Overfitting durch weniger Trainingsschritte verringert
* Web-Interface:

### Roadmap 
* DNN weiter optimieren:
	* Performance bei größer werdender Datenbasis prüfen (Bessere Ergebnisse bei größerer Varianz der Trainingsdaten?)
	* Entfernen von Farbe/ Konventierung in Graustufen zum schnelleren trainieren und bestmöglichen Abstraktion von Merkmalen zur Erkennung von Geschlecht

* Zusammenarbeit mit anderen Gruppen:
	* Datenbais automatisiert füllen
	* Automatsiert ausgeschnittene Figuren mit Verweis auf Tabellendaten, damit Figuren mit zugewiesenem Geschlecht als Trainingsdaten genutzt werden können

* Web-Interface: 
	* Verbindung von Web-Interface (JavaScript) und DNN (Python-Script) auf einem Host-Rechner
	* Beginn die Seite zu gestalten (noch ganz am Anfang)	
![](https://github.com/stereolith/brandberg-ki-10/blob/master/screenshots/Screenshot.jpg)

## Zwischenstand 07.05.2018

* kleine Datenbasis vorbereitet: 
	* insgesamt 50 Figuren ausgeschnitten und in Geschlechter aufgeteilt
	* Hintergrund entfernt (transparent)
	* Seitenverhältnis 4:5

* Daten in verarbeitbare Form gebracht via TFLearn "Image PreLoader"-Funktion
* Erstes Convolutional Neural Network aus einem Beispiel zur Klassifizierung vom CIFAR-10 dataset mit den Figuren-Daten erfolgreich trainert ([Python-Script](https://github.com/stereolith/brandberg-ki-10/blob/master/script/network.py))

![](https://raw.githubusercontent.com/stereolith/brandberg-ki-10/master/tensorboard_0705.PNG)
