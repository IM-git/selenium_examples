from .BasePage import BasePage
from tools.MouseKeyboardActions import MouseKeyboardActions
from selenium.webdriver.common.by import By


class ButtonsPage(BasePage):

# CHECK IS DISPLAYED
    def check_is_displayed_double_click_button(self, browser, locator, element):
        return self.base_element.check_is_displayed_2_0(browser, locator, element)

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

