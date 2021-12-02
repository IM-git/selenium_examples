import time
from selenium.webdriver.common.by import By
from pages import WidgetsPage
from locators import Widgets


class TestWidgets:

    @staticmethod
    def test_slider(browser, config):
        widgets_page = WidgetsPage.Slider(browser, config)
        open_slider_page = widgets_page.open_page(Widgets.LINK_SLIDER_PAGE)
        check_is_displayed_slider = widgets_page.check_is_displayed(
            browser, By.XPATH, Widgets.INPUT_SLIDER)
        move_to_slider = widgets_page.move_to_slider(
            By.XPATH, Widgets.INPUT_SLIDER)
        do_random_steps = widgets_page.making_random_steps(
            By.XPATH, Widgets.INPUT_SLIDER)
        checking_slider_value = widgets_page.checking_slider_value(
            By.XPATH, Widgets.VALUE_SLIDER)

        assert check_is_displayed_slider == True, \
            "The page is not loaded!!"
        assert do_random_steps == checking_slider_value,\
            "The steps which were did is not match the" \
            "displayed value steps on the page"

    @staticmethod
    def test_progress_bar(browser, config):
        widgets_page = WidgetsPage.ProgressBar(browser, config)
        open_progress_bar = widgets_page.open_page(
            Widgets.LINK_PROGRESS_BAR_PAGE)
        check_is_displayed_reset_button = widgets_page.\
            check_is_displayed(
            browser, By.XPATH, Widgets.PROGRESS_BAR_START_STOP_BUTTON)
        click_start_button = widgets_page.click_button(
            browser, By.XPATH, Widgets.PROGRESS_BAR_START_STOP_BUTTON)
        wait_while_progress_bar_became = widgets_page.\
            wait_while_progress_bar_became(
            Widgets.VALUE_PERCENT, By.XPATH, Widgets.VALUE_PROGRESS_BAR)
        click_stop_button = widgets_page.click_button(
            browser, By.XPATH, Widgets.PROGRESS_BAR_START_STOP_BUTTON)
        get_value_progress_bar = widgets_page.get_value_progress_bar(
            By.XPATH, Widgets.VALUE_PROGRESS_BAR)

        assert check_is_displayed_reset_button == True,\
            "The page is not loaded!!"
        assert wait_while_progress_bar_became in get_value_progress_bar,\
            "Entered value isn't match with value in the page!!"
