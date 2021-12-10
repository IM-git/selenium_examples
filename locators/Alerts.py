from tools.RandomName import RandomName

class Alerts:
    TIME_DEFAULT = 10
    LINK = 'https://demoqa.com/alerts'
    WAIT_WHILE_LOAD_IN_ALERT_PAGE = '//div[@class="body-height"]'
    DISPLAYED_ALERT_BUTTON = '//button[@id="alertButton"]'
    ID_ALERT_BUTTON = '//button[@id="alertButton"]'
    ID_ALERT_BUTTON_WITCH_APPEAR_AFTER = '//button[@id="timerAlertButton"]'
    ID_ALERT_BUTTON_WITCH_CONFIRM_BOX = '//button[@id="confirmButton"]'
    ID_ALERT_BUTTON_WITCH_PROMPT_BOX = '//button[@id="promtButton"]'
    GET_CONFIRM_RESULT_TEXT = '//span[@id="confirmResult"]'
    GET_PROMPT_RESULT_TEXT = '//span[@id="promptResult"]'
    WAY = 'tools/data_names.json'
    ENTER_NAME_IN_ALERT_PROMPT = RandomName.random_name(WAY)
