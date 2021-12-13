import requests
from pages import MainPage
from selenium.webdriver.common.by import By
from locators import Main
from tools import Logger


# @Logger.logger.catch()
def test_main_page(browser):
    main_page = MainPage()
    page_response = requests.get(url=Main.LINK)
    open_site_demoqa = main_page.open_page(browser, Main.LINK)
    get_title_demoqa = main_page.get_title(browser)
    wait_while_open_demoqa = main_page.wait_presence_of_element_located(
        browser, (By.XPATH, Main.ELEMENT_IMG))
    check_is_displayed_element_img = main_page.check_is_displayed(
        browser, By.XPATH, Main.ELEMENT_IMG)

    assert page_response.status_code == 200, "Received status code is not equal to expected!!"
    assert get_title_demoqa == "ToolsQA", "Another page is opened!"
    assert check_is_displayed_element_img == True, "The page is not loaded!"
