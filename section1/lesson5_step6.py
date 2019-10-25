from selenium import webdriver


browser = webdriver.Chrome('/home/user/Documents/stepik575course/chromedriver')
browser.get("http://suninjuly.github.io/huge_form.html")
elems = browser.find_elements_by_tag_name("input")
for elem in elems:
	elem.send_keys("spam")
button = browser.find_element_by_css_selector("button.btn")
button.click()
