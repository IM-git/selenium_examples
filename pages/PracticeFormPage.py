import os
from selenium import webdriver
from pages import BasePage
from tools.CheckingDateBirth import CheckingDateBirth
from tools.ChoiceHobbies import ChoiceHobbies
from tools.ChoiceGender import ChoiceGender
from selenium.webdriver.common.by import By
from tools.MouseKeyboardActions import MouseKeyboardActions


class PracticeFormPage(BasePage):

# ENTER VALUES
    def enter_value(self, browser, locator, element, name):
        value = self.base_element._find_element(
            browser, locator, element)
        click = self.base_element._click(value)
        MouseKeyboardActions()._enter_text(browser, name)

    def enter_date_of_birth(self, browser, locator, element, date):
        CheckingDateBirth()
        value = self.base_element._find_element(
            browser, locator, element)
        click = self.base_element._click(value)
        double_click = MouseKeyboardActions().\
            _select_all_text(browser, value)
        MouseKeyboardActions()._enter_text(browser, date)

    def enter_subject(self, browser, locator, element, subject):
        value = self.base_element._find_element(browser, locator, element)
        self.wait_element_to_be_clickable(browser, value)
        click = self.base_element._click(value)
        MouseKeyboardActions()._enter_text(browser, subject)
        self.wait_element_to_be_clickable(browser, value)
        MouseKeyboardActions()._click_tab(browser)

    def enter_path(self, browser, locator, element, path):
        value = self.base_element._find_element(browser, locator, element)
        value.send_keys(path)

    def enter_place(self, browser, locator, element, place):
        value = self.base_element._find_element(browser, locator, element)
        self.wait_element_to_be_clickable(browser, value)
        click = self.base_element._click(value)
        MouseKeyboardActions()._enter_text(browser, place)
        MouseKeyboardActions()._click_enter(browser)

# MAKE CHOICE
    def click_value(self, browser, locator, element):
        value_ = self.base_element._find_element(browser, locator, element)
        MouseKeyboardActions()._one_click(browser, value_)

    def click_arrow_down(self, browser):
        return MouseKeyboardActions()._click_arrow_down(browser)
