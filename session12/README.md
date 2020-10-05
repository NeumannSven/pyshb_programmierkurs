
# Distribution von Python Projekten
Wenn du ein Programm in Python erstellt hast, das sehr nützlich auch für andere Personen sein kann, möchtest du vielleicht an dritte weitergeben. Diese können vielleicht nicht so richtig was mit Python Quellcode was anfangen oder haben vielleicht auch noch nicht einmal eine Python Interpreter auf ihren Rechner installiert. Wie können wir nun unsere Applikation verteilen, damit diese auch von nicht Programmieren genutzt werden können. Python stellt ein paar Tools dafür bereit, die wir uns etwas näher anschauen.  

## Welche Tools gibt es?
Das Paket _distutils_ ist in der Standardbibliothek enthalten und kann über ein Setupscript verschiedene Installationsformate erzeugen. Es ist möglich Source und Binäre Distributionen zu erzeugen. Eine Source Distribution kann plattform übergreifent verwendet werden. Eine Binäre Distribution kann nur für das System, auf dem gerade das Setupscript läuft, erzeugt werden. Ein weiteres Packet mit den Namen_setuptools_ bietet noch mehr Möglichkeiten, ist aber nicht in der Standardbibliothek enthalten. Die oben genannten Pakete brachen jeweils eine vorhandene Python Installation. Mit dem Paket _pyinstaller_ ist man in der Lage, ausführbare Programme zu erzeugen, die keine installierte Python-Umgebung voraussetzen.


## distutils
Wir benötigen zum erzeugen einer Distribution immmer eine "setup.py" Datei in der ein paar Metadaten und die Information über die Zusammensetzung der
Distribution enthalten sind.

```python
from distutils.core import setup

setup(name='MyApp',
      version='1.0.0',
      description='My Application',
      author='Sven Neumann',
      author_email='sven.neumann@web.de',
      url='https://github.com/NeumannSven/pyshb_programmierkurs/tree/master/session12',
      py_modules=['MyApp'],
      #packages=['distutils', 'distutils.command'],
     )
```

### Source Distribution (sdist)

Hilfe welche Formate unterstütz werden kannst folgendermaßen bekommen.

```console
python setup.py sdist --help-formats

List of available source distribution formats:
  --formats=bztar  bzip2'ed tar-file
  --formats=gztar  gzip'ed tar-file
  --formats=tar    uncompressed tar file
  --formats=xztar  xz'ed tar-file
  --formats=zip    ZIP file
  --formats=ztar   compressed tar file
```

Wird kein Format angegeben, wird eine tar.gz Archiv erstellt.

```console
python setup.py sdist
```
Wenn Du ein zip Archiv erzeugen möchtest, muss das Format mit angegeben werden.

```console
python setup.py sdist --formats=zip
```

### Binäre Distribution (bdist)
Mit der erstellen setup.py Datei kann auch eine Binäre Distribution erstellt werden.
Mit folgenden Aufruf, bekommst du Information über die unterstützten Formate.

```console
python setup.py bdist --help-formats

List of available distribution formats:
  --formats=rpm      RPM distribution
  --formats=gztar    gzip'ed tar file
  --formats=bztar    bzip2'ed tar file
  --formats=xztar    xz'ed tar file
  --formats=ztar     compressed tar file
  --formats=tar      tar file
  --formats=wininst  Windows executable installer
  --formats=zip      ZIP file
  --formats=msi      Microsoft Installer
```

#### Windows installation
Für Windows können zwei verschiedene Installationsformate erstellt werden. Es gibt eine normale ausfürbare Installationsdatei mit der Endung "exe" oder eine Installationsdatei mit der Endung "msi".

##### EXE
Die Ausführbare Installationsdatei wird folgendermaßen erstellt.

```console
python setup.py bdist --formats=wininst
```

![Ausführbare Setup Datei](https://github.com/NeumannSven/pyshb_programmierkurs/blob/master/session12/exe.png "Ausführbare Setup Datei")

##### MSI
Eine MSI Datei kann durch Angeabe des Formats auch erstellt werden.

```console
python setup.py bdist --formats=msi
```
![Windows Setup Datei](https://github.com/NeumannSven/pyshb_programmierkurs/blob/master/session12/msi.png "Windows Setup Datei")

#### Linux package
Das Erstellen eines RPM Paketes ist auch möglich, aber Dazu muss man sich auch auf einen Linux System befinden.
Ein Crosscompiling wird nicht unterstüzt.

##### RPM
```console
python setup.py bdist --formats=rpm
```


## pyinstaller

### Ausführbare Applikation





