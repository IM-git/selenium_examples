import allure
import pytest

from locators import PracticeForm
from pages import PracticeFormPage
from tools import Logger


class TestPracticeForm:
    """
    Checking practice form page.
    Checking a response.
    In these tests necessary was changed windows size
    because of advertisement on the webpage which
    hinders the test to work.
    """
    # @Logger.logger.catch()
    @pytest.fixture(scope="function", autouse=True)
    @allure.link(url=PracticeForm.LINK_PRACTICE_FORM_PAGE,
                 name='LINK_PRACTICE_FORM_PAGE')
    @allure.feature("Practice form page(right).")
    def setup(self, browser):
        """Entering all required values."""
        browser.set_window_size(600, 1400)
        practice_form_page = PracticeFormPage(
            browser=browser,
            url=PracticeForm.LINK_PRACTICE_FORM_PAGE)
        practice_form_page.page_response()
        practice_form_page.open_page()
        practice_form_page.checks_is_displayed_practice_form_page()

    def test_practice_form_page_right(self, browser):
        practice_form_page = PracticeFormPage(
            browser=browser,
            url=PracticeForm.LINK_PRACTICE_FORM_PAGE)
        practice_form_page.enter_first_name()
        practice_form_page.enter_last_name()
        practice_form_page.enter_email()
        practice_form_page.choice_gender()
        practice_form_page.enter_mobile_number()
        practice_form_page.enter_date_of_birth()
        practice_form_page.scroll_down()

        practice_form_page.enter_subjects()
        practice_form_page.checks_subject_text_values()
        practice_form_page.choice_hobbies()
        practice_form_page.scroll_down()
        practice_form_page.enter_image()
        practice_form_page.scroll_down()
        practice_form_page.enter_current_address()
        practice_form_page.enter_state()
        practice_form_page.enter_city()
        practice_form_page.click_submit()
        practice_form_page.checks_is_displayed_modal_body()
        practice_form_page.checks_attribute_was_validated()

    # @Logger.logger.catch()
    @pytest.mark.xfail
    @allure.link(url=PracticeForm.LINK_PRACTICE_FORM_PAGE,
                 name='LINK_PRACTICE_FORM_PAGE')
    @allure.feature("Practice form page(failed).")
    def test_practice_form_page_failed(self, browser):
        """Entering not all required values.
        Test should not pass correct."""
        browser.set_window_size(600, 1400)
        practice_form_page = PracticeFormPage(
            browser=browser,
            url=PracticeForm.LINK_PRACTICE_FORM_PAGE)

        practice_form_page.enter_email()
        practice_form_page.enter_date_of_birth()
        practice_form_page.scroll_down()
        practice_form_page.enter_subjects()
        practice_form_page.checks_subject_text_values()
        practice_form_page.choice_hobbies()
        practice_form_page.scroll_down()
        practice_form_page.enter_image()
        practice_form_page.scroll_down()
        practice_form_page.enter_current_address()
        practice_form_page.enter_state()
        practice_form_page.enter_city()
        practice_form_page.click_submit()
        practice_form_page.checks_is_displayed_modal_body()
