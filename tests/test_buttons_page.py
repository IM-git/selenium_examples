import requests
from pages import ButtonsPage
from locators import Buttons
from selenium.webdriver.common.by import By
from src.enums import GlobalErrorMessages, ButtonsError
from tools import Logger


# @Logger.logger.catch()
def test_buttons_page(browser):
    buttons_page = ButtonsPage()
    page_response = requests.get(url=Buttons.LINK)
    open_buttons_page = buttons_page.open_page(browser, Buttons.LINK)
    get_title_buttons_page = buttons_page.get_title(browser)
    wait_while_loaded_buttons_page = buttons_page. \
        wait_presence_of_element_located(
        browser, (By.XPATH, Buttons.BUTTON_DOUBLE_CLICK_ME))
    check_is_displayed_double_click_button = buttons_page. \
        check_is_displayed(
        browser, By.XPATH, Buttons.BUTTON_DOUBLE_CLICK_ME)

# DOUBLE CLICK BUTTON
    click_double_click_button = buttons_page.click_double_click_button(
        browser, By.XPATH, Buttons.BUTTON_DOUBLE_CLICK_ME)
    get_double_click_result_text = buttons_page.get_text(
        browser, By.XPATH, Buttons.GET_DOUBLE_CLICK_RESULT_TEXT)

# RIGHT CLICK BUTTON
    click_one_right_button = buttons_page.click_one_right_button(
        browser, By.XPATH, Buttons.BUTTON_RIGHT_CLICK)
    get_right_click_result_text = buttons_page.get_text(
        browser, By.XPATH, Buttons.GET_RIGHT_CLICK_RESULT_TEXT)

# ONE CLICK BUTTON
    click_button = buttons_page.click_button(
        browser, By.XPATH, Buttons.BUTTON_CLICK)
    get_click_result_text = buttons_page.get_text(
        browser, By.XPATH, Buttons.GET_CLICK_RESULT_TEXT)

    assert page_response.status_code == 200, GlobalErrorMessages.WRONG_STATUS_CODE
    assert get_title_buttons_page == "ToolsQA", GlobalErrorMessages.WRONG_TITLE_PAGE
    assert check_is_displayed_double_click_button == True,\
        GlobalErrorMessages.WRONG_IS_DISPLAYED
    assert get_double_click_result_text == 'You have done a double click', \
        ButtonsError.WRONG_ANSWER_AFTER_DOUBLE_CLICK
    assert get_right_click_result_text == 'You have done a right click', \
        ButtonsError.WRONG_ANSWER_AFTER_RIGHT_CLICK
    assert get_click_result_text == 'You have done a dynamic click', \
        ButtonsError.WRONG_ANSWER_AFTER_RIGHT_CLICK
