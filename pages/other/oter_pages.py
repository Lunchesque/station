import logging
from utilities.util import Util
from base.basepage import BasePage
import utilities.custom_logger as cl
from pages.navigation import NavigationPage

class OtherPages(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.nav.NavigationPage(driver)
        self.util = Util()


    # locators
    _username_field = "//input[contains(@class, 'login-name')]"
    _password_field = "//input[contains(@class, 'login-password')]"
    _login_btn = "//input[@type='submit']"
    _logout_btn = "//a[@ng-click='logout()']"

    def getToGmail(self, gmailUrl):
        self.goToUrl(gmail)

    def enterGmailEmail(self, gemail):
        self.sendKeys(gemail, self._acc_email)

    def submitAccEmail(self):
        self.elementClick(self._email_submit_btn)

    def enterGmailPassword(self, passwordGmail):
        self.sendKeys(passwordGmail, self._acc_password)

    def submitPassword(self):
        self.elementClick(self._pass_submit_btn)

    def getUserPassword(self):
        self.getText(self._password_element)

    def getStation(self, stationUrl):
        self.goToUrl(stationUrl)

    def enterEmail(self, email):
        self.elementClear(self._username_field)
        self.sendKeys(self.getUserPassword(), self._username_field)

    def enterPassword(self, password):
        self.elementClear(self._password_field)
        self.sendKeys(password, self._password_field)

    def clickLoginBtn(self):
        self.elementClick(self._login_btn)
