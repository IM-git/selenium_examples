from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .BasePage import BasePage
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By


TIME_DEFAULT = 10
LINK = 'https://demoqa.com/alerts'
WAIT_WHILE_LOAD_IN_ALERT_PAGE = '//div[@class="body-height"]'
DISPLAYED_ALERT_BUTTON = '//button[@id="alertButton"]'
ID_ALERT_BUTTON = '//button[@id="alertButton"]'
ID_ALERT_BUTTON_WITCH_APPEAR_AFTER = '//button[@id="timerAlertButton"]'
ID_ALERT_BUTTON_WITCH_CONFIRM_BOX = '//button[@id="confirmButton"]'
ID_ALERT_BUTTON_WITCH_PROMPT_BOX = '//button[@id="promtButton"]'
GET_CONFIRM_RESULT_TEXT = '//span[@id="confirmResult"]'
GET_PROMPT_RESULT_TEXT = '//span[@id="promptResult"]'


class AlertsPage(BasePage):

    def open_alerts_page(self):
        return self.open_page(LINK)

    def wait_while_loaded_alerts_page(self):
        self.wait_presence_of_element_located(
            (By.XPATH, WAIT_WHILE_LOAD_IN_ALERT_PAGE))

    def check_is_displayed_alerts_button(self):
        element = self.base_element.find_element_(
            By.XPATH, DISPLAYED_ALERT_BUTTON)
        return self.base_element.check_is_displayed(element)

    def check_is_displayed_prompt_text(self):
        time_displayed_prompt_text = 1
        try:
            self.browser.implicitly_wait(time_displayed_prompt_text)
            element = self.base_element.find_element_(
                By.XPATH, GET_PROMPT_RESULT_TEXT)
            self.base_element.check_is_displayed(element)
        except NoSuchElementException:
            return False
        return True


    def click_alert_button(self):
        return self.click_element(By.XPATH, ID_ALERT_BUTTON)

    def click_alert_button_witch_appear_after_5_seconds(self):
        return self.click_element(
            By.XPATH, ID_ALERT_BUTTON_WITCH_APPEAR_AFTER)

    def click_alert_button_witch_confirm_box(self):
        return self.click_element(
            By.XPATH, ID_ALERT_BUTTON_WITCH_CONFIRM_BOX)

    def click_alert_button_witch_prompt_box(self):
        return self.click_element(
            By.XPATH, ID_ALERT_BUTTON_WITCH_PROMPT_BOX)


    def get_confirm_result_text(self):
        return self.get_text(By.XPATH, GET_CONFIRM_RESULT_TEXT)

    def get_prompt_result_text(self):
        return self.get_text(By.XPATH, GET_PROMPT_RESULT_TEXT)


    def get_alert_text(self):
        return Alert(self.browser).text

    def enter_text_in_alert_prompt(self):
        return Alert(self.browser).send_keys("User")


    def wait_while_alert_is_present(self):
        return WebDriverWait(self.browser, TIME_DEFAULT).until(
                EC.alert_is_present(),
                'Timed out waiting for PA creation'
                'confirmation popup to appear.')

    def alert_click_ok(self):
        try:
            self.wait_while_alert_is_present()
            self.browser.switch_to.alert.accept()
        except TimeoutException:
            raise Exception('No alert!!')

    def alert_click_cancel(self):
        try:
            self.wait_while_alert_is_present()
            self.browser.switch_to.alert.dismiss()
        except TimeoutException:
            raise Exception('No alert!!')
