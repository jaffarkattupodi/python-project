import pytest
from selenium import webdriver
@pytest.fixture
def set():
    driver=webdriver.Chrome()
    driver.implicitly_wait(25)
    return driver

