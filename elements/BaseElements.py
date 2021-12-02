class BaseElements:

    @staticmethod
    def find_element_(browser, locator, element):
        return browser.find_element(locator, element)

    def click_(self, element):
        return element.click()

    def get_to_attribute(self, element, attribute):
        return element.get_attribute(attribute)

    def get_text_(self, element):
        return element.text
