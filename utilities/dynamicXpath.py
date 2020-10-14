from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class DynamicXpath():

    def test(self):
        baseUrl = "https://letskodeit.com/"
        driver = webdriver.Chrome(executable_path="../basic/driver/chromedriver.exe")
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get(baseUrl)

        #Logearse
        email = "test@email.com"
        psswrd = "abcabc"

        login = driver.find_element(By.XPATH,"//div[contains(text(),'Sign Up or Log In')]")
        login.click()

        emailEl = driver.find_element(By.ID,"email")
        emailEl.send_keys(email)
        password = driver.find_element(By.ID,"password")
        password.send_keys(psswrd)
        login2 = driver.find_element(By.XPATH,"//div[@class='col-xs-12 col-md-12']/input")
        login2.click()

        #Seleccionar cursos
        course = "//h4[contains(text(),'{0}') and contains(@class,'dynamic-heading')]"
        courseLoc = course.format("JavaScript")

        courseEl = driver.find_element(By.XPATH,courseLoc)
        courseEl.click()

        time.sleep(5)
        driver.quit()



fn = DynamicXpath()
fn.test()