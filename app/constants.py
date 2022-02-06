URL = "https://www.medizinfuchs.de/"

PRODUCT_LIST = ['sildenafil', 'tadalafil', 'viagra', 'cialis', 'finasterid']


DATATYPES = {
    'index': 'text',
    'id': 'text',
    'name': 'text',
    'manufacturer': 'text',
    'low_price': 'float',
    'number_of_pills': 'int',
    'quantity_unit': 'text',
    'price_per_unit': 'text',
    'dosage': 'float',
    'dosage_unit': 'text',
    'position': 'int',
    'product': 'float',
    'time_stamp': 'timestamp'
}
# SELECTORS
PRODUCT_CLASS = "produkt"
PRODUCT_NAME_CLASS = "produktname"
MANUFACTURER_CLASS = "manufacturer"
PRODUCT_ID_CLASS = "produktbild"
PRICE_VALUE_CLASS = "priceValue"
PACKAGE_CLASS = "package"
PRICE_INFO_DIV = "div.produktbuttons"
PAGINATION_CLASS = "Pagination"

# REGEX
PACKAGE_INFO_REGEX = "(((\d+)\s+\×\s+)*(((\d+\.)*\d+)\s+(milliliter(s)*|ml|packung|stück)))"
PRICE_INFO_REGEX = "(\d+(\,)?\d+)\s{1}€ \/ (\d+)\s{1}(Stk|ml|Pckg)"
DOSAGE_FROM_PRODUCT_REGEX = "((\d+\.)?\d+)\s*(mg|milliliter(s)*)"
DOSAGE_FROM_PACKAGE_INFO_REGEX = "(((\d+)\s+\×\s+)*((\d+\.)*\d+)\s+(milliliter(s)*|ml))"
LOW_PRICE_REGEX = "(\d+,\d+)"
PRODUCT_ID_REGEX = "(\d+)\.html$"
