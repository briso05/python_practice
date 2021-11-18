#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

print('Hello python')

print(sys.argv[0])
print("====================")


#w:write, a:append
#with open("py15.txt","w") as f:
with open("py15.txt","a") as f:
    f.write("Hello python\n")

print("====================")
f = open("py15.txt","r")
print(f.readlines())



f.close()



