class BaseElements:

    @staticmethod
    def _find_element(browser, locator, element):
        return browser.find_element(locator, element)

    def _click(self, element):
        return element.click()

    def _get_to_attribute(self, element, attribute):
        return element.get_attribute(attribute)

    def _get_text(self, element):
        return element.text
