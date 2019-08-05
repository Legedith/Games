# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 13:53:04 2018

@author: DSC
"""

n=83
low = 0
high =100
guess =int((low+high)/2)
print("Please think of a number between 0 and 100!")
char=''
while char !='c':
    guess =int((low+high)/2)
    print('Is your secret number '+str(guess)+'?')
    print("Enter 'h' to indicate the guess is too high.",end='')
    print(" Enter 'l' to indicate the guess is too low.",end='')
    print(" Enter 'c' to indicate I guessed correctly.",end='')
    
    char = input('')
    if char == 'h':
        high = guess
    elif char == 'l':
        low = guess
    elif char =='c':
        break
    else:
        print("Sorry, I did not understand your input.")
print("Game over. Your secret number was: "+str(guess))
