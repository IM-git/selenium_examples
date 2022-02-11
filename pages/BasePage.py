from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys
from elements.BaseElements import BaseElements
from locators.Base import Base
from tools import Logger as Logger


class BasePage:

    def __init__(self):
        self.base_element = BaseElements()

    def open_page(self, browser, link):
        Logger.Logger().info(f"Open page: {link}.")
        browser.get(link)

    def get_title(self, browser):
        Logger.Logger().info(f"Get title: {browser.title}.")
        return browser.title

    def get_current_url(self, browser):
        Logger.Logger().info(f"Get current url: {browser.current_url}.")
        return browser.current_url

    def go_back(self, browser):
        Logger.Logger().info(f"Go to back.")
        return browser.back()

    def refresh_page(self, browser):
        Logger.Logger().info(f"Refresh page.")
        return browser.refresh()

    def wait_element_to_be_clickable(self, browser, element):
        Logger.Logger().info(f"Wait element to be clickable(Element: {element}).")
        return WebDriverWait(browser, Base.TIME).until(
            EC.element_to_be_clickable(element))

    def wait_presence_of_element_located(self, browser, element):
        Logger.Logger().info(f"Wait presence of element located(Element: {element}).")
        return WebDriverWait(browser, Base.TIME).until(
            EC.presence_of_element_located(element))

    def _implicitly_wait(self, browser, time):
        Logger.Logger().info(f"Implicitly wait(Time: {time}).")
        return browser.implicitly_wait(time)

    def get_text(self, browser, locator, element):
        Logger.Logger().info(f"Get text from element: {element}.")
        return self.base_element._get_text(
            self.base_element._find_element(browser, locator, element))

    def enter_text(self, browser, locator, element):
        Logger.Logger().info(f"Enter text from element: {element}.")
        value = self.base_element._find_element(
            browser, locator, element)
        return value.send_keys()

    def click_element(self, browser, locator, element):
        Logger.Logger().info(f"Click element: {element}.")
        return self.base_element._click(
            self.base_element._find_element(browser, locator, element))

    def check_is_displayed(self, browser, locator, element):
        Logger.Logger().info(f"Check is displayed element: {element}.")
        __implicitly_wait_time = 1
        browser.implicitly_wait(__implicitly_wait_time)
        try:
            BaseElements._find_element(browser, locator, element).\
                is_displayed()
        except NoSuchElementException:
            return False
        return True

    def get_attribute(self, browser, locator, element, attribute):
        Logger.Logger().info(f"Get attribute from element(Element: {element}, attribute: {attribute}).")
        elements = self.base_element._find_element(
            browser, locator, element)
        return self.base_element._get_to_attribute(elements, attribute)
