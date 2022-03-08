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
        self.driver.get("https://www.upword.ai/")
        self.driver.find_element(by=By.XPATH, value="/html/body/div[3]/header/div[1]/div[1]/nav/nav/div/a/div").click()
        time.sleep(5)

    def test_signin_email_pass(self):
        self.driver.find_element(by=By.ID, value="input-12").send_keys("testmcosio@gmail.com")
        self.driver.find_element(by=By.ID, value="input-15").send_keys("asdf1234!")
        self.driver.find_element(by=By.ID, value="login-form-btn").click()
        time.sleep(10)
        assert "Welcome" in self.driver.page_source

    # def test_signin_google_account(self):
    #     self.driver.find_element(by=By.ID, value="login-google-btn").click()
    #     time.sleep(10)
    #     google = self.driver.switch_to.window(self.driver.window_handles[1])
    #     self.driver.find_element(by=By.ID, value="identifierId").send_keys("testmcosio@gmail.com")
    #     self.driver.find_element(by=By.ID, value="identifierNext").click()
    #     time.sleep(10)




    #     assert "Welcome" in self.driver.page_source


    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
