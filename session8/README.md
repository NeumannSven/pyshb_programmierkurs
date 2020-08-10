# Datenbanken

## PostgreSQL


### Module pg8000
```python
import pg8000
# für eine schönere Ausgabe
from pprint import pprint
```

### Anlegen und befüllen von Tabellen


Alle Funktionen von Session 7 die Tabellen erzeugen und befüllen, können ohne Änderung übernommen werden.   


### Abfragen von Daten

Tabelle CUSTOMER

```python
def getCustomers(cur):
    sql_stmt = """
    SELECT * FROM CUSTOMER;"""
        
    return [row for row in cur.execute(sql_stmt)]
```

Tabelle PARTLISTS

```python
def getPartLists(cur):
    sql_stmt = """
    SELECT * FROM PARTLISTS;"""
        
    return [row for row in cur.execute(sql_stmt)]
```

Tabelle PARTS

```python
def getParts(cur):
    sql_stmt = """
    SELECT * FROM PARTS;"""
        
    return [row for row in cur.execute(sql_stmt)]
```

Tabelle PROJECTS

```python
def getProjects(cur):
    sql_stmt = """
    SELECT * FROM PROJECTS;"""
        
    return [row for row in cur.execute(sql_stmt)]
```

### Zeige Tabellen in einem Dialog

```python
def showDatabase(cur):

    import tkinter.ttk as ttk
    import tkinter as tk
    
    master = tk.Tk()
    master.title('Datenbank')
    
    tree=ttk.Treeview(master)
    
    tree["columns"]=("one","two","three")
    tree.column("#0", width=100, minwidth=100, stretch=tk.NO)
    tree.column("one", width=100, minwidth=100, stretch=tk.YES)
    tree.column("two", width=500, minwidth=200, stretch=tk.YES)
    tree.column("three", width=80, minwidth=50, stretch=tk.NO)

    tree.heading("#0",text="Tabellen",anchor=tk.W)
    tree.heading("one", text="Name",anchor=tk.W)
    tree.heading("two", text="Beschreibung",anchor=tk.W)
    tree.heading("three", text="Preis",anchor=tk.E)

    #Customer
    customerTab=tree.insert("", 1, "_0", text="Kunden", values=("","",""))
    for customer in getCustomers(cur):
        tree.insert(customerTab, "end", f"a{customer[0]}", text='', values=(customer[1],customer[2], customer[3]))

    #Projekte
    projectsTab=tree.insert("", 1, "_1", text="Projekte", values=("","",""))
    for project in getProjects(cur):
        tree.insert(projectsTab, "end", f"b{project[0]}", text='', values=(project[1],project[2], project[3]))
    
    #Artikel
    partTab=tree.insert("", 1, "_2", text="Artikel", values=("","",""))
    for part in getParts(cur):
        tree.insert(partTab, "end", f"c{part[0]}", text='', values=(part[1],part[2], part[3]))

    #Stücklisten
    partlistTab=tree.insert("", 1, "_3", text="Stücklisten", values=("","",""))
    for part in getPartLists(cur):
        tree.insert(partlistTab, "end", f"d{part[0]}", text='', values=(part[1],part[2], part[3]))

    tree.pack(side=tk.LEFT,fill=tk.X)
    
    master.mainloop()
```


### Ausführen der Funktionen

```python
if __name__ == "__main__":
    con = pg8000.connect(user="sven", password="", database="pyshb")
    cur = con.cursor()
    
    createCustomer(cur)
    createParts(cur)
    createProjects(cur)
    createPartLists(cur)
    
    showDatabase(cur)
    
    con.commit()
    con.close()
```





