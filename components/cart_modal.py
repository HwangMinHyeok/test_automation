from playwright.sync_api import expect
import re


class CartModal:
    def __init__(self, page):
        self.page = page
        self.root = page.locator("div#cartModal")

    # properties
    @property
    def VIEW_CART_BUTTON(self):
        return self.root.get_by_role("link", name="View Cart")
    
    @property
    def CONTINUE_SHOPPING_BUTTON(self):
        return self.root.get_by_role("button", name="Continue Shopping")
    
    
    # actions
    def click_continue_shopping(self) -> None:
        self.CONTINUE_SHOPPING_BUTTON.click()
        
    def click_view_cart(self) -> None:
        self.VIEW_CART_BUTTON.click()
        
    
    # expects
    def expect_cart_modal_opened(self) -> None:
        expect(self.root).to_be_visible()
    
    def expect_nav_to_view_cart_page(self) -> None:
        expect(self.page).to_have_url(re.compile(r".*/view_cart$"))
        
    def expect_cart_modal_closed(self) -> None:
        # expect(self.root).not_to_be_visible()
        expect(self.root).to_be_hidden()