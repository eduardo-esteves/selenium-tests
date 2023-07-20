import time

from selenium.webdriver.common.by import By
from pages.login_page import LoginPage

class TestCT01:
    def test_ct01_test_valid_login(self, setup_teardown):
        browser = setup_teardown

        login_page = LoginPage()
        login_page.make_login('standard_user', 'secret_sauce', browser)

        assert browser.find_element(By.CSS_SELECTOR, '.header_secondary_container > span.title').is_displayed()

        time.sleep(2)
