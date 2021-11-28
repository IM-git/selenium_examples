from pages import BasePage
from selenium.webdriver.common.by import By
from tools.MouseKeyboardActions import MouseKeyboardActions


LINK_PRACTICE_FORM_PAGE = 'https://demoqa.com/automation-practice-form'
ID_BUTTON_SUBMIT = '//button[@id="submit"]'
FIRST_NAME = 'User'
LAST_NAME = 'Userkov'
ID_FIRST_NAME = '//input[@id="firstName"]'
ID_LAST_NAME = '//input[@id="lastName"]'

class PracticeFormPage(BasePage):

    def open_practice_form_page(self):
        return self.open_page(LINK_PRACTICE_FORM_PAGE)

    def check_is_displayed_practice_form_page(self):
        element = self.base_element.find_element_(
            self.browser, By.XPATH, ID_BUTTON_SUBMIT)
        return self.base_element.check_is_displayed(element)

    def enter_first_name(self):
        value = self.base_element.find_element_(self.browser, By.XPATH, ID_FIRST_NAME)
        click = self.base_element.click_(value)
        MouseKeyboardActions(self.browser).enter_text(FIRST_NAME)

    def enter_last_name(self):
        value = self.base_element.find_element_(self.browser, By.XPATH, ID_LAST_NAME)
        click = self.base_element.click_(value)
        MouseKeyboardActions(self.browser).enter_text(LAST_NAME)

