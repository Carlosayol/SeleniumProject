from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class ScrollingElement():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome(executable_path="../basic/driver/chromedriver.exe")
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(3)

        #scroll abajo
        driver.execute_script("window.scrollBy(0,900);")
        time.sleep(2)

        #scroll arriba
        driver.execute_script("window.scrollBy(0,-900);")
        time.sleep(2)

        #Seleccionar elemento y enfocarlo
        element = driver.find_element(By.ID,"mousehover")
        driver.execute_script("arguments[0].scrollIntoView(true);",element)
        time.sleep(2)
        driver.execute_script("window.scrollBy(0,-100);")

        #Metodo nativo
        location = element.location_once_scrolled_into_view
        print(location)
        driver.execute_script("window.scrollBy(0,-100);")
        time.sleep(2)

        driver.quit()


fn = ScrollingElement()
fn.test()
