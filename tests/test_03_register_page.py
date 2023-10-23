from page_objects.register_page import RegisterPage


def test_check_register_page_title(driver, url):
    register_page = RegisterPage(driver)
    register_page.open(url)
    register_page.verify_title("Register Account")


def test_input_field_firstname(driver, url):
    register_page = RegisterPage(driver)
    register_page.open(url)
    assert "First Name" == register_page.firstname_input_field()


def test_input_field_lastname(driver, url):
    register_page = RegisterPage(driver)
    register_page.open(url)
    assert "Last Name" == register_page.lastname_input_field()


def test_input_field_email(driver, url):
    register_page = RegisterPage(driver)
    register_page.open(url)
    assert "E-Mail" == register_page.email_input_field()


def test_input_field_telephone(driver, url):
    register_page = RegisterPage(driver)
    register_page.open(url)
    assert "Telephone" == register_page.telephone_input_field()


def test_input_field_password(driver, url):
    register_page = RegisterPage(driver)
    register_page.open(url)
    assert "Password" == register_page.password_input_field()


def test_input_field_password_confirm(driver, url):
    register_page = RegisterPage(driver)
    register_page.open(url)
    assert "Password Confirm" == register_page.password_confirm_input_field()


def test_register_new_user(driver, url):
    register_page = RegisterPage(driver)
    register_page.open(url)
    register_page.input(register_page.find_firstname_input(), "Ivan")
    register_page.input(register_page.find_lastname_input(), "Ivanov")
    register_page.input(register_page.find_email_input(), "123@gmail.com")
    register_page.input(register_page.find_telephone_input(), "+79991234567")
    register_page.input(register_page.find_password_input(), "qwerty")
    register_page.input(register_page.find_password_confirm_input(), "qwerty")
    register_page.confirm_privacy_policy()
    register_page.click_continue_button()
    assert register_page.find_created_account_text() == "Your Account Has Been Created!"
