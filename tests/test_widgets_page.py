import time

from pages import WidgetsPage


class TestWidgets:

    # @staticmethod
    # def test_slider(browser, config):
    #     widgets_page = WidgetsPage.Slider(browser, config)
    #     open_slider_page = widgets_page.open_slider_page()
    #     check_is_displayed_slider = widgets_page.check_is_displayed_slider()
    #     move_to_slider = widgets_page.move_to_slider()
    #     do_random_steps = widgets_page.making_random_steps()
    #     checking_slider_value = widgets_page.checking_slider_value()
    #
    #     assert check_is_displayed_slider == True, \
    #         "The page is not loaded!!"
    #     assert do_random_steps == checking_slider_value,\
    #         "The steps which were did is not match the" \
    #         "displayed value steps on the page"

    @staticmethod
    def test_progress_bar(browser, config):
        widgets_page = WidgetsPage.ProgressBar(browser, config)
        open_progress_bar = widgets_page.open_progress_bar_page()
        check_is_displayed_reset_button = widgets_page.\
            check_is_displayed_button()
        click_start_button = widgets_page.click_start_stop_button()
        wait_while_progress_bar_became = widgets_page.wait_while_progress_bar_became()
        click_stop_button = widgets_page.click_start_stop_button()
        get_value_progress_bar = widgets_page.get_value_progress_bar()

        assert check_is_displayed_reset_button == True,\
            "The page is not loaded!!"
        assert wait_while_progress_bar_became in get_value_progress_bar,\
            "Entered value isn't match with value in the page!!"
