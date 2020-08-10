[Inhalt](../agenda.md)

# Applikation


## Aufgabe

Umbau der Applikation aus der Session 5 in eine Objectorientierte Applikation (OOP) und der Benutzung des Patters Model View Controller (MVC)  

## Programmcode 

### imports
```python

import json
import os
```

### Klasse Model
```python
class IdeenBoxModel:
    def __init__(self):
        self.data = self.load()
    
    def load(self, filename='data.json'):
        if not os.path.exists(filename):
            json.dump([['new item', "description", ['tags'], 'white', 'more information']], open(filename, 'w'))
        return json.load(open(filename))

    def save(self, filename='data.json'):
        with open(filename, 'w') as projectfile:
            json.dump(self.data, projectfile)
    
    def getData(self):
        return self.data
    
    def setData(self, index, item):
        self.data[index] = item
    
    def delItem(self, index):
        del(self.data[index])
        return len(self.data) - 1 
        
    def addItem(self, index):
        self.newitem = self.data[index].copy()
        self.newitem[0] += "_{}".format(index)
        self.data.append(self.newitem)
        return len(self.data) - 1 
```

### Klasse Controller

```python
class IdeenBoxCtrl:
    def __init__(self, model, view):
        self.model = model
        self.selectedIndex = 0
        self.selectedItem = self.model.getData()[self.selectedIndex]
        self.view = view
        
        self.view.setListBoxCallback(self.displayClickedItem)
        self.view.setSaveBtnCallback(self.saveProject)
        self.view.setPlusBtnCallback(self.addItem)
        self.view.setMinusBtnCallback(self.delItem)
        
        self.updateListBox()
        self.view.mainloop()


    def addItem(self, event):
        self.selectedIndex = self.model.addItem(self.selectedIndex)
        self.selectedItem = self.model.getData()[self.selectedIndex]
        self.updateListBox()

    def delItem(self, event):
        self.selectedIndex = self.model.delItem(self.selectedIndex)
        self.selectedItem = self.model.getData()[self.selectedIndex]
        self.updateListBox()

    def saveProject(self, event):
        self.selectedItem = self.view.getDisplayedItem()
        self.model.setData(self.selectedIndex, self.selectedItem)
        self.model.save()
        self.updateListBox()

    def updateListBox(self):
        self.view.deleteList()
        for item in self.model.getData():
            self.view.appendList(item[0], background=item[3])
        self.view.displayItem(self.selectedItem)

    def displayClickedItem(self, event):
        self.selectedIndex = event.widget.curselection()[0]
        self.selectedItem = self.model.getData()[self.selectedIndex]
        self.view.displayItem(self.selectedItem)
```

### Klasse View

