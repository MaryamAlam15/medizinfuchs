import json
import re
from typing import Tuple

from constants import (
    PRODUCT_NAME_CLASS,
    MANUFACTURER_CLASS,
    PRODUCT_ID_CLASS,
    PRICE_VALUE_CLASS,
    PRICE_INFO_DIV,
    PACKAGE_CLASS,
    PACKAGE_INFO_REGEX,
    PRICE_INFO_REGEX,
    DOSAGE_FROM_PRODUCT_REGEX,
    DOSAGE_FROM_PACKAGE_INFO_REGEX,
    LOW_PRICE_REGEX,
    PRODUCT_ID_REGEX,
)


class ProductExtractor:

    def __init__(self, product):
        self.product = product

    def extract_product_data(self) -> json:
        product_name = self._get_child_element_by_class('div', PRODUCT_NAME_CLASS)
        manufacturer = self._get_child_element_by_class('span', MANUFACTURER_CLASS)
        product_detail_url = self.product.find("div", attrs={"class": PRODUCT_ID_CLASS}).find("a")["href"]
        product_id = re.search(PRODUCT_ID_REGEX, product_detail_url).groups()[0]
        low_price = self._get_cleaned_low_price()
        price_per_unit = self._get_cleaned_price_per_unit()
        dosage, dosage_unit = self._get_cleaned_dosage_info()
        num_of_pills, quantity_unit = self._get_cleaned_quantity_info()

        return {
            "id": product_id,
            "name": product_name,
            "manufacturer": manufacturer,
            "low_price": float(low_price),
            "number_of_pills": num_of_pills,
            "quantity_unit": quantity_unit,
            "price_per_unit": price_per_unit,
            "dosage": dosage,
            "dosage_unit": dosage_unit,

        }

    def _get_child_element_by_class(
            self,
            child_tag: str,
            child_class: str
    ) -> str:
        return self.product.find(child_tag, attrs={"class": child_class}).get_text(strip=True)

    def _get_cleaned_price(self, regex: str, str_to_find: str) -> str:
        return re.search(regex, str_to_find).groups()[0].replace(",", ".").strip()

    def _get_cleaned_dosage_info(self) -> Tuple[str, str]:
        dosage = ''
        dosage_unit = ''

        package_info = self._get_child_element_by_class('span', PACKAGE_CLASS)
        product_name = self._get_child_element_by_class('div', PRODUCT_NAME_CLASS)

        dosage_info = re.search(DOSAGE_FROM_PRODUCT_REGEX, product_name.lower())
        if dosage_info:
            dosage_info = dosage_info.groups()
            dosage = dosage_info[0]
            dosage_unit = dosage_info[2]

        else:
            dosage_info = re.search(DOSAGE_FROM_PACKAGE_INFO_REGEX, package_info.lower())
            if dosage_info:
                dosage_info = dosage_info.groups()
                dosage = dosage_info[3]
                dosage_unit = dosage_info[5]

        dosage_unit = re.sub('(milliliters|milliliter)', 'ml', dosage_unit.lower())
        return dosage, dosage_unit

    def _get_cleaned_quantity_info(self) -> Tuple[str, str]:
        package_info = self._get_child_element_by_class('span', PACKAGE_CLASS)
        info = re.search(PACKAGE_INFO_REGEX, package_info.lower()).groups()
        num_of_pills = info[2] or info[4]
        quantity_unit = re.sub('(milliliters|milliliter)', 'ml', info[6].lower())
        return num_of_pills, quantity_unit

    def _get_cleaned_price_per_unit(self) -> str:
        all_spans = self.product.select_one(PRICE_INFO_DIV).find_all("span")
        price_per_unit_info = all_spans[len(all_spans) - 1].get_text(strip=True)
        price_per_unit = self._get_cleaned_price(PRICE_INFO_REGEX, price_per_unit_info)
        return price_per_unit

    def _get_cleaned_low_price(self) -> str:
        price_info = self._get_child_element_by_class('span', PRICE_VALUE_CLASS)
        low_price = self._get_cleaned_price(LOW_PRICE_REGEX, price_info)
        return low_price
