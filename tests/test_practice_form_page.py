import os
import time
import pyautogui
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import PracticeForm
from pages import PracticeFormPage
from tools import Logger


class TestPracticeForm:

    @staticmethod
    # @Logger.logger.catch()
    def test_practice_form_page_right(browser):
        practice_form_page = PracticeFormPage()
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
        enter_subject_computer_science = practice_form_page.enter_subject(
            browser, By.XPATH, PracticeForm.ID_SUBJECT,
            PracticeForm.SUBJECTS_COMPUTER_SCIENCE)
        enter_subject_english = practice_form_page.enter_subject(
            browser, By.XPATH, PracticeForm.ID_SUBJECT,
            PracticeForm.SUBJECTS_ENGLISH)
        get_subject_text_values = practice_form_page.get_text(
            browser, By.XPATH, PracticeForm.ID_SUBJECT_CONTAINER)
        choice_hobbies_reading = practice_form_page.click_value(
            browser, By.XPATH, PracticeForm.ID_HOBIE_READING)
        choice_hobbies_music = practice_form_page.click_value(
            browser, By.XPATH, PracticeForm.ID_HOBIE_MUSIC)
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

        assert check_is_displayed_practice_form_page == True, \
                    "The page is not loaded!!"
        assert check_is_displayed_modal_body == True, \
            "The modal body is not loaded!!"
        assert get_attribute == "was-validated", \
            "Submit button is not pushed!!"
        assert PracticeForm.SUBJECTS_COMPUTER_SCIENCE and\
            PracticeForm.SUBJECTS_ENGLISH in get_subject_text_values,\
            f'{PracticeForm.SUBJECTS_COMPUTER_SCIENCE} and' \
            f'{PracticeForm.SUBJECTS_ENGLISH} are not added in form!!'

    @staticmethod
    # @Logger.logger.catch()
    def test_practice_form_page_failed(browser):
        print(browser)
        practice_form_page = PracticeFormPage()
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
        choice_hobbies_reading = practice_form_page.click_value(
            browser, By.XPATH, PracticeForm.ID_HOBIE_READING)
        choice_hobbies_music = practice_form_page.click_value(
            browser, By.XPATH, PracticeForm.ID_HOBIE_MUSIC)
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

        assert check_is_displayed_practice_form_page == True, \
            "The page is not loaded!!"
        assert check_is_displayed_modal_body == False, \
            "The modal body is loaded!!"
        assert get_attribute == "was-validated",\
            "Submit button is not pushed!!"
        assert get_subject_text_values == '', 'Some text exist!!'
