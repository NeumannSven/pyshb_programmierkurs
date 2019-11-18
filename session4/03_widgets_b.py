from tkinter import *

# Hauptfenster erzeugen
root = Tk()
root.geometry('500x500')

hakenvar = IntVar()

haken = Checkbutton(root, text="Schalter", variable=hakenvar)
haken.grid(row=0, column=0)

option1 = Label(root, textvariable=hakenvar)
option1.grid(row=1,column=0)

auswahlvar = StringVar(value="Python")
auswahl1 = Radiobutton(root, text="Python", variable=auswahlvar, value="Python")
auswahl1.grid(row=2,column=0)
auswahl2 = Radiobutton(root, text="C++", variable=auswahlvar, value="C++")
auswahl2.grid(row=3,column=0)
auswahl3 = Radiobutton(root, text="Java", variable=auswahlvar, value="Java")
auswahl3.grid(row=4,column=0)

option2 = Label(root, textvariable=auswahlvar)
option2.grid(row=5,column=0)

root.mainloop()