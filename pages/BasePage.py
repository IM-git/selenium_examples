from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys
from elements.BaseElements import BaseElements
from locators.Base import Base


class BasePage:

    def __init__(self, browser, config):
        self.config = config
        self.browser = browser
        self.base_element = BaseElements()

    def open_page(self, link):
        self.browser.get(link)

    def get_title(self):
        return self.browser.title

    def get_current_url(self):
        return self.browser.current_url

    def go_back(self):
        return self.browser.back()

    def refresh_page(self):
        return self.browser.refresh()

    def wait_element_to_be_clickable(self, element):
        return WebDriverWait(self.browser, Base.TIME).until(
            EC.element_to_be_clickable(element))

    def wait_presence_of_element_located(self, element):
        return WebDriverWait(self.browser, Base.TIME).until(
            EC.presence_of_element_located(element))

    def _implicitly_wait(self, time):
        return self.browser.implicitly_wait(time)

    def get_text(self, locator, element):
        return self.base_element.get_text_(
            self.base_element.find_element_(self.browser, locator, element))

    def enter_text(self, locator, element):
        value = self.base_element.find_element_(
            self.browser, locator, element)
        return value.send_keys()

    def click_element(self, locator, element):
        return self.base_element.click_(
            self.base_element.find_element_(self.browser, locator, element))

    def check_is_displayed(self, browser, locator, element):
        return BaseElements.find_element_(browser, locator, element).is_displayed()
