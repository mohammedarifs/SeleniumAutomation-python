
from utils import configReader
from selenium.webdriver.common.by import By

class Product:
    def __init__(self, driver):
        self.driver = driver

    def click_add_to_cart(self):
        self.driver.find_element(By.ID, configReader.readconfig("dashboard","addtocartbtn")).click()

    def goto_cart(self):
        self.driver.find_element(By.CLASS_NAME, configReader.readconfig("dashboard","cartlink")).click()

    def read_product_name(self):
        return self.driver.find_element(By.CLASS_NAME,configReader.readconfig("dashboard","prouductlbl")).text