from selenium.webdriver.common.by import By

class HandyWrappers():

    def __init__(self, driver):
        self.driver = driver


    def getByType(self,locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "classname":
            return By.CLASS_NAME
        elif locatorType == "linktext":
            return By.LINK_TEXT
        elif locatorType == "name":
            return By.NAME
        else:
            print("Locator type is not supported")
        return False

    def getElement(self, locator, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            print("Element Found")
        except:
            print("Element not found")
        return element

    def isElementPresent(self, locator, byType):
        try:
            element = self.driver.find_element(byType, locator)
            if element is not None:
                print("Element Found")
                return True
            else: return False
        except:
            print("Element not found")
            return False

    def ElementsPresent(self, locator, byType):
        try:
            elements = self.driver.find_elements(byType, locator)
            if len(elements)>0:
                print("Existen Elementos")
                return True
            else: return False
        except:
            print("No hay Elementos")
            return False