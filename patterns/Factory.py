from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


class Factory:

    @staticmethod
    def get_browser(configuration):
        config = configuration
        if config['browser'] == 'chrome':
            return Factory.chrome_browser()
        elif config['browser'] == 'firefox':
            return Factory.firefox_browser()
        else:
            raise Exception(f' We are not use the "{Factory.config_browser(config)}".')

    @staticmethod
    def chrome_browser():
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        return driver

    @staticmethod
    def firefox_browser():
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        return driver

    @staticmethod
    def config_browser(config):
        if 'browser' not in config:
            print('The config file does not contain "browser"')
        elif config['browser'] not in ['chrome', 'firefox']:
            print(f' We are not use the "{config["browser"]}".')
        return config['browser']
