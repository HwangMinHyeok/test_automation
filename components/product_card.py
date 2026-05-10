from playwright.sync_api import expect

class ProductCard:
    def __init__(self, page, index: int = 0):
        self.root = page.locator("div.single-products").nth(index)
    
    
    # properties    
    @property
    def OVERLAY(self):
        return self.root.locator(".product-overlay")
    
    @property
    def ADD_TO_CART_BUTTON(self):
        return self.OVERLAY.locator("a.add-to-cart")
    
    
    # actions
    def hover(self) -> None:
        self.root.hover()
        
    def add_to_cart(self) -> None:
        self.ADD_TO_CART_BUTTON.click()
        
    
    # expects
    def expect_add_to_cart_visible(self) -> None:
        expect(self.ADD_TO_CART_BUTTON).to_be_visible()