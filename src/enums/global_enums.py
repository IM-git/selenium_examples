from enum import Enum


class GlobalErrorMessages(Enum):
    WRONG_STATUS_CODE = 'Received status code is not equal to expected!!'
    WRONG_TITLE_PAGE = 'Another page is opened!!'
    WRONG_IS_DISPLAYED = 'The page is not loaded!!'


class AlertsError(Enum):
    WRONG_ALERT_TEXT = 'Alert not displayed!!'
    WRONG_CONFIRM_RESULT_TEXT_OK = 'The answer does not match after clicking "Ok"!!'
    WRONG_CONFIRM_RESULT_TEXT_CANCEL = 'The answer does not match after clicking "Cancel"!!'


class ButtonsError(Enum):
    WRONG_ANSWER_AFTER_DOUBLE_CLICK = 'The answer does not match after double click!!'
    WRONG_ANSWER_AFTER_RIGHT_CLICK = 'The answer does not match after right click!!'


class PracticeFormPageError(Enum):
    WRONG_DISPLAYED_MODAL_BODY = 'The modal body is not loaded!!'
    WRONG_GET_ATTRIBUTE = 'Submit button is not pushed!!'
    WRONG_PRACTICE_FORM_SUBJECT = ' are not added in form!!'
    WRONG_SUBJECT_TEXT = 'Some text exist!!'


class WidgetsPageError(Enum):
    WRONG_DID_RANDOM_STEPS = 'The steps which were did is not match the displayed value steps on the page!!'
    WRONG_ENTERED_VALUE_IN_PAGE = 'Entered value is not match with value in the page!!'
