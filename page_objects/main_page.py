from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage
from typing import List


class MainPage(BasePage):
    SEARCH_INPUT = (By.CSS_SELECTOR, '#search input[name="search"]')
    SEARCH_BUTTON = (By.CSS_SELECTOR, '#search button[type="button"]')
    LOGO = (By.CSS_SELECTOR, '#logo a img')
    NAVIGATION_BAR = (By.CSS_SELECTOR, 'ul.navbar-nav > li')
    FEATURED = (By.CSS_SELECTOR, '.row .product-layout')
    DROPDOWN_BUTTON = (By.XPATH, "//button[contains(@class, 'dropdown-toggle')]")
    DROPDOWN_LIST = (By.CLASS_NAME, "dropdown-menu")
    EURO_BUTTON = (By.XPATH, "//button[@name='EUR']")
    DOLLAR_BUTTON = (By.XPATH, "//button[@name='USD']")
    POUND_BUTTON = (By.XPATH, "//button[@name='GBP']")
    CURRENCY_SYMBOL = (By.CSS_SELECTOR, "strong")

    def find_logo(self):
        self.element(MainPage.LOGO)

    def find_navigation_bar(self):
        return self.elements(MainPage.NAVIGATION_BAR)

    def find_navigation_bar_items_text(self, navigation_bar) -> List[str]:
        items_text = [element.text for element in navigation_bar]
        return items_text

    def find_search_input_field(self):
        return self.element(MainPage.SEARCH_INPUT)

    def click_search_button(self):
        self.click(self.element(MainPage.SEARCH_BUTTON))

    def find_featured_items(self):
        return self.elements(MainPage.FEATURED)

    def find_featured_item_titles(self, featured_items):
        for item in featured_items:
            return item.find_element(By.TAG_NAME, "h4").find_element(By.TAG_NAME, "a").text

    def find_dropdown_button(self):
        return self.elements_presence(MainPage.DROPDOWN_BUTTON)

    def click_dropdown_button(self):
        self.click(self.element(MainPage.DROPDOWN_BUTTON))

    def click_euro_button(self):
        self.click(self.element(MainPage.EURO_BUTTON))

    def click_dollar_button(self):
        self.click(self.element(MainPage.DOLLAR_BUTTON))

    def click_pound_button(self):
        self.click(self.element(MainPage.POUND_BUTTON))

    def find_currency_symbol_text(self):
        return self.element(MainPage.CURRENCY_SYMBOL).text
