from pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class LoginPageLocators:
    LOGIN_TAB = (By.XPATH, "//a[@data-l='t,login_tab']")
    QR_TAB = (By.XPATH, "//a[@data-l='t,qr_tab']")
    LOGIN_FIELD = (By.XPATH, "//input[@data-test-id='login-input']")
    PASSWORD_FIELD = (By.XPATH, "//input[@data-test-id='password-input']")
    LOGIN_BUTTON = (By.XPATH, "//button[@data-test-id='enter-action']")
    QR_LOGIN_BUTTON = (By.XPATH, "//button[@label='Войти по QR-коду']")
    FORGOT_PASSWORD_BUTTON = (By.XPATH, "//button[@data-test-id='forgot-password-link']")
    REGISTRATION_BUTTON = (By.XPATH, "//button[@data-test-id='registration-action']")
    VK_BUTTON = (By.XPATH, "//a[@data-l='t,vkc']")
    MAIL_BUTTON = (By.XPATH, "//a[@data-l='t,mailru']")
    GOOGLE_BUTTON = (By.XPATH, "//a[@data-l='t,google']")
    YANDEX_BUTTON = (By.XPATH, "//a[@data-l='t,yandex']")
    APPLE_BUTTON = (By.XPATH, "//a[@data-l='t,apple']")

class LoginPageHelper(BasePage):
    pass