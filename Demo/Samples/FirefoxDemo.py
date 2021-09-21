import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

firefox_options = webdriver.FirefoxOptions()
# firefox_options.add_argument("--headless")

path = "../../drivers/geckodriver"
driver = webdriver.Firefox(executable_path=path, options=firefox_options)

driver.get("https://www.google.com.ua/?hl=ru")
driver.find_element_by_name("q").send_keys("Automation step by step")

time.sleep(1)

driver.find_element_by_name("btnK").send_keys(Keys.ENTER)

print(driver.title)

driver.close()
driver.quit()