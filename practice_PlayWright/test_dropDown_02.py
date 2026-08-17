import pytest
from playwright.sync_api import Page, expect

def test_multidropdown(page:Page):
    page.goto('https://testautomationpractice.blogspot.com/')

    # by labels
    #page.locator('#colors').select_option(label=['Red','Green','Blue'])
    #page.locator('#colors').select_option(['Red','Green','Blue'])

    # by values
    #page.get_by_label('Colors:').select_option(value=['red','white','yellow'])
    #page.get_by_label('Colors:').select_option(['red','green','yellow'])

    # by index
    page.locator('#colors').select_option(index=[3,4,5])








    page.wait_for_timeout(5000)