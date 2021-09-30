#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 14:40:57 2021

@author: fennieliang
"""
#useful links for regular expression

#http://python-learnnotebook.blogspot.com/2018/10/python-regular-expression.html
#https://www.tutorialspoint.com/python/python_reg_expressions.htm

#regular expression
import re
string = 'I bet you’ve heard of Harry James Poter for 11,000,000.00 times.'
#string = "We are leaving in Taipei City in Taiwan"
'''
#match capital words
#matches = re.finditer('([A-Z][a-z]+\s)', string)
#matches = re.finditer('([A-Z][a-z]+\s+[A-Z][a-z]+\s)', string)
matches = re.finditer('([A-Z][a-z]+\s){1,}', string)
for word in matches:
    print (word[0])


try names with first and last names or even middle names
then a find_name function to the class
'''



#match money style digits
#matches = re.finditer('(\d+\s)', string)
#matches = re.finditer('(\d+\.\d\d\s)', string)
matches = re.finditer('(\d+,){0,}(\d+.)(\d+)', string)
for digit in matches:
    print (digit[0])  
    
'''
try big money with decimals
add a find_digit function to the class 
'''