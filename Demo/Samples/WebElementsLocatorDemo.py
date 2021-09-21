import time

from selenium import webdriver

driver = webdriver.Chrome("../../drivers/chromedriver")

driver.get("https://www.google.com.ua/?hl=ru")

searchBox = driver.find_element_by_name("q")

searchBox.send_keys("Hello")

time.sleep(2)
driver.close()
driver.quit()