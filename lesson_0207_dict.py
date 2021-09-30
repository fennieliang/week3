#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 15:52:38 2021

@author: fennieliang
"""

#dict {key1:value1,key2:value2,...} each pair in the dict is an item

dic1 = {
        "orange":1,
        "melon":2,
        "apple":3}

dic2 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

myDictionary = {
  "English": 80,
  "Mathmatics": 100,
  "Physics": 77,
  "Chemistry": 60,
  "English":90
}

'''
for item in myDictionary.items():
    print (f"this item is: {item}")
    
     
  
for key, value in dic1.items():
    print(f"key={key}; value={value}")
       
'''
for key in dic1.keys():#value cannot be found vis versa
    value = dic1.get(key)
    print (f"key = {key}",end="; ")
    print (f"value = {value}")
    
   
######################
#practice 0206 print the key of value = melon
########################


dic2 = dic1#equals to dic2 = dic1



#dic1.pop("orange")#pop out the specific item
#print (f"the reduced dic: {dic1}")

dic1.popitem()#pop out the last item
print (f"the new poped dic: {dic1}")

    
dic1.update({"pear": 4})#adding new item to the dict
print (f"the new dic: {dic1}")

# equals to 
dic2={"plum":5}
dic1.update(dic2)
print (dic1)


dic1.clear()#clear items in dic1
print (dic1)
