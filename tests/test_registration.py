import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import DeskLocators
from helpers import registration_data
import data


class TestRegistration:

    def test_registration_new_user(self,driver):
      
        email, password = registration_data()
        reg = WebDriverWait(driver, 20).until(expected_conditions.visibility_of_element_located(DeskLocators.REGISTRATION_BTN))

        assert reg.is_displayed() is True
        assert reg.is_enabled() is True

    
        reg.click()
        no_account = WebDriverWait(driver, 20).until(expected_conditions.visibility_of_element_located(DeskLocators.NO_ACCOUNT_BTN))
        assert no_account.is_displayed() is True
        assert no_account.is_enabled() is True

        no_account.click()
        email_input = WebDriverWait(driver,20).until(expected_conditions.visibility_of_element_located(DeskLocators.EMAIL))
        email_input.send_keys(email)
        driver.find_element(*DeskLocators.PASSWORD).send_keys(password)
        driver.find_element(*DeskLocators.SUBMIT_PASSWORD).send_keys(password)
        driver.find_element(*DeskLocators.CREATE_ACC_BTN).click()

        avatar = WebDriverWait(driver, 20).until(expected_conditions.visibility_of_element_located(DeskLocators.USER_AVATAR))
        user_name = WebDriverWait(driver, 20).until(expected_conditions.visibility_of_element_located(DeskLocators.USER_NAME))

        assert avatar.is_displayed() is True
        assert 'User' in user_name.text


    def test_registration_existed_user(self,driver):
        reg = WebDriverWait(driver, 20).until(expected_conditions.visibility_of_element_located(DeskLocators.REGISTRATION_BTN))

        assert reg.is_displayed() is True
        assert reg.is_enabled() is True

        reg.click()
        no_account = WebDriverWait(driver, 20).until(expected_conditions.visibility_of_element_located(DeskLocators.NO_ACCOUNT_BTN))
        
        assert no_account.is_displayed() is True
        assert no_account.is_enabled() is True
        
        no_account.click()
        email_input = WebDriverWait(driver,20).until(expected_conditions.visibility_of_element_located(DeskLocators.EMAIL))
        email_input.send_keys(data.EMAIL_EXIST_USER)
        driver.find_element(*DeskLocators.PASSWORD).send_keys(data.PASSWORD_EXIST_USER)
        driver.find_element(*DeskLocators.SUBMIT_PASSWORD).send_keys(data.PASSWORD_EXIST_USER)
        driver.find_element(*DeskLocators.CREATE_ACC_BTN).click()

        msg = WebDriverWait(driver, 20).until(expected_conditions.visibility_of_element_located(DeskLocators.ERROR_MSG))

        assert msg.is_displayed()