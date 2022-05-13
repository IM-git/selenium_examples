import pytest
import allure
from pages import ButtonsPage
from locators import Buttons


class TestButtonsPage:
    """
    Checking buttons page. Clicking all buttons and
    expect for correct operation of them.
    """

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        buttons_page = ButtonsPage(browser=browser, url=Buttons.LINK)
        buttons_page.page_response()
        buttons_page.open_page()
        buttons_page.checks_title()
        buttons_page.wait_while_loaded_buttons_page()
        buttons_page.check_is_displayed_double_click_button()

    @allure.feature("Buttons page.")
    @allure.link(url=Buttons.LINK, name='BUTTONS_LINK')
    # @Logger.logger.catch()
    def test_double_click_by_button(self, browser):
        """Checking double click by button."""
        buttons_page = ButtonsPage(browser=browser, url=Buttons.LINK)
        buttons_page.double_click_by_button()
        buttons_page.checks_double_click_result_text()

    @allure.feature("Buttons page.")
    @allure.link(url=Buttons.LINK, name='BUTTONS_LINK')
    # @Logger.logger.catch()
    def test_right_click_by_button(self, browser):
        """Checking right click by button."""
        buttons_page = ButtonsPage(browser=browser, url=Buttons.LINK)
        buttons_page.click_one_right_button()
        buttons_page.checks_right_click_result_text()

    @allure.feature("Buttons page.")
    @allure.link(url=Buttons.LINK, name='BUTTONS_LINK')
    # @Logger.logger.catch()
    def test_one_click_by_button(self, browser):
        """Checking one click by button."""
        buttons_page = ButtonsPage(browser=browser, url=Buttons.LINK)
        buttons_page.click_button()
        buttons_page.checks_click_result_text()
