#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from tkinter import *
import py35dbListPage as lp
import sqlite3
print('Hello python')

print(sys.argv[0])
print("====================")

class UpdatePage:
    def __init__(self,name):
        self.top = Tk()
        self.top.title("UpdatePage")
        self.top.geometry("250x200+150+100")
        self.top.resizable(False,False)

        print("name:",name)

        Label(self.top,text="num:").grid(row=0)
        Label(self.top,text="fname:").grid(row=1)
        Label(self.top,text="lname:").grid(row=2)

        self.numEntry = Entry(self.top)
        self.numEntry.insert(0, name[0])
        self.numEntry.grid(row=0,column=1)
        self.numEntry.configure(state='readonly')
        self.fnameEntry = Entry(self.top)
        self.fnameEntry.insert(0,name[1])
        self.fnameEntry.grid(row=1,column=1)
        self.lnameEntry = Entry(self.top)
        self.lnameEntry.insert(0,name[2])
        self.lnameEntry.grid(row=2,column=1)

        updateOkButton = Button(self.top, text="UpdateOK", command=self.onUpdateOk)
        updateOkButton.grid(row=3, column=1)
        
        deleteOkButton = Button(self.top, text="DeleteOK", command=self.onDeleteOk)
        deleteOkButton.grid(row=3, column=0)

        mainloop()

    def onUpdateOk(self):
        num = self.numEntry.get()
        fname = self.fnameEntry.get()
        lname = self.lnameEntry.get()
        print("onUpdateOk", num, fname, lname)
        conn = sqlite3.connect("py34test.db")
        sql_update = '''
            update test set fname = ?, lname = ? where num = ?
        '''
        values = (fname, lname, num)

        conn.execute(sql_update, values)
        conn.commit()
        print("updateOk")
        self.top.destroy()
        lp.ListPage()


    def onDeleteOk(self):
        num = self.numEntry.get()
        print("onDeleteOk", num)
        conn = sqlite3.connect("py34test.db")
        sql_delete = '''
            delete from test where num = ?
        '''
        conn.execute(sql_delete, num)
        conn.commit()

        print("deleteOK")
        
        self.top.destroy()
        lp.ListPage()

