import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()

def test_wrongLoginInfo():
    driver.get('http://localhost:8000/admin/login/')
    userelem = driver.find_element_by_name("username")
    userelem.clear()
    userelem.send_keys("Gerald")
    userelem.send_keys(Keys.RETURN)
    pswdelem = driver.find_element_by_name("password")
    pswdelem.clear()
    pswdelem.send_keys("asdasd")
    pswdelem.send_keys(Keys.RETURN)

    error = driver.find_element_by_xpath("//*[contains(text(), 'Please enter the correct username and password for a staff account. Note that both fields may be case-sensitive.')]")
    if error.is_displayed():
        assert(True)
    else:
        assert(False)
    driver.quit()
