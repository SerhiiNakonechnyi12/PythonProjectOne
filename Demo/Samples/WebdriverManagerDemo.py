import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


# driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

driver.get("https://www.google.com.ua/?hl=ru")
time.sleep(2)
driver.close()
driver.quit()