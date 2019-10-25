import os
from selenium import webdriver
import time
import math

browser = webdriver.Chrome()
try:
	link = "http://suninjuly.github.io/alert_accept.html"
	browser.get(link)
	browser.find_element_by_tag_name("button").click()
	browser.switch_to.alert.accept()
	x = int(browser.find_element_by_id("input_value").text)
	result = str(math.log(abs(12*math.sin(int(x)))))
	browser.find_element_by_id("answer").send_keys(result)
	browser.find_element_by_tag_name("button").click()	
finally:
	time.sleep(5)
	browser.quit()