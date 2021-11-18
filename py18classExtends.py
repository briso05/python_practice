#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

print('Hello python')

print(sys.argv[0])
print("====================")

#Person pname,getter,setter
class Person:
    pname = ""
    def setPname(self,pname):
        self.pname = pname
    def getPname(self):
        return self.pname

p = Person()
print(p.pname)
p.setPname("kim")
print(p.getPname())
print(vars(p))
print("===================")
#Student sname,getter,setter
class Student(Person):
    sname = ""
    def setSname(self,sname):
        self.sname = sname
    def getSname(self):
        return self.sname
s = Student()
print(s.sname)
s.setSname("lee")
print(s.getSname())
s.setPname("yang")
print(s.getPname())
print(vars(s))





