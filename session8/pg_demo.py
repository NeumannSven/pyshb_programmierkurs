
import pg8000
from pprint import pprint

def createCustomer(cur):
    sql_stmt = """
    CREATE TABLE CUSTOMER (
        ID INTEGER PRIMARY KEY,
        NAME TEXT,
        STREET TEXT,
        POSTCODE TEXT,
        CITY TEXT,
        COUNTRY TEXT);"""
    
    try:    
        cur.execute(sql_stmt)
        
        sql_stmts = [
        "INSERT INTO CUSTOMER (ID, NAME, STREET, POSTCODE, CITY, COUNTRY) VALUES('1', 'Kai Mauer', 'Berliner Strasse 112', '28199', 'Bremen', 'Germany');",
        "INSERT INTO CUSTOMER (ID, NAME, STREET, POSTCODE, CITY, COUNTRY) VALUES('2', 'Axel Höhle', 'Oldenburger Strasse 42', '28207', 'Bremen', 'Germany');",
        "INSERT INTO CUSTOMER (ID, NAME, STREET, POSTCODE, CITY, COUNTRY) VALUES('3', 'Reiner Engel', 'Hauptstrasse 2', '27087', 'Stuhr', 'Germany');",
        "INSERT INTO CUSTOMER (ID, NAME, STREET, POSTCODE, CITY, COUNTRY) VALUES('4', 'Anna Nass', 'Abendland Platz 76', '28309', 'Bremen', 'Germany');",
        "INSERT INTO CUSTOMER (ID, NAME, STREET, POSTCODE, CITY, COUNTRY) VALUES('5', 'Mario Ahner', 'Zum Hochofen 6', '67271', 'Nackterwäldchen', 'Germany');",
        "INSERT INTO CUSTOMER (ID, NAME, STREET, POSTCODE, CITY, COUNTRY) VALUES('6', 'Tim Buktu', 'Am Waldsee 23', '29693', 'Hodenhagen', 'Germany');"
        ]
        
        for stmt in sql_stmts:
            cur.execute(stmt)

    except Exception as e:
        print(e)


def createParts(cur):
    sql_stmt = """
    CREATE TABLE PARTS (
        ID INTEGER PRIMARY KEY,
        NAME TEXT,
        DESCRIPTION TEXT,
        PRICE REAL
    );"""
    
    try:
        cur.execute(sql_stmt)
        
        sql_stmts = [
        "INSERT INTO parts (ID, NAME, DESCRIPTION, PRICE) VALUES('1', 'ESP32', 'ESP32 NodeMCU Modul WLAN WiFi Development Board mit CP2102', '7.99');",
        "INSERT INTO parts (ID, NAME, DESCRIPTION, PRICE) VALUES('2', 'ESP8266', 'ESP8266 Mini NodeMcu mit ESP8266-12F WLAN Modul', '4.49');",
        "INSERT INTO parts (ID, NAME, DESCRIPTION, PRICE) VALUES('3', 'MB-102', 'Breadboard Steckbrett mit 830 Kontakten', '2.39');",
        "INSERT INTO parts (ID, NAME, DESCRIPTION, PRICE) VALUES('4', 'PB-400', 'Breadboard Steckbrett mit 400 Kontakten', '1.95');",
        "INSERT INTO parts (ID, NAME, DESCRIPTION, PRICE) VALUES('5', 'B10K', 'Trim Potentiometer mit Knopf 10K', '0.79');",
        "INSERT INTO parts (ID, NAME, DESCRIPTION, PRICE) VALUES('6', 'SPST-B', 'Mini Drucktaster Schalter AC 220V/2A/Schwarz', '1.60');",
        "INSERT INTO parts (ID, NAME, DESCRIPTION, PRICE) VALUES('7', 'SPST-R', 'Mini Drucktaster Schalter AC 220V/2A/Rot', '1.49');",
        "INSERT INTO parts (ID, NAME, DESCRIPTION, PRICE) VALUES('8', 'LED3R', 'LED 3mm Rot', '0.15');",
        "INSERT INTO parts (ID, NAME, DESCRIPTION, PRICE) VALUES('9', 'LED3Y', 'LED 3mm Gelb', '0.15');",
        "INSERT INTO parts (ID, NAME, DESCRIPTION, PRICE) VALUES('10', 'LED3G', 'LED 3mm Grün', '0.15');",
        "INSERT INTO parts (ID, NAME, DESCRIPTION, PRICE) VALUES('11', 'UA005', 'Breadboard Steckbrücken Drahtbrücken Set, Jumper Drähte mit 14 Verschiedene Längen + Flexible Breadboard Jumperkabel M/M + Pinzette', '11.99');",
        "INSERT INTO parts (ID, NAME, DESCRIPTION, PRICE) VALUES('12', 'DHT22', 'AM2302 Temperatursensor und Luftfeuchtigkeitssensor', '5.85');",
        "INSERT INTO parts (ID, NAME, DESCRIPTION, PRICE) VALUES('13', 'SG90', 'Micro Servo Motor 9G', '1.59');"
        ]
        
        for stmt in sql_stmts:
            cur.execute(stmt)

    except Exception as e:
        print(e)


