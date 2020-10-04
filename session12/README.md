
# Distribution von Python Projekten
Wie kann mein Kumpel meine neue Python App testen?

## Welche Tools gibt es?
Das Paket _distutils_ ist in der Standar Bibliothek enthalten und kann über ein Setupscript verschiedene Installationsformate erzeugen.
Es ist möglich Source und Binärie Distributionen zu erzeugen. Eine Source Distribution kann plattform übergreifent verwendet werden.
Eine Binärie Distribution kan nur für das System, auf dem gerade das Setupscript läuft, erzeugt werden. Eine weitere möglichkeit ist
das Packet _setuptools_ diese bittet noch mehr Möglichkeiten, ist aber nicht in der Standard Bibliothek enthalten. Die oben genannten Pakete
brachen jeweils eine vorhanden Python Installation. Mit dem Paket _pyinstaller_ ist man in der Lage sogenannte ausführbare Programme auszuliefern,
die kein installiertes Python benötigen.


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

Hilfe welche Formate unterstütz werden kannst folgendermaßen bekommen:

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

Wird kein Format angegeben, wird eine tar.gz Archiv erstellt:

```console
python setup.py sdist
```
Wenn Du ein zip Archiv erzeugen möchtest, muss das Format mit angegeben werden.

```console
python setup.py sdist --formats=zip
```

### Binärie Distribution (bdist)

#### Windows installation
##### EXE

##### MSI


#### Linux package
##### RPM



## pyinstaller

### Ausführbare Applikation





