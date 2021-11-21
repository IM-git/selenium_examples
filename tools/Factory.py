from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from tools import read_file


class Factory:

    @staticmethod
    def get_browser():
        config = Factory.config()
        if config['browser'] == 'chrome':
            return Factory.chrome_browser()
        elif config['browser'] == 'firefox':
            return Factory.firefox_browser()
        else:
            raise Exception(f' We are not use the "{Factory.config_browser}".')

    @staticmethod
    def config():
        data = read_file.read_file('tests/config.json')
        return data

    @staticmethod
    def chrome_browser():
        driver = webdriver.Chrome(ChromeDriverManager().install())
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