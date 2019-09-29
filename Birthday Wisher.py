# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 19:58:56 2018

@author: DSC
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')

#names = ['Naveen Bsc B','Kochikame','Ninja Hattori'
        # ,'Doremon V2.0','Grey Matter Pi','Lakshita Bsc Sf' ]
names = ["Temp"]
#msg = "By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms."
input('Enter anything after scanning QR code')
time.sleep(5)
for name in names:
    search = driver.find_element_by_class_name('_2zCfw')
    search.click()
    search.send_keys(name)
    search.send_keys(Keys.RETURN)
    msg_box = driver.find_element_by_class_name('_3u328')
    while(time.localtime()[3]!=23 and time.localtime()[4]!=14):
        continue
    msg_box.send_keys("Happy Birthday Tanshi")
    msg_box.send_keys(Keys.RETURN)
