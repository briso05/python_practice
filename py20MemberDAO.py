#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class MemberDAO:
    #insert,update,delete,selectAll,
    #searchList,selectOne
    def insert(self,vo):
        print("insert()..",vo.toString())
        return 1

    def update(self,vo):
        print("update()..",vo.toString())
        return 1

    
    def delete(self,vo):
        print("delete()..",vo.toString())
        return 1

    def selectOne(self,vo):
        print("selectOne()..",vo.toString())
        return MemberVO()

    def selectAll(self):
        print("selectAll()..")
        lst = []
        lst.append(MemberVO())
        lst.append(MemberVO())
        return lst

    def searchList(self,searchKey,searchWord):
        print("searchList()..")
        print("searchKey:",searchKey)
        print("serchWord:",searchWord)
        lst = []
        lst.append(MemberVO())
        lst.append(MemberVO())
        return lst




class MemberVO:
    num = 1
    id = "admin"
    pw = "hi1234"
    name = "kim"
    tel = "02"


    def toString(self):
        return "MemberVO : %d,%s,%s,%s,%s \n" % (self.num,self.id,self.pw,self.name,self.tel)

dao = MemberDAO()
vo = MemberVO()
print(dao.insert(vo))
print(dao.update(vo))
print(dao.delete(vo))
print(dao.selectOne(vo).toString())

lst = dao.selectAll()
print(lst)
for vo in lst:
    print(vo.toString())

#################
#mission
#StudentDAO,insert,update,delete,selectAll
#           selectOne,searchList
#StudentVO,num,name,kor,eng,math
