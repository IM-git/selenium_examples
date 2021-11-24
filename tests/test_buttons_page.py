import time
from pages import ButtonsPage
from selenium.webdriver.common.by import By


def test_buttons_page(browser, config):

    buttons_page = ButtonsPage(browser, config)
    open_buttons_page = buttons_page.open_buttons_page()
    get_title_buttons_page = buttons_page.get_title()
    wait_while_loaded_buttons_page = buttons_page. \
        wait_while_loaded_buttons_page()
    check_is_displayed_double_click_button = buttons_page. \
        check_is_displayed_double_click_button()

# DOUBLE CLICK BUTTON
    click_double_click_button = buttons_page.click_double_click_button()
    get_double_click_result_text = buttons_page.get_double_click_result_text()

    # time.sleep(2)

    assert get_title_buttons_page == "ToolsQA", "Another page is opened!"
    assert check_is_displayed_double_click_button == True,\
        "The page is not loaded!!"
    assert get_double_click_result_text == 'You have done a double click', \
        'The answer does not match after double click!!'
