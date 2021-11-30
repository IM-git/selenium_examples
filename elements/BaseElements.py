class BaseElements:

    # def __init__(self, browser):
    #     self.browser = browser

    @staticmethod
    def find_element_(browser, locator, element):
        return browser.find_element(locator, element)

    def click_(self, element):
        return element.click()

    def get_to_attribute(self, element, attribute):
        return element.get_attribute(attribute)

    def get_text_(self, element):
        return element.text

    def check_is_displayed(self, element):
        return element.is_displayed()

    def check_is_displayed_2_0(self, browser, locator, element):
        return BaseElements.find_element_(browser, locator, element).is_displayed()
