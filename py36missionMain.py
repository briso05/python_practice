#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from tkinter import *
import py36nbSelectAllPage as selp
import py36nbInsertPage as insp

print('Hello python')

print(sys.argv[0])
print("====================")
#tkinter + sqlite3
#NoteBook : MissionMain, InsertPage, UpdatePage, SelectAllPage
#insert, update, delete, selectAll
#db name : py36notebook.db
#table name : notebook
#columns : num, model, price, color

class MainPage:
    def __init__(self):
        self.top = Tk()
        self.top.title("Main Page")
        self.top.geometry("150x100+50+50")
        self.top.resizable(False,False)
       
        selectAllButton = Button(self.top, text="SelectAll Page",command=self.onGoToSelectAll)
        selectAllButton.grid(row=0,column=0)

        insertButton = Button(self.top, text="Insert Page", command=self.onGoToInsert)
        insertButton.grid(row=1,column=0)
        
        mainloop()
        
    def onGoToSelectAll(self):
        print("onGoToSelectAll")
        selp.SelectAllPage()

    def onGoToInsert(self):
        print("onGoToInsert")
        insp.InsertPage()

MainPage()
