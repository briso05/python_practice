#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

print('Hello python')

print(sys.argv[0])
print("====================")

#json object : key,value
dic = {}
dic = {'name':'yangssem','tel':'010'}

print(dic)
print(type(dic))
print("len:",len(dic))


print("====================")

print('name:',dic['name'])
print('name:',dic.get('name'))

print('tel:',dic['tel'])
print('tel:',dic.get('tel'))

print("====================")
print('name' in dic)
print('name2' in dic)

print("====================")

print(dic)
dic['addr'] = "seoul"
dic['score'] = [99,88,77]
dic['info'] = {'hobby':'baseball','email':'kim@aaa.com'}
print(dic)
print(dic['score'][0])
print(dic['info']['hobby'])
print("====================")

dic = {0:11,1:22}
dic = {i:i*10  for i in range(10)}
print(dic)
print(type(dic))
print(dic[0],dic[1])


dic = {'0':11,'1':22}
dic = {str(i):i*10 for i in range(10)}
print(dic)
print(dic['0'],dic['1'])

dic = {'key'+str(i):i*10 for i in range(10)}
print(dic)
for key in dic:
    print(key, dic[key])


print("====================")
print(dic.keys())
for key in dic.keys():
    print(key)
print("====================")
print(dic.values())
for value in dic.values():
    print(value)

print("====================")

print(dic.items())
for key,item in dic.items():
    print(key,item)

print("====================")
dic.clear()
#dic = {}
print(dic)


print("====================")
