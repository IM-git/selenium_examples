class BaseElements:

    def __init__(self, browser):
        self.browser = browser

    def find_element_(self, locator, element):
        return self.browser.find_element(locator, element)

    def click_(self, element):
        return element.click()

    def get_to_attribute(self, element, attribute):
        return element.get_attribute(attribute)

    def get_text_(self, element):
        return element.text

    def check_is_displayed(self, element):
        return element.is_displayed()
