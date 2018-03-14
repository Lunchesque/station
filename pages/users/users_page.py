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
    _avatar_element = "//input[@name='avatar']"
    _users_options_btn = "//span[contains(text(),'Auto_test_user')]//parent::td//following-sibling::td/div"
    _delete_btn = "//span[contains(text(),'Auto_test_user')]//parent::td//following-sibling::td/div/div/ul/li/a[(text()='Удалить') or (text()='Delete')]"
    _confirm_deletion_btn = "//button[@class='btn btn-primary ng-binding']"
    _count_test_users = "//span[contains(text(),'Auto_test_user')]"

    #path for avatars
    _guest_avatar = "/home/sergey/station/usersavatars/guest_avatar.png"
    _nabl_avatar = "/home/sergey/station/usersavatars/watcher_avatar.jpg"
    _oper_avatar = "/home/sergey/station/usersavatars/oper_avatar.jpg"
    _admin_avatar = "/home/sergey/station/usersavatars/admin_avatar.jpg"

    def clickAddUserBtn(self):
        self.elementClick(self._adduser_btn)

    def enterUserEmail(self, email):
        self.elementClear(self._useremail_field)
        self.sendKeys(email, self._useremail_field)

    def enterUserPhone(self, phone):
        self.elementClear(self._userphone_field)
        self.sendKeys(phone, self._userphone_field)

    def enterUserFullName(self, name):
        name = name + self.util.uniqueId()
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

    def uploadAvatar(self, role):
        if role == "0":
            self.sendKeys(self._guest_avatar, self._avatar_element)
        if role == "1":
            self.sendKeys(self._nabl_avatar, self._avatar_element)
        if role == "2":
            self.sendKeys(self._oper_avatar, self._avatar_element)
        if role == "3":
            self.sendKeys(self._admin_avatar, self._avatar_element)

    def saveUser(self):
        self.elementClick(self._saveuser_btn)

    def usersOptionsClick(self):
        self.actionChainsClick(self._users_options_btn)

    def deleteBtnClick(self):
        self.util.sleep(0.2)
        self.elementClick(self._delete_btn)

    def confirmDeleteBtnClick(self):
        self.elementClick(self._confirm_deletion_btn)

    def roleAndAvatarChoose(self, role):
        self.selectRole(role)
        self.uploadAvatar(role)

    def typeUserData(self, email, phone, name):
        self.enterUserEmail(email)
        self.enterUserPhone(phone)
        self.enterUserFullName(name)

    def typePassword(self, password, passwordConfirm):
        self.autoGenPassClick()
        self.showPasswordsClick()
        self.enterPassword(password)
        self.confirmPassword(passwordConfirm)

    def addUser(self, email="", phone="", name="", password="",
                                passwordConfirm="", role=""):
        self.clickAddUserBtn()
        self.typeUserData(email, phone, name)
        self.typePassword(password, passwordConfirm)
        self.roleAndAvatarChoose(role)
        self.saveUser()
        self.util.sleep(0.3)

    def getNumOfAutoTestUsers(self):
        return len(self.getElementList(self._count_test_users))
    #
    # def verifyNewAutoTestUserAdded(self):
    #

    def deleteUser(self):
        self.usersOptionsClick()
        self.deleteBtnClick()
        self.confirmDeleteBtnClick()
        self.util.sleep(0.3)

    def deleteAutoTestUsers(self):
        while self.elementPresenceCheck(self._count_test_users):
            self.deleteUser()
            if self.isElementPresent(self._count_test_users) == False:
                break
