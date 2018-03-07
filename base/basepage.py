"""
@package base

Base Page Class implementation

It implements methods which are common to all pages throughout the applecation

This class needs to be inherited by all the page classes
This class should not be used by creating object instances

Example:
    Class LoginPage(BasePage)
"""

from utilities.util import Util
from traceback import print_stack
from base.selenium_driver import SeleniumDriver

class BasePage(SeleniumDriver):

    def __init__(self, driver):
        """
        Inits BasePage class

        Returns:
            None
        """
        super(BasePage, self).__init__(driver)
        self.driver = driver
        self.util = Util()

    def verifyPageTitle(self, titleToVerify):
        """
        Verify the page title

        Parameters:
            titleToVerify: Title on the page that needs to be verified
        """
        try:
            actualTitle = self.getTitle()
            return self.util.verifyTextContains(actualTitle, titleToVerify)
        except:
            self.log.error("Failed to get page title")
            print_stack()
            return False
