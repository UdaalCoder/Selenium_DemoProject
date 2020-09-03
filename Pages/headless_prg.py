from selenium import webdriver
from settings import url

class HeadlessBrowser:
    un = '//input[@placeholder="Username"]'
    pwd = '//input[@type="password"and@name="pwd"]'
    login = '//div[text()="Login "]'

    def headless(self):
        print("in headless")
        option = webdriver.ChromeOptions()
        option.headless = True
        driver = webdriver.Chrome(executable_path=r'C:\Users\vidya gowda\PycharmProjects\Selenium_DemoProject\drivers\chromedriver.exe',options=option)
        return driver

    def get_url(self,driver):
        print("in url")
        driver.get(url[0])
        driver.maximize_window()

    def get_username(self,driver):
        print("in username")
        driver.implicitly_wait(10)
        driver.find_element_by_xpath(self.un).send_keys("admin")

    def get_password(self,driver):
        print("in pwd")
        driver.find_element_by_xpath(self.pwd).send_keys("manager")

    def get_loginBtn(self,driver):
        print("in login")
        driver.find_element_by_xpath(self.login).click()

    def loginActivities(self):
        wd = self.headless()
        self.get_url(wd)
        self.get_username(wd)
        self.get_password(wd)
        self.get_loginBtn(wd)
        print("logged in......")

obj = HeadlessBrowser()
obj.loginActivities()