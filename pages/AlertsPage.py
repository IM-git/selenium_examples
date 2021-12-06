from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .BasePage import BasePage
from selenium.webdriver.common.alert import Alert
from tools import Logger
from selenium.webdriver.common.by import By
from locators import Alerts


class AlertsPage(BasePage):

# CHECK IS DISPLAYED
    def check_is_displayed_prompt_text(self, browser, locator, element):
        Logger.Logger().info(f"Check is displayed prompt text(element:{element}).")
        time_displayed_prompt_text = 1
        try:
            self._implicitly_wait(browser, time_displayed_prompt_text)
            self.check_is_displayed(
                browser, locator, element)
        except NoSuchElementException:
            return False
        return True

# WORK WITH ALERT
    def get_alert_text(self, browser):
        Logger.Logger().info("Get alert text.")
        return Alert(browser).text

    def enter_text_in_alert_prompt(self, browser, text):
        Logger.Logger().info(f"Enter text in alert prompt: {text}.")
        return Alert(browser).send_keys(text)

# WORK WITH WAIT ALERT
    def wait_while_alert_is_present(self, browser, time):
        Logger.Logger().info(f"wait while alert is present(time: {time}).")
        return WebDriverWait(browser, time).until(
                EC.alert_is_present(),
                'Timed out waiting for PA creation'
                'confirmation popup to appear.')

# CLICK BUTTON ALERT
    def alert_click_ok(self, browser, time):
        Logger.Logger().info(f"Click alert 'ok'.")
        try:
            self.wait_while_alert_is_present(browser, time)
            browser.switch_to.alert.accept()
        except TimeoutException:
            raise Exception('No alert!!')

    def alert_click_cancel(self, browser, time):
        Logger.Logger().info(f"Click alert 'cancel'.")
        try:
            self.wait_while_alert_is_present(browser, time)
            browser.switch_to.alert.dismiss()
        except TimeoutException:
            raise Exception('No alert!!')
