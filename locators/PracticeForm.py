from selenium.webdriver.common.by import By

from tools.ChoiceGender import ChoiceGender
from tools.ChoiceHobbies import ChoiceHobbies
from tools.ChoiceSubjects import ChoiceSubjects


class PracticeForm:
    LINK_PRACTICE_FORM_PAGE = 'https://demoqa.com/automation-practice-form'
    ID_BUTTON_SUBMIT = (By.XPATH, '//button[@id="submit"]')
    FIRST_NAME = 'User'
    LAST_NAME = 'Userkov'
    EMAIL = 'example@email.com'
    MOBILE_NUMBER = '1234567890'
    DATE_OF_BIRTH = '15 Dec 2011'
    SUBJECTS_COMPUTER_SCIENCE = 'Computer Science'
    SUBJECTS_ENGLISH = 'English'
    SUBJECTS_OLD = ['English', 'Computer Science', 'Chemistry', 'Commerce',
                    'Economics', 'Social Studies', 'Maths', 'Physics', 'Arts',
                    'History', 'Civics']
    SUBJECTS = ChoiceSubjects().list_of_selected_subjects()
    PATH_TO_IMG = r"\img.png"
    TEXT_CURRENT_ADDRESS = '890 Fifth Avenue, Manhattan, New York.'
    STATE = 'Haryana'
    CITY = 'Panipat'
    ID_FIRST_NAME = (By.XPATH, '//input[@id="firstName"]')
    ID_LAST_NAME = (By.XPATH, '//input[@id="lastName"]')
    ID_EMAIL = (By.XPATH, '//input[@id="userEmail"]')
    ID_GENDER_MALE = (By.XPATH, '//input[@id="gender-radio-1"]')
    ID_GENDER_FEMALE = (By.XPATH, '//input[@id="gender-radio-2"]')
    ID_GENDER_OTHER = (By.XPATH, '//input[@id="gender-radio-3"]')
    VALUE_GENDER = ChoiceGender.get_random_gender()
    ID_MOBILE_NUMBER = (By.XPATH, '//input[@id="userNumber"]')
    ID_DATE_OF_BIRTH = (By.XPATH, '//input[@id="dateOfBirthInput"]')
    ID_SUBJECT = (By.XPATH, '//input[@id="subjectsInput"]')
    ID_SUBJECT_CONTAINER = (By.XPATH, '//div[@id="subjectsContainer"]')
    # ID_SUBJECT = '//div[contains(@class,"subjects-auto-complete__control")]'
    ID_HOBBY_SPORTS = (By.XPATH, '//input[@id="hobbies-checkbox-1"]')
    ID_HOBBY_READING = (By.XPATH, '//input[@id="hobbies-checkbox-2"]')
    ID_HOBBY_MUSIC = (By.XPATH, '//input[@id="hobbies-checkbox-3"]')
    LIST_ID_HOBBIES = ChoiceHobbies().get_hobbies()
    ID_CHOICE_IMG = (By.XPATH, '//input[@id="uploadPicture"]')
    ID_CURRENT_ADDRESS = (By.XPATH, '//textarea[@id="currentAddress"]')
    DIV_SELECT_STATE = (By.XPATH, '//div[@id="state"]')
    DIV_SELECT_CITY = (By.XPATH, '//div[@id="city"]')
    ID_SUBMIT = (By.XPATH, '//button[@id="submit"]')
    DIV_MODAL_BODY = (By.XPATH, '//div[@class="modal-body"]')
    MODAL_CONTENT = (By.XPATH, '//div[@class="modal-content"]')
    USER_FORM = (By.XPATH, '//form[@id="userForm"]')
    SCROLL_STEPS = 8
