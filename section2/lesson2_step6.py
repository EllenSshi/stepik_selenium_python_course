from selenium import webdriver
import time
import math

browser = webdriver.Chrome()
try:
	link = "http://suninjuly.github.io/execute_script.html"
	browser.get(link)
	x = int(browser.find_element_by_id("input_value").text)
	result = math.log(abs(12*math.sin(x)))
	answer_field = browser.find_element_by_id("answer")
	browser.execute_script("return arguments[0].scrollIntoView(true);", answer_field)
	answer_field.send_keys(str(result))
	browser.find_element_by_id("robotCheckbox").click()
	browser.find_element_by_id("robotsRule").click()
	browser.find_element_by_tag_name("button").click()
finally:
	time.sleep(5)
	browser.quit()