import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import page



class UpwordTest(unittest.TestCase):

    def setUp(self):
        s = Service("/Users/javiercosio/Documents/UPWORD/Upword_Selenium_Test_Cases/chromedriver")
        self.driver = webdriver.Chrome(service=s)
        self.driver.get("https://app.upword.ai/login")

    # def test_check_page_title(self):
    #     loginPage = page.LoginPage(self.driver)
    #     print(self.driver.title)
    #     assert loginPage.is_title_matched()

    def test_signup(self):
        loginPage = page.LoginPage(self.driver)
        loginPage.click_signup_link()
        signupPage = page.SignupPage(self.driver)
        assert signupPage.is_on_signup_page()

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()




