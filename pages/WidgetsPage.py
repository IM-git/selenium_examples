from pages import BasePage
from src.enums import WidgetsPageError
from locators import Widgets

from tools.MouseKeyboardActions import MouseKeyboardActions
from tools.RandomTools import RandomTools
from tools import Logger
from tools.allure_screenshot import taking_screenshot

VALUE_OF_1_TO_4 = 4
CORRECTING_VALUE = 3


class WidgetsPage(BasePage):
    """
    Widget page consist to slider and progress bar pages.
    """
    def __init__(self, *args, **kwargs):
        super(WidgetsPage, self).__init__(*args, **kwargs)
        self.mouse_keyboard_actions = MouseKeyboardActions(self.browser)


class SliderPage(WidgetsPage):
    """
    Methods for slider page.
    """
    def check_is_displayed_slider(self):
        self.check_is_displayed(*Widgets.INPUT_SLIDER)

    def move_to_slider(self):
        Logger.Logger().info(f"Move to slider.")
        value = self.base_element.find_element(
            self.browser, *Widgets.INPUT_SLIDER)
        self.mouse_keyboard_actions.move_to_element(value)

    def do_random_steps(self, locator, element):
        Logger.Logger().info(f"Making random steps(Element: {element}).")
        value = self.base_element.find_element(self.browser, locator, element)
        return RandomTools.Steps.do_random_steps(value)

    def checking_slider_value(self):
        Logger.Logger().info(f"Checking slider value.")
        value = int(self.base_element.get_to_attribute(
            self.browser, *Widgets.VALUE_SLIDER, attribute="value"))-25
        return abs(value)

    def checking_slider(self):
        steps = self.do_random_steps(*Widgets.INPUT_SLIDER)
        value = self.checking_slider_value()
        assert steps == value, (
            f'{WidgetsPageError.WRONG_DID_RANDOM_STEPS.value}.'
            f'Expected: {steps}, got: {value}',
            taking_screenshot(self.browser))


class ProgressBarPage(WidgetsPage):
    """
    Methods for progress bar page.
    """
    def click_button(self):
        Logger.Logger().info(f"Click button.")
        value = self.base_element.find_element(
            self.browser, *Widgets.PROGRESS_BAR_START_STOP_BUTTON)
        self.mouse_keyboard_actions.one_click(value)

    def check_is_displayed_reset_button(self):
        self.check_is_displayed(*Widgets.PROGRESS_BAR_START_STOP_BUTTON)

    def checks_value_progress_bar(self):
        """This isn't fully correct test method,
        because stopping the progress bar works right.
        Just couldn't come up more effective test method."""
        self.click_button()
        wait_while_progress_bar_became = self.wait_while_progress_bar_became(
            Widgets.VALUE_PERCENT)
        self.click_button()
        get_value_progress_bar = self.get_text(*Widgets.VALUE_PROGRESS_BAR)
        assert wait_while_progress_bar_became in get_value_progress_bar,\
            (f'{WidgetsPageError.WRONG_ENTERED_VALUE_IN_PAGE.value}.'
             f'Expected: {wait_while_progress_bar_became},'
             f'got: {get_value_progress_bar}',
             taking_screenshot(self.browser))

    def wait_while_progress_bar_became(self, value_percent):
        """Method has no way to get the correct value
        of 1 to 4 percent."""
        Logger.Logger().info(
            f"Wait while progress bar became: {value_percent}.")
        if value_percent >= VALUE_OF_1_TO_4:
            value = value_percent - CORRECTING_VALUE
            return self.correcting_value_percent(value_percent, value)
        else:
            return self.correcting_value_percent(value_percent, value_percent)

    def correcting_value_percent(self, value_percent, value):
        Logger.Logger().info(
            f"Correcting value percent(Value: {value_percent}).")
        if str(value) in self.get_text(*Widgets.VALUE_PROGRESS_BAR):
            return str(value_percent)
        else:
            return self.correcting_value_percent(value_percent, value)
