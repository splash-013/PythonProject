from time import time

from playwright.sync_api import Page, expect

# page.get_by_alt_name()

def test_verifytitle(page:Page):
    page.goto('https://demo.nopcommerce.com/')
    #time().sleep(5) #seconds
    #page.wait_for_timeout(5000)
    logo=page.get_by_alt_text('nopCommerce demo store')
    #expect(logo).to_be_visible()