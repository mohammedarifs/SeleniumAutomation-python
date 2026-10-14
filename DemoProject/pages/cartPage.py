from utils import configReader
from selenium.webdriver.common.by import By

class Cart:
    def __init__(self, driver):
        self.driver = driver

    def click_to_checkout(self):
        self.driver.find_element(By.ID, configReader.readconfig("cart","checkout")).click()


    def get_cart_title(self):
        return self.driver.find_element(By.CLASS_NAME, configReader.readconfig("cart","carttitle")).text
