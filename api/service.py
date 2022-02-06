from app.scrapper import MedizinfuchsScraper

class ProductService:

    def __init__(self):
        self.scrapper = MedizinfuchsScraper()

    def get_products(self) -> str:
        all_products = self.scrapper.get_all_data()
        return all_products

    def scrap_products(self):
        self.scrapper.init_data()
        return self.scrapper.get_all_data()

    def get_product(self, product: str):
        return self.scrapper.get_product_data(product)

    def scrap_product(self, product: str):
        self.scrapper.init_product_data(product)
        return self.scrapper.get_product_data(product)
