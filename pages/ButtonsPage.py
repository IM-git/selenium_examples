from .BasePage import BasePage
from locators import Buttons
from src.enums import ButtonsError

from tools.MouseKeyboardActions import MouseKeyboardActions
from tools.allure_screenshot import taking_screenshot
from tools import Logger


class ButtonsPage(BasePage):

    def __init__(self, *args, **kwargs):
        super(ButtonsPage, self).__init__(*args, **kwargs)
        self.mouse_keyboard_actions = MouseKeyboardActions(self.browser)

    def check_is_displayed_double_click_button(self):
        self.check_is_displayed(*Buttons.BUTTON_DOUBLE_CLICK_ME)

    def checks_double_click_result_text(self):
        value = self.get_text(*Buttons.GET_DOUBLE_CLICK_RESULT_TEXT)
        assert value == 'You have done a double click',\
            (ButtonsError.WRONG_ANSWER_AFTER_DOUBLE_CLICK.value,
             taking_screenshot(self.browser))

    def checks_right_click_result_text(self):
        value = self.get_text(*Buttons.GET_RIGHT_CLICK_RESULT_TEXT)
        assert value == 'You have done a right click',\
            (ButtonsError.WRONG_ANSWER_AFTER_RIGHT_CLICK.value,
             taking_screenshot(self.browser))

    def checks_click_result_text(self):
        value = self.get_text(*Buttons.GET_CLICK_RESULT_TEXT)
        assert value == 'You have done a dynamic click',\
            (ButtonsError.WRONG_ANSWER_AFTER_RIGHT_CLICK.value,
             taking_screenshot(self.browser))

    def click_one_right_button(self):
        Logger.Logger().info(f"One click right button.")
        value = self.base_element.find_element(
            self.browser, *Buttons.BUTTON_RIGHT_CLICK)
        self.mouse_keyboard_actions.right_click(value)

    def click_button(self):
        """Name button is 'Click Me'."""
        Logger.Logger().info(f"Click button.")
        value = self.base_element.find_element(
            self.browser, *Buttons.BUTTON_CLICK)
        self.mouse_keyboard_actions.one_click(value)

    def double_click_by_button(self):
        Logger.Logger().info(f"Double click button.")
        value = self.base_element.find_element(
            self.browser, *Buttons.BUTTON_DOUBLE_CLICK_ME)
        self.mouse_keyboard_actions.double_click(value)

    def wait_while_loaded_buttons_page(self):
        self.wait_presence_of_element_located(Buttons.BUTTON_DOUBLE_CLICK_ME)
