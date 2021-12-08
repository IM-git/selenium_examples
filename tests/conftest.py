import pytest
from patterns.Factory import Factory
from tools.read_file import read_file


IMPLICITLY_WAIT_TIME = 10


@pytest.fixture(scope='session')
def browser():
    driver = Factory().get_browser()
    driver.implicitly_wait(IMPLICITLY_WAIT_TIME)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope='session')
def config():
    data = read_file('tests/config.json')
    return data
