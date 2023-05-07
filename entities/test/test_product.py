import unittest
from entities.product import Product

class TestProduct(unittest.TestCase):
    
    def setUp(self):
        self.name = "iPone"
        self.price = 500.00

        self.smartphone = Product(self.name, self.price)


    def test_product_object(self):
        name = "Apple"
        price = 1.70

        product = Product(name, price)

        #assert product.name = name
        #assert product.price = price, "El precio debe ser igual al precio de la producto"

        self.assertEqual(product.name, name)
        self.assertEqual(product.price, price, "El precio debe ser igual al precio de la producto")

    def test_product_name(self):
        self.assertEqual(self.smartphone.name, self.name)

    def test_product_price(self):
        self.assertEqual(self.smartphone.price, self.price)
