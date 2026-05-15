from pytest_bdd import given, when, then
from pages.products_page import ProductsPage
from pages.view_cart_page import ViewCartPage

# Scenario: 단일 상품 - 카트에 추가 확인
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
    ViewCartPage(products_page).expect_product_exists(shared_data["product"])
    

# Scenario: 단일 상품 - 카트에서 삭제 확인
@given("카트에 상품이 담겨있다")
def given_product_in_cart(products_page, shared_data):
    index = 0
    
    ProductsPage(products_page).add_product_to_cart(index)
    shared_data["product"] = ProductsPage(products_page).product(index).get_product_info()

    ProductsPage(products_page).CART_MODAL.click_view_cart()
    
@when("삭제 버튼을 클릭한다")
def delete_product_from_cart(products_page, shared_data):
    ViewCartPage(products_page).click_delete_button(shared_data["product"])
    
@then("해당 상품이 카트에서 삭제된다")
def expect_product_deleted_from_cart(products_page, shared_data):
    ViewCartPage(products_page).expect_product_not_exists(shared_data["product"])


# Scenario: 여러 상품 - 카트에 추가 확인
@given("사용자가 Products 페이지에 있다")
def given_products_page():
    pass

@when("add to cart 버튼을 눌러 여러 상품을 카트에 추가한다")
def add_multiple_products_to_cart(products_page, shared_data):
    # 테스트의 안정성을 위해 항상 첫 번째, 두 번째, 열 번째 상품을 추가하도록
    indices = [0, 1, 9]
    
    shared_data["products"] = []
    
    for index in indices[:-1]:
        # 추가한 상품 정보를 shared_data에 저장 
        shared_data["products"].append(ProductsPage(products_page).product(index).get_product_info())
        
        # 상품을 카트에 추가하고 Continue Shopping 버튼 클릭하여 계속 쇼핑
        ProductsPage(products_page).add_product_to_cart(index)
        ProductsPage(products_page).CART_MODAL.click_continue_shopping()
    
    # 상품을 카트에 추가하고 View Cart 버튼 클릭하여 카트 페이지로 이동
    shared_data["products"].append(ProductsPage(products_page).product(indices[-1]).get_product_info())
    ProductsPage(products_page).add_product_to_cart(indices[-1])    
    ProductsPage(products_page).CART_MODAL.click_view_cart()


@then("카트에 해당 상품들이 모두 들어있다")
def expect_multiple_products_in_cart(products_page, shared_data):
    for product_info in shared_data["products"]:
        ViewCartPage(products_page).expect_product_exists(product_info)