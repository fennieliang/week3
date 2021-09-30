#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 13:25:08 2021

@author: fennieliang
"""
import re

string = 'I I I'

#clean paragraph
c_string =re.sub(r'[\W_]',' ', string)
#replace non-word character from the string
print (c_string)


c_string =re.sub(r' +',' ', c_string).strip()
#remove excess space, 
#and trim spaces appeared at the beginning and ending 
print (c_string)



'''
=======
practice 
add a doc_clean method to the class
======
'''  

from lesson_02_class import Text_process

p=Text_process#instantiate a class

words=p.doc_split_word(c_string)

print (words)

#bag of words
counts = dict()

for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1
        
print (counts)

'''
======
practice 
add a bag_word method to the class
======

'''  