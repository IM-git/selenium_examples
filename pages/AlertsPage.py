from .BasePage import BasePage
from selenium.webdriver.common.by import By


LINK = 'https://demoqa.com/alerts'
WAIT_WHILE_LOAD_IN_ALERT_PAGE = '//div[@class="body-height"]'
DISPLAYED_ALERT_BUTTON = '//button[@id="alertButton"]'


class AlertsPage(BasePage):

    def open_alerts_page(self):
        return self.open_page(LINK)

    def click_alert_button(self):
        return self.click_element(By.XPATH, '')

    def wait_while_loaded_alerts_page(self):
        self.wait_presence_of_element_located((By.XPATH, WAIT_WHILE_LOAD_IN_ALERT_PAGE))

    def check_is_displayed_alerts_button(self):
        element = self.base_element.find_element_(By.XPATH, DISPLAYED_ALERT_BUTTON)
        return self.base_element.check_is_displayed(element)
