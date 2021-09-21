from selenium import webdriver
import unittest
import HtmlTestRunner


class GoogleSearch(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='../drivers/chromedriver')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_search_automation(self):
        self.driver.get("https://www.google.com/")
        self.driver.find_element_by_name("q").send_keys("Automation")
        self.driver.find_element_by_name("btnK").click()
        print(self.driver.title)

    def test_search_serhii(self):
        self.driver.get("https://www.google.com/")
        self.driver.find_element_by_name("q").send_keys("Serhii Nakonechnyi")
        self.driver.find_element_by_name("btnK1").click()
        print(self.driver.title)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/Users/serhii/PycharmProjects/SeleniumTest/reports'))

