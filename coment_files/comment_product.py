# Definición de la clase ProductDiscountError que hereda de la clase Exception
''' La razón de esta clase es que queremos lanzar una excepción específica en caso de que se produzca un error al aplicar un descuento al precio de un producto.
Esta clase nos permitirá identificar claramente cuándo ocurre este tipo de error en el código y manejarlo adecuadamente'''
class ProductDiscountError(Exception):
    pass 

# El método __init__ se llama al crear una nueva instancia de la clase Product
def __init__(self, name: str, price: float, discount: float = 0.0) -> None:
    # Se asignan los atributos "name" y "price" al objeto que se está creando
    self.name = name
    self.price = price

    # Se verifica que el valor de descuento no sea mayor al precio del producto
    if discount > price:
        # Si el descuento es mayor al precio, se lanza la excepción ProductDiscountError
        raise ProductDiscountError(f"El descuento no puede ser mayor que el precio: {price}")
    
    # Si el descuento es válido, se asigna a la propiedad "discount" del objeto que se está creando
    self.discount = discount
