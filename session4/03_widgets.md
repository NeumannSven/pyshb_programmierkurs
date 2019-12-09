[Inhalt](../agenda.md)

# GUI

## Überblick über Widgets

Es gibt eine Vielzahl verschiedener Widgets für unterschiedliche Einsatzzwecke.

### Anzeige von Informationen

Das einfachste Widgets um Text anzuzeigen ist *Label*. Die Option ``sticky`` bei der ``grid`` Methode dient dazu, das Widget in seiner Zelle an die Wände zu "kleben".

```python
abschnitt1 = tk.Label(root, text="Anzeige von Informationen")
abschnitt1.grid(row=0, column=0, sticky='WE')
```

Wenn längere Texte mit Umbruch angezeigt werden sollen, gibt es *Message*. Bei vielen Widgets kann man das Aussehen mit der ``config`` Methode anpassen.
``grid_columnconfigure`` muss benutzt werden, damit Widgets auf den zur Verfügung stehenden Platz ausgedehnt werden.

```python
zen = "Beautiful is better than ugly.\n" \
"Explicit is better than implicit.\n" \
"Simple is better than complex.\n" \
"Complex is better than complicated."
nachricht1 = tk.Message(root, text=zen) #, width=500
nachricht1.config(bg='lightgreen', font=('times', 24, 'italic'))

nachricht1.grid(row=1, column=0, sticky='WE')
root.grid_columnconfigure(0, weight=1)
```

Ein *Canvas* ist ein Widget, auf dem frei gezeichnet werden kann. Es können einzelne Pixel gesetzt werden oder geometrische Formen gezeichnet werden.

```python
zeichnung1 = tk.Canvas(root, width=200, height=100)
zeichnung1.grid(row=2, column=0, sticky='WE')

zeichnung1.create_line(0, 0, 200, 100)
zeichnung1.create_rectangle(50, 25, 150, 75, fill="green")
```

### Auswahl von Optionen

Eine *Checkbox* kann dazu benutzt werden, um zum Beispiel Optionen auszuwählen. Bei tkinter gibt es die Möglichkeit, Widgets direkt mit Variablen zu verknüpfen.
Vorteil: Änderungen werden in beide Richtungen direkt weitergegeben.
Nachteil: Die Variablen müssen mit speziellen Typen erzeugt werden.

```python
hakenvar = tk.IntVar()
haken = tk.Checkbutton(root, text="Schalter", variable=hakenvar)
haken.grid(row=0, column=0)

option1 = tk.Label(root, textvariable=hakenvar)
option1.grid(row=1, column=0)
```

Ein *Radiobutton* bietet die Möglichkeit eine 1 aus x Auswahl zu treffen. Dazu legt man mehrere Widgets an, die sich die selbe Variable teilen.

```python
auswahlvar = tk.StringVar(value="Python")
auswahl1 = tk.Radiobutton(root, text="Python", variable=auswahlvar, value="Python")
auswahl1.grid(row=2, column=0)
auswahl2 = tk.Radiobutton(root, text="C++", variable=auswahlvar, value="C++")
auswahl2.grid(row=3, column=0)
auswahl3 = tk.Radiobutton(root, text="Java", variable=auswahlvar, value="Java")
auswahl3.grid(row=4, column=0)

option2 = tk.Label(root, textvariable=auswahlvar)
option2.grid(row=5, column=0)
```

Die *Combobox* vereint eine 1 aus x Auswahl mit einer optionalen Freitexteingabe. Die Auswahloptionen werden als Liste übergeben. Das Widget ist bei tkinter im Submodule ``ttk`` implementiert.

```python
from tkinter import ttk
combovar = tk.StringVar(value="Python")
combo = ttk.Combobox(root, values=["Python",
                                   "C++",
                                   "Java"
                                   ], textvariable=combovar)
combo.grid(row=6, column=0)

option3 = tk.Label(root, textvariable=combovar)
option3.grid(row=7, column=0)
```

### Eingabe von Inhalten

* Entry
* Scale/Slider
* Spinbox

[Inhalt](../agenda.md)
