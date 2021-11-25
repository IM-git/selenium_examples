from .BasePage import BasePage
from tools.MouseKeyboardActions import MouseKeyboardActions
from selenium.webdriver.common.by import By

LINK = 'https://demoqa.com/buttons'
BUTTON_DOUBLE_CLICK_ME = '//button[@id="doubleClickBtn"]'
GET_DOUBLE_CLICK_RESULT_TEXT = '//p[@id="doubleClickMessage"]'
BUTTON_RIGHT_CLICK = '//button[@id="rightClickBtn"]'
GET_RIGHT_CLICK_RESULT_TEXT = '//p[@id="rightClickMessage"]'
BUTTON_CLICK = '//button[text()="Click Me"]'
GET_CLICK_RESULT_TEXT = '//p[@id="dynamicClickMessage"]'


class ButtonsPage(BasePage):

    def open_buttons_page(self):
        return self.open_page(LINK)

    def wait_while_loaded_buttons_page(self):
        self.wait_presence_of_element_located(
            (By.XPATH, BUTTON_DOUBLE_CLICK_ME))

# CHECK IS DISPLAYED
    def check_is_displayed_double_click_button(self):
        element = self.base_element.find_element_(
            self.browser, By.XPATH, BUTTON_DOUBLE_CLICK_ME)
        return self.base_element.check_is_displayed(element)

# CLICK BUTTON
    def click_double_click_button(self):
        value = self.base_element.find_element_(
            self.browser, By.XPATH, BUTTON_DOUBLE_CLICK_ME)
        return MouseKeyboardActions(self.browser).double_click(value)

    def click_one_right_button(self):
        value = self.base_element.find_element_(
            self.browser, By.XPATH, BUTTON_RIGHT_CLICK)
        return MouseKeyboardActions(self.browser).right_click(value)

    def click_button(self):
        value = self.base_element.find_element_(
            self.browser, By.XPATH, BUTTON_CLICK)
        return MouseKeyboardActions(self.browser).one_click(value)

# GET TEXT
    def get_double_click_result_text(self):
        return self.get_text(By.XPATH, GET_DOUBLE_CLICK_RESULT_TEXT)

    def get_right_click_result_text(self):
        return self.get_text(By.XPATH, GET_RIGHT_CLICK_RESULT_TEXT)

    def get_click_result_text(self):
        return self.get_text(By.XPATH, GET_CLICK_RESULT_TEXT)
