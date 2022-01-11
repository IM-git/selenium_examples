import requests
from locators import Main
from src.enums import GlobalErrorMessages
from tools import Logger


# @Logger.logger.catch()
def test_main_page():
    page_response = requests.get(url=Main.LINK)

    assert page_response.status_code == 200, \
        GlobalErrorMessages.WRONG_STATUS_CODE.value
