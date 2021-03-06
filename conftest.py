import pytest
from pages.login.login_page import LoginPage
from base.webdriverfactory import WebDriverFactory

@pytest.fixture()
def setUp():
    print("Running conftest setUp")
    yield
    print("Running conftest tearDown")

@pytest.fixture(scope="class")
def oneTimeSetUp(request, browser, osType):
    print("Running conftest oneTimeSetUp")
    wdf = WebDriverFactory(browser)
    driver = wdf.getWebDriverInstance()
    lp = LoginPage(driver)
    lp.login("sergey.verkhovodko@synesis.ru", "admADM1/")

    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    driver.quit()
    print("Running conftest oneTimeTearDown")

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="type of OS")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")
