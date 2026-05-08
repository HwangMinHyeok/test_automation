from pytest_bdd import given, when, then
from pages.products_page import ProductsPage

# Scenario: 카트에 상품을 추가 가능
@given("사용자가 Products 페이지에 있다")
def given_products_page():
    pass

@when("상품에 마우스를 올린다")
def hover_product(products_page):
    ProductsPage(products_page).product(0).hover()

@then("상품을 카트에 추가할 수 있다")
def add_to_cart(products_page):
    ProductsPage(products_page).product(0).expect_add_to_cart_visible()
   
@when("Add To Cart 버튼을 클릭한다")
def click_add_to_cart(products_page):
    ProductsPage(products_page).product(0).add_to_cart()
    
@then("상품 추가 확인 modal이 표시된다")
def expect_cart_modal_visible(products_page):
    ProductsPage(products_page).expect_cart_modal_visible()