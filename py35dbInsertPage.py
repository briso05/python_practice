#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from tkinter import *
from py35dbListPage import *
import sqlite3

print('Hello python')

print(sys.argv[0])
print("====================")

class InsertPage:
    def __init__(self):
        self.top = Tk()
        self.top.title("InsertPage")
        self.top.geometry("250x200+300+100")
        self.top.resizable(False,False)

        Label(self.top,text="fname:").grid(row=0)
        Label(self.top,text="lname:").grid(row=1)

        self.fnameEntry = Entry(self.top)
        self.fnameEntry.insert(0,"Gildong")
        self.fnameEntry.grid(row=0,column=1)
        self.lnameEntry = Entry(self.top)
        self.lnameEntry.insert(0,"Hong")
        self.lnameEntry.grid(row=1,column=1)

        okButton = Button(self.top, text="OK", command=self.onclick)
        okButton.grid(row=2, column=1)
        
        mainloop()

    def onclick(self):
        fname = self.fnameEntry.get()
        lname = self.lnameEntry.get()
        print("onclicK", fname, lname)

        conn = sqlite3.connect("py34test.db")
        sql_insert = '''
            insert into test(fname, lname) values(?,?)
        '''
        values = (fname, lname)
        conn.execute(sql_insert,values)
        conn.commit()
        
        self.top.destroy()
        ListPage()

#InsertPage()
