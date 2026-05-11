from pytest_bdd import given, when, then
from pages.products_page import ProductsPage


# Scenario: 카트에 상품을 추가 가능
@given("사용자가 Products 페이지에 있다")
def given_products_page():
    pass

@when("상품에 마우스를 hover하고 add to cart 버튼을 클릭한다")
def hover_and_click_add_to_cart(products_page):
    ProductsPage(products_page).add_product_to_cart()
    
@then("상품 추가 확인 modal이 표시된다")
def expect_cart_modal_visible(products_page):
    ProductsPage(products_page).CART_MODAL.expect_cart_modal_opened()
    
    
# Scenario: 상품 추가 확인 modal - Continue Shopping 버튼 동작
@given("상품 추가 확인 modal - Continue Shopping 버튼 동작")
def given_cart_modal_visible(products_page):
    products_page = ProductsPage(products_page)
    products_page.add_product_to_cart()
    products_page.CART_MODAL.expect_cart_modal_opened()
    
@when("Continue Shopping 버튼을 클릭한다")
def click_continue_shopping_button(products_page):
    ProductsPage(products_page).CART_MODAL.click_continue_shopping()

@then("상품 추가 확인 modal이 닫힌다")
def expect_cart_modal_closed(products_page):
    ProductsPage(products_page).CART_MODAL.expect_cart_modal_closed()


# Scenario: 상품 추가 확인 modal - View Cart 버튼 동작
@given("상품 추가 확인 modal이 표시되어 있다")
def given_cart_modal_visible(products_page):
    products_page = ProductsPage(products_page)
    products_page.add_product_to_cart()
    products_page.CART_MODAL.expect_cart_modal_opened()
    
@when("View Cart 버튼을 클릭한다")
def click_view_cart_button(products_page):
    ProductsPage(products_page).CART_MODAL.click_view_cart()
    
@then("View Cart 페이지로 이동한다")
def expect_nav_to_view_cart_page(products_page):
    ProductsPage(products_page).CART_MODAL.expect_nav_to_view_cart_page()