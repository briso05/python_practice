#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from tkinter import *
from py30ListPage import *
from py31InsertPage import *
from py32UpdatePage import *

print('Hello python')

print(sys.argv[0])
print("====================")

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
