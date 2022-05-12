class BaseElements:

    @staticmethod
    def find_element(browser, locator, element):
        return browser.find_element(locator, element)

    def click(self, browser, locator, element):
        self.find_element(browser, locator, element).click()

    def get_to_attribute(self, browser, locator, element, attribute):
        self.find_element(browser, locator, element).get_attribute(attribute)

    def get_text(self, browser, locator, element):
        return self.find_element(browser, locator, element).text
