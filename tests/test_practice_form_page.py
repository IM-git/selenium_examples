import os
import allure
import requests
from flaky import flaky
from selenium.webdriver.common.by import By
from locators import PracticeForm
from pages import PracticeFormPage
from src.enums import GlobalErrorMessages, PracticeFormPageError
from tools import Logger
from tools.allure_screenshot import taking_screenshot


class TestPracticeForm:

    @staticmethod
    # @Logger.logger.catch()
    @allure.link(url=PracticeForm.LINK_PRACTICE_FORM_PAGE,
                 name='LINK_PRACTICE_FORM_PAGE')
    @allure.feature("Practice form page(right).")
    def test_practice_form_page_right(browser):
        """Checking practice form page. Entering all required values.
         Checking a response."""
        practice_form_page = PracticeFormPage()
        page_response = requests.get(url=PracticeForm.LINK_PRACTICE_FORM_PAGE)
        open_practice_form_page = practice_form_page.open_page(
            browser, PracticeForm.LINK_PRACTICE_FORM_PAGE)
        check_is_displayed_practice_form_page = practice_form_page.\
            check_is_displayed(
            browser, By.XPATH, PracticeForm.ID_BUTTON_SUBMIT)
        enter_first_name = practice_form_page.enter_value(
            browser, By.XPATH, PracticeForm.ID_FIRST_NAME,
            PracticeForm.FIRST_NAME)
        enter_last_name = practice_form_page.enter_value(
            browser, By.XPATH, PracticeForm.ID_LAST_NAME,
            PracticeForm.LAST_NAME)
        enter_email = practice_form_page.enter_value(
            browser, By.XPATH, PracticeForm.ID_EMAIL, PracticeForm.EMAIL)
        choice_gender = practice_form_page.click_value(
            browser, By.XPATH, PracticeForm.VALUE_GENDER)
        enter_mobile_number = practice_form_page.enter_value(
            browser, By.XPATH, PracticeForm.ID_MOBILE_NUMBER,
            PracticeForm.MOBILE_NUMBER)
        enter_date_of_birth = practice_form_page.enter_date_of_birth(
            browser, By.XPATH, PracticeForm.ID_DATE_OF_BIRTH,
            PracticeForm.DATE_OF_BIRTH)
        enter_subjects = practice_form_page.enter_subjects(
            browser, By.XPATH, PracticeForm.ID_SUBJECT,
            PracticeForm.SUBJECTS)
        get_subject_text_values = practice_form_page.get_text(
            browser, By.XPATH, PracticeForm.ID_SUBJECT_CONTAINER)
        choice_hobbies = practice_form_page.click_hobbies(
            browser, By.XPATH, PracticeForm.LIST_ID_HOBBIES)
        scroll_down =\
            [practice_form_page.click_arrow_down(browser) for _ in range(8)]
        enter_image = practice_form_page.enter_path(
            browser, By.XPATH, PracticeForm.ID_CHOICE_IMG,
            (os.getcwd() + PracticeForm.PATH_TO_IMG))
        enter_current_address = practice_form_page.enter_path(
            browser, By.XPATH, PracticeForm.ID_CURRENT_ADDRESS,
            PracticeForm.TEXT_CURRENT_ADDRESS)
        enter_state = practice_form_page.enter_place(
            browser, By.XPATH, PracticeForm.DIV_SELECT_STATE,
            PracticeForm.STATE)
        enter_city = practice_form_page.enter_place(
            browser, By.XPATH, PracticeForm.DIV_SELECT_CITY,
            PracticeForm.CITY)
        click_submit = practice_form_page.click_value(
            browser, By.XPATH, PracticeForm.ID_SUBMIT)
        check_is_displayed_modal_body = practice_form_page.\
            check_is_displayed(
            browser, By.XPATH, PracticeForm.DIV_MODAL_BODY)
        get_attribute = practice_form_page.get_attribute(
            browser, By.XPATH, PracticeForm.USER_FORM, 'class')

        assert page_response.status_code == 200,\
            GlobalErrorMessages.WRONG_STATUS_CODE.value
        assert check_is_displayed_practice_form_page == True, \
            (GlobalErrorMessages.WRONG_IS_DISPLAYED.value,
             taking_screenshot(browser))
        assert check_is_displayed_modal_body == True, \
            (PracticeFormPageError.WRONG_DISPLAYED_MODAL_BODY.value,
             taking_screenshot(browser))
        assert get_attribute == "was-validated", \
            (PracticeFormPageError.WRONG_GET_ATTRIBUTE.value,
             taking_screenshot(browser))
        assert PracticeForm.SUBJECTS == get_subject_text_values.split('\n'), \
            f'{PracticeForm.SUBJECTS} ' \
            f'{PracticeFormPageError.WRONG_PRACTICE_FORM_SUBJECT.value}'


    @staticmethod
    @flaky
    # @Logger.logger.catch()
    @allure.link(url=PracticeForm.LINK_PRACTICE_FORM_PAGE,
                 name='LINK_PRACTICE_FORM_PAGE')
    @allure.feature("Practice form page(failed).")
    def test_practice_form_page_failed(browser):
        """Checking practice form page. Entering not all required values.
        Test should not pass correct. Checking a response."""
        practice_form_page = PracticeFormPage()
        page_response = requests.get(url=PracticeForm.LINK_PRACTICE_FORM_PAGE)
        open_practice_form_page = practice_form_page.open_page(
            browser, PracticeForm.LINK_PRACTICE_FORM_PAGE)
        check_is_displayed_practice_form_page = practice_form_page. \
            check_is_displayed(
            browser, By.XPATH, PracticeForm.ID_BUTTON_SUBMIT)
        enter_email = practice_form_page.enter_value(
            browser, By.XPATH, PracticeForm.ID_EMAIL, PracticeForm.EMAIL)
        enter_date_of_birth = practice_form_page.enter_date_of_birth(
            browser, By.XPATH, PracticeForm.ID_DATE_OF_BIRTH,
            PracticeForm.DATE_OF_BIRTH)
        get_subject_text_values = practice_form_page.get_text(
            browser, By.XPATH, PracticeForm.ID_SUBJECT_CONTAINER)
        choice_hobbies = practice_form_page.click_hobbies(
            browser, By.XPATH, PracticeForm.LIST_ID_HOBBIES)
        scroll_down = \
            [practice_form_page.click_arrow_down(browser) for _ in range(8)]
        enter_image = practice_form_page.enter_path(
            browser, By.XPATH, PracticeForm.ID_CHOICE_IMG,
            (os.getcwd() + PracticeForm.PATH_TO_IMG))
        enter_current_address = practice_form_page.enter_path(
            browser, By.XPATH, PracticeForm.ID_CURRENT_ADDRESS,
            PracticeForm.TEXT_CURRENT_ADDRESS)
        enter_state = practice_form_page.enter_place(
            browser, By.XPATH, PracticeForm.DIV_SELECT_STATE,
            PracticeForm.STATE)
        enter_city = practice_form_page.enter_place(
            browser, By.XPATH, PracticeForm.DIV_SELECT_CITY,
            PracticeForm.CITY)
        click_submit = practice_form_page.click_value(
            browser, By.XPATH, PracticeForm.ID_SUBMIT)
        check_is_displayed_modal_body = practice_form_page. \
            check_is_displayed(
            browser, By.XPATH, PracticeForm.DIV_MODAL_BODY)
        get_attribute = practice_form_page.get_attribute(
            browser, By.XPATH, PracticeForm.USER_FORM, 'class')

        assert page_response.status_code == 200, \
            GlobalErrorMessages.WRONG_STATUS_CODE.value
        assert check_is_displayed_practice_form_page == True, \
            (GlobalErrorMessages.WRONG_IS_DISPLAYED.value,
             taking_screenshot(browser))
        assert check_is_displayed_modal_body == False, \
            (PracticeFormPageError.WRONG_DISPLAYED_MODAL_BODY.value,
             taking_screenshot(browser))
        assert get_attribute == "was-validated", \
            (PracticeFormPageError.WRONG_GET_ATTRIBUTE.value,
             taking_screenshot(browser))
        assert get_subject_text_values == '', \
            (PracticeFormPageError.WRONG_SUBJECT_TEXT.value,
             taking_screenshot(browser))
