import json
from datetime import datetime
from sqlite3 import Error
from typing import List, Any

import pandas as pd
import requests
from bs4 import BeautifulSoup, ResultSet
from constants import (
    URL,
    PRODUCT_LIST,
    PRODUCT_CLASS,
    PAGINATION_CLASS, DATATYPES,
)
from db import (
    get_all_records,
    get_product_records, store_records,
)
from extractor import ProductExtractor


class MedizinfuchsScraper:
    table: str
    db_name: str
    prod_name: str

    def __init__(self, prod_name: str = "") -> None:
        self.prod_name = prod_name
        self.db = "products_database"
        self.table = "products"

    def to_pandas(self, p_list: List) -> pd.DataFrame:
        pd.set_option("display.max_columns", None)
        df = pd.DataFrame(p_list)

        return df

    def to_sqlite(self, df: pd.DataFrame) -> None:
        store_records(self.db, self.table, df)

    def init_data(self) -> None:
        for product in PRODUCT_LIST:
            self.init_product_data(product)

    def init_product_data(self, product: str) -> None:
        prod_info = self._get_product_data(product)
        df = self.to_pandas(prod_info)
        self.to_sqlite(df)

    def get_all_data(self) -> json:
        try:
            rows = get_all_records(self.db, self.table)
            return self._transform_table_data_to_json(rows)

        except Error as e:
            print(e)

    def get_product_data(self, product: str) -> json:
        try:
            rows = get_product_records(self.db, self.table, product)
            return self._transform_table_data_to_json(rows)

        except Error as e:
            print(e)

    def _get_page_content(self, search_product: str, page_num: int = 1) -> BeautifulSoup:
        search_url = f"{URL}{search_product}.html/offset/{page_num}"
        page = requests.get(search_url)
        soup = BeautifulSoup(page.content, "html.parser")
        return soup

    def _parse_all_pages_for_product(self, search_product: str) -> ResultSet:
        """
        extracts content from all pages for a given product.
        """
        # extract first page and pagination on it.
        soup = self._get_page_content(search_product)
        products = soup.find_all(attrs={"class": PRODUCT_CLASS})

        pagination_div = soup.find("nav", attrs={"class": PAGINATION_CLASS})

        # if there"s no pagination; return the products from first page.
        if not pagination_div:
            return products

        # total pages.
        page_count = len(pagination_div.find_all("li")) + 1

        # get content from next pages.
        # page 1 is already extracted so start form 2.
        for page_num in range(2, page_count):
            soup = self._get_page_content(search_product, page_num)
            products.extend(soup.find_all(attrs={"class": PRODUCT_CLASS}))

        return products

    def _get_product_data(self, search_product: str) -> List:
        products = self._parse_all_pages_for_product(search_product)
        product_position = 0
        prod_info = []
        for product in products:
            extractor = ProductExtractor(product)
            cleaned_data = extractor.extract_product_data()

            cleaned_data.update(
                {
                    "position": product_position,
                    "product": search_product,
                    "time_stamp": datetime.now()
                }
            )
            prod_info.append(cleaned_data)
            product_position += 1

        return prod_info

    def _transform_table_data_to_json(self, rows: List[Any]) -> json:
        if not rows:
            return []

        df = pd.DataFrame.from_records(rows, columns=DATATYPES.keys())

        return json.loads(df.to_json(orient='records'))
