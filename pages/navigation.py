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
    _settings_btn = "//div[@kp-icon-svg='settings']"
    _users_page_link = "//a[@ui-sref='org.users']"

    def openUserSettings(self):
        self.elementClick(self._user_settings)

    def openUserPage(self):
        self.elementClick(self._settings_btn)
        self.elementClick(self._users_page_link)
