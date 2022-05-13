from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert

from .BasePage import BasePage
from tools import Logger
from tools.allure_screenshot import taking_screenshot
from src.enums import GlobalErrorMessages, AlertsError
from locators import Alerts


class AlertsPage(BasePage):

    def __init__(self, *args, **kwargs):
        super(AlertsPage, self).__init__(*args, **kwargs)

    def alert_click_ok(self):
        Logger.Logger().info(f"Click alert 'ok'.")
        try:
            self.wait_while_alert_is_present()
            self.browser.switch_to.alert.accept()
        except TimeoutException:
            raise Exception('No alert!!')

    def alert_click_cancel(self):
        Logger.Logger().info(f"Click alert 'cancel'.")
        try:
            self.wait_while_alert_is_present()
            self.browser.switch_to.alert.dismiss()
        except TimeoutException:
            raise Exception('No alert!!')

    def click_alert_button(self):
        self.click_element(*Alerts.ID_ALERT_BUTTON)

    def click_alert_button_witch_appear_after(self):
        self.click_element(*Alerts.ID_ALERT_BUTTON_WITCH_APPEAR_AFTER)

    def click_alert_button_witch_confirm_box(self):
        self.click_element(*Alerts.ID_ALERT_BUTTON_WITCH_CONFIRM_BOX)

    def click_alert_button_witch_prompt_box(self):
        self.click_element(*Alerts.ID_ALERT_BUTTON_WITCH_PROMPT_BOX)

    def check_alert_text_appear_5_seconds(self):
        value = self.get_alert_text()
        assert value == 'This alert appeared after 5 seconds', \
            (AlertsError.WRONG_ALERT_TEXT.value,
             taking_screenshot(self.browser))

    def check_alert_text_witch_confirm_box(self):
        value = self.get_alert_text()
        assert value == 'Do you confirm action?',\
            (AlertsError.WRONG_ALERT_TEXT.value,
             taking_screenshot(self.browser))

    def check_alert_text_witch_prompt_box_empty(self):
        value = self.get_alert_text()
        assert value == 'Please enter your name',\
            (AlertsError.WRONG_ALERT_TEXT.value,
             taking_screenshot(self.browser))

    def check_confirm_result_text_ok(self):
        value = self.get_text(*Alerts.GET_CONFIRM_RESULT_TEXT)
        assert value == 'You selected Ok',\
            (AlertsError.WRONG_CONFIRM_RESULT_TEXT_OK.value,
             taking_screenshot(self.browser))

    def check_confirm_result_text_cancel(self):
        value = self.get_text(*Alerts.GET_CONFIRM_RESULT_TEXT)
        assert value == 'You selected Cancel',\
            (AlertsError.WRONG_CONFIRM_RESULT_TEXT_CANCEL.value,
             taking_screenshot(self.browser))

    def checks_gotten_alert_text(self):
        alert_text = self.get_alert_text()
        assert alert_text == 'You clicked a button', \
            (AlertsError.WRONG_ALERT_TEXT.value,
             taking_screenshot(self.browser))

    def check_prompt_result_text_ok(self, name):
        value = self.get_text(*Alerts.GET_PROMPT_RESULT_TEXT)
        assert value == f'You entered {name}',\
            (AlertsError.WRONG_CONFIRM_RESULT_TEXT_OK.value,
             taking_screenshot(self.browser))

    def check_is_displayed_alerts_button(self):
        self.check_is_displayed(*Alerts.DISPLAYED_ALERT_BUTTON)

    def enter_text_in_alert_prompt(self, name):
        Logger.Logger().info(f"Enter text in alert prompt: {name}.")
        Alert(self.browser).send_keys(name)

    def get_alert_text(self):
        Logger.Logger().info("Get alert text.")
        return Alert(self.browser).text

    def wait_while_alert_is_present(self):
        WebDriverWait(self.browser, 10).until(
            EC.alert_is_present(),
            'Timed out waiting for PA creation confirmation popup to appear.')

    def wait_while_load_in_alert_page(self):
        self.wait_presence_of_element_located(
            Alerts.WAIT_WHILE_LOAD_IN_ALERT_PAGE)
