from tkinter import *

root = Tk()
root.geometry('500x500')

abschnitt1 = Label(root, text="Anzeige von Informationen")

abschnitt1.grid(row=0, column=0, sticky=W+E)

zen = "Beautiful is better than ugly.\n" \
"Explicit is better than implicit.\n" \
"Simple is better than complex.\n" \
"Complex is better than complicated."

nachricht1 = Message(root, text=zen)
nachricht1.config(bg='lightgreen', font=('times', 24, 'italic'))

nachricht1.grid(row=1, column=0, sticky=W+E)

root.mainloop()