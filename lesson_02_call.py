#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 11:35:17 2021

@author: fennieliang
"""

from lesson_02_class import Text_process as tp

string = 'I’m willing to bet you’ve Taipei heard of Harry Poter for 1000 times.'

p=tp.doc_length(string)

print(p)

'''
##### test split word method #########
p=tp.doc_split_word(string)
print(p)
################################
'''

'''
##### test names method #########
matches = tp.find_name(string)

for word in matches:
    print (word[0])
################################    
'''

'''    
###### test digit method ############################    
matches = tp.find_digit(string)

for word in matches:
    print (word[0])
    
################################
'''