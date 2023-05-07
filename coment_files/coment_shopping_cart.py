# Importamos la clase Product desde el módulo product
from entities.product import Product

# Definimos la clase ShoppingCart
class ShoppingCart:
    
    # Definimos el método constructor
    def __init__(self) -> None:
        # Inicializamos la lista de productos como vacía
        self.__products: list[Product] = []
    
    # Definimos el método getter para obtener la lista de productos
    @property
    def products(self) -> list[Product]:
        # Devolvemos una copia de la lista de productos para evitar modificar la original
        return self.__products.copy()
    
    # Definimos el método getter para obtener el total de la cesta de la compra
    @property
    def total(self) -> float:
        # Calculamos el total restando los descuentos de los precios de los productos y sumándolos todos
        return sum( [(product.price - product.discount) for product in self.__products ])
       
    
    # Definimos el método para añadir un producto a la lista
    def add_product(self, product: Product) -> None:
        # Añadimos el producto a la lista de productos
        self.__products.append(product)

    # Definimos el método para comprobar si la lista de productos está vacía
    def empty(self) -> bool:
        # Devolvemos True si la lista de productos está vacía, False en caso contrario
        return len(self.__products) == 0
    
    # Definimos el método para comprobar si la lista de productos tiene algún producto
    def has_product(self):
        # Devolvemos True si la lista de productos no está vacía, False en caso contrario
        return not self.empty()
    
    # Definimos el método para eliminar un producto de la lista
    def remove_product(self, product: Product) -> None:
        # Eliminamos el producto de la lista de productos
        self.__products.remove(product)



# TODO: actualizar el en resumen
''' 
En resumen, este código define la clase ShoppingCart que representa una lista de productos de compra. 
La clase tiene métodos para añadir y eliminar productos, así como para comprobar si la lista de productos está vacía o tiene algún producto. 
Además, la clase tiene un método getter para obtener la lista de productos, pero devuelve una copia para evitar modificar la lista original.'''