from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class ElementState():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome(executable_path="../basic/driver/chromedriver.exe")
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(5)

        bmwRadioBtn = driver.find_element(By.ID,"bmwradio")
        bmwRadioBtn.click()

        time.sleep(2)

        benzRadioBtn = driver.find_element(By.ID,"benzradio")
        benzRadioBtn.click()

        time.sleep(2)

        bmwCheck = driver.find_element(By.ID,"bmwcheck")

        #time.sleep(2)

        hondaCheck = driver.find_element(By.ID, "hondacheck")
        hondaCheck.click()

        time.sleep(2)

        print("BMW checkbox esta seleccionada? ", str(bmwCheck.is_selected()))
        print("Honda checkbox esta seleccionada? ", str(hondaCheck.is_selected()))

fn = ElementState()
fn.test()