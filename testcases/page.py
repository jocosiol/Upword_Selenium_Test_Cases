from locator import *

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

class LoginPage(BasePage):

    def is_title_matched(self):
        return "Upword" in self.driver.title
    
    def click_signup_link(self):
        link = self.driver.find_element(*LoginPageLocators.SIGNUP_LINK)
        link.click()
    
    def click_login_button(self):
        element = self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON)
        element.click()




class SignupPage(BasePage):
    
    def is_on_signup_page(self):
        return "Sign Up" in self.driver.page_source
