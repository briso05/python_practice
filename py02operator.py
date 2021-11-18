#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print('Hello python')

su = 100
result = su + 1
print('result',result)

name = "kim"
age = 20
print(name,age)
print(name+str(age))

#+,-,*,/,%
print('10+3=',10+3)
print('10-3=',10-3)
print('10*3=',10*3)
print('10**3=',10**3)
print('10/3=',10/3)
print('10//3=',10//3)
print('10%3=',10%3)

#&,|,^
#1100
#1010
print('12&10=',12&10)
print('12|10=',12|10)
print('12^10=',12^10)

#+=,-=,,,,&=,|=,^=
x = 10
x += 100
print(x)
x -= 100
print(x)
x = 12
x &= 10
print(x)

#++x,x++ NO
x = x + 1
x = x + 1
x = x + 1
x += 1
x += 1
x += 1
print(x)


#and, or
print(True and True)
print(True and False)

print(False or False)
print(True or False)

#==,!=,>,<,>=,<=
print('10==10',10==10)
print('10!=10',10!=10)
print('10<10',10<10)
print('10>10',10>10)
print('10>=10',10>=10)
print('10<=10',10<=10)

#bit move shift
#1000 : 0100
print(8>>1)
#1000 : 10000
print(8<<1)

#condition ? TrueValue : FalseValue >> NO
# condition and TrueValue or FalseValue >>OK
print(True and "KIM" or "LEE")
print(False and "KIM" or "LEE")

b = True
b = False
result = b and "KIM" or "LEE"
print("result:",result)

#TrueValue if True else  FalseValue
print("yangssem" if  True else  "Han")
print("yangssem" if  False else  "Han")

result = "yangssem" if b else "Han"
print("result:",result)





