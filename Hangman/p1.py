# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 20:58:43 2018

@author: DSC
"""

secretWord = 'apple'
temp = secretWord 
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's','a',]
##originalList = list(' '.join(secretWord))
##a='qwertyuiopasdfghjklzxcvbnm'
##for i in temp:
##    temp = temp.replace(i,'_ ')
##temp = list(temp)
###print(temp,originalList)
##for i in originalList[::2]:
##    if i in lettersGuessed:
##        i = '_'
##print(originalList)
#ans=''
#for char in secretWord:
#    if char in lettersGuessed:
#        ans+=char
#    else:
#        ans+="_"
#    ans+=" "
import string
a= "".join(sorted(set(string.ascii_lowercase)-set(lettersGuessed)))