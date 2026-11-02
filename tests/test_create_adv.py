from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import DeskLocators
from helpers import adv_info
import data
import random

class TestAdvCreate:

    def test_create_adv_by_authorized_user(self, driver):
        adv_name, adv_description, adv_price = adv_info()

        login_btn = WebDriverWait(driver, 20).until(expected_conditions.visibility_of_element_located(DeskLocators.REGISTRATION_BTN))
        login_btn.click()
        
        email_input = WebDriverWait(driver,20).until(expected_conditions.visibility_of_element_located(DeskLocators.EMAIL))
        email_input.send_keys(data.EMAIL_EXIST_USER)
        driver.find_element(*DeskLocators.PASSWORD).send_keys(data.PASSWORD_EXIST_USER)
        driver.find_element(*DeskLocators.LOGIN_BTN).click()

        WebDriverWait(driver,20).until(expected_conditions.visibility_of_element_located(DeskLocators.USER_NAME))

        driver.find_element(*DeskLocators.CREATE_ADV_BTN).click()
        
        WebDriverWait(driver, 20).until(expected_conditions.visibility_of_element_located(DeskLocators.NEW_ADV_MSG))
    
        driver.find_element(*DeskLocators.ADV_NAME).send_keys(adv_name)
        driver.find_element(*DeskLocators.ADV_DESCRIPTION).send_keys(adv_description)
        driver.find_element(*DeskLocators.ADV_PRICE).send_keys(adv_price)
       
        random.choice(driver.find_elements(*DeskLocators.ADV_CONDITIONS_RADIOBTN)).click()
        driver.find_element(*DeskLocators.CATEGORY_DROPDOWN).click()
        random.choice(driver.find_elements(*DeskLocators.CATEGORIES)).click()
        driver.find_element(*DeskLocators.TOWN_DROPDOWN).click()
        random.choice(driver.find_elements(*DeskLocators.TOWNS)).click()

        WebDriverWait(driver, 20).until(expected_conditions.visibility_of_element_located(DeskLocators.PUBLISH_BTN))
       
    
        driver.find_element(*DeskLocators.PUBLISH_BTN).click()
        avatar = WebDriverWait(driver, 20).until(expected_conditions.visibility_of_element_located(DeskLocators.USER_AVATAR))
        avatar.click()

        WebDriverWait(driver,20).until(expected_conditions.visibility_of_element_located(DeskLocators.EDIT_ADV)).is_displayed()
       
        driver.find_element(*DeskLocators.NEXT_PAGE).click()
        adv_titles = driver.find_elements(*DeskLocators.MY_ADV_TITLES)

    
        assert adv_name in [title.text for title in adv_titles]



    def test_create_adv_by_unauthorized_user(self, driver):
        WebDriverWait(driver, 20).until(expected_conditions.visibility_of_element_located(DeskLocators.CREATE_ADV_BTN))
        driver.find_element(*DeskLocators.CREATE_ADV_BTN).click()
        auth_is_needed_msg = WebDriverWait(driver, 20).until(expected_conditions.visibility_of_element_located(DeskLocators.AUTHORIZATION_IS_NEEDED_MSG))

        assert auth_is_needed_msg.is_displayed()