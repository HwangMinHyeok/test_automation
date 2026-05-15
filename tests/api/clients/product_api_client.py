import requests


class ProductApiError(Exception):
    pass


class ProductApiClient:
    BASE_URL = "https://automationexercise.com/api"
    
    def search_product(self, search_keyword : str):
        url = f"{self.BASE_URL}/searchProduct"
        payload = { "search_product": search_keyword }
        
        try:
            response = requests.post(url, data=payload, timeout=10)
        except requests.RequestException as error:
            raise ProductApiError("Product API request failed") from error
        
        try:
            return response.json()
        except ValueError as error:
            raise ProductApiError("Product API request returned invalid JSON") from error