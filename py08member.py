#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print('Hello py08member.py')

def insert(vo):
    print("insert()..",vo)
    return 1

def update(vo):
    print("update()..",vo)
    return 1

def delete(vo):
    print("delete()..",vo)
    return 1

def selectAll():
    print("selectAll()..")
    return [{"name":"kim","id":"admin"},
    {"name":"lee","pw":"hi123456"}]

def searchList(searchKey,searchWord):
    print("searchList()..")
    print("searchKey:",searchKey)
    print("searchWord:",searchWord)
    return [{"name":"kim","id":"admin"},
    {"name":"lee","pw":"hi123456"}]

def selectOne():
    print("selectOne()...")
    return {"name":"yang","id":"aaa","pw":"hi1212"}
    
