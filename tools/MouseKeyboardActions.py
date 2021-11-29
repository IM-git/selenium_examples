from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class MouseKeyboardActions:

    def __init__(self, browser):
        self.browser = browser

    def move_to_element(self, element):
        return webdriver.ActionChains(self.browser).\
            move_to_element(element).perform()

    def one_click(self, value):
        return webdriver.ActionChains(self.browser).\
            click(value).perform()

    def double_click(self, value):
        return webdriver.ActionChains(self.browser).\
            double_click(value).perform()

    def right_click(self, value):
        return webdriver.ActionChains(self.browser).\
            context_click(value).perform()

    def select_all_text(self, element):     # triple click
        return webdriver.ActionChains(self.browser).\
            double_click(element).click().perform()

    def enter_text(self, text):
        return webdriver.ActionChains(self.browser).send_keys(text).perform()

    def delete_text(self, element):
        return element.send_keys(Keys.DELETE)

    def click_arrow_up(self):
        return webdriver.ActionChains(self.browser).send_keys(Keys.ARROW_UP)

    def click_arrow_down(self):
        return webdriver.ActionChains(self.browser).\
            send_keys(Keys.ARROW_DOWN).perform()

    def click_enter(self):
        return webdriver.ActionChains(self.browser).\
            send_keys(Keys.ENTER).perform()

    def click_tab(self):
        return webdriver.ActionChains(self.browser).\
            send_keys(Keys.TAB).perform()

    def do_key_down(self):
        return webdriver.ActionChains(self.browser).key_down(Keys.SHIFT)

    def perform_(self, value):
        return value.perform()
