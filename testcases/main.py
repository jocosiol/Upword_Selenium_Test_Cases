import unittest
from selenium import webdriver
import page
from selenium.webdriver.common.by import By




class UpwordTest(unittest.TestCase):
    def setUp(self):
        PATH = "/Users/javiercosio/Documents/UPWORD/Upword_Selenium_Test_Cases/chromedriver"
        self.driver = webdriver.Chrome(PATH)
        self.driver.get("http://18.223.217.84:8080/login")

    # def test_check_page_title(self):
    #     loginPage = page.LoginPage(self.driver)
    #     print(self.driver.title)
    #     assert loginPage.is_title_matched()

    def test_signup(self):
        loginPage = page.LoginPage(self.driver)
        loginPage.driver.find_element(By.LINK_TEXT, "Signup").click()

        #loginPage.click_login_button()

        signupPage = page.SignupPage(self.driver)
        print(self.driver.title)
        # assert signupPage.is_on_signup_page()

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()