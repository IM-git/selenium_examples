from .BasePage import BasePage
from tools.MouseKeyboardActions import MouseKeyboardActions
from selenium.webdriver.common.by import By


class ButtonsPage(BasePage):

# CLICK BUTTON
    def click_double_click_button(self, browser, locator, element):
        value = self.base_element._find_element(
            browser, locator, element)
        return MouseKeyboardActions()._double_click(browser, value)

    def click_one_right_button(self, browser, locator, element):
        value = self.base_element._find_element(
            browser, locator, element)
        return MouseKeyboardActions()._right_click(browser, value)

    def click_button(self, browser, locator, element):
        value = self.base_element._find_element(
            browser, locator, element)
        return MouseKeyboardActions()._one_click(browser, value)
