from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import DeskLocators
from helpers import registration_data
import data

class TestLogout:
    def test_logout(self, driver):
        login_btn = WebDriverWait(driver, 20).until(expected_conditions.visibility_of_element_located(DeskLocators.REGISTRATION_BTN))
        login_btn.click()
        
        email_input = WebDriverWait(driver,20).until(expected_conditions.visibility_of_element_located(DeskLocators.EMAIL))
        email_input.send_keys(data.EMAIL_EXIST_USER)
        driver.find_element(*DeskLocators.PASSWORD).send_keys(data.PASSWORD_EXIST_USER)
        driver.find_element(*DeskLocators.LOGIN_BTN).click()

        WebDriverWait(driver, 20).until(expected_conditions.visibility_of_element_located(DeskLocators.LOGOUT_BTN))
       
        driver.find_element(*DeskLocators.LOGOUT_BTN).click()
        login_btn = WebDriverWait(driver, 20).until(expected_conditions.visibility_of_element_located(DeskLocators.REGISTRATION_BTN))
    

        assert login_btn
        assert not driver.find_elements(*DeskLocators.USER_AVATAR)
