#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import sqlite3
from tkinter import *
from py36nbSelectAllPage import *

print('Hello python')

print(sys.argv[0])
print("====================")

class InsertPage:
    def __init__(self):
        self.top = Tk()
        self.top.title("Insert Page")
        self.top.geometry("250x200+300+100")
        self.top.resizable(False,False)

        Label(self.top,text="model:").grid(row=0)
        Label(self.top,text="price:").grid(row=1)
        Label(self.top,text="color:").grid(row=2)

        self.modelEntry = Entry(self.top)
        self.modelEntry.insert(0,"LG Gram")
        self.modelEntry.grid(row=0,column=1)

        self.priceEntry = Entry(self.top)
        self.priceEntry.insert(0, "100")
        self.priceEntry.grid(row=1,column=1)

        self.colorEntry = Entry(self.top)
        self.colorEntry.insert(0, "#FFFFFF")
        self.colorEntry.grid(row=2,column=1)

        okButton = Button(self.top, text="OK", command=self.insertOk)
        okButton.grid(row=3, column=1)

        mainloop()

    def insertOk(self):
        model = self.modelEntry.get()
        price = self.priceEntry.get()
        color = self.colorEntry.get()
        print("insertOk",model,price,color)

        conn = sqlite3.connect("py36notebook.db")
        sql_insert = '''
            insert into notebook(model, price, color) values(?,?,?)
        '''
        values = (model, price, color)
        conn.execute(sql_insert, values)
        conn.commit()

        self.top.destroy()
        SelectAllPage()
