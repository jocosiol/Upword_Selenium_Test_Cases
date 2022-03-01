import unittest
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

    def test_new_article_from_url(self):
        self.driver.get("http://18.223.217.84:8080/login")
        self.driver.find_element(by=By.ID, value="input-12").send_keys("aviram7168+staging@gmail.com")
        self.driver.find_element(by=By.ID, value="input-15").send_keys("123456")
        self.driver.find_element(by=By.ID, value="login-form-btn").click()
        self.driver.implicitly_wait(20)
        self.driver.find_element(by=By.XPATH, value="//*[@id='nav-drawer']/div[1]/div[5]/div[2]/div/div/div[1]/div/div[2]/div[6]").click()
        self.driver.find_element(by=By.XPATH, value="//*[@id='14793']/div/div/div/div[3]/div[1]/div[2]").click()
        self.driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[3]/div/div/form/div[1]/div/div/div[1]/div/input").send_keys("https://medium.com/gen/russia-ukraine-and-the-revenge-of-geography-85a6a9e0ea78")
        self.driver.find_element(by=By.XPATH, value="//*[@id='app']/div[3]/div/div/form/div[2]/button[2]").click()
        self.driver.implicitly_wait(15)
        self.driver.find_element(by=By.XPATH, value="//*[@id='app-main-frame']/div/div[1]/div/div[1]/div[1]/div[1]/div").click()
        self.driver.find_element(by=By.XPATH, value="//*[@id='nav-drawer']/div[1]/div[5]/div[2]/div/div/div[1]/div/div[2]/div[6]").click()
        self.actionChains.context_click(self.driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/main/div/div[1]/div[2]/div/div[1]/div/div[2]/div/div/div/div[3]/div[2]")).perform()
        self.driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/main/div/div[1]/div[2]/div/ul[1]/div/div/div/div[4]").click()

    @classmethod
    def tearDownClass(self):
        self.driver.close()
        self.driver.quit()
        print("Test completed")

if __name__ == "__main__":
    unittest.main()
