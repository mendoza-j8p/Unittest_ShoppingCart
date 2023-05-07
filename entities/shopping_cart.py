from entities.product import Product

class ShoppingCart:

    def __init__(self) -> None:
        # self.__products = list()
        self.__products: list[Product] = []

    @property
    def products(self) -> list[Product]:
        return self.__products.copy()
    
    @property
    def total(self) -> float:
        return sum( [(product.price - product.discount) for product in self.__products ])
        
    
    def add_product(self, product: Product) -> None:
        self.__products.append(product)

    def empty(self) -> bool:
        return len(self.__products) == 0
    
    def has_product(self):
        return not self.empty()
    
    def remove_product(self, product: Product) -> None:
        self.__products.remove(product)

    
