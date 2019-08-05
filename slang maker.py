# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 21:44:41 2018

@author: DSC
"""
string=input('enter something: ')
vowels='aeiouAEIOU'
str=''
for char in string:
   if char not in vowels:
        str+=char
print(str)