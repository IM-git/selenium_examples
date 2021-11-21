import pytest
from tools.Factory import Factory
from tools.read_file import read_file


@pytest.fixture(scope='session')
def browser():
    driver = Factory().get_browser()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope='session')
def config():
    data = read_file('tests/config.json')
    return data
