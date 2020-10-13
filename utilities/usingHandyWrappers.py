from selenium import webdriver
from selenium.webdriver.common.by import By
from utilities.handyWrappers import HandyWrappers
import time

class usingWrappers():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome(executable_path="../basic/driver/chromedriver.exe")
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(5)

        hw = HandyWrappers(driver)

        openTabElement = hw.getElement("opentab","id")
        print("Texto en el Elemento: ", openTabElement.text)
        time.sleep(3)

        textField = hw.getElement("//input[@id='name']","xpath")
        textField.send_keys("Holi")
        time.sleep(3)

        driver.quit()



fn = usingWrappers()
fn.test()