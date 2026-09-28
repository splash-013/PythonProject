from playwright.sync_api import Page, Playwright

class CartPage:
    # LOCATOR
    def __init__(self,page:Page):
        self.page=page
        self.product_name_locator='#tbodyid tr td:nth-child(2)'

    # ACTION METHOD
    def check_product_in_cart(self,product_name):
        products=self.page.locator(self.product_name_locator)
        count=products.count()

        for i in range(count):
            name=products.nth(i).text_content().strip()
            print(name)
            if name==product_name:
                return products.nth(i)
        return None