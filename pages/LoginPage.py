from pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class LoginPageLocators:
    LOGIN_TAB = (By.XPATH, "//div[@data-test-id='tab-login']")
    QR_TAB = (By.XPATH, "//div[@data-test-id='tab-qr']")
    LOGIN_FIELD = (By.XPATH, "//input[@data-test-id='login-phone-email']")
    PASSWORD_FIELD = (By.XPATH, "//input[@data-test-id='login-password']")
    LOGIN_BUTTON = (By.XPATH, "//button[@data-test-id='login-submit-btn']")
    FORGOT_PASSWORD_BUTTON = (By.XPATH, "//a[@data-test-id='forgot-password-link']")
    REGISTRATION_BUTTON = (By.XPATH, "//button[@data-test-id='hero-register-btn']")
    ERROR_TEXT = (By.XPATH, "//div[@data-test-id='login-error']")

class LoginPageHelper(BasePage):
    def __init__(self,driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        self.find_element(LoginPageLocators.LOGIN_TAB)
        self.find_element(LoginPageLocators.QR_TAB)
        self.find_element(LoginPageLocators.LOGIN_FIELD)
        self.find_element(LoginPageLocators.PASSWORD_FIELD)
        self.find_element(LoginPageLocators.LOGIN_BUTTON)
        self.find_element(LoginPageLocators.FORGOT_PASSWORD_BUTTON)
        self.find_element(LoginPageLocators.REGISTRATION_BUTTON)

    def click_login(self):
        self.find_element(LoginPageLocators.LOGIN_BUTTON).click()

    def enter_login(self):
        self.find_element(LoginPageLocators.LOGIN_FIELD).send_keys("admin@gmail.com")

    def get_error_text(self):
        return self.find_element(LoginPageLocators.ERROR_TEXT).text