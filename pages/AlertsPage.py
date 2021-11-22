from .BasePage import BasePage
from selenium.webdriver.common.by import By


LINK = 'https://demoqa.com/'
ALERT_BUTTON = '//h5[text()="Alerts, Frame & Windows"]'
CHECK_CLASS_ELEMENT = '//div[@class="element-list collapse show"]'
CLICK_CLASS_ELEMENT = '//h5[text()="Alerts, Frame & Windows"]//preceding::div[@class="card-up"][3]'


class AlertsPage(BasePage):

    def open_main_page(self):
        return self.open_page(LINK)

    def click_alert_button(self):
        return self.click_element(By.XPATH, CLICK_CLASS_ELEMENT)

    def wait_while_open_alerts_windows_page(self):
        self.wait_presence_of_element_located((By.XPATH, CHECK_CLASS_ELEMENT))

    def check_is_displayed_alerts_listbox(self):
        element = self.base_element.find_element_(By.XPATH, CHECK_CLASS_ELEMENT)
        return self.base_element.check_is_displayed(element)
