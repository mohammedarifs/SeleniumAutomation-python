import pytest
import time
# from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By

# from DemoProject.pages import dashboardPage
from DemoProject.pages.cartPage import Cart
from DemoProject.pages.dashboardPage import Product
from DemoProject.pages.loginPage import LoginPage
from utils.configReader import read_test_data

test_data = read_test_data("testdata.csv")

# first test case
@pytest.mark.VerifyLogin
@pytest.mark.parametrize("row", test_data)
def test_login(Configure,row):
    driver = Configure
    login_page = LoginPage(driver)
    print(row['username'],row['password'])
    login_page.enter_username(row['username'])#execute second
    login_page.enter_password(row['password'])
    login_page.click_login()
    login_page.logout()

@pytest.mark.AddToCart
def test_add_to_cart(Configure):
    driver = Configure
    login_page = LoginPage(driver)
    login_page.enter_username("standard_user")#execute second
    login_page.enter_password("secret_sauce")
    login_page.click_login()
    dashboardPage=Product(driver)
    dashboardPage.click_add_to_cart()
    dashboardPage.goto_cart()
    product_name = dashboardPage.read_product_name()
    assert product_name == "Sauce Labs Bike Light", "product not matching"
    login_page.logout()


@pytest.mark.Checkout
def test_checkout(Configure):
    driver = Configure
    login_page = LoginPage(driver)
    login_page.enter_username("standard_user")#execute second
    login_page.enter_password("secret_sauce")
    login_page.click_login()
    dashboardPage=Product(driver)
    dashboardPage.goto_cart()
    cartPage = Cart(driver)
    cartPage.click_to_checkout()
    cart_tittle = cartPage.get_cart_title()
    assert cart_tittle =="Checkout: Your Information", "unable to read checkout page"
    login_page.logout()



@pytest.mark.PlaceOrder
def test_checkout(Configure):
    driver = Configure
    login_page = LoginPage(driver)
    login_page.enter_username("standard_user")#execute second
    login_page.enter_password("secret_sauce")
    login_page.click_login()
    dashboardPage=Product(driver)
    dashboardPage.goto_cart()
    cartPage = Cart(driver)
    cartPage.click_to_checkout()
    # orderpage.placeOrder()
    cart_tittle = cartPage.get_cart_title()
    assert cart_tittle =="Checkout: Your Information", "unable to read checkout page"
    login_page.logout()