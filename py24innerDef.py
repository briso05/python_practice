#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

print('Hello python')

print(sys.argv[0])
print("====================")

print(-11)
print(abs(-11))
print("====================")

print([])  #[]
#not exists (0,"",'') : True 
print(all([]))  #True
print(all([1,2,3]))  #True
print(all([1,2,3,0]))  #False
print(all([1,2,3,'']))  #False

#is not exists (o,"",'') : True 

print("====================")
print(any([1,0,0,"",0]))  #True


print("====================")
print(dir(sys))

print("====================")
print(dir([]))

print("====================")
print(dir(()))


print("====================")
print(dir(set()))


print("====================")
print(dir({}))


print("====================")
print(chr(97),chr(98),chr(66))


print("====================")
print(7/3)  #2.33333...
print(7//3) #2
print(7%3)  #1
print(divmod(7,3))     #(2,1)


print("====================")
print("kim"+"lee")
print("'kim' + 'lee'")
print(eval("'kim' + 'lee'"))
print(eval("22 + 33"))


print("====================")
# 0xffff
print(10,hex(10))  #0xa
print(255,hex(255)) #0xff


print("====================")
#  0o12
print(10,oct(10))  #0o12
print(255,oct(255)) #0o377

print("====================")
#  0b1111
print(10,bin(10)) #0b1010
print(255,bin(255))  #0b11111111



print("====================")
print(id("a"),id("b"),id("c"))


print("====================")
value = "CAT"

if value == "cat":
    print("aaa")

if value == "CAT":
    print("AAA")

print(dir(str))

if str.casefold(value) == "cat":
    print("casefold...")

if str.lower(value) == "cat":
    print("lower...")

value = "Hello"
if str.upper(value) == "HELLO":
    print("upper...")

if value.startswith("H"):
    print("startswith...")

if value.endswith("o"):
    print("endswith...")

