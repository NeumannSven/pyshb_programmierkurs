import tkinter as tk
from tkinter import ttk

# Hauptfenster erzeugen
root = tk.Tk()
root.geometry('500x500')
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

# Checkbox erzeugen
hakenvar = tk.IntVar(value=2)
haken = tk.Checkbutton(root, text="Schalter", variable=hakenvar)
haken.grid(row=0, column=0)

option1 = tk.Label(root, textvariable=hakenvar)
option1.grid(row=1, column=0)

# Radiobutton erzeugen
auswahlvar = tk.StringVar(value="")
auswahl1 = tk.Radiobutton(root, text="Python", variable=auswahlvar, value="Python")
auswahl1.grid(row=0, column=1, sticky="w")
auswahl2 = tk.Radiobutton(root, text="C++", variable=auswahlvar, value="C++")
auswahl2.grid(row=1, column=1, sticky="w")
auswahl3 = tk.Radiobutton(root, text="Java", variable=auswahlvar, value="Java")
auswahl3.grid(row=2, column=1, sticky="w")

option2 = tk.Label(root, textvariable=auswahlvar)
option2.grid(row=3, column=1)

# Combobox erzeugen
combovar = tk.StringVar(value="Python")
combo = ttk.Combobox(root, values=["Python",
                                   "C++",
                                   "Java"
                                   ], textvariable=combovar)
combo.grid(row=4, column=0, columnspan=2, sticky="we")

option3 = tk.Label(root, textvariable=combovar)
option3.grid(row=5, column=0, columnspan=2)

root.mainloop()
