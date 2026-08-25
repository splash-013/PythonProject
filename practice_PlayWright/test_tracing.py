from playwright.sync_api import Playwright, expect

def test_tracing(playwright:Playwright):
    browser=playwright.firefox.launch(headless=False)
    context=browser.new_context()
    page=context.new_page()

    # start tracing
    context.tracing.start(screenshots=True, snapshots=True)

    page.goto('https://www.demoblaze.com/index.html')
    page.locator('#login2').click()
    page.locator('#loginusername').fill('admin')
    page.locator('#loginpassword').fill('admin')
    page.get_by_role("button", name="Log in").click()
    page.wait_for_timeout(5000)
    expect(page.locator('#nameofuser')).to_have_text('Welcome admin')

    # close tracing
    context.tracing.stop(path='trace.zip')


    context.close()
    browser.close()