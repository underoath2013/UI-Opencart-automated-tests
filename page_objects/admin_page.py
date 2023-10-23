from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class AdminPage(BasePage):
    PATH = "/admin"
    USERNAME_INPUT = (By.CSS_SELECTOR, "#input-username")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#input-password")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    LOGOUT_BUTTON = (By.CSS_SELECTOR, 'a[href*="/admin/index.php?route=common/logout"]')
    OPENCART_LINK = (By.XPATH, "//*[text()='OpenCart']")
    FORGOTTEN_PASSWORD = (By.LINK_TEXT, "Forgotten Password")
    HEADER = (By.CSS_SELECTOR, "#header")
    FOOTER = (By.CSS_SELECTOR, "#footer")
    PANEL_BODY_CENTERED = (By.CSS_SELECTOR, ".col-sm-offset-4.col-sm-4 .panel-body")
    BOOTSTRAP_CONTAINER_FLUID = (By.CSS_SELECTOR, ".container-fluid")
    CATALOG_MENU = (By.CSS_SELECTOR, '#menu-catalog > a[data-toggle="collapse"]')
    PRODUCTS_BUTTON = (By.CSS_SELECTOR, 'a[href*="/admin/index.php?route=catalog/product"]')
    ADD_NEW_BUTTON = (By.CSS_SELECTOR, 'a[href*="/admin/index.php?route=catalog/product/add"]')
    GENERAL_TAB = (By.CSS_SELECTOR, "a[href='#tab-general']")
    DATA_TAB = (By.CSS_SELECTOR, "a[href='#tab-data']")
    PRODUCT_NAME_INPUT = (By.CSS_SELECTOR, '#input-name1')
    DESCRIPTION_TEXTBOX = (By.CSS_SELECTOR, "div[role='textbox']")
    META_TAG_TITLE_INPUT = (By.CSS_SELECTOR, "#input-meta-title1")
    MODEL_INPUT = (By.CSS_SELECTOR, "#input-model")
    SAVE_PRODUCT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    SUCCES_ALERT = (By.CSS_SELECTOR, "div.alert.alert-success")
    EDIT_BUTTON = (By.CSS_SELECTOR, 'a[href*="admin/index.php?route=catalog/product/edit"]')
    DELETE_BUTTON = (By.XPATH, "//button[@class='btn btn-danger']")

    def open(self, url):
        self.open_url(url + self.PATH)

    def find_header(self):
        self.element(AdminPage.HEADER)

    def find_footer(self):
        self.element(AdminPage.FOOTER)

    def find_panel_body_width(self):
        panel_body_width = self.element(AdminPage.PANEL_BODY_CENTERED).size["width"]
        return panel_body_width

    def find_panel_body_x(self):
        panel_body_x = self.element(AdminPage.PANEL_BODY_CENTERED).location["x"]
        return panel_body_x

    def find_container_width(self):
        container_width = self.element(AdminPage.BOOTSTRAP_CONTAINER_FLUID).size["width"]
        return container_width

    def username_input_field(self):
        return self.element(AdminPage.USERNAME_INPUT)

    def password_input_field(self):
        return self.element(AdminPage.PASSWORD_INPUT)

    def find_submit_button(self):
        self.element(AdminPage.SUBMIT_BUTTON)

    def forgotten_password_link(self):
        self.element(AdminPage.FORGOTTEN_PASSWORD)

    def opencart_link(self):
        self.element(AdminPage.OPENCART_LINK)

    def click_login_button(self):
        self.click(self.element(AdminPage.SUBMIT_BUTTON))

    def click_catalog_menu(self):
        self.click(self.element(AdminPage.CATALOG_MENU))

    def click_logout_button(self):
        self.click(self.element(AdminPage.LOGOUT_BUTTON))

    def click_products_button(self):
        self.click(self.element(AdminPage.PRODUCTS_BUTTON))

    def click_add_new_button(self):
        self.click(self.element(AdminPage.ADD_NEW_BUTTON))

    def click_general_tab(self):
        self.click(self.element(AdminPage.GENERAL_TAB))

    def product_name_input_field(self):
        return self.element(AdminPage.PRODUCT_NAME_INPUT)

    def description_textbox(self):
        return self.element(AdminPage.DESCRIPTION_TEXTBOX)

    def meta_tag_title(self):
        return self.element(AdminPage.META_TAG_TITLE_INPUT)

    def click_data_tab(self):
        self.click(self.element(AdminPage.DATA_TAB))

    def model_input_field(self):
        return self.element(AdminPage.MODEL_INPUT)

    def click_save_product_button(self):
        self.click(self.element(AdminPage.SAVE_PRODUCT_BUTTON))

    def find_alert_success(self):
        return self.element(AdminPage.SUCCES_ALERT)

    def find_edit_buttons(self):
        return self.elements(AdminPage.EDIT_BUTTON)

    def get_id_from_button(self, edit_buttons) -> str:
        button_url = edit_buttons[0].get_attribute('href')
        start_index = button_url.find("product_id=")
        value_after_id = button_url[start_index + len("product_id="):]
        return value_after_id

    def click_checkbox_in_table(self, id):
        checkbox = f"input[value='{id}']"
        checkbox_locator = (By.CSS_SELECTOR, checkbox)
        self.click(self.element(checkbox_locator))

    def click_delete_button(self):
        self.click(self.element(AdminPage.DELETE_BUTTON))
