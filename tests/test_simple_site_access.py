import allure
import requests
from locators import Main
from src.enums import GlobalErrorMessages
from tools import Logger


@allure.feature("Main page.")
# @Logger.logger.catch()
def test_main_page():
    """Checking only page responses: '200'."""
    page_response = requests.get(url=Main.LINK)

    assert page_response.status_code == 200, \
        GlobalErrorMessages.WRONG_STATUS_CODE.value
