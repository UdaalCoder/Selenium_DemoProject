#vidyashree.temp15@gmail.com
from settings import driver,url
class FK:

    crossBtn = '//button[@class="_2AkmmA _29YdH8"]'
    search = '//input[@placeholder="Search for products, brands and more"]'
    search_icon = '//button[@class="vh79eN"]'
    check_box = '//div[text()="6 GB & Above"]'
    mob_xpath = '(//div[@class="_1UoZlX"])[1]'
    cart = '//button[text()="ADD TO CART"]'

    def get_url(self):
        driver.get(url[1])
        driver.maximize_window()

    def search_products(self):
        page_title = driver.title
        print(page_title)
        print(driver.current_window_handle)
        print("in search")
        driver.find_element_by_xpath(self.crossBtn).click()
        driver.find_element_by_xpath(self.search).send_keys("Mobiles")
        driver.find_element_by_xpath(self.search_icon).click()
        return page_title

    def window_handling(self,a):
        print("in window handling")
        handles = driver.window_handles
        print(handles)
        for i in handles:
            driver.switch_to.window(i) #[p,c]
            title = driver.title
            print(title)
            if title!=a:
                driver.switch_to.window(i)

    def after_search(self):
        print("in after search")
        driver.implicitly_wait(10)
        driver.find_element_by_xpath(self.check_box).click()
        driver.find_element_by_xpath(self.mob_xpath).click()

    def after_winHandling(self):
        driver.implicitly_wait(10)
        driver.find_element_by_xpath(self.cart).click()

    def loginActivities(self):
        self.get_url()
        res = self.search_products()
        import time
        time.sleep(3)
        self.after_search()
        self.window_handling(res)
        self.after_winHandling()
        self.window_handling(res)


obj = FK()
obj.loginActivities()
