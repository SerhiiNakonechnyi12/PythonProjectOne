import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# chrome_options = webdriver.ChromeOptions()
chrome_options = Options()
chrome_options.add_argument("--headless")

# Running tests without launching the browser
driver = webdriver.Chrome(options=chrome_options, executable_path="../../drivers/chromedriver")

driver.get("https://www.google.com.ua/?hl=ru")
print(driver.title)
driver.find_element_by_name("q").send_keys("Automation step by step")
time.sleep(1)
driver.find_element_by_name("btnK").click()
print(driver.title)
driver.close()
driver.quit()
print("Completed")