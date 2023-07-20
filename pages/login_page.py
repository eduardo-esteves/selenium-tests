import time

from selenium.webdriver.common.by import By


class LoginPage:

    def make_login(self, user_name, user_pass, browser):
        # find elements
        browser.find_element(By.CSS_SELECTOR, 'input[name="user-name"]').send_keys(user_name)
        browser.find_element(By.CSS_SELECTOR, 'input[name="password"]').send_keys(user_pass)

        time.sleep(2)

        browser.find_element(By.CSS_SELECTOR, 'input[name="login-button"]').click()
