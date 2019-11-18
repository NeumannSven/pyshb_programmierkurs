import tkinter as tk

# Hauptfenster erzeugen
root = tk.Tk()
root.geometry('500x500')

# Texteingabefeld erzeugen
e = tk.Entry(root)
e.grid(row=0, column=0)

# Slider erzeugen
sterne = tk.IntVar()
s = tk.Scale(root, from_=1, to=5, variable=sterne, orient="horizontal")
s.grid(row=1, column=0)

bewertung = tk.Label(root, textvariable=sterne)
bewertung.grid(row=2, column=0)

# Spinbox erzeugen
prozente = tk.DoubleVar()
spin = tk.Spinbox(root, from_=0, to=100, increment=0.1, textvariable=prozente)
spin.grid(row=3, column=0)

anteil = tk.Label(root, textvariable=prozente)
anteil.grid(row=4, column=0)

root.mainloop()
