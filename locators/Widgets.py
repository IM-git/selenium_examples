from selenium.webdriver.common.by import By


class Widgets:
    LINK_SLIDER = 'https://demoqa.com/slider'
    LINK_PROGRESS_BAR = 'https://demoqa.com/progress-bar'
    INPUT_SLIDER = (By.XPATH, '//input[@class="range-slider range-slider--primary"]')
    VALUE_SLIDER = (By.XPATH, '//input[@id="sliderValue"]')
    PROGRESS_BAR_START_STOP_BUTTON = (By.XPATH, '//button[@id="startStopButton"]')
    PROGRESS_BAR_RESET_BUTTON = (By.XPATH, '//button[@id="resetButton"]')
    VALUE_PROGRESS_BAR = (By.XPATH, '//div[@class="progress-bar bg-info"]')
    VALUE_PERCENT = 7
