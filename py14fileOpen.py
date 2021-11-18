#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

print('Hello python')

print(sys.argv[0])
print("====================")

f = open("py14.txt","r")
print(f)
print(type(f))

while True:
    data = f.readline()
    if not data: break

    print(data,end="")

print("====================")
fw = open("py14fw.txt","w")
#fw.write("Hello wrold\n")

names = ['kim','lee','yang','han']
#0 kim
#1 lee
#...
#3 han
for i,name in enumerate(names):
    fw.write("%d %s\n" % (i,name))

#cat py14fw.txt


fw = open("py14fw.txt","r")
lst = fw.readlines()
print(lst)

print("====================")

f.close()
fw.close()
