#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import re
print('Hello python')

print(sys.argv[0])
print("====================")

#re : RegExp : Regular Expressions
#[] >> word
#. >> \nf 
#(*) >> >=0
#(+) >> >=1
#{m,n} >> ea

#123456-1234567
pattern = re.compile("(\d{6})[-](\d{7})")
data = "kim 123456-1234567 010-1111-1111 lee 222222-2222222 010-2222-2222"
print(data)
print("====================")


#\g<0> : [123456-1234567]
print(pattern.sub("[\g<0>]",data))

print("====================")
print(re.sub("(\d{6})[-](\d{7})","[\g<0>]",data))
print("====================")

#\g<1> : 123456-*******
print(pattern.sub("\g<1>-*******",data))



#mission : [010-1111-1111]
print("====================")
print(re.sub("(\d{3})[-](\d{4})[-](\d{4})","[\g<0>]",data))
print("====================")

#[010]-[1111]-[1111]

print(re.sub("(\d{3})-(\d{4})-(\d{4})",r"[\1]-[\2]-[\3]",data))
print("====================")








