# This an automated test example using auce Labs Demo App (https://www.saucedemo.com/)
# Only for practical purposes
import unittest
from login import Login
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class TestProductsFilter(unittest.TestCase):
    # Login first
    def setUp(self):
        login_test=Login()
        login_test.login()
        self.driver=login_test.driver

    # After the login, test the filters (Name A-z)
    def test_filter_name_asc(self):
        list_names=[]
        driver = self.driver
        driver.get("https://www.saucedemo.com/inventory.html")
        products_container = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, 'inventory_list')
            )
        )
        # select the filter and get all the names into an array
        select_filter=Select(driver.find_element(By.CLASS_NAME,'product_sort_container'))
        select_filter.select_by_value('az')

        products=products_container.find_elements(By.CLASS_NAME,'inventory_item')
        if(len(products)> 0):
            for p in products:
                name= p.find_element(By.CLASS_NAME,'inventory_item_name').text
                list_names.append(name)

        # This will tell if the filter is correct the test will pass or not.
        True if (list_names==sorted(list_names)) else False

    # After the login, test the filters (Name Z-a)
    def test_filter_name_desc(self):
        list_names=[]
        driver = self.driver
        driver.get("https://www.saucedemo.com/inventory.html")
        products_container = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, 'inventory_list')
            )
        )
        # select the filter and get all the names into an array
        select_filter=Select(driver.find_element(By.CLASS_NAME,'product_sort_container'))
        select_filter.select_by_value('za')

        products=products_container.find_elements(By.CLASS_NAME,'inventory_item')
        if(len(products)> 0):
            for p in products:
                name= p.find_element(By.CLASS_NAME,'inventory_item_name').text
                list_names.append(name)

        # This will tell if the filter is correct the test will pass or not.
        True if (list_names==sorted(list_names, reverse=True)) else False

    # After the login, test the filters (Price low-high)
    def test_filter_price_asc(self):
        list_prices=[]
        driver = self.driver
        driver.get("https://www.saucedemo.com/inventory.html")
        products_container = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, 'inventory_list')
            )
        )
        # select the filter and get all the prices into an array
        select_filter=Select(driver.find_element(By.CLASS_NAME,'product_sort_container'))
        select_filter.select_by_value('lohi')

        products=products_container.find_elements(By.CLASS_NAME,'inventory_item')
        if(len(products)> 0):
            for p in products:
                price= p.find_element(By.CLASS_NAME,'inventory_item_price').text
                price= price.replace('$',"",1) # we delete $
                list_prices.append(price)

        # This will tell if the filter is correct the test will pass or not.
        True if (list_prices==sorted(list_prices)) else False

    # After the login, test the filters (Price high-low)
    def test_filter_price_desc(self):
        list_prices=[]
        driver = self.driver
        driver.get("https://www.saucedemo.com/inventory.html")
        products_container = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, 'inventory_list')
            )
        )
        # select the filter and get all the names into an array
        select_filter=Select(driver.find_element(By.CLASS_NAME,'product_sort_container'))
        select_filter.select_by_value('hilo')

        products=products_container.find_elements(By.CLASS_NAME,'inventory_item')
        if(len(products)> 0):
            for p in products:
                price= p.find_element(By.CLASS_NAME,'inventory_item_price').text
                price= price.replace('$',"",1) # we delete $
                list_prices.append(price)

        # This will tell if the filter is correct the test will pass or not.
        True if (list_prices==sorted(list_prices, reverse=True)) else False

    def tearDown(self):
        self.driver.quit()

if __name__=='__main__':
    unittest.main()