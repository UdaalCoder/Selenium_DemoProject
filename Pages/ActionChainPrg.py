import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from settings import driver,url

class AC_class:
    un = '//input[@placeholder="Username"]'
    pwd = '//input[@type="password"and@name="pwd"]'
    login = '//div[text()="Login "]'
    Tasks = '//div[text()="Tasks"]'
    reports = '//div[text()="Reports"]'
    ele = '//div[text()="All Customers"]'

    def get_url(self):
        print("in url")
        driver.get(url[0])
        driver.maximize_window()

    def get_username(self):
        print("in username")
        driver.implicitly_wait(10)
        driver.find_element_by_xpath(self.un).send_keys("admin")

    def get_password(self):
        print("in pwd")
        driver.find_element_by_xpath(self.pwd).send_keys("manager")

    def get_loginBtn(self):
        print("in login")
        driver.find_element_by_xpath(self.login).click()

    def in_homePage(self):
        print("in home page")
        a_obj = ActionChains(driver)
        driver.find_element_by_xpath(self.Tasks).click()
        element_report = driver.find_element_by_xpath(self.reports)
        a_obj.context_click(element_report).perform()
        element = driver.find_element_by_xpath(self.ele)
        a_obj.click(element).perform()
        a_obj.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()

    def loginActivities(self):
        self.get_url()
        self.get_username()
        self.get_password()
        self.get_loginBtn()
        self.in_homePage()


obj = AC_class()
obj.loginActivities()