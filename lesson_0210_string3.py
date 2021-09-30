#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 12:47:27 2021

@author: fennieliang
"""
#regular expression
import re

#split string into words
string = input ('input a string:') #my name is xxxxx
print (f"the string length: {len(string)}")
print ("\n")


words = re.split(' ',string) 
print (words)
#how about there is no space characters 
#in the input string

words = re.split('[\W_]',string) 
#grouping the split characters
print (words)
#try _
'''

=======
add a function named doc_split_word to the Text_process class
=======
'''



