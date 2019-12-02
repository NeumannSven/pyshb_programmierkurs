[Inhalt](../agenda.md)

# Strings

## Allgemein
Strings sind ein elementarer Datentyp. In Python 3 sind alle Strings Unicodestrings.

```python
>>> s = "Hallo Bremen!"
>>> type(s)
<class 'str'>
```

Strings verhalten sich wie eine Liste aus Characters.

```python
>>> print(s[1])
a
>>> for c in s:
    print(c)
    
H
a
l
l
o...
```

Die Länge eines Strings erhält man mit len().

```python
>>> len(s)
13
```

## Teilstrings

Man bekommt Teilstrings z.B. durch Slicing.

``String[ von(incl.) : bis(excl.) ]``

```python
>>> print(s[6:12])
Bremen
```

Oder man zerteilt den String an Whitespaces.

```python
>>> l = s.split()
>>> print(l)
['Hallo', 'Bremen!']
```

## Strings bearbeiten

Überflüssige Whitespaces entfernen mit strip(). Achtung! Die meisten Funktionen geben einen neuen String zurück, der ursprüngliche String bleibt erhalten.

```python
>>> s = " Hallo Bremen!     "
>>> print(s.strip())
Hallo Bremen!
>>> print(s)
 Hallo Bremen!     
>>> s
' Hallo Bremen!     '
>>> s.strip()
'Hallo Bremen!'
```

Einzelne Zeichen ersetzen mit replace().

```python
>>> s
'Hallo Bremen!'
>>> s.replace('!','?')
'Hallo Bremen?'
>>> s.replace('n','r')
'Hallo Bremer!'
```

## Strings zusammensetzen

Strings können einfach addiert werden.

```python
>>> a = "Hallo"
>>> b = "Welt"
>>> a + b
'HalloWelt'
```

Fortgeschrittenes Zusammensetzen mit join(). Achtung! Die Funktion ist am Anfang nicht intuitiv.

```python
>>> " ".join([a, b])
'Hallo Welt'
```

Inhalte von Variablen können in Strings eingebettet werden. Ab Python 3.6 am einfachsten mit f-Strings.

```python
>>> alter = 38
>>> text = f"Ich bin {alter} Jahre alt."
>>> print(text)
Ich bin 38 Jahre alt.
```

## Strings verwenden im Programm

Inhalt eines Strings prüfen mit ``in`` oder ``not in``.

```python
>>> "Hamburg" in s
False
```

[Inhalt](../agenda.md)
