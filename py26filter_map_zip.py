#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

print('Hello python')

print(sys.argv[0])
print("====================")

lst = [0,1,-1,2,-2,3,-3,-5]
print(lst)

# item >=0 : [0,1,2]
# create def testFn()
def testFn(lst):
    print(lst)
    lst2 = []
    for item in lst:
        if item>=0:
            lst2.append(item)

    return lst2

print(testFn(lst))


print("======filter==============")

def fn(item):
    return item >= 0

for item in lst:
    print(fn(item))

print(filter(fn,lst))
print(list(filter(fn,lst)))
print(list(filter(lambda item:item>=0,lst)))


print("======map==============")
lst = [1,2,3,4,5,6,7]
#testFn2 : item**2

def testFn2(lst):
    lst2 = []
    for item in lst:
        lst2.append(item**2)
    return lst2

print(testFn2(lst))

def fn2(item):
    return item**2

print(fn2(10))
print(map(fn2,lst))
print(list(map(fn2,lst)))
print(list(map(lambda item:item**2,lst)))

print("======zip=========")
print(zip([1,2,3],[4,5,6]))
print(list(zip([1,2,3],[4,5,6])))
print(list(zip([1,2,3],[4,5,6],[10,20,30])))

print(list(zip("abcd","1234")))


