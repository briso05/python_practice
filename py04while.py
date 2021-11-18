#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

print('Hello python')

print(sys.argv[0])
print("====================")


i=0
while True:
    i+=1
    print("while",i)
    #if i==100 : break
    #if i==10:
    #    i=0
    if i==5 : continue
    print("aaaa")
    if i==10 : break

    print("End Input x:")
    x = input()
    if x=="x": break

