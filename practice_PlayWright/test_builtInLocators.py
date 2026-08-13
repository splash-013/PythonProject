#from time

from playwright.sync_api import Page, expect

def test_verify_elements(page:Page):
    page.goto('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    #time.sleep(5) #seconds wait in python
    page.wait_for_timeout(5000) #wait in playwright

    # 1) page.get_by_alt_text(), this is used for images
    # logo=page.get_by_alt_text('company-branding')
    # expect(logo).to_be_visible()
    # expect(page.get_by_alt_text('company-branding')).to_be_visible()

    # 2) page.get_by_text()
    # expect(page.get_by_text("Login")).to_be_visible()

    # 3) page.get_by_role()
    # page.get_by_role("button", name="Login").click()
    # #syntax - .get_by_role('role', name='name')

    # 4) page.get_by_label()
    # page.get_by_label('Username')

    # 5) page.get_by_placeholder()
    # page.get_by_placeholder('Username').fill('Admin')

    # 6) page.get_by_title()

    page.get_by_placeholder('Username').fill('Admin')
    page.wait_for_timeout(3000)
    page.get_by_placeholder('Password').fill('admin123')
    page.wait_for_timeout(3000)
    page.get_by_role("button", name="Login").click()
    page.wait_for_timeout(3000)





