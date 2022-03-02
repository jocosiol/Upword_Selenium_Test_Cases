import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


class Upword(unittest.TestCase):

    def setUp(self):
        self.s=Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.s)
        self.actionChains = ActionChains(self.driver)
        self.driver.maximize_window()

    def test_signin_email_pass(self):
        self.driver.get("http://18.223.217.84:8080/login")
        self.driver.find_element(by=By.ID, value="input-12").send_keys("aviram7168+staging@gmail.com")
        self.driver.find_element(by=By.ID, value="input-15").send_keys("123456")
        self.driver.find_element(by=By.ID, value="login-form-btn").click()
        time.sleep(7)
        assert "Welcome" in self.driver.page_source

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
