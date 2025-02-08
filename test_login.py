# This an automated test example using auce Labs Demo App (https://www.saucedemo.com/)
# Only for practical purposes
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Login(unittest.TestCase):
    def setUp(self):
        options=webdriver.ChromeOptions()
        options.headless=False
        self.driver=webdriver.Chrome(options=options)
    
    # This test tries to showcase a succesfull login
    def test_login(self):
        driver=self.driver
        driver.get("https://www.saucedemo.com/")
        username = driver.find_element(By.ID, "user-name")
        username.clear()
        password = driver.find_element(By.ID,"password")
        password.clear()

        username.send_keys("standard_user")
        username.send_keys(Keys.RETURN)
        password.send_keys("secret_sauce")
        password.send_keys(Keys.RETURN)
        time.sleep(3)

        login_button=driver.find_element(By.ID, "login-button")
        login_button.click()
        time.sleep(4)
    
    # This test tries to showcase a failed login
    def test_login_fail(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        username = driver.find_element(By.ID, "user-name")
        username.clear()
        password = driver.find_element(By.ID, "password")
        password.clear()

        username.send_keys("invalid_user")
        password.send_keys("wrong_password")
        login_button = driver.find_element(By.ID, "login-button")
        login_button.click()
        time.sleep(3)
        
        error_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//*[contains(text(), 'Epic sadface')]")))
        self.assertTrue(error_message.is_displayed())

    
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()