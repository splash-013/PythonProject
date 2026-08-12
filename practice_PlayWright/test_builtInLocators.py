#from time

from playwright.sync_api import Page, expect




def test_verify_elements(page:Page):
    page.goto('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    #time.sleep(5) #seconds wait in python
    #page.wait_for_timeout(5000) #wait in playwright

    # page.get_by_alt_name(), this is used for images
    # logo=page.get_by_alt_text('company-branding')
    # expect(logo).to_be_visible()
    #expect(page.get_by_alt_text('company-branding')).to_be_visible()

    # page.get_by_test()
    #expect(page.get_by_text("Login")).to_be_visible()



