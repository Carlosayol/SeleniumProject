from selenium import webdriver

class FindbyIdName():
    def test(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome(executable_path="../basic/driver/chromedriver.exe")
        # Abre el URL
        driver.get(baseUrl)

        elementbyid = driver.find_element_by_id("name")

        if elementbyid is not None:
            print("Existe el id name")
        else:
            print("Efe")

        elementbyName = driver.find_element_by_name("show-hide")

        if elementbyName is not None:
            print("Existe el nombre")
        else:
            print("Super F")

        

fn = FindbyIdName()
fn.test()