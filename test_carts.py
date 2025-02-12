# This an automated test example using auce Labs Demo App (https://www.saucedemo.com/)
# Only for practical purposes
import unittest
from login import Login
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

class TestCart(unittest.TestCase):
    # Login first
    def setUp(self):
        login_test=Login()
        login_test.login()
        self.driver=login_test.driver
    
    # Auxiliar functions for this test
    #  Add products to cart
    def add_products_cart(self):
        driver=self.driver
        driver.get("https://www.saucedemo.com/inventory.html")
        products_container = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, 'inventory_list')
            )
        )
        products=products_container.find_elements(By.CLASS_NAME,'inventory_item')
        if(len(products)> 0):
            for p in products:
                btn_add_to_cart= p.find_element(By.CLASS_NAME,'btn_inventory')
                btn_add_to_cart.click()
    
    # Form for the cart
    def checkout_form(self, first_name, last_name, postal_code):
        first_name_input= self.driver.find_element(By.ID,'first-name')
        first_name_input.clear()
        last_name_input= self.driver.find_element(By.ID,'last-name')
        last_name_input.clear()
        postal_code_input= self.driver.find_element(By.ID,'postal-code')
        postal_code_input.clear()

        first_name_input.send_keys(first_name)
        last_name_input.send_keys(last_name)
        postal_code_input.send_keys(postal_code)
        self.driver.find_element(By.ID,'continue').click()
     
        
    def test_cart_count(self):
        self.add_products_cart()
        cart_count=self.driver.find_element(By.CLASS_NAME,'shopping_cart_badge').text
        self.assertEqual(cart_count,'6')
    
    def test_details_cart(self):
        self.add_products_cart()
        self.driver.find_element(By.CLASS_NAME,'shopping_cart_link').click()
        cart_container = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, 'cart_list')
            )
        )
        carts_products=cart_container.find_elements(By.CLASS_NAME,'cart_item')
        carts_products[0].find_element(By.CLASS_NAME, 'inventory_item_name').click()
        self.driver.back()

    def test_delete_cart(self):
        self.add_products_cart()
        self.driver.find_element(By.CLASS_NAME,'shopping_cart_link').click()
        cart_container = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, 'cart_list')
            )
        )
        carts_products=cart_container.find_elements(By.CLASS_NAME,'cart_item')
        if(len(carts_products)> 0):
            for p in carts_products:
                try:
                    WebDriverWait(self.driver,5).until(
                        EC.visibility_of_element_located(
                            (By.CLASS_NAME, 'inventory_item_name')
                        )
                    )
                    btn_click=p.find_element(By.CLASS_NAME, 'cart_button')
                    btn_click.click()
                except NoSuchElementException:
                    False
    
    def test_checkout_cart_success(self):
        self.add_products_cart()
        self.driver.find_element(By.CLASS_NAME,'shopping_cart_link').click()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, 'cart_list')
            )
        )
        self.driver.find_element(By.ID,'checkout').click()
        self.checkout_form(first_name='Ana Test', last_name='Morgan',postal_code='11111')
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, 'summary_info')
            )
        )
        self.assertTrue(
            self.driver.find_element(By.CLASS_NAME, "summary_info").is_displayed() and
            self.driver.find_element(By.CLASS_NAME, "summary_value_label").is_displayed() and
            self.driver.find_element(By.CLASS_NAME, "summary_subtotal_label").is_displayed() and
            self.driver.find_element(By.CLASS_NAME, "summary_tax_label").is_displayed() and
            self.driver.find_element(By.CLASS_NAME, "summary_total_label").is_displayed()
        )

    def test_checkout_cart_fail_first_name(self):
        self.add_products_cart()
        self.driver.find_element(By.CLASS_NAME,'shopping_cart_link').click()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, 'cart_list')
            )
        )
        self.driver.find_element(By.ID,'checkout').click()
        self.checkout_form(first_name='', last_name='Morgan',postal_code='11111')
        error_message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, '//*[@id="checkout_info_container"]/div/form/div[1]/div[4]'))
        )
        self.assertTrue(error_message.is_displayed())

    def test_checkout_cart_fail_last_name(self):
        self.add_products_cart()
        self.driver.find_element(By.CLASS_NAME,'shopping_cart_link').click()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, 'cart_list')
            )
        )
        self.driver.find_element(By.ID,'checkout').click()
        self.checkout_form(first_name='Ana Test', last_name='',postal_code='11111')
        error_message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, '//*[@id="checkout_info_container"]/div/form/div[1]/div[4]'))
        )
        self.assertTrue(error_message.is_displayed())
    
    def test_checkout_cart_fail_postal_code(self):
        self.add_products_cart()
        self.driver.find_element(By.CLASS_NAME,'shopping_cart_link').click()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, 'cart_list')
            )
        )
        self.driver.find_element(By.ID,'checkout').click()
        self.checkout_form(first_name='Ana Test', last_name='Morgan',postal_code='')
        error_message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, '//*[@id="checkout_info_container"]/div/form/div[1]/div[4]'))
        )
        self.assertTrue(error_message.is_displayed())

    def test_checkout_cart_fail_no_anyField(self):
        self.add_products_cart()
        self.driver.find_element(By.CLASS_NAME,'shopping_cart_link').click()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, 'cart_list')
            )
        )
        self.driver.find_element(By.ID,'checkout').click()
        self.checkout_form(first_name='', last_name='',postal_code='')
        error_message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, '//*[@id="checkout_info_container"]/div/form/div[1]/div[4]'))
        )
        self.assertTrue(error_message.is_displayed())

    def tearDown(self):
        self.driver.quit()

if __name__=='__main__':
    unittest.main()