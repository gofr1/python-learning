#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
driver.maximize_window()
driver.get('http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html')

source = driver.find_element_by_xpath('//*[@id="box3"]')
dest = driver.find_element_by_xpath('//*[@id="box103"]')
action = ActionChains(driver)

action.drag_and_drop(source, dest).perform()

