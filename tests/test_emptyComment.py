import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()

def test_submitEmptyComment():
    driver.get('http://localhost:8000/blog/')
    blog = driver.find_element_by_name("blogpost")
    blog.click()
    elem = driver.find_element_by_name("commentSubmit")
    name = driver.find_element_by_name("author")
    elem.send_keys(Keys.RETURN)
    validation_message = name.get_attribute('required')
    if validation_message in name.text:
        assert(False)
    else:
        assert(True)
    driver.quit()
