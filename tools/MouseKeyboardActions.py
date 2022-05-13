from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class MouseKeyboardActions:

    def __init__(self, browser):
        self.__browser = browser

    def click_arrow_up(self):
        return webdriver.ActionChains(self.__browser).send_keys(Keys.ARROW_UP)

    def click_arrow_down(self):
        return webdriver.ActionChains(self.__browser).\
            send_keys(Keys.ARROW_DOWN).perform()

    def click_enter(self):
        return webdriver.ActionChains(self.__browser).\
            send_keys(Keys.ENTER).perform()

    def click_tab(self):
        return webdriver.ActionChains(self.__browser).\
            send_keys(Keys.TAB).perform()

    @staticmethod
    def delete_text(element):
        return element.send_keys(Keys.DELETE)

    def do_key_down(self):
        return webdriver.ActionChains(self.__browser).key_down(Keys.SHIFT)

    def double_click(self, value):
        return webdriver.ActionChains(
            self.__browser).double_click(value).perform()

    def enter_text(self, text):
        return webdriver.ActionChains(
            self.__browser).send_keys(text).perform()

    def move_to_element(self, element):
        return webdriver.ActionChains(
            self.__browser).move_to_element(element).perform()

    def one_click(self, value):
        return webdriver.ActionChains(self.__browser).click(value).perform()

    def right_click(self, value):
        return webdriver.ActionChains(self.__browser).\
            context_click(value).perform()

    def select_all_text(self, element):     # triple click
        return webdriver.ActionChains(self.__browser).\
            double_click(element).click().perform()
