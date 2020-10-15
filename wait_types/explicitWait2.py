from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from wait_types.explicitWaitType import ExplicityWaitType


class ExplicitWaitDemo():

    def test(self):
        baseUrl = "https://www.expedia.com/"
        driver = webdriver.Chrome(executable_path="../basic/driver/chromedriver.exe")
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)

        wait = ExplicityWaitType(driver)

        flg = driver.find_element(By.XPATH,"//span[contains(text(),'Flights')]//parent::a")
        flg.click()

        bttons = driver.find_elements(By.XPATH,"//button[@class='uitk-faux-input']")

        bttons[0].click()
        textbox1 = driver.find_element(By.XPATH,"//header/section[1]/div[1]/input[1]")
        textbox1.send_keys("SFO")
        textbox1.send_keys(Keys.ENTER)

        bttons[1].click()
        x = driver.switch_to.active_element
        x.send_keys("NYC")
        x.send_keys(Keys.ENTER)

        srch = driver.find_element(By.XPATH,"//button[contains(text(),'Search')]")
        srch.click()

        element = wait.waitForElement("//input[@id='stops-0']",locatorType="xpath",timeout=30)
        element.click()

        time.sleep(2)
        driver.quit()



fn = ExplicitWaitDemo()
fn.test()