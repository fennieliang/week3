#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 11:51:38 2021

@author: fennieliang
"""
import sys

#tuple (item1, item2, item3....)
t = ("chicken", "duck", "dog", "cat", "chicken") # tuple is not a unique item container
'''
print (t[0])



count = t.count("chicken")
print (f"there are {count} chicken in the tuple")

for i in range(len(t)):#use len to get the length of the t tuple
    print (f"forward list:{t[i]}")
'''
for i in range(len(t)):#use len to get the length of the t tuple
    print (f"backword list:{t[-i-1]}")

'''
t[0]= "sheep" #items in tuple are immutable (unchangeable)
print (t[0]) 

'''

t2 = (1, 2, 3) #does support concatenation
print (t+t2)

t = t2 #tuple can be reassigned
print (t)

