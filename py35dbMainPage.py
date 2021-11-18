#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from tkinter import *
from py35dbListPage import *
from py35dbInsertPage import *
import sqlite3

print('Hello python')

print(sys.argv[0])
print("====================")
#1.connection 
conn = sqlite3.connect("py34test.db")

#to confirm that there is any table
#ls
#sqlite3 py34test.db ".tables"

#2. create table
sql_create_table = '''
create table if not exists test(
num integer primary key autoincrement,
fname text,
lname text)
'''

conn.execute(sql_create_table)

class MainPage:
    def __init__(self):
        self.top = Tk()
        self.top.title("MainPage")
        self.top.geometry("100x120+0+0")
        self.top.resizable(False,False)

        listButton = Button(self.top, text="ListPage", command=self.onGoToList)
        listButton.grid(row=0, column=0)
       
        insertButton = Button(self.top, text="InsertPage", command=self.onGoToInsert)
        insertButton.grid(row=1, column=0)
        mainloop()

    def onGoToList(self):
        print("onGoToList")
        ListPage()

    def onGoToInsert(self):
        print("onGoToInsert")
        InsertPage()


MainPage()
