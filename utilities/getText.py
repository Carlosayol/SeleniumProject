from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

class getText():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome(executable_path="../basic/driver/chromedriver.exe")
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(5)

        openTabElement = driver.find_element(By.ID,"opentab")

        print("Texto en el Elemento ", openTabElement.text)

        driver.quit()






fn = getText()
fn.test()