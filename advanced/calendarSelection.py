from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class CalendarSelection():

    def test(self):
        baseUrl = "https://www.expedia.com"
        driver = webdriver.Chrome(executable_path="../basic/driver/chromedriver.exe")
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(5)

        flg = driver.find_element(By.XPATH,"//span[contains(text(),'Flights')]//parent::a")
        flg.click()

        #departing field
        dparting = driver.find_element(By.ID,"d1-btn")
        dparting.click()

        #selecting date
        datetoselect = driver.find_element(By.XPATH,
                                           "//div[@class='uitk-new-date-picker-month'][position()=1]//button[@data-day='31']")
        datetoselect.click()

        time.sleep(3)


        driver.quit()

    def test2(self):
        baseUrl = "https://www.expedia.com"
        driver = webdriver.Chrome(executable_path="../basic/driver/chromedriver.exe")
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(5)

        flg = driver.find_element(By.XPATH,"//span[contains(text(),'Flights')]//parent::a")
        flg.click()

        dparting = driver.find_element(By.ID,"d1-btn")
        dparting.click()

        #Getting dates
        monthdep = driver.find_element(By.XPATH,"//div[@class='uitk-new-date-picker-month'][position()=1]")
        allValidDates = dparting.find_elements(By.XPATH,"//button[not(@disabled)]")

        for date in allValidDates:
            if date.get_attribute('data-day') == '23':
                date.click()
                driver.find_element(By.XPATH,"//button[@data-stid='apply-date-picker']").click()
                break

        time.sleep(3)

        driver.quit()


fn = CalendarSelection()
fn.test2()