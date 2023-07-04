from selenium import webdriver

browser = webdriver.Chrome()

browser.get('https://www.saucedemo.com')

# print title of page
print(f'O titulo da página é: {browser.title}')

# print the current URL
print(f'A URL da página atual é: {browser.current_url}')

# print the page source
print(f'O código fonte da pagina é: {browser.page_source}')
