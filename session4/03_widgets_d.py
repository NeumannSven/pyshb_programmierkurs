# Module importieren
import tkinter as tk
import tkinter.messagebox as tkmessagebox

# Hauptfenster erzeugen
root = tk.Tk()


# Callback Funktion deklarieren
def hello_callback():
    tkmessagebox.showinfo("Hinweis", "Hallo Python!")


# Button erzeugen
b = tk.Button(root, text="Hallo", command=hello_callback)

# Button auf das Fenster legen
b.grid()

# Eventloop starten
root.mainloop()
