import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.get('https://demo.applitools.com')
browser.maximize_window()

user_name = browser.find_element(By.ID, 'username')
title = browser.find_element(By.CSS_SELECTOR, 'h4.auth-header')

user_name_placeholder = user_name.get_attribute('placeholder')

print(title.text)
print(user_name_placeholder)

assert title.text == 'Login Form', 'O texto do titulo é diferente do elemento selecionado'
assert user_name_placeholder == 'Enter your username'

browser.quit()
