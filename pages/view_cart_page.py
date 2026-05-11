from common.base import Base


class ViewCartPage(Base):
    def __init__(self, page):
        self.page = page
    
    def delete_button(self, index:int = 0):
        return self.locator("a.cart_quantity_delete").nth(index)
    
    
    # actions
    def click_delete_button(self, index:int = 0):
        self.delete_button(index).click()
    
    
    # expects
    def expect_product_exists(self, product_info: dict):
        product_id = product_info["id"]
        row = self.page.locator(f"#product-{product_id}")

        self.expect_visible(row)
        # self.expect(row).to_contain_text(product_info["name"])