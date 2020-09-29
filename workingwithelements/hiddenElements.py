from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

class HiddenElements():

    def test1(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome(executable_path="../basic/driver/chromedriver.exe")
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(3)

        textbox = driver.find_element(By.ID,"displayed-text")
        hidebtn = driver.find_element(By.ID,"hide-textbox")
        showbtn = driver.find_element(By.ID,"show-textbox")

        textboxstate = textbox.is_displayed()
        print("El elemento esta mostrado? ", str(textboxstate))
        time.sleep(2)

        hidebtn.click()
        textboxstate = textbox.is_displayed()
        print("El elemento esta mostrado? ", str(textboxstate))
        time.sleep(2)

        showbtn.click()
        textboxstate = textbox.is_displayed()
        print("El elemento esta mostrado? ", str(textboxstate))
        time.sleep(2)

        driver.quit()

    def test2(self):
        baseUrl = "https://www.expedia.com/?pwaLob=wizard-hotel-pwa-v2"
        driver = webdriver.Chrome(executable_path="../basic/driver/chromedriver.exe")
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(3)

        flights_a = driver.find_element(By.XPATH,"//ul[@id='uitk-tabs-button-container']//li[2]/a")
        flights_a.click()

        time.sleep(2)

        travelers_a = driver.find_element(By.LINK_TEXT,"2 travelers")
        travelers_a.click()

        time.sleep(2)

        try:
            child_hidden = driver.find_element("//div[contains(@class,'uitk-field uitk-field-select-field has-floatedLabel-label has-no-placeholder')]")
        except Exception as err:
            print(err)


fn = HiddenElements()
fn.test1()
fn.test2()