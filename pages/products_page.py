from common.base import Base
from components.product_card import ProductCard

class ProductsPage(Base):
    def product(self, index: int) -> ProductCard:
        return ProductCard(self.page.locator("div.single-products").nth(index))
    
    # properties
    @property
    def CART_MODAL(self):
        return self.page.locator("div#cartModal")    
    
    # actions
    
    
    # expects
    def expect_cart_modal_visible(self) -> None:
        self.expect_visible(self.CART_MODAL)