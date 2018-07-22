# brandberg-ki-10
DL network for classifying gender in Brandberg rock art

### 1. Convolutional Deep Neural Network
Das Convolutional Deep Neural Network zur Klassifizierung ist in den Python-Scripten unter /script/ definiert. Basis bietet TensorFLow mit dem [TFLearn-Wrapper](http://tflearn.org/). <br><br>
`network_standalone.py` Speichert das trainierte Netzwerk zur späteren Inferenz/ Klassifikaiton im webinterface ab, <br>
`network.py` bietet nach dem Training in der Python-Konsole die möglichkeit der direkten Klassifikation eines Eingabebildes mittels EIngabe eines Bild-Pfades

### 2. Web-Interface
Ein Web-Interface zur einfacherern Inferenz von Eingabebildern liegt in /webinterface/. Die Oberfläche bietet ein Crop-Tool für das Zuschneiden des Eingabebildes und eine Vorschau des ausgeschnitten Bildes. Das Ergebnis der Inferenz wird nach einigen Sekunden in einem Kuchendiagramm dargestellt.
* Die  enthaltenden Dateien müssen auf einem PHP-Fähigen Webserver (z.B. Apache) liegen
* Ein vorher trainiertes und abgespeichertes Netzwerk (siehe  `script/network.py`) muss im Root-Ordner des Webservers im Verzeichnis `/models/master/` liegen
* Auf dem Host-Rechner müssen Tensorflow und TFLearn installiert sein

![](https://github.com/stereolith/brandberg-ki-10/blob/master/screenshots/webui_final.PNG)


---


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

![](https://github.com/stereolith/brandberg-ki-10/blob/master/screenshots/tensorboard_0705.PNG)
