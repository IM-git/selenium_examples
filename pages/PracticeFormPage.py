import os
from selenium import webdriver
from pages import BasePage
from tools.CheckingDateBirth import CheckingDateBirth
from tools.ChoiceHobbies import ChoiceHobbies
from tools.ChoiceGender import ChoiceGender
from selenium.webdriver.common.by import By
from tools.MouseKeyboardActions import MouseKeyboardActions


class PracticeFormPage(BasePage):

    def check_is_displayed_value(self, browser, locator, element):
        return self.base_element.check_is_displayed_2_0(
            browser, locator, element)

# ENTER VALUES
    def enter_value(self, browser, locator, element, name):
        value = self.base_element.find_element_(
            browser, locator, element)
        click = self.base_element.click_(value)
        MouseKeyboardActions(browser).enter_text(name)

    def enter_date_of_birth(self, browser, locator, element, date):
        CheckingDateBirth()
        value = self.base_element.find_element_(
            browser, locator, element)
        click = self.base_element.click_(value)
        double_click = MouseKeyboardActions(browser).\
            select_all_text(value)
        MouseKeyboardActions(browser).enter_text(date)

    def enter_subject(self, browser, locator, element, subject):
        value = self.base_element.find_element_(browser, locator, element)
        click = self.base_element.click_(value)
        MouseKeyboardActions(browser).enter_text(subject)
        MouseKeyboardActions(browser).click_tab()

    def enter_path(self, browser, locator, element, path):
        value = self.base_element.find_element_(browser, locator, element)
        value.send_keys(path)

    def enter_place(self, browser, locator, element, place):
        value = self.base_element.find_element_(browser, locator, element)
        self.wait_element_to_be_clickable(value)
        click = self.base_element.click_(value)
        MouseKeyboardActions(browser).enter_text(place)
        MouseKeyboardActions(browser).click_enter()

# MAKE CHOICE
    def click_value(self, browser, locator, element):
        value_ = self.base_element.find_element_(browser, locator, element)
        MouseKeyboardActions(browser).one_click(value_)

    def click_arrow_down(self, browser):
        return MouseKeyboardActions(browser).click_arrow_down()
