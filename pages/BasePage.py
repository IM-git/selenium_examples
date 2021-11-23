from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from elements.BaseElements import BaseElements


TIME = 10


class BasePage:

    def __init__(self, browser, config):
        self.config = config
        self.browser = browser
        self.base_element = BaseElements(self.browser)

    def open_page(self, link):
        self.browser.get(link)

    def get_title(self):
        return self.browser.title

    def get_current_url(self):
        return self.browser.current_url

    def go_back(self):
        return self.browser.back()

    def wait_element_to_be_clickable(self, element):
        return WebDriverWait(self.browser, TIME).until(
            EC.element_to_be_clickable(element))

    def wait_presence_of_element_located(self, element):
        return WebDriverWait(self.browser, TIME).until(
            EC.presence_of_element_located(element))

    def get_text(self, locator, element):
        return self.base_element.get_text_(
            self.base_element.find_element_(locator, element))

    def click_element(self, locator, element):
        return self.base_element.click_(
            self.base_element.find_element_(locator, element))

    # def click_element(self, locator, element):
    #     return BaseElements(self.browser).click_(BaseElements(self.browser).find_element_(locator, element))

    # @staticmethod
    # def findfind(browser, locator, element):    # Вариант что бы не оправлять в BaseElement browser а делать все здесь
    #     return browser.BaseElements().find_element_(locator, element)
