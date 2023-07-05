from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

browser = webdriver.Chrome()
browser.maximize_window()

browser.get('https://chercher.tech/practice/explicit-wait-sample-selenium-webdriver')

wait_driver = WebDriverWait(browser, 12)

# browser.find_element(By.ID, 'alert').click()
# wait_driver.until(EC.alert_is_present())

button_change_text = browser.find_element(By.CSS_SELECTOR, 'button#populate-text')
button_change_text.click()

print(button_change_text.get_attribute('outerHTML'))

wait_driver.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'h2#h2'), 'Selenium Webdriver'))
h2_text = browser.find_element(By.CSS_SELECTOR, 'h2#h2').text

assert h2_text == 'Selenium Webdriver'

browser.quit()
