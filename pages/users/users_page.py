import logging
import utilities.custom_logger as cl
from base.basepage import BasePage
from utilities.util import Util
from pages.navigation import NavigationPage


class UsersPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.nav = NavigationPage(driver)
        self.util = Util()

    #locators
    _adduser_btn = "//button[@ng-click='create()']"
    _useremail_field = "//input[@name='email']"
    _userphone_field = "//input[@name='phone']"
    _userfullname_field = "//input[@name='fullName']"
    _autogenpass_checkbox = "//input[@name='autoGeneratePassword']"
    _showpasses_checkbox = "//input[@name='showPasswords']"
    _password_field = "//input[@name='password']"
    _confirmpass_field = "//input[@name='password_confirmation']"
    _saveuser_btn = "//button[@ng-click='save()']"
    _role_dropdown = "//select[@name='role']"
    _avatarUpload_element = "//input[@name='avatar']"

    def clickAddUserBtn(self):
        self.elementClick(self._adduser_btn)

    def enterUserEmail(self, email):
        self.elementClear(self._useremail_field)
        self.sendKeys(email, self._useremail_field)

    def enterUserPhone(self, phone):
        self.elementClear(self._userphone_field)
        self.sendKeys(phone, self._userphone_field)

    def enterUserFullName(self, name):
        self.elementClear(self._userfullname_field)
        self.sendKeys(name, self._userfullname_field)

    def autoGenPassClick(self):
        self.elementClick(self._autogenpass_checkbox)

    def showPasswordsClick(self):
        self.elementClick(self._showpasses_checkbox)

    def enterPassword(self, password):
        self.elementClear(self._password_field)
        self.sendKeys(password, self._password_field)

    def confirmPassword(self, passwordConfirm):
        self.elementClear(self._confirmpass_field)
        self.sendKeys(passwordConfirm, self._confirmpass_field)

    def selectRole(self, role):
        self.dropdownSelect(role, self._role_dropdown)

    # def uploadAvatar(self):
    #     self.

    def saveUser(self):
        self.elementClick(self._saveuser_btn)

    def addUser(self, email="", phone="", name="",
                password="", passwordConfirm="", role=""):
        self.clickAddUserBtn()
        self.enterUserEmail(email)
        self.enterUserPhone(phone)
        self.enterUserFullName(name)
        self.autoGenPassClick()
        self.showPasswordsClick()
        self.enterPassword(password)
        self.confirmPassword(passwordConfirm)
        self.selectRole(role)
        self.saveUser()
        self.util.sleep(2)
