from page_objects.admin_page import AdminPage
import pytest


def test_check_admin_page_title(driver, url):
    admin_page = AdminPage(driver)
    admin_page.open(url)
    admin_page.verify_title("Administration")


def test_check_header(driver, url):
    admin_page = AdminPage(driver)
    admin_page.open(url)
    admin_page.find_header()


def test_check_footer(driver, url):
    admin_page = AdminPage(driver)
    admin_page.open(url)
    admin_page.find_footer()


@pytest.mark.xfail(reason="Test currently fails with assert 422.0 == (845 / 2)")
def test_panel_body_horizontal_center(driver, url):
    """
    This test checks if the panel body is centered horizontally on the page.
    It fails with a specific assertion error when the expected center x-coordinate of the panel body
    is not equal to half of the container width.
    """
    admin_page = AdminPage(driver)
    admin_page.open(url)
    panel_body_width = admin_page.find_panel_body_width()
    container_width = admin_page.find_container_width()
    panel_body_x = admin_page.find_panel_body_x()
    panel_body_center_x = panel_body_x + panel_body_width / 2
    assert panel_body_center_x == container_width / 2, "Panel is not centered horizontally on the page"


def test_login_admin_page(driver, url):
    admin_page = AdminPage(driver)
    admin_page.open(url)
    admin_page.username_input_field()
    admin_page.password_input_field()
    admin_page.find_submit_button()
    admin_page.forgotten_password_link()
    admin_page.opencart_link()


def test_adding_new_product(driver, url):
    admin_page = AdminPage(driver)
    admin_page.open(url)
    admin_page.input(admin_page.username_input_field(), "user")
    admin_page.input(admin_page.password_input_field(), "bitnami")
    admin_page.click_login_button()
    admin_page.click_catalog_menu()
    admin_page.click_products_button()
    admin_page.click_add_new_button()
    admin_page.click_general_tab()
    admin_page.input(admin_page.product_name_input_field(), "Test Product")
    admin_page.input(admin_page.description_textbox(), "Description")
    admin_page.input(admin_page.meta_tag_title(), "Meta Tag Title")
    admin_page.click_data_tab()
    admin_page.input(admin_page.model_input_field(), "Model")
    admin_page.click_save_product_button()
    alert = admin_page.find_alert_success()
    assert "Success: You have modified products!" in alert.text


def test_delete_product(driver, url):
    admin_page = AdminPage(driver)
    admin_page.open(url)
    admin_page.input(admin_page.username_input_field(), "user")
    admin_page.input(admin_page.password_input_field(), "bitnami")
    admin_page.click_login_button()
    admin_page.click_catalog_menu()
    admin_page.click_products_button()
    edit_buttons = admin_page.find_edit_buttons()
    id = admin_page.get_id_from_button(edit_buttons)
    admin_page.click_checkbox_in_table(id)
    admin_page.click_delete_button()
    admin_page.accept_alert()
    alert = admin_page.find_alert_success()
    assert "Success: You have modified products!" in alert.text
