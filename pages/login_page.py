import time

from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self):
        self.user_name = (By.CSS_SELECTOR, 'input[name="user-name"]')
        self.user_passwd = (By.CSS_SELECTOR, 'input[name="password"]')
        self.login_button = (By.CSS_SELECTOR, 'input[name="login-button"]')

    def make_login(self, user_name, user_pass, browser):
        # find elements
        browser.find_element(*self.user_name).send_keys(user_name)
        browser.find_element(*self.user_passwd).send_keys(user_pass)

        time.sleep(2)

        browser.find_element(*self.login_button).click()
