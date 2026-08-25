# install pytest plugin pytes-rerunfailures
# this is used for flaky tests
# syntax: --reruns 3 --reruns-delay 2  rerun test 3 times with delay of 2 secs
# writes this in the terminal

from playwright.sync_api import Playwright, expect

def test_flaky(playwright:Playwright):
    browser=playwright.firefox.launch(headless=False)
    context=browser.new_context()
    page=context.new_page()

    page.goto('https://www.demoblaze.com/index.html')
    page.locator('#login2').click()
    page.wait_for_timeout(3000)
    page.locator('#loginusername').fill('admin')
    page.locator('#loginpassword').fill('admin')
    page.get_by_role("button", name="Log in").click()

    expect(page.locator('#nameofuser')).to_have_text('Welcome admin')
