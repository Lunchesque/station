import logging
from utilities.util import Util
from base.basepage import BasePage
import utilities.custom_logger as cl
from pages.navigation import NavigationPage


class LoginPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.nav = NavigationPage(driver)
        self.util = Util()

    #locators
    _adm_login_locators1 = "//li/a[@href='#']"
    _adm_login_locators2 = "//img[@class='brand-img']"
    _adm_login_locators3 = "//img[@ng-if='current.user.avatar']"
    _adm_login_locators4 = "//a[@kp-icon-svg='attention']"
    _adm_login_locators5 = "//a[@kp-icon-svg='globe']"
    _adm_login_locators6 = "//div[@class='btn btn-default navbar-btn dropdown-toggle']"
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

    def verifyAdmLogin(self):
        res1 = self.elementPresenceCheck(self._adm_login_locators1)
        res2 = self.elementPresenceCheck(self._adm_login_locators2)
        res3 = self.elementPresenceCheck(self._adm_login_locators3)
        res4 = self.elementPresenceCheck(self._adm_login_locators4)
        res5 = self.elementPresenceCheck(self._adm_login_locators5)
        res6 = self.elementPresenceCheck(self._adm_login_locators6)
        if res1 and res2 and res3 and res4 and res5 and res6 == True:
            return True