# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 18:31:44 2018

@author: DSC
"""

an_letter = 'aeiouAEIOU'
word = input("I Am gonna cheer for you, What's your name: ")
times = int(input("Enthusiasm level (1-10): "))
for char in word:
    if char in an_letter:
        print('Give me an '+char+'! '+char)
    else:
        print('Give me a '+char+'! '+char)
for i in range(times):
    print(word)
    