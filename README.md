# Proyecto de práctica con unittest

Este proyecto está creado con el fin de practicar el uso de la librería unittest para realizar pruebas unitarias en un proyecto de Python. Se trata de un sistema simple de carrito de compras, donde se pueden agregar y remover productos, calcular el total de la compra y verificar si el carrito está vacío.

## Estructura del proyecto

El proyecto cuenta con tres archivos principales:

* **product.py**: Contiene la definición de la clase **Product**, que representa un producto con su nombre, precio y descuento (opcional). También define una excepción ProductDiscountError que se lanza si se intenta aplicar un descuento mayor al precio del producto.

* **shopping_cart.py**: Define la clase **ShoppingCart**, que representa el carrito de compras. Permite agregar y remover productos, verificar si está vacío y calcular el total de la compra.

* **main.py**: Contiene la importación de las clases **Product** y **ShoppingCart**.

Además, tiene una carpeta llamada **comment_files** , contiene tres archivos con nombres que comienzan por "comment_" que son copias de los anteriores con comentarios en línea.

## Uso del proyecto

Para utilizar el proyecto, simplemente importa las clases **Product** y **ShoppingCart** desde el archivo **main.py**.

## Ejecución de pruebas

El archivo **tests.py** contiene las pruebas unitarias para las clases **Product** y **ShoppingCart**. Estas pruebas verifican que las clases funcionen correctamente en diferentes escenarios.

Para ejecutar las pruebas, asegúrate de tener la librería unittest instalada en tu sistema y ejecuta el siguiente comando en la terminal dentro del directorio del proyecto:

## Ejecutar pruebas desde terminal

A traves de las rutas podemos ser muy especificos sobre las pruebas o prueba que vamos a ejecutar.
Basta con colocar el directorio, la ruta o rutas donde se encuenta la(s) prueba(s) utilizando punto.
De esta manera:

**Para ejecutar todas las pruebas dento de la ruta donde se encuentra la termina (>>> pwd):**

```bash
python -m unittest discover
```

**Para ejecutar los todos los modulos de un archivo:**

```bash
python -m unittest -v entities.test.test_shopping_cart
```

**Para ejecutar un modulo concreto de un archivo concreto:**

```bash
python -m unittest -v entities.test.test_shopping_cart.TestShoppingCart
```

**Para ejecutar explicitamente una prueba de una clase podemos ejecutar:**

```bash
python -m unittest -v entities.test.test_shopping_cart.TestShoppingCart.test_discount_error
```

## Contribución

Si deseas contribuir con el proyecto, no dudes en hacer un pull request o abrir una issue para discutir los cambios propuestos.
