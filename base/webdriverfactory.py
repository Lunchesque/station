"""
@package base

WebDriver Factory class implementation
It creates a webdriver instance based on browser configuration

Example:
    wdf = WebDriverFactory(browser)
    wdf.getWebDriverInstance()
"""
import traceback
from selenium import webdriver

class WebDriverFactory():

    def __init__(self, browser):
        """
        Inits WebDriverFactory class

        Returns:
            None
        """
        self.browser = browser

    """
        Set chrome driver and IE einvorment based on OS

        chromedriver = C:/.../chromedriver.exe
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver = webdriver.Chrome(chromedriver)

        PREFERRED: Set the path on the machine where browser will be executed
    """

    def getWebDriverInstance(self):
        """
        Get WebDriver Instance based on the browser configuration
        Returns:
            'WebDriver Instance'
        """
        baseUrl = "https://172.20.9.134"
        if self.browser == "iexplorer":
            driver = webdriver.Ie()
        elif self.browser == "firefox":
            driver = webdriver.Firefox()
        elif self.browser == "chrome":
            driver = webdriver.Chrome()
        else:
            driver = webdriver.Chrome()
        # Setting Driver Implict wait time for An Element
        driver.implicitly_wait(5)
        # Maximizing brouser window
        driver.maximize_window()
        # Loading browser with App URL
        driver.get(baseUrl)
        return driver
