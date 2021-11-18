#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

print('Hello python')

print(sys.argv[0])
print("====================")
def test(name,kor,eng,math):
    total = kor+eng+math
    avg = total/3
    grade=""
    if avg>=90:
        grade="A"
    elif avg>=80:
        grade="B"
    elif avg>=70:
        grade="C"
    else:
        grade="F"
    print(name,kor,eng,math,total,avg,grade)
test("kim",99,88,77)
print("====================")

def test2(*args):
    print("test2",args,type(args))
    for item in args:
        print(item)

test2(11,22,33,44,55,66)
test2(11,44,55,66)

print("====================")
#input(),name, kor,eng,math,total,avg,grade
def score():
    print("Input name:")
    name = input()
    print("Input kor:")
    kor = input()
    print("Input eng:")
    eng = input()
    print("Input math:")
    math = input()

    total = int(kor) + int(eng) + int(math)
    avg = total/3

    grade=""
    if avg>=90:
        grade="A"
    elif avg>=80:
        grade="B"
    elif avg>=70:
        grade="C"
    else:
        grade="F"
    print(name,kor,eng,math,total,avg,grade)
    return (name,kor,eng,math,total,avg,grade)

st = score()
print(st,type(st))
print("====================")

def printList(lst):
    for item in lst:
        print(item)



printList([11,22,33])





