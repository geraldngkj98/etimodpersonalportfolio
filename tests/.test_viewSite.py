import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()

def test_viewSite():
    driver.get('http://localhost:8000/admin/login/')
    userelem = driver.find_element_by_name("username")
    userelem.clear()
    userelem.send_keys("Gerald")
    userelem.send_keys(Keys.RETURN)
    pswdelem = driver.find_element_by_name("password")
    pswdelem.clear()
    pswdelem.send_keys("27D29r98")
    pswdelem.send_keys(Keys.RETURN)

    driver.find_element_by_xpath('//a[@href="'+"/"+'"]').click()

