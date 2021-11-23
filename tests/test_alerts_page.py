import time
from pages import AlertsPage
from selenium.webdriver.common.by import By


def test_alerts_page(browser, config):
    alerts_page = AlertsPage(browser, config)
    open_main_page = alerts_page.open_alerts_page()
    get_title_alerts_page = alerts_page.get_title()
    wait_while_loaded_alerts_page = alerts_page.wait_while_loaded_alerts_page()
    check_is_displayed_alerts_button = alerts_page.check_is_displayed_alerts_button()

    assert get_title_alerts_page == "ToolsQA", "Another page is opened!"
    assert check_is_displayed_alerts_button == True, "The page is not loaded!"
