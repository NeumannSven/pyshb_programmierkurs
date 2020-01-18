[Inhalt](../agenda.md)

# Applikation


## Entwurf

![Sammler](https://github.com/NeumannSven/pyshb_programmierkurs/blob/master/session5/ui.jpeg "Sammler")



## 

```python


import tkinter as tk
import tkinter.scrolledtext as st
import json
import os
from pprint import pprint

selectedItem = []
project = [['new item', "description", ['tags'], 'white', 'more information']]
selectedIndex = 0

bg = '#C5C5C5'


def loadProject(filename='data.json'):
    if not os.path.exists(filename):
        json.dump(project, open(filename, 'w'))
    return json.load(open(filename))

def updateListBox():
    listbox.delete(0, 'end')
    for item in project:
        listbox.insert('end', item[0])
        listbox.itemconfig('end', background=item[3])
        
def updateItemClick(event):
    global selectedItem, selectedIndex
    selectedIndex = event.widget.curselection()[0]
    updateItem()
    
def updateItem():
    global selectedItem
    selectedItem = project[selectedIndex]
    var_titel.set(selectedItem[0])
    var_description.set(selectedItem[1])
    var_tag.set(','.join(selectedItem[2]))
    var_color.set(selectedItem[3])
    txt_content.delete('1.0', 'end')
    txt_content.insert('end', selectedItem[4])


project = loadProject()


window = tk.Tk()
window.title('Ideen Box')

frame = tk.Frame(window, bg=bg)
frame.grid(sticky='nesw')

listbox = tk.Listbox(frame, selectmode='single', activestyle='none', width=40)
listbox.grid(row=0, column=0, rowspan=6, sticky='nesw', padx=5, pady=5)
listbox.bind('<ButtonRelease-1>', updateItemClick)

frm_edit = tk.Frame(frame, bg=bg)
frm_edit.grid(row=6, column=0, sticky='nesw', padx=5)

btn_plus = tk.Button(frm_edit, text='+')
btn_plus.pack(side='left')

btn_minus = tk.Button(frm_edit, text='-')
btn_minus.pack(side='left')

lbl_titel = tk.Label(frame, text='Titel', bg=bg)
lbl_titel.grid(row=0, column=1, sticky='nw')
var_titel = tk.StringVar()
txt_titel = tk.Entry(frame, textvariable=var_titel)
txt_titel.grid(row=1, column=1, sticky='nw', padx=5, pady=5)

lbl_tag = tk.Label(frame, text='Tags', bg=bg)
lbl_tag.grid(row=0, column=2, sticky='nw')
var_tag = tk.StringVar()
txt_tag = tk.Entry(frame, textvariable=var_tag)
txt_tag.grid(row=1, column=2, sticky='nw', padx=5, pady=5)

lbl_description = tk.Label(frame, text='Beschreibung', bg=bg)
lbl_description.grid(row=2, column=1, sticky='nw')
var_description = tk.StringVar()
txt_description = tk.Entry(frame, textvariable=var_description)
txt_description.grid(row=3, column=1, sticky='nw', padx=5, pady=5)

lbl_color = tk.Label(frame, text='Farbe', bg=bg)
lbl_color.grid(row=2, column=2, sticky='nw')
var_color = tk.StringVar()

colors = ['white', 'gray', 'yellow', 'pink']
btn_color = []
frm_btn_color = tk.Frame(frame, bg=bg)
frm_btn_color.grid(row=3, column=2, sticky='nesw', padx=5, pady=5)

for index, color in enumerate(colors):
    btn_color.append(tk.Radiobutton(frm_btn_color, text=color, value=color,indicatoron=0,
                                    variable=var_color, selectcolor=color, background=color))
    btn_color[-1].grid(row=0, column=index)


txt_content = st.ScrolledText(frame, wrap='word')
txt_content.grid(row=4, rowspan=2, column=1, columnspan=2, sticky='nesw', padx=5, pady=5)

btn_save = tk.Button(frame, text='Speichern')
btn_save.grid(row=6, column=2, sticky='e', padx=5, pady=5)


updateListBox()
updateItem()

window.mainloop()


```



## Ergebnis

![Sammler](https://github.com/NeumannSven/pyshb_programmierkurs/blob/master/session5/ibox.png "Sammler")





[Inhalt](../agenda.md)
