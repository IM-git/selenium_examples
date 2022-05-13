import allure
from flaky import flaky
from pages import SliderPage
from pages import ProgressBarPage
from locators import Widgets


class TestWidgets:

    # @Logger.logger.catch()
    @allure.link(url=Widgets.LINK_SLIDER, name='LINK_SLIDER')
    @allure.feature("Slider page.")
    def test_slider(self, browser):
        """Checking correct operation a slider
        on the widgets page."""
        slider_page = SliderPage(browser=browser,
                                 url=Widgets.LINK_SLIDER)
        slider_page.page_response()
        slider_page.open_page()
        slider_page.check_is_displayed_slider()
        slider_page.move_to_slider()
        slider_page.checking_slider()

    # @Logger.logger.catch()
    @allure.link(url=Widgets.LINK_PROGRESS_BAR,
                 name='LINK_PROGRESS_BAR_PAGE')
    @flaky(max_runs=4)
    @allure.feature("Progress bar page.")
    def test_progress_bar(self, browser):
        """Checking correct operation a progress bar
        on the widgets page.
        Uses flaky, the test has 4 attempts to run,
        if test passed, the run will be stopped."""
        progress_bar_page = ProgressBarPage(browser=browser,
                                            url=Widgets.LINK_PROGRESS_BAR)
        progress_bar_page.page_response()
        progress_bar_page.open_page()
        progress_bar_page.check_is_displayed_reset_button()
        progress_bar_page.checks_value_progress_bar()
