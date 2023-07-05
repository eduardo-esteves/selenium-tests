import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.get('https://demo.applitools.com')
browser.maximize_window()

user_name = browser.find_element(By.ID, 'username')
check_remember_me = browser.find_element(By.CSS_SELECTOR, '[type="checkbox"].form-check-input')

is_visible = user_name.is_displayed()

assert is_visible, 'Elemento não está visivel'
# Pode acontecer que o elemento não esteja habilitado para uso.
assert user_name.is_enabled(), 'Elemento não está habilitado para uso'
# O comportamento padrão é justamente não estar selecionado
assert not check_remember_me.is_selected(), 'Elemento está selecionado'

# Clico no botão para deixá-lo selecionado e fazer o teste inverso abaixo
check_remember_me.click()
# Agora espero que o elemento esteja selecionado
assert check_remember_me.is_selected(), 'Elemento não está selecionado'


browser.quit()
