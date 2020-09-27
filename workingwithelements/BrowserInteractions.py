from selenium import webdriver

class BrowserInteractions():

    def test(self):

        baseurl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome(executable_path="../basic/driver/chromedriver.exe")

        #Ejercicios

        driver.maximize_window()

        driver.get(baseurl)

        print("El titulo de la pagina es ",driver.title)
        print("El url actual de la pagina es ",driver.current_url)

        driver.refresh()
        print("La pagina se refresco por primera vez")

        driver.get("https://letskodeit.teachable.com/?_ga=2.47774754.483877351.1601217995-2052041573.1600008645")
        print("El titulo de la pagina es ", driver.title)
        print("El url actual de la pagina ahora es ",driver.current_url)

        driver.back()
        print("El titulo de la pagina es ", driver.title)

        driver.forward()
        print("El titulo de la pagina es ",driver.title)

        page_source = driver.page_source

        driver.quit()




fn = BrowserInteractions()
fn.test()