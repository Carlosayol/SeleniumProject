from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class switchToWindow():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome(executable_path="../basic/driver/chromedriver.exe")
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(3)

        parentHandle = driver.current_window_handle
        print("El handle padrecito es ",parentHandle)

        driver.find_element(By.ID,"openwindow").click()
        time.sleep(2)

        handles = driver.window_handles

        for handle in handles:
            print(handle)
            if handle not in parentHandle:
                driver.switch_to.window(handle)
                searchbox = driver.find_element(By.ID, "search-courses")
                searchbox.send_keys("python")
                time.sleep(3)
                driver.close()
                break

        driver.switch_to.window(parentHandle)
        driver.find_element(By.ID,"name").send_keys("holi")
        time.sleep(3)

        driver.quit()



fn = switchToWindow()
fn.test()