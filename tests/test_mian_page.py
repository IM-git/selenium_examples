from pages.MainPage import MainPage


def test_main_page(browser, config):
    main_page = MainPage(browser, config)
    main_page.open_demoqa()
    title = main_page.get_title()
    print(f'\n###Title: {title}###')
    assert title == "ToolsQA", "Another page is opened!"
