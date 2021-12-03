from pages import BasePage
from tools.MouseKeyboardActions import MouseKeyboardActions
from selenium.webdriver.common.by import By
from tools.RandomTools import RandomTools


class WidgetsPage:

    def __init__(self):
        pass

    # SLIDER PAGE
    class Slider(BasePage):

        def move_to_slider(self, browser, locator, element):
            value = self.base_element.find_element_(
                browser, locator, element)
            return MouseKeyboardActions(browser).\
                move_to_element(value)

        def making_random_steps(self, browser, locator, element):
            value = self.base_element.find_element_(
                browser, locator, element)
            return RandomTools.Steps.do_random_steps(value)

        def checking_slider_value(self, browser, locator, element):
            elements = self.base_element.find_element_(
                browser, locator, element)
            value = int(self.base_element.get_to_attribute(
                element=elements, attribute="value"))-25
            return abs(value)

    # PROGRESS BAR PAGE
    class ProgressBar(BasePage):

        def click_button(self, browser, locator, element):
            value = self.base_element.find_element_(browser, locator, element)
            return MouseKeyboardActions(browser).one_click(value)

        def get_value_progress_bar(self, browser, locator, element):
            return self.get_text(browser, locator, element)

        # My function has no way to get the correct value of 1 to 4 percent.
        def wait_while_progress_bar_became(
                self, browser, value_percent, locator, element):
            value_of_1_to_4 = 4
            correcting_value = 2
            if value_percent >= value_of_1_to_4:
                value = value_percent - correcting_value
                return self.correcting_value_percent(
                    browser, value_percent, value, locator, element)
            else:
                return self.correcting_value_percent(
                    browser, value_percent, value_percent, locator, element)

        def correcting_value_percent(
                self, browser, value_percent, value, locator, element):
            if str(value) in self.get_value_progress_bar(browser, locator, element):
                return str(value_percent)
            else:
                return self.correcting_value_percent(
                    browser, value_percent, value, locator, element)
