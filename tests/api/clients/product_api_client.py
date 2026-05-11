import requests

class ProductApiClient:
    BASE_URL = "https://automationexercise.com/api"
    
    def search_product(self, search_keyword : str):
        url = f"{self.BASE_URL}/searchProduct"
        payload = { "search_product": search_keyword }
        
        response = requests.post(url, data=payload)
        return response.json()