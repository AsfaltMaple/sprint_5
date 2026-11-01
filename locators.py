from selenium.webdriver.common.by import By

class DeskLocators:
    #кнопки
    REGISTRATION_BTN = By.XPATH, "//button[text()='Вход и регистрация']"
    ADD_ADV_BTN = By.XPATH, "//button[text()='Разместить объявление']"
    NO_ACCOUNT_BTN = By.XPATH, "//button[text()='Нет аккаунта']"
    CREATE_ACC_BTN = By.XPATH, "//button[text()='Создать аккаунт']"
    LOGOUT_BTN = By.XPATH, "//button[text()='Выйти']"
    LOGIN_BTN = By.XPATH, "//button[@type='submit' and text()='Войти']"
    CREATE_ADV_BTN = By.XPATH, "//button[text()='Разместить объявление']"
    PUBLISH_BTN = By.XPATH, "//button[@type ='submit' and text()='Опубликовать']"
    EDIT_ADV = By.CSS_SELECTOR, ".editButton"
    
    #инпуты
    EMAIL = By.XPATH, ".//input[@name='email']"
    PASSWORD = By.XPATH, "//input[@name='password']"
    SUBMIT_PASSWORD = By.XPATH, "//input[@name='submitPassword']"
    USER_AVATAR = By.XPATH, "//button[@class='circleSmall']"
    USER_NAME = By.XPATH, "//*[@class='profileText name']"
    ADV_NAME = By.XPATH, "//input[@placeholder='Название']"
    ADV_DESCRIPTION = By.XPATH, "//*[@placeholder='Описание товара']"
    ADV_PRICE = By.XPATH, "//*[@name='price']"
   
    #рамки полей
    EMAIL_FIELD_BORDER = By.XPATH, "//input[@name='email']/parent::div"
    PASSWORD_FIELD_BORDER = By.XPATH, "//input[@name='password']/parent::div"
    SUBMIT_PASS_FIELD_BORDER = By.XPATH, "//input[@name='submitPassword']/parent::div"
   
    #сообщения/заголовки
    ERROR_MSG = By.XPATH, "//span[contains(@*, 'input_span') and text()='Ошибка']"
    AUTHORIZATION_IS_NEEDED_MSG = By.XPATH, "//h1[text()='Чтобы разместить объявление, авторизуйтесь']" 
    NEW_ADV_MSG =By.XPATH, "//h1[text()='Новое объявление']"
    MY_ADS_HEADER = By.XPATH, "//h1[text()='Мои объявления']"
    MY_ADV_TITLES = By.XPATH, "//h2[@class='h2']"


    #радиокнопки (обе) выбора состояния товара
    ADV_CONDITIONS_RADIOBTN = By.XPATH, "//label[@class ='h2']"

    #допдауны выбора категории и города для объявления
    CATEGORY_DROPDOWN = By.XPATH, "(//button[contains(@class, 'dropDownMenu_arrowDown')])[1]"
    CATEGORIES = By.XPATH, "(//div[contains(@class, 'dropDownMenu_dropMenu')])[1]//button[contains(@class, 'dropDownMenu_btn')]"
    TOWN_DROPDOWN = By.XPATH, "(//button[contains(@class, 'dropDownMenu_arrowDown')])[2]"
    TOWNS = By.XPATH, "(//div[contains(@class, 'dropDownMenu_dropMenu')])[2]//button[contains(@class, 'dropDownMenu_btn')]"