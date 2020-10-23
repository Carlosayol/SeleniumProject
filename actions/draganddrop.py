from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

class dragAndDrop():

    def test(self):
        baseUrl = "https://jqueryui.com/droppable/"
        driver = webdriver.Chrome(executable_path="../basic/driver/chromedriver.exe")
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(3)

        driver.switch_to.frame(0)

        draggable = driver.find_element(By.ID,"draggable")
        droppable = driver.find_element(By.ID,"droppable")

        try:
            actions = ActionChains(driver)
            actions.drag_and_drop(draggable,droppable).perform()
            time.sleep(2)
        except:
            print("fallo el drag and drop")

        driver.quit()

fn = dragAndDrop()
fn.test()