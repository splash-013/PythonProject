from playwright.sync_api import Page, expect

def test_textbox(page:Page):
    page.goto('https://testautomationpractice.blogspot.com/')
    page.locator('#name').fill('Palash') # .fill is used to add text or data
    # page.get_by_placeholder('Enter Name').fill('Palash')
    #page.get_by_lable('Name:').fill(''Palash) # lable wont work here, check chatgpt

    page.get_by_placeholder('Enter EMail').fill('user@gmail.com')
    phone=page.locator('#phone')
    phone.fill('9545813888')

    #Assertions
    expect(phone).to_be_visible() # check element is visible
    expect(phone).to_be_enabled() # check if enabled

    page.wait_for_timeout(5000)