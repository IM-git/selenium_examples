from tools.ChoiceGender import ChoiceGender
from tools.ChoiceHobbies import ChoiceHobbies
from tools.ChoiceSubjects import ChoiceSubjects


class PracticeForm:
    LINK_PRACTICE_FORM_PAGE = 'https://demoqa.com/automation-practice-form'
    ID_BUTTON_SUBMIT = '//button[@id="submit"]'
    FIRST_NAME = 'User'
    LAST_NAME = 'Userkov'
    EMAIL = 'example@email.com'
    MOBILE_NUMBER = '1234567890'
    DATE_OF_BIRTH = '11 Nov 2011'
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
    ID_FIRST_NAME = '//input[@id="firstName"]'
    ID_LAST_NAME = '//input[@id="lastName"]'
    ID_EMAIL = '//input[@id="userEmail"]'
    ID_GENDER_MALE = '//input[@id="gender-radio-1"]'
    ID_GENDER_FEMALE = '//input[@id="gender-radio-2"]'
    ID_GENDER_OTHER = '//input[@id="gender-radio-3"]'
    VALUE_GENDER = ChoiceGender.get_random_gender()
    ID_MOBILE_NUMBER = '//input[@id="userNumber"]'
    ID_DATE_OF_BIRTH = '//input[@id="dateOfBirthInput"]'
    ID_SUBJECT = '//input[@id="subjectsInput"]'
    ID_SUBJECT_CONTAINER = '//div[@id="subjectsContainer"]'
    # ID_SUBJECT = '//div[contains(@class,"subjects-auto-complete__control")]'
    ID_HOBBY_SPORTS = '//input[@id="hobbies-checkbox-1"]'
    ID_HOBBY_READING = '//input[@id="hobbies-checkbox-2"]'
    ID_HOBBY_MUSIC = '//input[@id="hobbies-checkbox-3"]'
    LIST_ID_HOBBIES = ChoiceHobbies().get_hobbies()
    ID_CHOICE_IMG = '//input[@id="uploadPicture"]'
    ID_CURRENT_ADDRESS = '//textarea[@id="currentAddress"]'
    DIV_SELECT_STATE = '//div[@id="state"]'
    DIV_SELECT_CITY = '//div[@id="city"]'
    ID_SUBMIT = '//button[@id="submit"]'
    DIV_MODAL_BODY = '//div[@class="modal-body"]'
    MODAL_CONTENT = '//div[@class="modal-content"]'
    USER_FORM = '//form[@id="userForm"]'
