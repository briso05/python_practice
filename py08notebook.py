#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print('Hello py08notebook.py')

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
    return [{"num":1,"model":"nb001","price":1000,"color":"#ffffff"},
            {"num":"2","model":"sm002","price":2000,"color":"#ff0000"}]

def searchList(searchKey,searchWord):
    print("searchList()..")
    print("searchKey:",searchKey)
    print("searchWord:",searchWord)
    return [{"num":1,"model":"nb001","price":1000,"color":"#ffffff"},
            {"num":"2","model":"sm002","price":2000,"color":"#ff0000"}]

def selectOne(vo):
    print("selectOne()...",vo)
    return {"num":99,"model":"lg999","price":3333,"color":"#00ff00"}
    
