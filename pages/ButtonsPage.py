from .BasePage import BasePage
from tools.MouseKeyboardActions import MouseKeyboardActions
from tools import Logger
from selenium.webdriver.common.by import By


class ButtonsPage(BasePage):

# CLICK BUTTON
    def click_double_click_button(self, browser, locator, element):
        Logger.Logger().info(f"Double click button(Element: {element}).")
        value = self.base_element._find_element(
            browser, locator, element)
        return MouseKeyboardActions()._double_click(browser, value)

    def click_one_right_button(self, browser, locator, element):
        Logger.Logger().info(f"One click right button(Element: {element}).")
        value = self.base_element._find_element(
            browser, locator, element)
        return MouseKeyboardActions()._right_click(browser, value)

    def click_button(self, browser, locator, element):
        Logger.Logger().info(f"Click button(Element: {element}).")
        value = self.base_element._find_element(
            browser, locator, element)
        return MouseKeyboardActions()._one_click(browser, value)
