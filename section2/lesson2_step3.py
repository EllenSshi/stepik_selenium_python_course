from selenium import webdriver
from selenium.webdriver.support.ui import Select
import math
import time


def calc(x,y):
	return str(x+y)
link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
try:
	browser.get(link)
	x = browser.find_element_by_id("num1").text
	y = browser.find_element_by_id("num2").text
	result = calc(int(x),int(y))
	select = Select(browser.find_element_by_tag_name("select"))
	select.select_by_visible_text(result)
	button = browser.find_element_by_css_selector("button.btn")
	button.click()	
finally:
	time.sleep(10)
	browser.quit()