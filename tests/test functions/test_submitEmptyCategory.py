import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.maximize_window()

def test_emptyCatSubmit():
    driver.get('http://localhost:8000/admin/login/')
    userelem = driver.find_element_by_name("username")
    userelem.clear()
    userelem.send_keys("Gerald")
    userelem.send_keys(Keys.RETURN)
    pswdelem = driver.find_element_by_name("password")
    pswdelem.clear()
    pswdelem.send_keys("27D29r98")
    pswdelem.send_keys(Keys.RETURN)

    time.sleep(1)
    driver.find_element_by_xpath('//a[@href="'+"/admin/blog/category/add/"+'"]').click()
    elem = driver.find_element_by_name("_save")
    elem.click()

    error = driver.find_element_by_xpath("//ul[@class='errorlist']/li")   
    if error.is_displayed():
        assert(True)
    else:
        assert(False)
    driver.quit()
