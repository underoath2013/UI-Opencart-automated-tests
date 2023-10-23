import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.logger = driver.logger
        self.class_name = type(self).__name__

    @allure.step
    def open_url(self, url):
        self.logger.info("%s: Open url: %s" % (self.class_name, url))
        self.driver.get(url)

    @allure.step
    def click(self, element):
        self.logger.info("%s: Move and click: %s" % (self.class_name, element.tag_name))
        ActionChains(self.driver).move_to_element(element).pause(0.1).click().perform()

    @allure.step
    def input(self, element, value):
        self.click(element)
        element.clear()
        self.logger.info("%s: Input value: %s" % (self.class_name, value))
        element.send_keys(value)

    @allure.step
    def verify_title(self, title):
        self.logger.info("%s: Check for title: %s" % (self.class_name, str(title)))
        try:
            return WebDriverWait(self.driver, 3).until(EC.title_is(title))
        except TimeoutException:
            allure.attach(
                name=f"{self.driver.current_url}",
                body=self.driver.get_screenshot_as_png(),
                attachment_type=allure.attachment_type.PNG
            )
            error = f"Didn't wait for title {title}"
            self.logger.error(error)
            raise AssertionError(error)

    @allure.step
    def element_in_element(self, parent_locator: tuple, child_locator: tuple):
        self.logger.info("%s: Find element %s in %s" % (self.class_name, child_locator, parent_locator))
        return self.element(parent_locator).find_element(*child_locator)

    @allure.step
    def elements_in_element(self, parent_locator: tuple, child_locator: tuple):
        self.logger.info("%s: Find elements %s in %s" % (self.class_name, child_locator, parent_locator))
        return self.element(parent_locator).find_elements(*child_locator)

    @allure.step
    def element(self, locator: tuple):
        self.logger.info("%s: Check if element %s is visible" % (self.class_name, str(locator)))
        try:
            return WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            allure.attach(
                name=f"{self.driver.current_url}",
                body=self.driver.get_screenshot_as_png(),
                attachment_type=allure.attachment_type.PNG
            )
            error = f"Didn't wait for element visibility {locator}"
            self.logger.error(error)
            raise AssertionError(error)

    @allure.step
    def get_placeholder_value(self, element):
        placeholder = element.get_attribute("placeholder")
        self.logger.info("%s: Get placeholder attribute: %s" % (self.class_name, placeholder))
        return placeholder

    @allure.step
    def elements(self, locator: tuple):
        self.logger.info("%s: Check if all elements %s is visible" % (self.class_name, str(locator)))
        try:
            return WebDriverWait(self.driver, 3).until(EC.visibility_of_all_elements_located(locator))
        except TimeoutException:
            allure.attach(
                name=f"{self.driver.current_url}",
                body=self.driver.get_screenshot_as_png(),
                attachment_type=allure.attachment_type.PNG
            )
            error = f"Didn't wait for elements visibility {locator}"
            self.logger.error(error)
            raise AssertionError(error)

    @allure.step
    def verify_product_item(self, product_name):
        self.logger.info("%s: Verify product item: %s" % (self.class_name, product_name))
        return self.element((By.LINK_TEXT, product_name))

    @allure.step
    def title_contains(self, title: str):
        self.logger.info("%s: Check title: %s" % (self.class_name, title))
        try:
            return WebDriverWait(self.driver, 3).until(EC.title_contains(title))
        except TimeoutException:
            allure.attach(
                name=f"{self.driver.current_url}",
                body=self.driver.get_screenshot_as_png(),
                attachment_type=allure.attachment_type.PNG
            )
            error = f"Didn't wait for title {title}"
            self.logger.error(error)
            raise AssertionError(error)

    @allure.step
    def elements_presence(self, locator: tuple):
        self.logger.info("%s: Check if all elements %s is presence" % (self.class_name, locator))
        try:
            return WebDriverWait(self.driver, 3).until(EC.presence_of_all_elements_located(locator))
        except TimeoutException:
            allure.attach(
                name=f"{self.driver.current_url}",
                body=self.driver.get_screenshot_as_png(),
                attachment_type=allure.attachment_type.PNG
            )
            error = f"Didn't wait for elements presense {locator}"
            self.logger.error(error)
            raise AssertionError(error)

    @allure.step
    def accept_alert(self):
        try:
            alert = WebDriverWait(self.driver, 3).until(EC.alert_is_present())
            alert.accept()
            self.logger.info("%s: Accept alert %s" % (self.class_name, alert))
        except TimeoutException:
            allure.attach(
                name=f"{self.driver.current_url}",
                body=self.driver.get_screenshot_as_png(),
                attachment_type=allure.attachment_type.PNG
            )
            error = f"Didn't wait for alert"
            self.logger.error(error)
            raise AssertionError(error)

        # self.driver.switch_to.alert.accept()

    @allure.step
    def cancel_alert(self):
        try:
            alert = WebDriverWait(self.driver, 3).until(EC.alert_is_present())
            alert.dismiss()
            self.logger.info("%s: Dismiss alert %s" % (self.class_name, alert))
        except TimeoutException:
            allure.attach(
                name=f"{self.driver.current_url}",
                body=self.driver.get_screenshot_as_png(),
                attachment_type=allure.attachment_type.PNG
            )
            error = f"Didn't wait for alert"
            self.logger.error(error)
            raise AssertionError(error)
