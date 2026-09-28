# parametrize for username and password parameters

import pytest
from playwright.sync_api import Page, Playwright, expect

login_data=[('userone_01@gmail.com','User@123','valid'), # Your test data should tell the test what outcome is expected, valid invalid
            ('qwerty@fmail.com','qwerty','invalid'),]

@pytest.mark.parametrize('username,password,expected_success',login_data)
def test_login(username,password,expected_success,page:Page):
    page.goto('https://demowebshop.tricentis.com/')
    page.locator('.ico-login').click()
    page.locator('#Email').fill(username)
    page.locator('#Password').fill(password)
    page.locator('.button-1.login-button').click()

    if expected_success=='valid':
        # successful login
        name=page.locator("div[class='header-links'] a[class='account']")
        expect(name).to_contain_text(username)

    else:
        # unsuccessful login
        error_message=page.locator('.validation-summary-errors')
        expect(error_message).to_be_visible(timeout=5000)

