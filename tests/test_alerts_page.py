import time
from pages import AlertsPage
from selenium.webdriver.common.by import By
from locators import Alerts


def test_alerts_page(browser, config):

    alerts_page = AlertsPage(browser, config)
    open_main_page = alerts_page.open_page(Alerts.LINK)
    get_title_alerts_page = alerts_page.get_title()
    wait_while_loaded_alerts_page = alerts_page.\
        wait_presence_of_element_located((By.XPATH, Alerts.WAIT_WHILE_LOAD_IN_ALERT_PAGE))
    check_is_displayed_alerts_button = alerts_page.\
        check_is_displayed_alerts_button(By.XPATH, Alerts.DISPLAYED_ALERT_BUTTON)

# ALERT BUTTON
    click_alert_button = alerts_page.click_element(By.XPATH, Alerts.ID_ALERT_BUTTON)
    get_alert_text = alerts_page.get_alert_text()
    alert_click_ok = alerts_page.alert_click_ok(Alerts.TIME_DEFAULT)

# APPEAR 5 SECOND
    click_alert_button_with_appear_after_5_seconds = alerts_page.\
        click_element(By.XPATH, Alerts.ID_ALERT_BUTTON_WITCH_APPEAR_AFTER)
    wait_while_alert_is_present = alerts_page.wait_while_alert_is_present(Alerts.TIME_DEFAULT)
    get_alert_text_appear_5_seconds = alerts_page.get_alert_text()
    alert_click_ok_appear_5_seconds = alerts_page.alert_click_ok(Alerts.TIME_DEFAULT)

# CONFIRM BOX 'Ok'
    click_alert_button_witch_confirm_box = alerts_page.\
        click_element(By.XPATH, Alerts.ID_ALERT_BUTTON_WITCH_CONFIRM_BOX)
    get_alert_text_witch_confirm_box_ok = alerts_page.get_alert_text()
    alert_click_ok = alerts_page.alert_click_ok(Alerts.TIME_DEFAULT)
    get_confirm_result_text_ok = alerts_page.get_text(By.XPATH, Alerts.GET_CONFIRM_RESULT_TEXT)

# CONFIRM BOX 'Cancel'
    click_alert_button_witch_confirm_box = alerts_page. \
        click_element(By.XPATH, Alerts.ID_ALERT_BUTTON_WITCH_CONFIRM_BOX)
    get_alert_text_witch_confirm_box_cancel = alerts_page.get_alert_text()
    alert_click_cancel = alerts_page.alert_click_cancel(Alerts.TIME_DEFAULT)
    get_confirm_result_text_cancel = alerts_page.get_text(By.XPATH, Alerts.GET_CONFIRM_RESULT_TEXT)

# PROMPT BOX EMPTY 'Ok'
    click_alert_button_witch_prompt_box = alerts_page.click_element(By.XPATH, Alerts.ID_ALERT_BUTTON_WITCH_PROMPT_BOX)
    get_alert_text_witch_prompt_box_empty_ok = alerts_page.get_alert_text()
    alert_click_ok = alerts_page.alert_click_ok(Alerts.TIME_DEFAULT)
    check_is_displayed_prompt_text_ok = alerts_page.check_is_displayed_prompt_text(By.XPATH, Alerts.GET_PROMPT_RESULT_TEXT)

# PROMPT BOX 'Cancel'
    click_alert_button_witch_prompt_box = alerts_page.click_element(By.XPATH, Alerts.ID_ALERT_BUTTON_WITCH_PROMPT_BOX)
    get_alert_text_witch_prompt_box_cancel = alerts_page.get_alert_text()
    alert_click_ok = alerts_page.alert_click_ok(Alerts.TIME_DEFAULT)
    check_is_displayed_prompt_text_cancel = alerts_page.check_is_displayed_prompt_text(By.XPATH, Alerts.GET_PROMPT_RESULT_TEXT)

# PROMPT BOX 'Ok' WITH TEXT
    click_alert_button_witch_prompt_box = alerts_page.click_element(By.XPATH, Alerts.ID_ALERT_BUTTON_WITCH_PROMPT_BOX)
    get_alert_text_witch_prompt_box_ok = alerts_page.get_alert_text()
    enter_text_in_alert_prompt = alerts_page.enter_text_in_alert_prompt(Alerts.ENTER_TEXT_IN_ALERT_PROMPT)
    alert_click_ok = alerts_page.alert_click_ok(Alerts.TIME_DEFAULT)
    get_prompt_result_text_ok = alerts_page.get_text(By.XPATH, Alerts.GET_PROMPT_RESULT_TEXT)


    # time.sleep(2)

    assert get_title_alerts_page == "ToolsQA", "Another page is opened!"
    assert check_is_displayed_alerts_button == True,\
        "The page is not loaded!!"
    assert get_alert_text == 'You clicked a button',\
        "Alert not displayed!!"
    assert get_alert_text_appear_5_seconds ==\
           'This alert appeared after 5 seconds', "Alert not displayed!!"
    assert get_alert_text_witch_confirm_box_ok == 'Do you confirm action?',\
        "Alert not displayed!!"
    assert get_confirm_result_text_ok == 'You selected Ok',\
        'The answer does not match after clicking "Ok"!!'
    assert get_alert_text_witch_confirm_box_cancel == 'Do you confirm action?', \
        "Alert not displayed!!"
    assert get_confirm_result_text_cancel == 'You selected Cancel', \
        'The answer does not match after clicking "Cancel"!!'
    assert get_alert_text_witch_prompt_box_empty_ok == 'Please enter your name', \
        "Alert not displayed!!"
    assert check_is_displayed_prompt_text_ok == False, \
        'The answer text exists after clicking "Ok"!!'
    assert get_alert_text_witch_prompt_box_cancel == 'Please enter your name', \
        "Alert not displayed!!"
    assert check_is_displayed_prompt_text_cancel == False, \
        'The answer text exists after clicking "Cancel"!!'

    assert get_alert_text_witch_prompt_box_ok == 'Please enter your name', \
        "Alert not displayed!!"
    assert get_prompt_result_text_ok == 'You entered User', \
        'The answer does not match after clicking "Ok"!!'
