import pytest
from selenium import webdriver


@pytest.fixture
def setup_teardown():
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.implicitly_wait(10)

    browser.get('https://www.saucedemo.com')

    # Run test
    yield browser

    # teardown
    browser.quit()
