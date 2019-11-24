import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()

def test_submitVulgarComment():
    driver.get('http://localhost:8000/blog/')
    blog = driver.find_element_by_name("blogpost")
    blog.click()
    elem = driver.find_element_by_name("commentSubmit")
    name = driver.find_element_by_name("author")
    name.send_keys("Gerald")
    comment = driver.find_element_by_name("body")
    comment.send_keys("FUCKFUCKFUCK")
    elem.send_keys(Keys.RETURN)
    driver.quit()
