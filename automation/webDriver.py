#!/usr/bin/env python3

# pip3 install selenium
# drivers should be downloaded from:
# https://github.com/mozilla/geckodriver/releases
# on linux place geckodriver to your PATH folder like /usr/bin

from selenium import webdriver
driver = webdriver.Firefox()
driver.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

# # can use Copy XPath from Inspect Element page:
# messageField = driver.find_element_by_xpath('//*[@id="user-message"]')
messageField = driver.find_element_by_id('user-message')
messageField.send_keys('Hello World')

showMessageButton = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/div[2]/form/button')
showMessageButton.click()

#

additionalField1 = driver.find_element_by_xpath('//*[@id="sum1"]')
additionalField1.send_keys('10')

additionalField2 = driver.find_element_by_xpath('//*[@id="sum2"]')
additionalField2.send_keys('11')

getTotalButton = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div[2]/form/button')
getTotalButton.click()

