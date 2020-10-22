from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class switchToAlert():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome(executable_path="../basic/driver/chromedriver.exe")
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(3)

        driver.find_element(By.ID,"name").send_keys("Asereje")
        driver.find_element(By.ID,"alertbtn").click()

        time.sleep(2)

        alert = driver.switch_to.alert
        alert.accept()

        driver.find_element(By.ID, "name").send_keys("Asereje")
        driver.find_element(By.ID, "confirmbtn").click()

        time.sleep(2)

        confirm = driver.switch_to.alert
        confirm.dismiss()

        time.sleep(2)
        driver.quit()




fn = switchToAlert()
fn.test()