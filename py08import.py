#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import py08AAA
import py08AAA as pa
from py08AAA import *
#from py08member import *
import py08member as m
import py08notebook as nb
#notebook : num,model,price,color

print('Hello py08import.py')

print(sys.argv[0])
print("====================")

py08AAA.score()
pa.score()
score()

#py08member.py : insert,update,delete,selectAll,selectOne,searchList

print("====================")
print("insert:",m.insert({"name":"kkk","id":"kk123","pw":"hi1212"}))

print("====================")
print("update:",m.update({"name":"rrr","id":"rr213","pw":"hi1212"}))

print("====================")
print("delete:",m.delete({"name":"qqq","id":"qq123","pw":"hi1212"}))

print("====================")
print("selectAll:",m.selectAll())

print("====================")
print("searchList:",m.searchList("name","ki"))

print("====================")
print("selectOne:",m.selectOne())

print("====================")

print("===notebook=================")
print("insert:",nb.insert({"model":"k001","price":3000,"color":"#ffff00"}))

print("====================")
print("update:",nb.update({"num":88,"model":"r001","price":7777,"color":"#777777"}))

print("====================")
print("delete:",nb.delete({"num":66}))

print("====================")
print("selectAll:",nb.selectAll())

print("====================")
print("searchList:",nb.searchList("model","lg"))

print("====================")
print("selectOne:",nb.selectOne({"num":44}))

print("====================")






