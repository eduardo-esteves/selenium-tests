from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.maximize_window()
browser.implicitly_wait(12)

browser.get('https://chercher.tech/practice/implicit-wait-example')

checkbox = browser.find_element(By.CSS_SELECTOR, 'input[type="checkbox"]')

assert checkbox.is_displayed()

browser.quit()
