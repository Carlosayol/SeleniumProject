from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class ImplicitWaitDemo():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/"
        driver = webdriver.Chrome(executable_path="../basic/driver/chromedriver.exe")
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(5)

        login = driver.find_element(By.XPATH,"//div[@id='navbar']//a[@href='/sign_in']")
        login.click()

        emailEl = driver.find_element(By.ID,"user_email")
        emailEl.send_keys("test")

        driver.quit()



fn = ImplicitWaitDemo()
fn.test()