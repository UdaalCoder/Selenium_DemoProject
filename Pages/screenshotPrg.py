s_file = r"C:\Users\vidya gowda\PycharmProjects\Selenium_DemoProject\screenshots_file\\"

class ScreenshotClass:
    from settings import driver, url

    un = '//input[@placeholder="Username"]'
    pwd = '//input[@type="password"and@name="pwd"]'
    login = '//div[text()="Login "]'

    def get_url(self):
        self.driver.get(self.url[0])
        self.driver.maximize_window()
        self.driver.save_screenshot(s_file+"url.png")

    def get_username(self):
        self.driver.find_element_by_xpath(self.un).send_keys("admin")
        self.driver.get_screenshot_as_file(s_file+"username.png")

    def get_password(self):
        self.driver.find_element_by_xpath(self.pwd).send_keys("manager")
        print(self.driver.get_screenshot_as_png())

    def get_loginBtn(self):
        self.driver.find_element_by_xpath(self.login).click()
        print(self.driver.get_screenshot_as_base64())

    def Login_activites(self):
        self.get_url()
        self.get_username()
        self.get_password()
        self.get_loginBtn()
        self.driver.close()

s = ScreenshotClass()
s.Login_activites()