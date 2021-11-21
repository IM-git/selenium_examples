from .BasePage import BasePage


class MainPage(BasePage):

    LINK = "https://demoqa.com/"

    def open_demoqa(self):
        self.open_page(self.LINK)
