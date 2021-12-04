from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys
from elements.BaseElements import BaseElements
from locators.Base import Base


class BasePage:

    def __init__(self):
        self.base_element = BaseElements()

    def open_page(self, browser, link):
        browser.get(link)

    def get_title(self, browser):
        return browser.title

    def get_current_url(self, browser):
        return browser.current_url

    def go_back(self, browser):
        return browser.back()

    def refresh_page(self, browser):
        return browser.refresh()

    def wait_element_to_be_clickable(self, browser, element):
        return WebDriverWait(browser, Base.TIME).until(
            EC.element_to_be_clickable(element))

    def wait_presence_of_element_located(self, browser, element):
        return WebDriverWait(browser, Base.TIME).until(
            EC.presence_of_element_located(element))

    def _implicitly_wait(self, browser, time):
        return browser.implicitly_wait(time)

    def get_text(self, browser, locator, element):
        return self.base_element._get_text(
            self.base_element._find_element(browser, locator, element))

    def enter_text(self, browser, locator, element):
        value = self.base_element._find_element(
            browser, locator, element)
        return value.send_keys()

    def click_element(self, browser, locator, element):
        return self.base_element._click(
            self.base_element._find_element(browser, locator, element))

    # def check_is_displayed(self, browser, locator, element):
    #     return BaseElements._find_element(browser, locator, element).is_displayed()

    def check_is_displayed(self, browser, locator, element):
        __implicitly_wait_time = 1
        browser.implicitly_wait(__implicitly_wait_time)
        try:
            BaseElements._find_element(browser, locator, element).is_displayed()
        except NoSuchElementException:
            return False
        return True
