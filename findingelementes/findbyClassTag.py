from selenium import webdriver


class FindbyClassTag():
    def test(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome(executable_path="../basic/driver/chromedriver.exe")
        # Abre el URL
        driver.get(baseUrl)

        #No usar la clase completa que nos da ChroPath
        elementbyClassName = driver.find_element_by_class_name("displayed-class")

        if elementbyClassName is not None:
            print("Existe el elemento con la clase")
            elementbyClassName.send_keys("Testing the Element")
        else:
            print("Efe")

        elementbyTagName = driver.find_element_by_tag_name("h1")

        if elementbyTagName is not None:
            print("Existe un elemento con el tag")
            print(elementbyTagName.text)
        else:
            print("Super F")


fn = FindbyClassTag()
fn.test()