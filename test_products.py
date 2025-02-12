# This an automated test example using auce Labs Demo App (https://www.saucedemo.com/)
# Only for practical purposes
import unittest
from login import Login
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestProducts(unittest.TestCase):
    # Login first
    def setUp(self):
        login_test = Login()
        login_test.login()
        self.driver = login_test.driver

    # After the login, test if the products are displayed
    def test_products_visibility(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/inventory.html")
        products_conatiner = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, 'inventory_list')
            )
        )
        products = products_conatiner.find_elements(By.CLASS_NAME, 'inventory_item')
        self.assertGreater(len(products), 0, "No hay productos")

    # After the login, test if the product detail is displayed
    def test_product_details(self):
        product = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, 'inventory_item_img')
            )
        )
        product.click()
        self.driver.back()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()