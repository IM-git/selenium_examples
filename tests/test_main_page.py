from pages import MainPage
from selenium.webdriver.common.by import By
from locators import Main


def test_main_page(browser, config):
    main_page = MainPage(browser, config)
    open_site_demoqa = main_page.open_page(Main.LINK)
    get_title_demoqa = main_page.get_title()
    wait_while_open_demoqa = main_page.wait_presence_of_element_located(
        (By.XPATH, Main.ELEMENT_IMG))
    check_is_displayed_element_img = main_page.check_is_displayed_img(
        browser, By.XPATH, Main.ELEMENT_IMG)

    assert get_title_demoqa == "ToolsQA", "Another page is opened!"
    assert check_is_displayed_element_img == True, "The page is not loaded!"
