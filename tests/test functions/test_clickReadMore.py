import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()

def test_clickReadMore():
    driver.get('http://localhost:8000/projects/')
    elem = driver.find_element_by_name("test")
    elem.click()
    driver.quit()
