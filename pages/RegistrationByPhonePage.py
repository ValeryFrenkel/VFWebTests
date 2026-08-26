import allure
from pages.BasePage import BasePage
from selenium.webdriver.common.by import By
import random
import re

#random_country_item = random.randint(0,40)

class RegistrationByPhonePageLocators:
    REGISTER_PHONE_BUTTON = (By.XPATH, "//button[@data-test-id='register-phone-toggle']")
    COUNTRY_LIST = (By.XPATH, "//select[@data-test-id='phone-country-select']")
    #COUNTRY_ITEM = (By.XPATH, f"//option[@data-test-id='phone-country-option-{random_country_item}']")
    COUNTRY_ITEM = (By.XPATH, "//select[@data-test-id='phone-country-select']/option")
    PHONE_NUMBER_FIELD = (By.XPATH, "//input[@data-test-id='phone-number-input']")
    SEND_CODE_BUTTON = (By.XPATH, "//button[@data-test-id='phone-send-code-btn']")
    BACK_TO_EMAIL_REGISTRATION_BUTTON = (By.XPATH, "//button[@data-test-id='phone-cancel-btn']")

class RegistrationByPhonePageHelper(BasePage):
    def __init__(self,driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        with allure.step("Проверяем корректность загрузки страницы"):
            self.attach_screenshot()
        self.find_element(RegistrationByPhonePageLocators.COUNTRY_LIST)
        self.find_element(RegistrationByPhonePageLocators.PHONE_NUMBER_FIELD)
        self.find_element(RegistrationByPhonePageLocators.SEND_CODE_BUTTON)
        self.find_element(RegistrationByPhonePageLocators.BACK_TO_EMAIL_REGISTRATION_BUTTON)

    @allure.step('Выбираем случайную страну в списке')
    def select_random_country(self):
        self.find_element(RegistrationByPhonePageLocators.COUNTRY_LIST).click()
        country_items = self.find_elements(RegistrationByPhonePageLocators.COUNTRY_ITEM)
        random_number = random.randint(0, len(country_items))
        country_item_text = country_items[random_number].get_attribute('text')
        country_item_value = country_items[random_number].get_attribute('value')
        phone_code = re.search(r"\+\d+", country_item_text).group()
        country_items[random_number].click()
        self.attach_screenshot()
        return phone_code, country_item_value



