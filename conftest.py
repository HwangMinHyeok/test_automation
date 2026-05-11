import pytest
from playwright.sync_api import sync_playwright
import time


BASE_URL = "https://automationexercise.com"
MAX_RETRIES = 3


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

def safe_goto(page, url):
    for _ in range(MAX_RETRIES):
        page.goto(url)
        
        if not page.locator("text=queue full").is_visible():
            return
        
        time.sleep(3)
    
    raise Exception("서버 과부하로 인한 일시적 페이지 접근 실패")
  
  
# URL별 페이지 fixture
@pytest.fixture
def home_page(page):
    safe_goto(page, BASE_URL)
    return page

@pytest.fixture
def login_page(page):
    safe_goto(page, BASE_URL + "/login")
    return page

@pytest.fixture
def products_page(page):
    safe_goto(page, BASE_URL + "/products")
    return page

@pytest.fixture
def view_cart_page(page):
    safe_goto(page, BASE_URL + "/view_cart")
    return page


# shared fixture
@pytest.fixture
def shared_data():
    return {}