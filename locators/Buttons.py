from selenium.webdriver.common.by import By


class Buttons:
    LINK = 'https://demoqa.com/buttons'
    BUTTON_DOUBLE_CLICK_ME = (By.XPATH, '//button[@id="doubleClickBtn"]')
    GET_DOUBLE_CLICK_RESULT_TEXT = (By.XPATH, '//p[@id="doubleClickMessage"]')
    BUTTON_RIGHT_CLICK = (By.XPATH, '//button[@id="rightClickBtn"]')
    GET_RIGHT_CLICK_RESULT_TEXT = (By.XPATH, '//p[@id="rightClickMessage"]')
    BUTTON_CLICK = (By.XPATH, '//button[text()="Click Me"]')
    GET_CLICK_RESULT_TEXT = (By.XPATH, '//p[@id="dynamicClickMessage"]')
