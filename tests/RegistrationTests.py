import allure
from core.BaseTest import browser
from pages.BasePage import BasePage
from pages.LoginPage import LoginPageHelper
from pages.RegistrationByPhonePage import RegistrationByPhonePageHelper
from pages.RegistrationByEmailPage import RegistrationByEmailPageHelper

BASE_URL = 'https://sn.rv-school.ru/'


@allure.suite("Проверка регистрации через телефон")
@allure.title("Проверка выбора случайной страны при регистрации")
def test_registration_random_country(
        browser
):
    BasePage(browser).get_url(BASE_URL)
    LoginPage = LoginPageHelper(browser)
    LoginPage.click_registration_button()
    RegistrationByEmailPagee = RegistrationByEmailPageHelper(browser)
    RegistrationByEmailPagee.click_registration_by_phone_button()
    RegistrationByPhonePage = RegistrationByPhonePageHelper(browser)
    phone_code, country_field_value = (
        RegistrationByPhonePage.select_random_country()
    )
    assert phone_code == country_field_value
