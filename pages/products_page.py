from common.base import Base
from components.product_card import ProductCard
from components.cart_modal import CartModal

class ProductsPage(Base):
    def __init__(self, page):
        self.page = page
    
    def product(self, index: int = 0) -> ProductCard:
        return ProductCard(self.page, index)
    
    def get_product_ids(self):
        elements = self.page.locator("div.productinfo a.add-to-cart").all()
        return [int(el.get_attribute("data-product-id")) for el in elements]
    

    # properties
    @property
    def CART_MODAL(self) -> CartModal:
        return CartModal(self.page)  
    
    @property
    def SEARCH_INPUT(self):
        return self.page.get_by_placeholder("Search Product")
    
    @property
    def SEARCH_BUTTON(self):
        return self.page.locator("#submit_search")
    
    
    # actions
    def add_product_to_cart(self, index: int = 0):
        product_card = self.product(index)
        product_card.hover()
        product_card.add_to_cart()
    
    def search_product(self, keyword : str):
        self.fill(self.SEARCH_INPUT, keyword)
        self.click(self.SEARCH_BUTTON)
        
    
    # expects
    
    
    # api
    