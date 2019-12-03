[Inhalt](../agenda.md)

# Dateien Teil 2

Um Dateien zu kopieren, zu verschieben, zu löschen müssen die Module ``shutil``, ``os`` und ``pathlib`` importiert werden.

## Pfadobjekte

Mit den Funktionen aus dem Modul ``pathlib`` können Verzeichnisse und Dateien einfach repräsentiert werden und an andere Funktionen übergeben werden.

```python
import pathlib
pfad = pathlib.Path.cwd()
pfad = pathlib.Path("/var/www")
pfad = pathlib.Path("c:/windows/system32")
pfad2 = pfad / "unterverzeichnis" / "dateiname.py"
```

## Dateien kopieren und verschieben

Zum Kopieren und Verschieben von Dateien nutzt man die Funktionen aus ``shutil``.
``copy2`` kopiert Metadaten wie Berechtigungen mit. ``move`` nutzt standardmäßig auch ``copy2``.

```python
import shutil
shutil.copy2(logdatei, alte_logs)
shutil.move(logdatei, alte_logs)
```

## Dateien löschen

Dateien löschen entweder mit ``unlink`` aus dem Modul ``pathlib`` oder mit ``remove`` aus dem Modul ``os``.

```python
import pathlib
import os
pathlib.unlink(logdatei)
os.remove(logdatei)
```

## Dateien komprimieren

Im Modul ``shutil`` gibt es dafür die Funktion ``make_archive``. Damit wird ein komplettes Verzeichnis in eine komprimierte Datei verpackt. Es stehen verschiedene Kompressionsverfahren zur Verfügung.
Die archiverte Datei sollte nicht im gleichen Verzeichnis angelegt werden, in dem die zu verpackenden Dateien liegen.

```python
import shutil
shutil.make_archive(alte_logs / "logs", "zip", alte_logs)
```

[Dateien Teil 2](03_dateien_2.md)

[Inhalt](../agenda.md)
