import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()

def test_clickInBlogPost():
    driver.get('http://localhost:8000/blog/')
    elem = driver.find_element_by_name("blogpost")
    elem.click()          
