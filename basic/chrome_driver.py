from selenium import webdriver

class ChromeDriver():
    def test(self):
        driver = webdriver.Chrome(executable_path="driver/chromedriver.exe")
        # Abre el URL
        driver.get("http://www.letskodeit.com")

cc = ChromeDriver()
cc.test()