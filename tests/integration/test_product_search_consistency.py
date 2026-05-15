from tests.api.clients.product_api_client import ProductApiClient
from pages.products_page import ProductsPage

def test_ui_api_product_search_consistency(products_page, keyword : str = "top"):
    # UI
    ProductsPage(products_page).search_product(keyword)
    ui_ids = ProductsPage(products_page).get_product_ids()
    
    
    # API
    client = ProductApiClient()
    response = client.search_product(keyword)
    searched_products = response.get("products", [])
    api_ids = [product["id"] for product in searched_products]

    
    # comparison
    for uid in ui_ids:
        assert uid in api_ids