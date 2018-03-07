import os
import logging
from datetime import datetime
from traceback import print_stack
import utilities.custom_logger as cl
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SeleniumDriver():

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def back(self):
        return self.driver.back()

    def forward(self):
        return self.driver.forward()

    def getTitle(self):
        return self.driver.title

    def getCurrentUrl(self):
        return self.driver.current_url

    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "classname":
            return By.CLASS_NAME
        elif locatorType == "linktext":
            return By.LINK_TEXT
        else:
            self.log.info("Locator type " + locatorType + " not correct/supported")
        return False

    def getElement(self, locator, locatorType="xpath"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            self.log.info("Element --" + locator + "-- Found")
        except:
            self.log.info("Element not found")
        return element

    def getElementList(self, locator, locatorType="xpath"):
        """
        NEW METHOD
        Get list of elements
        """
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_elements(byType, locator)
            self.log.info("Elements list with locator --" + locator + "-- found")
        except:
            self.log.info("Elements list with locator --" + locator + "-- not found")
        return element

    def elementClick(self, locator="", locatorType="xpath", element=None):
        """
        Click on element --> MODIFIED
        Either provide element or a combination of locator and locatorType
        """

        try:
            if locator:     #This means if locator is not emty
                element = self.getElement(locator, locatorType)
            element.click()
            self.log.info("Element --" + locator + "-- clicked")
        except:
            self.log.info("Cannot click --" + locator + "-- element")
            print_stack()

    def dropdownSelect(self, value, locator, locatorType="xpath", selectType="index", element=None):
        selectType = selectType.lower()
        if locator:
            element = self.getElement(locator, locatorType)
        if selectType == "index":
            return Select(element).select_by_index(value)
        elif selectType == "value":
            return Select(element).select_by_value(value)
        elif selectType == "visible text":
            return Select(element).select_by_visible_text(value)
        else:
            self.log.info("Cannot select element with --" + value + "-- value with select type --" +
                                selectType + "--")
            print_stack()

    def elementClear(self, locator="", locatorType="xpath", element=None):
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            element.clear()
            self.log.info("Element --" + locator + "-- cleared seccessful")
        except:
            self.log.info("Cannot clear --" + locator + "-- element")
            print_stack()

    def iframeSwitch(self, name):
        try:
            self.driver.switch_to.frame(name)
            self.log.info("Seccessfully switched to --" + name + "-- IFrame")
        except:
            self.log.info("Cannot swith to --" + name + "-- IFrame")
            print_stack()

    def switchParentPage(self):
        try:
            self.driver.switch_to.default_content()
            self.log.info("Seccessfully switched to default page")
        except:
            self.log.info("Cannot swith to default page")
            print_stack()

    def sendKeys(self, data, locator, locatorType="xpath"):
        """
        Send keys to an element --> MODIFIED
        Either proveide element or combination of locator and locatorType
        """
        try:
            if locator:     #This means if locator is not emty
                element = self.getElement(locator, locatorType)
            element.send_keys(data)
            self.log.info("Send data --" + data + "-- to the --" + locator + "-- element")
        except:
            self.log.info("Cannot send data --" + data + "-- to the --" + locator + "-- element")
            print_stack()

    def getText(self, locator="", locatorType="xpath", element=None, info=""):
        """
        NEW METHOD
        Get 'Text' on an element
        Either provide element or a combination of locator and locatorType
        """
        try:
            if locator: # This means if locator is not empty
                self.log.debug("In locator condition")
                element = self.getElement(locator, locatorType)
            self.log.debug("Before finding text")
            text = element.text
            self.log.debug("After finding element, size is: " + str(len(text)))
            if len(text) == 0:
                text = element.get_attribute("innerText")
            if len(text) != 0:
                self.log.info("Getting text on element :: " +  info)
                self.log.info("The text is  --" + text + "--")
                text = text.strip()
        except:
            self.log.error("Failed to get text on element " + info)
            print_stack()
            text = None

    def isElementPresent(self, locator, locatorType="xpath", element=None):
        """
        Check if element is present -> MODIFIED
        Either provide element or a combination of locator and locatorType
        """
        try:
            if locator:  # This means if locator is not empty
                element = self.getElement(locator, locatorType)
            if element is not None:
                self.log.info("Element with locator --" + locator + "-- present")
                return True
            else:
                self.log.info("Element with locator --" + locator + "-- not present")
                return False
        except:
            print("Element not found")
            return False

    def elementPresenceCheck(self, locator, locatorType="xpath"):
        try:
            elementList = self.getElementList(locator, locatorType)
            if len(elementList) > 0:
                self.log.info("Element Found")
                return True
            else:
                self.log.info("Element not found")
                return False
        except:
            self.log.info("Element not found")
            return False

    def isElementDisplayed(self, locator="", locatorType="xpath", element=None):
        """
        NEW METHOD
        Check if element is displayed
        Either provide element or a combination of locator and locatorType
        """
        isDisplayed = False
        try:
            if locator:  # This means if locator is not empty
                element = self.getElement(locator, locatorType)
            if element is not None:
                isDisplayed = element.is_displayed()
                self.log.info("Element --" + locator + "-- is displayed")
            else:
                self.log.info("Element --" + locator + "-- not displayed")
            return isDisplayed
        except:
            print("Element not found")
            return False

    def waitForElement(self, locator, locatorType="xpath",
                       timeout=10, pollFrequency=0.5):
        element = None

        try:
            byType = self.wrapper.getByType(locatorType)
            self.log.info("Waiting for maximum :: " + str(timeout) +
                  " :: seconds for element to be clickable")

            wait = WebDriverWait(self.driver, 10, poll_frequency=0.5,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((byType,
                                                             locator)))

            self.log.info("Element appeared on the page")
        except:
            self.log.info("Element not appeared on the page")
            print_stack()

        return element

    def screenShot(self, resultMessage):
        time = datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S")
        fileName = resultMessage + " " + time + ".png"
        screenshotDirectory = "../screenshots/"
        currentDirectory = os.path.dirname(__file__)
        relativeFileName = screenshotDirectory + fileName
        destinationFile = os.path.join(currentDirectory, relativeFileName)
        destinationDirectory = os.path.join(currentDirectory, screenshotDirectory)

        try:
            if not os.path.exists(destinationDirectory):
                os.makedirs(destinationDirectory)
            self.driver.save_screenshot(destinationFile)
            self.log.info("Screenshot saved --> " + destinationFile)
        except NotADirectoryError:
            self.log.info("### Exception Occurred")
            print_stack()

    def webScroll(self, direction="down"):
        """
        NEW METHOD
        """
        if direction == "up":
            # Scroll Up
            self.driver.execute_script("window.scrollBy(0, -1000);")

        if direction == "down":
            # Scroll Down
            self.driver.execute_script("window.scrollBy(0, 1000);")
