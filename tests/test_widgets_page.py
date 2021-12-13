import time
import requests
from selenium.webdriver.common.by import By
from pages import WidgetsPage
from locators import Widgets
from src.enums import GlobalErrorMessages, WidgetsPageError
from tools import Logger


class TestWidgets:

    @staticmethod
    # @Logger.logger.catch()
    def test_slider(browser):
        widgets_page = WidgetsPage.Slider()
        page_response = requests.get(url=Widgets.LINK_SLIDER_PAGE)
        open_slider_page = widgets_page.open_page(
            browser, Widgets.LINK_SLIDER_PAGE)
        check_is_displayed_slider = widgets_page.check_is_displayed(
            browser, By.XPATH, Widgets.INPUT_SLIDER)
        move_to_slider = widgets_page.move_to_slider(
            browser, By.XPATH, Widgets.INPUT_SLIDER)
        do_random_steps = widgets_page.making_random_steps(
            browser, By.XPATH, Widgets.INPUT_SLIDER)
        checking_slider_value = widgets_page.checking_slider_value(
            browser, By.XPATH, Widgets.VALUE_SLIDER)

        assert page_response.status_code == 200,\
            GlobalErrorMessages.WRONG_STATUS_CODE
        assert check_is_displayed_slider == True, \
            GlobalErrorMessages.WRONG_IS_DISPLAYED
        assert do_random_steps == checking_slider_value,\
            WidgetsPageError.WRONG_DID_RANDOM_STEPS

    @staticmethod
    # @Logger.logger.catch()
    def test_progress_bar(browser):
        widgets_page = WidgetsPage.ProgressBar()
        page_response = requests.get(url=Widgets.LINK_PROGRESS_BAR_PAGE)
        open_progress_bar = widgets_page.open_page(
            browser, Widgets.LINK_PROGRESS_BAR_PAGE)
        check_is_displayed_reset_button = widgets_page.\
            check_is_displayed(
            browser, By.XPATH, Widgets.PROGRESS_BAR_START_STOP_BUTTON)
        click_start_button = widgets_page.click_button(
            browser, By.XPATH, Widgets.PROGRESS_BAR_START_STOP_BUTTON)
        wait_while_progress_bar_became = widgets_page.\
            wait_while_progress_bar_became(
            browser, Widgets.VALUE_PERCENT, By.XPATH,
            Widgets.VALUE_PROGRESS_BAR)
        click_stop_button = widgets_page.click_button(
            browser, By.XPATH, Widgets.PROGRESS_BAR_START_STOP_BUTTON)
        get_value_progress_bar = widgets_page.get_value_progress_bar(
            browser, By.XPATH, Widgets.VALUE_PROGRESS_BAR)

        assert page_response.status_code == 200,\
            GlobalErrorMessages.WRONG_STATUS_CODE
        assert check_is_displayed_reset_button == True,\
            GlobalErrorMessages.WRONG_IS_DISPLAYED
        assert wait_while_progress_bar_became in get_value_progress_bar,\
            WidgetsPageError.WRONG_ENTERED_VALUE_IN_PAGE
