from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class ClickAndSendKeys():
    def test(self):
        baseUrl = "https://letskodeit.teachable.com/"
        driver = webdriver.Chrome(executable_path="../basic/driver/chromedriver.exe")
        driver.maximize_window()

        driver.get(baseUrl)

        driver.implicitly_wait(4)

        loginlink = driver.find_element(By.XPATH,"//div[@id='navbar']//a[@href='/sign_in']")
        loginlink.click()

        userEmailField = driver.find_element(By.ID,"user_email")
        userPassField = driver.find_element(By.ID,"user_password")

        userEmailField.send_keys("test")
        userPassField.send_keys("test")

        time.sleep(3)

        userEmailField.clear()
        userPassField.clear()

        time.sleep(3)

        userEmailField.send_keys("meeee")
        userPassField.send_keys("meeee")

fn = ClickAndSendKeys()
fn.test()