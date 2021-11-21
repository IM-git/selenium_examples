class BasePage:
    def __init__(self, browser, config):
        self.config = config
        self.browser = browser

    def open_page(self, link):
        self.browser.get(link)

    def get_title(self):
        return self.browser.title
