from pytest_bdd import given, scenarios, when, then
from pages.login_page import LoginPage

scenarios("../features/login.feature")

@given("사용자가 로그인 페이지에 있다")
def given_login_page():
    pass

@when("올바른 계정을 입력하고 로그인한다")
def valid_login(login_page):
    page = LoginPage(login_page)
    page.login("samplemail123@gmail.com", "password")

@then("로그인에 성공한다")
def login_success(login_page):
    LoginPage(login_page).expect_login_success()
    
@when("올바르지 않은 계정을 입력한다")
def invalid_login(login_page):
    page = LoginPage(login_page)
    page.login("invalid@gmail.com", "wrongpassword")
    
@then("로그인에 실패한다")
def login_failure(login_page):
    LoginPage(login_page).expect_login_failure()