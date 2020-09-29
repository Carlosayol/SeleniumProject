from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

class DropdownSelect():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome(executable_path="../basic/driver/chromedriver.exe")
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(5)

        dropdown = driver.find_element(By.ID,"carselect")
        sel = Select(dropdown)

        sel.select_by_index("0")
        print("Seleccionado por index 0 bmw")

        time.sleep(4)

        sel.select_by_value("honda")
        print("Seleccionado por valor Honda")

        time.sleep(4)

        sel.select_by_visible_text("Benz")
        print("Seleccionado por texto Benz")

        time.sleep(4)




fn = DropdownSelect()
fn.test()