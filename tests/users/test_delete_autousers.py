import pytest, unittest
from ddt import ddt, data, unpack
from utilities.read_data import getCSVData
from utilities.teststatus import StatusTest
from pages.users.users_page import UsersPage
from pages.navigation import NavigationPage


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class AddUsersTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.up = UsersPage(self.driver)
        self.ts = StatusTest(self.driver)
        self.nav = NavigationPage(self.driver)

    def setUp(self):
        self.nav.openUserPage()

    @pytest.mark.run(order=1)
    def test_delete_auto_users(self):
        self.up.deleteAutoTestUsers()
