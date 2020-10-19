from selenium import webdriver

class WindowSize():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome(executable_path="../basic/driver/chromedriver.exe")
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(3)

        height = driver.execute_script("return window.innerHeight;")
        width = driver.execute_script("return window.innerWidth;")

        print("Ancho de la pagina ",width)
        print("Alto de la pagina ",height)


fn = WindowSize()
fn.test()