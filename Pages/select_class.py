from selenium.webdriver.support.select import Select
from settings import driver
filepath = r'C:\Users\vidya gowda\PycharmProjects\Selenium_DemoProject\html_files\Select_dropdown.html'
import time

driver.get(filepath)
driver.maximize_window()
element = driver.find_element_by_id("cars")
s = Select(element)
s.select_by_value("sub1")
time.sleep(2)
s.select_by_index(3)
time.sleep(2)
s.select_by_visible_text("Mysore")
time.sleep(2)

options = s.options
print(options)
print("all_options are")
for i in options:
    print(i.text)
print()
selected_options = s.all_selected_options
print(selected_options)
print("all_selected_options are")
for i in selected_options:
    print(i.text)
print()
first_selected = s.first_selected_option
print("first_selected_option : ",first_selected.text)
print()
print(s.is_multiple)
s.deselect_by_value("sub2")
time.sleep(2)
s.deselect_by_index(2)
time.sleep(2)
s.deselect_by_visible_text("Mumbai")
time.sleep(2)
driver.close()

