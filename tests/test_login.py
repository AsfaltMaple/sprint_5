from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import DeskLocators
from helpers import registration_data
import data


class TestLogin:

    def test_login(self, driver):
        login_btn = WebDriverWait(driver, 20).until(expected_conditions.visibility_of_element_located(DeskLocators.REGISTRATION_BTN))
        login_btn.click()

        email_input = WebDriverWait(driver,20).until(expected_conditions.visibility_of_element_located(DeskLocators.EMAIL))
        email_input.send_keys(data.EMAIL_EXIST_USER)
        driver.find_element(*DeskLocators.PASSWORD).send_keys(data.PASSWORD_EXIST_USER)
        driver.find_element(*DeskLocators.LOGIN_BTN).click()

        avatar = WebDriverWait(driver, 20).until(expected_conditions.visibility_of_element_located(DeskLocators.USER_AVATAR))
        user_name = WebDriverWait(driver, 20).until(expected_conditions.visibility_of_element_located(DeskLocators.USER_NAME))
        
        assert avatar.is_displayed() is True
        assert 'User' in user_name.text
        assert 'https://qa-desk.education-services.ru' in driver.current_url #вообще-то не переходит на "главную", в урле остается указание на стр входа /signin
