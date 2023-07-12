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

time.sleep(2)

# Clico no botão para logar
browser.find_element(By.CSS_SELECTOR, 'input[name="login-button"]').click()

time.sleep(2)

assert browser.find_element(By.CSS_SELECTOR, '.header_secondary_container > span.title').is_displayed()

# Detalhes do pedido
product = browser.find_element(By.XPATH, '//div[@class="inventory_item_name" and text()="Sauce Labs Backpack"]')
product.click()

time.sleep(2)

# Adicionar o produto ao carrinho
browser.find_element(By.XPATH, '//button[contains(@class, "btn_inventory") and text()="Add to cart"]').click()

time.sleep(3)

# E clico no link do carrinho
browser.find_element(By.ID, "shopping_cart_container").click()

assert browser.find_element(By.XPATH, '//div[@class="inventory_item_name" and text()="Sauce Labs Backpack"]').is_displayed()

# clicar no botão para finalizar a compra
browser.find_element(By.ID, 'checkout').click()

time.sleep(2)

# Preencher o formulário com os dados pessoais iniciando com o nome
browser.find_element(By.CSS_SELECTOR, 'input[name="firstName"]').send_keys('Eduardo')
# Preencher sobrenome
browser.find_element(By.CSS_SELECTOR, 'input[name="lastName"]').send_keys('Esteves')
# Preencher o CEP
browser.find_element(By.CSS_SELECTOR, 'input[name="postalCode"]').send_keys('0345140')

time.sleep(2)

# Enviar os dados pessoais para carregar o resumo e confirmação da compra
browser.find_element(By.ID, 'continue').click()

time.sleep(2)

# Clicar no botão para finalizar a compra
browser.find_element(By.ID, 'finish').click()

time.sleep(3)

browser.quit()
