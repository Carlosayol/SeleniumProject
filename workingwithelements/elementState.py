from selenium import webdriver
from selenium.webdriver.common.by import By

class ElementState():

    def isEnabled(self):
        baseUrl = "https://www.google.com"
        driver = webdriver.Chrome(executable_path="../basic/driver/chromedriver.exe")
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(3)

        e1 = driver.find_element(By.NAME,"q")
        e1State = e1.is_enabled()
        print("E1 esta habilitado? ",str(e1State))

        e2 = driver.find_element(By.NAME,"iflsig")
        e2State = e2.is_enabled()
        print("E2 esta habilitado? ",str(e2State))

        e1.send_keys("letskodeit")

fn = ElementState()
fn.isEnabled()