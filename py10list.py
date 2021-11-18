#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

print('Hello python')

print(sys.argv[0])
print("====================")

#notebook,member
#nblist
nblist = [
        {"num":1,"model":"sm001","price":1000,"color":"#595959"},
        {"num":2,"model":"sm002","price":2000,"color":"#121212"}
        ]
print(nblist)
#mlist
mlist = [
        {"num":1001,"id":"admin01","pw":"hi1212","name":"kim","tel":"010"},
        {"num":1002,"id":"admin02","pw":"hi2222","name":"kim2","tel":"02"}
        ]
print(mlist)

print("=====================")
lst = []
lst = [0,0,0,0]


lst = [0 for i in range(10)]
lst = [1 for i in range(10)]
lst = ["kim" for i in range(10)]
#0-9
lst = [i for i in range(10)]
#1-10
lst = [i+1 for i in range(10)]
#0,1,4,9,16,,,81
lst = [i**2 for i in range(10)]

print(lst)
print(type(lst))
print(len(lst))


print("=====================")

for item in lst:
    print(item,end=" ")
print()
print("=====================")
for i in range(len(lst)):
    print(i,end=" ")
print()

print("=====================")

for index,item in enumerate(lst):
    print(index,item)


print("=====================")

print(lst[-1],lst[len(lst)-1])


print("=====================")
lst = [(i+1)*11 for i in range(5)]
print(lst)

lst = lst + lst
print(lst)

lst = lst * 2
print(lst)

print("=====================")
lst.append(100)
lst.append(200)
print(lst)


print("=====================")
#first item remove
lst.remove(11)
print(lst)

#delete index 
del lst[0]
print(lst)

#delete range
lst[2:5] = []
print(lst)

print("=====================")
lst.reverse()
print(lst)

lst.sort()
print(lst)

lst.reverse()
print(lst)
print("=====================")

lst.insert(0,"kim")
print(lst)
lst.insert(10,"yang")
print(lst)
print("=====================")

#last item remove
print(lst.pop())
print(lst.pop())
print(lst)

print("=====================")
lst[1] = 2000
print(lst)
lst[1] = [66,77,88]
print(lst)

lst[1:3] = [99,99]
print(lst)
print("=====================")

lst = []
print(lst)
lst.append([11,22,33])
lst.append([44,55,66])
print(lst)

print("=====================")
lst = []
lst.extend([77,88,99])
lst.extend([11,22,33])
print(lst)

print("=====================")
lst = []
lst.append({"num":1,"name":"kim","age":33})
lst.append({"num":1,"name":"kim","age":33})
lst.append({"num":1,"name":"kim","age":33})
lst.append({"num":1,"name":"kim","age":33})
print(lst)


print("=====================")
#append,extend,pop,insert,remove
#sort,reverse,len,type
#del lst[0], lst[1:3]
#i for i in range(10):
lst = []
#mission

print(lst)

print("=====================")
#tuple to list
lst = list((1,2,3))
print(type(lst))



