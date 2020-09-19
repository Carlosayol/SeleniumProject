from selenium import webdriver
from selenium.webdriver.common.by import By

class ListOfElements():
    def test(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome(executable_path="../basic/driver/chromedriver.exe")
        # Abre el URL
        driver.get(baseUrl)

        listOfElementsByClassName = driver.find_elements_by_class_name("inputs")

        if listOfElementsByClassName is not None:
            sz = len(listOfElementsByClassName)
            print(f"Existen {sz} elementos por la clase especificada")

        listOfElementsByTagName = driver.find_elements(By.TAG_NAME,"button")

        if listOfElementsByTagName is not None:
            sz1 = len(listOfElementsByTagName)
            print(f"Existen {sz1} elementos por el tag name especificada")

fn = ListOfElements()
fn.test()