from settings import driver
c_path = r'C:\Users\vidya gowda\PycharmProjects\Selenium_DemoProject\html_files\alert and pop up handling\confirmation_alert.html'
s_path = r'C:\Users\vidya gowda\PycharmProjects\Selenium_DemoProject\html_files\alert and pop up handling\simple_alert.html'
p_path = r'C:\Users\vidya gowda\PycharmProjects\Selenium_DemoProject\html_files\alert and pop up handling\Prompt_alert.html'

class Alerts:

    def get_url(self):
        # driver.get(c_path)
        # driver.get(s_path)
        driver.get(p_path)
        driver.maximize_window()

    def con_alert(self):
        driver.find_element_by_name("alert").click()
        alert_obj = driver.switch_to.alert
        #alert_obj = driver.switch_to_alert() --> warning
        alert_obj.accept()
        driver.find_element_by_name("alert").click()
        alert_obj.dismiss()

    def simple_alert(self):
        driver.find_element_by_name("alert").click()
        alert_obj = driver.switch_to.alert
        alert_obj.accept()

    def prompt_alert(self):
        driver.find_element_by_name("employeeLogin").click()
        alert_obj = driver.switch_to.alert
        alert_obj.send_keys("Vidya")
        print(alert_obj.text)
        alert_obj.accept()
        print(alert_obj.text)
        alert_obj.accept()

a = Alerts()
a.get_url()
a.prompt_alert()