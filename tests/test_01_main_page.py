from page_objects.main_page import MainPage


def test_check_main_page_title(driver, url):
    main_page = MainPage(driver)
    main_page.open_url(url)
    main_page.verify_title("Your Store")


def test_check_logo(driver, url):
    main_page = MainPage(driver)
    main_page.open_url(url)
    main_page.find_logo()


def test_items_navigation_bar(driver, url):
    expected_navigation_bar_items = ["Desktops", "Laptops & Notebooks", "Components",
                                     "Tablets", "Software", "Phones & PDAs", "Cameras", "MP3 Players"]
    main_page = MainPage(driver)
    main_page.open_url(url)
    navigation_bar = main_page.find_navigation_bar()
    navigation_bar_items_text = main_page.find_navigation_bar_items_text(navigation_bar)
    assert len(navigation_bar) == 8, "Wrong items quantity in navigation bar"
    assert navigation_bar_items_text == expected_navigation_bar_items, f"Unexpected item in navigation bar"


def test_search_field_button(driver, url):
    search_input = "Macbook"
    main_page = MainPage(driver)
    main_page.open_url(url)
    search_field = main_page.find_search_input_field()
    main_page.input(search_field, search_input)
    main_page.click_search_button()
    main_page.title_contains(search_input)


def test_featured_items(driver, url):
    expected_featured_item_titles = ['MacBook', 'iPhone', 'Apple Cinema 30"', 'Canon EOS 5D']
    main_page = MainPage(driver)
    main_page.open_url(url)
    featured_items = main_page.find_featured_items()
    item_title = main_page.find_featured_item_titles(featured_items)
    assert len(featured_items) == 4, f"Expected 4 items in 'Featured', but found {len(featured_items)}"
    assert item_title in expected_featured_item_titles, f"Unexpected item in featured: {item_title}"


def test_switch_to_euro_currency(driver, url):
    main_page = MainPage(driver)
    main_page.open_url(url)
    main_page.find_dropdown_button()
    main_page.click_dropdown_button()
    main_page.click_euro_button()
    currency_symbol = main_page.find_currency_symbol_text()
    assert currency_symbol == '€', f"Wrong currency symbol: {currency_symbol}"


def test_switch_to_pound_currency(driver, url):
    main_page = MainPage(driver)
    main_page.open_url(url)
    main_page.find_dropdown_button()
    main_page.click_dropdown_button()
    main_page.click_pound_button()
    currency_symbol = main_page.find_currency_symbol_text()
    assert currency_symbol == '£', f"Wrong currency symbol: {currency_symbol}"


def test_switch_to_dollar_currency(driver, url):
    main_page = MainPage(driver)
    main_page.open_url(url)
    main_page.find_dropdown_button()
    main_page.click_dropdown_button()
    main_page.click_dollar_button()
    currency_symbol = main_page.find_currency_symbol_text()
    assert currency_symbol == '$', f"Wrong currency symbol: {currency_symbol}"
