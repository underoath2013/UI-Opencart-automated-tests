from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class RegisterPage(BasePage):
    PATH = "/index.php?route=account/register"
    FIRSTNAME = (By.CSS_SELECTOR, '#input-firstname')
    LASTNAME = (By.CSS_SELECTOR, '#input-lastname')
    EMAIL = (By.CSS_SELECTOR, '#input-email')
    TELEPHONE = (By.CSS_SELECTOR, '#input-telephone')
    PASSWORD = (By.CSS_SELECTOR, '#input-password')
    PASSWORD_CONFIRM = (By.CSS_SELECTOR, '#input-confirm')
    PRIVACY_CHECKBOX = (By.CSS_SELECTOR, "input[value='1'][name='agree']")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "input[value='Continue']")
    CREATED_ACCOUNT_TEXT = (By.XPATH, "//h1[normalize-space()='Your Account Has Been Created!']")

    def open(self, url):
        self.open_url(url + self.PATH)

    def firstname_input_field(self):
        first_name_field = self.element(RegisterPage.FIRSTNAME)
        return self.get_placeholder_value(first_name_field)

    def lastname_input_field(self):
        last_name_field = self.element(RegisterPage.LASTNAME)
        return self.get_placeholder_value(last_name_field)

    def email_input_field(self):
        email_field = self.element(RegisterPage.EMAIL)
        return self.get_placeholder_value(email_field)

    def telephone_input_field(self):
        telephone_field = self.element(RegisterPage.TELEPHONE)
        return self.get_placeholder_value(telephone_field)

    def password_input_field(self):
        password_field = self.element(RegisterPage.PASSWORD)
        return self.get_placeholder_value(password_field)

    def password_confirm_input_field(self):
        password_confirm_field = self.element(RegisterPage.PASSWORD_CONFIRM)
        return self.get_placeholder_value(password_confirm_field)

    def find_firstname_input(self):
        return self.element(RegisterPage.FIRSTNAME)

    def find_lastname_input(self):
        return self.element(RegisterPage.LASTNAME)

    def find_email_input(self):
        return self.element(RegisterPage.EMAIL)

    def find_telephone_input(self):
        return self.element(RegisterPage.TELEPHONE)

    def find_password_input(self):
        return self.element(RegisterPage.PASSWORD)

    def find_password_confirm_input(self):
        return self.element(RegisterPage.PASSWORD_CONFIRM)

    def confirm_privacy_policy(self):
        self.click(self.element(RegisterPage.PRIVACY_CHECKBOX))

    def click_continue_button(self):
        self.click(self.element(RegisterPage.CONTINUE_BUTTON))

    def find_created_account_text(self):
        return self.element(RegisterPage.CREATED_ACCOUNT_TEXT).text
