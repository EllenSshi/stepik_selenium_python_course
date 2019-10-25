import os
from selenium import webdriver
import time

browser = webdriver.Chrome()
try:
	file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'file.txt')
	link = "http://suninjuly.github.io/file_input.html"
	browser.get(link)
	browser.find_element_by_css_selector("[name='firstname']").send_keys("test")
	browser.find_element_by_css_selector("[name='lastname']").send_keys("test")
	browser.find_element_by_css_selector("[name='email']").send_keys("test@test.test")
	browser.find_element_by_css_selector("[type='file']").send_keys(file_path)
	browser.find_element_by_tag_name("button").click()
	alert = browser.switch_to.alert
	print(alert.text)
	alert.accept()
finally:
	time.sleep(5)
	browser.quit()