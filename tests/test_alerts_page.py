import allure
import pytest

from pages import AlertsPage
from locators import Alerts

from tools import Logger
from tools.RandomName import RandomName

WAY = 'tools/data_names.json'
NAME = RandomName.random_name(WAY)


class TestAlertPage:

    @pytest.fixture(scope="function", autouse=True)
    # @Logger.logger.catch()
    def setup(self, browser):
        """Checking alerts page. Clicking all alert buttons and
        expect for correct operation of them"""
        alerts_page = AlertsPage(browser=browser, url=Alerts.LINK)

        alerts_page.page_response()
        alerts_page.open_page()
        alerts_page.check_title_alerts_page()
        alerts_page.wait_while_load_in_alert_page()
        alerts_page.check_is_displayed_alerts_button()

    @allure.feature("Alert page.")
    @allure.link(url=Alerts.LINK, name='ALERTS_LINK')
    # @Logger.logger.catch()
    def test_alert_button(self, browser):
        alerts_page = AlertsPage(browser=browser, url=Alerts.LINK)
        alerts_page.click_alert_button()
        alerts_page.checks_gotten_alert_text()
        alerts_page.alert_click_ok()

    @allure.feature("Alert page.")
    @allure.link(url=Alerts.LINK, name='ALERTS_LINK')
    # @Logger.logger.catch()
    def test_alert_button_appear_five_second(self, browser):
        """Appear 5 second."""
        alerts_page = AlertsPage(browser=browser, url=Alerts.LINK)
        alerts_page.click_alert_button_witch_appear_after()
        alerts_page.wait_while_alert_is_present()
        alerts_page.check_alert_text_appear_5_seconds()
        alerts_page.alert_click_ok()

    @allure.feature("Alert page.")
    @allure.link(url=Alerts.LINK, name='ALERTS_LINK')
    # @Logger.logger.catch()
    def test_alert_button_confirm_box_ok(self, browser):
        """Confirm box 'ok'."""
        alerts_page = AlertsPage(browser=browser, url=Alerts.LINK)
        alerts_page.click_alert_button_witch_confirm_box()
        alerts_page.check_alert_text_witch_confirm_box()
        alerts_page.alert_click_ok()
        alerts_page.check_confirm_result_text_ok()

    @allure.feature("Alert page.")
    @allure.link(url=Alerts.LINK, name='ALERTS_LINK')
    # @Logger.logger.catch()
    def test_alert_button_confirm_box_cancel(self, browser):
        """Confirm box 'cancel'."""
        alerts_page = AlertsPage(browser=browser, url=Alerts.LINK)
        alerts_page.click_alert_button_witch_confirm_box()
        alerts_page.check_alert_text_witch_confirm_box()
        alerts_page.alert_click_cancel()
        alerts_page.check_confirm_result_text_cancel()

    @allure.feature("Alert page.")
    @allure.link(url=Alerts.LINK, name='ALERTS_LINK')
    # @Logger.logger.catch()
    def test_alert_button_confirm_prompt_box_empty_ok(self, browser):
        """Prompt box empty 'ok'."""
        alerts_page = AlertsPage(browser=browser, url=Alerts.LINK)
        alerts_page.click_alert_button_witch_prompt_box()
        alerts_page.check_alert_text_witch_prompt_box_empty()
        alerts_page.alert_click_ok()

    @allure.feature("Alert page.")
    @allure.link(url=Alerts.LINK, name='ALERTS_LINK')
    # @Logger.logger.catch()
    def test_alert_button_confirm_prompt_box_empty_cancel(self, browser):
        """Prompt box 'cancel'."""
        alerts_page = AlertsPage(browser=browser, url=Alerts.LINK)
        alerts_page.click_alert_button_witch_prompt_box()
        alerts_page.check_alert_text_witch_prompt_box_empty()
        alerts_page.alert_click_cancel()

    @allure.feature("Alert page.")
    @allure.link(url=Alerts.LINK, name='ALERTS_LINK')
    # @Logger.logger.catch()
    def test_alert_button_confirm_prompt_box_with_text(self, browser):
        """Prompt box 'ok' with text"""
        alerts_page = AlertsPage(browser=browser, url=Alerts.LINK)
        alerts_page.click_alert_button_witch_prompt_box()
        alerts_page.check_alert_text_witch_prompt_box_empty()
        alerts_page.enter_text_in_alert_prompt(NAME)
        alerts_page.alert_click_ok()
        alerts_page.check_prompt_result_text_ok(NAME)
