import pytest, unittest
from ddt import ddt, data, unpack
from utilities.read_data import getCSVData
from pages.navigation import NavigationPage
from utilities.teststatus import StatusTest
from pages.users.users_page import UsersPage
from pages.login.login_page import LoginPage

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class SmokeTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.up = UsersPage(self.driver)
        self.ts = StatusTest(self.driver)
        self.nav = NavigationPage(self.driver)
        self.lp = LoginPage(self.driver)

    @pytest.mark.first
    @data(*getCSVData("/home/sergey/station/data/admilogindata.csv"))
    @unpack
    def test_admin_login(self, admEmail, admPassword):
        self.lp.logout()
        self.lp.login(email=admEmail, password=admPassword)
        result = self.lp.verifyAdmLogin()
        assert result == True
        self.ts.mark(result, "TEST PASSED")


    def setUp(self):
        self.nav.openUserPage()

    @pytest.mark.order1
    @data(*getCSVData("/home/sergey/station/data/addusersdata.csv"))
    @unpack
    def test_add_users(self, uemail, uphone, uname, upassword, upasswordConfirm, urole):
        _old_users = self.up.getNumOfAutoTestUsers()
        self.up.addUser(email=uemail, phone=uphone, name=uname, password=upassword,
                            passwordConfirm=upasswordConfirm, role=urole)
        _new_users = self.up.getNumOfAutoTestUsers()
        assert _new_users == _old_users + 1
        self.ts.mark("True", "TEST PASSED")

    @data(*getCSVData(""))
    @unpack
    def test_mail_check(sefl, ):


    @pytest.mark.last
    def test_delete_auto_users(self):
        self.up.deleteAutoTestUsers()
        _new_users = self.up.getNumOfAutoTestUsers()
        assert _new_users == 0
        self.ts.markFinal("SmokeTest", "TRUE", "ALL TESTS PASSED SECCESFUL")
