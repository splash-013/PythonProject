from playwright.sync_api import Playwright, Page, expect
import json
import pytest

# Read json file
file=open('D:/PythonProject/testData/data.json','r')
# Load json file
login_data=json.load(file)

@pytest.mark.parametrize('username,password,expected_success',
                         [
                             (data['username'], data['password'], data['expected_success'])
                             for data in login_data
                         ]
                         )

def test_login_json(username, password, expected_success,page):
    page.goto('https://demowebshop.tricentis.com/')
    page.locator('.ico-login').click()
    page.locator('#Email').fill(username)
    page.locator('#Password').fill(password)
    page.locator('.button-1.login-button').click()