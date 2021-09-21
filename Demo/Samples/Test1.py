import time

from selenium import webdriver

driver = webdriver.Chrome("../../drivers/chromedriver")

driver.set_page_load_timeout(10)

driver.get("https://www.google.com.ua/?hl=ru")

driver.find_element_by_name("q").send_keys("Automation step by step")

time.sleep(1)

driver.find_element_by_xpath("//*[@class='gNO89b']").click()

time.sleep(2)

driver.close()
driver.quit()

print("Test Completed")