import time

import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_teardown")
class TestCT01:
    def test_ct01_test_valid_login(self, setup_teardown):
        browser = setup_teardown
        # find elements
        user_name = browser.find_element(By.CSS_SELECTOR, 'input[name="user-name"]')
        user_pass = browser.find_element(By.CSS_SELECTOR, 'input[name="password"]')

        user_name.send_keys('standard_user')
        user_pass.send_keys('secret_sauce')

        time.sleep(2)

        browser.find_element(By.CSS_SELECTOR, 'input[name="login-button"]').click()

        assert browser.find_element(By.CSS_SELECTOR, '.header_secondary_container > span.title').is_displayed()

        time.sleep(2)
