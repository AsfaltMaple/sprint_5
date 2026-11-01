import pytest
from selenium import webdriver

@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()
    driver.get("https://qa-desk.education-services.ru/")
    yield driver
    driver.quit()
