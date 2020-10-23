from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

class mouseHovering():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome(executable_path="../basic/driver/chromedriver.exe")
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(3)

        driver.execute_script("window.scrollBy(0,600)")
        time.sleep(2)

        hoverElement = driver.find_element(By.ID,"mousehover")
        topElementXpath = "//a[contains(text(),'Top')]"

        try:
            actions = ActionChains(driver)
            actions.move_to_element(hoverElement).perform()
            time.sleep(2)
            topElement = driver.find_element(By.XPATH, topElementXpath)
            actions.move_to_element(topElement).click().perform()
            time.sleep(2)
        except:
            print("No se encontro el elemento")

        driver.quit()



fn = mouseHovering()
fn.test()
