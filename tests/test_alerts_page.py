from pages import AlertsPage
from selenium.webdriver.common.by import By


def test_alerts_page(browser, config):
    alerts_page = AlertsPage(browser, config)
    open_main_page = alerts_page.open_main_page()
    click_alert_button = alerts_page.click_alert_button()
    get_title_alerts_page = alerts_page.get_title()
    wait_while_open_alerts_page = alerts_page.\
        wait_while_open_alerts_windows_page()
    check_is_displayed_alerts_listbox = alerts_page.\
        check_is_displayed_alerts_listbox()

    assert get_title_alerts_page == "ToolsQA", "Another page is opened!"
    assert check_is_displayed_alerts_listbox == True, "The page is not loaded!"
