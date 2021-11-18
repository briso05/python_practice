#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from tkinter import *
import py30ListPage as lp
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
        print("split():",name.split())

        Label(self.top,text="fname:").grid(row=0)
        Label(self.top,text="lname:").grid(row=1)

        self.fnameEntry = Entry(self.top)
        self.fnameEntry.insert(0,name.split()[0])
        self.fnameEntry.grid(row=0,column=1)
        self.lnameEntry = Entry(self.top)
        self.lnameEntry.insert(0,name.split()[1])
        self.lnameEntry.grid(row=1,column=1)

        updateOkButton = Button(self.top, text="UpdateOK", command=self.onUpdateOk)
        updateOkButton.grid(row=2, column=1)
        
        deleteOkButton = Button(self.top, text="DeleteOK", command=self.onDeleteOk)
        deleteOkButton.grid(row=2, column=0)

        mainloop()

    def onUpdateOk(self):
        print("onUpdateOk", self.fnameEntry.get(), self.lnameEntry.get())
        self.top.destroy()
        lp.ListPage()

    def onDeleteOk(self):
        print("onDeleteOk", self.fnameEntry.get(), self.lnameEntry.get())
        self.top.destroy()
        lp.ListPage()

