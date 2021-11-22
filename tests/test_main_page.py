from pages import MainPage


def test_main_page(browser, config):
    main_page = MainPage(browser, config)
    open_site_demoqa = main_page.open_demoqa()
    get_title_demoqa = main_page.get_title()
    wait_while_open_demoqa = main_page.wait_while_open_demoqa()
    check_is_displayed_element_img = main_page.check_is_displayed_img()

    assert get_title_demoqa == "ToolsQA", "Another page is opened!"
    assert check_is_displayed_element_img == True, "The page is not loaded!"
