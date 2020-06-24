from selenium import webdriver
import unittest
import HtmlTestRunner


class TestPHP(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--window-size=1420,1080')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        cls.driver = webdriver.Chrome("/usr/bin/chromedriver", options=chrome_options)

    def test_about_us_tab(self):
        self.driver.get("http://192.168.56.102:8083")
        self.driver.find_element_by_id("About Us").click()
        self.elem_text = self.driver.find_element_by_id("PID-ab2-pg").text
        assert "This is about page." in self.elem_text

    def test_home_tab(self):
        self.driver.get("http://192.168.56.102:8083")
        self.driver.find_element_by_id("Home").click()
        self.elem_text = self.driver.find_element_by_xpath("/html/body/div/footer/small").text
        assert "2020 Simple PHP Website." in self.elem_text

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="./selenium_reports"))
