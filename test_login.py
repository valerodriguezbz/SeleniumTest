# This an automated test example using auce Labs Demo App (https://www.saucedemo.com/)
# Only for practical purposes
import unittest
from login import Login
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLogin(unittest.TestCase):
    def test_login_success(self):
        # Call the test base
        login_test = Login()
        login_test.login()
        driver = login_test.driver

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((
                By.CLASS_NAME, "inventory_list"
            ))
        )

        self.assertTrue(
            driver.find_element(By.CLASS_NAME, "inventory_list").is_displayed()
        )
        login_test.tearDown()

    def test_login_fail(self):
        login_test = Login()
        login_test.login(username="invalid_user", password="wrong_password")
        driver = login_test.driver

        error_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//*[contains(text(), 'Epic sadface')]"))
        )
        self.assertTrue(error_message.is_displayed())
        login_test.tearDown()

    def test_logout(self):
        login_test = Login()
        login_test.login()
        driver = login_test.driver
        driver.find_element(By.CLASS_NAME,'bm-burger-button').click()
        logout_item= WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="logout_sidebar_link"]')
            )
        )
        logout_item.click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, 'login_wrapper')
            )
        )
        self.assertTrue(driver.find_element(By.CLASS_NAME,'login_wrapper'))
        login_test.tearDown()
