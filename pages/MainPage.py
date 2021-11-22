from .BasePage import BasePage
from selenium.webdriver.common.by import By


LINK = 'https://demoqa.com/'
ELEMENT_IMG = '//img[@alt="Selenium Online Training"]'


class MainPage(BasePage):

    def open_demoqa(self):
        self.open_page(LINK)

    def wait_while_open_demoqa(self):
        self.wait_presence_of_element_located((By.XPATH, ELEMENT_IMG))

    def check_is_displayed_img(self):
        element = self.base_element.find_element_(By.XPATH, ELEMENT_IMG)
        return self.base_element.check_is_displayed(element)
