from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .BasePage import BasePage
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from locators import Alerts


class AlertsPage(BasePage):

# CHECK IS DISPLAYED
    def check_is_displayed_prompt_text(self, browser, locator, element):
        time_displayed_prompt_text = 1
        try:
            self._implicitly_wait(time_displayed_prompt_text)
            self.check_is_displayed(
                browser, locator, element)
        except NoSuchElementException:
            return False
        return True

# WORK WITH ALERT
    def get_alert_text(self):
        return Alert(self.browser).text

    def enter_text_in_alert_prompt(self, text):
        return Alert(self.browser).send_keys(text)

# WORK WITH WAIT ALERT
    def wait_while_alert_is_present(self, time):
        return WebDriverWait(self.browser, time).until(
                EC.alert_is_present(),
                'Timed out waiting for PA creation'
                'confirmation popup to appear.')

# CLICK BUTTON ALERT
    def alert_click_ok(self, time):
        try:
            self.wait_while_alert_is_present(time)
            self.browser.switch_to.alert.accept()
        except TimeoutException:
            raise Exception('No alert!!')

    def alert_click_cancel(self, time):
        try:
            self.wait_while_alert_is_present(time)
            self.browser.switch_to.alert.dismiss()
        except TimeoutException:
            raise Exception('No alert!!')
