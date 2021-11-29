import os
from selenium import webdriver
from pages import BasePage
from tools.CheckingDateBirth import CheckingDateBirth
from tools.ChoiceHobbies import ChoiceHobbies
from tools.ChoiceGender import ChoiceGender
from selenium.webdriver.common.by import By
from tools.MouseKeyboardActions import MouseKeyboardActions


LINK_PRACTICE_FORM_PAGE = 'https://demoqa.com/automation-practice-form'
ID_BUTTON_SUBMIT = '//button[@id="submit"]'
FIRST_NAME = 'User'
LAST_NAME = 'Userkov'
EMAIL = 'example@email.com'
MOBILE_NUMBER = '1234567890'
DATE_OF_BIRTH = '11 Nov 2011'
SUBJECTS_COMPUTER_SCIENCE = 'Computer Science'
SUBJECTS_ENGLISH = 'English'
PATH_TO_IMG = r"\img.png"
TEXT_CURRENT_ADDRESS = '890 Fifth Avenue, Manhattan, New York.'
STATE = 'Haryana'
CITY = 'Panipat'
ID_FIRST_NAME = '//input[@id="firstName"]'
ID_LAST_NAME = '//input[@id="lastName"]'
ID_EMAIL = '//input[@id="userEmail"]'
ID_GENDER_OTHER = '//input[@id="gender-radio-3"]'
ID_MOBILE_NUMBER = '//input[@id="userNumber"]'
ID_DATE_OF_BIRTH = '//input[@id="dateOfBirthInput"]'
ID_SUBJECT = '//input[@id="subjectsInput"]'
ID_HOBIE_SPORTS = '//input[@id="hobbies-checkbox-1"]'
ID_HOBIE_READING = '//input[@id="hobbies-checkbox-2"]'
ID_HOBIE_MUSIC = '//input[@id="hobbies-checkbox-3"]'
ID_CHOICE_IMG = '//input[@id="uploadPicture"]'
ID_CURRENT_ADDRESS = '//textarea[@id="currentAddress"]'
DIV_SELECT_STATE = '//div[@id="state"]'
DIV_SELECT_CITY = '//div[@id="city"]'
ID_SUBMIT = '//button[@id="submit"]'
DIV_MODAL_BODY = '//div[@class="modal-body"]'


class PracticeFormPage(BasePage):

    def open_practice_form_page(self):
        return self.open_page(LINK_PRACTICE_FORM_PAGE)

    def check_is_displayed_practice_form_page(self):
        element = self.base_element.find_element_(
            self.browser, By.XPATH, ID_BUTTON_SUBMIT)
        return self.base_element.check_is_displayed(element)

    def check_is_displayed_modal_body(self):
        element = self.base_element.find_element_(
            self.browser, By.XPATH, DIV_MODAL_BODY)
        return self.base_element.check_is_displayed(element)

# ENTER VALUES
    def enter_first_name(self):
        value = self.base_element.find_element_(
            self.browser, By.XPATH, ID_FIRST_NAME)
        click = self.base_element.click_(value)
        MouseKeyboardActions(self.browser).enter_text(FIRST_NAME)

    def enter_last_name(self):
        value = self.base_element.find_element_(
            self.browser, By.XPATH, ID_LAST_NAME)
        click = self.base_element.click_(value)
        MouseKeyboardActions(self.browser).enter_text(LAST_NAME)

    def enter_email(self):
        value = self.base_element.find_element_(
            self.browser, By.XPATH, ID_EMAIL)
        click = self.base_element.click_(value)
        MouseKeyboardActions(self.browser).enter_text(EMAIL)

    def enter_mobile_number(self):
        value = self.base_element.find_element_(
            self.browser, By.XPATH, ID_MOBILE_NUMBER)
        click = self.base_element.click_(value)
        MouseKeyboardActions(self.browser).enter_text(MOBILE_NUMBER)

    def enter_date_of_birth(self):
        CheckingDateBirth()
        value = self.base_element.find_element_(
            self.browser, By.XPATH, ID_DATE_OF_BIRTH)
        click = self.base_element.click_(value)
        double_click = MouseKeyboardActions(self.browser).\
            select_all_text(value)
        MouseKeyboardActions(self.browser).enter_text(DATE_OF_BIRTH)

    def enter_subject(self):
        value = self.base_element.find_element_(
            self.browser, By.XPATH, ID_SUBJECT)
        click = self.base_element.click_(value)
        MouseKeyboardActions(self.browser).enter_text(
            SUBJECTS_COMPUTER_SCIENCE)
        MouseKeyboardActions(self.browser).click_tab()
        MouseKeyboardActions(self.browser).enter_text(SUBJECTS_ENGLISH)

    def enter_image(self):
        value = self.base_element.find_element_(
            self.browser, By.XPATH, ID_CHOICE_IMG)
        value.send_keys(os.getcwd() + PATH_TO_IMG)

    def enter_current_address(self):
        value = self.base_element.find_element_(
            self.browser, By.XPATH, ID_CURRENT_ADDRESS)
        value.send_keys(TEXT_CURRENT_ADDRESS)

    def enter_state(self):
        value = self.base_element.find_element_(
            self.browser, By.XPATH, DIV_SELECT_STATE)
        self.wait_element_to_be_clickable(value)
        click = self.base_element.click_(value)
        MouseKeyboardActions(self.browser).enter_text(STATE)
        MouseKeyboardActions(self.browser).click_enter()

    def enter_city(self):
        value = self.base_element.find_element_(
            self.browser, By.XPATH, DIV_SELECT_CITY)
        self.wait_element_to_be_clickable(value)
        click = self.base_element.click_(value)
        MouseKeyboardActions(self.browser).enter_text(CITY)
        MouseKeyboardActions(self.browser).click_enter()

# MAKE CHOICE
    def choice_gender(self):
        ChoiceGender()
        value = self.base_element.find_element_(
            self.browser, By.XPATH, ID_GENDER_OTHER)
        MouseKeyboardActions(self.browser).one_click(value)

    def choice_hobbies(self):
        ChoiceHobbies()
        value = self.base_element.find_element_(
            self.browser, By.XPATH, ID_HOBIE_READING)
        MouseKeyboardActions(self.browser).one_click(value)
        value = self.base_element.find_element_(
            self.browser, By.XPATH, ID_HOBIE_MUSIC)
        MouseKeyboardActions(self.browser).one_click(value)

    def click_arrow_down(self):
        return MouseKeyboardActions(self.browser).click_arrow_down()

    def click_submit(self):
        value = self.base_element.find_element_(
            self.browser, By.XPATH, ID_SUBMIT)
        MouseKeyboardActions(self.browser).one_click(value)
