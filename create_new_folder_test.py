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
        self.driver.get("https://www.upword.ai/")
        self.driver.find_element(by=By.XPATH, value="/html/body/div[3]/header/div[1]/div[1]/nav/nav/div/a/div").click()
        self.driver.find_element(by=By.ID, value="input-12").send_keys("testmcosio@gmail.com")
        self.driver.find_element(by=By.ID, value="input-15").send_keys("asdf1234!")
        self.driver.find_element(by=By.ID, value="login-form-btn").click()
        time.sleep(10)

    def test_create_folder_from_button(self):
        self.driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/main/div/div[1]/div[2]/div/div[1]/div/div[2]/div/div/div/div[1]/div[2]/div").click()
        self.driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[3]/div/div/form/div[1]/div/div/div[1]/div/input").send_keys("AA - Test Folder from rigth click")
        self.driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[3]/div/div/form/div[2]/button[2]").click()
        time.sleep(2)
        assert self.driver.find_elements(by=By.XPATH, value="//*[contains(text(), 'AA - Test Folder from rigth click')]")
        self.actionChains.context_click(self.driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[1]/div/main/div/div[1]/div[2]/div/div[1]/div/div[2]/div/div/div/div[1]/div[2]/div[2]")).perform()
        self.driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[1]/div/main/div/div[1]/div[2]/div/ul[1]/div/div/div/div[3]").click()
        time.sleep(3)
    
    def test_create_folder_by_rigth_click(self):
        self.actionChains.context_click(self.actionChains.move_by_offset(600,150).perform()).perform()
        self.driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[1]/div/main/div/div[1]/div[2]/div/ul[2]/div").click()
        self.driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[3]/div/div/form/div[1]/div/div/div[1]/div/input").send_keys("BB - Test Folder from Button")
        self.driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[3]/div/div/form/div[2]/button[2]").click()
        time.sleep(2)
        assert self.driver.find_elements(by=By.XPATH, value="//*[contains(text(), 'BB - Test Folder from Button')]")
        self.actionChains.context_click(self.driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[1]/div/main/div/div[1]/div[2]/div/div[1]/div/div[2]/div/div/div/div[1]/div[2]/div[2]")).perform()
        self.driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[1]/div/main/div/div[1]/div[2]/div/ul[1]/div/div/div/div[3]").click()
        time.sleep(3)

    def test_create_subfolder_by_button(self):
        self.driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/main/div/div[1]/div[2]/div/div[1]/div/div[2]/div/div/div/div[1]/div[2]/div").click()
        self.driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[3]/div/div/form/div[1]/div/div/div[1]/div/input").send_keys("CC - Test Folder from Button")
        self.driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[3]/div/div/form/div[2]/button[2]").click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[1]/div/main/div/div[1]/div[2]/div/div[1]/div/div[2]/div/div/div/div[1]/div[2]/div[2]").click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/main/div/div[1]/div[2]/div/div[1]/div/div[2]/div/div/div/div[1]/div[2]/div").click()
        self.driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[3]/div/div/form/div[1]/div/div/div[1]/div/input").send_keys("cc - Test Subfolder from Button")
        self.driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[3]/div/div/form/div[2]/button[2]").click()
        time.sleep(2)
        assert self.driver.find_elements(by=By.XPATH, value="//*[contains(text(), 'cc - Test Subfolder from Button')]")
        self.driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[1]/div/main/div/div[1]/div[2]/div/div[1]/div/div[1]/ul/li[1]/div").click()
        time.sleep(2)
        self.actionChains.context_click(self.driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[1]/div/main/div/div[1]/div[2]/div/div[1]/div/div[2]/div/div/div/div[1]/div[2]/div[2]")).perform()
        self.driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[1]/div/main/div/div[1]/div[2]/div/ul[1]/div/div/div/div[3]").click()
        time.sleep(3)

    def test_create_subfolder_by_rigth_click(self):
        self.actionChains.context_click(self.actionChains.move_by_offset(1,1).perform()).perform()
        self.driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[1]/div/main/div/div[1]/div[2]/div/ul[2]/div").click()
        self.driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[3]/div/div/form/div[1]/div/div/div[1]/div/input").send_keys("DD - Test Folder from Rigth Click")
        self.driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[3]/div/div/form/div[2]/button[2]").click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[1]/div/main/div/div[1]/div[2]/div/div[1]/div/div[2]/div/div/div/div[1]/div[2]/div[2]").click()
        time.sleep(3)
        self.actionChains.context_click(self.actionChains.move_by_offset(1,1).perform()).perform()
        self.driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[1]/div/main/div/div[1]/div[2]/div/ul[2]/div").click()
        self.driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[3]/div/div/form/div[1]/div/div/div[1]/div/input").send_keys("dd - Test Subfolder from Rigth Click")
        self.driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[3]/div/div/form/div[2]/button[2]").click()
        time.sleep(1)
        assert self.driver.find_elements(by=By.XPATH, value="//*[contains(text(), 'dd - Test Subfolder from Rigth Click')]")
        self.driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[1]/div/main/div/div[1]/div[2]/div/div[1]/div/div[1]/ul/li[1]/div").click()
        time.sleep(1)
        self.actionChains.context_click(self.driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[1]/div/main/div/div[1]/div[2]/div/div[1]/div/div[2]/div/div/div/div[1]/div[2]/div[2]")).perform()
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