#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

print('Hello python')

print(sys.argv[0])
print("====================")


#python3 py03sys_if.py 11 22 33
print(sys.argv)
print(sys.argv[1])
print(sys.argv[2])
print(sys.argv[3])

#11 22 33
print(11,22,33)

#112233
print(11,end="")
print(22,end="")
print(33,end="")
print()

#print("{}{}{}",11,22,33)
print("{}{}{}".format(11,22,33))



#cosole read : input()
print("Input your name:")
name = input()
print("name:",name)


print("Input kor:")
kor = input()
print("kor:",kor)


print("Input eng:")
eng = input()
print("eng:",eng)

total = int(kor) + int(eng)
print("total:",total)


#if True :
if False :
    print("a{}:{}:{}:{}".format(name,kor,eng,total))

print("b{}:{}:{}:{}".format(name,kor,eng,total))


if total>100:
    print("GOOD")
else:
    print("BAD")

if total/2>=90:
    print("A")
elif total/2>=80:
    print("B")
else:
    print("C")







