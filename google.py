# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 19:45:33 2019

@author: DSC
"""
import random
import csv
csvFile = open('cheat.csv', 'w', newline='', encoding='utf-8')
writer = csv.writer(csvFile)

def boo(i):
    return bin(i).replace("0b","").replace("", " ").strip()
    
#bin(n).replace("0b","")
prefix = 'What is the binary equivalent of '
for i in range(129):
    writer.writerow([prefix+str(i), boo(i), boo(i+random.randint(1,15)), boo(i+random.randint(15,30))  ])
    
