#!/usr/bin/env python
# coding: utf-8

# In[7]:


import time
 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select, WebDriverWait
 
import requests
 
# variable to store the name of the contact
# contact = "Vinodh Personal"
contact = "Lokesh Reddy"
#variable to store message
message = "Hi, this is automated message from vinodh script"

url = "https://web.whatsapp.com"

#open a Whatsapp Web interface which automatically asks you to scan the QR code
driver = webdriver.Chrome('/Users/vinodhkumar/Downloads/chromedriver')

driver.get(url)
print("Scan QR Code and press Enter")
input() # used to pause the interface until user presser enter
print("Running ...")
time.sleep(15)

selected_contact = driver.find_element_by_xpath("//span[@title='"+contact+"']")
selected_contact.click() # select contact
message = driver.find_element_by_xpath('//div[@class= "_3uMse"]')
message.send_keys('Hey This Automated software')
send = driver.find_element_by_xpath('//button[@class= "_1U1xa"]')
send.click()
print('done')


# In[ ]:




