import pytest
import allure
from pages import MainPage
from locators import Main
from tools import Logger


class TestMainPage:
    """
    Checking main page. Open main page.
    Checking the text in the tab header.
    Checking the image display.
    """
    # @pytest.fixture(scope="function", autouse=True)
    @allure.feature("Main page.")
    @allure.link(url=Main.LINK, name='MAIN_LINK')
    # @Logger.logger.catch()
    def test_main_page(self, browser):
        main_page = MainPage(browser=browser, url=Main.LINK)
        main_page.page_response()
        main_page.open_page()
        main_page.checks_title()
        main_page.wait_while_open_demoqa()
        main_page.checks_is_displayed_element_img()
