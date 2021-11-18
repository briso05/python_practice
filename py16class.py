#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

print('Hello python')

print(sys.argv[0])
print("====================")

#OOP : Object Orianted Programming
#num,id,pw,userName,tel
class MemberVO:
    num = 1
    id = "admin"
    pw = "hi1212"
    userName = "yangssem"
    tel = "010"
m = MemberVO()
print(m)
print(type(m))
print(m.num,m.id,m.pw,m.userName,m.tel)

print("====================")
#create class NoteBookVO
#num,model,price,color

class NoteBookVO:
    num = 1
    model = "lg001"
    price = 2000
    color = "#00ff00"

nb = NoteBookVO()
print(nb)
print(nb.num,nb.model,nb.price,nb.color)
