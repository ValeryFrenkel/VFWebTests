import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--window-size=1920,1080")

@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()