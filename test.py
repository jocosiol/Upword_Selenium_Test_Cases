from multiprocessing.connection import wait
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
actionChains = ActionChains(driver)
driver.maximize_window()

driver.get("http://18.223.217.84:8080/login")

driver.find_element(by=By.ID, value="input-12").send_keys("aviram7168+staging@gmail.com")
driver.find_element(by=By.ID, value="input-15").send_keys("123456")
driver.find_element(by=By.ID, value="login-form-btn").click()
driver.implicitly_wait(15)
driver.find_element(by=By.XPATH, value="//*[@id='nav-drawer']/div[1]/div[5]/div[2]/div/div/div[1]/div/div[2]/div[6]").click()
driver.find_element(by=By.XPATH, value="//*[@id='14793']/div/div/div/div[3]/div[1]/div[2]").click()
driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[3]/div/div/form/div[1]/div/div/div[1]/div/input").send_keys("https://medium.com/gen/russia-ukraine-and-the-revenge-of-geography-85a6a9e0ea78")
driver.find_element(by=By.XPATH, value="//*[@id='app']/div[3]/div/div/form/div[2]/button[2]").click()
driver.implicitly_wait(15)
driver.find_element(by=By.XPATH, value="//*[@id='app-main-frame']/div/div[1]/div/div[1]/div[1]/div[1]/div").click()
driver.find_element(by=By.XPATH, value="//*[@id='nav-drawer']/div[1]/div[5]/div[2]/div/div/div[1]/div/div[2]/div[6]").click()
actionChains.context_click(driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/main/div/div[1]/div[2]/div/div[1]/div/div[2]/div/div/div/div[3]/div[2]")).perform()
driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/main/div/div[1]/div[2]/div/ul[1]/div/div/div/div[4]").click()
