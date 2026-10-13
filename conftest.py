from asyncio import timeout

import pytest
# import time
# from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture()
def setup():
    global driver
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.saucedemo.com/")
    driver.implicitly_wait(10)
    yield driver  #in you mentoined yield
    driver.quit()
    # print("run at the end")

@pytest.fixture
def teardown():
    print("run teardown")
@pytest.fixture
def session_start():
    print("run session_start")

@pytest.fixture
def session_finish():
    print("run session_stop")


@pytest.fixture
def secondtestfix():
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.saucedemo.com/")
    driver.implicitly_wait(10)  #execute first
    driver.maximize_window()
    yield driver
    driver.close()#execute third
