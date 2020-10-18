from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class autoComplete():

    def test(self):
        baseUrl = "https://www.southwest.com/"
        driver = webdriver.Chrome(executable_path="../basic/driver/chromedriver.exe")
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(5)

        #Enviar datos
        cityDeparture = driver.find_element(By.ID,"LandingAirBookingSearchForm_originationAirportCode")
        cityDeparture.click()

        #Se manda enter para confirmar
        x = driver.switch_to.active_element
        x.send_keys("New York")
        x.send_keys(Keys.ENTER)

        time.sleep(3)
        driver.quit()



fn = autoComplete()
fn.test()