#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

print('Hello python')

print(sys.argv[0])
print("====================")

#def >> function,method

def sum():
    print("sum()")

sum()


print("====================")

def sum(a,b):
    print("sum(a,b):",a,b)

sum(11,22)


print("====================")

def sum():
    print("sum()")
    return 100

print("sum():",sum())

print("====================")
def sum(x,y):
    print("sum(x,y):", x,y)
    return x+y

result = sum(111,222)
print("result:",result)

print("====================")

#10 : 55, 100:5050 >> def sum
def sum(x):
    hap = 0
    for i in range(1,x+1):
        hap += i
    return hap

print(sum(10))
print(sum(100))

print("=============================")
#function call back -> usually used in event handling
def testFn(fn):
    print(fn(10,3))

def minus(x,y):
    return x-y

testFn(minus)