```python
import tkinter as tk
import tkinter.scrolledtext as st

class IdeenBoxView(tk.Tk):
    
    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        
        self.bg = '#C5C5C5'
        self.title('Ideen Box')

        self.frame = tk.Frame(self, bg=self.bg)
        self.frame.grid(sticky='nesw')

        self.listbox = tk.Listbox(self.frame, selectmode='single', activestyle='none', width=40)
        self.listbox.grid(row=0, column=0, rowspan=6, sticky='nesw', padx=5, pady=5)
        

        self.frm_edit = tk.Frame(self.frame, bg=self.bg)
        self.frm_edit.grid(row=6, column=0, sticky='nesw', padx=5)

        self.btn_plus = tk.Button(self.frm_edit, text='+')
        self.btn_plus.pack(side='left')

        self.btn_minus = tk.Button(self.frm_edit, text='-')
        self.btn_minus.pack(side='left')

        self.lbl_titel = tk.Label(self.frame, text='Titel', bg=self.bg)
        self.lbl_titel.grid(row=0, column=1, sticky='nw')
        self.var_titel = tk.StringVar()
        self.txt_titel = tk.Entry(self.frame, textvariable=self.var_titel)
        self.txt_titel.grid(row=1, column=1, sticky='nw', padx=5, pady=5)

        self.lbl_tag = tk.Label(self.frame, text='Tags', bg=self.bg)
        self.lbl_tag.grid(row=0, column=2, sticky='nw')
        self.var_tag = tk.StringVar()
        self.txt_tag = tk.Entry(self.frame, textvariable=self.var_tag)
        self.txt_tag.grid(row=1, column=2, sticky='nw', padx=5, pady=5)

        self.lbl_description = tk.Label(self.frame, text='Beschreibung', bg=self.bg)
        self.lbl_description.grid(row=2, column=1, sticky='nw')
        self.var_description = tk.StringVar()
        self.txt_description = tk.Entry(self.frame, textvariable=self.var_description)
        self.txt_description.grid(row=3, column=1, sticky='nw', padx=5, pady=5)

        self.lbl_color = tk.Label(self.frame, text='Farbe', bg=self.bg)
        self.lbl_color.grid(row=2, column=2, sticky='nw')
        self.var_color = tk.StringVar()

        self.colors = ['white', 'gray', 'yellow', 'pink']
        self.btn_color = []
        self.frm_btn_color = tk.Frame(self.frame, bg=self.bg)
        self.frm_btn_color.grid(row=3, column=2, sticky='nesw', padx=5, pady=5)

        for index, color in enumerate(self.colors):
           self.btn_color.append(tk.Radiobutton(self.frm_btn_color, text=color, value=color, indicatoron=0,
                                           variable=self.var_color, selectcolor=color, background=color))
           self.btn_color[-1].grid(row=0, column=index)

        self.txt_content = st.ScrolledText(self.frame, wrap='word')
        self.txt_content.grid(row=4, rowspan=2, column=1, columnspan=2, sticky='nesw', padx=5, pady=5)

        self.btn_save = tk.Button(self.frame, text='Speichern')
        self.btn_save.grid(row=6, column=2, sticky='e', padx=5, pady=5)


    def setListBoxCallback(self, callbackMethod):
        self.listbox.bind('<ButtonRelease-1>', callbackMethod)

    def setSaveBtnCallback(self, callbackMethod):
        self.btn_save.bind('<ButtonRelease-1>', callbackMethod)

    def setPlusBtnCallback(self, callbackMethod):
        self.btn_plus.bind('<ButtonRelease-1>', callbackMethod)

    def setMinusBtnCallback(self, callbackMethod):
        self.btn_minus.bind('<ButtonRelease-1>', callbackMethod)
        
    def deleteList(self):
        self.listbox.delete(0, 'end')        
    
    def appendList(self, item, background):
        self.listbox.insert('end', item)
        self.listbox.itemconfig('end', background=background)        
        
    def displayItem(self, selectedItem):
        self.var_titel.set(selectedItem[0])
        self.var_description.set(selectedItem[1])
        self.var_tag.set(','.join(selectedItem[2]))
        self.var_color.set(selectedItem[3])
        self.txt_content.delete('1.0', 'end')
        self.txt_content.insert('end', selectedItem[4])
    
    def getDisplayedItem(self):
        return [self.var_titel.get(),
                self.var_description.get(),
                [tag.strip() for tag in self.var_tag.get().split(',')],
                self.var_color.get(),
                self.txt_content.get('1.0', 'end')]
            
    def updateItemClick(self, event):
        self.ctrl.selectedIndex = event.widget.curselection()[0]
        self.updateItem()

        
    def updateItem(self):
        self.crtl.selectedItem = self.crl.data[self.crtl.selectedIndex]
        self.var_titel.set(self.crtl.selectedItem[0])
        self.var_description.set(self.crtl.selectedItem[1])
        self.var_tag.set(','.join(self.crtl.selectedItem[2]))
        self.var_color.set(self.crtl.selectedItem[3])
        self.txt_content.delete('1.0', 'end')
        self.txt_content.insert('end', self.crtl.selectedItem[4])
```

### Starten der Applikation

```python
if __name__ == "__main__":
    model = IdeenBoxModel()
    view = IdeenBoxView()
    ctrl = IdeenBoxCtrl(model, view)
```

## Ergebnis

![Sammler](https://github.com/NeumannSven/pyshb_programmierkurs/blob/master/session5/ibox.png "Sammler")

## Kompletter Source Code
[ibox.pyw](ibox.pyw)


[Inhalt](../agenda.md)

