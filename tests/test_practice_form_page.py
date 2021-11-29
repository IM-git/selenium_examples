import os
import time
import pyautogui
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages import PracticeFormPage


def test_practice_form_page(browser, config):
    practice_form_page = PracticeFormPage(browser, config)
    open_practice_form_page = practice_form_page.open_practice_form_page()
    check_is_displayed_practice_form_page = practice_form_page.\
        check_is_displayed_practice_form_page()
    enter_first_name = practice_form_page.enter_first_name()
    enter_last_name = practice_form_page.enter_last_name()
    enter_email = practice_form_page.enter_email()
    choice_gender = practice_form_page.choice_gender()
    enter_mobile_number = practice_form_page.enter_mobile_number()
    enter_date_of_birth = practice_form_page.enter_date_of_birth()
    enter_subject = practice_form_page.enter_subject()
    choice_hobbies = practice_form_page.choice_hobbies()
    scroll_down = [practice_form_page.click_arrow_down() for _ in range(8)]
    enter_image = practice_form_page.enter_image()
    enter_current_address = practice_form_page.enter_current_address()
    enter_state = practice_form_page.enter_state()
    enter_city = practice_form_page.enter_city()
    click_submit = practice_form_page.click_submit()
    check_is_displayed_modal_body = practice_form_page.\
        check_is_displayed_modal_body()
    time.sleep(2)

    assert check_is_displayed_practice_form_page == True, \
                "The page is not loaded!!"
    assert check_is_displayed_modal_body == True, \
        "The modal body is not loaded!!"