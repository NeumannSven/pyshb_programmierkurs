[Inhalt](../agenda.md)

# Tupel
Ein Tupel ist eine unveränderbare Sequenz. Ein Tupel kann aus Items mit beliebigen Datentypen zusammen gesetzt sein.
Tupel werden in runden Klammern gesetzt und durch Komma getrent.

```python
>>> t = (1,2,3)
>>> t
(1, 2, 3)
>>> type(t)
<class 'tuple'>
>>> t
(1, 2, 3)
>>> t[0]
1
>>> t[1]
2
>>> t[1] = 5
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    t[1] = 5
TypeError: 'tuple' object does not support item assignment
>>> 
```

# Listen
Eine Liste ist eine veränderbare Sequenz. Eine Liste kann aus Items mit beliebigen Datentypen zusammen gesetzt sein.
Listen werden in eckigen Klammern gesetzt und durch Komma getrent.


```python
>>> l = [1,2,3]
>>> l
[1, 2, 3]
>>> type(l)
<class 'list'>
>>> l
[1, 2, 3]
>>> l[0]
1
>>> l[1]
2
>>> l[1] = "Hallo"
>>> l
[1, 'Hallo', 3]
>>> 
```

# Dictionaries
Ein Dictionary ist eine veränderbare Sequenz aus Wertpaaren. Es ermöglicht einen Zugrif auf Werte(value) über einen Schlüssel(key). Ein Dictionary mit Wertpaaren wird in geschweiften Klammern gesetzt und durch Komma getrent. Ein Wertpaar besteht immer aus einen Schlüssel(key) und einen Wert(value) und diese werden durch einen Doppelpunkt getrennt.

```python
>>> d = {"eins":1,"zwei":2,"drei":3}
>>> d
{'eins': 1, 'zwei': 2, 'drei': 3}
>>> d[0]
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    d[0]
KeyError: 0
>>> d["eins"]
1
>>> d["zwei"] = "Hallo"
>>> d
{'eins': 1, 'zwei': 'Hallo', 'drei': 3}
>>> 

```


[Inhalt](../agenda.md)
