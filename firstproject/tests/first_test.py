import pytest
import time
# from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By

# from firstproject.pages import dashboardPage
from firstproject.pages.cartPage import Cart
from firstproject.pages.dashboardPage import Product
from firstproject.pages.loginPage import LoginPage


# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC




@pytest.mark.secondlogin
def test_login_second(secondtestfix):
    driver = secondtestfix
    login_page = LoginPage(driver)
    login_page.enter_username("standard_user")#execute second
    login_page.enter_password("secret_sauce")
    login_page.click_login()
    login_page.logout()

@pytest.mark.secondaddtocart
def test_add_to_cart(secondtestfix):
    driver = secondtestfix
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


@pytest.mark.secondCheckout
def test_checkout(secondtestfix):
    driver = secondtestfix
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
