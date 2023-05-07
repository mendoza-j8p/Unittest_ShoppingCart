import unittest
from entities.product import Product, ProductDiscountError
from entities.shopping_cart import ShoppingCart


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

        # Creamos una instancia de la clase Product con el nombre y precio dados
        self.smartphone = Product(self.name, self.price)

        # Creamos una instancia de la clase ShoppingCart vacía
        self.shopping_cart_1 = ShoppingCart()

        # Creamos otra instancia de la clase ShoppingCart y le añadimos el producto creado
        self.shopping_cart_2 = ShoppingCart()
        self.shopping_cart_2.add_product(self.smartphone)

    # Se ejecuta despues de cada prueba
    def tearDown(self):
        pass

    def test_product_object(self):
        name = "Apple"
        price = 1.70

        # Creamos una nueva instancia de la clase Product con el nombre y precio dados
        product = Product(name, price)

        # Verificamos que el nombre y precio del producto creado sean iguales a los especificados
        self.assertEqual(product.name, name)
        self.assertEqual(product.price, price, "El precio debe ser igual al precio de la producto")

    def test_product_name(self):
        # Verificamos que el nombre del producto creado anteriormente sea igual al especificado
        self.assertEqual(self.smartphone.name, self.name)

    def test_product_price(self):
        # Verificamos que el precio del producto creado anteriormente sea igual al especificado
        self.assertEqual(self.smartphone.price, self.price)

    def test_shopping_cart_empty(self):
        # Verificamos que la instancia de ShoppingCart creada anteriormente esté vacía
        self.assertTrue(self.shopping_cart_1.empty(), "La cesta debe estar vacia")

    def test_shopping_cart_has_product(self):
        # Verificamos que la instancia de ShoppingCart creada anteriormente contenga un producto
        self.assertTrue(self.shopping_cart_2.has_product())

        # Verificamos que la instancia de ShoppingCart creada anteriormente no esté vacía
        self.assertFalse(self.shopping_cart_2.empty())

    def test_product_in_shopping_cart(self):
        # Creamos una nueva instancia de la clase Product
        product = Product("Nuevo producto", 10.00)

        # Añadimos el nuevo producto a la instancia de ShoppingCart creada anteriormente
        self.shopping_cart_2.add_product(product)

        # Verificamos que el nuevo producto y el producto anteriormente creado estén en la instancia de ShoppingCart
        self.assertIn(product, self.shopping_cart_2.products)
        self.assertIn(self.smartphone, self.shopping_cart_2.products)

    def test_product_not_in_shopping_cart(self):
        # Removemos el producto creado anteriormente de la instancia de ShoppingCart
        self.shopping_cart_2.remove_product(self.smartphone)

        # Verificamos que el producto anteriormente creado ya no está en la instancia de ShoppingCart
        self.assertNotIn(self.smartphone, self.shopping_cart_2.products)

    def test_discount_error(self):
        # Utiliza el método "assertRaises" para verificar que al intentar crear un objeto Product con un descuento mayor que el precio,
        # se levanta un error de tipo "ProductDiscountError".
        with self.assertRaises(ProductDiscountError):
            Product(name="Example", price=10.00, discount=11.00)




    def test_total_shopping_cart(self):
        # Verificamos el cálculo del total de la compra en el carrito de compras.
        # Agrega dos productos, uno con descuento y otro sin descuento.
        self.shopping_cart_1.add_product(Product(name="Libro", price= 15.00))
        self.shopping_cart_1.add_product(Product(name="Camara", price= 700.00, discount=70.00))

        # Verificamos si el total está por encima de cero, por debajo de 1000.00 y 
        # es igual a la suma de los precios de los productos con el descuento aplicado.
        self.assertGreater(self.shopping_cart_1.total, 0)
        self.assertLess(self.shopping_cart_1.total, 1000.00)
        self.assertEqual(self.shopping_cart_1.total, 645.00)

    def test_total_empty_shopping_cart(self):
        # Verificamos si el total de un carrito de compras vacío es cero.
        self.assertEqual(self.shopping_cart_1.total, 0.00)



if __name__ == "__main__":
    # Ejecutamos las pruebas
    unittest.main()




# TODO: actualizar el en resumen
'''
En resumen, este código es un conjunto de pruebas unitarias para la clase ShoppingCart que utiliza la librería unittest.
Las pruebas verifican la funcionalidad de métodos como add_product(), empty(), has_product(), remove_product() y otras en diferentes casos de uso.
Además, se utiliza la clase Product para crear objetos de prueba.'''