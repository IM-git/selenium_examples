from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class MouseKeyboardActions:

    def __init__(self, browser):
        self.browser = browser

    def move_to_element(self, element):
        return webdriver.ActionChains(self.browser).move_to_element(element).perform()

    def one_click(self, value):
        return webdriver.ActionChains(self.browser).click(value)

    def double_click(self, value):
        return webdriver.ActionChains(self.browser).double_click(value).perform()

    def select_all_text(self, element):     # triple click
        return webdriver.ActionChains(self.browser).double_click(element).click()

    def enter_text(self, text):
        return webdriver.ActionChains(self.browser).send_keys(text)

    def delete_text(self, element):
        return element.send_keys(Keys.DELETE).perform()

    def click_arrow_up(self):
        return webdriver.ActionChains(self.browser).send_keys(Keys.ARROW_UP)

    def do_key_down(self):
        return webdriver.ActionChains(self.browser).key_down(Keys.SHIFT)

    def perform_(self, value):
        return value.perform()
