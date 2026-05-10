from common.base import Base
from components.product_card import ProductCard
from components.cart_modal import CartModal

class ProductsPage(Base):
    def product(self, index: int = 0) -> ProductCard:
        return ProductCard(self.page, index)
    

    # properties
    @property
    def CART_MODAL(self) -> CartModal:
        return CartModal(self.page)  
    
    
    # actions
    def add_product_to_cart(self, index: int = 0):
        product_card = self.product(index)
        product_card.hover()
        product_card.add_to_cart()
    
    # expects