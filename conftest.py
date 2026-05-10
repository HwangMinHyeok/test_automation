import pytest
from playwright.sync_api import sync_playwright

BASE_URL = "https://automationexercise.com"

# 베이스 페이지 fixture
@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        block_ads(page)

        yield page
        
        context.close()
        browser.close()
        
def block_ads(page):
    page.route("**/*googlesyndication.com/**", lambda route: route.abort())
    page.route("**/*doubleclick.net/**", lambda route: route.abort())
    page.route("**/*googleadservices.com/**", lambda route: route.abort())        

  
# URL별 페이지 fixture
@pytest.fixture
def home_page(page):
    page.goto(BASE_URL)
    return page

@pytest.fixture
def login_page(page):
    page.goto(BASE_URL + "/login")
    return page

@pytest.fixture
def products_page(page):
    page.goto(BASE_URL + "/products")
    return page

@pytest.fixture
def view_cart_page(page):
    page.goto(BASE_URL + "/view_cart")
    return page


# shared fixture
@pytest.fixture
def shared_data():
    return {}