import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.maximize_window()
browser.implicitly_wait(10)

browser.get('https://www.saucedemo.com')

# find elements
user_name = browser.find_element(By.CSS_SELECTOR, 'input[name="user-name"]')
user_pass = browser.find_element(By.CSS_SELECTOR, 'input[name="password"]')

user_name.send_keys('standard_user')
user_pass.send_keys('secret_sauce')

# Clico no botão para logar
browser.find_element(By.CSS_SELECTOR, 'input[name="login-button"]').click()

assert browser.find_element(By.CSS_SELECTOR, '.header_secondary_container > span.title').is_displayed()

# Detalhes do pedido
product = browser.find_element(By.XPATH, '//div[@class="inventory_item_name" and text()="Sauce Labs Backpack"]')
product.click()

# Adicionar o produto ao carrinho
browser.find_element(By.XPATH, '//button[contains(@class, "btn_inventory") and text()="Add to cart"]').click()

# E clico no link do carrinho
browser.find_element(By.ID, "shopping_cart_container").click()

time.sleep(5)

assert browser.find_element(By.XPATH, '//div[@class="inventory_item_name" and text()="Sauce Labs Backpack"]').is_displayed()

browser.quit()
