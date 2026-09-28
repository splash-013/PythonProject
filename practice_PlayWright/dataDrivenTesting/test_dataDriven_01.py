import pytest
from playwright.sync_api import Playwright, expect, Page

search_items=['laptop','gift card','smartphone','monitor']  # list of items, monitor is not present

@pytest.mark.parametrize('items',search_items) # pre-defined function 'parametrize' in pytest, 'items' variable for search_items list
def test_datadriven(items,page:Page): # add the variable 'items', it will execute each element in the list one by one
    page.goto('https://demowebshop.tricentis.com/')
    page.locator('#small-searchterms').fill(items)
    page.locator('.button-1.search-box-button').click()

    # assertion
    first_item=page.locator('h2 a').nth(0)
    expect(first_item).to_contain_text(items,ignore_case=True)
