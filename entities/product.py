class ProductDiscountError(Exception):
    pass


class Product:

    def __init__(self, name: str, price: float, discount: float = 0.0) -> None:
        self.name = name
        self.price = price

        if discount > price:
            raise ProductDiscountError(f"El descuento no puede ser mayor que el precio: {price}")
        
        # assert tambien podemos usarlo para el mismo fin

        self.discount = discount
    
    @property
    def code(self):
        return f"{self.name}"