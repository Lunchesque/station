import logging
import utilities.custom_logger as cl
from base.basepage import BasePage

#pytest -s -v tests/home/login_test.py


class NavigationPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #locators
    _user_settings = "//*[contains(@ng-if, 'current.user.avatar')]"

    def openUserSettings(self):
        self.elementClick(self._user_settings)
