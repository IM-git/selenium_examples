import requests
import allure
from pages import MainPage
from selenium.webdriver.common.by import By
from locators import Main
from src.enums import GlobalErrorMessages
from tools import Logger
from tools.allure_screenshot import AllureScreenshot


@allure.feature("Main page.")
# @Logger.logger.catch()
def test_main_page(browser):
    """Checking main page. Open main page.
    Checking the text in the tab header. Checking the image display."""
    main_page = MainPage()
    page_response = requests.get(url=Main.LINK)
    open_site_demoqa = main_page.open_page(browser, Main.LINK)
    get_title_demoqa = main_page.get_title(browser)
    wait_while_open_demoqa = main_page.wait_presence_of_element_located(
        browser, (By.XPATH, Main.ELEMENT_IMG))
    check_is_displayed_element_img = main_page.check_is_displayed(
        browser, By.XPATH, Main.ELEMENT_IMG)

    assert page_response.status_code == 200, \
        GlobalErrorMessages.WRONG_STATUS_CODE.value
    assert get_title_demoqa == "ToolsQA", \
        GlobalErrorMessages.WRONG_TITLE_PAGE.value
    assert check_is_displayed_element_img == True, \
        GlobalErrorMessages.WRONG_IS_DISPLAYED.value

    taking_screenshot = AllureScreenshot().make_screenshot(browser)
