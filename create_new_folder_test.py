import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


class Upword(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.s=Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.s)
        self.actionChains = ActionChains(self.driver)
        self.driver.maximize_window()
        self.driver.get("http://18.223.217.84:8080/login")
        self.driver.find_element(by=By.ID, value="input-12").send_keys("aviram7168+staging@gmail.com")
        self.driver.find_element(by=By.ID, value="input-15").send_keys("123456")
        self.driver.find_element(by=By.ID, value="login-form-btn").click()
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value="//*[@id='nav-drawer']/div[1]/div[5]/div[2]/div/div/div[1]/div/div[2]/div[6]").click()
        time.sleep(3)

    def test_create_folder_from_button(self):
        self.driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/main/div/div[1]/div[2]/div/div[1]/div/div[2]/div/div/div/div[1]/div[2]/div").click()
        self.driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[3]/div/div/form/div[1]/div/div/div[1]/div/input").send_keys("Test Folder from Button")
        self.driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[3]/div/div/form/div[2]/button[2]").click()
        time.sleep(2)
        assert self.driver.find_elements(by=By.XPATH, value="//*[contains(text(), 'Test Folder from Button')]")
        self.actionChains.context_click(self.driver.find_element(by=By.XPATH, value="//*[contains(text(), 'Test Folder from Button')]")).perform()
        self.driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[1]/div/main/div/div[1]/div[2]/div/ul[1]/div/div/div/div[3]").click()
        time.sleep(3)

    @classmethod
    def tearDownClass(self):
        self.driver.close()
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()



## /html/body/div[1]/div/div/main/div/div[1]/div[2]/div/ul[2] rightclick

### /html/body/div[1]/div/div/main/div/div[1]/div[2]/div/div[1]/div/div[2]/div/div/div/div[1]/div[2]/div