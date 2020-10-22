from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class switchToFrame():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome(executable_path="../basic/driver/chromedriver.exe")
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(3)

        element = driver.find_element(By.XPATH,"//legend[contains(text(),'iFrame Example')]")
        element.location_once_scrolled_into_view

        time.sleep(2)

        #Usando ID
        #driver.switch_to.frame("courses-iframe")

        #Usando posicion en arreglo"
        driver.switch_to.frame(0)

        searchbox = driver.find_element(By.ID, "search-courses")
        searchbox.send_keys("python")

        time.sleep(2)

        driver.switch_to.default_content()
        driver.execute_script("window.scrollBy(0,-1000)")

        time.sleep(2)
        driver.quit()



fn = switchToFrame()
fn.test()