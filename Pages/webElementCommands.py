from settings import driver,url

driver.get(url[0])
driver.maximize_window()
#driver.find_element_by_css_selector('input[id="username"]').send_keys("admin")
driver.find_element_by_css_selector("input#username").send_keys("admin")
driver.find_element_by_css_selector("input.textField.pwdfield").send_keys("manager")
bool_value = driver.find_element_by_css_selector("input#keepLoggedInCheckBox").is_selected()
print("is selected o/p :",bool_value)
print(driver.find_element_by_css_selector("input#username").is_enabled())
print(driver.find_element_by_partial_link_text("Forgot").is_displayed())
print(driver.find_element_by_partial_link_text("Forgot").tag_name)
print(driver.find_element_by_id("loginButton").text)
print(driver.find_element_by_id("loginButton").get_attribute("href"))
print(driver.find_element_by_id("loginButton").location)
print(driver.find_element_by_id("loginButton").size)
print(driver.find_element_by_id("loginButton").rect)
print(driver.find_element_by_id("loginButton").value_of_css_property("Font"))