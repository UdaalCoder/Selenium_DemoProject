from selenium.webdriver.common.by import By
from settings import driver,url

driver.get(url[0])
driver.maximize_window()
driver.find_element(By.ID,"username").send_keys("admin")
#driver.find_element_by_name("pwd").send_keys("manager")
driver.find_element_by_class_name("textField.pwdfield").send_keys("manager")
#driver.find_element_by_id()
div_tag = driver.find_elements_by_tag_name("div")
driver.find_element_by_link_text("Forgot your password?").click()
driver.find_element_by_partial_link_text("login page").click()
print(len(div_tag))

