import json
import unittest

from api.main import app


class TestMedizinfuchsAPI(unittest.TestCase):
    def setUp(self) -> None:
        self.client = app.test_client()

    def test_get_products(self):
        resp = self.client.get('/products')
        data = json.loads(resp.get_data())
        self.assertIsNotNone(data)
        self.assertEqual(resp.status_code, 200)
    
    def test_scrap_products(self):
        resp = self.client.get('/products/scrape')
        data = json.loads(resp.get_data())
        self.assertIsNotNone(data)
        self.assertEqual(resp.status_code, 200)

    def test_get_product(self):
        resp = self.client.get('/products/sildenafil')
        data = json.loads(resp.get_data())
        self.assertIsNotNone(data)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(data[0]['product'], 'sildenafil')

    def test_scrap_product(self):
        resp = self.client.get('/products/sildenafil/scrape')
        data = json.loads(resp.get_data())
        self.assertIsNotNone(data)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(data[0]['product'], 'sildenafil')
