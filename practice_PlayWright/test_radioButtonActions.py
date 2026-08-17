import pytest
from playwright.sync_api import Page, expect
def test_radiobuttonactions(page:Page):
    page.goto('https://testautomationpractice.blogspot.com/')
    #page.get_by_label('Male').check() # label won't work here, check ChatGPT
    #page.locator('#male').check()
    #page.get_by_role('radio',name='Male', exact=True).check() #check notes for exact=True

    radio=page.locator('.form-check-input[value=male]')
    expect(radio).not_to_be_checked() # check if it is already checked by default

    radio.check() # .check() is preferred for radio buttons

    #Assertions
    expect(radio).to_be_visible()  # check element is visible
    expect(radio).to_be_enabled()  # check if enabled
    expect(radio).to_be_checked()  # check if it is checked or not
    page.wait_for_timeout(5000)