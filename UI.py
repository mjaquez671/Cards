import tkinter as tk
from tkinter import ttk
import sqlite3

def build(app):
    mainwin = app
    btn = tk.Button(master=mainwin, text='Press Me')
    btn.pack()
    return mainwin


class mainWindow:
    def __init__(self):
        app = tk.Tk()

        app = build(app)
        app.mainloop()


#x = mainWindow()



def connect():

    con1 = sqlite3.connect("db.db")
    cur1 = con1.cursor()
    cur1.execute("CREATE TABLE IF NOT EXISTS table1(id INTEGER PRIMARY KEY, First TEXT, Surname TEXT)")
    con1.commit()
    con1.close()
def View():
    con1 = sqlite3.connect("db.db")
    cur1 = con1.cursor()
    cur1.execute("SELECT * FROM table1")
    rows = cur1.fetchall()
    for row in rows:
        print(row)
        tree.insert("", tk.END, values=row)
    con1.close()
# connect to the database
connect()
root = tk.Tk()

tree = ttk.Treeview(root, column=("c1", "c2", "c3","c4","c5"), show='headings')
table_headers = ["Requestor","Reason","Shop","Timestamp","Notes"]
table_header_number = ["#1","#2","#3","#4","#5"]
for i in range(5):
    tree.column(table_header_number[i],anchor = tk.CENTER)
    tree.heading(table_header_number[i], text = table_headers[i])



tree.pack()

button1 = tk.Button(text="Display data", command=View)

button1.pack(pady=10)

root.mainloop()
