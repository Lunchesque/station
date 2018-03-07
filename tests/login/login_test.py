import pytest, unittest
from ddt import ddt, data, unpack
from utilities.read_data import getCSVData
from utilities.teststatus import StatusTest
from pages.login.login_page import LoginPage
from pages.login.navigation_page import NavigationPage


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = StatusTest(self.driver)
    
    def setUp(self):
        self.lp.logout()

    @pytest.mark.run(order=1)
    @data(*getCSVData("logindata.csv"))
    @unpack
    def test_valid_login(self, cemail, cpassword):
        self.lp.login(email = cemail, password = cpassword)
        result = True
        self.ts.markFinal("test_valid_login", result, "Login was seccessful")
