import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages import BasePage
from tools.MouseKeyboardActions import MouseKeyboardActions
from selenium.webdriver.common.by import By
from tools.RandomTools import RandomTools


LINK_SLIDER_PAGE = 'https://demoqa.com/slider'
LINK_PROGRESS_BAR_PAGE = 'https://demoqa.com/progress-bar'
INPUT_SLIDER = '//input[@class="range-slider range-slider--primary"]'
VALUE_SLIDER = '//input[@id="sliderValue"]'
PROGRESS_BAR_START_STOP_BUTTON = '//button[@id="startStopButton"]'
PROGRESS_BAR_RESET_BUTTON = '//button[@id="resetButton"]'
VALUE_PROGRESS_BAR = '//div[@class="progress-bar bg-info"]'
TEST_ELEM = '//div[text()="19%"]'


class WidgetsPage:

    def __init__(self):
        pass

    # SLIDER PAGE
    class Slider(BasePage):

        def open_slider_page(self):
            return self.open_page(LINK_SLIDER_PAGE)

        def check_is_displayed_slider(self):
            element = self.base_element.find_element_(
                self.browser, By.XPATH, INPUT_SLIDER)
            return self.base_element.check_is_displayed(element)

        def move_to_slider(self):
            value = self.base_element.find_element_(
                self.browser, By.XPATH, INPUT_SLIDER)
            return MouseKeyboardActions(self.browser).\
                move_to_element(value)

        def making_random_steps(self):
            value = self.base_element.find_element_(
                self.browser, By.XPATH, INPUT_SLIDER)
            return RandomTools.Steps.do_random_steps(value)

        def checking_slider_value(self):
            element = self.base_element.find_element_(
                self.browser, By.XPATH, VALUE_SLIDER)
            return int(self.base_element.get_to_attribute(element=element, attribute="value"))-25

    # PROGRESS BAR PAGE
    class ProgressBar(BasePage):

        def open_progress_bar_page(self):
            return self.open_page(LINK_PROGRESS_BAR_PAGE)

        def check_is_displayed_button(self):
            element = self.base_element.find_element_(
                self.browser, By.XPATH, PROGRESS_BAR_START_STOP_BUTTON)
            return self.base_element.check_is_displayed(element)

        def click_start_stop_button(self):
            value = self.base_element.find_element_(
                self.browser, By.XPATH, PROGRESS_BAR_START_STOP_BUTTON)
            return MouseKeyboardActions(self.browser).one_click(value)

        def click_reset_button(self):
            value = self.base_element.find_element_(
                self.browser, By.XPATH, PROGRESS_BAR_RESET_BUTTON)
            return MouseKeyboardActions(self.browser).one_click(value)

        def text(self):
            return self.get_text(By.XPATH, VALUE_PROGRESS_BAR)

        def wait_while_progress_bar_became(self):
            # return time.sleep(2)
            element = self.base_element.find_element_(self.browser, By.XPATH, TEST_ELEM)
            return WebDriverWait(self.browser, 10).until(EC.text_to_be_present_in_element(
                (By.XPATH, VALUE_PROGRESS_BAR), '19%'))
