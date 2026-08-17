import pytest
from playwright.sync_api import Page, expect

# Single select drop down

def test_singledropdown(page:Page):
    page.goto('https://testautomationpractice.blogspot.com/')

    # by label
    page.locator('#country').select_option(label='Japan')
    page.locator('#country').select_option('Japan')

    # by value
    #page.get_by_label('Country:').select_option(value='china')
    #page.get_by_label('Country:').select_option('China')

    # by index
    # page.locator('#country').select_option(index=3)

    page.wait_for_timeout(5000)
