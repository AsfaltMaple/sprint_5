import pytest
import data
from selenium import webdriver


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()
    driver.get(data.URL)
    yield driver
    driver.quit()
