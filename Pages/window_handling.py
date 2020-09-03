#vidyashree.temp15@gmail.com
import time

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
        print("page title is : ",page_title)
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
        for i in handles:#[p,c]
            driver.switch_to.window(i)
            title = driver.title
            print("title is : ",title)
            if title!=a:
                print("##########switched######")
                driver.switch_to.window(i)

    def after_search(self):
        print("in after search")
        driver.implicitly_wait(10)
        driver.find_element_by_xpath(self.check_box).click()
        time.sleep(3)
        driver.find_element_by_xpath(self.mob_xpath).click()

    def after_winHandling(self):
        driver.implicitly_wait(10)
        driver.find_element_by_xpath(self.cart).click()
        pagetitle2 = driver.title
        print("page title 2 is : ",pagetitle2)
        return pagetitle2


    def loginActivities(self):
        self.get_url()
        page_title = self.search_products()
        import time
        time.sleep(3)
        self.after_search()
        self.window_handling(page_title)
        pagetitle2 = self.after_winHandling()
        time.sleep(3)
        self.window_handling(pagetitle2)


obj = FK()
obj.loginActivities()
