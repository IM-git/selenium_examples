class BaseElements:

    def __init__(self, browser):
        self.browser = browser

    def find_element(self):
        return self.browser.find_element()

    def click(self, element):
        return element.click()
