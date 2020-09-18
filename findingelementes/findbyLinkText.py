from selenium import webdriver


class FindbyLinkText():
    def test(self):
        baseUrl = "http://automationpractice.com/index.php"
        driver = webdriver.Chrome(executable_path="../basic/driver/chromedriver.exe")
        # Abre el URL
        driver.get(baseUrl)

        elementbyLinkText = driver.find_element_by_link_text("Contact us")

        if elementbyLinkText is not None:
            print("Existe el link text")
        else:
            print("Efe")

        elementbyPartialLinkText = driver.find_element_by_partial_link_text("Sign")

        if elementbyPartialLinkText is not None:
            print("Existe el css selector")
        else:
            print("Super F")


fn = FindbyLinkText()
fn.test()