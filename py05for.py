#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

print('Hello python')

print(sys.argv[0])
print("====================")




#0~9
for i in range(10):
    print(i,end="")

print()

#10~19
for i in range(10,20):
    print(i,end=" ")
print()


print("=====================")
#2*1=2,2*2=4,,,2*9=18
#3*1=3,3*2=6,,,3*9=27
#...
#9*1=9,9*2=18,,,9*9=81

for x in range(2,10):
    for i in range(1,10):
        #print("{}*{}={}".format(x,i,x*i))
        print("{}*{}={}".format(x,i,x*i),end=" ")
    print()


print("=====================")
lst = [11,22,33,44,55]

print("lst length:",len(lst))
print("yangssem length:",len("yangssem"))

for item in lst:
    print(item)


for i in range(len(lst)):
    print(i,lst[i])


#sum for
sum=0
for item in lst:
    sum+=item
print("sum:",sum)





