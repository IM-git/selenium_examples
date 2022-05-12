import allure
from allure_commons.types import AttachmentType


class AllureScreenshot:

    @staticmethod
    def make_screenshot(driver):
        with allure.step("Make screenshot"):
            allure.attach(driver.get_screenshot_as_png(), name='Screenshot',
                          attachment_type=AttachmentType.PNG)


def taking_screenshot(browser):
    AllureScreenshot().make_screenshot(browser)
