from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="../../drivers/chromedriver")
# Implicit Waits (Wait on time 4 second or eth. with check every 500 ms)
# driver.implicitly_wait(4)

driver.get("https://www.google.com/")

driver.find_element_by_name("q").send_keys("Automation")

wait = WebDriverWait(driver, 10)
try:
    # Explicit Waits (wait with condition)
    element = wait.until(EC.element_to_be_clickable((By.NAME, "btnK")))
    print("element is clickable")
except:
    print("element is not clickable")
    exit(1)

element.click()

# driver.find_element_by_name("btnK").click()

print("Test Completed")
driver.close()
driver.quit()
