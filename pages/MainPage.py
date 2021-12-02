from .BasePage import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):

    def check_is_displayed_img(self, browser, locator, element):
        return self.base_element.check_is_displayed_2_0(browser, locator, element)
