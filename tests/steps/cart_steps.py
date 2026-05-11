from pytest_bdd import given, when, then
from pages.products_page import ProductsPage
from pages.view_cart_page import ViewCartPage

# Scenario: 단일 상품 카트 추가 확인
@given("사용자가 Products 페이지에 있다")
def given_products_page():
    pass

@when("add to cart 버튼을 눌러 상품을 카트에 추가한다")
def add_product_to_cart(products_page, shared_data):
    # 테스트의 안정성을 위해 항상 첫 번째 상품을 추가하도록
    index = 0
    
    # 추가한 상품 정보를 shared_data에 저장
    shared_data["product"] = ProductsPage(products_page).product(index).get_product_info()
    
    # 상품을 카트에 추가하고 View Cart 버튼 클릭하여 카트 페이지로 이동
    ProductsPage(products_page).add_product_to_cart(index)
    ProductsPage(products_page).CART_MODAL.click_view_cart()


@then("카트에 해당 상품이 들어있다")
def expect_product_in_cart(products_page, shared_data):
    product_info = shared_data["product"]
    ViewCartPage(products_page).expect_product_exists(product_info)
