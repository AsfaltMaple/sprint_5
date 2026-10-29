import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import DeskLocators

def browser_settings():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    return chrome_options

@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome(options=browser_settings())
    try:
        driver.get("https://qa-desk.education-services.ru/")
        yield driver
    finally:
        driver.quit()
