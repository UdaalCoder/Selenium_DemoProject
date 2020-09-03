from PIL import Image

s_file = r"C:\Users\vidya gowda\PycharmProjects\Selenium_DemoProject\screenshots_file\\"

class ScreenshotClass:
    from settings import driver, url
    un = '//input[@placeholder="Username"]'
    pwd = '//input[@type="password"and@name="pwd"]'
    login = '//div[text()="Login "]'
    logo = '//div[@class="apCustomLogoContainer"]'

    def get_url(self):
        self.driver.get(self.url[0])
        self.driver.maximize_window()
        self.driver.save_screenshot(s_file+"url.png")

    def get_logo(self):
        element = self.driver.find_element_by_xpath(self.logo)
        loc = element.location #{x,y}
        siz = element.size  #{w,h}
        x = loc["x"]
        y = loc["y"]
        w = siz["width"] + x
        h = siz["height"] + y
        original_img = Image.open(s_file+"url.png")
        crop_attr = (x,y,w,h)
        cropped_img = original_img.crop(crop_attr)
        cropped_img.save(s_file+"Logo.png")

    def Login_activites(self):
        self.get_url()
        self.get_logo()
        self.driver.close()

s = ScreenshotClass()
s.Login_activites()