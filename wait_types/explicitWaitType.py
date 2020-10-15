from traceback import print_stack
from utilities.handyWrappers import HandyWrappers
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

class ExplicityWaitType():

    def __init__(self,driver):
        self.driver = driver
        self.hw = HandyWrappers(driver)

    def waitForElement(self, locator, locatorType="id",timeout=10,
                       pollFrequency=0.5):

        element = None
        try:
            byType = self.hw.getByType(locatorType)
            print("Esperando a :: " +str(timeout)+ " :: segundos para que aparezca el elemento")
            wait = WebDriverWait(self.driver, 10, poll_frequency=1,
                                 ignored_exceptions=[NoSuchElementException, ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((byType, locator)))
            element.click()
            print("Elemento aparecio en la web")
        except:
            print("No aparecio el elemento")
            print_stack()
        return element