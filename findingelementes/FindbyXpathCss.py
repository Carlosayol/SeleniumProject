from selenium import webdriver


class FindbyXpathCss():
    def test(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome(executable_path="../basic/driver/chromedriver.exe")
        # Abre el URL
        driver.get(baseUrl)

        elementbyXpath = driver.find_element_by_xpath("//input[@id='name']")

        if elementbyXpath is not None:
            print("Existe el xpath")
        else:
            print("Efe")

        elementbyCss = driver.find_elements_by_css_selector("#name")

        if elementbyCss is not None:
            print("Existe el css selector")
        else:
            print("Super F")


fn = FindbyXpathCss()
fn.test()