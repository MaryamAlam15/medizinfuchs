import json

from flask import Flask

from .service import ProductService

app = Flask(__name__)


@app.route('/products', methods=['GET'])
def get_products() -> json:
    return json.dumps(ProductService().get_products())


@app.route('/products/scrap', methods=['GET'])
def scrap_products() -> json:
    return json.dumps(ProductService().scrap_products())


@app.route('/products/<string:product>', methods=['GET'])
def get_product(product: str) -> json:
    return json.dumps(ProductService().get_product(product=product))


@app.route('/products/<string:product>/scrap', methods=['GET'])
def scrap_product(product: str) -> json:
    return json.dumps(ProductService().scrap_product(product=product))
