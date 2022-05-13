from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import requests

from elements.BaseElements import BaseElements
from locators.Base import Base
from tools import Logger as Log
from tools.allure_screenshot import taking_screenshot
from src.enums import GlobalErrorMessages, AlertsError


class BasePage:

    def __init__(self, browser: object = None, url: str = None):
        self.browser = browser
        self.__url = url
        self.base_element = BaseElements()
        self.time = Base.TIME

    def open_page(self):
        Log.Logger().info(f"Open page: {self.__url}.")
        self.browser.get(self.__url)

    def checks_title(self):
        title = self.browser.title
        assert title == "ToolsQA",\
            (GlobalErrorMessages.WRONG_TITLE_PAGE.value,
             taking_screenshot(self.browser))

    def get_current_url(self):
        return self.browser.current_url

    def get_text(self, locator, element):
        Log.Logger().info(f"Get text from element: {element}.")
        return self.base_element.get_text(self.browser, locator, element)

    def enter_text(self, locator, element):
        Log.Logger().info(f"Enter text from element: {element}.")
        value = self.base_element.find_element(self.browser, locator, element)
        value.send_keys()

    def click_element(self, locator, element):
        Log.Logger().info(f"Click element: {element}.")
        self.base_element.click(self.browser, locator, element)

    def check_is_displayed(self, locator, element):
        Log.Logger().info(f"Check is displayed element: {element}.")
        # self.browser.implicitly_wait(10)
        value = BaseElements.find_element(
            self.browser, locator, element).is_displayed()
        assert value is True,\
            (GlobalErrorMessages.WRONG_IS_DISPLAYED.value,
             taking_screenshot(self.browser))

    def get_attribute(self, locator, element, attribute):
        Log.Logger().info(f"Get attribute from element(Element: {element},"
                          f"attribute: {attribute}).")
        return self.base_element.get_to_attribute(
            self.browser, locator, element, attribute)

    def page_response(self):
        response = requests.get(self.__url)
        assert response.status_code == 200,\
            GlobalErrorMessages.WRONG_STATUS_CODE.value

    def wait_element_to_be_clickable(self, element):
        Log.Logger().info(f"Wait element to be clickable.")
        WebDriverWait(self.browser, self.time).until(
            EC.element_to_be_clickable(element))

    def wait_presence_of_element_located(self, element):
        Log.Logger().info(f"Wait presence of element located.")
        WebDriverWait(self.browser, self.time).until(
            EC.presence_of_element_located(element))
