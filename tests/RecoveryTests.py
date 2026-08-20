import allure

from core.BaseTest import browser
from pages.BasePage import BasePage
from pages.LoginPage import LoginPageHelper
from pages.RecoveryPage import RecoveryPageHelper

BASE_URL = 'https://sn.rv-school.ru/'
LOGIN_TEXT = "email"
PASSWORD_TEXT = "1"
EMPTY_CREDENTIALS_ERROR = 'Пользователь с таким телефоном, почтой или логином не найден. Проверьте данные и попробуйте снова.'

@allure.suite("Проверка восстановления пользователя")
@allure.title("Проверка перехода к восстановлению после нескольких неудачных попыток авторизации")
def test_go_to_recovery_after_many_fails(browser):
    BasePage(browser).get_url(BASE_URL)
    LoginPage = LoginPageHelper(browser)
    LoginPage.enter_login(LOGIN_TEXT)
    LoginPage.enter_password(PASSWORD_TEXT)
    for _ in range(2):
        LoginPage.click_login()
        assert LoginPage.get_error_text() == EMPTY_CREDENTIALS_ERROR
    LoginPage.click_login()
    LoginPage.click_recovery_button()
    RecoveryPageHelper(browser)

