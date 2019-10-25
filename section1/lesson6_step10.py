from selenium import webdriver
import time


link = "http://suninjuly.github.io/registration2.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element_by_xpath("//div[@class='first_block']/div[contains(@class, 'first_class')]/input[contains(@class, 'first')]")
    input1.send_keys("Alyona")
    input2 = browser.find_element_by_xpath("//div[@class='first_block']/div[contains(@class, 'second_class')]/input[contains(@class, 'second')]")
    input2.send_keys("Shishkina")
    input3 = browser.find_element_by_xpath("//div[@class='first_block']/div[contains(@class, 'third_class')]/input[contains(@class, 'third')]")
    input3.send_keys("test@test.ru")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(1)
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text
finally:
    time.sleep(5)
    browser.quit()
