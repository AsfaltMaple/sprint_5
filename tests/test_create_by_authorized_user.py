from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import DeskLocators
from helpers import registration_data
import data

class TestAdvCreate:

   # def test_create_adv_by_authorized_user(self, driver):
    #    login_btn = WebDriverWait(driver, 20).until(expected_conditions.visibility_of_element_located(DeskLocators.REGISTRATION_BTN))
    #   login_btn.click()
        
    #    email_input = WebDriverWait(driver,20).until(expected_conditions.visibility_of_element_located(DeskLocators.EMAIL))
    #    email_input.send_keys(data.EMAIL_EXIST_USER)
    #    driver.find_element(*DeskLocators.PASSWORD).send_keys(data.PASSWORD_EXIST_USER)
    #    driver.find_element(*DeskLocators.LOGIN_BTN).click()



    def test_create_adv_by_unauthorized_user(self, driver):
        create_btn = WebDriverWait(driver, 20).until(expected_conditions.visibility_of_element_located(DeskLocators.CREATE_ADV_BTN))
        assert create_btn.is_displayed()
        assert create_btn.is_enabled()

        driver.find_element(*DeskLocators.CREATE_ADV_BTN).click()
        auth_is_needed_msg = WebDriverWait(driver, 20).until(expected_conditions.visibility_of_element_located(DeskLocators.AUTHORIZATION_IS_NEEDED_MSG))

        assert auth_is_needed_msg.is_displayed()