from selenium import webdriver
from selenium.webdriver.common.by import By
from utilities.handyWrappers import HandyWrappers
import time


class ElementPresence():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome(executable_path="../basic/driver/chromedriver.exe")
        driver.maximize_window()
        driver.implicitly_wait(5)
        hw = HandyWrappers(driver)
        driver.get(baseUrl)

        check1 = hw.isElementPresent("name",By.ID)
        print(str(check1))

        check2 = hw.ElementsPresent("//input[@id='name']",By.XPATH)
        print(str(check2))

        check3 = hw.ElementsPresent("name",By.NAME)
        print(str(check3))

        driver.quit()



fn = ElementPresence()
fn.test()