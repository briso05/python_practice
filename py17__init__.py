#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

print('Hello python')

print(sys.argv[0])
print("====================")

#OOP : Object Orianted Programming
#num,id,pw,userName,tel
class MemberVO:
    #def __init__(self):
    #    print("__init__")

    def __init__(self,num,id,pw,userName,tel):
        self.num = num
        self.id = id
        self.pw = pw
        self.userName = userName
        self.tel = tel

m = MemberVO(1,"admin","hi1234","kim","02")
#m = MemberVO()
print(m)
print(type(m))
print(m.num,m.id,m.pw,m.userName,m.tel)

print("====================")
#create class NoteBookVO
#num,model,price,color

class NoteBookVO:
    def __init__(self,num,model,price,color):
        self.num = num
        self.model = model
        self.price = price
        self.color = color

nb = NoteBookVO(11,"sm001",3000,"#ffff00")
print(nb)
print(nb.num,nb.model,nb.price,nb.color)
print("====================")

#ScoreVO : num,name,kor,eng,math
class ScoreVO:
    num = 0
    name = ""
    kor = 0
    eng = 0
    math = 0

    def setNum(self,num):
        self.num = num
    def getNum(self):
        return self.num

    def setName(self,name):
        self.name = name
    def getName(self):
        return self.name

    def setKor(self,kor):
        self.kor = kor
    def getKor(self):
        return self.kor

    def setEng(self,eng):
        self.eng = eng
    def getEng(self):
        return self.eng

    def setMath(self,math):
        self.math = math
    def getMath(self):
        return self.math

s = ScoreVO()
print(s.num,s.name,s.kor,s.eng,s.math)

s.setNum(11)
s.setName("kim")
s.setKor(99)
s.setEng(88)
s.setMath(77)
print(s.num,s.name,s.kor,s.eng,s.math)
print(s.getNum(),s.getName(),s.getKor(),s.getEng(),s.getMath())

#java null >>> python None
s = None
print(s)
