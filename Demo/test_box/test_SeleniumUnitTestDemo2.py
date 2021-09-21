#! / usr / bin / python
# coding=utf-8
import unittest
from selenium import webdriver
import HtmlTestRunner

class MyTestCase(unittest.TestCase):
    # Для запуска настроек на каждом тесте
    # def setUp(self):
    #     self.driver = webdriver.Chrome(executable_path="../drivers/chromedriver")
    #     self.driver.implicitly_wait(10)
    #     self.driver.maximize_window()

    # Для запуска настоек 1 раз
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="./drivers2/chromedriver")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_search_1(self):
        self.driver.get("https://www.google.com")
        self.driver.find_element_by_name("q").send_keys("Automation step by step")
        self.driver.find_element_by_name("btnK").click()
        x = self.driver.title
        print(x)
        self.assertEqual(x, "Automation step by step - Поиск в Google")

    def test_search_2(self):
        self.driver.get("https://www.google.com")
        self.driver.find_element_by_name("q").send_keys("Serhii")
        self.driver.find_element_by_name("btnK").click()
        x = self.driver.title
        print(x)
        self.assertEqual(x, "Serhii - Поиск в Google")

    @unittest.skip("This is a skipped test.")
    def test_skip(self):
        """ This test should be skipped. """

    # def tearDown(self):
    #     self.driver.close()
    #     self.driver.quit()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/Users/serhii/PycharmProjects/SeleniumTest/reports'))
