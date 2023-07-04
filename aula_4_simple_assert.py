import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.get('https://www.saucedemo.com')
browser.maximize_window()

# find elements
auth_fields = browser.find_elements(By.XPATH, '//*[@class="input_error form_input"]')

assert len(auth_fields) == 2, 'Número de elementos encontrados é diferente do esperado'

time.sleep(5)
browser.quit()
