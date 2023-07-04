import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.get('https://www.saucedemo.com')
browser.maximize_window()

# find elements
user_name = browser.find_element(By.ID, 'user-name')
password = browser.find_element(By.ID, 'password')

# fill fields
user_name.send_keys('standard_user')
password.send_keys('secret_sauce')

time.sleep(5)
browser.quit()
