import pytest
from playwright.sync_api import sync_playwright
import time
import re
from pathlib import Path

BASE_URL = "https://automationexercise.com"
MAX_RETRIES = 3

ARTIFACTS_DIR = Path("artifacts")
SCREENSHOTS_DIR = ARTIFACTS_DIR / "screenshots"
TRACES_DIR = ARTIFACTS_DIR / "traces"


def safe_artifact_name(nodeid):
    return re.sub(r"[^a-zA-Z0-9_.ㄱ-ㅎㅏ-ㅣ가-힣-]+", "_", nodeid)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    setattr(item, f"rep_{report.when}", report)


# 베이스 페이지 fixture
@pytest.fixture
def page(request):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        
        context.tracing.start(screenshots=True, snapshots=True, sources=True)
        page = context.new_page()

        block_ads(page)

        yield page
        
        # 테스트 실패 시 해당 자료 저장
        test_failed = getattr(request.node, "rep_call", None)
        test_failed = test_failed is not None and test_failed.failed
        
        if test_failed:
            SCREENSHOTS_DIR.mkdir(parents=True, exist_ok=True)
            TRACES_DIR.mkdir(parents=True, exist_ok=True)

            artifact_name = safe_artifact_name(request.node.nodeid)

            page.screenshot(
                path=SCREENSHOTS_DIR / f"{artifact_name}.png",
                full_page=True,
            )

            context.tracing.stop(
                path=TRACES_DIR / f"{artifact_name}.zip",
            )
        else:
            context.tracing.stop()
        
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