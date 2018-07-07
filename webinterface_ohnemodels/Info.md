Das bereits trainierte Model muss in den htdocs-Ordner kopiert werden. Dieses kann leider nicht auf github 
hochgeladen werden, da die Dateien zu groß sind. Die drei Dateien "brandberg.tflearn.meta", "brandberg.tflearn.index" sowie 
"brandberg.tflearn.data-00000-of-00001", die beim Trainieren des Netzwerkes auf dem eigenen PC erzeugt werden, müssen sich 
im Unterordner "master" eines Ordners "models" im htdocs-Ordner befinden. Diese Ordnerstruktur muss selbst angelegt werden.

![](https://github.com/stereolith/brandberg-ki-10/blob/master/screenshots/Ordner-Struktur.PNG)


![](https://github.com/stereolith/brandberg-ki-10/blob/master/screenshots/Ordner-Struktur-model-Dateien.PNG)

Benötigt wird die Installation der Python-Library "matplotlib" (https://matplotlib.org/users/installing.html).
Ergebnis der Classification wird als Kreisdiagramm in PNG-Datei (result.png) in htdocs-Ordner gespeichert (siehe classifier.py).
Sobald result.png vorhanden, lässt sich die Grafik per Klick auf den Button "Show the result" auf der HTML-Seite anzeigen.
