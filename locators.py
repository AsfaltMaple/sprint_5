#from selenium import webdriver
from selenium.webdriver.common.by import By

class DeskLocators:
    REGISTRATION_BTN = By.XPATH, "//button[text()='Вход и регистрация']"
    ADD_ADV_BTN = By.XPATH, "//button[text()='Разместить объявление']"
    NO_ACCOUNT_BTN = By.XPATH, "//button[text()='Нет аккаунта']"
    EMAIL = By.XPATH, ".//input[@name='email']"
    PASSWORD = By.XPATH, "//input[@name='password']"
    SUBMIT_PASSWORD = By.XPATH, "//input[@name='submitPassword']"
    CREATE_ACC_BTN = By.XPATH, "//button[text()='Создать аккаунт']"
    LOGOUT_BTN = By.XPATH, "//button[text()='Выйти']"
    USER_AVATAR = By.XPATH, "//button[@class='circleSmall']"
    USER_NAME = By.XPATH, "//*[@class='profileText name']"
    ERROR_MSG = By.XPATH, "//span[contains(@*, 'input_span') and text()='Ошибка']"
    EMAIL_FIELD_BORDER = By.XPATH, "//input[@name='email']/parent::div"
    PASSWORD_FIELD_BORDER = By.XPATH, "//input[@name='password']/parent::div"
    SUBMIT_PASS_FIELD_BORDER = By.XPATH, "//input[@name='submitPassword']/parent::div"
    LOGIN_BTN = By.XPATH, "//button[@type='submit' and text()='Войти']"
    CREATE_ADV_BTN = By.XPATH, "//button[text()='Разместить объявление']"
    AUTHORIZATION_IS_NEEDED_MSG = By.XPATH, "//h1[text()='Чтобы разместить объявление, авторизуйтесь']"               