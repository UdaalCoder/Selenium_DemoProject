from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

class xPathExamples:
    from settings import driver, url

    un = '//input[@placeholder="Username"]'
    pwd = '//input[@type="password"and@name="pwd"]'
    login = '//div[text()="Login "]'

    def get_url(self):
        self.driver.get(self.url[0])

    def get_username(self):
        self.driver.implicitly_wait(10)
        element = WebDriverWait(self.driver,20).until(expected_conditions.presence_of_element_located(("xpath",self.un)))
        element.send_keys("admin")

    def get_password(self):
        self.driver.find_element_by_xpath(self.pwd).send_keys("manager")

    def get_loginBtn(self):
        self.driver.find_element_by_xpath(self.login).click()

    def LoginActivities(self):
        self.get_url()
        self.get_username()
        self.get_password()
        self.get_loginBtn()

obj = xPathExamples()
obj.LoginActivities()

