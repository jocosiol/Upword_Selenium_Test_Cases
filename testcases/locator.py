from selenium.webdriver.common.by import By

class LoginPageLocators(object):
    SIGNUP_LINK = (By.LINK_TEXT, "Signup")
    LOGIN_BUTTON = (By.ID, "login-form-btn")
