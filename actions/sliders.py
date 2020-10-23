from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

class sliders():

    def test(self):
        baseUrl = "https://jqueryui.com/slider/"
        driver = webdriver.Chrome(executable_path="../basic/driver/chromedriver.exe")
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(3)

        driver.switch_to.frame(0)

        slider = driver.find_element(By.XPATH,"//div[@id='slider']//span")

        try:
            actions = ActionChains(driver)
            actions.drag_and_drop_by_offset(slider,60,0).perform()
            time.sleep(2)
        except:
            print("fallo el drag and drop por offset")

        driver.quit()

fn = sliders()
fn.test()