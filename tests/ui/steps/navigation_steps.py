from pytest_bdd import given, when, then
from pages.home_page import HomePage

@given("사용자가 홈페이지에 있다")
def given_home_page():
    pass

@when("로그인 버튼을 클릭한다")
def click_login_button(home_page):
    HomePage(home_page).click_signup_login_button()
    
@then("로그인 페이지로 이동한다")
def expect_login_page(home_page):
    HomePage(home_page).expect_navigation_to_login_page()
    
@when("Products 버튼을 클릭한다")
def click_products_button(home_page):
    HomePage(home_page).click_products_button()
    
@then("Products 페이지로 이동한다")
def expect_products_page(home_page):
    HomePage(home_page).expect_navigation_to_products_page()
    
@when("Cart 버튼을 클릭한다")
def click_cart_button(home_page):
    HomePage(home_page).click_cart_button()

@then("Cart 페이지로 이동한다")
def expect_cart_page(home_page):
    HomePage(home_page).expect_navigation_to_cart_page()