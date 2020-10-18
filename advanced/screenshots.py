from selenium import webdriver
from selenium.webdriver.common.by import By
import time
class screenShots():

    def test(self):
        baseUrl = "https://courses.letskodeit.com/"
        driver = webdriver.Chrome(executable_path="../basic/driver/chromedriver.exe")
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(4)

        #Intentado logear (fallara)
        driver.find_element(By.XPATH,"//a[contains(text(),'Sign In')]").click()
        driver.find_element(By.ID,"email").send_keys("abc@hotmail.com")
        driver.find_element(By.ID,"password").send_keys("asereje")
        driver.find_element(By.XPATH,"//div[@class='col-xs-12 col-md-12']//input").click()

        time.sleep(5)

        location = "C:/Users/Usuario/Desktop/test.png"

        try:
            driver.save_screenshot(location)
            print("Se guardo una screenshot en ",location)
        except NotADirectoryError:
            print("No es una ruta correcta")

        driver.quit()

fn = screenShots()
fn.test()