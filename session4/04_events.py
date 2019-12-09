# Modul importieren
import tkinter as tk

# Hauptfenster erzeugen
root = tk.Tk()
root.geometry('500x500')

# Beispiel Widget erzeugen
zeichnung1 = tk.Canvas(root, width=200, height=100)
zeichnung1.grid(row=0, column=0, sticky='WE')
zeichnung1.create_line(0, 0, 200, 100)
zeichnung1.create_rectangle(50, 25, 150, 75, fill="green")

# Laben Widget erzeugen
abschnitt1 = tk.Label(root, text="Anzeige von Informationen")
abschnitt1.grid(row=1, column=0, sticky='WE')


# Callback Funktion für Maustaste gedrückt deklarieren
def pressed_callback(event):
    abschnitt1["text"] = f"Mausbutton gedrückt bei ({event.x}, {event.y})"


# Callback Funktion für Maustaste losgelassen deklarieren
def released_callback(event):
    abschnitt1["text"] = f"Mausbutton losgelassen bei ({event.x}, {event.y})"


# Events an die Funktionen binden
zeichnung1.bind("<ButtonPress-1>", pressed_callback)
zeichnung1.bind("<ButtonRelease-1>", released_callback)

# Eventloop starten
root.mainloop()