def createProjects(cur):
    sql_stmt = """
    CREATE TABLE PROJECTS (
        ID INTEGER PRIMARY KEY,
        NUMBER TEXT,
        NAME TEXT,
        CUSTOMERS_ID INTEGER
    );"""
    

    try:    
        cur.execute(sql_stmt)
        
        sql_stmts = [
        "INSERT INTO projects (ID, NUMBER, NAME, CUSTOMERS_ID) VALUES('1', '2300-1', 'Zeitschalter', '1');",
        "INSERT INTO projects (ID, NUMBER, NAME, CUSTOMERS_ID) VALUES('2', '99x137-2', 'Temperaturanzeige', '2');",
        "INSERT INTO projects (ID, NUMBER, NAME, CUSTOMERS_ID) VALUES('3', '1742-3', 'Türöffner', '1');"
        ]
        
        for stmt in sql_stmts:
            cur.execute(stmt)

    except Exception as e:
        print(e)


def createPartLists(cur):
    sql_stmt = """
    CREATE TABLE PARTLISTS (
        ID INTEGER PRIMARY KEY,
        PROJECTS_ID INTEGER,
        QUANTITY INTEGER,
        PARTS_ID INTEGER,
        NOTE TEXT,
        FOREIGN KEY (PROJECTS_ID) REFERENCES PROJECTS(ID),
        FOREIGN KEY (PARTS_ID) REFERENCES PARTS(ID)
    );"""
    
    try:
        cur.execute(sql_stmt)

        sql_stmts = [
        "INSERT INTO PARTLISTS (ID, PROJECTS_ID, QUANTITY, PARTS_ID, NOTE) VALUES('1', '1', '2', '1', '');",
        "INSERT INTO PARTLISTS (ID, PROJECTS_ID, QUANTITY, PARTS_ID, NOTE) VALUES('2', '1', '5', '12', '');"
        ]
        
        for stmt in sql_stmts:
            cur.execute(stmt)

    except Exception as e:
        print(e)


def getCustomers(cur):
    sql_stmt = """
    SELECT * FROM CUSTOMER;"""
        
    return [row for row in cur.execute(sql_stmt)]

def getPartLists(cur):
    sql_stmt = """
    SELECT * FROM PARTLISTS;"""
        
    return [row for row in cur.execute(sql_stmt)]
        
    
def getParts(cur):
    sql_stmt = """
    SELECT * FROM PARTS;"""
        
    return [row for row in cur.execute(sql_stmt)]


def getProjects(cur):
    sql_stmt = """
    SELECT * FROM PROJECTS;"""
        
    return [row for row in cur.execute(sql_stmt)]



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


if __name__ == "__main__":
    con = pg8000.connect(user="sven", password="", database="pyshb")
    cur = con.cursor()
    
    #createCustomer(cur)
    #createParts(cur)
    #createProjects(cur)
    #createPartLists(cur)
    
    #pprint(getCustomers(cur))
    
    showDatabase(cur)
    
    
    con.commit()
    
    con.close()

