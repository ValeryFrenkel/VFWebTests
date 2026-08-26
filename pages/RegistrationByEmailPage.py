import allure
from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class RegistrationByEmailPageLocators:
    NAME_FIELD = (By.XPATH, "//input[@data-test-id='display-name']")
    USERNAME_FIELD = (By.XPATH, "//input[@data-test-id='username']")
    EMAIL_FIELD = (By.XPATH, "//input[@data-test-id='email']")
    PHONE_FIELD = (By.XPATH, "//input[@data-test-id='phone']")
    PASSWORD_FIELD = (By.XPATH, "//input[@data-test-id='register-password']")
    CONFIRM_PASSWORD_FIELD = (By.XPATH, "//input[@data-test-id='confirm-password']")
    CREATE_ACCOUNT_BUTTON = (By.XPATH, "//button[@data-test-id='register-submit-btn']")
    REGISTER_PHONE_BUTTON = (By.XPATH, "//button[@data-test-id='register-phone-toggle']")

class RegistrationByEmailPageHelper(BasePage):
    def __init__(self,driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        with allure.step("Проверяем корректность загрузки страницы"):
            self.attach_screenshot()
        self.find_element(RegistrationByEmailPageLocators.NAME_FIELD)
        self.find_element(RegistrationByEmailPageLocators.USERNAME_FIELD)
        self.find_element(RegistrationByEmailPageLocators.EMAIL_FIELD)
        self.find_element(RegistrationByEmailPageLocators.PHONE_FIELD)
        self.find_element(RegistrationByEmailPageLocators.PASSWORD_FIELD)
        self.find_element(RegistrationByEmailPageLocators.CONFIRM_PASSWORD_FIELD)
        self.find_element(RegistrationByEmailPageLocators.CREATE_ACCOUNT_BUTTON)
        self.find_element(RegistrationByEmailPageLocators.REGISTER_PHONE_BUTTON)


    @allure.step('Нажимаем на кнопку "Регистрация по телефону"')
    def click_registration_by_phone_button(
            self
    ):
        self.find_element(RegistrationByEmailPageLocators.REGISTER_PHONE_BUTTON).click()
        self.attach_screenshot()