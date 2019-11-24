import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.maximize_window()

def test_changeWrongPswd():
    driver.get('http://localhost:8000/admin/login/')
    userelem = driver.find_element_by_name("username")
    userelem.clear()
    userelem.send_keys("Gerald")
    userelem.send_keys(Keys.RETURN)
    pswdelem = driver.find_element_by_name("password")
    pswdelem.clear()
    pswdelem.send_keys("27D29r98")
    pswdelem.send_keys(Keys.RETURN)

    driver.refresh()
    driver.find_element_by_xpath('//a[@href="'+"/admin/password_change/"+'"]').click()

    time.sleep(1)
    oldpswd = driver.find_element_by_xpath('//*[@id="id_old_password"]')
    oldpswd.send_keys("27D29r98")

    time.sleep(1)
    newpswd1 = driver.find_element_by_xpath('//*[@id="id_new_password1"]')
    newpswd1.send_keys("ETIModule19")

    time.sleep(1)
    newpswd2 = driver.find_element_by_xpath('//*[@id="id_new_password2"]')
    newpswd2.send_keys("OMEGAlul1")
    newpswd2.send_keys(Keys.RETURN)

    error = driver.find_element_by_xpath("//ul[@class='errorlist']/li")
    if error.is_displayed():
        assert(True)
    else:
        assert(False)
    driver.quit()
