[Inhalt](../agenda.md)

# GUI

## Erstes Fenster

tkinter importieren und das Hauptfenster erzeugen. Das Hauptfenster dient als *parent* für alle weiteren Elemente.

```python
import tkinter as tk
root = tk.Tk()
```

Erstes Widget erzeugen. Der erste Parameter ist immer das Hauptfenster. Die weiteren Parameter hängen ab vom Widget.

```python
testlabel = tk.Label(root, text="Hallo PySpace Bremen!")
testlabel.grid(row=0)
```

Das Element muss auf dem Hauptfenster platziert werden. Der *grid* Layoutmanager ordnet Widgets in Zeilen und Spalten an.

```python
testlabel.grid(row=0)
```

Damit das Fenster offen bleibt, muss der Eventloop gestartet werden. Damit wartet das Programm auf Klicks und andere Nutzerinteraktionen.

```python
root.mainloop()
```

[Widgets](03_widgets.md)

[Inhalt](../agenda.md)
