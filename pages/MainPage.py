from .BasePage import BasePage

from locators import Main


class MainPage(BasePage):

    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

    def checks_is_displayed_element_img(self):
        self.check_is_displayed(*Main.ELEMENT_IMG)

    def wait_while_open_demoqa(self):
        self.wait_presence_of_element_located(Main.ELEMENT_IMG)
