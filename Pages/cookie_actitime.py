from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import json

class xPathExamples:
    from settings import driver, url
    cookie_path = r'C:\Users\vidya gowda\PycharmProjects\Selenium_DemoProject\cookies_file\\'

    un = '//input[@placeholder="Username"]'
    pwd = '//input[@type="password"and@name="pwd"]'
    login = '//div[text()="Login "]'

    def get_url(self):
        self.driver.get(self.url[0])
        self.driver.maximize_window()

    def get_username(self):
        self.driver.implicitly_wait(10)
        element = WebDriverWait(self.driver,20).until(expected_conditions.presence_of_element_located(("xpath",self.un)))
        element.send_keys("admin")

    def get_password(self):
        self.driver.find_element_by_xpath(self.pwd).send_keys("manager")

    def get_loginBtn(self):
        self.driver.find_element_by_xpath(self.login).click()

    def get_cookiesfunc(self):
        cookies = self.driver.get_cookies()
        print(cookies)
        with open(self.cookie_path+"cookies.json","w") as file:
            json.dump(cookies,file)

    def adding_cookies(self):
        with open(self.cookie_path+"cookies.json","r") as file:
            data = json.load(file)
        for i in data:
            self.driver.add_cookie(i)


    def LoginActivities(self):
        self.get_url()
        # self.get_username()
        # self.get_password()
        # self.get_loginBtn()
        # self.get_cookiesfunc()
        self.adding_cookies()
        self.get_url()

obj = xPathExamples()
obj.LoginActivities()

