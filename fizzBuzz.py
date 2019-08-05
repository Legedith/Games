# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 13:47:47 2018

@author: DSC
"""
for i in range(1,100):
    s=''
    if i%3==0:
       s+= 'Fizz'
    if i%5==0:
        s+= 'Buzz'
    if not s:
        print(i)
    else: print(s)