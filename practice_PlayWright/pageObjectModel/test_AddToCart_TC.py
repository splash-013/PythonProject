import pytest
from playwright.sync_api import Page, expect, Playwright

# IMPORT ALL THE REQUIRED CLASSES FROM THE POM FILES
from loginPage_POM import LoginPage # from pom_file_name import class_name
from homePage_POM import HomePage
from cartPage_POM import CartPage

@pytest.mark.parametrize("username, password,product_name",
                         [("User_001","User@123","Samsung galaxy s6")
                         ])
def test_add_product_to_cart_test_case(page:Page,username,password,product_name):
    page.goto('https://www.demoblaze.com/index.html')

    # LOGIN PAGE
    login_page=LoginPage(page) # LoginPage() OBJECT, this automatically calls the constructor in the login POM class
    # CALL THE FUNCTIONS FORM THE LoginPage POM CLASS
    login_page.click_login()
    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_login_button()

    # HOME PAGE
    home_page=HomePage(page)
    home_page.add_product_to_cart(product_name)
    home_page.goto_cart()
    page.wait_for_timeout(5000)

    # CART PAGE
    cart_page=CartPage(page)
    product_in_cart=cart_page.check_product_in_cart(product_name)
    page.wait_for_timeout(5000)

    # ASSERTION
    expect(product_in_cart).to_be_visible()


