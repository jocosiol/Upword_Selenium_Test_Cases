from multiprocessing.connection import wait
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.maximize_window()

driver.get("http://18.223.217.84:8080/login")

driver.find_element(by=By.ID, value="input-12").send_keys("aviram7168+staging@gmail.com")
driver.find_element(by=By.ID, value="input-15").send_keys("123456")
driver.find_element(by=By.ID, value="login-form-btn").click()

driver.implicitly_wait(10)

my_folder = driver.find_element(by=By.XPATH, value="//*[@id='nav-drawer']/div[1]/div[5]/div[2]/div/div/div[1]/div/div[2]/div[6]")
my_folder.click()


