import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()

def test_emptyCredentialLogin():
    driver.get('http://localhost:8000/admin/login/')
    userelem = driver.find_element_by_name("username")
    userelem.clear()
    userelem.send_keys("")
    userelem.send_keys(Keys.RETURN)
    pswdelem = driver.find_element_by_name("password")
    pswdelem.clear()
    pswdelem.send_keys("")
    pswdelem.send_keys(Keys.RETURN)

    validation_message = userelem.get_attribute('required')
    if validation_message in userelem.text:
        assert(False)
    else:
        assert(True)
    driver.quit()
