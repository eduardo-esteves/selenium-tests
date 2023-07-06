import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

browser = webdriver.Chrome()
browser.maximize_window()

browser.get('https://chercher.tech/practice/practice-dropdowns-selenium-webdriver')

wait_driver = WebDriverWait(browser, 12)

dropdown_products = Select(browser.find_element(By.CSS_SELECTOR, 'select#first'))
dropdown_products.select_by_visible_text('Google')
time.sleep(3)

dropdown_products.select_by_index(2)
time.sleep(3)

# Selecionando multiplas opções
dropdown_foods = Select(browser.find_element(By.CSS_SELECTOR, 'select#second'))

dropdown_foods.select_by_value('pizza')
time.sleep(3)

dropdown_foods.select_by_value('burger')
time.sleep(3)


