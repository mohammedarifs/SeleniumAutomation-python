
from selenium.webdriver.common.by import By
from utils import configReader

class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self,value):
        # username = self.driver.find_element(By.ID,)
        # username.send_keys(value)
        username = self.driver.find_element(By.ID, configReader.readconfig("login","username"))
        username.send_keys(value)

    def enter_password(self,value):
        self.driver.find_element(By.ID, configReader.readconfig("login","password")).send_keys(value)

    def click_login(self):
        login = self.driver.find_element(By.ID, configReader.readconfig("login","loginbtn"))
        login.click()

    def logout(self):
        self.driver.find_element(By.ID, configReader.readconfig("login","menubtn")).click()
        self.driver.find_element(By.ID, configReader.readconfig("login","logoutbtn")).click()