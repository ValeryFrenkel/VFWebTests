from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import allure


class BasePage:
    def __init__(
            self,
            driver
    ):
        self.driver = driver

    def find_element(
            self,
            locator,
            time=5
    ):
        return WebDriverWait(self.driver, time).until(
            expected_conditions.visibility_of_element_located(locator), message=f"Не удалось найти элемент {locator}"
        )

    def find_elements(
            self,
            locator,
            time=5
    ):
        return WebDriverWait(self.driver, time).until(
            expected_conditions.visibility_of_all_elements_located(locator), message=f"Не удалось найти элементы {locator}"
        )

    @allure.step("Открываем главную страницу")
    def get_url(
            self,
            url
    ):
        return self.driver.get(url)

    def attach_screenshot(
            self
    ):
        allure.attach(self.driver.get_screenshot_as_png(), 'скриншот', allure.attachment_type.PNG)
