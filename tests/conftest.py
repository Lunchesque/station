import pytest
from selenium import webdriver
from pages.login.login_page import LoginPage
from base.webdriverfactory import WebDriverFactory
from ddt import ddt, data, unpack
from utilities.read_data import getCSVData

@pytest.fixture()
def setUp():
    print("Running conftest demo setUp")
    yield
    print("Running conftest demo tearDown")

@pytest.fixture(scope="class")
def oneTimeSetUp(request, browser, osType):
    print("Running conftest demo oneTimeSetUp")
    wdf = WebDriverFactory(browser)
    driver = wdf.getWebDriverInstance()
    lp = LoginPage(driver)
    lp.login("sergey.verkhovodko@synesis.ru", "admADM1/")

    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    driver.quit()
    print("Running conftest demo oneTimeTearDown")

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="type of OS")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")
