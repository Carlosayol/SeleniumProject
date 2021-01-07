from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class switchToFrame():

    def test(self):
        baseUrl = "https://courses.letskodeit.com/courses/learn-python3-from-scratch/buy"
        driver = webdriver.Chrome(executable_path="../basic/driver/chromedriver.exe")
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(3)

        driver.execute_script("window.scrollBy(0,1000);")

        time.sleep(2)

        #Usando ID
        #driver.switch_to.frame("courses-iframe")

        #Usando posicion en arreglo"
        driver.switch_to.frame(0)

        credit_input = driver.find_element(By.NAME, "cardnumber")
        credit_input.send_keys("1111111111111111")

        driver.switch_to.default_content()

        # iframe_list = driver.find_elements(By.XPATH,"//iframe")
        # print(len(iframe_list))
        # for  i in range (len(iframe_list)):
        #     driver.switch_to.frame(iframe_list[i])
        #     try:
        #         element = driver.find_element(By.NAME, "cardnumber")
        #         if element is not None:
        #             print("element found at index ", i)
        #     except:
        #         print("f")
        #     driver.switch_to.default_content()

        driver.switch_to.frame(1)

        credit_input2 = driver.find_element(By.NAME, "exp-date")
        credit_input2.send_keys(1234)

        driver.switch_to.default_content()


        #enroll_buttons = driver.find_elements(By.XPATH,"//div[@class='stripe-outer ']//button")
        #enroll_button = enroll_buttons[2]
        #enroll_button.click()
        #print(enroll_buttons)

        time.sleep(2)


        #driver.execute_script("window.scrollBy(0,-1000)")






        driver.quit()



fn = switchToFrame()
fn.test()