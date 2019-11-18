from tkinter import *

# Hauptfenster erzeugen
root = Tk()
root.geometry('500x500')

# Label erzeugen
abschnitt1 = Label(root, text="Anzeige von Informationen")

abschnitt1.grid(row=0, column=0, sticky=W+E)

# Message vorbereiten und anzeigen
zen = "Beautiful is better than ugly.\n" \
"Explicit is better than implicit.\n" \
"Simple is better than complex.\n" \
"Complex is better than complicated."

nachricht1 = Message(root, text=zen) #, width=500
nachricht1.config(bg='lightgreen', font=('times', 24, 'italic'))

nachricht1.grid(row=1, column=0, sticky=W+E)
root.grid_columnconfigure(0, weight=1)

# Graphik erzeugen
zeichnung1 = Canvas(root, width=200, height=100)

zeichnung1.grid(row=2, column=0, sticky=W+E)
zeichnung1.create_line(0, 0, 200, 100)
zeichnung1.create_rectangle(50, 25, 150, 75, fill="green")

root.mainloop()
