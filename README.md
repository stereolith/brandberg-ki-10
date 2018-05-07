# brandberg-ki-10
DL network for classifying gender in Brandberg rock art


## Zwischenstand 07.05.2018

* kleine Datenbasis vorbereitet: 
	* insgesamt 50 Figuren ausgeschnitten und in Geschlechter aufgeteilt
	* Hintergrund entfernt (transparent)
	* Seitenverhältnis 4:5

* Daten in verarbeitbare Form gebracht via TFLearn "Image PreLoader"-Funktion
* Erstes Convolutional Neural Network aus einem Beispiel zur Klassifizierung vom CIFAR-10 dataset mit den Figuren-Daten erfolgreich trainert ([Python-Script](https://github.com/stereolith/brandberg-ki-10/blob/master/script/network.py))

![](https://raw.githubusercontent.com/stereolith/brandberg-ki-10/master/tensorboard_0705.PNG)
