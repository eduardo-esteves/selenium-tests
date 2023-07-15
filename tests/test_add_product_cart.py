import time

import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures('setup_teardown')
class TestCT02:
    def test_ct02_add_product_cart(self, setup_teardown):
        browser = setup_teardown
        # find elements
        user_name = browser.find_element(By.CSS_SELECTOR, 'input[name="user-name"]')
        user_pass = browser.find_element(By.CSS_SELECTOR, 'input[name="password"]')

        user_name.send_keys('standard_user')
        user_pass.send_keys('secret_sauce')

        time.sleep(2)

        # Clico no botão para logar
        browser.find_element(By.CSS_SELECTOR, 'input[name="login-button"]').click()

        assert browser.find_element(By.CSS_SELECTOR, '.header_secondary_container > span.title').is_displayed()

        time.sleep(2)

        # Detalhes do pedido
        product = browser.find_element(By.XPATH, '//div[@class="inventory_item_name" and text()="Sauce Labs Backpack"]')
        product.click()

        time.sleep(2)

        # Adicionar o produto ao carrinho
        browser.find_element(By.XPATH, '//button[contains(@class, "btn_inventory") and text()="Add to cart"]').click()

        time.sleep(2)

        # E clico no link do carrinho
        browser.find_element(By.ID, "shopping_cart_container").click()

        time.sleep(2)

        assert browser.find_element(By.XPATH, '//div[@class="inventory_item_name" and text()="Sauce Labs Backpack"]').is_displayed()

