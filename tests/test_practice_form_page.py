import time

from pages import PracticeFormPage


def test_practice_form_page(browser, config):
    practice_form_page = PracticeFormPage(browser, config)
    open_practice_form_page = practice_form_page.open_practice_form_page()
    check_is_displayed_practice_form_page = practice_form_page.check_is_displayed_practice_form_page()
    enter_first_name = practice_form_page.enter_first_name()
    enter_last_name = practice_form_page.enter_last_name()
    time.sleep(2)


    assert check_is_displayed_practice_form_page == True, \
                "The page is not loaded!!"