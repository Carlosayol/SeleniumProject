from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class JavaScriptExecution():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome(executable_path="../basic/driver/chromedriver.exe")
        driver.maximize_window()
        #driver.get(baseUrl)
        #Usando javascript
        driver.execute_script("window.location = 'https://letskodeit.teachable.com/p/practice';")

        driver.implicitly_wait(3)

        element = driver.execute_script("return document.getElementById('name');")
        element.send_keys("Holi")
        time.sleep(3)


fn = JavaScriptExecution()
fn.test()