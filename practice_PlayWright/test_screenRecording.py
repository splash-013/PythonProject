from playwright.sync_api import Playwright, expect

def test_screen_record(playwright:Playwright):
    browser=playwright.webkit.launch(headless=False)
    context=browser.new_context(
        record_video_dir='videos/',
        record_video_size={"width":1024, 'height':768} #optional
    )
    page=context.new_page()

    page.goto('https://www.demoblaze.com/index.html')
    page.locator('#login2').click()
    page.locator('#loginusername').fill('admin')
    page.locator('#loginpassword').fill('admin')
    page.get_by_role("button", name="Log in").click()
    page.wait_for_timeout(5000)
    expect(page.locator('#nameofuser')).to_have_text('Welcome admin')

    context.close()
    browser.close()
