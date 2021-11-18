#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import random

print('Hello python')

print(sys.argv[0])
print("====================")

print(random.random())
print(random.random()*10)
print(int(random.random()*10))
print("-----")
for i in range(6):
    print(random.randrange(1,45+1))

print("====================")
#lotto numbers >> set

s = set()

while len(s) < 6 :
    num = random.randrange(1,45+1)
    print(num)
    s.add(num)
    print(len(s))

print(s)
lst = list(s)
lst.sort()
print(lst)
#print(dir([]))


print("====================")

card = ['A','J','Q','K']
print(card)
random.shuffle(card)
print(card)
print("chioce : ",random.choice(card))
print("====================")


card = ['sA','s2','s3','s4','s5','s6','s7','s8','s9','s10','sJ','sQ','sK']
random.shuffle(card)
print(random.choice(card))
# card 7 ea choice >> set







