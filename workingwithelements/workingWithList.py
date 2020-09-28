from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class ElementList():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome(executable_path="../basic/driver/chromedriver.exe")
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(5)

        checkboxList = driver.find_elements(By.XPATH,"//input[contains(@type,'checkbox') and contains(@name,'cars')]")
        size = len(checkboxList)
        print("Los checkbox seleccionados son ", str(size))

        for checkbox in checkboxList:
            checkbox.click()
            time.sleep(3)

fn = ElementList()
fn.test()