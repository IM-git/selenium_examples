import os

from src.enums import PracticeFormPageError
from pages import BasePage
from locators import PracticeForm

from tools.allure_screenshot import taking_screenshot
from tools.CheckingDateBirth import CheckingDateBirth
from tools.MouseKeyboardActions import MouseKeyboardActions
from tools import Logger


class PracticeFormPage(BasePage):

    def __init__(self, *args, **kwargs):
        super(PracticeFormPage, self).__init__(*args, **kwargs)
        self.mouse_keyboard_actions = MouseKeyboardActions(self.browser)

    def checks_attribute_was_validated(self):
        value = self.get_attribute(*PracticeForm.USER_FORM, 'class')
        assert value == "was-validated",\
            (PracticeFormPageError.WRONG_GET_ATTRIBUTE.value,
             taking_screenshot(self.browser))

    def checks_is_displayed_modal_body(self):
        self.check_is_displayed(*PracticeForm.DIV_MODAL_BODY)

    def checks_is_displayed_practice_form_page(self):
        self.check_is_displayed(*PracticeForm.ID_BUTTON_SUBMIT)

    def checks_subject_text_values(self):
        value = self.get_text(*PracticeForm.ID_SUBJECT_CONTAINER)
        assert PracticeForm.SUBJECTS == value.split('\n'),\
            f'{PracticeForm.SUBJECTS} ' \
            f'{PracticeFormPageError.WRONG_PRACTICE_FORM_SUBJECT.value}'

    def choice_gender(self):
        self.click_value(*PracticeForm.VALUE_GENDER)

    def click_hobbies(self, *elements):
        for locator, element in elements:
            self.click_value(locator, element)

    def choice_hobbies(self):
        self.click_hobbies(*PracticeForm.LIST_ID_HOBBIES)

    def click_arrow_down(self):
        Logger.Logger().info(f"Click arrow down.")
        self.mouse_keyboard_actions.click_arrow_down()

    def click_value(self, locator, element):
        Logger.Logger().info(f"Click value(Element: {element}).")
        value = self.base_element.find_element(self.browser, locator, element)
        self.mouse_keyboard_actions.one_click(value)

    def click_submit(self):
        self.click_value(*PracticeForm.ID_SUBMIT)

    def enter_city(self):
        self.enter_place(*PracticeForm.DIV_SELECT_CITY, PracticeForm.CITY)

    def enter_current_address(self):
        self.enter_path(*PracticeForm.ID_CURRENT_ADDRESS,
                        PracticeForm.TEXT_CURRENT_ADDRESS)

    def enter_date_of_birth(self):
        Logger.Logger().info(
            f"Enter date of birth(date: {PracticeForm.DATE_OF_BIRTH}).")
        __minimum_age = 10
        CheckingDateBirth().compare_date(
            PracticeForm.DATE_OF_BIRTH, __minimum_age)
        value = self.base_element.find_element(self.browser,
                                               *PracticeForm.ID_DATE_OF_BIRTH)
        self.base_element.click(self.browser, *PracticeForm.ID_DATE_OF_BIRTH)
        self.mouse_keyboard_actions.select_all_text(value)
        self.mouse_keyboard_actions.enter_text(PracticeForm.DATE_OF_BIRTH)

    def enter_email(self):
        self.enter_value(*PracticeForm.ID_EMAIL, PracticeForm.EMAIL)

    def enter_first_name(self):
        self.enter_value(*PracticeForm.ID_FIRST_NAME, PracticeForm.FIRST_NAME)

    def enter_image(self):
        self.enter_path(*PracticeForm.ID_CHOICE_IMG,
                        (os.getcwd() + PracticeForm.PATH_TO_IMG))

    def enter_last_name(self):
        self.enter_value(*PracticeForm.ID_LAST_NAME, PracticeForm.LAST_NAME)

    def enter_mobile_number(self):
        self.enter_value(*PracticeForm.ID_MOBILE_NUMBER,
                         PracticeForm.MOBILE_NUMBER)

    def enter_path(self, locator, element, path):
        Logger.Logger().info(f"Enter path: {path}.")
        value = self.base_element.find_element(self.browser, locator, element)
        value.send_keys(path)

    def enter_place(self, locator, element, place):
        Logger.Logger().info(f"Enter place: {place}.")
        value = self.base_element.find_element(self.browser, locator, element)
        self.wait_element_to_be_clickable(value)
        self.base_element.click(self.browser, locator, element)
        self.mouse_keyboard_actions.enter_text(place)
        self.mouse_keyboard_actions.click_enter()

    def enter_value(self, locator, element, name):
        Logger.Logger().info(
            f"Enter value(Element: {element}, name: {name}).")
        self.base_element.click(self.browser, locator, element)
        self.mouse_keyboard_actions.enter_text(name)

    def enter_subjects(self):
        Logger.Logger().info(
            f"Enter subject(subject: {PracticeForm.SUBJECTS}).")
        value = self.base_element.find_element(self.browser,
                                               *PracticeForm.ID_SUBJECT)
        self.wait_element_to_be_clickable(value)
        for subject in PracticeForm.SUBJECTS:
            self.base_element.click(self.browser, *PracticeForm.ID_SUBJECT)
            self.mouse_keyboard_actions.enter_text(subject)
            self.wait_element_to_be_clickable(value)
            self.mouse_keyboard_actions.click_tab()
        self.mouse_keyboard_actions.click_tab()

    def enter_state(self):
        value = self.base_element.find_element(self.browser,
                                               *PracticeForm.DIV_SELECT_STATE)
        self.wait_element_to_be_clickable(value)
        self.enter_place(*PracticeForm.DIV_SELECT_STATE, PracticeForm.STATE)

    def scroll_down(self):
        for _ in range(PracticeForm.SCROLL_STEPS):
            self.click_arrow_down()
