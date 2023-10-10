import os
import logging
import datetime
from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import FirefoxOptions, ChromeOptions


class Logger:
    def __init__(self, test_name, log_level):
        self.logger = logging.getLogger(test_name)
        self.logger.setLevel(log_level)
        formatter = logging.Formatter('%(levelname)s %(message)s')

        if not os.path.exists("logs"):
            os.makedirs("logs")
        log_file = os.path.join("logs", f"{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}_{test_name}.log")
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

    def info(self, message):
        self.logger.info(message)

    def error(self, message):
        self.logger.error(message)


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome", help="Available browsers: firefox, chrome")
    parser.addoption("--url", default="http://192.168.0.109:8081", help="Base URL for the tests")
    parser.addoption("--maximize", action="store_true", help="Maximize browser window")
    parser.addoption("--headless", action="store_true", help="Headless mode")
    parser.addoption("--log_level", choices=["INFO", "ERROR"],
                     default="INFO", help="Set the log level (INFO, ERROR)")
    parser.addoption("--remote", action="store_true", help="Run tests remotely using Selenoid")
    parser.addoption("--bv", help="Browser version")
    parser.addoption("--remote_url", default="http://selenoid:4444/wd/hub",
                     help="Remote URL for Selenoid's command_executor")


@pytest.fixture
def url(request):
    return request.config.getoption("--url")


@pytest.fixture
def driver(request):
    browser_name = request.config.getoption("--browser")
    browser_version = request.config.getoption("--bv")
    maximize = request.config.getoption("--maximize")
    headless = request.config.getoption("--headless")
    log_level = request.config.getoption("--log_level")
    remote = request.config.getoption("--remote")
    remote_url = request.config.getoption("--remote_url")

    logger = Logger(request.node.name, log_level)
    logger.info("===> Test %s started at %s" %
                (request.node.name, datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')))

    # local execution
    if not remote:
        if browser_name == "firefox":
            options = FirefoxOptions()
            if headless:
                options.headless = True
            driver = webdriver.Firefox(options=options)
        elif browser_name == "chrome":
            service = Service()
            options = ChromeOptions()
            if headless:
                options.add_argument("headless=new")
            driver = webdriver.Chrome(service=service, options=options)
        else:
            raise ValueError(f"Driver {browser_name} not supported")

    # remote execution with Selenoid
    if remote:
        if browser_name == "firefox":
            options = FirefoxOptions()
            options.browser_version = browser_version
            if headless:
                options.headless = True
            driver = webdriver.Remote(
                command_executor=remote_url,
                options=options
            )
        elif browser_name == "chrome":
            options = ChromeOptions()
            options.browser_version = browser_version
            if headless:
                options.add_argument("headless=new")
            driver = webdriver.Remote(
                command_executor=remote_url,
                options=options
            )

    if maximize:
        driver.maximize_window()

    driver.logger = logger

    logger.info(f"Browser {browser_name} started")

    yield driver

    driver.quit()
    logger.info("===> Test %s finished at %s\n" %
                (request.node.name, datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')))
