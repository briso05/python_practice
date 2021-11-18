#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

print('Hello python')

print(sys.argv[0])
print("====================")

#tuple >> readonly

tp = ()
tp = (0,0,0,0)
#tp = (0 for i in range(10)) : Error
tp = tuple([0 for i in range(10)])

print(tp)
print(type(tp))
print("len:",len(tp))

print("=====================")

#tp.append(100) Error

tp = tp + (11,22,33)
print(tp)
tp = tp * 2
print(tp)


print("=====================")
tp = (11,22,33)
for item in tp:
    print(item)

for index,item in enumerate(tp):
    print(index,item)





