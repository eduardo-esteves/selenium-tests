
class BasePage:

    def __init__(self, browser):
        self.browser = browser

    def find_elemento(self, locator):
        return self.browser.find_element(*locator)

    def find_elementos(self, locator):
        return self.browser.find_elements(*locator)

    def writer(self, locator, text):
        self.find_elemento(locator).send_keys(text)

    def click(self, locator):
        self.find_elemento(locator).click()
