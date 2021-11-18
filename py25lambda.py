#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

print('Hello python')

print(sys.argv[0])
print("====================")

def testFn(x):
    return x**2

print(testFn(3))


print("====argument================")
print(lambda x : x**2)
print((lambda x : x**2)(4))

def testFn4(fn):
    print(fn(7))


testFn4(lambda x:x**2)

print("====var================")
testFn2 = lambda x : x**2
print(testFn2(5))


print("====return================")
def testFn3():
    return lambda x: x**2

print(testFn3())
print(testFn3()(6))





