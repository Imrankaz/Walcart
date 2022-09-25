import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# from selenium import *

import pytest



@pytest.fixture()
def test_firefoxDriver():
    global driver
    driver = webdriver.Firefox(executable_path="D:\study2\walcart\git\Walcart\Automation\Webdriver\geckodriver.exe")
    driver.maximize_window()
    driver.delete_all_cookies()
    # driver.get(login_page_url)

    # go to login page
    driver.get("https://www.walcart.com/customer/account/login/referer/aHR0cHM6Ly93d3cud2FsY2FydC5jb20vY3VzdG9tZXIvYWNjb3VudC9sb2dvdXRTdWNjZXNzLw%2C%2C/")
    time.sleep(5)

    # login using mobile number
    driver.find_element(By.XPATH,"//input[@id='mobile']").send_keys("01680064381")
    driver.find_element(By.XPATH,"//fieldset[@class='fieldset login']//button[@type='button']//span[text()='CONTINUE']").click()
    time.sleep(5)

    # Took to another page and input password, then press sign button
    driver.find_element(By.XPATH, "//input[@id='pass']").send_keys("edcn[4Yy")
    driver.find_element(By.XPATH, "//fieldset[@class='fieldset login']//button[@type='button']//span[text()='SIGN IN']").click()
    time.sleep(5)



    yield

    # clear previous orders from  https://www.walcart.com/checkout/cart/
    driver.get("https://www.walcart.com/checkout/cart/")
    time.sleep(5)
    #RemoveBaskets
    # driver.find_element(By.XPATH,"//div[@class='column main']//tbody[@class='cart item']//tr[@class='item-actions item-actions-top']//a[@title='Remove']").click()
    # time.sleep(5)

    #print("ggggggggggggggggggggggggggggggggggg")
    countRemoveBaskets = driver.find_element(By.XPATH, "//div[@class='column main']//tbody[@class='cart item']//tr[@class='item-actions item-actions-top']//a[@title='Remove']").is_displayed()
    print(countRemoveBaskets)
    time.sleep(5)

    if countRemoveBaskets == True :
        driver.find_element(By.XPATH,"//div[@class='column main']//tbody[@class='cart item']//tr[@class='item-actions item-actions-top']//a[@title='Remove']").click()
        time.sleep(5)

    driver.close()
    driver.quit()


def test_task_for_Successful_AddToCart(test_firefoxDriver):

    # go to a product page
    driver.get("https://www.walcart.com/unimart-80011.html")
    time.sleep(5)
    # click on "Add to Cart"
    driver.find_element(By.XPATH, "//div[@class='sticky-addcart-wrap']//button[@id='product-addtocart-button']").click()
    time.sleep(5)

    # click on "View Cart"
    driver.find_element(By.XPATH, "//div[@class='cart-sum-wrap']//a[@class='action primary viewcart']").click()
    time.sleep(5)

    # assert url == "https://www.walcart.com/checkout/cart/"
    actual_URL = driver.current_url

    if actual_URL == "https://www.walcart.com/checkout/cart/":
        assert True
    else:
        assert False




def test_task_for_Successful_ProceedToCheckout(test_firefoxDriver):

    # go to a product page
    driver.get("https://www.walcart.com/unimart-80011.html")
    time.sleep(5)
    # click on "Add to Cart"
    driver.find_element(By.XPATH, "//div[@class='sticky-addcart-wrap']//button[@id='product-addtocart-button']").click()
    time.sleep(5)

    # click on "View Cart"
    driver.find_element(By.XPATH, "//div[@class='cart-sum-wrap']//a[@class='action primary viewcart']").click()
    time.sleep(5)

    # assert url == "https://www.walcart.com/checkout/cart/"


    # click on "Proceed to Checkout"
    driver.find_element(By.XPATH, "//div[@class='cart-container']//button[@class='action primary checkout']").click()
    time.sleep(5)

    # assert url == "https://www.walcart.com/checkout/#shipping"
    actual_URL = driver.current_url

    if actual_URL == "https://www.walcart.com/checkout/#shipping":
        assert True
    else:
        assert False


def test_task_for_Successful_ReviewAndPayments(test_firefoxDriver):

    # go to a product page
    driver.get("https://www.walcart.com/unimart-80011.html")
    time.sleep(5)
    # click on "Add to Cart"
    driver.find_element(By.XPATH, "//div[@class='sticky-addcart-wrap']//button[@id='product-addtocart-button']").click()
    time.sleep(5)

    # click on "View Cart"
    driver.find_element(By.XPATH, "//div[@class='cart-sum-wrap']//a[@class='action primary viewcart']").click()
    time.sleep(5)

    # assert url == "https://www.walcart.com/checkout/cart/"


    # click on "Proceed to Checkout"
    driver.find_element(By.XPATH, "//div[@class='cart-container']//button[@class='action primary checkout']").click()
    time.sleep(5)

    # click on "Next" and take to payment page
    driver.find_element(By.XPATH, "//div[@class='main-wrap col-12']//ol[@id='checkoutSteps']//button[@type='submit']/span[text()='Next']").click()
    time.sleep(5)

    # assert url == "https://www.walcart.com/checkout/#payment"
    actual_URL = driver.current_url

    if actual_URL == "https://www.walcart.com/checkout/#payment":
        assert True
    else:
        assert False





