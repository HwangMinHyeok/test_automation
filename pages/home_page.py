from common.base import Base

class HomePage(Base):
    # properties
    @property
    def SIGNUP_LOGIN_BUTTON(self):
        return self.page.get_by_role("link", name="Signup / Login")
    
    @property
    def LOGOUT_BUTTON(self):
        return self.page.get_by_role("link", name="Logout")
    
    @property
    def PRODUCTS_BUTTON(self):
        return self.page.get_by_role("link", name="Products")
    
    @property
    def CART_BUTTON(self):
        return self.page.get_by_role("link", name="Cart")
    
    
    # actions
    def click_signup_login_button(self):
        self.click(self.SIGNUP_LOGIN_BUTTON)
        
    def click_products_button(self):
        self.click(self.PRODUCTS_BUTTON)
        
    def click_cart_button(self):
        self.click(self.CART_BUTTON)
    
    
    # expects
    def expect_navigation_to_login_page(self):
        self.page.wait_for_url("**/login")
        
    def expect_navigation_to_products_page(self):
        self.page.wait_for_url("**/products")
    
    def expect_navigation_to_cart_page(self):
        self.page.wait_for_url("**/view_cart")