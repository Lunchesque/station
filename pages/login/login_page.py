import logging
import utilities.custom_logger as cl
from base.basepage import BasePage
from utilities.util import Util
from pages.navigation import NavigationPage


class LoginPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.nav = NavigationPage(driver)
        self.util = Util()

    #locators
    _username_field = "//input[contains(@class, 'login-name')]"
    _password_field = "//input[contains(@class, 'login-password')]"
    _login_btn = "//input[@type='submit']"
    _logout_btn = "//a[@ng-click='logout()']"

    def enterEmail(self, email):
        self.elementClear(self._username_field)
        self.sendKeys(email, self._username_field)

    def enterPassword(self, password):
        self.elementClear(self._password_field)
        self.sendKeys(password,self. _password_field)

    def clickLoginBtn(self):
        self.elementClick(self._login_btn)

    def login(self, email="", password=""):
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginBtn()
        self.util.sleep(2)

    def logout(self):
        self.nav.openUserSettings()
        self.elementClick(self._logout_btn)
