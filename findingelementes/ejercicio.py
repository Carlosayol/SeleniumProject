from selenium import webdriver

class Ejercicios():
    def test(self):
        baseUrl1 = "https://letskodeit.teachable.com/p/practice"
        baseUrl2 = "https://www.w3schools.com/css/css_table.asp"
        driver = webdriver.Chrome(executable_path="../basic/driver/chromedriver.exe")
        # Abre el URL
        driver.get(baseUrl1)

        #Encontrando el valod del curso de Python
        element1 = driver.find_element_by_xpath("//table[@id='product']//td[contains(text(),'Python Programming Language')]//following-sibling::td")

        if element1 is not None:
            print("Se encontro la tabla y y el valor del curso, el cual es",element1.text)
        else:
            print("Error en la matrix")

        driver.get(baseUrl2)
        element2 = driver.find_element_by_xpath("//table[@id='customers']//td[contains(text(),'Island Trading')]//following-sibling::td[1]")

        if element2 is not None:
            print("Se encontro la tabla y el dueño de la empresa, el cual es",element2.text)
        else:
            print("Super F")


fn = Ejercicios()
fn.test()