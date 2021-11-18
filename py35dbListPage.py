#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
#import tkinter
from tkinter import *
import py35dbUpdatePage as up
import sqlite3

print('Hello python')

print(sys.argv[0])
print("====================")

#python GUI : tkinter
class ListPage:
    def __init__(self):

        self.top = Tk()
        self.top.title("ListPage")
        self.top.geometry("150x200+100+100")
        self.top.resizable(False,False)

        lstBox = Listbox(self.top,selectbackground="orange")
        lstBox.bind("<<ListboxSelect>>",self.onselected)
        
        print("self.selectAll()")
        lst = self.selectAll()

        #lst = ['Gildong Hong','python Kim','linux Lee','java Han']
        #lst = lst *5
        lst.reverse()
        for item in lst:
            lstBox.insert(0,item)


        lstBox.pack()
        mainloop()
    
    def selectAll(self):
        print("selectAll...")
        conn = sqlite3.connect("py34test.db")
        sql_selectAll = '''
            select * from test order by num desc
        '''
        cursor = conn.execute(sql_selectAll)
        rows = cursor.fetchall()
        print(rows)
        return rows

    def onselected(self,event):
        index = event.widget.curselection()[0]
        name = event.widget.get(index)
        print("onselected:",index,name)
        self.top.destroy()
        up.UpdatePage(name)


#ListPage()
