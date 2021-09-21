from selenium import webdriver
import time
import unittest
import HtmlTestRunner

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

from SampleProjects2.Pages.loginPage import LoginPage
from SampleProjects2.Pages.homePage import HomePage


class LoginTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='../../drivers/chromedriver')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_valid(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")

        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()

        homepage = HomePage(driver)
        homepage.click_welcome_link()
        homepage.click_logout_link()

        # driver.find_element_by_id("txtUsername").send_keys("Admin")
        # driver.find_element_by_id("txtPassword").send_keys("admin123")
        # driver.find_element_by_id("btnLogin").click()
        # driver.find_element_by_id("welcome").click()
        # driver.find_element_by_link_text("Logout").click()
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        driver = cls.driver
        driver.close()
        driver.quit()
        print("Test completed")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='../../reports',
                                                           report_name="LoginTestResults_SP2",
                                                           report_title="Unit tests report for SampleProjects2"
                                                           ))
