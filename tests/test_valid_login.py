from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.get('https://www.saucedemo.com')
browser.maximize_window()
browser.implicitly_wait(10)

# find elements
user_name = browser.find_element(By.CSS_SELECTOR, 'input[name="user-name"]')
user_pass = browser.find_element(By.CSS_SELECTOR, 'input[name="password"]')

user_name.send_keys('standard_user')
user_pass.send_keys('secret_sauce')

browser.find_element(By.CSS_SELECTOR, 'input[name="login-button"]').click()

assert browser.find_element(By.CSS_SELECTOR, '.header_secondary_container > span.title').is_displayed()

browser.quit()
