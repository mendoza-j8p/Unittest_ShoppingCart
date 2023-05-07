import unittest
from entities.product import Product, ProductDiscountError
from entities.shopping_cart import ShoppingCart


def is_available_to_skip():
    return True

def is_conected():
    return False

class TestShoppingCart(unittest.TestCase):

    # Se ejecuta antes de cada clase, es decir antes de TODAS las pruebas
    @classmethod
    def setUpClass(cls):
        pass
    
    # Se ejecuta despues de cada clase, es decir despues de TODAS las pruebas
    @classmethod
    def tearDownClass(cls):
        pass


    # Se ejecuta antes de cada prueba
    def setUp(self):
        self.name = "iPhone"
        self.price = 500.00

        self.smartphone = Product(self.name, self.price)

        self.shopping_cart_1 = ShoppingCart()

        self.shopping_cart_2 = ShoppingCart()
        self.shopping_cart_2.add_product(self.smartphone)

    # Se ejecuta despues de cada prueba
    def tearDown(self):
        pass

    def test_shopping_cart_empty(self):
        self.assertTrue(self.shopping_cart_1.empty(), "La cesta debe estar vacia")

    def test_shopping_cart_has_product(self):
        self.assertTrue(self.shopping_cart_2.has_product())
        self.assertFalse(self.shopping_cart_2.empty())

    def test_product_in_shopping_cart(self):
        product = Product("Nuevo producto", 10.00)
        self.shopping_cart_2.add_product(product)

        self.assertIn(product, self.shopping_cart_2.products)
        self.assertIn(self.smartphone, self.shopping_cart_2.products)

    def test_product_not_in_shopping_cart(self):
        self.shopping_cart_2.remove_product(self.smartphone)
        self.assertNotIn(self.smartphone, self.shopping_cart_2.products)

    def test_discount_error(self):
        with self.assertRaises(ProductDiscountError):
            Product(name="Example", price=10.00, discount=11.00)

    def test_total_shopping_cart(self):
        self.shopping_cart_1.add_product(Product(name="Libro", price= 15.00))
        self.shopping_cart_1.add_product(Product(name="Camara", price= 700.00, discount=70.00))

        self.assertGreater(self.shopping_cart_1.total, 0)
        self.assertLess(self.shopping_cart_1.total, 1000.00)
        self.assertEqual(self.shopping_cart_1.total, 645.00)

    def test_total_empty_shopping_cart(self):
        self.assertEqual(self.shopping_cart_1.total, 0.00)

    



    # skip -> La prueba no se ejecuta
    @unittest.skip("La prueba no se ejecuta")
    def test_skip_example(self):
        self.assertEqual(1, 1)

    # skipIf -> Evalua sobre Verdadero
    @unittest.skipIf(is_available_to_skip(), "No se cuenta con todos los requerimientos")
    def test_skip_example_two(self):
        pass

    # skipUnless -> Evalua sobre Falso (a menos que)
    @unittest.skipUnless(is_conected(), "No se cuenta con todos los requerimientos")
    def test_skip_example_three(self):
        pass


    def test_code_product(self):
        self.assertRegex(self.smartphone.code, self.smartphone.name)

if __name__ == "__main__":
    unittest.main()




