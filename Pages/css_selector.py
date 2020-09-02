from settings import driver,url

driver.get(url[0])
driver.maximize_window()
#driver.find_element_by_css_selector('input[id="username"]').send_keys("admin")
driver.find_element_by_css_selector("input#username").send_keys("admin")
driver.find_element_by_css_selector("input.textField.pwdfield").send_keys("manager")
driver.find_element_by_css_selector("a#loginButton>div").click()
