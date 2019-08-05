# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 13:03:28 2018

@author: DSC
"""
import random,sys
def getAnswer(answerNumber):
       if answerNumber == 1:
           return 'It is certain'
       elif answerNumber == 2:
           return 'It is decidedly so'
       elif answerNumber == 3:
           return 'Yes'
       elif answerNumber == 4:
           return 'Reply hazy try again'
       elif answerNumber == 5:
           return 'Ask again later'
       elif answerNumber == 6:
           return 'Concentrate and ask again'
       elif answerNumber == 7:
           return 'My reply is no'
       elif answerNumber == 8:
           return 'Outlook not so good'
       elif answerNumber == 9:
           return 'Very doubtful'
       elif answerNumber == 10:
           return 'Nipun is not human!'
       
print('Welcome to Magic8Ball, Please ask a question and press 8. ')
while True:
    answer = input("You could type exit to Exit. ")
    if answer =='8':
        r = random.randint(1, 10)
        fortune = getAnswer(r)
        print(fortune)
    elif answer =='exit': sys.exit()
    