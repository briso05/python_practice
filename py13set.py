#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

print('Hello python')

print(sys.argv[0])
print("====================")

s = {0}
s = {1,2,3,3,3,3,4,5,5}

print(s)
print(type(s))
print("len:",len(s))

#print(s[0]) not index Error
lst = list(s)
print(lst[0])
lst = [1,2,3,3,3,3,3,3]
s = set(lst)
print(s)
print("=====add===============")
s.add(100)
s.add(100)
s.add(1000)
print(s)

print("=====remove===============")
s.remove(1000)
s.remove(3)
print(s)

print("=====update===============")
s = {11,22,33,11,22,33}
print(s)
s.update({44,55,66})
print(s)
print("====================")

s1 = set([11,22,33,33,44])
s2 = set([44,44,55,66])
print(s1,s2)

print("=======and=============")

#s3 = s1 + s2  #Error
s3 = set([]) and s2
s3 = False and s2
s3 = "" and s2
s3 = 0 and s2
print(s3)

print("=======and=============")
s3 = set([1]) and s2
s3 = 1 and s2
s2 = "kim" and s2
print(s3)


print("======or==============")
s3 = set() or s2
print(s3)




print("====&, intersection================")
s3 = s1 & s2
print(s3)

s3 = s1.intersection(s2)
print(s3)

print("===|, union=================")
s3 = s1 | s2
print(s3)

s3 = s1.union(s2)
print(s3)



print("==== -,difference ================")

s3 = s1 - s2
print(s3)

s3 = s1.difference(s2)
print(s3)

print("====================")

print(s3.pop())
print(s3.pop())
print(s3.pop())


