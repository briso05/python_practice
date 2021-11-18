#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

print('Hello python')

print(sys.argv[0])
print("====================")
#Korean ssn, getter,setter
class Korean:
    ssn = ""
    def setSsn(self,ssn):
        self.ssn = ssn
    def getSsn(self):
        return self.ssn

k = Korean()
print(k.ssn)
k.setSsn("123456-1234567")
print(k.getSsn())
print(vars(k))
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
class Student(Person,Korean):
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
s.setSsn("654321-7654321")
print(s.getSsn())
print(vars(s))

print("====================")
print(Student.__bases__)
print(issubclass(Student,Korean))
print(issubclass(Student,Person))




