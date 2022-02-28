import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import page

class UpwordTest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        s = Service("/Users/javiercosio/Documents/UPWORD/Upword_Selenium_Test_Cases/chromedriver")
        self.driver = webdriver.Chrome(service=s)
        self.driver.get("https://app.upword.ai/login")


    # def test_check_page_title(self):
    #     loginPage = page.LoginPage(self.driver)
    #     print(self.driver.title)
    #     assert loginPage.is_title_matched()

    def test_signup(self):
        loginPage = page.LoginPage(self.driver)
        self.driver.implicitly_wait(10)
        loginPage.click_signup_link()
        self.driver.implicitly_wait(10)
        signupPage = page.SignupPage(self.driver)
        self.driver.implicitly_wait(10)
        assert signupPage.is_on_signup_page()

    @classmethod
    def tearDownClass(self):
        self.driver.close()
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()




