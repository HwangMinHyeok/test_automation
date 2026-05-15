from common.base import Base


class ViewCartPage(Base):
    def __init__(self, page):
        self.page = page
    
    def row(self, product_id):
        return self.page.locator(f"#product-{product_id}")
    
    
    # actions
    def click_delete_button(self, product_info):
        self.page.wait_for_url("**/view_cart")
        self.row(product_info["id"]).locator("a.cart_quantity_delete").click()

    
    # expects
    def expect_product_exists(self, product_info):
        self.expect_visible(self.row(product_info["id"]))
    
    def expect_product_not_exists(self, product_info):
        self.expect_not_visible(self.row(product_info["id"]))