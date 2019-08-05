# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 02:15:53 2018

@author: DSC
"""

def reverse(a):
        rem = 0
        res = 0
        while (a%10 !=0 or a/10 != 0):
            rem = a%10
            res = res*10+rem
            a = a//10
        return res
a = 0
b = 0
for i in range(10000):
    for j in range(10000):
        b = i*j
        a = reverse(i+j)
        if a==b:
            print(i,j,a)
        
        
        
        
        
