#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
#import tkinter
from tkinter import *

print('Hello python')

print(sys.argv[0])
print("====================")

#python GUI : tkinter

top = Tk()

lstBox = Listbox(top)
def onselected(event):
    index = event.widget.curselection()[0]
    print("onselected:",index,event.widget.get(index))
lstBox.bind("<<ListboxSelect>>",onselected)

lst = ['yangssem','python','linux','java']
lst = lst *5
lst.reverse()
for item in lst:
    lstBox.insert(0,item)


lstBox.pack()
top.mainloop()
