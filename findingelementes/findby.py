from selenium import webdriver
from selenium.webdriver.common.by import By

class FindbyClassTag():
    def test(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome(executable_path="../basic/driver/chromedriver.exe")
        # Abre el URL
        driver.get(baseUrl)

        elementbyID = driver.find_element(By.ID, "openwindow")

        if elementbyID is not None:
            print("Existe el elemento con el ID")
        else:
            print("Efe")

        elementbyXpath = driver.find_element(By.XPATH,"//*[@id='displayed-text']")

        if elementbyXpath is not None:
            print("Existe un elemento con el xpath especificdado")
        else:
            print("Super F")

        elementbyCssSelector = driver.find_element(By.CSS_SELECTOR,"#name")

        if elementbyCssSelector is not None:
            print("Existe un elemento con el css especificado")
        else:
            print("sorry bro")

fn = FindbyClassTag()
fn.test()