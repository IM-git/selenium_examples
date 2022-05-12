from selenium.webdriver.common.by import By


class Alerts:
    TIME_DEFAULT = 10
    LINK = 'https://demoqa.com/alerts'
    WAIT_WHILE_LOAD_IN_ALERT_PAGE = (By.XPATH, '//div[@class="body-height"]')
    DISPLAYED_ALERT_BUTTON = (By.XPATH, '//button[@id="alertButton"]')
    ID_ALERT_BUTTON = (By.XPATH, '//button[@id="alertButton"]')
    ID_ALERT_BUTTON_WITCH_APPEAR_AFTER = (By.XPATH, '//button[@id="timerAlertButton"]')
    ID_ALERT_BUTTON_WITCH_CONFIRM_BOX = (By.XPATH, '//button[@id="confirmButton"]')
    ID_ALERT_BUTTON_WITCH_PROMPT_BOX = (By.XPATH, '//button[@id="promtButton"]')
    GET_CONFIRM_RESULT_TEXT = (By.XPATH, '//span[@id="confirmResult"]')
    GET_PROMPT_RESULT_TEXT = (By.XPATH, '//span[@id="promptResult"]')
    WAY = 'tools/data_names.json'
