from selenium import webdriver
from selenium.webdriver.common.by import By

class Login:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.headless = False
        self.driver = webdriver.Chrome(options=options)

    def login(self, username="standard_user", password="secret_sauce"):
        self.driver.get("https://www.saucedemo.com/")
        user_input = self.driver.find_element(By.ID, "user-name")
        user_input.clear()
        user_input.send_keys(username)

        password_input = self.driver.find_element(By.ID, "password")
        password_input.clear()
        password_input.send_keys(password)

        login_button = self.driver.find_element(By.ID, "login-button")
        login_button.click()

    def tearDown(self):
        self.driver.quit()