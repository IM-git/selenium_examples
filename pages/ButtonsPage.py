from .BasePage import BasePage
from tools.MouseKeyboardActions import MouseKeyboardActions
from selenium.webdriver.common.by import By


class ButtonsPage(BasePage):

# CLICK BUTTON
    def click_double_click_button(self, locator, element):
        value = self.base_element.find_element_(
            self.browser, locator, element)
        return MouseKeyboardActions(self.browser).double_click(value)

    def click_one_right_button(self, locator, element):
        value = self.base_element.find_element_(
            self.browser, locator, element)
        return MouseKeyboardActions(self.browser).right_click(value)

    def click_button(self, locator, element):
        value = self.base_element.find_element_(
            self.browser, locator, element)
        return MouseKeyboardActions(self.browser).one_click(value)

