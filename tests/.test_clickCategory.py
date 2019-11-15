import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()

def test_clickCategory():
    driver.get('http://localhost:8000/blog/2/')
    elem = driver.find_element_by_name("category")
    elem.click()          
