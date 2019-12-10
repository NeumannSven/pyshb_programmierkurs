import tkinter as tk

# Hauptfenster erzeugen
root = tk.Tk()

# Label Widget erzeugen
testlabel = tk.Label(root, text="Hallo PySpace Bremen!")

# Label Widget auf das Hauptfenster legen
testlabel.grid(row=0)

# Mainloop starten
root.mainloop()

print("Ende")
