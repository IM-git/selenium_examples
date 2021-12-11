import os
from selenium import webdriver
from pages import BasePage
from tools.CheckingDateBirth import CheckingDateBirth
from tools.ChoiceHobbies import ChoiceHobbies
from selenium.webdriver.common.by import By
from tools.MouseKeyboardActions import MouseKeyboardActions
from tools import Logger


class PracticeFormPage(BasePage):

# ENTER VALUES
    def enter_value(self, browser, locator, element, name):
        Logger.Logger().info(f"Enter value(Element: {element}, name: {name}).")
        value = self.base_element._find_element(
            browser, locator, element)
        click = self.base_element._click(value)
        MouseKeyboardActions()._enter_text(browser, name)

    def enter_date_of_birth(self, browser, locator, element, date):
        Logger.Logger().info(f"Enter date of birth(Element: {element}, date: {date}).")
        CheckingDateBirth()
        value = self.base_element._find_element(
            browser, locator, element)
        click = self.base_element._click(value)
        double_click = MouseKeyboardActions().\
            _select_all_text(browser, value)
        MouseKeyboardActions()._enter_text(browser, date)

    def enter_subject(self, browser, locator, element, subject):
        Logger.Logger().info(f"Enter subject(Element: {element}, subject: {subject}).")
        value = self.base_element._find_element(browser, locator, element)
        self.wait_element_to_be_clickable(browser, value)
        click = self.base_element._click(value)
        MouseKeyboardActions()._enter_text(browser, subject)
        self.wait_element_to_be_clickable(browser, value)
        MouseKeyboardActions()._click_tab(browser)

    def enter_path(self, browser, locator, element, path):
        Logger.Logger().info(f"Enter path: {path}.")
        value = self.base_element._find_element(browser, locator, element)
        value.send_keys(path)

    def enter_place(self, browser, locator, element, place):
        Logger.Logger().info(f"Enter place: {place}.")
        value = self.base_element._find_element(browser, locator, element)
        self.wait_element_to_be_clickable(browser, value)
        click = self.base_element._click(value)
        MouseKeyboardActions()._enter_text(browser, place)
        MouseKeyboardActions()._click_enter(browser)

# MAKE CHOICE
    def click_value(self, browser, locator, element):
        Logger.Logger().info(f"Click value(Element: {element}).")
        value_ = self.base_element._find_element(browser, locator, element)
        MouseKeyboardActions()._one_click(browser, value_)

    def click_arrow_down(self, browser):
        Logger.Logger().info(f"Click arrow down.")
        return MouseKeyboardActions()._click_arrow_down(browser)

# CLICK HOBBIES
    def click_hobbies(self, browser, locator, elements):
        for element in elements:
            self.click_value(browser, locator, element)
