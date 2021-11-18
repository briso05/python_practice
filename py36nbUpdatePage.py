#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from tkinter import *
import py36nbSelectAllPage as selp
import sqlite3

print('Hello python')

print(sys.argv[0])
print("====================")

class UpdatePage:
    def __init__(self,notebook):
        self.top = Tk()
        self.top.title("Update Page")
        self.top.geometry("250x200+150+100")
        self.top.resizable(False,False)

        print("notebook:", notebook)
        
        Label(self.top, text="num:").grid(row=0)
        Label(self.top, text="model:").grid(row=1)
        Label(self.top, text="price:").grid(row=2)
        Label(self.top, text="color:").grid(row=3)
        
        self.numEntry = Entry(self.top)
        self.numEntry.insert(0, notebook[0])
        self.numEntry.grid(row=0,column=1)
        self.numEntry.configure(state='readonly')

        self.modelEntry = Entry(self.top)
        self.modelEntry.insert(0, notebook[1])
        self.modelEntry.grid(row=1,column=1)

        self.priceEntry = Entry(self.top)
        self.priceEntry.insert(0, notebook[2])
        self.priceEntry.grid(row=2,column=1)
        
        self.colorEntry = Entry(self.top)
        self.colorEntry.insert(0, notebook[3])
        self.colorEntry.grid(row=3,column=1)

        updateOkButton = Button(self.top, text="Update", command=self.onUpdateOk)
        updateOkButton.grid(row=4, column=1)

        deleteOkButton = Button(self.top, text="Delete", command=self.onDeleteOk)
        deleteOkButton.grid(row=4, column=0)

        mainloop()


    def onUpdateOk(self):
        num = self.numEntry.get()
        model = self.modelEntry.get()
        price = self.priceEntry.get()
        color = self.colorEntry.get()
        print("onUpdateOk", num, model, price, color)

        conn = sqlite3.connect("py36notebook.db")
        sql_update = '''
            update notebook set model = ?, price = ?, color = ? where num = ?
        '''
        values = (model, price, color, num)

        conn.execute(sql_update, values)
        conn.commit()

        print("updateOk")
        self.top.destroy()
        selp.SelectAllPage()


    def onDeleteOk(self):
        num = self.numEntry.get()
        print("onUpdateOk", num)

        conn = sqlite3.connect("py36notebook.db")
        sql_delete = '''
            delete from notebook where num = ?
        '''
        conn.execute(sql_delete, num)
        conn.commit()

        print("deleteOk")
        self.top.destroy()
        selp.SelectAllPage()

        
