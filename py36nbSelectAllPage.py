#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from tkinter import *
import sqlite3
import py36nbUpdatePage as up

print('Hello python')

print(sys.argv[0])
print("====================")

class SelectAllPage:
    def __init__(self):
        self.top = Tk()
        self.top.title("SelectAll Page")
        self.top.geometry("200x200+100+100")
        self.top.resizable(False,False)

        lstBox = Listbox(self.top, selectbackground="orange")
        lstBox.bind("<<ListboxSelect>>", self.onSelected)

        print("self.selectAll()")
        lst = self.selectAll()
        lst.reverse()

        for item in lst:
            lstBox.insert(0,item)

        lstBox.pack()
        mainloop()


    def selectAll(self):
        print("====selectAll====")
        conn = sqlite3.connect("py36notebook.db")
        sql_selectAll = '''
            select * from notebook order by num desc
        '''
        cursor = conn.execute(sql_selectAll)
        rows = cursor.fetchall()
        print(rows)
        return rows

    def onSelected(self, event):
        index = event.widget.curselection()[0]
        notebook = event.widget.get(index)
        print("onSelected:",index,notebook)
        self.top.destroy()
        up.UpdatePage(notebook)


