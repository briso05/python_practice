#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print('Hello python')

#python3 py01hello.py
#chmod u+x py01hello.py  > ./py01hello.py

#line : (;)
#block : {} No
#depth : line sort

a = 10
print(a)
print(type(a))

a = 5
print(type(1/a))
print(type(a*2))
print(type(a**2))


#5 5 5
#5
print(a,end=" ")
print(a,end=" ")
print(a,end=" ")
print()

print(a,"hello",100,"world")

b = True
c = False
print(b,c)
print(type(b))

d = 7+7j
print(d)
print(type(d))

name = "kim"
print(name)
print(type(name))


lst = [11,22,33,33,33]
print(lst)
print(type(lst))

tp = (1,2,3,4,5)
print(tp)
print(type(tp))

s = {11,22,33,11,22,44}
print(s)
print(type(s))

dt = {'name':'kim','age':33}
print(dt)
print(type(dt))

name = "kim"
age = 30
txt = name+" "+str(age)
txt = "{} {}".format(name,age)
txt = "%s %d" % (name,age)
print(txt)

txt = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"

txt = '''aaaaaaaaaaaaaa
bbbbbbbbbbbbbb
cccccccccccccc'''

print(txt)

