import tkinter as tk

# Hauptfenster erzeugen
root = tk.Tk()
root.geometry('700x700')

# Label erzeugen
abschnitt1 = tk.Label(root, text="Anzeige von Informationen")

abschnitt1.grid(row=0, column=0, sticky='WE')

# Message vorbereiten und anzeigen
zen = "Beautiful is better than ugly.\n" \
"Explicit is better than implicit.\n" \
"Simple is better than complex.\n" \
"Complex is better than complicated."

nachricht1 = tk.Message(root, text=zen) #, width=500
nachricht1.config(bg='lightgreen', font=('times', 24, 'italic'))

nachricht1.grid(row=0, column=1, sticky='WE')
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=4)

# Graphik erzeugen
zeichnung1 = tk.Canvas(root, width=200, height=100)

zeichnung1.grid(row=2, column=0, sticky='WE')
zeichnung1.create_line(0, 0, 200, 100)
zeichnung1.create_rectangle(50, 25, 150, 75, fill="green")
zeichnung1.create_rectangle(100, 50, 100, 50, fill="red", outline="red")

root.mainloop()
